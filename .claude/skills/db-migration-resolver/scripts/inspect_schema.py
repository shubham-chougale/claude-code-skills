#!/usr/bin/env python3
"""
inspect_schema.py — Connect to a database and inspect actual schema.

Usage:
    python inspect_schema.py --url <db_url> [--table <table_name>] [--check-fk <fk_json>]

Output: JSON to stdout with schema information.

Supports: PostgreSQL (psycopg2/asyncpg), MySQL (pymysql), SQLite.
Requires: sqlalchemy (install with: pip install sqlalchemy)
"""
import argparse
import json
import sys


def get_engine(db_url: str):
    try:
        from sqlalchemy import create_engine
        return create_engine(db_url)
    except ImportError:
        print(json.dumps({"error": "sqlalchemy not installed. Run: pip install sqlalchemy"}))
        sys.exit(1)
    except Exception as e:
        print(json.dumps({"error": f"Could not create engine: {e}"}))
        sys.exit(1)


def inspect_table(engine, table_name: str) -> dict:
    """Get column definitions and constraints for a specific table."""
    from sqlalchemy import inspect as sa_inspect
    inspector = sa_inspect(engine)

    result = {
        "table": table_name,
        "exists": False,
        "columns": [],
        "primary_keys": [],
        "foreign_keys": [],
        "indexes": [],
        "unique_constraints": [],
        "row_count": None,
    }

    all_tables = inspector.get_table_names()
    if table_name not in all_tables:
        return result

    result["exists"] = True
    result["columns"] = inspector.get_columns(table_name)
    result["primary_keys"] = inspector.get_pk_constraint(table_name)
    result["foreign_keys"] = inspector.get_foreign_keys(table_name)
    result["indexes"] = inspector.get_indexes(table_name)
    result["unique_constraints"] = inspector.get_unique_constraints(table_name)

    # Get row count
    try:
        with engine.connect() as conn:
            from sqlalchemy import text
            row = conn.execute(text(f"SELECT COUNT(*) FROM {table_name}")).fetchone()
            result["row_count"] = row[0] if row else 0
    except Exception:
        result["row_count"] = "unknown"

    # Serialize non-JSON-safe types
    for col in result["columns"]:
        col["type"] = str(col["type"])

    return result


def check_fk_violation(engine, child_table: str, fk_column: str,
                        parent_table: str, parent_column: str) -> dict:
    """Check for orphaned rows that would violate a FK constraint."""
    result = {
        "child_table": child_table,
        "fk_column": fk_column,
        "parent_table": parent_table,
        "parent_column": parent_column,
        "orphaned_count": 0,
        "sample_orphans": [],
        "safe_to_add_fk": True,
    }

    query = f"""
        SELECT COUNT(*) FROM {child_table}
        WHERE {fk_column} IS NOT NULL
          AND {fk_column} NOT IN (SELECT {parent_column} FROM {parent_table})
    """
    sample_query = f"""
        SELECT {fk_column} FROM {child_table}
        WHERE {fk_column} IS NOT NULL
          AND {fk_column} NOT IN (SELECT {parent_column} FROM {parent_table})
        LIMIT 5
    """

    try:
        with engine.connect() as conn:
            from sqlalchemy import text
            count_row = conn.execute(text(query)).fetchone()
            result["orphaned_count"] = count_row[0] if count_row else 0

            if result["orphaned_count"] > 0:
                result["safe_to_add_fk"] = False
                rows = conn.execute(text(sample_query)).fetchall()
                result["sample_orphans"] = [row[0] for row in rows]
    except Exception as e:
        result["error"] = str(e)

    return result


def list_tables(engine) -> dict:
    """List all tables in the database with row counts."""
    from sqlalchemy import inspect as sa_inspect
    inspector = sa_inspect(engine)
    tables = inspector.get_table_names()

    result = {"tables": []}
    with engine.connect() as conn:
        from sqlalchemy import text
        for table in tables:
            try:
                row = conn.execute(text(f"SELECT COUNT(*) FROM {table}")).fetchone()
                count = row[0] if row else 0
            except Exception:
                count = "unknown"
            result["tables"].append({"name": table, "row_count": count})

    return result


def get_applied_revisions(engine, framework: str) -> dict:
    """Read which migrations have been applied from alembic_version or django_migrations."""
    result = {"framework": framework, "applied": [], "error": None}

    try:
        with engine.connect() as conn:
            from sqlalchemy import text
            if framework == "alembic":
                rows = conn.execute(text("SELECT version_num FROM alembic_version")).fetchall()
                result["applied"] = [row[0] for row in rows]
            elif framework == "django":
                rows = conn.execute(
                    text("SELECT app, name, applied FROM django_migrations ORDER BY applied")
                ).fetchall()
                result["applied"] = [{"app": r[0], "name": r[1], "applied_at": str(r[2])} for r in rows]
    except Exception as e:
        result["error"] = str(e)

    return result


def main():
    parser = argparse.ArgumentParser(description="Inspect actual database schema")
    parser.add_argument("--url", required=True, help="Database URL (e.g. postgresql://user:pass@host/db)")
    parser.add_argument("--table", help="Inspect a specific table")
    parser.add_argument("--list-tables", action="store_true", help="List all tables with row counts")
    parser.add_argument("--check-fk", help="JSON: {child_table, fk_column, parent_table, parent_column}")
    parser.add_argument("--applied", choices=["alembic", "django"], help="Show applied migrations")
    args = parser.parse_args()

    engine = get_engine(args.url)

    output = {}

    if args.list_tables:
        output["tables"] = list_tables(engine)

    if args.table:
        output["table_schema"] = inspect_table(engine, args.table)

    if args.check_fk:
        try:
            fk_info = json.loads(args.check_fk)
            output["fk_check"] = check_fk_violation(
                engine,
                fk_info["child_table"],
                fk_info["fk_column"],
                fk_info["parent_table"],
                fk_info["parent_column"],
            )
        except (json.JSONDecodeError, KeyError) as e:
            output["error"] = f"Invalid --check-fk JSON: {e}"

    if args.applied:
        output["applied_migrations"] = get_applied_revisions(engine, args.applied)

    if not output:
        parser.print_help()
        sys.exit(1)

    print(json.dumps(output, indent=2, default=str))


if __name__ == "__main__":
    main()

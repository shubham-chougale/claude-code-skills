#!/usr/bin/env python3
"""
apply_fix.py — Apply an approved migration fix.

Usage:
    python apply_fix.py --fix <fix_json_string>

The fix JSON must come from detect_alembic.py or detect_django.py output.
This script ONLY applies fixes after explicit user approval — never call it
automatically. Always show the user what will happen before running.

Supported fix types:
  - rename_migration_file
  - update_down_revision
  - create_merge_migration (alembic)
  - create_merge_migration_django
  - stamp_revision (alembic) — requires explicit approval
  - dump_table_csv — backup data before destructive op
"""
import argparse
import csv
import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path


def rename_migration_file(fix: dict) -> dict:
    """Rename a migration file to resolve numbering conflict."""
    src = Path(fix["source_file"])
    dst = Path(fix["target_file"])

    if not src.exists():
        return {"success": False, "error": f"Source file not found: {src}"}
    if dst.exists():
        return {"success": False, "error": f"Target file already exists: {dst}"}

    shutil.move(str(src), str(dst))
    return {"success": True, "message": f"Renamed {src.name} → {dst.name}"}


def update_down_revision(fix: dict) -> dict:
    """Update down_revision in a migration file."""
    filepath = Path(fix["file"])
    old_revision = fix["old_down_revision"]
    new_revision = fix["new_down_revision"]

    if not filepath.exists():
        return {"success": False, "error": f"File not found: {filepath}"}

    source = filepath.read_text(encoding="utf-8")

    # Replace down_revision value
    pattern = rf"(down_revision\s*=\s*)['\"]?{re.escape(str(old_revision))}['\"]?"
    replacement = f"\\g<1>'{new_revision}'"
    new_source = re.sub(pattern, replacement, source, count=1)

    if new_source == source:
        return {"success": False, "error": "Could not find down_revision to replace"}

    # Backup original
    backup = filepath.with_suffix(".py.bak")
    shutil.copy2(str(filepath), str(backup))

    filepath.write_text(new_source, encoding="utf-8")
    return {
        "success": True,
        "message": f"Updated down_revision in {filepath.name}",
        "backup": str(backup),
    }


def create_merge_migration_alembic(fix: dict) -> dict:
    """Run alembic merge to create a merge migration."""
    revisions = fix["revisions"]
    merge_name = fix.get("merge_name", "merge_heads")
    alembic_dir = fix.get("alembic_dir", ".")

    cmd = ["alembic", "-c", str(Path(alembic_dir) / "alembic.ini"),
           "merge", "-m", merge_name] + revisions

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, cwd=alembic_dir)
        if result.returncode == 0:
            return {"success": True, "message": result.stdout.strip(),
                    "command": " ".join(cmd)}
        else:
            return {"success": False, "error": result.stderr.strip(),
                    "command": " ".join(cmd)}
    except FileNotFoundError:
        return {"success": False, "error": "alembic not found. Is it installed and in PATH?"}


def create_merge_migration_django(fix: dict) -> dict:
    """Run manage.py makemigrations --merge."""
    app = fix["app"]
    merge_name = fix.get("merge_name", "merge_heads")
    project_dir = fix.get("project_dir", ".")

    cmd = ["python", "manage.py", "makemigrations", "--merge",
           "--name", merge_name, app]

    try:
        result = subprocess.run(
            cmd, capture_output=True, text=True, cwd=project_dir, input="y\n"
        )
        if result.returncode == 0:
            return {"success": True, "message": result.stdout.strip(),
                    "command": " ".join(cmd)}
        else:
            return {"success": False, "error": result.stderr.strip(),
                    "command": " ".join(cmd)}
    except FileNotFoundError:
        return {"success": False, "error": "manage.py not found. Check project_dir."}


def stamp_revision_alembic(fix: dict) -> dict:
    """Run alembic stamp — marks revision as applied without running it. RISKY."""
    revision = fix["revision"]
    alembic_dir = fix.get("alembic_dir", ".")

    cmd = ["alembic", "-c", str(Path(alembic_dir) / "alembic.ini"), "stamp", revision]

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, cwd=alembic_dir)
        if result.returncode == 0:
            return {"success": True, "message": f"Stamped revision {revision}",
                    "command": " ".join(cmd)}
        else:
            return {"success": False, "error": result.stderr.strip(),
                    "command": " ".join(cmd)}
    except FileNotFoundError:
        return {"success": False, "error": "alembic not found. Is it installed and in PATH?"}


def dump_table_csv(fix: dict) -> dict:
    """Backup a table or column to CSV before destructive operation."""
    db_url = fix["db_url"]
    table = fix["table"]
    columns = fix.get("columns", ["*"])
    output_path = Path(fix.get("output_path", f"{table}_backup.csv"))

    try:
        from sqlalchemy import create_engine, text
    except ImportError:
        return {"success": False, "error": "sqlalchemy not installed. Run: pip install sqlalchemy"}

    try:
        engine = create_engine(db_url)
        col_str = ", ".join(columns)
        with engine.connect() as conn:
            result = conn.execute(text(f"SELECT {col_str} FROM {table}"))
            col_names = result.keys()
            rows = result.fetchall()

        with open(output_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(list(col_names))
            writer.writerows([list(row) for row in rows])

        return {
            "success": True,
            "message": f"Backed up {len(rows)} rows from {table} to {output_path}",
            "output_file": str(output_path),
            "row_count": len(rows),
        }
    except Exception as e:
        return {"success": False, "error": str(e)}


FIX_HANDLERS = {
    "rename_migration_file": rename_migration_file,
    "update_down_revision": update_down_revision,
    "create_merge_migration": create_merge_migration_alembic,
    "create_merge_migration_django": create_merge_migration_django,
    "stamp_revision": stamp_revision_alembic,
    "dump_table_csv": dump_table_csv,
}

RISKY_FIX_TYPES = {"stamp_revision", "dump_table_csv"}


def main():
    parser = argparse.ArgumentParser(description="Apply an approved migration fix")
    parser.add_argument("--fix", required=True, help="JSON string describing the fix to apply")
    parser.add_argument("--dry-run", action="store_true", help="Show what would happen without doing it")
    parser.add_argument("--force", action="store_true", help="Force execution of risky operations (stamp_revision, dump_table_csv)")
    args = parser.parse_args()

    try:
        fix = json.loads(args.fix)
    except json.JSONDecodeError as e:
        print(json.dumps({"success": False, "error": f"Invalid JSON: {e}"}))
        sys.exit(1)

    fix_type = fix.get("fix_type")
    if not fix_type:
        print(json.dumps({"success": False, "error": "fix_type is required in fix JSON"}))
        sys.exit(1)

    handler = FIX_HANDLERS.get(fix_type)
    if not handler:
        print(json.dumps({
            "success": False,
            "error": f"Unknown fix_type '{fix_type}'. Available: {list(FIX_HANDLERS.keys())}",
        }))
        sys.exit(1)

    # Check if this is a risky operation
    if fix_type in RISKY_FIX_TYPES and not args.force:
        print(json.dumps({
            "success": False,
            "error": f"Fix type '{fix_type}' requires explicit approval. Pass --force flag to proceed.",
            "warning": "This operation may alter or delete data. Ensure you have backups.",
        }))
        sys.exit(2)

    if args.dry_run:
        print(json.dumps({
            "dry_run": True,
            "fix_type": fix_type,
            "fix": fix,
            "message": f"Would apply fix: {fix_type}. Run without --dry-run to proceed.",
        }))
        return

    result = handler(fix)
    print(json.dumps(result, indent=2))

    if not result.get("success"):
        sys.exit(1)


if __name__ == "__main__":
    main()

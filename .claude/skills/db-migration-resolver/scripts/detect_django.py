#!/usr/bin/env python3
"""
detect_django.py — Scan a Django project for migration conflicts.

Usage:
    python detect_django.py --path <django_project_root>

Output: JSON to stdout with detected conflicts.
Does NOT require a running DB — reads migration files directly.
"""
import argparse
import ast
import json
import os
import re
import sys
from collections import defaultdict
from pathlib import Path


def find_migration_dirs(project_root: Path) -> list[Path]:
    """Find all Django app migration directories under the project root."""
    migration_dirs = []
    for item in project_root.rglob("migrations"):
        if item.is_dir() and (item / "__init__.py").exists():
            migration_dirs.append(item)
    return migration_dirs


def parse_django_migration(filepath: Path) -> dict | None:
    """Parse a Django migration file to extract dependencies and operations."""
    try:
        source = filepath.read_text(encoding="utf-8")
        tree = ast.parse(source)
    except (OSError, SyntaxError):
        return None

    result = {
        "file": str(filepath),
        "filename": filepath.name,
        "app": filepath.parent.parent.name,
        "dependencies": [],
        "operations": [],
        "risky_ops": [],
        "has_reverse": True,  # assume reversible unless we find noop
    }

    for node in ast.walk(tree):
        if not isinstance(node, ast.ClassDef) or node.name != "Migration":
            continue

        for item in node.body:
            # Extract dependencies
            if isinstance(item, ast.Assign):
                for target in item.targets:
                    if isinstance(target, ast.Name) and target.id == "dependencies":
                        if isinstance(item.value, (ast.List, ast.Tuple)):
                            for elt in item.value.elts:
                                if isinstance(elt, (ast.Tuple, ast.List)) and len(elt.elts) == 2:
                                    try:
                                        app = ast.literal_eval(elt.elts[0])
                                        name = ast.literal_eval(elt.elts[1])
                                        result["dependencies"].append((app, name))
                                    except Exception:
                                        pass

            # Extract operations
            if isinstance(item, ast.Assign):
                for target in item.targets:
                    if isinstance(target, ast.Name) and target.id == "operations":
                        if isinstance(item.value, ast.List):
                            for op_node in item.value.elts:
                                if isinstance(op_node, ast.Call):
                                    op_name = ""
                                    if isinstance(op_node.func, ast.Attribute):
                                        op_name = op_node.func.attr
                                    elif isinstance(op_node.func, ast.Name):
                                        op_name = op_node.func.id
                                    result["operations"].append(op_name)

    # Classify risky operations
    risky_map = {
        "RemoveField": "remove_field",
        "DeleteModel": "delete_model",
        "AlterField": "alter_field",
        "RenameField": "rename_field",
        "RenameModel": "rename_model",
        "AddConstraint": "add_constraint",
        "RunSQL": "raw_sql",
        "RunPython": "run_python",
        "SeparateDatabaseAndState": "state_only",
    }
    for op in result["operations"]:
        if op in risky_map:
            result["risky_ops"].append(risky_map[op])

    # Check for RunSQL noop (reverse_sql=None or migrations.RunSQL.noop)
    if "RunSQL" in result["operations"]:
        if "RunSQL.noop" in source or "reverse_sql=None" in source:
            result["has_reverse"] = False

    # Check for RunPython without reverse
    if "RunPython" in result["operations"]:
        if not re.search(r"RunPython\([^)]+,[^)]+\)", source):
            # Single argument = no reverse function
            result["has_reverse"] = False

    return result


def detect_branching(app_migrations: dict[str, list[dict]]) -> list[dict]:
    """Find apps with multiple leaf migrations (no other migration depending on them)."""
    conflicts = []

    for app, migrations in app_migrations.items():
        # Build set of all migrations that are depended on by something
        depended_on = set()
        for m in migrations:
            for dep_app, dep_name in m["dependencies"]:
                if dep_app == app:
                    depended_on.add(dep_name)

        # Leaves = migrations not depended on by anyone
        leaves = [m for m in migrations if m["filename"].replace(".py", "") not in depended_on]

        if len(leaves) > 1:
            conflicts.append({
                "type": "branching_migration",
                "severity": "medium",
                "description": f"App '{app}' has {len(leaves)} leaf migrations (branching conflict): "
                               + ", ".join(l["filename"] for l in leaves),
                "app": app,
                "files": [l["file"] for l in leaves],
                "auto_fix": True,
                "fix_command": f"python manage.py makemigrations --merge --name merge_heads {app}",
            })

    return conflicts


def detect_data_loss_ops(app_migrations: dict[str, list[dict]]) -> list[dict]:
    """Flag destructive operations."""
    destructive = {"remove_field", "delete_model"}
    conflicts = []
    for app, migrations in app_migrations.items():
        for m in migrations:
            found = [op for op in m["risky_ops"] if op in destructive]
            if found:
                conflicts.append({
                    "type": "data_loss_risk",
                    "severity": "high",
                    "description": f"{m['app']}/{m['filename']} contains destructive operations: "
                                   + ", ".join(found),
                    "files": [m["file"]],
                    "risky_ops": found,
                    "auto_fix": False,
                    "suggestion": "Backup data with `manage.py dumpdata` before applying. "
                                  "Consider deprecating (rename) instead of removing.",
                })
    return conflicts


def detect_irreversible(app_migrations: dict[str, list[dict]]) -> list[dict]:
    """Flag migrations with no reverse logic."""
    conflicts = []
    for app, migrations in app_migrations.items():
        for m in migrations:
            if not m["has_reverse"] and m["risky_ops"]:
                conflicts.append({
                    "type": "irreversible_migration",
                    "severity": "high",
                    "description": f"{m['app']}/{m['filename']} has no reverse/downgrade logic "
                                   f"for operations: {', '.join(m['risky_ops'])}",
                    "files": [m["file"]],
                    "auto_fix": False,
                    "suggestion": "Add a reverse function to RunPython or provide reverse_sql in RunSQL.",
                })
    return conflicts


def detect_fk_constraints(app_migrations: dict[str, list[dict]]) -> list[dict]:
    """Flag migrations that add FK constraints or enforce NOT NULL."""
    conflicts = []
    for app, migrations in app_migrations.items():
        for m in migrations:
            # Check for AddConstraint or AlterField making field non-nullable
            if "add_constraint" in m["risky_ops"] or "alter_field" in m["risky_ops"]:
                try:
                    source = Path(m["file"]).read_text(encoding="utf-8")
                    if "ForeignKey" in source or "null=False" in source:
                        conflicts.append({
                            "type": "constraint_risk",
                            "severity": "high",
                            "description": f"{m['app']}/{m['filename']} adds FK or NOT NULL constraint. "
                                           "Verify existing data is compatible.",
                            "files": [m["file"]],
                            "auto_fix": False,
                            "suggestion": "Run inspect_schema.py to check for orphaned/null rows first.",
                        })
                except OSError:
                    pass
    return conflicts


def main():
    parser = argparse.ArgumentParser(description="Detect Django migration conflicts")
    parser.add_argument("--path", required=True, help="Django project root directory")
    args = parser.parse_args()

    project_root = Path(args.path)
    if not project_root.exists():
        print(json.dumps({"error": f"Directory not found: {args.path}"}))
        sys.exit(1)

    migration_dirs = find_migration_dirs(project_root)
    if not migration_dirs:
        print(json.dumps({"conflicts": [], "summary": "No Django migration directories found."}))
        return

    app_migrations: dict[str, list[dict]] = defaultdict(list)
    total_files = 0

    for mdir in migration_dirs:
        app_name = mdir.parent.name
        for f in sorted(mdir.glob("*.py")):
            if f.name == "__init__.py":
                continue
            parsed = parse_django_migration(f)
            if parsed:
                app_migrations[app_name].append(parsed)
                total_files += 1

    conflicts = []
    conflicts.extend(detect_branching(dict(app_migrations)))
    conflicts.extend(detect_data_loss_ops(dict(app_migrations)))
    conflicts.extend(detect_irreversible(dict(app_migrations)))
    conflicts.extend(detect_fk_constraints(dict(app_migrations)))

    output = {
        "framework": "django",
        "apps_scanned": len(app_migrations),
        "scanned_files": total_files,
        "conflict_count": len(conflicts),
        "conflicts": conflicts,
        "summary": f"Found {len(conflicts)} conflict(s) across {total_files} migration file(s) "
                   f"in {len(app_migrations)} app(s)."
                   if conflicts else
                   f"No conflicts found in {total_files} migration file(s) across "
                   f"{len(app_migrations)} app(s).",
    }
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
detect_alembic.py — Scan an Alembic migrations directory for conflicts.

Usage:
    python detect_alembic.py --path <alembic_versions_dir>

Output: JSON to stdout with detected conflicts.
"""
import argparse
import ast
import json
import os
import re
import sys
from collections import defaultdict
from pathlib import Path


def parse_migration_file(filepath: Path) -> dict | None:
    """Extract revision, down_revision, upgrade/downgrade ops from a migration file."""
    try:
        source = filepath.read_text(encoding="utf-8")
    except OSError:
        return None

    result = {
        "file": str(filepath),
        "filename": filepath.name,
        "revision": None,
        "down_revision": None,
        "has_upgrade": False,
        "has_downgrade": False,
        "downgrade_is_empty": False,
        "risky_ops": [],
    }

    # Extract revision and down_revision via regex (faster than full AST for these)
    rev_match = re.search(r"^revision\s*=\s*['\"]([^'\"]+)['\"]", source, re.MULTILINE)
    down_match = re.search(r"^down_revision\s*=\s*(.+)$", source, re.MULTILINE)

    if rev_match:
        result["revision"] = rev_match.group(1).strip()

    if down_match:
        raw = down_match.group(1).strip()
        if raw in ("None", "null"):
            result["down_revision"] = None
        elif raw.startswith("(") or raw.startswith("["):
            # Tuple/list — merge migration with multiple parents
            try:
                result["down_revision"] = ast.literal_eval(raw)
            except Exception:
                result["down_revision"] = raw
        else:
            result["down_revision"] = raw.strip("'\"")

    # Detect upgrade/downgrade presence
    result["has_upgrade"] = bool(re.search(r"^def upgrade\(\)", source, re.MULTILINE))
    result["has_downgrade"] = bool(re.search(r"^def downgrade\(\)", source, re.MULTILINE))

    # Detect empty/noop downgrade
    if result["has_downgrade"]:
        downgrade_match = re.search(
            r"def downgrade\(\):\s*\n((?:[ \t]+.*\n)*)", source, re.MULTILINE
        )
        if downgrade_match:
            body = downgrade_match.group(1).strip()
            if not body or body in ("pass", "..."):
                result["downgrade_is_empty"] = True

    # Detect risky operations
    risky_patterns = [
        (r"op\.drop_column\(", "drop_column"),
        (r"op\.drop_table\(", "drop_table"),
        (r"op\.drop_constraint\(", "drop_constraint"),
        (r"op\.alter_column\(.*type_=", "type_change"),
        (r"op\.alter_column\(.*nullable=False", "not_null_change"),
        (r"op\.create_foreign_key\(", "create_fk"),
        (r"op\.execute\(", "raw_sql"),
    ]
    for pattern, label in risky_patterns:
        if re.search(pattern, source):
            result["risky_ops"].append(label)

    return result


def detect_branching(migrations: list[dict]) -> list[dict]:
    """Find migrations where two+ files share the same down_revision (branch point)."""
    parent_map = defaultdict(list)
    for m in migrations:
        dr = m["down_revision"]
        if isinstance(dr, (list, tuple)):
            # This is already a merge migration — skip for branch detection
            continue
        parent_map[dr].append(m)

    conflicts = []
    for parent, children in parent_map.items():
        if len(children) > 1:
            conflicts.append({
                "type": "branching_migration",
                "severity": "medium",
                "description": f"Multiple migrations share parent '{parent}': "
                               + ", ".join(c["filename"] for c in children),
                "files": [c["file"] for c in children],
                "revisions": [c["revision"] for c in children],
                "parent_revision": parent,
                "auto_fix": True,
                "fix_command": f"alembic merge -m 'merge_heads' "
                               + " ".join(c["revision"] for c in children),
            })
    return conflicts


def detect_empty_downgrades(migrations: list[dict]) -> list[dict]:
    """Find migrations with risky ops but empty/missing downgrade."""
    conflicts = []
    for m in migrations:
        if m["risky_ops"] and (not m["has_downgrade"] or m["downgrade_is_empty"]):
            conflicts.append({
                "type": "irreversible_downgrade",
                "severity": "high",
                "description": f"{m['filename']} has risky operations "
                               f"({', '.join(m['risky_ops'])}) but downgrade() is empty/missing.",
                "files": [m["file"]],
                "risky_ops": m["risky_ops"],
                "auto_fix": False,
                "suggestion": "Add proper downgrade() logic or document why rollback is impossible.",
            })
    return conflicts


def detect_data_loss_ops(migrations: list[dict]) -> list[dict]:
    """Flag migrations that contain destructive operations."""
    destructive = {"drop_column", "drop_table", "drop_constraint"}
    conflicts = []
    for m in migrations:
        found = [op for op in m["risky_ops"] if op in destructive]
        if found:
            conflicts.append({
                "type": "data_loss_risk",
                "severity": "high",
                "description": f"{m['filename']} contains potentially destructive operations: "
                               + ", ".join(found),
                "files": [m["file"]],
                "risky_ops": found,
                "auto_fix": False,
                "suggestion": "Backup affected rows before applying. Consider renaming column "
                              "instead of dropping.",
            })
    return conflicts


def detect_fk_ops(migrations: list[dict]) -> list[dict]:
    """Flag migrations that create FK constraints (need data validation first)."""
    conflicts = []
    for m in migrations:
        if "create_fk" in m["risky_ops"]:
            conflicts.append({
                "type": "fk_constraint",
                "severity": "high",
                "description": f"{m['filename']} creates a FK constraint. Verify no orphaned rows "
                               "exist before applying.",
                "files": [m["file"]],
                "auto_fix": False,
                "suggestion": "Run inspect_schema.py to check for orphaned rows first.",
            })
    return conflicts


def main():
    parser = argparse.ArgumentParser(description="Detect Alembic migration conflicts")
    parser.add_argument("--path", required=True, help="Path to alembic/versions directory")
    args = parser.parse_args()

    versions_dir = Path(args.path)
    if not versions_dir.exists():
        print(json.dumps({"error": f"Directory not found: {args.path}"}))
        sys.exit(1)

    migration_files = sorted(versions_dir.glob("*.py"))
    migration_files = [f for f in migration_files if not f.name.startswith("__")]

    if not migration_files:
        print(json.dumps({"conflicts": [], "summary": "No migration files found."}))
        return

    migrations = []
    for f in migration_files:
        parsed = parse_migration_file(f)
        if parsed and parsed["revision"]:
            migrations.append(parsed)

    conflicts = []
    conflicts.extend(detect_branching(migrations))
    conflicts.extend(detect_empty_downgrades(migrations))
    conflicts.extend(detect_data_loss_ops(migrations))
    conflicts.extend(detect_fk_ops(migrations))

    output = {
        "framework": "alembic",
        "scanned_files": len(migrations),
        "conflict_count": len(conflicts),
        "conflicts": conflicts,
        "summary": f"Found {len(conflicts)} conflict(s) in {len(migrations)} migration file(s)."
                   if conflicts else f"No conflicts found in {len(migrations)} migration file(s).",
    }
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()

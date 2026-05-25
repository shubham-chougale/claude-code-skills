#!/usr/bin/env python3
"""
detect_changes.py — Detect what changed in a commit or file edit and identify which docs and diagrams need updating.

Usage:
    python detect_changes.py                          # Analyze the last git commit
    python detect_changes.py --file path/to/file.py   # Analyze a single file change
    python detect_changes.py --staged                 # Analyze staged changes
    python detect_changes.py --quiet                  # Machine-readable JSON output
"""

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

# File pattern → (document name, diagrams flagged)
ROUTING_RULES = [
    # Pattern (regex), Document to update, Diagrams flagged, Action type
    (r"migrations/|.*_migration\.|\.sql$",           "DATABASE",         ["erd"],                            "auto_update"),
    (r"routes/|controllers/|endpoints/|api/|views/", "API",              ["sequence-diagram", "api-lifecycle"], "auto_update"),
    (r"package\.json|requirements\.txt|Podfile|build\.gradle|go\.mod", "SETUP", [],                          "auto_update"),
    (r"\.env\.example",                              "SETUP",            [],                                  "auto_update"),
    (r"src/components/|^components/",                "COMPONENT_DOC",    [],                                  "auto_update"),
    (r"src/modules/|src/services/",                  "MODULE_DOC",       [],                                  "auto_update"),
    (r"infra/|terraform/|\.tf$",                     "INFRA",            ["deployment-topology"],            "flag"),
    (r"\.github/workflows/|Jenkinsfile|\.gitlab-ci\.yml", "CICD",        ["cicd-pipeline"],                   "flag"),
    (r"docker-compose\.yml|Dockerfile",              "INFRA",            ["deployment-topology"],            "flag"),
]

# Change type → list of impacted documents (from change_impact_map)
CHANGE_IMPACT = {
    "new_feature":      ["USER_STORIES", "FRD", "API", "DATABASE", "HLD", "TEST_CASES", "RELEASE_NOTES", "CHANGELOG"],
    "feature_modified": ["FRD", "API", "DATABASE", "TEST_CASES", "RELEASE_NOTES", "CHANGELOG"],
    "feature_removed":  ["FRD", "API", "DATABASE", "SCOPE", "RELEASE_NOTES", "CHANGELOG"],
    "bug_fix":          ["TEST_CASES", "CHANGELOG", "RELEASE_NOTES", "RUNBOOK"],
    "api_change":       ["API", "FRD", "TEST_CASES", "RELEASE_NOTES", "CHANGELOG"],
    "db_schema_change": ["DATABASE", "TEST_CASES", "RELEASE_NOTES", "CHANGELOG"],
    "ui_change":        ["FRD", "USER_STORIES", "TEST_CASES", "RELEASE_NOTES", "CHANGELOG"],
    "infra_change":     ["INFRA", "DEPLOY", "CICD", "RUNBOOK", "CHANGELOG"],
    "performance_fix":  ["TEST_CASES", "CHANGELOG", "RELEASE_NOTES"],
}


def get_changed_files(mode="last_commit"):
    """Get list of changed files based on mode."""
    try:
        if mode == "last_commit":
            result = subprocess.run(
                ["git", "diff", "--name-only", "HEAD~1", "HEAD"],
                capture_output=True, text=True, check=True
            )
        elif mode == "staged":
            result = subprocess.run(
                ["git", "diff", "--name-only", "--cached"],
                capture_output=True, text=True, check=True
            )
        else:
            return []
        return [f for f in result.stdout.strip().split("\n") if f]
    except subprocess.CalledProcessError as e:
        print(f"⚠️  detect_changes.py: git command failed — ensure you are running inside a git repository.", file=sys.stderr)
        return []
    except FileNotFoundError:
        print(f"⚠️  detect_changes.py: git not found — ensure git is installed and in PATH.", file=sys.stderr)
        return []


def get_commit_message():
    """Get the last commit message for change type detection."""
    try:
        result = subprocess.run(
            ["git", "log", "-1", "--pretty=%s"],
            capture_output=True, text=True, check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError:
        return ""


def classify_change_type(commit_msg):
    """Infer change type from conventional commit prefix."""
    msg = commit_msg.lower()
    if msg.startswith("feat:") or msg.startswith("feat("):
        return "new_feature"
    if msg.startswith("fix:") or msg.startswith("fix("):
        return "bug_fix"
    if msg.startswith("refactor:"):
        return "feature_modified"
    if msg.startswith("perf:"):
        return "performance_fix"
    if msg.startswith("revert:"):
        return "feature_removed"
    return None


def route_files_to_docs(changed_files):
    """Map changed files to documents and diagrams using routing rules."""
    affected = {}
    for file_path in changed_files:
        for pattern, doc, diagrams, action in ROUTING_RULES:
            if re.search(pattern, file_path):
                if doc not in affected:
                    affected[doc] = {"action": action, "diagrams": set(), "trigger_files": []}
                affected[doc]["diagrams"].update(diagrams)
                affected[doc]["trigger_files"].append(file_path)
                break
    # Convert sets to lists for JSON
    for doc in affected:
        affected[doc]["diagrams"] = sorted(list(affected[doc]["diagrams"]))
    return affected


def render_human_report(affected, change_type, commit_msg):
    """Print a human-readable report."""
    if not affected and not change_type:
        print("📋 Doc Maintenance Check — No documentation impact detected.")
        return

    print("\n📋 Documentation Maintenance Check")
    print("=" * 60)

    if commit_msg:
        print(f"Commit:      {commit_msg[:80]}")
    if change_type:
        print(f"Change type: {change_type}")
        impact = CHANGE_IMPACT.get(change_type, [])
        if impact:
            print(f"Impacts:     {', '.join(impact)}")

    print()

    if affected:
        auto_updates = {k: v for k, v in affected.items() if v["action"] == "auto_update"}
        flags = {k: v for k, v in affected.items() if v["action"] == "flag"}

        if auto_updates:
            print("✅ Auto-update needed:")
            for doc, info in auto_updates.items():
                print(f"   • {doc} — triggered by: {info['trigger_files'][0]}")
                if info["diagrams"]:
                    for diag in info["diagrams"]:
                        print(f"     ⚠️  Diagram needs review: {diag}.html")
            print()

        if flags:
            print("⚠️  Flagged for human review:")
            for doc, info in flags.items():
                print(f"   • {doc} — triggered by: {info['trigger_files'][0]}")
                if info["diagrams"]:
                    for diag in info["diagrams"]:
                        print(f"     ⚠️  Diagram needs review: {diag}.html")
            print()

    print("Next step:")
    print('  Tell Claude: "Check .claude/hooks/hooks.md and apply the doc maintenance for this change."')
    print()


def main():
    parser = argparse.ArgumentParser(description="Detect changes and identify affected documentation")
    parser.add_argument("--file", help="Analyze a single file path")
    parser.add_argument("--staged", action="store_true", help="Analyze staged changes")
    parser.add_argument("--quiet", action="store_true", help="Output machine-readable JSON only")
    args = parser.parse_args()

    if args.file:
        changed_files = [args.file]
        commit_msg = ""
    elif args.staged:
        changed_files = get_changed_files("staged")
        commit_msg = ""
    else:
        changed_files = get_changed_files("last_commit")
        commit_msg = get_commit_message()

    change_type = classify_change_type(commit_msg) if commit_msg else None
    affected = route_files_to_docs(changed_files)

    if args.quiet:
        print(json.dumps({
            "changed_files": changed_files,
            "commit_message": commit_msg,
            "change_type": change_type,
            "affected_docs": affected,
            "impacted_by_type": CHANGE_IMPACT.get(change_type, []) if change_type else []
        }, indent=2))
    else:
        render_human_report(affected, change_type, commit_msg)


if __name__ == "__main__":
    main()

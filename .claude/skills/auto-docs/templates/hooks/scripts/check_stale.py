#!/usr/bin/env python3
"""
check_stale.py — Quick stale doc check, used by PR checks and pre-push hooks.

Unlike audit_docs.py (full audit), this is fast and focused:
- Checks only docs affected by the current PR / branch diff
- Returns exit code 0 if clean, 1 if any docs are stale relative to the changes

Usage:
    python check_stale.py                    # Check current branch vs main
    python check_stale.py --base develop     # Check vs different base branch
    python check_stale.py --since-session-start  # Check changes since session start
    python check_stale.py --summary-only     # Brief output
"""

import argparse
import re
import subprocess
import sys
from pathlib import Path

# Import shared routing logic
sys.path.insert(0, str(Path(__file__).parent))
from detect_changes import ROUTING_RULES, CHANGE_IMPACT, classify_change_type


def get_diff_files(base_branch="main"):
    """Get files changed between current branch and base."""
    try:
        result = subprocess.run(
            ["git", "diff", "--name-only", f"{base_branch}...HEAD"],
            capture_output=True, text=True, check=True
        )
        return [f for f in result.stdout.strip().split("\n") if f]
    except subprocess.CalledProcessError:
        return []


def get_session_changed_files():
    """Get files changed since last commit (for in-Claude-session checks)."""
    try:
        result = subprocess.run(
            ["git", "diff", "--name-only", "HEAD"],
            capture_output=True, text=True, check=True
        )
        return [f for f in result.stdout.strip().split("\n") if f]
    except subprocess.CalledProcessError:
        return []


def identify_required_doc_updates(changed_files):
    """For each changed code file, identify the doc(s) that should be updated."""
    required = {}
    for file_path in changed_files:
        for pattern, doc, diagrams, action in ROUTING_RULES:
            if re.search(pattern, file_path):
                required.setdefault(doc, {"files": [], "diagrams": set(), "action": action})
                required[doc]["files"].append(file_path)
                required[doc]["diagrams"].update(diagrams)
                break
    return required


def doc_was_updated_in_diff(doc_name, changed_files):
    """Check if the doc file itself appears in the diff."""
    # Common doc paths
    doc_paths = {
        "API": "docs/architecture/API.md",
        "DATABASE": "docs/architecture/DATABASE.md",
        "SETUP": "docs/deployment/SETUP.md",
        "FRD": "docs/requirements/FRD.md",
        "HLD": "docs/architecture/HLD.md",
        "LLD": "docs/architecture/LLD.md",
        "CICD": "docs/deployment/CICD.md",
        "INFRA": "docs/deployment/INFRA.md",
        "TEST_CASES": "docs/testing/TEST_CASES.md",
        "CHANGELOG": "CHANGELOG.md",
    }
    target = doc_paths.get(doc_name, "")
    return any(target in f for f in changed_files)


def main():
    parser = argparse.ArgumentParser(description="Quick stale doc check for PR / pre-push")
    parser.add_argument("--base", default="main", help="Base branch to compare against")
    parser.add_argument("--since-session-start", action="store_true", help="Check uncommitted changes only")
    parser.add_argument("--summary-only", action="store_true", help="Brief output")
    args = parser.parse_args()

    if args.since_session_start:
        changed_files = get_session_changed_files()
    else:
        changed_files = get_diff_files(args.base)

    if not changed_files:
        if not args.summary_only:
            print("✅ No changes detected.")
        sys.exit(0)

    required = identify_required_doc_updates(changed_files)

    if not required:
        if not args.summary_only:
            print(f"✅ {len(changed_files)} files changed — no doc updates required.")
        sys.exit(0)

    stale_docs = []
    for doc, info in required.items():
        if not doc_was_updated_in_diff(doc, changed_files):
            stale_docs.append((doc, info))

    if not stale_docs:
        if not args.summary_only:
            print(f"✅ All affected docs were updated in this branch.")
        sys.exit(0)

    # Stale docs found
    if args.summary_only:
        doc_names = ", ".join(d for d, _ in stale_docs)
        print(f"⚠️  {len(stale_docs)} doc(s) need updating: {doc_names}")
    else:
        print()
        print(f"⚠️  Doc Updates Needed for This Branch")
        print("=" * 60)
        for doc, info in stale_docs:
            action_label = "auto-update" if info["action"] == "auto_update" else "human review"
            print(f"\n  • {doc} — needs {action_label}")
            print(f"    Triggered by:")
            for f in info["files"][:3]:
                print(f"      - {f}")
            if info["diagrams"]:
                for diag in sorted(info["diagrams"]):
                    print(f"    ⚠️  Diagram also needs review: {diag}.html")

        print()
        print("Tell Claude:")
        print('  "Check .claude/hooks/hooks.md and update the docs flagged by check_stale.py"')
        print()

    sys.exit(1)


if __name__ == "__main__":
    main()

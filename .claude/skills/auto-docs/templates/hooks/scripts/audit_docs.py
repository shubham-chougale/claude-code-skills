#!/usr/bin/env python3
"""
audit_docs.py — Full documentation staleness audit.

Reads every doc's `last_updated` header, compares against the staleness
threshold in settings.json, and reports stale documents.

Usage:
    python audit_docs.py                # Full report
    python audit_docs.py --format brief # One-line summary per doc
    python audit_docs.py --format json  # Machine-readable
"""

import argparse
import json
import re
from datetime import date, datetime
from pathlib import Path

SETTINGS_PATH = Path(".claude/skills/auto-docs/settings.json")
DOCS_ROOT = Path("docs")
CHANGELOG_PATH = Path("CHANGELOG.md")


def load_doc_registry():
    """Load the documents config from settings.json."""
    if not SETTINGS_PATH.exists():
        return {}
    try:
        data = json.loads(SETTINGS_PATH.read_text(encoding="utf-8"))
        return data.get("documents", {})
    except json.JSONDecodeError:
        return {}


def parse_last_updated(content):
    """Extract last_updated date from the document header."""
    match = re.search(r"last_updated:\s*(\d{4}-\d{2}-\d{2})", content)
    if not match:
        return None
    try:
        return datetime.strptime(match.group(1), "%Y-%m-%d").date()
    except ValueError:
        return None


def check_document(doc_name, config):
    """Check a single document's freshness."""
    path = Path(config["path"].lstrip("/"))
    threshold = config.get("staleness_threshold_days")

    if not path.exists():
        return {
            "name": doc_name,
            "path": str(path),
            "status": "missing",
            "reason": "File does not exist",
        }

    content = path.read_text(encoding="utf-8")
    last_updated = parse_last_updated(content)

    if not last_updated:
        return {
            "name": doc_name,
            "path": str(path),
            "status": "no_header",
            "reason": "No last_updated header found",
        }

    if threshold is None:
        return {
            "name": doc_name,
            "path": str(path),
            "status": "fresh",
            "last_updated": last_updated.isoformat(),
            "reason": "Permanent doc — no staleness check",
        }

    days_old = (date.today() - last_updated).days

    if days_old > threshold:
        return {
            "name": doc_name,
            "path": str(path),
            "status": "stale",
            "last_updated": last_updated.isoformat(),
            "days_old": days_old,
            "threshold": threshold,
            "reason": f"Last updated {days_old} days ago (threshold: {threshold})",
        }

    return {
        "name": doc_name,
        "path": str(path),
        "status": "fresh",
        "last_updated": last_updated.isoformat(),
        "days_old": days_old,
        "threshold": threshold,
    }


def render_full_report(results):
    """Print the full audit report."""
    today = date.today().isoformat()
    fresh = [r for r in results if r["status"] == "fresh"]
    stale = [r for r in results if r["status"] == "stale"]
    missing = [r for r in results if r["status"] == "missing"]
    no_header = [r for r in results if r["status"] == "no_header"]

    print()
    print(f"📋 Doc Audit Report — {today}")
    print("=" * 60)
    print()

    if fresh:
        print(f"✅ Up to date ({len(fresh)}):")
        for r in fresh:
            print(f"   • {r['name']}")
        print()

    if stale:
        print(f"⚠️  Needs update ({len(stale)}):")
        for r in stale:
            print(f"   • {r['name']} — {r['reason']}")
            print(f"     Path: {r['path']}")
        print()

    if no_header:
        print(f"❓ Missing header ({len(no_header)}):")
        for r in no_header:
            print(f"   • {r['name']} — {r['path']}")
        print()

    if missing:
        print(f"❌ Missing files ({len(missing)}):")
        for r in missing:
            print(f"   • {r['name']} — expected at {r['path']}")
        print()

    total_issues = len(stale) + len(missing) + len(no_header)
    if total_issues == 0:
        print("🎉 All docs are fresh. No action needed.")
    else:
        print(f"Action required: {total_issues} item(s) need attention.")
    print()


def render_brief_report(results):
    """One line per doc."""
    for r in results:
        status_icon = {"fresh": "✅", "stale": "⚠️ ", "missing": "❌", "no_header": "❓"}[r["status"]]
        print(f"{status_icon} {r['name']:<20} {r['reason'] if 'reason' in r else 'OK'}")


def main():
    parser = argparse.ArgumentParser(description="Documentation staleness audit")
    parser.add_argument("--format", choices=["full", "brief", "json"], default="full")
    args = parser.parse_args()

    registry = load_doc_registry()
    if not registry:
        print("⚠️  Could not load document registry from settings.json")
        return

    results = [check_document(name, cfg) for name, cfg in registry.items()]

    if args.format == "json":
        print(json.dumps(results, indent=2, default=str))
    elif args.format == "brief":
        render_brief_report(results)
    else:
        render_full_report(results)


if __name__ == "__main__":
    main()

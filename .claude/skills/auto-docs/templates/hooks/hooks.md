# Documentation Hooks — {{PROJECT_NAME}}

> **This is the file to point Claude to.**
> Say to Claude: *"Check `.claude/hooks/hooks.md` and apply the doc maintenance rules for this change."*
> Claude will then read this file, the supporting scripts, and the maintenance rules — then update the right docs and diagrams.

---

## The Problem We Are Solving

Documentation drifts out of sync with code. This happens on every project. The reason is simple:

```
Code changes happen every day.
Docs only get updated when someone remembers.
Nobody ever remembers.
Result: docs become a lie within 4 weeks.
```

The fix is to remove the "remember" step. Updates must be triggered by events — commits, PRs, releases, sprint cycles — not by human discipline.

This folder implements **4 layers of automation** so docs and diagrams stay accurate from project start to project end.

---

## The 4 Hook Layers

| Layer | When It Runs | What It Catches | Works Without Claude? |
|-------|-------------|-----------------|----------------------|
| 1. Git Hooks | On every `git commit` and `git push` | All commits, even outside Claude sessions | ✅ Yes |
| 2. Claude Code Hooks | When Claude edits code in a session | Edits made via Claude | ⚠️ Only in Claude sessions |
| 3. CI / PR Checks | On every PR opened or updated | Catches stale docs before merge | ✅ Yes (runs on GitHub) |
| 4. Sprint Audit | On-demand via `/auto-docs audit` or cron | Periodic full-system check | ✅ Yes |

These layers overlap on purpose. If one misses, another catches it.

---

## What Is In This Folder

```
.claude/hooks/
├── hooks.md                        ← This file. The entry point for Claude.
├── doc-maintenance.md              ← Detailed maintenance rules (what doc updates when)
├── claude-hooks.json               ← Reference config for Claude Code hooks
└── scripts/
    ├── detect_changes.py           ← Detect what changed and which docs are affected
    ├── update_changelog.py         ← Auto-append CHANGELOG.md from commit message
    ├── audit_docs.py               ← Full staleness audit (powers /auto-docs audit)
    └── check_stale.py              ← Quick stale check (used by PR hook)

.githooks/                          ← Lives at repo root, installed into .git/hooks/
├── post-commit                     ← Runs after every commit
├── post-commit.ps1                 ← Windows PowerShell variant
├── pre-push                        ← Optional: warns about stale docs before push
└── install.sh                      ← One-time installer (and install.ps1 for Windows)

.github/workflows/
└── doc-check.yml                   ← PR-time staleness check via GitHub Actions
```

---

## How To Use This System

### Telling Claude to Apply Hooks

When you make a change and want docs updated, say one of these to Claude:

```
"Check .claude/hooks/hooks.md and update the relevant docs for this change."
```

```
"Run the doc maintenance flow from .claude/hooks/ for what I just committed."
```

```
"I just changed [X]. Use .claude/hooks/hooks.md to figure out which docs and diagrams need updating."
```

Claude reads this file → reads `doc-maintenance.md` → identifies the change type → updates the right documents → flags the right diagrams.

### Running Hooks Manually

```bash
# Detect what changed in the last commit and report affected docs
python .claude/hooks/scripts/detect_changes.py

# Auto-append CHANGELOG from your last commit message
python .claude/hooks/scripts/update_changelog.py

# Full staleness audit
python .claude/hooks/scripts/audit_docs.py

# Quick stale check (for PR pre-checks)
python .claude/hooks/scripts/check_stale.py
```

### Installing Git Hooks (one time per developer machine)

```bash
# Mac / Linux
bash .githooks/install.sh

# Windows PowerShell
.\.githooks\install.ps1
```

This copies the hook scripts from `.githooks/` into `.git/hooks/` so they fire on every commit.

---

## What Each Layer Does in Detail

### Layer 1 — Git Hooks

**File:** `.githooks/post-commit`

After every commit, the hook:
1. Reads the commit diff
2. Runs `detect_changes.py` to identify what changed
3. Auto-appends an entry to `/CHANGELOG.md`
4. Prints a list of docs and diagrams that may need updating
5. If any critical doc is stale, prints a warning (but does not block)

**File:** `.githooks/pre-push`

Before push, the hook:
1. Runs `check_stale.py`
2. If P0 docs (BRD, ROLLBACK, API) are stale, asks for confirmation before pushing
3. Otherwise: silent pass

### Layer 2 — Claude Code Hooks

**File:** `claude-hooks.json` — merge contents into `.claude/settings.json`

Configures Claude Code to:
- After Claude uses `Edit` or `Write` on a code file → run `detect_changes.py`
- After Claude finishes a session → suggest doc updates if any changes are pending
- Before Claude starts a new task → check for stale docs and surface them

This means if you ask Claude to edit code, it knows to also update the docs without you having to remind it.

### Layer 3 — CI / PR Checks

**File:** `.github/workflows/doc-check.yml`

On every PR:
1. Runs `check_stale.py` against the PR diff
2. Posts a PR comment listing any docs that should be updated in this PR
3. Adds a status check — green if docs are fresh, yellow if any are stale
4. Does not block the merge (configurable)

### Layer 4 — Sprint Audit

**File:** `scripts/audit_docs.py`

Run manually or via cron at sprint end:
1. Reads every doc's `last_updated` header
2. Compares against `staleness_threshold_days` in `settings.json`
3. Compares API.md endpoints vs actual API files in the repo
4. Compares DATABASE.md tables vs actual migrations
5. Outputs a full Stale Doc Report

---

## How Changes Get Routed to Documents

When something changes, the hook system uses this routing logic (defined in `doc-maintenance.md`):

| Code Change | Document Updated | Diagram Flagged |
|------------|------------------|-----------------|
| API file (`routes/`, `controllers/`, `endpoints/`) | API.md | sequence-diagram, api-lifecycle |
| Migration file | DATABASE.md | erd |
| Package file (`package.json`, etc.) | SETUP.md | — |
| Pipeline config (`.github/workflows/`) | CICD.md (flag) | cicd-pipeline |
| Infra config (`terraform/`, `*.tf`) | INFRA.md (flag) | deployment-topology |
| New service directory | HLD.md (flag) | system-architecture |
| Component file | /docs/components/[name].md | — |
| Any code change | CHANGELOG.md | — |

Full mapping lives in `doc-maintenance.md`.

---

## Safety Rules — What Hooks Will Never Do

Hooks are designed to be helpful, not destructive. They will never:

- Delete content from any document
- Overwrite human-written sections with auto-generated content
- Auto-edit BRD, SCOPE, ROLLBACK, INCIDENT_RESPONSE, POSTMORTEM (these are human-only)
- Block a commit or push without explicit confirmation
- Modify diagrams — only flag them for human review

All edits are additive or replacement-with-preservation. Originals are kept.

---

## Troubleshooting

**Git hooks aren't firing after install:**
```bash
# Check that hooks are executable (Linux/Mac)
chmod +x .git/hooks/post-commit .git/hooks/pre-push

# Verify hook is installed
ls -la .git/hooks/
```

**Python scripts fail with "module not found":**
```bash
pip install -r .claude/hooks/scripts/requirements.txt
```

**Claude isn't reading this file when I ask:**
Be explicit: *"Read `.claude/hooks/hooks.md` first, then apply the maintenance rules."*

**A doc was auto-updated but the change is wrong:**
The doc still has the full edit history in git. Revert the unwanted edit. Then update `doc-maintenance.md` if the routing rule was wrong.

---

## Updating This System

If you change how the hook system works:

1. Update `doc-maintenance.md` with the new routing rule
2. Update the relevant script in `scripts/`
3. Update this `hooks.md` if the user-facing behavior changed
4. Commit and push — the hooks update for the whole team

---

*Last updated: {{DATE}} | Generated by /auto-docs init*

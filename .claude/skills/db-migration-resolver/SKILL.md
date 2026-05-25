---
name: db-migration-resolver
description: |
  Detects and resolves database migration conflicts for Alembic (SQLAlchemy) and Django projects.
  Automatically identifies branching migrations, schema drift, data loss risks, FK constraint
  violations, and irreversible downgrade issues. Auto-fixes safe conflicts and guides users
  interactively through risky resolutions. Use this skill whenever the user mentions migrations,
  alembic, django migrations, schema conflicts, migration branching, migration drift, rollback
  issues, or says things like "my migrations are broken", "alembic won't upgrade", "migration
  history is messed up", "schema out of sync", or "migration conflict after merging branches".
---

# Database Migration Conflict Resolver

Detect and resolve database migration conflicts in Alembic and Django projects. Work through
three phases: **detect** conflicts, **analyze and suggest** fixes, then **resolve interactively**
— auto-applying safe fixes and asking the user before touching anything risky.

## Start Here

1. Ask which framework: **Alembic** or **Django**?
2. Ask for the project root directory path
3. Read the relevant reference file for framework-specific commands:
   - Alembic → read `references/alembic.md`
   - Django → read `references/django.md`
4. Run the appropriate detection script (see Scripts section)
5. Present findings and guide resolution interactively

## What to Detect (MVP)

Read `references/conflict-types.md` for the full catalog. The four MVP scenarios:

| # | Conflict | Risk Level | Resolution |
|---|----------|-----------|------------|
| 1 | Branching/duplicate migrations | Medium | Auto-fix (with approval) |
| 2 | Schema drift + data loss warnings | High | Ask user — multiple options |
| 3 | FK constraint violations | High | Ask user — offer cleanup script |
| 4 | Irreversible downgrade | High | Warn + ask to add backup logic |

## Scripts

Run these scripts via bash. They output structured JSON — never load the script source into context.

```bash
# Detect Alembic conflicts
python .claude/skills/db-migration-resolver/scripts/detect_alembic.py --path {migrations_dir}

# Detect Django conflicts
python .claude/skills/db-migration-resolver/scripts/detect_django.py --path {project_dir}

# Inspect actual DB schema (needs connection string)
python .claude/skills/db-migration-resolver/scripts/inspect_schema.py --url {db_url} --table {table}

# Apply an approved fix
python .claude/skills/db-migration-resolver/scripts/apply_fix.py --fix {fix_json}
```

Ask the user for the DB connection string interactively when schema inspection is needed.
Never store or log credentials.

## Interactive Resolution Format

Always present findings in this format before taking any action:

```
🔍 Found N migration conflict(s):

[1] {CONFLICT TYPE} — {AUTO-FIX or REQUIRES APPROVAL}
    Problem: {plain English explanation}
    Impact:  {what breaks if not fixed}
    Fix:     {what we will do}
    [A]pply  [S]kip  [M]anual

[2] ...

Choose action for each conflict, or [F]ix All Safe / [R]eview All
```

- **Auto-fix eligible**: branching history, duplicate revision IDs, missing `downgrade()` stubs
- **Always ask first**: dropping columns/tables, type changes, FK constraints, data-altering ops
- Never apply any fix without explicit user confirmation ("A", "yes", "apply", "go ahead")

## Resolution Rules

| Operation | Safe to Auto-Apply | Requires Approval |
|-----------|-------------------|-------------------|
| Rename migration file | ✅ | — |
| Update `down_revision` | ✅ | — |
| Run `alembic merge` | ✅ | — |
| `alembic stamp {rev}` | — | ✅ Always ask |
| Drop column/table | — | ✅ Always ask |
| Add NOT NULL column | — | ✅ Always ask |
| Create FK constraint | — | ✅ Always ask |
| Change column type | — | ✅ Always ask |
| Delete/modify data | — | ✅ Always ask |

## After Fixing

After each fix, verify it worked:
- Alembic: run `alembic heads` — should show exactly 1 head
- Django: run `manage.py showmigrations` — no conflicts marker
- Report success or new errors to the user

## Reference Files

Load these only when needed (don't preload both):

- `references/alembic.md` — Alembic CLI commands, version file structure, fix patterns
- `references/django.md` — Django CLI commands, migration file structure, fix patterns
- `references/conflict-types.md` — Full catalog of all conflict types with fix guidance

## Security & Safety

- Never run destructive DB commands (DROP, DELETE, TRUNCATE) without explicit user approval
- Always show the exact command before running it
- Offer to dump affected rows to CSV before any data-removing operation
- If unsure about safety, ask — never guess on risky operations

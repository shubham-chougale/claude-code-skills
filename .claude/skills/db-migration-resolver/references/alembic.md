# Alembic Migration Reference

## Key CLI Commands

```bash
alembic heads           # Show current head(s) — more than 1 means branching conflict
alembic branches        # Show all branch points in history
alembic current         # Show what revision the DB is currently at
alembic history --verbose  # Full migration history with details
alembic upgrade head    # Apply all pending migrations
alembic downgrade -1    # Roll back one step
alembic merge -m "merge" <rev1> <rev2>  # Merge two branch heads into one
alembic stamp <rev>     # Mark a revision as applied WITHOUT running it (risky — ask first)
alembic revision --autogenerate -m "desc"  # Generate new migration from model diff
```

## Migration File Structure

Located in `alembic/versions/` (or custom path set in `alembic.ini`).

```python
# Example Alembic migration file
revision = '2a3b4c5d6e7f'      # This file's unique ID
down_revision = '1a2b3c4d5e6f'  # Parent migration (None = root)
branch_labels = None
depends_on = None

def upgrade():
    # Forward changes
    op.add_column('users', sa.Column('email', sa.String(255)))

def downgrade():
    # Reverse changes — must mirror upgrade exactly
    op.drop_column('users', 'email')
```

## Detecting Branching Conflicts

**Symptom:** `alembic heads` returns more than one line.

**Manual detection (no DB needed):**
1. Scan all `.py` files in `versions/`
2. Collect all `down_revision` values
3. Find any `down_revision` value that appears in more than one file → that's the branch point

**Example conflict:**
```
File A: revision='abc123', down_revision='root001'
File B: revision='def456', down_revision='root001'  ← same parent as A = BRANCH!
```

**Fix: `alembic merge`**
```bash
alembic merge -m "merge heads" abc123 def456
# Creates new file: merge_abc123_def456.py with both as parents
```
This is safe to auto-apply (with user approval) — it only creates a new merge file.

## Detecting Schema Drift

**Symptom:** `alembic upgrade head` fails with "column already exists" or "table doesn't exist".

**Detection approach:**
1. Run `alembic history` to get list of applied revisions
2. Check `alembic_version` table in DB for what's stamped as applied
3. For each applied migration, verify its `upgrade()` ops match actual DB schema
4. Discrepancy = schema drift

**Common causes:**
- Manual `ALTER TABLE` run directly on DB
- Migration applied partially then failed mid-way
- DB restored from snapshot at older revision
- Migration file edited after being applied

**Fix options (always ask user):**
1. `alembic stamp <rev>` — mark as applied without running (use if schema already matches)
2. Drop and recreate the offending object, then re-run migration
3. Write a new "cleanup" migration that brings DB to expected state

## Detecting Data Loss Risks

Scan `upgrade()` function for these dangerous patterns:

```python
# HIGH RISK — data loss
op.drop_column(...)
op.drop_table(...)
op.drop_constraint(...)

# MEDIUM RISK — may fail or truncate data
op.alter_column(..., type_=sa.Integer())  # type change
op.alter_column(..., nullable=False)       # add NOT NULL without default
op.add_column(..., sa.Column('x', sa.String(50)))  # tighter length
```

Always warn the user and offer to:
- Show count of affected rows first
- Dump affected rows to CSV before proceeding
- Suggest a softer alternative (rename column instead of dropping)

## Detecting Irreversible Downgrades

**Red flags in `downgrade()`:**
```python
def downgrade():
    pass  # Empty! Can't undo upgrade
```
```python
def downgrade():
    raise NotImplementedError  # Explicit no-rollback
```

If `upgrade()` drops data but `downgrade()` can't restore it → flag as irreversible.

**Suggested fix:**
- Add data dump to CSV in `upgrade()` before destructive op
- Or add a comment documenting why downgrade isn't possible

## Detecting FK Constraint Violations

When a migration adds a FK constraint:
```python
op.create_foreign_key('fk_user_id', 'orders', 'users', ['user_id'], ['id'])
```

Before applying, check for orphaned rows:
```sql
SELECT COUNT(*) FROM orders
WHERE user_id NOT IN (SELECT id FROM users);
```

If count > 0 → constraint will fail on `upgrade`. Options:
1. Delete orphaned rows (destructive — ask user)
2. Set `user_id = NULL` (if nullable)
3. Create missing parent rows first

## alembic.ini Key Settings

```ini
[alembic]
script_location = alembic          # Where migrations live
sqlalchemy.url = postgresql://...  # DB connection
version_locations = alembic/versions  # Where version files are
```

## Common Error Messages & Meaning

| Error | Meaning |
|-------|---------|
| `FAILED: Multiple head revisions` | Branching conflict — use `alembic merge` |
| `Can't locate revision identified by 'abc'` | Migration file deleted or renamed |
| `Column 'x' already exists` | Schema drift — migration already partially applied |
| `Table 'y' doesn't exist` | Migration dependency out of order or schema drift |
| `IntegrityError: FK constraint failed` | FK violation — orphaned rows exist |

# Migration Conflict Types — Full Catalog

## Tier 1: MVP (Highest Impact)

### 1. Branching / Duplicate Migrations
**What:** Two migration files share the same parent revision, creating a fork in history.
**Why it breaks:** The migration runner can't determine order, refuses to upgrade.
**Detection:** Multiple heads (`alembic heads` > 1 line; Django "multiple leaf nodes" error)
**Auto-fix eligible:** Yes — merge the branches into a single head
**Fix:**
- Alembic: `alembic merge -m "merge" <rev1> <rev2>`
- Django: `manage.py makemigrations --merge --name <name> <app>`

---

### 2. Schema Drift
**What:** Migration history says schema is X, actual DB is Y (column exists when it shouldn't, or missing when it should exist).
**Why it breaks:** Future migrations fail with "already exists" or "doesn't exist" errors.
**Detection:** Compare `alembic_version`/`django_migrations` table against actual DB schema
**Auto-fix eligible:** No — always ask user (risk of data loss or incorrect stamp)
**Fix options:**
1. Stamp revision as applied (if schema already matches): `alembic stamp <rev>`
2. Write a reconciliation migration to bring DB to expected state
3. Manually alter DB to match what migration expects, then re-run

---

### 3. Data Loss — Column/Table Drop
**What:** Migration drops a column or table that contains live data.
**Why it breaks:** Data is permanently lost; no rollback possible after migration runs.
**Detection:** Scan for `op.drop_column`, `op.drop_table`, `RemoveField`, `DeleteModel`
**Auto-fix eligible:** No — always ask user
**Fix options:**
1. Backup data first (`dumpdata`, CSV export, `SELECT INTO`)
2. Rename column to `_deprecated` instead of dropping
3. Proceed with awareness of the data loss

---

### 4. Foreign Key Constraint Violation
**What:** Migration adds FK constraint but existing rows violate it (orphaned rows).
**Why it breaks:** DB rejects the constraint creation; migration fails mid-way.
**Detection:** Query for rows where FK column has no matching parent row
**Auto-fix eligible:** No — data decisions require user input
**Fix options:**
1. Delete orphaned rows (destructive)
2. Set FK column to NULL (if nullable)
3. Create missing parent rows first
4. Disable FK checks temporarily (DB-specific, use carefully)

---

### 5. Irreversible Downgrade
**What:** `downgrade()` (Alembic) or `reverse` (Django) is missing, empty, or uses `noop`.
**Why it breaks:** Can't roll back if migration causes production issues.
**Detection:** Check `downgrade()` is not `pass`/empty; check Django `RunPython` has reverse
**Auto-fix eligible:** Partial — can add a stub with warning comment automatically
**Fix:**
- Add data export in `upgrade()` before destructive operation
- Add proper `downgrade()` that reverses each operation in reverse order
- If truly irreversible, document it explicitly with a comment

---

## Tier 2: Medium Impact (Phase 2)

### 6. Type Conversion Without Data Validation
**What:** Migration changes column type (e.g., `String → Integer`) without checking existing data is compatible.
**Why it breaks:** DB raises `invalid input syntax` error on conversion; migration fails, may leave column in broken state.
**Detection:** Look for `op.alter_column` with type change; check existing data values
**Fix:** Validate data first, then migrate in two steps (add new column, copy+convert, drop old)

---

### 7. NOT NULL Without Default
**What:** Adding a NOT NULL column to a table that already has rows, without a default value.
**Why it breaks:** DB rejects the ALTER TABLE — existing rows can't satisfy NOT NULL.
**Detection:** `op.add_column` with `nullable=False` and no `server_default`
**Fix:** Add with `nullable=True` first, backfill values, then add NOT NULL constraint

---

### 8. Index Conflicts
**What:** Two migrations try to create the same index, or a migration drops a column but leaves its index.
**Why it breaks:** "Index already exists" error, or orphaned index consuming space/causing confusion.
**Detection:** Scan for `op.create_index` with duplicate names; check `op.drop_column` leaves no index behind
**Fix:**
- Duplicate index: add `IF NOT EXISTS` or drop-before-create
- Orphaned index: add `op.drop_index` in same migration as column drop

---

### 9. Stale Migration Stamps
**What:** `alembic_version`/`django_migrations` table references a revision that no longer exists as a file.
**Why it breaks:** Alembic/Django can't locate the current revision; all future operations fail.
**Detection:** Compare migration table entries against actual files in `versions/` or `migrations/`
**Fix (always ask user):**
- Alembic: `alembic stamp <last_valid_rev>` — repoint to nearest valid ancestor
- Django: manually delete ghost row from `django_migrations`, then re-apply

---

## Tier 3: Edge Cases (Phase 3)

### 10. Concurrent Migration Execution
**What:** Multiple app instances run migrations simultaneously (common in container deployments).
**Why it breaks:** Table locks, partial applies, race conditions in `alembic_version` update.
**Detection:** Check if migration table has a locking mechanism; look for multi-instance setup
**Fix:** Use Alembic's `with_for_update()` locking or distribute via migration lock table

### 11. Cross-Environment Schema Mismatch
**What:** Migration works in dev (empty table) but fails in prod (millions of rows, different indexes).
**Why it breaks:** Long-running locks, timeouts, memory issues, or dialect-specific syntax gaps.
**Detection:** Check table size before migration; flag ALTER TABLE on large tables
**Fix:** Use concurrent index creation (`CREATE INDEX CONCURRENTLY`), batched updates, zero-downtime migration patterns

### 12. Missing Extension / Dialect Feature
**What:** Migration uses PostgreSQL-specific syntax (e.g., `uuid_generate_v4()`) but target is MySQL or SQLite.
**Why it breaks:** SQL syntax error on non-supported DB.
**Detection:** Check dialect-specific operations against `sqlalchemy.url` or Django `DATABASES` setting
**Fix:** Use SQLAlchemy dialect-agnostic types, or add a dialect check in migration

---

## Risk Classification Summary

| Risk | Auto-Apply | Ask First | Description |
|------|-----------|-----------|-------------|
| Rename/reorder migrations | ✅ | — | No data impact |
| Merge branch heads | ✅ | — | Creates new merge file |
| Alembic stamp | — | ✅ | Changes version tracking |
| Add column (nullable) | ✅ | — | Safe, non-breaking |
| Add NOT NULL column | — | ✅ | Breaks existing rows |
| Drop column | — | ✅ | Permanent data loss |
| Drop table | — | ✅ | Permanent data loss |
| Type change | — | ✅ | May corrupt data |
| Create FK constraint | — | ✅ | May fail on orphaned rows |
| Delete orphaned rows | — | ✅ | Data loss |
| Stamp revision | — | ✅ | Tracks state incorrectly if wrong |
| Any RunSQL/RunPython | — | ✅ | Unpredictable side effects |

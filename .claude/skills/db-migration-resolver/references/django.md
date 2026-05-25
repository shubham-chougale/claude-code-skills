# Django Migration Reference

## Key CLI Commands

```bash
python manage.py showmigrations              # List all apps and their migrations + applied status
python manage.py showmigrations --list       # Same, formatted as list
python manage.py migrate                     # Apply all pending migrations
python manage.py migrate <app> <migration>   # Migrate to a specific state
python manage.py migrate <app> zero          # Roll back all migrations for an app
python manage.py makemigrations              # Auto-generate new migrations from model changes
python manage.py makemigrations --check      # Check if migrations needed (exit 1 if yes)
python manage.py sqlmigrate <app> <name>     # Show the SQL a migration would run
python manage.py squashmigrations <app> <from> <to>  # Squash migrations into one
python manage.py showmigrations --plan       # Show full dependency tree
```

## Migration File Structure

Located in `<app>/migrations/` within each Django app.

```python
# Example Django migration
from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),     # (app_label, migration_name)
        ('products', '0003_add_sku'),  # Can depend on multiple apps
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(max_length=20, default='pending'),
        ),
    ]
```

## Detecting Branching Conflicts

**Symptom:** `manage.py migrate` fails with "inconsistent migration history" or "leaf nodes" error.

**Detection:**
1. For each app, find migrations with no other migration depending on them → these are "leaves"
2. If an app has more than one leaf → branching conflict

```bash
python manage.py showmigrations --plan 2>&1 | grep -E "\[X\]|\[ \]"
```

**Example conflict:**
```
users
 [X] 0001_initial
 [X] 0002_add_email       ← branch A
 [ ] 0002_add_phone       ← branch B (same number! conflict)
```

**Fix: Create a merge migration**
```bash
python manage.py makemigrations --merge --name merge_email_phone users
# Creates: users/migrations/0003_merge_email_phone.py
```

Django's merge migration has both conflicting migrations in `dependencies`.

## Detecting Schema Drift

**Symptom:** `makemigrations --check` exits 1 (model changes not reflected in migrations).

**Detection approach:**
1. Run `manage.py showmigrations` — check for `[ ]` (unapplied) migrations
2. Run `manage.py makemigrations --check` — if exit code 1, models have drifted from migrations
3. Run `manage.py migrate --run-syncdb` (dev only) to see what SQL would sync

**Common causes:**
- Model fields changed without running `makemigrations`
- Migration file manually deleted
- DB table modified directly with raw SQL
- Copied DB from different environment

**Fix options (always ask user):**
1. Run `makemigrations` to generate the missing migration
2. `manage.py migrate --fake <app> <migration>` — mark as applied without running (risky)
3. Write manual migration to reconcile discrepancy

## Detecting Data Loss Risks

Scan migration `operations` list for dangerous patterns:

```python
# HIGH RISK — data loss
migrations.DeleteModel(name='OldTable')
migrations.RemoveField(model_name='user', name='legacy_id')

# MEDIUM RISK — may fail or silently truncate
migrations.AlterField(  # type change
    model_name='product',
    name='price',
    field=models.IntegerField()  # was DecimalField
)
migrations.AlterField(  # removing null=True
    model_name='user',
    name='phone',
    field=models.CharField(max_length=20)  # was null=True
)
```

Before applying:
- Show row count for affected table/field
- Offer to dump to CSV: `python manage.py dumpdata <app.Model> > backup.json`
- Suggest `RemoveField` alternative: rename to `legacy_phone` and deprecate

## Detecting FK Constraint Violations

Django enforces FK at DB level. When a migration adds a ForeignKey:

```python
migrations.AddField(
    model_name='order',
    name='user',
    field=models.ForeignKey('users.User', on_delete=models.CASCADE)
)
```

Check for orphaned rows before applying:
```python
# In Django shell: python manage.py shell
Order.objects.exclude(user_id__in=User.objects.values('id')).count()
```

If count > 0 → migration will fail. Options:
1. Delete orphaned rows
2. Point orphans to a default user
3. Add `null=True` to the FK first, set values, then make NOT NULL in next migration

## Detecting Irreversible Downgrades

**Red flag:** `RunSQL` in operations without a reverse SQL:
```python
migrations.RunSQL(
    sql="ALTER TABLE users DROP COLUMN legacy_id",
    reverse_sql=migrations.RunSQL.noop  # Can't undo!
)
```

Also check `RunPython` operations — if the Python function doesn't have a `reverse` parameter:
```python
migrations.RunPython(populate_slugs)          # No reverse — can't undo!
migrations.RunPython(populate_slugs, undo_slugs)  # OK — has reverse
```

## `django_migrations` Table

Django tracks applied migrations in this table:
```sql
SELECT app, name, applied FROM django_migrations ORDER BY applied;
```

If a migration file exists but has no row in `django_migrations` → unapplied.
If a row exists but file is gone → "ghost migration" — causes errors on new `migrate` calls.

**Ghost migration fix (ask user first):**
```bash
python manage.py migrate --fake <app> <migration>  # Mark as applied without running
```

## Common Error Messages & Meaning

| Error | Meaning |
|-------|---------|
| `InconsistentMigrationHistory` | Applied migrations have missing dependencies |
| `NodeNotFoundError` | Migration file referenced but doesn't exist |
| `Multiple leaf nodes` | Branching conflict — use `makemigrations --merge` |
| `MigrationSchemaMissing` | `django_migrations` table missing — run `migrate` first |
| `IntegrityError: NOT NULL constraint` | Adding NOT NULL column without default |
| `ValueError: Cannot alter` | Trying to change field type with incompatible data |

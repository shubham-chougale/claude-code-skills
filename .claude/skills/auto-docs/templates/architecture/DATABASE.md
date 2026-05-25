---
last_updated: {{DATE}}
changed: Initial document created
updated_by: Backend Lead
sprint: 1
---

# Database Design — {{PROJECT_NAME}}

> View ERD Diagram → [erd.html](../diagrams/erd.html)

## Database

**Type:** {{DB_TYPE}} (e.g. PostgreSQL 15)
**ORM / Migration Tool:** {{ORM}} (e.g. Alembic / Django Migrations / Prisma)

## Schema Overview

```
users
  └── has many → sessions
  └── has many → [resource]

[resource]
  └── belongs to → users
  └── has many → [sub-resource]
```

---

## Tables

### users

| Column | Type | Nullable | Default | Description |
|--------|------|----------|---------|-------------|
| id | UUID | No | gen_random_uuid() | Primary key |
| email | VARCHAR(255) | No | — | Unique. Indexed. |
| password_hash | VARCHAR(255) | No | — | bcrypt hash |
| name | VARCHAR(100) | No | — | Display name |
| is_verified | BOOLEAN | No | false | Email verified |
| is_locked | BOOLEAN | No | false | Account locked |
| failed_attempts | INTEGER | No | 0 | Failed login count |
| created_at | TIMESTAMP | No | now() | Creation time |
| updated_at | TIMESTAMP | No | now() | Last update time |

**Indexes:**
- `users_email_idx` — UNIQUE on `email`

---

### sessions

| Column | Type | Nullable | Default | Description |
|--------|------|----------|---------|-------------|
| id | UUID | No | gen_random_uuid() | Primary key |
| user_id | UUID | No | — | FK → users.id |
| refresh_token | VARCHAR(500) | No | — | Hashed refresh token |
| expires_at | TIMESTAMP | No | — | Token expiry |
| created_at | TIMESTAMP | No | now() | Session created |

**Indexes:**
- `sessions_user_id_idx` — on `user_id`
- `sessions_refresh_token_idx` — UNIQUE on `refresh_token`

**Foreign Keys:**
- `user_id` → `users.id` ON DELETE CASCADE

---

### [table_name]

| Column | Type | Nullable | Default | Description |
|--------|------|----------|---------|-------------|
| id | UUID | No | gen_random_uuid() | Primary key |
| [column] | [type] | [yes/no] | [default] | [description] |
| created_at | TIMESTAMP | No | now() | — |

---

## Migration History

| Migration | Date | Change |
|-----------|------|--------|
| 001_initial_schema | {{DATE}} | Create users and sessions tables |

---
*Owner: Backend Lead — auto-updated when migration files are committed. Verify table definitions after each update.*

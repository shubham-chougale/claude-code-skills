---
last_updated: {{DATE}}
changed: Initial document created
updated_by: Tech Lead
sprint: 1
---

# Local Development Setup — {{PROJECT_NAME}}

This guide gets you from zero to a running local environment. Follow steps in order. If something fails, check the Troubleshooting section at the bottom before asking for help.

## Prerequisites

Install these before starting:

| Tool | Version | Install |
|------|---------|---------|
| [Node.js / Python / etc.] | [version] | [link or command] |
| [Database, e.g. PostgreSQL] | [version] | [link or command] |
| [Docker] | Latest | [link] |
| [Other tool] | [version] | [link] |

## 1. Clone the Repository

```bash
git clone [repository URL]
cd {{PROJECT_NAME}}
```

## 2. Install Dependencies

```bash
[install command — e.g. npm install / pip install -r requirements.txt]
```

## 3. Set Up Environment Variables

```bash
cp .env.example .env
```

Open `.env` and fill in the required values:

| Variable | Description | Where to Get It |
|----------|-------------|-----------------|
| `DATABASE_URL` | PostgreSQL connection string | Set up locally or use Docker |
| `JWT_SECRET` | Secret key for JWT signing | Generate: `openssl rand -hex 32` |
| `[VAR_NAME]` | [Description] | [Where to get the value] |

## 4. Set Up Database

```bash
# Start the database (if using Docker)
docker-compose up -d db

# Run migrations
[migration command]

# Seed with development data (optional)
[seed command]
```

## 5. Start the Development Server

```bash
[start command — e.g. npm run dev / python manage.py runserver]
```

The app runs at: `http://localhost:[PORT]`

## 6. Verify Setup

Open your browser and go to `http://localhost:[PORT]`. You should see [describe what a working local app looks like].

## Running Tests

```bash
# Unit tests
[test command]

# With coverage
[coverage command]

# E2E tests (requires running app)
[e2e command]
```

## Troubleshooting

**Port already in use:**
```bash
lsof -ti:[PORT] | xargs kill -9
```

**Database connection refused:**
Make sure PostgreSQL is running: `docker-compose ps`

**Migration errors:**
```bash
[rollback command]
[migrate fresh command]
```

**[Other common issue]:**
[Solution]

---
*Owner: Tech Lead — auto-updated when dependencies or environment variables change. Verify steps after each update.*

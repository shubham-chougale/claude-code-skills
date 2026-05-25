---
last_updated: {{DATE}}
changed: Initial document created
updated_by: DevOps
sprint: 2
---

# Rollback Plan — {{PROJECT_NAME}}

**Read this document before every production deployment.**

If a deployment goes wrong, execute the steps below immediately. Do not investigate first — rollback first, investigate after the system is stable.

## Decision Threshold

Rollback immediately if any of the following are true within 15 minutes of deployment:

- [ ] Error rate exceeds 5% (baseline: <0.5%)
- [ ] API response time exceeds 2 seconds at p95 (baseline: <500ms)
- [ ] Health check endpoint returns non-200
- [ ] Any P0 bug is reported by a user
- [ ] Database connection errors in logs

## Rollback Steps

### Step 1 — Alert the Team

Notify in [Slack channel / Teams channel]: "Rolling back [version] deploy. ETA stable: [X] minutes."

### Step 2 — Rollback the Application

```bash
# Option A — Redeploy the previous version
[command to deploy previous version tag]

# Option B — Revert to last known good container image
[docker / kubectl rollout undo command]

# Option C — [Platform-specific rollback]
[command]
```

### Step 3 — Rollback Database Migrations (if needed)

Only do this if the deployment included a migration AND it caused the issue.

```bash
# Check current migration state
[show current migration command]

# Rollback one migration
[rollback command]

# Verify schema is back to expected state
[verification command]
```

**Warning:** Rolling back migrations that deleted data is not possible. If data was deleted by a migration, escalate to Tech Lead immediately.

### Step 4 — Verify Rollback Succeeded

- [ ] Health check returns 200: `GET /health`
- [ ] Error rate returns to baseline
- [ ] Login flow works
- [ ] Notify team: "Rollback complete. System stable."

### Step 5 — Post-Rollback

- Do NOT redeploy the same code without identifying and fixing the root cause
- File a P0 bug ticket with the deployment details and error logs
- Schedule a postmortem within 24 hours

## Contact List

| Role | Name | Contact |
|------|------|---------|
| DevOps On-Call | [Name] | [Phone / Slack] |
| Tech Lead | [Name] | [Phone / Slack] |
| Engineering Manager | [Name] | [Phone / Slack] |

---
*Owner: DevOps — update when the deployment process changes. Read before every production deploy.*

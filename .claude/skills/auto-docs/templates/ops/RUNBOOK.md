---
last_updated: {{DATE}}
changed: Initial document created
updated_by: DevOps / Backend Lead
sprint: 0 (pre-launch)
---

# Runbook — {{PROJECT_NAME}}

This document is for whoever is on-call. It covers common operational tasks, known issues, and how to resolve them. If you're reading this under pressure, start at the issue that matches your alert.

## On-Call Contacts

| Role | Name | Contact |
|------|------|---------|
| Primary On-Call | [Name] | [Phone / Slack] |
| Backup On-Call | [Name] | [Phone / Slack] |
| Tech Lead | [Name] | [Phone / Slack] |
| Engineering Manager | [Name] | [Phone / Slack] |

## System Health Checks

Run these to get a quick read on system state:

```bash
# Application health
curl https://{{PROJECT_NAME}}.com/health

# Check error rate (last 15 min)
[monitoring command or dashboard link]

# Check database connections
[db connection check command]

# Check active processes
[process check command]
```

## Common Issues and Fixes

### High Error Rate (>5%)

**Symptoms:** Error rate alert fires. Users report failures.

1. Check recent deployments — was anything deployed in the last 2 hours?
2. If yes → execute [ROLLBACK.md](../deployment/ROLLBACK.md)
3. If no → check application logs:
   ```bash
   [log command — e.g. kubectl logs / aws logs]
   ```
4. Look for the most common error. Match to the issues below.

---

### Database Connection Errors

**Symptoms:** `ECONNREFUSED` or `too many connections` in logs.

```bash
# Check active connections
[db connections query]

# Restart connection pool (no data loss)
[restart command]

# If above fails, restart the app server
[app restart command]
```

If connections are maxed out but app is healthy — scale the connection pool in INFRA.md and redeploy.

---

### High Memory Usage

**Symptoms:** Memory usage >90%. App slows down or crashes.

```bash
# Check memory usage
[memory check command]

# Restart app instance (brief downtime ~10s)
[restart command]
```

If this recurs more than once a week, file a P2 bug for memory leak investigation.

---

### Slow API Responses (>2s at p95)

1. Check database query performance in [monitoring dashboard]
2. Check if a specific endpoint is slow or all endpoints
3. Check for a recent deploy that changed queries
4. If a new deploy → consider rolling back
5. If ongoing → check DB indexes, connection pool size

---

### Scheduled Job Failures

**Job name:** [Job name]
**Schedule:** [e.g. Every day at 02:00 UTC]

```bash
# Check last run status
[job status command]

# Manually trigger the job
[manual trigger command]

# Check job logs
[job logs command]
```

---

## Restart Procedures

### Restart Application (no data loss)

```bash
[rolling restart command]
```
Downtime: ~0 seconds (rolling restart)

### Restart Database (last resort)

```bash
[db restart command]
```
Downtime: ~30 seconds. Confirm with Tech Lead before doing this.

## Escalation Path

```
Alert fires
    ↓
Primary on-call investigates (15 min)
    ↓
Cannot resolve → call Backup on-call
    ↓
Still unresolved → call Tech Lead
    ↓
User impact >30 min → notify Engineering Manager
```

---
*Owner: DevOps / Backend Lead — add new entries after every incident. Review monthly.*

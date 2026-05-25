---
last_updated: {{DATE}}
changed: Initial document created
updated_by: DevOps / Tech Lead
sprint: 0 (pre-launch)
---

# Incident Response — {{PROJECT_NAME}}

## Incident Severity Levels

| Level | Definition | Response Time | Example |
|-------|-----------|---------------|---------|
| SEV-1 | Complete outage. All users affected. Data loss risk. | Immediate | App down, DB unreachable |
| SEV-2 | Core feature broken. Most users affected. | Within 30 min | Login broken, payments failing |
| SEV-3 | Non-critical feature broken. Workaround exists. | Within 2 hours | Export fails, email delay |
| SEV-4 | Minor issue. Small subset of users affected. | Next business day | UI glitch on edge case |

## Who to Contact

| Role | Name | Phone | Slack | When to Call |
|------|------|-------|-------|--------------|
| Primary On-Call | [Name] | [Phone] | [@handle] | Always first |
| Backup On-Call | [Name] | [Phone] | [@handle] | Primary unreachable |
| Tech Lead | [Name] | [Phone] | [@handle] | SEV-1 or SEV-2 |
| Engineering Manager | [Name] | [Phone] | [@handle] | SEV-1 lasting >30 min |
| CEO / Leadership | [Name] | [Phone] | [@handle] | SEV-1 lasting >1 hour |

## Incident Response Steps

### 1. Detect and Acknowledge (0–5 min)

- Alert fires in [PagerDuty / OpsGenie / Slack]
- On-call acknowledges within 5 minutes
- Post in [#incidents Slack channel]: "Investigating [alert name]. ETA update: 15 min."

### 2. Assess Severity (5–10 min)

- Determine SEV level using the table above
- If SEV-1 or SEV-2: start a war room call immediately
- Assign incident commander (usually the Tech Lead)

### 3. Communicate (ongoing)

Post status updates every 15 minutes in [#incidents]:
```
[HH:MM] Status: Investigating database connection errors.
Users affected: ~500. ETA resolution: 30 min.
```

Update the status page at [link] if user-facing.

### 4. Resolve

Follow the relevant section in [RUNBOOK.md](RUNBOOK.md).
If a deploy caused the incident: execute [ROLLBACK.md](../deployment/ROLLBACK.md).

### 5. All-Clear (immediately after resolution)

Post in [#incidents]: "Incident resolved at [time]. Root cause: [one sentence]. Postmortem scheduled: [date]."
Update status page to "All systems operational."

### 6. Postmortem (within 24 hours)

Create a postmortem file at `/docs/ops/postmortems/YYYY-MM-DD-incident-name.md`.
Use the template in [POSTMORTEM.md](POSTMORTEM.md).

---
*Owner: DevOps / Tech Lead — update when escalation paths or contacts change.*

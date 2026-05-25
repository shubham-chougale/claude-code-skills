---
last_updated: {{DATE}}
changed: Initial document created
updated_by: DevOps
sprint: 0 (pre-launch)
---

# Monitoring & Alerting — {{PROJECT_NAME}}

## Monitoring Stack

| Tool | Purpose | Dashboard |
|------|---------|-----------|
| [e.g. Datadog / Grafana] | APM + metrics | [link] |
| [e.g. Sentry] | Error tracking | [link] |
| [e.g. Uptime Robot / Pingdom] | Uptime monitoring | [link] |
| [e.g. CloudWatch] | Infrastructure metrics | [link] |

## Key Metrics and Baselines

| Metric | Healthy Baseline | Warning Threshold | Critical Threshold |
|--------|-----------------|-------------------|-------------------|
| Error rate | <0.5% | >2% | >5% |
| API response time (p95) | <500ms | >1s | >2s |
| Database response time | <100ms | >500ms | >1s |
| Memory usage | <70% | >80% | >90% |
| CPU usage | <60% | >75% | >90% |
| Uptime | 99.9% | <99.5% | <99% |

## Alerts

| Alert Name | Condition | Severity | Notifies |
|-----------|-----------|----------|----------|
| High Error Rate | Error rate >5% for 2 min | SEV-1 | PagerDuty → On-call |
| Slow API | p95 >2s for 5 min | SEV-2 | Slack #alerts |
| High Memory | Memory >90% for 5 min | SEV-2 | Slack #alerts |
| DB Connection Errors | >10 errors/min | SEV-1 | PagerDuty → On-call |
| Uptime Check Failed | Health check fails 3 times | SEV-1 | PagerDuty → On-call |
| Disk Usage High | Disk >85% | SEV-3 | Slack #alerts |

## Alert Routing

```
SEV-1 → PagerDuty → On-call phone call
SEV-2 → Slack #alerts + PagerDuty push notification
SEV-3 → Slack #alerts only
SEV-4 → Weekly digest
```

## Log Locations

| Log Type | Location | Retention |
|----------|----------|-----------|
| Application logs | [CloudWatch / Datadog / ELK] | 30 days |
| Access logs | [S3 / CloudWatch] | 90 days |
| Error logs | Sentry | 90 days |
| Audit logs | [S3] | 1 year |

## Dashboard Links

| Dashboard | URL | Shows |
|-----------|-----|-------|
| Main overview | [link] | All key metrics |
| API performance | [link] | Response times, error rates by endpoint |
| Database | [link] | Query performance, connections |
| Infrastructure | [link] | CPU, memory, disk per server |

## On-Call Rotation

**Tool:** [PagerDuty / OpsGenie]
**Rotation:** [Weekly / Bi-weekly]
**Schedule:** [link to schedule]

---
*Owner: DevOps — update when monitoring tools, thresholds, or alert routing changes.*

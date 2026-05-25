---
last_updated: {{DATE}}
changed: Initial document created
updated_by: DevOps
sprint: 2
---

# Infrastructure — {{PROJECT_NAME}}

> View Deployment Topology → [deployment-topology.html](../diagrams/deployment-topology.html)

## Cloud Provider

**Provider:** [AWS / GCP / Azure / DigitalOcean]
**Region:** [e.g. us-east-1]
**Account ID:** [Stored in secrets manager — never in this doc]

## Architecture Overview

```
[Internet]
    ↓
[CDN — e.g. CloudFront]
    ↓
[Load Balancer]
    ↓
[App Servers — e.g. EC2 / ECS / GKE]
    ↓
[Database — e.g. RDS PostgreSQL]
[Cache — e.g. ElastiCache Redis]
[Storage — e.g. S3]
```

## Services

| Service | Type | Spec | Region | Purpose |
|---------|------|------|--------|---------|
| [App Server] | [EC2 / ECS / K8s] | [t3.medium / 2CPU 4GB] | us-east-1 | Run application |
| [Database] | [RDS PostgreSQL] | [db.t3.medium] | us-east-1 | Primary database |
| [Cache] | [ElastiCache Redis] | [cache.t3.micro] | us-east-1 | Session + caching |
| [Storage] | [S3] | Standard | us-east-1 | File storage |
| [CDN] | [CloudFront] | — | Global | Static asset serving |

## Environment Configuration

| Variable | Staging | Production |
|----------|---------|------------|
| App Instances | 1 | 2–4 (auto-scaled) |
| Database Connections | 20 | 100 |
| Cache Memory | 512MB | 2GB |
| Log Level | DEBUG | ERROR |

## Networking

- **VPC:** [VPC ID or name]
- **Subnets:** Public (load balancer) + Private (app + database)
- **Security Groups:** App allows 443 inbound from LB only. DB allows 5432 from app only.
- **SSL:** Certificates managed via [ACM / Let's Encrypt]

## Access and Credentials

All credentials are stored in [AWS Secrets Manager / Vault / Parameter Store]. Access requires [IAM role / VPN + MFA].

To access staging:
```bash
[SSH command or kubectl command]
```

## Monitoring

See [MONITORING.md](../ops/MONITORING.md) for dashboards and alert configurations.

## Cost

| Service | Monthly Estimate |
|---------|-----------------|
| [App Server] | $[X] |
| [Database] | $[X] |
| [Cache] | $[X] |
| Total | $[X] |

---
*Owner: DevOps — update when infrastructure changes are applied.*

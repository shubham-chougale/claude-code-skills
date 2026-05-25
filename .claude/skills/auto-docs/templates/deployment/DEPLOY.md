---
last_updated: {{DATE}}
changed: Initial document created
updated_by: DevOps
sprint: 2
---

# Deployment Guide — {{PROJECT_NAME}}

> View Deployment Topology → [deployment-topology.html](../diagrams/deployment-topology.html)
> View CI/CD Pipeline → [cicd-pipeline.html](../diagrams/cicd-pipeline.html)

## Pre-Deployment Checklist

Run through this before every deployment:

- [ ] All tests passing in CI
- [ ] Staging environment tested and signed off
- [ ] Database migrations reviewed
- [ ] Rollback plan reviewed → [ROLLBACK.md](ROLLBACK.md)
- [ ] On-call engineer notified
- [ ] Deployment window confirmed (avoid peak hours)

## Environments

| Environment | Deploy Branch | URL | Who Deploys |
|-------------|--------------|-----|-------------|
| Staging | `staging` | staging.{{PROJECT_NAME}}.com | Automatic via CI |
| Production | `main` | {{PROJECT_NAME}}.com | Manual trigger |

## Deploy to Staging

Staging deploys automatically on every merge to the `staging` branch. No manual action needed.

To force a staging deploy:
```bash
git checkout staging
git merge develop
git push origin staging
```

## Deploy to Production

```bash
# Step 1 — Ensure you are on main and it is up to date
git checkout main
git pull origin main

# Step 2 — Run migrations (if any)
[migration command for {{STACK}}]

# Step 3 — Deploy
[deploy command — e.g. kubectl apply / terraform apply / eb deploy]

# Step 4 — Verify deployment
[health check command or URL]

# Step 5 — Monitor for 15 minutes
Watch error rates and response times in [monitoring dashboard link]
```

## Post-Deployment Verification

After every production deploy, verify:

1. [ ] Health check endpoint returns 200: `GET /health`
2. [ ] Login flow works end-to-end
3. [ ] [Key feature 1] works correctly
4. [ ] Error rate is below baseline in monitoring
5. [ ] Response times are within expected range

If any check fails → execute [ROLLBACK.md](ROLLBACK.md) immediately.

## Deployment Log

| Date | Version | Deployed By | Status | Notes |
|------|---------|-------------|--------|-------|
| {{DATE}} | v0.1.0 | [Name] | Success | Initial deployment |

---
*Owner: DevOps — update when the deployment process or infrastructure changes.*

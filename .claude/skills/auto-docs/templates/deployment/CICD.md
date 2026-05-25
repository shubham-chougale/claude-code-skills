---
last_updated: {{DATE}}
changed: Initial document created
updated_by: DevOps
sprint: 2
---

# CI/CD Pipeline — {{PROJECT_NAME}}

> View Pipeline Diagram → [cicd-pipeline.html](../diagrams/cicd-pipeline.html)

## Pipeline Overview

```
Code pushed
    ↓
[CI Tool — e.g. GitHub Actions / GitLab CI / Jenkins]
    ↓
Build → Test → Lint → Security Scan
    ↓ (if passing)
Deploy to Staging (automatic on staging branch)
    ↓
Deploy to Production (manual trigger on main branch)
```

## CI Tool

**Platform:** [GitHub Actions / GitLab CI / CircleCI / Jenkins]
**Config file:** `.github/workflows/ci.yml` or equivalent

## Pipeline Stages

| Stage | Trigger | Runs On | Approx. Time | Blocks Deploy |
|-------|---------|---------|--------------|---------------|
| Build | Every push | All branches | ~2 min | Yes |
| Unit Tests | Every push | All branches | ~3 min | Yes |
| Integration Tests | PR only | PR branches | ~5 min | Yes |
| Lint | Every push | All branches | ~1 min | Yes |
| Security Scan | PR only | PR branches | ~3 min | Yes |
| Deploy Staging | Merge to staging | staging branch | ~4 min | — |
| Deploy Production | Manual trigger | main branch | ~5 min | — |

## Stage Definitions

### Build
Compiles the application and checks for build errors.
```yaml
# [Paste relevant CI config snippet here]
```

### Unit Tests
Runs all unit tests. Coverage must meet the 80% threshold.
```yaml
# [Paste relevant CI config snippet here]
```

### Deploy Staging
Automatic deployment to staging on every merge to the `staging` branch. No approval required.

### Deploy Production
Manual trigger only. Requires:
- All CI stages green
- At least one team lead approval in the GitHub Actions UI

## Secrets and Environment Variables

Secrets are stored in [GitHub Secrets / AWS Secrets Manager / Vault]. Never commit secrets to the repository.

| Secret Name | Used By | Who Manages It |
|-------------|---------|----------------|
| `DATABASE_URL` | App | DevOps |
| `JWT_SECRET` | App | DevOps |
| `[SECRET_NAME]` | [Stage] | [Owner] |

## Failure Handling

If any stage fails:
- PR is blocked from merging
- Developer who triggered the failure is notified via [Slack / email]
- Check the CI logs in [link to CI platform]

## Pipeline Change Log

| Date | Change | Changed By |
|------|--------|------------|
| {{DATE}} | Initial pipeline setup | DevOps |

---
*Owner: DevOps — update when pipeline stages, tools, or configuration changes.*

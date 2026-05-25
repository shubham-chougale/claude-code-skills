---
last_updated: {{DATE}}
changed: Initial document created
updated_by: QA Lead
sprint: 1
---

# Test Plan — {{PROJECT_NAME}}

## Scope

This plan covers testing for {{PROJECT_NAME}} across all feature areas. It defines what gets tested, how, with which tools, and what "passing" means for each level.

## Testing Levels

| Level | What It Tests | Tool | Who Runs It | When |
|-------|--------------|------|-------------|------|
| Unit | Individual functions | {{UNIT_TEST_TOOL}} | Developer | On every commit |
| Integration | Services + database | {{UNIT_TEST_TOOL}} | Developer | On every PR |
| E2E | Full user flows | {{E2E_TOOL}} | QA + CI | On every PR to staging |
| Performance | Load and response times | [k6 / Locust / JMeter] | QA | Before each release |
| UAT | Business scenarios | Manual | Stakeholders | Before release |

## Test Environments

| Environment | URL | Database | Purpose |
|-------------|-----|----------|---------|
| Local | localhost | Local / Docker | Developer testing |
| Staging | staging.{{PROJECT_NAME}}.com | Staging DB | QA + UAT |
| Production | {{PROJECT_NAME}}.com | Production DB | Live |

## Coverage Targets

| Layer | Minimum Coverage |
|-------|-----------------|
| Unit tests | 80% |
| Integration tests | Key happy paths + all error paths |
| E2E tests | All critical user journeys |

## Feature Test Coverage

| Feature Area | Unit | Integration | E2E | Status |
|-------------|------|-------------|-----|--------|
| Authentication | Required | Required | Required | Pending |
| [Feature 2] | Required | Required | Required | Pending |
| [Feature 3] | Required | Optional | Required | Pending |

## Entry and Exit Criteria

**Entry Criteria (before testing begins):**
- Feature code merged to staging branch
- All unit tests passing
- No P0 or P1 bugs open from previous cycle

**Exit Criteria (before release):**
- All test cases executed
- No P0 bugs open
- No P1 bugs open without approved waiver
- UAT sign-off received
- Performance benchmarks met

## Defect Priority

| Priority | Definition | Resolution Time |
|----------|-----------|----------------|
| P0 | System down, data loss, security breach | Fix before release |
| P1 | Core feature broken, no workaround | Fix before release |
| P2 | Core feature broken, workaround exists | Fix within 2 sprints |
| P3 | Minor issue, cosmetic | Fix when capacity allows |

---
*Owner: QA Lead — update when a new major feature area is added to the project.*

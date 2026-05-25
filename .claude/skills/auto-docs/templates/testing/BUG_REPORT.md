---
last_updated: {{DATE}}
changed: Initial document created
updated_by: QA Lead
sprint: 0
---

# Bug Report Template — {{PROJECT_NAME}}

Copy the template below when filing a new bug. File one bug per report. Incomplete reports will be returned for more detail.

---

## Bug Report Template

```
## Bug ID: BUG-[NUMBER]

**Title:** [One line summary — be specific. Bad: "Login broken". Good: "Login fails with 500 error when email contains plus sign"]

**Reported By:** [Name]
**Date:** [YYYY-MM-DD]
**Sprint:** [Sprint number]
**Priority:** P0 / P1 / P2 / P3
**Status:** Open / In Progress / Fixed / Verified / Closed

---

### Environment

- **Platform:** Web / iOS / Android
- **Browser / OS:** [e.g. Chrome 124, macOS 14.4]
- **App Version / Build:** [e.g. v1.2.0, build 204]
- **Environment:** Local / Staging / Production

---

### Steps to Reproduce

1. [Step 1 — be exact. What URL, what data, what action]
2. [Step 2]
3. [Step 3]

### Expected Result

[What should happen based on the requirements or design]

### Actual Result

[What actually happened. Include error message verbatim if shown.]

### Screenshot / Video

[Attach file or paste link]

### Logs / Console Output

[Paste relevant error logs here. Remove sensitive data first.]

---

### Additional Context

[Any other information: how often does it happen, specific data that triggers it, regression or new bug, related tickets]

### Fix Notes (filled by developer)

[What was changed to fix this and why]

### Verified By

[QA name + date after confirming the fix]
```

---

## Priority Definitions

| Priority | Criteria |
|----------|----------|
| P0 | System down, data loss, or security breach |
| P1 | Core feature broken with no workaround |
| P2 | Core feature broken with workaround available |
| P3 | Minor issue, cosmetic, or low-usage path |

---
*This template is set once at project start. File individual bugs using the template above.*

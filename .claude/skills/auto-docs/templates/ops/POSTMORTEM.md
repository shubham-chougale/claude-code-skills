---
last_updated: {{DATE}}
changed: Template created
updated_by: Tech Lead
sprint: 0
---

# Postmortem Template — {{PROJECT_NAME}}

Copy and rename this file as: `YYYY-MM-DD-incident-name.md`
Fill in all sections within 24 hours of resolution. Do not edit after publishing.

---

# Postmortem: [Incident Name]

**Date:** [YYYY-MM-DD]
**Duration:** [HH:MM] — [HH:MM] ([X] hours [Y] minutes)
**Severity:** SEV-[1/2/3]
**Status:** Resolved

**Author:** [Name]
**Reviewers:** [Name, Name]

---

## What Happened

[2–4 sentences. What was broken, who was affected, and how it was discovered. No blame. Just facts.]

## Impact

- **Users affected:** [X users / All users / % of users]
- **Features broken:** [List what stopped working]
- **Data affected:** [Yes — describe / No]
- **Revenue impact:** [$ estimate if applicable / N/A]

## Timeline

All times in UTC.

| Time | Event |
|------|-------|
| HH:MM | Alert fired / Issue first noticed |
| HH:MM | On-call engineer acknowledged |
| HH:MM | Root cause identified |
| HH:MM | Fix deployed |
| HH:MM | System confirmed stable |
| HH:MM | Incident closed |

## Root Cause

[One paragraph. The specific, technical reason the incident happened. Avoid "human error" as a root cause — find the underlying system or process failure that allowed the error to have impact.]

## What Went Wrong

[Bullet list of things that failed or were missing that contributed to the incident.]

- [Thing 1]
- [Thing 2]

## What Went Well

[Bullet list of things that worked during the incident — fast detection, good communication, effective tooling, etc.]

- [Thing 1]
- [Thing 2]

## Action Items

These must be filed as tickets and assigned before this document is published.

| Action | Owner | Priority | Ticket | Due |
|--------|-------|----------|--------|-----|
| [Preventive action 1] | [Name] | P1/P2 | [Ticket ID] | [Date] |
| [Preventive action 2] | [Name] | P1/P2 | [Ticket ID] | [Date] |

---
*This file is written once and never edited after the review period ends.*

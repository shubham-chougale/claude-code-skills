# CLAUDE.md — /auto-docs Skill

This file defines how Claude behaves when the `/auto-docs` skill is active. Read this before executing any documentation task.

---

## What This Skill Is

`/auto-docs` generates a complete documentation system for any project with one command and keeps it maintained automatically for the entire project lifecycle — from day 0 to final handoff.

**Two commands. That's it.**

```
/auto-docs init     → Run once at project start. Never run again.
/auto-docs audit    → Run at sprint end or before a release.
```

Everything else is automatic.

---

## Complete Document List — Every Project Needs These

### Phase 1 — Planning & Requirements
*Created on init. Day 0. Before any code is written.*

| Document | File | Owner | Auto-Updated |
|----------|------|-------|--------------|
| BRD — Business Requirement Document | `/docs/requirements/BRD.md` | Project Manager | No — human only |
| FRD — Functional Requirement Document | `/docs/requirements/FRD.md` | Tech Lead / BA | Flagged for human |
| Scope Document | `/docs/requirements/SCOPE.md` | Project Manager | No — human only |
| User Stories + Acceptance Criteria | `/docs/requirements/USER_STORIES.md` | BA / PM | Partially auto |

**What each one is:**
- **BRD** — Why the project exists. What business problem it solves. Written for executives. No technical language.
- **FRD** — What the system must do. Written as system behavior ("The system shall..."). One requirement per line.
- **Scope** — Explicit list of what is IN scope and what is OUT of scope. No ambiguity allowed.
- **User Stories** — Features broken down by user perspective. Format: "As a [user], I want [action] so that [benefit]." Every story has acceptance criteria.

---

### Phase 2 — Architecture & Design
*Created on init. Filled in during Sprint 0–1.*

| Document | File | Owner | Auto-Updated |
|----------|------|-------|--------------|
| HLD — High Level Design | `/docs/architecture/HLD.md` | Tech Lead / Architect | Flagged for human |
| LLD — Low Level Design | `/docs/architecture/LLD.md` | Senior Developer | Flagged for human |
| API Design Document | `/docs/architecture/API.md` | Backend Lead | Yes — auto |
| Database Design — ERD | `/docs/architecture/DATABASE.md` | Backend Lead | Yes — auto |

**What each one is:**
- **HLD** — Big picture. How the system is structured. Components, services, how they connect. Diagram-first. Readable by non-architects.
- **LLD** — Module-level detail. Classes, functions, data models. Written for developers on the team.
- **API Doc** — Every endpoint. Method, path, request body, response schema, error codes. Example-first format.
- **ERD** — Every table, column, data type, relationship, and index. Updated automatically when a migration file is committed.

---

### Phase 3 — Development
*Auto-maintained on every commit.*

| Document | File | Owner | Auto-Updated |
|----------|------|-------|--------------|
| Changelog | `/CHANGELOG.md` | Auto | Yes — every commit |
| Environment Setup Guide | `/docs/deployment/SETUP.md` | Tech Lead | Yes — on dependency change |
| Component / Module Docs | `/docs/components/` or `/docs/modules/` | Developer | Yes — on PR merge |
| Git Branching Strategy | `/docs/guides/GIT_STRATEGY.md` | Tech Lead | No — set once |
| Coding Standards | `/docs/guides/CODING_STANDARDS.md` | Tech Lead | No — set once |

**What each one is:**
- **Changelog** — Running log of every meaningful change. One line per entry. Imperative verb. Auto-appended on every commit.
- **Setup Guide** — How to run the project locally. Written for a developer joining on day 1. Auto-updated when package files change.
- **Component/Module Docs** — What each piece does. Inputs, outputs, usage example. Auto-updated when that module changes.
- **Git Strategy** — Branch naming, PR rules, merge policy. Written once. Never auto-changed.
- **Coding Standards** — Rules for writing code in this project. Written once. Never auto-changed.

---

### Phase 4 — Testing
*Created on init. Updated every sprint.*

| Document | File | Owner | Auto-Updated |
|----------|------|-------|--------------|
| Test Plan | `/docs/testing/TEST_PLAN.md` | QA Lead | Flagged for human |
| Test Cases | `/docs/testing/TEST_CASES.md` | QA Team | Template auto-added |
| UAT Document | `/docs/testing/UAT.md` | Project Manager | No — human only |
| Bug Report Template | `/docs/testing/BUG_REPORT.md` | QA Lead | No — set once |

**What each one is:**
- **Test Plan** — What gets tested, how, with which tools, in which environments. Flagged when a new feature area is added.
- **Test Cases** — Specific scenarios. Input → Action → Expected Result. Auto-adds blank template when a new user story starts.
- **UAT** — Business-user validation scenarios. Non-technical language. Updated after each UAT session by PM.
- **Bug Report Template** — Standardized format for logging defects. Written once at project start.

---

### Phase 5 — Deployment
*Created on init. Updated when infra or pipeline changes.*

| Document | File | Owner | Auto-Updated |
|----------|------|-------|--------------|
| Deployment Guide | `/docs/deployment/DEPLOY.md` | DevOps | Flagged for human |
| CI/CD Pipeline Document | `/docs/deployment/CICD.md` | DevOps | Flagged for human |
| Infrastructure Document | `/docs/deployment/INFRA.md` | DevOps | Flagged for human |
| Rollback Plan | `/docs/deployment/ROLLBACK.md` | DevOps | No — human only |
| Release Notes | `/docs/releases/v[version].md` | PM + Tech Lead | Yes — auto-generated |

**What each one is:**
- **Deployment Guide** — Exact numbered steps to deploy. Written for someone doing it at 2am under pressure.
- **CI/CD Doc** — How the automated build/deploy pipeline works. Stages, triggers, failure handling.
- **Infrastructure Doc** — Servers, cloud config, environment variables, third-party services.
- **Rollback Plan** — Exactly what to do if a deployment fails. Step-by-step. No ambiguity.
- **Release Notes** — Auto-generated from CHANGELOG.md when a release branch is created. Plain English for end users.

---

### Phase 6 — Maintenance
*Created before go-live. Updated post-launch.*

| Document | File | Owner | Auto-Updated |
|----------|------|-------|--------------|
| Runbook | `/docs/ops/RUNBOOK.md` | DevOps / Backend Lead | Partially auto |
| Incident Response Playbook | `/docs/ops/INCIDENT_RESPONSE.md` | DevOps | No — human only |
| Postmortem | `/docs/ops/postmortems/[date]-[name].md` | Tech Lead | No — one file per incident |
| Monitoring & Alerting Guide | `/docs/ops/MONITORING.md` | DevOps | No — set once |

**What each one is:**
- **Runbook** — How to operate the live system. What to check, what to restart, common issues and fixes.
- **Incident Response** — Who to call, what steps to take, escalation path. For live production incidents.
- **Postmortem** — What broke, why, how it was fixed, what prevents recurrence. One file per incident. Never edited after writing.
- **Monitoring Guide** — What metrics to watch, alert thresholds, dashboard locations.

---

## Priority — What Gets Created First

```
CRITICAL (must exist before dev starts):
  BRD, FRD, Scope, User Stories, HLD, API Doc, ERD

HIGH (must exist before first release):
  Test Plan, Deployment Guide, Rollback Plan, Setup Guide, Changelog

MEDIUM (must exist before go-live):
  LLD, CI/CD Doc, Runbook, Release Notes

LOW (created as needed):
  Postmortem, Bug Report Template, Monitoring Guide
```

---

## What Changes Go Where

When a feature is added:
```
User Stories    ← New story added
FRD             ← New requirement added
API Doc         ← New endpoints added (auto)
DATABASE        ← New tables/columns if needed (auto)
HLD             ← Updated if architecture changes
Test Cases      ← New scenario template added (auto)
Release Notes   ← Listed under upcoming release (auto)
Changelog       ← Entry appended (auto)
```

When a feature is modified:
```
FRD             ← Requirement updated
API Doc         ← Endpoint updated (auto)
DATABASE        ← Schema change noted (auto)
Test Cases      ← Existing cases updated
Acceptance Criteria ← Updated definition of done
Changelog       ← Entry: "updated: [what changed]" (auto)
Release Notes   ← Listed as enhancement (auto)
```

When a feature is removed:
```
FRD             ← Requirement marked removed
API Doc         ← Endpoint marked deprecated (auto)
DATABASE        ← Table/column marked for removal (auto)
Scope           ← Moved to out of scope
Changelog       ← Entry: "removed: [what]" (auto)
Release Notes   ← Listed as breaking change (auto)
```

When a bug is fixed:
```
Test Cases      ← New regression test case added
Changelog       ← Entry: "fix: [what]" (auto)
Release Notes   ← Listed under Fixed (auto)
Runbook         ← Add entry if it was an operational issue
```

---

## The Hooks Folder — How To Behave When User Points To It

When the user says any of these:
- *"Check `.claude/hooks/hooks.md`"*
- *"Apply the doc maintenance rules"*
- *"Update docs for this change"*
- *"Run the hooks for what I just changed"*

Follow this exact sequence:

**Step 1 — Read the entry file**
Read `/.claude/hooks/hooks.md` first. It is the master guide and points to everything else.

**Step 2 — Identify the change**
- If the user mentioned a specific file or area, use that
- If unclear, run: `python .claude/hooks/scripts/detect_changes.py`
- Read the JSON output to identify affected docs and diagrams

**Step 3 — Read the routing rules**
Open `/.claude/hooks/doc-maintenance.md` for the full mapping of change type → documents affected.

**Step 4 — Apply updates**
For each affected document:
- If `auto_updated: true` in settings.json → update the doc directly
- If `auto_updated: flagged` → tell the user what needs updating and ask before editing
- If `auto_updated: false` (human-only) → never auto-edit, just flag

**Step 5 — Flag diagrams**
For each affected diagram, post:
```
⚠️ Diagram needs review: [diagram-name.html]
Reason: [specific code change]
Open: /docs/diagrams/[diagram-name].html
```

Never auto-edit diagrams. The user updates the Mermaid source in the HTML file.

**Step 6 — Update last-updated headers**
On every document touched, refresh the header:
```
---
last_updated: [today's date]
changed: [plain English description of what changed]
updated_by: [role from DOC_OWNERS.md]
sprint: [current sprint number if known]
---
```

**Step 7 — Summarize the work**
Tell the user what changed, what was flagged, and what still needs human attention.

---

## The 4 Hook Layers — When Each Fires

| Layer | Location | Fires On | Your Role |
|-------|----------|----------|-----------|
| Git hooks | `.githooks/` | git commit, git push | Reactive — already ran |
| Claude hooks | `.claude/settings.json` hooks block | PostToolUse, Stop | Active during your session |
| CI / PR check | `.github/workflows/doc-check.yml` | PR opened | Reactive — already ran |
| Sprint audit | `audit_docs.py` | On demand or cron | Run when user invokes /auto-docs audit |

When a user mentions the hooks folder, they likely want you to do the work that the automated layers flagged. The scripts identify *what* — your job is to do *how*.

---

## Visual Diagrams — The 9 HTML Diagrams

Every project gets 9 interactive Mermaid.js diagrams in `/docs/diagrams/`. Each diagram is a self-contained HTML file with an editable source panel, a rendered diagram view, and direct links to the documents it belongs to.

| Diagram | File | Linked From | When To Flag For Update |
|---------|------|-------------|--------------------------|
| System Architecture | system-architecture.html | HLD | New service or module added, integration changed |
| Sequence Diagram | sequence-diagram.html | HLD, API | API changes, new feature flows |
| ERD | erd.html | DATABASE | Migration file committed |
| Data Flow | data-flow.html | HLD, FRD | New feature, infra change |
| User Flow | user-flow.html | FRD, USER_STORIES | UI change, new feature |
| API Lifecycle | api-lifecycle.html | API | API change, middleware change |
| Deployment Topology | deployment-topology.html | INFRA, DEPLOY | Infra change, new service |
| CI/CD Pipeline | cicd-pipeline.html | CICD, DEPLOY | Pipeline file change |
| Git Branching | git-branching.html | GIT_STRATEGY | Strategy change (rare) |

### How Diagrams Update

**Diagrams are never auto-edited.** Claude only flags them when something has changed that affects them. The human edits the Mermaid source text in the HTML file directly — the diagram re-renders on click.

When a commit or PR triggers a diagram update flag, post this format:
```
⚠️ Diagram needs updating: [diagram-name.html]
Reason: [Specific code change that affects this diagram]
Document to also update: [linked document]
```

### Diagram Editing

Each HTML file has three parts:
1. **Diagram panel** — Renders the Mermaid source as an interactive SVG
2. **Source editor** — Textarea with the Mermaid code, with a Render button
3. **Header** — Title, document link, last-updated date

Users edit the source, click Render, and the diagram updates. No external tools needed.

---

## Automatic Maintenance Rules

These rules are wired in permanently when `/auto-docs init` runs. They never need to be set up again.

### On Every Git Commit
```
File changed                    → Document updated
─────────────────────────────────────────────────
routes/ controllers/ api/       → API.md auto-updated
migrations/ *.sql               → DATABASE.md auto-updated
package.json requirements.txt   → SETUP.md auto-updated
Podfile build.gradle            → SETUP.md auto-updated
Any code file                   → CHANGELOG.md appended
components/ src/components/     → /docs/components/ auto-updated
modules/ src/                   → /docs/modules/ auto-updated
```

### On Every Pull Request
```
PR opened
  → Scan diff for change type
  → Check if relevant doc is updated in the PR
  → If doc stale → PR comment: "Doc update needed: [document name]"
  → If doc updated → silent, no action
```

### On Every Release
```
Release branch created
  → Read CHANGELOG.md since last git tag
  → Auto-generate /docs/releases/v[version].md
  → Snapshot all docs into /docs/releases/v[version]/archive/
  → Update version numbers in API.md
```

### Sprint End Audit (via /auto-docs audit)
```
Compare current code state vs current doc state
  → Flag every doc not updated in the last 2 sprints
  → Flag every API endpoint not in API.md
  → Flag every DB table not in DATABASE.md
  → Flag every completed story with no release note
  → Output: Stale Doc Report with action items
```

---

## Document Lifecycle

Every document goes through this lifecycle:

```
BORN      → Created at init with pre-filled template
ACTIVE    → Updated automatically or flagged for human
AUDITED   → Checked every sprint for staleness
VERSIONED → Snapshot taken at every release
ARCHIVED  → Old versions kept in /docs/releases/v[x]/archive/
```

A document is never deleted. It is either current, archived, or deprecated-with-note.

---

## Last-Updated Header — Every Document

Every generated document has this at the top:

```
---
last_updated: YYYY-MM-DD
changed: [plain English description of what changed]
updated_by: [role — not person name]
sprint: [sprint number]
---
```

This header is updated automatically on every relevant change. The team never has to wonder when a doc was last touched or why.

---

## Tone Rules — How Every Document Must Read

Documents must read like a senior developer or experienced PM wrote them. Not like AI generated them.

### What to Do
```
✅ Active voice — "The system sends an email" not "An email will be sent"
✅ Present tense — "Returns 200" not "Will return 200"
✅ Short sentences — one idea per sentence, 20 words max
✅ Lead with the what, then explain the why
✅ Use specific numbers — "loads in 180ms" not "loads quickly"
✅ Use code examples instead of long prose descriptions
✅ Write for the reader who will use this at 2am under pressure
```

### What Not to Do
```
❌ No filler openers — never start with "In this document we will..."
❌ No passive voice — "the data is stored" → "the system stores the data"
❌ No over-explanation — don't explain what is already obvious from the heading
❌ No vague claims — "fast", "secure", "scalable" mean nothing without numbers
❌ No future tense for current behavior — if it works now, write in present tense
❌ No "Note:", "Please note:", "It is important to note that"
❌ No AI-pattern phrases — "Certainly!", "Of course!", "Great question!"
❌ No unnecessary bullet points — if it flows naturally as prose, write it as prose
```

---

## What to Do on Init

When `/auto-docs init` is invoked, follow this exact sequence:

**Step 1 — Ask the 5 questions. Wait for all answers before proceeding.**
```
1. Project name?
2. Project type? (Web App / iOS / Android / API Only / Fullstack)
3. Tech stack? (e.g. React + Django, Swift + Node)
4. Team size? (Solo / 2–5 / 6–15 / 15+)
5. Expected first release? (approximate month is fine)
```

**Step 2 — Confirm what will be generated.**
Show the user exactly what will be created based on their answers. Wait for confirmation.

**Step 3 — Generate the folder structure.**
Create all directories and files. Pre-fill every template with project name, stack, date, and team info from the answers.

**Step 4 — Generate DOC_OWNERS.md.**
List every document, its owner role, update trigger, and whether it is auto-maintained or human-maintained.

**Step 5 — Wire the maintenance rules.**
Write `.claude/hooks/doc-maintenance.md` with the commit, PR, and release rules for this specific project.

**Step 6 — Show the completion summary.**
Tell the user what was created, what they need to fill in manually (BRD, FRD, Scope), and confirm that automatic maintenance is active.

---

## What to Do on Audit

When `/auto-docs audit` is invoked, follow this sequence:

**Step 1 — Scan all documents for last-updated headers.**
**Step 2 — Compare API.md endpoints against current API files in the repo.**
**Step 3 — Compare DATABASE.md tables against current migration files.**
**Step 4 — Check CHANGELOG.md for entries since last release tag.**
**Step 5 — Check every completed user story for a corresponding release note entry.**
**Step 6 — Output the Stale Doc Report.**

Report format:
```
📋 Doc Audit Report — Sprint [N] — [Date]

✅ Up to date:
   CHANGELOG.md, API.md, DATABASE.md, SETUP.md

⚠️  Needs update:
   FRD.md — Feature [X] was added 3 weeks ago, FRD not updated
   TEST_CASES.md — 2 user stories in dev have no test cases

❌ Missing:
   RUNBOOK.md — Not created yet. Go-live is in 2 weeks.
   ROLLBACK.md — Not created yet. Required before release.

Action required: 2 docs need updating, 2 docs need creating
```

---

## What NOT to Do — Hard Rules

```
❌ Never delete existing content from any document
❌ Never overwrite a human-written section with auto-generated content
❌ Never auto-edit BRD or Scope — always flag for human
❌ Never guess which doc to update — if unsure, flag it and ask
❌ Never generate docs without asking the 5 init questions first
❌ Never run audit silently — always output the full report
❌ Never mark a doc as "up to date" without actually checking it
❌ Never create postmortem files automatically — human writes these
❌ Never write doc content that sounds like AI wrote it
❌ Never add headers like "Overview", "Introduction", "Conclusion" to technical docs
```

---

## What Humans Must Always Do

Some documents require human judgment. Claude never auto-edits these:

```
BRD              → Human writes. Claude flags when likely stale.
Scope            → Human writes. Claude flags when change requests arrive.
FRD              → Human writes. Claude flags when new features are committed.
HLD              → Human writes. Claude flags when new services appear.
Rollback Plan    → Human writes. Claude flags when deploy process changes.
UAT Document     → Human writes after each UAT session.
Postmortem       → Human writes within 48 hours of incident.
Incident Response → Human writes. Claude never edits this.
```

---

## Stack-Aware Behavior

When the user selects a project type during init, generate these extras:

**Web App (React / Vue / Svelte)**
- `/docs/components/` folder
- Component doc template with: props, emits, slots, usage example

**Mobile iOS (Swift / SwiftUI)**
- `/docs/modules/` folder
- Module doc template with: class/struct name, public methods, dependencies, usage

**Mobile Android (Kotlin / Jetpack Compose)**
- `/docs/modules/` folder
- Module doc template with: class name, public API, dependencies, usage

**API Only**
- Expand `/docs/architecture/API.md` with OpenAPI-style format
- Add `/docs/architecture/ERRORS.md` — all error codes and meanings

**Fullstack**
- All of the above combined

---

## Folder Structure Reference

```
/docs
├── requirements/
│   ├── BRD.md                   ← Business requirement
│   ├── FRD.md                   ← Functional requirement
│   ├── SCOPE.md                 ← In scope / Out of scope
│   └── USER_STORIES.md          ← Stories + acceptance criteria
├── architecture/
│   ├── HLD.md                   ← High level design
│   ├── LLD.md                   ← Low level design
│   ├── API.md                   ← All endpoints
│   └── DATABASE.md              ← ERD + schema
├── guides/
│   ├── SETUP.md                 ← Local dev setup
│   ├── GIT_STRATEGY.md          ← Branch + PR rules
│   └── CODING_STANDARDS.md      ← Code style rules
├── components/                  ← Web projects only
│   └── [ComponentName].md
├── modules/                     ← Mobile projects only
│   └── [ModuleName].md
├── testing/
│   ├── TEST_PLAN.md             ← Testing approach
│   ├── TEST_CASES.md            ← Test scenarios
│   ├── UAT.md                   ← Business validation
│   └── BUG_REPORT.md            ← Bug report template
├── deployment/
│   ├── DEPLOY.md                ← Deploy steps
│   ├── SETUP.md                 ← Local setup
│   ├── CICD.md                  ← Pipeline docs
│   ├── INFRA.md                 ← Infrastructure
│   └── ROLLBACK.md              ← Rollback plan
├── ops/
│   ├── RUNBOOK.md               ← Operations guide
│   ├── INCIDENT_RESPONSE.md     ← Incident handling
│   ├── MONITORING.md            ← Alerts + dashboards
│   └── postmortems/
│       └── YYYY-MM-DD-name.md   ← One file per incident
└── releases/
    └── v[version].md            ← One file per release
/CHANGELOG.md                    ← Root level. Always.
/DOC_OWNERS.md                   ← Ownership map. Always.
/.claude/hooks/doc-maintenance.md ← Auto-maintenance rules
```

---

## End of Project — Handoff Package

When the project ends or is handed off, run `/auto-docs audit` one final time, then generate:

```
/handoff/
├── FINAL_SYSTEM_DESIGN.md     ← Copy of latest HLD + LLD
├── FINAL_API_REFERENCE.md     ← Copy of latest API.md
├── FINAL_DATABASE_SCHEMA.md   ← Copy of latest DATABASE.md
├── FULL_CHANGELOG.md          ← Complete changelog
├── RUNBOOK.md                 ← Operations guide
└── README.md                  ← Where to find everything
```

This package is complete, self-contained, and usable by anyone taking over the project.

---

## Quick Reference Card

```
COMMAND              WHEN TO RUN          WHAT IT DOES
───────────────────────────────────────────────────────────────────
/auto-docs init      Day 0, once ever     Generates all docs + wires maintenance
/auto-docs audit     Sprint end, pre-release  Finds stale docs, missing docs, gaps

AUTOMATIC (no command needed)
───────────────────────────────────────────────────────────────────
On every commit    → Changelog updated, API/DB/Setup docs updated
On every PR        → Staleness check runs, stale docs flagged
On every release   → Release notes generated, docs archived
```

---

**Skill Version**: 1.0.0
**Last Updated**: 2026-05-21
**Status**: Production Ready

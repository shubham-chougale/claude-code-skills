---
name: auto-docs
description: Automated documentation generation and lifetime maintenance for any project. Run once at project start — docs maintain themselves forever after.
version: 1.0.0
---

# /auto-docs

## What This Skill Does

Generates a complete documentation system for any project with a single command. After init, all documentation updates automatically — triggered by commits, PRs, and sprint cycles. No manual doc maintenance required from the team.

## When to Invoke This Skill

Invoke `/auto-docs` when:
- Starting any new project (web, mobile, API, fullstack)
- A project has no documentation structure yet
- Existing docs are out of sync and need a full reset
- User says "set up docs", "create documentation", "auto docs", "doc system"

---

## How It Works

```
/auto-docs init
      ↓
Asks 5 questions about the project
      ↓
Generates full /docs folder with pre-filled templates
      ↓
Wires automatic maintenance hooks into the project
      ↓
Done — docs maintain themselves from this point forward
```

---

## The 5 Init Questions

Ask these in order. Wait for answers before proceeding.

```
1. What is the project name?
2. What type of project?
   → Web App / Mobile (iOS) / Mobile (Android) / API Only / Fullstack
3. What is the tech stack?
   → e.g. React + Django, Swift + Node, Kotlin + FastAPI
4. How many people are on the team?
   → Solo / 2–5 / 6–15 / 15+
5. What is the expected first release date?
   → Approximate month is fine
```

---

## What Gets Generated on Init

### Folder Structure

```
/docs
├── requirements/
│   ├── BRD.md
│   ├── FRD.md
│   ├── SCOPE.md
│   └── USER_STORIES.md
├── architecture/
│   ├── HLD.md
│   ├── LLD.md
│   ├── API.md
│   └── DATABASE.md
├── guides/
│   ├── GIT_STRATEGY.md
│   └── CODING_STANDARDS.md
├── testing/
│   ├── TEST_PLAN.md
│   ├── TEST_CASES.md
│   ├── UAT.md
│   └── BUG_REPORT.md
├── deployment/
│   ├── DEPLOY.md
│   ├── SETUP.md
│   ├── CICD.md
│   ├── INFRA.md
│   └── ROLLBACK.md
├── ops/
│   ├── RUNBOOK.md
│   ├── INCIDENT_RESPONSE.md
│   ├── MONITORING.md
│   └── postmortems/
├── diagrams/
│   ├── system-architecture.html   ← Services + components (interactive)
│   ├── sequence-diagram.html      ← Request/response flow (interactive)
│   ├── erd.html                   ← Database tables + relations (interactive)
│   ├── data-flow.html             ← Data movement through system (interactive)
│   ├── user-flow.html             ← User navigation paths (interactive)
│   ├── api-lifecycle.html         ← Full API request path (interactive)
│   ├── deployment-topology.html   ← Servers + cloud + network (interactive)
│   ├── cicd-pipeline.html         ← Build to production stages (interactive)
│   └── git-branching.html         ← Branch strategy (interactive)
└── releases/
/CHANGELOG.md
/DOC_OWNERS.md

/.claude/hooks/                      ← Layer 2 + entry point for Claude
├── hooks.md                         ← Master guide — tell Claude to read this
├── doc-maintenance.md               ← Routing rules per change type
├── claude-hooks.json                ← Claude Code hooks config (PostToolUse, etc.)
└── scripts/
    ├── detect_changes.py            ← Maps changed files → affected docs/diagrams
    ├── update_changelog.py          ← Auto-appends CHANGELOG.md from commits
    ├── audit_docs.py                ← Full staleness audit (powers /auto-docs audit)
    └── check_stale.py               ← PR-time + pre-push stale check

/.githooks/                          ← Layer 1: Git hooks
├── post-commit                      ← Bash version
├── post-commit.ps1                  ← Windows PowerShell version
├── pre-push                         ← Warns on stale docs before push
├── install.sh                       ← Installer for Mac/Linux
└── install.ps1                      ← Installer for Windows

/.github/workflows/                  ← Layer 3: CI / PR checks
└── doc-check.yml                    ← Auto-comments on PRs with stale docs
```

### Stack-Aware Generation

| Stack Selected | Extra Docs Generated |
|----------------|----------------------|
| React / Vue / Svelte | /docs/components/ folder + component template |
| iOS (Swift) | /docs/modules/ folder + Swift module template |
| Android (Kotlin) | /docs/modules/ folder + Kotlin module template |
| API Only | /docs/architecture/API.md expanded with OpenAPI format |
| Fullstack | All of the above combined |

---

## Document Definitions

### Phase 1 — Planning & Requirements (Created on Init, Day 0)

#### BRD — Business Requirement Document
```
What:     Why this project exists, what business problem it solves
Tone:     Executive-readable, no technical jargon
Owner:    Project Manager
Lives in: /docs/requirements/BRD.md
Updates:  Only when business goal or stakeholder changes
Trigger:  Stakeholder meeting outcome — human updates this
```

#### FRD — Functional Requirement Document
```
What:     Exact features the system must do, written as system behavior
Tone:     Precise, third-person ("The system shall...")
Owner:    Tech Lead / BA
Lives in: /docs/requirements/FRD.md
Updates:  Every time a feature is added, changed, or removed
Trigger:  Sprint planning or change request → Claude flags for update
```

#### Scope Document
```
What:     Explicit list of what is IN scope and OUT of scope
Tone:     Bullet list, no ambiguity
Owner:    Project Manager
Lives in: /docs/requirements/SCOPE.md
Updates:  When scope changes are formally approved
Trigger:  Change request → human updates this
```

#### User Stories + Acceptance Criteria
```
What:     Feature breakdown from user perspective + definition of done
Tone:     "As a [user], I want [action] so that [benefit]"
Owner:    BA / PM
Lives in: /docs/requirements/USER_STORIES.md
Updates:  Every sprint — new stories added, completed stories marked done
Trigger:  Sprint planning → Claude adds new stories, marks completed ones
```

---

### Phase 2 — Architecture & Design (Created on Init, Sprint 0–1)

#### HLD — High Level Design
```
What:     How the system is structured — components, services, interactions
Tone:     Technical but readable by non-architects
Owner:    Tech Lead / Architect
Lives in: /docs/architecture/HLD.md
Updates:  When a new service, module, or major architectural decision changes
Trigger:  New directory or service added to repo → Claude flags for update
```

#### Database Design — ERD
```
What:     All tables, columns, data types, relationships, indexes
Tone:     Technical, schema-first, migration history noted
Owner:    Backend Lead
Lives in: /docs/architecture/DATABASE.md
Updates:  Every time a migration file is added or modified
Trigger:  Migration file committed → Claude auto-updates this
```

#### API Design Document
```
What:     All endpoints — method, path, request, response, error codes
Tone:     Developer-to-developer, example-first
Owner:    Backend Lead
Lives in: /docs/architecture/API.md
Updates:  Every time an endpoint is added, changed, or deprecated
Trigger:  API file committed → Claude auto-updates this
```

#### LLD — Low Level Design
```
What:     Module-level detail — classes, functions, public interfaces, dependencies
Tone:     Technical, written for developers on the team
Owner:    Senior Developer
Lives in: /docs/architecture/LLD.md
Updates:  When module interfaces or internal logic changes significantly
Trigger:  Major refactor or new module → Claude flags for human update
```

---

### Phase 3 — Development (Auto-maintained every commit)

#### Changelog
```
What:     Running log of every meaningful change
Tone:     Imperative verb, one line per entry
Owner:    Auto-generated
Lives in: /CHANGELOG.md
Updates:  Every commit automatically
Trigger:  Git commit → Claude appends entry
Format:
  ## [Sprint 3] — YYYY-MM-DD
  - feat: Add Google OAuth login
  - fix: Resolve session timeout on mobile
  - chore: Update API rate limit config
```

#### Component / Module Documentation
```
What:     What each component or module does, inputs, outputs, usage
Tone:     Concise, example-first
Owner:    Developer who wrote it
Lives in: /docs/components/ or /docs/modules/
Updates:  When module interface or behavior changes
Trigger:  PR merge touching the module → Claude auto-updates
```

#### Environment Setup Guide
```
What:     How to run the project locally
Tone:     Step-by-step, written for a new developer joining day 1
Owner:    Tech Lead
Lives in: /docs/deployment/SETUP.md
Updates:  When dependencies, env vars, or setup steps change
Trigger:  package.json / requirements.txt change → Claude auto-updates
```

#### Git Branching Strategy
```
What:     Branch structure, naming conventions, merge rules
Tone:     Process-oriented, written for the whole team
Owner:    Tech Lead
Lives in: /docs/guides/GIT_STRATEGY.md
Updates:  Only when branching strategy formally changes
Trigger:  Strategy change — human writes this. Never auto-edited.
```

#### Coding Standards
```
What:     Rules for writing code in this project — naming, structure, error handling
Tone:     Direct, rule-based, with code examples for each rule
Owner:    Tech Lead
Lives in: /docs/guides/CODING_STANDARDS.md
Updates:  When standards are formally agreed by the team
Trigger:  Standards update — human writes this. Never auto-edited.
```

---

### Phase 4 — Testing (Auto-maintained per sprint)

#### Test Plan
```
What:     What gets tested, approach, tools, environments
Tone:     Process-oriented, clear pass/fail criteria
Owner:    QA Lead
Lives in: /docs/testing/TEST_PLAN.md
Updates:  When new feature area added
Trigger:  New epic added to FRD → Claude flags for QA to update
```

#### Test Cases
```
What:     Specific scenarios — input, action, expected result
Tone:     Numbered, unambiguous, one scenario per case
Owner:    QA Team
Lives in: /docs/testing/TEST_CASES.md
Updates:  Every sprint — new cases for new features
Trigger:  User story moved to In Development → Claude adds case template
```

#### UAT Document
```
What:     Business validation scenarios tested by client/stakeholders
Tone:     Non-technical, written for business users
Owner:    Project Manager
Lives in: /docs/testing/UAT.md
Updates:  After each UAT session
Trigger:  UAT session scheduled → human updates this
```

#### Bug Report Template
```
What:     Standardized format for filing defects
Tone:     Form-style — exact fields, no ambiguity about what info to capture
Owner:    QA Lead
Lives in: /docs/testing/BUG_REPORT.md
Updates:  Set once at project start. Rarely changed.
Trigger:  Initial setup only. Never auto-edited.
```

---

### Phase 5 — Release (Auto-generated per release)

#### Release Notes
```
What:     User-facing summary of what changed in this release
Tone:     Plain English, written for end users — not developers
Owner:    PM + Tech Lead (reviewed together)
Lives in: /docs/releases/v[version].md
Created:  Every release — auto-generated from CHANGELOG.md
Trigger:  Release branch created → Claude generates this automatically
Format:
  ## v1.2.0 — June 2026
  ### What's New
  - Users can now sign in with Google
  ### Improvements
  - Dashboard loads 40% faster
  ### Fixed
  - Login session no longer expires unexpectedly
```

#### Deployment Guide
```
What:     Exact steps to deploy — commands, configs, rollback plan
Tone:     Numbered steps, no assumptions
Owner:    DevOps
Lives in: /docs/deployment/DEPLOY.md
Updates:  When deployment process or infra changes
Trigger:  CI/CD or infra file committed → Claude flags for DevOps review
```

#### CI/CD Pipeline Document
```
What:     Pipeline stages, tools, approval gates, secrets management
Tone:     Operational, written for DevOps and engineers debugging the pipeline
Owner:    DevOps
Lives in: /docs/deployment/CICD.md
Updates:  When pipeline stages, tools, or configuration changes
Trigger:  Pipeline file committed → Claude flags for DevOps update
```

#### Infrastructure Document
```
What:     Cloud services, network topology, environment configs, costs
Tone:     Technical, structured by service type
Owner:    DevOps
Lives in: /docs/deployment/INFRA.md
Updates:  When infrastructure is added, removed, or reconfigured
Trigger:  Infra config committed → Claude flags for DevOps update
```

#### Rollback Plan
```
What:     Exact steps to undo a failed deployment, including DB rollback
Tone:     Action-first, written for someone executing under pressure
Owner:    DevOps
Lives in: /docs/deployment/ROLLBACK.md
Updates:  When deployment process changes
Trigger:  Deploy process change — human writes this. Never auto-edited.
```

---

### Phase 6 — Maintenance (Post-Launch)

#### Runbook
```
What:     How to operate the live system — monitoring, alerts, common issues
Tone:     Action-oriented, written for whoever is on-call at 2am
Owner:    DevOps / Backend Lead
Lives in: /docs/ops/RUNBOOK.md
Updates:  After every incident or operational change
Trigger:  Incident resolved → Claude adds entry from incident details
```

#### Postmortem
```
What:     What broke, why, how fixed, what prevents recurrence
Tone:     Factual, blameless, future-focused
Owner:    Tech Lead / On-call engineer
Lives in: /docs/ops/postmortems/[date]-[incident].md
Created:  Within 48 hours of incident resolution
Trigger:  Incident resolved — one file per incident, never edited after
```

#### Incident Response Playbook
```
What:     Escalation paths, contact info, communication protocol per severity
Tone:     Action-oriented, decision-tree style
Owner:    DevOps / Tech Lead
Lives in: /docs/ops/INCIDENT_RESPONSE.md
Updates:  When escalation paths or on-call contacts change
Trigger:  Escalation path change — human writes this. Never auto-edited.
```

#### Monitoring & Alerting Guide
```
What:     Metrics, thresholds, alert routing, dashboard locations
Tone:     Reference-style with concrete numbers and thresholds
Owner:    DevOps
Lives in: /docs/ops/MONITORING.md
Updates:  When alerts, thresholds, or dashboards change
Trigger:  Alert/dashboard change — human writes this. Never auto-edited.
```

---

## Automatic Maintenance — Wired at Init

When init completes, these rules are permanently active for the project:

### On Every Commit
```
Claude reads git diff
  → API file changed?           → Update API.md + flag sequence-diagram.html + api-lifecycle.html
  → Migration file added?       → Update DATABASE.md + flag erd.html
  → Package file changed?       → Update SETUP.md
  → Pipeline config changed?    → Flag CICD.md + cicd-pipeline.html
  → Infra config changed?       → Flag INFRA.md + deployment-topology.html
  → New service/module dir?     → Flag HLD.md + system-architecture.html
  → Component/module changed?   → Update /docs/components/[name].md or /docs/modules/[name].md
  → Any code change?            → Append to CHANGELOG.md
```

### On Every PR
```
Claude scans PR diff
  → Identifies what type of change it is
  → Checks if relevant doc was updated in the PR
  → If doc is stale → adds PR comment: "Doc update needed: [doc name]"
  → If doc is updated → silent, no interruption
```

### Sprint End Audit
```
Claude compares current code vs current docs
  → Lists every doc that is stale
  → Shows what specifically is out of sync
  → Generates a short Stale Doc Report
  → Team resolves gaps before next sprint starts
```

### On Release
```
Claude reads CHANGELOG.md since last release tag
  → Auto-generates /docs/releases/v[version].md
  → Snapshots all docs into /docs/releases/v[version]/archive/
  → Updates version numbers in API doc
```

---

## Document Last-Updated Format

Every generated document includes this header block:

```markdown
---
last_updated: YYYY-MM-DD
changed: [what changed in plain English]
updated_by: [role — not person name]
sprint: [sprint number]
---
```

This block updates automatically on every relevant commit. The team always knows exactly when a doc was last touched and why.

---

## Documentation Tone Rules

All generated documents follow these rules so they never read like AI wrote them:

```
✅ Use active voice ("The system sends" not "An email will be sent")
✅ Use present tense ("Returns a 200 response" not "Will return")
✅ Short sentences — one idea per sentence
✅ No filler phrases ("In this document we will explore...")
✅ No over-explanation of obvious things
✅ Lead with the what, follow with the why
✅ Code examples over long descriptions
✅ Specific numbers over vague claims ("loads in 200ms" not "loads fast")
```

---

## Ownership Map — DOC_OWNERS.md

Generated at init. Defines who is responsible for each document:

```
| Document       | Owner Role      | Auto-Updated | Human Required |
|----------------|-----------------|--------------|----------------|
| BRD            | Project Manager | No           | Yes            |
| FRD            | Tech Lead / BA  | Flagged      | Yes            |
| Scope          | Project Manager | No           | Yes            |
| User Stories   | BA / PM         | Partially    | Yes            |
| HLD            | Tech Lead       | Flagged      | Yes            |
| ERD            | Backend Lead    | Yes          | No             |
| API Doc        | Backend Lead    | Yes          | No             |
| Changelog      | Auto            | Yes          | No             |
| Test Cases     | QA Team         | Template     | Yes            |
| Release Notes  | PM + Tech Lead  | Yes          | Review only    |
| Runbook        | DevOps          | Partially    | Yes            |
| Postmortem     | Tech Lead       | No           | Yes            |
```

---

## Safety Rules

- Never delete existing content from a document — only append or update
- Never overwrite a human-written section with auto-generated content
- Always show what changed before writing to a doc
- If unsure which doc to update — flag it, don't guess
- BRD and Scope are never auto-edited — always flagged for human

---

## Hook System — 4 Layers of Automation

Init wires up four parallel maintenance layers. Each layer fires on different events. If one misses a change, another catches it.

### Layer 1 — Git Hooks (works outside Claude)

Lives in `/.githooks/`. Installed once per developer machine via `bash .githooks/install.sh`.

- `post-commit` — Auto-appends CHANGELOG.md, prints affected docs after every commit
- `pre-push` — Warns about stale docs before push (non-blocking)

### Layer 2 — Claude Code Hooks (in-session edits)

Lives in `.claude/settings.json` (config block). Source: `/.claude/hooks/claude-hooks.json`.

- `PostToolUse` — Fires after Claude edits a file. Runs `detect_changes.py` to track affected docs
- `Stop` — Fires when Claude finishes. Surfaces accumulated doc update suggestions
- `UserPromptSubmit` — Pre-runs audit when user mentions docs

### Layer 3 — CI / PR Checks (server-side)

Lives in `/.github/workflows/doc-check.yml`.

- On every PR, runs `check_stale.py` against the diff
- Posts a PR comment listing stale docs that should be updated before merge
- Non-blocking by default (can be configured to block)

### Layer 4 — Sprint Audit (on-demand)

Lives in `/.claude/hooks/scripts/audit_docs.py`. Triggered by:
- `/auto-docs audit` command
- Cron job (optional)
- Manual invocation

Runs full staleness check across every document, including comparing API.md endpoints to actual code.

### The Master Entry Point

`/.claude/hooks/hooks.md` is the single file users point Claude at when they want docs updated:

> *"Check `.claude/hooks/hooks.md` and update the docs for this change."*

Claude reads it → loads the rules → updates docs → flags diagrams.

---

## Diagrams — Visual Reference System

All diagrams live in `/docs/diagrams/` as self-contained HTML files. Each diagram uses Mermaid.js and renders interactively in any browser. Users edit the Mermaid source text directly inside the file — no external tools needed.

### The 9 Diagrams

| Diagram | File | Linked From | Updates When |
|---------|------|-------------|--------------|
| System Architecture | `system-architecture.html` | HLD.md | New service added, integration changed |
| Sequence Diagram | `sequence-diagram.html` | HLD.md, API.md | API changes, new features |
| ERD | `erd.html` | DATABASE.md | Migration file committed |
| Data Flow Diagram | `data-flow.html` | HLD.md, FRD.md | New feature, infra change |
| User Flow | `user-flow.html` | FRD.md, USER_STORIES.md | UI change, new feature |
| API Request Lifecycle | `api-lifecycle.html` | API.md | API change, infra change |
| Deployment Topology | `deployment-topology.html` | INFRA.md | Infra change, new service |
| CI/CD Pipeline | `cicd-pipeline.html` | CICD.md | Pipeline file committed |
| Git Branching Strategy | `git-branching.html` | GIT_STRATEGY.md | Branching strategy change |

### How Diagrams Stay Updated

When a commit or PR touches something that affects a diagram, the skill flags it:

```
Migration file committed
  → DATABASE.md auto-updated
  → erd.html flagged: "ERD needs updating — schema changed"

New API endpoint committed
  → API.md auto-updated
  → sequence-diagram.html flagged: "Sequence diagram may need updating"
  → api-lifecycle.html flagged: "API lifecycle diagram may need updating"

New service directory added
  → HLD.md flagged
  → system-architecture.html flagged: "Architecture diagram needs new service added"

Pipeline config file changed
  → CICD.md flagged
  → cicd-pipeline.html flagged: "CI/CD diagram needs updating"
```

### Diagram HTML Structure

Each HTML file contains:
- Header bar with diagram title, document link, last-updated date
- Rendered Mermaid diagram (live SVG output)
- Editable source text area — edit the Mermaid code, click Render
- Update instructions with exact Mermaid syntax for common changes

### Linking Diagrams to Documents

Every relevant document includes a diagram reference line:

```markdown
> View diagram → [System Architecture](../diagrams/system-architecture.html)
```

---

## Audit Command

```
/auto-docs audit
```

Runs a staleness check across all docs. Use at sprint end or before a release.

Output format:
```
📋 Doc Audit Report — Sprint 4 — 2026-06-01

✅ Up to date:    CHANGELOG.md, API.md, DATABASE.md
⚠️  Needs update: FRD.md (feature X added 3 weeks ago, FRD not updated)
⚠️  Needs update: TEST_CASES.md (2 new stories have no test cases)
❌ Missing:       RUNBOOK.md (not created yet — go-live in 2 weeks)

Action required: 2 docs flagged, 1 doc missing
```

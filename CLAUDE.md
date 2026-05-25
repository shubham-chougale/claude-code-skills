# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 📌 Project Overview

**Industrial Trends** is a Claude Code workspace for AI/GenAI trend discovery and engineering tools. It contains three production-ready custom skills that help with:
- Discovering latest AI/GenAI engineering updates
- Building distinctive, production-grade frontend interfaces
- Detecting and resolving database migration conflicts

## 🛠️ Available Skills

### 1. 🎯 /get-trending-in-AI
**AI/GenAI Engineering Trend Discovery**

Discovers, analyzes, and summarizes the latest AI/GenAI frameworks, libraries, tools, and research with practical production value.

**Features**:
- 7-category discovery modes (frameworks, models, agents, repos, production, upcoming, custom)
- Deduplication engine (45+ tracked discoveries)
- Technology trend identification
- HTML report generation with auto-browser opening
- Strategic engineering takeaways

**Location**: `.claude/skills/get-trending-in-AI/`

**Usage**:
```bash
/get-trending-in-AI
→ Select category (1-7)
→ Report generates & opens in browser automatically
```

**Output**: Self-contained HTML report (syntax-highlighted, no dependencies)

**Performance**: 30-60 seconds per execution

---

### 2. 🎨 /frontend-design
**Production-Grade Frontend Interface Design**

Creates distinctive, high-quality frontend interfaces with exceptional design that avoids generic "AI slop" aesthetics.

**Features**:
- Bold aesthetic directions (11+ styles: minimalism, maximalism, retro, luxury, etc.)
- Distinctive typography choices
- Advanced CSS animations & effects
- Responsive spatial composition
- Production-ready code

**Supported Frameworks**:
- React 16+ (with Motion library support)
- Vue 3+
- HTML/CSS/JS (vanilla)
- Svelte

**Location**: `.claude/skills/frontend-design/`

**Usage**:
```bash
/frontend-design
→ Describe component/page/application
→ Choose aesthetic direction
→ Code generated with exceptional design
```

**Output**: Complete, working code with professional design

---

### 3. 🗄️ /db-migration-resolver
**Database Migration Conflict Detector & Resolver**

Detects and resolves database migration conflicts for Alembic (SQLAlchemy) and Django projects.

**Features**:
- Auto-detect conflict types (branching, schema drift, FK violations, irreversible downgrades)
- Risk assessment (medium/high risk categorization)
- Safe auto-fixes (file renames, revision updates, merge operations)
- Approval workflow (always ask before risky operations)
- Schema inspection utilities

**Supported Frameworks**:
- Alembic (SQLAlchemy) 1.0+
- Django 3.0+

**Location**: `.claude/skills/db-migration-resolver/`

**Usage**:
```bash
/db-migration-resolver
→ Select framework (Alembic or Django)
→ Provide project path
→ Conflicts detected & interactive resolution
```

**Output**: Interactive conflict report + approved fixes

---

### 4. 📄 /auto-docs
**Automated Documentation Generation & Lifetime Maintenance**

Generates a complete documentation system for any project with a single command. After init, all documentation updates automatically — triggered by commits, PRs, and sprint cycles. No manual doc maintenance required.

**Commands**:
- `/auto-docs init` — Run once at project start. Generates full `/docs` structure + wires automatic maintenance
- `/auto-docs audit` — Run at sprint end or before release. Finds stale docs, gaps, and missing documents

**What It Generates**:
- BRD, FRD, Scope, User Stories (requirements)
- HLD, API Doc, Database/ERD (architecture)
- Test Plan, Test Cases, UAT (testing)
- Deployment Guide, Setup Guide (deployment)
- Runbook, Postmortem template (operations)
- Changelog, Release Notes (auto-maintained)

**Supported Project Types**:
- Web App (React, Vue, Angular, Svelte)
- Mobile iOS (Swift, SwiftUI)
- Mobile Android (Kotlin, Jetpack Compose)
- API Only (Django, FastAPI, Node, Rails)
- Fullstack (any combination)

**Automatic Maintenance** (no manual effort after init):
- Every commit → Changelog updated, API/DB docs updated if relevant
- Every PR → Staleness check runs, flags outdated docs
- Every release → Release notes auto-generated from changelog
- Sprint end → Full audit report generated

**Location**: `.claude/skills/auto-docs/`

**Usage**:
```bash
/auto-docs init
→ Answer 5 questions about your project
→ Full /docs structure generated
→ Automatic maintenance wired in — done forever

/auto-docs audit
→ Sprint-end staleness report
→ Shows what's up to date, what needs attention, what's missing
```

---

## 📁 Project Structure

```
industrial-trends-main/
├── CLAUDE.md                              ← You are here
├── SKILLS_INVENTORY.md                    ← GitHub-ready skills inventory
├── genai_trends_YYYY_MM_DD.html          ← Generated trend reports
│
└── .claude/
    ├── settings.json                      ← Configuration & hooks
    ├── settings.local.json               ← Local overrides
    │
    └── skills/
        ├── README.md                      ← Skills documentation
        ├── get-trending-in-AI/
        │   ├── SKILL.md
        │   ├── settings.json
        │   └── DEDUPLICATION_GUIDE.md
        ├── frontend-design/
        │   ├── SKILL.md
        │   ├── settings.json
        │   └── LICENSE.txt
        ├── db-migration-resolver/
        │   ├── SKILL.md
        │   ├── settings.json
        │   ├── references/
        │   │   ├── alembic.md
        │   │   ├── django.md
        │   │   └── conflict-types.md
        │   └── scripts/
        │       ├── detect_alembic.py
        │       ├── detect_django.py
        │       ├── inspect_schema.py
        │       └── apply_fix.py
        └── auto-docs/
            ├── SKILL.md
            ├── settings.json
            └── templates/
                ├── requirements/
                ├── architecture/
                ├── testing/
                ├── deployment/
                └── ops/
```

## 🚀 Quick Start

### Running Skills

```bash
# Discover latest AI trends
/get-trending-in-AI

# Build a frontend component
/frontend-design

# Resolve migration conflicts
/db-migration-resolver

# Set up documentation for any new project
/auto-docs init

# Audit doc health at sprint end or before release
/auto-docs audit
```

### Workflow Examples

**Scenario 1: Get Latest AI Trends**
```
1. Run: /get-trending-in-AI
2. Select: 1-7 (or custom category)
3. Report generates
4. Browser opens automatically with results
5. Review recommendations & findings
```

**Scenario 2: Design a Frontend Component**
```
1. Run: /frontend-design
2. Describe what you want (component, page, app)
3. Choose aesthetic direction (minimalist, maximalist, retro, etc.)
4. Code generated with exceptional design
5. Copy code & integrate into project
```

**Scenario 3: Fix Migration Conflicts**
```
1. Run: /db-migration-resolver
2. Select framework (Alembic or Django)
3. Provide project path
4. Conflicts detected & analyzed
5. Apply fixes (auto-safe or manual-approval)
6. Verify with migration commands
```

**Scenario 4: Set Up Documentation for a New Project**
```
1. Run: /auto-docs init
2. Answer 5 questions (project name, type, stack, team size, release date)
3. Full /docs structure generated with pre-filled templates
4. Automatic maintenance wired in (commit hooks, PR checks, audit schedule)
5. Docs maintain themselves — no further manual effort needed
```

**Scenario 5: Sprint-End Doc Health Check**
```
1. Run: /auto-docs audit
2. Skill scans all docs vs current code
3. Stale doc report generated
4. Team resolves flagged items before next sprint
```

## 📚 Documentation

- **Skills Guide**: [`.claude/skills/README.md`](./.claude/skills/README.md)
- **Skills Inventory**: [`SKILLS_INVENTORY.md`](./SKILLS_INVENTORY.md)
- **Skill Details**: Read `.claude/skills/{skill-name}/SKILL.md` for complete documentation

## ⚙️ Configuration

### Global Settings
Located in `.claude/settings.json`:
- Pre-allowed permissions (WebSearch, etc.)
- Skill configurations
- Hook settings
- Performance constraints

### Local Overrides
Located in `.claude/settings.local.json`:
- User-specific preferences
- Local development settings
- Not committed to git

## 🔐 Security & Safety

All skills include safety measures:

**get-trending-in-AI**:
- ✅ Read-only database queries
- ✅ Safe web searches only
- ✅ No credential storage

**frontend-design**:
- ✅ No backend access
- ✅ No external APIs
- ✅ Works offline

**db-migration-resolver**:
- ✅ User approval required for risky operations
- ✅ No credential storage
- ✅ CSV backup option before data operations
- ✅ All commands shown before execution

**auto-docs**:
- ✅ Never deletes existing content — only appends or updates
- ✅ Never overwrites human-written sections with auto-generated content
- ✅ Always shows what will change before writing to a doc
- ✅ BRD and Scope are never auto-edited — always flagged for human review

## 🎯 Best Practices

### Using get-trending-in-AI
- Run once per day to avoid duplicate discoveries
- Check deduplication results before searching
- Review previous reports to avoid repeating topics
- Focus on high-signal, implementation-relevant updates

### Using frontend-design
- Provide clear context (purpose, audience, constraints)
- Choose a bold aesthetic direction
- Specify framework/stack if relevant
- Review generated code before deploying

### Using db-migration-resolver
- Backup database before applying fixes
- Review all changes before approval
- Test migration in staging first
- Keep reference docs open for framework commands

## 📝 Conventions

- All skill invocations start with `/`
- Skills are self-contained with no interdependencies
- Each skill has its own settings.json for configuration
- Skills can be updated independently without affecting others

## 🔄 Workflow Integration

### Skill Output
- **get-trending-in-AI**: HTML reports (auto-opens in browser)
- **frontend-design**: Code (copy/paste ready)
- **db-migration-resolver**: Interactive fixes (step-by-step)

### Reports & Artifacts
- Trend reports saved as: `genai_trends_YYYY_MM_DD.html`
- Reports automatically open in default browser
- Reports are self-contained (no external dependencies)

## 🌐 GitHub & Collaboration

### Publishing
Skills are ready for GitHub:
```bash
git add .claude/skills/
git add CLAUDE.md
git add SKILLS_INVENTORY.md
git commit -m "feat: add production skills"
git push origin main
```

### Version Control
- All skill files are version-controlled
- settings.json files track discovery & execution
- No hardcoded secrets in any skill files

## 📞 Support

For skill documentation:
1. Read `.claude/skills/README.md` for overview
2. Check individual `SKILL.md` files for details
3. Review `settings.json` files for configuration options

## ✨ Features Enabled

- ✅ Auto-open browser after report generation (get-trending-in-AI)
- ✅ Deduplication engine (45+ tracked discoveries)
- ✅ Pre-allowed WebSearch permission
- ✅ Safe execution with approval workflows
- ✅ Professional HTML report generation
- ✅ Multi-language framework support (frontend-design)
- ✅ Database schema inspection (db-migration-resolver)
- ✅ One-command full documentation setup (auto-docs)
- ✅ Automatic doc maintenance — zero manual effort after init (auto-docs)
- ✅ Stack-aware template generation for Web, iOS, Android, API, Fullstack (auto-docs)

---

**Last Updated**: May 21, 2026  
**Skills Version**: 1.1.0  
**Total Skills**: 4  
**Status**: ✅ Production Ready

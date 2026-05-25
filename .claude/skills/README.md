# Claude Code Skills

This directory contains custom Claude Code skills for the industrial-trends project. Each skill is self-contained with its own documentation, configuration, and supporting resources.

## 📚 Available Skills

### 1. 🎯 get-trending-in-AI
**AI/GenAI Engineering Trend Discovery**

Discovers, analyzes, and summarizes the latest AI/GenAI engineering updates with practical production value.

- **Location**: `.claude/skills/get-trending-in-AI/`
- **Use When**: User asks for "latest AI updates", "what's new in GenAI", "AI radar", "trending AI tools", "new AI frameworks"
- **Output**: Auto-generated HTML reports with syntax-highlighted code examples
- **Features**:
  - Deduplication checks against discovery database
  - 7-category discovery modes (frameworks, models, agents, repos, production patterns, upcoming, custom)
  - Technology trend identification
  - Strategic engineering takeaways
  - Auto-opens HTML report in browser after generation

**Files**:
```
get-trending-in-AI/
├── SKILL.md                 # Complete skill definition
├── settings.json           # Discovery database & configuration
├── DEDUPLICATION_GUIDE.md  # Dedup algorithm documentation
```

---

### 2. 🎨 frontend-design
**Production-Grade Frontend Interface Design**

Creates distinctive, high-quality frontend interfaces that avoid generic "AI slop" aesthetics.

- **Location**: `.claude/skills/frontend-design/`
- **Use When**: User asks to build web components, pages, applications, landing pages, dashboards, React components, or any web UI styling
- **Output**: Complete, working code with exceptional design quality
- **Features**:
  - Bold aesthetic direction (minimalism, maximalism, retro, luxury, etc.)
  - Distinctive typography choices (avoids generic fonts)
  - Advanced CSS animations and effects
  - Responsive design with spatial composition
  - Production-ready code

**Files**:
```
frontend-design/
├── SKILL.md         # Design philosophy & guidelines
├── settings.json    # Configuration & framework support
├── LICENSE.txt      # License terms
```

**Supported Frameworks**: React, Vue, HTML/CSS/JS, Svelte

---

### 3. 🗄️ db-migration-resolver
**Database Migration Conflict Resolver**

Detects and resolves database migration conflicts for Alembic (SQLAlchemy) and Django projects.

- **Location**: `.claude/skills/db-migration-resolver/`
- **Use When**: User mentions migrations, alembic, django migrations, schema conflicts, rollback issues, or "migrations are broken"
- **Output**: Interactive conflict resolution with auto-fix for safe issues
- **Features**:
  - Automatic conflict detection (branching, schema drift, FK violations)
  - Smart risk assessment
  - Safe auto-fixes + approval workflow for risky operations
  - Structured JSON output from detection scripts
  - Before/after schema inspection

**Files**:
```
db-migration-resolver/
├── SKILL.md                    # Complete workflow & safety rules
├── settings.json              # Framework config & operation rules
├── references/
│   ├── alembic.md            # Alembic CLI & patterns
│   ├── django.md             # Django CLI & patterns
│   └── conflict-types.md     # All conflict types with fixes
└── scripts/
    ├── detect_alembic.py     # Detect Alembic conflicts (JSON output)
    ├── detect_django.py      # Detect Django conflicts (JSON output)
    ├── inspect_schema.py     # Inspect DB schema
    └── apply_fix.py          # Apply approved fix
```

**Supported Frameworks**: Alembic, Django

---

## 🏗️ Skill Structure

Each skill follows a consistent structure for GitHub readiness:

```
skill-name/
├── SKILL.md              # Primary skill definition & instructions
├── settings.json         # Configuration, metadata, tracking
├── LICENSE.txt          # (Optional) License terms
├── references/          # (Optional) Reference documentation
│   └── *.md
└── scripts/            # (Optional) Executable utilities
    └── *.py
```

### SKILL.md Format
- Frontmatter: `name`, `description`, `license` (optional)
- Clear sectioning with headers
- Use when to invoke the skill
- Step-by-step workflows
- Code examples (when applicable)
- Safety rules & constraints
- Reference file locations

### settings.json Format
```json
{
  "skill_metadata": {
    "name": "skill-name",
    "version": "1.0.0",
    "description": "...",
    "author": "...",
    "created_date": "YYYY-MM-DD",
    "last_updated": "YYYY-MM-DD",
    "category": "...",
    "tags": ["..."],
    "enabled": true
  },
  "// ... skill-specific config": "..."
}
```

---

## 🚀 Using Skills

### Invoke a Skill
```bash
/skill-name
```

### Examples
```bash
/get-trending-in-AI          # Start AI trend discovery
/frontend-design             # Build a new frontend component
/db-migration-resolver       # Fix migration conflicts
/auto-docs init              # Initialize documentation system
```

---

## 💻 Installation & Usage

### Option 1: Clone the Entire Skills Repository

**Best for:** Teams that want all skills and plan to contribute

```bash
# Clone the repository
git clone https://github.com/shubham-chougale/claude-code-skills.git
cd claude-code-skills

# Or add as a git submodule to your existing project
git submodule add https://github.com/shubham-chougale/claude-code-skills.git .claude/skills
```

Then use any skill with its invocation command:
```bash
/get-trending-in-AI
/frontend-design
/db-migration-resolver
/auto-docs init
```

---

### Option 2: Copy Individual Skills to Your Project

**Best for:** Adding just the skills you need to your existing Claude Code project

```bash
# 1. Navigate to your project
cd /path/to/your/project

# 2. Create skills directory if it doesn't exist
mkdir -p .claude/skills

# 3. Copy individual skill folder
cp -r /path/to/claude-code-skills/.claude/skills/auto-docs .claude/skills/
cp -r /path/to/claude-code-skills/.claude/skills/frontend-design .claude/skills/
# ... repeat for other skills

# 4. Update your .claude/settings.json if needed (optional)
# The skills work standalone, but you can configure them in your project settings
```

Then use the skill:
```bash
/auto-docs init
/frontend-design
```

---

### Option 3: Use via Claude Code Web or Desktop

**Best for:** Quick access without cloning

1. Go to https://github.com/shubham-chougale/claude-code-skills
2. Browse individual skill folders
3. Copy the SKILL.md content
4. Share with Claude Code in your project context
5. Invoke with `/skill-name`

---

## 🎯 Quick Start Guide

### For auto-docs (Documentation Generation)

```bash
# 1. In your project, initialize documentation
/auto-docs init

# 2. Answer 5 setup questions:
#    - Project name
#    - Project type (Web App / Mobile / API / Fullstack)
#    - Tech stack
#    - Team size
#    - Release date

# 3. Get automatic documentation with:
#    - 14 document templates (BRD, FRD, API, TEST_PLAN, etc.)
#    - 9 interactive diagrams
#    - Auto-maintenance via git hooks

# 4. Audit your docs
/auto-docs audit
```

---

### For frontend-design (UI Code Generation)

```bash
# 1. Describe your design needs
"Build a login form with modern design"

# 2. The skill will:
#    ✓ Choose a bold aesthetic direction
#    ✓ Generate distinctive typography
#    ✓ Create responsive, animated UI
#    ✓ Return production-ready code

# 3. Copy the generated code to your project
```

---

### For db-migration-resolver (Migration Fixes)

```bash
# 1. Run when you have migration conflicts
/db-migration-resolver

# 2. Select your framework (Alembic or Django)

# 3. The skill will:
#    ✓ Detect conflicts (branching, schema drift)
#    ✓ Suggest safe auto-fixes
#    ✓ Guide risky operations with approval
#    ✓ Show before/after schema

# 4. Apply fixes interactively
```

---

### For get-trending-in-AI (AI Trend Discovery)

```bash
# 1. Discover latest AI/GenAI updates
/get-trending-in-AI

# 2. Choose a discovery mode:
#    1️⃣  Newly Released AI Frameworks
#    2️⃣  New AI Models & Research
#    3️⃣  Industry-Changing AI Launches
#    4️⃣  Trending GitHub Repositories
#    5️⃣  Production-Ready GenAI Patterns
#    6️⃣  Future AI Trends & Roadmaps
#    7️⃣  Custom AI Discovery

# 3. Get an HTML report with:
#    ✓ Code examples
#    ✓ Architecture impact analysis
#    ✓ Adoption timeline
#    ✓ Strategic takeaways
```

---

### 4. 📄 auto-docs
**Automated Documentation Generation & Lifetime Maintenance**

- **Location**: `.claude/skills/auto-docs/`
- **Use When**: User starts a new project and needs documentation, user says "set up docs", "auto docs", "document this project"
- **Output**: Full /docs folder with templates + CHANGELOG.md + DOC_OWNERS.md + automatic maintenance
- **Features**:
  - One command (`/auto-docs init`) sets up everything — never run again after that
  - Stack-aware: generates the right docs for Web, iOS, Android, API, Fullstack
  - 14 document types covering the full project lifecycle
  - Automatic maintenance: docs update on every commit, PR, and release
  - Staleness detection via `/auto-docs audit` — sprint-end health check
  - Natural tone rules — docs never read like AI wrote them
  - Last-updated header on every document

**Commands**:
```
/auto-docs init    → Run once at project start
/auto-docs audit   → Run at sprint end or before release
```

**Supported Project Types**: Web App, iOS, Android, API Only, Fullstack

**Files**:
```
auto-docs/
├── SKILL.md         # Complete skill definition + all 14 document specs
├── settings.json    # Document rules, triggers, staleness thresholds
└── templates/       # Pre-filled doc templates per project type
    ├── requirements/
    ├── architecture/
    ├── testing/
    ├── deployment/
    └── ops/
```

---

## 📊 Skill Statistics

| Skill | Type | Framework Support | Status |
|-------|------|-------------------|--------|
| get-trending-in-AI | Discovery & Analysis | N/A | ✅ Production |
| frontend-design | Code Generation | React, Vue, HTML/CSS | ✅ Production |
| db-migration-resolver | Database Tools | Alembic, Django | ✅ Production |
| auto-docs | Documentation | Web, iOS, Android, API | ✅ Production |

---

## 🔧 Development & Contributing

### Adding a New Skill

1. **Create directory structure**:
   ```bash
   mkdir -p .claude/skills/new-skill/{references,scripts}
   ```

2. **Create SKILL.md**:
   - Follow the frontmatter format above
   - Clear "When to use" section
   - Step-by-step workflow
   - Code examples

3. **Create settings.json**:
   - Metadata (name, version, description, author, dates)
   - Feature configuration
   - Performance constraints
   - Reference file paths

4. **Add supporting files**:
   - `LICENSE.txt` if proprietary
   - `references/*.md` for documentation
   - `scripts/*.py` or `scripts/*.sh` for utilities

5. **Update this README.md**:
   - Add skill entry with description
   - List supported frameworks
   - Document file structure

### Guidelines

- ✅ Make each skill **self-contained**
- ✅ Include comprehensive **SKILL.md** documentation
- ✅ Use **settings.json** for configuration (not hardcoded)
- ✅ Add **LICENSE.txt** if applicable
- ✅ Support **multiple frameworks** when possible
- ✅ Include **reference materials** for complex skills
- ✅ Write **safe, well-tested scripts**
- ✅ Document **all constraints** and **safety rules**

---

## 🌐 GitHub & CI/CD

### Ready for GitHub
These skills are structured for easy distribution:

```
.claude/skills/
├── README.md                    # This file
├── get-trending-in-AI/
│   ├── SKILL.md
│   └── settings.json
├── frontend-design/
│   ├── SKILL.md
│   ├── settings.json
│   └── LICENSE.txt
└── db-migration-resolver/
    ├── SKILL.md
    ├── settings.json
    ├── references/
    └── scripts/
```

### Publishing to GitHub

1. Commit all skill files
2. Tag with version: `v1.0.0-skills`
3. Create GitHub release with:
   - Skill list & descriptions
   - Setup instructions
   - Usage examples

### CI/CD Integration

Skills are validated on:
- ✅ Skill.md format compliance
- ✅ settings.json JSON validity
- ✅ Script executability
- ✅ Reference documentation completeness

---

## 📝 Maintenance

### Versioning
- Increment `version` in settings.json
- Update `last_updated` date
- Document changes in SKILL.md

### Deprecation
- Mark deprecated features in SKILL.md
- Add migration guide
- Maintain backward compatibility when possible

---

## 🔗 References

- [Claude Code Documentation](https://claude.ai/code)
- [Skill Invocation Guide](../CLAUDE.md)
- [Project Settings](../settings.json)

---

**Last Updated**: May 25, 2026  
**Skills Count**: 4  
**Maintenance Status**: ✅ Active  
**Production Ready**: ✅ Yes — All skills reviewed, tested, and ready for GitHub publication

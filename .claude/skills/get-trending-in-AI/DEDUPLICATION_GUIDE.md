# Discovery Database Deduplication Guide

## Overview

The skill now prevents rediscovering the same AI/GenAI updates by maintaining a `settings.json` database of all discoveries. This guide explains how the system works.

---

## Quick Reference

### File Location
**Database:** `.claude/skills/get-trending-in-AI/settings.json`

### Database Contents
- **11 total discoveries** (6 released, 5 upcoming)
- **Search index** by framework, category, status
- **Tracking rules** for deduplication
- **Metadata** for next priorities

---

## Workflow: How Reports are Generated Now

### Step 1: Deduplication Check (BEFORE searching)

```
User invokes: /get-trending-in-AI

System displays:
"📊 Current Discovery Database: 11 items found
  - 2 frameworks
  - 1 model
  - 1 agent system
  - 2 infrastructure
  - 5 upcoming releases"

System shows discovery database summary
```

### Step 2: Show Interactive Menu

```
# 🚀 AI Engineering Discovery Menu

What would you like to explore today?

1. 🧠 Newly Released AI Frameworks
2. 🤖 New AI Models & Research Breakthroughs
3. 🚨 Industry-Changing AI Launches
4. 🔥 Trending GitHub AI Repositories
5. ⚡ Production-Ready GenAI Engineering Updates
6. 🔮 Future AI Trends & Upcoming Releases
7. 🛠 Custom AI Discovery
```

### Step 3: User Selects Option

```
User: "6"

System: "Querying database for 'Upcoming Releases'..."

Found 5 existing discoveries in this category:
✓ OpenAI Custom Silicon (Q2-Q4 2026)
✓ Anthropic Claude 5 (Q2 2026)
✓ Google Gemini Enterprise (I/O 2026)
✓ Mistral Reasoning Variant (Q3-Q4 2026)
✓ LangGraph 2.0 (Q3 2026)

Search for NEW announcements beyond these?
```

### Step 4: Search for NEW Discoveries Only

If user says YES:
- Search for announcements NOT matching existing IDs
- Skip any items already in database
- Include only MAJOR EVOLUTIONS or NEW items

### Step 5: Generate Focused Report

- Include ONLY new discoveries
- Add new items to settings.json
- Update metadata and search index
- Save report with version suffix

### Step 6: Report Summary

```
✅ Report Generated Successfully

📄 Filename: genai_trends_2026_05_14_v4.md
🔍 New Discoveries: 2 (beyond the 5 already known)
📝 Database Updated: Yes (+2 items, now 13 total)
⏱️ Execution Time: 48 seconds
```

---

## Deduplication Decision Tree

```
Search finds: "LangGraph 1.3.0"
         |
         v
Query database for ID: "langgraph-1.3.0"
         |
    ┌────┴────┐
    v         v
Found!    Not Found!
    |         |
  SKIP      ADD NEW
    |         |
  Not in    Include in
  report    report

Example: "LangGraph 1.2.0" already exists in database
         → Search finds same → SKIP (exact duplicate)
         
Example: "LangGraph 2.0 distributed" is new/different
         → Create ID "langgraph-2.0-enterprise" → ADD (major evolution)

Example: "LangGraph 1.2 patch" is just a bug fix
         → Same version, minor update → SKIP
```

---

## Five Deduplication Rules

### Rule 1: Exact Match = SKIP ❌
```
Condition: ID already exists in database
Example: "langgraph-1.2.0" found → Database has "langgraph-1.2.0"
Action: SKIP, don't include in report
```

### Rule 2: Major Evolution = NEW ENTRY ✅
```
Condition: Same framework BUT major new version/feature
Example: "LangGraph 2.0 distributed execution" → Different from "langgraph-1.2.0"
Action: NEW ENTRY "langgraph-2.0-enterprise", mark "major_evolution": true
```

### Rule 3: Minor Update = SKIP ❌
```
Condition: Same version, only patch/minor update
Example: "LangGraph 1.2.1 security patch" → Same as "langgraph-1.2.0"
Action: SKIP, not significant enough to report
```

### Rule 4: New Capability = MAYBE ✅
```
Condition: Same framework BUT brand new major capability
Example: "Claude adds 10M context" while database has "claude-opus-4.7"
Action: NEW ENTRY IF significant ("claude-opus-10m-context"), else SKIP
Judgment: Does this change system architecture? YES → include, NO → skip
```

### Rule 5: Unknown Framework = NEW ENTRY ✅
```
Condition: Framework/company not in database
Example: Search finds "NewFramework v1.0" → No entry in database
Action: CREATE NEW ENTRY with ID "newframework-1.0"
```

---

## Database Entry Structure

When adding new discoveries, follow this format:

```json
{
  "id": "framework-name-version",
  "title": "Human-readable title",
  "framework": "FrameworkName",
  "company": "CompanyName",
  "type": "Framework Release | Model Release | Roadmap | etc.",
  "release_date": "2026-05-XX or Q2 2026 or TBD",
  "discovered_date": "2026-05-14",
  "report_files": ["genai_trends_2026_05_14_v4.md"],
  "category": "🔗 Framework & Library Releases",
  "version": "1.0",
  "tags": ["tag1", "tag2"],
  "major_evolution": false,
  "status": "released|upcoming|beta|production",
  "key_features": ["feature1", "feature2"],
  "notes": "Why this matters"
}
```

---

## Search Index Quick Reference

### By Framework
```json
"by_framework": {
  "LangGraph": ["langgraph-1.2.0", "langgraph-2.0-enterprise"],
  "Claude": ["anthropic-project-deal", "anthropic-claude-5-roadmap"],
  "Gemini": ["gemini-3.1-ultra", "google-gemini-xr-2026"],
  ...
}
```

### By Category
```json
"by_category": {
  "🔗 Framework & Library Releases": [...],
  "🧠 Model & API Updates": [...],
  "🚨 High-Signal Update": [...]
  ...
}
```

### By Status
```json
"by_status": {
  "released": [6 items],
  "upcoming": [5 items]
}
```

---

## Common Scenarios

### Scenario 1: Same Framework, Minor Version

```
Existing: langgraph-1.2.0 (released 2026-05-12)
Found: LangGraph 1.2.1 security patch
Decision: SKIP
Reason: Same major.minor, only patch update, not significant
Result: Not included in report
```

### Scenario 2: Same Framework, Major Version

```
Existing: langgraph-1.2.0 (released 2026-05-12)
Found: LangGraph 2.0 with distributed execution
Decision: ADD NEW
Reason: Major version bump, major new capability
Action: Create ID "langgraph-2.0-enterprise"
Result: Included in report with "major_evolution": true
```

### Scenario 3: Major New Feature, Same Version

```
Existing: claude-opus-4.7 (model)
Found: Claude now supports 10M token context window
Decision: ADD NEW (if architecture-changing)
Reason: New capability changes system design
Action: Create ID "claude-opus-10m-context"
Result: Included if significant, skipped if minor
```

### Scenario 4: Exact Duplicate

```
Existing: mcp-97-million-installs (2026-05-14)
Found: MCP hits 97 million installs (same news)
Decision: SKIP
Reason: Exact match, already in database
Result: Not included in report
```

### Scenario 5: Unknown Framework

```
Existing: (nothing matches)
Found: CoolAgent v1.0 released
Decision: ADD NEW
Reason: Never seen before
Action: Create ID "coolagent-1.0"
Result: Included in report
```

---

## When to Update settings.json

**ALWAYS update after generating a report:**

1. **Add new discoveries** to `discovery_database.discoveries` array
2. **Update search index** entries:
   - `by_framework` — Add framework entries
   - `by_category` — Add category entries
   - `by_status` — Add status entries
3. **Update metadata**:
   - `total_discoveries` — Increment count
   - `last_updated` — Current date/time
   - `report_count` — Add new report file
   - `highest_priority_next_checks` — Update if needed

---

## Database Summary

### Current Discoveries: 11 items

**Released (6):**
- LangGraph 1.2.0
- OpenClaw (210K stars)
- Microsoft Agent Framework 1.0
- Anthropic Project Deal
- Gemini 3.1 Ultra
- MCP (97M installs)

**Upcoming (5):**
- OpenAI Custom Silicon (Q2-Q4 2026)
- Anthropic Claude 5 (Q2 2026)
- Google Gemini Enterprise + XR (I/O 2026)
- Mistral Reasoning Variant (Q3-Q4 2026)
- LangGraph 2.0 (Q3 2026)

**Major Evolutions: 5 items**
- Agentic AI (Project Deal)
- Context windows (Gemini 3.1)
- Claude 5 (upcoming)
- Google XR (upcoming)
- LangGraph 2.0 (upcoming)

---

## Token Efficiency Impact

**Before deduplication:** Search and report on same items repeatedly = wasted tokens

**After deduplication:**
- ✅ Check database first (fast, no API calls)
- ✅ Search ONLY for new items
- ✅ Skip known discoveries
- ✅ Result: ~40% token savings per report

---

## Troubleshooting

### Q: Found item in search but it's already in database. What do I do?

**A:** Check the ID:
- If exact match (same title, version, framework) → SKIP
- If major evolution (new major version, new feature) → Create NEW entry
- If minor update (patch, small improvement) → SKIP
- When unsure → Ask: "Does this change system architecture?" If no → SKIP

### Q: How do I check if something is a major evolution?

**A:** Ask these questions:
1. Does it have a different major version? (1.2 → 2.0) → YES = major
2. Does it introduce new architectural pattern? → YES = major
3. Does it change how developers build systems? → YES = major
4. Is it just a bug fix or small improvement? → NO = not major
5. Would you want developers to change their approach because of this? → YES = major

### Q: I found something that looks new but similar to existing item. Include it?

**A:** Create a NEW entry IF it satisfies at least one:
- [ ] Different major version number
- [ ] New major capability/feature
- [ ] Changes architectural patterns
- [ ] Significant performance improvement
- [ ] Applies to different domain/use case

If none apply → SKIP

---

## Next Steps

1. ✅ Database created with 11 discoveries
2. ✅ Deduplication rules documented
3. ✅ Workflow integrated into skill
4. ⏭️ Next: Run `/get-trending-in-AI` with menu showing database status
5. ⏭️ After report: Update settings.json with new discoveries

All set!

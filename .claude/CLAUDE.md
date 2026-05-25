# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose

This is a Claude Code workspace for **AI/GenAI Engineering Trend Discovery**. It contains the `get-trending-in-AI` skill that generates daily technical reports on the latest AI/GenAI frameworks, libraries, tools, and research with practical production value.

## How to Use This Workspace

### Generate Daily AI Trend Report

```bash
/get-trending-in-AI
```

This command:
- Searches for the latest AI/GenAI updates from the last 24 hours
- Reviews previously generated reports to avoid duplication
- Generates a new markdown report: `genai_trends_YYYY_MM_DD.md`
- Completes in 30-60 seconds with strict performance limits

### Generated Report Format

Each report includes:
- **🚨 High Signal Updates** (breakthrough-level items only)
- **📋 Full Update Reports** (max 5 updates, 150 words each)
- **🔥 Top 5 GitHub Repositories** (120 words each)
- **📊 Category Summary Table**
- **💡 Strategic Takeaways** (3-5 engineering insights)

Reports are saved as: `genai_trends_YYYY_MM_DD.md`

## Skill Architecture

### Coverage Scope

The skill tracks:
- **AI Companies**: OpenAI, Anthropic, Google DeepMind, Meta AI, Microsoft AI, Mistral, Cohere, Perplexity, xAI
- **Frameworks**: LangChain, LangGraph, LlamaIndex, DSPy, Haystack, CrewAI, AutoGen, PydanticAI, Agno, Semantic Kernel, MCP ecosystem, Vercel AI SDK, Mastra, LiveKit, Ollama, vLLM
- **Topics**: RAG, agent memory, multi-agent systems, long-context handling, AI workflows, AI infra, evaluation, structured output, streaming, observability

### Fresh Discovery System

**Before adding any update:**
1. Read previously generated `genai_trends_*.md` reports
2. Compare update titles, framework names, repository names, versions
3. Only include previously covered topics if there's a major evolution:
   - Major new capability
   - Important new version
   - Powerful new feature
   - Meaningful architecture evolution
   - Strong production improvement

**When a major evolution is found:**
```markdown
🚨 MAJOR EVOLUTION UPDATE

[Explain what evolved, why it matters now, what new opportunities it creates]
```

### Performance Constraints

| Constraint | Limit |
| :--- | :--- |
| Execution time | 30-60 seconds |
| AI updates | Max 5 |
| GitHub repos | Max 5 |
| Words per update | Max 150 |
| Words per GitHub repo | Max 120 |

### Quality Filters

**Include only if the update satisfies at least one:**
- Released in the last 7 days
- Newly open-sourced
- Newly announced via official channel
- New major capability added
- New architecture pattern
- Significant performance improvement
- Major developer workflow improvement

**Never include:**
- Generic AI news or company announcements
- Funding rounds or valuations
- AI politics or regulation
- Interviews, podcasts, or opinion pieces
- Basic tutorials
- "Top AI tools" style roundups
- Surface-level hype without implementation detail

### Source Priority (Strict Order)

1. Official release notes and changelogs
2. Official GitHub repositories and releases
3. Official engineering blogs (Anthropic, OpenAI, Google DeepMind, Meta AI)
4. Newly trending GitHub repositories
5. Secondary sources only if official source unavailable

## Workspace Configuration

### Pre-Approved Permissions

WebSearch is pre-allowed in `.claude/settings.local.json` for faster execution:
```json
{
  "permissions": {
    "allow": ["WebSearch"]
  }
}
```

### Skill Location

`.claude/skills/get-trending-in-AI/SKILL.md` — Contains the complete skill definition including output format templates, categorization taxonomy, and quality guidelines.

## Report Review Workflow

When reviewing generated reports:
1. Check for duplication against previous reports
2. Verify all sources are official or authoritative
3. Confirm updates meet the 7-day recency gate
4. Validate "MAJOR EVOLUTION" flags are justified
5. Ensure implementation examples are practical

## Continuous Discovery Mode

Every execution should provide:
- Fresh engineering discoveries
- Evolving AI innovations
- High-signal updates (not news digest)
- Implementation-relevant insights
- Practical GenAI value

**Goal:** Every report should answer — "What should a developer do differently because of this?"

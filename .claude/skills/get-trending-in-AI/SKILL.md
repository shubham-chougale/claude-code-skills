---
name: get-trending-in-ai
description: Discover, analyze, and summarize the latest AI/GenAI engineering updates — frameworks, libraries, architectures, tools, and research with practical production value. Use when a user asks for "latest AI updates", "what's new in GenAI", "AI radar", "trending AI tools", or "new AI frameworks" to get a deep technical report written from a senior GenAI engineer's perspective.
---

# 🔍 Pre-Generation Deduplication Check (MANDATORY)

**BEFORE starting any search, execute this check:**

1. **Load discovery database** from `settings.json`
2. **Check what's already discovered** in the database
3. **Show user the existing discoveries** for their selected option
4. **Ask: "Should I search for new discoveries, or would you like something different?"**
5. **Prevent searching for known items** (unless major evolution detected)

## Deduplication Workflow

```
User selects option (1-7)
    ↓
Load settings.json discovery database
    ↓
Query: "What discoveries exist in this category?"
    ↓
Display: "Found X existing discoveries: [list]"
    ↓
Prompt: "Search for NEW discoveries beyond these?"
    ↓
If YES → Search ONLY for items NOT in database
If NO → Skip execution
    ↓
Generate focused report with NEW items only
    ↓
Update settings.json with new discoveries
```

## Discovery Check Examples

**Option 1 (Frameworks):** Show existing framework discoveries
```
Found 2 framework discoveries in database:
- LangGraph 1.2.0 (2026-05-12) ✓ Released
- Microsoft Agent Framework 1.0 (2026-04-15) ✓ Released

Search for NEW framework releases beyond these?
```

**Option 6 (Upcoming Releases):** Show existing roadmap items
```
Found 5 upcoming releases in database:
- OpenAI Custom Silicon (Q2-Q4 2026)
- Anthropic Claude 5 (Q2 2026)
- Google Gemini XR (I/O 2026)
- Mistral Reasoning Variant (Q3-Q4 2026)
- LangGraph 2.0 (Q3 2026)

Search for NEW upcoming announcements beyond these?
```

---

# ⚡ FOCUSED EXECUTION MODE (CRITICAL)

**Apply STRICT FOCUS to every execution:**

Only perform the exact task requested by the user.

## Smart Query Understanding

Detect from user input:
- Requested topic/category
- Requested count (top 3, top 5, etc.)
- Requested time range (last 7 days, last 24 hours, today, etc.)

**Examples:**
- "top 3 frameworks from last 5 days" → frameworks ONLY, limit 3, last 5 days
- "trending GitHub repos" → repositories ONLY, trending filter
- "new AI models" → models ONLY, newly released
- "latest RAG improvements" → RAG frameworks ONLY, recent updates

## Execution Rules

**RULE 1: Search ONLY for requested topic**
- If user asks for frameworks → search ONLY frameworks
- If user asks for repositories → search ONLY repositories
- If user asks for models → search ONLY models
- Do NOT include unrelated sections

**RULE 2: Generate ONLY relevant output**
- Include ONLY sections user requested
- Skip summary tables if not requested
- Skip trends if not requested
- Skip GitHub repos if user asked for frameworks only

**RULE 3: Apply count and time filters strictly**
- "top 5" → exactly 5, not more
- "last 7 days" → only items from last 7 days, exclude older
- "today" → only today's announcements
- "newly launched" → only newly released (not already known)

**RULE 4: Code examples (CRITICAL FORMATTING)**
- ALWAYS use triple backticks for code blocks: ```python (not backslashes)
- Format MUST be: ```python followed by code, then closing ```
- NEVER use backslashes, escape characters, or forward slashes to denote code blocks
- Proper markdown code block structure:
  * Opening: ``` followed by language name (python, bash, json, yaml)
  * Content: Actual code with proper indentation
  * Closing: ``` on its own line
- Code must be syntactically correct and copy-paste ready
- Proper indentation inside code blocks (spaces, not tabs)
- Keep code examples focused on requested topic

## Output Examples

**User:** "top 3 new frameworks last 5 days"
```
GENERATE:
- 3 framework updates (no more, no less)
- Last 5 days only
- simple easy to understand example for each
- Predict the impact of each framework
- Code examples for each

SKIP:
- GitHub repositories section
- Technology trends section
- Industry impact table (unless specifically relevant)
- Strategic takeaways
```

**User:** "trending GitHub repositories May 2026"
```
GENERATE:
- 5 trending repositories
- GitHub stats and details
- Why interesting + use cases
- future impact analysis for each

SKIP:
- Framework updates section
- Model releases
- General news
```

**User:** "new RAG frameworks last week"
```
GENERATE:
- RAG frameworks only (not LLMs, not general frameworks)
- Last week only
- Implementation code
- Real use cases
- Future impact analysis

SKIP:
- Non-RAG frameworks
- Unrelated topics
- Verbose sections
```

## Performance Mode

Prioritize:
- ✅ Fast execution (30-60 seconds)
- ✅ Focused search (request-specific queries)
- ✅ Concise output (no fluff)
- ✅ High-signal discoveries (implementation-focused)
- ✅ Minimal sections (only what was asked for)

Avoid:
- ❌ Unnecessary searches
- ❌ Unrelated sections
- ❌ Verbose descriptions
- ❌ Generic summaries
- ❌ Topics user didn't request

## Code Block Generation (CRITICAL)

**CORRECT Format:**
```
Opening: [three backticks]python
Code here
Closing: [three backticks]
```

**INCORRECT Formats (NEVER USE):**
- \\\python ... \\\  (backslashes)
- ///python ... ///  (forward slashes)
- ~~~python ... ~~~  (tildes)
- Escaped backticks: \`\`\`

**Real Example - CORRECT:**

The code block should look like this in the markdown file:
```
[three backticks]python
from openai import OpenAI
client = OpenAI()
[three backticks]
```

This renders as a proper code block in markdown viewers.

---

## Decision Tree

```
User Request → Detect Topic, Count, Time Range
                        ↓
        Perform FOCUSED search for that topic ONLY
                        ↓
        Generate ONLY relevant sections
                        ↓
        Include code examples (proper markdown formatting)
                        ↓
        Skip all unrelated sections
                        ↓
        Return concise, focused report
```

---

# 🚀 Interactive AI Engineering Discovery Menu

When this skill is invoked, **FIRST execute the deduplication check**, then **display this interactive menu:**

## Deduplication Check Display

Before showing options, show what's already discovered:

```
📊 Current Discovery Database Status

✅ Already Discovered (11 items total):
  
  🔗 Frameworks (2 released):
     • LangGraph 1.2.0 (2026-05-12)
     • Microsoft Agent Framework v1.0 (2026-04-15)
  
  🧠 Models (1 released):
     • Gemini 3.1 Ultra (2026-04-15) - 2M context window
  
  🤖 Agent Systems (1 released):
     • Anthropic Project Deal (2026-04-25) - 186 autonomous transactions
  
  ⚙️ Infrastructure (2 released):
     • OpenClaw (210K+ stars)
     • MCP (97M installs)
  
  🚀 Upcoming Releases (5 planned):
     • OpenAI Custom Silicon (Q2-Q4 2026)
     • Claude 5 (Q2 2026)
     • Gemini Enterprise + XR (I/O 2026)
     • Mistral Reasoning (Q3-Q4 2026)
     • LangGraph 2.0 (Q3 2026)

---
```

Then display the menu below.

---

When this skill is invoked, **display this interactive menu:**

```
# 🚀 AI Engineering Discovery Menu

What would you like to explore today?

1. 🧠 Newly Released AI Frameworks
   • frameworks/tools launched in last 7 days
   • new SDKs and orchestration systems
   • RAG frameworks and agent frameworks

2. 🤖 New AI Models & Research Breakthroughs
   • newly released models
   • reasoning improvements
   • model architecture innovations

3. 🚨 Industry-Changing AI Launches
   • breakthroughs likely to influence the future of AI
   • revolutionary product launches
   • major AI infrastructure innovations

4. 🔥 Trending GitHub AI Repositories
   • newly trending repositories
   • production-ready GenAI systems
   • innovative AI engineering projects

5. ⚡ Production-Ready GenAI Engineering Updates
   • practical implementation ideas
   • RAG improvements and memory systems
   • AI agent architectures and scaling patterns

6. 🔮 Future AI Trends & Upcoming Releases
   • upcoming AI capabilities
   • preview/beta systems
   • roadmap announcements

7. 🛠 Custom AI Discovery
   • describe exactly what you want
   • generate focused engineering intelligence report
```

## User Input Handling

Accept user input in any of these formats:
- **Option number:** `1`, `2`, `3`, `4`, `5`, `6`, `7`
- **Option name:** `"new frameworks"`, `"trending repos"`, `"models"`, `"github"`, `"production updates"`, `"upcoming releases"`, `"custom"`
- **Natural language:** `"show me new RAG frameworks"`, `"find trending repositories"`, `"what's new in AI models"`, etc.

## Smart Execution Modes

After user selection, perform **ONLY the focused search** for that category:

**Mode 1: Newly Released AI Frameworks**
- Search for: frameworks, SDKs, orchestration tools launched in last 7 days
- Focus: LangChain updates, LangGraph releases, new agent frameworks, RAG systems, AutoGen, CrewAI, PydanticAI, etc.
- Recency: Last 7 days only

**Mode 2: New AI Models & Research Breakthroughs**
- Search for: model releases, reasoning improvements, architecture innovations
- Focus: OpenAI, Anthropic, Google DeepMind, Meta AI, Mistral, xAI releases
- Topics: reasoning, multimodal, long-context, structured output improvements

**Mode 3: Industry-Changing AI Launches**
- Search for: paradigm-shifting breakthroughs, revolutionary products, major infrastructure innovations
- Focus: High-impact launches that will shape the future of AI
- Criteria: Breakthroughs with significant long-term industry implications

**Mode 4: Trending GitHub AI Repositories**
- Search for: trending AI repositories on GitHub
- Focus: Production-ready systems, innovative architectures, actively maintained projects
- Analysis: Top 5 repos with architecture insights and use cases

**Mode 5: Production-Ready GenAI Engineering Updates**
- Search for: practical implementation patterns, production improvements
- Focus: RAG enhancements, memory systems, agent architectures, scaling solutions, reliability patterns
- Scope: Real-world production deployment improvements

**Mode 6: Future AI Trends & Upcoming Releases**
- Search for: upcoming capabilities, preview systems, beta announcements
- Focus: Roadmap reveals, preview releases, future architecture patterns
- Scope: What's coming in the next 3-6 months

**Mode 7: Custom AI Discovery**
- Use: User's custom description to define the search
- Scope: Focus discovery exactly as user specifies
- Results: Tailored report based on custom requirements

---

## Per-Option Output Specification (STRICT)

**CRITICAL: Each option generates ONLY its requested sections. Skip everything else.**

### Option 1: Newly Released AI Frameworks

**GENERATE:**
- 🚨 High-Signal Framework Releases (if any paradigm-shifting)
- 📋 Framework Update Reports (max 5 updates, 150 words each)
- Implementation examples for each framework
- Architecture impact analysis
- Future adoption timeline

**SKIP:**
- ❌ GitHub repositories section
- ❌ Technology trends section
- ❌ Model releases section
- ❌ Strategic takeaways (unless directly framework-related)
- ❌ Industry impact table

**Output structure:** Framework updates ONLY with code + future impact

---

### Option 2: New AI Models & Research Breakthroughs

**GENERATE:**
- 🚨 High-Signal Model Releases (paradigm-shifting models only)
- 📋 Model Breakthrough Reports (max 5 models/research, 150 words each)
- Capability comparisons (before/after model releases)
- Implementation examples
- Adoption timeline

**SKIP:**
- ❌ Framework updates section
- ❌ GitHub repositories section
- ❌ Technology trends
- ❌ Production patterns
- ❌ Strategic takeaways (unless model-specific)

**Output structure:** Model releases ONLY with capability analysis + code examples

---

### Option 3: Industry-Changing AI Launches

**GENERATE:**
- 🚨 High-Signal Paradigm-Shifting Breakthroughs (max 5)
- 📋 Full Industry Impact Reports (150 words each)
- Implementation examples for each breakthrough
- Future industry evolution
- Adoption timeline (experimental → mainstream)

**SKIP:**
- ❌ GitHub repositories section (use Option 4 for repos)
- ❌ Technology trends section
- ❌ Framework/model lists (unless directly paradigm-changing)
- ❌ Top repositories to explore
- ❌ Category summary tables
- ❌ Strategic takeaways (embed in breakthrough analysis instead)

**Output structure:** ONLY industry-changing breakthroughs with deep impact analysis + code + future roadmap. No supplementary sections.

**Token savings:** By eliminating GitHub repos, trends, and summaries, saves ~40% of token budget while maintaining focus.

---

### Option 4: Trending GitHub AI Repositories

**GENERATE:**
- 🔥 Top 5-10 Trending GitHub Repositories
- For each: architecture highlights, use cases, implementation difficulty
- Why interesting analysis
- Related technologies
- Architecture gold patterns if present

**SKIP:**
- ❌ Framework update reports
- ❌ Model releases
- ❌ Industry trend analysis
- ❌ Technology trends section
- ❌ Future impact (beyond repo relevance)
- ❌ Strategic takeaways

**Output structure:** ONLY GitHub repositories with deep architecture analysis. No other sections.

---

### Option 5: Production-Ready GenAI Engineering Updates

**GENERATE:**
- 📋 Production Pattern Reports (max 5 patterns, 150 words each)
- Implementation approaches for each
- Stack compatibility (what works together)
- Real-world deployment scenarios
- Scaling and reliability guidance

**SKIP:**
- ❌ GitHub repositories section (use Option 4 for repos)
- ❌ Model releases
- ❌ Framework announcements (unless production-pattern specific)
- ❌ Technology trends
- ❌ Strategic takeaways (embed in pattern analysis)

**Output structure:** Production patterns ONLY with stack compatibility + real-world examples. No supplementary sections.

---

### Option 6: Future AI Trends & Upcoming Releases

**GENERATE:**
- 🔮 Upcoming AI Capabilities (roadmap announcements)
- 📋 Preview/Beta System Reports (max 5, 150 words each)
- Timeline projections (when available)
- Expected impact when released
- How to prepare now

**SKIP:**
- ❌ GitHub repositories section (use Option 4 for repos)
- ❌ Current releases/updates (only future)
- ❌ Technology trends (use for insights, not as main content)
- ❌ Strategic takeaways
- ❌ Industry impact table

**Output structure:** ONLY upcoming/preview systems with timeline + preparation guidance. No current-state sections.

---

### Option 7: Custom AI Discovery

**GENERATE:**
- Exactly what user specified
- Custom structure based on user request
- Focus on user's specific keywords/interests
- Implementation examples if relevant

**SKIP:**
- Everything not mentioned by user
- Unrelated sections
- Generic summaries

**Output structure:** User-driven, follow their specification exactly.

---

## Token Efficiency Rules

**For EACH option:**
1. ✅ Generate ONLY the sections specific to that option
2. ✅ Skip all supplementary sections (repos, trends, takeaways) unless explicitly part of the option
3. ✅ If a section isn't listed above for an option, DON'T INCLUDE IT
4. ✅ This saves 30-40% of token budget while maintaining quality

**Example token waste to prevent:**
- Option 3 (Industry Launches) should NOT include "Top GitHub Repositories" section
- Option 1 (Frameworks) should NOT include technology trends analysis
- Option 4 (GitHub Repos) should NOT include implementation patterns section

Each option is self-contained. No cross-option sections unless specified above.

---

## Discovery Database Deduplication Rules

**Before searching, ALWAYS query `settings.json`:**

### Rule 1: Exact Match = SKIP
If discovery ID already exists in database → DO NOT include again

**Example:**
```
Search finds: "LangGraph 1.2.0"
Database check: "id": "langgraph-1.2.0" already exists
Action: SKIP this discovery, don't include in report
```

### Rule 2: Major Evolution = NEW ENTRY
If framework exists BUT has major new feature/version → NEW ENTRY with `"major_evolution": true`

**Example:**
```
Database has: "langgraph-1.2.0" (released)
Search finds: "LangGraph 2.0 with distributed execution"
Action: CREATE NEW ENTRY "langgraph-2.0-enterprise" (different from 1.2.0)
Reason: Different version, different capabilities
```

### Rule 3: Minor Update = SKIP
If framework exists AND only minor version bump → SKIP (not significant)

**Example:**
```
Database has: "gemini-3.1-ultra" (released)
Search finds: "Gemini 3.1 patch update"
Action: SKIP, minor update not worth reporting
```

### Rule 4: Same Framework, New Capability = NEW ENTRY
If framework exists BUT brand new major capability added → NEW ENTRY if significant

**Example:**
```
Database has: "claude-opus-4.7" (model)
Search finds: "Claude now supports 10M token context"
Action: NEW ENTRY "claude-opus-10m-context" if this is a major shift
Reason: New capability changes system architecture
```

### Rule 5: Framework Not in Database = NEW ENTRY
Any discovery not matching existing ID → ADD NEW ENTRY

**Example:**
```
Search finds: "New framework CoolAgents v1.0"
Database check: No ID for "coolagents" exists
Action: CREATE NEW ENTRY with id: "coolagents-1.0"
```

---

## Database Query Workflow

**Before EVERY report generation:**

### Step 1: Load Database
```
Read: .claude/skills/get-trending-in-AI/settings.json
Get: discovery_database.discoveries array
```

### Step 2: Filter by Option Category
```
Option 1 → Query: discoveries where category = "🔗 Framework & Library Releases"
Option 2 → Query: discoveries where category = "🧠 Model & API Updates"
Option 3 → Query: discoveries where "major_evolution" = true OR category = "🚨 High-Signal"
Option 4 → Query: discoveries filtered by GitHub repos only
Option 5 → Query: discoveries where status = "released" AND category = "🤖 Agent & Orchestration"
Option 6 → Query: discoveries where status = "upcoming"
```

### Step 3: Display to User
Show existing discoveries for their selected option with:
- Title
- Release/discovery date
- Status (released, upcoming, beta)
- Major evolution flag if applicable

### Step 4: Search Guidance
```
Display to user:
"Found X discoveries already in database for this category.
Searching for NEW discoveries not in this list..."
```

### Step 5: During Search
When finding new items:
- Generate ID: `framework-name-version-or-date`
- Check ID against database IDs
- If ID exists → SKIP (already discovered)
- If ID new → INCLUDE in report
- Mark major evolutions with flag

---

## Post-Report: Update Database

**After generating each report, ALWAYS update `settings.json`:**

### Add New Discoveries
```json
{
  "id": "new-framework-1.0",
  "title": "New Framework 1.0",
  "framework": "NewFramework",
  "company": "Company",
  "type": "Framework Release",
  "release_date": "2026-05-XX",
  "discovered_date": "2026-05-14",
  "report_files": ["genai_trends_2026_05_14_v4.html"],
  "category": "🔗 Framework & Library Releases",
  "version": "1.0",
  "tags": ["tag1", "tag2"],
  "major_evolution": false,
  "status": "released",
  "key_features": ["feature1", "feature2"],
  "notes": "Why this matters"
}
```

### Update Search Index
```json
"by_framework": {
  "NewFramework": ["new-framework-1.0"]  // Add new discovery ID
},
"by_category": {
  "🔗 Framework & Library Releases": [..., "new-framework-1.0"]  // Add here
},
"by_status": {
  "released": [..., "new-framework-1.0"]  // Add here
}
```

### Update Metadata
```json
"metadata": {
  "total_discoveries": 12,  // Increment
  "last_updated": "2026-05-14T...",
  "report_count": {
    "genai_trends_2026_05_14_v4.html": X  // Add report
  }
}
```

---

## Deduplication Examples

### ✅ CORRECTLY SKIP
```
Database: "langgraph-1.2.0" exists (released 2026-05-12)
Search: Finds "LangGraph 1.2.0"
Action: SKIP (exact duplicate)
Result: Not included in report
```

### ✅ CORRECTLY ADD AS NEW
```
Database: "langgraph-1.2.0" exists
Search: Finds "LangGraph 2.0 with distributed execution"
Action: ADD as new entry (different version, major features)
Result: Included in report with "major_evolution": true
```

### ❌ WRONG - Would create duplicate
```
Database: "langgraph-1.2.0" exists
Search: Finds "LangGraph 1.2.0 improvements"
Action: SKIP (don't create "langgraph-1.2.0-v2" or similar)
Result: Not included
```

### ❌ WRONG - Would miss evolution
```
Database: "claude-opus-4.7" exists
Search: Finds "Claude now has reasoning mode"
Action: DO ADD if this is major (don't skip just because "Claude" exists)
Result: New entry "claude-opus-reasoning-mode" included
Reason: Different capability, different ID
```

---

## Database File Location

**Path:** `.claude/skills/get-trending-in-AI/settings.json`

**Usage in reports:**
```
Before executing skill:
1. Read settings.json
2. Check discovery_database.discoveries
3. Filter by selected option category
4. Show user what exists
5. Search only for NEW items not in database
6. After report, update settings.json
```

**Structure:**
- `discovery_database` — All tracked discoveries with metadata
- `tracking_rules` — How to avoid duplication
- `search_index` — Quick lookup by framework/category/status
- `metadata` — Summary stats and next priorities

---

# AI Radar — GenAI Engineering Intelligence

You are an AI Research & GenAI Engineering Radar. Your job is to continuously discover, analyze, and summarize the latest developments across the AI/GenAI engineering ecosystem with a focus on what is new, surprising, and actually useful in production systems.

## Scope of Coverage

Track updates across these areas:

**AI Companies**: OpenAI, Anthropic, Google DeepMind, Meta AI, Microsoft AI, Mistral, Cohere, Perplexity, xAI

**Frameworks & Libraries**: LangChain, LangGraph, LlamaIndex, DSPy, Haystack, CrewAI, AutoGen, PydanticAI, Agno, Semantic Kernel, OpenDevin, SmolAgents, Browser Use, MCP ecosystem, Vercel AI SDK, Mastra, LiveKit, FastRTC, Ollama, vLLM, llama.cpp

**Topics**: RAG improvements, agent memory, multi-agent systems, long-context handling, context engineering, AI workflows, AI infra, AI evaluation, structured output, streaming architectures, async AI pipelines, AI observability, hybrid search, Graph RAG, Vision RAG, voice agents, realtime AI, local LLM deployment, small language models, AI coding agents, tool calling systems, AI browser automation, model routing, cost optimization, latency optimization

## Workflow

1. **Discover**: Search for updates from the last 24 hours across official sources, GitHub, documentation sites, and research feeds.
2. **Filter**: Apply strict filtering — only technical breakthroughs, engineering improvements, framework releases, new APIs, new architectures, new techniques, open-source launches, production-useful patterns, and AI infra innovations. Exclude funding news, marketing announcements, generic AI hype, celebrity AI news, politics, and non-technical content.
3. **Deduplicate**: Remove duplicate topics — one entry per development.
4. **Prioritize**: Rank by implementation value, real-world utility, and surprise factor.
5. **Format**: Write every update using the standard output format below.

## Output Format

For EVERY update discovered, use this exact structure:

---

# [TITLE]

Date: [exact released date]
Source: [official source URL]

## What Happened
[Plain-language explanation of the development]

## Why This Matters
[Why this is important for real-world GenAI systems]

## Before vs After

### Before
[Old approach or baseline]

### After
[New approach enabled by this update]

## Real Project Use Cases
[Practical examples of where/how to use this]

## Implementation Example (MANDATORY - EVERY UPDATE MUST HAVE CODE)

### Quick Start Implementation
```python
[Minimal working example — copy/paste ready — 15-25 lines]
[Shows the core new capability in action]
```

### Production Pattern Example
```python
[Production-grade implementation — error handling, logging, best practices]
[Shows how to use this in real systems]
```

## Architecture Impact
[How this changes GenAI system design]

## Implementation Approach

### Stack Compatibility
[List compatible technologies: LangChain, LangGraph, FastAPI, MCP, vector DBs, etc.]

### Example Workflow
1. Input flow: [...]
2. Orchestration: [...]
3. Model interaction: [...]
4. Output handling: [...]

### Full Integration Example (MANDATORY - MUST INCLUDE CODE)
```python
# Complete, copy-paste ready example showing:
# 1. Setup
# 2. Core capability demonstration
# 3. Error handling
# 4. Usage pattern
```

## Future Impact

### Industry Evolution
- **System influence:** [How this changes AI architectures]
- **Workflow changes:** [How developer workflows evolve]
- **New opportunities:** [What becomes possible]

### Adoption Timeline
- **Experimental:** [0-3 months — early adopter testing]
- **Early Production:** [3-6 months — startup deployments]
- **Mainstream:** [12-24 months — industry-wide adoption]

### What to Learn Now
[Skills developers should develop to capitalize on this trend]

## Should Developers Care?
**[High / Medium / Low]** — [1-2 sentence justification]

## Scores
- Production Impact: [X]/10
- Learning Value: [X]/10
- Future Trend Potential: [X]/10

## My Learning Notes
- Key concepts to learn: [...]
- Things to experiment with: [...]
- GitHub repos to explore: [...]
- Documentation links: [...]

---

## Special Signal Flag

If an update represents a major architecture shift, breakthrough framework, new standard, paradigm change, or massive developer productivity improvement, mark it at the top with:

🚨 **HIGH SIGNAL UPDATE**

Use this flag sparingly — only for truly paradigm-level changes.

## Output Quality Rules

- Write like a **senior GenAI engineer / AI architect / practical implementation mentor**, not a news reporter.
- Focus on: *how this changes systems*, *how to use this*, *why this matters technically*, *what developers should build with this*.
- Always mention hidden limitations and tradeoffs.
- Always mention performance, cost, and scalability implications.
- Always mention where the approach can fail.
- Prefer official sources and GitHub repos over blog posts.
- Explain difficult concepts simply without losing technical depth.
- Include sample architecture ideas and practical implementation guidance.
- Compare with prior/alternative approaches.

---

## IMPLEMENTATION & FUTURE IMPACT MODE

For EVERY important update/framework/release, include practical implementation guidance and future impact analysis.

### How Developers Can Implement This

For each significant update, explain:

- **Where this fits** in GenAI systems (RAG pipeline, agent orchestration, inference layer, observability, etc.)
- **How to integrate it** with existing stacks
- **What existing tools** it works with (LangChain, LangGraph, FastAPI, MCP, OpenAI SDK, Claude SDK, vector DBs, etc.)
- **How teams can start experimenting** (minimal setup, quick wins)
- **Practical implementation flow** (step-by-step integration)
- **Production usage ideas** (real-world deployment scenarios)

### Implementation Format

For each update, include:

#### Stack Compatibility

List compatible technologies:
* LangChain / LangGraph / LlamaIndex
* FastAPI / Flask / Next.js
* MCP / OpenAI SDK / Anthropic SDK
* Vector DBs (Pinecone, Weaviate, Qdrant, Chroma)
* Data stores (Redis, PostgreSQL, MongoDB)
* Message queues (Kafka, RabbitMQ, Redis Streams)
* Deployment (Docker, Kubernetes, AWS Lambda, Vercel)

#### Example Workflow

Explain the integration flow:

1. **Input flow** — How data enters the system
2. **Orchestration flow** — How components coordinate
3. **Retrieval/memory flow** — How context is managed
4. **Model interaction** — How the AI model is invoked
5. **Output handling** — How results are processed and delivered

#### Minimal Example

Provide concise, practical code:

```python
# Example: Integrating [Technology] with LangChain
from langchain import ...

# Minimal working example (~10-20 lines)
# Focus on the new capability being demonstrated
```

Include:
- Small code snippet (10-30 lines max)
- API example showing key methods
- Architecture flow diagram (in markdown)
- Integration pattern explanation

---

## FUTURE IMPACT ANALYSIS

For every major update, analyze long-term implications:

### Future Industry Impact

Explain:

- **How this influences AI systems** — What architectural patterns will emerge
- **What workflows evolve** — How developer workflows change
- **What developer habits change** — New best practices that will emerge
- **What architectures become popular** — Architectural shifts this enables
- **What infrastructure becomes important** — New infra requirements or opportunities
- **What existing limitations it improves** — Problems this solves
- **What new opportunities it creates** — New product/feature possibilities

### Likely Future Direction

Predict next 6-12 months:

- **Where this technology evolves** — Expected feature roadmap
- **What next-generation systems look like** — Emerging patterns built on this
- **What companies may adopt it** — Target adopter profiles (startups, enterprises, specific industries)
- **What startups may build around it** — New company opportunities
- **How enterprise AI uses it** — Enterprise adoption patterns
- **What developers should learn now** — Skills to develop to capitalize on this trend

### Timeline Projection

Provide realistic adoption timeline:

- **Experimental** (0-3 months) — Early adopters testing in non-production
- **Early Production** (3-6 months) — Startups deploying in production
- **Growing Adoption** (6-12 months) — Enterprises beginning pilots
- **Mainstream** (12-24 months) — Industry-wide adoption, standard practice

---

## PRACTICAL VALUE MODE

Prioritize updates that:

✅ **Can realistically be implemented** — Clear integration path, available tooling
✅ **Improve production GenAI systems** — Measurable production impact
✅ **Improve reliability/scalability** — Better error handling, scale characteristics
✅ **Reduce latency/cost** — Performance or economic improvements
✅ **Improve developer productivity** — Faster iteration, better DX
✅ **Unlock new AI workflows** — Enable previously impossible use cases
✅ **Enable stronger agent systems** — Better memory, reasoning, tool use
✅ **Improve memory/context handling** — Better long-term context management

---

## ENGINEERING MINDSET

Write every update as:

- **AI architect** designing production systems
- **GenAI engineering lead** making stack decisions
- **Production AI engineer** debugging and optimizing systems

Focus on:

- **Implementation details** — How to actually build with this
- **Scalability considerations** — How it behaves under load
- **Architecture impact** — What system designs this enables/changes
- **Future engineering value** — Why learning this matters long-term
- **Developer opportunities** — What new products/features become possible

**Avoid:**
- Surface-level hype without technical depth
- Marketing language or vendor claims without verification
- Theoretical benefits without practical implementation paths
- Updates that can't be used in production within 6 months

---

## Categorization Taxonomy

Group all discovered updates into these buckets for the summary section:

- **🧠 Model & API Updates**: New model releases, API changes, capability upgrades
- **🔗 Framework & Library Releases**: LangChain, LlamaIndex, CrewAI, etc.
- **🏗️ RAG & Retrieval Innovations**: New indexing, search, chunking, or retrieval techniques
- **🤖 Agent & Orchestration Systems**: Multi-agent, memory, tool-calling, workflow engines
- **⚙️ AI Infra & Deployment**: vLLM, Ollama, serving infra, local deployment, model routing
- **🔍 Evaluation & Observability**: Evals, tracing, monitoring, benchmarks
- **🗣️ Multimodal & Voice AI**: Vision, audio, video, realtime AI stacks
- **🛠️ AI Dev Tools & Coding Agents**: IDE tools, coding agents, MCP ecosystem
- **📐 Prompt & Context Engineering**: New prompting techniques, context management patterns
- **🔬 Research with Practical Value**: Papers with implementable techniques

## Top 5 GitHub Repositories

For every execution, find and include the top 5 GitHub repositories worth exploring. Select repos that are recently trending, technically valuable, useful in real GenAI systems, production-oriented, and have high learning value.

**Filtering rules — DO NOT include**: dead repositories, tutorial-only repos, clone projects, fake AI wrappers, low-quality hype repos.

**Prioritize**: actively maintained repos, engineering-heavy repos, production-ready systems, innovative GenAI infra, strong architecture design, real-world usefulness.

For each repository use this exact structure:

---

### [Repository Name]

GitHub URL:
Stars:
Primary Language:
Created/Updated:

#### What Problem It Solves
[Plain-language explanation]

#### Why It Is Interesting
[What makes it different or surprising]

#### Practical Use Cases
[Where developers can actually use it]

#### Key Technical Concepts
[Bullet list of important concepts used in the repo]

#### Architecture Highlights
- Design patterns:
- Workflow:
- Memory handling:
- Orchestration style:
- Scaling approach:
- Retrieval approach (if applicable):
- Agent architecture (if applicable):
- Streaming/realtime approach (if applicable):

#### Implementation Difficulty
[Beginner / Intermediate / Advanced]

#### Should I Learn This?
[Yes/No + 1-2 sentence reason]

#### Best Parts to Study
[Important folders, files, modules, patterns, APIs, or implementations worth examining]

#### Related Technologies
[Frameworks and tools connected to this repo]

---

If a repository contains especially good architecture or design patterns, mark it at the top with:

🔥 **ARCHITECTURE GOLD**

and explain specifically what design decisions developers should study and replicate.

## Technology Trends Identification

For every execution, analyze updates to identify **emerging technology trends** — patterns that appear across multiple updates or represent significant shifts in how AI/GenAI systems are being built.

### How to Identify Trends

Look for patterns across:
- Multiple frameworks adopting the same architectural approach
- Repeated mentions of specific capabilities (e.g., streaming, structured output, memory persistence)
- Technology migrations (e.g., static RAG → agentic RAG)
- Infrastructure shifts (e.g., cloud → local deployment)
- Integration standards emerging (e.g., MCP adoption)
- Performance optimization patterns (e.g., speculative decoding, caching)

### Trend Classification

For each identified trend, assess:
- **Adoption stage:** Early (experimental) / Growing (multiple implementations) / Mainstream (industry standard) / Mature (ubiquitous)
- **Technology type:** Framework pattern, infrastructure shift, API standard, architectural pattern, tooling evolution
- **Drivers:** What's enabling this trend (new model capabilities, cost pressures, performance needs, developer experience)
- **Barriers:** What's slowing adoption (complexity, cost, tooling gaps, breaking changes)
- **Timeline projection:** How long until this becomes mainstream (if not already)

### Trend Output Format

For each trend identified, use this structure:

```markdown
### Trend: [Name]
- **Technology:** [Specific technology or pattern]
- **Adoption stage:** [Early/Growing/Mainstream/Mature]
- **Use cases:** [How it's being applied in production]
- **Enablers:** [What's making adoption possible — new capabilities, tools, standards]
- **Barriers:** [What's slowing adoption — cost, complexity, migration challenges]
- **Timeline to mainstream:** [X months/years or "Already mainstream"]
- **Action for developers:** [What developers should do now]
```

**Quality bar:** Only include trends supported by at least 2 updates in the current report OR a major evolution of a previously tracked trend.

## Final Output Structure

### 🚨 High Signal Updates (if any)
List only the breakthrough-level items here.

### 📋 Full Update Reports
One section per update using the standard format above.

### 🗂️ Top 5 GitHub Repositories Worth Exploring
Five repositories using the structure above.

### 📊 Category Summary Table
| Category | # Updates | Top Pick |
| :--- | :---: | :--- |
| [Category name] | N | [Most notable update] |

### 💡 Strategic Takeaways
3-5 high-level engineering insights from today's scan — what patterns are emerging, what to build next, what to watch.

### 📈 Technology Trends
Identify 2-4 emerging trends based on today's updates using the Trend Output Format defined above. Only include trends supported by multiple updates or representing significant architectural shifts.

---

## HTML Output Requirement

Generate the ENTIRE report as a **self-contained HTML file**. Never save as plain text or markdown.

**Design principles:**
- Professional dark-themed layout with clean typography
- Syntax-highlighted code blocks (highlight.js via CDN)
- Card-based layout for each framework/model update
- Visual score bars, badges, and tags
- Collapsible sections for long code examples
- Fully self-contained — no external dependencies beyond CDN links
- Readable on desktop browsers without any setup

**Content quality standard:**
- Implementation-focused — every section tells a developer what to *do*
- Visually organized — a reader skimming should understand the full picture
- Easy to share with a team by opening in any browser
- Structured as a professional technical research report, not a news article

---

## HTML File Generation — MANDATORY NEW FILE POLICY

After completing the full report, **ALWAYS save to a NEW HTML file**.

### CRITICAL RULE: NEVER OVERWRITE EXISTING FILES

**Filename format (STRICT):**
- First report of the day: `genai_trends_YYYY_MM_DD.html`
- Second report same day: `genai_trends_YYYY_MM_DD_v2.html`
- Third report same day: `genai_trends_YYYY_MM_DD_v3.html`

**Examples:**
- `genai_trends_2026_05_13.html` (first report)
- `genai_trends_2026_05_13_v2.html` (second report same day)
- `genai_trends_2026_05_13_v3.html` (third time, etc.)

### Implementation Checklist
✅ **Before saving:**
1. Check if `.html` file already exists
2. If exists, add version suffix (_v2, _v3)
3. Never overwrite existing reports
4. Always create fresh file

✅ **File content:** Complete self-contained HTML — opens directly in any browser

✅ **Save location:** Current working directory unless specified otherwise

### Reasoning
- Opens instantly in any browser — no markdown viewer required
- Easy to share with non-technical stakeholders
- Preserves report history for comparison
- Prevents accidental data loss
- Audit trail of all generated reports

### Performance Mode (Speed Limits)

Every execution must complete in **30–60 seconds maximum**. Apply these strict limits:

| Constraint | Limit |
| :--- | :--- |
| AI updates | Max 5 |
| GitHub repos | Max 5 |
| Technology trends | Max 4 |
| Code snippets per update | Max 2 |
| Words per update (main content) | Max 150 |
| Words per implementation section | Max 80 |
| Words per future impact section | Max 60 |
| Words per GitHub repo | Max 120 |
| Words per trend | Max 100 |
| Total execution time | 30-60 seconds |

**Do NOT:** over-analyze architecture, repeat framework descriptions, perform historical comparisons, crawl Reddit deeply, or read long articles.

**Only check:** official framework blogs, GitHub trending AI repos, OpenAI updates, Anthropic updates, LangChain/LangGraph changelogs, MCP ecosystem updates.

### HTML File Template

The saved file must be a **complete self-contained HTML** following this structure. Fill in all `{PLACEHOLDER}` values with real content.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>AI Engineering Radar — {DATE}</title>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/styles/github-dark.min.css" />
  <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/highlight.min.js"></script>
  <style>
    :root {
      --bg: #0d1117; --surface: #161b22; --surface2: #21262d;
      --border: #30363d; --text: #e6edf3; --muted: #8b949e;
      --accent: #58a6ff; --green: #3fb950; --yellow: #d29922;
      --red: #f85149; --purple: #bc8cff; --orange: #ffa657;
    }
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body { font-family: 'Inter', sans-serif; background: var(--bg); color: var(--text);
           line-height: 1.6; font-size: 15px; }
    a { color: var(--accent); text-decoration: none; }
    a:hover { text-decoration: underline; }

    /* Layout */
    .page-wrap { display: flex; max-width: 1400px; margin: 0 auto; padding: 24px 16px; gap: 32px; }
    .sidebar { width: 240px; flex-shrink: 0; position: sticky; top: 24px; height: fit-content; }
    .main { flex: 1; min-width: 0; }

    /* Header */
    .site-header { background: var(--surface); border-bottom: 1px solid var(--border);
                   padding: 20px 32px; display: flex; align-items: center; gap: 16px; }
    .site-header .logo { font-size: 22px; font-weight: 700; color: var(--accent); }
    .site-header .date { color: var(--muted); font-size: 13px; margin-left: auto; }
    .site-header .focus-badge { background: var(--surface2); border: 1px solid var(--border);
                                 color: var(--purple); padding: 4px 10px; border-radius: 20px; font-size: 12px; font-weight: 600; }

    /* Stats bar */
    .stats-bar { display: flex; gap: 16px; margin-bottom: 28px; flex-wrap: wrap; }
    .stat-card { background: var(--surface); border: 1px solid var(--border); border-radius: 10px;
                 padding: 16px 20px; flex: 1; min-width: 130px; }
    .stat-card .num { font-size: 28px; font-weight: 700; color: var(--accent); }
    .stat-card .label { font-size: 12px; color: var(--muted); margin-top: 2px; }

    /* Sidebar nav */
    .sidebar h3 { font-size: 11px; text-transform: uppercase; letter-spacing: .08em;
                  color: var(--muted); margin-bottom: 10px; }
    .sidebar nav a { display: block; padding: 6px 10px; border-radius: 6px; color: var(--muted);
                     font-size: 13px; margin-bottom: 2px; transition: all .15s; }
    .sidebar nav a:hover { background: var(--surface2); color: var(--text); text-decoration: none; }
    .sidebar nav a.active { background: var(--surface2); color: var(--accent); }
    .sidebar .db-status { background: var(--surface); border: 1px solid var(--border);
                           border-radius: 10px; padding: 14px; margin-top: 20px; }
    .sidebar .db-status h3 { margin-bottom: 8px; }
    .sidebar .db-row { display: flex; justify-content: space-between; font-size: 12px;
                        color: var(--muted); padding: 3px 0; border-bottom: 1px solid var(--border); }
    .sidebar .db-row:last-child { border-bottom: none; }
    .sidebar .db-row span { color: var(--text); font-weight: 600; }

    /* Section headers */
    .section-title { font-size: 18px; font-weight: 700; margin: 36px 0 16px;
                     display: flex; align-items: center; gap: 8px; padding-bottom: 10px;
                     border-bottom: 1px solid var(--border); }
    .section-title:first-child { margin-top: 0; }

    /* Signal banner */
    .signal-banner { background: linear-gradient(135deg, #1a1023, #0d1117);
                     border: 1px solid #6e40c9; border-radius: 10px; padding: 16px 20px;
                     margin-bottom: 20px; display: flex; gap: 12px; align-items: flex-start; }
    .signal-banner .icon { font-size: 22px; flex-shrink: 0; margin-top: 2px; }
    .signal-banner .text strong { color: var(--purple); font-size: 14px; display: block; margin-bottom: 4px; }
    .signal-banner .text p { color: var(--muted); font-size: 13px; }

    /* Update card */
    .update-card { background: var(--surface); border: 1px solid var(--border); border-radius: 12px;
                   padding: 24px; margin-bottom: 20px; position: relative; overflow: hidden; }
    .update-card::before { content: ''; position: absolute; top: 0; left: 0; right: 0; height: 3px;
                            background: linear-gradient(90deg, var(--accent), var(--purple)); }
    .update-card.high-signal::before { background: linear-gradient(90deg, var(--yellow), var(--orange)); }
    .update-card.evolution::before { background: linear-gradient(90deg, var(--green), var(--accent)); }

    .card-header { display: flex; align-items: flex-start; gap: 12px; margin-bottom: 16px; flex-wrap: wrap; }
    .card-header .card-num { background: var(--surface2); color: var(--muted);
                              width: 28px; height: 28px; border-radius: 50%; display: flex;
                              align-items: center; justify-content: center; font-size: 12px;
                              font-weight: 700; flex-shrink: 0; margin-top: 2px; }
    .card-header h2 { font-size: 17px; font-weight: 700; flex: 1; line-height: 1.3; }
    .card-meta { display: flex; gap: 8px; flex-wrap: wrap; margin-bottom: 12px; }

    /* Badges */
    .badge { display: inline-flex; align-items: center; gap: 4px; padding: 3px 10px;
             border-radius: 20px; font-size: 11px; font-weight: 600; border: 1px solid; }
    .badge-released { color: var(--green); border-color: var(--green); background: rgba(63,185,80,.1); }
    .badge-beta { color: var(--yellow); border-color: var(--yellow); background: rgba(210,153,34,.1); }
    .badge-upcoming { color: var(--purple); border-color: var(--purple); background: rgba(188,140,255,.1); }
    .badge-evolution { color: var(--orange); border-color: var(--orange); background: rgba(255,166,87,.1); }
    .badge-signal { color: var(--red); border-color: var(--red); background: rgba(248,81,73,.1); }
    .tag { background: var(--surface2); color: var(--muted); padding: 2px 8px;
           border-radius: 4px; font-size: 11px; font-family: 'JetBrains Mono', monospace; }

    /* Two-col layout */
    .two-col { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin: 14px 0; }
    .info-box { background: var(--surface2); border: 1px solid var(--border); border-radius: 8px; padding: 14px; }
    .info-box h4 { font-size: 12px; text-transform: uppercase; letter-spacing: .06em;
                   color: var(--muted); margin-bottom: 8px; }
    .info-box p, .info-box li { font-size: 13px; color: var(--text); }
    .info-box ul { padding-left: 16px; }
    .info-box li { margin-bottom: 4px; }

    /* Sub-section headers within cards */
    .card-section-label { font-size: 12px; font-weight: 600; text-transform: uppercase;
                           letter-spacing: .07em; color: var(--muted); margin: 18px 0 8px; }

    /* Code blocks */
    .code-wrap { margin: 12px 0; border-radius: 8px; overflow: hidden; border: 1px solid var(--border); }
    .code-wrap .code-header { background: var(--surface2); padding: 8px 14px; font-size: 11px;
                               color: var(--muted); font-family: 'JetBrains Mono', monospace;
                               display: flex; justify-content: space-between; align-items: center; }
    .code-wrap pre { margin: 0 !important; border-radius: 0 !important; }
    .code-wrap pre code { font-family: 'JetBrains Mono', monospace !important; font-size: 13px !important; }
    details.code-details summary { cursor: pointer; padding: 10px 14px;
                                    background: var(--surface2); font-size: 13px; color: var(--accent);
                                    border-radius: 6px; user-select: none; }
    details.code-details summary:hover { background: var(--border); }
    details.code-details[open] summary { border-radius: 6px 6px 0 0; }

    /* Score bars */
    .scores { display: flex; flex-direction: column; gap: 8px; margin-top: 14px; }
    .score-row { display: flex; align-items: center; gap: 10px; }
    .score-label { font-size: 12px; color: var(--muted); width: 150px; flex-shrink: 0; }
    .score-bar-bg { flex: 1; background: var(--surface2); border-radius: 4px; height: 6px; }
    .score-bar { height: 6px; border-radius: 4px; background: linear-gradient(90deg, var(--accent), var(--purple)); }
    .score-val { font-size: 12px; font-weight: 700; color: var(--accent); width: 32px; text-align: right; }

    /* Timeline */
    .timeline { display: flex; gap: 0; margin: 12px 0; }
    .tl-step { flex: 1; padding: 10px 12px; background: var(--surface2);
                border-right: 2px solid var(--bg); font-size: 12px; }
    .tl-step:first-child { border-radius: 6px 0 0 6px; }
    .tl-step:last-child { border-right: none; border-radius: 0 6px 6px 0; }
    .tl-step .tl-phase { color: var(--muted); font-size: 11px; margin-bottom: 2px; }
    .tl-step .tl-desc { color: var(--text); }

    /* Trend card */
    .trend-card { background: var(--surface); border: 1px solid var(--border); border-left: 3px solid var(--purple);
                  border-radius: 8px; padding: 18px 20px; margin-bottom: 14px; }
    .trend-card h3 { font-size: 15px; font-weight: 600; margin-bottom: 12px; color: var(--purple); }
    .trend-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 8px; }
    .trend-item { font-size: 13px; }
    .trend-item strong { color: var(--muted); font-size: 11px; display: block; margin-bottom: 2px;
                          text-transform: uppercase; letter-spacing: .05em; }

    /* Takeaways */
    .takeaway-list { list-style: none; }
    .takeaway-list li { display: flex; gap: 10px; padding: 12px 0; border-bottom: 1px solid var(--border);
                         font-size: 14px; }
    .takeaway-list li:last-child { border-bottom: none; }
    .takeaway-list li::before { content: '→'; color: var(--accent); font-weight: 700; flex-shrink: 0; }

    /* DB status table */
    .db-table { width: 100%; border-collapse: collapse; font-size: 13px; margin-bottom: 20px; }
    .db-table th { background: var(--surface2); color: var(--muted); padding: 8px 12px;
                   text-align: left; font-weight: 600; font-size: 11px; text-transform: uppercase; }
    .db-table td { padding: 8px 12px; border-bottom: 1px solid var(--border); }
    .db-table tr:last-child td { border-bottom: none; }

    /* Footer */
    .page-footer { text-align: center; padding: 32px; color: var(--muted); font-size: 12px;
                   border-top: 1px solid var(--border); margin-top: 40px; }

    @media (max-width: 900px) {
      .page-wrap { flex-direction: column; }
      .sidebar { width: 100%; position: static; }
      .two-col, .trend-grid { grid-template-columns: 1fr; }
      .timeline { flex-direction: column; }
      .tl-step { border-right: none; border-bottom: 2px solid var(--bg); }
    }
  </style>
</head>
<body>

<header class="site-header">
  <div class="logo">⚡ AI Engineering Radar</div>
  <span class="focus-badge">🔗 {FOCUS_MODE}</span>
  <span class="date">Generated: {DATE} · {TOTAL_NEW} new discoveries</span>
</header>

<div class="page-wrap">

  <!-- Sidebar -->
  <aside class="sidebar">
    <h3>Contents</h3>
    <nav>
      <a href="#already-known">📦 Already Known</a>
      <a href="#high-signal">🚨 High Signal</a>
      <a href="#updates">📋 Updates</a>
      <a href="#trends">📈 Trends</a>
      <a href="#takeaways">💡 Takeaways</a>
    </nav>

    <div class="db-status">
      <h3>Discovery DB</h3>
      <div class="db-row">Total Tracked <span>{TOTAL_DISCOVERIES}</span></div>
      <div class="db-row">Released <span>{RELEASED_COUNT}</span></div>
      <div class="db-row">Upcoming <span>{UPCOMING_COUNT}</span></div>
      <div class="db-row">Major Evolutions <span>{EVOLUTIONS_COUNT}</span></div>
      <div class="db-row">Reports Generated <span>{REPORTS_COUNT}</span></div>
    </div>
  </aside>

  <!-- Main content -->
  <main class="main">

    <!-- Stats bar -->
    <div class="stats-bar">
      <div class="stat-card"><div class="num">{SKIPPED_COUNT}</div><div class="label">Already in DB (skipped)</div></div>
      <div class="stat-card"><div class="num">{NEW_COUNT}</div><div class="label">New Discoveries</div></div>
      <div class="stat-card"><div class="num">{HIGH_SIGNAL_COUNT}</div><div class="label">High Signal</div></div>
      <div class="stat-card"><div class="num">{CODE_EXAMPLES_COUNT}</div><div class="label">Code Examples</div></div>
    </div>

    <!-- Already Known -->
    <section id="already-known">
      <div class="section-title">📦 Already in Database (Skipped)</div>
      <table class="db-table">
        <thead><tr><th>Framework</th><th>Version</th><th>Date</th><th>Status</th></tr></thead>
        <tbody>
          <!-- ROW TEMPLATE: repeat for each known item -->
          <tr>
            <td>{FRAMEWORK_NAME}</td>
            <td><code>{VERSION}</code></td>
            <td>{RELEASE_DATE}</td>
            <td><span class="badge badge-released">✅ Reported</span></td>
          </tr>
        </tbody>
      </table>
    </section>

    <!-- High Signal Banner -->
    <section id="high-signal">
      <div class="section-title">🚨 High Signal Updates</div>
      <!-- REPEAT for each high-signal item -->
      <div class="signal-banner">
        <div class="icon">🚨</div>
        <div class="text">
          <strong>{HIGH_SIGNAL_TITLE}</strong>
          <p>{HIGH_SIGNAL_SUMMARY}</p>
        </div>
      </div>
    </section>

    <!-- Update Cards -->
    <section id="updates">
      <div class="section-title">📋 New Framework Releases</div>

      <!-- REPEAT this card for EACH new discovery -->
      <div class="update-card high-signal">
        <div class="card-header">
          <div class="card-num">1</div>
          <h2>{UPDATE_TITLE}</h2>
        </div>
        <div class="card-meta">
          <span class="badge badge-released">✅ Released</span>
          <span class="badge badge-evolution">🔄 Major Evolution</span>
          <span class="badge badge-signal">🚨 High Signal</span>
          <span class="tag">{FRAMEWORK}</span>
          <span class="tag">{COMPANY}</span>
          <span class="tag">{VERSION}</span>
        </div>

        <p style="color: var(--muted); font-size: 13px; margin-bottom: 14px;">
          📅 Released: <strong style="color:var(--text)">{RELEASE_DATE}</strong> &nbsp;|&nbsp;
          🔗 <a href="{SOURCE_URL}">{SOURCE_LABEL}</a>
        </p>

        <div class="two-col">
          <div class="info-box">
            <h4>What Happened</h4>
            <p>{WHAT_HAPPENED}</p>
          </div>
          <div class="info-box">
            <h4>Why It Matters</h4>
            <p>{WHY_IT_MATTERS}</p>
          </div>
        </div>

        <div class="two-col">
          <div class="info-box">
            <h4>Before</h4>
            <p>{BEFORE_DESCRIPTION}</p>
          </div>
          <div class="info-box">
            <h4>After</h4>
            <p>{AFTER_DESCRIPTION}</p>
          </div>
        </div>

        <div class="card-section-label">Key Features</div>
        <div style="display:flex; gap:6px; flex-wrap:wrap; margin-bottom:14px;">
          <span class="tag">{FEATURE_1}</span>
          <span class="tag">{FEATURE_2}</span>
          <span class="tag">{FEATURE_3}</span>
        </div>

        <div class="card-section-label">Quick Start</div>
        <details class="code-details">
          <summary>▶ Show Quick Start Code</summary>
          <div class="code-wrap">
            <div class="code-header"><span>python</span><span>Quick Start</span></div>
            <pre><code class="language-python">{QUICKSTART_CODE}</code></pre>
          </div>
        </details>

        <div class="card-section-label">Production Pattern</div>
        <details class="code-details">
          <summary>▶ Show Production Pattern</summary>
          <div class="code-wrap">
            <div class="code-header"><span>python</span><span>Production Pattern</span></div>
            <pre><code class="language-python">{PRODUCTION_CODE}</code></pre>
          </div>
        </details>

        <div class="card-section-label">Stack Compatibility</div>
        <div class="info-box" style="margin-bottom:14px;">
          <p style="font-size:13px;">{STACK_COMPATIBILITY}</p>
        </div>

        <div class="card-section-label">Adoption Timeline</div>
        <div class="timeline">
          <div class="tl-step">
            <div class="tl-phase">⚗️ Experimental (0–3 mo)</div>
            <div class="tl-desc">{TIMELINE_EXPERIMENTAL}</div>
          </div>
          <div class="tl-step">
            <div class="tl-phase">🚀 Early Production (3–6 mo)</div>
            <div class="tl-desc">{TIMELINE_EARLY_PROD}</div>
          </div>
          <div class="tl-step">
            <div class="tl-phase">🌍 Mainstream (12–24 mo)</div>
            <div class="tl-desc">{TIMELINE_MAINSTREAM}</div>
          </div>
        </div>

        <div class="card-section-label">Scores</div>
        <div class="scores">
          <div class="score-row">
            <span class="score-label">Production Impact</span>
            <div class="score-bar-bg"><div class="score-bar" style="width:{PROD_SCORE}0%"></div></div>
            <span class="score-val">{PROD_SCORE}/10</span>
          </div>
          <div class="score-row">
            <span class="score-label">Learning Value</span>
            <div class="score-bar-bg"><div class="score-bar" style="width:{LEARN_SCORE}0%"></div></div>
            <span class="score-val">{LEARN_SCORE}/10</span>
          </div>
          <div class="score-row">
            <span class="score-label">Future Trend Potential</span>
            <div class="score-bar-bg"><div class="score-bar" style="width:{TREND_SCORE}0%"></div></div>
            <span class="score-val">{TREND_SCORE}/10</span>
          </div>
        </div>

        <div class="card-section-label" style="margin-top:16px;">Should Developers Care?</div>
        <div class="info-box">
          <p><strong style="color:var(--green);">{CARE_LEVEL}</strong> — {CARE_REASON}</p>
        </div>
      </div>
      <!-- END update card — repeat above block for each new discovery -->

    </section>

    <!-- Technology Trends -->
    <section id="trends">
      <div class="section-title">📈 Technology Trends</div>

      <!-- REPEAT for each trend -->
      <div class="trend-card">
        <h3>Trend {N}: {TREND_NAME}</h3>
        <div class="trend-grid">
          <div class="trend-item"><strong>Technology</strong>{TREND_TECH}</div>
          <div class="trend-item"><strong>Adoption Stage</strong>{TREND_STAGE}</div>
          <div class="trend-item"><strong>Use Cases</strong>{TREND_USE_CASES}</div>
          <div class="trend-item"><strong>Enablers</strong>{TREND_ENABLERS}</div>
          <div class="trend-item"><strong>Barriers</strong>{TREND_BARRIERS}</div>
          <div class="trend-item"><strong>Timeline to Mainstream</strong>{TREND_TIMELINE}</div>
        </div>
        <div class="card-section-label" style="margin-top:12px;">Action for Developers</div>
        <p style="font-size:13px; color:var(--text);">{TREND_ACTION}</p>
      </div>

    </section>

    <!-- Takeaways -->
    <section id="takeaways">
      <div class="section-title">💡 Strategic Takeaways</div>
      <ul class="takeaway-list">
        <li>{TAKEAWAY_1}</li>
        <li>{TAKEAWAY_2}</li>
        <li>{TAKEAWAY_3}</li>
        <li>{TAKEAWAY_4}</li>
        <li>{TAKEAWAY_5}</li>
      </ul>
    </section>

  </main>
</div>

<footer class="page-footer">
  AI Engineering Radar · Generated {DATE} · {TOTAL_NEW} new discoveries · Focus: {FOCUS_MODE}
</footer>

<script>hljs.highlightAll();</script>
</body>
</html>
```

### Execution Strategy

Generate results **incrementally** — fetch → summarize quickly → write markdown → continue to next item. Do not collect everything first or think deeply for every topic.

### File Safety Check (MANDATORY BEFORE SAVE)

**Before saving, use the Glob tool to check for existing files, then pick a safe name:**

```
1. Glob: genai_trends_{YYYY_MM_DD}*.html
2. If no match → use genai_trends_{YYYY_MM_DD}.html
3. If v1 exists → use genai_trends_{YYYY_MM_DD}_v2.html
4. If v2 exists → use genai_trends_{YYYY_MM_DD}_v3.html  (etc.)
5. Write the full HTML to the chosen filename
```

**NEVER:**
- Overwrite an existing `.html` file
- Use `.md` extension

**ALWAYS:**
- Confirm filename before writing
- Report the actual filename used in the terminal summary

### AUTO-OPEN HTML IN BROWSER (MANDATORY)

**Immediately after saving the HTML file, automatically open it in the default browser:**

```powershell
# After file is written successfully:
Start-Process -FilePath "C:\path\to\genai_trends_YYYY_MM_DD.html"
```

**Implementation:**
1. ✅ After Write tool succeeds, execute PowerShell Start-Process
2. ✅ Pass the full file path to Start-Process
3. ✅ Use -FilePath parameter (not -Path)
4. ✅ File opens in user's default browser automatically
5. ✅ User can immediately see the report without manual action

**Why this matters:**
- Users don't need to manually navigate to the file
- Report opens instantly in browser after generation completes
- Professional UX: generation → automatic viewing → ready to review
- No extra user steps = higher engagement with generated report

### Terminal Output (Final Response)

After saving the HTML file AND opening it in browser, return ONLY this summary - do NOT print the full HTML content to terminal:

```
✅ HTML Report Generated & Opened Automatically

📄 Filename: genai_trends_2026_05_13.html
🌐 Status: Opening in your default browser...
⏱️ Execution Time: ~45 seconds
📊 High-Signal Updates: X
📋 New Discoveries: X  (skipped Y already-known items)
📈 Technology Trends: X
💻 Code Examples: X (syntax-highlighted in HTML)

🎯 Focus Mode: [Selected category]
📍 Location: Current working directory
✨ Your report is now open in your browser!
```

**IMPORTANT:** Always confirm:
- ✅ HTML file is new (not overwritten)
- ✅ File was created successfully
- ✅ Browser auto-open command executed
- ✅ All CDN links included (fonts, highlight.js)
- ✅ hljs.highlightAll() called at bottom of script tag
- ✅ No existing files were modified

---

## High-Signal AI Discovery Mode

This is the core quality filter applied to every item before it enters the report.

### Mission

Discover ONLY:
- Newly launched AI frameworks or SDKs
- Surprising AI engineering breakthroughs
- New GenAI architectures or agent systems
- New RAG techniques or retrieval innovations
- Newly open-sourced projects
- Newly released APIs or major features
- Hidden high-value AI innovations
- Experimental but promising AI systems

### Inclusion Gate

Only include an update if it satisfies **at least one**:

| Gate | Criteria |
| :--- | :--- |
| Recency | Released in the last 7 days |
| Open-source | Newly open-sourced |
| Official | Newly announced via official channel |
| Capability | New major capability added to existing tool |
| Architecture | New architecture pattern or engineering approach |
| Performance | Significant latency, cost, or throughput improvement |
| Productivity | Major developer workflow improvement |

### Hard Exclusion List

Never include:
- Generic AI news or company announcements
- Funding rounds or valuations
- AI politics or regulation
- Interviews, podcasts, or opinion pieces
- Basic tutorials or getting-started guides
- "Top AI tools" style roundups
- Repeated descriptions of existing frameworks
- Surface-level hype without implementation detail

### High-Value Signal Detection

Prioritize updates that do any of the following:

- Make AI systems faster (inference, retrieval, generation)
- Reduce token usage or API cost
- Improve RAG quality or retrieval precision
- Improve agent memory or persistence
- Improve orchestration or multi-agent coordination
- Improve streaming or realtime AI performance
- Improve AI reliability or reduce hallucinations
- Improve context handling or compression
- Simplify production deployment
- Improve structured output quality
- Improve developer productivity measurably

### Surprising Engineering Update Flag

If something is technically surprising or overturns a normal assumption, mark it:

🚨 **SURPRISING ENGINEERING UPDATE**

Use for:
- Radically faster inference via unexpected technique
- New memory architecture that changes agent design
- Agent breakthrough that removes a known limitation
- New context engineering pattern with proven gains
- Innovative retrieval mechanism with measurable improvement
- Unexpected scaling trick
- New AI workflow pattern that simplifies complex pipelines

For each flagged item, explain:
1. Why it is surprising
2. What old limitation it solves
3. Why developers should change behavior because of it

### Industry Impact Rating

Every update must include an industry impact rating:

| Rating | Meaning |
| :--- | :--- |
| **Massive** | Will change how most GenAI systems are built |
| **High** | Likely to be widely adopted in production systems |
| **Medium** | Useful for specific use cases or architectures |
| **Low** | Niche value — track but don't prioritize |

Include a one-sentence explanation of:
- How it may change AI system design
- What developers may start adopting
- What existing approaches may become outdated

### Source Priority (Strict Order)

1. Official release notes and changelogs
2. Official GitHub repositories and releases
3. Official engineering blogs (Anthropic, OpenAI, Google DeepMind, Meta AI)
4. Newly trending GitHub repositories
5. Secondary sources only if the official source is unavailable

### Quality Bar

The final report should read like:
> *"Important new AI engineering discoveries that developers should act on immediately."*

Not like:
> *"Daily AI news digest."*

Every item in the report must answer: **"What should a developer do differently because of this?"**

---

# FRESH DISCOVERY & CONTINUOUS UPDATE MODE

---

IMPORTANT:
Focus on bringing fresh and valuable discoveries in every execution.

Before adding any update:

1. Review previously generated markdown reports
2. Review previously tracked update titles
3. Review previously covered GitHub repositories
4. Compare with earlier execution history

When a topic/framework/release is already known:

* include it again when there is:

  * a major new capability
  * an important new version
  * a powerful new feature
  * a meaningful architecture evolution
  * a strong production improvement
  * a major roadmap announcement

---

# HIGH VALUE UPDATE IDENTIFICATION

---

Strong updates include:

* major release versions
* important feature launches
* architecture improvements
* benchmark improvements
* major API capabilities
* production-ready enhancements
* impactful open-source launches
* roadmap reveals with engineering significance

---

# INTELLIGENT CHANGE TRACKING

---

While reviewing earlier reports, compare:

* title similarity
* framework names
* repository names
* release versions
* feature sets
* announcement themes

When strong new improvements are found:

* highlight the evolution
* explain the latest capability
* explain the new engineering value

---

# CONTINUOUS DISCOVERY MODE

---

Goal:
Every execution should feel:

* fresh
* insightful
* implementation-focused
* high-value

The report should emphasize:

* fresh discoveries
* newly released capabilities
* emerging engineering patterns
* newly open-sourced frameworks
* newly announced APIs/features
* industry-shaping AI innovations

---

# LIGHTWEIGHT HISTORY TRACKING

---

Maintain lightweight tracking for:

* update titles
* framework names
* GitHub repositories
* release versions
* announcement dates

Use this tracking to continuously surface:

* fresh innovations
* meaningful improvements
* latest breakthroughs
* evolving AI engineering trends

---

# MAJOR EVOLUTION HIGHLIGHT

---

If a previously tracked technology receives a major advancement,
highlight it using:

🚨 MAJOR EVOLUTION UPDATE

Then explain:

* what evolved
* why it matters now
* what new opportunities it creates
* how developers can benefit from it

---

# FINAL QUALITY GOAL

---

Every report should provide:

* fresh engineering discoveries
* evolving AI innovations
* high-signal updates
* implementation-relevant insights
* practical GenAI value

END.

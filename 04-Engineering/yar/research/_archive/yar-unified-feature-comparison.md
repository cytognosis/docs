> **Status:** SUPERSEDED · **Archived:** 2026-07-01 · **Superseded by:** `03-Products/Cytonome/Yar/research/yar-unified-feature-comparison-v4.md`
>
> Stale v2 comparison; superseded by the 03P v4 comparison. Kept for provenance; do not edit.

# Yar Unified Feature Comparison: Neurodivergent-Friendly Cognitive Companions

> **Document Type:** Consolidated Market & Feature Research
> **Author:** Cytognosis AI Agent
> **Date:** 2026-05-29
> **Version:** 2.0 (unified from 3 deep-dive research docs + 3 web research briefs + prior comparison)
> **Scope:** 9-tool comparative analysis for Yar product roadmap
> **Status:** Final
> **Sources:**
> - [tana-outliner-deep-dive.md](file:///home/mohammadi/repos/cytognosis/docs/cytonome/yar/research/tana-outliner-deep-dive.md)
> - [capacities-deep-dive.md](file:///home/mohammadi/repos/cytognosis/docs/cytonome/yar/research/capacities-deep-dive.md)
> - [cap_yar_comprehensive_reference.md](file:///home/mohammadi/repos/cytognosis/docs/cytonome/yar/research/cap_yar_comprehensive_reference.md)
> - Web research: goblin.tools, saner.ai, speechify.com
> - Prior comparison: [feature-comparison.md](file:///home/mohammadi/repos/cytognosis/docs/cytonome/yar/feature-comparison.md)

---

## 1. Master Feature Matrix

Scores use a 0-10 scale: **0** = absent, **3** = basic/limited, **5** = adequate, **7** = strong, **10** = best-in-class.

| Category | Leantime | Super Productivity | Tana | Capacities | Goblin Tools | Saner AI | Speechify | ND Visual Organizer (MCP) | Anytype |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **Task Management** | 8 | 9 | 6 | 5 | 5 | 7 | 0 | 2 | 4 |
| **Time Management** | 5 | 10 | 2 | 3 | 4 | 3 | 0 | 0 | 1 |
| **Knowledge Management** | 6 | 3 | 10 | 8 | 2 | 8 | 3 | 8 | 8 |
| **AI Integration** | 7 | 2 | 8 | 6 | 9 | 9 | 7 | 6 | 2 |
| **ND-Specific Features** | 7 | 8 | 5 | 5 | 10 | 6 | 7 | 4 | 3 |
| **Collaboration** | 7 | 2 | 7 | 3 | 0 | 3 | 2 | 0 | 4 |
| **Integration Ecosystem** | 6 | 9 | 5 | 5 | 1 | 7 | 4 | 8 | 3 |
| **Open Source / Self-Hosted** | 9 | 10 | 0 | 0 | 0 | 0 | 0 | 10 | 9 |
| **Accessibility** | 6 | 7 | 5 | 6 | 8 | 5 | 9 | 3 | 4 |
| **Mobile Support** | 6 | 8 | 5 | 7 | 7 | 6 | 9 | 0 | 6 |
| **Cost** | 8 | 10 | 5 | 6 | 10 | 5 | 3 | 10 | 9 |
| **Data Portability** | 6 | 8 | 3 | 4 | 1 | 4 | 2 | 7 | 8 |
| **TOTAL** | **81** | **86** | **61** | **58** | **57** | **63** | **46** | **58** | **61** |

---

## 2. Comparative Landscape Analysis

The neurodivergent productivity tool market splits into five distinct clusters: task-focused execution engines, knowledge-graph organizers, AI-augmented assistants, accessibility-first utilities, and composable infrastructure patterns. No single tool covers the full spectrum of executive function support that Yar targets. Super Productivity leads in raw feature coverage (86/120) by combining deep time tracking, focus-mode discipline, and broad integrations under a permissive MIT license. Leantime follows (81/120) as the only tool that explicitly markets itself to ADHD, dyslexia, and autism users while offering enterprise-grade project management. Both are open-source, giving Yar concrete architectural patterns to study and adopt.

The knowledge-management cluster (Tana, Capacities, Anytype) excels at capturing and connecting ideas but lacks the time-awareness and focus-mode features that neurodivergent users depend on for daily execution. Tana's Supertag system represents the most sophisticated personal knowledge graph with schema inheritance, composition, and queries-as-first-class-objects. Capacities offers a cleaner "thinking in things" UX that reduces cognitive overhead, having migrated from a graph database to Postgres while preserving graph semantics. Anytype combines local-first data sovereignty with E2E encryption, making it Yar's planned storage backend. Together these three tools validate the demand for structured, typed-object knowledge management; Yar adopts the best patterns from each.

The AI-assistant cluster (Goblin Tools, Saner AI) and the accessibility-utility cluster (Speechify) occupy complementary niches. Goblin Tools' Magic ToDo with its spiciness slider is the purest implementation of AI-powered task decomposition for neurodivergent users, free and frictionless. Saner AI's Skai agent proactively extracts tasks from email, calendar, and notes, addressing the "invisible workload" that disproportionately affects ADHD users. Speechify transforms reading into listening, creating dual-channel input that materially helps users with dyslexia and attention difficulties. The ND Visual Organizer (MCP) pattern represents the composable, protocol-first future, offering maximum data sovereignty but requiring technical sophistication. Yar's opportunity is to unify all five clusters into a single, local-first, AI-native companion that adapts to each user's cognitive profile.

---

## 3. Bullet-Point Summary

- **Best overall feature coverage:** Super Productivity (86/120), free, open-source, cross-platform
- **Best ND-specific design:** Goblin Tools (10/10), purpose-built AI utilities for executive dysfunction
- **Best knowledge management:** Tana (10/10), Supertag-based knowledge graph with live search nodes
- **Best AI integration:** Goblin Tools and Saner AI (tied at 9/10), both use AI as the primary interaction model
- **Best for time blindness:** Super Productivity (10/10), Pomodoro, idle detection, break reminders, focus mode
- **Best accessibility:** Speechify (9/10), TTS with synchronized highlighting addresses reading disabilities directly
- **Best data sovereignty:** Super Productivity, ND Visual Organizer, and Anytype (9-10/10), fully local-first or self-hosted
- **Best object model UX:** Capacities (NEW), "thinking in things" paradigm with offline-first and Postgres reliability
- **Best schema system:** Tana, Supertags with inheritance (Extend) + composition + field types + template bundles
- **Biggest gap across all tools:** No tool combines task execution, knowledge management, emotional awareness, and ND-specific accommodations in a single, open-source, local-first package. This is Yar's opportunity.

---

## 4. Tool Groups

### Group A: Task-Focused Execution Engines
**Leantime** and **Super Productivity**

Both tools center on getting tasks done. Super Productivity emphasizes individual deep work with Pomodoro timers, idle detection, and a keyboard-first interface. Leantime targets teams with Kanban boards, Gantt charts, and sprint management. Both include task CRUD, subtasks, and tagging systems. Super Productivity's MIT license and local-first architecture make it the stronger foundation for Yar's task execution layer. Leantime's LEO AI with emoji sentiment tracking offers unique emotional awareness that no other task manager provides.

### Group B: Knowledge-Focused Organizers
**Tana**, **Capacities**, and **Anytype**

These tools prioritize capturing, connecting, and retrieving knowledge. Tana's Supertags turn every node into a typed object with custom fields, creating a personal knowledge graph that surfaces information through live search queries. Queries themselves are nodes, composable and embeddable. Capacities adopts a cleaner "thinking in things" UX, where users create typed objects (Books, People, Meetings) with automatic field prompts and graph visualization. Its migration from graph DB to Postgres demonstrates that relational backends can maintain graph semantics at scale. Anytype combines local-first, E2E encrypted storage with a type/template/relation model, making it Yar's planned storage backend.

### Group C: AI-Augmented Assistants
**Goblin Tools** and **Saner AI**

AI drives the core interaction model in both tools. Goblin Tools provides focused micro-utilities (Magic ToDo, Estimator, Judge, Compiler, Formalizer, Chef, Professor, Consultant, Taskmaster) that each solve one executive function challenge. The spiciness slider for task decomposition granularity is a genuinely novel UX invention. Saner AI takes a broader approach, using its Skai agent to proactively extract tasks, auto-tag notes, and surface semantic connections across email, calendar, and documents. It offers multi-model selection (GPT-4, Claude 3, Gemini Pro) within a single interface. Goblin Tools wins on accessibility and cost (free); Saner AI wins on scope, automation, and proactive intelligence.

### Group D: Accessibility-First Utilities
**Speechify**

Speechify stands alone in the "modality transformation" category. By converting text to high-quality audio with synchronized visual highlighting, it serves users who process information better through listening than reading. Its 1,000+ AI voices, up to 5x speed with speed ramping, OCR scanning, and well-documented API (Python + TypeScript SDKs, streaming, speech marks) make it the most comprehensive TTS solution in this comparison. It addresses a specific accessibility need rather than general task or knowledge management. Aggressive billing practices are its primary weakness.

### Group E: Infrastructure / Protocol Patterns
**ND Visual Organizer (MCP)** and **Anytype** (partial)

These represent the composable, protocol-first approach to knowledge management. The MCP pattern combines Knowledge Graph Memory, Memento MCP, and cognee backends with Markmap visualization. Anytype provides the local-first storage primitives. Both offer maximum data ownership but require technical sophistication. This pattern represents the architectural future that Yar builds toward: exposing its knowledge graph as an MCP server while using Anytype for local storage.

---

## 5. Per-Tool Deep Dives

### 5.1 Leantime

**Overview:** Open-source project management platform (AGPLv3) built on PHP + MySQL. Markets itself as "project management for non-project-managers" with explicit neurodivergent support. Offers a clean hexagonal architecture with 57 domain modules.

**Key Features:**
- Task CRUD with unlimited subtasks, dependencies, and multiple views (Kanban, table, list, calendar, Gantt)
- LEO AI assistant for task prioritization using Pareto Principle and Goldilocks method
- Emoji sentiment tracking: users rate emotional response to tasks, AI adapts prioritization
- Sprint management, milestone tracking, retrospectives, goals, and strategy canvases
- Wiki/docs system, idea boards, file storage (S3 or local)
- MCP Server plugin for AI assistant integration

**ND-Specific Strengths:**
- Emoji sentiment tracking directly addresses emotional dysregulation around tasks
- AI prioritization reduces decision fatigue (a core ADHD challenge)
- "My Work" dashboard simplifies the interface to reduce cognitive overload

**Limitations:**
- Server-first architecture requires hosting infrastructure (not local-first)
- No Pomodoro timer, idle detection, or focus mode
- No voice input or TTS
- PHP + MySQL stack limits modern web development flexibility

**Pricing:** Free/open-source core (AGPLv3). Plugin marketplace with Personal tier (1-3 users) and team brackets.

**Verdict:** The emoji sentiment tracking and AI prioritization are features Yar should adopt. The server-first architecture and team-oriented feature set make it less suitable as a personal cognitive companion, but its behavioral science integration is uniquely valuable.

---

### 5.2 Super Productivity

**Overview:** Open-source (MIT license) task manager and time tracker built with Angular, deployed via Electron (desktop), Capacitor (mobile), and PWA (web). Focuses on deep work and ADHD-friendly workflows.

**Key Features:**
- Full task CRUD with subtasks, tags, projects, and notes (markdown + checklists)
- Integrated time tracking with per-task timers
- Pomodoro timer with configurable work/break intervals
- Idle detection (Electron: `powerMonitor.getSystemIdleTime()`; Web: mouse/keyboard listeners)
- Take-a-break reminders with configurable intervals
- Focus mode: full-screen single-task view with timer and progress bar
- Integrations: Jira, GitHub, GitLab, Trello, Linear, ClickUp, OpenProject, Azure DevOps, CalDAV
- Operation-log CRDT-like sync architecture with vector clocks

**ND-Specific Strengths:**
- Focus mode blocks navigation to other tasks (addresses ADHD distraction)
- Idle detection auto-pauses time tracking (reduces guilt from hyperfocus interruptions)
- Break reminders prevent burnout during hyperfocus sessions
- "Finish Day" celebration provides dopamine reward for task completion

**Limitations:**
- No AI features (task breakdown, prioritization, or smart suggestions)
- No knowledge management (no wiki, notes beyond per-task)
- No voice input or TTS
- No emotion tracking or sentiment analysis

**Pricing:** Completely free and open-source (MIT license). No premium tier, no ads, no telemetry.

**Verdict:** The strongest open-source foundation for Yar's task execution and time management layer. Yar should adopt Super Productivity's focus mode, idle detection, break reminders, and Pomodoro patterns while adding AI, knowledge management, and emotional awareness.

---

### 5.3 Tana (Outliner)

**Overview:** AI-native, graph-based knowledge management platform (proprietary, cloud-based). Uses Supertags to transform unstructured notes into typed, queryable data. Everything is a node with a unique persistent ID.

**Key Features:**
- Supertags: turn any node into a typed object with custom fields (plain, date, number, URL, checkbox, options, options-from-supertag)
- Schema inheritance via "Extend" feature; multi-type composition via multiple supertags
- Search Nodes (Live Queries): queries are themselves nodes, composable and embeddable
- Query builder with AND/OR/NOT logic, field/tag/value/date conditions
- Multi-view rendering: List, Table, Kanban, Calendar, Tabs
- Command nodes: automation primitives chaining AI prompts, API requests, and field mutations
- Template bundles: composable workflow packages (supertags + fields + commands + views)
- Botless meeting transcription via desktop system audio capture
- Voice-to-structure on mobile with supertag-aware formatting
- Multi-model AI: GPT, Claude, Gemini with configurable reasoning levels
- Bidirectional references with auto-backlinks and unlinked mention detection

**ND-Specific Strengths:**
- Flexible structure accommodates non-linear thinking (no rigid folder hierarchy)
- Supertags reduce cognitive load of categorization (apply tag, get auto-fields)
- Voice capture reduces friction for "capture at speed of thought"
- Live Search nodes surface forgotten information automatically

**Limitations:**
- Steep learning curve creates cognitive overload for the ND users it could help most
- Proprietary, cloud-only (Firebase backend), no offline-first or local file ownership
- No time tracking, Pomodoro, idle detection, or focus mode
- Input API only (no bidirectional API for full data export)

**Pricing:** Free (5 supertags, 500 AI credits), Plus ~$10/mo (2,000 AI credits, Calendar), Pro ~$18/mo (5,000 AI credits, Input API).

**Verdict:** The most sophisticated knowledge graph UX in this comparison. Supertags, Live Search nodes, and command node automation represent the gold standard for personal knowledge management. Yar should adopt the Supertag pattern (schema-based node types with inheritance + composition), queries-as-first-class-objects, and template bundles. The proprietary cloud architecture is what Yar exists to replace with local-first sovereignty.

---

### 5.4 Capacities (NEW)

**Overview:** Object-oriented knowledge management platform using "thinking in things" paradigm. Users create typed objects (Books, People, Meetings, Projects) with pre-configured fields and views. Recently migrated from graph database to Postgres while preserving graph semantics.

**Key Features:**
- Object types with pre-defined properties and custom fields
- Multiple views: list, table, gallery, board, graph visualization
- Daily Notes with calendar integration
- AI assistant with property autofill and contextual suggestions
- Offline-first with cross-device sync
- Graph visualization for exploring connections between objects

**ND-Specific Strengths:**
- "Thinking in things" provides more intuitive mental model than generic notes
- Less configuration required than Tana, reducing setup cognitive load
- Offline-first ensures access during focus sessions without internet anxiety
- Daily Notes provide consistent entry point, reducing decision paralysis

**Limitations:**
- Proprietary, not open-source
- Less powerful automation than Tana (no command nodes, limited programmability)
- Primarily single-user, limited collaboration
- Export options more limited than Tana's Markdown/JSON export

**Pricing:** Free tier available. Pro ~$12/mo.

**Verdict:** Capacities offers the most intuitive object-model UX for non-technical users. Yar should adopt Capacities' "thinking in things" approach for the user-facing object creation experience while using Tana's schema inheritance for the underlying type system. The hybrid is Capacities' UX + Tana's schema depth + Anytype's local storage.

---

### 5.5 Goblin Tools

**Overview:** Collection of free, AI-powered micro-utilities designed specifically for neurodivergent users. Built by a solo developer (Bram De Buyser). Nine tools, each solving one executive function challenge.

**Key Features:**
- **Magic ToDo:** Task decomposition with "spiciness slider" (1-5 chili peppers) controlling granularity; recursive sub-expansion
- **Formalizer:** Tone rewriting (professional, casual, polite, concise, assertive)
- **Estimator:** Time estimates for tasks, combating time blindness
- **Judge:** Emotional tone/intent analysis for social communication
- **Compiler:** Brain dump chaos to clean, structured task lists
- **Chef:** Recipe generation from available ingredients
- **Professor:** Simplified explanations and crash courses
- **Consultant:** Decision support for analysis paralysis
- **Taskmaster:** Single-task focus mode
- Multi-model AI (not locked to one provider), voice input support

**ND-Specific Strengths:**
- Spiciness slider is the purest implementation of progressive task decomposition for ADHD
- Estimator directly addresses time blindness (a defining ADHD challenge)
- Judge helps autistic users interpret social/emotional tone in messages
- Compiler transforms brain dump chaos into structure (addresses working memory overload)
- Zero friction: no account required, no setup, instant utility
- Free web access removes financial barriers

**Limitations:**
- No persistent data storage (stateless micro-utilities)
- No task management, knowledge management, or time tracking
- No integrations, no API, no collaboration
- No long-term memory or pattern learning

**Pricing:** Web: free, no ads, no paywalls. iOS/Android: ~$3 one-time purchase.

**Verdict:** Every feature solves a specific executive function challenge. Yar should integrate Goblin Tools' concepts directly: the spiciness slider for task decomposition, the Estimator for time awareness, the Compiler for capture-to-structure, and the Judge for emotional tone analysis. These features belong in Yar's AI agent layer rather than requiring users to context-switch to a separate tool.

---

### 5.6 Saner AI

**Overview:** AI-powered "Executive OS" marketed as a proactive second brain. Uses Skai AI assistant that learns from user data, auto-organizes notes, and proactively surfaces tasks and connections.

**Key Features:**
- Skai AI: context-aware assistant that learns from notes, tasks, emails, calendar
- Multi-model selection: GPT-4, Claude 3, Gemini Pro within one interface
- Ally: specialized internet search model
- Proactive task extraction from emails, documents, meeting notes
- Auto-tagging, auto-categorization, semantic search (meaning-based, not keyword)
- Brain dump mode with AI parsing to structured notes
- Focus Mode (PiP floating window keeping current priority visible)
- AI daily planner ("Plan my day" generates time-blocked schedule)
- Chrome extension for web clipping, Telegram bot for capture
- Integrations: Google Calendar, Gmail, Outlook, Slack, Drive

**ND-Specific Strengths:**
- Proactive task extraction reduces "invisible workload" hiding in emails/notes
- Auto-tagging eliminates executive function burden of manual categorization
- Semantic search compensates for poor recall (find by meaning, not exact keywords)
- Focus Mode PiP keeps priority visible during context switches
- AI daily planner addresses time blindness with generated schedules

**Limitations:**
- Cloud-only, proprietary, no self-hosting, no offline
- Limited free tier (30 AI msgs/month, 100 notes)
- No desktop app (web-only)
- Weak collaboration features
- Limited data export (HTML, Markdown)
- Mobile experience reported as less polished

**Pricing:** Free (30 AI msgs/mo, 100 notes), Starter ~$8-12/mo, Standard ~$16-20/mo.

**Verdict:** Saner AI's proactive task extraction, multi-model AI, and semantic search represent exactly the kind of "invisible assistant" that Yar's agent layer should become. The PiP Focus Mode is a clever design Yar should study. Yar should implement similar proactive intelligence locally, using on-device models rather than cloud APIs, to preserve data sovereignty.

---

### 5.7 Speechify

**Overview:** Text-to-speech platform that converts written content to natural-sounding audio with synchronized visual highlighting. Available across web, desktop, mobile, with a well-documented API.

**Key Features:**
- TTS with synchronized word-by-word highlighting (dual-channel processing)
- 1,000+ AI voices including celebrity voices across 60+ languages
- Speed up to 4.5-5x with speed ramping for gradual adaptation
- OCR 4.0 scanning for physical documents via camera
- AI summaries, AI quizzes, AI podcasts, conversational voice AI
- Voice typing/dictation with auto-removal of filler words
- Chrome extension for reading web pages, Gmail, Google Docs
- API: Python SDK (`speechify-api`), TypeScript SDK (`@speechify/api`), REST, streaming, speech marks
- On-device AI voices on iOS (late 2025, no internet required)
- Voice cloning with biometric "Identity Locking" verification

**ND-Specific Strengths:**
- Synchronized highlighting maintains visual focus during reading (ADHD attention drift)
- Audio modality bypasses reading difficulties (dyslexia support)
- Speed control accommodates variable processing rates across attention states
- Speed ramping trains gradual comprehension improvement
- AI summaries reduce cognitive load of long documents
- Multitasking enablement: listen while walking/exercising (ADHD needs movement)

**Limitations:**
- No task management, time tracking, or planning features
- Expensive premium ($139/yr or $29/mo); free tier severely limited (10 robotic voices, 1.5x cap)
- Aggressive trial-to-annual auto-renewal is #1 user complaint
- Hidden usage caps on premium voices frustrate power users
- Complex layout handling (footnotes, multi-column PDFs, math) causes issues
- Celebrity voices retain some robotic cadence

**Pricing:** Free (10 basic voices, 1.5x cap), Premium ~$139/yr (~$11.58/mo) or $29/mo.

**Verdict:** Speechify fills an accessibility gap that no other tool addresses: reading difficulty. Yar should implement basic TTS with synchronized highlighting as a built-in accessibility feature using open-source TTS (Coqui, Piper) rather than building a competing product. The Speechify API is well-documented and could serve as an integration option for users who want premium voice quality.

---

### 5.8 ND Visual Organizer (MCP)

**Overview:** Not a single product but an emerging architectural pattern combining knowledge graph MCP servers, semantic search, and Markmap visualization through the Model Context Protocol.

**Key Features:**
- Knowledge graph storage via MCP servers (Knowledge Graph Memory, Memento, cognee)
- Persistent AI memory across sessions (entities, relationships, context)
- Semantic search via vector embeddings (ChromaDB, SQLite, Neo4j)
- Visual mind map generation from Markdown via Markmap
- Composable: mix and match servers for memory, search, and visualization
- Full data ownership, all data stored locally

**ND-Specific Strengths:**
- Visual mind maps benefit spatial thinkers
- Persistent AI memory learns user patterns over time
- Semantic search compensates for poor verbal recall

**Limitations:**
- Requires technical sophistication to deploy
- No mobile support, no standardized UX
- No task management or ND-specific accommodations
- Fragmented ecosystem, few mature implementations

**Pricing:** Free and open-source.

**Verdict:** The MCP pattern represents the architectural future that Yar builds toward. Yar should expose its knowledge graph as an MCP server and integrate Markmap visualization into its UI. This makes Yar's data accessible to any MCP-compatible AI client.

---

### 5.9 Anytype

**Overview:** Local-first, open-source, E2E encrypted knowledge management platform. Object-based with types, templates, and relations. Yar's planned primary storage backend.

**Key Features:**
- Object types with templates and relations (typed knowledge objects)
- Sets and Collections for dynamic object views
- Graph view for relationship exploration
- E2E encryption with recovery key
- Syncing across devices via Anytype middleware
- Full offline support with conflict resolution
- Open-source (Any-sync protocol)

**ND-Specific Strengths:**
- Local-first eliminates internet anxiety during focus sessions
- Type system provides structure without complexity overhead
- Graph view supports non-linear thinking

**Limitations:**
- No AI integration (no LLM, no automation)
- Limited time management features
- Smaller community than Notion/Obsidian
- No TTS or voice input

**Pricing:** Free core. Memberships available for expanded storage.

**Verdict:** Anytype provides the local-first, encrypted, typed-object storage layer that Yar builds upon. Its type/template/relation model maps well to Yar's object system. Yar adds the AI agent layer, ND-specific accommodations, voice-first capture, and emotional awareness that Anytype lacks.

---

## 6. Yar Feature Adoption Roadmap

### Priority 1: Adopt Immediately (Gaps in all competitors)

| Feature | Source Inspiration | Yar Implementation |
|:---|:---|:---|
| **Spiciness slider for task decomposition** | Goblin Tools Magic ToDo | Build into Yar's AI agent: user slides 1-5 to control how granularly the agent breaks down tasks |
| **Time estimation for tasks** | Goblin Tools Estimator | Agent estimates duration based on historical data + task complexity |
| **Brain dump compiler** | Goblin Tools Compiler | Extend capture pipeline: voice/text brain dump to structured YarObjects via AI |
| **Proactive task extraction** | Saner AI Skai | Agent monitors captures, calendar, and linked sources; surfaces action items |
| **Emoji sentiment on tasks** | Leantime LEO | Add optional emoji rating to YarObjects, feed into AI prioritization |
| **Schema-based node types (Supertags)** | Tana | Node types with field definitions, inheritance (Extend), and composition |
| **Queries as first-class objects** | Tana Live Searches | Query objects stored and embedded like any other node; live-updating views |
| **Multi-view rendering** | Tana / Capacities | List, Table, Kanban, Calendar views for query results |

### Priority 2: Adopt Next Phase (Strong patterns from leaders)

| Feature | Source Inspiration | Yar Implementation |
|:---|:---|:---|
| **Focus mode** | Super Productivity | Full-screen single-task view in Flutter app with active voice session timer |
| **Idle detection** | Super Productivity | Phone: accelerometer/screen-off; Desktop: Electron `powerMonitor` |
| **Break reminders** | Super Productivity | Configurable, non-judgmental nudges that learn personal fatigue patterns |
| **Template bundles** | Tana | Composable workflow packages (types + fields + commands + views) |
| **PiP Focus Window** | Saner AI | Floating window keeping current priority visible across apps |
| **AI daily planner** | Saner AI | "Plan my day" generates time-blocked schedule from tasks/calendar/notes |
| **Tone analysis** | Goblin Tools Judge | Emotional tone interpretation for social communication support |
| **TTS with synchronized highlighting** | Speechify | Built-in TTS using open-source engines (Coqui/Piper) with word tracking |
| **"Thinking in things" UX** | Capacities | Type-creation experience with auto-prompted fields and visual templates |

### Priority 3: Strategic Differentiators (No competitor offers these)

| Feature | Gap Analysis | Yar Advantage |
|:---|:---|:---|
| **Voice-first emotional awareness** | No tool combines voice input + emotion tracking + AI response | Yar's Gemma + HuBERT pipeline is unique |
| **CAP safety gate** | No tool provides clinical-adjacent safety boundaries | Yar's CAP framework is unique in the market |
| **Local-first AI knowledge graph** | Tana is cloud-only; Capacities is proprietary; MCP pattern requires tech setup | Yar + Anytype provides accessible local-first KG |
| **Unified ND companion** | Every tool solves 1-2 problems; no tool solves all | Yar integrates task + time + knowledge + emotion + AI |
| **MCP server interface** | Only Leantime offers MCP; none expose personal KG via MCP | Yar as first ND-focused MCP server |
| **On-device multi-modal AI** | Saner/Goblin use cloud AI; no tool runs AI locally | Yar's on-device Gemma/HuBERT enables offline AI |

---

## 7. Gap Analysis

### The Unified Companion Gap

The market has fragmented ND support across specialized tools. Users currently need 3-5 tools to cover their needs:

| Need | Current Solution | Problem |
|:---|:---|:---|
| Task execution + time management | Super Productivity | No AI, no knowledge management |
| Knowledge graph + type system | Tana or Capacities | No time management, proprietary, no emotional awareness |
| Task decomposition + time estimation | Goblin Tools | No persistence, no integration, stateless |
| Proactive AI assistant | Saner AI | Cloud-only, no offline, limited export |
| Reading accessibility | Speechify | No task/knowledge management, expensive |

**No single tool combines:**
1. Task execution with time-awareness (Super Productivity)
2. Typed knowledge graph with schema inheritance (Tana + Capacities)
3. AI-powered task decomposition with granularity control (Goblin Tools)
4. Proactive, context-aware AI assistance (Saner AI)
5. Multimodal accessibility (Speechify)
6. Local-first data sovereignty (Anytype + MCP)
7. Emotional awareness and safety (CAP, unique to Yar)

This is Yar's opportunity. By unifying these capabilities into a single, local-first, AI-native companion that adapts to each user's cognitive profile, Yar fills the gap that the entire market leaves open.

### Missing from ALL Tools

| Capability | Status Across All 9 Tools |
|:---|:---|
| Voice-first emotional awareness | Absent in all |
| Clinical-adjacent safety boundaries | Absent in all |
| On-device AI for offline ND support | Absent in all (Speechify has on-device TTS only) |
| Personalized cognitive profile adaptation | Absent in all |
| Cross-tool data portability standard | Absent in all (each uses proprietary formats) |
| Biomedical domain integration | Absent in all |

---

## 8. Methodology Notes

**Scoring Criteria:**
- Scores reflect feature depth, polish, and relevance to neurodivergent users
- A score of 10 indicates best-in-class within this comparison set, not perfection
- Scores weight actual user experience over marketing claims
- Open-source scores reflect both code availability and permissiveness of license

**Research Sources:**
- Official product websites and documentation
- GitHub repositories (Super Productivity, Leantime, Anytype)
- Product review aggregators (G2, ProductHunt)
- Community discussions (Reddit, HackerNews)
- Deep-dive analysis documents (Tana: 825 lines, Capacities: 904 lines, CAP/Yar: 450 lines)
- Live web research (Goblin Tools, Saner AI, Speechify, May 2026)
- Previous Cytognosis analysis (Leantime vs Super Productivity, May 2026)

**Changes from Version 1.0:**
- Added Capacities (from capacities-deep-dive.md, 904-line analysis)
- Added Anytype (from cap_yar_comprehensive_reference.md, Yar's planned storage backend)
- Enriched Tana analysis with Supertag schema details, command nodes, template bundles (from 825-line deep dive)
- Enriched Goblin Tools with full 9-tool inventory, multi-model architecture, Consultant + Taskmaster tools
- Enriched Saner AI with Skai multi-model details (GPT-4/Claude 3/Gemini Pro), Ally search model, PiP Focus Mode
- Enriched Speechify with API details (Python + TypeScript SDKs), voice cloning, on-device iOS voices, billing complaints
- Updated recommendations to incorporate Supertag/type system adoption as Priority 1

**Limitations:**
- Pricing and features reflect the state of each tool as of May 2026
- ND Visual Organizer (MCP) represents an architectural pattern, not a single product
- Accessibility scores are based on publicly available information; formal WCAG audits were not conducted
- Capacities and Anytype analysis draws from prior deep-dive documents rather than live web research

**Conflict of Interest Disclosure:**
- Cytognosis Foundation has no financial relationship with any tool analyzed
- Anytype is Yar's planned storage backend; this relationship is disclosed and scores reflect independent assessment
- This comparison serves Yar's product development roadmap exclusively

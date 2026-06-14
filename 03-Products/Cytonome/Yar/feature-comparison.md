> **Status**: Active
> **Date**: 2026-06-14
> **Author**: @mohammadi
> **Audience**: engineers, stakeholders
> **Tags**: `cytonome`, `features`, `yar`

# Yar Feature Comparison: Neurodivergent-Friendly Task & Knowledge Management

**Document Type:** Market & Feature Research
**Author:** Cytognosis AI Agent
**Date:** 2026-05-29
**Version:** 1.0
**Scope:** 7-tool comparative analysis for Yar product roadmap
**Status:** Draft for review

---

## 1. Master Feature Matrix

Scores use a 0–10 scale: **0** = absent, **3** = basic/limited, **5** = adequate, **7** = strong, **10** = best-in-class.

| Category | Leantime | Super Productivity | Tana | Goblin Tools | Saner AI | Speechify | ND Visual Organizer (MCP) |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **Task Management** | 8 | 9 | 6 | 5 | 7 | 0 | 2 |
| **Time Management** | 5 | 10 | 2 | 4 | 3 | 0 | 0 |
| **Knowledge Management** | 6 | 3 | 10 | 2 | 8 | 3 | 8 |
| **AI Integration** | 7 | 2 | 8 | 9 | 9 | 7 | 6 |
| **ND-Specific Features** | 7 | 8 | 5 | 10 | 6 | 7 | 4 |
| **Collaboration** | 7 | 2 | 7 | 0 | 3 | 2 | 0 |
| **Integration Ecosystem** | 6 | 9 | 5 | 1 | 7 | 4 | 8 |
| **Open Source / Self-Hosted** | 9 | 10 | 0 | 0 | 0 | 0 | 10 |
| **Accessibility** | 6 | 7 | 5 | 8 | 5 | 9 | 3 |
| **Mobile Support** | 6 | 8 | 5 | 7 | 6 | 9 | 0 |
| **Cost** | 8 | 10 | 5 | 10 | 5 | 3 | 10 |
| **Data Portability** | 6 | 8 | 3 | 1 | 4 | 2 | 7 |
| **TOTAL** | **81** | **86** | **61** | **57** | **63** | **46** | **58** |

---

## 2. Comparative Landscape Analysis

The neurodivergent productivity tool market splits into four distinct clusters: task-focused execution engines, knowledge-graph organizers, AI-augmented assistants, and accessibility-first utilities. No single tool covers the full spectrum of executive function support that Yar targets. Super Productivity leads in raw feature coverage (86/120) by combining deep time tracking, focus-mode discipline, and broad integrations under a permissive MIT license. Leantime follows (81/120) as the only tool that explicitly markets itself to ADHD, dyslexia, and autism users while offering enterprise-grade project management.

The knowledge-management cluster (Tana, Saner AI, ND Visual Organizer) excels at capturing and connecting ideas but lacks the time-awareness and focus-mode features that neurodivergent users depend on for daily execution. Tana's Supertag system represents the most sophisticated personal knowledge graph, yet its proprietary, cloud-only architecture and steep learning curve create barriers for the exact population it could serve best. Saner AI's proactive task extraction from email/calendar/notes addresses the "invisible workload" problem that disproportionately affects ADHD users, but locks data in a closed SaaS model.

Goblin Tools and Speechify occupy a unique "single-purpose excellence" niche. Goblin Tools' Magic ToDo with its spiciness slider is the purest implementation of AI-powered task decomposition for neurodivergent users, free and frictionless. Speechify transforms reading into listening, a modality shift that benefits dyslexic users and those with attention difficulties. Neither tool manages tasks or knowledge in any persistent way, making them complementary utilities rather than competitors. The ND Visual Organizer (MCP) pattern represents an emerging category: AI-native knowledge infrastructure that operates as a protocol layer rather than an application, offering the highest composability but requiring technical sophistication to deploy.

---

## 3. Bullet-Point Summary

- **Best overall feature coverage:** Super Productivity (86/120), free, open-source, cross-platform
- **Best ND-specific design:** Goblin Tools (10/10), purpose-built AI utilities for executive dysfunction
- **Best knowledge management:** Tana (10/10), Supertag-based knowledge graph with live search nodes
- **Best AI integration:** Goblin Tools and Saner AI (tied at 9/10), both use AI as the primary interaction model
- **Best for time blindness:** Super Productivity (10/10), Pomodoro, idle detection, break reminders, focus mode
- **Best accessibility:** Speechify (9/10), TTS with synchronized highlighting addresses reading disabilities directly
- **Best data sovereignty:** Super Productivity and ND Visual Organizer (MCP) (both 10/10), fully local-first or self-hosted
- **Biggest gap across all tools:** No tool combines task execution, knowledge management, and ND-specific accommodations in a single, open-source, local-first package. This is Yar's opportunity.

---

## 4. Tool Groups

### Group A: Task-Focused Execution Engines
**Leantime** and **Super Productivity**

Both tools center on getting tasks done. Super Productivity emphasizes individual deep work with Pomodoro timers, idle detection, and a keyboard-first interface. Leantime targets teams with Kanban boards, Gantt charts, and sprint management. Both include task CRUD, subtasks, and tagging systems. Super Productivity's MIT license and local-first architecture make it the stronger foundation for Yar's task execution layer.

### Group B: Knowledge-Focused Organizers
**Tana** and **ND Visual Organizer (MCP)**

These tools prioritize capturing, connecting, and retrieving knowledge. Tana's Supertags turn every node into a typed object with custom fields, creating a personal knowledge graph that surfaces information through live search queries. The ND Visual Organizer (MCP) pattern achieves similar goals through knowledge graph MCP servers (Memento, cognee, Knowledge Graph Memory) combined with Markmap visualization. Tana offers superior UX; the MCP approach offers superior composability and data ownership.

### Group C: AI-Augmented Assistants
**Goblin Tools** and **Saner AI**

AI drives the core interaction model in both tools. Goblin Tools provides focused micro-utilities (Magic ToDo, Estimator, Judge, Compiler, Formalizer) that each solve one executive function challenge well. Saner AI takes a broader approach, using its Skai agent to proactively extract tasks, auto-tag notes, and surface semantic connections across email, calendar, and documents. Goblin Tools wins on accessibility and cost (free); Saner AI wins on scope and automation.

### Group D: Accessibility-First Utilities
**Speechify**

Speechify stands alone in the "modality transformation" category. By converting text to high-quality audio with synchronized visual highlighting, it serves users who process information better through listening than reading. Its 900 wpm speed, 1,000+ voices, and 60+ language support make it the most comprehensive TTS solution in this comparison. It addresses a specific accessibility need (reading difficulty) rather than general task/knowledge management.

---

## 5. Per-Tool Deep Dives

### 5.1 Leantime

**Overview:** Open-source project management platform (AGPLv3) built on PHP + MySQL. Markets itself as "project management for non-project-managers" with explicit neurodivergent support for ADHD, dyslexia, and autism. Offers a clean hexagonal architecture with 57 domain modules.

**Key Features:**
- Task CRUD with unlimited subtasks, dependencies, and multiple views (Kanban, table, list, calendar, Gantt)
- LEO AI assistant for task prioritization using Pareto Principle and Goldilocks method
- Emoji sentiment tracking: users rate emotional response to tasks, AI adapts prioritization accordingly
- Sprint management, milestone tracking, retrospectives, goals, and strategy canvases (Lean, SWOT, BMC)
- Wiki/docs system, idea boards, file storage (S3 or local)
- User roles, 2FA, LDAP/OIDC, plugin marketplace
- MCP Server plugin for AI assistant integration (read projects, create tasks, log time)

**ND-Specific Strengths:**
- Emoji sentiment tracking directly addresses emotional dysregulation around tasks
- AI prioritization reduces decision fatigue (a core ADHD challenge)
- "My Work" dashboard simplifies the interface to reduce cognitive overload
- Behavioral science integration in task structuring

**Limitations:**
- Server-first architecture requires hosting infrastructure (not local-first)
- No Pomodoro timer, idle detection, or focus mode
- No voice input or TTS
- PHP + MySQL stack limits modern web development flexibility
- Team-oriented features add complexity for personal use

**Pricing:**
- Free/open-source core (AGPLv3)
- Plugin marketplace with Personal tier (1–3 users) and team brackets
- Premium support packages for enterprise

**Verdict:** Strong project management foundation with genuine ND awareness. The emoji sentiment tracking and AI prioritization are features Yar should adopt. The server-first architecture and team-oriented feature set make it less suitable as a personal cognitive companion.

---

### 5.2 Super Productivity

**Overview:** Open-source (MIT license) task manager and time tracker built with Angular, deployed via Electron (desktop), Capacitor (mobile), and PWA (web). Focuses on deep work and ADHD-friendly workflows. Local-first with optional sync.

**Key Features:**
- Full task CRUD with subtasks, tags, projects, and notes (markdown + checklists)
- Integrated time tracking with per-task timers
- Pomodoro timer with configurable work/break intervals
- Idle detection (Electron: `powerMonitor.getSystemIdleTime()`; Web: mouse/keyboard listeners)
- Take-a-break reminders with configurable intervals
- Focus mode: full-screen single-task view with timer and progress bar
- Tracking reminders for gentle nudges
- Daily planner with drag-and-drop scheduling
- Integrations: Jira, GitHub, GitLab, Trello, Linear, ClickUp, OpenProject, Azure DevOps, CalDAV
- Cross-device sync via WebDAV, Dropbox, or SuperSync (peer-to-peer encrypted)
- Operation-log CRDT-like sync architecture with vector clocks
- "Finish Day" button that celebrates completed work

**ND-Specific Strengths:**
- Focus mode blocks navigation to other tasks (addresses ADHD distraction)
- Idle detection auto-pauses time tracking (reduces guilt from hyperfocus interruptions)
- Break reminders prevent burnout during hyperfocus sessions
- Keyboard-first design reduces executive function load of mouse navigation
- "Finish Day" celebration provides dopamine reward for task completion
- Clean, distraction-free interface reduces visual overwhelm

**Limitations:**
- No AI features (task breakdown, prioritization, or smart suggestions)
- No knowledge management (no wiki, notes beyond per-task, no linking)
- No voice input or TTS
- No emotion tracking or sentiment analysis
- Notes are task-attached only, no standalone knowledge base
- No external API for third-party tools

**Pricing:**
- Completely free and open-source (MIT license)
- No premium tier, no ads, no telemetry
- Developer accepts donations

**Verdict:** The strongest open-source foundation for Yar's task execution and time management layer. The focus mode, idle detection, break reminders, and Pomodoro features directly address ADHD challenges. Yar should study and adopt Super Productivity's patterns while adding the AI, knowledge management, and emotional awareness layers that it lacks.

---

### 5.3 Tana (Outliner)

**Overview:** AI-native, graph-based knowledge management platform (proprietary, cloud-based). Uses Supertags to transform unstructured notes into typed, queryable data. Recently split into Tana Outliner (personal) and New Tana/T2 (team collaboration).

**Key Features:**
- Supertags: turn any node into a typed object with custom fields (e.g., #Task, #Meeting, #Person)
- Search Nodes (Live Queries): dynamic, live-updating views that pull matching nodes from entire workspace
- AI integration: live transcription, AI commands for data extraction/reformatting, context-aware chat with notes
- Personal knowledge graph: every bullet is a node with multi-directional links
- Tana Capture mobile app: text, voice memos (auto-transcription), photos, file uploads
- Input API for sending data into workspace from external tools
- Readwise integration, Google Calendar sync

**ND-Specific Strengths:**
- Flexible structure accommodates non-linear thinking (no rigid folder hierarchy)
- Supertags reduce cognitive load of categorization (apply tag, get auto-fields)
- Voice capture on mobile reduces friction for "capture at speed of thought"
- Live Search nodes surface forgotten information automatically

**Limitations:**
- Steep learning curve creates cognitive overload for the ND users it could help most
- Proprietary, cloud-only (Firebase backend), no offline-first or local file ownership
- No time tracking, Pomodoro, idle detection, or focus mode
- No task prioritization or AI-driven scheduling
- Input API only (no bidirectional API for full data export)
- No emotion tracking or sentiment analysis
- Visual/functional noise from abundance of features if not carefully customized

**Pricing:**
- Free: Core editor, 500 AI credits/month
- Plus: ~$10/month (2,000 AI credits, Google Calendar, mobile/desktop)
- Pro: ~$18/month (5,000 AI credits, Readwise, advanced automation)
- Student/NGO discounts available

**Verdict:** The most sophisticated knowledge graph UX in this comparison. Supertags and Live Search nodes represent the gold standard for personal knowledge management. However, the proprietary cloud lock-in, absent time management features, and steep learning curve limit its fit for Yar's target users. Yar should study Tana's Supertag pattern and implement a similar typed-object system on top of Anytype's local-first architecture.

---

### 5.4 Goblin Tools

**Overview:** Collection of free, AI-powered micro-utilities designed specifically for neurodivergent users (ADHD, autism). Built by a solo developer. Runs as a web app with optional paid mobile apps.

**Key Features:**
- **Magic ToDo:** Breaks large tasks into smaller steps with a "spiciness slider" (1–5) controlling decomposition granularity
- **Formalizer:** Rewrites text to match a target tone (professional, casual, polite, concise)
- **Estimator:** Provides time estimates for tasks, combating time blindness
- **Judge:** Analyzes text to interpret likely emotional tone/intent (helps with social communication)
- **Compiler:** Takes scattered brain dump notes and organizes them into clean, actionable task lists
- **Chef:** Generates recipes from available ingredients
- **Professor:** Simplified explanations and crash courses on topics

**ND-Specific Strengths:**
- Spiciness slider is the purest implementation of progressive task decomposition for ADHD
- Estimator directly addresses time blindness (a defining ADHD challenge)
- Judge helps autistic users interpret social/emotional tone in messages
- Compiler transforms brain dump chaos into structure (addresses working memory overload)
- Zero friction: no account required, no setup, instant utility
- Free web access removes financial barriers

**Limitations:**
- No persistent data storage (stateless micro-utilities, no memory between sessions)
- No task management (no lists, no tracking, no completion status)
- No knowledge management (no notes, no linking, no search)
- No time tracking or Pomodoro features
- No collaboration features
- No integrations or API
- No mobile app offline capability (web-only free tier)
- Proprietary (not open-source)

**Pricing:**
- Web: Completely free, no ads, no paywalls
- iOS/Android: One-time low-cost purchase (~$2–5)

**Verdict:** The most accessible and targeted ND tool in this comparison. Every feature solves a specific executive function challenge. Yar should integrate Goblin Tools' concepts directly: the spiciness slider for task decomposition, the Estimator for time awareness, and the Compiler for capture-to-structure processing. These features should be built into Yar's AI agent layer rather than requiring users to context-switch to a separate tool.

---

### 5.5 Saner AI

**Overview:** AI-powered productivity platform (proprietary SaaS) marketed as an "Executive OS" and "Second Brain." Uses Skai, a proactive AI assistant, to automatically organize, tag, and manage knowledge across emails, calendar, and documents.

**Key Features:**
- Skai AI assistant: learns from user data, auto-organizes, auto-tags, auto-categorizes notes
- Proactive task extraction from emails, notes, documents, and calendar events
- Semantic search using natural language queries (meaning-based, not keyword-based)
- Unified knowledge base connecting Google Drive, Gmail, Slack, Calendar
- Voice-to-text capture, Chrome extension for web clipping, file imports (PDF, Markdown, Word)
- Auto-linking of related items across data sources

**ND-Specific Strengths:**
- Proactive task extraction reduces "invisible workload" (tasks hiding in emails/notes)
- Auto-tagging eliminates the executive function burden of manual categorization
- Semantic search compensates for poor recall (find by meaning, not exact keywords)
- Reduces context-switching by unifying disparate data sources

**Limitations:**
- Cloud-only, proprietary, no self-hosting option
- No task execution features (no Pomodoro, focus mode, time tracking)
- No emotion tracking or sentiment analysis
- Limited free tier (30 AI messages/month, 100 notes)
- Data locked in Saner's infrastructure (limited export)
- No open-source components
- External AI model access may incur additional costs

**Pricing:**
- Free: 30 AI messages/month, 100 notes
- Starter: $12/month ($8 annual), 30 AI messages/day, 1,000 notes
- Standard: $20/month ($16 annual), unlimited AI messages/notes

**Verdict:** Saner AI's proactive task extraction and semantic search represent exactly the kind of "invisible assistant" that Yar's agent layer should become. The concept of Skai monitoring incoming information and surfacing action items aligns with Yar's mission. Yar should implement similar proactive intelligence locally, using on-device models rather than cloud APIs, to preserve data sovereignty.

---

### 5.6 Speechify

**Overview:** Text-to-speech platform (proprietary SaaS) that converts written content to natural-sounding audio with synchronized visual highlighting. Available across web, desktop, and mobile.

**Key Features:**
- TTS with synchronized word-by-word highlighting (dual-channel processing: visual + auditory)
- Adjustable speed up to 5x (900 wpm) with speed ramping for gradual adaptation
- 1,000+ AI voices including celebrity voices across 60+ languages
- AI summaries of long documents
- OCR scanning for printed/physical documents
- Voice typing (dictation)
- Cross-platform sync (web, Mac, Windows, iOS, Android)
- Chrome extension for reading web pages aloud

**ND-Specific Strengths:**
- Synchronized highlighting helps maintain focus during reading (addresses ADHD attention drift)
- Audio modality bypasses reading difficulties (dyslexia support)
- Speed control allows users to find their optimal processing rate
- Speed ramping trains gradual comprehension improvement
- AI summaries reduce cognitive load of long documents
- OCR extends accessibility to physical documents

**Limitations:**
- No task management, time tracking, or planning features
- No knowledge management (no notes, no linking, no organization)
- No persistent user data beyond reading library
- Expensive premium tier ($139/year or $29/month)
- Free tier severely limited (10 robotic voices, 1.5x speed cap)
- Proprietary, no open-source components
- No offline capabilities on free tier
- Celebrity voices feel gimmicky, detract from accessibility focus

**Pricing:**
- Free: Basic TTS, 10 standard voices, 1.5x speed cap
- Premium: ~$139/year ($11.58/month) or $29/month, full feature access

**Verdict:** Speechify fills a specific accessibility gap that no other tool in this comparison addresses: reading difficulty. The synchronized highlighting + audio combination creates dual-channel input that materially helps users with dyslexia and attention difficulties. Yar should implement basic TTS with synchronized highlighting as an accessibility feature, but does not need to compete with Speechify's voice library or speed capabilities. Integrating with Speechify's API (if available) or using open-source TTS (Coqui, Piper) would be more appropriate than building a competing product.

---

### 5.7 ND Visual Organizer (MCP)

**Overview:** Not a single product but an emerging architectural pattern combining knowledge graph MCP servers, semantic search, and Markmap visualization. Represents the composable, AI-native approach to knowledge management through the Model Context Protocol.

**Key Features:**
- Knowledge graph storage via MCP servers (Knowledge Graph Memory, Memento MCP, cognee)
- Persistent AI memory across sessions (entities, relationships, context)
- Semantic search via vector embeddings (ChromaDB, SQLite, Neo4j backends)
- Visual mind map generation from Markdown via Markmap-based MCP servers
- Composable: mix and match servers for memory, search, and visualization
- Full data ownership: all data stored locally in user-controlled databases

**ND-Specific Strengths:**
- Visual mind maps provide spatial representation that benefits visual thinkers
- Persistent AI memory means the AI "remembers" user preferences and patterns over time
- Semantic search compensates for poor verbal recall (find by concept, not keyword)
- Composable architecture allows customization to individual cognitive needs

**Limitations:**
- Requires technical sophistication to set up and maintain
- No task management, time tracking, or planning features
- No mobile support (MCP servers run on desktop/server only)
- No standardized UX (each MCP client provides its own interface)
- No collaboration features
- No emotion tracking or ND-specific accommodations
- Fragmented ecosystem: many small projects, few mature/stable options
- No accessibility standards (relies on MCP client's accessibility)

**Pricing:**
- Free and open-source (MIT/Apache 2.0 licenses typical)
- Requires self-hosting infrastructure

**Verdict:** The MCP knowledge graph pattern represents the architectural future that Yar should build toward. Yar's Anytype integration already provides a local knowledge graph; adding MCP server interfaces would allow Yar's data to be accessible to any MCP-compatible AI client. The visualization capabilities (Markmap mind maps) are directly relevant for ND users who think spatially. Yar should expose its knowledge graph as an MCP server and integrate Markmap-style visualization into its UI.

---

## 6. Recommendations for Yar

### Priority 1: Adopt Immediately (Gaps in all competitors)

| Feature | Source Inspiration | Yar Implementation |
|:---|:---|:---|
| **Spiciness slider for task decomposition** | Goblin Tools Magic ToDo | Build into Yar's AI agent: user slides 1–5 to control how granularly the agent breaks down tasks |
| **Time estimation for tasks** | Goblin Tools Estimator | Agent estimates duration based on historical data + task complexity |
| **Brain dump compiler** | Goblin Tools Compiler | Extend capture pipeline: voice/text brain dump → structured YarObjects via AI |
| **Proactive task extraction** | Saner AI Skai | Agent monitors captures, calendar, and linked sources → surfaces action items |
| **Emoji sentiment on tasks** | Leantime LEO | Add optional emoji rating to YarObjects, feed into AI prioritization |

### Priority 2: Adopt in Next Phase (Strong patterns from leaders)

| Feature | Source Inspiration | Yar Implementation |
|:---|:---|:---|
| **Focus mode** | Super Productivity | Full-screen single-task view in Flutter app with active voice session timer |
| **Idle detection** | Super Productivity | Phone: accelerometer/screen-off; Desktop: Electron `powerMonitor` |
| **Break reminders** | Super Productivity | Configurable, non-judgmental nudges that learn personal fatigue patterns |
| **Supertag-style typed objects** | Tana | YarObject types with auto-populated fields via Anytype supertag equivalent |
| **Live search / saved queries** | Tana Search Nodes | Knowledge graph queries that auto-update as new captures arrive |

### Priority 3: Strategic Differentiators (No competitor offers these)

| Feature | Gap Analysis | Yar Advantage |
|:---|:---|:---|
| **Voice-first emotional awareness** | No tool combines voice input + emotion tracking + AI response | Yar's Gemma + HuBERT pipeline is unique |
| **CAP safety gate** | No tool provides clinical-adjacent safety boundaries | Yar's CAP framework is unique in the market |
| **Local-first AI knowledge graph** | Tana is cloud-only; MCP pattern requires tech setup | Yar + Anytype provides accessible local-first KG |
| **Unified ND companion** | Every tool solves 1–2 problems; no tool solves all | Yar integrates task + time + knowledge + emotion + AI |
| **MCP server interface** | Only Leantime offers MCP; none expose personal KG via MCP | Yar could be the first ND-focused MCP server |

### Key Insight

The market has fragmented ND support across specialized tools. Users currently need 3–4 tools to cover their needs: Super Productivity for tasks/time, Tana or Saner AI for knowledge, Goblin Tools for task decomposition, and Speechify for reading. Yar's opportunity is to unify these capabilities into a single, local-first, AI-native companion that adapts to each user's cognitive profile. The competitive moat is the combination of voice-first capture, emotional awareness, and proactive AI, all running on-device.

---

## 7. Methodology Notes

**Scoring Criteria:**
- Scores reflect feature depth, polish, and relevance to neurodivergent users
- A score of 10 indicates best-in-class within this comparison set, not perfection
- Scores weight actual user experience over marketing claims
- Open-source scores reflect both code availability and permissiveness of license

**Research Sources:**
- Official product websites and documentation
- GitHub repositories (Super Productivity, Leantime)
- Product review aggregators (G2, ProductHunt)
- Community discussions (Reddit, HackerNews)
- Previous Cytognosis analysis (Leantime vs Super Productivity deep dive, May 2026)

**Limitations:**
- Pricing and features reflect the state of each tool as of May 2026
- ND Visual Organizer (MCP) represents an architectural pattern, not a single product, so scoring reflects the best available implementations
- Accessibility scores are based on publicly available information; formal WCAG audits were not conducted
- AI integration scores reflect current capabilities; all tools are actively developing AI features

**Conflict of Interest Disclosure:**
- Cytognosis Foundation has no financial relationship with any tool analyzed
- This comparison serves Yar's product development roadmap exclusively

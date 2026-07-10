# Open-Source ADHD Tool Codebase Analysis

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: engineers
> **Tags**: `engineering`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)

> **Document Type:** Technical Codebase Deep-Dive
> **Author:** Cytognosis AI Agent
> **Date:** 2026-05-31
> **Version:** 1.0
> **Repos Analyzed:**
> - [Leantime](https://github.com/Leantime/leantime) (AGPL-3.0, PHP + MySQL)
> - [Super Productivity](https://github.com/johannesjo/super-productivity) (MIT, Angular + TypeScript)
> - [OMI AI](https://github.com/BasedHardware/omi) (MIT, Python + Dart + Swift)
> **Index:** Zoekt (383 MB total index across all three repos)

---

## 1. Repository Overview

| Metric | Leantime | Super Productivity | OMI AI |
|:---|:---:|:---:|:---:|
| **License** | AGPL-3.0 | MIT | MIT |
| **Primary Language** | PHP (838 files) | TypeScript (1,782 files) | Python (653), Dart (607), Swift (359) |
| **Template/View Files** | Blade (PHP templates) | HTML (212), SCSS (256) | Dart widgets |
| **Clone Size** | 80 MB | 79 MB | 1.2 GB |
| **Zoekt Index Size** | 72 MB (1,491 files) | 86 MB (4,192 files) | 243 MB (5,784 files) |
| **Domain Modules** | 57 | 45+ feature modules | Backend + App + Plugins |
| **Architecture** | Hexagonal (Domain-driven) | NgRx state management | FastAPI + Flutter + Firebase |

---

## 2. Leantime Architecture Analysis

### 2.1 Domain-Driven Design

Leantime uses a clean hexagonal architecture with 57 domain modules organized under `app/Domain/`. Each module follows a consistent structure:

```
Domain/{ModuleName}/
├── Controllers/     # HTTP request handlers
├── Services/        # Business logic
├── Repositories/    # Data access
├── Models/          # Data structures
├── Templates/       # Blade views
├── Events/          # Domain events (some modules)
└── Composers/       # View composers (some modules)
```

**Key Domain Modules (ND-Relevant):**

| Module | Function | ND Relevance |
|:---|:---|:---|
| `Canvas` | Strategy canvases, retrospectives | Emoji sentiment tracking lives here |
| `Tickets` | Core task CRUD | Main task management |
| `Sprints` | Sprint planning + velocity | Time estimation |
| `Dashboard` | My Work view | Reduces cognitive overload |
| `Gamecenter` | Achievement system | Dopamine rewards |
| `Calendar` | Calendar views | Time awareness |
| `Wiki` | Documentation | Knowledge management |
| `Ideas` | Idea boards | Brain dump capture |
| `Notifications` | Alert system | Reminder infrastructure |
| `Queue` | Background processing | Async task execution |
| `Reports` | Analytics + reporting | Progress visualization |

### 2.2 AI/Emotion Features (8 files in Domain)

Leantime's emotional tracking surfaces primarily in the Canvas module:

- **Emoji sentiment fields** appear in Canvas repositories and templates
- The `Gamecenter` module provides achievement-based dopamine feedback
- AI integration (31 files in `app/`) connects to OpenAI for LEO assistant
- Sprint models include emotional metadata alongside velocity tracking

### 2.3 MCP Integration

Leantime has an MCP test file at `tests/Httprequests/MCP.http`, indicating early-stage MCP server capability. This is one of the few productivity tools with any MCP integration at all.

### 2.4 Code Quality Assessment

| Criterion | Score | Notes |
|:---|:---:|:---|
| **Modularity** | 8/10 | Clean DDD with 57 isolated domains |
| **Consistency** | 7/10 | Blade templates vary in structure |
| **Test Coverage** | 6/10 | Tests exist but coverage uncertain |
| **Documentation** | 7/10 | README, CONTRIBUTING, CLAUDE.md present |
| **Extensibility** | 8/10 | Plugin system with marketplace |
| **Modern Patterns** | 5/10 | PHP + MySQL stack limits modern dev |

---

## 3. Super Productivity Architecture Analysis

### 3.1 Angular + NgRx State Management

Super Productivity is a well-architected Angular application with a comprehensive NgRx store. The project structure separates concerns cleanly:

```
src/app/
├── core/              # Core services and utilities
├── core-ui/           # Shared UI components
├── features/          # Feature modules (45+)
├── pages/             # Route-level pages
├── pfapi/             # Data persistence API
├── plugins/           # Plugin system
├── root-store/        # Root NgRx state
└── routes/            # Route definitions
```

### 3.2 Feature Module Inventory (ND-Relevant)

| Feature Module | Files | Function | ND Relevance |
|:---|:---:|:---|:---|
| `focus-mode/` | 18+ files | Full-screen single-task with timer | **Critical**: blocks distraction, enforces single-task |
| `idle/` | 9 files | System idle detection | Auto-pauses tracking during hyperfocus breaks |
| `take-a-break/` | 1 file | Break reminder service | Prevents burnout during hyperfocus |
| `time-tracking/` | Multiple | Per-task time recording | Time awareness |
| `planner/` | Multiple | Day planning view | Task scheduling |
| `boards/` | Multiple | Kanban view | Visual organization |
| `work-context/` | Multiple | Context switching | Reduces context-switch cost |
| `finish-day-before-close/` | Multiple | Day completion flow | Dopamine closure |
| `reminder/` | Multiple | Task reminders | Prospective memory |
| `tracking-reminder/` | Multiple | Time tracking prompts | Time awareness |
| `simple-counter/` | Multiple | Simple task counters | Low-friction tracking |
| `task-repeat-cfg/` | Multiple | Recurring tasks | Routine building |

### 3.3 Focus Mode Deep Dive

The focus mode implementation is sophisticated, supporting three distinct modes:

```typescript
export enum FocusModeMode {
  'Flowtime' = 'Flowtime',   // Open-ended, break when ready
  'Pomodoro' = 'Pomodoro',   // Classic 25/5 intervals
  'Countdown' = 'Countdown', // Custom duration countdown
}
```

**Screen flow:**
1. `TaskSelection` → Choose which task to focus on
2. `DurationSelection` → Pick timer mode/duration
3. `Preparation` → Optional countdown before start
4. `Main` → Full-screen focus with timer
5. `Break` → Break timer with offer to continue
6. `SessionDone` → Celebration + next action

**Strategy Pattern:** Uses `FocusModeStrategy` interface for mode-specific behavior (session duration, break calculation, auto-start behavior). The Flowtime mode is especially relevant for ADHD, as it respects natural flow states rather than interrupting with rigid intervals.

### 3.4 Idle Detection Implementation

The idle detection module uses:
- **Desktop (Electron):** `powerMonitor.getSystemIdleTime()` for OS-level idle monitoring
- **Web:** Mouse/keyboard listener-based idle detection
- Auto-pauses time tracking when user goes idle
- Dialog prompts user on return: "What were you doing?"

### 3.5 Take-a-Break Service

Simple but effective: configurable interval, non-judgmental nudge. Learns personal fatigue patterns through usage data.

### 3.6 Code Quality Assessment

| Criterion | Score | Notes |
|:---|:---:|:---|
| **Modularity** | 9/10 | 45+ isolated feature modules with NgRx stores |
| **Consistency** | 9/10 | Strict Angular conventions throughout |
| **Test Coverage** | 7/10 | `.spec.ts` files alongside most components |
| **Documentation** | 8/10 | AGENTS.md, ARCHITECTURE-DECISIONS.md, CLAUDE.md |
| **Extensibility** | 7/10 | Plugin system, but less flexible than Leantime |
| **Modern Patterns** | 9/10 | Angular 18+, NgRx, standalone components |

---

## 4. OMI AI Architecture Analysis

### 4.1 Multi-Platform Architecture

OMI is the most complex codebase, spanning hardware wearable, mobile app, backend, desktop, plugins, and MCP server:

```
omi/
├── app/              # Flutter mobile app (Dart, 607 files)
├── backend/          # FastAPI server (Python, 653 files)
├── desktop/          # Desktop companion
├── mcp/              # MCP server (Python)
├── omi/              # Hardware firmware
├── omiGlass/         # Smart glasses firmware
├── plugins/          # Plugin ecosystem (50+ plugins)
└── scripts/          # Deployment and utilities
```

### 4.2 Backend Architecture (Python + FastAPI)

**Database Layer:** Firebase/Firestore-based with comprehensive modules:

| Database Module | Function | ND Relevance |
|:---|:---|:---|
| `memories.py` | Persistent memory storage | Long-term context retention |
| `conversations.py` | Conversation history | Session continuity |
| `tasks.py` | Task management | Action items |
| `action_items.py` | Extracted action items | Proactive task surfacing |
| `knowledge_graph.py` | Knowledge graph storage | Semantic relationships |
| `vector_db.py` | Vector embeddings | Semantic search |
| `focus_sessions.py` | Focus session tracking | Focus mode data |
| `goals.py` | Goal tracking | Long-term planning |
| `daily_summaries.py` | Daily summary generation | Review/reflection |
| `trends.py` | Pattern detection | Behavioral insights |

**Memory Model Categories:**
```python
class MemoryCategory(str, Enum):
    interesting = "interesting"  # AI-flagged interesting info
    system = "system"            # System-generated memories
    manual = "manual"            # User-created memories
    # + legacy categories for backward compatibility
```

### 4.3 AI/LLM Integration (171 backend files)

OMI has the deepest AI integration of any tool in this analysis:
- Multiple LLM provider support
- Real-time transcription processing
- Memory extraction from conversations
- Task/action item extraction
- Daily summary generation
- Trend detection and pattern analysis
- Voice emotion analysis (via Hume AI plugin)

### 4.4 Voice/Speech Pipeline (266 backend files)

The most extensive voice processing pipeline:
- Real-time audio streaming from wearable device
- Multiple transcription engines (Whisper, Deepgram)
- Diarization (speaker identification)
- Conversation segmentation
- Automatic summarization
- Action item extraction from spoken conversations

### 4.5 Plugin Ecosystem (50+ plugins)

OMI's plugin system is remarkably rich:

| Plugin | Function |
|:---|:---|
| `hume-ai` | Emotion detection from voice |
| `_mem0` | Memory management integration |
| `_multion` | Multi-browser automation |
| `composio` | Tool composability |
| `chatgpt` | ChatGPT integration |
| `ahda` | ADHD-specific assistant |
| `omi-notion-app` | Notion sync |
| `omi-linear-app` | Linear issue tracking |
| `omi-github-app` | GitHub integration |
| `omi-slack-app` | Slack notifications |
| `omi-clickup-app` | ClickUp integration |
| `omi-google-calendar-app` | Calendar sync |
| `omi-whoop-app` | Health wearable data |

The `ahda` plugin is particularly relevant, appears to be an ADHD-specific assistant plugin.

### 4.6 MCP Server

OMI provides a production-ready MCP server (`mcp-server-omi`) with the following tools:

| MCP Tool | Function |
|:---|:---|
| `get_memories` | Retrieve stored memories with filtering |
| `create_memory` | Create new memory entries |
| `delete_memory` | Remove memory entries |
| `edit_memory` | Update existing memories |
| `get_conversations` | Retrieve conversation history |
| `get_conversation_by_id` | Get specific conversation |
| `search_conversations` | Semantic conversation search |

This MCP server is MIT-licensed and could serve as a reference implementation for Yar's own MCP server.

### 4.7 App Architecture (Flutter + Dart)

The mobile app uses a clean provider-based state management:
```
app/lib/
├── backend/         # API client
├── core/            # Core services
├── models/          # Data models
├── pages/           # UI screens
├── providers/       # State management
├── services/        # Business logic
├── ui/              # Shared UI components
├── utils/           # Utilities
└── widgets/         # Reusable widgets
```

### 4.8 Code Quality Assessment

| Criterion | Score | Notes |
|:---|:---:|:---|
| **Modularity** | 7/10 | Multi-platform but some coupling |
| **Consistency** | 6/10 | Varies across Python/Dart/Swift |
| **Test Coverage** | 5/10 | Tests present but sparse |
| **Documentation** | 7/10 | AGENTS.md, README, CLAUDE.md per component |
| **Extensibility** | 9/10 | Rich plugin system, MCP server, API |
| **Modern Patterns** | 8/10 | FastAPI, Flutter, Firebase, MCP |

---

## 5. Cross-Codebase Pattern Analysis

### 5.1 Feature Implementation Heat Map

Pattern searches across all three codebases reveal implementation density:

| Pattern | Leantime | Super Productivity | OMI |
|:---|:---:|:---:|:---:|
| Focus Mode | 0 files | **80 files** | 22 files |
| Pomodoro/Timer | 72 files | **69 files** | 2 files |
| Idle Detection | 0 files | **9 files** | 0 files |
| Emotion/Mood/Sentiment | 8 files | 0 files | **23 files** |
| AI/LLM Integration | 31 files | 0 files | **171 files** |
| Task Decomposition | 0 files | 0 files | **133 files** |
| Voice/Speech | 0 files | 0 files | **266 files** |
| Knowledge Graph/Memory | 0 files | 0 files | **19 files** |

### 5.2 Complementary Strengths

The three codebases are remarkably complementary:

- **Leantime** excels at: DDD architecture, emoji sentiment tracking, project management, team collaboration
- **Super Productivity** excels at: Focus mode, idle detection, break reminders, time tracking, cross-platform deployment (Electron + Capacitor + PWA)
- **OMI** excels at: AI/voice pipeline, memory persistence, plugin ecosystem, MCP server, real-time transcription

### 5.3 Patterns to Adopt for Yar

| Pattern | Source | Implementation Notes |
|:---|:---|:---|
| **Focus Mode Strategy Pattern** | Super Productivity | `FocusModeStrategy` interface with Flowtime/Pomodoro/Countdown modes |
| **Idle Detection** | Super Productivity | Electron `powerMonitor` + web fallback |
| **NgRx Store Pattern** | Super Productivity | Feature-scoped state management |
| **Emoji Sentiment Fields** | Leantime | Canvas model pattern for task emotional tracking |
| **Memory Categories** | OMI | `MemoryCategory` enum with boosts/weights |
| **MCP Server Pattern** | OMI | FastMCP with CRUD + search tools |
| **Plugin Architecture** | OMI | Independent plugin modules with standard interface |
| **Knowledge Graph DB** | OMI | Firebase + vector DB dual storage |
| **Real-time Transcription** | OMI | Whisper + Deepgram with diarization |
| **Domain Module Pattern** | Leantime | Clean hexagonal with Controllers/Services/Repos |

---

## 6. Architecture Recommendations for Yar

### 6.1 State Management

Adopt Super Productivity's NgRx-inspired pattern but in Flutter's Riverpod/Bloc:
- Feature-scoped state modules
- Clear separation of UI state, timer state, and data state
- Strategy pattern for focus mode variants

### 6.2 AI Pipeline

Combine OMI's approach with local-first execution:
- Real-time voice → transcription → NER → task extraction pipeline
- Memory categorization with category boosts
- Vector DB for semantic search
- Daily summary generation from conversation history

### 6.3 Plugin System

OMI's plugin pattern provides the best extensibility model:
- Standard plugin interface with lifecycle hooks
- Independent deployment per plugin
- MCP server for external AI client access

### 6.4 Data Layer

Hybrid approach combining Anytype's local-first storage with OMI's knowledge graph:
- Anytype for typed object storage (local-first, E2E encrypted)
- Vector embeddings for semantic search
- Knowledge graph for relationship navigation
- MCP server for external access

---

## 7. Methodology Notes

**Analysis Tools:**
- Zoekt code indexing (383 MB index across 11,467 files)
- Direct grep-based pattern analysis
- File structure inspection
- Source code reading for critical modules

**Limitations:**
- Shallow clones (depth 1) may miss historical patterns
- Runtime behavior not tested (no builds or test runs)
- Plugin quality varies; only top-level analysis performed
- OMI's 1.2 GB clone includes binary assets (firmware, ML models)

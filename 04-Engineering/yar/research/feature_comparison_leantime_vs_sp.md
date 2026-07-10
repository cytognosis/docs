# Feature Comparison: Leantime vs Super Productivity vs Yar

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: engineers
> **Tags**: `engineering`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)

## Executive Summary

| Dimension | Leantime | Super Productivity | Yar (Cytonome) |
|-----------|----------|-------------------|----------------|
| **Core Identity** | Project management for non-PMs | Deep work task manager | Cognitive companion, by neurodivergent minds |
| **Architecture** | Server-side PHP + MySQL | Angular mono-app → Electron/Capacitor/Web | Python backend + Flutter mobile + browser extension |
| **ND Focus** | "Built for ADHD, dyslexia, autism" (marketing) | ADHD & Focus use-case page | **Core mission**: CAP safety gate, emotion tracking, local-first |
| **Data Model** | Server-first, SQL-backed | Local-first, IndexedDB | Local-first, knowledge graph (Anytype) |
| **License** | AGPLv3 | MIT | Apache 2.0 |

---

## 1. Feature Matrix

### Legend
- 🟢 **Perfect fit** for Yar's current/next phases
- 🟡 **Partial fit** — useful concept but needs adaptation
- 🔴 **Not a fit** — wrong scope or philosophy
- 🤖 **AI-automatable** — our agent can automate/pre-draft this

### Task Management & Execution

| Feature | Leantime | Super Productivity | Yar Fit | AI-Automatable? |
|---------|----------|-------------------|---------|-----------------|
| **Task CRUD** (create/read/update/delete) | ✅ Tickets domain (`app/Domain/Tickets/`) | ✅ NgRx store (`features/tasks/`) | 🟢 Core — YarObjects already model this | 🤖 Agent pre-drafts tasks from captures |
| **Kanban boards** | ✅ Multiple views (kanban, table, list, calendar, gantt) | ✅ (`features/boards/`) | 🟡 Visual planning useful but not core | — |
| **Subtasks / dependencies** | ✅ Unlimited subtasks + dependencies | ✅ Subtasks with parent links | 🟢 Graph links already support this | 🤖 Agent decomposes tasks into subtasks |
| **Tags / labels** | ✅ (`app/Domain/Tags/`) | ✅ (`features/tag/`) + virtual TODAY_TAG | 🟢 YarObject.type + properties | 🤖 Agent auto-tags from content |
| **Due dates / scheduling** | ✅ Via tickets | ✅ dueDay/dueWithTime mutual exclusivity | 🟡 Useful for anchoring routines | 🤖 Agent suggests dates based on patterns |
| **Sprint management** | ✅ (`app/Domain/Sprints/`) | ❌ | 🔴 Scrum is organizational overhead | — |
| **Milestone tracking** | ✅ Full milestone support | ❌ | 🔴 Too formal for personal companion | — |

### Time Tracking & Focus

| Feature | Leantime | Super Productivity | Yar Fit | AI-Automatable? |
|---------|----------|-------------------|---------|-----------------|
| **Time tracking** | ✅ (`app/Domain/Timesheets/`) | ✅ (`features/time-tracking/`) — per-task timers | 🟢 Critical for ND users to understand time perception | 🤖 Agent tracks via voice session timestamps |
| **Pomodoro timer** | ❌ | ✅ Built-in pomodoro with breaks | 🟢 Focus management is core ND need | — |
| **Idle detection** | ❌ | ✅ (`features/idle/`) — detects AFK, offers resume/discard | 🟢 Reduces manual tracking burden | — |
| **Take-a-break reminders** | ❌ | ✅ (`features/take-a-break/`) — configurable intervals | 🟢 Burnout prevention for hyperfocus | 🤖 Agent learns personal break patterns |
| **Focus mode** | ❌ | ✅ (`features/focus-mode/`) — distraction-free single task | 🟢 Critical for ADHD | — |
| **Tracking reminders** | ❌ | ✅ (`features/tracking-reminder/`) | 🟢 Gentle nudges without guilt | 🤖 Agent personalizes reminder timing |
| **Worklog / time reports** | ✅ Via timesheets | ✅ (`features/worklog/`) — daily/weekly summaries | 🟡 Useful but must avoid "surveillance" feel | 🤖 Agent generates reflective summaries |

### Planning & Strategy

| Feature | Leantime | Super Productivity | Yar Fit | AI-Automatable? |
|---------|----------|-------------------|---------|-----------------|
| **Day planner** | ✅ Dashboard "My Work" | ✅ (`features/planner/`) — drag-and-drop day planning | 🟢 Daily anchor planning is core to Yar | 🤖 Agent pre-drafts daily plan from pending tasks |
| **Goals & metrics** | ✅ (`app/Domain/Goalcanvas/`, `Strategy/`) | ❌ | 🟡 Long-term goals useful but must be gentle | 🤖 Agent tracks goal progress automatically |
| **Lean Canvas** | ✅ (`app/Domain/Leancanvas/`) | ❌ | 🔴 Business tool, not personal | — |
| **SWOT Analysis** | ✅ (`app/Domain/Swotcanvas/`) | ❌ | 🔴 Strategic planning tool | — |
| **Risk Analysis** | ✅ (`app/Domain/Riskscanvas/`) | ❌ | 🔴 Enterprise concern | — |
| **Retrospectives** | ✅ (`app/Domain/Retroscanvas/`) | ❌ | 🟡 Reflection is valuable but needs reframing as "end-of-day" | 🤖 Agent generates daily reflection prompts |
| **Calendar integration** | ✅ (`app/Domain/Calendar/`) | ✅ (`features/calendar-integration/`) — CalDAV/iCal | 🟡 Useful but secondary | — |

### Knowledge & Information Management

| Feature | Leantime | Super Productivity | Yar Fit | AI-Automatable? |
|---------|----------|-------------------|---------|-----------------|
| **Wiki / Docs** | ✅ (`app/Domain/Wiki/`) | ❌ | 🟡 Yar captures serve this role differently | — |
| **Notes** | ❌ | ✅ (`features/note/`) — markdown notes per project | 🟢 Capture-as-note is already core | — |
| **Idea boards** | ✅ (`app/Domain/Ideas/`) | ❌ | 🟡 Captures could surface as "idea board" view | 🤖 Agent clusters captures into idea themes |
| **Comments / discussions** | ✅ (`app/Domain/Comments/`) | ❌ | 🔴 Multi-user feature | — |
| **File storage** | ✅ S3 or local (`app/Domain/Files/`) | ❌ | 🟡 Yar stores captures locally | — |

### Sync & Integration

| Feature | Leantime | Super Productivity | Yar Fit | AI-Automatable? |
|---------|----------|-------------------|---------|-----------------|
| **Local-first storage** | ❌ Server-first | ✅ IndexedDB, local files | 🟢 Core principle | — |
| **Cross-device sync** | Via MySQL server | ✅ WebDAV, Dropbox, local file sync, SuperSync | 🟢 Must sync phone ↔ laptop | — |
| **Jira integration** | ❌ | ✅ (`features/issue/`) — bidirectional | 🔴 Enterprise tooling | — |
| **GitHub integration** | ❌ | ✅ (`features/issue/`) — import issues | 🟡 Useful for dev-oriented ND users | — |
| **CalDAV sync** | ❌ | ✅ Full CalDAV client | 🟡 Nice-to-have | — |
| **Anytype integration** | ❌ | ❌ | 🟢 **Unique to Yar** — already built | — |
| **Slack/Discord integration** | ✅ | ❌ | 🔴 Organizational tool | — |

### Accessibility & ND Support

| Feature | Leantime | Super Productivity | Yar Fit | AI-Automatable? |
|---------|----------|-------------------|---------|-----------------|
| **ADHD-specific UX** | ✅ Marketing claim, simplified UI | ✅ Focus mode, take-a-break, idle detection | 🟢 **Core differentiator** | — |
| **Dark mode** | ✅ | ✅ Material Design dark theme | 🟢 Default (WCAG AAA) | — |
| **i18n / translations** | ✅ 20+ languages via Crowdin | ✅ ngx-translate, 40+ languages | 🟢 Critical for global reach | — |
| **Guided onboarding** | ❌ | ✅ (`features/onboarding/`, `features/shepherd/`) | 🟢 Reduces cognitive load of setup | 🤖 Agent walks through setup conversationally |
| **Voice input** | ❌ | ❌ | 🟢 **Unique to Yar** — Gemma + HuBERT | — |
| **Emotion tracking** | ❌ | ❌ | 🟢 **Unique to Yar** — voice sentiment sensor | 🤖 Agent interprets emotional state |
| **CAP safety gate** | ❌ | ❌ | 🟢 **Unique to Yar** — no clinical claims | — |

### Administration & Security

| Feature | Leantime | Super Productivity | Yar Fit | AI-Automatable? |
|---------|----------|-------------------|---------|-----------------|
| **User roles / permissions** | ✅ Per-project | ❌ Single-user | 🔴 Yar is personal | — |
| **2FA** | ✅ (`app/Domain/TwoFA/`) | ❌ | 🔴 No server auth needed | — |
| **LDAP / OIDC** | ✅ | ❌ | 🔴 Enterprise | — |
| **Plugin system** | ✅ (`app/Plugins/`) — marketplace | ✅ (`packages/plugin-api/`) — Vite-based | 🟡 Future extensibility | — |
| **API** | ✅ JSON-RPC | ❌ (no external API) | 🟢 FastAPI already built | — |

---

## 2. Implementation Deep Dives

### Super Productivity: Key Code Patterns for Yar

#### A. State Management (NgRx)
SP uses NgRx (Redux for Angular) with entity adapters. Each feature has a self-contained `store/` directory:
```
features/tasks/store/
├── task.actions.ts        # Action definitions
├── task.effects.ts        # Side effects (async ops)
├── task.reducer.ts        # Pure state transitions
└── task.selectors.ts      # Memoized queries
```
**Yar parallel**: Yar uses FastAPI + Pydantic models. The equivalent pattern would be domain events + command handlers, which aligns with our knowledge graph approach.

#### B. Idle Detection (`features/idle/`)
Electron: uses `powerMonitor.getSystemIdleTime()` polled every 60s.
Web: uses `document.addEventListener('mousemove'|'keydown')` + `setTimeout`.
When idle > threshold: shows dialog offering to discard idle time or add it to current task.

**Yar adoption**: The phone app can detect idle via accelerometer/screen-off events. The desktop app via the same Electron API.

#### C. Focus Mode (`features/focus-mode/`)
Full-screen single-task view with large timer, task title, and progress bar. Blocks navigation to other tasks. Configurable session length.

**Yar adoption**: Implement as a "deep work" screen in Flutter with the active voice session timer.

#### D. Sync Architecture (`packages/sync-core/`)
Operation-log based CRDT-like sync:
- Each mutation generates an `OpLogEntry` with vector clock
- Conflict resolution via last-writer-wins on per-entity basis
- Providers: WebDAV, local file, Dropbox, SuperSync (proprietary)
- Package boundary enforcement via ESLint rules

**Yar adoption**: Critical for phone ↔ laptop sync. Anytype already handles sync for structured objects; we need a lighter sync for captures and CAP decisions.

#### E. Multi-Platform Build (`electron-builder.yaml`)
Single Angular app built once → deployed to:
- **Electron** (desktop): Windows NSIS/portable, macOS DMG, Linux AppImage/deb/snap/rpm
- **Capacitor** (mobile): Android APK via Gradle, iOS via Xcode
- **Web**: Service Worker PWA at app.super-productivity.com
- **Docker**: Nginx serving static files

**Build triggers**: `v*` tags trigger `build.yml` which:
1. Creates draft GitHub Release
2. Builds Linux + Snap on `ubuntu-latest`
3. Builds macOS DMG on `macos-latest` (with notarization)
4. Builds Windows exe on `windows-latest` (with SignPath code signing)
5. Separate workflows publish to Snap Store, Mac App Store, Google Play, Windows Store, AUR, Flathub, Docker Hub

### Leantime: Key Code Patterns

#### A. Domain Architecture
Clean hexagonal architecture with 57 domain modules:
```
app/Domain/Tickets/       # Tasks (core)
├── Controllers/          # HTTP handlers
├── Models/               # Data models
├── Repositories/         # Database access
├── Services/             # Business logic
├── Templates/            # Blade views
└── Hxcontrollers/        # HTMX partial endpoints
```

**Yar parallel**: Yar already uses a similar pattern with `api/routes_*.py`, `models/`, `core/`, `storage/`.

#### B. Canvas System
Multiple canvas types (Lean, SWOT, Business Model, Empathy Map, Retrospective) share a common `Canvas` base class. Each canvas is a domain module with templates.

**Yar adoption**: The "canvas" concept maps to Yar's capture → structured object pipeline. An AI agent could auto-generate canvas-like visualizations from clustered captures.

#### C. Plugin System
Plugins live in `app/Plugins/` with autoloaded service providers. Each plugin can register routes, views, middleware, and event listeners.

**Yar adoption**: A plugin system for sensor types (e.g., Apple Watch, OURA) is already part of our roadmap.

---

## 3. AI Agent Automation Candidates

| Task | Automation Approach | Priority |
|------|---------------------|----------|
| **Task creation from captures** | Agent parses voice/text captures → generates YarObjects with type, title, summary | P0 — already partially implemented via model router |
| **Daily plan generation** | Agent analyzes pending tasks, deadlines, energy patterns → drafts today's schedule | P0 — critical for ADHD users |
| **Task decomposition** | Agent breaks large tasks into subtasks with estimated durations | P1 — reduces "where do I start?" paralysis |
| **Auto-tagging / categorization** | Agent classifies captures into knowledge graph categories | P1 — already done by GemmaRouterStub |
| **Reflection / worklog summaries** | Agent generates end-of-day narrative from tracked time + completed tasks | P1 — replaces manual worklog writing |
| **Break timing optimization** | Agent learns personal focus/fatigue patterns → suggests break intervals | P2 — requires multi-day usage data |
| **Goal progress tracking** | Agent aggregates task completions → reports progress toward declared goals | P2 — requires goal definition UX |
| **Idea clustering** | Agent groups thematically related captures → surfaces as "idea board" | P2 — requires capture volume |
| **Calendar suggestion** | Agent proposes time blocks based on task estimates and free calendar slots | P3 — requires calendar integration |

---

## 4. Priority Features for Next Yar Phases

### Phase 1 (Current): Core Companion Loop
Already built/building:
- ✅ Capture pipeline (voice + text)
- ✅ CAP safety gate
- ✅ Anytype integration
- ✅ Emotion tracking architecture

### Phase 2: Focus & Time Awareness
Adopt from Super Productivity:
1. 🟢 **Focus mode** — single-task deep work screen
2. 🟢 **Idle detection** — pause/resume tracking automatically
3. 🟢 **Take-a-break reminders** — configurable, non-judgmental
4. 🟢 **Daily planner** — drag-drop or AI-generated day plan

### Phase 3: Sync & Multi-Device
Adopt from Super Productivity:
1. 🟢 **Local-first sync** — operation-log approach for captures
2. 🟢 **Zeroconf discovery** — already designed in previous session

### Phase 4: Knowledge & Reflection
Adopt from Leantime (reframed):
1. 🟡 **Retrospective → Daily Reflection** — AI-generated, not manual
2. 🟡 **Goals → Personal Compass** — gentle goal tracking without pressure
3. 🟡 **Idea Board → Insight Clusters** — AI-grouped capture themes

> **Status**: Active
> **Date**: 2026-06-14
> **Author**: @mohammadi
> **Audience**: engineers
> **Tags**: `yar`, `system-doc`, `architecture`

# Yar — System Doc

**Status**: MVP (firstVersion branch); Phase 7 refactor in progress (multi-app monorepo)
**Version**: v0.1.x → v0.2.0-rc1 (post-refactor)
**Repository**: github.com/cytognosis/Yar (name subject to change per Shahin's update)

## 1. Purpose and scope

Yar is the **local-first personal knowledge graph + cognitive offloading system** for Cytognosis. Users capture text/voice/web content; local Gemma 4 model routes into typed objects; CAP-Lite guards privacy & safety; SQLite stores by default with guarded external write to Anytype optional.

Multi-app surface (post-refactor):
- **Mobile** (Flutter): voice capture + offline-first
- **Desktop** (Tauri): full keyboard workflow
- **Extension** (MV3 + side panel): in-browser web capture
- **Web** (React + Vite): browser-first complement

Plus shared backend (FastAPI + SQLite).

**Out of scope**: clinical diagnosis (CAP-Lite blocks); cloud-hosted user data by default (local-first); interview/supervisor system (separate Cytognosis service uses CAP from cyto-skills).

## 2. Standards and protocols used

| Standard | Use |
|---|---|
| UV workspaces | Python monorepo (packages/*) |
| Melos | Flutter monorepo (apps/mobile) |
| pnpm workspaces | TS apps (apps/extension, web, desktop/web) |
| Cargo workspace | Rust (apps/desktop/src-tauri) |
| mise | Toolchain pinning |
| prek | Pre-commit monorepo-aware |
| FastAPI | Backend |
| SQLModel | ORM |
| flutter_gemma | Mobile model inference |
| LiteRT | Edge model runtime |
| MCP | Anytype adapter |
| CAP (HTTP/JSON binding) | Privacy/safety guard |
| LinkML | All schemas (via cytoskeleton submodule) |
| OpenTelemetry | Observability |
| Tailscale | Edge-Center connectivity (when interview system used) |
| NATS JetStream | A2A messaging (when interview system used) |

See [`02_standards_inventory.md`](../02_standards_inventory.md).

## 3. Architecture

### 3.1 Diagram (post-refactor)

```mermaid
flowchart TB
  subgraph YarRepo["Yar/ (multi-app monorepo)"]
    subgraph Backend["packages/ (UV workspace, Python)"]
      Core["yar-core (shared types)"]
      Backend2["yar-backend (FastAPI)"]
      CLI["yar-cli"]
      Tools["yar-tools"]
    end

    subgraph Apps["apps/"]
      Mobile["apps/mobile (Flutter)"]
      Desktop["apps/desktop (Tauri: Rust + web)"]
      Extension["apps/extension (MV3 + side panel)"]
      Web["apps/web (React + Vite)"]
    end

    subgraph External["external/ (three independent submodules)"]
      Skel["cytoskeleton @ v2.0.0-rc1"]
      CytoSk["cyto-skills @ v1.0.0-rc1 (skill runtime)"]
      CAPRef["cap @ v0.1.0 (CAP protocol)"]
    end
  end

  subgraph Local["User device"]
    Mobile -->|HTTP localhost| Backend2
    Desktop -->|HTTP localhost| Backend2
    Extension -->|HTTP localhost or message bridge| Backend2
    Web -->|HTTP| Backend2
    Backend2 -->|reads/writes| SQLite[(SQLite)]
    Backend2 -->|sidecar HTTP /directive| CAP[@cytognosis/cap server]
    Mobile -->|LiteRT inference| GemmaLocal[Gemma 4 E2B local]
  end

  subgraph Optional["Optional integrations"]
    Anytype["Anytype (via MCP)"]
    Center["Center Supervisor (Cytognosis hosted)"]
  end

  Backend2 -.->|via MCP, guarded by CAP| Anytype
  Backend2 -.->|A2A over Tailscale+NATS, guarded by CAP| Center

  Skel -->|schemas symlinked| Backend2
  CytoSk -->|provides CAP server| CAP
```

### 3.2 Components

**Backend (packages/)**:
- `yar-core/`: shared Pydantic types (YarObject, Capture, Link, Guard); used by all backend packages.
- `yar-backend/`: FastAPI app with 15 route files (capture, voice, objects, planning, communication, retrieval, export, annotations, schemas, anytype, cap, model, persona, health).
- `yar-cli/`: admin CLI.
- `yar-tools/`: data prep scripts.

**Apps (apps/)**:
- `mobile/`: Flutter with flutter_gemma + speech_to_text + http; targets iOS + Android.
- `desktop/`: Tauri v2 wrapping `apps/desktop/web/` (React).
- `extension/`: MV3 + side panel + content script; Chrome + Edge.
- `web/`: standalone web client (React + Vite + Tailwind + shadcn).

**External (three independent submodules)**:
- `external/cytoskeleton`: pinned v2.0.0-rc1; provides schemas + envs + templates.
- `external/cyto-skills`: pinned v1.0.0-rc1; provides skill runtime + MCP server (NO CAP).
- `external/cap`: pinned v0.1.0; provides CAP protocol implementation (sidecar HTTP/JSON).

**Storage**: SQLite default; Anytype optional external graph (via `packages/yar-anytype/`).

### 3.3 Data flow: capture

User input → Yar mobile (Flutter) → backend.capture POST → form Directive → CAP guard → SQLite write (if allowed) → response.

(See [00_cross_system_architecture.md §5 Scenario A](00_cross_system_architecture.md#scenario-a).)

### 3.4 Deployment topology

- **Single-user, local**: backend runs on user device; CAP sidecar same process group (cyto-skills @ HTTP/JSON).
- **Family/group, hosted**: backend on Cytognosis-managed VM; CAP sidecar same VM; storage on managed Postgres + Cloud Storage.
- **Future: assessment integration**: Center Supervisor runs in Cytognosis-hosted environment; Edge agent on user device; A2A over Tailscale+NATS connects them; CAP guards every message.

### 3.5 Assumptions

- Mobile: Gemma 4 E2B available via flutter_gemma (downloads on first run or bundled).
- Backend: SQLite default; PostgreSQL for hosted deployments.
- CAP: sidecar on localhost:7100 (HTTP) or :7101 (gRPC).
- Schemas: live in cytoskeleton; consumed via symlink.
- Per-branch config drives which app is active per development branch.

## 4. Implementation plan

### 4.1 Phase mapping

- Phase 7 (subplan `07_yar/`): full refactor.
- Phase 1: cytoskeleton has Yar schemas (yar/yar_object.yaml, capture.yaml, etc.).
- Phase 4: cyto-skills has CAP TS impl.

### 4.2 Current refactor work

See [`/Plans/design/07_yar/02_checklist.md`](../../../07_yar/02_checklist.md). Key:
1. Reorganize into multi-app monorepo (packages/, apps/, workspace manifests).
2. Add cytoskeleton + cyto-skills submodules.
3. Migrate 4 JSON Schemas to LinkML in cytoskeleton.
4. CAP TS port from Python ref (in cyto-skills/cap/).
5. Yar backend uses CAP server via HTTP/JSON.
6. Per-branch config for apps (mobile/desktop/extension/web).
7. Cytocast adoption (post-hoc copier copy --skip-if-exists).
8. Inherit `_shared/` workflows.

### 4.3 Out of scope (deferred)

- Center Supervisor integration (separate Cytognosis service; out of this session).
- Multi-tenant Yar SaaS deployment.
- Mobile app cloud sync (local-only v1).
- iOS App Store / Google Play distribution (Phase 10+).
- Genomic/neuroimaging data ingestion in Yar (cytos handles).

## 5. Current implementation

### 5.1 Repository

- URL: github.com/cytognosis/Yar
- Refactor sandbox: `/home/mohammadi/repos/cytognosis/refactor/Yar/`
- Branches: `main`, `firstVersion`, `refactor/v2-multi-app-monorepo`, `app/mobile`, `app/desktop`, `app/extension`, `app/web`

### 5.2 Features (current MVP)

- 15 FastAPI route files (capture, voice, objects, planning, communication, retrieval, export, annotations, schemas, anytype, cap, model, persona, health, mock_router)
- Coordinator pipeline (text/voice/url → object inference → CAP guard → storage)
- SQLite graph store (objects, links, captures, execution reports, schema metadata, voice turns, Anytype plans)
- CAP-Lite guard (blocks diagnosis/treatment/unsafe; raw_data_shared: false by default)
- Anytype MCP adapter (status, tool discovery, search, read, guarded writes)
- Daily gentle planning (anchors, timeboxes, carry-forward)
- Communication Translator Lite (incoming + outgoing with CAP-Lite post-checks)
- JSON + Markdown export
- LinkML-like schema loader + registry endpoint
- Flutter mobile app with voice capture + transcript editing + object review + Anytype write planning

After refactor:
- Multi-app monorepo (apps/mobile/desktop/extension/web)
- LinkML schemas (via cytoskeleton)
- CAP TS sidecar (via cyto-skills @ HTTP/JSON)
- Per-branch config for app-specific envs/skills

### 5.3 Interfaces

#### Backend HTTP API

```bash
# Capture
$ curl -X POST http://localhost:8000/capture \
  -H "Content-Type: application/json" \
  -d '{"content":"Idea: cytoskeleton needs schema sub-versioning","type":"Idea"}'

# Response (allowed)
{ "object_id": "obj_abc123", "status": "stored", "links": [] }

# Diagnosis attempt (denied by CAP-Lite)
$ curl -X POST http://localhost:8000/capture \
  -d '{"content":"You have anxiety","type":"Note","mode":"diagnostic_claim"}'

# Response
{
  "status": "refused",
  "refusal": {
    "refusal_type": "non_diagnostic_boundary_crossed",
    "explanation": "CAP-Lite blocks diagnostic claims.",
    "retry_hint": "Rephrase as observation: 'I'm noticing anxiety.'"
  }
}

# Daily plan
$ curl http://localhost:8000/planning/today

# Retrieval
$ curl "http://localhost:8000/retrieval?q=cytoskeleton"

# Export
$ curl http://localhost:8000/export/markdown > my-yar.md
```

#### Mobile (Flutter)

Tab-based UI: Capture, Inbox, Plan, Profile. Voice mic on Capture tab. Native speech-to-text → Gemma routing → object review → confirm to commit.

#### Extension (browser)

Side panel; capture button on toolbar; clip page; right-click context menu options. Communicates with backend via HTTP (localhost) or message bridge.

#### Desktop (Tauri)

Full keyboard-driven UI; system tray icon; global hotkey for quick capture; file watcher integration.

### 5.4 Tests

```bash
# Python packages
uv run pytest packages/

# Flutter
cd apps/mobile && flutter test

# TS/JS
pnpm test

# Rust (Tauri)
cd apps/desktop/src-tauri && cargo test

# E2E
scripts/run_dev.sh  # starts backend + CAP sidecar; runs smoke
```

### 5.5 Configuration

```yaml
# .cytognosis-config.yaml (root)
profile: yar-backend
cytoskeleton:
  ref: v2.0.0-rc1
  env: agentic
cyto_skills:
  ref: v1.0.0-rc1
cap:
  ref: v1.0.0-rc1
  policy: cap-lite
schemas:
  consume: [core/cytos.yaml, domains/yar/*]
```

```yaml
# .cytognosis-config-branch.yaml on app/mobile branch
extends: .cytognosis-config.yaml
profile: yar-mobile
cytoskeleton:
  env: app-phone
  components_extra: [dart/services/flutter-gemma, dart/services/speech-to-text]
templates: [app-phone]
```

## 6. Future / missing / suggestions

### 6.1 Known gaps

- Center Supervisor integration (interview system) — separate service.
- Real-time multi-device sync (CRDT via Iroh) — deferred.
- iOS App Store / Google Play distribution.
- Performance tuning for large graphs (>100k objects).
- Archiving + GDPR retention policies.

### 6.2 Suggestions

- Add Iroh CRDT layer for optional offline-first multi-device sync.
- Support multiple LLM backends (Gemma 4 + Phi-3 + Llama 3.x for fallback).
- Audit log export for HIPAA-affected users (Tier 1).
- Plugin system for custom object types beyond the 10 core + 8 optional.

### 6.3 Open RFCs

- Yar name rename (Shahin's update notes rename possible).
- Multi-tenant Yar SaaS architecture.

## 7. Cross-references

- [Cross-system architecture](00_cross_system_architecture.md)
- [CAP system doc](04_cap.md)
- [Cyto-skills system doc](03_cyto_skills.md)
- [Phase 7 subplan](../../../07_yar/)
- [Standards inventory](../02_standards_inventory.md)
- [Decision log §D9](../../../09_decision_log.md)

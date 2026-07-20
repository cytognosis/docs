> **Status**: Active
> **Date**: 2026-06-14
> **Author**: @mohammadi
> **Audience**: engineers
> **Tags**: `yar`, `refactor`, `plan`

# 07 — Yar Refactor — Plan & Reasoning

## 1. Current state

### Yar repo (firstVersion branch)
- Monolithic FastAPI backend (Python 3.12+) in `src/yar/` (15 route files, coordinator/router/services/storage modules).
- Separate Flutter mobile app in `mobile/` (Dart 3.4, Flutter 3.22, flutter_gemma 0.13.6).
- 4 JSON Schemas in `schemas/`: capture, guard_decision, linkml_anytype_mapping, yar_object.
- Existing `CAP/` directory with v0.1 production-candidate research package (gRPC + HTTP/JSON bindings, conformance + hardening, integration code).
- No copier/cytocast lineage (greenfield wrt cytocast).
- No desktop or extension apps yet.

### CAP context (separate product, NOT inside cyto-skills)

CAP is a standalone protocol. For Phase I, the canonical implementation stays at:
- `~/Documents/Cytognosis/Infra and design/CAP/cytognosis_cap_v01_production_candidate/` — primary Python implementation (gRPC + HTTP/JSON; conformance 28/28; hardening 33/33).
- `https://github.com/cytognosis/Yar/tree/main/CAP` — Yar-side integration shims (older version, simpler).

Phase I work for CAP:
- Compare/consolidate with related protocols (A2A — already used; discovery; etc.) from `/curations/tools/`.
- Produce final docs (technical + ADHD-friendly + agent prompt) at `/refactor/phases/docs/CAP/`.

Yar consumes CAP as an independent submodule/dependency — NOT via cyto-skills.

### Standards / tools used in Yar + CAP

Per `09_cross_cutting_standards/02_standards_inventory.md`. Key:
- MCP (Anytype adapter; cyto-skills tools).
- A2A (Edge-Center communication; CAP messages transit over A2A).
- LangGraph (Center Supervisor orchestration).
- NATS JetStream (async messaging).
- Tailscale (mesh networking with mTLS).
- Iroh CRDT (optional offline-first state sync).
- LiteRT (edge inference, Gemma 4 E2B quantized).
- OPA (policy evaluation via CAP).
- OpenTelemetry (observability).
- DSSE + in-toto (artifact signing via CAP).
- W3C PROV (provenance via CAP).
- LinkML (schemas via cytoskeleton).

## 2. CAP — keep canonical Python implementation; consolidate with curated protocols

Per Shahin's clarification: CAP is the canonical communication protocol exactly as implemented in `/Infra/CAP/cytognosis_cap_v01_production_candidate/`. We do NOT rewrite it for Phase I. We DO:

1. **Compare/consolidate** with curated protocols from `/curations/tools/`:
   - A2A (Agent-to-Agent Protocol) — already used by CAP for Edge-Center messaging.
   - Discovery protocols — how agents find each other.
   - Tailscale + NATS — transport.
   - Iroh CRDT — state sync.
   - OPA — policy.
   - MCP — tool invocation.

2. **Produce final docs** for CAP (Phase I deliverable):
   - Technical full doc.
   - ADHD-friendly version with diagrams + GitHub Alerts + 101 sections.
   - Dedicated agent prompt with links to technical docs.

3. **Yar imports CAP** as an independent submodule pinned to a release tag.

CAP runs as a sidecar (HTTP/JSON binding) alongside the Yar backend. Yar's FastAPI routes call `http://localhost:7100/directive` (or similar) for guard evaluation.

The CAP Python ref impl in `/Infra/CAP/` remains canonical. Yar/CAP/ contents merge into `/Infra/CAP/` (or vice versa, per consolidation in Task 2 Phase I) — one canonical CAP location going forward.

A potential TypeScript or Rust re-implementation is deferred to Phase 7+ (separate concern).

## 3. Target structure — Yar multi-app monorepo

```
Yar/
├── mise.toml                            # Python + Node + Rust + Flutter toolchain pins
├── .cytognosis-config.yaml              # root config: profile=yar-backend default
├── pyproject.toml                       # UV workspace root
├── uv.lock
├── .copier-answers.yml                  # cytocast registration (Phase 3+)
├── pnpm-workspace.yaml                  # for any TS/JS
├── package.json
├── packages/                            # UV Python workspace members
│   ├── yar-core/                        # shared types, schemas, base utilities
│   │   ├── pyproject.toml
│   │   └── src/yar_core/
│   ├── yar-backend/                     # FastAPI app
│   │   ├── pyproject.toml
│   │   └── src/yar_backend/
│   ├── yar-cli/
│   ├── yar-tools/
│   └── yar-anytype/                     # Anytype submodule with dedicated functions (NEW)
│       ├── pyproject.toml
│       └── src/yar_anytype/
│           ├── client.py                # Anytype MCP client
│           ├── push.py                  # write objects/relations to Anytype
│           ├── pull.py                  # read from Anytype
│           ├── schema_bridge.py         # LinkML schemas ↔ Anytype types
│           └── tests/
├── apps/                                # per-app dirs
│   ├── mobile/                          # Flutter (Melos workspace if multi-Dart-pkg)
│   │   ├── pubspec.yaml
│   │   └── lib/
│   ├── desktop/                         # Tauri (Rust + web)
│   │   ├── src-tauri/
│   │   └── web/
│   ├── extension/                       # MV3 + side panel
│   │   ├── manifest.json
│   │   └── src/
│   └── web/                             # standalone web client (optional)
├── external/                            # three INDEPENDENT submodules
│   ├── cytoskeleton/                    # submodule @ v2.0.0-rc1 (schemas, templates, envs)
│   ├── cyto-skills/                     # submodule @ v1.0.0-rc1 (skill runtime; MCP server)
│   └── cap/                             # submodule @ v0.1.0 (CAP protocol)
├── shared/                              # cross-app config; schemas symlinked from external/cytoskeleton/schemas
├── docs/
├── tests/
└── .github/workflows/                   # inherited from cytocast _shared/ (Phase 3+)
```

**Key change from prior plan**: `external/cyto-skills/` and `external/cap/` are **independent** submodules. CAP is NOT a subdirectory of cyto-skills.

## 4. Multi-agent architecture in Yar

Per `/Infra/CAP/cytognosis_multi_agent_architecture_report.md`:

### 4.1 Two-agent system

- **Edge Interviewer Agent**: local on user device (mobile/desktop/extension). Gemma 4 E2B via LiteRT (quantized). Propose-only authority.
- **Center Supervisor Agent**: hosted Cytognosis service. LangGraph orchestrator. Approve/revise/interrupt authority.

### 4.2 Communication stack

- **A2A protocol** for handshake and discovery.
- **NATS JetStream** for ordered messaging (topics: `directives`, `decisions`, `observations`).
- **Tailscale** for zero-trust mTLS connectivity.
- **Iroh CRDT** for optional offline-first state sync.

### 4.3 CAP integration

Every Edge-Center interaction passes through CAP:
- Edge forms Directive.
- Edge-side CAP Guard evaluates (CAP-Lite: blocks diagnosis/treatment/unsafe).
- Edge sends Directive to Center via A2A (CAP primitives serialized over A2A messages).
- Center-side CAP Guard re-evaluates (CAP-Med: stricter clinical rules).
- Center returns GuardDecision.
- Edge Executor acts only if allowed.

Audit trail: hash-chain on both sides; cross-referenced via EvidenceRef hashes.

### 4.4 Yar's role in this architecture

Yar is the user-facing surface (Edge):
- Mobile/desktop/extension/web apps run the Edge agent.
- Backend FastAPI hosts Edge agent runtime + storage.
- Center Supervisor is a **separate service** (Cytognosis-controlled; not in Yar repo; not in this subplan).
- Yar uses CAP for edge-side guard evaluation via local CAP sidecar (`http://localhost:7100/directive`).
- Yar uses cyto-skills for skill catalog + MCP server (e.g., the Anytype MCP adapter).

## 5. Yar multi-app monorepo details

### 5.1 Per-branch config

Branches (one per active app + integration branches):
- `main` — backbone, all packages
- `app/mobile` — mobile-focused; `.cytognosis-config-branch.yaml` sets profile=yar-mobile, env=app-phone
- `app/desktop` — desktop-focused
- `app/extension` — extension-focused
- `app/web` — web-focused
- `refactor/v2-multi-app-monorepo` — this refactor

Each app/* branch's `.cytognosis-config-branch.yaml` controls cytoskeleton env, skills to install, schemas to consume, templates to base on.

### 5.2 Schema migration to LinkML

Yar's 4 JSON Schemas → `cytoskeleton/schemas/domains/yar/`:
- yar_object.yaml
- capture.yaml
- guard_decision.yaml
- linkml_anytype_mapping.yaml

Codegen produces Pydantic in `cytoskeleton/schemas/codegen/pydantic/yar/`; Yar imports.

For Phase I (the 24-hour deadline), schema migration is **minimal**: just copy the JSON Schemas into `cytoskeleton/assets/schemas/yar/` for placement (full LinkML conversion deferred to Phase 7).

### 5.3 Templates migration

Current phone template in `Yar/mobile/`, current desktop template (to be created) in `Yar/apps/desktop/`. These move INTO `cytoskeleton/assets/templates/app-phone/` and `cytoskeleton/assets/templates/app-desktop/` (Phase 7 full migration). Phase I sets up the destination structure but doesn't fully move.

### 5.4 Anytype submodule

`packages/yar-anytype/` — dedicated Python package for Anytype integration:
- `client.py`: thin wrapper over Anytype MCP adapter.
- `push.py`: write objects + relations to Anytype, respecting CAP-guarded approval.
- `pull.py`: read from Anytype, return as YarObject types.
- `schema_bridge.py`: LinkML schemas ↔ Anytype types mapping.
- All interactions with Anytype MCP routed here.

## 6. Phase I scope (24-hour Gemma Hackathon)

Phase I is a SUBSET of full Phase 7:

| Task | Phase I (now) | Phase 7 (later) |
|---|---|---|
| Yar repo reorg into multi-app | Minimal: scaffold packages/, apps/ skeleton | Full UV workspace + Melos + cargo + pnpm wiring |
| Add cytoskeleton + cyto-skills + cap submodules | Setup external/ dirs; clone | Full submodule wiring with release tags |
| Migrate Yar schemas to cytoskeleton | Copy JSON Schemas into cytoskeleton/assets/schemas/yar/ | Convert to LinkML + Pydantic codegen |
| Move phone/desktop templates to cytoskeleton | Document target locations | Full move + Claude Design refresh |
| CAP integration | Update Yar/CAP/ docs; document HTTP sidecar pattern | Optional TS port; submodule pinning |
| Anytype submodule | Create `packages/yar-anytype/` skeleton | Full push/pull/schema_bridge implementation |

## 7. Phase I deliverables (Yar/CAP track)

Per Shahin's Task 2 instructions, Phase I produces:

1. **Consolidated cytognosis skills** (Task 2.1): Merged from `/Infra/05_skills_revised/` + `/refactor/cytoagent/skills/cytognosis/`; placed in canonical location; symlinked for Claude + Antigravity access.

2. **Minimal cytoskeleton reorg** (Task 2.2): `assets/` directory holds `envs/`, `schemas/`, `templates/` sub-trees. Yar JSON Schemas copied to `assets/schemas/yar/`.

3. **CAP final docs** at `/refactor/phases/docs/CAP/` (Task 2.3):
   - Technical multi-section doc.
   - ADHD-friendly version with diagrams, GitHub Alerts, 101 sections.
   - Dedicated prompt for agent execution with links to docs.

4. **Yar research docs** at `/refactor/phases/docs/Yar/research/` (Task 2.4):
   - Tone, audience, features, identity.
   - Ecosystem fit.
   - Impact summary (for Gemma Hackathon README).

5. **Yar implementation docs** at `/refactor/phases/docs/Yar/implementation/` (Task 2.5):
   - Lean-time + super-productivity scoping (v1; v2 in Phase II).
   - 3 variants: technical, easy-read, agent execution plan.
   - Phone/desktop template move plan.
   - Schema migration plan.
   - CAP integration details.
   - Anytype submodule design.

6. **Phase I master doc** at `/refactor/phases/docs/phase1.md` (Task 2.6): comprehensive doc referencing all the above; provides full context to Antigravity for executing the plan.

## 8. What we are NOT doing in Phase I

- NOT rewriting CAP (Python ref impl stays canonical).
- NOT publishing anything (Phase 10).
- NOT fully implementing the Center Supervisor (separate Cytognosis service).
- NOT live multi-org policy federation.
- NOT performance benchmarks for CAP guard latency (target < 50ms p95; measure when scaled).

## 9. Verification

See `04_verification.md`. Critical:
- Yar reorg into packages/+apps/ without breaking existing functionality.
- CAP docs (3 variants) authored at `/refactor/phases/docs/CAP/`.
- Yar research + implementation docs at `/refactor/phases/docs/Yar/`.
- Phase1.md master doc at `/refactor/phases/docs/phase1.md`.
- Cytoskeleton `assets/` reorg minimal-breaking.
- Cytognosis skills consolidated + symlinked.

## 10. Handoff

After Phase I:
- Antigravity receives the phase1.md master doc + all referenced artifacts.
- Antigravity executes: cytoskeleton minimal reorg, Yar package reorganization, CAP doc integration, Anytype submodule scaffold.
- Output: Updated Yar ready for Gemma Hackathon submission.
- Subsequent phases (full cyto-skills rewrite, complete schema migration, full template move) happen AFTER hand-off.

> **Status**: Active
> **Date**: 2026-06-14
> **Author**: @mohammadi
> **Audience**: engineers, stakeholders
> **Tags**: `cytonome`, `architecture`, `cross-system`

# Cytognosis Cross-System Architecture

**Last reviewed**: 2026-05-17
**Status**: post-refactor target (subplans 01-08 implement)

## 1. The eight systems

```mermaid
flowchart TB
  subgraph "Brand layer"
    Branding["branding<br/>(Design System v10)"]
    ClaudeDesign["Claude Design"]
  end

  subgraph "Content & template layer"
    Cytoskeleton["cytoskeleton<br/>(envs + schemas + templates + skills)"]
    Cytocast["cytocast<br/>(template engine + dev skills)"]
  end

  subgraph "Runtime layer"
    CytoSkills["cyto-skills (JS/TS)<br/>(MCP-tools + classifier + judge + synthesizer)"]
  end

  subgraph "Protocol layer (separate)"
    CAP["CAP (Python canonical; Yar consumes as sidecar)<br/>(Authority Protocol for multi-agent comm)"]
  end

  subgraph "Application layer"
    Cytos["cytos<br/>(foundation kernel)"]
    Yar["Yar<br/>(personal KG; mobile/desktop/extension/web)"]
    Neuro["neuro-* (future)"]
  end

  subgraph "Infrastructure & docs"
    Infra["infrastructure<br/>(GCP, HIPAA, container framework, data strategy)"]
    Website["website<br/>(cytognosis.org)"]
    Plans["Plans (this repo)<br/>(canonical refactor plans)"]
  end

  ClaudeDesign <-->|bidirectional sync via DESIGN.md| Branding
  Branding -->|PyPI: cytognosis-branding| Cytoskeleton
  Branding -->|PyPI / submodule| Website
  Cytoskeleton -->|submodule + components.yml ref| Cytocast
  Cytocast -->|copier copy + post-create hooks| Cytos
  Cytocast -->|copier copy| Yar
  Cytocast -->|copier copy| Neuro
  Cytoskeleton -->|submodule| Cytos
  Cytoskeleton -->|submodule| Yar
  CytoSkills -->|MCP server, runtime| Yar
  CAP -.runtime guard.- Yar
  Cytos -.consumes schemas.- Cytoskeleton
  Yar -.imports CAP via HTTP/JSON.- CAP
  Infra -.->|hosts| Yar
  Infra -.->|hosts| Cytos
  Infra -.->|hosts| Website
```

## 2. Per-system role

| System | Role | Language | Repo |
|---|---|---|---|
| **branding** | Cytognosis Design System (tokens, profiles, components, assets, voice). Paired with Claude Design. | Markdown + CSS + SVG + PyPI Python pkg | `cytognosis/branding` |
| **cytoskeleton** | Upstream content hub: envs + schemas + templates + skills (universal, operational, meta, personas, template-usage). | Python (mostly), YAML, multi-language components | `cytognosis/cytoskeleton` |
| **cytocast** | Package-template engine (Copier-based) + dev skills + `_shared/` payload. | Python + YAML + workflows | `cytognosis/cytocast` |
| **cyto-skills** | JS/TS runtime: MCP-aligned skill registry + classifier + judge + synthesizer + IDE deploy. Does **NOT** include CAP. | TypeScript / Node.js | `cytognosis/cyto-skills` (renamed from cytoagent) |
| **CAP** | Cytognosis Authority Protocol — standalone multi-layer communication protocol. Separate product from cyto-skills. | Python (canonical); optional TS port deferred | `/Infra/CAP/cytognosis_cap_v01_production_candidate/` (canonical); future `cytognosis/cap` repo (TBD) |
| **cytos** | Foundation biomedical kernel: ingests 50+ sources, builds KG (10.7M nodes × 118.5M edges), provides query services + modeling stubs. | Python 3.13+ | `cytognosis/cytos` |
| **Yar** | Personal knowledge graph capture system; multi-app (mobile/desktop/extension/web). | Python (backend), Dart (mobile), Rust (Tauri desktop), TS (extension, web) | `cytognosis/Yar` |
| **infrastructure** | GCP, HIPAA SOPs, container framework, data strategy. | Markdown + Python (stack_manager.py) + YAML | `cytognosis/infrastructure` |
| **website** | cytognosis.org — FastAPI + vanilla HTML/JS. | Python + HTML/CSS/JS | `cytognosis/website` |
| **neuro-*** (future) | Domain-specific packages built from cytocast template, consuming cytos + cytoskeleton. | Python + R | `cytognosis/neuro-*` |

## 3. Dependency graph (version-pinned)

```
cytognosis-branding v2.x      ← Source of truth: branding repo
   ├─→ cytoskeleton (PyPI dep)
   └─→ website (PyPI dep + submodule for static assets)

cytoskeleton v2.x             ← Upstream submodule for everyone
   ├─→ cytocast (modules/cytoskeleton submodule + components.yml ref)
   ├─→ cytos (external/cytoskeleton submodule)
   ├─→ Yar (external/cytoskeleton submodule)
   └─→ neuro-* (external/cytoskeleton submodule)

cytocast v2.x                 ← Template engine + dev skills
   └─→ (used at scaffold time + via copier update)

cyto-skills v1.x              ← JS/TS skill runtime (no CAP)
   ├─→ Yar (external/cyto-skills submodule)
   └─→ (deployed alongside any agent that needs MCP)

CAP v0.1.x                    ← Standalone protocol, separate from cyto-skills
   ├─→ Yar (external/cap submodule; HTTP/JSON sidecar at localhost:7100)
   ├─→ Center Supervisor agents (separate Cytognosis service)
   └─→ Any agent that needs explicit authority semantics
```

**No circular dependencies**. Cytocast no longer depends on cyto-skills (the legacy cytoagent dep is broken; see Phase 3). CAP and cyto-skills are INDEPENDENT peer dependencies for Yar — neither contains the other.

## 4. Skill phase model (canonical)

```mermaid
flowchart LR
  A["Brand-phase<br/>branding/skills/"] --> Stage1[Design / brand identity]
  B["Template-phase<br/>cytoskeleton/skills/"] --> Stage2[Scaffold time<br/>(universal, operational, meta, personas, template-usage)]
  C["Dev-phase<br/>cytocast/skills/"] --> Stage3[Coding time<br/>(languages, backend, frontend, ai-ml, devops, engineering, documents, research, science)]
  D["Runtime-phase<br/>cyto-skills/skills/"] --> Stage4[Deployed agent invocation<br/>(MCP tools + CAP guard)]
```

Skills are vendored into generated packages at scaffold time (cytocast invokes install_skills, which pulls from cytoskeleton + cytocast skills/ dirs + cyto-skills MCP server registry).

## 5. Data flow scenarios

### Scenario A: User capture → CAP-guarded storage in Yar

```mermaid
sequenceDiagram
  participant User
  participant YarMobile as Yar mobile (Flutter)
  participant YarBackend as Yar backend (FastAPI)
  participant CAP as CAP TS sidecar
  participant Storage as SQLite

  User->>YarMobile: voice/text input
  YarMobile->>YarBackend: POST /capture {content, type}
  YarBackend->>YarBackend: form Directive (capture content, propose-only)
  YarBackend->>CAP: POST /directive
  CAP->>CAP: evaluate (CAP-Lite: check diagnosis/treatment/unsafe)
  alt allowed
    CAP-->>YarBackend: GuardDecision: allow
    YarBackend->>Storage: insert object
    Storage-->>YarBackend: ID
    YarBackend-->>YarMobile: 200 {object_id, status: stored}
    YarMobile-->>User: confirmation
  else denied
    CAP-->>YarBackend: GuardDecision: deny, reason: non_diagnostic_boundary_crossed
    YarBackend-->>YarMobile: 200 {status: refused, refusal: {...}}
    YarMobile-->>User: gentle explanation
  end
```

### Scenario B: New cytos KG snapshot generation

```mermaid
sequenceDiagram
  participant Dev
  participant Cytos
  participant DVC
  participant GCS as gs://cytognosis-data/
  participant Cytoskeleton

  Dev->>Cytos: nox -s kg_build
  Cytos->>Cytoskeleton: load schemas (via external/cytoskeleton/schemas)
  Cytos->>Cytos: run 9 DVC stages
  Cytos->>DVC: dvc repro
  DVC->>GCS: push intermediates + KG snapshot
  GCS-->>DVC: confirms
  DVC-->>Cytos: complete
  Cytos->>Cytos: publish RO-Crate to cytos/kg/snapshots/v2026.06/
```

### Scenario C: Cytoskeleton v2 release propagates to cytos

```mermaid
sequenceDiagram
  participant Maintainer
  participant Cytoskeleton
  participant Cytocast
  participant Cytos

  Maintainer->>Cytoskeleton: merge PR, tag v2.1.0
  Cytoskeleton->>Cytoskeleton: notify-downstream.yml fires
  Cytoskeleton->>Cytocast: repository_dispatch event
  Cytocast->>Cytocast: template-update.yml; bump components.yml ref to v2.1.0
  Cytocast->>Cytocast: open PR
  Cytocast->>Cytos: repository_dispatch (cytocast tagged new version)
  Cytos->>Cytos: template-update.yml; copier update --vcs-ref v2.1.0
  Cytos->>Cytos: open PR
  Maintainer->>Cytos: review + merge PR
```

### Scenario D: New package generated from cytocast

```mermaid
sequenceDiagram
  participant Dev
  participant Cytocast
  participant Cytoskeleton
  participant NewPkg as new package dir

  Dev->>Cytocast: uvx copier copy github:cytognosis/cytocast --vcs-ref v2.0.0
  Cytocast->>Cytocast: prompt for profile, name, etc.
  Cytocast->>NewPkg: render template files
  Cytocast->>NewPkg: hook 1: setup_scaffold (create dirs)
  Cytocast->>Cytoskeleton: hook 2: install_cytoskeleton (clone at v2.0.0 to external/)
  Cytoskeleton->>NewPkg: components installed
  Cytocast->>NewPkg: hook 3: install_skills (read .cytognosis-config.yaml, vendor from cytocast/skills + cytoskeleton/skills)
  Cytocast->>NewPkg: hook 4: copy_and_merge_locks
  Cytocast->>NewPkg: hook 5: setup_env (uv sync)
  Cytocast->>NewPkg: hook 6: setup_dvc (if bio profile)
  Cytocast-->>Dev: package ready
```

## 6. Deployment topology

```mermaid
flowchart TB
  subgraph "Developer machines"
    DevLap["Developer laptop<br/>(uv + mise + git)"]
  end

  subgraph "GitHub"
    Branding[branding]
    Skel[cytoskeleton]
    CC[cytocast]
    CS[cyto-skills]
    Cytos[cytos]
    YarRepo[Yar]
    Infra[infrastructure]
    Website[website]
  end

  subgraph "GCP — cytognosis-infrastructure"
    AR["Artifact Registry<br/>(cytognosis-pypi)"]
    GHWIF["Workload Identity<br/>Federation"]
    Hosts["Cloud Run<br/>(website)"]
  end

  subgraph "GCP — cytognosis-data"
    DataBucket["gs://cytognosis-data/<br/>(Tier 2)"]
  end

  subgraph "GCP — cytognosis-phi-prod"
    PHIBucket["gs://cytognosis-phi-prod/<br/>(Tier 1, CMEK, VPC SC)"]
    Vertex["Vertex AI<br/>(Confidential)"]
    Audit["Audit Logs<br/>(7yr retention)"]
  end

  subgraph "User devices"
    Mobile["Yar mobile (iOS/Android)<br/>Edge: Gemma 4 E2B via LiteRT"]
    Desktop["Yar desktop (Tauri)"]
    Ext["Yar extension (Chrome/Edge)"]
  end

  subgraph "Cytognosis hosted"
    Center["Center Supervisor<br/>(LangGraph + Gemma 4)"]
    CAPSrv["CAP server<br/>(cyto-skills/cap HTTP/JSON)"]
  end

  DevLap -->|gh push| Branding
  DevLap -->|gh push| Skel
  DevLap -->|...| CC
  GHWIF -.-> AR
  Branding -->|publish on tag| AR
  Skel -->|publish on tag| AR
  CC -->|publish on tag| AR
  CS -->|publish on tag| AR
  Mobile -.->|A2A over NATS+Tailscale| Center
  Mobile -.->|local SQLite| Mobile
  Desktop -.->|same| Center
  Ext -.->|same| Center
  Center -.->|policy eval| CAPSrv
  Center -->|writes audit| Audit
  Cytos -.->|DVC pull/push| DataBucket
  Website -.->|deployed to| Hosts
  Hosts -.->|reads tokens from| AR
```

## 7. Cross-cutting concerns

### 7.1 Branch naming + CI

Per master plan §6.1: `feat/`, `refactor/v<N>-`, `fix/`, `chore/`, `auto/`, `release/`. Every Cytognosis repo has the `_shared/.github/workflows/` payload (inherited from cytocast) for: ci, publish-dev, publish-release, release-please, security, deps, template-update, notify-downstream.

### 7.2 Versioning

SemVer everywhere. release-please + Conventional Commits drives version bumps.

### 7.3 Auth

GH Actions ↔ GCP via Workload Identity Federation. No long-lived service account keys checked into repos.

### 7.4 HIPAA

Tier 1 data (PHI) → cytognosis-phi-prod bucket, CMEK, VPC SC, audit logs 7yr. See `infrastructure/docs/data-strategy/compliance/` for the 9 SOPs.

### 7.5 Observability

OpenTelemetry from every Cytognosis package. Spans cross CAP boundaries (annotated by CAP audit layer). Cloud Monitoring alerts on: bucket anomaly, IAM change, geo deviation.

### 7.6 Docs

cytognosis-doc skill drives all structured technical writing. New templates added per `09_cross_cutting_standards/03_doc_skill_enhancements.md`.

## 8. Why this architecture?

### Why eight systems?

We considered a monorepo. Rejected because:
- Different velocities (branding evolves with design; cytos with KG; Yar with apps).
- Different access controls (branding mostly public; phi-* repos may stay private).
- Different toolchains (Python + TS + Dart + Rust).
- Different release cadences.

We considered fewer systems (e.g., merge cytoskeleton + cytocast). Rejected because:
- Cytoskeleton is content (declarative); cytocast is engine (imperative). Conflating them loses the separation of concerns.

### Why four-phase skill model?

To prevent "where does this skill live?" debates. Every skill maps to one phase:
- Brand-phase: design system
- Template-phase: scaffold time
- Dev-phase: coding time
- Runtime-phase: deployed agent

### Why CAP as a separate layer?

CAP is transport- and language-agnostic. Embedding it in any one system would couple guard semantics to that system's lifecycle. Hosting CAP in cyto-skills/cap/ workspace package keeps it co-located with the runtime layer but separately versionable.

### Why JS/TS for cyto-skills (not Python)?

- MCP SDK and agent ecosystems are TS-first in 2026.
- Vercel AI SDK, LangChain.js, Cloudflare Workers Agents — TS ecosystem.
- Browser/extension/Tauri can run cyto-skills directly.
- Python adapter (`cytognosis-cap-py`) covers Python clients.

## 9. Risks + mitigations

| Risk | Likelihood | Mitigation |
|---|---|---|
| Branding/Claude Design drift | Medium | Weekly drift detection cron + PR-mediated sync |
| Cytoskeleton breaking change cascade | Medium | Pin downstream to release tags; auto-merge patch updates only after green CI |
| CAP performance | Low | Benchmark target < 50ms p95; revisit Rust if missed |
| HIPAA non-compliance | Medium | 9 operational SOPs + audit log review quarterly |
| Multi-language monorepo (Yar) coordination | Medium | mise + prek + workspace tooling |
| Vendor lock-in (GCP) | Low | Standards-based interfaces (PostgreSQL, S3-compatible) where possible |

## 10. References

- Master plan: `~/Documents/Cytognosis/Plans/design/00_master_plan.md`
- Decision log: `~/Documents/Cytognosis/Plans/design/09_decision_log.md`
- Standards inventory: `../02_standards_inventory.md`
- Per-system docs: `01_cytocast.md`, `02_cytos.md`, `03_cyto_skills.md`, `04_cap.md`, `05_yar.md`

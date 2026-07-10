# Toolchain + Operational Track — Cytognosis Foundation

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: leadership
> **Tags**: `strategy`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)

**Date:** 2026-06-03 · Built from cytomem corpus (10,006 artifacts / 27 sources) + direct file reads.
**Track pillar:** Toolchain (cytoskeleton, cytocast, cytoskills, cytomem) + Operational (infrastructure, branding, website, org, docs)
**Cross-track link:** Toolchain LinkML KG schemas directly support IGoR TA1 ontology asks.
Reading time: ~8 min. **If you only read one thing:** the toolchain architecture is substantially designed and partially built; the three critical gaps are compute orchestration (no `cytoinfra run`), the three parallel registry patterns needing unification, and branding repo not ready for public release.

---

## BLUF

The toolchain is well-architected but execution-incomplete. cytoskeleton has a sound asset registry and VFS; cytomem is live with 10,006 artifacts and semantic search partially operational; cytoskills holds 65 skills in a pnpm monorepo; cytocast is the Copier-based project scaffolder with strong dev standards baked in. The big gaps: compute orchestration does not exist yet, three parallel registry patterns need to converge, and the branding repo has critical pre-release blockers that are 18 months stale.

---

## 1. Toolchain Repos — Current State

### 1.1 cytoskeleton (Asset Registry and VFS)

**Role:** Universal asset registry. Every tracked artifact gets a unique `<package>/<type>/<name>@<version>` full ID with a manifest YAML, provenance chain, and storage backend reference.

**Implemented:**
- 7 asset types: Component, Environment, Docker, ExecutionEnvironment, Schema, Skill, StoreManifest — all backed by LinkML schema at `w3id.org/cytognosis/cytoskeleton/core`.
- Lifecycle stages: `draft → described → built → tested → published → archived`.
- Dual-scope index: Global `~/.cytognosis/index.yaml` and local `./.cytognosis-index.yaml`.
- 7 VFS backends: LocalVFS, GCSVFS, LocalGitVFS, GitHubVFS, S3VFS, HFHubDriver, ZenodoDriver. Every `put()` carries a `ProvenanceRecord`; `AssetStat` includes `swhid` (Software Heritage ID, ISO 18670:2025).
- RO-Crate 1.2 auto-generation from store manifests.
- DVC integration for dataset versioning (`.dvc/config` present; lockfiles currently polluting cytomem graph).

**Gaps:**
- No `Code`, `Model`, `Paper`, or `Dataset` asset types, despite the URI scheme (`cytognosis://`) supporting them. Cytos defines these separately; they are not unified with cytoskeleton.
- Three parallel registry patterns exist: cytoskeleton AssetCatalog, cytos DatasetRegistry, cytoinfra ContainerRegistry. Inconsistent manifest formats, no unified query interface.

**Canonical docs:** `docs/toolchain/cytoskeleton/platform-design.md` (moved from `cytoskeleton/design/platform_design_v2.md`, which now contains a redirect stub).

---

### 1.2 cytocast (Project Scaffolder)

**Role:** Copier-based project template that generates fully-configured Python projects embedding all Cytognosis dev standards.

**Implemented:**
- Templates for Django, FastAPI, bio-modeling, and ML profiles (`profiles/*.yaml`).
- Full dev standards stack: ruff (format + lint), mypy (type checking), nox (session automation: `lint_ci`, `lint_release`, `type_ci`, `test`, `security`, `init_project`), pre-commit hooks (format-check, linting-check, typing-check, test-check).
- Progressive quality enforcement: Sandbox (permissive, auto-fix) → Dev (imports + docstrings) → PR (strict, no auto-fix) → Release (strictest, naming + complexity).
- 16 license options covering permissive OSS (Apache-2.0, MIT, BSD), copyleft (GPL-3.0, LGPL-3.0), Creative Commons (CC BY, CC BY-SA, CC BY-NC, CC0), responsible AI (OpenRAIL-M/D/S), and proprietary. OpenRAIL is the default for ML model outputs.
- Trusted PyPI publishing via GitHub OIDC (no stored tokens).
- Bandit security rules via ruff (`S105`, `S608`, `S301`, `S602`).
- AI agent configuration scaffold under `.agents/` (config.yaml, skills/, workflows/, commands/, plugins/ for Claude/Gemini/Cursor/Windsurf).
- CI/CD workflows: deploy-docs, release (GH Actions).
- Cloud deployment docs covering Cloud Run and related GCP services.

**Canonical docs:** `docs/toolchain/cytocast/features/` (swe-standards, licensing, cicd-features, cloud-deployment, project-scaffolding, data-science-tooling, default-standards, etc.).

---

### 1.3 cytoskills (Skills Registry)

**Role:** TypeScript + Python hybrid pnpm monorepo. Packages and distributes AI agent skills across Claude, Gemini, Cursor, and Windsurf.

**Implemented:**
- 65 skills across 12 categories: cytognosis (8), science (5), engineering (6), ai-ml (4), meta (8), documents (6), research (4), operations (6), languages (8), frontend (8), infrastructure (1: cytoskeleton), community (1).
- Key science skills: bioinformatics, graph (ontology-tools), healthcare-ai, visualization, fhir.
- Ontology tooling: `packages/core/src/ontology.ts` provides ontology query helpers (cross-track support for IGoR schema needs).
- Tooling: biome (linter/formatter), vitest (tests).

**Gap:**
- Single infrastructure skill (cytoskeleton). No skills yet for cytocast, cytomem, or cytoinfra operations.

**Canonical docs:** `docs/toolchain/cytoskills/architecture.md`, `cytoskills-automation.md`, `branding-skill-spec.md`.

---

### 1.4 cytomem (Graph Memory and Index)

**Role:** Knowledge graph spine indexing all repos and Obsidian vault. Provides semantic recall, deduplication, and task tracking.

**Current status:**
- Live: 10,006 artifacts, 27 sources (repos + Obsidian + 7 Cowork projects + 6 curated archive sources).
- Semantic search operational but partially degraded: `task-65fec913` (in-progress) is fixing Graphiti vector embeddings for all artifacts.
- Open tasks from graph:
  - `task-784af3b7` (p1): cross-repo DEPENDS_ON / SUPERSEDES / MIGRATED_TO edges in Neo4j — not yet built.
  - `task-705bd369` (p2): Sigma.js KG visualizer in cytoexplorer.
  - `task-52a6abc4` (p3): evaluate InfraNodus Obsidian plugin.

**Graph-hygiene finding (from Stage 4 taxonomy):**
Semantic recall returns non-content noise from cytoskeleton: `.dvc/tmp/rwlock`, `.dvc/tmp/btime`, `.dvc/tmp/lock`, `.github/PULL_REQUEST_TEMPLATE.md`, `.coderabbit.yaml`. These dilute recall precision. **Recommendation (not yet done):** add `.dvc/tmp`, `.github`, and lockfile patterns to `exclude` in `cytomem/configs/repos.yaml` and re-ingest repos. This is a low-effort, high-value fix.

**Config files:**
- `cytomem/configs/repos.yaml` — 19 repos registered (12 active, 3 utility, 2 archived, 2 other). All toolchain and operational repos present. `cytodocs` marked archived (absorbed into cytomem). `cytoexplorer` marked archived.
- `cytomem/configs/tracks.yaml` — taxonomy frozen.

---

## 2. Operational Repos — Current State

### 2.1 infrastructure

**GCP architecture (documented, partially deployed):**

| Service | Deployment | URL |
|---|---|---|
| Website | Cloud Run (always-on) | cytognosis.org |
| Neo4j | Cytohost (on-demand) | kg.cytognosis.org |
| Wiki.js | Cytohost (on-demand) | docs.cytognosis.org |
| MLflow | Cytohost (on-demand) | mlflow.cytognosis.org |
| Jupyter | Notebook pool VM | notebook.cytognosis.org |
| Zoekt | Cytohost (on-demand) | code.cytognosis.org |

**Cytohost v2 spec:** e2-highmem-2 (2 vCPU, 16 GB RAM), Ubuntu 24.04 LTS x86_64, 200 GB data disk (persistent), idle-stop (30 min), IAP tunnel SSH, Cloud DNS `*.cytognosis.org`.

**Containers:** 8 containers (neo4j 5.18.1, surrealdb v2, mlflow 2.21.0, caddy, hedgedoc, grobid 0.8.1, cytognosis-compute 0.6.0, cytognosis-gpu 0.6.0). 4 stacks: core, research, data-services, neo4j-only.

**Phase 0 tasks (all marked incomplete):**
- P0-1: Delete research VM at 34.61.134.177
- P0-2: Migrate cytohost to e2-highmem-2 (x86)
- P0-3: Add Instance Schedule + idle-stop
- P0-4: Reserve static IP + Cloud DNS update
- P0-5: Deploy Wiki.js (replace HedgeDoc)
- P0-6: Create `cytognosis/docs` GitHub repo
- P0-7: Set up Wiki.js bidirectional GitHub sync

**DVC:** Configuration present. Strategy documented at `docs/infrastructure/dvc-strategy.md`. GCS remote `gs://cytognosis-data-hub/` is the data backbone.

**Data strategy:** SSSOM cross-ontology mapping and scholarly KG docs present in both `infrastructure/docs/data-strategy/` and `docs/infrastructure/data-strategy/` (duplicate pair, see Section 5).

**Recommended tool stack (design-complete, not yet deployed):**

| Category | Primary | Complement |
|---|---|---|
| Job Orchestration | Prefect (self-hosted) | — |
| Compute Backend | GCP Cloud Batch | Compute Engine (persistent) |
| Provenance | redun (as library) | — |
| Code Repos | Gitea + Zoekt | GitNexus MCP, Mani |
| Literature | Zotero + WebDAV | pyzotero for AI |
| Model Registry | MLflow | HF Hub Collections |
| Documentation | Wiki.js | Obsidian vault + GitHub docs repo |

---

### 2.2 branding

**Status:** Substantially incomplete. Last substantive update: 2025-01-15 (18 months ago, per `TODO.md` timestamp).

**What exists:** Brand guidelines (8 chapters: color, typography, logo, voice, motion, etc.), trademark doc, web HTML/CSS scaffold, templates README stubs.

**Critical pre-release blockers (unresolved):**
- Template directories `slides/`, `documents/`, `social/` are empty.
- Favicon and multi-resolution icon set missing.
- Logo variants (monochrome, reversed/white, horizontal/vertical, favicon) missing.
- Web fonts directory empty (no WOFF2/WOFF files).
- `guidelines/README.md` updated 2026-03-14; `guidelines/08_templates.md` and `guidelines/10_templates.md` are duplicates (different chapter numbering, same content area).

**Note on `branding/repos.yaml` alias:** `cytoplex` is registered with `aliases: [CAP]`. Per voice rules, use "Cytoplex" not "CAP" in all Cytognosis-branded output.

---

### 2.3 website

**Status:** Deployed on Cloud Run (always-on). `cytognosis.org` is live.

**What cytomem indexes:** The website repo is tracked as operational/active. No specific content-state docs surfaced in recalls beyond the deployment architecture. The `branding/web/html/index.html` and CSS files exist as brand reference but the production site is in the `website` repo.

---

### 2.4 org

**Status:** Active with `red_flags: ["contains historical docs, some unique, evaluate for consolidation"]` per `repos.yaml`.

**Key unique content:** `org/plans/research/biotools-schema-edam-research.md` (also at `docs/schemas/biotools-schema-edam-research.md` — duplicate pair).

---

### 2.5 docs

**Status:** Active, canonical engineering home. Organized as:
- `toolchain/` — cytoskeleton, cytocast, cytoskills, cytoexplorer
- `infrastructure/` — DNS/GCP, hosting/deployment, data-strategy, gcp-setup, audits
- `schemas/` — tagging-ontology, linkml-playbook (22 chapters), software-metadata/linkml-software-schema-fields, biotools-schema-edam-research

**Role per canonical-home rule:** `docs` repo is the single engineering canonical home. Both Obsidian and Wiki.js read/write the same repo. Agent pushes go to `drafts/` for human review.

---

## 3. LinkML KG Schemas and the IGoR Ontology Connection

The Cytognosis KG schema stack is directly relevant to IGoR TA1 data standardization asks. The connection:

**What we have:**
- `docs/schemas/linkml-playbook/` — 22-chapter end-to-end tutorial covering: Biolink model, UMLS/SNOMED CT, GA4GH (VRS, Phenopackets), SOSA/SSN (sensor/wearable), CELLxGENE (single-cell), HDMF/NWB (neural data), SSSOM cross-ontology mapping, BioCypher (Neo4j ingestion), structured extraction (OntoGPT, Instructor, scispaCy).
- `cytos/data/staged/biolink/biolink-model.yaml` — Biolink model staged.
- `cytos/schemas/bioschemas_profiles.yaml` — Bioschemas profiles.
- `cytos` KG: 10.7M nodes, 118.5M edges, 36 domain LinkML schemas (including clinical, disease, genomics, phenotype, measurement, person, population, scholarly, sensor).
- `docs/infrastructure/data-strategy/sssom-cross-ontology-mapping.md` — SSSOM workflow documented.
- `cytoskills/packages/core/src/ontology.ts` — ontology query helpers available to agents.

**IGoR link (one line):** The Cytognosis LinkML KG stack (36 domain schemas + Biolink + SSSOM cross-mapping + structured extraction playbook) provides the ontology grounding and data standardization layer that IGoR TA1 requires for harmonizing multi-modal psychiatric phenotype data.

---

## 4. Dev Standards and Openness Posture

**Dev standards (cytocast-enforced in all generated projects):**
- Python: `uv` for package management, `src/` layout, `pyproject.toml`-first.
- Linting: `ruff` (format + lint, Bandit security rules via ruff plugin).
- Type checking: `mypy` (full strictness at PR and release gates).
- Test sessions: `nox` (lint_ci, lint_release, type_ci, test, security, init_project).
- Conventional Commits (feat, fix, docs, refactor, test, chore, perf, ci).
- AI agent configs under `.agents/` scaffolded by default.

**Openness posture:**
- Code: Apache-2.0 default (patent grant, permissive).
- ML models: OpenRAIL-M default (open access with responsible-use behavioral restrictions).
- Datasets: OpenRAIL-D or CC BY 4.0 depending on project.
- Proprietary option available for PBC/commercial arm (Cytoplex/Yar).
- Branding: `TRADEMARK.md` present; trademark usage documented.

**Cytoskills is TypeScript-first** (pnpm monorepo, biome, vitest) — intentionally distinct from the Python ecosystem. Skills are distributed as `.skill` zip packages.

---

## 5. Top-3 Priorities

| Priority | What | Why Urgent |
|---|---|---|
| **P1 — Compute Orchestration** | Implement `cytoinfra run` with Prefect + Cloud Batch + redun provenance (Phase 1 tasks P1-1 through P1-8). Also complete Phase 0 cytohost migration (P0-1 through P0-7). | No workloads can be scheduled on GCP; two-VM waste is ongoing; wiki.js not deployed. Zero-execution state on a fully designed architecture. |
| **P2 — Graph Hygiene + Semantic Search** | Add `.dvc/tmp`, `.github`, lockfile excludes to `cytomem/configs/repos.yaml` and re-ingest. Complete `task-65fec913` (Graphiti embedding fix). Then build cross-repo DEPENDS_ON edges (`task-784af3b7`). | Degraded semantic recall affects all subagent work. Noise dilutes every cytomem query. |
| **P3 — Registry Convergence + Missing Asset Types** | Add Code, Model, Paper, Dataset asset types to cytoskeleton core schema. Define a unified registry interface over cytoskeleton AssetCatalog, cytos DatasetRegistry, cytoinfra ContainerRegistry. | 300+ external repos with no metadata, papers not tracked as assets, no model provenance chain. Blocks the data-to-model lifecycle. |

---

## 6. Gaps

| Gap | Current State | Impact |
|---|---|---|
| **No compute orchestration** | `cytoinfra` = container lifecycle only. No `run`, no pools, no job DAGs. | Cannot schedule any GCP workloads. |
| **Three registry patterns** | cytoskeleton, cytos, cytoinfra each have separate manifest formats. | No unified asset query. |
| **External repos unmanaged** | 300+ repos, 179 GB, 28 orgs, zero metadata. | Lost knowledge, no AI searchability. |
| **Branding repo stale** | Empty templates, missing logo variants, no fonts. Last update Jan 2025. | Cannot publish brand kit publicly. |
| **Semantic search degraded** | Graphiti embeddings partially broken; `.dvc/tmp` noise in index. | Recall precision reduced. |
| **Phase 0 infra tasks all open** | Cytohost not migrated, Wiki.js not deployed, DNS not finalized. | No persistent services running. |

---

## 7. Duplicate Docs Needing Canonical-Home Assignment

These pairs exist in two repos with identical content. Both are indexed by cytomem. **Do not edit either copy yet**; assign canonical home first.

| Document | Copy 1 (candidate canonical) | Copy 2 (supersede) |
|---|---|---|
| DNS and GCP Architecture | `docs/infrastructure/DNS_AND_GCP_ARCHITECTURE.md` | `infrastructure/docs/DNS_AND_GCP_ARCHITECTURE.md` |
| HOSTING_AND_DEPLOYMENT | `docs/infrastructure/HOSTING_AND_DEPLOYMENT.md` | `infrastructure/docs/HOSTING_AND_DEPLOYMENT.md` |
| gcp-setup | `docs/infrastructure/gcp-setup.md` | `infrastructure/docs/gcp-setup.md` |
| deployment_walkthrough | `docs/infrastructure/self_hosted/deployment_walkthrough.md` | `infrastructure/docs/self_hosted/deployment_walkthrough.md` |
| sssom-cross-ontology-mapping | `docs/infrastructure/data-strategy/sssom-cross-ontology-mapping.md` | `infrastructure/docs/data-strategy/sssom-cross-ontology-mapping.md` |
| scholarly-knowledge-graph | `docs/infrastructure/data-strategy/scholarly-knowledge-graph.md` | `infrastructure/docs/data-strategy/scholarly-knowledge-graph.md` |
| biotools-schema-edam-research | `docs/schemas/biotools-schema-edam-research.md` | `org/plans/research/biotools-schema-edam-research.md` |
| branding guidelines templates | `branding/guidelines/08_templates.md` | `branding/guidelines/10_templates.md` |

**Recommendation:** `docs` repo is canonical for all infrastructure and schema docs per the Stage 4 rule. `infrastructure` repo copies become superseded references. `org` copy of biotools research becomes superseded. Branding duplicate needs content comparison before merge.

---

## 8. Cross-Track Links

- **IGoR (Funding track):** LinkML schemas + SSSOM + structured extraction playbook = IGoR TA1 ontology compliance layer.
- **Cytoverse (Cytoverse track):** cytos KG (10.7M nodes, 118.5M edges) lives at the intersection of Cytoverse science and Toolchain infrastructure. The 36 domain schemas are the Cytoverse ontological backbone.
- **Cytonome (Cytonome track):** Cytoplex uses cytoskeleton's VFS and asset registry. `Yar/src/yar/data/schemas/linkml_anytype_mapping.schema.json` links Yar's data model to the LinkML standard.
- **Cytoscope (Cytoscope track):** SOSA/SSN sensor schema (`docs/schemas/linkml-playbook/08_sosa_ssn_to_linkml.md`) and `cytos/schemas/domains/sensor/` are the schema foundation for Cytoscope's wearable data.

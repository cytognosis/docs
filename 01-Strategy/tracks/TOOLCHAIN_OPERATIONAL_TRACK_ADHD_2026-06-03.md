# Toolchain + Operational Track — ADHD Version

**Date:** 2026-06-03
Reading time: ~3 min. **If you only read one thing:** the toolchain is designed but not running. Three things block progress: no compute orchestration, noisy graph memory, and fragmented registries.

---

## BLUF

The toolchain architecture is solid and substantially documented. Execution is the gap: cytoinfra has no job scheduler, cytomem's semantic search has noise reducing precision, and three registry patterns need to converge. Fix these in order. Branding is 18 months stale and not urgent relative to infra.

---

## Done (no action needed)

- [x] cytomem live: 10,006 artifacts, 27 sources, semantic recall operational
- [x] cytoskeleton asset registry built: 7 asset types, 7 VFS backends, RO-Crate, provenance
- [x] cytoskills: 65 skills, 12 categories, deployed across Claude/Gemini/Cursor/Windsurf
- [x] cytocast: Copier scaffolder with ruff, mypy, nox, pre-commit, 16 license options, OpenRAIL defaults
- [x] LinkML KG playbook: 22-chapter end-to-end doc in `docs/schemas/linkml-playbook/`
- [x] cytos KG: 10.7M nodes, 118.5M edges, 36 domain schemas
- [x] Infrastructure architecture designed: Prefect + Cloud Batch + Cytohost v2 spec finalized
- [x] Tool evaluations complete: code repos (Gitea+Zoekt), literature (Zotero), model registry (MLflow+HF Hub), docs (Wiki.js)
- [x] Taxonomy frozen, canonical-home rule established

---

## Top 3 Priorities (do now, no outreach needed)

| # | What | Effort | Why |
|---|---|---|---|
| **1** | Fix cytomem graph hygiene: add `.dvc/tmp`, `.github`, lockfiles to `exclude` in `cytomem/configs/repos.yaml`, re-ingest. Then unblock `task-65fec913` (Graphiti embeddings). | Low | Noisy recalls degrade every subagent task now. |
| **2** | Execute Phase 0 infra tasks (P0-1 through P0-7): delete old research VM, migrate cytohost to e2-highmem-2 x86, idle-stop, static IP, deploy Wiki.js, create docs repo. | Medium | All 7 tasks are open. No persistent services running. |
| **3** | Add Code/Model/Paper/Dataset asset types to cytoskeleton core schema; design unified registry interface over the three parallel registries (cytoskeleton, cytos, cytoinfra). | Medium | 300+ repos and papers are invisible to the asset layer. |

---

## Repo Status Snapshot

| Repo | Track | Status | Key gap |
|---|---|---|---|
| **cytomem** | Toolchain | Active, degraded | Embedding fix in-progress; noise in index |
| **cytoskeleton** | Toolchain | Active, partial | Missing Code/Model/Paper/Dataset types |
| **cytocast** | Toolchain | Active, solid | No gaps — standards fully codified |
| **cytoskills** | Toolchain | Active, solid | 1 infra skill; needs cytocast/cytomem skills |
| **infrastructure** | Operational | Designed, undeployed | Phase 0 tasks all open |
| **branding** | Operational | Stale (Jan 2025) | Empty templates, missing logos/fonts |
| **website** | Operational | Live | Cloud Run, no current gaps flagged |
| **org** | Operational | Active, evaluate | Historical docs, some unique — consolidate |
| **docs** | Operational | Active, canonical | Engineering canonical home per rule |

---

## Schema-to-IGoR Link (one sentence)

The Cytognosis LinkML stack (36 domain schemas + Biolink + SSSOM + structured-extraction playbook in `docs/schemas/linkml-playbook/`) is the ontology-grounding layer that IGoR TA1 needs to harmonize multi-modal psychiatric phenotype data.

---

## Dev Standards (quick reference)

| Tool | Role |
|---|---|
| `uv` | Package management, virtual envs |
| `ruff` | Format + lint + Bandit security rules |
| `mypy` | Type checking (strict at PR + release) |
| `nox` | Session runner (lint, type, test, security, init) |
| pre-commit | Runs format + lint on every commit |
| Conventional Commits | feat/fix/docs/refactor/test/chore |
| Apache-2.0 | Default code license |
| OpenRAIL-M | Default ML model license |
| OpenRAIL-D | Default data license |

---

## Graph Hygiene (fix this week)

**File:** `cytomem/configs/repos.yaml`
**What to add:** `exclude` patterns for `.dvc/tmp/**`, `.github/**`, `*.lock`, `rwlock`, `btime` in the cytoskeleton repo entry.
**Effect:** Removes `.dvc/tmp/rwlock`, `.dvc/tmp/btime`, `.dvc/tmp/lock`, `.github/PULL_REQUEST_TEMPLATE.md`, `.coderabbit.yaml` from semantic recall results. Improves recall precision across all tracks.

---

## Duplicate Docs (paths for canonical-home assignment — do not edit yet)

| Document | Canonical home | Supersede |
|---|---|---|
| DNS_AND_GCP_ARCHITECTURE | `docs/infrastructure/` | `infrastructure/docs/` |
| HOSTING_AND_DEPLOYMENT | `docs/infrastructure/` | `infrastructure/docs/` |
| gcp-setup | `docs/infrastructure/` | `infrastructure/docs/` |
| deployment_walkthrough | `docs/infrastructure/self_hosted/` | `infrastructure/docs/self_hosted/` |
| sssom-cross-ontology-mapping | `docs/infrastructure/data-strategy/` | `infrastructure/docs/data-strategy/` |
| scholarly-knowledge-graph | `docs/infrastructure/data-strategy/` | `infrastructure/docs/data-strategy/` |
| biotools-schema-edam-research | `docs/schemas/` | `org/plans/research/` |
| branding/guidelines/templates | `08_templates.md` | `10_templates.md` (compare first) |

---

## Cross-Track Links (quick)

- **IGoR:** LinkML schemas = IGoR TA1 ontology layer.
- **Cytoverse:** cytos KG lives at the Cytoverse/Toolchain boundary.
- **Cytonome:** Cytoplex uses cytoskeleton VFS; Yar has `linkml_anytype_mapping.schema.json`.
- **Cytoscope:** SOSA/SSN schema chapter 08 + `cytos/schemas/domains/sensor/` = wearable data standard.

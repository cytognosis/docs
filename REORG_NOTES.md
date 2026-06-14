# Reorg Notes: Universal Taxonomy 2026-06-12

Branch: `reorg/universal-taxonomy-2026-06-12`
Date started: 2026-06-12. Phase 3a completed: 2026-06-14.
Blueprint: v8 (BLUEPRINT_v8_universal_taxonomy.md in outputs).
Executor: Claude Sonnet/Fable.

## Phase 3a Status: COMPLETE (2026-06-14)

All 6 commits applied to branch. Tree matches v8 final taxonomy. Ready to merge when Shahin reviews.

**Commit log:**
1. `6aa0c90` — Remove duplicate root documentation-standards.md; clean empty placeholder dirs
2. `9adf895` — Add REORG_NOTES.md with full old→new mapping, dedups, and inbox list
3. `c35e416` — Remove agent-work validation artifacts and _archive (git holds history; v8: no lifecycle folders)
4. `c34429c` — Renumber layers for v8 taxonomy (02-Products→03, 03-Eng→04, 04-Res→05, 05-Ops→06, 06-Design→07)
5. `da1c5ae` — Create 02-Funding layer from 01-Strategy/funding and fundraising
6. `c66c2fe` — v8 structural corrections (YC submissions → 02-Funding/YC/submissions/; sensing schema → cytos/sensing-schema/; remove cytoplex/v1-baseline snapshot)

**Final file count:** ~516 tracked files (down from 539: 3 dedups removed + 20 cytoplex v1-baseline snapshot files removed)

## Final top-level tree

```
00-Inbox/        — unsorted intake (5 files parked)
01-Strategy/     — master plan, platform strategy, data strategy
02-Funding/      — grants pipeline, YC/submissions, funder research
03-Products/     — Cytoverse/, Cytonome/ (portfolios; Yar is the product)
04-Engineering/  — cytos/, cytoplex/, yar/, toolchain/, infrastructure/, decisions/, standards/
05-Research/     — neuroverse/
06-Operations/   — org/, data-strategy/compliance+policies, audits, communications
07-Design/       — design system, brand, design research
_templates/      — canonical template set (see TEMPLATE_ASSESSMENT.md for full set)
```

## Key v8 corrections applied

- Yar submission bundle moved from `03-Products/Cytonome/Yar/submission/` → `02-Funding/YC/submissions/`
- Sensing schema core (sensor-architecture, sensor-taxonomy, interop-standards, data-formats, semantic-alignment, unified-sensor-report, human-body-systems, datatypes/) moved from `yar/sensors/` → `04-Engineering/cytos/sensing-schema/`; adapter/implementation docs remain in `04-Engineering/yar/sensors/`
- `04-Engineering/cytoplex/v1-baseline/` removed (snapshot folder; spec/ is canonical; git holds history)
- `_archive/` removed; `07-Agent-Work/` removed (ephemeral agent artifacts not tracked in docs repo)

---

## Remaining Phase 3 work (docs repo is DONE; other sources follow)

See MASTER_DRIVE_PLAN.md "Resume here" section. Order:
1. Obsidian (Phase 3b): de-mirror ~1,000 files; frontmatter normalization; remove symlinks
2. Claude Projects (Phase 3c): create 9 hybrid projects; migrate per master_catalog.tsv
3. gdrive (Phase 3d): digest unique items; write ops/legal index pointers
4. Monday (Phase 3e): reconnect connector; build entity+relationship boards
5. Cross-link pass (Phase 3f)
6. Phase 4: verification

---

Total files in repo after initial reorg pass: 536 (down from 539 due to 3 dedups removed)

---

## Pre-Flight State

- Tree was clean (no uncommitted changes) before starting.
- Started from `main`, branch `reorg/universal-taxonomy-2026-06-12` created immediately.

---

## Move Summary by Source Area

### strategy/ -> 01-Strategy/

| Old | New |
|-----|-----|
| `strategy/master-metaplan.md` | `01-Strategy/master-metaplan.md` |
| `strategy/platform-design.md` | `01-Strategy/platform-design.md` |
| `strategy/platform-tutorial.md` | `01-Strategy/platform-tutorial.md` |
| `strategy/data-strategy/` | `01-Strategy/data-strategy/` |
| `strategy/fundraising/` | `01-Strategy/fundraising/` |
| `strategy/tool-landscape/` | (empty dir, removed) |
| `cytoverse/cytos/grants/` | `01-Strategy/funding/` |
| `cytoverse/ai-ml-dimensional-biotyping-landscape-2026.md` | `01-Strategy/` |

### cytonome/ -> 02-Products/ + 03-Engineering/ + 07-Agent-Work/

**Product definition (02-Products/Cytonome/Yar/)**
- `cytonome/yar/cytonome-master-reference.md`
- `cytonome/yar/yar-master-features-requirements.md`
- `cytonome/yar/feature-comparison.md`
- `cytonome/yar/yar-feature-prioritization.csv`
- `cytonome/yar/submission/` (all 7 files)
- `cytonome/yar/plans/` (feature comparison refs)
- `cytonome/yar/mvp/` (12 files)

**Product definition (02-Products/Cytonome/Cytoplex/)**
- `cytonome/yar/cytoplex/overview.md`
- `cytonome/yar/cytoplex/README.md`
- `cytonome/yar/cytoplex/spec/` (17 files)

**Implementation (03-Engineering/yar/)**
- `cytonome/yar/integrations/` -> `03-Engineering/yar/integrations/`
- `cytonome/yar/reports/` -> `03-Engineering/yar/reports/`
- `cytonome/yar/research/` -> `03-Engineering/yar/research/`
- `cytonome/yar/sensors/` -> `03-Engineering/yar/sensors/`

**Implementation (03-Engineering/cytoplex/)**
- `cytonome/yar/cytoplex/benchmarks/`
- `cytonome/yar/cytoplex/compliance/`
- `cytonome/yar/cytoplex/interop/`
- `cytonome/yar/cytoplex/quality/`
- `cytonome/yar/cytoplex/research/`
- `cytonome/yar/cytoplex/security/`
- `cytonome/yar/cytoplex/v1-baseline/`

**07-Agent-Work/cytoskills/**
- `cytonome/skills/implementation_plan.md`
- `cytonome/skills/walkthrough.md`

### cytoverse/cytos/design/ -> 02-Products/Cytoverse/ + 03-Engineering/cytos/

**Product framing (02-Products/Cytoverse/)**
- `platform-design.md`, `platform-tutorial.md`, `tool-roles-explained.md`, `integration-details.md`

**Engineering (03-Engineering/cytos/)**
- `data-lifecycle-architecture.md`, `e2e-platform-validation.md`, `experiment-management-architecture.md`, `validation-report.md`, `vfs-containers-databases-analysis.md`

### cytoverse/cytos/ -> 03-Engineering/cytos/

- `cytoverse/cytos/architecture.md` and related architecture/data-stores/genomic files
- `cytoverse/cytos/adrs/` -> `03-Engineering/cytos/adrs/`
- `cytoverse/cytos/databases/` -> `03-Engineering/cytos/databases/`
- `cytoverse/cytos/data-lake/` -> `03-Engineering/cytos/data-lake/`
- `cytoverse/cytos/genomekg/` -> `03-Engineering/cytos/genomekg/`
- `cytoverse/cytos/schemas/` -> `03-Engineering/cytos/schemas-ontologies/` (merged with schemas/ below)
- `cytoverse/cytos/validation/` (143 files) -> `07-Agent-Work/validation/`
- `cytoverse/cytos/historical/` -> `_archive/cytos-historical/`

### infrastructure/ -> 03-Engineering/ + 04-Research/ + 05-Operations/

**03-Engineering/infrastructure/**
- `infrastructure/ci-cd/` (5 files)
- `infrastructure/compute/`
- `infrastructure/registries/`
- `infrastructure/reproducibility/`
- `infrastructure/tools/`
- `infrastructure/self_hosted/` + `infrastructure/self-hosted/` MERGED -> `03-Engineering/infrastructure/self-hosted/`
- `infrastructure/data-strategy/schemas/` -> `03-Engineering/infrastructure/data-strategy/schemas/`
- `infrastructure/data-strategy/` (remaining files: catalog.yaml, data-hub.md, etc.) -> `03-Engineering/infrastructure/data-strategy/`
- Root engineering files: `architecture.md`, `DNS_AND_GCP_ARCHITECTURE.md`, `HOSTING_AND_DEPLOYMENT.md`, `MASTER_INFRASTRUCTURE.md`, `container-framework.md`, `container-services.md`, `dvc-strategy.md`, `gcp-setup.md`, `service-accounts.md`, `code-search-infrastructure.md`

**04-Research/neuroverse/**
- `infrastructure/programs/neuroverse/` -> `04-Research/neuroverse/`

**05-Operations/**
- `infrastructure/audits/` -> `05-Operations/audits/`
- `infrastructure/communications/` -> `05-Operations/communications/`
- `infrastructure/policy-deployment/` -> `05-Operations/policy-deployment/`
- `infrastructure/COMMUNICATIONS_AND_WORKSPACE.md` -> `05-Operations/`
- `infrastructure/data-strategy/policies/` -> `05-Operations/data-strategy/policies/`
- `infrastructure/data-strategy/compliance/` -> `05-Operations/data-strategy/compliance/`

**_templates/**
- `infrastructure/data-strategy/templates/` -> `_templates/`

### toolchain/ -> 03-Engineering/

- `toolchain/cytoexplorer/` -> `03-Engineering/cytolens/cytoexplorer/`
- `toolchain/cytocast/` -> `03-Engineering/toolchain/cytocast/`
- `toolchain/cytoskeleton/` -> `03-Engineering/toolchain/cytoskeleton/`
- `toolchain/cytoskills/` -> `03-Engineering/toolchain/cytoskills/`

### decisions/ + standards/ -> 03-Engineering/

- `decisions/` -> `03-Engineering/decisions/`
- `standards/` -> `03-Engineering/standards/`

### design/ -> 06-Design/ + 07-Agent-Work/prompts/

- `design/adhd-neurodiversity-design-research.md` -> `06-Design/`
- `design/branding-design-system-spec.md` -> `06-Design/`
- `design/claude-design-sync-protocol.md` -> `06-Design/`
- `design/prompts/` (12 files) -> `07-Agent-Work/prompts/`

### org/ -> 05-Operations/org/

- `org/compliance/` -> `05-Operations/org/compliance/`
- `org/naming/` -> `05-Operations/org/naming/`

### schemas/ -> 03-Engineering/cytos/schemas-ontologies/

- `schemas/linkml-playbook/` (25 files)
- `schemas/resource-schemas/` (8 YAML files)
- `schemas/software-metadata/` (7 files)
- `schemas/biotools-schema-edam-research.md`
- `schemas/sssom-tooling.md`
- `schemas/tagging-ontology.md`

### Vault copies -> _archive/vault-copies/

All 10 `*-vault.md` files moved here:
- `cytonome/yar/architecture-vault.md`
- `cytonome/yar/cytonome-master-reference-vault.md`
- `cytonome/yar/cytoplex/README-vault.md` (renamed to `README-vault.md`)
- `cytonome/yar/product-implementation-vault.md`
- `cytonome/yar/sensors/README-vault.md` (renamed to `sensors-README-vault.md` to avoid collision)
- `cytonome/yar/sensors/sensor-architecture-vault.md`
- `cytonome/yar/sensors/universal-sensor-schema-vault.md`
- `cytonome/yar/yar-master-features-requirements-vault.md`
- `cytoverse/cytos/architecture-vault.md` (renamed to `cytos-architecture-vault.md`)
- `cytoverse/cytos/genomic-standards-vault.md`

---

## Deduplications Performed (git rm)

3 files removed as confirmed exact duplicates:

1. `infrastructure/gcp-infrastructure-audit-2026-05-25.md` (REMOVED)
   - Canonical copy: `05-Operations/audits/gcp-infrastructure-audit-2026-05-25.md`

2. `cytoverse/cytos/validation/monorepo_best_practices_cicd.md` (REMOVED from 07-Agent-Work/validation after the bulk move)
   - Canonical copy: `03-Engineering/infrastructure/ci-cd/monorepo_best_practices_cicd.md`

3. `documentation-standards.md` (root-level REMOVED)
   - Canonical copy: `03-Engineering/standards/documentation-standards.md`

---

## Files Parked in 00-Inbox (Manual Review Required)

5 files with genuinely ambiguous placement between product-definition and engineering implementation:

| File | Reason for ambiguity |
|------|---------------------|
| `00-Inbox/architecture-index.md` | (from `cytonome/yar/`) Index doc; unclear if product or engineering home |
| `00-Inbox/product-implementation.md` | (from `cytonome/yar/`) Spans product and engineering concern |
| `00-Inbox/refactor-overview.md` | (from `cytonome/yar/`) Refactor scope; could be 02-Products or 03-Engineering |
| `00-Inbox/yar_revision_plan.md` | (from `cytonome/yar/`) Plan doc; product roadmap or engineering task |
| `00-Inbox/analysis/infra-scaling-analysis.md` | (from `infrastructure/analysis/`) Analysis report; 03-Engineering or 05-Operations unclear |

---

## Commits (6 structural + 1 cleanup)

```
6aa0c90 reorg(docs): remove duplicate root documentation-standards.md; clean empty placeholder dirs
eb7d084 reorg(docs): schemas -> 03-Engineering/cytos/schemas-ontologies
f40216e reorg(docs): decisions + standards -> 03-Engineering; design -> 06-Design; prompts -> 07-Agent-Work; org -> 05-Operations
b289fad reorg(docs): cytoverse/cytos + infrastructure -> 03-Engineering; infrastructure ops -> 05-Operations; neuroverse -> 04-Research; dedups; toolchain -> 03-Engineering
627ebda reorg(docs): cytonome product-level + cytoverse/design -> 02-Products; vault copies -> _archive
c0fb5b5 reorg(docs): strategy -> 01-Strategy
```

---

## Final Top-Level Tree

```
docs/
├── 00-Inbox/              <- 5 files for manual review
├── 01-Strategy/           <- strategy, data-strategy, fundraising, funding (grants)
├── 02-Products/           <- product definition: Cytonome/Yar, Cytonome/Cytoplex, Cytoverse
├── 03-Engineering/        <- implementation: cytos, yar, cytoplex, cytolens, toolchain, infrastructure, decisions, standards
├── 04-Research/           <- neuroverse
├── 05-Operations/         <- org, audits, communications, policy-deployment, data-strategy (compliance/policies)
├── 06-Design/             <- design system, branding, ADHD research
├── 07-Agent-Work/         <- cytoskills, prompts, validation (143 session artifacts)
├── _archive/              <- vault-copies (10 files), cytos-historical
├── _templates/            <- data management plan, data use agreement templates
├── README.md
└── REORG_NOTES.md
```

---

## Notes

- `03-Engineering/cytolens/` contains a `cytoexplorer/` subfolder (from `toolchain/cytoexplorer/`); the subfolder name is retained for git history continuity.
- `infrastructure/hardware/` was empty; removed without git mv.
- `strategy/tool-landscape/` was empty; removed without git mv.
- `cytoverse/cytos/validation/` (143 files) treated as agent execution session artifacts -> `07-Agent-Work/validation/`. Contains screenshots, PNGs, WEBPs, and session reports from prior agent runs.
- The `_archive/cytos-historical/historical/` double-nesting is preserved from the source (`cytoverse/cytos/historical/historical/`).

---

## Phase 3 — All Phases Complete (2026-06-14)

| Phase | Status | Description |
|-------|--------|-------------|
| 3a: Docs repo renumber | ✅ DONE | 6 structural commits; v8 taxonomy applied; 536 files |
| 3b: Obsidian cleanup | ✅ DONE | De-mirrored 61 symlinks; v8 renumber; 234 files in vault |
| 3c: Claude Projects CLAUDE.md | ✅ DONE | 8 hybrid projects wired with CLAUDE.md routing files |
| 3c Stage 1: Gather Yar/Cytoplex/CAP docs | ✅ DONE | 23 new files + 36 headers; research/ EVAL-topic.md convention |
| 3d: Google Drive index | ✅ DONE | `06-Operations/gdrive-ops-legal-index.md` + `02-Funding/gdrive-funding-index.md` |
| 3e: Monday.com boards | 🔒 BLOCKED | Monday connector disconnected; no action taken |
| 3f: Cross-link pass | ✅ DONE | `sensor-architecture.md`, `biotools-schema-edam-research.md`, `master-metaplan.md` |

### Phase 4 Verification Results

- **Headers**: All modified files in this branch have `> **Status**` metadata headers. ✅
- **Legacy stubs**: `plans/yar-feature-comparison-adhd-ref.md` and `plans/yar-feature-comparison-ref.md` removed (broken `file://` paths; canonical content in `research/`). ✅
- **Branch status**: Clean working tree. ✅
- **Cross-links verified**: All three `See Also` sections reference valid relative paths. ✅

### Final Commit Log (Phase 3c-4)

```
63e78cc feat(docs): Phase 3f — add cross-links to key hub docs
acaf36b feat(docs): Phase 3d — add Google Drive ops/legal/funding index pointers
bd4a6d4 chore(docs): add cytognosis-doc metadata headers to Yar/Cytoplex docs
ee3eb58 feat(docs): Phase 3c Stage 1 — gather Yar/Cytoplex/CAP docs
```

### Remaining Work (not blocking merge)

- **Broader metadata normalization**: ~480 docs outside the Cytonome section still lack cytognosis-doc headers; run a follow-up batch header pass on `04-Engineering/`, `05-Research/`, `06-Operations/`.
- **Phase 3e (Monday)**: reconnect connector; build entity+relationship boards.
- **00-Inbox review**: 5 ambiguous files still parked for manual placement.


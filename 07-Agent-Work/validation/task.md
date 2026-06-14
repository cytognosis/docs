# Infrastructure Documentation Overhaul — Task Tracker

## Phase A — New Docs (15 files) ✅ COMPLETE

### Compliance
- `[x]` `docs/data-strategy/compliance/HIPAA-STATUS.md` — master 45 CFR control tracker
- `[x]` `docs/data-strategy/compliance/nih-gds-requirements.md` — NIH GDS + NIST 800-171

### Neuroverse Program
- `[x]` `docs/programs/neuroverse/README.md` — program overview
- `[x]` `docs/programs/neuroverse/datasets-cohorts.md` — cohorts, modalities, access routes
- `[x]` `docs/programs/neuroverse/infrastructure.md` — data env, SAE architecture
- `[x]` `docs/programs/neuroverse/action-plan.md` — IRB, access, onboarding, roadmap

### Reproducibility
- `[x]` `docs/reproducibility/README.md` — master strategy entry
- `[x]` `docs/reproducibility/schema-strategy.md`
- `[x]` `docs/reproducibility/artifact-vfs-swhid.md`
- `[x]` `docs/reproducibility/envs-containers.md`
- `[x]` `docs/reproducibility/provenance-lineage.md`
- `[x]` `docs/reproducibility/seek-workflowhub.md`
- `[x]` `docs/reproducibility/acceptance-kpis.md`

### Tools
- `[x]` `docs/tools/external-repos-directory.md` — BioContextAI, BioCypher, GA4GH, etc.

### Root
- `[x]` `CHANGELOG.md` — running infra changelog

## Phase B — Major Updates (5 files) ✅ COMPLETE
- `[x]` `README.md` — add Reproducibility, Programs sections
- `[x]` `QUICK_REFERENCE.md` — add HIPAA summary, neuroverse, reproducibility
- `[x]` `docs/MASTER_INFRASTRUCTURE.md` — add pointers to new subtrees
- `[x]` `docs/data-strategy/README.md` — add HIPAA-STATUS, NIH GDS, neuroverse + reproducibility links
- `[x]` `docs/data-strategy/dataset-catalog.md` — add Neuroverse cohort cross-reference

## Phase C — Minor Updates (4 files) ✅ COMPLETE
- `[x]` `docs/data-strategy/templates/data-management-plan-template.md` — status annotations + Neuroverse cross-links
- `[x]` `docs/data-strategy/compliance/hipaa-compliance-framework.md` — link to HIPAA-STATUS
- `[x]` `docs/data-strategy/compliance/phi-security-controls-checklist.md` — marked 30+ controls [x], fixed audit retention to 7yr, added evidence links
- `[x]` `SKILL.md` — bumped to v2.0.0; added 19 new triggers; expanded file tree; 5 new decision rules

## Phase D — Commit & Push ✅ COMPLETE
- `[x]` Verify all docs reachable via README or MASTER_INFRASTRUCTURE
- `[x]` Check no stale `cytonode-01` / `calcom-server-v2` references
- `[x]` Commit 1: **d35f072** — 19 files, 4,346 insertions (new docs + major navigation updates)
- `[x]` Commit 2: **92b3140** — 5 files, 153 insertions (remaining cross-links, PHI checklist, SKILL.md v2)
- `[x]` Pushed to `feat/infrastructure-haul-2026-05`

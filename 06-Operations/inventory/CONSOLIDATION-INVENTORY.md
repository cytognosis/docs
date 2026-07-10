# Consolidation Inventory — What Was Consolidated and Where

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: stakeholders, engineers
> **Tags**: `inventory`, `consolidation`, `catalog`
> **Variants**: Technical (this doc) - Readable (`simple/CONSOLIDATION-INVENTORY.md`) - Agent (n/a)

> [!NOTE]
> **TL;DR**: The main deliverables per area and their canonical locations after the 2026-07-10 reformat round. Full machine list: `catalog.tsv`. Prior locations: `provenance-archives.tsv`.

## A. Disease biotypes — `05-Research/foundational/disease-biotypes/`

| Category | Main deliverables | Location |
|----------|-------------------|----------|
| Canonical index | `BIOTYPES_CHEATSHEET_v2.md` | `diseases/` |
| Per-disease dossiers (15) | adhd, anorexia, anxiety, asd (+ asd-research-brief), bipolar, mdd, ocd, ptsd, schizophrenia, sud-alcohol/cannabis/nicotine/opioid, tourette | `diseases/` |
| Transdiagnostic (4) | micro, meso, macro, connectomic-synthesis (+ BRAIN_MAP.html) | `transdiagnostic/` |
| Cross-scale (2) | molecular-cellular-biotypes.md, multiscale-biomarkers.md | `disease-biotypes/` |
| Archived | ad hoc _TEMPLATE_AND_CONVENTIONS.md (superseded) | `diseases/_archive/` |
| Plain-language | README | `simple/` |

## B. Psychology axes — `05-Research/foundational/dimensional/`

| Category | Main deliverables | Location |
|----------|-------------------|----------|
| Canonical synthesis | `psych-axes-synthesis.md` (merges the SOTA review) | `dimensional/` |
| Neuroplasticity dossier | BDNF_TrkB_Neuroplasticity_Axes_Dossier_2026-06-03.md | `dimensional/` |
| RDoC harmonization | README index + 11 matrices + 10 reference tables (21 CSVs) | `dimensional/rdoc-harmonization/` |
| Clinical instruments (3 CSV) | PHQ-9/GAD-7, DASS, schizophrenia-symptoms mappings | `05-Research/cytoverse/behavioral/clinical-instruments/` |
| Raw source (pointer) | SOTA "Converging Evidence" review | `05-Research/foundational/problem-and-gap/original/` |
| Plain-language | psych-axes-synthesis.md | `dimensional/simple/` |

## C. Yar — `03-Products/Cytonome/Yar/` (6 doc categories) + `04-Engineering/yar/`

| Category | Main deliverables | Location |
|----------|-------------------|----------|
| 1. Product overview | yar-product-spec.md (canonical) + _prompt.md (agent), YAR_FEATURE_CATALOG.md (62 features), sensor-architecture.md, sensor-ecosystem.md, INTEGRATION_PLAN.md | `Yar/` |
| 2. Specs (22) | sensors (physiological, social-interaction, speech-mentalstate, menstrual); platform (CSP, data-sovereignty, edge-ai-hybrid, multi-agent, sync-protocol, storage-engine); behavior (neurobehavioral-axes, personas-voice, crisis-detection, privacy-boundary); storage-eng (SurrealDB tuning/rootcause/advanced, storage recommendation, benchmark tracker/report); client-eval | `Yar/spec/` (+ 15 readable twins in `spec/adhd/`) |
| 3. MVP (14) | scope, architecture, entity model, LinkML mapping, task list, demo flow, risks/acceptance, CAP usage, setup, milestone-1 | `Yar/mvp/` |
| 4. Benchmarks (6) | storage/DB benchmark reports | `Yar/benchmark/` (duplicate `benchmarks/` merged in) |
| 5. Research (15) | feature comparisons, evidence base | `Yar/research/` |
| 6. Prompts (3) + Steering (3) | agent prompts, steering docs | `Yar/prompts/`, `Yar/steering/` |
| Engineering | yar-system-doc.md + sensors/integrations/research/reports/refactor | `04-Engineering/yar/` |
| Plain-language | README | `Yar/simple/` |

## D. Funding — `02-Funding/` (system of record: `reusable-blocks/slot-library/`)

| Category | Main deliverables | Location |
|----------|-------------------|----------|
| System of record | slot-library README | `reusable-blocks/slot-library/` |
| Slots (27) | universal U01-U22 + org A01-A05 | `slot-library/slots/` |
| Funder configs (10 YAML) | arpah_mission_office, astera_residency, brains_accelerator, doe_genesis, foresight_nodes, google_impact_challenge, heilmeier, nih_r01, nsf_tech_labs, yc_nonprofit | `slot-library/funders/` |
| Funder profiles (71) | one profile per opportunity (ARPA-H, ARIA, Astera, Anthropic, RWJF, etc.) | `slot-library/research/profiles/` |
| Proposals | astera_2026 (assembled slots) | `slot-library/proposals/astera_2026/` |
| Crosswalk | funder_crosswalk_matrix.md, funder_metadata.md | `reusable-blocks/` |
| Strategy/other | YC (7), architecture (2), strategy incl. grant-alignment-map.md (2), status (2), foresight, plans, testing | `02-Funding/*` |
| Archived | opportunities stub, raw-source/ (kept, not reformatted) | `_archive/`, `reusable-blocks/raw-source/` |
| Plain-language | README | `02-Funding/simple/` |

## Cross-cutting deliverables

| Deliverable | Location |
|-------------|----------|
| Doc skill v5.6.0 templates | cytoskills `cytognosis-doc/references/{literature-synthesis-template.md, funding-opportunity-profile-template.md}` |
| Master Catalog | `06-Operations/inventory/{MASTER-CATALOG.md, catalog.tsv, provenance-archives.tsv, build_catalog.py}` |
| Migrated overview docs (Step 3) | cytos-pillar, toolchain-overview, operations-overview, org-context, grant-alignment-map (docs repo) + readable twins in Obsidian vault |

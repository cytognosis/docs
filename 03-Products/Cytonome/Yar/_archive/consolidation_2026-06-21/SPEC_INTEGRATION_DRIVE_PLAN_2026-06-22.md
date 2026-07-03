> **Status**: Active
> **Date**: 2026-06-22
> **Author**: Shahin Mohammadi (via Cowork)
> **Audience**: founder, engineers
> **Tags**: `yar`, `spec`, `integration`, `drive-plan`, `psych-axes`

# Yar Spec Integration + ADHDfy — Master Drive Plan (2026-06-22)

> **Reading time**: ~4 min
> **If you only read one thing**: Section "Phase plan" — discovery → incorporate existing work → standardize to cytognosis-doc templates → ADHDfy every spec → verify/sync.

## BLUF

The 9 v0.1 Yar specs were drafted from the consolidation plan but did NOT incorporate (a) existing implementation/schemas in the code repos, or (b) the large prior psych-axes corpus. This plan folds all of that in, standardizes every spec to the cytognosis-doc templates (blockquote metadata header + per-type template), and produces an ADHD-friendly variant of every spec via the 11-step ADHDfy pipeline.

## Done-list (progress)

- [x] Batch 0-5: 9 v0.1 specs drafted + headers + verification PASS-WITH-FIXES (2026-06-22)
- [x] cytognosis-doc skill read; templates + ADHDfy pipeline located
- [x] Phase D: discovery (INCORPORATION_MAP.md + PSYCH_AXES_SYNTHESIS.md)
- [x] Phase T: templates read
- [x] Phase I: all 14 specs incorporated + standardized (axes rebuilt; maturity corrected)
- [x] Phase A: 15 ADHD variants written to spec/adhd/
- [x] Phase V: verified PASS-WITH-FIXES; synced to Grants 2026-06-22

## Discovery surface (do not lose)

**Code repos** (`/home/mohammadi/repos/cytognosis/`, skip `.venv`/`node_modules`/`third_party`):
Yar (app impl), cytoplex (CAP impl), cytos (sensing-schema, `src/cytos`, `schemas/`, `kg/biocypher/schema_config.yaml`), cytocast (`profiles/schema/profile_schema.linkml.yaml`), yar_supervisor_reproducible_benchmark_package (edge-AI supervisor benchmark), neuro-pheno + archive/neuro-pheno, cytomem.

**Psych-axes corpus**:
- `/home/mohammadi/Documents/drafts/Science/psych/`: `neurobehavioral-dimension-direction-model.md` (EQ dimension+direction model; PATO/OBA/ICF/RDoC/Cognitive Atlas/SNOMED post-coordination; 8-type deviation typology), `cdisc-qrs-comprehensive-reference.md` (Part 1 instruments+crosswalks), `cdisc-qrs-feature-space-design.md` (Part 2 six-layer stack), `RDoC_harmonization/` (README + reference_tables/*.csv incl. reference_behavior.csv EQ decomposition + matrices/*.csv), `archive/neuro_onto/` (task1-6 CSVs incl. task5_unified_axes.csv, task6_behavioral_factors.csv), `books/` DSM-5-TR + ICD-11-CDDR (reference), HiTOP papers.
- `/home/mohammadi/Documents/_archive/old_Obsidian Vault/Science/psych/` (mirror of the above; reconcile, do not double-count).
- `/home/mohammadi/Claude/Projects/Science and Platform/`: NeuroMONDO* (disease classification ontology + SSSOM crosswalks), NeuroSTORM_datasets.
- `/home/mohammadi/Claude/Projects/Grants and Applications/`: task5_unified_axes.csv, neuropsychiatric cohorts/landscape.

## Spec → incorporation sources (map)

| Spec | Code/schema sources | Psych-axes sources |
|---|---|---|
| SPEC-neurobehavioral-axes (MAJOR rebuild) | cytos schemas | dimension-direction model, CDISC-QRS P1/P2, RDoC harmonization, task5_unified_axes, neuro_onto, NeuroMONDO, DSM/ICD, HiTOP |
| SPEC-CSP | cytos/sensing-schema, cytos/schemas, biocypher schema_config | unified-axis crosswalk for signal taxonomy |
| SPEC-sensor-physiological | Yar adapters, cytos/sensing-schema | axis mapping |
| SPEC-sensor-speech-mentalstate | Yar voice code, cytocast | axis mapping |
| SPEC-sensor-social-interaction | Yar, AWARE | axis mapping |
| SPEC-sensor-menstrual | (likely none) | cycle-phase covariate to axes |
| SPEC-personas-voice | cytocast profile_schema.linkml | — |
| SPEC-multi-agent | cytoplex, supervisor benchmark | — |
| SPEC-edge-ai-hybrid | yar_supervisor_reproducible_benchmark_package, cytoplex | — |
| SPEC-storage-engine / sync | Yar storage code | — |

## Phase plan

- **D1a** Repo impl/schema sweep → `_research/INCORPORATION_MAP.md` (per-spec artifacts + divergences).
- **D1b** Psych-axes synthesis → `_research/PSYCH_AXES_SYNTHESIS.md` (adopt EQ dimension+direction model + unified axis registry; revisions for the axes spec + sensor crosswalk).
- **T** Read templates: adhdfy-pipeline, adhd-friendly-template, transformation-rules, sensor-spec, module-spec, platform-design, protocol-impl.
- **I** Incorporate + standardize each spec (axes spec = major rebuild). Add blockquote metadata header; keep YAML spec_id frontmatter.
- **A** ADHDfy each spec → `adhd/<spec>_adhd.md` (11-step pipeline).
- **V** Verify (subagent), sync docs-repo → Grants, present.

## Standing constraints

- Canonical = docs-repo `Yar/spec/`; mirror to Grants for review.
- Naming: CSP not USAP; never "Substrate"; CAP/Cytoplex not "Cognitive Agent Protocol".
- SPEC-storage-engine stays `draft` (DB engine open pending SurrealDB retest).
- Confidential factorized-PRS genomic layer: abstract mention only, never methods.
- Affirming, dimensional (not diagnostic) language. No em dashes. Oxford comma.
- Max 2 parallel Sonnet subagents; Opus for synthesis.

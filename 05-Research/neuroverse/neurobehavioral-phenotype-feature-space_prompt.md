# Neurobehavioral phenotype feature space (agent brief)

> **Variants**: Agent seed (this doc) - Technical (see docs repo 05-Research/neuroverse/) - Readable (neurobehavioral-phenotype-feature-space.md in Obsidian vault)

> **Status:** Active · **Date:** 2026-07-01 · **Variant:** agent (self-contained). **Technical source:** [neurobehavioral-phenotype-feature-space.md](neurobehavioral-phenotype-feature-space.md).

## Goal
Define one continuous, multi-resolution feature space for neurobehavioral phenotypes onto which both measurement instruments and DSM/ICD diagnoses project, to serve as the Cytognosis coordinate axis for continuous monitoring.

## Scope
In: the six-layer architecture (BFO/IAO, ICF, MF/MFOEM, HiTOP/RDoC, HPO/SNOMED, PROMIS/CDISC), the five-tuple feature identifier, instrument-to-feature and diagnosis-to-feature mapping, Neo4j Cypher traversal templates over a UMLS+SNOMED+OLS4 graph. Out: model training (see co-embedding review), data governance (see datasets-cohorts, infrastructure).

## Decided / done
- Six-layer stack chosen over any single ontology (none covers all domains).
- HiTOP = dimensional backbone; RDoC = mechanistic anchor; ICF = mid-grain scaffold.
- Each feature node carries a five-part ID: ICF, HiTOP, RDoC, HPO, SNOMED(+UMLS).
- 40-row bulk-download inventory of components compiled.

## Open questions
- The stack does not exist publicly and must be curated; no owner or timeline assigned yet.
- Coverage gaps across cognition, sleep, sexual function, substance, QoL need reconciliation.
- Relationship to BDNF axes and factorized-PRS (named in planning, not yet written) is undefined; see [Cytoverse science-foundation](../../03-Products/Cytoverse/science-foundation.md).

## Pending tasks (prioritized)
1. Stand up the curated feature graph from the bulk-download inventory (Cypher templates in the technical doc).
2. Validate diagnosis reconstruction (DSM-5-TR, ICD-11) as feature combinations against a labeled cohort.
3. Reconcile with the [instrument reference](cdisc-qrs-instrument-reference.md) item catalog.

## Source-of-truth files
- Technical: `05-Research/neuroverse/neurobehavioral-phenotype-feature-space.md`
- Companion instrument vocabulary: `05-Research/neuroverse/cdisc-qrs-instrument-reference.md`
- Harmonization reference data: `~/datasets/cytognosis/ontologies/` (disease, clinical-instruments, rdoc)

## Success criteria
Instruments and diagnoses both project onto the shared axes; a query at any layer returns consistent features; diagnosis reconstruction matches held-out labels above an agreed threshold.

## Start commands
Read the technical doc top-to-bottom; then inspect the Neo4j graph with the Cypher templates in its section 8. Reference tables live under `~/datasets/cytognosis/ontologies/`.

# Cytoverse Track: Science Foundation State

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: leadership
> **Tags**: `strategy`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)

**Date:** 2026-06-03 | **Classification:** Internal, confidential. Contains platform-confidential IP references (Section 5). | **Reading time:** ~10 min.

**If you only read one thing:** The science foundation is real and defensible. The BDNF/TrkB axis paper has a clear publishable scope and strong grant alignment (EVIDENT/HSF, IGoR TA1). The KG/cytos platform is production-ready at 9.3M nodes. The cellular micro-to-meso causal bridge is the convergence spine connecting all three funding tracks. The factorized PRS remains confidential platform IP and must stay off the bipolar paper.

---

## Done List

- [x] Science keystone dossier written (BDNF/TrkB axes, publish vs platform boundary defined)
- [x] Transdiagnostic MICRO, MESO, and MACRO syntheses complete (14 disorders mapped)
- [x] Cytos KG production at 9.3M nodes, 53M edges, 52 node labels, 200+ edge types
- [x] Data lake organized (~1.5TB, 13-category structure documented)
- [x] Validation infrastructure operational (VFS, RO-Crate, provenance 93.3% coverage)
- [x] Genomic atlas implemented (GWAS, eQTL, PRS, LDGM, pangenome modules all production)
- [x] Bioentity landscape evaluated (semantic vs biomolecular entity gap identified)
- [x] Transdiagnostic axes mapped to Nature 2025 five-factor genomic structure (Grotzinger et al.)
- [x] Publish-vs-platform boundary defined (Section 7 of BDNF dossier)

---

## 1. Taxonomy Position

Cytoverse is the **Map** pillar. Its role is to build the science foundation that every other pillar depends on:

| What it produces | Who consumes it |
|---|---|
| Dimensional neuropsychiatric axes (Mood, Thought, Cognitive) | Cytonome biotype classifier, IGoR TA1 |
| KG (ontology + observation + genome) | Cytoscope biotype layer, HSF/EVIDENT grant framing |
| Cellular micro-to-meso causal bridge | IGoR TA1 differentiator; HSF mechanism anchor |
| Publishable bipolar axis paper | Priority claim, academic credibility, grant leverage |
| Confidential platform science | Cytoplex genotype factorization, Psychoverse coordinate (moat) |

Primary repos: `cytos`, `docs/cytoverse`. Primary research corpus: `X-Labs/04-research/`.

---

## 2. Current State of the Science Foundation

### 2.1 BDNF/TrkB Axes: the scientific keystone

The first scientific keystone is a set of **continuous, molecularly grounded neuropsychiatric axes** defined by dysregulation downstream of BDNF/TrkB signaling, demonstrated first in bipolar disorder:

- **Mood / neuroplasticity axis:** CREB-driven plasticity program (mBDNF/TrkB to CREB, LTP, dendritic arborization, neurogenesis).
- **Thought axis:** GABAergic/E/I balance (TrkB-PLCgamma-PKC and PI3K to KCC2 and GABA-A trafficking; mBDNF/proBDNF ratio sets inhibitory tone).
- **Cognitive axis:** BDNF-CREB learning/memory programs (ERK/CREB late-LTP; mTOR-4EBP1 local translation; hippocampal/prefrontal circuits).

**Discovery cohort:** McLean (published, PsychENCODE schizophrenia capstone). **Out-of-distribution validation:** MtSinai cohort (cross-validation in progress).

**Molecular differentiator:** cholesterol-TrkB feedforward loop (Casarotto et al., Cell 2021; Moliner et al., Nat Neurosci 2023). All antidepressants and psychedelics converge on TrkB TMD binding; they are neuroplastogens, not receptor agonists. This is the EVIDENT mechanistic anchor.

**Uncertainties to flag in the paper (no overclaiming):**
- Val66Met main effect is weak and contested in mixed-ancestry samples.
- SREBP/mTOR/TrkB loop is inferred from component studies, not yet demonstrated in one mood-disorder system.
- Adult proBDNF secretion is debated.
- BDNF-KCC2 evidence is strongest in development/ASD; less direct in adult BD/MDD.

### 2.2 Cytos KG Platform: current production state

| Component | Status | Scale |
|---|---|---|
| Ontology Graph (OG) | Production | UMLS, SNOMED, 37 OBO ontologies, HRA, UniChem, Ensembl |
| Catalog Graph (CG) | Production | PKG2.0, PlaNet, OpenAlex |
| Observation Graph (ObG) | Production | Monarch, PrimeKG, Open Targets, GWAS |
| GenomeKG | Production | GENCODE, GWAS Catalog, PGC, WGS VCF |
| **Total** | **Production** | **9.3M nodes, 53M edges, 52 labels, 200+ edge types** |

Backend: KGStore protocol (Neo4j production; DuckDB dev/analytics; SurrealDB partial). Key modules: genomic atlas (GWAS/eQTL/PRS/LDGM), brain atlas, scholarly KG, schema system (43 LinkML schemas in cytoskeleton).

**Known gaps:**
- SurrealDB client missing async context manager (bug).
- Pathway and developmental-stage nodes not yet loaded.
- VRS 2.0 seqrepo integration blocked.
- KG biomolecular entities (genes, proteins, variants as instances) not yet first-class in graph; only ontology classes present.

### 2.3 Data Lake

~1.5TB organized in a 13-category structure on local compute. Categories include: ontologies (69GB), vocabularies (136GB), external KGs (393GB, including Monarch/PheKnowlator/PrimeKG/Open Targets), identifiers (171GB), single-cell, neuroimaging (319GB), embeddings (34GB), network data (200GB). Provenance coverage: 93.3% (56/60 Parquet files with validated SHA-256 sidecar). VFS lifecycle validated; RO-Crate provenance operational.

### 2.4 Transdiagnostic axes synthesis (the scientific context)

Fourteen disorders mapped across MICRO (molecular/cellular), MESO (connectomic), and MACRO (behavior/systems) scales. Key finding relevant to Cytoverse:

The 2025 Nature five-factor genomic structure (Grotzinger et al., 1,056,201 cases) provides the anchor:
- **SB factor** (SCZ + BD): excitatory neurons.
- **Internalizing factor** (MDD + PTSD + anxiety): oligodendrocytes.
- **Neurodevelopmental factor** (ASD + ADHD + Tourette).
- **Compulsive/eating factor** (OCD + anorexia).
- **Substance-use factor** (AUD/OUD/NUD/CUD): dopaminergic + metabolic.

BDNF/TrkB plasticity, E/I imbalance, oxidative/mitochondrial stress, and immune/microglial activation all recur across factors, making them valid transdiagnostic sensing targets. The BDNF axes defined in Section 2.1 cut across the SB and internalizing factors in ways that make them especially useful for BD and MDD stratification.

---

## 3. The Cellular Micro-to-Meso Causal Bridge Thesis

This is the convergence spine of all three near-term funding tracks.

**The thesis:** Psychiatric variation is not flat. It runs from genome to transcriptome to single-cell gene programs (micro) up to circuit topology and functional connectivity (meso). Most of the field works at one scale: geneticists use GWAS, circuit neuroscientists use fMRI, clinicians use symptoms. Cytognosis's differentiated position is building the **causal link across scales**: demonstrating that specific molecularly defined cell-type programs (micro) predict, and causally explain, the circuit-level differences (meso) that ultimately drive symptom biotypes.

**Concretely:**
- **Micro:** BDNF/TrkB axis biotypes (Mood, Thought, Cognitive axes) defined by dysregulated cell-type-specific programs in postmortem snRNA-seq.
- **Bridge:** snRNA-seq cell-type decomposition reveals that the SB-factor genomic signal concentrates in excitatory neurons and the internalizing-factor signal in oligodendrocytes; the KCC2/GABA-A trafficking biology links micro-scale interneuron dysfunction to meso-scale E/I imbalance and gamma oscillation deficits.
- **Meso:** The functional connectivity signatures (dlPFC-sgACC edge, amygdala-vmPFC edge, CSTC loop topology) that emerge from cellular dysfunction; the meso-scale biotypes that Cytoscope will ultimately sense.

**Why HSF cares:** HSF/EVIDENT funds objective measures and responder identification for neuroplastogens. Our micro-to-meso bridge says: BDNF-axis molecular biotype (micro) predicts who sits where on the plasticity-state continuum (meso) and therefore who responds to a TrkB-engaging neuroplastogen. That is the exact EVIDENT target.

**Why IGoR TA1 cares:** IGoR TA1 asks for biological mechanisms underlying heterogeneity, not just symptom clustering. The cellular bridge provides the mechanistic justification: heterogeneity in circuit-level response to treatment arises from variation in molecularly defined cell-type states. This differentiates our IGoR bid from approaches that remain at the connectomic level.

**Why Cytoscope connects here:** Cytoscope's biotype layer needs a theory of what it is sensing. The micro-to-meso bridge is that theory: the sensor reads meso-scale signals (EEG gamma, fNIRS-CCO, aperiodic slope), and the bridge tells us what molecular state those signals index.

---

## 4. Top-3 Science Priorities

### Priority 1: Complete and submit the bipolar paper (McLean + MtSinai OOD validation)

**Why first:** This is the priority and credit claim for the axis framework. Without a preprint, there is no IGoR credibility and no EVIDENT anchor. It also locks the Shahin/Brad/Xikun authorship on the axis framework before any consortium-facing work creates attribution ambiguity.

**Scope:** Publishable science only (BDNF/TrkB molecular biology, the Mood/Thought/Cognitive axes, discovery in McLean, OOD validation in MtSinai). Compute compliance: McLean re-analysis on Cytognosis resources; MtSinai WGS runs inside MtSinai approved environment with Panos's team. No Luria for Cytognosis-relevant work (IPPIA boundary).

**Open to-dos:** Finalize Cognitive-axis pathway set; integrate TrkB-glucocorticoid and TRPC mechanisms; decide final scope with Brad and Xikun.

**Confidentiality note:** The factorized PRS and genotype factorization model stay OFF this paper. Publish the biology; own the measurement platform.

### Priority 2: Run stratified-LDSC to de-risk the confidential platform science

**Why second:** The cheapest de-risking step before building the full PRS pipeline is to confirm that CREB-bound and SREBP-bound genomic regions are enriched for the relevant trait heritability. If the heritability enrichment signal is not there, the platform premise needs rethinking before significant engineering investment. This is a cheap, publishable intermediate step (heritability partitioning is publishable on its own).

**Distinct from Priority 1:** This work is platform IP scoping. The result informs whether the confidential platform layer is biologically justified; it does not appear in the bipolar paper.

### Priority 3: Load biomolecular entities (genes, proteins, variants) as first-class KG nodes

**Why third:** The KG currently has ontology classes for genes but not individual gene/protein/variant instances. Cytoverse's genomic-to-circuit bridge requires traversing from GWAS hits (variant instances) through eQTL associations to cell-type gene programs. That traversal is blocked until biomolecular entities are first-class. The bioentity landscape evaluation identified the gap; bionty + biothings integration is the solution.

**Scope:** Add Gene (Ensembl, ~60K human), Protein (UniProt, ~20K reviewed), and Variant (dbSNP/ClinVar) as instance nodes. Pathway nodes (GO/PW) are also needed. This is an engineering sprint.

---

## 5. Confidential Platform Science

The factorized PRS and genotype factorization model are confidential platform IP.

**What it does:** Reconstructs the BDNF-axis biotypes from a person's genome alone by computing process-specific polygenic scores restricted to transcription-factor-bound regions (CREB-bound for the neuroplasticity axis; SREBP-bound for the cholesterol/TrkB axis). This yields per-person, process-specific axes computable noninvasively from genotype, which is the foundation of the Psychoverse coordinate.

**Why it is the moat:** The publishable science (the biology and that the axes exist) establishes priority. The platform (the genome-derived measurement, integration, and product) is the proprietary layer above. The moat is the TF-region-factorized, mechanism-anchored, coordinate-system formulation, not the per-pathway PRS concept itself (PRSet already exists).

**What to claim precisely when the time comes:** Not "per-person pathway PRS is new" (PRSet owns that). Claim the TF-region-factorized, mechanistically anchored, coordinate-system formulation.

**Where it lives:** This section. Not in the bipolar paper. Not in consortium-facing material. Not in any external-facing Cytoverse description.

---

## 6. Gaps

| Gap | Priority | Notes |
|---|---|---|
| Bipolar paper draft not yet submitted | P0 | Blocking IGoR credibility and EVIDENT anchor |
| Stratified-LDSC for CREB/SREBP heritability not run | P1 | De-risk before platform pipeline build |
| Biomolecular entity nodes not in KG | P1 | Blocks micro-to-meso bridge traversal |
| Cognitive-axis pathway set not finalized | P1 | Required for paper completion |
| SurrealDB async context manager bug | P2 | Blocks SurrealDB backend use |
| VRS 2.0 seqrepo integration blocked | P2 | Variant annotation incomplete |
| MtSinai WGS DUA compliance not confirmed | P1 | Required before OOD genomic validation |
| proBDNF secretion mechanism (adult) | Science uncertainty | Flag in paper; do not overclaim |

---

## 7. Duplicate and Historical Science Docs: Canonical-Home Assignments

These files were identified in the corpus. **Do not edit them.** Reconcile canonical home during Stage 5 cleanup.

| File / cluster | Current locations | Canonical home (do not edit now) | Disposition of others |
|---|---|---|---|
| `01_plan_prose.md` (cytos platform design) | `docs/cytoverse/cytos/historical/historical/01_plan_prose.md`; also referenced as having copies in `cytos/design/historical` and `cytos/docs/historical/historical` | `docs/cytoverse/cytos` engineering canonical | Historical copies = superseded; index in cytomem; do not delete |
| Transdiagnostic MICRO/MESO synthesis | `X-Labs/04-research/transdiagnostic/` | Same (already canonical) | None seen |
| `molecular-cellular-biotypes.md` | `X-Labs/04-research/` | `X-Labs/04-research/` (already canonical) | None seen |
| BDNF dossier | `X-Labs/04-research/BDNF_TrkB_Neuroplasticity_Axes_Dossier_2026-06-03.md` | Same (already canonical) | Preceded by sections in `molecular-cellular-biotypes.md` (superseded) |
| `neurobehavioral-dimension-direction-model.md` | `personal-drafts/Science/psych/` | Superseded by BDNF dossier | Keep indexed, do not edit |

---

## 8. Cross-Track Convergence Summary

| Funding track | Science connection | What Cytoverse delivers |
|---|---|---|
| IGoR TA1 | Cellular micro-to-meso bridge as the mechanistic heterogeneity explanation | Axis biology, KG ontology support for IGoR ontology asks, GWAS/eQTL data infrastructure |
| HSF / EVIDENT | BDNF/TrkB neuroplastogen mechanism as the measurable plasticity state | Molecular biotype → responder identification; TrkB-convergent mechanism framing |
| NSF X-Labs / Cytoscope | Micro-to-meso bridge as the theory of what Cytoscope sensors are reading | Biotype layer definitions; meso-scale node/edge targets (gamma, dlPFC-sgACC, etc.) |

---

## 9. Key References

Casarotto et al., Cell 2021 (PMID 33606976). Moliner et al., Nat Neurosci 2023 (PMID 37280397). Gupta et al., Mol Neurobiol 2025 (PMID 40342191). Barde, physiopathology of BDNF 2025. Grotzinger et al., Nature 2025 (doi:10.1038/s41586-025-09820-3). Choi et al. (PRSet), PLOS Genet 2023 (PMID 36732591). Finucane et al. (S-LDSC), Nat Genet 2015. ARPA-H EVIDENT (first teams announced April 21, 2026, $139.4M). WikiPathways WP4829.

---

**Related files:**
- `~/Claude/Projects/X-Labs/04-research/BDNF_TrkB_Neuroplasticity_Axes_Dossier_2026-06-03.md` (science keystone, contains confidential Section 5)
- `~/Claude/Projects/X-Labs/01-strategy/STAGE4_META_STRATEGY_TAXONOMY_2026-06-03.md` (taxonomy anchor)
- `docs/cytoverse/cytos/architecture.md` (KG platform architecture)
- `docs/cytoverse/cytos/module-map-v2.md` (Cytos module status)
- `docs/cytoverse/cytos/genomic-atlas.md` (genomic subsystem)

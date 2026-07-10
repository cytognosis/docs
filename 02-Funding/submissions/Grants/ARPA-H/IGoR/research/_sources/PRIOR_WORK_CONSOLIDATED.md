# CytoIGoR — Prior Work Consolidated Brief

**Compiled:** 2026-06-11
**Purpose:** Single-stop reference for the lead writer of the ARPA-H IGoR full proposal (due 2026-08-06). Captures specific phrasings, numbers, names, and open decisions from all prior drafts. Do not generalize the content — reuse the exact formulations where possible.
**Reading time:** ~18 min
**If you only read one thing:** Section 1 (TA1 Technical Narrative) and Section 7 (Open Decisions) are the highest-leverage pages.

**Source files:**
- `ARPA-H_IGoR_Solution_Summary_REVISED_2026-06-05.md` (most current solution summary; IPAI-prime framing)
- `ARPA-H_IGoR_Solution_Summary_REVISED_2026-06-02.md` (prior draft; Cytognosis-prime framing)
- `IGoR_Comprehensive_Reference_2026-06-05.md` (solicitation analysis + consortium mapping)
- `IGoR_TA1-TA2_Methods_DeepDive_2026-06-05.md` (full technical stack; contains PROPRIETARY content)
- `IGoR_Cost_Breakdown_2026-06-02.md` (cost model)
- `IGoR_Strategy_Master_2026-06-03.md` (strategic decisions)
- `IGoR_Key_Info_and_Disease_Strategy_2026-06-02.md` (disease framing)
- `IGoR_TA1-TA2_Partner_Onepager_2026-06-05.md` (external-facing one-pager)
- `IGoR_Teaming_Page_Submission_2026-06-06.md` (teaming-page text)
- `IGoR_Candidate_Slate_Tier1-3_2026-06-03.md` (partner tiering)
- `schizophrenia_MONDO_subtypes_22q11_TBX1.md` (MONDO/genetic evidence)
- `cellular-disease-model-standards-comparison.md` (standards landscape)
- `disease-knowledge-standards-comparison_2026-06-10.md` (Cytoverse stack reference)

---

## CONTENTS

1. Technical Narrative — TA1 (Causal Disease Model)
2. Technical Narrative — TA2/TA3/TA4
3. Disease Strategy
4. Team Configuration
5. Cost Model
6. Key Citations
7. Open Questions and Decisions
8. Internal Inconsistencies Flagged

---

## 1. TECHNICAL NARRATIVE — TA1

### 1a. Positioning phrase (committed language)

**Concept summary opening (verbatim from 2026-06-05 SS):**

> "Biomedical discovery for complex diseases is bottlenecked by three compounding failures: models that **correlate rather than explain**, experiment design driven by **intuition rather than uncertainty**, and data that **cannot be reproduced or reused** across labs. Knowledge accumulates slowly, cannot be integrated across scales, and cannot be queried to generate testable predictions."

**TA1 positioning claim (verbatim):**

> "The 'virtual cell' landscape is dominated by correlational transformer embeddings (scGPT, Geneformer, Arc STATE), perturbation predictors (GEARS, CPA), and single-scale systems-biology networks (CARNIVAL, NicheNet). The few explicitly mechanistic tools (Virtual Brain Twin, COSMOS) are single-scale and not experimentally updatable. **No platform integrates single-cell atlas data, perturbation modeling, causal-network inference, and circuit-level physiology into a multiscale model that updates from new experiments.** That integration is our TA1."

**Micro-to-meso bridge phrase (used in Candidate Slate):**

> "The cellular micro-to-meso bridge" — used as the CytoIGoR wedge vs. HSF. This differentiates IGoR from the ARPA-H Health Science Futures track.

### 1b. Four-Pillar architecture (from IGoR_TA1-TA2_Methods_DeepDive_2026-06-05)

The TA1/TA2 stack is organized into **four pillars**, each flowing into the next:

```
Pillar 1 (Network priors) -> Pillar 2 (Causal generative modeling)
-> Pillar 3 (Joint cellular/clinical shift-space) -> Pillar 4 (Ontology OOD + experiment design)
-> (Pillar 4 proposes experiments that feed back to Pillar 1)
```

**The single most important design principle (BLUF from methods doc):**

> "Everything is measured as a *shift (delta) in pathway space relative to a dataset-specific control*, which is what lets us aggregate cellular and clinical evidence into the same causal model and what makes TA2's experiment proposals mechanistically targeted rather than literature-mined."

### 1c. Pillar 1 — Network curation

**Harmonization backbone:** Molecular Interaction (MI) ontology (term MI:0190)

**Sources harmonized (commit this list):**
STRING, Reactome, Reactome FI, SIGNOR, TFLink, IntAct, BioGRID, OmniPath, Co-abundance Atlas

**Edge type taxonomy (MI top types):**

| Layer | MI terms | Examples |
|---|---|---|
| Functional / causal | MI:2245, MI:0414 | signaling, regulatory, metabolic, PTM, epigenetic |
| Molecular / experimental | MI:0045 | direct vs indirect x high vs low throughput x physical vs genetic |
| Predicted | MI:0063 | co-expression, text-mining, homology |
| Phenotypic | genetic | genetic interactions |

**Neuro-specific layers added on top:**

| Layer | Method/source | What it contributes |
|---|---|---|
| Cell-type-specific PPIs | Kasper Lage AP-MS in iPSC-derived neurons (autism, *Cell Genomics* 2022) | Experimentally validated, neuron-resolved physical edges; IGF2BP1-3 complex convergence |
| Cell-type GRNs | PsychENCODE brainSCOPE multiome GRNs (snRNA + snATAC, 24 brain cell types) + ChIP-seq | Directed TF -> target and enhancer-gene edges, cell-type-resolved |
| Cell-type co-expression | CS-CORE (depth/noise-corrected co-expression from scRNA-seq UMIs) | Unbiased per-cell-type co-expression; used inside generative decoders |

**Coverage map design (differentiating):** We build dedicated tools to map which pathways, processes, and subnetworks each interaction type/technology covers well. This coverage map is used as (a) a confidence prior during inference, and (b) a driver for TA2 to propose experiments that fill under-covered regions.

### 1d. Pillar 2 — Causal generative modeling

**SAMS-VAE extension (committed framing):**

The model extends the sparse additive mechanism-shift idea (**SAMS-VAE**; Bereket and Karaletsos, NeurIPS 2023; arXiv:2311.02794). Shahin contributed to the published work and to unpublished joint Perturb-seq + POSH morphological models in TSC and monogenic epilepsy / neurodevelopmental NGN2 lines at insitro.

**Committed phrasing:** "A cell's latent state is a **basal/healthy state plus sparse additive shifts**. We model **extrinsic factors (treatment and/or disease)** as sparse mechanism-shifts acting on the **intrinsic basal cell state**."

**Covariance-preserving decoders (departure from prior art):**

> "We replace the independent negative-binomial losses used in VAEs (scVI, and perturbation models built on it including SAMS-VAE) with **CS-CORE-informed, vine-copula decoders** (the dependence construction from **scDesign3**), so reconstructed cells preserve real **gene-gene covariance** rather than treating genes as conditionally independent."

References: CS-CORE (Su et al. *Nat Commun* 2023; DOI 10.1038/s41467-023-40503-7); scDesign3 (Song et al. *Nat Biotechnol* 2024; DOI 10.1038/s41587-023-01772-1).

**GNN-based intervention design — PDGrapher (committed):**

> "We adopt **PDGrapher**'s two-phase graph neural network over our interaction network: (1) **propose perturbagens** that shift a diseased state toward a target/healthy state (inverse design), and (2) **predict the response** to a candidate perturbation. Interventions are represented as **edge mutilations** on the causal graph."

Reference: Gonzalez et al. *Nat Biomed Eng* 2025; DOI 10.1038/s41551-025-01481-x.

**AlphaGenome usage (committed):**

AlphaGenome (Google DeepMind, 2025) provides sequence-to-regulatory-grammar representations. **Apache-2.0 code, noncommercial weights; suitable for 501(c)(3) nonprofit research.** Used as a tool, not retrained. COMT/TBX1/DGCR8 perturbation effects on gene regulatory networks are encoded using causal inference over single-cell multiome data.

### 1e. Pillar 2b — Factorized-PRS (PROPRIETARY — mark all pages; keep off partner materials)

**THIS SECTION IS CROWN-JEWEL IP. Do not include in partner-facing one-pagers, teaming pages, or any non-proprietary section of the submission. Mark affected proposal pages "Proprietary."**

**What it is:** An extension of PRS (polygenic risk score) from one collapsed score into many biologically disentangled, pathway-focused scores. The method factorizes the genotype x phenotype matrix so that:

- Genotype factors are sparse (following the sparsity-of-shift mechanism), biologically disentangled, and enriched in distinct processes -> interpretable, literature-alignable, and directly translatable into follow-up experiments.
- Phenotype factors are transdiagnostic -> they capture variation within and across disease labels and serve as candidate biotypes/biomarkers.

**Novelty claim (must be stated precisely against precedent):**

> "Novelty must be claimed precisely against **PRSet** (pathway-partitioned PRS; Choi et al. *GigaScience* / *PLoS Genet* 2020) as the nearest precedent: our contribution is the joint, sparse, disentangled genotype-and-phenotype factorization tied to the mechanism-shift, not pathway partitioning alone."

**In the proposal:** stated under proprietary marking; referenced publicly only as "we additionally factorize patient-level genetic variation into sparse, pathway-disentangled, transdiagnostic axes that double as candidate biotypes; the detailed factorization method is proprietary."

### 1f. Pillar 3 — Joint cellular + clinical shift-space

**The failure mode we name (committed framing):**

> "In-vitro-only programs (including prior insitro work, and current efforts at Xaira, Recursion) prioritize interventions that make **disease cells look like healthy cells**, then use clinical data only afterward to validate. These pipelines often **cannot distinguish clinically relevant disease axes**, because many cellular signatures are **artifacts of the model system**: iPSC differentiation artifacts, missing cellular composition and interactions (e.g., glial-neuronal), and missing systemic effects (microbiome, immune)."

**Our contribution (committed):** We measure everything as a shift (delta) in pathway space relative to a dataset-specific control, on both cellular and clinical scales. That common representation lets us aggregate and reconcile cellular and clinical evidence into the same causal model, and surface disease axes that are consistent across scales (and therefore robust to model-system artifacts).

### 1g. Pillar 4 — Ontology conditioning and experiment design

**Ontology table (committed):**

| Domain | Ontology |
|---|---|
| Disease | MONDO |
| Cell type | Cell Ontology (CL) |
| Tissue / brain region | UBERON |
| Process / pathway | Gene Ontology + Pathway Ontology (incl. GO-plus) |

**Box embeddings:** TransBox (EL++-closed; subsumption encoded as box containment, so is-a transitivity is exact). Reference: Xiong et al. (2024) arXiv:2410.14571.

**Two functions of ontology conditioning:**
1. OOD generalization: the model can reason about unseen cell types or disorders by interpolating in ontology space.
2. Gap finding: under-explored ontology subtrees are exactly where interpolation is unreliable; those gaps become high-value experiment targets for TA2.

**Hypothesis template (fixed, committed phrasing):**

> **"Perturbing pathway / process X will shift the disease phenotype in disease Y toward healthy by modulating Z."**

Because X, Y, Z are ontology terms, each hypothesis is grounded with ontology-aware NER (spaCy, scispaCy, medspaCy for negation/context) and templated, schema-validated extraction (Instructor + Pydantic) to pull harmonized, ontology-aligned evidence for and against the hypothesis for the TA2 agents.

**Hub/key-node selection (how hypotheses become experiments):**

> "We find the **hubs / key nodes** (transcription factors, key signaling biomolecules) whose perturbation is predicted to **modulate the largest number of downstream biomolecules** in the target process (the process enriched on our genotype factors). Perturbing those hubs is the highest-value way to shift disease cells toward a healthy state."

### 1h. Quantitative SOTA comparison table (committed)

| Capability | SOTA baseline | CytoIGoR target |
|---|---|---|
| Disease-model basis | Correlational embeddings; single-scale mechanistic | Mechanistic, multiscale (molecular -> circuit), auto-updating |
| Experiment design | LLM-suggested or active-learning, black-box | Mechanistic-model-grounded, value-of-information ranked |
| Cross-lab reproducibility | Ad hoc, batch-effect-laden | Layered protocol stack, >=90% concordance target |
| Experimental cycle time | Conventional baseline | >=10x faster by Phase III (IGoR marquee metric) |

### 1i. Data sources committed to in TA1

- **PsychENCODE single-cell atlases** (PI co-led): multi-cohort schizophrenia; brainSCOPE GRNs (Emani et al. *Science* 2024)
- **PsychAD atlas** (*Nat. Neurosci.* 2024; Batiuk et al.; PI co-author)
- **ROSMAP atlas** (*Nature* 2019; Mathys, Mohammadi et al.)
- **PGC schizophrenia GWAS** (referenced for genomic layer; exact version/release not specified in docs — to confirm)
- **Open Targets** (GWAS causal gene scoring, L2G)
- **JUMP Cell Painting Consortium** (>116K compounds; Carpenter/Broad)

### 1j. Go/no-go metrics for TA1 (committed)

- Phase I: model explains >=30% of variance in 22q11DS-specific cell-type shifts; first TA4 data return cuts parameter uncertainty >=20%.
- Phase II: at least one prospective prediction validated in an independent dataset; TA1 update latency <=24 h.

### 1k. Standards stack for TA1 representation

From `disease-knowledge-standards-comparison_2026-06-10.md`, the recommended Cytoverse/TA1 layered stack:

| Layer | Adopt |
|---|---|
| Identity/semantic backbone | MIRIAM + Bioregistry; OBO (GO, CL, Uberon, Mondo, HPO); RO relations; Biolink graph schema |
| Causal mechanism | INDRA + CoGEx (+ EMMAA) as assembly engine; GO-CAM as curated ground truth |
| Executable disease model | Disease-Map pattern: SBGN/CellDesigner -> CaSQ -> SBML-qual -> MaBoSS |
| Genomic causal anchor | Open Targets (L2G, GWAS fine-mapping) + Mendelian randomization + Perturb-seq causal GRN |
| Omics bridge | VEGA / SENA-discrepancy-VAE (pathway-space, causal-identifiable latents); GEARS for perturbation prediction |
| Data layer | AnnData/MuData, CZ CELLxGENE Census; scverse |
| Temporal / progression | SuStaIn/EBM (clinical staging) + pseudotime/CellRank; build thin RO/Mondo-grounded progression schema |
| Reproducibility | OMEX/COMBINE + SED-ML + KiSAO; FAIR/Bioregistry |

**Key SENA framing from standards doc (relevant to factorized-PRS positioning):**

> "SENA-discrepancy-VAE (2025): causal representation learning with **causal identifiability** plus latent factors constrained to GO biological-process space; the current leading edge of 'causal + interpretable + omics.'"

This is the closest public comparator to our factorized-PRS; claim novelty precisely.

---

## 2. TECHNICAL NARRATIVE — TA2 / TA3 / TA4

### 2a. TA2 — New Science Engine

**Core framing (committed, verbatim):**

> "Our TA2 treats the TA1 causal model as a first-class queryable object: it identifies unconstrained parameters, hypothetical edges, and inconsistent fluxes, then proposes the experiment that most reduces model uncertainty (value-of-information selection)."

**Three-component architecture (committed):**

1. **Tournament** of competing causal-link hypotheses: generate -> critique -> rank -> evolve. Adversarial critics grounded in mechanistic constraints, not literature retrieval alone. Pattern established by DeepMind Co-Scientist (open reimplementation: LLNL open-ai-co-scientist).

2. **Mechanistic-model-grounded retrieval-augmented planning (RAP):** The retrieval corpus is the structured output of the TA1 model (unconstrained parameter sets, hypothesized edges with uncertainty bounds, inconsistent flux predictions), not papers alone. Selects the experiment with the highest value of information.

3. **Test-time validation scaling:** Before surfacing a hypothesis to the experimental queue, the engine runs lightweight mechanistic simulations to pre-validate the prediction is consistent with known constraints. Filters low-quality experiment designs before they consume wet-lab resources.

**Hard-line language (IGoR-required; must appear in the proposal):**

> "This is explicitly not a wrapper around a frontier large language model." (appears verbatim in both SS drafts)

**Open scaffolding stack (committed):** LangGraph (stateful backbone), AutoGen/AG2 (debate and critique), Anthropic Agent SDK (explainable critique traces), MCP-grounded tools via ToolUniverse and BioContextAI. No dependence on closed-source frontier model APIs for the core reasoning loop.

**SOTA gap claim (commit):** "Of approximately 15 agentic-science systems surveyed (Co-Scientist, Robin/Kosmos, Biomni, SciAgents, the Stanford Virtual Lab, OpenScientist, Coscientist, Lila Sciences, and others), **none interrogate a mechanistic or causal disease model to generate hypotheses**."

**Go/no-go metrics for TA2 (committed):**
- Phase I: >=3 proposed experiments executed with cross-lab reproducibility; hypothesis rank correlates with experimental effect size (Spearman r >=0.4 on first ten experiments).
- Phase II: end-to-end cycle time (model query to validated data return) <=12 weeks; knowledge generation rate at least 3x conventional on benchmarked tasks.

### 2b. TA3 — Interoperable Protocol Stack

**Committed description:** Declarative experiment specs from TA2 are translated through an intent -> protocol -> calibration -> hardware stack covering >=3 modalities:

1. Live-cell imaging + same-cell scRNA-seq via Cellanome R3200 (Perturb-LINK pooled CRISPR)
2. Optical pooled screening + Cell Painting morphological screening via Carpenter
3. Untargeted multi-omics (metabolomics, lipidomics, proteomics) via Panome Bio

**Standards used:** Open LinkML-based schemas; all protocol versions archived and versioned. Carpenter's Cell Painting Gallery, JUMP dataset, and OASIS/COBA open image-data standards seed the TA3 layer.

**RFC process (IGoR requirement):** locked-default parameters; changes go through RFC-governed process backed by evidence.

### 2c. TA4 — Validated-Lab Marketplace

**Phase targets (committed):**

- Phase I: intra-team reproducibility; >=85% concordance; >=1 experiment
- Phase II: cross-team execution; >=90% concordance; >=3 experiments; multicellular systems
- Phase III: unified marketplace; external-researcher use; >=3 labs; >=90% concordance across marketplace

**Data return:** QC-rich, model-ready packages formatted to the IGoR common data model; openly released at each phase milestone.

### 2d. Phase I anchor experiment (committed)

> "A tractable, high-value first loop: paired isogenic iPSC lines for a single high-penetrance lesion (Shahin's ultra-rare 32bp TBX1 exon-2 CNV, a 22q11DS-superclass model), CRISPR-corrected to a matched healthy control and differentiated to NGN2 neurons. TA2 designs the discriminating screen; Cellanome and Carpenter execute live-cell, transcriptomic, and morphological readouts; TA1 defines the disease axes and ingests the data."

**Built-in mechanistic test:**

> "A built-in mechanistic test (whether vitamin B12 / methylcobalamin reverts the phenotype, predicted from Tbx1-mutant mouse rescue) gives an early, falsifiable validation of the closed loop."

Mouse rescue reference: *Life Sci Alliance* 8(2):e202403075 (not in the citations list yet — add to proposal refs).

**Option noted:** this study may run as a parallel, independently funded effort with Carpenter. If kept separate it still de-risks IGoR by establishing the line set and assays.

---

## 3. DISEASE STRATEGY

### 3a. Primary (Phase I/II): 22q11.2 deletion syndrome

**Rationale for 22q11DS as exemplar (committed framing):**

> "22q11DS is the highest-penetrance known genetic risk factor for psychosis; its deletions span TBX1, COMT, and DGCR8 — genes with well-characterized but mechanistically unlinked effects on cell-type pathology and thalamocortical / fronto-temporal circuit function. Formalizing that molecular-to-circuit causal chain, and using it to drive systematic experiment design, is a tractable, scientifically important, and measurable deliverable."

**IGoR framing rule (committed strategy):**

> "Do not propose a single disease (22q11DS alone): too narrow, reads as the well-bounded problem they reject. Do not propose a vague area with no anchor. Frame as: a neuropsychiatric AREA, with 22q11DS as the Phase I/II flagship exemplar, generalizing to idiopathic schizophrenia or broader transdiagnostic psychiatry in Phase III."

### 3b. Risk statistics for 22q11DS (from schizophrenia_MONDO doc; cite Schneider et al. 2023)

| Metric | Value | Source |
|---|---|---|
| Lifetime psychosis risk (22q11DS -> schizophrenia) | ~25% (~25-fold vs. general population) | Murphy et al. 1999 *Arch Gen Psychiatry* |
| Pooled prevalence of psychotic disorders in 22q11DS | 11.50% (95% CI: 9.40-14.00%) | Schneider et al. 2023 *BJPsych* (PMID:36786112) |
| Pooled prevalence of schizophrenia specifically | 9.70% (95% CI: 6.50-14.20%) | Same meta-analysis |
| 5-year incidence of psychosis | 10.60% (95% CI: 6.60-16.70%) | Same meta-analysis |
| Relative risk (22q11DS -> schizophrenia spectrum) | ~20-25x | Bassett & Chow 1999; Murphy et al. 1999 |
| Prevalence of 22q11.2 deletion in schizophrenia cohorts | ~0.3-1% vs ~0.025% general population | Multiple GWAS/CNV studies |

### 3c. TBX1 — the causal anchor (nuanced; both evidence and caveats committed)

**TBX1 locus:** chr 22q11.21; OMIM:602054; primary causal gene for cardiovascular/pharyngeal defects of 22q11.2DS; also expressed in oligodendrocyte lineage and embryonic cortex.

**Evidence FOR TBX1 as schizophrenia model:**
- Tbx1+/- mice: reduced prepulse inhibition (PPI) — a validated schizophrenia endophenotype (Paylor et al. 2006 *PNAS* PMID:16684884)
- One human family with TBX1 frameshift mutation: psychiatric features including psychosis co-segregated without chromosomal deletion (same paper)
- Tbx1 loss in mesodermal cells disrupts corticogenesis via premature neurogenesis in somatosensory cortex anlage (Vitelli et al. 2017 *Cereb Cortex* PMID:27131548)
- Tbx1 heterozygosity in oligodendrocyte lineage specifically disrupts myelination of fimbria axons (Kim & Bhatt 2025 *bioRxiv* 2025.12.30.697076)

**Evidence AGAINST (must acknowledge in proposal):**
- TBX1 sequence variation does NOT significantly contribute to the genetic etiology of psychotic/affective disorders in the general nonsyndromic population (Funke et al. 2007 *Mol Med* PMID:17622321)
- Only rare coding variants identified; lack population frequency for statistical association
- Other 22q11 genes (DGCR8, PRODH, GNB1L, COMT) have stronger direct mechanistic links to psychosis pathways

**Verdict (from MONDO doc):** "TBX1 is a **partial model** — strong PPI endophenotype in mice; very weak evidence in nonsyndromic schizophrenia. Frame TBX1 as the primary genetic handle (the highest-penetrance single-gene lesion) in 22q11DS, not as a standalone schizophrenia gene."

**The 22q11DS causal chain we commit to formalizing:**
TBX1-COMT-DGCR8 -> cell-type pathology -> thalamocortical / fronto-temporal circuit dysfunction

**SCZD4 ontology note (from MONDO doc):** 22q11DS-associated schizophrenia maps to SCZD4 (OMIM:600850/PRODH). SCZD4 is NOT a direct child of MONDO:0005090 (schizophrenia); 22q11DS is a separate MONDO entity (MONDO:0011511, DiGeorge syndrome / velocardiofacial syndrome). Flag this in any ontology-based model.

**SCHEMA exome data (useful for the proposal genomic layer):** Singh et al. 2022 *Nat Genet* (PMID:35396579) — 24,248 cases vs 97,322 controls. Top 10 exome-wide genes (P < 2.14 x 10-6): SETD1A, CUL1, XPO7, TRIO, CACNA1G, SP4, GRIA3, GRIN2A, HERC1, RB1CC1. Key pathway clusters: glutamate signaling (GRIA3/GRIN2A/CACNA1G), chromatin (SETD1A/ASH1L/KDM6B), ubiquitin-proteasome (CUL1/HERC1).

### 3d. Phase III extension: idiopathic schizophrenia

The same framework generalizes to idiopathic schizophrenia in Phase III, satisfying IGoR's explicit second-disease generalization requirement. The schizophrenia GWAS layer (PGC), SCHEMA exome data, and the PsychENCODE multi-cohort atlas (*Science* 2024; Ruzicka, Mohammadi et al.) directly support this. Brad Ruzicka (McLean/Harvard) is the clinical/translational co-lead for this extension.

### 3e. Bipolar extension (committed cautiously)

The 22q11DS model carries bipolar disorder relevance (15-25% rate in 22q11DS). The BDNF/TrkB axes (Mood/Thought/Cognitive) and the multi-cohort bipolar paper (in progress, with McLean data under NDA; IRB via North Star) are the scientific foundation for a future extension. **Do NOT mention the in-progress bipolar paper publicly or in non-proprietary sections; it is a data/NDA study, not an IRB study.**

The teaming-page text (2026-06-06) notes: "Confirm the bipolar claim wording ('first single-cell atlases of schizophrenia and bipolar disorder') reads the way you want publicly, given the bipolar paper is still in progress."

---

## 4. TEAM CONFIGURATION

### 4a. Current prime/sub structure (decided 2026-06-03)

**Decided structure:** IPAI/Purdue = prime + PI; Cytognosis = funded sub-award (TA1/TA2 lead); Cellanome + 2nd lab = TA3/TA4.

**Rationale (committed):** "Funds still reach Cytognosis as a real sub-award (builds its record and resources the org), while Purdue's track record, infrastructure, and F&A environment carry the win."

**Reversibility note (from 2026-06-05 SS):** "If we instead submit Cytognosis-prime, only the cover page, the PI line, and the BOE shares swap; the technical content (Sections 1-3) is identical."

**Cytognosis IDs:** SAM UEI HS4PRLL7AKY5; CAGE 197W9; eRA CYTOGNOSIS; EIN 39-4383634; mailing address 394 Innisfree Dr, Daly City, CA 94015.

### 4b. Key personnel table

| Role | Person | Affiliation | Status | Notes |
|---|---|---|---|---|
| Prime PI | Ananth Grama, PhD | Purdue IPAI (Director) | Confirmed warm, not yet formally committed | Cleanest PI option; physical AI, scalable distributed computing, mechanistic modeling |
| TA1/TA2 Lead | Shahin Mohammadi, PhD | Cytognosis Foundation | Confirmed (founder/CEO) | 20 years computational biology; MIT/Kellis, Broad, insitro, GenBio AI; co-led *Science* 2024 SZ atlas; creator of ACTIONet |
| Co-Lead, Clinical/Translational | Brad Ruzicka, MD/PhD | McLean Hospital / Harvard | Confirmed (co-authored *Science* 2024 paper) | Psychiatric biobank access; 22q11DS and schizophrenia translational validation; Grant Co-Lead (replaced Jose) |
| Optical screening / validation | Anne Carpenter, PhD | Broad Institute (now); Purdue/IPAI ~Sep 2026 | Warm/prospective; dialogue active | Inventor of Cell Painting and CellProfiler; leads JUMP consortium; 2025 NeuroPainting *Nat. Commun.* paper on 22q11.2 iPSC neurons directly de-risks TA1 validation |
| TA3/TA4 Lead | Dwight Baker, SVP Product Development | Cellanome | Advancing (structure agreed, not signed; NDA sent) | R3200 platform; endorsed pooled-CRISPR-in-neuron/glia anchor; will be at Proposers' Day; calcium-imaging capability being confirmed under NDA |
| TA4 multi-omics | Adam Richardson, VP Operations | Panome Bio | Warm/prospective | CLIA-certified CRO; untargeted metabolomics, lipidomics, proteomics; orthogonal molecular readout |
| Project Manager | Patty Purcell | TBD/consultant | Availability risk (may take full-time role) | Line up a backup PM immediately |
| Software Architect | TBD (human, NOT the PI, NOT an AI agent) | TBD | KEY GAP — must name a human | ~$240K fully loaded; SOC 15-1252 |

**Anne Carpenter routing note (from Comprehensive Reference):** Broad affiliation is the near-term route (pre-Aug 6 full proposal). Purdue/IPAI affiliation lands ~Sep 2026 after the full-proposal deadline. Use Broad network for the proposal; transition to IPAI post-award.

**Transfyr (candidate, not named):** ex-ARPA-H-director founder; potential TA3/TA4 observability partner. COI check required before teaming; not named in any submission until cleared.

### 4c. Eligibility and conflict notes

**NSF citizenship rule vs ARPA-H:** NSF Senior/Key Personnel have a citizenship constraint. ARPA-H does not. The IGoR submission (ARPA-H) has no citizenship bar. This is why MH-26-140 (NIH) is designated as the parallel vehicle where Cytognosis/Shahin can be PI, and NSF X-Labs (Herve-led) has Shahin in a non-Key role. No action needed for IGoR, but document for team coordination.

**Faraz Faghri NIH 50% contractor status:** Mentioned in memory context as a constraint. Not explicitly addressed in the IGoR docs. Flag: if Faraz is being considered for IGoR, verify whether his NIH contractor status creates a conflict or effort-allocation issue.

**Anne Carpenter Broad/IPAI timing:** Carpenter's Purdue/IPAI move is not yet public as of the docs. Use Broad affiliation on proposal; add a note that she will transition to IPAI.

**Shahin's two money streams (from Strategy Master):** "Keep the two money streams clean: Shahin's IGoR effort rides the Cytognosis sub-award (paid by Cytognosis from the sub); the Purdue appointment salary rides a separate existing IPAI grant for distinct effort. Do not let one award pay the same hours twice. Structure with Duane and Ananth."

**Broad IPPIA firewall:** Shahin has a 2023-10-17 Broad IPPIA (with PEC Luria-only scope). Cytognosis work must be firewalled. Wind down Broad affiliation after the bipolar paper is published. No conflict noted specifically for IGoR, but document the firewall.

**FFRDC/government bar:** FFRDCs and government entities are barred from IGoR (prime or sub). No Cytognosis team members are at FFRDCs; no issue identified.

### 4d. Mandatory roles (IGoR requirement)

IGoR requires three named roles, all distinct people:
1. Principal Investigator (Grama or Mohammadi — not yet finalized)
2. Project Manager (Purcell or backup — availability risk)
3. Software Architect (TBD — KEY GAP; not an AI agent; must be a named human)

---

## 5. COST MODEL

### 5a. Total and split (5 years, 3 phases: 18 + 18 + 24 mo)

**Midpoint (planning, not a ceiling):** ~$30M consortium total
**Range:** $25-60M
**Comparables used:** PARADIGM ~$17M/team avg; NITRO ~$20-39M/performer

| Performer | Role | Share | 5-yr total | ~Annual |
|---|---|---|---|---|
| IPAI/Purdue (prime) | Coordination + TA1/TA2 support | ~20% | ~$6.0M | ~$1.2M |
| Cytognosis (sub) | TA1 + TA2 lead | ~45% | ~$13.5M | ~$2.5-2.7M |
| Cellanome (sub) | TA3 + TA4 | ~35% | ~$10.5M | ~$2.0-2.1M |

**Note on prime/sub order:** The 2026-06-02 SS had Cytognosis as prime (same dollar splits, different order); the 2026-06-05 SS switched to IPAI as prime. The dollar splits are identical in both versions.

**Phasing:** Phase I ~80% of steady-state (build); Phase II full (integration); Phase III heaviest (second disease + external experiments).

### 5b. Cytognosis sub-award detail (~$2.5M/yr; ~7.5 FTE)

| Role | FTE | Fully loaded | Source anchor |
|---|---|---|---|
| PI (Mohammadi), partial effort | 0.5 | ~$100K | Reasonable comp ~$200K/yr; coordinated/capped across awards |
| Software architect (TA2/integration; IGoR-required) | 1.0 | ~$240K | SOC 15-1252; San Jose median ~$180K base |
| Senior ML/AI engineer (TA2) | 1.0 | ~$260K | SOC 15-1221; Bay base $180-220K |
| ML/AI research scientist (TA1/TA2) | 1.0 | ~$240K | SOC 15-1221 |
| Computational biologists (TA1) | 2.0 | ~$420K | SOC 19-1029; Bay base $140-175K |
| Technical project manager (IGoR-required) | 1.0 | ~$200K | SOC 11-3021/15-1299 |
| Research scientist / postdoc | 1.0 | ~$110K | NIH NRSA floor + Bay premium |
| **Personnel subtotal** | ~7.5 | **~$1.57M** | |

**Other Cytognosis prime costs (annual):**
- Compute: ~$400K (TA1 training ~$250K + TA2 inference/orchestration ~$150K; H100 blended ~$2.50/GPU-hr on committed cloud)
- Other direct (travel, open-source infra/CI, data licensing, external security/audit, dev hardware): ~$200K
- Indirect at 15% de minimis MTDC rate (2 CFR 200.414(f)): ~$330K (effective ~12% after equipment + over-$50K-subaward exclusions)
- **Prime annual total: ~$2.5M**

**Compute options noted:** H100 on-demand: ~$2.99 (Lambda), ~$3.00 (GCP), ~$3.90 (AWS P5); marketplace floor ~$1.50-2.00. On-prem 8xH100 server ~$200-320K hardware; break-even vs cloud ~18 months at 50% use. Recommendation: cloud/committed for Phase I; reassess on-prem if utilization sustained.

### 5c. Cellanome sub (~$2.0M/yr; experiment-heavy)

**Per-experiment cost anchors (committed to these ranges):**
- Optical pooled screens (R3200): ~$50-500K each
- Targeted Perturb-seq: $5-30K/screen; genome-scale $50-300K
- scRNA-seq: ~$200-700/sample multiplexed
- iPSC-to-neuron differentiation: ~$3-15K/run

**Model:** ~$2M/yr for 3-5 screens + ~100 scRNA-seq samples + iPSC lines per year, scaling in Phase III. Cellanome actual per-screen pricing must be confirmed for the sub-award justification.

### 5d. Purdue/IPAI sub (~$1.2M/yr)

1-2 researchers + Grama and Carpenter effort + students. Purdue applies its negotiated F&A (~55-60% MTDC, on-campus). Covers TA1 mechanistic-modeling reinforcement and pooled-optical-screening expertise.

### 5e. Indirect rate notes

- **Cytognosis:** 15% de minimis MTDC (2 CFR 200.414(f)) is the defensible anchor. A negotiated NICRA would take 18-24 months to establish. On an OT, ARPA-H negotiates the actual rate (not bound by 2 CFR 200).
- **MTDC exclusions:** first $50K of each subaward only; amounts above excluded from prime indirect.
- Each sub applies its own rate (Purdue negotiated F&A; Cellanome G&A).

### 5f. BOE sentence (verbatim from 2026-06-05 SS)

> "A 5-year, 3-phase consortium. Cytognosis leads TA1/TA2 with ~7 FTE (PI, software architect, ML/AI engineering and science, computational biology, project manager) plus compute and the open-source release stack. Cellanome (TA3/TA4) provides R3200-based interoperable protocol execution and the experiment marketplace. Purdue/IPAI reinforces TA1 mechanistic modeling and pooled optical screening. Costs are driven by personnel and experimental throughput, ramping across phases as the second disease area and external validation come online."

---

## 6. KEY CITATIONS

### 6a. PI-authored papers (confirmed, use in team section)

| # | Citation | Role | Use |
|---|---|---|---|
| 1 | Ruzicka WB, Mohammadi S, et al. (2024). Single-cell multi-cohort dissection of the schizophrenia transcriptome. *Science*, 384(6698). | PI co-led | Primary track record; 22q11DS Phase III anchor |
| 2 | Batiuk MY, et al. (2024). Upper-layer cortical neurons drive schizophrenia-associated pathology (PsychAD). *Nat. Neurosci.*, 27, 1773-1784. | PI co-author | Second atlas; cell-type resolution |
| 3 | Mathys H, Mohammadi S, et al. (2019). Single-cell transcriptomic analysis of Alzheimer's disease. *Nature*, 570, 332-337. | PI co-author | ROSMAP atlas; demonstrates atlas-building capability |

### 6b. Partner and validation papers

| # | Citation | Use |
|---|---|---|
| 11 | Tegtmeyer M, ..., Carpenter AE, Singh S, Nehme R, et al. (2025). Combining phenomics with transcriptomics reveals cell-type-specific morphological and molecular signatures of the 22q11.2 deletion. *Nature Communications*, 16:6332. DOI: 10.1038/s41467-025-61547-x. | NeuroPainting; direct 22q11DS validation precedent for TA1/TA3 |
| 12 | Haghighi M, ..., Carpenter AE, et al. (2025). Identifying and targeting abnormal mitochondrial localization associated with psychosis. *bioRxiv* 2025.10.08.676630. | Cell Painting applied to psychosis; Carpenter TA4 precedent |

### 6c. Methods and tools (TA1/TA2)

| # | Citation | Use |
|---|---|---|
| 4 | Avsec Z, et al. / Google DeepMind (2025). AlphaGenome. github.com/google-deepmind/alphagenome. Apache-2.0 code; noncommercial weights. | TA1 sequence-to-regulatory layer |
| 5 | LLNL (2024). Open AI Co-Scientist. github.com/llnl/open-ai-co-scientist. | TA2 tournament scaffolding reference |
| 6 | Roohani Y, Huang K, Leskovec J (2024). GEARS: predicting transcriptional outcomes of multigene perturbations. *Nat. Biotechnol.*, 42, 216-228. | TA1 perturbation baseline |
| 7 | CZI Science (2024). How to build a virtual cell. *Cell*, 187. [NOTE: version conflict — see Section 8] | TA1 landscape framing |
| 8 | Replogle JM, et al. (2022). Genome-wide Perturb-seq reveals rare coding variants affecting cell fitness. *Cell*, 185(19), 3615-3632. | TA3/TA4 BOE cost anchor |
| 9 | Virtual Brain Twin Consortium (2025). virtualbraintwin.eu. | Single-scale circuit comparator for TA1 |
| 10 | Nair A, et al. (2024). 22q11.2 deletion syndrome shapes brain transcriptome and regional cell-type signatures. *Mol. Psychiatry*, 29. [NOTE: page numbers TBD — see Section 8] | 22q11DS molecular-to-brain anchor |
| — | Bereket M, Karaletsos T. (2023). Modelling cellular perturbations with the sparse additive mechanism shift VAE (SAMS-VAE). *NeurIPS*; arXiv:2311.02794. | TA1 mechanism-shift backbone |
| — | Gonzalez G, et al. (2025). Combinatorial prediction of therapeutic perturbations using causally inspired neural networks (PDGrapher). *Nat Biomed Eng*. DOI 10.1038/s41551-025-01481-x. | TA1 intervention design |
| — | Su Y, et al. (2023). CS-CORE. *Nat Commun* 14:4846. DOI 10.1038/s41467-023-40503-7. | TA1 noise-corrected co-expression decoder |
| — | Song D, et al. (2024). scDesign3 (vine copula). *Nat Biotechnol* 42:247-252. DOI 10.1038/s41587-023-01772-1. | TA1 covariance-preserving decoder |
| — | Emani PS, et al. / PsychENCODE (2024). Single-cell genomics and regulatory networks for 388 human brains (brainSCOPE GRNs). *Science* 384:eadi5199. | TA1 GRN layer |
| — | Xiong B, et al. (2024). TransBox: EL++-closed ontology embedding with box embeddings. arXiv:2410.14571. | TA1 ontology conditioning |
| — | Choi SW, et al. (2020). PRSet / PRSice-2 pathway-based polygenic scores. *GigaScience / PLoS Genet*. | Factorized-PRS precedent (proprietary section) |
| — | Lage K, et al. (2022). Cell-type-resolved interactome of autism risk genes (IGF2BP convergence; AP-MS in iNs). *Cell Genomics* 2(9):100182. | TA1 neuro-specific PPI layer |

### 6d. Disease evidence (22q11DS/schizophrenia)

| PMID / DOI | Citation | Use |
|---|---|---|
| PMID:36786112 | Schneider M et al. 2023 *BJPsych* — meta-analysis of psychosis rates in 22q11DS | ★ Best current estimate; 11.5% pooled psychosis prevalence |
| PMID:10199234 | Murphy KC et al. 1999 *Arch Gen Psychiatry* — ~30% lifetime schizophrenia | Lifetime risk quantification |
| PMID:28379838 | Vorstman JAS et al. 2017 *Nat Neurosci* | ★ Best review of 22q11->psychosis mechanisms |
| PMID:16684884 | Paylor R et al. 2006 *PNAS* | ★ Foundational TBX1 PPI deficit + human family |
| PMID:17622321 | Funke B et al. 2007 *Mol Med* | Against: no TBX1 contribution to nonsyndromic psychosis |
| PMID:35396579 | Singh et al. 2022 *Nat Genet* — SCHEMA exome analysis | Rare variant genomic layer; 10 exome-wide genes |
| bioRxiv 2025.12.30.697076 | Kim & Bhatt 2025 | New TBX1 oligodendrocyte myelination + NDD behavior |
| DOI:10.1038/s41380-022-01674-9 | Malone et al. 2022 *Mol Psychiatry* | Polygenic x 22q11 interaction |

### 6e. ARPA-H solicitation reference

| # | Citation |
|---|---|
| 13 | ARPA-H (2026). IGoR Solicitation ARPA-H-SOL-26-155, Proactive Health Office. sam.gov (opp 287ec68e). |

---

## 7. OPEN QUESTIONS AND DECISIONS

### Already decided

| Decision | Resolution | Source |
|---|---|---|
| Prime/sub structure | IPAI/Purdue prime; Cytognosis funded sub-awardee | Strategy Master 2026-06-03 |
| PI (primary) | Ananth Grama (cleanest) | Strategy Master 2026-06-03 |
| Disease area (Phase I/II) | 22q11DS as exemplar; neuropsychiatric area | Key Info + Disease Strategy |
| Disease area (Phase III) | Idiopathic schizophrenia | Committed in both SS drafts |
| TA1/TA2 lead | Cytognosis (Shahin) | All docs |
| TA3/TA4 primary partner | Cellanome (advancing; not yet signed) | Candidate Slate 2026-06-05 |
| Open-source license | Apache 2.0 code; CC BY 4.0 docs | Both SS drafts |
| Factorized-PRS | PROPRIETARY; mark pages; keep off partner materials | Methods Deep-Dive |
| NSF vs ARPA-H for Shahin as PI | ARPA-H = no citizenship bar; fine for Shahin | Strategy Master |
| U01 MH-26-140 | Defer this cycle; revisit June 2027 | Strategy Master |
| Brad = Grant Co-Lead | Confirmed; Jose replaced by Brad | Word/naming rules memory |

### Still open (must resolve before Aug 6)

| Decision | Status | Urgency |
|---|---|---|
| PI: Ananth sole PI vs Shahin co-PI | Gated on Purdue visiting-scholar appointment | HIGH — before cover page lock |
| Confirm IPAI's formal appetite to be prime | Not yet formally committed | HIGH — before Solution Summary submission Jun 25 |
| Cellanome teaming agreement signed | Structure agreed; NDA pending; calcium-imaging scope TBD | HIGH — needed for full proposal |
| Second firm TA4 lab (Panome or Carpenter) | Prospective/warm | HIGH — >=2 labs required |
| Named software architect (human, not PI, not AI) | KEY GAP | HIGH — IGoR-required |
| Backup PM (Patty availability risk) | Tier 2 not yet recruited | HIGH — IGoR-required |
| Transfyr COI check | Not resolved | Medium — before naming |
| TBX1 iPSC study: fold into IGoR or run parallel | Open | Medium — affects Phase I anchor |
| Carpenter route: Broad now vs IPAI; IGoR sub-award vs informal | Open | Medium — affects TA1 validation and BOE |
| Proposer Day attendance (Ananth, Shahin, or both) | TBD | Medium |
| Milad (ARPA-H) insider read | Email sent; awaiting follow-up | Medium |
| Shankar Subramaniam (UCSD) Wellcome role verification | Being verified | Low for IGoR; high for Wellcome Leap track |
| Bipolar paper public framing on teaming page | Flag: "first single-cell atlases of schizophrenia and bipolar disorder" — paper still in progress | Medium — teaming page live |

---

## 8. INTERNAL INCONSISTENCIES FLAGGED

### 8a. Prime/sub framing mismatch between the two SS drafts

- **2026-06-02 SS:** Cytognosis as prime; Purdue/IPAI as sub.
- **2026-06-05 SS:** IPAI/Purdue as prime; Cytognosis as funded sub-awardee.
- **Resolution:** The 2026-06-05 framing is decided (Strategy Master 2026-06-03). The 2026-06-02 draft is superseded for the prime/PI language. The technical content (Sections 1-3) is identical in both.
- **Action:** Use only the 2026-06-05 SS as the base for the full proposal. The cover page, PI line, and BOE shares must reflect IPAI-prime.

### 8b. Ref 7 ("How to build a virtual cell") — volume/page discrepancy

- 2026-06-02 SS cites: *Cell*, 189(7), 1175-1188.
- 2026-06-05 SS cites: *Cell*, 187. (No volume/pages given.)
- Both drafts flag this as "verify before submission."
- **Action:** Confirm exact citation details (author list, volume, pages, DOI) before Aug 6. The 2026-06-02 draft's specific citation (189:7) may be more complete, but it needs independent verification.

### 8c. Ref 4 (AlphaGenome) — author list and year not locked

- 2026-06-05 SS: "Avsec Z, et al. / Google DeepMind (2025)."
- 2026-06-02 SS: "Outeiral C, Strahm M, Shi J, et al. (2021; updated)."
- These are different author lists and years — likely different versions of the same resource, or one is incorrect.
- The 2026-06-05 version flags this citation explicitly: "confirm exact citation details... flagged in the prior strategy doc as needing a check."
- **Action:** Verify the correct author list, year, and DOI for AlphaGenome. The methods deep-dive only cites "AlphaGenome as a tool" without a specific citation. This must be resolved before the reference list is finalized.

### 8d. Ref 10 (Nair et al. 2024 Mol Psychiatry) — page numbers absent

- 2026-06-05 SS cites: "Nair A, et al. (2024). 22q11.2 deletion syndrome shapes brain transcriptome and regional cell-type signatures. *Molecular Psychiatry*, 29."
- 2026-06-02 SS adds: "29, 1234-1247" (but this may be placeholder).
- Both drafts flag ref 10 as needing a check.
- **Action:** Confirm volume, pages, and PMID/DOI for Nair et al. 2024 before submission.

### 8e. Ref 8 (Perturb-seq; Replogle et al.) — authorship attribution

- 2026-06-02 SS: "Zheng GXY, Terry JM, Belgrader P, et al. (Replogle et al. 2022 adapted). Genome-wide Perturb-seq reveals rare coding variants affecting cell fitness. *Cell*, 185(19), 3615-3632."
- 2026-06-05 SS: "Replogle JM, et al. (2022). Genome-wide Perturb-seq. *Cell*, 185(19), 3615-3632."
- The 2026-06-02 citation mixes Replogle and Zheng author attributions (different papers/years). The 2026-06-05 version is cleaner.
- **Action:** Use the 2026-06-05 phrasing; verify that Cell 185:19 3615-3632 is specifically Replogle et al. (first author confirmation needed).

### 8f. PM cost anchors differ slightly between documents

- 2026-06-02 SS: PM budgeted at "1.0 FTE (fully loaded approximately $200K/year)."
- Cost Breakdown 2026-06-02: PM at "~$200K; SOC 11-3021/15-1299." Consistent.
- **No inconsistency** — these match. Note: the software architect in the 2026-06-02 SS is "1.0 FTE approximately $240K/year; SOC 15-1252" which also matches the cost breakdown. Confirmed consistent.

### 8g. Phase go/no-go metrics — slight phrasing variation

- 2026-06-02 SS TA2 Phase II metric: "end-to-end cycle time <=12 weeks; knowledge generation rate at least 3x conventional."
- 2026-06-05 SS does not include the 12-week metric explicitly in TA2 Phase II go/no-go — it appears in the full-loop discussion instead.
- **Action:** Reconcile into one authoritative go/no-go table for the full proposal. The 2026-06-02 SS has more granular Phase II/III metrics.

### 8h. Faraz Faghri NIH 50% contractor status

- Referenced in memory context as a relevant constraint.
- Not addressed anywhere in the IGoR docs.
- **Action:** If Faghri is being considered for any IGoR role (TA1/TA2 personnel), verify his NIH contractor status and whether it creates effort or conflict issues. This needs to be resolved before listing personnel in the full proposal.

### 8i. "Transfyr" — COI check not resolved

- Listed as a candidate TA3/TA4 observability partner in multiple docs.
- COI check flagged as pending in every doc that mentions Transfyr.
- As of the most recent docs (2026-06-05/06), Transfyr has not been named in any submission.
- **Action:** Complete COI check before the full-proposal partner list is finalized.

### 8j. SENA-discrepancy-VAE vs SAMS-VAE positioning

- The methods deep-dive (2026-06-05) commits to SAMS-VAE (Bereket/Karaletsos 2023) as the mechanism-shift backbone.
- The standards comparison (2026-06-10) recommends SENA-discrepancy-VAE as the "current leading edge of causal + interpretable + omics."
- These are not incompatible (SENA is a different framing of causal-identifiable VAEs), but the proposal should clarify the relationship: SAMS-VAE as the mechanism-shift backbone + SENA-style causal identifiability as the design principle for the factorized-PRS extension.
- **Action:** Harmonize the TA1 methods description to acknowledge SENA-style causal identifiability without replacing the SAMS-VAE framing.

---

*This brief is current as of 2026-06-11. Re-run consolidation after any new partner agreements, citation verifications, or PI decisions. The full proposal (Aug 6) will require: confirmed Cellanome teaming agreement; named software architect; named backup PM; verified citation list (refs 4, 7, 8, 10); and confirmed Carpenter sub-award route.*

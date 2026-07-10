## 30. Our contribution: TA1 four-pillar disease-model architecture

**Core claim (committed verbatim):** "No platform integrates single-cell atlas data, perturbation modeling, causal-network inference, and circuit-level physiology into a multiscale model that updates from new experiments. That integration is our TA1."

**Unifying design principle:** Everything is represented as a *shift (delta) in pathway space relative to a dataset-specific control*. This shared representation lets cellular (induced) and clinical (natural) evidence aggregate into one causal model, and surfaces disease axes that are robust to model-system artifacts.

**Required model properties:** modular (each pillar is a separable component with a defined interface), mechanistic (typed causal edges, not correlational embeddings), multiscale (molecular to cell-type to circuit), and verifiable (hub-node predictions are falsifiable by TA4 perturbation experiments).

The four pillars flow in sequence, with Pillar 4 feeding back into Pillar 1 via new experiment data:

```
Pillar 1 (Network priors) -> Pillar 2 (Causal generative modeling)
-> Pillar 3 (Joint shift-space) -> Pillar 4 (Ontology OOD + experiment design)
-> (experiments feed back to Pillar 1)
```

---

### Pillar 1: Cell-type-aware mechanistic network

**Harmonization backbone:** The **Molecular Interaction (MI) ontology** (term MI:0190) is the unifying vocabulary. Nine major databases are harmonized into a single typed, deduplicated graph: **STRING, Reactome, Reactome FI, SIGNOR, TFLink, IntAct, BioGRID, OmniPath, and the Co-abundance Atlas**.

**Edge-type taxonomy:**

| Layer (MI top type) | Subtyping basis | Examples |
|---|---|---|
| Functional/causal (MI:2245, MI:0414) | Mechanism class | Signaling, regulatory, metabolic, PTM, epigenetic |
| Molecular/experimental (MI:0045) | Detection method | Direct vs. indirect; high vs. low throughput; physical vs. genetic |
| Predicted (MI:0063) | Data source | Co-expression, text-mining, homology |
| Phenotypic | Genetic | Genetic interactions |

**Neuro-specific layers added on top of the generic prior:**

| Layer | Method/source | Contribution |
|---|---|---|
| Cell-type-specific PPIs | Kasper Lage AP-MS in iPSC-derived neurons; IGF2BP1-3 complex (Lage et al. *Cell Genomics* 2022) | Experimentally validated, neuron-resolved physical edges |
| Cell-type GRNs | **PsychENCODE brainSCOPE** multiome GRNs (snRNA + snATAC, 24 brain cell types) + ChIP-seq (Emani et al. *Science* 2024) | Directed TF-to-target and enhancer-gene edges, cell-type-resolved |
| Cell-type co-expression | **CS-CORE** (Su et al. *Nat Commun* 2023; DOI 10.1038/s41467-023-40503-7) | Depth- and noise-corrected co-expression from scRNA-seq UMIs, used inside generative decoders |

**Coverage map (differentiating design):** We build dedicated tools to map which pathways, processes, and subnetworks each interaction type and technology covers well. This coverage map serves two functions: (a) a confidence prior during model inference, and (b) a direct driver for TA2 to propose experiments targeting under-covered regions.

**TA2 interface:** The coverage map and the set of under-constrained parameters are the primary structured outputs that Pillar 1 exposes to TA2 for value-of-information experiment selection.

---

### Pillar 2: Causal generative modeling

**Mechanism-shift backbone (committed framing):** We extend the sparse additive mechanism-shift model **SAMS-VAE** (Bereket and Karaletsos, *NeurIPS* 2023; arXiv:2311.02794). A cell's latent state is a **basal/healthy state plus sparse additive shifts**. Disease and disease-associated genetic variation enter as **extrinsic factors modeled as sparse mechanism-shifts on the intrinsic basal cell state**.

**Identifiability:** Disease-associated genetic variation is modeled as a **soft intervention** on the latent causal model of cellular biological processes. Identifiability guarantees for this framing exist under Zhang et al. (2023; arXiv:2307.06250), and the pathway-space structure follows de la Fuente et al. (SENA-discrepancy-VAE; ICLR 2025; arXiv:2506.12439).

**Covariance-preserving decoders (departure from prior art):** We replace the independent negative-binomial losses used in scVI and prior SAMS-VAE implementations with **CS-CORE-informed, vine-copula decoders** from **scDesign3** (Song et al. *Nat Biotechnol* 2024; DOI 10.1038/s41587-023-01772-1). Reconstructed cells thereby preserve real gene-gene covariance rather than treating genes as conditionally independent.

**Gene identity encoding:** Gene identity is grounded in regulatory-network topology via a co-expression-aware, perturbation-adaptive gene-identity representation developed by the team (proprietary, under review; see restricted section 32), which captures perturbation-induced functional rewiring.

**GNN-based intervention design (PDGrapher):** We adopt PDGrapher's two-phase graph neural network over the interaction network (Gonzalez et al. *Nat Biomed Eng* 2025; DOI 10.1038/s41551-025-01481-x). Phase 1 proposes perturbagens that shift a diseased state toward a healthy target (inverse design); Phase 2 predicts the response to a candidate perturbation. Interventions are represented as **edge mutilations** on the causal graph.

**AlphaGenome as a tool:** AlphaGenome (Google DeepMind, 2025; Apache-2.0 code, noncommercial weights) provides sequence-to-regulatory-grammar representations for COMT, TBX1, and DGCR8 perturbation effects encoded by causal inference over single-cell multiome data. It is used as a tool, not retrained.

**Pillar 2b is proprietary; the detailed factorization method is held internal.**

---

### Pillar 3: Joint cellular and clinical shift-space

**The failure mode we name (committed framing):** In-vitro-only programs (including prior insitro work, and current efforts at Xaira, Recursion) prioritize interventions that make disease cells look like healthy cells, then use clinical data only afterward to validate. These pipelines often cannot distinguish clinically relevant disease axes because many cellular signatures are artifacts of the model system: iPSC differentiation artifacts, missing glial-neuronal interactions, and missing systemic effects.

**Our contribution:** Every signal, whether from a patient cohort or a dish, is represented as a **shift (delta) in pathway space relative to a dataset-specific control** on both scales. That common representation lets cellular (induced) and clinical (natural) evidence aggregate and reconcile in the same causal model. Disease axes that are consistent across scales are robust to model-system artifacts and are therefore the most likely to be clinically relevant.

**Data sources contributing to both scales:**

- Cellular: TA4 iPSC-neuron Perturb-seq, Cell Painting, live-cell imaging
- Clinical: PGC schizophrenia GWAS (Trubetskoy et al. *Nature* 2022), SCHEMA rare-variant data, PsychENCODE multi-cohort atlas (Ruzicka, Mohammadi et al. *Science* 2024), Open Targets Platform (Falaguera et al. *Nat Commun* 2025)

---

### Pillar 4: Ontology-conditioned OOD generalization and experiment design

**Ontology conditioning (committed table):**

| Domain | Ontology |
|---|---|
| Disease | MONDO |
| Cell type | Cell Ontology (CL) |
| Tissue/brain region | UBERON |
| Process/pathway | Gene Ontology + Pathway Ontology (incl. GO-plus) |

Each ontology is pre-embedded with **box embeddings** using **TransBox** (Xiong et al. 2024; arXiv:2410.14571), an EL++-closed representation where subsumption is encoded as box containment so that is-a transitivity is exact. These embeddings are mapped into the model's latent space via projection heads as conditioning variables.

**Two functions of ontology conditioning:**

1. **OOD generalization:** The model reasons about unseen cell types or disorders by interpolating in ontology space with respect to the closest seen examples.
2. **Gap finding:** Under-explored ontology subtrees, where interpolation is unreliable, become high-value experiment targets for TA2.

**Fixed hypothesis template (committed phrasing):**

> "Perturbing pathway/process X will shift the disease phenotype in disease Y toward healthy by modulating Z."

Because X, Y, Z are ontology terms, each hypothesis is grounded with ontology-aware named entity recognition (spaCy, **scispaCy**, **medspaCy** for negation and context) and templated, schema-validated extraction (**Instructor** + Pydantic) to pull harmonized, ontology-aligned evidence for and against the hypothesis for the TA2 agents.

**Hub/key-node selection (how hypotheses become experiments):** We identify the hubs and key nodes (transcription factors, key signaling biomolecules) whose perturbation is predicted to modulate the largest number of downstream biomolecules in the target process. These are the highest-value experiments for shifting disease cells toward a healthy state; they are handed to TA2 as ranked experiment candidates.

**Feedback to Pillar 1:** Validated experimental data returned from TA4 flows through a structured auto-update API, performing Bayesian parameter updates, flagging newly constrained or inconsistent parameters, and emitting updated uncertainty maps. TA1 update latency target: Phase II <=24 h; Phase III <=4 h.

---

### TA1 go/no-go metrics

| Phase | Metric |
|---|---|
| Phase I | Model explains >=30% of variance in 22q11DS-specific cell-type shifts; first TA4 data return cuts parameter uncertainty >=20%; >=3 mechanistic sub-models; >=3 quantitative knowledge gaps algorithmically detected |
| Phase II | At least one prospective prediction experimentally confirmed in an independent dataset; >=10 sub-models across >=2 scales; update latency <=24 h |
| Phase III | >=15 sub-models across >=3 scales; validated novel hypotheses in both diseases; latency <=4 h; all models deposited open-access in certified executable form |

> [!NOTE]
> **Standards basis:** the representation and causal-knowledge standards behind these pillars are surveyed in section 24; the specific stack we adopt (INDRA and GO-CAM, the Disease Map to SBML-qual route, the OBO/RO/Biolink backbone, and Open Targets anchoring) is in section 35.


### 30.5 The three-latent structural causal model (Pillar 2 refinement)

Pillar 2 factorizes each cell's latent state into **three causal sets of latent variables**, which is what lets the model separate therapy from side effect:

1. **Basal state (intrinsic):** the cell's healthy, intrinsic latent state.
2. **Disease effect:** latent factors driven by disease-associated genetic variation that are **causal on the cell state** (the disease-as-perturbation operator of section 10).
3. **Treatment or intervention effect:** latent factors for an intervention that act on the cell state by **two distinct paths**, either **directly** on the cell state (an off-target or side-effect route) or **indirectly by modulating the disease effect** (the therapeutic route).

The observed cell state is generated from the basal state shifted by the disease effect and the treatment effect, with the treatment entering both directly and through the disease pathway. This makes a clinically critical distinction **identifiable**: whether a candidate intervention improves the phenotype because it **corrects the disease mechanism** or because it **independently pushes the cell state**, which separates efficacy from side-effect liability. It extends the sparse-mechanism-shift and soft-intervention identifiability basis (SAMS-VAE; Zhang et al. 2023) from one intervention type to **disease and treatment as separate, composable causal operators**, jointly constrained by perturbation data (Perturb-seq, the phenotypic-triage screen) and clinical cohorts.


### 30.6 Genomic front-end and generative core (public-level overview)

The disease model begins from **pretrained genomic foundation models** (AlphaGenome, VariantFormer, Evo 2) that embed gene bodies and regulatory regions from sequence. These embeddings are contextualized on a **gene functional network** through multiresolution graph diffusion, then factored into a small set of **interpretable, sparse disease-axis factors**. The axes condition a **compositional, multimodal conditional-flow-matching generative model** and serve as **exogenous variables of a structural causal model** that learns how the axes causally interact (the disease-effect operator of the three-latent SCM in section 30.5). The detailed method, including the factorization and the generative-model extensions, is proprietary and is documented in restricted sections 31 and 32. A potential collaboration on the sequence-to-embedding step is noted in the team tracker.

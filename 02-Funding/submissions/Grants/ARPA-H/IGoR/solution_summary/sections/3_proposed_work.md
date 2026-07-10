## 3. Proposed Work

**Final deliverable.** A closed-loop IGoR system demonstrated on schizophrenia and extended to bipolar disorder: a self-updating causal TA1 model, a TA2 engine that designs its own experiments, and TA3 and TA4 partners that execute them, reaching the 10x cycle-time target. **Phase I is anchored by a phenotypic-triage screen** that empirically selects the genetic forms and cellular phenotypes the model is built on.

### TA1, comprehensive disease models (our primary contribution; Cytognosis with IPAI)

TA1 is built in four pillars (a cell-type-aware mechanistic network, a causal generative model, a joint cellular-clinical shift-space, and ontology-conditioned experiment design). Four elements carry the depth of this proposal:

- **Paired clinical and cellular modeling.** Isogenic iPSC pairs and patient clinical cohorts are represented in **one pathway-space shift model**, so cellular and clinical evidence constrain the same disease axes and culture artifacts do not masquerade as disease signal.
- **Genomic factorization (the input building blocks).** We initialize from **pretrained genomic foundation models** (AlphaGenome, VariantFormer, Evo 2) to embed gene bodies and regulatory regions, contextualize them on a **gene functional network** through multiresolution graph diffusion, and factor the result into a small set of **sparse, interpretable, transdiagnostic disease-axis factors** that double as candidate biotypes. The detailed method is proprietary; novelty is claimed precisely against the PRSet pathway-PRS precedent.
- **Causal modeling with virtual-cell perturbation models.** A **three-latent structural causal model** separates the cell's **basal state**, the **disease effect** (causal on the cell state), and a **treatment effect** that acts either **directly** on the cell (a side-effect route) or by **modulating the disease** (the therapeutic route). This extends sparse-mechanism-shift and soft-intervention identifiability (SAMS-VAE; Zhang et al. 2023) to disease and treatment as separate, composable operators, and it makes efficacy versus side-effect liability an identifiable prediction. The disease-axis factors condition a **compositional, multimodal conditional-flow-matching generative model** and enter this structural causal model as the disease-effect operator, so the model also learns how the axes causally interact.
- **Phenotypic-triage screen (the Phase I anchor).** Across the penetrant-variant panel (the 22q11.2 deletion and TBX1, plus high-odds-ratio SCHEMA genes such as SETD1A, GRIN2A, GRIA3, and CUL1), engineered as **isogenic pairs** (a healthy line with each variant introduced by CRISPR), we measure **transcriptomic, morphological, and functional calcium-imaging** phenotypes, systematically extending the 22q11 Cell Painting precedent to select the lines and disease axes that anchor the model.

TA1 is built only by Cytognosis, IPAI, and students, to keep the mission-critical core focused.

### TA2, the New Science Engine (Cytognosis and IPAI lead)

A non-LLM-wrapper engine that interrogates the TA1 model's own uncertain parameters and conflicting edges to choose the highest-value experiment, through a hypothesis tournament, mechanistic-model-grounded planning, and test-time validation that pre-screens designs by simulation. Optional collaborators may augment the engine.

### TA3, interoperable protocols (partner in discussion)

A layered, declarative protocol stack (intent, protocol, calibration, hardware) built on open standards (the LabOP lineage) with an RFC-governed process, so an experiment transfers between laboratories as easily as a data file.

### TA4, validated laboratories (two arms; two or more laboratories)

TA4 runs two independent experimental arms that together satisfy the program's requirement for two or more validated TA4 laboratories. The **academic arm** is Matthew Tegtmeyer's lab (Purdue), which runs all wet-lab experiments: iPSC-derived NGN2 neuron disease models and multi-modal fixed-cell high-plex readouts (RNA ~350-plex, protein ~50-plex, Cell-Painting-style morphology, and in-situ CRISPR-guide sequencing). The **industry arm** is **Cellanome**, providing live-cell imaging, same-cell scRNA-seq, and pooled CRISPR on the R3200 (Perturb-LINK). The two arms are orthogonal: the academic arm is fixed-cell and very high scale; Cellanome is live-cell and temporal. This enables a **cross-arm reproducibility milestone** directly aligned with the program's concordance gates. **Anne Carpenter (IPAI/Purdue)** provides the common computational layer: interpretable morphology and cellular-imaging models (no bench) that consume readouts from both arms and bridge to TA1/TA2 analysis. Illumina adds high-throughput sequencing and Billion Cell Atlas data access.

### Milestones (phase-gated, quantitative)

| Metric | Phase I | Phase II | Phase III |
|---|---|---|---|
| Experimental cycle time | baseline established | >=4x | >=10x |
| TA1 variance explained in 22q11DS cell-type shifts | >=30% | improved over literature-only | >=2x Phase I |
| Model update latency | baseline | <=24 h | <=4 h |
| Cross-laboratory concordance | >=80% (>=2 labs) | >=90% (cross-team) | >=90% (marketplace) |
| Novel predictions experimentally confirmed | design and baseline | >=1 | both disease areas |
| Disease areas | 1 (schizophrenia) | 1 | 2nd (bipolar) |

### Alternatives and risk

We considered a foundation-model-only TA1 and rejected it as correlational and non-updating, and patient lines alone, rejected for lacking genetically matched controls, which is why we engineer isogenic pairs. The central risk, that polygenic disease resists in-dish modeling, is mitigated by **starting from penetrant forms** and by the phenotypic-triage screen that empirically selects strong-signal lines. ARPA-H expects substantial technical risk; here it is counterbalanced by transformative upside, a causal, self-updating disease model that distinguishes therapy from side effect.

## 24. Landscape: standards for disease knowledge and cellular models

> [!NOTE]
> Consolidated from two standards reviews (cellular-disease-model standards; disease-knowledge standards, causal, temporal, and omics-aware). The takeaway sharpens our thesis (section 10) and grounds the standards stack we adopt (section 35).

> [!TIP]
> **If you read one thing:** no single standard does all four of {molecular **causality**, a **disease-progression time axis**, **cell-type-resolved omics** context, and **hypothesis and gap tracking** with provenance}. The field answers with a **layered stack**, and the temporal axis is the biggest hole, which is exactly the opening our platform exploits.

### 24.1 Four jobs that get confused for one

Standard selection fails when these are conflated. Pick by the job, not the buzzword.

| Job | What it answers | Standards |
|---|---|---|
| **Quantitative dynamics** | What is the model, and how does it evolve in physical time? | SBML, CellML |
| **Simulation protocol** | How do I run and reproduce it (solver, edits, outputs)? | SED-ML (plus KiSAO, OMEX) |
| **Causal knowledge** | What is known to cause what, with evidence? | Disease Maps, GO-CAM, BioPAX, BEL, INDRA |
| **Learned statistical** | What will the cell do, predicted from data? | AI virtual cells (no declarative standard yet) |

### 24.2 The five-layer stack

Most real systems combine one item from several layers; the layers are complementary, not competing.

| Layer | Examples | Role |
|---|---|---|
| **5. Omics data and learned models** | AnnData/`.h5ad`, MuData, CZ CELLxGENE Census (~169M cells), foundation models | The data and the big predictive models |
| **4. Knowledge-omics bridge** | P-NET, KPNN, VEGA, SENA-discrepancy-VAE; GEARS; Mendelian randomization, Perturb-seq | Make symbolic knowledge constrain and interpret single-cell data |
| **3. Knowledge graphs and causal statements** | Monarch, Open Targets, PrimeKG, SPOKE, Hetionet; GO-CAM, BEL, BioPAX, INDRA/EMMAA | What causes what, with evidence |
| **2. Semantic backbone** | MIRIAM, SBO, Relation Ontology, Biolink; OBO (GO, CL, UBERON, MONDO, HPO) | So everything points at the same gene, cell, and disease |
| **1. Models and simulation** | SBML (+qual/fbc/comp/multi/spatial), CellML, SBGN, NeuroML; SED-ML, OMEX | Models you can run and reproduce |

### 24.3 Model and simulation standards (the runnable layer)

- **SBML** is the lingua franca of quantitative cell modeling (BioModels hosts ~1,100 curated models; every major simulator reads it). Its **packages** are the real power: **qual** (executable Boolean causality, the disease-map execution target), **fbc** (genome-scale metabolism), **comp** (hierarchical composition), **multi** (rule-based complexes), **spatial** (reaction-diffusion PDEs).
- **CellML** is math-agnostic and wins for electrophysiology and multi-physics organ physiology; weaker for molecular signaling because it has no biochemical vocabulary.
- **SED-ML** encodes the experiment, not the biology; its model-change elements formalize **in silico interventions** (knockouts, parameter scans), the closest the simulation ecosystem comes to a counterfactual.
- **SBGN** is the visual notation (PD, ER, AF); **NeuroML/LEMS** covers neurons to circuits.
- **Whole-cell** modeling resists single-format serialization: the Karr M. genitalium model stitched ~28 sub-models across formalisms, so whole-cell today means a **composition framework (Vivarium)** orchestrating many small standardized models, at the cost of a standard file format.

### 24.4 Executable disease knowledge: the Disease Map pattern

"DisMech" in our prior notes points at **Disease Maps**: curated, comprehensive molecular-mechanism maps of a specific disease, drawn in CellDesigner with SBGN semantics, stored as SBML plus layout, annotated via MIRIAM, and hosted on **MINERVA**. They become runnable through one canonical pipeline:

`Literature and curation -> CellDesigner map (SBGN + SBML) -> CaSQ -> SBML-qual -> MaBoSS -> time-dependent state probabilities`

**CaSQ** auto-infers a Boolean model from the curated map; **MaBoSS** simulates it into stochastic time-probability curves over disease-relevant states (for example apoptosis versus survival). This is the standards-based route from integrated knowledge to a runnable causal model with a short-timescale time axis, as demonstrated by the COVID-19 Disease Map.

### 24.5 Causal-knowledge standards (and the hypothesis-and-gap engine)

When the requirement is explicit, evidence-backed causality rather than kinetic simulation, four frameworks lead.

| Framework | Causal depth | Provenance | Gap / hypothesis support |
|---|---|---|---|
| **BioPAX L3** | activation/inhibition; no PTM type | Evidence + PMID | graph traversal for missing links |
| **BEL / CBN** | typed (directlyIncreases/Decreases) | per-statement quoted text + PMID | NPA/RCR; predecessor-less nodes = gaps |
| **GO-CAM** | very high (RO causal hierarchy, signed, mechanism-typed) | ECO code + PMID per annotation | **incomplete models explicitly flag gaps** |
| **INDRA + CoGEx + EMMAA** | very high (mechanism-typed Statements, belief scores) | full multi-source evidence per Statement | **best in class: literature surveillance, model_checker, reverse causal reasoning** |

> [!IMPORTANT]
> **INDRA/EMMAA is the closest existing thing to a standardized hypothesis-and-gap engine:** it assembles mechanism-typed statements from machine reading and databases, scores belief, continuously self-updates over new literature, and flags contradictions. This is directly relevant to **TA1 knowledge-gap identification** and **TA2 hypothesis generation** (sections 30 and 33); GO-CAM is the cleanest curated ground truth because its relation hierarchy structurally marks where mechanism is unknown.

### 24.6 The semantic backbone

Integration depends on shared identity and relation vocabularies: **MIRIAM/Bioregistry** (resolvable cross-references), **SBO** (model-element types), **Relation Ontology** (the shared causal and temporal relations, the semantic glue), **Biolink** (the KG metagraph schema with per-edge source provenance), and the **OBO Foundry** ontologies (**GO, CL, UBERON, MONDO, HPO**). CL, UBERON, and MONDO are exactly the terms the CZ CELLxGENE schema mandates, which is what lets single-cell metadata line up with mechanism knowledge.

### 24.7 Biomedical knowledge graphs

KGs give breadth and connectivity for traversal, embedding, and repurposing, but most edges are **associative, not mechanistic-causal**. Monarch (1.12M nodes), Open Targets, PrimeKG, SPOKE, Hetionet, and the Clinical Knowledge Graph differ in scale and provenance. For **causal anchoring of variants**, Open Targets (Locus-to-Gene plus GWAS fine-mapping) is strongest; for mechanism-level causality you still need GO-CAM or INDRA. KGs are the connectivity prior and candidate generator, not the mechanism ground truth.

### 24.8 The temporal and disease-progression axis (the biggest gap)

There is **no widely adopted OWL/RDF schema for disease progression** (stage ordering, stage-membership probabilities, biomarker thresholds, transition rates). MONDO, HPO, EFO, and DOID stop at age-of-onset, severity, and frequency qualifiers; RO offers a thin `precedes` vocabulary not used for clinical staging. The gap is filled by computation, not schema: **Event-Based Models** and **SuStaIn** (subtype-and-stage inference, widely used in neurodegeneration), and single-cell **pseudotime/latent-time** methods (Monocle, Palantir, scVelo, CellRank 2). Where time does live in standards: physical time in SBML/CellML, attractors in SBML-qual, MaBoSS state-time curves, and SED-ML time-course tasks.

### 24.9 The central gap, stated plainly

No single machine-readable schema integrates all four of: signed mechanism-typed **causality**; a **disease-progression time** axis as a queryable dimension; **cell-type-resolved** omics context; and automated **hypothesis generation and gap tracking** with provenance. The best available is a federated stack (section 35). A schema that unifies these is an open, fundable problem and a defensible platform thesis, and it aligns precisely with our disease-as-perturbation frame (section 10) and the IGoR mandate for self-updating causal models.

### Sources

Model and simulation: SBML L3 packages and L3V2 Core (sbml.org); SED-ML L1V5 (PMID:38613325); SBGN PD L1V2.1; CellML 2.0 (doi:10.15252/msb.20199110); NeuroML 2025 (PMC11723582); OMEX/COMBINE (PMC4272562); whole-cell and Vivarium (PMID:35134830). Disease Maps: MINERVA FAIR (bioRxiv 2024.08.28.610042); CaSQ (PMC7575051); MaBoSS/CoLoMoTo. Causal standards: GO-CAM (Nat Genet 2019, PMC7012280); INDRA, CoGEx, EMMAA (Gyori Lab). Semantic and KGs: Biolink (arXiv:2203.13906); Monarch 2024 (NAR D938); Open Targets 25.03; MONDO 2025; Cell Ontology 2025. Temporal and bridge: SuStaIn (PMC8387598); CZ CELLxGENE 2025 (NAR D886); GEARS (PMC11180609); P-NET (PMC8514339); KPNN; VEGA (doi:10.1038/s41467-021-26017-0); SENA-discrepancy-VAE (arXiv:2506.12439).

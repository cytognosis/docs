## 35. Our contribution: the IGoR standards stack

> [!NOTE]
> This is the decision that follows from the landscape in section 24: **adopt a layered, standards-grounded stack rather than a single format, and build the missing temporal-causal schema as the differentiating contribution.** Most layers are mature standards we adopt; one layer is the part worth inventing. This also supplies the open-standards substance TA3 requires.

### What we adopt, and why

| Layer | We adopt | Maps to | Why this, not the alternative |
|---|---|---|---|
| **Semantic backbone** | MIRIAM and Bioregistry; OBO (GO, **CL**, UBERON, **MONDO**, HPO); Relation Ontology; Biolink graph schema | TA1 Pillar 4 (ontology-conditioned design) | Non-negotiable for interoperability and for joining mechanism to single-cell metadata; CL, UBERON, and MONDO are the CZ CELLxGENE terms |
| **Causal mechanism** | **INDRA + CoGEx (+ EMMAA)** as the assembly and reasoning engine; **GO-CAM** as curated ground truth | TA1 Pillar 1 (network priors) and Objective 2 (gap identification); feeds TA2 | INDRA gives mechanism-typed statements, belief scores, provenance, and automated gap and hypothesis tracking, and exports to executable models; GO-CAM structurally marks gaps |
| **Executable disease model** | Disease-Map pattern: SBGN/CellDesigner to **CaSQ to SBML-qual to MaBoSS** | TA1 verifiability; TA4 readouts | The only standards-based route from integrated knowledge to a runnable causal model with stochastic state-time dynamics; deposit as OMEX |
| **Genomic causal anchor** | **Open Targets** (Locus-to-Gene, GWAS fine-mapping) and Mendelian randomization; Perturb-seq causal GRN | TA1 Pillar 2 and Pillar 2b | Grounds the map in human-genetic causality; this is where the proprietary factorization (restricted section 31) and the transdiagnostic axes attach |
| **Omics bridge** | **VEGA / SENA-discrepancy-VAE** (pathway-space, causal-identifiable latents); **GEARS** for perturbation prediction | TA1 Pillar 2 and Pillar 3 | Lets single-cell data constrain and interpret the causal map while staying interpretable; SENA-VAE is the current causal-plus-interpretable frontier |
| **Data layer** | **AnnData/MuData**, **CZ CELLxGENE Census**, scverse | TA1 ingestion; TA4 returns | Standard containers, atlas-scale corpus, ontology-conformant metadata |
| **Reproducibility** | **OMEX/COMBINE + SED-ML + KiSAO**; FAIR and Bioregistry | TA3 open layer; IV&V | One archive reproduces a model and its interventional experiments; matches our openness policy and the IV&V containerization requirement |

### The part worth inventing: a disease-progression schema

Every framework in section 24 leaves the **time and disease-progression axis** empty: there is no FAIR, queryable schema for stage ordering, stage-membership probabilities, and transition rates grounded in standard ontologies.

> [!IMPORTANT]
> **Our differentiating standardization contribution** is a thin, FAIR, **RO/MONDO/CL-grounded disease-progression schema** that links long-timescale clinical staging (SuStaIn and Event-Based Model outputs) to short-timescale mechanistic state transitions (SBML-qual and MaBoSS) and to cell-state trajectories (pseudotime, CellRank). Owning a clean schema for this missing layer is a genuine, ownable contribution that aligns with the continuous-axis, geometry-of-disease-over-time platform thesis (section 10) and gives TA3 a defensible open-standards deliverable beyond protocol execution.

### Why this strengthens the proposal

- It turns a methods survey into a **build decision**: adopt mature standards everywhere they exist, and invent only where the field is genuinely empty.
- It links the standards layer to **human-genetic causality** (Open Targets, Mendelian randomization, and the proprietary factorization), keeping a single causal spine from variant to cell state to disease stage.
- It gives **TA3** a substantive open-standards story (the progression schema plus OMEX/COMBINE reproducibility) that complements, rather than duplicates, the protocol-execution standards in section 22.

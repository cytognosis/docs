# Standards for Representing Cellular Models of Disease

**Reading time: ~9 min. If you only read one thing:** there is no single standard that "does cells." The landscape splits into four jobs that get confused for one another: **(1) quantitative dynamics** (SBML, CellML), **(2) simulation protocol** (SED-ML), **(3) causal/mechanistic knowledge** (DisMech, GO-CAM, BioPAX), and **(4) learned statistical models** (AI virtual cells). Pick by the job, not the buzzword. SBML/CellML are best for pathway-to-network scale; whole-cell and disease-causal modeling currently outrun any single declarative standard.

---

## TL;DR (BLUF)

- **SBML** = the workhorse for **biochemical reaction networks** (metabolism, signaling, gene regulation). Pathway to genome-scale. Largest tool ecosystem.
- **CellML** = general **math-markup** for any ODE/algebraic system; strongest for **multiscale physiology** (cardiac electrophysiology, the Physiome Project).
- **SED-ML** = **not a model**. It describes *how to run and reproduce* a simulation. Pairs with SBML/CellML inside a COMBINE archive.
- **DisMech** = a **disease-mechanism knowledge base** (graph + ontology, causal weighting). It is **qualitative knowledge, not simulatable dynamics**.
- **Whole-cell modeling**: no standard is sufficient alone; the field stitches multiple math formalisms together (composite/hybrid frameworks).
- **Causal models**: three different tiers exist (executable logic, causal knowledge graphs, learned causal AI). They are not interchangeable.

---

## 1. The core mental model: what is each standard actually for?

Two orthogonal axes decide everything. **What** the standard encodes, and at **what scale**.

| Standard | What it encodes | Math/representation | Simulatable? | Native scale |
|---|---|---|---|---|
| **SBML** | Biochemical reactions: species, reactions, kinetic laws, compartments | ODE / stochastic / constraint-based (FBA) / logical, via packages | **Yes** | Reaction → pathway → genome-scale network |
| **CellML** | Arbitrary systems of equations, modular components with units | ODE / DAE / algebraic (MathML) | **Yes** | Single process → multiscale organ physiology |
| **SED-ML** | The *experiment*: which model, what edits, which solver, what outputs | Procedure description (no biology) | It drives simulation; encodes none itself | Orthogonal to scale |
| **DisMech** | Disease pathophysiology: mechanism nodes, causal up/downstream links, evidence | LinkML schema + ontology graph, weighted scores | **No** (knowledge, not dynamics) | Statement → disease → cross-disease KB |

**Key distinction most people miss:** SBML and CellML answer *"what is the model?"* SED-ML answers *"how do I run it reproducibly?"* DisMech answers *"what is known about why this disease happens?"* Mixing these up is the #1 source of tool-selection error.

---

## 2. Full landscape (the named standards plus the ones you actually need)

The five you named are a slice. Here is the working set for cellular disease modeling, grouped by job.

### Tier A — Quantitative dynamics (executable mechanistic models)

| Standard | Sweet spot | Scale / # variables | Tooling |
|---|---|---|---|
| **SBML** (core + packages) | Metabolism, signaling, gene-regulatory kinetics | Kinetic: tens–hundreds of species (parameterization-limited). Constraint-based: 2,000–10,000+ reactions (genome-scale) | Largest: COPASI, Tellurium/libRoadRunner, libSBML, BioModels DB |
| **CellML** | Electrophysiology, cardiac, multiscale physiology | Tens–hundreds of variables; strong unit/dimension handling | OpenCOR, Physiome Model Repository |
| **NeuroML / LEMS** | Neurons: ion channels → cells → networks | Channel to circuit scale | jNeuroML, NEURON export |
| **BNGL / Kappa** (rule-based) | Combinatorial complexity (multisite phosphorylation, polymers) | State space can be astronomically large; rules stay compact | BioNetGen, KaSim, PySB |

### Tier B — Constraint-based and qualitative/logical

| Standard | Sweet spot | Causal? |
|---|---|---|
| **SBML-fbc** package | Genome-scale metabolic models (flux balance analysis) | Stoichiometric, not mechanistic-causal |
| **SBML-qual** package | Boolean / multivalued logical networks | **Yes — executable causal logic** |
| **GINsim / CellNOpt** formats | Logical regulatory networks fit to data | **Yes** |

### Tier C — Causal / mechanistic knowledge (qualitative, evidence-backed)

| Standard | Sweet spot | Nature |
|---|---|---|
| **DisMech** (Monarch) | Curated disease pathophysiology with provenance | Ontology graph, causal weighting, scored |
| **GO-CAM** (Gene Ontology Causal Activity Models) | "Activity A causally influences activity B" | Causal knowledge graph |
| **BioPAX** | Pathway interactions and states | Qualitative pathway knowledge |
| **SBGN** | Standardized *diagrams* of the above | Visual notation only |

### Tier D — Learned / statistical (AI virtual cells)

| Approach | Sweet spot | "Standard"? |
|---|---|---|
| **AI virtual cell** foundation models (scGPT, Geneformer, scFoundation, CZI Virtual Cell) | Predicting cell state, perturbation response from data | **No declarative standard yet.** Represented as model weights + datasets (AnnData/`.h5ad`, scverse) |

### Meta-standards (the connective tissue)

- **COMBINE archive (OMEX)**: bundles model + SED-ML + metadata into one shareable unit.
- **MIRIAM / MIASE**: minimum-information annotation and simulation-experiment rules.
- **SBOL**: genetic/synthetic-biology designs (adjacent, not cellular dynamics).

---

## 3. Whole-cell modeling vs small-scale pathway focus

**Direct answer: SBML and CellML are best for pathway-to-network scale. Neither is sufficient for true whole-cell modeling on its own.**

| Need | Best fit | Why |
|---|---|---|
| Single pathway / module kinetics | **SBML** (or CellML) | Reaction-centric, rich kinetics, best tooling |
| Genome-scale metabolism | **SBML-fbc** | Constraint-based FBA scales to thousands of reactions |
| Multiscale physiology (cell → tissue → organ) | **CellML** | General math, units, modular composition |
| Large combinatorial signaling | **BNGL / Kappa** | Rules avoid state-space blowup |
| **True whole-cell** (all processes at once) | **No single standard** | Requires *multiple math formalisms* simultaneously |

**Why whole-cell breaks the standards:** the landmark Karr 2012 *M. genitalium* whole-cell model combined ~28 sub-models in different mathematical frameworks (ODE, FBA, stochastic, Boolean). SBML/CellML each assume one formalism per model. Whole-cell modeling therefore uses **composite/hybrid frameworks** (e.g., the `wc_lang` / WC-modeling approach from the Karr lab) plus **SED-ML + COMBINE** to orchestrate and reproduce. SBML's **comp** (hierarchical composition) package helps modularize, but does not solve the multi-algorithm problem.

**Rule of thumb:**

- **Small-scale / pathway:** SBML (signaling, metabolism, gene regulation), CellML (electrophysiology).
- **Genome-scale but single-formalism:** SBML-fbc.
- **Whole-cell:** composite frameworks + orchestration standards, not a single markup.

---

## 4. Which standards for causal models?

"Causal" means three different things here. Match the tier to your actual goal.

| If you mean... | Use | Output |
|---|---|---|
| **Executable causal logic** (perturb a node, propagate effects) | **SBML-qual**, GINsim, CellNOpt; or mechanistic SBML/CellML (causal by mass-action construction) | Simulatable Boolean/kinetic predictions |
| **Causal knowledge representation** (curated "A drives B," with evidence) | **DisMech**, **GO-CAM**, BioPAX | Queryable causal graph, provenance, scoring |
| **Learned / inferred causality** (data-driven SCMs, counterfactuals) | AI causal models (no markup standard) | Learned causal graph / structural model |

**Notes that matter for disease work:**

- **DisMech is the strongest fit for disease *etiology* knowledge.** Its graph weights upstream mechanism nodes above downstream terminal nodes, which is exactly a causal-influence prior. But it is **not runnable** — you cannot simulate a perturbation in DisMech; you query and score it.
- **GO-CAM** is the cleanest pure causal-activity standard if you want machine-readable "molecular activity X causally upstream of Y."
- **Mechanistic SBML/CellML are causal by construction** (each reaction is a causal mass/flux relation), but they encode *mechanism*, not *disease narrative*.
- **Data-driven causal AI has no shared declarative standard.** This is the open gap — and the layer where a learned cellular model would live.

---

## 5. Decision cheat-sheet

```
Goal                                  -> Standard
------------------------------------- -> -----------------------------
Pathway kinetics / signaling          -> SBML
Genome-scale metabolism (FBA)         -> SBML-fbc
Cardiac / electrophysiology / organ   -> CellML
Neuron channels -> networks           -> NeuroML / LEMS
Big combinatorial signaling           -> BNGL / Kappa
Logical / executable causal network   -> SBML-qual / GINsim
Disease mechanism knowledge (causal)  -> DisMech / GO-CAM / BioPAX
Reproduce a published simulation      -> SED-ML (+ COMBINE archive)
Whole-cell (all processes)            -> Composite framework + SED-ML
Predict cell state from data          -> AI virtual cell (no standard yet)
```

---

## 6. Relevance to a learned cellular model of disease

The named standards cluster into **mechanistic-declarative** (SBML, CellML, SED-ML) and **knowledge-graph causal** (DisMech, GO-CAM, BioPAX). A modern **AI virtual cell / cellular foundation model** sits in a **third paradigm with no equivalent interchange standard** — it is shipped as weights plus `.h5ad`/scverse datasets.

The practical implication: a learned model can **consume** DisMech-style causal priors and **be validated against** SBML/CellML mechanistic models, but there is currently no declarative standard that captures a learned cellular model's structure the way SBML captures a reaction network. That absence is itself the design opportunity.

---

## Sources

- DisMech — Monarch Initiative Disease Mechanisms KB: https://github.com/monarch-initiative/dismech and LinkML registry https://linkml.io/linkml-registry/details/monarch-initiative_dismech/
- DisMech ontology scores: https://github.com/monarch-initiative/dismech-ont-scores
- "Toward community standards and software for whole-cell modeling": https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5451320/
- "Data integration strategies for whole-cell modeling": https://academic.oup.com/femsyr/article/doi/10.1093/femsyr/foae011/7636488
- VCell modeling and simulation environment (BPS2025): https://www.cell.com/biophysj/fulltext/S0006-3495(24)01534-0
- "Virtual Cells: From Conceptual Frameworks to Biomedical Applications": https://arxiv.org/html/2509.18220v1
- "AI-driven virtual cell models in preclinical research" (npj Digital Medicine, 2025): https://www.nature.com/articles/s41746-025-02198-6

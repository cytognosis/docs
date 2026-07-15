# Appendix C.2 — Task Description Document (TDD)

**Proposal title:** A Closed-Loop, Mechanistically Grounded Research Engine for Complex Neuropsychiatric Disease: Schizophrenia to Bipolar Disorder
**Prime organization:** Institute for Physical AI (IPAI), Purdue University
**Program:** ARPA-H-SOL-26-155 (Intelligent Generator of Research, IGoR), Proactive Health Office
**Award instrument:** Other Transaction
**Period of performance:** 60 months (Phase I Months 0–18; Phase II Months 18–36; Phase III Months 36–60)
**Total ARPA-H request:** ~$42,900,000 (~$43M; bottom-up planning estimate; Appendix C.4 workbook controlling)
**ARPA-H Program Manager:** Paul E. Sheehan, PhD (Proactive Health Office)
**Date of submission:** 2026-08-13 (extended from 2026-08-06)

---

## General Objective

PsychIGoR will build, validate, and openly release a closed-loop biomedical research engine for complex neuropsychiatric disease. The engine couples four Technical Areas (TAs): a mechanistic, multiscale causal disease model (TA1); a New Science Engine that designs experiments by value of information against that model (TA2); a layered, instrument-agnostic protocol stack (TA3); and a marketplace of validated laboratories that execute TA3 protocols and return model-ready data to TA1 (TA4). Phase I establishes the architecture and a walking-skeleton closed loop focused on schizophrenia, anchored by the Stage 1 phenotypic-triage screen. Phase II demonstrates cross-team interoperability and a self-updating model, anchored by Stage 2 unbiased pooled Perturb-seq. Phase III scales to a unified marketplace and extends the second disease, bipolar disorder (which shares genetic architecture and cellular biology with schizophrenia), anchored by Stage 3 targeted combinatorial perturbation.

Team PsychIGoR is uniquely constituted to bridge the clinical and cellular research traditions that are ordinarily pursued in separate organizations with different methods and literatures. The team unites world-class expertise in both the clinical dimension (Mohammadi, Ruzicka) and the cellular dimension (Tegtmeyer, Carpenter) of neuropsychiatric disease on one integrated team, and the cellular pair (Tegtmeyer and Carpenter) has already published together on exactly the iPSC-neuron phenotyping technology IGoR needs (NeuroPainting, Tegtmeyer et al. 2025).

**Human subjects:** None. All work uses (a) existing, de-identified cohort transcriptomic and genomic data governed by existing IRB approvals and NIH Genomic Data Sharing policy at the originating institutions, and (b) established or purpose-engineered iPSC lines (cell/tissue culture). No new human subjects research is conducted under this award.

**Animal subjects:** None. No vertebrate animal experiments are conducted under this award.

Every task below cross-walks to Appendix C.3. The responsible organization is named explicitly for each task. IP assertions are provided for deliverables with less than Unlimited Rights; all other deliverables carry Unlimited Rights and will be released as open-source under Apache-2.0, MIT, or BSD licenses.

---

## Task List Outline

### Phase I (Months 0–18): Concept and Component Development

- 1.1.0 TA1: Disease Model Architecture and Causal Core
  - 1.1.1 Multiscale network prior construction
  - 1.1.2 Causal generative model: basal/disease/treatment three-latent SCM
  - 1.1.3 Joint cellular-clinical shift space alignment
  - 1.1.4 Ontology-conditioned hypothesis template and gap detection
- 1.2.0 TA2: Orchestration Core and Experiment Design
  - 1.2.1 Hypothesis tournament and adversarial critic framework
  - 1.2.2 Mechanistic model-grounded RAP and value-of-information selection
  - 1.2.3 ExperimentIntent schema and TA2-TA3 interface
- 1.3.0 TA3: Protocol Schema and Calibration Artifacts (Version 1)
  - 1.3.1 Four-layer protocol stack on LabOP
  - 1.3.2 LabCapabilityProfile schema and SiLA 2 hardware integration
  - 1.3.3 One-semantic-foundation schema ratification (DDD workshop, Month 3)
- 1.4.0 TA4: Intra-Team Cell Line and Instrument Validation
  - 1.4.1 Purdue in-house iPSC-neuron (22q11.2 anchor) and Cell Painting validation
  - 1.4.2 Cellanome live-cell and Perturb-seq validation
  - 1.4.3 Illumina sequencing validation and BCA data access
- 1.5.0 Program Integration: Walking-Skeleton Closed Loop

### Phase II (Months 18–36): Integration and Interoperability

- 2.1.0 TA1: Auto-Updating Mechanistic Model
  - 2.1.1 Automated ingestion pipeline and update latency optimization
  - 2.1.2 Multi-scale model expansion and model-card documentation
  - 2.1.3 Novel prediction experimental confirmation
- 2.2.0 TA2: Multi-Backend Deployment and Usability Study
  - 2.2.1 Open-weight model backend integration
  - 2.2.2 Usability study with domain scientists
  - 2.2.3 Design-to-TA1-improvement feedback loop
- 2.3.0 TA3: RFC Governance and Cross-Team Protocol Execution
  - 2.3.1 RFC process operationalization and first two RFCs
  - 2.3.2 Cross-team protocol execution at three or more laboratories
- 2.4.0 TA4: Cross-Team Marketplace Interface and Concordance
  - 2.4.1 Marketplace request/return interface deployment
  - 2.4.2 Cross-team concordance validation
- 2.5.0 Program Integration: Interoperability Gate and Cycle-Time Milestone

### Phase III (Months 36–60): Scaling, Generalization, and Transition

- 3.1.0 TA1: Bipolar Extension and Open-Access Model Deposit
  - 3.1.1 Bipolar disorder data integration and disease axis transfer
  - 3.1.2 Scale-out to 15 or more sub-models across 3 or more scales
  - 3.1.3 Open-access certified deposit
- 3.2.0 TA2: Generalization to Bipolar and External User Study
  - 3.2.1 Bipolar experiment design and validation
  - 3.2.2 External user study (20 or more researchers)
- 3.3.0 TA3: Open Standards Engagement and Connect-a-Thon
  - 3.3.1 Open data and metadata layer delivery
  - 3.3.2 External standards body engagement
  - 3.3.3 Phase III connect-a-thon
- 3.4.0 TA4: Unified Marketplace and Autonomous Exception Handling
  - 3.4.1 Unified marketplace deployment
  - 3.4.2 Autonomous exception handling scale-up
- 3.5.0 Program Integration: Transition, Open-Access Certification, and Sustainability

---

## Per-Task Tables

### Phase I (Months 0–18)

---

| Field | Content |
|---|---|
| **Phase** | Phase I (Months 0–18) |
| **Task** | 1.1.0 |
| **Title** | TA1: Disease Model Architecture and Causal Core |
| **Objective** | Establish the computational languages, schemas, ontologies, and causal generative core that underlie all TA1 sub-models, producing a running, containerized model that ingests existing atlas data and returns experimentally testable mechanistic hypotheses. |
| **Approach / Detailed description** | Construct a multiscale interaction network harmonized on the Molecular Interaction ontology. Build the three-latent structural causal model (basal state, disease effect, treatment effect) using a covariance-preserving decoder extending SAMS-VAE. Encode disease-associated genetic variation as soft interventions. Ground gene identity in regulatory-network topology using spectral, co-expression-aware positional encoding. Deploy the PDGrapher graph neural network for intervention design. Build the joint cellular-clinical shift space so that both induced (cellular) and natural (clinical) signals are aggregated in one coordinate system. Condition all predictions on MONDO, Cell Ontology, UBERON, and Gene Ontology and express hypotheses using a fixed template. Generate a coverage map identifying under-covered pathway regions, which serves as direct input to TA2. Ingest the PsychENCODE single-cell dataset and the multi-cohort schizophrenia atlas (Ruzicka, Mohammadi et al. 2024). Initialize gene and variant representations from pretrained genomic foundation models (AlphaGenome, VariantFormer). Align cellular and clinical disease axes in residual space by optimal transport or MMD regularization. Embed OBO ontologies using TransBox EL++ with an OOD projection head for unseen entities. Apply graph-wavelet GNNs for multiresolution network diffusion. **Stage 1 experimental anchor (co-designed with TA4):** the Phase I disease-model architecture is validated by the Stage 1 phenotypic-triage screen: the SZ variant panel (22q11.2 CNVs, SCHEMA rare-coding genes, plus PsyGene/SSPsyGene-nominated genes) plus BD variants and controls, engineered as isogenic NGN2 pairs, with transcriptomic, morphological, and single-cell calcium-imaging readouts; the 5-10 genes with the most robust, reproducible phenotypic shifts versus controls become the quantitative Phase I milestones and feed TA1 disease axes directly. |
| **Location** | Cytognosis Foundation (South San Francisco, CA); IPAI/Purdue (West Lafayette, IN) |
| **Responsible organization** | Cytognosis Foundation (lead); IPAI/Purdue (co-contributor, Grama group; Anne Carpenter co-lead for computational morphology) |
| **Deliverables** | (1) Architecture document: languages, schemas, ontologies (Unlimited Rights, Apache-2.0). (2) Three or more mechanistic sub-models in containerized executable form (Unlimited Rights, Apache-2.0). (3) Coverage map identifying three or more quantitative knowledge gaps (Unlimited Rights). (4) One or more TA4 data returns ingested and model-updated (Unlimited Rights). *IP assertion: the detailed factorized-PRS axis method embedded in the causal generative core is a proprietary deliverable; it is referenced here as a marked deliverable with Limited Rights. No method detail is disclosed in this document.* |
| **Human subjects** | No. Uses existing, de-identified single-cell transcriptomic data (PsychENCODE, multi-cohort atlas) governed by originating-institution IRB and NIH GDS policy. No new human subjects research. |
| **Animal subjects** | No. |
| **Milestones** | (1) Architecture document including languages, schemas, and ontologies is completed and deposited in the program-shared repository by Month 3. (2) Three or more mechanistic sub-models pass unit tests and execute reproducibly in the IV&V containerized environment by Month 12. (3) Three or more quantitative knowledge gaps are algorithmically detected and formatted as ExperimentIntent objects passed to TA2 by Month 15. (4) One or more TA4 data returns are ingested and produce a measurable update to at least one sub-model parameter by Month 18. |

---

| Field | Content |
|---|---|
| **Phase** | Phase I (Months 0–18) |
| **Task** | 1.1.1 |
| **Title** | Multiscale network prior construction |
| **Objective** | Assemble a curated, multi-layer interaction network spanning protein-protein, signaling, regulatory, and metabolic edges with cell-type-specific coverage from PsychENCODE. |
| **Approach / Detailed description** | Integrate public interaction databases (STRING, SIGNOR, OmniPath, PsychENCODE regulatory networks) harmonized to the Molecular Interaction ontology using Biolink-compliant RDF. Apply depth-corrected co-expression from the multi-cohort atlas to weight cell-type-specific edges. Compute a coverage score per process and edge class. Export the graph in standard formats (GraphML, RDF/Turtle) with all identifiers grounded in OBO ontologies. |
| **Location** | Cytognosis Foundation (CA) |
| **Responsible organization** | Cytognosis Foundation |
| **Deliverables** | Versioned, containerized network graph with provenance (PROV-O) record (Unlimited Rights, Apache-2.0). Coverage map in machine-readable form. |
| **Human subjects** | No. |
| **Animal subjects** | No. |
| **Milestones** | (1) Network incorporating three or more edge classes and two or more cell-type-specific layers is built and passes schema validation by Month 6. (2) Coverage map reports scores for all 50 or more Gene Ontology biological processes in the GWAS-implicated gene set by Month 9. (3) Network loads and queries execute in under 60 seconds on the IV&V reference hardware by Month 12. |

---

| Field | Content |
|---|---|
| **Phase** | Phase I (Months 0–18) |
| **Task** | 1.1.2 |
| **Title** | Causal generative model: basal/disease/treatment three-latent SCM |
| **Objective** | Build and validate a structural causal model that separates basal cell state, disease effect, and treatment effect as identifiable latents, enabling mechanistic prediction of perturbation outcomes. |
| **Approach / Detailed description** | Implement the three-latent SCM as a covariance-preserving VAE extending SAMS-VAE. Train on PsychENCODE and the multi-cohort atlas with disease genotype as a soft intervention. Apply identifiability guarantees (Zhang et al. 2023). Implement the spectral, co-expression-aware positional encoding for gene identity. Integrate PDGrapher for intervention-design proposals. Validate that the disease latent axis differentiates schizophrenia from control single-cell profiles with an AUROC of 0.80 or greater. |
| **Location** | Cytognosis Foundation (CA); IPAI/Purdue (IN) |
| **Responsible organization** | Cytognosis Foundation (lead); IPAI/Purdue (co-contributor) |
| **Deliverables** | Trained model weights and training code (Unlimited Rights, Apache-2.0). Model card documenting architecture, training data, and performance metrics (Unlimited Rights). *IP assertion: the factorized-PRS axis method is a proprietary component embedded in this deliverable; Limited Rights apply to that method only.* |
| **Human subjects** | No. |
| **Animal subjects** | No. |
| **Milestones** | (1) Model trains to convergence on the multi-cohort atlas and achieves AUROC >= 0.80 for disease vs. control classification by Month 10. (2) Three or more pathway-space disease axes are extracted and annotated with their top implicated gene sets and GO processes by Month 14. (3) PDGrapher proposes three or more candidate perturbations ranked by predicted downstream effect size by Month 16. |

---

| Field | Content |
|---|---|
| **Phase** | Phase I (Months 0–18) |
| **Task** | 1.1.3 |
| **Title** | Joint cellular-clinical shift space alignment |
| **Objective** | Represent both induced (cellular perturbation) and natural (clinical cohort) signals as pathway-space shifts relative to matched controls, enabling aggregation of evidence across experimental contexts. |
| **Approach / Detailed description** | Define a shared pathway-space coordinate system. Project cellular perturbation readouts (CRISPRi/a knockdown transcriptomes) and clinical cohort data (PsychENCODE bulk and single-cell) into the same shift space. Compute pairwise alignment scores between cellular and clinical shifts. Identify pathway axes consistent across both evidence sources. |
| **Location** | Cytognosis Foundation (CA) |
| **Responsible organization** | Cytognosis Foundation |
| **Deliverables** | Joint shift-space alignment code and documentation (Unlimited Rights, Apache-2.0). Alignment score matrix for two or more pathway axes (Unlimited Rights). |
| **Human subjects** | No. Uses existing de-identified cohort data. |
| **Animal subjects** | No. |
| **Milestones** | (1) At least two pathway axes show alignment between cellular and clinical shifts with a Pearson correlation of 0.60 or greater by Month 15. (2) Alignment pipeline runs end-to-end in under two hours on a single GPU by Month 18. (3) Shift-space coordinate specification is incorporated into the TA3 semantic foundation schema by Month 18. |

---

| Field | Content |
|---|---|
| **Phase** | Phase I (Months 0–18) |
| **Task** | 1.1.4 |
| **Title** | Ontology-conditioned hypothesis template and gap detection |
| **Objective** | Produce machine-readable, ontology-grounded hypotheses from the TA1 model in a fixed template, enabling TA2 to rank and select experiments by value of information. |
| **Approach / Detailed description** | Condition model predictions on MONDO (disease), Cell Ontology (cell type), UBERON (tissue), and Gene Ontology (process). Implement the hypothesis template: "perturbing process X shifts disease Y toward healthy by modulating Z." Compute a coverage map that scores each process for evidence density. Rank candidate hub nodes by estimated downstream effect on disease-enriched processes. Format top-ranked candidates as ExperimentIntent objects for TA2. |
| **Location** | Cytognosis Foundation (CA) |
| **Responsible organization** | Cytognosis Foundation |
| **Deliverables** | Hypothesis-template schema and ExperimentIntent object specification (Unlimited Rights, Apache-2.0). Coverage map updated on every model revision (Unlimited Rights). |
| **Human subjects** | No. |
| **Animal subjects** | No. |
| **Milestones** | (1) Three or more ExperimentIntent objects are generated and formatted per the TA3 schema by Month 15. (2) Coverage map ranks 30 or more candidate processes with associated confidence scores and GWAS-locus overlap by Month 16. (3) Coverage map update is triggered automatically on each TA1 model revision and completes within one hour by Month 18. |

---

| Field | Content |
|---|---|
| **Phase** | Phase I (Months 0–18) |
| **Task** | 1.2.0 |
| **Title** | TA2: Orchestration Core and Experiment Design |
| **Objective** | Build the agentic orchestration system that transforms TA1 knowledge-gap outputs into executable ExperimentIntent objects rated high-value by domain scientists, demonstrating that the system is grounded in mechanism rather than in language-model pattern matching. |
| **Approach / Detailed description** | Implement a hypothesis tournament: competing causal-link hypotheses are evaluated by adversarial critic agents grounded in the TA1 model output and mechanistic constraints. Apply retrieval-augmented planning (RAP) where the retrieval corpus is the structured TA1 coverage map and model output, not free-text literature alone. Score experiments by a value-of-information metric computed against the TA1 uncertainty estimates. Pre-screen proposals with lightweight simulations before proposing to the researcher. Build on open, swappable agentic scaffolding (stateful agent graphs, multi-agent debate, explainable critique traces) so future model backends can be swapped. Produce explainable narratives and visualizations for every proposed experiment. Require human authorization before issuing any ExperimentIntent object to TA3. ***[SIFT-authored draft — Dan Bryce / SIFT to revise]*** SIFT contributes a scoped value-of-information planning and scheduling layer under the Cytognosis and IPAI lead, building on XPlan (DARPA SD2 lineage). From a prioritized set of TA1 knowledge gaps, XPlan develops hypotheses and identifies experimental designs to close them, expressed as ExperimentIntent objects in a new ontology layer encoding biological entities, experimental variables, measurable outcomes, and expected model updates. Agentic programming methods connect human experts with TA1 mechanistic models to collaboratively develop machine-interpretable experimental intent. Expressing intent in structured, ontology-grounded terms provides the semantic specificity to drive downstream TA3 protocol generation without ad hoc text reformatting. ***[end SIFT-authored draft]*** |
| **Location** | Cytognosis Foundation (CA); IPAI/Purdue (IN); Phylo (optional, CA) |
| **Responsible organization** | Cytognosis Foundation (lead); IPAI/Purdue (co-contributor); SIFT (scoped VOI planning layer, not TA2 co-lead); Phylo (optional, TA2 agentic add-on) |
| **Deliverables** | Orchestration architecture document and code repository (Unlimited Rights, Apache-2.0). Three or more proposed experiments with explainable narratives and human-authorization records (Unlimited Rights). TA2-TA3 interface specification (Unlimited Rights). |
| **Human subjects** | No. |
| **Animal subjects** | No. |
| **Milestones** | (1) Orchestration architecture document is reviewed at the DDD workshop and accepted by the program team by Month 3. (2) TA2-TA1 interface is demonstrated end-to-end (coverage map in, ExperimentIntent out) by Month 9. (3) Three or more experiments are proposed and executed via TA3-TA4, with 50% or more rated high-value by an independent expert panel of three or more domain scientists by Month 18. |

---

| Field | Content |
|---|---|
| **Phase** | Phase I (Months 0–18) |
| **Task** | 1.2.1 |
| **Title** | Hypothesis tournament and adversarial critic framework |
| **Objective** | Build the multi-agent debate and adversarial critic system that evaluates competing causal-link hypotheses against TA1 model constraints. |
| **Approach / Detailed description** | Implement a tournament where three or more agent instances propose and criticize alternative causal explanations for each detected knowledge gap. Critics are constrained to cite specific TA1 model edges and GWAS-locus evidence; unconstrained assertions are penalized. Track hypothesis scores across tournament rounds. Output the winning hypothesis and its supporting TA1 evidence as the ExperimentIntent rationale. |
| **Location** | Cytognosis Foundation (CA) |
| **Responsible organization** | Cytognosis Foundation |
| **Deliverables** | Adversarial critic code and tournament harness (Unlimited Rights, Apache-2.0). Critique trace logs for each proposed experiment (Unlimited Rights). |
| **Human subjects** | No. |
| **Animal subjects** | No. |
| **Milestones** | (1) Tournament completes for three or more knowledge gaps and produces ranked hypotheses with mechanistic citations by Month 12. (2) Critic agents reduce the fraction of unsupported claims in proposed rationales by 40% or more relative to an LLM-only baseline by Month 15. (3) Tournament output is formatted as a machine-readable critique trace that passes the IV&V schema validation by Month 18. |

---

| Field | Content |
|---|---|
| **Phase** | Phase I (Months 0–18) |
| **Task** | 1.2.2 |
| **Title** | Mechanistic model-grounded RAP and value-of-information selection |
| **Objective** | Select the single experiment that maximally resolves uncertainty in the TA1 model, prioritizing interventional experiments over confirmatory ones. |
| **Approach / Detailed description** | Implement a value-of-information (VOI) scorer that takes the TA1 uncertainty estimates and coverage map as inputs and returns a ranked list of candidate experiments. Apply lightweight TA1 simulation to pre-screen each candidate. Use the ranked list to filter the hypothesis-tournament output. Confirm that VOI scores correlate with post-experiment TA1 model improvement (assessed retrospectively). |
| **Location** | Cytognosis Foundation (CA); IPAI/Purdue (IN) |
| **Responsible organization** | Cytognosis Foundation (lead); IPAI/Purdue (co-contributor) |
| **Deliverables** | VOI scoring code integrated with the TA1 model API (Unlimited Rights, Apache-2.0). Ranked experiment proposals with VOI scores (Unlimited Rights). |
| **Human subjects** | No. |
| **Animal subjects** | No. |
| **Milestones** | (1) VOI scorer produces ranked experiment lists for three or more knowledge gaps by Month 12. (2) Pre-screening simulation eliminates 20% or more of proposals that would have produced null TA1 updates, validated retrospectively on at least three executed experiments, by Month 18. (3) VOI score and post-experiment TA1 update magnitude show Spearman correlation >= 0.50 across three or more Phase I experiments by Month 18. |

---

| Field | Content |
|---|---|
| **Phase** | Phase I (Months 0–18) |
| **Task** | 1.2.3 |
| **Title** | ExperimentIntent schema and TA2-TA3 interface |
| **Objective** | Define and ratify the ExperimentIntent object and its TA2-to-TA3 handoff interface so that every TA2 proposal is directly executable by TA3 without manual reformatting. |
| **Approach / Detailed description** | Author the ExperimentIntent schema in LinkML with all fields URI-bound to OBO ontologies. Required fields include: proposed perturbation (GA4GH VRS identifier or Sequence Ontology modality tag), target cell type (Cell Ontology), readout modality, VOI score, human authorization record, and a narrative rationale. Ratify the schema at the Month 3 DDD workshop. Validate that a TA3 LabOP protocol can be generated from any valid ExperimentIntent object without human reformatting. |
| **Location** | Cytognosis Foundation (CA); SIFT (TA3 counterpart) |
| **Responsible organization** | Cytognosis Foundation (lead); SIFT (interface counterpart) |
| **Deliverables** | ExperimentIntent LinkML schema, Pydantic model, and RDF serialization (Unlimited Rights, Apache-2.0). Ratified interface specification signed by both Cytognosis and SIFT leads (Unlimited Rights). |
| **Human subjects** | No. |
| **Animal subjects** | No. |
| **Milestones** | (1) ExperimentIntent schema v1.0 is ratified at the DDD workshop, Month 3. (2) Three or more valid ExperimentIntent objects are transmitted to TA3 and converted to executable LabOP protocols without manual reformatting by Month 12. (3) Schema passes IV&V schema validation with zero blocking errors by Month 18. |

---

| Field | Content |
|---|---|
| **Phase** | Phase I (Months 0–18) |
| **Task** | 1.3.0 |
| **Title** | TA3: Protocol Schema and Calibration Artifacts (Version 1) |
| **Objective** | Deliver a layered, instrument-agnostic protocol stack grounded in LabOP and the one-semantic-foundation schema, capable of expressing two or more experimental modalities and executing with comparable outcomes across two team laboratories. |
| **Approach / Detailed description** | Build the four-layer stack (Intent, Process, Calibration, Hardware). Adopt LabOP as the backbone (SIFT co-authored LabOP under DARPA SD2); add SiLA 2 at the hardware layer. Extend LabOP with three new phases (cellular model, perturbation, readout) each with a quantitative QC gate. Define calibration artifacts for each laboratory. Ratify the ExperimentIntent and LabCapabilityProfile schemas at the DDD workshop. Implement LLM-based extraction (Instructor with Pydantic; DSPy as backup) to onboard laboratories. Define the RFC governance process for locked-parameter changes. ***[SIFT-authored draft — Dan Bryce / SIFT to revise]*** TA2-TA3 interface: SIFT leads the design and implementation of the shared semantic layer encoding relationships among mechanistic disease models, knowledge gaps, experimental variables, and protocol steps, so TA2 hypothesis outputs translate into TA3 protocol specifications through structured, traceable representations rather than ad hoc text generation. LabOP already integrates ontologies for measurement units, container types, chemical entities, and biological materials; IGoR extends this with a richer knowledge-graph layer. The interface is formally specified at the Phase I DDD workshop, with explicit data models defining TA2-to-TA3 data flows, formats, and validation constraints. TA3 three-tier model: (1) UML Activity Model base providing control flow, dataflow, parameterization, and activity composition; (2) LabOP protocols above it encoding sample arrays, datasets, primitive operations, and external ontologies for measures, units, strains, chemicals, media, and containers; (3) LabOP Executions at top recording execution sequences, runtime variable bindings, datasets, and provenance per W3C PROV-O. The existing execution engine spans metadata simulation through semi-automated to fully automated, exporting machine-readable and natural-language formats for TA4 labs of varying automation sophistication. SIFT will enhance the engine to support protocol authoring against TA1 mechanistic models, expand LabOP primitive libraries for the chosen disease focus, and support IV&V bake-offs and the RFC process, contributing LabOP as the candidate program-wide protocol standard. ***[end SIFT-authored draft]*** |
| **Location** | SIFT (Arlington, VA) |
| **Responsible organization** | SIFT (lead) |
| **Deliverables** | LabOP protocol schema with perturbation-biology extensions (Unlimited Rights, Apache-2.0). Calibration artifact package for two or more laboratories (Unlimited Rights). LabCapabilityProfile schema (Unlimited Rights, Apache-2.0). RFC governance document (Unlimited Rights). |
| **Human subjects** | No. |
| **Animal subjects** | No. |
| **Milestones** | (1) ExperimentIntent and LabCapabilityProfile schemas are ratified at the DDD workshop by Month 3. (2) Two or more modalities (morphological screening, scRNA-seq library preparation) are expressed in valid LabOP protocols by Month 12. (3) The same LabOP morphological protocol is executed at both TA4 arms (Purdue/IPAI Tegtmeyer lab fixed-cell high-plex readouts and Cellanome R3200) and produces outputs within 15% coefficient of variation on three or more morphological features, analyzed by Carpenter's computational models, by Month 18. |

---

| Field | Content |
|---|---|
| **Phase** | Phase I (Months 0–18) |
| **Task** | 1.3.1 |
| **Title** | Four-layer protocol stack on LabOP |
| **Objective** | Implement the Intent, Process, Calibration, and Hardware layers with QC gates so that a failed experiment can be traced to its cause in the PROV-O provenance record. |
| **Approach / Detailed description** | Map existing LabOP primitives to the Process layer. Define new LabOP primitives for perturbation biology: InduceDifferentiation, MatureCulture (cellular model phase); DeliverGuideRNA, TreatCompound (perturbation phase); CalciumImagingAcquisition, ScRNAseqLibraryPrep, CellPaintingStain (readout phase). Attach a quantitative QC gate to each phase: cellular model (MAP2+/TUJ1+ >= 0.85, NeuN >= 0.80); perturbation (knockdown log2FC <= -1.5, activation >= 3x, viability >= 0.90); readout (genes/cell >= 1000, doublets <= 5%, stable calcium baseline). Record every execution step and QC result in PROV-O. |
| **Location** | SIFT (VA) |
| **Responsible organization** | SIFT |
| **Deliverables** | Extended LabOP library with perturbation-biology primitives (Unlimited Rights, Apache-2.0). PROV-O provenance record templates (Unlimited Rights). |
| **Human subjects** | No. |
| **Animal subjects** | No. |
| **Milestones** | (1) Six or more new LabOP primitives for perturbation biology pass unit tests by Month 9. (2) Three QC gates (cellular model, perturbation, readout) are implemented and tested against synthetic QC failure scenarios by Month 12. (3) PROV-O record captures all execution steps and QC outcomes end-to-end for two or more executed protocols by Month 18. |

---

| Field | Content |
|---|---|
| **Phase** | Phase I (Months 0–18) |
| **Task** | 1.3.2 |
| **Title** | LabCapabilityProfile schema and SiLA 2 hardware integration |
| **Objective** | Enable automatic matching of protocol hardware requirements to laboratory capabilities and auto-populate capability profiles via SiLA 2 feature discovery. |
| **Approach / Detailed description** | Author the LabCapabilityProfile schema in LinkML. Define required fields: instrument identifiers, supported modalities, QC calibration status, throughput limits, SiLA 2 Feature identifiers. Implement SiLA 2 feature-discovery auto-population for the Opentrons OT-2 and the high-content imager. Validate that a TA3 protocol-matching step can route a Cell Painting ExperimentIntent to a laboratory with confirmed Cell Painting capability without manual intervention. |
| **Location** | SIFT (VA); IPAI/Purdue (IN, instrument integration) |
| **Responsible organization** | SIFT (lead); IPAI/Purdue (instrument integration) |
| **Deliverables** | LabCapabilityProfile LinkML schema and Pydantic model (Unlimited Rights, Apache-2.0). SiLA 2 adapter for Opentrons OT-2 (Unlimited Rights, Apache-2.0). |
| **Human subjects** | No. |
| **Animal subjects** | No. |
| **Milestones** | (1) LabCapabilityProfile schema v1.0 is ratified at the DDD workshop by Month 3. (2) SiLA 2 auto-population fills the LabCapabilityProfile for two instruments without manual editing by Month 12. (3) Protocol-to-lab routing matches Cell Painting and scRNA-seq protocols to correct labs with zero routing errors across five or more test cases by Month 18. |

---

| Field | Content |
|---|---|
| **Phase** | Phase I (Months 0–18) |
| **Task** | 1.3.3 |
| **Title** | One-semantic-foundation schema ratification (DDD workshop, Month 3) |
| **Objective** | Ensure that every TA uses the same gene, variant, cell-type, and process identifiers with no translation layer between TA1, TA2, TA3, and TA4. |
| **Approach / Detailed description** | Author the canonical identifier policy in a single LinkML document: genes as Ensembl or HGNC identifiers grounded in Biolink; natural variants in GA4GH VRS and HGVS; engineered perturbations carrying locus plus Sequence Ontology modality tag; cell types in Cell Ontology; tissues in UBERON; processes in GO; diseases in MONDO. Validate the policy at the DDD workshop with representatives from all four TAs. Enforce via schema validation in CI pipelines for all four TA code repositories. |
| **Location** | SIFT (VA, lead); all TAs (reviewer) |
| **Responsible organization** | SIFT (lead); Cytognosis, IPAI/Purdue, Cellanome (reviewers) |
| **Deliverables** | One-semantic-foundation policy document and shared LinkML identifier module (Unlimited Rights, Apache-2.0). CI validation hook for all four TA repositories (Unlimited Rights). |
| **Human subjects** | No. |
| **Animal subjects** | No. |
| **Milestones** | (1) One-semantic-foundation policy is ratified by all TA leads at the DDD workshop by Month 3. (2) CI validation hook passes on all four TA repositories with zero blocking identifier-namespace errors by Month 9. (3) The same gene identifier resolves identically in the TA1 graph, the TA2 ExperimentIntent, the TA3 protocol, and the TA4 data record for three or more genes confirmed by a cross-TA integration test by Month 18. |

---

| Field | Content |
|---|---|
| **Phase** | Phase I (Months 0–18) |
| **Task** | 1.4.0 |
| **Title** | TA4: Intra-Team Cell Line and Instrument Validation (academic arm + industry arm) |
| **Objective** | Validate the Phase I cellular model anchor (22q11.2 isogenic iPSC-neuron lines) across both TA4 arms and demonstrate cross-arm reproducibility, achieving 80% or greater concordance on the same experiment run at the academic arm (Tegtmeyer/Purdue fixed-cell high-plex readouts) and the industry arm (Cellanome R3200). |
| **Approach / Detailed description** | **Stage 1 experimental anchor.** This task executes the Stage 1 phenotypic-triage screen: curated SZ variant panel (22q11.2 CNVs, SCHEMA rare-coding genes, PsyGene/SSPsyGene-nominated genes) plus BD variants and control genes, engineered as isogenic NGN2 pairs; transcriptomic, morphological, and single-cell calcium-imaging readouts; triage to the 5-10 genes with the most robust, reproducible, and prominent phenotypic shifts versus controls. The count and effect-size metrics from this triage are the quantitative Phase I milestones for TA1 and TA4. **Academic arm (Purdue, Tegtmeyer lab, Biomedical Engineering / Integrative Neuroscience):** Tegtmeyer group establishes the 22q11.2 iPSC-neuron model using the NGN2-accelerated differentiation protocol (Tegtmeyer et al. 2025) and runs fixed-cell high-plex readouts (RNA ~350-plex, protein ~50-plex, Cell-Painting-style morphology, in-situ CRISPR-guide sequencing). Carpenter group (IPAI/Purdue, no bench) validates computational morphological profiling and CellProfiler/interpretable-model feature extraction on these readouts. **Industry arm (Cellanome):** validate live-cell imaging and pooled CRISPR-seq readouts using the same 22q11.2 lines received as a cell-bank aliquot via the R3200; the Phase I functional neuronal activity readout is **single-cell calcium imaging** via the R3200, which folds into the live-cell imaging stack. **Cross-arm concordance:** both arms run the same IV&V reference morphological assay and submit quantitative QC metrics; Carpenter's computational models provide the common analysis layer that makes the two arms comparable. **Illumina:** validate NovaSeq X library quality for scRNA-seq libraries from both arms (optional in-kind). Labs declare LabCapabilityProfiles. |
| **Location** | IPAI/Purdue (IN); Cellanome (San Mateo, CA); Illumina (San Diego, CA) |
| **Responsible organization** | Purdue, Tegtmeyer lab (Biomedical Engineering / Integrative Neuroscience; iPSC-neuron + fixed-cell high-plex readouts; TA4 academic execution); IPAI/Purdue, Carpenter group (computational morphology and imaging models, no bench); Cellanome (live-cell + Perturb-seq, industry arm); Illumina (optional, sequencing) |
| **Deliverables** | Validated 22q11.2 iPSC-neuron cell bank with QC certificate (Unlimited Rights). Cell Painting workflow validation report from two laboratories (Unlimited Rights). LabCapabilityProfiles for each participating laboratory (Unlimited Rights). IV&V calibration artifact package (Unlimited Rights). |
| **Human subjects** | No. iPSC lines are established or engineered cell lines; no human subjects research. |
| **Animal subjects** | No. |
| **Milestones** | (1) 22q11.2 iPSC lines differentiate to NGN2 neurons at MAP2+/TUJ1+ >= 0.85 and NeuN >= 0.80 at IPAI/Purdue by Month 9. (2) The IV&V reference morphological assay is executed at both the academic arm (IPAI/Purdue, fixed-cell high-plex readouts) and the industry arm (Cellanome R3200), with 80% or greater cross-arm concordance (Spearman correlation >= 0.80 on 20 or more morphological features analyzed by Carpenter's computational models) by Month 15. (3) LabCapabilityProfiles for three or more instruments across two or more laboratories are submitted to the TA3 registry by Month 18. |

---

| Field | Content |
|---|---|
| **Phase** | Phase I (Months 0–18) |
| **Task** | 1.4.1 |
| **Title** | Purdue academic arm: iPSC-neuron wet-lab (22q11.2 anchor), fixed-cell high-plex readouts, and Carpenter computational validation |
| **Objective** | Stand up the Tegtmeyer iPSC-neuron disease-model wet-lab at Purdue (Biomedical Engineering / Integrative Neuroscience, distinct from IPAI), commission the fixed-cell high-plex multi-modal readout platform, and validate Carpenter's computational morphology/imaging models on the resulting data. |
| **Approach / Detailed description** | Install and commission the high-content imaging system (~$350K) and the spinning-disk confocal/calcium-imaging rig (~$275K) for Tegtmeyer's wet-lab. Install two Opentrons OT-2 liquid handlers and validate LabOP compatibility. Acquire 22q11.2 disease iPSC lines and CRISPR-corrected isogenic controls. Execute the NGN2-accelerated differentiation protocol. Run fixed-cell high-plex readouts on differentiated neurons: RNA ~350-plex, protein ~50-plex, Cell-Painting-style morphological features, and in-situ CRISPR-guide sequencing. Validate Carpenter's CellProfiler-based and interpretable morphology models on the resulting morphological features (Carpenter computational; no additional bench). Validate single-cell calcium imaging as the functional readout. Document all protocols in LabOP format. |
| **Location** | IPAI/Purdue (IN) |
| **Responsible organization** | Purdue, Tegtmeyer lab (Biomedical Engineering / Integrative Neuroscience, non-IPAI dept; wet-lab, fixed-cell high-plex readouts); IPAI/Purdue, Carpenter group (computational morphology model validation) |
| **Deliverables** | Commissioned instrument validation reports for high-content imager, confocal, OT-2 liquid handlers, and fixed-cell high-plex readout platform (Unlimited Rights). Validated 22q11.2 iPSC-NGN2 neuron protocol in LabOP format (Unlimited Rights). Computational morphological profiling validation report from Carpenter's models on fixed-cell readout data (Unlimited Rights). |
| **Human subjects** | No. |
| **Animal subjects** | No. |
| **Milestones** | (1) High-content imaging system and confocal/calcium rig are commissioned and pass vendor qualification by Month 6. (2) NGN2 differentiation protocol produces neurons with MAP2+/TUJ1+ >= 0.85 and NeuN >= 0.80 in three or more independent runs by Month 10. (3) Cell Painting morphological profiles discriminate 22q11.2 disease from isogenic control with an AUROC >= 0.80 on three or more independent wells by Month 15. |

---

| Field | Content |
|---|---|
| **Phase** | Phase I (Months 0–18) |
| **Task** | 1.4.2 |
| **Title** | Cellanome live-cell and Perturb-seq validation |
| **Objective** | Validate Cellanome's live-cell imaging and same-cell Perturb-seq readouts using the 22q11.2 iPSC-neuron lines and demonstrate concordance with the Purdue Cell Painting readout. |
| **Approach / Detailed description** | Receive 22q11.2 iPSC-neuron cell bank aliquot from Purdue. Establish the R3200 live-cell imaging protocol for neuronal morphology. Run a targeted Perturb-seq screen on three or more candidate CRISPRi targets identified by TA1. Validate that the same loci show directional transcriptional effects in Cellanome's scRNA-seq readout as in the Purdue bulk benchmarks. Submit quantitative QC metrics and LabCapabilityProfile. |
| **Location** | Cellanome (San Mateo, CA) |
| **Responsible organization** | Cellanome |
| **Deliverables** | Live-cell imaging and Perturb-seq validation report (Unlimited Rights). LabCapabilityProfile for the R3200 instrument (Unlimited Rights). Raw data deposit in program-shared repository (Unlimited Rights). |
| **Human subjects** | No. |
| **Animal subjects** | No. |
| **Milestones** | (1) Live-cell imaging protocol for iPSC-neurons is validated with three or more morphological features meeting predefined thresholds by Month 12. (2) Targeted Perturb-seq screen on three or more CRISPRi targets produces single-cell transcriptomes with median genes/cell >= 1000 and doublet rate <= 5% by Month 15. (3) Directional log2FC concordance between Cellanome scRNA-seq and Purdue bulk for three or more CRISPRi targets is >= 80% (same sign) by Month 18. |

---

| Field | Content |
|---|---|
| **Phase** | Phase I (Months 0–18) |
| **Task** | 1.4.3 |
| **Title** | Illumina sequencing validation and BCA data access |
| **Objective** | Validate NovaSeq X library quality for scRNA-seq libraries from team laboratories and establish access to the Billion Cell Atlas perturbation dataset. |
| **Approach / Detailed description** | Receive scRNA-seq libraries from IPAI/Purdue and Cellanome. Run sequencing on NovaSeq X and validate Q30 scores, mapping rates, and per-cell gene counts against the program QC thresholds. Establish a data-transfer agreement for Billion Cell Atlas perturbation data. Deposit processed count matrices in the program-shared repository in a standard format (AnnData/h5ad). |
| **Location** | Illumina (San Diego, CA) |
| **Responsible organization** | Illumina |
| **Deliverables** | Sequencing QC report for two or more library batches (Unlimited Rights). BCA data-access agreement and data-transfer documentation (Unlimited Rights). Processed count matrices in program repository (Unlimited Rights). |
| **Human subjects** | No. |
| **Animal subjects** | No. |
| **Milestones** | (1) NovaSeq X sequencing of two or more library batches achieves Q30 >= 80% and median genes/cell >= 1000 per Phase I QC thresholds by Month 15. (2) BCA data-access agreement is executed and at least one BCA dataset is deposited in the shared repository by Month 12. (3) Count matrices from two or more Phase I experiments are deposited in program repository within five business days of sequencing completion by Month 18. |

---

| Field | Content |
|---|---|
| **Phase** | Phase I (Months 0–18) |
| **Task** | 1.5.0 |
| **Title** | Program Integration: Walking-Skeleton Closed Loop |
| **Objective** | Demonstrate that the four TAs operate as a connected loop: TA2 reads TA1 knowledge gaps, produces ExperimentIntent objects, TA3 converts them to executable protocols, TA4 executes the protocols and returns data to TA1, and TA1 updates. |
| **Approach / Detailed description** | Convene the DDD workshop at kickoff (Month 1) to co-design all cross-TA interfaces and ratify the one-semantic-foundation schema. Generate shared interface specification and version it in the program repository. Containerize all TA1 artifacts for IV&V. Execute one complete closed-loop cycle within the team: TA1 detects one or more gaps, TA2 proposes and authorizes one experiment, TA3 generates a LabOP protocol, TA4 executes the protocol and returns data, and TA1 ingests and updates. Confirm that all TA1 artifacts build and execute on the IV&V reference environment. |
| **Location** | All performing organizations; DDD workshop in Washington DC or Purdue |
| **Responsible organization** | IPAI/Purdue (prime, integration lead) |
| **Deliverables** | Shared interface specification v1.0 (Unlimited Rights). Walking-skeleton demonstration report (Unlimited Rights). IV&V containerization package for TA1 (Unlimited Rights). |
| **Human subjects** | No. |
| **Animal subjects** | No. |
| **Milestones** | (1) DDD workshop is held by Month 2 and produces a ratified interface specification signed by all TA leads. (2) A complete closed-loop cycle (TA1 gap, TA2 proposal, TA3 protocol, TA4 execution, TA1 update) is demonstrated within the team by Month 18. (3) 100% of TA1 model artifacts build and execute reproducibly in the IV&V containerized environment by Month 18. |

---

### Phase II (Months 18–36)

---

| Field | Content |
|---|---|
| **Phase** | Phase II (Months 18–36) |
| **Task** | 2.1.0 |
| **Title** | TA1: Auto-Updating Mechanistic Model |
| **Objective** | Enable the TA1 model to ingest TA4 data returns automatically and update sub-model parameters with a latency of 24 hours or less, expanding to 10 or more sub-models across two or more biological scales. |
| **Approach / Detailed description** | Build an automated ingestion pipeline: TA4 data returns trigger a validation and normalization step, then a model-update step that re-trains or fine-tunes affected sub-models. Implement incremental learning to avoid full retraining on each data return. Expand the disease model from Phase I's three sub-models to ten or more, adding a second biological scale (e.g., circuit-level or pathway-network in addition to single-cell). Generate model cards for each sub-model. Confirm statistically that the updated model outperforms a literature-only model on a held-out prediction task. **Stage 2 experimental anchor:** Phase II is anchored by disease-model-specific unbiased pooled Perturb-seq in the prioritized lines from Stage 1 triage, which provides the basis for learning treatment-effect embeddings and validating therapeutic interventions in the TA1 model. |
| **Location** | Cytognosis Foundation (CA); IPAI/Purdue (IN) |
| **Responsible organization** | Cytognosis Foundation (lead); IPAI/Purdue (co-contributor; Carpenter co-lead on computational morphology sub-models) |
| **Deliverables** | Automated ingestion pipeline code (Unlimited Rights, Apache-2.0). Ten or more sub-models with model cards (Unlimited Rights). Statistically significant improvement report vs. literature-only model (Unlimited Rights). |
| **Human subjects** | No. |
| **Animal subjects** | No. |
| **Milestones** | (1) Ten or more TA4 data returns are ingested and produce measurable sub-model parameter updates by Month 27. (2) Sub-model count reaches ten or more across two or more biological scales by Month 30. (3) At least one novel TA1 prediction is confirmed via TA4 experiment by Month 33. (4) Model update latency from TA4 data receipt to updated model availability is <= 24 hours for 90% or more of ingested data returns by Month 36. |

---

| Field | Content |
|---|---|
| **Phase** | Phase II (Months 18–36) |
| **Task** | 2.1.1 |
| **Title** | Automated ingestion pipeline and update latency optimization |
| **Objective** | Build and optimize the data pipeline from TA4 data deposit to TA1 model update, achieving <= 24 h latency. |
| **Approach / Detailed description** | Implement event-driven ingestion triggered by TA4 data deposits. Validate and normalize incoming data against the one-semantic-foundation schema. Apply incremental model update. Monitor latency and alert on SLA breach. Publish a latency dashboard visible to all TA leads. |
| **Location** | Cytognosis Foundation (CA) |
| **Responsible organization** | Cytognosis Foundation |
| **Deliverables** | Ingestion pipeline code and latency dashboard (Unlimited Rights, Apache-2.0). |
| **Human subjects** | No. |
| **Animal subjects** | No. |
| **Milestones** | (1) Pipeline processes 10 or more simulated data returns without error by Month 21. (2) Median update latency falls below 24 hours on 10 or more real data returns by Month 30. (3) Latency dashboard is operational and accessible to all TA leads by Month 36. |

---

| Field | Content |
|---|---|
| **Phase** | Phase II (Months 18–36) |
| **Task** | 2.1.2 |
| **Title** | Multi-scale model expansion and model-card documentation |
| **Objective** | Expand the TA1 model to 10 or more sub-models covering two or more biological scales and document each with a machine-readable model card. |
| **Approach / Detailed description** | Add a second biological scale (synaptic/circuit-level or pathway-network) to complement the single-cell scale built in Phase I. Build sub-models for at least 10 implicated processes identified by the TA2 coverage map. Author model cards following ML model card conventions adapted for disease-biology models: training data, performance metrics, known failure modes, and update history. |
| **Location** | Cytognosis Foundation (CA); IPAI/Purdue (IN) |
| **Responsible organization** | Cytognosis Foundation (lead); IPAI/Purdue |
| **Deliverables** | Ten or more sub-models with model cards (Unlimited Rights, Apache-2.0). |
| **Human subjects** | No. |
| **Animal subjects** | No. |
| **Milestones** | (1) Five or more new sub-models are built beyond the Phase I three by Month 27. (2) Ten or more sub-models spanning two or more scales are available and versioned in the program repository by Month 33. (3) Model cards for all 10 or more sub-models pass IV&V completeness check by Month 36. |

---

| Field | Content |
|---|---|
| **Phase** | Phase II (Months 18–36) |
| **Task** | 2.1.3 |
| **Title** | Novel prediction experimental confirmation |
| **Objective** | Confirm at least one TA1 model prediction that was not derivable from published literature, via a TA4-executed experiment. |
| **Approach / Detailed description** | Identify one or more candidate predictions where TA1 model output diverges from a literature-only baseline. Propose the experiment via TA2, execute via TA3-TA4, and compare outcome to model prediction. Assess statistical significance of the confirmed prediction (p < 0.05, effect size >= 1.5x over matched control). |
| **Location** | Cytognosis Foundation (CA); IPAI/Purdue (IN); all TA4 labs |
| **Responsible organization** | Cytognosis Foundation (TA1 lead); IPAI/Purdue (TA4 execution lead) |
| **Deliverables** | Confirmed-prediction report with experimental evidence and statistical analysis (Unlimited Rights). |
| **Human subjects** | No. |
| **Animal subjects** | No. |
| **Milestones** | (1) One or more candidate non-obvious predictions are identified and formatted as ExperimentIntent objects by Month 24. (2) Experiment is executed and data returned by Month 30. (3) Confirmed prediction report with p < 0.05 and effect size >= 1.5x is completed by Month 33. |

---

| Field | Content |
|---|---|
| **Phase** | Phase II (Months 18–36) |
| **Task** | 2.2.0 |
| **Title** | TA2: Multi-Backend Deployment and Usability Study |
| **Objective** | Deploy two or more model backends including one open-weight model, demonstrate that the system is useful to domain scientists (70% or more rate it useful in a usability study), and confirm that TA2 designs lead to measurable TA1 model improvement. |
| **Approach / Detailed description** | Integrate a second model backend (an open-weight model such as Llama 3 or Mistral) into the agentic scaffolding alongside the primary frontier model, validated to produce equivalent experiment proposals. Conduct a usability study with ten or more domain scientists: provide each with a real knowledge gap and ask them to use TA2 to propose an experiment; collect structured feedback on usefulness, explainability, and trust. Demonstrate that experiments designed by TA2 in Phase II produce TA1 model improvements of a measurable magnitude relative to randomly selected experiments. |
| **Location** | Cytognosis Foundation (CA); IPAI/Purdue (IN); usability participants distributed |
| **Responsible organization** | Cytognosis Foundation (lead); IPAI/Purdue (co-contributor); Phylo (optional backend integration) |
| **Deliverables** | Multi-backend TA2 system with two or more model backends (Unlimited Rights, Apache-2.0). Usability study report with statistical summary (Unlimited Rights). Feedback on design-to-TA1-improvement linkage (Unlimited Rights). |
| **Human subjects** | No. Usability study collects professional feedback from domain scientists acting in their professional capacity; this is standard software usability evaluation and does not constitute human subjects research. |
| **Animal subjects** | No. |
| **Milestones** | (1) Second (open-weight) model backend integrated and producing equivalent experiment proposals to the primary backend on 5 or more benchmark knowledge gaps by Month 27. (2) Usability study completed with 10 or more domain scientists, 70% or more reporting the system as useful by Month 33. (3) 75% or more of TA2-proposed experiments in Phase II are rated high-value by the expert panel by Month 36. |

---

| Field | Content |
|---|---|
| **Phase** | Phase II (Months 18–36) |
| **Task** | 2.2.1 |
| **Title** | Open-weight model backend integration |
| **Objective** | Enable the TA2 agentic system to operate with an open-weight LLM backend, reducing dependency on commercial API availability. |
| **Approach / Detailed description** | Select and fine-tune or prompt-engineer an open-weight model (Llama 3, Mistral, or equivalent). Validate on a benchmark set of five or more knowledge-gap prompts against the primary backend. Deploy using open-source serving infrastructure (vLLM or equivalent). Document performance differences in the model-backend comparison report. |
| **Location** | Cytognosis Foundation (CA) |
| **Responsible organization** | Cytognosis Foundation; Phylo (optional) |
| **Deliverables** | Open-weight model integration code (Unlimited Rights, Apache-2.0). Backend comparison report (Unlimited Rights). |
| **Human subjects** | No. |
| **Animal subjects** | No. |
| **Milestones** | (1) Open-weight backend deployed and serving requests by Month 24. (2) Backend produces experiment proposals with 80% or more overlap with primary backend proposals on five benchmark knowledge gaps by Month 27. (3) Serving latency for open-weight backend is <= 2x primary backend on a standardized benchmark by Month 30. |

---

| Field | Content |
|---|---|
| **Phase** | Phase II (Months 18–36) |
| **Task** | 2.2.2 |
| **Title** | Usability study with domain scientists |
| **Objective** | Measure whether domain scientists find TA2 useful, explainable, and trustworthy at a rate of 70% or more. |
| **Approach / Detailed description** | Recruit 10 or more domain scientists (computational biologists, neuropsychiatrists, geneticists) from within the team and from partner institutions. Present each participant with a real Phase II knowledge gap. Ask them to use TA2 to propose an experiment. Collect structured responses on: usefulness (5-point Likert), explainability, and trust. Analyze results and incorporate findings into TA2 design improvements. |
| **Location** | Distributed (remote study); led by Cytognosis |
| **Responsible organization** | Cytognosis Foundation |
| **Deliverables** | Usability study design, data, and statistical summary report (Unlimited Rights). |
| **Human subjects** | No. Professional feedback from domain scientists acting in their research capacity; not human subjects research per 45 CFR 46. |
| **Animal subjects** | No. |
| **Milestones** | (1) Study design and protocol approved by program team by Month 22. (2) Study completed with 10 or more participants by Month 30. (3) 70% or more of participants rate the system useful (>= 4/5 on Likert scale) by Month 33. |

---

| Field | Content |
|---|---|
| **Phase** | Phase II (Months 18–36) |
| **Task** | 2.2.3 |
| **Title** | Design-to-TA1-improvement feedback loop |
| **Objective** | Confirm that TA2-designed experiments produce larger TA1 model improvements than randomly selected experiments. |
| **Approach / Detailed description** | Compare post-experiment TA1 parameter update magnitudes for TA2-selected versus randomly selected experiments (matched for assay type and scale). Compute mean update magnitude and 95% confidence interval for each group. Report statistical significance. |
| **Location** | Cytognosis Foundation (CA) |
| **Responsible organization** | Cytognosis Foundation |
| **Deliverables** | Feedback-loop analysis report (Unlimited Rights). |
| **Human subjects** | No. |
| **Animal subjects** | No. |
| **Milestones** | (1) Comparison dataset of 6 or more TA2-selected and 6 or more randomly selected experiments is assembled by Month 30. (2) Statistical analysis shows TA2-selected experiments produce measurably larger TA1 updates (p < 0.10 by Month 33). (3) Analysis is incorporated into the Phase II technical progress report by Month 36. |

---

| Field | Content |
|---|---|
| **Phase** | Phase II (Months 18–36) |
| **Task** | 2.3.0 |
| **Title** | TA3: RFC Governance and Cross-Team Protocol Execution |
| **Objective** | Operate the RFC process with two or more ratified RFCs and demonstrate execution of the same protocol at three or more laboratories including one cross-team laboratory, each meeting predefined reproducibility thresholds. |
| **Approach / Detailed description** | Formalize the RFC governance document. Initiate the first RFC to govern a locked parameter identified as a source of inter-laboratory variation in Phase I (e.g., iPSC culture media formulation). Process two or more RFCs through the full review cycle (propose, review, approve or reject with rationale). Execute the Cell Painting protocol and an NGN2-neuron scRNA-seq library prep protocol at three or more laboratories, including one cross-team laboratory outside the PsychIGoR team, each running three or more experiments to the predefined reproducibility thresholds. Expand to three or more modalities. |
| **Location** | SIFT (VA); IPAI/Purdue (IN); Cellanome (CA); cross-team lab (in discussion) |
| **Responsible organization** | SIFT (lead) |
| **Deliverables** | Two or more ratified RFCs with full review records (Unlimited Rights). Protocol execution reports from three or more laboratories (Unlimited Rights). Three or more modalities in the LabOP schema (Unlimited Rights). |
| **Human subjects** | No. |
| **Animal subjects** | No. |
| **Milestones** | (1) RFC process is operational with governance document signed by all TA3 participants by Month 21. (2) Two or more RFCs complete the full review cycle by Month 30. (3) The same LabOP protocol is executed at three or more laboratories including one cross-team lab, each running three or more experiments with coefficient of variation <= 20% on three or more key morphological or transcriptomic features by Month 36. |

---

| Field | Content |
|---|---|
| **Phase** | Phase II (Months 18–36) |
| **Task** | 2.3.1 |
| **Title** | RFC process operationalization and first two RFCs |
| **Objective** | Establish the RFC process as the authoritative mechanism for governed changes to locked TA3 protocol parameters. |
| **Approach / Detailed description** | Publish the RFC governance document specifying the proposal, review, comment, decision, and versioning steps. Assign SIFT as the RFC secretariat. Initiate RFC-001 for a Phase I-identified locked parameter. Initiate RFC-002 based on Phase II cross-team execution observations. Track each RFC to closure. |
| **Location** | SIFT (VA) |
| **Responsible organization** | SIFT |
| **Deliverables** | RFC governance document (Unlimited Rights). RFC-001 and RFC-002 records with rationale and decision (Unlimited Rights). |
| **Human subjects** | No. |
| **Animal subjects** | No. |
| **Milestones** | (1) RFC governance document ratified by Month 21. (2) RFC-001 completed and parameter change (or rejection with rationale) published by Month 27. (3) RFC-002 completed by Month 33. |

---

| Field | Content |
|---|---|
| **Phase** | Phase II (Months 18–36) |
| **Task** | 2.3.2 |
| **Title** | Cross-team protocol execution at three or more laboratories |
| **Objective** | Demonstrate that TA3 protocols produce reproducible outputs at laboratories outside the immediate PsychIGoR team. |
| **Approach / Detailed description** | Identify one cross-team laboratory (a laboratory from a different IGoR team or an independent academic lab). Transfer LabOP protocols and IV&V calibration artifacts. Provide remote support via the TA3 LabCapabilityProfile and RFC governance process. Execute three or more experiments at the cross-team lab and compare outputs to the IPAI/Purdue reference. |
| **Location** | SIFT (protocol support); cross-team laboratory (TBD); IPAI/Purdue (reference) |
| **Responsible organization** | SIFT (lead); cross-team laboratory |
| **Deliverables** | Cross-team execution report with reproducibility metrics (Unlimited Rights). |
| **Human subjects** | No. |
| **Animal subjects** | No. |
| **Milestones** | (1) Cross-team laboratory identified and LabCapabilityProfile submitted to TA3 registry by Month 24. (2) Three or more experiments executed at cross-team lab by Month 33. (3) Concordance between cross-team and IPAI/Purdue reference outputs is >= 90% on three or more features by Month 36, consistent with the TA4 cross-team Phase II target. |

---

| Field | Content |
|---|---|
| **Phase** | Phase II (Months 18–36) |
| **Task** | 2.4.0 |
| **Title** | TA4: Cross-Team Marketplace Interface and Concordance |
| **Objective** | Deploy the marketplace request/return interface and demonstrate cross-team experiment execution at 90% or greater concordance across three or more experiments, with exception rates reduced by 50% or more relative to Phase I. |
| **Approach / Detailed description** | Build the marketplace request interface: an API that receives an ExperimentIntent from TA2, matches it to a laboratory with the required LabCapabilityProfile, issues the TA3 protocol to that laboratory, tracks execution, and accepts the data return. Validate the interface with three or more cross-team experiments. Track exceptions (protocol deviations, QC failures, aborted runs) and measure the reduction versus Phase I. |
| **Location** | IPAI/Purdue (IN); Cellanome (CA); Illumina (CA); cross-team labs |
| **Responsible organization** | IPAI/Purdue (marketplace interface lead); Cellanome, Illumina (execution) |
| **Deliverables** | Marketplace request/return API (Unlimited Rights, Apache-2.0). Three or more cross-team experiment execution records (Unlimited Rights). Exception-rate comparison report (Unlimited Rights). |
| **Human subjects** | No. |
| **Animal subjects** | No. |
| **Milestones** | (1) Marketplace API is deployed and tested with simulated requests by Month 24. (2) Three or more cross-team experiments are ordered and executed via the marketplace API by Month 33. (3) Cross-team concordance is >= 90% on three or more experiments by Month 36. (4) Exception rate per experiment is reduced >= 50% versus Phase I baseline by Month 36. |

---

| Field | Content |
|---|---|
| **Phase** | Phase II (Months 18–36) |
| **Task** | 2.4.1 |
| **Title** | Marketplace request/return interface deployment |
| **Objective** | Build and validate the API that routes ExperimentIntent objects from TA2 to the matched laboratory and receives model-ready data returns. |
| **Approach / Detailed description** | Implement the API with endpoints for: experiment request submission, capability matching query, status tracking, and data return ingestion. Validate API against TA3 LabCapabilityProfile registry. |
| **Location** | IPAI/Purdue (IN) |
| **Responsible organization** | IPAI/Purdue |
| **Deliverables** | Marketplace API code (Unlimited Rights, Apache-2.0). API documentation (Unlimited Rights). |
| **Human subjects** | No. |
| **Animal subjects** | No. |
| **Milestones** | (1) API deployed and returns valid responses to 10 or more test requests by Month 24. (2) API integrated with TA3 LabCapabilityProfile registry and returns correct lab matches for 5 or more test protocols by Month 27. (3) API handles data return ingestion and triggers TA1 update pipeline for 3 or more real experiments by Month 36. |

---

| Field | Content |
|---|---|
| **Phase** | Phase II (Months 18–36) |
| **Task** | 2.4.2 |
| **Title** | Cross-team concordance validation |
| **Objective** | Confirm that cross-team experiments achieve >= 90% concordance, qualifying the marketplace for Phase III scale-out. Cross-arm concordance between the academic arm (Tegtmeyer/Purdue fixed-cell high-plex readouts) and the industry arm (Cellanome R3200) is computed first to establish the intra-PsychIGoR baseline. |
| **Approach / Detailed description** | Define concordance as Spearman correlation >= 0.90 on 20 or more morphological features or directional log2FC agreement on 80% or more of tested genes (scRNA-seq). First, confirm cross-arm concordance between the academic arm (Tegtmeyer fixed-cell high-plex readouts) and the industry arm (Cellanome R3200) using Carpenter's computational morphology models as the common analysis layer. Then execute three or more cross-team experiments using the same LabOP protocol. Compute concordance metrics for both intra-team cross-arm and cross-team comparisons. Report any discordant results and submit an RFC if a locked parameter is implicated. |
| **Location** | IPAI/Purdue (IN); Cellanome (CA); cross-team lab |
| **Responsible organization** | IPAI/Purdue (Tegtmeyer academic arm reference; Carpenter computational analysis); Cellanome (industry arm + cross-team execution) |
| **Deliverables** | Concordance validation report for three or more cross-team experiments (Unlimited Rights). |
| **Human subjects** | No. |
| **Animal subjects** | No. |
| **Milestones** | (1) Concordance metrics computed for all three or more cross-team experiments by Month 33. (2) Three or more of three or more experiments meet the >= 90% concordance threshold by Month 36. (3) Discordant results (if any) are documented and an RFC initiated within two weeks of identification. |

---

| Field | Content |
|---|---|
| **Phase** | Phase II (Months 18–36) |
| **Task** | 2.5.0 |
| **Title** | Program Integration: Interoperability Gate and Cycle-Time Milestone |
| **Objective** | Demonstrate a cross-team interoperability test and confirm that the experimental cycle time is at least 4x faster than the Phase I baseline. |
| **Approach / Detailed description** | Execute one or more cross-team interoperability tests: a second team's laboratory receives a PsychIGoR LabOP protocol and returns data that updates the PsychIGoR TA1 model. Measure cycle time from TA1 gap detection to model update for five or more Phase II cycles and compare to the Phase I baseline. Report the IV&V biannual review findings. |
| **Location** | All performing organizations; IV&V partner reviews |
| **Responsible organization** | IPAI/Purdue (prime, integration lead) |
| **Deliverables** | Phase II interoperability test report (Unlimited Rights). Cycle-time comparison report (Unlimited Rights). |
| **Human subjects** | No. |
| **Animal subjects** | No. |
| **Milestones** | (1) One or more successful cross-team interoperability tests completed by Month 33. (2) Median cycle time from TA1 gap detection to TA1 model update is >= 4x faster than Phase I baseline, measured over five or more Phase II cycles, by Month 36. (3) Phase II progress report is submitted to ARPA-H PM on schedule by Month 36. |

---

### Phase III (Months 36–60)

---

| Field | Content |
|---|---|
| **Phase** | Phase III (Months 36–60) |
| **Task** | 3.1.0 |
| **Title** | TA1: Bipolar Extension and Open-Access Model Deposit |
| **Objective** | Extend the TA1 model to bipolar disorder, scale to 15 or more sub-models across three or more biological scales, achieve <= 4 h update latency, and deposit all models in certified open-access executable form. |
| **Approach / Detailed description** | Integrate bipolar GWAS data (PGC BD3) and rare-variant data. Transfer schizophrenia disease axes to bipolar by mapping the shared genetic architecture and updating the shift-space alignment with bipolar cohort data (PsychENCODE supplementary releases). Build five or more additional sub-models for bipolar-specific and transdiagnostic processes, reaching 15 or more total. Add a third biological scale (e.g., circuit or systems level). Optimize update latency to <= 4 h via asynchronous model update and incremental learning. Deposit all models in Zenodo or equivalent certified repository in containerized executable form. **Stage 3 experimental anchor:** Phase III is anchored by targeted, combinatorial perturbation of pathways and processes nominated by the TA1 model and the TA2 engine; combinatorial designs are required because single-point interventions at non-hub genes are often limited by compensatory or redundant pathways, and hub-gene interventions risk broad side effects. Stage 3 perturbations are the primary experimental fuel for reaching the 10x cycle-time target and confirming novel validated hypotheses in both disease areas. |
| **Location** | Cytognosis Foundation (CA); IPAI/Purdue (IN) |
| **Responsible organization** | Cytognosis Foundation (lead); IPAI/Purdue (co-contributor; Carpenter co-lead on computational morphology) |
| **Deliverables** | Bipolar-extended TA1 model with 15 or more sub-models across three or more scales (Unlimited Rights, Apache-2.0). Open-access certified deposit with DOI (Unlimited Rights). Latency audit report (Unlimited Rights). |
| **Human subjects** | No. |
| **Animal subjects** | No. |
| **Milestones** | (1) Bipolar GWAS and cohort data integrated and bipolar-specific disease axes extracted by Month 45. (2) Sub-model count reaches 15 or more across three or more scales by Month 54. (3) Update latency is <= 4 h for 90% or more of TA4 data returns by Month 57. (4) All 15 or more models are deposited in certified open-access executable form with DOI by Month 60. |

---

| Field | Content |
|---|---|
| **Phase** | Phase III (Months 36–60) |
| **Task** | 3.1.1 |
| **Title** | Bipolar disorder data integration and disease axis transfer |
| **Objective** | Integrate bipolar genetic and transcriptomic data and demonstrate that the schizophrenia disease axes transfer with measurable alignment to bipolar axes. |
| **Approach / Detailed description** | Pull PGC BD3 GWAS summary statistics and rare-variant data. Integrate available bipolar single-cell data (PsychENCODE BD, McLean biobank where applicable under existing IRB and GDS policy). Map shared loci and pathways between schizophrenia and bipolar to identify transferable axes. Update the joint cellular-clinical shift space with bipolar evidence. |
| **Location** | Cytognosis Foundation (CA); McLean/HMS (MA, data governance) |
| **Responsible organization** | Cytognosis Foundation (lead); McLean/HMS (data governance) |
| **Deliverables** | Bipolar data integration pipeline and documentation (Unlimited Rights, Apache-2.0). Bipolar-schizophrenia axis alignment report (Unlimited Rights). |
| **Human subjects** | No. Uses existing de-identified data governed by originating-institution IRB and NIH GDS policy. |
| **Animal subjects** | No. |
| **Milestones** | (1) Bipolar GWAS data integrated and three or more shared pathway axes identified by Month 42. (2) Bipolar disease axes show Pearson correlation >= 0.60 with corresponding schizophrenia axes by Month 48. (3) Joint shift-space alignment includes bipolar cohort evidence by Month 50. |

---

| Field | Content |
|---|---|
| **Phase** | Phase III (Months 36–60) |
| **Task** | 3.1.2 |
| **Title** | Scale-out to 15 or more sub-models across three or more scales |
| **Objective** | Expand the TA1 model to cover 15 or more mechanistic sub-models spanning single-cell, pathway, and systems scales. |
| **Approach / Detailed description** | Build five or more new sub-models beyond the Phase II 10, covering bipolar-specific and transdiagnostic processes. Add the systems (circuit or network) scale as the third layer. Update model cards for all sub-models. |
| **Location** | Cytognosis Foundation (CA); IPAI/Purdue (IN) |
| **Responsible organization** | Cytognosis Foundation (lead); IPAI/Purdue |
| **Deliverables** | Fifteen or more sub-models with updated model cards (Unlimited Rights, Apache-2.0). |
| **Human subjects** | No. |
| **Animal subjects** | No. |
| **Milestones** | (1) Twelve or more sub-models available by Month 48. (2) Fifteen or more sub-models across three or more scales by Month 54. (3) All sub-models pass IV&V reproducibility check by Month 57. |

---

| Field | Content |
|---|---|
| **Phase** | Phase III (Months 36–60) |
| **Task** | 3.1.3 |
| **Title** | Open-access certified deposit |
| **Objective** | Make all TA1 model artifacts permanently accessible to the biomedical community in certified, executable, and documented form. |
| **Approach / Detailed description** | Package all 15 or more sub-models with their training code, model cards, and example inference scripts in containerized form. Deposit on Zenodo or equivalent with DOI. Register in a biomedical AI model registry (e.g., Hugging Face Hub). Submit data to dbGaP or GEO per NIH GDS policy for any derived genomic datasets. |
| **Location** | Cytognosis Foundation (CA); IPAI/Purdue (IN) |
| **Responsible organization** | Cytognosis Foundation (lead); IPAI/Purdue |
| **Deliverables** | Open-access deposit with DOI (Unlimited Rights). Data submission records for NIH GDS policy compliance (Unlimited Rights). |
| **Human subjects** | No. |
| **Animal subjects** | No. |
| **Milestones** | (1) All sub-model containers pass the IV&V reproducibility check by Month 57. (2) Deposit with DOI is live on Zenodo by Month 59. (3) Model registry entry is live with download count reported to ARPA-H PM by Month 60. |

---

| Field | Content |
|---|---|
| **Phase** | Phase III (Months 36–60) |
| **Task** | 3.2.0 |
| **Title** | TA2: Generalization to Bipolar and External User Study |
| **Objective** | Demonstrate TA2 on bipolar disorder, achieve 85% or more high-value experiment rate, and confirm utility in an external user study with 20 or more researchers, 80% or more reporting the system useful. |
| **Approach / Detailed description** | Extend TA2 to consume bipolar knowledge gaps and produce bipolar ExperimentIntent objects. Expand the user study to 20 or more researchers including external users (academic labs, clinical collaborators). Quantify design efficiency vs. a conventional baseline (time-per-hypothesis, expert rating, resulting TA1 update magnitude). |
| **Location** | Cytognosis Foundation (CA); external participants (distributed) |
| **Responsible organization** | Cytognosis Foundation (lead) |
| **Deliverables** | Bipolar TA2 extension (Unlimited Rights, Apache-2.0). External user study report (Unlimited Rights). Design efficiency report vs. conventional baseline (Unlimited Rights). |
| **Human subjects** | No. External user study is professional usability evaluation; not human subjects research. |
| **Animal subjects** | No. |
| **Milestones** | (1) Bipolar experiment design demonstrated with three or more ExperimentIntent objects by Month 48. (2) External user study completed with 20 or more researchers by Month 54. (3) 85% or more of TA2-proposed experiments rated high-value by Month 57. (4) 80% or more of external users rate the system useful by Month 57. |

---

| Field | Content |
|---|---|
| **Phase** | Phase III (Months 36–60) |
| **Task** | 3.2.1 |
| **Title** | Bipolar experiment design and validation |
| **Objective** | Extend TA2 to bipolar knowledge gaps and validate the first bipolar-specific experiment. |
| **Approach / Detailed description** | Update the TA2 retrieval corpus with bipolar TA1 coverage map. Generate three or more ExperimentIntent objects for bipolar-specific knowledge gaps. Execute via TA3-TA4 and confirm at least one non-obvious bipolar prediction. |
| **Location** | Cytognosis Foundation (CA); all TA4 labs |
| **Responsible organization** | Cytognosis Foundation |
| **Deliverables** | Bipolar ExperimentIntent objects (Unlimited Rights). Validated bipolar prediction report (Unlimited Rights). |
| **Human subjects** | No. |
| **Animal subjects** | No. |
| **Milestones** | (1) Three or more bipolar ExperimentIntent objects generated by Month 45. (2) One or more bipolar experiments executed via TA4 by Month 51. (3) At least one novel validated bipolar hypothesis confirmed (p < 0.05) by Month 57. |

---

| Field | Content |
|---|---|
| **Phase** | Phase III (Months 36–60) |
| **Task** | 3.2.2 |
| **Title** | External user study (20 or more researchers) |
| **Objective** | Confirm that the TA2 system is useful and trusted by a diverse cohort of external researchers at a rate of 80% or more. |
| **Approach / Detailed description** | Recruit 20 or more researchers including external users (academic labs, clinical researchers, and representatives from Phase III partner laboratories not on the team). Provide standardized knowledge-gap prompts for both schizophrenia and bipolar disorder. Collect structured usability feedback. Analyze and report disaggregated by disease and user type. |
| **Location** | Distributed; led by Cytognosis |
| **Responsible organization** | Cytognosis Foundation |
| **Deliverables** | External user study data and statistical report (Unlimited Rights). |
| **Human subjects** | No. Professional usability evaluation. |
| **Animal subjects** | No. |
| **Milestones** | (1) Recruitment of 20 or more researchers confirmed by Month 45. (2) Study completed and data collected by Month 51. (3) 80% or more of participants report the system as useful (>= 4/5 Likert) by Month 54. |

---

| Field | Content |
|---|---|
| **Phase** | Phase III (Months 36–60) |
| **Task** | 3.3.0 |
| **Title** | TA3: Open Standards Engagement and Connect-a-Thon |
| **Objective** | Deliver the open data and metadata layer, engage one or more external standards bodies, execute protocols at five or more laboratories across teams, support four or more modalities, and complete the Phase III connect-a-thon interoperability demonstration. |
| **Approach / Detailed description** | Develop the open data and metadata layer: machine-readable metadata companion to all deposited data, aligned with FAIR principles and the one-semantic-foundation schema. Engage one or more external standards body (SLAS Technology, SiLA Consortium, or an instrument manufacturer) to propose adoption of LabOP perturbation-biology extensions. Execute protocols at five or more laboratories across multiple IGoR teams in preparation for the connect-a-thon. Organize and execute the Phase III connect-a-thon: laboratories from two or more IGoR teams exchange LabOP protocols and demonstrate interoperability. |
| **Location** | SIFT (VA); all participating laboratories |
| **Responsible organization** | SIFT (lead) |
| **Deliverables** | Open data and metadata layer specification (Unlimited Rights, Apache-2.0). Standards body engagement report (Unlimited Rights). Connect-a-thon execution report with interoperability metrics (Unlimited Rights). |
| **Human subjects** | No. |
| **Animal subjects** | No. |
| **Milestones** | (1) Open data and metadata layer specification published by Month 48. (2) Engagement with one or more external standards body initiated by Month 48. (3) Protocols run at five or more laboratories across two or more IGoR teams by Month 54. (4) Four or more modalities supported by Month 54. (5) Connect-a-thon completed and interoperability demonstrated between two or more IGoR teams by Month 57. |

---

| Field | Content |
|---|---|
| **Phase** | Phase III (Months 36–60) |
| **Task** | 3.3.1 |
| **Title** | Open data and metadata layer delivery |
| **Objective** | Deliver a FAIR-aligned, machine-readable metadata companion for all program-deposited data, aligned with the TA3 one-semantic-foundation schema. |
| **Approach / Detailed description** | Define the metadata schema in LinkML. Require all TA4 data deposits to include a companion metadata record. Publish schema and example records. |
| **Location** | SIFT (VA) |
| **Responsible organization** | SIFT |
| **Deliverables** | Open metadata schema and documentation (Unlimited Rights, Apache-2.0). |
| **Human subjects** | No. |
| **Animal subjects** | No. |
| **Milestones** | (1) Schema published and adopted by all team labs by Month 45. (2) 100% of Phase III data deposits include a valid metadata record by Month 54. (3) Schema passes FAIR maturity assessment at level 2 or above by Month 57. |

---

| Field | Content |
|---|---|
| **Phase** | Phase III (Months 36–60) |
| **Task** | 3.3.2 |
| **Title** | External standards body engagement |
| **Objective** | Submit LabOP perturbation-biology extensions to one or more external standards bodies for adoption consideration. |
| **Approach / Detailed description** | Identify the most appropriate standards body (SLAS Technology, SiLA Consortium, LabOP/PAML standards group, or an Illumina instrument standards working group). Draft a standards proposal or extension specification. Submit and track the proposal status. |
| **Location** | SIFT (VA) |
| **Responsible organization** | SIFT |
| **Deliverables** | Standards proposal submitted to one or more external bodies (Unlimited Rights). Engagement status report (Unlimited Rights). |
| **Human subjects** | No. |
| **Animal subjects** | No. |
| **Milestones** | (1) External standards body identified and engagement initiated by Month 42. (2) Standards proposal or extension specification submitted by Month 51. (3) Engagement status report (acknowledgment, review, or adoption) submitted to ARPA-H PM by Month 57. |

---

| Field | Content |
|---|---|
| **Phase** | Phase III (Months 36–60) |
| **Task** | 3.3.3 |
| **Title** | Phase III connect-a-thon |
| **Objective** | Demonstrate that LabOP protocols from PsychIGoR execute successfully at a laboratory on a different IGoR team and vice versa, confirming program-level interoperability. |
| **Approach / Detailed description** | Coordinate with the ARPA-H PM and at least one other IGoR team. Exchange LabOP protocol packages with LabCapabilityProfiles. Execute one or more cross-team protocols at each team's laboratory. Document outcomes against the IV&V concordance thresholds. |
| **Location** | IPAI/Purdue (IN); partner IGoR team laboratory (TBD) |
| **Responsible organization** | SIFT (protocol coordination); IPAI/Purdue (execution host) |
| **Deliverables** | Connect-a-thon interoperability report (Unlimited Rights). |
| **Human subjects** | No. |
| **Animal subjects** | No. |
| **Milestones** | (1) Connect-a-thon partner laboratory(ies) identified and Associate Performer Agreement(s) executed by Month 42. (2) Protocol exchange completed and remote execution attempted by Month 54. (3) Interoperability demonstrated with concordance >= 80% on three or more features at the partner lab by Month 57. |

---

| Field | Content |
|---|---|
| **Phase** | Phase III (Months 36–60) |
| **Task** | 3.4.0 |
| **Title** | TA4: Unified Marketplace and Autonomous Exception Handling |
| **Objective** | Deploy the unified marketplace accepting experiment orders from any qualified researcher, achieve >= 90% concordance across the marketplace, and handle >= 70% of protocol exceptions autonomously. |
| **Approach / Detailed description** | Extend the Phase II marketplace API to a unified interface accepting requests from external researchers with Associate Performer Agreements. Publish laboratory capability manifests and onboarding documentation. Implement automated exception-handling logic for the top exception classes identified in Phases I and II (reagent QC failures, instrument calibration drift, cell viability below threshold). Track the fraction of exceptions handled without human escalation. |
| **Location** | IPAI/Purdue (IN); Cellanome (CA); Illumina (CA); external labs |
| **Responsible organization** | IPAI/Purdue (marketplace lead); Cellanome, Illumina (execution) |
| **Deliverables** | Unified marketplace API and onboarding documentation (Unlimited Rights, Apache-2.0). Public capability manifests for all participating laboratories (Unlimited Rights). Exception-handling automation code (Unlimited Rights). |
| **Human subjects** | No. |
| **Animal subjects** | No. |
| **Milestones** | (1) Unified marketplace accepts external researcher orders by Month 48. (2) Marketplace concordance is >= 90% across experiments ordered via the marketplace by Month 54. (3) 70% or more of protocol exceptions are handled autonomously without human escalation by Month 57. (4) Experiments from at least two disease indications are executed via the marketplace by Month 60. |

---

| Field | Content |
|---|---|
| **Phase** | Phase III (Months 36–60) |
| **Task** | 3.4.1 |
| **Title** | Unified marketplace deployment |
| **Objective** | Open the marketplace to external researchers and publish laboratory capability manifests. |
| **Approach / Detailed description** | Extend the API authentication and authorization layer to support external users with Associate Performer Agreements. Publish capability manifests for all participating laboratories. Provide onboarding documentation and a self-service capability-match query. |
| **Location** | IPAI/Purdue (IN) |
| **Responsible organization** | IPAI/Purdue |
| **Deliverables** | External-user marketplace API and onboarding documentation (Unlimited Rights, Apache-2.0). Capability manifests for three or more laboratories (Unlimited Rights). |
| **Human subjects** | No. |
| **Animal subjects** | No. |
| **Milestones** | (1) External-user authentication deployed and tested by Month 45. (2) Capability manifests for three or more labs published by Month 48. (3) First external researcher order received and executed by Month 51. |

---

| Field | Content |
|---|---|
| **Phase** | Phase III (Months 36–60) |
| **Task** | 3.4.2 |
| **Title** | Autonomous exception handling scale-up |
| **Objective** | Automate the handling of the top protocol exception classes, reducing the fraction requiring human escalation to 30% or fewer. |
| **Approach / Detailed description** | Analyze Phase I and II exception logs to identify the top five exception classes. Implement automated exception-resolution logic for each class (reagent substitution, instrument recalibration trigger, repeat-run authorization). Test on historical exceptions. Deploy in production. |
| **Location** | IPAI/Purdue (IN); SIFT (VA, protocol logic) |
| **Responsible organization** | IPAI/Purdue (lead); SIFT (protocol logic) |
| **Deliverables** | Exception-handling automation code (Unlimited Rights, Apache-2.0). Exception-rate reduction report (Unlimited Rights). |
| **Human subjects** | No. |
| **Animal subjects** | No. |
| **Milestones** | (1) Top five exception classes identified from Phase I and II logs by Month 39. (2) Automated handling logic deployed for three or more exception classes by Month 48. (3) 70% or more exceptions handled autonomously by Month 57. |

---

| Field | Content |
|---|---|
| **Phase** | Phase III (Months 36–60) |
| **Task** | 3.5.0 |
| **Title** | Program Integration: Transition, Open-Access Certification, and Sustainability |
| **Objective** | Complete the program deliverables, confirm that at least one external researcher uses the IGoR end-to-end, and demonstrate a >= 10x cycle-time improvement over the Phase I baseline. |
| **Approach / Detailed description** | Execute the transition plan: transfer stewardship of the open-source repositories to Cytognosis as the nonprofit steward; finalize at least one sustained partnership or adoption path (public-private marketplace partnership, academic consortium, or philanthropic continuation). Certify all artifacts as open-access in a recognized repository. Measure cycle time for five or more Phase III experiments and compare to the Phase I baseline. Report to ARPA-H PM. |
| **Location** | All performing organizations |
| **Responsible organization** | IPAI/Purdue (prime, integration lead); Cytognosis Foundation (open-source steward) |
| **Deliverables** | Transition plan and stewardship transfer record (Unlimited Rights). At least one sustained partnership agreement or adoption-path documentation (Unlimited Rights). Cycle-time comparison report (Unlimited Rights). Final open-access certification (Unlimited Rights). |
| **Human subjects** | No. |
| **Animal subjects** | No. |
| **Milestones** | (1) Transition plan is submitted to ARPA-H PM by Month 54. (2) At least one external researcher uses the IGoR end-to-end (gap to experiment to TA1 update) by Month 57. (3) Cycle-time comparison report demonstrates >= 10x improvement over Phase I baseline across five or more Phase III experiments by Month 57. (4) All program artifacts are certified open-access with DOIs and deposited by Month 60. |

---

## Cross-Walk Note

Every task and milestone above maps to Appendix C.3 (Price Proposal) as follows: Phase I tasks (1.1.0–1.5.0) map to the Phase I cost columns in Table 1-A and Table 6-A; Phase II tasks (2.1.0–2.5.0) map to Phase II columns; Phase III tasks (3.1.0–3.5.0) map to Phase III columns. Labor, equipment, materials, travel, and ODC lines in C.3 are organized by the same Phase-and-TA structure used here. The Appendix C.4 workbook provides per-task cost detail. Any IP assertion in the deliverables column of this document is reflected in the C.3 narrative under the relevant organization's cost entry.

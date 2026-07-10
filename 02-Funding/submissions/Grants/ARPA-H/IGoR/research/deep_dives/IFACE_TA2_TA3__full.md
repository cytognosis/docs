# TA2-to-TA3 Interface: Experiment-Intent Specification and Protocol Compilation

**Document class:** Internal, journal-grade deep dive. Proprietary content excluded. Do not distribute.
**Prepared:** 2026-06-14
**Feeds:** IGoR full proposal (Appendix C.1, C.2, C.4), Phase I Domain-Driven Design workshop, and the SIFT subaward scope of work.
**Reading time:** approximately 20 minutes.
**If you read one section:** read Section 3 (the interface contract and experiment-intent object) and Section 4 (the planning-to-protocol bridge). Everything else provides context and rigor.

> [!CAUTION]
> Restricted sections (31, 32, 41) of the Research Master are referenced here only structurally. Their technical content does not appear in this document. The factorized-PRS (Section 31) and the perturbation model under review (Section 32) are cited as "our perturbation model (restricted section 32)" and "our causal factorization (restricted section 31)" respectively.

---

## Abstract

The ARPA-H IGoR solicitation requires that TA2's New Science Engine produce, and TA3's interoperable protocol stack consume, a formally specified experiment intent, the structured representation of what a proposed experiment must do, without specifying how any particular instrument accomplishes it. This interface is the program's most critical seam: it is where the Bayesian value-of-information reasoning of the science engine becomes an executable, instrument-agnostic protocol that can run across heterogeneous laboratories and return provenance-linked data to the TA1 model update loop.

This document characterizes the interface contract between TA2 and TA3. It defines the six required fields of the experiment-intent object (cell type, time frame, stimuli, response, phenotype, quality requirements), specifies how those fields map onto the LabOP intent layer and protocol primitives, and traces the end-to-end pipeline from SIFT's Bayesian value-of-information ranking through hierarchical experiment planning to LabOP specialization for physical execution. It then assesses what is fully automatable with existing tooling, what requires new LabOP primitives or planner extensions, and what remains technically unclear. The recommended interface format is a LinkML-grounded schema cross-referenced to Cell Ontology, Gene Ontology, MONDO, and SBOL3 terms, ratifiable at the Phase I Domain-Driven Design workshop. This schema constitutes a concrete and fundable TA3 deliverable, and it is the shortest path from the existing TA2 and TA3 component capabilities to the Phase I walking-skeleton milestone.

---

## 1. Context: What the Interface Must Connect

### 1.1 The TA2 output: a ranked, mechanistically grounded experiment proposal

TA2's New Science Engine (Section 33 of the Research Master; detailed in `TA2_science_engine__full.md`) produces ranked experiment proposals through three coupled components: a hypothesis tournament grounded in the TA1 causal model's constraint set; mechanistic-model-grounded retrieval-augmented planning (MM-RAP), which queries the TA1 model's structured uncertainty output rather than a paper corpus; and test-time validation scaling, which pre-screens proposals against the causal graph and TA4 laboratory capability manifests before surfacing them for human authorization.

The output of the science engine is a ranked hypothesis accompanied by an experiment specification sufficient to generate a protocol. The IGoR Appendix A Program and Technical Description requires that this specification include: (1) the target cell type, (2) the experimental time frame, (3) the stimuli or perturbation type, (4) the expected or desired response, and (5) the phenotype to be measured. The sixth required element, quality requirements, is implied by the TA3 calibration layer and the concordance gating thresholds stated in Phase I and Phase II milestones.

The SIFT planning stack (Goldman, Trivedi, Bryce, AAAI Fall Symposium; Kuter, Goldman, Bryce, Beal, 2018; Bryce et al., ACS Synthetic Biology, 2022) adds two functions above the experiment specification: it converts the ranked specification into a scheduled, resource-allocated experiment plan, and it compiles that plan to a LabOP protocol appropriate to the available TA4 laboratory. These two functions, plan compilation and protocol specialization, are the technical content of the TA2-to-TA3 handoff.

### 1.2 The TA3 input: the LabOP intent layer

TA3's four-layer stack (Intent, Protocol, Calibration, Hardware; Appendix A; detailed in `TA3_protocols__full.md`) receives the experiment intent at the top layer. The LabOP intent layer encodes the declarative scientific question, quality requirements, and success criteria as a typed Protocol object in the `labop` Python library, serialized as an SBOL3 RDF document. This representation is modality-agnostic: a live-cell imaging protocol and a sequencing-based Perturb-seq protocol differ in their Protocol-layer primitives but share the same Intent-layer structure.

The central question this document addresses is: what is the canonical format that TA2 must emit for TA3 to consume, and how does SIFT's planning stack mediate the conversion?

### 1.3 The program requirement: a Phase I walking skeleton

The IGoR Phase I continuation gate requires a demonstrable closed-loop cycle: TA2 proposes an experiment, TA3 generates a protocol, TA4 executes it, and data return to TA1. The TA2-to-TA3 interface must be formally specified, not just described in prose, by the Phase I Domain-Driven Design workshop. Failure to formalize this interface is a program risk: without a machine-readable contract, the walking skeleton cannot be automated, and Phase I reproducibility milestones cannot be achieved.

---

## 2. The Experiment-Intent Specification: What TA2 Must Emit

### 2.1 Six required fields

Appendix A, TA2 Objective 1, states that the science engine must produce experiment designs specifying cell type, time frame, stimuli, response, and phenotype in sufficient detail to generate a protocol. The research team adds a sixth required field, quality requirements, to match the TA3 calibration layer and the concordance gating thresholds. Together these six fields constitute the **experiment-intent object**, the canonical information payload at the TA2-to-TA3 interface.

| Field | Required by | Content | Ontology grounding |
|---|---|---|---|
| Cell type | Appendix A, TA2-O1 | The specific cell type or cell line to be used; includes differentiation state if applicable | Cell Ontology (CL) term and NCIT cell-line identifier; CZ CELLxGENE conformant |
| Time frame | Appendix A, TA2-O1 | The experimental duration and key timepoints for measurement and intervention; includes the longitudinal schedule for multi-timepoint designs | ISO 8601 durations; linked to the disease-progression schema (Section 35 of the Research Master) |
| Stimuli | Appendix A, TA2-O1 | The perturbation type and target: CRISPR knockout, compound treatment, optogenetic activation, or combinations thereof | Gene Ontology Molecular Function for perturbation target; ChEBI for compounds; NCIT for CRISPR constructs |
| Response | Appendix A, TA2-O1 | The expected or desired downstream biological response as predicted by the TA1 mechanistic model; formulated as a directional causal statement | GO Biological Process terms; INDRA statement format; linked to TA1 causal graph edges |
| Phenotype | Appendix A, TA2-O1 | The measurable readout modality and the specific features to be quantified; includes the assay type and instrumentation class | Human Phenotype Ontology (HPO) or Mammalian Phenotype Ontology; BAO (BioAssay Ontology) for assay type; OAE for assay equipment |
| Quality requirements | TA3 Calibration layer; Phase concordance gates | Minimum acceptable values for key QC metrics: cell viability threshold, concordance floor, signal-to-noise floor, maximum allowed confounding; linked to the RFC parameter set | OBI (Ontology for Biomedical Investigations) for measurement quality; TA3 RFC log for parameter versioning |

### 2.2 The minimal viable serialization

The experiment-intent object can be serialized as a JSON-LD document with a LinkML schema as its definitional backbone. JSON-LD is preferred over plain JSON because it preserves the ontology bindings required for TA1 model updates and for SBOL3 compatibility. The LinkML schema provides: (a) typed field definitions with cardinality constraints; (b) direct mapping to RDF predicates, enabling the intent object to be stored in and queried from an SBOL3 protocol repository; and (c) a machine-readable contract against which both TA2 output validators and TA3 input parsers can independently verify conformance.

A minimal illustrative schema (YAML, LinkML convention):

```yaml
id: https://igor.arpa-h.gov/schema/ExperimentIntent
name: ExperimentIntentSchema
prefixes:
  cl: "http://purl.obolibrary.org/obo/CL_"
  go: "http://purl.obolibrary.org/obo/GO_"
  mondo: "http://purl.obolibrary.org/obo/MONDO_"
  sbol: "http://sbols.org/v3#"
  prov: "http://www.w3.org/ns/prov#"

classes:
  ExperimentIntent:
    description: >-
      The canonical information payload at the TA2-to-TA3 interface.
      Required by IGoR Appendix A, TA2 Objective 1. Must be complete before
      SIFT XP planner ingests the specification for plan compilation.
    slots:
      - experiment_id            # UUID; links to TA2 tournament record
      - cell_type                # CL term URI
      - cell_line_id             # NCIT or Cellosaurus identifier
      - differentiation_state    # CL term URI; optional for primary cells
      - time_frame               # TimeFrame object (see below)
      - stimuli                  # list of Stimulus objects
      - predicted_response       # INDRA Statement URI; links to TA1 causal graph
      - phenotype_readout        # PhenotypeReadout object
      - quality_requirements     # QualitySpec object
      - voi_score                # float; Bayesian VOI estimate from TA2 engine
      - ta1_gap_reference        # URI of the TA1 uncertainty map entry that motivated this design
      - human_authorization      # timestamp and researcher identifier; required before TA3 ingestion

  TimeFrame:
    slots:
      - total_duration           # ISO 8601 duration (e.g., P7D for 7 days)
      - timepoints               # list of Timepoint objects with ISO 8601 timestamps
      - longitudinal             # boolean; true if multi-timepoint imaging required

  Stimulus:
    slots:
      - perturbation_type        # enum: CRISPR_KO | compound | RNAi | optogenetic | other
      - target_gene              # HGNC identifier
      - target_go_function       # GO Molecular Function term URI
      - compound_id              # ChEBI identifier; required for compound perturbations
      - delivery_modality        # enum: lentiviral | electroporation | lipofection | direct | other

  PhenotypeReadout:
    slots:
      - assay_type               # BAO assay term URI
      - modality                 # enum: morphological | transcriptomic | proteomic | imaging | electrophysiology
      - instrument_class         # OAE instrument class URI
      - features                 # list of feature names expected in the output data package
      - data_format              # enum: AnnData | MuData | TIFF | FASTQ | CSV

  QualitySpec:
    slots:
      - min_cell_viability       # float [0, 1]
      - min_concordance          # float [0, 1]; phase-gated (>=0.80 Phase I; >=0.90 Phase II)
      - min_effect_size          # float; minimum Cohen's d or log2-fold-change
      - max_confounding_score    # float; from TA3 RFC parameter set version
      - rfc_parameter_version    # string; identifies the RFC log entry governing these thresholds
```

This schema is illustrative and will require refinement at the Phase I Domain-Driven Design workshop. Its structure, however, is sufficiently specified to begin tooling development in parallel.

### 2.3 Why SBOL3 grounding is required

The experiment-intent object must be SBOL3-compatible for two downstream reasons. First, TA3 stores canonical protocols as SBOL3 RDF documents in the protocol repository; the intent object becomes the top-level Protocol object's annotation, linking the canonical protocol back to the TA2 tournament record and TA1 uncertainty map entry that generated it. Second, TA4 execution records, serialized using the PROV-O ontology, link back to the canonical protocol's SBOL3 URI, completing the provenance chain from TA2 design through TA3 protocol to TA4 execution to TA1 model update.

Without SBOL3 grounding, this chain is broken: execution records cannot be linked to the intent that generated them, and TA1 cannot know which model uncertainty was resolved by a given experiment. This traceability is the technical foundation of the 10x cycle-time target.

---

## 3. The Interface Contract

### 3.1 What TA2 guarantees

When TA2 emits an experiment-intent object, it commits to the following properties:

1. **Mechanistic traceability.** Every field in the intent object traces to a specific entry in the TA1 uncertainty map: an under-constrained parameter, an under-evidenced causal edge, or an inconsistent flux prediction. The `ta1_gap_reference` slot carries this link.

2. **VOI ranking provenance.** The `voi_score` field carries the Bayesian value-of-information estimate from the SIFT Bayesian VOI model (Goldman, Trivedi, Bryce, AAAI Fall Symposium), so that downstream consumers, including the SIFT XP planner, can prioritize across concurrent experiment proposals.

3. **TA4 feasibility pre-check.** Component 3 of the TA2 engine (test-time validation scaling) has verified that the proposed perturbation type, readout modality, and instrument class are available in at least one TA4 laboratory's capability manifest. If no TA4 laboratory can execute the proposed experiment, TA2 does not emit the intent object; it revises the proposal.

4. **Ontology alignment.** All terms in the intent object are resolvable URIs from the named ontologies. No free-text description is accepted in a slot that has an ontology binding.

5. **Human authorization.** The `human_authorization` timestamp confirms that a named researcher has explicitly approved the experiment for submission to TA3. Consequential actions cannot be taken without this authorization.

### 3.2 What TA3 guarantees

When TA3 receives a conformant experiment-intent object, it commits to the following properties:

1. **Plan generation within one business day (Phase I target).** The SIFT XP planner ingests the intent object and produces a scheduled, resource-allocated experiment plan, including laboratory assignment, instrument reservation, and a reagent procurement estimate.

2. **Protocol generation within one business day of plan acceptance.** SIFT compiles the experiment plan to a LabOP Protocol object and its specialization for the assigned TA4 laboratory's backend (OpenTrons OT2, SiLA-based R3200, Illumina SampleSheet).

3. **Calibration parameter governance.** All parameter values in the compiled protocol are drawn from the current RFC-governed parameter set. Deviations from the locked defaults require a new RFC before the protocol is issued.

4. **PROV execution record returned with data.** Every TA4 experiment execution returns a PROV-O conformant execution record linked to the canonical protocol's SBOL3 URI. TA1 can consume this record alongside the experimental data.

5. **Cross-laboratory specialization from one canonical source.** If the same experiment is to be executed at two TA4 laboratories (as required for intra-team concordance checking in Phase I), both specializations are generated from the same canonical LabOP Protocol object, not from two independently authored protocols.

### 3.3 Interface governance

The interface contract is ratified at the Phase I Domain-Driven Design workshop and versioned as a program artifact. Changes to the schema require a process analogous to the TA3 RFC: a versioned proposal, supporting rationale, and an update to the interface contract document. The Software Architect has final authority over schema changes between workshop cycles. The TA2 engine's output validator and the TA3 input parser are both generated from the same LinkML schema, guaranteeing that both sides track the same version.

---

## 4. The Planning-to-Protocol Bridge: SIFT VOI and Plan Compilation

### 4.1 The three-stage pipeline

The conversion from a ranked TA2 experiment proposal to an executable TA3 protocol is a three-stage pipeline. Each stage has a defined input format, a defined output format, and a defined responsible party.

| Stage | Input | Responsible | Output | Standard used |
|---|---|---|---|---|
| 1. VOI ranking and selection | TA1 uncertainty map; TA2 tournament ranked list; TA4 capability manifests | Cytognosis TA2 engine (MM-RAP component); SIFT Bayesian VOI model | Ranked, pre-screened ExperimentIntent objects with VOI scores | LinkML ExperimentIntent schema; SIFT Bayesian VOI model (Goldman, Trivedi, Bryce) |
| 2. Hierarchical experiment plan compilation | ExperimentIntent objects; TA4 laboratory schedules; reagent inventories | SIFT XP planner (Kuter, Goldman, Bryce, Beal, 2018) | Scheduled experiment plan: sub-experiment decomposition, resource allocation, dependency graph, laboratory assignments | SIFT XP plan representation; PDDL-compatible plan format |
| 3. LabOP protocol generation and specialization | SIFT XP experiment plan | SIFT TA3 (LabOP) | Canonical LabOP Protocol object; laboratory-specific specializations | LabOP (Bartley et al., ACM JETC 2023, doi:10.1145/3604568); SBOL3 RDF; PROV-O |

### 4.2 Stage 1: VOI ranking and experiment selection

The science engine's MM-RAP component queries the TA1 model's structured uncertainty output: parameter distributions with bounds, coverage maps, and inconsistent flux predictions. The hub/key-node selector from TA1 Pillar 4 supplies the prioritized perturbation targets; the TA2 tournament ranks hypotheses by their estimated discriminating power against the TA1 uncertainty map.

SIFT's Bayesian VOI model (Goldman, Trivedi, Bryce, AAAI Fall Symposium) provides the formal ranking criterion. The expected information gain for each candidate experiment, I(theta; y | a) = H(theta) - E_y[H(theta | y, a)], is estimated against the TA1 posterior over model parameters. The highest-VOI candidate that also passes TA4 feasibility checking becomes the priority ExperimentIntent object emitted to TA3.

The VOI model was originally developed for synthetic-biology Design-Build-Test-Learn (DBTL) contexts (Goldman, Trivedi, Bryce). Its application to mammalian iPSC-neuron workflows requires one extension: the experiment design space A must be parameterized to include the modalities available in the TA4 laboratory roster (Cell Painting morphological screening, Perturb-LINK live-cell imaging with same-cell scRNA-seq, optical pooled CRISPR screening, high-throughput sequencing). The modality-specific likelihood models needed to estimate expected information gain for each modality are a Phase I validation task.

### 4.3 Stage 2: Hierarchical experiment plan compilation

The SIFT XP planner (Kuter, Goldman, Bryce, Beal, 2018) performs hierarchical task network (HTN) decomposition of the experiment plan. Starting from the ExperimentIntent object, the planner:

1. Decomposes the experiment into sub-experiments and protocol sub-steps with dependencies and resource requirements.
2. Assigns sub-experiments to available TA4 laboratories based on their capability manifests and current schedules.
3. Produces a dependency graph that governs the ordering of sub-steps (e.g., cell differentiation must complete before perturbation delivery; imaging at 24 h must precede library preparation at 72 h).
4. Estimates reagent requirements and flags procurement lead-time conflicts.
5. Outputs a structured plan document that the LabOP protocol generation step consumes.

The XP planner's output format is the handoff object between Stages 2 and 3. Currently this format is defined internally by SIFT. For IGoR, it must be formalized as a shared schema, since Cytognosis's TA2 engine and SIFT's TA3 pipeline both read it. The Phase I Domain-Driven Design workshop must produce this formalization.

For multi-lab execution (required for Phase I concordance checking), the planner generates parallel plan branches: one for each assigned TA4 laboratory. Both branches consume the same ExperimentIntent object, ensuring that the scientific content is identical across laboratory assignments. The plan branches differ only in laboratory-specific resource identifiers and schedule slots.

### 4.4 Stage 3: LabOP protocol generation and specialization

Starting from the SIFT XP plan, the TA3 pipeline generates a canonical LabOP Protocol object using the `labop` Python library. The Protocol object is serialized as an SBOL3 RDF document and stored in the version-controlled protocol repository. The canonical protocol is the source of truth; all laboratory-specific specializations are derived outputs.

Specialization proceeds using the LabOP specializer mechanism (Bartley et al., ACM JETC 2023, doi:10.1145/3604568):

- **Carpenter (Broad/IPAI):** specialization to OpenTrons OT2 Python scripts and CellProfiler pipeline definitions for Cell Painting and optical pooled screening.
- **Cellanome R3200:** specialization to SiLA 2 Feature calls for the CellCage-based live-cell imaging and Perturb-LINK workflow.
- **Illumina:** specialization to SampleSheet.csv run-parameter files and DRAGEN pipeline configuration for sequencing-based assays.
- **Human-readable Markdown:** for manual verification and emergency fallback at any laboratory.

The canonical LabOP Protocol object carries the ExperimentIntent object as an annotation, preserving the full chain from TA2 tournament record through TA3 protocol to TA4 execution. The PROV-O execution records generated by TA4 laboratories link back to the canonical protocol's SBOL3 URI, closing the provenance loop.

### 4.5 The Bryce et al. Round Trip precedent

Bryce et al. (ACS Synthetic Biology, 2022, doi:10.1021/acssynbio.1c00305) demonstrated a fully automated DBTL loop in synthetic biology, integrating the XP planning stack with lab automation for yeast logic-circuit replication. This is the closest published precedent to the TA2-to-TA3 pipeline described here. Its relevance is high for the planning and protocol-generation stages; its domain is synthetic biology, not mammalian iPSC workflows, and the generalisation must be explicitly validated in Phase I.

The key result from Bryce et al. that justifies confidence in the XP-to-LabOP compilation step is that the round-trip pipeline successfully converted experiment plans into LabOP protocols and executed them across heterogeneous platforms without protocol reauthoring. This is exactly the property that IGoR's multi-lab reproducibility milestones require.

---

## 5. What Is Automatable Now, What Needs Work, and What Is Unclear

### 5.1 Automatable now with existing tooling

The following pipeline steps can be executed with existing, publicly available tooling as of June 2026, without new development beyond integration engineering:

| Step | Tooling | Evidence of readiness |
|---|---|---|
| TA2 hypothesis ranking by VOI | SIFT Bayesian VOI model; Goldman, Trivedi, Bryce (AAAI Fall Symp.) | Published in peer-reviewed venue; demonstrated in synthetic-biology context |
| ExperimentIntent object construction and validation | LinkML `linkml-runtime` Python library; schema to be defined at DDD workshop | LinkML is production-ready and used widely in NCATS/biomedical contexts |
| SBOL3 serialization of the intent object | `sbol3` Python library (stable as of 2026) | SBOL3 Python tooling is actively maintained; used in LabOP protocol authoring |
| LabOP Protocol object generation from a plan | `labop` Python library; Bartley et al. 2023 | Demonstrated for synthetic-biology protocols; library is pip-installable |
| Specialization to OpenTrons OT2 | `labop` OT2 specializer; library includes OT2 backend | Demonstrated in LabOP published examples and Bryce et al. 2022 |
| Specialization to human-readable Markdown | `labop` Markdown specializer | Available and tested in LabOP reference implementations |
| PROV-O execution record generation | `labop` execution engine with PROV output; W3C PROV-O | Native LabOP output; W3C standard |

### 5.2 Requires new development: LabOP primitive extensions

The following steps require new LabOP primitive library development. These are fundable Phase I deliverables, not fundamental research challenges:

| Gap | Required development | Phase target | Partners |
|---|---|---|---|
| No LabOP primitives for iPSC differentiation protocols | Author `cell_culture` extension primitives: `Differentiate`, `InduceDifferentiation`, `VerifyDifferentiationState` | Phase I | SIFT + Carpenter + Cellanome (SOP knowledge source) |
| No LabOP primitives for live-cell longitudinal imaging | Author `live_cell_imaging` primitives: `TimeLapseImaging`, `CellCageLoad`, `ImagingSchedule` | Phase I | SIFT + Cellanome |
| No LabOP primitives for same-cell scRNA-seq library preparation (Perturb-LINK) | Author `single_cell_rnaseq` extension primitives: `PerturbLINKLibraryPrep`, `SameCellRetrieval` | Phase I | SIFT + Cellanome |
| No LabOP primitives for optical pooled CRISPR screening | Author `optical_pooled_screening` primitives: `LibraryDelivery`, `InSituSequencing`, `PooledCRISPRSelection` | Phase I-II | SIFT + Carpenter |
| R3200 SiLA Feature Definition not publicly documented | NDA-gated technical exchange with Cellanome to document the SiLA Feature Definition; then author the LabOP SiLA/R3200 specializer | Phase I | SIFT + Cellanome |

### 5.3 Requires new development: planner extensions

| Gap | Required development | Phase target |
|---|---|---|
| SIFT XP plan format is not yet a shared schema | Formalize the XP plan output as a LinkML schema; generate a Python parser for both SIFT and Cytognosis consumption | Phase I DDD workshop |
| VOI likelihood models are not defined for mammalian imaging and scRNA-seq modalities | Develop likelihood functions for Cell Painting morphological features, live-cell imaging metrics, and Perturb-seq effect sizes as inputs to the Bayesian VOI model | Phase I (validation task) |
| TA4 laboratory capability manifests have no open format | Define a lightweight LinkML schema for laboratory capability manifests (modalities, instrument types, current availability); author one per TA4 laboratory | Phase I |
| Multi-lab plan branching for concordance checking | Extend the XP planner to generate parallel plan branches from a single ExperimentIntent object, ensuring scientific equivalence across branches | Phase I |

### 5.4 Unclear or unresolved

| Uncertainty | Nature of the uncertainty | Recommended resolution |
|---|---|---|
| Cellanome R3200 SiLA interface availability | Cellanome has no publicly documented API or SiLA Feature Definition as of 2026-06-14; the LabOP specializer for the R3200 cannot be built without this information | NDA-gated technical exchange in Phase I Month 2; make this a named Phase I dependency with a go/no-go review |
| VOI score calibration across modalities | Whether a VOI score computed against the TA1 mechanistic model for a scRNA-seq readout is comparable to a VOI score for a Cell Painting readout is not established; cross-modality VOI normalization requires empirical calibration | Phase I validation experiment: run the VOI model against the Phase I anchor experiment design and compare ranked predictions to expert-panel ratings (Spearman r target >=0.4) |
| TA1 uncertainty map API format | The TA1 Pillar 4 hub-selector and uncertainty-map output format has been described architecturally (Research Master, Section 30) but not yet implemented as a queryable API | Phase I software deliverable: a working Pillar 4 hub-selector API with a defined JSON-LD schema; required before VOI ranking can operate |
| Scalability of the planning stack to campaigns with >10 concurrent experiments | The SIFT XP planner's scalability in this regime has been demonstrated in synthetic-biology but not in mammalian multi-lab contexts | Phase II scaling test; plan for HTN decomposition complexity analysis in Phase I architecture documentation |
| Handling of experiment failure and protocol revision | The current interface contract describes the forward path (design to protocol to execution). The backward path (execution failure to protocol revision to re-execution) requires a defined exception-handling protocol at the TA2-TA3 interface | Define an exception-handling workflow in Phase I DDD workshop; TA4 exception reduction milestones (50% reduction by Phase II) depend on this |

---

## 6. Recommended Interface Schema

### 6.1 Format recommendation

**Recommended format: LinkML schema, serialized as JSON-LD, cross-referenced to Cell Ontology, Gene Ontology, MONDO, SBOL3, and PROV-O.**

LinkML (Moxon et al., 2021; https://linkml.io; maintained by NCATS and the open community) is the recommended schema definition language for the following reasons:

1. **Bidirectional serialization.** A single LinkML schema generates validators, Python dataclasses, and JSON-LD context files simultaneously. TA2's output validator and TA3's input parser are both derived from the same source, eliminating schema drift.

2. **Ontology binding natively supported.** LinkML's `range` and `uri_or_curie` types support direct binding to OBO Foundry ontology terms, which is required for the cell-type, gene target, and phenotype slots.

3. **RDF compatibility.** The JSON-LD output of a LinkML-validated document is directly importable into an SBOL3 protocol repository, preserving the provenance chain.

4. **Precedent in biomedical standards.** LinkML is used by the NMDC (National Microbiome Data Collaborative), NCATS Biomedical Translator, and the MIxS metadata standards. It is not experimental software.

5. **Tooling maturity.** `linkml-runtime` is pip-installable, actively maintained, and has a stable API as of version 1.x.

An alternative is to define the interface using JSON Schema with `$ref` links to external ontologies. JSON Schema is more widely known but provides weaker ontology binding (link-only, not validation-enforced) and does not generate RDF-compatible serializations natively. It is acceptable if the team finds JSON Schema tooling more accessible, but the RDF compatibility requirement makes LinkML the stronger choice.

A second alternative is to express the interface directly as SBOL3 RDF. This is possible but burdens TA2 with detailed knowledge of the SBOL3 object model, which is SIFT/TA3's domain. Using LinkML as an intermediate schema insulates TA2 from SBOL3 specifics while guaranteeing RDF compatibility downstream.

### 6.2 SBOL grounding rationale

SBOL3 grounding is required, not optional, for the following chain:

ExperimentIntent (JSON-LD, LinkML schema) --> LabOP Protocol object (SBOL3 RDF) --> PROV-O execution record (links to LabOP Protocol URI) --> TA1 model update (consumes execution record + data)

Without SBOL3 grounding at the intent layer, the TA1 model update step cannot know which model uncertainty entry was targeted by a given executed experiment. This breaks the closed loop that is the Phase I walking-skeleton milestone.

### 6.3 Ratification process

The DDD workshop (Phase I, Month 3, Appendix A) is the natural venue for ratification. The recommended process:

1. **Month 1-2 (pre-workshop):** Cytognosis and SIFT independently draft their side of the interface. Cytognosis defines what TA2 can commit to producing; SIFT defines what TA3 requires as input. Both use the illustrative schema in Section 2.2 as a starting point.
2. **Month 3 (DDD workshop):** Reconcile the two drafts into a ratified schema. Resolve naming and cardinality conflicts. Identify any new required slots. Sign off on the serialization format and versioning protocol.
3. **Month 4-6:** Implement the TA2 output validator and the TA3 input parser from the ratified schema. Run the Phase I anchor experiment design through the full pipeline as a proof-of-concept.
4. **Ongoing:** Schema changes require a mini-RFC process (proposal, impact analysis, version bump) before implementation.

---

## 7. Alignment to TA2 and TA3 ISO Objectives and Program Phases

### 7.1 TA2 objectives

| IGoR objective | How the interface satisfies it |
|---|---|
| TA2-O1: Generate and prioritize experimental hypotheses by interrogating the TA1 comprehensive disease model | The ExperimentIntent object's `ta1_gap_reference` and `voi_score` slots are direct evidence of mechanistic grounding; they trace every emitted intent to a specific TA1 uncertainty entry and a Bayesian ranking |
| TA2-O2: Produce hypotheses with traceable mechanistic reasoning that human researchers can interrogate, validate, and override | The `human_authorization` slot enforces the human-in-the-loop gate; the `predicted_response` slot links to the INDRA statement in the TA1 causal graph for researcher inspection |

### 7.2 TA3 objectives

| IGoR objective | How the interface satisfies it |
|---|---|
| TA3-O1: Develop a layered interoperable protocol stack enabling experimental procedures to be specified independently of instruments, then compiled to hardware-specific execution with full provenance | The intent-to-protocol pipeline (Stage 1 through Stage 3) maps directly onto the four-layer stack; the canonical LabOP Protocol object provides the hardware-independent representation; PROV-O records provide provenance |
| TA3-O2: Engage external standards bodies and equipment manufacturers to ensure protocol standards have adoption potential beyond IGoR | LinkML is an open, NCATS-maintained standard; LabOP is governed by the Bioprotocols Working Group; the ExperimentIntent schema will be contributed to the Bioprotocols Working Group as a Phase III deliverable |

### 7.3 Phase-by-phase interface deliverables

| Phase | Interface deliverable | Success criterion |
|---|---|---|
| Phase I (18 mo) | Ratified LinkML ExperimentIntent schema (v1.0); TA2 output validator and TA3 input parser generated from schema; ExperimentIntent-to-LabOP pipeline demonstrated on Phase I anchor experiment | At least 1 ExperimentIntent object successfully compiled to a LabOP Protocol and executed at two TA4 laboratories from the same canonical source |
| Phase II (18 mo) | Schema extended to cover >=3 modalities; XP plan format formalized as a shared schema; VOI likelihood models validated against first 10 executed experiments (Spearman r >=0.4 target) | At least 3 ExperimentIntent objects per cycle compiled to LabOP Protocols and executed at >=3 laboratories; RFC-governed parameter changes reflected in successive schema versions |
| Phase III (24 mo) | ExperimentIntent schema published as a Bioprotocols Working Group proposal; open data layer integrates intent provenance for all executed experiments | Schema adopted by at least one external team; cross-team connect-a-thon uses the same ExperimentIntent format |

---

## 8. Gaps, Best-Fit Components, and Interface Risks

### 8.1 Summary gap table

| Gap | Severity | Owner | Resolution path | Phase target |
|---|---|---|---|---|
| TA1 Pillar 4 hub-selector API not implemented | High | Cytognosis | Phase I software deliverable: working API with JSON-LD schema | Phase I Month 6 |
| ExperimentIntent schema not formalized | High | Cytognosis + SIFT | DDD workshop; draft schema is in this document | Phase I Month 3 |
| SIFT XP plan output format not a shared schema | High | SIFT | Formalize at DDD workshop; generate Python parser | Phase I Month 3 |
| Cellanome R3200 SiLA Feature Definition unavailable | High | SIFT + Cellanome | NDA-gated technical exchange; Phase I dependency | Phase I Month 2 |
| VOI likelihood models not defined for mammalian modalities | High | SIFT + Cytognosis | Phase I validation experiment; Spearman r metric | Phase I Month 18 |
| No LabOP primitives for iPSC, live-cell imaging, Perturb-LINK | High | SIFT (prime author) + Cellanome + Carpenter | Phase I TA3 deliverable: new primitive libraries | Phase I Month 12 |
| TA4 capability manifest format undefined | Medium | SIFT + TA4 labs | Lightweight LinkML schema; Phase I deliverable | Phase I Month 6 |
| Exception handling workflow not specified | Medium | Cytognosis + SIFT | DDD workshop; link to TA4 exception reduction milestones | Phase I Month 3 |
| XP planner scalability in mammalian multi-lab context | Medium | SIFT | Phase II scaling test; Phase I architecture analysis | Phase II |
| Cross-modality VOI score normalization | Medium | Cytognosis + SIFT | Empirical calibration against Phase I experiments | Phase I-II |

### 8.2 Best-fit component summary

| Component | Role at the interface | Justification |
|---|---|---|
| SIFT Bayesian VOI model (Goldman, Trivedi, Bryce) | Stage 1: ranks ExperimentIntent candidates by expected information gain | Only published Bayesian VOI model for experiment selection in a DBTL context; published in peer-reviewed venue |
| SIFT XP hierarchical planner (Kuter, Goldman, Bryce, Beal, 2018) | Stage 2: converts intent to scheduled experiment plan | Demonstrated HTN decomposition with resource allocation in synthetic-biology DBTL; extensible to mammalian workflows |
| LabOP (Bartley et al., ACM JETC 2023) | Stage 3: encodes canonical protocol; generates specializations | Only open standard covering Intent and Protocol layers with formal execution semantics and multi-backend specialization |
| LinkML | Schema definition language for ExperimentIntent and XP plan | Bidirectional serialization; ontology binding; RDF compatibility; NCATS-maintained; production-ready |
| SBOL3 | Persistent identity and RDF representation for LabOP protocols | Required for provenance chain continuity; W3C-compliant |
| PROV-O | Execution record provenance | W3C standard; native LabOP output; required for TA1 model update linkage |
| Cell Ontology (CL) | Cell-type slot grounding | CZ CELLxGENE conformant; required for cross-dataset interoperability |
| Gene Ontology (GO) | Perturbation target and predicted-response slot grounding | Standard for molecular function and biological process annotation |
| MONDO | Disease context annotation | Standard for disease entity identity; links to TA1 disease model |
| INDRA + CoGEx | Predicted-response slot provenance; TA1 causal graph query | Mechanism-typed statement format with belief scores and provenance; supplies the causal link format for the predicted-response slot |

---

## References

1. Bartley B, Beal J, Rogers M, Bryce D, Goldman RP, Keller B, Lee P, Biggers V, Nowak J, Weston M. Building an Open Representation for Biological Protocols. bioRxiv 2022.07.05.498808. doi:10.1101/2022.07.05.498808. Published July 8, 2022.
2. Bartley B et al. Building an Open Representation for Biological Protocols. *ACM Journal on Emerging Technologies in Computing Systems* 19(3), 2023. doi:10.1145/3604568.
3. Bryce D, Goldman RP, Beal J et al. Formalizing Sample Transformation Plans. AAAI Fall Symposium. [Year to be confirmed against SIFT records.]
4. Bryce D et al. Round Trip: Automated Pipeline for Experimental Design, Execution, and Analysis. *ACS Synthetic Biology*, 2022. doi:10.1021/acssynbio.1c00305.
5. Bunne C et al. How to Build the Virtual Cell with Artificial Intelligence: Priorities and Opportunities. *Cell* 187, 7045-7063, 2024. doi:10.1016/j.cell.2024.11.015.
6. Eslami M, Moseley R, Eramian H, Bryce D, Haase S. AutoGater. *Scientific Reports*, 2024.
7. Goldman RP, Trivedi N, Bryce D et al. A Bayesian Model for Experiment Choice in Synthetic Biology. AAAI Fall Symposium. [Year to be confirmed against SIFT records; cite as Goldman et al., AAAI Fall Symp.]
8. Goldman RP, Moseley M, Roehner N, Cummins B et al. Highly-automated high-throughput replication of yeast-based logic-circuit assessments. *Synthetic Biology*, 2022.
9. Kuter U, Goldman RP, Bryce D, Beal J. XP: Experiment Planning for Synthetic Biology. 2018. [Conference and full citation to be confirmed.]
10. McLaughlin JA et al. Synthetic biology open language (SBOL) version 3: Simplified data exchange for biodesign. *Frontiers in Bioengineering and Biotechnology*, 2020. doi:10.3389/fbioe.2020.00486.
11. Moxon S et al. The LinkML Modeling Language. 2021. https://linkml.io. [Confirm primary publication venue.]
12. Ulrich D et al. SiLA 2: The Next Generation Lab Automation Standard. *SLAS Technology*, 2022. PubMed: 35639108. doi:10.1177/24726303221085635.
13. W3C PROV Data Model. https://www.w3.org/TR/prov-o/ (accessed 2026-06-14).
14. Zhang J et al. Identifiability Guarantees for Causal Disentanglement from Soft Interventions. *NeurIPS 2023*. [arXiv:2307.06250; verify final proceedings citation.]

**IGoR program materials:**
- ARPA-H. IGoR Program and Technical Description. Appendix A, ARPA-H-SOL-26-155. 2026.

**Internal cross-references:**
- `TA2_science_engine__full.md` -- TA2 engine architecture and SIFT VOI integration
- `TA3_protocols__full.md` -- LabOP architecture, four-layer stack, primitives, specialization
- `SIFT_capabilities_analysis.md` -- SIFT plan-to-protocol and value-of-information capabilities
- Research Master, Section 33 -- TA2 engine contribution
- Research Master, Section 34 -- TA3 and TA4 execution stack
- Research Master, Section 35 -- Standards stack and disease-progression schema

**Citations flagged for verification before submission:**
- Goldman, Trivedi, Bryce AAAI Fall Symp: verify year and proceedings volume.
- Kuter, Goldman, Bryce, Beal XP 2018: verify conference name (AAAI? ICAPS?) and full citation.
- Bryce, Goldman, Beal et al. Formalizing Sample Transformation Plans: verify AAAI Fall Symp year and proceedings.
- Moxon et al. LinkML 2021: confirm primary peer-reviewed publication versus preprint.
- Goldman et al. Synthetic Biology 2022: verify journal title and DOI.

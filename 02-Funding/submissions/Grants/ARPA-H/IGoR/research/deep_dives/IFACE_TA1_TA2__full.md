# TA1-to-TA2 Interface: A Mechanistic-Model-Grounded Research Deep-Dive

**Document type:** Internal deep-dive, publication-quality review
**Prepared for:** ARPA-H IGoR Proposal (ARPA-H-SOL-26-155), TA1-TA2 interface architecture
**Date:** 2026-06-14
**Profile:** Internal build only. Contains references to SPEAR (confidential, under anonymous review) and to the factorized-PRS (proprietary crown-jewel IP). Do not distribute or include in the `shareable` build. See firewall rules in the Research Master, sections 31 and 32.

---

## Abstract / BLUF

This document specifies the data-and-control-flow contract between TA1 (Comprehensive Disease Models) and TA2 (New Science Engine) for the IGoR program. The central architectural question is: how does a reasoning engine query, critique, and advance a mechanistic causal disease model rather than merely retrieving from text? The answer requires a formally specified interface that flows structured probabilistic outputs from TA1 into TA2 and returns ontology-aligned testable hypotheses and experiment designs back. This bidirectional flow is the technical substrate for what we term mechanistic-model-grounded retrieval-augmented planning (MM-RAP), a distinct architectural class that no published system has implemented.

The TA1 model state that TA2 queries now explicitly includes three new structural elements introduced by the Research Master sections 30.5-31b: (1) a set of **k interpretable disease-axis factors (archetypes)** derived from the genomic front-end factorization, each encoding a sparse, pathway-disentangled dimension of disease-associated genetic variation; (2) a **deep structural causal model (SCM) over those axes** that learns their causal interactions, making axis-to-axis causal edge uncertainty an explicit interface object; and (3) **per-axis and per-archetype uncertainty**, propagated from the genomic-factor posterior through the generative core, and accessible to TA2 for value-of-information scoring. Knowledge gaps now include under-determined disease axes (archetype count k and archetype weight vectors with high posterior variance) and poorly constrained axis-to-axis causal edges in the deep SCM, both of which are high-value targets for TA2's VOI-guided experiment selection.

Because the generative core supports **compositional conditioning** (classifier-free guidance generalized to conditional flow matching, per Research Master section 32b), TA2 can request **combinations** of axes, perturbations, and archetypes as designed experiments. The interface contract must carry such compositional experiment requests as structured objects, not free-text instructions. This compositional capacity is a new class of query at the TA1-TA2 boundary that prior drafts of this document did not specify.

The knowledge-gap-identification function occupies a boundary zone between TA1 (which detects gaps structurally) and TA2 (which prioritizes and translates them into experiment designs). ARPA-H explicitly notes this boundary is an open question; our recommendation places gap detection in TA1 and gap prioritization and experiment specification in TA2, with a thin bidirectional query protocol joining the two. Prior art in BOED, GraphRAG, CausalRAG, NIMMGen, and GRACE is surveyed and differentiated. Gaps and best-fit compositions are identified for each phase.

**Reading time:** approximately 25 minutes.
**If you read one section:** read Section 3 (the interface contract) and Section 5 (the grounding stack and how it differs from GraphRAG and CausalRAG).

---

## 1. Why the Interface Is the Central Design Problem

### 1.1 The IGoR program requirement

Appendix A of the IGoR solicitation requires that TA2 "interact with and interrogate" the TA1 Comprehensive Disease Model. It states explicitly that systems which "merely prompt an LLM to suggest experiments and route them to an automated laboratory do not meet the requirements of this program." The program further states that the TA1/TA2 boundary for knowledge-gap identification "is an open question and expects that it will be refined during the program."

These two requirements together define the central design problem: TA2 must have a real query-and-response relationship with TA1, not just access to a static snapshot of the model's prior state. The interface must support:

1. TA2 querying TA1 for uncertainty, gaps, and inconsistencies in the current model state.
2. TA2 using that query response as the primary retrieval corpus for experiment planning.
3. TA1 updating its model state from the data returned by TA4 experiments that TA2 proposed.
4. TA2 receiving the updated model state and revising its hypothesis queue accordingly.

With the disease-axis architecture now specified (Research Master sections 30.5-31b), two additional interface requirements emerge:

5. TA2 querying TA1 for uncertainty over disease-axis factors and the causal structure among them, and using that uncertainty as the primary input to VOI scoring.
6. TA2 submitting compositional experiment requests (targeting combinations of axes, perturbations, and archetypes) that TA1 can evaluate by running compositionally conditioned generative queries.

This is a bidirectional, stateful, event-driven interface. It is not a file-share or a database query over a static artifact.

### 1.2 The field gap

The survey in TA2 deep-dive Section 3 establishes that no published agentic-science system maintains this kind of interface. GraphRAG (Edge et al. 2024, Microsoft Research) retrieves over a graph derived from text. CausalRAG (Wang et al., Findings of ACL 2025, arXiv:2503.19878) retrieves over text-extracted causal triples. NIMMGen (Guan et al., arXiv:2602.18008, ICML 2026 submission) generates mechanistic model code de novo but does not maintain a living, experiment-updated causal object. GRACE (arXiv:2602.15039, 2026) is the closest published work in physical science: an agentic system grounded in explicit Monte Carlo simulations rather than learned world models, with an interpret-act-validate loop over the simulator. GRACE is in particle physics, not in disease biology, and its models are first-principles simulators with known equations, not inferred causal disease models with quantified parameter uncertainty. The Agentic Scientific Simulation paper (arXiv:2603.00214, 2026) formalizes execution-grounded model construction as an interpret-act-validate loop, providing a useful vocabulary, but its scope is model reconstruction rather than model-grounded hypothesis planning.

The interface we specify here closes this gap precisely, for the biological disease modeling domain.

---

## 2. The TA1 Model as a Queryable Object

### 2.1 What TA1 produces at the interface boundary

The TA1 four-pillar architecture (Research Master Section 30; TA1 deep-dive Sections 7.1-7.4) produces, at any point in the program, a computable model object with the following properties:

**Pillar 1 outputs (mechanistic network layer):**
- A directed Biolink-formatted causal knowledge graph over biological processes, with per-edge belief scores from INDRA assembly and ECO-coded evidence provenance.
- A coverage map: for each subgraph region defined by GO biological process, MONDO disease, CL cell-type, and UBERON tissue identifiers, a measure of belief-weighted evidence density. Low-density regions are candidate knowledge gaps.
- An inconsistency register: pairs of mechanistic assertions that are mutually contradictory given the current causal graph structure (detected by CoGEx model checking or INDRA belief conflict detection).

**Pillar 2 outputs (causal generative layer), updated to reflect the three-latent SCM and disease-axis architecture:**
- The posterior distribution over SAMS-VAE mechanism-shift parameters: for each biological process, the posterior mean and variance of the mask entry m_t and the effect vector e_t that characterizes the disease perturbation on that process (Bereket and Karaletsos, NeurIPS 2023, arXiv:2311.02794).
- Posterior uncertainty maps: for each biological process dimension, the credible interval width, computed from the IWELBO posterior approximation.
- **Disease-axis factor set:** k axis vectors (archetypes) derived from the genomic front-end factorization (Research Master section 31b). Each axis is a sparse, pathway-disentangled causal dimension that conditions the generative core. The posterior uncertainty over each axis (archetype weight vector variance, factor loading credible intervals from GLEANR/FactorGo) is propagated and exposed as a first-class interface object.
- **Axis-level causal structure:** the deep structural causal model (deep SCM) over the k disease axes, encoding learned directed causal edges among them (Research Master section 31b, step 5). Each axis-to-axis edge has a posterior probability and credible interval. Under-determined edges (wide credible intervals, low confidence) are enumerated as a candidate gap register at the axis-causal-structure level.
- **Per-archetype uncertainty:** for each of the k archetypes, the posterior variance over its weight vector in the factorization. Archetypes with high posterior variance are poorly identified from the current data and are candidate high-value experimental targets.
- Soft-intervention parameters: the factorized-PRS axes (restricted, Section 31) that parameterize the disease operator; their uncertainty is propagated from the GLEANR/FactorGo posterior over genomic factor loadings.
- A set of "ghost edges": causal connections hypothesized by the mechanistic network but not yet evidenced by single-cell data from TA4 experiments, flagged for experimental resolution.

**Pillar 3 outputs (joint shift-space layer):**
- The joint cellular-clinical shift representation: a delta vector in biological-process space per cohort or perturbation condition, with confidence intervals that reflect both data quantity and the sVAE-ligr transfer uncertainty when bridging from model system to clinical cohort (Hediyeh-zadeh, Fischer, Theis 2024, ICLR 2024 MLG workshop).
- Identified inconsistencies between cellular-level and clinical-level evidence for the same biological process, flagged as high-value TA2 targets.
- **Axis-level shift projection:** for each disease-axis factor, the corresponding shift in the joint cellular-clinical shift-space. This links the genomic-level archetype representation to observable cellular phenotypes and clinical readouts, and is a prerequisite for TA2 to specify experiments that confirm or refute specific axis-to-phenotype predictions.

**Pillar 4 outputs (ontology-conditioned gap and intervention design layer):**
- Ranked hub-node list: transcription factors and signaling biomolecules predicted by PDGrapher to maximally shift disease-relevant biology, scored by predicted intervention magnitude and ranked by estimated information gain against the Pillar 2 uncertainty map (Gonzalez et al., Nature Biomedical Engineering 2025, doi:10.1038/s41551-025-01481-x).
- Under-explored ontology subtree map: GO biological process, MONDO disease, and Cell Ontology subtrees where the disease map lacks coverage and where the model's OOD interpolation confidence (TransBox box embeddings, Xiong et al. arXiv:2410.14571) falls below a threshold.
- The Disease Map executable: the CellDesigner -> CaSQ -> SBML-qual -> MaBoSS pipeline producing stochastic attractor state-probability time courses, runnable independently by TA2 for pre-simulation screening of hypotheses.
- **Axis-gap register:** a register of under-determined disease axes (archetypes whose posterior variance exceeds a threshold, or axis-to-axis causal edges with wide credible intervals). This is the axis-level analog of the biological-process-level gap register and is the primary VOI target set when TA2 is prioritizing experiments expected to resolve the disease-axis causal structure.

### 2.2 Encoding the model output as a queryable schema

All four pillars' outputs must be represented in a machine-readable schema that TA2 can query at runtime. We specify this using LinkML (Research Master Section 35), producing JSON-LD or Turtle RDF output that is simultaneously:

- Directly queryable by a SPARQL or SHACL reasoning layer in TA2.
- Serializable as structured JSON for LLM-readable context injection.
- Diff-able across model update events (so TA2 can detect exactly which parameter distributions changed when new TA4 data arrived).

The core schema object is the **TA1ModelState** document, which is versioned and event-stamped. Each model update event produces a new TA1ModelState with a delta record against the prior version.

The TA1ModelState schema is extended relative to prior drafts to include the following new top-level objects:

- **`DiseaseAxisSet`**: a list of k axis records, each containing the axis index, a pathway annotation (GO/Reactome), the posterior mean and variance of the archetype weight vector, and the factor loading credible intervals.
- **`AxisCausalStructure`**: the adjacency matrix of the deep SCM over axes, with per-edge posterior probability and credible interval.
- **`AxisGapRegister`**: the ranked list of under-determined axes and axis-causal edges, sorted by posterior variance.
- **`CompositionalQueryResult`**: the response object returned when TA2 issues a compositional conditioning query (see Section 3.5).

---

## 3. The Interface Contract: Data-and-Control-Flow Specification

### 3.1 What flows from TA1 to TA2

The following data objects cross the TA1-to-TA2 boundary, in order of operational priority:

| Data object | TA1 source pillar | Schema type | Update trigger |
|---|---|---|---|
| **Uncertainty map** | Pillar 2 posterior | LinkML `ModelUncertaintyMap` | On every TA4 data return event |
| **Disease-axis factor set** | Pillar 2 genomic front-end | LinkML `DiseaseAxisSet` | On genomic data ingestion or archetype posterior update |
| **Axis causal structure** | Pillar 2 deep SCM | LinkML `AxisCausalStructure` | On posterior update of deep SCM; on TA4 perturbation data return targeting axis-linked biology |
| **Axis gap register** | Pillar 4 axis-gap layer | LinkML `AxisGapRegister` | On every model update |
| **Gap register** | Pillar 1 coverage map + Pillar 4 OOD map | LinkML `KnowledgeGapRegister` | On every model update and on a configurable schedule |
| **Inconsistency register** | Pillar 1 INDRA conflict detection | LinkML `InconsistencyRegister` | On every literature update (EMMAA cycle) |
| **Hub-node ranked list** | Pillar 4 PDGrapher output | LinkML `HubNodeList` | On every model update |
| **Ghost-edge list** | Pillar 2 latent graph, Pillar 1 network | LinkML `GhostEdgeList` | On every model update |
| **Model executable handle** | Pillar 4 Disease Map pipeline | Container URI + API endpoint | Phase I: on demand; Phase II: streaming |
| **Shift-space snapshot** | Pillar 3 | LinkML `ShiftSpaceSnapshot` | On TA4 data return; on new clinical cohort ingestion |
| **Axis-level shift projection** | Pillar 3 (axis-projected) | LinkML `AxisShiftProjection` | On Pillar 3 update |

**Key property of this flow:** every data object carries calibrated uncertainty (credible intervals, belief scores, coverage fractions). TA2 does not receive point estimates; it receives distributions. The disease-axis factor set and axis causal structure carry their own uncertainty terms: archetype weight-vector variance and axis-to-axis edge credible intervals, respectively. These are the technical basis for VOI-guided experiment selection at the axis level: the experiment that most reduces the area under the axis-gap-register uncertainty distribution is selected alongside experiments that target biological-process-level gaps.

### 3.2 What flows from TA2 back to TA1

| Data object | TA2 source component | Schema type | Trigger |
|---|---|---|---|
| **Ranked hypothesis set** | Tournament component | LinkML `HypothesisSet` | After each tournament round |
| **Compositional experiment request** | RAP planner, axis-targeting component | LinkML `CompositionalExperimentRequest` | When TA2 proposes experiments targeting axis combinations |
| **Executed experiment record** | From TA3/TA4 after execution | LinkML `ExperimentRecord` | On experiment completion |
| **Posterior update trigger** | TA2 planning layer | Event notification (CloudEvents format) | On TA4 data return |
| **VOI score trace** | Tournament ranking | LinkML `VOIScoreTrace` | After each tournament round |
| **Critic rejection log** | Mechanistic critic agent | LinkML `CriticLog` | After each critique pass |

The **`CompositionalExperimentRequest`** is new in this revision. It encodes a TA2-specified experiment as a combination of one or more disease axes, perturbations, and archetypes to co-condition, along with the biological readout modality expected to discriminate among compositional predictions. This object type is required because the TA1 generative core supports compositional conditioning (Research Master section 32b): a combination of disease axes and interventions can be specified as a single conditioned generation, and the interface must carry this request in structured form so TA1 can execute it correctly without ambiguity about which axes and perturbations are combined.

The **posterior update trigger** is the most critical return flow: it is the event that fires TA1's Bayesian update pipeline. The update latency targets (Phase II: <=24 hours; Phase III: <=4 hours, per Appendix A Table 1) are measured from this trigger event to the time TA1 emits a new TA1ModelState with updated uncertainty maps.

### 3.3 Control flow: the closed-loop cycle

```
TA1 ModelState(t) --> TA2 Tournament:
  query UncertaintyMap, GapRegister, HubNodeList
  query DiseaseAxisSet, AxisCausalStructure, AxisGapRegister
  generate hypotheses against gap set and axis-gap set
  critique hypotheses with MechanisticCritic(TA1 graph constraint set + axis SCM)
  rank by VOI score (SIFT Bayesian VOI model, over both process-level and axis-level uncertainty)
  select top-K hypotheses
  for compositional axis-targeting hypotheses:
    issue CompositionalExperimentRequest to TA1
    receive CompositionalQueryResult (predicted distributions over combined axes)
    update VOI score with axis-resolution estimate
  pre-simulate with TA1 Disease Map pipeline (POST /simulate)
  pass surviving hypotheses to TA3

TA3 --> TA4: protocol generation + execution

TA4 data return --> ExperimentRecord
ExperimentRecord --> posterior update trigger
TA1 Bayesian update:
  ModelState(t) --> ModelState(t+1)
  DiseaseAxisSet posterior update (if experiment was axis-targeted)
  AxisCausalStructure posterior update (if experiment resolved an axis-to-axis edge)
TA1ModelState(t+1) delta --> TA2: revised UncertaintyMap, DiseaseAxisSet, AxisCausalStructure
TA2: update hypothesis queue priorities
repeat
```

This loop is the "walking skeleton" required by Appendix A Phase I. The minimal Phase I implementation must demonstrate at least one complete cycle: one hypothesis from TA2 tournament, one protocol from TA3, one experiment executed by TA4, one data return to TA1, one model update, one updated TA2ModelState. In Phase II and III, the compositional experiment request path must be validated, demonstrating that TA2 can propose axis-combination experiments that TA1 can evaluate and return conditional predictions for.

### 3.4 The query API design

The TA2 planning engine queries TA1 via a defined API rather than reading static files. The API exposes four primary query types from prior drafts, extended by two new endpoints for axis-level and compositional queries:

1. **`GET /uncertainty_map?process_ids=[]&credible_interval=0.95`**: Returns the posterior mean and credible interval for each specified biological process dimension.

2. **`GET /gap_register?ontology_domain=[GO|MONDO|CL]&threshold=<coverage_fraction>`**: Returns knowledge gaps sorted by coverage fraction below the threshold, filterable by ontology domain.

3. **`GET /hub_nodes?top_k=<N>&disease_id=<MONDO:ID>&cell_type=<CL:ID>`**: Returns the top-K hub nodes ranked by predicted intervention magnitude for the specified disease and cell-type context.

4. **`POST /simulate?hypothesis=<HypothesisRecord>`**: Runs the Disease Map pipeline (SBML-qual + MaBoSS) for the given hypothesis and returns attractor state-probability time courses. This is the test-time pre-simulation endpoint. Phase I: synchronous call, runtime <60 seconds. Phase II: asynchronous, streaming results.

5. **`GET /axis_state?axis_ids=[]&credible_interval=0.95`**: Returns the posterior mean, variance, and credible interval for each specified disease-axis factor (archetype weight vector and factor loadings), plus the axis-to-axis causal edge posteriors from the deep SCM for edges connecting the requested axes. This is the primary VOI-input query for axis-level experiment planning.

6. **`POST /compositional_query?request=<CompositionalExperimentRequest>`**: Accepts a compositional conditioning request (a combination of axis identifiers, perturbation targets, and readout modalities) and returns predicted cellular-state distributions under that combination from the generative core. Phase I: synchronous, restricted to pairs of axes; Phase II: arbitrary axis combinations. This endpoint is the mechanization of the compositional-conditioning capability described in Research Master section 32b.

All API responses are LinkML-validated JSON-LD documents. The query-response pair is logged to an audit trail (Anthropic Agent SDK audit chain) for IV&V inspection.

### 3.5 Compositional experiment requests: the new interface class

The compositional-conditioning capability of the generative core (Research Master section 32b) is scientifically important because many disease phenotypes arise from the interaction of multiple axes, and a single-axis perturbation experiment cannot disambiguate axis-interaction effects from main-axis effects. TA2 must be able to request experiments designed to probe those interactions.

The **`CompositionalExperimentRequest`** schema contains:

- **`axis_set`**: list of axis identifiers from the `DiseaseAxisSet`, each with a conditioning weight (the relative strength of each axis in the compositional condition).
- **`perturbation_set`**: list of perturbation targets (GO molecular function identifiers or MONDO disease codes), each paired with an intervention type (CRISPR knockout, small molecule, etc.) and a dose range.
- **`archetype_combination`**: optional specification of a combination of archetype weight vectors to condition on simultaneously (for multi-archetype experiments).
- **`predicted_discriminant`**: the biological readout predicted by the model to best discriminate among the compositional conditions (derived from the Pillar 4 hub-node ranked list filtered to axis-linked nodes).
- **`voi_estimate`**: the estimated VOI for this compositional experiment, computed from the axis-gap register by summing the expected posterior variance reduction over all axis-to-axis edges expected to be informed by the experiment outcome.

TA1 receives the `CompositionalExperimentRequest`, runs the generative core's compositional conditioning (using the guided compositional generation formulation of section 32b), and returns a `CompositionalQueryResult` containing predicted distributions and estimated discriminating power. TA2 uses this result to refine the VOI score and, if the score exceeds threshold, promote the experiment to the TA3 queue.

---

## 4. The Knowledge-Gap-Identification Boundary Question

### 4.1 The ARPA-H framing

Appendix A states: "The TA1/TA2 boundary for knowledge gap identification is an open question and expects that it will be refined during the program." This is the only interface question the solicitation explicitly names as open. The statement implies that ARPA-H reviewers understand the boundary is non-trivial and will accept a justified placement rather than demanding a fixed answer.

### 4.2 Three placement options

**Option A: Gap detection fully in TA1 (our recommendation).**

TA1 Pillar 4 computes the gap register algorithmically from coverage maps, ontology-space OOD scores, INDRA conflict detection, and posterior uncertainty. With the disease-axis architecture, Pillar 4 additionally computes the axis-gap register from the axis posterior variances and axis-to-axis causal edge credible intervals. The gap register and axis-gap register are structured data objects with uncertainty-weighted scores for each candidate gap. TA2 receives both registers and performs two functions: (a) prioritization of gaps by VOI score against the current experimental queue and budget; (b) translation of abstract gaps into concrete experiment specifications, including compositional experiment requests for axis-targeting gaps.

*Rationale:* gap detection requires domain-specific mechanistic knowledge embedded in the Pillar 1 network, the Pillar 4 ontology-conditioned OOD layer, and the disease-axis deep SCM. An LLM agent without access to the TA1 model state cannot detect that a specific axis-to-axis causal edge is poorly constrained without computing the credible interval from the deep SCM posterior. The mechanistic content is TA1's responsibility; prioritization and translation are TA2's responsibility.

**Option B: Gap detection fully in TA2.**

TA2 agents inspect the TA1 model by querying its uncertainty map and running its own gap-detection reasoning (using LLM-based abductive reasoning or knowledge-graph traversal). TA1 exposes only raw model parameters; the agent interprets them.

*Disadvantage:* this places mechanistic reasoning about the disease model inside the LLM agent, which re-introduces the LLM-wrapper problem. The agent's gap detection would be limited to what the LLM can infer from the parameter distributions, which is less reliable than the Pillar 4 algorithm that operates directly on the ontology-structured knowledge graph and the axis deep SCM.

**Option C: Split, with a joint detection layer.**

A third, jointly governed microservice performs gap detection by consuming TA1's uncertainty maps and running a jointly developed algorithm, logging output accessible to both TA1 and TA2.

*Disadvantage:* this introduces a third architectural component with its own interface, adding complexity and a potential single point of failure. For Phase I, where the goal is a walking skeleton, this is architecturally premature.

### 4.3 Our recommendation: Option A with a thin bidirectional protocol

Place gap detection in TA1 Pillar 4. Expose the gap register and axis-gap register to TA2 via the `GET /gap_register` and `GET /axis_state` APIs. TA2 is responsible for VOI-ranked prioritization and translation into executable experiment specifications, including the composition of axis-targeting requests for axis-causal-structure gaps. The justification is that gap detection requires traversal and coverage computation over the disease-specific causal knowledge graph and the deep SCM over disease axes, both of which are mechanistic content owned by TA1.

The Phase I proposal text should state: "We place knowledge-gap identification in TA1 Pillar 4, which computes coverage-weighted gap registers from the mechanistic network, ontology-conditioned uncertainty layer, and the disease-axis causal structure. TA2 retrieves these registers and applies VOI prioritization and experiment specification, including compositional axis-targeting requests, maintaining a clean division of mechanistic reasoning (TA1) from experimental planning (TA2). We expect this boundary to be refined in the Phase I Domain-Driven Design workshop."

---

## 5. Grounding Mechanisms: How TA2 Queries and Is Constrained by the Model

### 5.1 Posterior query: retrieving the model's distributional state

At each tournament round, the planning engine queries TA1 for the current posterior distribution over the biological processes and disease axes most relevant to the candidate hypothesis set. The query returns:

- **Mean activity shift** per process under the disease perturbation: this is the SAMS-VAE mean effect vector e_t filtered by the mean mask m_t.
- **Posterior variance** per process: the IWELBO-derived variance of the mechanism-shift magnitude.
- **Cross-process covariance**: the off-diagonal terms of the posterior covariance matrix, which encode which process shifts are statistically linked.
- **Disease-axis factor posteriors** (via `GET /axis_state`): the mean and variance of each axis's archetype weight vector, and the posterior probability of each axis-to-axis causal edge in the deep SCM.

This distributional query is the "retrieval" step in MM-RAP. The retrieved object is not a document or a knowledge-graph edge; it is a posterior distribution over causal mechanism parameters and disease-axis factors. The LLM agent uses this distribution to answer the question: "which biological processes are most uncertain, which disease axes are most under-determined, which axis-causal edges are most poorly constrained, and which combination of experiments is most likely to resolve the highest-value gaps?"

### 5.2 Mechanistic critics: checking hypotheses against the causal constraint set

Each hypothesis generated by the tournament passes through a mechanistic critic before ranking. The critic is a dedicated agent that checks the hypothesis against the TA1 causal graph constraint set in two passes, extended by a third pass for axis-specific hypotheses:

**Pass 1: Structural feasibility.**

The critic queries the Pillar 1 Biolink knowledge graph to verify that a directed causal path exists from the proposed perturbation target (a GO molecular function or GO biological process) to the proposed downstream outcome (the disease phenotype encoded as a MONDO term with associated cell-type shifts in CL space). If no path exists in the current graph, the critic flags the hypothesis as structurally infeasible, with a citation of the missing edge.

The path query uses SPARQL over the Biolink-formatted graph, filtered to the biological-process and causal-upstream-of predicates of the Relation Ontology. Paths longer than a configurable hop limit (Phase I default: 5 hops) are flagged as speculative but not rejected, because the graph's sparsity at long range reflects coverage gaps rather than established absence of mechanism.

**Pass 2: Quantitative consistency.**

For hypotheses that pass structural feasibility, the critic runs the Pillar 4 Disease Map pre-simulation (the `POST /simulate` API call described in Section 3.4). It submits the proposed perturbation as an edge mutilation on the SBML-qual Boolean model and checks whether the resulting MaBoSS attractor distribution shifts in the direction predicted by the hypothesis. Hypotheses where the pre-simulation produces an attractor shift of less than epsilon (Phase I threshold: 5% shift in the probability mass of the target disease attractor) are flagged as quantitatively inconsistent.

**Pass 3: Axis-causal consistency (for axis-targeting hypotheses).**

Hypotheses that propose to probe or resolve a specific axis-to-axis causal relationship are checked against the `AxisCausalStructure` object. The critic verifies that the proposed experiment's predicted discriminant is consistent with the direction of the axis-causal edge the hypothesis claims to test, as predicted by the deep SCM's current posterior mean. Hypotheses that target axis-causal edges whose posterior probability already exceeds a confidence threshold (Phase I: 0.90) are deprioritized as already-resolved. Hypotheses that target axis-causal edges with posterior probability near 0.5 (maximum uncertainty) receive a priority boost.

This three-pass critic structure is the distinguishing element of our TA2. A literature-only critic can check whether the hypothesis is mentioned in papers; it cannot check whether the hypothesis is consistent with the mechanistic model's flux predictions or with the axis causal structure.

### 5.3 Test-time mechanistic simulation: pre-screening before the experimental queue

Before any hypothesis is promoted from the tournament ranking list to the TA3 experiment queue, the planning engine runs a pre-screening step that uses the TA1 Disease Map pipeline as a lightweight proxy simulator. This is distinct from the mechanistic critic (which checks consistency) because it estimates the expected information gain: how much would the TA1 model's uncertainty map and axis-gap register change if this experiment were executed and its result were as predicted by the current model?

The estimation procedure is a one-step perturbation of the TA1 model:

1. Simulate the hypothesized experiment result (the predicted perturbagen effect from PDGrapher, or the compositional generative prediction from `POST /compositional_query`) as a new data point.
2. Run a fast posterior update (variational inference, not full MCMC) to compute the updated uncertainty map and axis-gap register.
3. Compute the reduction in total posterior variance across the biological processes and disease axes affected by the hypothesis.
4. This reduction is the estimated information gain, which becomes the VOI score for the hypothesis.

For compositional experiments, steps 1-2 are run for each combination of axes specified in the `CompositionalExperimentRequest`, and the VOI score reflects the expected reduction in axis-causal-structure uncertainty summed over all targeted axis-to-axis edges.

Hypotheses with VOI score below a threshold (Phase I: bottom 25% of the ranked set) are returned to the evolution step of the tournament, where the ontology terms or axis combinations are modified to generate higher-VOI variants.

This pre-screening is the "test-time validation scaling" component described in the TA2 deep-dive Section 4.4, operationalized as a model simulation step rather than a secondary LLM pass.

### 5.4 Anchoring LLM outputs to the model: reducing hallucination

LLM-generated hypothesis text (the narrative justification for each hypothesis) is anchored to the TA1 model via ontology alignment. The Instructor+Pydantic schema-validation layer (see TA2 deep-dive Section 4.5) enforces that:

- Every biological process referenced in hypothesis text maps to a valid GO term present in the Pillar 1 knowledge graph.
- Every disease reference maps to a valid MONDO identifier used in the Pillar 3 shift-space representation.
- Every cell type maps to a valid CL identifier used in the TA4 validated-lab cell-type catalog.
- Every intervention target maps to a valid hub-node identifier from the Pillar 4 hub-node ranked list.
- Every disease-axis reference maps to a valid axis identifier from the `DiseaseAxisSet` currently emitted by TA1.
- Every compositional experiment request references only axis identifiers present in the `DiseaseAxisSet` and perturbation targets present in the hub-node ranked list.

If the LLM generates a process, disease, cell type, intervention target, or disease-axis identifier not in the model's current output, the Pydantic schema validator rejects the output and returns an error that requests a revision restricted to model-grounded terms. This is not a soft prompt instruction; it is a hard structural enforcement via Python type validation.

---

## 6. Comparison to GraphRAG, CausalRAG, and Related Systems

### 6.1 Standard GraphRAG

GraphRAG (Edge et al., Microsoft Research, widely cited 2024-2025; survey in ACM Transactions on Information Systems, 2025, doi:10.1145/3777378) builds a knowledge graph from extracted text entities and relations. The graph encodes what was written in papers. The nodes are named entities; the edges are relations found in sentences.

**The three structural differences from MM-RAP:**

| Property | GraphRAG | MM-RAP |
|---|---|---|
| **Retrieval corpus** | Derivative of text; entities and relations named in papers | Live output of a mechanistic simulation: posterior distributions, coverage fractions, flux predictions, disease-axis factors |
| **Edge semantics** | Literature claims; qualitative | Mechanistic model predictions; quantified with posterior uncertainty; axis-to-axis causal edges with deep SCM posteriors |
| **Update mechanism** | Batch re-indexing of new papers | Event-driven Bayesian update on new experimental data returns; axis causal structure updated on axis-targeted experiments |

### 6.2 CausalRAG

CausalRAG (Wang et al., Findings of ACL 2025, arXiv:2503.19878) adds directionality to the GraphRAG pattern by extracting causal triples from source text and organizing them in a directed causal graph. Retrieval walks the causal graph from seed entities to retrieve causally connected subgraphs.

**Differences from MM-RAP:**

| Property | CausalRAG | MM-RAP |
|---|---|---|
| **Causal edge source** | LLM-extracted from paper sentences | Mechanistic model inference from multi-scale experimental and genomic data; axis causal structure from deep SCM |
| **Edge uncertainty** | Not quantified; binary presence/absence | Posterior probability and credible interval from IWELBO or INDRA belief score; axis-to-axis edges from deep SCM posteriors |
| **Update** | Static; edges do not update from new experiments | Dynamic; edges update with every TA4 data return; axis SCM updates on axis-targeted experiments |
| **Constraint checking** | Not supported | Structural feasibility (path query) + quantitative consistency (pre-simulation) + axis-causal consistency (deep SCM check) |
| **Compositional queries** | Not supported | Compositional axis-and-perturbation experiment requests via `POST /compositional_query` |

### 6.3 NIMMGen

NIMMGen (Guan et al., arXiv:2602.18008, ICML 2026 submission) is the closest published antecedent. It generates code for neural-integrated mechanistic models (NIMMs) using LLMs, refining them through a modeling-verification-reflection loop. The key structural difference: NIMMGen's mechanistic model is an output of the LLM agent, constructed de novo from data for each task instance. There is no pre-existing disease model that the agent queries. The model is a compartment ODE (SIR-type) generated to fit the data, not a four-pillar causal architecture with a disease-axis factorization accumulated over years of biological prior knowledge and experimental data.

MM-RAP treats TA1 as a first-class external object that the agent queries but does not construct. This is the difference between an agent that generates its own mechanistic grounding and an agent that is grounded in an externally maintained mechanistic object, including its disease-axis causal structure. The latter is more faithful to the IGoR requirement that TA2 "interrogate" TA1, implying TA1 is an independent artifact.

### 6.4 GRACE and agentic scientific simulation

GRACE (arXiv:2602.15039, 2026) uses a Monte Carlo particle-physics simulator as the authoritative arbiter of physical validity, with an agent that constructs runnable toy simulations from natural-language prompts. The Agentic Scientific Simulation paper (arXiv:2603.00214, 2026) formalizes this as an execution-grounded interpret-act-validate loop.

Our architecture is structurally aligned with the GRACE/agentic-simulation approach: the TA1 Disease Map pipeline (CaSQ -> SBML-qual -> MaBoSS) plays the role of the simulator; the mechanistic critic's pre-simulation pass plays the role of the validate step; the `POST /compositional_query` endpoint plays the role of a compositional scenario evaluator. The key extension is the Bayesian uncertainty quantification layer and the disease-axis causal structure: our simulator does not just validate hypotheses as consistent/inconsistent; it returns posterior distributions that TA2 uses for VOI scoring, and the disease-axis deep SCM is an additional structured layer of uncertainty not present in GRACE. GRACE operates in a domain with known physical laws; our domain requires inferring the causal law structure from data, both at the biological-process level and at the disease-axis level, which is why the identifiability framework (Zhang et al. NeurIPS 2023, arXiv:2307.06250) is necessary.

### 6.5 Comparison table

| System | Mechanistic model type | Model pre-existing? | Uncertainty quantified? | Updates from experiments? | VOI-guided selection? | Compositional queries? |
|---|---|---|---|---|---|---|
| GraphRAG | Text-graph derivative | No (built from corpus) | No | No (batch re-index) | No | No |
| CausalRAG | Text-extracted causal triples | No (built from corpus) | No | No | No | No |
| NIMMGen | LLM-generated ODE/SIR code | No (generated per task) | No | No | No | No |
| Co-Scientist | None; literature only | N/A | No | No | No | No |
| GRACE | First-principles Monte Carlo | Yes (physics simulator) | No | N/A | No | No |
| Stanford Virtual Lab | AlphaFold structure prediction | Yes (tool call) | No | No | No | No |
| **MM-RAP (ours)** | **TA1 four-pillar causal disease model + disease-axis deep SCM** | **Yes (accumulated across program)** | **Yes (IWELBO posterior + axis SCM posteriors)** | **Yes (Bayesian update, <=24h)** | **Yes (VOI criterion over process and axis uncertainty)** | **Yes (compositional axis+perturbation requests)** |

---

## 7. Alignment to the TA1 and TA2 ISO Objectives and the Phases

### 7.1 TA1 Objective 2 (knowledge-gap identification) and the interface

TA1 Objective 2 requires that the model "update from new experimental data in near-real-time." The interface contract makes this operationally concrete:

- The posterior update trigger (CloudEvents notification from TA2/TA4) fires TA1's Bayesian update pipeline.
- The updated TA1ModelState delta is emitted to TA2 within the Phase-specific latency target.
- The gap register is recomputed from the updated coverage map and emitted to TA2 as a new `KnowledgeGapRegister` object.
- The axis-gap register is recomputed from updated axis posteriors and axis-causal-structure posteriors and emitted as a new `AxisGapRegister` object.

When a TA4 experiment was designed as an axis-targeting experiment (via a `CompositionalExperimentRequest`), the posterior update pipeline additionally updates the `AxisCausalStructure` object, reflecting the new evidence about axis-to-axis causal edges. This is not merely an update to a static knowledge base; it is a recalculation of which axes remain causally ambiguous, which axis-to-axis edges remain poorly constrained, and which hub nodes remain the highest-value targets.

### 7.2 TA2 Objective 1 (hypothesis generation and prioritization) and the interface

TA2 Objective 1 requires that the engine "generate and prioritize experimental hypotheses by interrogating the TA1 disease model." The interface contract makes this operationally concrete:

- Hypotheses are generated from the TA1 gap register and axis-gap register, not from literature searches.
- Prioritization uses both the TA1 uncertainty map (biological-process level) and the axis-gap register (axis level) as inputs to the VOI calculation.
- The mechanistic critic checks each hypothesis against the TA1 causal graph and, for axis-targeting hypotheses, against the `AxisCausalStructure` object.
- Compositional experiment requests target combinations of disease axes identified from the axis-gap register as jointly under-determined.

All operational steps depend on real-time access to the TA1 model state, including the disease-axis objects. A system that reads the TA1 model once at proposal time and generates hypotheses from a snapshot would not satisfy TA2 Objective 1, because the disease-axis causal structure changes with each axis-targeted TA4 data return.

### 7.3 Phase-by-phase interface deliverables

| Phase | TA1-side deliverable | TA2-side deliverable | Interface milestone |
|---|---|---|---|
| **Phase I (18 mo)** | TA1ModelState v1: Pillar 1 network + Pillar 4 gap register; `GET /gap_register`, `GET /hub_nodes`, `GET /axis_state` (k<=4 axes) APIs operational; Disease Map executable containerized; initial `DiseaseAxisSet` with uncertainty; initial `AxisCausalStructure` from Phase I genomic data | Tournament prototype; `POST /simulate` integration; mechanistic critic (structural feasibility pass + axis-causal pass); >=3 experiments proposed, at least one axis-targeting; initial `CompositionalExperimentRequest` schema defined | Walking skeleton: >=1 complete closed loop; interface schema documented including axis objects; IV&V-accessible |
| **Phase II (18 mo)** | Full posterior uncertainty maps via `GET /uncertainty_map`; ghost-edge list; Pillar 3 shift-space snapshot + axis-shift projections; `POST /compositional_query` operational (pairwise axes); update latency <=24 hours for both biological-process and axis-level objects | Full MM-RAP with VOI scoring over process and axis uncertainty; quantitative consistency critic (pre-simulation pass); axis-causal consistency critic; compositional experiment requests; 2+ model backends | Full bidirectional interface demonstrated including compositional axis queries; >=4x cycle-time improvement; >=70% expert-panel high-value rate |
| **Phase III (24 mo)** | Second disease (bipolar) model state including disease-axis extension; update latency <=4 hours | Extension to bipolar disease context including bipolar-specific axis-gap prioritization; >=85% expert-panel high-value rate; >=20 users | Full integration demonstrated on two disease areas; all artifacts open-access |

---

## 8. Prior Art, White Space, and Citations

### 8.1 The white space our interface occupies

The six properties that define the white space (from TA2 deep-dive Section 3.6) map onto the interface contract as follows, with three new properties added for the disease-axis architecture:

1. **A pre-built, experimentally-updatable causal model as the primary retrieval object.** The interface exports the TA1ModelState as the primary retrieval corpus, including the `DiseaseAxisSet` and `AxisCausalStructure`.
2. **VOI-guided experiment selection from the model's uncertainty.** The `GET /uncertainty_map` and `GET /axis_state` queries are the inputs to the VOI calculation.
3. **Mechanistic critics grounded in the model's constraint set.** The `GET /gap_register`, the path-query API, and the `AxisCausalStructure` provide the constraint set for the three-pass critic.
4. **Test-time mechanistic pre-simulation.** The `POST /simulate` API is the pre-simulation endpoint.
5. **Bidirectional interface with TA1.** The posterior update trigger and ModelState delta (including axis-level delta objects) are the return channels.
6. **Ontology-aligned hypothesis templates.** The Pydantic schema validators enforce ontology alignment, extended to axis identifiers.
7. **Compositional conditioning support.** The `POST /compositional_query` endpoint and the `CompositionalExperimentRequest` schema enable TA2 to propose multi-axis, multi-perturbation experiments that the generative core can evaluate under compositional conditioning. This property has no precedent in any published agentic-science system.
8. **Disease-axis causal structure as a queryable, updatable object.** The `AxisCausalStructure` and `AxisGapRegister` make the deep SCM over disease axes a first-class interface object, distinct from the biological-process-level knowledge graph.

Each of these eight properties requires the interface contract specified in Section 3. None can be satisfied by a system that retrieves from text.

### 8.2 Published prior art summary table

| Work | Year | Venue | Relevant to interface | Gap vs. our design |
|---|---|---|---|---|
| GraphRAG (Edge et al.) | 2024 | Microsoft Research | Text-graph retrieval pattern | No mechanistic model; no uncertainty; no update; no compositional queries |
| CausalRAG (Wang et al.) | 2025 | Findings of ACL, arXiv:2503.19878 | Causal triple retrieval | Text-extracted edges; no uncertainty; no update; no axis structure |
| NIMMGen (Guan et al.) | 2026 | arXiv:2602.18008 (ICML) | LLM-generated mechanistic model code | Model generated, not queried; no VOI; no disease-axis factorization |
| GRACE (GRACE team) | 2026 | arXiv:2602.15039 | Simulation-grounded agentic design | Physics domain; no uncertainty quantification; no axis structure; not biological |
| Agentic Sci. Sim. (anon.) | 2026 | arXiv:2603.00214 | Formalism for interpret-act-validate | Model construction, not model-grounded planning; no axis structure |
| BATCHIE Consortium | 2025 | Nature Communications | Bayesian active learning for drug combos | No LLM hypothesis engine; no causal disease model; no axis factorization |
| Co-Scientist (Gottweis et al.) | 2026 | Nature, arXiv:2502.18864 | Tournament hypothesis generation pattern | Literature only; no mechanistic model; no compositional queries |
| Stanford Virtual Lab (Swanson et al.) | 2025 | Nature | AlphaFold as tool in agent | Structure, not causal disease model; no uncertainty; no axis structure |
| BioScientist Agent | 2025 | Surveys literature | KG-augmented biomedical agent | Static KG; no mechanistic simulation; no disease-axis factorization |

### 8.3 Web-search findings (2025-2026 additional prior art)

The 2026 web search surfaces two additional works relevant to the interface design:

**Augmenting LLMs with causal reasoning for planning under uncertainty** (PMC:12901353): applies psychologically grounded causal models to augment LLM planning; relevant to our mechanistic critic design. Does not use a disease model, a disease-axis factorization, or an experimental update loop.

**PersonaAI** (bioRxiv 2026.01.16.699755): dual-phase agentic framework for hypothesis generation and validation in aging research. Closer to a literature-mining agent than a mechanistic-model-grounded planner.

**GRACE** (arXiv:2602.15039) remains the strongest published precedent for simulation-grounded agentic experimental design, and our design should explicitly position against it in the proposal.

---

## 9. Gaps at the Interface and Best-Fit Compositions

### 9.1 Gap 1: TA1ModelState schema not yet formalized, including axis objects

The LinkML schema for `TA1ModelState`, `KnowledgeGapRegister`, `UncertaintyMap`, `HubNodeList`, `DiseaseAxisSet`, `AxisCausalStructure`, `AxisGapRegister`, and `CompositionalExperimentRequest` is described architecturally but not yet implemented. The axis-related objects are new requirements introduced by the research master revision and are the highest-priority additions to the Phase I schema.

**Best-fit action:** The Phase I Domain-Driven Design workshop (required by Appendix A) should produce the formal schema as its primary technical deliverable, covering both biological-process-level and axis-level objects. SIFT's planning stack, which requires a formally specified experiment specification as its input (Kuter, Goldman, Bryce, Beal 2018), provides the downstream constraint that drives the schema design backward from TA3 requirements. The `CompositionalExperimentRequest` schema must additionally satisfy the constraint that the generative core's compositional conditioning API can interpret it without ambiguity.

### 9.2 Gap 2: The `POST /simulate` endpoint latency

The Disease Map pre-simulation (CaSQ -> SBML-qual -> MaBoSS) must run in <60 seconds per hypothesis for the Phase I walking skeleton to be feasible. MaBoSS stochastic simulations over Boolean networks of 50-200 nodes (the expected size of our 22q11DS disease map) typically run in 1-30 seconds depending on node count and sample number. This is feasible but must be validated early in Phase I.

**Best-fit action:** Phase I Month 3 benchmark: run the 22q11DS disease map candidate (TBX1/COMT/DGCR8 -> oligodendrocyte lineage subgraph) through CaSQ + SBML-qual + MaBoSS with 1,000 stochastic trajectories. If runtime exceeds 60 seconds, implement a pre-compiled attractor cache that MaBoSS can query without full re-simulation.

### 9.3 Gap 3: Bidirectional protocol for partial updates

When TA4 returns data from an experiment, TA1 may update only a subset of the biological processes and/or disease axes in its model. The TA2 planning engine needs to know which parts of the model changed and which did not, to avoid unnecessary recomputation of VOI scores for hypotheses unaffected by the update.

**Best-fit action:** Include a delta record in the TA1ModelState versioning system. Each ModelState update emits a `ChangedProcessSet` object listing only the biological process dimensions and disease-axis objects whose posterior distributions changed by more than an epsilon threshold. TA2 updates VOI scores only for hypotheses referencing processes or axes in the `ChangedProcessSet`.

### 9.4 Gap 4: Critic grounding when the TA1 graph is sparse

In Phase I, the Pillar 1 mechanistic network for 22q11DS is sparse in peripheral subgraphs. A hypothesis referencing a GO process with no edges in the current graph will always fail the structural feasibility critic, even if the absence reflects a coverage gap rather than established non-existence of the mechanism. Over-rejection of novel hypotheses in sparse regions is a real risk.

**Best-fit action:** The structural feasibility critic should differentiate between (a) absence of a path in a well-covered subgraph (genuine infeasibility) and (b) absence of a path in a sparse subgraph (coverage gap). The Pillar 4 coverage map provides this distinction: paths that traverse low-coverage regions should produce a "speculative but feasible" flag rather than an outright rejection. Speculative hypotheses are ranked separately and reviewed by the human researcher before entering the experimental queue.

### 9.5 Gap 5: Interpretability of the posterior query for human researchers

The `GET /uncertainty_map` and `GET /axis_state` responses are machine-readable JSON-LD documents. Human researchers reviewing the tournament output need an interpretable summary of why a given hypothesis was selected, including any axis-level reasoning.

**Best-fit action:** Each hypothesis in the tournament output should include a two-sentence provenance statement in natural language, generated by the LLM agent but anchored to the ontology-aligned model gap or axis-causal gap that prompted the hypothesis. Format: "This hypothesis targets [GO:term or axis identifier], which has a posterior variance of [V] (credible interval [CI]) in the current TA1 model. It is the [rank]th highest-value target because [it resolves inconsistency between Pillar 1 assertions A and B / it covers the largest coverage gap in the [domain] subgraph / it addresses a ghost edge between processes X and Y / it probes the axis-to-axis causal edge between axis A and axis B, which has posterior probability [P] and is the most under-determined edge in the axis SCM]."

### 9.6 Gap 6: `POST /compositional_query` latency and Phase I scope

The compositional conditioning query requires running the generative core over combinations of axes and perturbations. For Phase I with k<=4 axes, pairwise combinations produce at most 6 pairs, each requiring a generative forward pass. At inference time, conditional flow matching forward passes over moderate-scale cellular state spaces are expected to run in seconds on a GPU. This is a new latency target not previously specified.

**Best-fit action:** Phase I Month 6 benchmark: run pairwise axis compositional queries over the Phase I 22q11DS axis set (expected k=2-3 axes) through the generative core. Target: <30 seconds per query. If the target is missed, restrict Phase I compositional queries to pre-cached axis combination predictions. Phase II: arbitrary combinations, asynchronous, streaming.

---

## 10. Summary: The Interface as the Program's Technical Backbone

The TA1-to-TA2 interface is not an implementation detail; it is the technical backbone of the IGoR program. Without a specified, versioned, bidirectional interface:

- TA2 cannot satisfy the "not an LLM wrapper" requirement, because it cannot demonstrate that its outputs depend on the TA1 model state in a way that a pure LLM call cannot replicate.
- TA1 cannot satisfy the "near-real-time update" requirement, because there is no defined mechanism by which experimental data triggers a model update with measurable latency.
- The Phase I walking skeleton cannot be demonstrated, because there is no formal specification of what must flow between the TAs for the loop to close.

The interface contract specified here provides that backbone. It places gap detection in TA1 Pillar 4 (extended to cover the disease-axis causal structure), VOI-guided prioritization and experiment specification in TA2, pre-simulation screening at the interface boundary, compositional axis-targeting experiment requests as a new interface class, and posterior update triggering as the return channel. The eight white-space properties are satisfied by specific components of the interface, and the gaps at the interface are addressable by defined Phase I deliverables.

---

## Consolidated References

All citations from TA1 and TA2 deep-dives apply. Interface-specific additions:

**Causal RAG and graph retrieval:**
- Wang, Y., Han, Z., et al. CausalRAG: Integrating Causal Graphs into Retrieval-Augmented Generation. Findings of ACL 2025. arXiv:2503.19878.
- Edge et al. From Local to Global: A Graph RAG Approach to Query-Focused Summarization. Microsoft Research, 2024.
- GraphRAG survey. ACM Transactions on Information Systems, 2025. doi:10.1145/3777378.

**Agentic simulation-grounded agents:**
- GRACE team. GRACE: An Agentic AI for Particle Physics Experiment Design and Simulation. arXiv:2602.15039, 2026.
- Agentic Scientific Simulation. Execution-Grounded Model Construction and Reconstruction. arXiv:2603.00214, 2026.

**Bayesian experiment design:**
- BATCHIE Consortium. A Bayesian active learning platform for scalable combination drug screens. Nature Communications, January 2025.
- Jones, B., et al. A Bayesian active learning strategy for sequential experimental design in systems biology. PMC 2014. doi:10.1186/s12918-014-0102-6.

**NIMMGen (closest agent precedent):**
- Guan, Z., et al. NIMMGen: Learning Neural-Integrated Mechanistic Digital Twins with LLMs. arXiv:2602.18008, ICML 2026 submission. [Verify acceptance status before submission.]

**SIFT planning stack:**
- Goldman, R.P., Trivedi, N., Bryce, D., et al. A Bayesian Model for Experiment Choice in Synthetic Biology. AAAI Fall Symposium. [Verify year.]
- Kuter, U., Goldman, R.P., Bryce, D., Beal, J. XP: Experiment Planning for Synthetic Biology. 2018. [Verify conference and full citation.]
- Bryce, D., et al. Round Trip. ACS Synthetic Biology, 2022. doi:10.1021/acssynbio.1c00305.

**Disease-axis architecture and generative core (internal; restricted):**
- Research Master sections 30.5, 30.6, 31, 31b, 32, 32b. Internal only. Not for citation in external submissions. Where the method must appear in a submission, mark pages "Proprietary" and reference only public-level descriptions.

**Standards:**
- LinkML. Linked data Modeling Language. https://linkml.io.
- CloudEvents specification. https://cloudevents.io.
- Biolink Model. Unni et al. arXiv:2203.13906.
- INDRA. Gyori et al. Mol Syst Biol 2017.
- MaBoSS. Stoll et al. BMC Bioinformatics 2012.
- CaSQ. PMC7575051.

**Citations flagged for verification before submission:**
- Guan et al. arXiv:2602.18008: confirm ICML acceptance status and proceedings citation.
- Goldman, Trivedi, Bryce AAAI Fall Symp: verify year and proceedings.
- Kuter et al. XP 2018: verify full conference citation.
- GRACE arXiv:2602.15039: confirm as published preprint; verify if peer-reviewed venue exists.
- Agentic Scientific Simulation arXiv:2603.00214: confirm as published preprint.
- Gottweis et al. Nature 2026 (Co-Scientist): verify final DOI.
- Swanson et al. Virtual Lab Nature 2025: verify DOI.
- San et al. Nature Comp Sci 2026 (digital twins): verify DOI.

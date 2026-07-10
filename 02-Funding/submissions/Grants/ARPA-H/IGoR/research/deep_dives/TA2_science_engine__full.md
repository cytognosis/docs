# TA2 New Science Engine: A Deep-Dive Review

**Document class:** Internal, journal-grade review. Proprietary content included. Do not distribute.
**Prepared:** 2026-06-14
**Feeds:** IGoR full proposal (Appendix C.1, C.2), Solution Summary, and the TA1-TA2 interface deep-dive.
**Reading time:** approximately 25 minutes.
**If you read one section:** read Section 4 (our TA2 design) and Section 5 (alignment to the IGoR bar). Everything else is scaffolding.

> [!CAUTION]
> SPEAR (Section 32 of the Research Master) is confidential and under anonymous review. It is referenced here as "our perturbation model (restricted section 32)" in accordance with the internal-build firewall. The factorized-PRS (Section 31) is proprietary. Both are cited structurally but their technical content does not appear in this document.

---

## Abstract

The ARPA-H IGoR solicitation requires a TA2 New Science Engine that is "not a wrapper around a frontier LLM" and that interrogates a mechanistic or causal disease model to generate and rank experimental hypotheses. A survey of approximately 18 agentic-science systems (Google Co-Scientist, Sakana AI-Scientist v2, FutureHouse Robin and Kosmos, Stanford Biomni, SciAgents, Microsoft Discovery, NIMMGen, Stanford Virtual Lab, and others) finds that none satisfy this bar: all mine literature and structured databases as their primary retrieval corpus, or run black-box active-learning loops with no mechanistic constraint. CausalRAG (ACL 2025) and related graph-RAG work retrieve over text-extracted causal triples, not over a living simulation model. NIMMGen (arXiv:2602.18008, ICML) is the closest antecedent: it generates code for mechanistic models using LLMs and evaluates them against observational data, but its mechanistic models are generated de novo as epidemiological compartment models, not queried as a first-class causal disease object that accumulates experimental evidence.

Our TA2 New Science Engine closes this gap with three coupled components: (1) a hypothesis tournament in which adversarial critics are grounded in the structured output of the TA1 causal model rather than in literature alone; (2) mechanistic-model-grounded retrieval-augmented planning (RAP), whose retrieval corpus is the TA1 model's uncertainty and coverage maps, not papers; and (3) test-time validation scaling through lightweight mechanistic pre-simulation before any hypothesis enters the experimental queue. SIFT's Bayesian value-of-information ranking and hierarchical experiment planning (Goldman, Trivedi, Bryce; Kuter, Goldman, Bryce, Beal 2018; Bryce et al. ACS Synth Biol 2022) provide the formal planning layer that bridges our engine's ranked experiment targets to TA3 LabOP protocol generation. Together, these components constitute what we term mechanistic-model-grounded retrieval-augmented planning (MM-RAP), a formally distinct capability that no published system provides.

---

## 1. The Agentic-Science Landscape

### 1.1 Architecture patterns

Three architecture patterns dominate the current field.

**Tournament generation-critique-ranking-evolution (TCR).** Pioneered by the Google DeepMind Co-Scientist (Gottweis et al., Nature 2026; arXiv:2502.18864), this pattern uses specialized agents to generate hypotheses, critique them against literature and databases, rank by discriminating power, and iteratively evolve survivors. The LLNL open-ai-co-scientist (github.com/llnl/open-ai-co-scientist, 2024) is an open reimplementation using Claude and Gemini Flash under an OpenRouter backend, with an Elo-based tournament for pairwise hypothesis comparison. Multiple community forks exist (jataware/open-coscientist; Kaimen-Inc/Co-Scientist; raktim-mondol/co-scientist). All use literature and structured databases as the retrieval corpus; none query a mechanistic simulation.

**Autonomous end-to-end experiment loops.** Sakana AI-Scientist v2 (arXiv:2504.08066; ICLR 2025 workshop; open-sourced at github.com/sakanaai/ai-scientist-v2) uses agentic tree search to generate ML research hypotheses, write and execute code experiments, analyze results, and draft manuscripts, producing the first fully AI-generated paper to pass peer review at a workshop level. Its domain is machine learning, not biological mechanism, and it has no causal disease model.

**PI-specialist-critic multi-agent structures.** The Stanford Virtual Lab (Nature 2025) implements a PI agent directing specialist and critic agents for nanobody design, calling AlphaFold as a tool. This is the only field system that calls a structure-prediction model as a first-class tool rather than retrieving from a static database, making it a partial precedent for our TA2 architecture.

### 1.2 System-by-system survey

| System | Open/closed | Approach | Interrogates a mechanistic or causal model? | Key citation |
|---|---|---|---|---|
| Co-Scientist (Google DeepMind, 2026) | Closed (Gemini; Google Labs/Cloud) | TCR tournament; multi-agent generation, critique, ranking, evolution over literature and databases | No; literature/database retrieval only | Gottweis et al., Nature 2026; arXiv:2502.18864 |
| AI-Scientist v2 (Sakana AI, 2025) | Open (GitHub, Apache) | Autonomous ML-research loop; agentic tree search for idea generation; code execution and manuscript writing | No; ML benchmarks only; no biological mechanistic model | arXiv:2504.08066 |
| Biomni / Stanford Biomedical Agent (Huang et al., 2025) | Open | General biomedical agent with approximately 150 curated tools spanning literature, databases, sequence, and structure | No; tool and database retrieval; no mechanistic simulation | Huang et al. 2025 |
| Robin (FutureHouse, 2025) | Open | Literature synthesis and hypothesis generation; long-context paper reading; demonstrated drug repurposing (Ripasudil for AMD) | No; literature and database only | FutureHouse research announcement 2025 |
| Kosmos (FutureHouse/Edison, 2025) | Proprietary | Autonomous data analysis and hypothesis generation; "structured world models" for coherence over 1,500 papers and 42,000 lines of analysis code | No; "world models" are coherence structures over text, not mechanistic simulations | FutureHouse, 2025 |
| AI-Scientist (Sakana, v1, 2024) | Open (GitHub) | Generates, executes, analyzes, and writes ML research | No; ML code benchmarks only | Lu et al. 2024 |
| Coscientist (CMU, Nature 2023) | Open | Autonomous chemistry: GPT-4 plus hardware control APIs for wet-lab operations | No; chemistry wet-lab tools, no causal disease model | Boiko et al., Nature 2023 |
| ChemCrow (2023) | Open (MIT license) | GPT-4 plus 18 chemistry tools | No; chemistry tool belt only | Bran et al. 2023 |
| Stanford Virtual Lab (2025) | Open | PI plus specialist plus critic agent structure for nanobody design; calls AlphaFold as a tool | Partial; AlphaFold structure prediction is used as a tool, but it is not a causal disease model | Swanson et al., Nature 2025 |
| SciAgents (MIT, 2024) | Open | Knowledge-graph multi-agent hypothesis generation; graph-relation traversal | No; static graph relations, not dynamic causal simulation | Ghafarollahi and Buehler, arXiv:2409.05556 |
| Microsoft Discovery | Proprietary (Azure) | Enterprise knowledge graph plus agentic R&D pipeline; simulator hooks available | Partial; simulator hooks exist but no published mechanistic disease model is in the retrieval loop | Microsoft, 2025 |
| Lila Sciences | Proprietary | AI-directed science factory with integrated robotic labs; active-learning closed loop | No; active learning with black-box mechanism; no causal disease model | |
| Periodic Labs | Proprietary | AI plus robotic physical-science laboratories | Unclear; focus is materials and physical science | |
| NIMMGen (Guan et al., arXiv:2602.18008, 2026) | Early/open (ICML) | Agentic framework that generates code for neural-integrated mechanistic models (NIMM) using LLMs; iterative refinement via modeling, verification, and reflection agents | Partial; generates mechanistic model code from data, but models are constructed de novo by the agent rather than queried as a living, experiment-updated causal object | Guan et al., arXiv:2602.18008 |
| Agentic digital twins (Nature Comp Sci, 2026) | Research | LLM-orchestrated simulation environments as digital twins for experimental design | Partial; concept and framework, not a deployed disease system; twins are reactive rather than experiment-integrated | San et al., Nature Comp Sci 2026 |
| LLNL open-ai-co-scientist (2024) | Open (GitHub) | Open reimplementation of Co-Scientist tournament pattern; Elo ranking; integrated arXiv search | No; literature retrieval only | github.com/llnl/open-ai-co-scientist |

### 1.3 Supporting infrastructure (not hypothesis-generating agents)

- **BioContextAI:** MCP-grounding registry for biomedical tool access; middleware, not an agent.
- **ToolUniverse (Harvard, 2025):** protocol for 1,000-plus tool interactions; open.
- **AutoGen/AG2:** debate and critique framework; agent backbone, not a science engine.
- **LangGraph:** stateful backbone for multi-step agent workflows.

### 1.4 The architectural gap

The gap in the field is structural, not incremental. Current agentic-science systems treat the retrieval corpus as a static artifact: papers in a vector store, database entries, static graph edges. No system makes the living output of a mechanistic or causal simulation model the primary retrieval object.

This is not a limitation of LLM capability. It is an architectural choice: existing systems were not designed to receive structured, probabilistic output from a mechanistic model (unconstrained parameter sets, hypothesized edges, inconsistent flux predictions) and use that output to select the highest-value experiment. The IGoR solicitation names this gap precisely in its "not a wrapper around a frontier LLM" bar and its requirement that TA2 "interact with and interrogate" the TA1 comprehensive disease model (Appendix A).

---

## 2. Planning and Value of Information: SIFT and the Broader Literature

### 2.1 The optimal-experiment-design literature

The fundamental problem of experiment selection under a mechanistic model is formalized as **Bayesian optimal experimental design (BOED)**: choose the experiment a* that maximizes the expected information gain I(theta; y | a) = H(theta) - E_y[H(theta | y, a)], where theta are unobserved model parameters and y is the experimental outcome. This mutual-information objective is the formal equivalent of the value-of-information (VOI) heuristic used in planning literature.

Key recent results in biology:

- **BATCHIE** (Nature Communications, January 2025): Bayesian active learning platform for scalable drug combination screening, explicitly maximizing mutual information between screening outcomes and model parameters. This is the cleanest biological instantiation of BOED for experiment selection.
- **Bayesian active learning for systems biology** (Jones et al., PMC 2014): shows that automatic BOED supports kinetic parameter estimation in systems-biology ODE models, a direct precedent for using BOED against a mechanistic network model.
- **PDGrapher** (Gonzalez et al., Nature Biomedical Engineering, 2025; doi:10.1038/s41551-025-01481-x): two-phase GNN over the causal graph; Phase 1 proposes perturbagens shifting diseased to healthy states (inverse design); Phase 2 predicts response. Our TA1 adopts PDGrapher directly (Section 30 of the Research Master).

### 2.2 SIFT: Bayesian VOI and hierarchical experiment planning

SIFT (Smart Information Flow Technologies, Minneapolis) has developed the most directly relevant planning stack. The key publications are:

- **Goldman, Trivedi, Bryce et al., "A Bayesian Model for Experiment Choice in Synthetic Biology."** AAAI Fall Symposium. Presents a formal Bayesian VOI model for ranking experiment candidates in a synthetic-biology design-build-test-learn (DBTL) context. The model computes the expected reduction in model uncertainty for each candidate experiment, selecting the one that maximizes information gain. This is the formal grounding for our "highest-value-of-information experiment" language.

- **Kuter, Goldman, Bryce, Beal. "XP: Experiment Planning for Synthetic Biology." 2018.** Hierarchical experiment planning: decomposes a high-level campaign goal into sub-experiments with dependencies, resources, and timing, producing a structured plan that can be handed to a laboratory execution system. This is the formal precedent for the TA2-to-TA3 interface our architecture requires.

- **Bryce, Goldman, Beal et al., "Formalizing Sample Transformation Plans."** AAAI Fall Symposium. Formalizes the sample-transformation protocol: the sequence of physical operations (pipetting, incubation, measurement) required to execute a planned experiment. This is the bridge from the abstract experiment plan to the LabOP protocol representation.

- **Bryce et al., "Round Trip: Automated Pipeline for Experimental Design, Execution, and Analysis."** ACS Synthetic Biology, 2022. doi:10.1021/acssynbio.1c00305. Demonstrates a fully automated DBTL loop in synthetic biology (yeast logic circuits), integrating the planning stack with lab automation. Establishes SIFT's automation and reproducibility pedigree. The domain is synthetic biology; generalization to mammalian iPSC workflows requires validation.

- **Eslami, Moseley, Eramian, Bryce, Haase. "AutoGater."** Scientific Reports, 2024. ML-based flow-cytometry gating for quality control in the DBTL loop.

**Fit with our engine.** Our TA2 chooses what to test and why (the VOI selection from the TA1 causal model). SIFT's planning stack converts that ranked experiment target into a scheduled, resource-allocated, executable plan that hands off to LabOP. This is the TA2-to-TA3 interface IGoR scores. SIFT acts as a scoped TA2 planning-and-scheduling contributor under Cytognosis TA2 lead; the disease-model-grounded hypothesis engine stays with Cytognosis.

**Domain caveat.** SIFT's planning track record is in synthetic biology. The generalization to mammalian iPSC, live-cell imaging, scRNA-seq, and electrophysiology workflows must be explicitly validated during Phase I.

### 2.3 Relationship between BOED, VOI, and our engine

The three components of our engine map precisely onto the classical BOED framework:

| BOED concept | Our TA2 instantiation |
|---|---|
| Prior over model parameters theta | TA1 causal model parameter distributions, coverage maps, and edge uncertainty |
| Experiment design space A | TA4 validated-lab modality set (perturbation type, readout, cell type, timepoint) |
| Expected information gain I(theta; y | a) | Estimated discriminating power of each hypothesis ranked in the tournament |
| Design selection a* = argmax I(theta; y | a) | Hub/key-node selector from Pillar 4 of TA1 |
| Posterior update p(theta | y, a*) | TA1 Bayesian parameter update on experimental data return; update latency target Phase II <=24 h |

---

## 3. Grounding LLMs on Mechanistic and Causal Models: GraphRAG and the White Space

### 3.1 Standard GraphRAG

GraphRAG (Edge et al., Microsoft Research; widely cited in 2024-2025) retrieves over a knowledge graph built from extracted text relationships. A GraphRAG survey (ACM Transactions on Information Systems, 2025) defines it as "a subclass of RAG that leverages graph structure to organize and retrieve knowledge, using structural databases where graphs model dependencies among knowledge pieces." The graph is built from text: entities and relations are extracted by an LLM from a document corpus, stored as nodes and edges in a graph database, and retrieved by graph-walk queries.

Key point: the graph is a derivative of text. It encodes what was written in papers, not what the mechanistic model predicts. The nodes are entities named in documents, not parameters with probability distributions derived from experiments.

### 3.2 CausalRAG and causal-graph retrieval

CausalRAG (Wang et al., Findings of ACL 2025; arXiv:2503.19878) introduces directed causal structure into retrieval. It extracts directed causal triples from source text, indexes them in a graph, retrieves causally connected subgraphs via graph walks from query-linked seed nodes, and conditions generation on the causally grounded evidence narrative.

This is the closest published system to our approach in intent: it retrieves causal relationships rather than semantic associations. However, the causal graph is still extracted from text. The edges are claims made in papers, not predictions with quantified uncertainty generated by a mechanistic simulation. CausalRAG does not query a running mechanistic model; it queries a static graph of textual causal claims.

### 3.3 Related work: knowledge-graph-grounded hypothesis generation

- **KG-CoI, SciMON** (2024-2025): graph-structured multi-hop reasoning for hypothesis plausibility, using biomedical knowledge graphs (PrimeKG, OpenTargets). Retrieval is over static graph entries, not dynamic model outputs.
- **MedRAG** (ACM Web Conference 2025): knowledge-graph-elicited reasoning for healthcare; retrieves over a medical ontology graph. Static.
- **SciAgents** (arXiv:2409.05556, MIT): knowledge-graph multi-agent system; traverses static graph edges representing literature-extracted relationships.
- **EpisTwin** (arXiv:2603.06290): knowledge-graph-grounded neuro-symbolic architecture for personal AI; the knowledge graph is a static structured representation, not a dynamic simulation.

None of these systems query a mechanistic model in simulation mode: no system asks the model "what does your posterior predict for pathway X under this perturbation?" and uses that probabilistic output as the retrieval result.

### 3.4 NIMMGen: the closest precedent and its gap

NIMMGen (Guan et al., arXiv:2602.18008, ICML submission) is the most relevant prior work. Its key contributions are:

1. An evaluation framework (NIMM) for LLM-generated mechanistic models under partial observability and diverse task objectives, across public health, clinical health, and materials science.
2. An agentic framework (NIMMGen) with a modeling agent, verification agent, environment engine, and reflection agent that iteratively constructs and refines neural-integrated mechanistic model code.
3. Demonstrated counterfactual intervention simulation using the generated mechanistic models.

**The gap relative to our TA2:** NIMMGen's mechanistic models are generated de novo by the agent from data, as parameterized ODE compartment models (SIR-type for epidemiology). The mechanistic model is an output of the LLM agent, not a structured causal object that the agent queries. There is no prior causal disease model that the agent interrogates. The agent does not select experiments that maximize information gain against an uncertainty map. The models are not updated incrementally from new experiments through a defined Bayesian update API.

### 3.5 The agentic digital twins precedent

San et al. (Nature Computational Science, 2026) describe "the evolution of digital twins from reactive to agentic systems," with the key properties of self-learning, autonomous, and linking models, data, and human interaction. The paper is a conceptual framework. No deployed biological disease system using this architecture has been published.

### 3.6 The white space our TA2 occupies

The white space is defined by six properties that no published system combines:

1. **A pre-built, causal, experimentally-updatable disease model (TA1) as the primary retrieval object.** The corpus is not text or static graph edges; it is the structured, probabilistic output of a living mechanistic simulation: parameter distributions, edge uncertainty, flux inconsistencies, coverage gaps.
2. **VOI-guided experiment selection from the causal model's uncertainty.** The experiment is chosen because it maximally reduces uncertainty in the TA1 model, not because it is mentioned most in papers.
3. **Mechanistic critics in the hypothesis tournament.** Adversarial agents challenge hypotheses on mechanistic grounds using the TA1 constraint set, not just on literature consistency.
4. **Test-time mechanistic pre-simulation.** Before any hypothesis reaches the experimental queue, it is pre-screened by a lightweight mechanistic simulation. This filters infeasible or redundant designs without consuming TA4 resources.
5. **Bidirectional interface with TA1.** New experimental data returns to TA1 through a structured update API, closing the loop. The next planning round uses the updated model, not the same prior.
6. **Ontology-aligned hypothesis templates.** Every hypothesis is structured against MONDO (disease), Cell Ontology, UBERON, and Gene Ontology terms, making the mechanistic basis explicit and human-verifiable.

The term we propose internally for this architecture is **mechanistic-model-grounded retrieval-augmented planning (MM-RAP)**, to distinguish it from standard GraphRAG (text-graph retrieval) and CausalRAG (text-extracted causal triples). The retrieval object in MM-RAP is a running mechanistic model with quantified uncertainty, not a derivative of text.

---

## 4. Our TA2 New Science Engine

### 4.1 Core positioning

**Committed verbatim:** "This is explicitly not a wrapper around a frontier large language model."

The mechanistic model is the first-class queryable object. Literature evidence is used to ground and critique hypotheses, never to generate them. Every experiment proposal traces directly to a specific gap or inconsistency in the TA1 causal model.

Leadership: Cytognosis co-leads TA2 with Phylo (creator of Biomni; Kexin Huang, PhD). IPAI provides support. DataTecnica is the named alternate TA2 partner if Phylo is unavailable.

### 4.2 Component 1: Hypothesis tournament

The tournament runs four stages: generate, critique, rank, evolve.

**Generate.** Hypotheses originate in gaps detected by the TA1 Pillar 4 ontology-conditioned gap finder: under-constrained parameters in the mechanistic network, under-explored ontology subtrees where model interpolation is unreliable, and flux inconsistencies across the multi-scale model. All hypotheses take the fixed template:

> "Perturbing pathway/process X will shift the disease phenotype in disease Y toward healthy by modulating Z."

Because X, Y, and Z are ontology terms (Gene Ontology, MONDO, Cell Ontology), every hypothesis is machine-readable, alignable across datasets, and traceable to a specific TA1 model gap.

**Critique.** Adversarial critic agents challenge each hypothesis on two grounds: (a) mechanistic feasibility against the TA1 causal graph constraint set; (b) literature consistency, using scispaCy and medspaCy for negation and context-aware evidence extraction, and Instructor plus Pydantic for schema-validated, ontology-aligned evidence aggregation. The mechanistic critique is the differentiating layer; the literature critique is secondary.

**Rank.** Hypotheses are ranked by estimated discriminating power, operationalized as the expected reduction in TA1 model uncertainty if the proposed experiment were executed. This is the VOI criterion. SIFT's Bayesian VOI model (Goldman, Trivedi, Bryce) provides the formal planning layer.

**Evolve.** Low-ranking hypotheses are revised by modifying the ontology terms or the proposed intervention target, guided by the TA1 coverage map. High-ranking survivors are passed to Component 2.

The tournament pattern is established in the literature (Co-Scientist, LLNL open-ai-co-scientist). Our key departure is that adversarial critics are grounded in the mechanistic constraint set, not only in literature retrieval. This is not an incremental change; it is a structural one, because it makes the discriminating criterion the TA1 model's uncertainty rather than citation frequency.

### 4.3 Component 2: Mechanistic-model-grounded retrieval-augmented planning (MM-RAP)

**The retrieval corpus is TA1's structured output, not papers.** Specifically, the planning engine queries:

- Under-constrained parameter sets with uncertainty bounds (from Pillar 1 and Pillar 2 of TA1)
- Hypothesized edges flagged as under-evidenced by the coverage map
- Inconsistent flux predictions across the multi-scale model
- Under-explored ontology subtrees (from Pillar 4 OOD gap detection)

The hub/key-node selector from Pillar 4 identifies transcription factors and signaling nodes whose perturbation is predicted to maximally shift disease-relevant downstream biology. These become the prioritized experiment targets.

The experiment specification produced by MM-RAP is detailed enough for TA3 protocol generation: cell type (Cell Ontology term), perturbation target (GO term plus gene identifier), timepoint, and readout modality. SIFT's hierarchical experiment planner (XP; Kuter et al. 2018) then converts this specification into a scheduled, resource-allocated plan that the LabOP protocol layer can execute.

**Why this differs from GraphRAG.** In GraphRAG, the retrieval corpus is a graph built from text. The nodes are entities named in papers; the edges are relations extracted from sentences. In MM-RAP, the retrieval corpus is the live output of a mechanistic simulation with quantified parameter uncertainty. The "documents" being retrieved are posterior parameter distributions, not paper abstracts. The "retrieval query" is a request for the regions of the model with highest posterior uncertainty, not a semantic similarity search.

**Why this differs from CausalRAG.** CausalRAG retrieves directed causal triples extracted from text by an LLM. The edges represent causal claims made in papers. In MM-RAP, the edges represent causal links inferred by a mechanistic model from multi-scale experimental and genomic data, each with a posterior probability and an uncertainty bound. The graph is a product of inference, not of text extraction.

### 4.4 Component 3: Test-time validation scaling

Before a hypothesis enters the experimental queue, the engine runs lightweight mechanistic pre-simulations to filter infeasible or low-information designs. Pre-screening checks include:

- Consistency with known causal graph structure in TA1 (does the proposed perturbation have a connected path to the target outcome in the network?)
- Feasibility within the TA4 validated-lab modality set (is the required readout available in a validated TA4 lab?)
- Non-redundancy with already-executed experiments (has this hypothesis or a close variant already been tested, and what was the result?)

Hypotheses surviving pre-screening are formatted as explainable narratives with ontology-aligned evidence traces and ranked for human researcher review. Consequential actions (experiment submission to TA3) require explicit human authorization.

### 4.5 Open scaffolding stack

The engine is built on open, swappable components. The core reasoning loop has no dependency on closed-source frontier model APIs.

| Layer | Technology | Rationale |
|---|---|---|
| Stateful backbone | LangGraph | Persistent multi-step agent state across the tournament rounds |
| Debate and critique | AutoGen/AG2 | Multi-agent debate with explicit critic roles |
| Explainable critique traces | Anthropic Agent SDK | Audit trails for mechanistic reasoning steps |
| Biomedical tool access | ToolUniverse; BioContextAI (MCP-grounded) | Access to 1,000-plus curated biomedical tools and databases |
| Hypothesis extraction | Instructor plus Pydantic | Schema-validated, ontology-aligned LLM output |
| Ontology-aware NER | scispaCy; medspaCy | Negation and context-aware biomedical entity recognition |
| Planning layer | SIFT XP planning stack | Hierarchical experiment plan generation and VOI ranking |
| Protocol handoff | LabOP (SIFT TA3) | Standardized protocol for TA3 execution |

By Phase II, at least two model backends including at least one open-weight model are required by the IGoR solicitation.

### 4.6 Go/no-go metrics

| Phase | Metric |
|---|---|
| Phase I | >=3 proposed experiments executed with cross-lab reproducibility; >=50% rated high-value by an expert panel; orchestration architecture documented; interfaces to TA1 and TA3 demonstrated |
| Phase II | >=2 model backends (>=1 open-weight); usability study with >=10 domain scientists; >=70% find the system useful; >=75% of proposed experiments rated high-value; designs produce measurable TA1 improvement |
| Phase III | >=85% high-value; demonstrated on bipolar disorder (second disease area); design efficiency quantified against a conventional baseline; >=20 researchers including external users; >=80% find useful |

An internal benchmark worth restoring in the full proposal: Spearman r >=0.4 between hypothesis rank and experimental effect size on the first 10 experiments executed.

---

## 5. Alignment to the TA2 ISO Objectives, Phases, and the Not-an-LLM-Wrapper Bar

### 5.1 The IGoR TA2 objectives

Appendix A specifies two TA2 objectives:

1. **TA2.O1: Hypothesis generation and prioritization.** The system must generate and prioritize experimental hypotheses by interrogating the TA1 comprehensive disease model, not by literature retrieval alone.
2. **TA2.O2: Explainability and human interface.** The system must produce hypotheses with traceable mechanistic reasoning that human researchers can interrogate, validate, and override.

Both objectives are structurally satisfied by our three-component design. The tournament and MM-RAP satisfy TA2.O1; the ontology-aligned hypothesis templates, explainable critique traces, and human-authorization gate satisfy TA2.O2.

### 5.2 The not-an-LLM-wrapper bar

Appendix A states: "Systems that merely prompt an LLM to suggest experiments and route them to an automated laboratory do not meet the requirements of this program."

Our design fails this disqualification criterion on three independent grounds:

1. The retrieval corpus is the TA1 mechanistic model's structured output, not an LLM's parametric knowledge. An LLM that does not have access to the TA1 model cannot produce the same retrieval results.
2. The adversarial critics are mechanistically grounded in the TA1 causal graph constraint set. A critic that merely retrieves literature will not reject a hypothesis that violates a mechanistic constraint not captured in papers.
3. Test-time validation runs a lightweight mechanistic simulation. A frontier LLM cannot simulate the TA1 model's flux predictions by parametric recall.

### 5.3 Phase-by-phase alignment

| Phase | IGoR requirement | Our TA2 deliverable |
|---|---|---|
| Phase I (18 mo) | Demonstrate closed-loop cycle: TA2 proposes, TA3 generates protocol, TA4 executes, data returns to TA1; walking skeleton | Tournament prototype with TA1 model interface; >=3 experiments proposed and executed; architecture documented; TA1-TA3 interfaces demonstrated |
| Phase II (18 mo) | Integrate with >=2 TA4 labs; >=2 model backends; usability study; >=4x cycle-time improvement | Full tournament with SIFT VOI ranking; open-weight model backend; user study with >=10 scientists; designs produce measurable TA1 improvement |
| Phase III (24 mo) | Second disease area; >=10x cycle-time improvement; >=20 external users | Extension to bipolar disorder (second area); >=85% expert-panel high-value rate; >=20 users including external |

### 5.4 Phase I walking skeleton

The Phase I walking skeleton milestone (Appendix A) requires a demonstrable closed-loop cycle within 18 months. For TA2, this means:

- A running tournament instance that queries the TA1 Pillar 1 coverage map and Pillar 4 gap finder.
- At least 3 experiment proposals reaching TA3 in LabOP protocol format.
- At least 1 experiment executed in a TA4 lab with data returned to TA1.
- A documented TA1-TA2 interface specification (parameter uncertainty format, ontology alignment, hub-node output schema).

---

## 6. Gaps, Best-Fit Components, and Interface Risks

### 6.1 Within TA2

| Gap | Severity | Best-fit mitigation |
|---|---|---|
| Absence of published MM-RAP precedent | High; reviewers may ask for proof-of-concept | NIMMGen (arXiv:2602.18008) is the closest antecedent; cite as precedent, differentiate on the three structural properties (pre-built disease model, VOI selection, bidirectional update) |
| SIFT planning stack validated only in synthetic biology | Medium; generalization to mammalian iPSC and imaging workflows is unvalidated | Phase I explicit validation task: adapt SIFT XP to iPSC-neuron Perturb-seq and live-cell imaging workflows; report generalization results at Phase I review |
| Open-weight model backend not yet specified | Medium; Phase II requirement | Phase I deliverable: benchmark two open-weight models (Llama 3.x, Mistral-class) against Claude baseline on hypothesis quality; select primary open-weight backend by end of Phase I |
| Spearman r metric dropped from full-proposal milestone table | Low; affects internal validation | Restore Spearman r >=0.4 as an internal go/no-go benchmark; consider including in the Phase I milestone table in Appendix C.2 |
| AutoGen/AG2 multi-agent coordination latency at scale | Low; engineering risk | Phase I architecture review; LangGraph's stateful backbone provides natural checkpointing |

### 6.2 At the TA1-TA2 interface

| Interface requirement | Gap | Recommended action |
|---|---|---|
| TA1 must emit structured uncertainty output (parameter uncertainty maps, edge confidence, coverage gaps) in a format TA2 can query | TA1 Pillar 4 interface specification not yet formalized | Phase I Domain-Driven Design workshop must produce a formal schema (JSON-LD or RDF) for TA1 uncertainty output; document as a Phase I milestone |
| TA2 must produce ontology-aligned experiment specifications that TA1 can ingest as posterior update triggers | Bidirectional protocol not yet specified | Include a formal TA1-TA2 data contract in the Phase I architecture documentation |
| Hub/key-node selector output must be queryable at runtime | Pillar 4 is described architecturally but not yet implemented | Phase I software deliverable: a working Pillar 4 hub-selector API with a defined schema |

### 6.3 At the TA2-TA3 interface

| Interface requirement | Gap | Recommended action |
|---|---|---|
| SIFT XP plan output must map to LabOP protocol primitives | The SIFT plan-to-LabOP compilation step is not yet implemented | Phase I deliverable: an adapter layer between SIFT XP output and LabOP primitives; validate on one iPSC-neuron Perturb-seq protocol |
| TA2 experiment specification must include sufficient detail for LabOP (cell type, perturbation, timepoint, readout) | Specification schema not yet formalized | Define schema in Phase I DDD workshop; include in Appendix C.2 technical plan |

---

## References

1. Bartley, B.A., et al. Building an Open Representation for Biological Protocols (PAML to LabOP). ACM JETC 19(3), 2023. doi:10.1145/3604568.
2. BATCHIE Consortium. A Bayesian active learning platform for scalable combination drug screens. Nature Communications, January 2025.
3. Bereket, M. and Karaletsos, T. Modelling Cellular Perturbations with the Sparse Additive Mechanism Shift Variational Autoencoder. NeurIPS 2023. arXiv:2311.02794.
4. Boiko, D.A., et al. Autonomous chemical research with large language models. Nature 2023. [Coscientist]
5. Bran, A.M., et al. ChemCrow: Augmenting Large Language Models with Chemistry Tools. 2023.
6. Bryce, D., et al. Round Trip: Automated Pipeline for Experimental Design, Execution, and Analysis. ACS Synthetic Biology, 2022. doi:10.1021/acssynbio.1c00305.
7. Bunne, C., et al. How to Build the Virtual Cell with Artificial Intelligence: Priorities and Opportunities. Cell 187, 7045-7063, 2024. doi:10.1016/j.cell.2024.11.015.
8. Eslami, M., Moseley, R., Eramian, H., Bryce, D., Haase, S. AutoGater. Scientific Reports, 2024.
9. Ghafarollahi, A. and Buehler, M.J. SciAgents: Automating Scientific Discovery through Multi-Agent Intelligent Graph Reasoning. arXiv:2409.05556, 2024.
10. Goldman, R.P., Trivedi, N., Bryce, D., et al. A Bayesian Model for Experiment Choice in Synthetic Biology. AAAI Fall Symposium. [Exact year to be confirmed against SIFT records; cite as Goldman et al., AAAI Fall Symp.]
11. Gonzalez, G., et al. PDGrapher: A GNN framework for perturbation design. Nature Biomedical Engineering, 2025. doi:10.1038/s41551-025-01481-x.
12. Gottweis, J., et al. Towards an AI co-scientist. Nature, 2026. [arXiv:2502.18864; also referenced as Nature 2026 publication; verify DOI.]
13. Guan, Z., et al. NIMMGen: Learning Neural-Integrated Mechanistic Digital Twins with LLMs. arXiv:2602.18008, 2026. [ICML submission; verify final proceedings citation if accepted.]
14. Huang, K., et al. Biomni: A general biomedical agent. 2025. [Phylo; verify publication venue and arXiv ID.]
15. Jones, B., et al. A Bayesian active learning strategy for sequential experimental design in systems biology. PMC 2014. doi:10.1186/s12918-014-0102-6.
16. Kuter, U., Goldman, R.P., Bryce, D., Beal, J. XP: Experiment Planning for Synthetic Biology. 2018. [Verify conference and year.]
17. Lu, C., et al. The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery. Sakana AI, 2024. github.com/SakanaAI/AI-Scientist.
18. Microsoft Research. AI-Powered Scientific Discovery: Microsoft Discovery. 2025.
19. San, O., Rasheed, B., Bozdemir, B., et al. The evolution of digital twins from reactive to agentic systems. Nature Computational Science, 2026.
20. Sakana AI. The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via Agentic Tree Search. arXiv:2504.08066, 2025. github.com/sakanaai/ai-scientist-v2.
21. Swanson, K., et al. The Virtual Lab: AI Agents Design New SARS-CoV-2 Nanobodies with Experimental Validation. Nature, 2025.
22. Wang, Y., Han, Z., et al. CausalRAG: Integrating Causal Graphs into Retrieval-Augmented Generation. Findings of ACL 2025. arXiv:2503.19878.
23. Zhang, J., et al. Identifiability Guarantees for Causal Disentanglement from Soft Interventions. NeurIPS 2023. [Verify arXiv ID: arXiv:2307.06250 as cited in Research Master section 30.]

**SIFT citations (LabOP and protocol standards):**
- Bartley et al. (2023) covers PAML/LabOP; see item 1 above.
- Goldman, Trivedi, Bryce: item 10 above.
- Kuter, Goldman, Bryce, Beal (2018): item 16 above.
- Bryce et al. ACS Synth Biol 2022: item 6 above.

**Citations flagged for verification before submission:**
- Gottweis et al. Nature 2026: arXiv:2502.18864 confirmed; verify final DOI.
- Guan et al. arXiv:2602.18008: confirm ICML acceptance status.
- Huang et al. Biomni 2025: verify arXiv ID and venue.
- Swanson et al. Virtual Lab 2025: verify DOI.
- San et al. Nature Comp Sci 2026: verify DOI.
- Goldman, Trivedi, Bryce AAAI Fall Symp: verify year and proceedings citation.
- Kuter et al. XP 2018: verify conference and full citation.
- Zhang et al. NeurIPS 2023: verify arXiv ID (candidate: arXiv:2307.06250).

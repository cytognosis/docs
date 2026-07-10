## 33. Our contribution: TA2 New Science Engine

**Core positioning (committed verbatim):** "This is explicitly not a wrapper around a frontier large language model." Of approximately 15 agentic-science systems surveyed (Co-Scientist, Robin/Kosmos, Biomni, SciAgents, the Stanford Virtual Lab, OpenScientist, Coscientist, Lila Sciences, and others), none interrogate a mechanistic or causal disease model to generate hypotheses. All mine literature and databases, or run black-box wet-lab loops with active learning but no mechanistic constraint.

**What makes TA2 distinct:** TA2 treats the TA1 causal model as a **first-class queryable object**. It identifies unconstrained parameters, hypothetical edges, and inconsistent predictions, then proposes the experiment with the highest value of information. The mechanistic model grounds every hypothesis; literature evidence is used only to ground and critique hypotheses, not to generate them.

**Leadership:** Cytognosis co-leads TA2 with **Phylo** (creator of Biomni; Kexin Huang, PhD) and IPAI support. Phylo contributes agentic biomedical AI design and multi-agent scientific reasoning. DataTecnica is the named alternate TA2 partner if Phylo is unavailable.

---

### Component 1: Hypothesis tournament

The engine runs a **tournament** of competing causal-link hypotheses with four stages: generate, critique, rank, and evolve.

- **Generate:** Hypotheses are derived from Pillar 4's TA1 gaps (under-constrained parameters, under-explored ontology subtrees) and take the fixed template: "Perturbing pathway/process X shifts disease Y toward healthy by modulating Z."
- **Critique:** **Adversarial critic agents** challenge each hypothesis on mechanistic grounds, not just literature consistency. Critics are grounded in the constraint set of the TA1 causal model.
- **Rank:** Hypotheses are ranked by estimated discriminating power and value of information against model uncertainty.
- **Evolve:** Low-ranking hypotheses are revised or replaced iteratively.

The tournament pattern was established by the DeepMind Co-Scientist design and the open reimplementation at LLNL (open-ai-co-scientist, 2024). Our key departure is that adversarial critics are grounded in mechanistic constraints from TA1, not only literature retrieval.

---

### Component 2: Mechanistic-model-grounded retrieval-augmented planning (RAP)

**The retrieval corpus is TA1's structured output, not papers.** Specifically, the corpus consists of:

- Under-constrained parameter sets with uncertainty bounds
- Hypothesized edges flagged by the coverage map as under-evidenced
- Inconsistent flux predictions across the multi-scale model

Planning queries this corpus to select the experiment that most reduces total model uncertainty (value-of-information selection). The experiment is specified in sufficient detail for TA3 protocol generation: cell type, perturbation target, timepoint, and readout modality.

**Hub selection:** TA2 calls the Pillar 4 hub/key-node selector to identify which transcription factors or signaling nodes, when perturbed, are predicted to maximally shift disease-relevant downstream biology. These become the prioritized experiment targets handed to TA3.

---

### Component 3: Test-time validation scaling

Before surfacing a hypothesis to the experimental queue, the engine runs **lightweight mechanistic simulations** to pre-screen predictions against known biological constraints. This filters low-quality experiment designs before they consume wet-lab resources in TA4.

Pre-screening checks include:

- Consistency with known causal graph structure in TA1
- Feasibility within the TA4 validated-lab modality set
- Non-redundancy with already-executed experiments

Hypotheses that survive pre-screening are formatted as explainable narratives and ranked proposals for human researcher review. Consequential actions (experiment submission to TA3) require explicit human authorization.

---

### Open scaffolding stack

TA2 is built on open, swappable components. No dependence on closed-source frontier model APIs for the core reasoning loop:

| Layer | Technology |
|---|---|
| Stateful backbone | **LangGraph** |
| Debate and critique | **AutoGen/AG2** |
| Explainable critique traces | **Anthropic Agent SDK** |
| Biomedical tool access | MCP-grounded tools via **ToolUniverse** and **BioContextAI** |
| Hypothesis extraction | **Instructor** + Pydantic (schema-validated LLM output) |
| Ontology-aware NER | **scispaCy**, **medspaCy** (negation and context) |

The scaffolding is designed so future open-weight models can be incorporated without re-engineering. At least two model backends, including at least one open-weight model, are required by Phase II.

---

### TA2 go/no-go metrics

| Phase | Metric |
|---|---|
| Phase I | >=3 proposed experiments executed with cross-lab reproducibility; >=50% rated high-value by an expert panel; orchestration architecture documented; interfaces to TA1 and TA3 demonstrated |
| Phase II | >=2 model backends (>=1 open-weight); usability study with >=10 domain scientists, >=70% find the system useful; >=75% of proposed experiments rated high-value; designs produce measurable TA1 improvement |
| Phase III | >=85% high-value; demonstrated on bipolar disorder; design efficiency quantified against a conventional baseline; >=20 researchers including external users, >=80% find it useful |

**Note on a dropped metric:** Earlier drafts (2026-06-02 SS) included an explicit Phase II TA2 metric of end-to-end cycle time <=12 weeks and knowledge generation rate >=3x conventional. The 2026-06-05 SS and the full proposal (FULLPROPOSAL_DRAFT) folded the cycle-time target into the program-level metric (>=4x faster by Phase II, >=10x by Phase III) rather than as a TA2-specific go/no-go. The program-level cycle-time metric now captures this intent. The Spearman r >=0.4 correlation metric (hypothesis rank vs. experimental effect size on the first 10 experiments) was present in the 2026-06-02 SS go/no-go but was not carried forward explicitly into the FULLPROPOSAL_DRAFT milestone table; it remains a useful internal benchmark and should be restored in the full proposal.

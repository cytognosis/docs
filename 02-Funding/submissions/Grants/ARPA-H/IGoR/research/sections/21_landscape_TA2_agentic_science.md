## 21. Landscape: TA2 agentic-science and orchestration systems

This section surveys the approximately 15 agentic-science systems that define the TA2 field. The central finding is that none interrogate a mechanistic or causal disease model to generate hypotheses. IGoR explicitly requires an engine that is "not a wrapper around a frontier LLM." Our TA2 closes that gap.

---

### 21.1 Current agentic-science systems

| System | Open/closed | Approach | Interrogates a mechanistic/causal model? |
|---|---|---|---|
| **Co-Scientist** (Google DeepMind 2025) | Closed (Gemini; Google Labs/Cloud) | Multi-agent hypothesis generation, critique, ranking, and evolution tournaments grounded in literature and database retrieval | No; literature/database retrieval only |
| **AI-Scientist** (Sakana AI 2024) | Open (GitHub) | Autonomous ML-research loop: idea generation, experiment coding, result analysis, paper writing | No; ML code benchmarks only, no biological mechanistic model |
| **Biomni** (Stanford; Phylo 2025) | Open | General biomedical agent with ~150 curated tools spanning literature, databases, sequence, and structure tools | No; tool/database retrieval; no mechanistic simulation |
| **Robin** (FutureHouse 2025) | Open | Literature synthesis and hypothesis generation agent; long-context paper reading | No; literature/database |
| **Kosmos** (FutureHouse 2025) | Proprietary | Automated data analysis and experimental design agent | No; statistical/literature |
| **OpenScientist / AutoScientists** (2025) | Open (Apache 2.0) | Claude-Code subagent teams; self-organizing multi-agent research pipelines | No; data/literature access only |
| **Coscientist** (CMU, Nature 2023) | Open | Autonomous chemistry: GPT-4 + hardware control APIs for wet-lab operations | No; chemistry wet-lab tools, no causal disease model |
| **ChemCrow** (2023) | Open (MIT) | GPT-4 + 18 chemistry tools | No; chemistry tool belt only |
| **Stanford Virtual Lab** (Nature 2025) | Open | PI + specialist + critic agent structure for nanobody design; calls AlphaFold as a tool | Partial; AlphaFold structure tool, not a causal disease model |
| **SciAgents** (MIT 2024) | Open | Knowledge-graph multi-agent hypothesis generation; graph-relation traversal | No; graph relations, not dynamic causal simulation |
| **Microsoft Discovery** | Proprietary (Azure) | Enterprise knowledge graph plus agentic R&D pipeline; simulator hooks available | Partial; simulator hooks exist but no published mechanistic disease model |
| **Lila Sciences** | Proprietary | AI-directed science factory with integrated robotic labs; active-learning closed loop | No; active learning with black-box mechanism; no causal disease model |
| **Periodic Labs** | Proprietary | AI plus robotic physical-science laboratories | Unclear; focus is materials/physical science |
| **NIMMGen** (2026) | Early/open | LLM integrated with mechanistic digital twins for hypothesis generation | Partial; mechanistic digital twins grounding, limited biological scope |
| **Agentic digital twins** (Nature Comp. Sci. 2025) | Research | LLM-orchestrated simulation environments as digital twins for experimental design | Partial; concept/framework, not a deployed disease system |

---

### 21.2 Supporting open infrastructure

Several supporting tools and registries underpin agentic-science systems but are not themselves hypothesis-generating agents:

- **BioContextAI**: MCP-grounding registry for biomedical tool access.
- **ToolUniverse** (Harvard 2025): protocol for 1,000+ tool interactions; open.
- **LLNL open-ai-co-scientist** (github.com/llnl/open-ai-co-scientist): open reimplementation of the Co-Scientist tournament pattern; used as our scaffolding reference.

---

### 21.3 Architecture patterns in the field

The tournament pattern (generate, critique, rank, evolve) pioneered by Co-Scientist is the leading adversarial quality approach. The Stanford Virtual Lab demonstrates the PI-specialist-critic multi-agent structure for scientific reasoning. Retrieval-augmented planning in current systems uses literature and databases as the retrieval corpus.

The key architectural gap is in the retrieval corpus: current systems retrieve papers and database entries. No system retrieves the structured output of a mechanistic causal model, such as unconstrained parameter sets, hypothesized edges with uncertainty bounds, or inconsistent flux predictions.

---

### 21.4 The open-source path

The "fully open DeepMind" combination is not achievable: Co-Scientist is Gemini-based and available only via Google Labs/Cloud. AlphaGenome weights are noncommercial-only. Our open-core path uses open agent scaffolding (LLNL open-ai-co-scientist patterns, or Biomni/OpenScientist patterns) on open or Claude models, calling AlphaGenome and other tools via model-context protocol (MCP) integrations (ToolUniverse, BioContextAI), with open-weight LLM backends in Phase II.

---

### 21.5 Gap we exploit: the IGoR bar

The gap is precise and stated in the IGoR solicitation: no existing system interrogates a mechanistic or causal disease model to generate hypotheses, and none qualify as something other than a wrapper around a frontier LLM.

Our TA2 closes both parts of this gap:

1. **Mechanistic grounding.** The retrieval corpus for our planning system is the structured output of the TA1 causal model: unconstrained parameters, hypothesized edges, inconsistent flux predictions, and network coverage gaps. Literature is used only to ground hypotheses, not to generate them.

2. **Not an LLM wrapper.** Mechanistic grounding via TA1, multimodal experiment design via TA3, and distributed validated execution via TA4 provide capabilities no frontier LLM can supply by itself. The agent explains its reasoning through ontology-aligned hypothesis templates and evidence traces that make the mechanistic basis explicit.

The architecture has three components: (a) a tournament of competing causal-link hypotheses with adversarial critics grounded in mechanistic constraints; (b) mechanistic-model-grounded retrieval-augmented planning whose corpus is TA1 output; and (c) test-time validation via lightweight mechanistic simulations that pre-screen hypotheses before they consume experimental resources.

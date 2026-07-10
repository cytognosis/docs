# IGoR TA1 / TA2 — Research and Positioning

**Date:** 2026-06-02 · Expands the Gemini "AI Scientific Discovery Tools Comparison" with current (2026) research, for the IGoR Solution Summary. Cytognosis leads **TA1 (mechanistic disease models)** and **TA2 (the New Science Engine)**; Cellanome covers TA3/TA4.

## Strategic read (the wedge)

1. **TA2 differentiation:** of ~15 agentic-science systems surveyed, **none interrogate a mechanistic/causal disease model** to generate hypotheses, they mine literature/databases (Co-Scientist, Robin/Kosmos, PaperQA2, SciAgents, STORM, Biomni) or run black-box wet-lab loops (Lila, Periodic Labs). IGoR explicitly wants an engine that is "not a wrapper around a frontier LLM." A TA2 that treats the **Cytoverse causal model as a first-class queryable substrate** (identify unconstrained parameters, hypothetical edges, inconsistent flux; propose experiments that most reduce model uncertainty) is the open gap and a defensible wedge.
2. **TA1 differentiation:** the field is dominated by **correlational embeddings** (cell foundation models) and perturbation predictors; truly **mechanistic, multiscale, causal, experimentally-updatable** disease models barely exist, and **none link molecular → circuit for neuropsychiatric disease**. Cytognosis's single-cell atlases + perturbation modeling + systems-biology networks are exactly that integration, anchored on **22q11DS** (strong circuit phenotypes, no molecular-to-circuit causal chain yet).
3. **Open-core reality:** **Co-Scientist is not open** (Gemini-based Google Labs/Cloud product; only third-party reimplementations exist, e.g., LLNL's). **AlphaGenome** code is Apache 2.0 but **weights are noncommercial-only** (fine for a 501(c)(3) research use; needs an H100). A "fully open DeepMind combo" is infeasible as stated. **Open-core path:** open agent scaffolding (LLNL open Co-Scientist reimplementation, or AutoScientists/Biomni patterns) on Claude or open models, **calling AlphaGenome-PyTorch as a tool**, with MCP tool-grounding (ToolUniverse, BioContextAI). More on-brand than depending on a closed product.

## TA2 — the New Science Engine: expanded landscape

| System | What it is | Open? | Reasons over mechanistic/causal models? |
|---|---|---|---|
| Co-Scientist (DeepMind) | Multi-agent gen/critique/rank/evolve tournaments | No (Gemini; Labs/Cloud) | No (literature/DB) |
| AI-Scientist (Sakana) | Autonomous ML-research loop | Yes (GitHub) | No (ML only) |
| Biomni (Stanford) | General biomedical agent, 150 tools | Yes | No (DB/tool) |
| Robin/Kosmos (FutureHouse) | Hypothesis + data-analysis agents | Robin open; Kosmos proprietary | No |
| OpenScientist / AutoScientists | Claude-Code subagents; self-organizing teams | Yes (Apache 2.0) | No (data/literature) |
| BioContextAI | MCP grounding registry | Yes | No (middleware) |
| ToolUniverse (Harvard) | 1,000+ tool interaction protocol | Yes | No (tool belt) |
| Coscientist (CMU, Nature 2023) | Autonomous chemistry experiments | Yes | No (wet-lab tools) |
| ChemCrow | GPT-4 + 18 chemistry tools | Yes (MIT) | No |
| Stanford Virtual Lab (Nature 2025) | PI+specialist+critic agents (nanobodies) | Yes | Partial (AlphaFold tool) |
| SciAgents (MIT) | Knowledge-graph multi-agent hypotheses | Yes | Graph relations, not dynamic models |
| Microsoft Discovery | Enterprise graph + agentic R&D | Proprietary (Azure) | Partial (simulator hooks) |
| Lila Sciences | AI "science factory" + robotic labs | Proprietary | Active learning, black-box mechanism |
| Periodic Labs | AI + robotic physical-science labs | Proprietary | Unclear |

**Architecture for our TA2 (satisfies IGoR's explainable / evolvable / not-an-LLM-wrapper bar):** tournament **generation → critique → ranking → evolution** (adversarial quality) + **retrieval-augmented planning where the "corpus" is mechanistic-model outputs, not just papers** + **test-time validation scaling** (run mechanistic simulations to validate before surfacing). Substrates: LangGraph (stateful backbone), AutoGen/AG2 (debate), Anthropic Agent SDK (explainable critique), MCP via ToolUniverse/BioContextAI (tool/model grounding). Nascent prior art to cite: NIMMGen (LLM-integrated mechanistic digital twins, 2026); "agentic digital twins" (Nature Comp. Sci. 2025).

## TA1 — Comprehensive Disease Models: SOTA and the gap

| Tool / effort | Scale | Mechanistic? | Causal? | Auto-updates? |
|---|---|---|---|---|
| scGPT / Geneformer / scFoundation / UCE | cell | No | No | No |
| TranscriptFormer / scPRINT(-2) | cell | No | Partial (GRN) | No |
| Arc STATE (270M cells, Tahoe-100M) | cell | Partial | Partial (CRISPR) | No |
| insitro TherML | cell/tissue | Partial | Partial | Partial (proprietary) |
| GEARS / CPA / scGen | cell | Partial | Partial | No |
| CARNIVAL / COSMOS / NicheNet (systems bio) | molecular network | **Yes** | **Yes** (within prior net) | No |
| AlphaGenome / Enformer / Borzoi | sequence-regulatory | Yes (grammar) | Partial | No |
| Virtual Brain Twin (TVB) | circuit/system | **Yes** | Partial | clinical loop only |
| **IGoR TA1 target (ours)** | **molecular→circuit** | **Yes** | **Yes** | **Yes** |

**The gap:** most "virtual cell" models are correlational; the few mechanistic tools (systems-biology networks; the Virtual Brain Twin) are single-scale and not experimentally-updatable; **no platform integrates atlas + perturbation + causal-graph + circuit into a disease-specific, auto-updating multiscale model.** That integration is exactly what IGoR TA1 asks for, and what a single-cell + systems-biology PI is uniquely positioned to build. **22q11DS** is the ideal anchor: a single locus (incl. TBX1, COMT, DGCR8) → cell-type pathology → thalamocortical/fronto-temporal circuit deficits → psychosis risk; the molecular-to-circuit chain is missing and formalizing it is the deliverable.

## Consortium mapping for the proposal

- **TA1 (Cytognosis, lead):** mechanistic, multiscale, causal 22q11DS→transdiagnostic model (molecular→cell→circuit), auto-updated from Cellanome experiments.
- **TA2 (Cytognosis, lead):** open, mechanistic-model-grounded orchestration engine (tournament + model-grounded RAP + validation scaling). The field's gap.
- **TA3/TA4 (Cellanome):** R3200 (programmable CellCage + live imaging + scRNA-seq) as the interoperable protocol + experiment-marketplace node; ≥2 TA4 labs.
- **IPAI (Ananth Grama + Anne Carpenter):** TA1 reinforcement (physical-AI, mechanistic modeling) + pooled optical screening (Carpenter), tying to the 22q11.2 phenomics+transcriptomics line of work.
- **Open-core:** open scaffolding + AlphaGenome(-PyTorch) as a tool; Apache 2.0 / CC BY releases.

## Key sources

Co-Scientist (DeepMind blog; Nature 2026; LLNL open reimpl github.com/llnl/open-ai-co-scientist); AlphaGenome (github.com/google-deepmind/alphagenome_research; STAT 2026-01-28, noncommercial weights); Stanford Virtual Lab (Nature 2025); SciAgents (arXiv 2409.05556); CZI "How to Build a Virtual Cell" (Cell 2024); Arc STATE (arcinstitute.org); causal ML for single-cell (Nature Genetics 2025); Virtual Brain Twin (virtualbraintwin.eu, 2025); 22q11DS brain signatures (Mol Psychiatry 2024). Full URL list in the two research subagent returns logged this session.

# IGoR Research Master: Scientific and Technical Source of Record

**ARPA-H IGoR (ARPA-H-SOL-26-155); internal consolidation of methods landscape and our key contributions**

Compiled 2026-06-14 | Profile: **shareable** (excludes restricted sections)

> [!NOTE]
> This is the **source of record** for the science and technology behind the IGoR proposal: the external methods landscape and our key contributions as expressed across proposal variants. It is compiled from modular section files in `sections/` by `build.py`. Edit the section files, not this compiled output.

> [!CAUTION]
> **Restricted sections** (the proprietary factorization method, a perturbation model under review, and the Phase I personal-genomic anchor) appear only in the `internal` build. The `shareable` build drops proprietary, personal, and internal-decision sections; treat it as an internal working draft and review it before any external or partner use, and mark proprietary pages "Proprietary" in any ARPA-H submission.

**How to build:** `python build.py --all` produces both profiles in markdown and PDF. Use `--profile shareable` for the partner-safe version. PDF rendering uses pandoc with weasyprint; diagrams are embedded as figure images from `../figures/` so they render in both markdown and PDF.

## Section index

- [Executive overview](sections/00_executive_overview.md)
- [Core thesis: disease as the causal perturbation operator](sections/10_thesis_disease_as_perturbation.md)
- [Landscape: TA1 disease models and virtual-cell methods](sections/20_landscape_TA1_virtual_cell.md)
- [Landscape: TA2 agentic-science and orchestration systems](sections/21_landscape_TA2_agentic_science.md)
- [Landscape: TA3 protocol standards and TA4 lab automation](sections/22_landscape_TA3_TA4_standards_labs.md)
- [Theory: causal representation learning and identifiability](sections/23_causal_representation_theory.md)
- [Landscape: standards for disease knowledge and cellular models](sections/24_landscape_disease_and_model_standards.md)
- [Our contribution: TA1 four-pillar disease-model architecture](sections/30_contrib_TA1_architecture.md)
- [Our contribution: TA2 New Science Engine](sections/33_contrib_TA2_engine.md)
- [Our contribution: TA3 and TA4 execution stack](sections/34_contrib_TA3_TA4_execution.md)
- [Our contribution: the IGoR standards stack](sections/35_contrib_standards_stack.md)
- [Disease strategy and evidence base](sections/40_disease_strategy_and_evidence.md)
- [Penetrant schizophrenia genetics and the familial-disease rationale for cellular models](sections/42_penetrant_schizophrenia_genetics.md)
- [Metrics, milestones, and quantitative targets](sections/50_metrics_and_targets.md)
- [Team, consortium, and cost model](sections/60_team_consortium_and_cost.md)
- [Consolidated references and verification status](sections/99_references.md)


---

## 00. Executive overview

> [!TIP]
> **If you read one thing:** we propose the only IGoR TA1 that treats **disease-associated genetic variation as the causal perturbation operator** on a self-updating, multiscale, mechanistic model of cellular biology, then drive a non-LLM-wrapper reasoning engine (TA2) and a validated execution loop (TA3, TA4) from it. Section 10 states the thesis; sections 30 to 34 state how we build it.

**What this document is.** This is the consolidated scientific and technical source of record for the IGoR proposal. It holds two things: the **external methods landscape** (sections 20 to 23) and **our key contributions** as they have stabilized across proposal variants (sections 30 to 70). It is the master that the one-pager, Solution Summary, and full proposal are refined from.

**The program in one paragraph.** ARPA-H IGoR (ARPA-H-SOL-26-155) funds approximately three teams over five years to build a closed loop: TA1 mechanistic disease models, a TA2 New Science Engine that finds gaps and designs experiments, a TA3 interoperable protocol stack, and a TA4 validated-lab marketplace. The marquee metric is a **10x reduction in experimental cycle time** by Phase III. Full solicitation truth lives in `../materials/IGoR_Comprehensive_Reference.md`.

**Our approach in five moves.**

1. **TA1, four pillars** (section 30): a cell-type-aware mechanistic network; a causal generative model in which genotype acts as a sparse soft intervention; a joint cellular and clinical shift-space; and ontology-conditioned experiment design. Required properties: modular, mechanistic, multiscale, verifiable.
2. **The crown-jewel factorization** (section 31, proprietary): patient genetic variation factorized into sparse, pathway-disentangled, transdiagnostic axes that double as candidate biotypes.
3. **TA2 New Science Engine** (section 33): a hypothesis tournament, mechanistic-model-grounded retrieval-augmented planning, and test-time validation scaling. Explicitly not a wrapper around a frontier LLM.
4. **TA3 and TA4 execution** (section 34): an open layered protocol stack (SIFT, TA3 lead; Daniel Bryce lead, Robert Goldman advisory; confirmed) plus a validated multi-lab marketplace with two experimental arms: Matt Tegtmeyer lab (Purdue, academic; fixed-cell high-plex readouts: RNA ~350-plex, protein ~50-plex, Cell-Painting-style morphology, in-situ CRISPR-guide sequencing) and Cellanome (industry; R3200 + Perturb-LINK). Anne Carpenter (IPAI/Purdue, confirmed) provides computational morphology and imaging models across both arms (no wet bench). Illumina is TA4.2 (sequencing and bioinformatics, proposed).
5. **Disease strategy** (section 40): 22q11.2 deletion syndrome as the Phase I cellular anchor, idiopathic schizophrenia as the required second area, with a cautious bipolar extension.

**Where the proposal stands (2026-06-18).** A **multi-performer consortium at $50M**, **IPAI/Purdue as prime** with Ananth Grama as PI, Cytognosis and IPAI jointly leading TA1 and TA2. SIFT confirmed as TA3 lead (Bryce/Goldman). Anne Carpenter confirmed at IPAI/Purdue (computational, no wet bench). Elham Jebalbarezi Sarbijan (tentative) fills the Software/Systems Architect seat. Transfyr and SPOC declined 2026-06-18. Section 60 holds the team and cost model; section 70 traces how we got here; section 90 lists what is still open.

> [!CAUTION]
> **Restricted sections (31, 32, 41) are internal only.** They contain the proprietary factorization, a perturbation model under anonymous review, and a personal-genomic Phase I anchor. They appear only in the `internal` build and must never enter partner-facing or public submission text.

### How to navigate

| If you want | Read |
|---|---|
| The one-line bet and why it is novel | Section 10 |
| What others have built and where the gap is | Sections 20 to 23 |
| What we build, pillar by pillar | Sections 30, 33, 34 |
| Disease rationale and evidence | Section 40 |
| Targets we must hit | Section 50 |
| Who is on the team and what it costs | Section 60 |
| How the proposal evolved | Section 70 |
| What is unresolved before submission | Section 90 |


---

## 10. Core thesis: disease as the causal perturbation operator

> [!IMPORTANT]
> **The bet:** existing virtual-cell and perturbation models learn the effects of experimentally delivered perturbations (a CRISPR knockout, a compound). We instead treat **disease, specifically disease-associated genetic variation across patient cohorts, as the causal perturbation operator** acting on a latent causal model of cellular biological processes. This single reframing is what makes our TA1 mechanistic, multiscale, and clinically grounded rather than correlational.

### Why this is the right frame

Most foundation models of the cell are **correlational**: they learn a static representation and predict expression, but they do not encode which molecular events cause which downstream changes, and they do not update when new experiments arrive (section 20). Perturbation predictors add partial causality but stay at one scale and one objective. None integrate atlas-scale data, causal-network inference, and circuit-level physiology into a model that **updates from new experiments**. That integration is our TA1, and the disease-as-perturbation frame is what unlocks it.

### Three components of the thesis

1. **Disease genotype as a soft intervention.** A patient's risk variants act as a sparse, partially specified intervention on unobserved latent biological processes. This is exactly the setting for which **identifiability guarantees exist** for causal disentanglement from soft interventions (Zhang et al. 2023), and it inherits the sparse-mechanism-shift structure of **SAMS-VAE** (Bereket and Karaletsos 2023) and the sVAE lineage (section 23).
2. **Polygenic variation as sparse mechanism identification.** Rather than collapsing risk into a single score, we factorize patient genetic variation into a small number of pathway-disentangled, transdiagnostic axes. The factorization method is proprietary and is documented in restricted section 31; its precedent and the precise novelty claim against **PRSet** are stated there.
3. **Disease axes as a disentangled causal representation.** The recovered axes double as **candidate biotypes**: interpretable coordinates that connect genotype to cell-type pathology to circuit-scale dysfunction, and that TA2 can target for the highest-value experiments.

### The inversion, stated precisely

> We invert the virtual-cell paradigm (Bunne et al. 2024) so that disease-associated genetic variation acts as a soft intervention on a latent causal model of cellular biological processes, for which identifiability guarantees exist (Zhang et al. 2023).

This is the committed novelty sentence used across the Solution Summary and full proposal. It is defensible, specific, and tied to named prior art, which is what ARPA-H reviewers reward.

### What stays constant across every proposal variant

Section 70 shows the team, budget, and disease title all changed over time. The thesis did not. The constants are: a **self-updating, multiscale, mechanistic causal TA1**; a TA2 that is **not a wrapper around a frontier LLM**; and **22q11.2 deletion syndrome** as the Phase I cellular anchor. Treat these three as the load-bearing claims to protect in any revision.


---

## 20. Landscape: TA1 disease models and virtual-cell methods

This section surveys the methods our TA1 builds on or differentiates from, organized by class. All evaluation claims are drawn from the cited literature.

---

### 20.1 Correlational single-cell foundation models

**Correlational foundation models** learn universal representations (URs) of cell state via self-supervised objectives on large single-cell atlases. They excel at embedding, annotation, batch integration, and transfer learning. None natively support causal perturbation prediction.

| Method | What it does | Causal? | Multiscale? | Auto-updating? |
|---|---|---|---|---|
| **scGPT** (Cui et al. 2024) | Transformer on ranked gene expression; pre-trained on ~33M cells | No | No | No |
| **Geneformer** (Theodoris et al. 2023) | Transformer with expression-rank tokenization; 30M cell corpus | No | No | No |
| **scFoundation** (Hao et al. 2024) | Read-depth-aware pre-training; 50M cells | No | No | No |
| **UCE** (Rosen et al. 2023) | Universal cell embedding; multi-species | No | No | No |
| **TranscriptFormer** | Large-scale cross-species transcriptome FM | No | Partial (GRN head) | No |
| **scPRINT / scPRINT-2** | GRN-aware cell-state encoder; partial causal structure in GRN head | Partial | Partial | No |

The 2025 Arc Institute Virtual Cell Challenge demonstrated that no pure foundation model outperformed conventional statistical methods on perturbation prediction (Eisenstein, Nature 2026). This gap motivates the shift toward world-model and causal architectures.

---

### 20.2 Perturbation predictors

**Perturbation predictors** model the effect of experimentally delivered genetic or chemical interventions on cell state. They are more directly relevant to disease modeling but treat interventions as discrete, observed labels rather than soft causal operators.

| Method | What it does | Causal? | Multiscale? | Auto-updating? |
|---|---|---|---|---|
| **GEARS** (Roohani et al. 2024) | GNN over gene ontology graph; multigene combinatorial perturbation prediction | Partial | No | No |
| **CPA** (Lotfollahi et al. 2023) | Compositional perturbation autoencoder; additive latent shifts | No | No | No |
| **scGen** (Lotfollahi et al. 2019) | Style-transfer VAE for perturbation response | No | No | No |

GEARS incorporates biological graph structure but not latent causal identifiability. CPA and scGen model perturbation effects as additive or style shifts without causal disentanglement.

---

### 20.3 Causal sVAE lineage (mechanism-sparsity models)

The **sparse mechanism-shift** lineage applies causal representation learning to single-cell perturbation data. This is the closest family to our TA1 causal generative core.

| Method | What it does | Causal? | Multiscale? | Auto-updating? |
|---|---|---|---|---|
| **sVAE** (Lachapelle et al. CLeaR 2022) | Mechanism sparsity regularization for nonlinear ICA; permutation-identifiable latents | Yes | No | No |
| **sVAE+** (Lopez et al. CLeaR 2023) | Applies sVAE to single-cell genomics; Beta-Bernoulli sparse bipartite graph between perturbations and latent biological processes | Yes | No | No |
| **SAMS-VAE** (Bereket and Karaletsos NeurIPS 2023) | Sparse additive mechanism-shift VAE; z = basal + additive sparse perturbation effects; IWELBO training | Yes | No | No |
| **sVAE-ligr** (Hediyeh-zadeh et al. ICLR 2024 MLG) | Extends sVAE to latent intervention labels via Generative Replay; mechanism transportability across modalities | Yes | No | No |
| **Zhang et al. DSCM** (Zhang et al. NeurIPS 2023) | Identifiability guarantees for soft interventions on latent causal DAGs; DSCM decoder; CD-equivalence class recovery | Yes | No | No |
| **SENA-discrepancy-VAE** (de la Fuente et al. ICLR 2025) | Causal identifiability with latent factors constrained to GO biological-process space; current leading edge of causal + interpretable + omics | Yes | Partial | No |

The SAMS-VAE architecture is our direct mechanism-shift backbone. Zhang et al. provide the formal identifiability guarantees. SENA provides the pathway-space conditioning precedent. None of these models treat disease-associated polygenic variants as the intervention signal.

---

### 20.4 Virtual-cell world models and large systems

**World models** support action-conditioned simulation rather than static embeddings; they are the next generation of the AIVC agenda (Bunne et al. Cell 2024).

| Method | What it does | Causal? | Multiscale? | Auto-updating? |
|---|---|---|---|---|
| **AIVC / Bunne et al.** (Cell 2024) | Conceptual framework: predictive-generative-queryable trifecta; maps research agenda | Conceptual | Conceptual | No |
| **VCWM / AIDO** (Xing and Song, GenBio AI 2026) | Operational definition: encoder E + transition core F + decoder D; p(x' \| x, a, e) | Partial | Partial | No |
| **AlphaCell** (Chuai et al. bioRxiv 2026) | Three-component world model; OT-CFM flow over 220M cells + 90M perturbed profiles; genome-wide Virtual Cell Space | Yes (OT-CFM) | No | No |
| **STACK** (Dong et al. bioRxiv 2026) | In-context learning for single-cell biology; 149M cells; Perturb Sapiens whole-organism perturbation atlas | Partial (ICL) | Partial | No |
| **X-Cell / X-Atlas** (Wang et al. bioRxiv 2026) | Diffusion LM; 25.6M CRISPRi Perturb-seq cells; 4.9B params (X-Cell-Ultra); power-law scaling; multi-modal priors | Yes | No | No |
| **Arc STATE** (Adduri et al. 2025) | 270M cells; population-level kernel alignment loss; CRISPR perturbation training | Partial | No | No |
| **CellFlow** (Palma et al. ICLR 2024 MLG) | Flow-matching generative model in raw count space; OT-CFM on Negative Binomial parameters | Partial | No | No |

AlphaCell and X-Cell represent the current frontier in scale and perturbation coverage. Neither treats disease-associated genetic variation as the causal perturbation operator; both are anchored to CRISPR/chemical perturbation paradigms.

---

### 20.5 Systems-biology and network tools

These tools model molecular mechanism explicitly but operate at a single scale and are not experimentally self-updating.

| Method | What it does | Causal? | Multiscale? | Auto-updating? |
|---|---|---|---|---|
| **CARNIVAL** (Liu et al. 2019) | Integer linear programming over signaling networks to find causal paths consistent with omics data | Yes | No | No |
| **COSMOS** (Dugourd et al. 2021) | Combines CARNIVAL with metabolomics; multi-omics causal network | Yes | Partial | No |
| **NicheNet** (Browaeys et al. 2020) | Ligand-receptor signaling model; cell-cell communication | Yes | No | No |
| **Virtual Brain Twin** (TVB; virtualbraintwin.eu 2025) | Computational brain circuit model; data-assimilation loop with clinical imaging | Yes | Circuit only | Partial (clinical) |

The Virtual Brain Twin is the closest single-scale mechanistic comparator; it operates at the circuit level only, without a molecular or cellular causal layer.

---

### 20.6 Genomic regulatory tools

| Method | What it does | Causal? | Multiscale? | Auto-updating? |
|---|---|---|---|---|
| **AlphaGenome** (Google DeepMind 2025) | Sequence-to-regulatory grammar; gene regulatory predictions from DNA; Apache-2.0 code, noncommercial weights | Yes (grammar) | No | No |
| **Enformer** (Avsec et al. 2021) | Deep learning from sequence to gene expression and chromatin; 200 kb context | Yes (grammar) | No | No |
| **Borzoi** (Linder et al. 2023) | Long-range sequence model; 524 kb context; cell-type-specific expression | Yes (grammar) | No | No |

We use AlphaGenome as a tool, not a retrained model, to encode COMT/TBX1/DGCR8 regulatory effects into our network prior layer.

---

### 20.7 Intervention-design GNNs

**PDGrapher** (Gonzalez et al. Nat Biomed Eng 2025) is the key intervention-design baseline. It applies a two-phase graph neural network over an interaction network to (1) propose perturbagens that shift a diseased state toward a healthy target (inverse design), and (2) predict the cellular response to a candidate perturbation, with interventions encoded as edge mutilations on the causal graph. We adopt PDGrapher as our intervention-design component in Pillar 2.

---

### 20.8 Covariance-aware decoders

| Method | What it does |
|---|---|
| **CS-CORE** (Su et al. Nat Commun 2023) | Depth/noise-corrected co-expression from scRNA-seq UMI counts; used as decoder prior |
| **scDesign3** (Song et al. Nat Biotechnol 2024) | Vine-copula-based generative model; preserves gene-gene covariance structure |

Prior VAE-based perturbation models (scVI, SAMS-VAE) use conditionally independent negative-binomial decoders that discard gene-gene covariance. We replace these with CS-CORE-informed vine-copula decoders from scDesign3 to preserve real co-expression structure in reconstructed cells.

---

### 20.9 Gap we exploit

No existing platform integrates single-cell atlas data, perturbation modeling, causal-network inference, and circuit-level physiology into a self-updating multiscale model. Specifically:

- Foundation models are correlational; they cannot be queried for causal mechanism.
- Perturbation predictors treat experimentally delivered knockouts as the only perturbation type; none treat disease-associated polygenic genetic variation as the causal operator.
- The causal sVAE lineage provides identifiability theory but operates on experimental perturbation labels, not disease genotype.
- World models (AlphaCell, X-Cell) scale to massive data but remain anchored to CRISPR/chemical perturbation paradigms with no molecular-to-circuit integration.
- Systems-biology tools (CARNIVAL, NicheNet, Virtual Brain Twin) are single-scale and not experimentally self-updating.

Our TA1 closes this gap by treating disease-associated genetic variation as a soft intervention on a latent causal biological-process model, grounding that model in cell-type-aware network priors and a joint cellular-clinical shift space, and coupling it to a closed experimental loop that returns new data to update the model.


---

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


---

## 22. Landscape: TA3 protocol standards and TA4 lab automation

This section surveys the protocol standards ecosystem and lab-automation landscape relevant to IGoR TA3 (interoperable experimental procedures) and TA4 (validated-laboratory marketplace). The key finding is that no existing stack provides a layered intent-to-hardware abstraction with procedurally locked parameters and an open validated marketplace.

---

### 22.1 Protocol and standards efforts

#### Declarative/machine-readable protocol languages

**LabOP** (Laboratory Open Protocol language) is the most directly relevant open standard. LabOP provides a machine-readable, modality-agnostic protocol language based on RDF/OWL, supporting declarative specification of experimental intent that can be compiled to hardware-specific execution. It is the basis for our TA3 intent layer and is developed by partners at SIFT (Robert Goldman and Dan Bryce, automated-planning experts).

**SiLA 2** (Standardization in Lab Automation, version 2) provides an open gRPC-based communication standard for laboratory instrument interfaces, enabling software to control lab hardware across vendors. SiLA 2 addresses the hardware-interface layer but not the higher-level intent or protocol-semantic layers.

**Autoprotocol** (Transcriptic/Strateos) is a JSON-based protocol format targeting cloud-lab execution. It is vendor-specific and does not abstract across instrument types.

#### Data modeling and schema standards

**LinkML** (Linked data Modeling Language) provides a YAML-based schema-definition language that compiles to JSON Schema, OWL, SHACL, and other formats. We use LinkML to define open schemas for experiment metadata, QC parameters, and data-return packages in our TA3 stack.

**OMEX/COMBINE and SED-ML** provide standards for archiving and re-executing computational models alongside their experimental metadata. **KiSAO** (Kinetic Simulation Algorithm Ontology) supports reproducibility of simulation runs. These standards anchor the computational reproducibility layer of TA1 model archiving.

**FAIR principles and Bioregistry** underpin all data and metadata in our system, with persistent, resolvable identifiers for every entity.

#### Open data standards for imaging

The **Cell Painting Gallery** (Broad Institute / Carpenter lab) and **JUMP** (Joint Undertaking in Morphological Profiling) dataset provide open image-data standards and a reference compendium of morphological profiles for ~116,000 compounds across multiple cell lines, seeding the TA3 morphological-screening layer. The **OASIS/COBA** standards (Open Archive for Spatial Imaging/Serology) extend these principles to spatial omics data.

---

### 22.2 Cloud and automated labs

**Emerald Cloud Lab** (ECL) is the most established cloud-lab platform, providing remote automated execution of a broad set of experimental protocols. ECL demonstrates the feasibility of protocol-driven remote execution but uses a proprietary protocol stack, lacks an open validated marketplace, and is not designed around a mechanistic disease model.

**Lila Sciences** and **Periodic Labs** operate proprietary AI-directed robotic laboratory systems (see Section 21). Both emphasize autonomous active-learning loops without a mechanistic causal model grounding experiment selection.

**CROs (contract research organizations)** such as Panome Bio (TA4 partner; untargeted metabolomics, lipidomics, proteomics; CLIA-certified) provide validated experimental services but do not participate in open marketplace frameworks with machine-readable capability manifests.

---

### 22.3 Phenomics and morphological screening resources

**Cell Painting / JUMP** (Carpenter lab, Broad Institute; JUMP Consortium) provides the largest open reference compendium of cellular morphological profiles. The Carpenter lab's 2025 NeuroPainting paper (Tegtmeyer et al. Nat Commun 2025) directly demonstrates Cell Painting applied to 22q11.2 deletion iPSC-derived neurons, establishing morphological and transcriptomic signatures of the deletion; this directly de-risks our TA4 anchor experiment.

**Cellanome R3200** provides a programmable CellCage platform integrating live-cell imaging with same-cell pooled-CRISPR sequencing (Perturb-LINK), enabling simultaneous morphological and transcriptomic readouts in neuronal models. Cellanome is the **industry experimental arm of TA4**.

**Element Biosciences AVITI24 / Teton CytoProfiling** is the multi-modal same-cell platform used by the **academic experimental arm (Matt Tegtmeyer lab, Purdue)**. It delivers co-detection of RNA (350-plex subcellular), protein and phospho-protein (50-plex), Cell-Painting-style organelle morphology (nucleus, membrane, actin, ER, Golgi, mitochondria), and in-situ CRISPR-guide sequencing (DISS) from fixed cells at subcellular resolution across hundreds of thousands to millions of cells; has a dedicated neuroscience panel. Element = fixed-cell in-situ at massive scale; Cellanome = live-cell temporal. The two platforms are orthogonal/complementary; running the same variant lines on both provides a built-in cross-arm concordance check aligned with the program's concordance gates. Element's Cell-Painting-like morphology output feeds into Anne Carpenter's computational morphology models.

---

### 22.4 What is missing

The landscape lacks three capabilities that our TA3/TA4 stack provides:

1. **A layered intent-to-hardware abstraction with procedurally locked parameters.** Existing protocol languages (Autoprotocol, SiLA) address individual layers without integrating intent, protocol-semantic, calibration, and hardware layers into a unified stack. No existing system implements an RFC-governed process that treats parameter changes as requiring explicit scientific justification.

2. **An open validated marketplace.** Emerald Cloud Lab, Lila, and CROs are proprietary or point-to-point. No open, machine-readable marketplace exists where labs publish validated capability manifests and researchers can direct experiments to validated labs based on those capabilities.

3. **Alignment between protocol standards and a mechanistic disease model.** Existing standards treat protocols as self-contained; none are designed so that protocol outputs feed directly into an updating causal disease model, or so that the disease model drives which parameters the protocol must constrain. Our TA3/TA4 stack is designed around this closed-loop requirement from the start.

---

### 22.5 Our TA3/TA4 stack

The TA3 stack covers four abstraction layers: **intent** (declarative scientific question and quality requirements), **protocol** (standard processes with error handling), **calibration** (parameters and uncertainty standardized across devices, with independent IV&V calibration artifacts), and **hardware** (machine-specific settings isolated behind common interfaces). Parameters with weak scientific justification are locked by default; changes require RFC-governed justification. LinkML-based open schemas define all metadata. The stack supports at least four modalities: live-cell imaging, optical/morphological screening, sequencing-based assays, and functional assays.

TA4 has two experimental arms. The **academic arm** is the **Matt Tegtmeyer lab (Purdue)**, running all wet-lab experiments with fixed-cell high-plex readouts (RNA ~350-plex, protein ~50-plex, Cell-Painting-style morphology, and in-situ CRISPR-guide sequencing). The **industry arm** is **Cellanome** (R3200 + Perturb-LINK; live-cell temporal readouts). **Anne Carpenter** provides the **computational morphology/imaging-model layer** (interpretable models; no wet-lab bench); her models consume readouts from both arms and bridge into TA1/TA2. **Illumina** contributes the Billion Cell Atlas perturbation resource as in-kind resource sharing (Lab 3). Each lab publishes machine-readable capability manifests, validates against shared IV&V calibration artifacts, and demonstrates cross-laboratory concordance (Phase I target: 85%; Phase II and III: 90%).

> [!NOTE]
> **Related:** this section covers protocol-execution standards (how an experiment is run). The model and disease-knowledge representation standards (how disease mechanism is encoded) are in section 24, and the stack we adopt is in section 35.


---

## 23. Theory: causal representation learning and identifiability

This section summarizes the theoretical foundations that underpin the TA1 causal generative model. All claims are drawn from cited literature; this section is conceptual and does not describe our proprietary methods.

---

### 23.1 The sparse mechanism shift hypothesis

The foundational principle of our causal architecture is the **sparse mechanism shift hypothesis** (Schölkopf et al. 2021). The hypothesis states: when an intervention occurs, only a few mechanisms change at a time. Formally, if the data-generating process is governed by a set of causal mechanisms, an intervention on a variable X changes only the mechanism for X, leaving all other mechanisms intact. This sparse change is what distinguishes interventional distributions from observational distributions and is what makes causal structure learnable from multi-environment data.

The sparse mechanism shift is the correct prior for biological perturbation data: a CRISPR knockout of gene X, or a disease-associated variant at locus Y, perturbs a small number of downstream biological process mechanisms rather than globally reorganizing the cell's regulatory state.

---

### 23.2 Mechanism sparsity regularization and identifiable disentanglement (sVAE)

Lachapelle et al. (CLeaR 2022) translated the sparse mechanism shift into a practical disentanglement algorithm via **mechanism sparsity regularization**. The key result (Theorem 5 in Lachapelle et al.): if the latent factors of interest depend sparsely on observed auxiliary variables (perturbation labels) via a causal graphical model (CGM), then regularizing the learned CGM to be sparse recovers the latent variables up to permutation equivalence.

The implementation is a VAE-based model, called **sVAE**, where:

- Latent factors z_1, ..., z_p each represent a distinct biological process.
- Each perturbation label a_k connects to a sparse subset of latent factors via the bipartite adjacency G^a (the "action-to-latent" graph).
- Regularizing G^a toward sparsity forces the model to allocate each perturbation to a minimal, disentangled set of biological process dimensions.
- The recovered latent factors are permutation-identifiable: the model cannot confuse two distinct biological processes, up to an arbitrary reordering of the latent dimensions.

This established the first principled, identifiable disentanglement method grounded in causal theory for biological perturbation data.

---

### 23.3 Sparse mechanism shift in single-cell genomics (sVAE+)

Lopez et al. (CLeaR 2023) applied the sparse mechanism shift framework directly to single-cell genomics. **sVAE+** treats each genetic or chemical perturbation as a stochastic soft intervention targeting an unknown, sparse subset of latent variables. The key biological interpretation: each latent unit z_i represents "the activity of a distinct biological process." The sparse bipartite graph G^a learned by the model identifies which biological processes are shifted by each perturbation and by how much.

sVAE+ introduces a Bayesian extension via a Beta(1, K) prior on perturbation-target probabilities, avoiding the hyperparameter sensitivity of the original sVAE binary masks. Models exploiting the sparse mechanism shift hypothesis significantly outperform non-causal baselines on out-of-distribution transfer learning tasks in CRISPR perturbation data.

---

### 23.4 Additive sparse mechanism shifts (SAMS-VAE)

Bereket and Karaletsos (NeurIPS 2023) advanced the framework as **SAMS-VAE** (Sparse Additive Mechanism Shift VAE). The model decomposes perturbed cell state as:

> z_i = z^b_i + z^p_i, where z^p_i = sum_{t} d_{i,t} (e_t * m_t)

Here z^b_i is the basal (unperturbed) state embedding, e_t is a global latent effect vector for perturbation t, and m_t is a binary mask (Bernoulli prior with small alpha) that enforces sparsity. The mask m_t identifies which biological process dimensions are shifted by perturbation t; the global effect vector e_t represents the direction and magnitude of the shift.

The identifiability claim follows directly from the Sparse Mechanism Shift framework: sparsifying the shift mechanism (via m_t) recovers disentangled, perturbation-specific latent subspaces that compose additively for combinatorial generalization. SAMS-VAE was developed in part with contributions from the Cytognosis team at insitro, and its additive decomposition is the immediate architectural predecessor of our TA1 generative core.

---

### 23.5 Identifiability guarantees from soft interventions (Zhang et al.)

Zhang et al. (NeurIPS 2023) provide the deepest formal identifiability theory for our setting. The paper establishes: given **soft interventions** on unobserved latent causal variables, and under a generalized faithfulness assumption, one can recover the latent causal model up to a **CD-equivalence class** (permutation, scale, and shift of latent variables) and predict the effect of unseen combinations of interventions.

Key concepts:

- **Soft intervention**: changes the conditional distribution of a latent variable U_i given its parents, but does not remove the parental dependency (unlike a hard/do-calculus intervention). Disease-associated genetic variants are soft interventions: they shift the activity of a biological process while preserving its regulatory context.
- **Hard intervention**: eliminates the parental dependency entirely (e.g., a complete gene knockout). This is the standard in CRISPR perturbation models.
- **Deep structural causal model (DSCM)**: the decoder architecture proposed by Zhang et al.; models the latent DAG G with nodes representing unobserved causal variables U = (U_1, ..., U_p), where the decoder is a DSCM over this structure.
- **CD-equivalence class**: the set of latent causal models that are statistically indistinguishable from the data; recovery up to this class is the best possible result without additional assumptions.

The paper proves that soft interventions, even when they do not identify the exact mechanism, provide sufficient constraint to guarantee latent causal structure recovery. This is the formal theoretical backbone for why our proposed approach, treating disease-associated genetic variants as soft interventions on a latent biological-process DAG, is identifiable in principle.

The closely related **SENA-discrepancy-VAE** (de la Fuente et al. ICLR 2025) applies causal representation learning with latent factors explicitly constrained to GO biological-process space and provides the current leading edge of causal, interpretable, pathway-grounded single-cell modeling. SENA-style causal identifiability is a design principle for our TA1 extension of SAMS-VAE.

---

### 23.6 The virtual-cell world-model paradigm

The AI virtual cell (AIVC) agenda (Bunne et al. Cell 2024) formally defines the virtual cell as "a multi-scale, multi-modal, large-neural-network-based model capable of representing and simulating the behavior of molecules, cells, and tissues across diverse states," requiring a simultaneously predictive, generative, and queryable system.

Xing and Song (GenBio AI 2026) provide the sharpest operational definition as the **Virtual Cell World Model (VCWM)**, adapting the world-model framework from embodied AI:

> p(x' | x, a, e): next cell state x' conditioned on current state x, action (intervention) a, and cellular environment e.

The VCWM has three components: a structured encoder E mapping multi-modal observations and environment to a latent cellular manifold M, an action-conditioned transition core F that evolves latent state under interventions, and a generative decoder D rendering cross-modally consistent outputs.

The transition core F maps directly to our proposed causal perturbation operator: disease-associated genetic variation constitutes the action a that drives state evolution on the cellular manifold. This transforms the genotype-phenotype problem into action-conditioned latent state evolution, for which identifiability guarantees exist under the soft-intervention framework of Zhang et al.

---

### 23.7 Disease as soft causal intervention: the key reframing

All existing perturbation models treat experimentally delivered genetic knockouts or chemical compounds as the intervention. The intervention is discrete, directly observed, and imposed from outside the cell.

We instead treat disease and disease-associated genetic variation as the causal perturbation operator. This reframing has three theoretical components:

1. **Disease genotype as soft intervention.** Disease-associated variants shift the activity of biological processes in a graded, probabilistic way rather than ablating gene function. This maps onto the soft-intervention identifiability framework of Zhang et al. (2023), providing the theoretical guarantee that disease axes are recoverable from multi-cohort data.

2. **Polygenic decomposition as sparse mechanism identification.** Disease is a polygenic signal: many variants, each with small effect, collectively shift a sparse set of biological process dimensions. Decomposing polygenic genetic scores into biological process components is equivalent to learning the sparse bipartite graph G^a of sVAE/SAMS-VAE from genomic rather than CRISPR perturbation data.

3. **Disease axes as disentangled causal representation.** The output is a set of sparse, biologically disentangled disease axes, each corresponding to a biological process dimension shifted by the disease genotype, recoverable up to CD-equivalence class by the identifiability guarantees of Zhang et al. These axes factorize the genotype-phenotype map and constitute the core scientific contribution of TA1.

This theoretical framing positions our work within the AIVC/VCWM research agenda while addressing the open gap: using the virtual cell to model the biological perturbation that disease imposes on cell state across patient populations, not only the response to an experimenter's discrete intervention.


---

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


---

## 30. Our contribution: TA1 four-pillar disease-model architecture

**Core claim (committed verbatim):** "No platform integrates single-cell atlas data, perturbation modeling, causal-network inference, and circuit-level physiology into a multiscale model that updates from new experiments. That integration is our TA1."

**Unifying design principle:** Everything is represented as a *shift (delta) in pathway space relative to a dataset-specific control*. This shared representation lets cellular (induced) and clinical (natural) evidence aggregate into one causal model, and surfaces disease axes that are robust to model-system artifacts.

**Required model properties:** modular (each pillar is a separable component with a defined interface), mechanistic (typed causal edges, not correlational embeddings), multiscale (molecular to cell-type to circuit), and verifiable (hub-node predictions are falsifiable by TA4 perturbation experiments).

The four pillars flow in sequence, with Pillar 4 feeding back into Pillar 1 via new experiment data:

```
Pillar 1 (Network priors) -> Pillar 2 (Causal generative modeling)
-> Pillar 3 (Joint shift-space) -> Pillar 4 (Ontology OOD + experiment design)
-> (experiments feed back to Pillar 1)
```

---

### Pillar 1: Cell-type-aware mechanistic network

**Harmonization backbone:** The **Molecular Interaction (MI) ontology** (term MI:0190) is the unifying vocabulary. Nine major databases are harmonized into a single typed, deduplicated graph: **STRING, Reactome, Reactome FI, SIGNOR, TFLink, IntAct, BioGRID, OmniPath, and the Co-abundance Atlas**.

**Edge-type taxonomy:**

| Layer (MI top type) | Subtyping basis | Examples |
|---|---|---|
| Functional/causal (MI:2245, MI:0414) | Mechanism class | Signaling, regulatory, metabolic, PTM, epigenetic |
| Molecular/experimental (MI:0045) | Detection method | Direct vs. indirect; high vs. low throughput; physical vs. genetic |
| Predicted (MI:0063) | Data source | Co-expression, text-mining, homology |
| Phenotypic | Genetic | Genetic interactions |

**Neuro-specific layers added on top of the generic prior:**

| Layer | Method/source | Contribution |
|---|---|---|
| Cell-type-specific PPIs | Kasper Lage AP-MS in iPSC-derived neurons; IGF2BP1-3 complex (Lage et al. *Cell Genomics* 2022) | Experimentally validated, neuron-resolved physical edges |
| Cell-type GRNs | **PsychENCODE brainSCOPE** multiome GRNs (snRNA + snATAC, 24 brain cell types) + ChIP-seq (Emani et al. *Science* 2024) | Directed TF-to-target and enhancer-gene edges, cell-type-resolved |
| Cell-type co-expression | **CS-CORE** (Su et al. *Nat Commun* 2023; DOI 10.1038/s41467-023-40503-7) | Depth- and noise-corrected co-expression from scRNA-seq UMIs, used inside generative decoders |

**Coverage map (differentiating design):** We build dedicated tools to map which pathways, processes, and subnetworks each interaction type and technology covers well. This coverage map serves two functions: (a) a confidence prior during model inference, and (b) a direct driver for TA2 to propose experiments targeting under-covered regions.

**TA2 interface:** The coverage map and the set of under-constrained parameters are the primary structured outputs that Pillar 1 exposes to TA2 for value-of-information experiment selection.

---

### Pillar 2: Causal generative modeling

**Mechanism-shift backbone (committed framing):** We extend the sparse additive mechanism-shift model **SAMS-VAE** (Bereket and Karaletsos, *NeurIPS* 2023; arXiv:2311.02794). A cell's latent state is a **basal/healthy state plus sparse additive shifts**. Disease and disease-associated genetic variation enter as **extrinsic factors modeled as sparse mechanism-shifts on the intrinsic basal cell state**.

**Identifiability:** Disease-associated genetic variation is modeled as a **soft intervention** on the latent causal model of cellular biological processes. Identifiability guarantees for this framing exist under Zhang et al. (2023; arXiv:2307.06250), and the pathway-space structure follows de la Fuente et al. (SENA-discrepancy-VAE; ICLR 2025; arXiv:2506.12439).

**Covariance-preserving decoders (departure from prior art):** We replace the independent negative-binomial losses used in scVI and prior SAMS-VAE implementations with **CS-CORE-informed, vine-copula decoders** from **scDesign3** (Song et al. *Nat Biotechnol* 2024; DOI 10.1038/s41587-023-01772-1). Reconstructed cells thereby preserve real gene-gene covariance rather than treating genes as conditionally independent.

**Gene identity encoding:** Gene identity is grounded in regulatory-network topology via a co-expression-aware, perturbation-adaptive gene-identity representation developed by the team (proprietary, under review; see restricted section 32), which captures perturbation-induced functional rewiring.

**GNN-based intervention design (PDGrapher):** We adopt PDGrapher's two-phase graph neural network over the interaction network (Gonzalez et al. *Nat Biomed Eng* 2025; DOI 10.1038/s41551-025-01481-x). Phase 1 proposes perturbagens that shift a diseased state toward a healthy target (inverse design); Phase 2 predicts the response to a candidate perturbation. Interventions are represented as **edge mutilations** on the causal graph.

**AlphaGenome as a tool:** AlphaGenome (Google DeepMind, 2025; Apache-2.0 code, noncommercial weights) provides sequence-to-regulatory-grammar representations for COMT, TBX1, and DGCR8 perturbation effects encoded by causal inference over single-cell multiome data. It is used as a tool, not retrained.

**Pillar 2b is proprietary; the detailed factorization method is held internal.**

---

### Pillar 3: Joint cellular and clinical shift-space

**The failure mode we name (committed framing):** In-vitro-only programs (including prior insitro work, and current efforts at Xaira, Recursion) prioritize interventions that make disease cells look like healthy cells, then use clinical data only afterward to validate. These pipelines often cannot distinguish clinically relevant disease axes because many cellular signatures are artifacts of the model system: iPSC differentiation artifacts, missing glial-neuronal interactions, and missing systemic effects.

**Our contribution:** Every signal, whether from a patient cohort or a dish, is represented as a **shift (delta) in pathway space relative to a dataset-specific control** on both scales. That common representation lets cellular (induced) and clinical (natural) evidence aggregate and reconcile in the same causal model. Disease axes that are consistent across scales are robust to model-system artifacts and are therefore the most likely to be clinically relevant.

**Data sources contributing to both scales:**

- Cellular: TA4 iPSC-neuron Perturb-seq, Cell Painting, live-cell imaging
- Clinical: PGC schizophrenia GWAS (Trubetskoy et al. *Nature* 2022), SCHEMA rare-variant data, PsychENCODE multi-cohort atlas (Ruzicka, Mohammadi et al. *Science* 2024), Open Targets Platform (Falaguera et al. *Nat Commun* 2025)

---

### Pillar 4: Ontology-conditioned OOD generalization and experiment design

**Ontology conditioning (committed table):**

| Domain | Ontology |
|---|---|
| Disease | MONDO |
| Cell type | Cell Ontology (CL) |
| Tissue/brain region | UBERON |
| Process/pathway | Gene Ontology + Pathway Ontology (incl. GO-plus) |

Each ontology is pre-embedded with **box embeddings** using **TransBox** (Xiong et al. 2024; arXiv:2410.14571), an EL++-closed representation where subsumption is encoded as box containment so that is-a transitivity is exact. These embeddings are mapped into the model's latent space via projection heads as conditioning variables.

**Two functions of ontology conditioning:**

1. **OOD generalization:** The model reasons about unseen cell types or disorders by interpolating in ontology space with respect to the closest seen examples.
2. **Gap finding:** Under-explored ontology subtrees, where interpolation is unreliable, become high-value experiment targets for TA2.

**Fixed hypothesis template (committed phrasing):**

> "Perturbing pathway/process X will shift the disease phenotype in disease Y toward healthy by modulating Z."

Because X, Y, Z are ontology terms, each hypothesis is grounded with ontology-aware named entity recognition (spaCy, **scispaCy**, **medspaCy** for negation and context) and templated, schema-validated extraction (**Instructor** + Pydantic) to pull harmonized, ontology-aligned evidence for and against the hypothesis for the TA2 agents.

**Hub/key-node selection (how hypotheses become experiments):** We identify the hubs and key nodes (transcription factors, key signaling biomolecules) whose perturbation is predicted to modulate the largest number of downstream biomolecules in the target process. These are the highest-value experiments for shifting disease cells toward a healthy state; they are handed to TA2 as ranked experiment candidates.

**Feedback to Pillar 1:** Validated experimental data returned from TA4 flows through a structured auto-update API, performing Bayesian parameter updates, flagging newly constrained or inconsistent parameters, and emitting updated uncertainty maps. TA1 update latency target: Phase II <=24 h; Phase III <=4 h.

---

### TA1 go/no-go metrics

| Phase | Metric |
|---|---|
| Phase I | Model explains >=30% of variance in 22q11DS-specific cell-type shifts; first TA4 data return cuts parameter uncertainty >=20%; >=3 mechanistic sub-models; >=3 quantitative knowledge gaps algorithmically detected |
| Phase II | At least one prospective prediction experimentally confirmed in an independent dataset; >=10 sub-models across >=2 scales; update latency <=24 h |
| Phase III | >=15 sub-models across >=3 scales; validated novel hypotheses in both diseases; latency <=4 h; all models deposited open-access in certified executable form |

> [!NOTE]
> **Standards basis:** the representation and causal-knowledge standards behind these pillars are surveyed in section 24; the specific stack we adopt (INDRA and GO-CAM, the Disease Map to SBML-qual route, the OBO/RO/Biolink backbone, and Open Targets anchoring) is in section 35.


### 30.5 The three-latent structural causal model (Pillar 2 refinement)

Pillar 2 factorizes each cell's latent state into **three causal sets of latent variables**, which is what lets the model separate therapy from side effect:

1. **Basal state (intrinsic):** the cell's healthy, intrinsic latent state.
2. **Disease effect:** latent factors driven by disease-associated genetic variation that are **causal on the cell state** (the disease-as-perturbation operator of section 10).
3. **Treatment or intervention effect:** latent factors for an intervention that act on the cell state by **two distinct paths**, either **directly** on the cell state (an off-target or side-effect route) or **indirectly by modulating the disease effect** (the therapeutic route).

The observed cell state is generated from the basal state shifted by the disease effect and the treatment effect, with the treatment entering both directly and through the disease pathway. This makes a clinically critical distinction **identifiable**: whether a candidate intervention improves the phenotype because it **corrects the disease mechanism** or because it **independently pushes the cell state**, which separates efficacy from side-effect liability. It extends the sparse-mechanism-shift and soft-intervention identifiability basis (SAMS-VAE; Zhang et al. 2023) from one intervention type to **disease and treatment as separate, composable causal operators**, jointly constrained by perturbation data (Perturb-seq, the phenotypic-triage screen) and clinical cohorts.


### 30.6 Genomic front-end and generative core (public-level overview)

The disease model begins from **pretrained genomic foundation models** (AlphaGenome, VariantFormer, Evo 2) that embed gene bodies and regulatory regions from sequence. These embeddings are contextualized on a **gene functional network** through multiresolution graph diffusion, then factored into a small set of **interpretable, sparse disease-axis factors**. The axes condition a **compositional, multimodal conditional-flow-matching generative model** and serve as **exogenous variables of a structural causal model** that learns how the axes causally interact (the disease-effect operator of the three-latent SCM in section 30.5). The detailed method, including the factorization and the generative-model extensions, is proprietary and is documented in restricted sections 31 and 32. A potential collaboration on the sequence-to-embedding step is noted in the team tracker.


---

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


---

## 34. Our contribution: TA3 and TA4 execution stack

**Role in the loop:** TA3 translates TA2 experiment designs into instrument-agnostic, reproducible protocol specifications. TA4 executes those protocols across a network of validated laboratories and returns QC-rich, model-ready data to TA1.

---

### TA3: Layered Interoperable Protocol Stack (SIFT lead)

**Lead:** **SIFT** (Robert Goldman, PhD and Dan Bryce, PhD), developers of LabOP, leads TA3. SIFT engages equipment makers and standards bodies and participates in program bake-offs.

**Four-layer stack:** Each experiment design from TA2 traverses four abstraction layers:

| Layer | What it encodes |
|---|---|
| **Intent** | Declarative scientific question, quality requirements, success criteria |
| **Protocol** | Standard processes with error handling and versioned parameter sets |
| **Calibration** | Parameters and uncertainty standardized across devices; IV&V calibration artifacts |
| **Hardware** | Machine-specific settings, isolated behind common interfaces |

This layering separates scientifically meaningful parameters from arbitrary local lab preference, which is the core IGoR reproducibility requirement. Changes to locked-default parameters go through a **Request-for-Comments (RFC) process** backed by evidence; the RFC log is a durable audit trail.

**Open standards backbone:** The TA3 stack is built on the **LabOP** lineage with **LinkML-based open schemas** for all protocol representations. All protocol versions are archived and versioned. Carpenter's open image-data standards (Cell Painting Gallery, JUMP dataset, OASIS/COBA) and Cellanome's documented SOP-based workflows seed the TA3 standard at program start.

**Modality coverage (Phase I >=2; Phase II >=3; Phase III >=4):**

1. Live-cell imaging + same-cell scRNA-seq (Cellanome R3200 Perturb-LINK)
2. Optical pooled screening + Cell Painting morphological screening (Carpenter)
3. High-throughput sequencing-based assays (Illumina)
4. Functional and multi-omics assays (available as Phase III extension)

**Governance:** Changes to locked protocol parameters require RFC-governed process with documented justification. This is the mechanism by which the stack eliminates arbitrary procedural variation, a stated IGoR requirement.

**TA3 milestones:**

| Phase | Deliverable/milestone |
|---|---|
| Phase I | Protocol schema and calibration artifacts defined; same protocol run at two team labs with comparable outcomes on >=1 experiment; >=2 modalities |
| Phase II | RFC process operational with >=2 RFCs executed; protocols run at >=3 labs including >=1 cross-team, each executing >=3 experiments to predefined reproducibility thresholds; >=3 modalities |
| Phase III | Open data and metadata layer delivered; engagement with >=1 external standards body or manufacturer; protocols run at >=5 labs across teams; >=4 modalities; connect-a-thon interoperability demonstrated |

---

### TA4: Validated-Lab Marketplace (Carpenter, Cellanome, Illumina)

**Structure:** At least two validated laboratories (IGoR minimum) execute TA3 protocols and return gold-standard, model-ready data packages. The full proposal names three TA4 performers spanning complementary modalities.

**TA4 laboratory roster:**

| Lab | Performer | Primary modality | Key platform |
|---|---|---|---|
| TA4 Lab 1 | **Carpenter Laboratory** (Anne Carpenter, PhD; Broad Institute, transitioning to Purdue/IPAI ~Sep 2026) | Optical pooled screening + Cell Painting morphological profiling | CellProfiler, JUMP dataset (>116K compounds), optical pooled CRISPR |
| TA4 Lab 2 | **Cellanome** (Dwight Baker, SVP Product Development) | Live-cell imaging + same-cell scRNA-seq + pooled CRISPR | **R3200 programmable CellCage**, Perturb-LINK (pools CRISPR delivery with longitudinal live imaging and same-cell scRNA-seq) |
| TA4 Lab 3 | **Illumina** | High-throughput sequencing + perturbation data | **Billion Cell Atlas** perturbation resource (contributed partly as in-kind resource sharing) |

**Note on Panome Bio:** Earlier drafts (REVISED_2026-06-05 SS and the Candidate Slate 2026-06-03) listed **Panome Bio** (Adam Richardson, VP Operations) as a fourth warm TA4 performer providing CLIA-certified untargeted metabolomics, lipidomics, and proteomics. Panome does not appear in the FULLPROPOSAL_DRAFT or COST_MODEL_2026-06-12 base team; it is held as an optional TA4 add. The current 7-performer structure uses Illumina as the third TA4 lab.

**Phase I anchor experiment:** Paired isogenic iPSC lines carrying a **22q11.2-region lesion** (a patient-derived 22q11.2-region TBX1 exon 2 CNV validation line; see restricted section 41), CRISPR-corrected to a matched healthy control and differentiated to NGN2 neurons. TA2 designs the discriminating screen; Carpenter and Cellanome execute morphological, live-cell, and transcriptomic readouts; TA1 defines the disease axes and ingests the results, establishing the cycle-time baseline. Cell-type morphological and molecular signatures of the 22q11.2 deletion are experimentally established as a precedent by Tegtmeyer et al. *Nat Commun* 2025 (DOI: 10.1038/s41467-025-61547-x).

**Phase concordance gating:** Data ingestion into TA1 is conditional on passing concordance thresholds.

| Phase | Concordance threshold | Scope |
|---|---|---|
| Phase I | >=80% (intra-team) | Same experiment at two team labs |
| Phase II | >=90% (cross-team) | >=3 experiments; multicellular systems |
| Phase III | >=90% across marketplace | Unified marketplace; external-researcher use; >=3 labs |

**Data return format:** QC-rich packages formatted to the IGoR common data model. All data are released openly at each phase milestone, consistent with the open-science license (Apache 2.0 code; CC BY 4.0 documentation).

**Resource sharing (in-kind, ~$4.0M):**

- Illumina: Billion Cell Atlas perturbation data access + sequencing credits
- Cellanome: discounted R3200 instrument access
- Cloud compute research credits for TA1/TA2
- JUMP Cell Painting reference data (open; leverages prior public investment)

**TA4 milestones:**

| Phase | Milestone |
|---|---|
| Phase I | >=1 cell line and instrument validated on IV&V artifacts at each of two labs; intra-team reproducibility at >=80% concordance; two-way capability communication established |
| Phase II | >=2 additional instruments validated per lab; marketplace request/return interface operational; cross-team experiment at >=90% concordance across >=3 experiments; exceptions per experiment reduced >=50% vs. Phase I |
| Phase III | Unified marketplace across teams; experiments ordered and executed across teams; >=90% concordance; >=70% of exceptions handled autonomously; connect-a-thon completed |


---

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


---

## 40. Disease strategy and evidence base

**IGoR framing rule (committed strategy):** "Do not propose a single disease (22q11DS alone): too narrow, reads as the well-bounded problem they reject. Do not propose a vague area with no anchor. Frame as: a neuropsychiatric area, with 22q11DS as the Phase I-II flagship exemplar, generalizing to idiopathic schizophrenia or broader transdiagnostic psychiatry in Phase III."

**Proposal title:** "A Closed-Loop, Mechanistically Grounded Research Engine for Complex Neuropsychiatric Disease: Schizophrenia to Bipolar Disorder."

---

### Phase I/II anchor: 22q11.2 deletion syndrome (22q11DS)

**Rationale (committed framing):** "22q11DS is the highest-penetrance known genetic risk factor for psychosis; its deletions span TBX1, COMT, and DGCR8, genes with well-characterized but mechanistically unlinked effects on cell-type pathology and thalamocortical/fronto-temporal circuit function. Formalizing that molecular-to-circuit causal chain, and using it to drive systematic experiment design, is a tractable, scientifically important, and measurable deliverable."

**Key epidemiological statistics (meta-analysis evidence):**

| Metric | Value | Source |
|---|---|---|
| Pooled prevalence of psychotic disorders in 22q11DS | 11.5% (95% CI: 9.4-14.0%) | Schneider et al. 2023 *BJPsych* (PMID: 36786112) |
| Pooled prevalence of schizophrenia specifically | 9.7% (95% CI: 6.5-14.2%) | Same meta-analysis |
| 5-year incidence of psychosis | 10.6% (95% CI: 6.6-16.7%) | Same meta-analysis |
| Relative risk for schizophrenia spectrum | ~20-25x vs. general population | Bassett and Chow 1999; Murphy et al. 1999 *Arch Gen Psychiatry* (PMID: 10199234) |
| Prevalence of 22q11.2 deletion in schizophrenia cohorts | ~0.3-1% vs. ~0.025% in general population | Multiple CNV/GWAS studies |

**The causal chain we commit to formalizing:**

```
TBX1 / COMT / DGCR8 (22q11.21 locus)
    -> cell-type pathology (oligodendrocyte lineage; cortical and somatosensory; interneuron/excitatory imbalance)
    -> thalamocortical / fronto-temporal circuit dysfunction
```

**TBX1 as the primary genetic handle:** TBX1 (OMIM:602054; chr 22q11.21) is the primary causal gene for cardiovascular and pharyngeal defects of 22q11.2DS. It is also expressed in the oligodendrocyte lineage and embryonic cortex.

Supporting evidence for TBX1 as a schizophrenia model anchor:

- Tbx1+/- mice show reduced prepulse inhibition (PPI), a validated schizophrenia endophenotype (Paylor et al. 2006 *PNAS*; PMID: 16684884)
- Tbx1 loss in mesodermal cells disrupts corticogenesis via premature neurogenesis in the somatosensory cortex anlage (Vitelli et al. 2017 *Cereb Cortex*; PMID: 27131548)
- Tbx1 heterozygosity in the oligodendrocyte lineage specifically disrupts myelination of fimbria axons (Kim and Bhatt 2025 *bioRxiv* 2025.12.30.697076)

**Caveat acknowledged (required for proposal):** TBX1 sequence variation does NOT significantly contribute to the genetic etiology of psychotic or affective disorders in the general nonsyndromic population (Funke et al. 2007 *Mol Med*; PMID: 17622321). TBX1 is framed as the primary genetic handle within 22q11DS, not as a standalone schizophrenia gene. Other 22q11 genes (DGCR8, PRODH, GNB1L, COMT) carry stronger direct mechanistic links to psychosis pathways in idiopathic schizophrenia.

**Phase I anchor experiment:** Paired isogenic iPSC lines carrying a patient-derived 22q11.2-region (TBX1 exon 2 CNV) validation line; see restricted section 41. Lines are CRISPR-corrected to a matched healthy control and differentiated to NGN2 neurons.

**MONDO/ontology note:** 22q11DS-associated schizophrenia maps to SCZD4 (OMIM:600850/PRODH). SCZD4 is not a direct child of MONDO:0005090 (schizophrenia); 22q11DS is a separate MONDO entity (MONDO:0011511, DiGeorge syndrome/velocardiofacial syndrome). This distinction must be encoded correctly in the TA1 ontology layer.

---

### Key datasets and assays supporting Phase I/II

| Dataset/assay | Description | Use in TA1 |
|---|---|---|
| **PsychENCODE brainSCOPE** (Emani et al. *Science* 2024; DOI: 10.1126/science.adi5199) | Single-cell genomics and regulatory networks for 388 human brains; 24 brain cell types | GRN layer; cell-type-specific TF-to-target edges |
| **PsychAD atlas** (Batiuk et al. *Nat Neurosci* 2024) | Upper-layer cortical neuron pathology in schizophrenia | Cell-type resolution; co-author |
| **Ruzicka, Mohammadi et al. *Science* 2024** (multi-cohort schizophrenia atlas; DOI: 10.1126/science.adg5136) | Single-cell multi-cohort dissection of schizophrenia transcriptome | Primary schizophrenia cell-type atlas; PI co-led |
| **ROSMAP atlas** (Mathys, Mohammadi et al. *Nature* 2019) | Single-cell Alzheimer's disease atlas | Demonstrates atlas-building capability; co-author |
| **SCHEMA exome** (Singh et al. *Nat Genet* 2022; DOI: 10.1038/s41586-022-04556-w) | 24,248 cases vs. 97,322 controls; 10 exome-wide genes | Rare-variant genomic layer; glutamate/chromatin/ubiquitin pathways |
| **NeuroPainting / Tegtmeyer et al. *Nat Commun* 2025** (DOI: 10.1038/s41467-025-61547-x) | Cell-type-specific morphological and molecular signatures of the 22q11.2 deletion in iPSC-derived neurons and astrocytes | Direct TA1/TA3 validation precedent; Carpenter senior author |
| **JUMP Cell Painting Consortium** (>116K compounds) | Genome-scale morphological profiles; Carpenter/Broad | TA4 Phase I morphological readout baseline |
| **Open Targets Platform** (Falaguera et al. *Nat Commun* 2025) | Temporal trends in drug target evidence; GWAS causal gene scoring (L2G) | Target credentialing and genetic support scoring |
| **PGC schizophrenia GWAS** (Trubetskoy et al. *Nature* 2022; DOI: 10.1038/s41586-022-04434-5) | Mapping genomic loci implicating genes and synaptic biology | Genomic layer; soft interventions into TA1 causal model |

---

### Phase III: Idiopathic schizophrenia

The same modeling framework generalizes to idiopathic schizophrenia in Phase III, satisfying IGoR's explicit second-disease generalization requirement. The schizophrenia GWAS layer (PGC, Trubetskoy et al. 2022), SCHEMA rare-variant data, and the PsychENCODE/multi-cohort atlas directly support this extension. Brad Ruzicka (McLean/Harvard, clinical co-lead) is the primary interface for the Phase III schizophrenia translational validation layer.

---

### Bipolar disorder: cautious Phase III extension

Bipolar disorder is the stated Phase III second disease in the full proposal title and cover block ("Schizophrenia to Bipolar Disorder"). The 22q11DS model carries bipolar disorder relevance (an estimated 15-25% rate in 22q11DS cohorts). The BDNF/TrkB axes, which underpin mood, thought, and cognitive dimensions, and the shared mechanistic pathway to rapid-acting antidepressant plasticity (ketamine, psilocybin), provide the scientific bridge.

Framing guidance: bipolar is presented as a biologically and genetically related Phase III extension that shares cellular biology and disease axes with schizophrenia, not as a primary focus. The degree of independence between the schizophrenia and bipolar extensions is framed as an empirical question that the causal model will address.

> [!NOTE]
> **Penetrant-form deep dive:** the MONDO and OMIM SCZD subtype landscape, the 22q11DS risk statistics, the TBX1 evidence (for and against), and the SCHEMA rare-variant convergence that justify building cellular models on penetrant forms are consolidated in section 42.


---

## 42. Penetrant schizophrenia genetics and the familial-disease rationale for cellular models

> [!TIP]
> **If you read one thing:** schizophrenia is mostly polygenic and therefore hard to model in a dish, but it has **high-penetrance genetic forms** (the 22q11.2 deletion and a set of large-effect rare-variant genes such as SETD1A, GRIN2A, and CUL1) that behave almost Mendelian. We use these the way neurodegeneration research uses **familial Alzheimer (APP, PSEN1) and familial Parkinson (SNCA, LRRK2)**: as near-deterministic genotype handles that give a strong, interpretable genotype-to-cellular-phenotype signal, justifying cellular models built on them first and then generalized to idiopathic disease.

### 42.1 Why penetrant forms justify cellular models

A diffuse polygenic score spreads tiny effects across thousands of loci, which no iPSC model can express as a clean phenotype. A penetrant variant concentrates the causal signal, which is exactly what a cellular model needs to read out. This is the same move that made neurodegeneration tractable in a dish.

| Field | Familial / penetrant handle | Why it enabled cellular models |
|---|---|---|
| **Alzheimer disease** | APP, PSEN1, PSEN2 (autosomal dominant) | Near-deterministic genotype; iPSC neurons show amyloid and tau phenotypes that anchor the sporadic disease model |
| **Parkinson disease** | SNCA, LRRK2, GBA | Strong genotype-to-phenotype signal in iPSC dopaminergic neurons; defines the axes sporadic cases are read against |
| **Schizophrenia (our entry)** | **22q11.2 deletion (~25x risk)** and large-effect SCHEMA genes (SETD1A, GRIN2A, GRIA3, CUL1) | Penetrant, near-Mendelian handles that produce measurable cellular phenotypes, anchoring a model later generalized to idiopathic schizophrenia |

> [!IMPORTANT]
> This is the bridge from the thesis (section 10): a **penetrant variant is the cleanest soft-intervention** on the latent causal model, so penetrant forms are where the disease-as-perturbation frame is most identifiable. They are the Phase I cellular anchor (section 41, restricted); idiopathic schizophrenia is the harder Phase III generalization (section 40).

### 42.2 The genetic-subtype landscape (MONDO and OMIM SCZD loci)

OMIM defines **19 numbered SCZD loci**; the gene-level ones are the usable cellular handles. An ontology caveat matters for TA1 design.

| SCZD | Gene / locus | Mechanism class | Evidence | Notes |
|---|---|---|---|---|
| **SCZD4** | 22q11.21 deletion (**PRODH**, plus DGCR8, COMT, TBX1, GNB1L) | CNV, multi-gene | Strongest known risk | The flagship penetrant handle (42.3) |
| **SCZD9** | **DISC1** (1q42.2) | Translocation | De-emphasized in recent GWAS | Historical; not in SCHEMA |
| **SCZD13** | **CHRNA7** (15q13.3 microdeletion) | CNV | Replicated CNV | nicotinic receptor |
| **SCZD15** | **SHANK3** (22q13.33) | Rare CNV/deletion | Phelan-McDermid overlap | postsynaptic scaffold |
| **SCZD16** | **VIPR2** (7q36.3 microduplication) | CNV | Nature 2011 | VIP receptor |
| **SCZD17** | **NRXN1** (2p16.3 deletion) | CNV/deletion | Replicated | presynaptic adhesion |
| **SCZD18** | **SLC1A1** (9p24.2) | Rare coding | Glutamate transporter EAAC1 | glutamate clearance |
| **SCZD19** | **RBM12** (20p13) | Heterozygous LoF | Danish pedigrees | RNA binding |

> [!CAUTION]
> **Ontology gap to handle in TA1 (sections 24 and 30):** SCZD4 (22q11/PRODH, OMIM 600850) is **not a direct child of MONDO:0005090 (schizophrenia)**; 22q11.2DS is a separate MONDO entity (MONDO:0011511, DiGeorge/velocardiofacial syndrome). Six SCZD loci (SCZD4, 6, 9, 13, 14, 18) have MONDO IDs but are not direct schizophrenia children. Our ontology-conditioned model must reconcile the genetics-first view (22q11DS as a schizophrenia handle) with the MONDO classification, or it will mis-place the disease.

### 42.3 22q11.2 deletion syndrome: the highest-penetrance handle

| Metric | Value | Source |
|---|---|---|
| Lifetime psychosis risk | **~25%** (~25-fold vs. general population) | Murphy et al. 1999; consensus reviews |
| Pooled psychotic-disorder prevalence | **11.5%** (95% CI 9.4 to 14.0) | Schneider et al. 2023 (PMID:36786112) |
| Pooled schizophrenia prevalence | **9.7%** (95% CI 6.5 to 14.2) | Same meta-analysis |
| 22q11.2 deletion in schizophrenia cohorts | **~0.3 to 1%** vs. ~0.025% general | Karayiorgou et al. 1995; CNV studies |
| Fraction of all schizophrenia attributable | **~1 to 2%** | Karayiorgou et al. 1995 |

The deletion spans multiple psychosis-relevant genes (PRODH glutamate/proline, DGCR8 miRNA biogenesis, COMT dopamine catabolism, GNB1L, TBX1), which is why it is a multi-gene causal handle rather than a single-gene model.

### 42.4 TBX1: a partial model, used precisely

TBX1 is the primary causal gene for the cardiac, thymic, and craniofacial features of 22q11DS, and it has real but bounded psychiatric evidence. We state it honestly to avoid overclaiming.

- **For (mechanistic):** Tbx1+/- mice show reduced prepulse inhibition, a validated schizophrenia endophenotype (Paylor et al. 2006); a human family with a TBX1 frameshift co-segregated psychiatric features without the full deletion; Tbx1 loss disrupts corticogenesis (Vitelli et al. 2017) and oligodendrocyte myelination of fimbria axons (Kim and Bhatt 2025).
- **Against (genetic):** TBX1 sequence variation does not significantly contribute to nonsyndromic schizophrenia (Funke et al. 2007); variants are rare and underpowered in case-control studies; PRODH, DGCR8, COMT, and GNB1L have stronger direct links to psychosis pathways.

> [!IMPORTANT]
> **How we use TBX1:** as a high-penetrance developmental handle that mimics a familial-disease entry, not as a standalone schizophrenia gene. Its best-supported neural phenotypes (corticogenesis, myelination, prepulse inhibition) are the cellular and circuit readouts the model targets, and the honest genetic caveat is stated in the proposal rather than buried.

### 42.5 Rare-variant convergence (SCHEMA) defines what the cellular models read out

SCHEMA (Singh et al. 2022, *Nat Genet*, PMID:35396579; 24,248 cases, 97,322 controls) provides an orthogonal, gene-level tier of large-effect rare variants. Ten genes reach exome-wide significance and 32 reach 5% FDR. The high-odds-ratio genes are the cleanest cellular handles.

| Tier | Genes (illustrative) |
|---|---|
| **Exome-wide significant (10)** | **SETD1A, CUL1, XPO7, TRIO, CACNA1G, SP4, GRIA3, GRIN2A, HERC1, RB1CC1** |
| **Highest odds ratios** | CUL1 (OR ~44), XPO7 (~28), GRIN2A (~24), GRIA3 (~20) |

The convergent biology tells the cellular models which phenotypes to measure:

| Pathway | SCHEMA genes |
|---|---|
| **Glutamate signaling** | GRIA3 (AMPA), GRIN2A (NMDA), CACNA1G (T-type Ca channel) |
| **Chromatin and histone regulation** | SETD1A, ASH1L, KDM6B, H1-4, ZMYM2, ZNF136 |
| **Synaptic and presynaptic** | PCLO, SV2A, DAGLA, MAGI2 |
| **Ubiquitin-proteasome** | CUL1, HERC1 |
| **Rho/actin signaling** | TRIO, FYN |
| **Autophagy and mTOR** | RB1CC1, NPRL3 |
| **Transcription factors** | SP4, NR3C2, NR4A2 |

> [!NOTE]
> The full 42-gene SCHEMA table (P < 5e-4), the complete 19-locus SCZD table with MONDO and OMIM identifiers, and the SCZD-named genes outside the SCHEMA top list are preserved verbatim in `_sources/schizophrenia_MONDO_subtypes_22q11_TBX1.md`.

### 42.6 Implications for our cellular models

- **Build on penetrant forms first.** The 22q11.2 deletion and high-OR SCHEMA genes give iPSC-derived neuron and astrocyte models a measurable phenotype, anchoring TA1 (sections 30 and 40) and the Phase I experiment (section 41).
- **Read out convergent pathways.** Glutamatergic (GRIN2A, GRIA3), chromatin (SETD1A), and synaptic (NRXN1, SHANK3) axes are the molecular and cellular phenotypes the models must capture, and they double as the candidate disease axes the factorization targets (section 31, restricted).
- **Generalize via learned axes.** Penetrant forms calibrate the causal model; the transdiagnostic axes then project idiopathic, polygenic schizophrenia onto the same coordinate system (sections 10 and 40), which is the Phase III generalization.
- **Respect the ontology.** Encode the SCZD4-versus-MONDO:0005090 gap explicitly (sections 24 and 30) so genetics-first handles and disease classification stay consistent.

### Sources

22q11DS and schizophrenia: Murphy et al. 1999 (PMID:10199234); Schneider et al. 2023 (PMID:36786112); Karayiorgou et al. 1994 (PMID:8213821) and 1995 (PMID:7667299); Gothelf et al. 2007 (PMID:17046719); Vorstman et al. 2017 (PMID:28379838); Fiksinski et al. 2022 (PMID:35577927); Malone et al. 2022 (doi:10.1038/s41380-022-01674-9). TBX1: Paylor et al. 2006 (PMID:16684884); Funke et al. 2007 (PMID:17622321); Vitelli et al. 2017 (PMID:27131548); Kim and Bhatt 2025 (bioRxiv 2025.12.30.697076); Stark et al. 2008 (IJNP). Rare variants: SCHEMA, Singh et al. 2022 (PMID:35396579). Ontology: MONDO:0005090 and MONDO:0011511 (OLS4); OMIM SCZD1 to SCZD19.


### 42.7 Isogenic disease-in-a-dish and the Phase I phenotypic-triage screen

**Why engineered isogenic lines, not only patient lines.** A patient-derived iPSC line carries the variant but has **no genetically matched healthy control**, so any cellular difference is confounded by genetic background. Starting from a **common healthy iPSC background and inducing each variant by CRISPR** yields **isogenic case-control pairs** that isolate the causal effect of the variant, which is the clean soft-intervention the thesis (section 10) requires. Patient lines remain a useful complementary, real-genome check.

**The phenotypic-triage (phenoproxy) screen.** Not every penetrant variant produces a measurable in-dish phenotype, so Phase I runs a **systematic screen across the variant panel** (the 22q11.2 deletion and TBX1, high-odds-ratio SCHEMA genes such as SETD1A, GRIN2A, GRIA3, and CUL1, and selected SCZD loci) in iPSC-derived neurons and astrocytes, measuring **multimodal phenotypes**:

- **Transcriptomic:** single-cell RNA-seq signatures and pathway-space shifts.
- **Morphological:** high-content Cell Painting and neuronal morphometry.
- **Functional activity:** single-cell **calcium imaging**, the scalable single-cell activity readout and an optical modality that folds into the high-content and live-cell imaging stack; MEA is not required.
- Optional proteomic and metabolomic readouts where a variant implicates those layers.

**What it produces.** A ranked variant-to-phenotype map showing which genetic forms yield robust, reproducible disease-in-a-dish signatures. Strong-signal lines anchor the TA1 causal model and are carried forward; weak-signal variants are deprioritized. This **expands the Carpenter group's 22q11 NeuroPainting precedent** (Tegtmeyer et al. 2025) from one deletion and one modality to a **systematic, multi-variant, multi-modal screen**, which is both a concrete Phase I deliverable and the empirical basis for selecting the disease axes (sections 30 and 31).


---

## 50. Metrics, milestones, and quantitative targets

**Program marquee metrics (from IGoR Appendix A):** The IGoR program targets at least a 4x improvement in experimental cycle time by Phase II and at least a 10x improvement by Phase III, with at least 90% cross-laboratory concordance and at least 85% of TA2-proposed experiments rated high-value by an expert panel.

Our proposed targets meet or exceed every program minimum. Items where our self-set targets exceed the program minimum are marked with an asterisk (*).

---

### Integrated go/no-go table by phase and TA

| TA | Metric | Phase I (mo 18) | Phase II (mo 36) | Phase III (mo 60) | Notes |
|---|---|---|---|---|---|
| **TA1** | Disease-model sub-models | >=3 | >=10, across >=2 scales | >=15, across >=3 scales | Program minimum not stated at this granularity; self-set |
| **TA1** | Quantitative knowledge gaps detected | >=3 algorithmically | Ongoing; gaps feed TA2 | Ongoing | Self-set; makes gaps explicit and rankable |
| **TA1** | Variance explained (22q11DS cell-type shifts) | >=30% | Not specified | Not specified | Self-set; Phase I go/no-go* |
| **TA1** | Parameter uncertainty reduction (first TA4 return) | >=20% | Not specified | Not specified | Self-set* |
| **TA1** | Novel prediction confirmed | Not applicable | >=1 in independent dataset | Novel validated hypotheses in both diseases | Self-set Phase II go/no-go |
| **TA1** | Model update latency | Baseline established | <=24 h | <=4 h | Self-set; program asks for "low latency" without a number |
| **TA2** | Expert panel rating (high-value experiments) | >=50% | >=75% | >=85% | Matches program minimum by Phase III |
| **TA2** | Usability (researchers rating system useful) | Not applicable | >=70% (>=10 scientists) | >=80% (>=20 researchers incl. external) | Self-set |
| **TA2** | Model backends (>=1 open-weight) | 1 | >=2 | >=2 | Program asks for open-weight capability; self-set Phase II target |
| **TA3** | Modalities covered | >=2 | >=3 | >=4 | Program minimum >=3 modalities; Phase I target is below program minimum (build ramp) |
| **TA3** | Labs running protocols | 2 (team only) | >=3 (incl. >=1 cross-team) | >=5 across teams | Matches program requirements |
| **TA3** | RFCs | Not applicable | >=2 | Ongoing | Self-set governance metric |
| **TA4** | Cross-lab concordance | >=80% (intra-team) | >=90% (cross-team) | >=90% across marketplace | Meets program minimum (>=90%) by Phase II* |
| **TA4** | Experiments executed to concordance standard | >=1 at 2 labs | >=3 (cross-team) | Marketplace scale | Program requires >=2 labs; self-set experiment counts |
| **TA4** | Exceptions handled autonomously | Not applicable | Reduced >=50% vs. Phase I | >=70% autonomous | Self-set Phase II/III targets |
| **Program** | Experimental cycle time | Baseline established | >=4x faster vs. baseline | >=10x faster vs. baseline | Matches IGoR marquee metrics |

---

### Metrics that exceed program minimums (starred items)

1. **TA1 variance explained (>=30%, Phase I):** The program does not specify a percentage; we set this as a Phase I go/no-go to make TA1 progress falsifiable at the first gate.
2. **TA1 parameter uncertainty reduction (>=20%, first TA4 return):** Directly tests the closed-loop hypothesis that TA4 data constrains the TA1 model; program does not require this specific check.
3. **TA4 concordance at Phase II (>=90%):** The program requires >=90% concordance but does not specify it must be achieved by Phase II. We set this as a Phase II target, one phase earlier than the program minimum.

---

### Dropped metric: Spearman r >=0.4 (TA2 Phase I)

The **2026-06-02 Solution Summary** included a TA2 Phase I go/no-go metric requiring hypothesis rank to correlate with experimental effect size at Spearman r >=0.4 on the first ten experiments. This metric does not appear in the **FULLPROPOSAL_DRAFT (2026-06-12)** milestone table.

This metric is scientifically important: it provides a direct, falsifiable test of whether the TA2 value-of-information ranking is actually predictive. It should be restored in the full proposal. The program does not require it, but including it demonstrates mechanistic rigor.

---

### Program-level cycle-time target pathway

| Phase | Cycle-time target | How we demonstrate it |
|---|---|---|
| Phase I | Baseline established (conventional research, months to years) | Document a representative conventional experiment timeline at Phase I kickoff |
| Phase II | >=4x faster than baseline | Measure time from TA2 query to validated TA4 data return; compare to baseline |
| Phase III | >=10x faster than baseline | Same measurement at marketplace scale; document in transition plan |


---

## 60. Team, consortium, and cost model

**Current structure (decided 2026-06-03):** IPAI/Purdue = prime + PI; Cytognosis = funded sub-award (TA1 lead, TA2 co-lead); five additional sub-awardees for TA2, TA3, and TA4. This is a 7-performer structure. Total ARPA-H request: **$50,000,000** over 60 months (3 phases: 18 + 18 + 24 months). This supersedes the earlier $30M midpoint and Cytognosis-as-prime framing from the 2026-06-02 and 2026-06-05 solution summaries.

**Rationale for IPAI-prime:** "Funds still reach Cytognosis as a real sub-award (builds its record and resources the org), while Purdue's track record, infrastructure, and F&A environment carry the win." (Strategy Master 2026-06-03)

---

### Performer roles table

| Performer | Type | TA role | PI/key lead | Status |
|---|---|---|---|---|
| **IPAI/Purdue** | Academia (prime) | Coordination, PI, software architecture, TA1/TA2 support | Ananth Grama, PhD (Director, IPAI) | Warm; not yet formally committed |
| **Cytognosis Foundation** | Nonprofit 501(c)(3) | TA1 co-lead; TA2 co-lead | Shahin Mohammadi, PhD (Founder/CEO) | Confirmed |
| **Phylo** | For-profit | TA2 agentic-science co-lead | Kexin Huang, PhD (Founder; creator of Biomni) | Warm/in-discussion |
| **SIFT** | For-profit | TA3 lead (LabOP/protocol stack) | Robert Goldman, PhD and Dan Bryce, PhD | Committed TA3 lead |
| **Matt Tegtmeyer Lab (Purdue)** | Academia | TA4 academic experimental arm (fixed-cell high-plex readouts: RNA ~350-plex, protein ~50-plex, morphology, in-situ CRISPR-guide sequencing; all wet-lab experiments) | Matthew Tegtmeyer, PhD | Recruited; confirming effort/subaward |
| **Anne Carpenter (Broad/IPAI)** | Academia (computational) | TA4 computational morphology/imaging-model lead (no bench; CellProfiler, Cell Painting Gallery, JUMP; bridges TA4 experimental arms to TA1/TA2) | Anne Carpenter, PhD (Senior Director, Broad Imaging Platform) | Warm; dialogue active |
| **Cellanome** | For-profit | TA4 industry experimental arm (R3200 live-cell + Perturb-LINK same-cell CRISPR) | Dwight Baker, SVP Product Development | Advancing; 3-person call 2026-06-17; NDA sent |
| **Illumina** | For-profit | TA4 lab 3 (sequencing + data) | Key contact in discussion | In-discussion |
| **McLean Hospital/HMS** | Academia | Clinical co-lead (translational grounding) | W. Brad Ruzicka, MD/PhD | Confirmed |

**Open mandatory roles (must resolve before Aug 6):**

- **Project Manager:** Patty Purcell (in discussion; availability risk, may take a full-time role elsewhere). Line up a backup PM now. ~1.0 FTE, ~$200K/yr fully loaded.
- **Software Architect:** TBD human, not the PI and not an AI agent. Owns TA1-TA2 interface specs, cross-team interoperability, and open-source release. ~1.0 FTE, ~$250K/yr fully loaded. This is a named IGoR-required role and is the most critical open gap.

---

### Cost model: $50M, 3-phase allocation by performer

Source: COST_MODEL.md (2026-06-12); this is the authoritative current version.

| Performer | 5-yr total | Phase I (18 mo) | Phase II (18 mo) | Phase III (24 mo) |
|---|---|---|---|---|
| IPAI/Purdue (prime) | $7.0M | $1.9M | $2.1M | $3.0M |
| Cytognosis (sub) | $14.0M | $4.0M | $4.2M | $5.8M |
| Phylo (sub) | $4.0M | $1.1M | $1.2M | $1.7M |
| SIFT (sub) | $5.0M | $1.5M | $1.5M | $2.0M |
| Carpenter Lab (sub) | $5.0M | $1.3M | $1.5M | $2.2M |
| Cellanome (sub) | $8.0M | $2.0M | $2.4M | $3.6M |
| Illumina (sub) | $4.0M | $0.9M | $1.2M | $1.9M |
| Cross-team/integration/reserve | $3.0M | $0.8M | $0.9M | $1.3M |
| **Total** | **$50.0M** | **$13.5M** | **$15.0M** | **$21.5M** |

---

### Consolidated Basis of Estimate (BOE) categories

| Category | Amount | Basis |
|---|---|---|
| Direct labor (fully burdened) | $22.0M | ~14 funded FTE/yr blended across 7 organizations at 2026 loaded rates |
| Labor hours | ~147,000 hrs | $22.0M / ~$150/hr blended (salary + fringe) |
| Subcontracts/consultants | $1.0M | Clinical co-lead effort, biostatistics, ethics/IRB, standards consultants |
| Materials | $6.0M | iPSC/NGN2 differentiation, CRISPRi/a libraries, Perturb-seq kits, Cell Painting reagents, sequencing consumables |
| Equipment | $2.5M | Imaging/instrument access, lab and GPU hardware |
| Travel | $1.0M | DDD workshop (kickoff), TA3 bake-offs, connect-a-thon, biannual IV&V reviews, dissemination |
| Other direct costs (ODC) | $7.0M | GPU/cloud compute (TA1 training + TA2 agentic inference), sequencing-as-a-service, storage, software/API licenses, grad tuition |
| Indirect (F&A/overhead) | $9.0M | Cytognosis 15% de minimis MTDC; Purdue ~57% on-campus F&A; commercial subs' overhead reconciled |
| Profit/fee | $1.5M | Commercial subs ~7-10% on cost base; none for nonprofit/academia |
| **Total** | **$50.0M** | |
| Resource sharing (Performer, in-kind) | ~$4.0M | Illumina Billion Cell Atlas data + sequencing credits; Cellanome instrument access; cloud research credits |

---

### Cytognosis sub-award detail (~$2.5-3.0M/yr steady state; ~7.5 FTE)

| Role | FTE | Loaded $/yr |
|---|---|---|
| PI (Mohammadi), partial | 0.5 | ~$100K |
| Software architect (TA2/integration; IGoR-required) | 1.0 | ~$250K |
| Senior ML/AI engineer (TA2) | 1.0 | ~$260K |
| ML research scientist (TA1/TA2) | 1.0 | ~$240K |
| Computational biologists (TA1) | 2.0 | ~$420K |
| Technical project manager | 1.0 | ~$200K |
| Research scientist/postdoc | 1.0 | ~$120K |
| **Personnel subtotal** | ~7.5 | **~$1.59M** |

Plus compute ~$400K/yr, ODC ~$200K/yr, indirect at 15% de minimis MTDC. 5-yr total ~$14.0M (Phase III heavier due to second disease and scaled inference).

**Labor rate anchors (2026, Bay Area):**

- Senior ML/AI engineer: ~$260K; ML research scientist: ~$240K; software architect: ~$250K; computational biologist: ~$210K; research scientist/postdoc: ~$120-130K; technical PM: ~$200K
- H100 blended cloud/spot: ~$2.50-3.00/GPU-hr

**Indirect rates:**

- Cytognosis: 15% de minimis MTDC (2 CFR 200.414(f)); on an OT, ARPA-H negotiates the actual rate
- Purdue: ~57% on-campus F&A (negotiated)
- Commercial subs: overhead embedded in loaded rate + fee ~7-10%
- MTDC excludes first $50K of each subaward only

---

### Evolution from earlier versions

The 2026-06-02 cost model (IGoR_Cost_Breakdown_2026-06-02.md) and the 2026-06-05 SS used a 3-performer structure (Cytognosis prime ~$13.5M, Cellanome ~$10.5M, Purdue/IPAI ~$6.0M) at a planning midpoint of ~$30M. The FULLPROPOSAL_DRAFT and COST_MODEL_2026-06-12 expand to a 7-performer structure (adding Phylo, SIFT, and Illumina as named sub-awardees) and a $50M total request. The per-performer Cytognosis and Purdue/IPAI dollar amounts in the current model are consistent with the earlier planning shares; the increase reflects the full team scope. The prime/sub order also changed: the 2026-06-02 SS had Cytognosis as prime; the 2026-06-05 SS switched to IPAI-prime, which is the committed structure.


### Confirmed team decisions (2026-06-14)

- **Prime and PI:** confirmed **IPAI-Purdue as prime with Ananth Grama as PI**. The Cytognosis-prime alternative is retired as the base case; revisiting it would change only the cover page and the BOE order.
- **Project Manager:** **Patricia (Patty) Purcell** is added as PM (required role, distinct from the PI).
- **Software and Systems Architect (open role, actively recruiting).** Required by the ISO and distinct from the PI and PM. Target profile: senior or principal level, roughly 10 or more years building **interoperable, API-first, open-source systems**, with demonstrated **architectural authority over cross-organization implementation and integration** (including AI-accelerated development); expertise in **data and metadata schemas and standards** (for example LinkML, ontologies, FAIR), distributed and cloud systems, and ML/AI engineering platforms; ideally scientific or biomedical data interoperability. About $240K fully loaded is budgeted; state the annual level of effort.
- **TA3 and TA4 partners:** in **active parallel discussion; none finalized.** Candidate communications follow `partnerships/PARTNER_OUTREACH_STRATEGY.md` so we neither overstate commitments nor signal an empty roster.


### Roster with status (2026-06-14)

Confirmed members are untagged; tentative entries carry a short status. Full detail and engagement intel in `partnerships/TEAM_TRACKER.md`.

| Role | Member | Status |
|---|---|---|
| Prime and PI | IPAI/Purdue, Ananth Grama | confirmed |
| TA1 and TA2 co-leads | Cytognosis (Shahin Mohammadi) and IPAI, Purdue | confirmed |
| Clinical and translational | W. Brad Ruzicka, McLean | confirmed |
| TA4 academic experimental arm | Matthew Tegtmeyer, Purdue (fixed-cell high-plex readouts: RNA ~350-plex, protein ~50-plex, morphology, in-situ CRISPR-guide sequencing; all wet-lab experiments) | recruited; confirming effort/subaward |
| TA4 computational morphology/imaging-model lead | Anne Carpenter, Broad/IPAI (no bench; CellProfiler, Cell Painting Gallery, JUMP) | confirmed (~90%; joint Purdue/Broad) |
| Project Manager | Patricia Purcell | verbally agreed (terms TBD) |
| Software and Systems Architect | planned Cytognosis hire (recruiting); Elham Jebalbarezi Sarbijan (IPAI/Purdue) interim | recruiting |
| TA2 (Cytognosis and IPAI lead; add-ons optional) | Phylo (Kexin Huang), FutureHouse | in discussion |
| TA3 lead, LabOP | Dan Bryce (SIFT), Tim Fallon (UCSD) | in discussion |
| TA4 laboratories (two or more) | Matt Tegtmeyer (academic arm), Cellanome (industry arm), Illumina, SPOC; Panome (alternate) | in discussion |

> [!NOTE]
> Harvard's ToolUniverse is a tool we may use (MCP tool access), not a team or TA2 partner. Cytognosis and IPAI build TA2 jointly; Phylo and FutureHouse are optional add-ons, not blockers.


### Partner principles and flags (2026-06-14)

- **TA1 is in-house only:** Cytognosis, IPAI, and students. No external TA1 partners, to keep the mission-critical core focused.
- **DataTecnica (Faraz Faghri)** is an optional **TA2** add-on (CNS machine-learning, biobank-scale; neurodegeneration focus). Verify before including: Faraz's NIH employment status (federal employees are barred), OCI, and the salary cap (funded portion only).
- **Transfyr (Renee Wegrzyn)** is a strong TA3 (reproducibility and interoperability) and possible TA4 candidate, but the founder is the **former ARPA-H director**, a significant conflict-of-interest and appearance risk that can affect the whole team. Counsel-gated; see `partnerships/TEAM_TRACKER.md`.


---

## 99. Consolidated references and verification status

All references are drawn directly from source documents (SCIENCE_BRIEF.md, IGoR_TA1_TA2_Research_2026-06-02.md, IGoR_TA1-TA2_Methods_DeepDive_2026-06-05.md, PRIOR_WORK_CONSOLIDATED.md, full_proposal/FULLPROPOSAL_DRAFT.md). Items marked (verify) require an independent check against arXiv, PubMed, or journal DOI lookup before submission. Items marked (internal) are not for distribution.

---

### Virtual cell and world models

1. Bunne C, Roohani Y, Rosen Y, et al. How to build the virtual cell with artificial intelligence: priorities and opportunities. *Cell*. 2024;187(25):7045-7063. doi:10.1016/j.cell.2024.11.015. [NOTE: a separate draft cited Cell 189(7):1175-1188; verify volume and pages, see inconsistency flag in PRIOR_WORK_CONSOLIDATED §8b]

2. Eisenstein M. Can biology move into the matrix? *Nature*. 2026;654:286-288. doi: see PDF footnote ref 4 (verify final DOI; the document header cites doi:10.1038/d41586-2026-02777-8, verify).

3. Xing E, Song L. A world model of the virtual cell. GenBio AI technical report, May 3, 2026. No arXiv or DOI in document, verify.

4. Chuai G, Chen X, Yang X, et al. Towards building a world model to simulate perturbation-induced cellular dynamics by AlphaCell. *bioRxiv*. 2026. doi:10.64898/2026.03.02.709176.

5. Dong M, Adduri A, Gautam D, et al. STACK: in-context learning of single-cell biology. *bioRxiv*. 2026. doi:10.64898/2026.01.09.698608.

6. Wang C, Karimzadeh M, Ravindra NG, et al. X-Cell: scaling causal perturbation prediction across diverse cellular contexts via diffusion language models. *bioRxiv*. 2026. doi:10.64898/2026.03.18.712807.

---

### Single-cell foundation models

7. Cui H, Wang C, Maan H, et al. scGPT: toward building a foundation model for single-cell multi-omics using generative AI. *Nat Methods*. 2024. (Verify: full citation details and DOI not confirmed in source documents.)

8. Theodoris CV, Xiao L, Bhatt P, et al. Transfer learning enables predictions in network biology. *Nature*. 2023;618(7965):616-624. doi:10.1038/s41586-023-06139-9. [Geneformer]

9. Hao M, Gong J, Zeng X, et al. Large-scale foundation model on single-cell transcriptomics. *Nat Methods*. 2024;21:1481-1491. doi:10.1038/s41592-024-02305-7. [scFoundation] (verify)

10. Adduri A, Dong M, et al. STATE: a foundation model for single-cell perturbation prediction. 2025. (Verify: arXiv ID and journal/conference; cited as "Arc STATE" in source documents; no DOI confirmed.)

---

### Perturbation predictors

11. Roohani Y, Huang K, Leskovec J. GEARS: predicting transcriptional outcomes of novel multigene perturbations. *Nat Biotechnol*. 2024;42:216-228. doi:10.1038/s41587-023-01905-6.

12. Lotfollahi M, Wolf FA, Theis FJ. scGen predicts single-cell perturbation responses. *Nat Methods*. 2019;16(8):715-721. doi:10.1038/s41592-019-0494-8.

13. Lotfollahi M, Klimovskaia Susmelj A, De Donno C, et al. Predicting cellular responses to complex perturbations in high-throughput screens. *Mol Syst Biol*. 2023;19(6):e11517. doi:10.15252/msb.202211517. [CPA]

---

### Causal sVAE lineage and mechanism-sparsity models

14. Lachapelle S, Rodriguez Lopez P, Sharma Y, Everett K, Le Priol R, Lacoste A, Lacoste-Julien S. Disentanglement via mechanism sparsity regularization: a new principle for nonlinear ICA. *Proceedings of Machine Learning Research* 140:1-57. CLeaR 2022. arXiv:2107.10098.

15. Lopez R, Tagasovska N, Ra S, Cho K, Pritchard JK, Regev A. Learning causal representations of single cells via sparse mechanism shift modeling (sVAE+). CLeaR 2023. *Proceedings of Machine Learning Research*. arXiv:2211.03553. [FLAGGED: sVAE+ Lopez et al. arXiv:2211.03553 cited as CLeaR 2023 in source documents; verify conference proceedings year and volume, flagged unverified in SCIENCE_BRIEF.md]

16. Bereket M, Karaletsos T. Modelling cellular perturbations with the sparse additive mechanism shift variational autoencoder (SAMS-VAE). NeurIPS 2023. arXiv:2311.02794.

17. Hediyeh-zadeh S, Fischer T, Theis FJ. Disentanglement via mechanism sparsity by replaying realizations of the past (sVAE-ligr). ICLR 2024 MLG workshop. No arXiv ID in source document, verify.

18. Zhang J, Greenewald K, Squires C, Srivastava A, Shanmugam K, Uhler C. Identifiability guarantees for causal disentanglement from soft interventions. NeurIPS 2023. arXiv:2307.06250. [NOTE: arXiv ID 2307.06250 is from the full_proposal reference list; SCIENCE_BRIEF.md says "ID not in PDF, verify." The full_proposal entry is the more complete citation; confirm match.]

19. de la Fuente J, Lehmann R, Ruiz-Arenas C, et al. Interpretable causal representation learning for biological data in the pathway space (SENA-discrepancy-VAE). ICLR 2025. arXiv:2506.12439. [NOTE: arXiv ID 2506.12439 may postdate the ICLR 2025 submission date, verify arXiv ID and ICLR proceedings entry]

20. Schölkopf B, Locatello F, Bauer S, et al. Toward causal representation learning. *Proceedings of the IEEE*. 2021;109(5):612-634. doi:10.1109/JPROC.2021.3058954. [sparse mechanism shift hypothesis]

---

### Flow-based generative models

21. Palma A, Richter T, Zhang H, Dittadi A, Theis FJ. CellFlow: a generative flow-based model for single-cell count data. ICLR 2024 MLG workshop. No arXiv ID or DOI in source document, verify.

---

### Our team's perturbation model (internal)

22. [internal, embargoed] Team perturbation-model manuscript, anonymous submission to NeurIPS 2026, under review. Method name and title withheld; cited only in restricted section 32. Do not list in external reference sets.

---

### Sequence-to-regulatory / genomic grammar models

23. Avsec Z, et al. (Google DeepMind). AlphaGenome. GitHub: github.com/google-deepmind/alphagenome. Apache-2.0 code; noncommercial weights. 2025. [NOTE: author list and year disputed between source documents, full_proposal cites "Avsec Z, et al. / Google DeepMind (2025)" while an earlier draft cited "Outeiral C, Strahm M, Shi J, et al. (2021; updated)." Verify the correct citation, flagged in PRIOR_WORK_CONSOLIDATED §8c]

24. Avsec Z, Agarwal V, Visentin D, et al. Effective gene expression prediction from sequence by integrating long-range interactions. *Nat Methods*. 2021;18(10):1196-1203. doi:10.1038/s41592-021-01252-x. [Enformer]

25. Linder J, Bhate A, Rajesh A, et al. Borzoi: sequence modeling of gene expression at enhancer resolution. *Nat Genet*. 2023. (Verify: DOI and volume/pages not confirmed in source documents.)

---

### Intervention-design GNNs

26. Gonzalez G, Lin X, Herath I, Veselkov K, Bronstein M, Zitnik M. Combinatorial prediction of therapeutic perturbations using causally inspired neural networks (PDGrapher). *Nat Biomed Eng*. 2025. doi:10.1038/s41551-025-01481-x.

---

### Systems-biology and network tools

27. Liu A, Trairatphisan P, Gjerga E, Didangelos A, Barratt J, Saez-Rodriguez J. From expression footprints to causal pathways: contextualizing large signaling networks with CARNIVAL. *NPJ Syst Biol Appl*. 2019;5:40. doi:10.1038/s41540-019-0118-z.

28. Dugourd A, Kuppe C, Sciacovelli M, et al. Causal integration of multi-omics data with prior knowledge to generate mechanistic hypotheses (COSMOS). *Mol Syst Biol*. 2021;17(1):e9730. doi:10.15252/msb.20209730.

29. Browaeys R, Saelens W, Saeys Y. NicheNet: modeling intercellular communication by linking ligands to target genes. *Nat Methods*. 2020;17(2):159-162. doi:10.1038/s41592-019-0667-5.

30. Virtual Brain Twin Consortium. virtualbraintwin.eu. 2025. (Consortium reference; no single DOI; cite website and relevant publications.)

---

### Network and co-expression tools

31. Su Y, Miller R, Hazelbaker B, et al. Cell-type-specific co-expression inference from single-cell RNA-sequencing data (CS-CORE). *Nat Commun*. 2023;14:4846. doi:10.1038/s41467-023-40503-7.

32. Song D, Wang Q, Yan G, et al. scDesign3 generates realistic in silico single-cell and spatial omics data using statistical copula models. *Nat Biotechnol*. 2024;42:247-252. doi:10.1038/s41587-023-01772-1.

33. Garrido-Rodriguez M, Holland CH, Ramirez Flores RO, et al. Integrating knowledge and omics via large-scale models of signaling networks (OmniPath). *Mol Syst Biol*. 2022;18:e11036. doi:10.15252/msb.202211036.

---

### Neuro-specific network priors

34. Lage K, et al. A cell-type-resolved interactome of autism risk genes (IGF2BP1-3 complex; AP-MS in iNs). *Cell Genomics*. 2022;2(9):100182. doi:10.1016/j.xgen.2022.100182.

35. Emani PS, Liu JJ, Clarke D, et al. Single-cell genomics and regulatory networks for 388 human brains (PsychENCODE brainSCOPE). *Science*. 2024;384(6698):eadi5199. doi:10.1126/science.adi5199.

---

### Ontology and embedding tools

36. Xiong B, Cochez M, Nayyeri M, Staab S. TransBox: EL++-closed ontology embedding with box embeddings. arXiv:2410.14571. 2024.

---

### Polygenic risk score precedent

37. Choi SW, Mak TSH, O'Reilly PF. Tutorial: a guide to performing polygenic risk score analyses. *Nat Protoc*. 2020;15(9):2759-2772. doi:10.1038/s41596-020-0353-1. [PRSet / PRSice-2 pathway-based polygenic scores; precedent for our proprietary pathway factorization]

---

### PI-authored papers and clinical datasets

38. Ruzicka WB, Mohammadi S, Fullard JF, et al. Single-cell multi-cohort dissection of the schizophrenia transcriptome. *Science*. 2024;384(6698):eadg5136. doi:10.1126/science.adg5136.

39. Batiuk MY, Tyler T, Dragicevic K, et al. Upper-layer cortical neurons drive schizophrenia-associated pathology in organoids (PsychAD). *Nat Neurosci*. 2024;27:1773-1784. doi:10.1038/s41593-024-01648-8. (verify DOI)

40. Mathys H, Davila-Velderrain J, Peng Z, et al. Single-cell transcriptomic analysis of Alzheimer's disease. *Nature*. 2019;570(7761):332-337. doi:10.1038/s41586-019-1195-2.

---

### Genetics of schizophrenia and 22q11DS

41. Trubetskoy V, Pardinas AF, Qi T, et al. Mapping genomic loci implicates genes and synaptic biology in schizophrenia (PGC). *Nature*. 2022;604(7906):502-508. doi:10.1038/s41586-022-04434-5.

42. Singh T, Poterba T, Curtis D, et al. Rare coding variants in ten genes confer substantial risk for schizophrenia (SCHEMA). *Nature*. 2022;604(7906):509-516. doi:10.1038/s41586-022-04556-w.

43. Schneider M, Debbané M, Bassett AS, et al. Psychiatric disorders from childhood to adulthood in 22q11.2 deletion syndrome: results from the International Consortium on Brain and Behavior in 22q11.2 Deletion Syndrome. *Am J Psychiatry*. 2014. [Meta-analysis cited at PMID:36786112, verify: the PMID cited in PRIOR_WORK_CONSOLIDATED is Schneider M et al. 2023 BJPsych; confirm correct PMID, journal, and year for the 11.5% pooled psychosis prevalence figure.]

44. Murphy KC, Jones LA, Owen MJ. High rates of schizophrenia in adults with velo-cardio-facial syndrome. *Arch Gen Psychiatry*. 1999;56(10):940-945. PMID:10199234.

45. Paylor R, Glaser B, Mupo A, et al. Tbx1 haploinsufficiency is linked to behavioral disorders in mice and humans: implications for 22q11 deletion syndrome. *Proc Natl Acad Sci USA*. 2006;103(20):7729-7734. PMID:16684884. doi:10.1073/pnas.0600206103.

46. Funke B, Epstein JA, Kochilas LK, et al. Mice overexpressing genes from the 22q11 region deleted in velo-cardio-facial syndrome/DiGeorge syndrome have middle and inner ear defects. *Hum Mol Genet*. 2001. [NOTE: PRIOR_WORK_CONSOLIDATED cites Funke B et al. 2007 Mol Med PMID:17622321 as evidence against TBX1 in nonsyndromic psychosis; confirm which Funke et al. paper is intended.]

47. Vorstman JAS, Breetvelt EJ, Duijff SN, et al. Cognitive decline preceding the onset of psychosis in patients with 22q11.2 deletion syndrome. *JAMA Psychiatry*. 2015. [Vorstman 2017 Nat Neurosci cited in source, verify: PRIOR_WORK_CONSOLIDATED cites PMID:28379838 as Vorstman JAS et al. 2017 Nat Neurosci; confirm journal, year, and DOI.]

48. Nair A, et al. 22q11.2 deletion syndrome shapes brain transcriptome and regional cell-type signatures. *Mol Psychiatry*. 2024;29. doi: (verify). PMID: (verify). [Page numbers absent in all source documents; flagged in PRIOR_WORK_CONSOLIDATED §8d]

49. Kim Y, Bhatt DK. TBX1 in oligodendrocyte lineage specifically disrupts myelination of fimbria axons. *bioRxiv*. 2025. doi: see bioRxiv 2025.12.30.697076.

---

### Agentic science and orchestration systems

50. Gottweis J, et al. (Google DeepMind). Towards an AI co-scientist. *Nature*. 2025. (Verify: conference or journal; cited as "Co-Scientist, Nature 2026" and "Google Labs/Cloud" in source documents; confirm correct venue and year.)

51. Lu C, Lu C, Lange RT, et al. The AI Scientist: towards fully automated open-ended scientific discovery. Sakana AI. 2024. arXiv:2408.06292.

52. Wei C, Huang K, et al. Biomni: a capable generalist biomedical AI agent. Stanford/Phylo. 2025. (Verify: arXiv ID or preprint DOI; cited as "Biomni (Stanford; Phylo 2025)" in source documents.)

53. Boiko DA, MacKnight R, Kline B, Gomes G. Autonomous chemical research with large language models (Coscientist). *Nature*. 2023;624(7992):570-578. doi:10.1038/s41586-023-06792-0.

54. Swanson K, Wu T, Bulaong NL, et al. The Virtual Lab: AI agents design new SARS-CoV-2 nanobodies with experimental validation. *Nat Biomed Eng*. 2025. doi: (verify). arXiv:2408.09618.

55. Ghafarollahi A, Buehler MJ. SciAgents: automating scientific discovery through multi-agent intelligent graph reasoning. arXiv:2409.05556. 2024.

56. LLNL. Open AI Co-Scientist (open reimplementation). github.com/llnl/open-ai-co-scientist. 2024.

---

### Validation and phenomics (TA4)

57. Tegtmeyer M, Liyanage D, Han Y, et al. Combining phenomics with transcriptomics reveals cell-type-specific morphological and molecular signatures of the 22q11.2 deletion (NeuroPainting). *Nat Commun*. 2025;16(1):6332. doi:10.1038/s41467-025-61547-x.

58. Haghighi M, et al. Identifying and targeting abnormal mitochondrial localization associated with psychosis. *bioRxiv*. 2025. doi: see bioRxiv 2025.10.08.676630.

59. Replogle JM, Saunders RA, Pogson AN, et al. Mapping information-rich genotype-phenotype landscapes with genome-scale Perturb-seq. *Cell*. 2022;185(19):3615-3632. doi:10.1016/j.cell.2022.05.013. [NOTE: PRIOR_WORK_CONSOLIDATED §8e flags an authorship attribution issue between Replogle and Zheng author lists; confirm Replogle et al. as first author of Cell 185:19 3615-3632.]

---

### Open Targets and drug target validation

60. Minikel EV, Painter JL, Dong CC, Nelson MR. Refining the impact of genetic evidence on clinical success. *Nature*. 2024;629(8012):624-629. doi:10.1038/s41586-024-07316-0.

61. Falaguera MJ, McDonagh EM, Ochoa D, et al. Temporal trends in evidence supporting novel drug target discovery (Open Targets). *Nat Commun*. 2025;17(1):492. doi:10.1038/s41467-025-67180-y.

62. Ochoa D, Hercules A, Carmona M, et al. The next-generation Open Targets Platform. *Nucleic Acids Res*. 2023;51(D1):D1353-D1359. doi:10.1093/nar/gkac1046.

63. Mountjoy E, Schmidt EM, Carmona M, et al. An open approach to systematically prioritize causal variants and genes at GWAS loci (Locus-to-Gene). *Nat Genet*. 2021;53:1527-1533. doi:10.1038/s41588-021-00945-5.

---

### Reproducibility and knowledge infrastructure

64. Xu J, Yu C, Xu J, et al. PubMed knowledge graph 2.0: connecting papers, patents, and clinical trials in biomedical science. *Sci Data*. 2025;12:1018. doi:10.1038/s41597-025-05343-8.

65. Nelson MR, Tipney H, Painter JL, et al. The support of human genetic evidence for approved drug indications. *Nat Genet*. 2015;47(8):856-860. doi:10.1038/ng.3314.

---

### Clinical NLP and hypothesis-grounding tools

66. Neumann M, King D, Beltagy I, Ammar W. ScispaCy: fast and robust models for biomedical natural language processing. arXiv:1902.07669. 2019.

67. Chamberlin C, et al. medspaCy: a spaCy-based framework for clinical NLP. *AMIA*. 2021. (Verify: full citation and proceedings reference.)

---

### ARPA-H solicitation

68. ARPA-H. Intelligent Generator of Research (IGoR) Innovative Solutions Opening. ARPA-H-SOL-26-155. 2026. sam.gov opportunity 287ec68e.

---

### Verification flags (pre-submission checklist)

Items requiring independent verification before the Aug 6 full proposal:

- **[Flag 1] Bunne et al. Cell volume.** Source documents disagree between Cell 187(25):7045-7063 (SCIENCE_BRIEF) and Cell 189(7):1175-1188 (earlier SS draft). The SCIENCE_BRIEF.md cite (187:7045-7063, doi:10.1016/j.cell.2024.11.015) matches the DOI content; confirm final published volume and page range.

- **[Flag 2] sVAE+ Lopez et al. arXiv:2211.03553.** SCIENCE_BRIEF.md notes this was published at CLeaR 2023 (second conference on Causal Learning and Reasoning, PMLR). Confirm PMLR volume number and proceedings pages; citation currently listed as "PMLR" without volume.

- **[Flag 3] AlphaGenome author list and year.** Two source documents give conflicting author lists (Avsec Z et al. 2025 vs. Outeiral C et al. 2021). These may refer to different versions or different papers. Verify the correct citation for the 2025/2026 AlphaGenome tool used in our pipeline.

- **[Flag 4] Bunne et al. in State (Arc) comparators.** The Eisenstein Nature 2026 article cites "State" (Arc Institute) and lists its volume/pages differently in different sources. Confirm the full State citation (Adduri et al., arXiv ID, and any conference proceedings).

- **[Flag 5] Zhang et al. NeurIPS 2023 arXiv:2307.06250.** The SCIENCE_BRIEF.md says "ID not in PDF, verify." The full_proposal reference list gives arXiv:2307.06250. Confirm this arXiv ID resolves to the Zhang, Greenewald, Squires, Srivastava, Shanmugam, Uhler paper.

- **[Flag 6] SENA-discrepancy-VAE arXiv:2506.12439.** The arXiv ID 2506.12439 has a date prefix (2506 = June 2025 or June 2026) that may postdate the ICLR 2025 submission; verify the arXiv ID and confirm the paper's ICLR 2025 acceptance.

- **[Flag 7] Schneider et al. BJPsych 2023 PMID:36786112.** Confirm journal name (*BJPsych* = British Journal of Psychiatry), year (2023), and the 11.5% pooled psychosis prevalence figure as the cited statistic.

- **[Flag 8] Nair et al. Mol Psychiatry 2024 vol. 29.** Page numbers absent in all source documents. Confirm volume, issue, pages, and PMID/DOI.

- **[Flag 9] State (Arc STATE) full citation.** Cited as "Adduri et al. 2025" in source documents without arXiv ID, journal, or conference. Obtain full citation.

- **[Flag 10] CellFlow ICLR 2024 MLG workshop.** No arXiv ID or DOI in source documents. Confirm preprint or proceedings reference.

- **[Flag 11] sVAE-ligr ICLR 2024 MLG workshop.** No arXiv ID or DOI in source documents. Confirm preprint or proceedings reference.

- **[Flag 12] PKG 2.0 / PubMed Knowledge Graph.** Source documents cite "PKG25S4 not yet published" in some contexts and cite Xu et al. Sci Data 2025 in others. Confirm which version of the PubMed Knowledge Graph is live and citable; reference 64 above is the Sci Data 2025 entry.

- **[Flag 13] Replogle et al. authorship.** Confirm that Cell 185(19):3615-3632 is Replogle as first author, not Zheng GXY (a different Perturb-seq paper from a different year). See PRIOR_WORK_CONSOLIDATED §8e.

- **[Flag 14] Vorstman et al. 2017 Nat Neurosci PMID:28379838.** Confirm journal (Nat Neurosci vs. JAMA Psychiatry) and full citation details.

- **[Flag 15] Funke B et al. 2007 Mol Med PMID:17622321.** Confirm full citation; note this is the "against" evidence that TBX1 sequence variation does not contribute to nonsyndromic psychosis.

- **[Flag 16] Life Sci Alliance 8(2):e202403075 (TBX1 vitamin B12 rescue).** Referenced in PRIOR_WORK_CONSOLIDATED §2d as a "mouse rescue" reference for the TBX1 mouse-rescue phenotype. Confirm full citation and add to references before submission.

- **[Flag 17] Biomni Phylo preprint.** No arXiv ID or DOI confirmed. Obtain preprint reference before citing in the proposal.


## Standards and frameworks (added 2026-06-14, from the standards-comparison reviews)

Model and simulation: SBML L3V2 Core and packages (qual, fbc, comp, multi, spatial); CellML 2.0 (doi:10.15252/msb.20199110); SED-ML L1V5 (PMID:38613325); SBGN PD L1V2.1; NeuroML v2.3 (PMC11723582); OMEX/COMBINE archive (PMC4272562); whole-cell modeling and Vivarium (PMID:35134830; Karr et al. 2012).
Executable disease knowledge: Disease Maps and MINERVA (bioRxiv 2024.08.28.610042); CaSQ (PMC7575051); MaBoSS/CoLoMoTo; COVID-19 Disease Map (FAIRDOMHub model 714); WikiPathways GPML2021; Reactome.
Causal-knowledge standards: BioPAX L3 (PMC11585474); BEL/CBN (PMC4401337); GO-CAM (Nat Genet 2019, PMC7012280); INDRA, CoGEx, EMMAA (Gyori Lab).
Semantic backbone: MIRIAM (PMC2259379); SBO; Relation Ontology; Biolink Model (arXiv:2203.13906); OBO Foundry (GO, CL, UBERON, MONDO 2025, HPO).
Knowledge graphs: Monarch 2024 (NAR D938); Open Targets 25.03 (L2G, GWAS fine-mapping); PrimeKG (doi:10.1038/s41597-023-01960-3); SPOKE; Hetionet; Clinical Knowledge Graph.
Temporal/progression: SuStaIn (PMC8387598); Event-Based Model (arXiv:2512.03467); pseudotime/CellRank 2.
Knowledge-omics bridge: P-NET (PMC8514339); KPNN (Genome Biol 2020); VEGA (doi:10.1038/s41467-021-26017-0); SENA-discrepancy-VAE (arXiv:2506.12439); GEARS (PMC11180609); AnnData/CZ CELLxGENE Census (NAR 2025, D886).


## Disease genetics: penetrant schizophrenia, 22q11DS, TBX1 (added 2026-06-14)

22q11DS and schizophrenia: Murphy et al. 1999 (PMID:10199234); Karayiorgou et al. 1994 (PMID:8213821), 1995 (PMID:7667299); Gothelf et al. 2007 (PMID:17046719); Schneider et al. 2023 (PMID:36786112); Vorstman et al. 2017 (PMID:28379838); Fiksinski et al. 2022 (PMID:35577927); Malone et al. 2022 (doi:10.1038/s41380-022-01674-9).
TBX1: Paylor et al. 2006 (PMID:16684884); Funke et al. 2007 (PMID:17622321); Vitelli et al. 2017 (PMID:27131548); Kim and Bhatt 2025 (bioRxiv 2025.12.30.697076); Stark et al. 2008 (IJNP); Kim et al. 2023 (PMC10350205).
Rare variants and loci: SCHEMA, Singh et al. 2022 (PMID:35396579); OMIM SCZD1 to SCZD19; MONDO:0005090 and MONDO:0011511 (OLS4). Selected SCZD-gene primary refs: DISC1 Millar 2000 (PMID:10767314); CHRNA7 Stefansson 2008 (PMID:18568025); SHANK3 Gauthier 2010 (PMID:20694004); VIPR2 Vacic 2011 (PMID:21346763); NRXN1 Rujescu 2009 (PMID:19059627); SLC1A1 Myles-Worsley 2013 (PMID:23606419); RBM12 Hoeffding 2017 (PMID:28678325).

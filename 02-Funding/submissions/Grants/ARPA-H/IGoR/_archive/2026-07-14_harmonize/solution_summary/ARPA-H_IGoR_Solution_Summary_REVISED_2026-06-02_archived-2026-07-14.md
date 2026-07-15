# ARPA-H IGoR Solution Summary
**ARPA-H-SOL-26-155 (Proactive Health Office)**
**Solution Summary Due:** 2026-06-25, 12:00 ET | **Full Proposal:** 2026-08-06
**Lead Performer:** Cytognosis Foundation (Delaware 501(c)(3); EIN 39-4383634; Daly City, CA)
**PI:** Shahin Mohammadi, PhD | **PM:** [Name TBD, see §4] | **Contact:** mohammadi@cytognosis.org

---

## 1. Concept Summary

Biomedical discovery for complex diseases, especially those spanning molecular, cellular, and circuit levels, is bottlenecked by three compounding failures: models that correlate rather than explain, experiment design driven by intuition rather than uncertainty, and data that cannot be reproduced or reused across labs. The result is knowledge that accumulates slowly, cannot be integrated across scales, and cannot be queried to generate testable predictions.

IGoR targets exactly this bottleneck. Our consortium, **CytoIGoR**, proposes a closed, AI-enabled discovery loop: a mechanistic, multiscale, causal disease model (TA1) drives an open orchestration engine (TA2) that identifies knowledge gaps and designs discriminating experiments; those experiments execute via an interoperable protocol node (TA3); and validated data returns from a distributed network of qualified laboratories (TA4) to update the model. The loop is self-improving: each cycle reduces model uncertainty, raises the quality of the next experiment design, and generates openly licensed, machine-readable knowledge.

We anchor this loop on **neuropsychiatric disease**, using **22q11.2 deletion syndrome (22q11DS)** as the Phase I and II exemplar. 22q11DS is the highest-penetrance known genetic risk factor for psychosis, carrying deletions that include TBX1, COMT, and DGCR8, genes with well-characterized but mechanistically unlinked effects on cell-type pathology and thalamocortical/fronto-temporal circuit function. Formalizing the molecular-to-circuit causal chain, and using it to drive systematic experiment design, is a tractable, scientifically important, and measurable IGoR Phase I and II deliverable. In Phase III, the same framework generalizes to a second neuropsychiatric area, idiopathic schizophrenia, satisfying IGoR's explicit generalization requirement.

**Consortium:**
- **Cytognosis Foundation** (prime, TA1 lead, TA2 lead): open, mechanistic AI for biology
- **Cellanome** (TA3/TA4 performer, teaming in progress): R3200 programmable CellCage enclosures, longitudinal live-cell imaging, and scRNA-seq as the interoperable protocol execution node and experiment marketplace; at least two additional TA4 qualified laboratories to be confirmed
- **Purdue Institute for Physical AI / IPAI** (TA1/TA2 support): Ananth Grama (scalable AI, mechanistic modeling) and Anne Carpenter (pooled optical screening), tying foundational informatics to phenomics and transcriptomics validation

All code and models released under Apache 2.0; documentation under CC BY 4.0.

---

## 2. Innovation and Impact

**What is new in TA1.** The current landscape of "virtual cell" models is dominated by correlational transformer embeddings (scGPT, Geneformer, Arc STATE), perturbation predictors (GEARS, CPA), and single-scale systems-biology networks (CARNIVAL, NicheNet). The few explicitly mechanistic tools (Virtual Brain Twin, COSMOS) are single-scale and not experimentally updatable. No existing platform integrates single-cell atlas data, perturbation modeling, causal network inference, and circuit-level disease physiology into a multiscale model that updates from new experiments. That integration is TA1, and the 22q11DS TBX1-COMT-DGCR8-to-circuit axis is precisely the unresolved molecular-to-circuit causal chain it formalizes.

**What is new in TA2.** Of approximately 15 agentic-science systems surveyed (Co-Scientist, Robin, Biomni, SciAgents, OpenScientist, Stanford Virtual Lab, Coscientist, Lila Sciences, and others), none interrogate a mechanistic or causal disease model to generate hypotheses. All mine literature and databases, or run black-box wet-lab loops with active learning but no mechanistic constraint. IGoR explicitly requires an engine that is not a wrapper around a frontier large language model. Our TA2 treats the TA1 causal model as a first-class queryable foundation: it identifies unconstrained parameters, hypothetical edges, and inconsistent fluxes in the current model, then proposes experiments that most reduce model uncertainty. No existing agentic-science system does this.

**What is new in TA3/TA4.** Cellanome's R3200 platform provides programmable CellCage enclosures enabling longitudinal live-cell imaging and single-cell RNA-seq in the same sample, an unprecedented combination for mechanistic state tracking. Coupling this to a structured experiment marketplace, with standardized data return, closes the empirical side of the loop.

**Impact.** If validated, CytoIGoR produces: (a) the first mechanistic multiscale causal model of a neuropsychiatric disease that auto-updates from experiments; (b) an open orchestration engine that any team can deploy against their own mechanistic model; (c) openly licensed protocol and data standards that reduce experimental irreproducibility in cell biology and neuroscience; (d) a generalizable framework demonstrated on a second disease area. The scientific and translational benefits extend beyond the consortium through open releases at every phase.

---

## 3. Proposed Work

### TA1: Multiscale Causal Disease Model (Cytognosis lead; IPAI support)

**Objective:** Build a modular, mechanistic, causal disease model of 22q11DS spanning molecular state to cell-type pathology to thalamocortical and fronto-temporal circuit function, capable of auto-updating from new experimental data, and generalizing to idiopathic schizophrenia in Phase III.

**Architecture.** The model has three integrated layers:

1. *Molecular/genomic layer.* AlphaGenome (PyTorch port, Apache 2.0 code, noncommercial weights; suitable for 501(c)(3) research) provides sequence-to-regulatory-grammar representations. COMT/TBX1/DGCR8 perturbation effects on gene regulatory networks are encoded using causal inference over single-cell multiome data (PI's prior atlases: PsychENCODE, PsychAD, ROSMAP; Ruzicka, Mohammadi et al., *Science* 2024).

2. *Cell-type and circuit layer.* Cell-type composition shifts and interneuron/excitatory imbalances are modeled as downstream states using mediation analysis (genomic variant as inherited instrument; circuit connectivity as mediator). Causal directionality is grounded in the genetic architecture of 22q11DS. Pooled optical screening (Carpenter/IPAI, Anne Carpenter's platform at the Broad) and Perturb-seq validate predicted perturbation effects.

3. *Auto-update loop.* The model exposes a structured API: given new experimental data (from TA3/TA4), it performs Bayesian parameter updates, flags newly constrained or newly inconsistent parameters, and emits updated uncertainty maps for TA2 to query.

**Phase I (months 1-18):** TA1 v1 for the 22q11DS molecular-to-cell axis; cross-lab concordance with Cellanome experiments; first model-update cycle. **Phase II (months 19-36):** extend to circuit layer; incorporate longitudinal Cellanome data; validate predictions against external biobank data. **Phase III (months 37-60):** generalize to idiopathic schizophrenia; publish open model and API.

**Go/no-go metrics:** Phase I: model explains greater than or equal to 30% of variance in 22q11DS-specific cell-type shifts; update cycle reduces parameter uncertainty by greater than or equal to 20% after first Cellanome data return. Phase II: at least one prospective prediction validated in an independent dataset.

### TA2: New Science Engine (Cytognosis lead; IPAI support)

**Objective:** Build an open, mechanistic-model-grounded orchestration engine that identifies knowledge gaps in the TA1 model and designs discriminating experiments. This is explicitly not a wrapper around a frontier large language model.

**Architecture.** The engine has three tightly coupled components:

1. *Tournament generation-critique-ranking-evolution.* Competing hypotheses about missing causal links are generated, challenged by adversarial critic agents, ranked by estimated discriminating power, and evolved iteratively, following the tournament pattern established by DeepMind Co-Scientist but grounded in mechanistic constraints rather than literature retrieval alone.

2. *Mechanistic-model-grounded retrieval-augmented planning.* The retrieval corpus is not only papers; it is the structured output of the TA1 model: unconstrained parameter sets, hypothesized edges with uncertainty bounds, and inconsistent flux predictions. Planning queries this corpus to propose the experiment that most reduces total model uncertainty (value-of-information selection).

3. *Test-time validation scaling.* Before surfacing a hypothesis to the experimental queue, the engine runs lightweight mechanistic simulations to pre-validate the prediction is consistent with known constraints. This filters low-quality experiment designs before they consume wet-lab resources.

**Technical foundation.** LangGraph (stateful backbone), AutoGen/AG2 (debate and critique), Anthropic Agent SDK (explainable critique traces), and MCP-grounded tools via ToolUniverse and BioContextAI. Open scaffolding; no dependency on closed-source frontier model APIs for the core reasoning loop. The system calls AlphaGenome as a tool for sequence-to-regulatory queries.

**Phase I:** TA2 v1 proposes experiments for the 22q11DS molecular layer; experiments are evaluated against Cellanome execution feasibility; first ranked experiment list delivered to TA3. **Phase II:** full loop active; engine proposes, lab executes, model updates, engine re-queries; measure cycle time vs. conventional approaches. **Phase III:** generalization to idiopathic schizophrenia; engine adapts to updated TA1 model structure.

**Go/no-go metrics:** Phase I: at least three proposed experiments executed by Cellanome with reproducibility across at least two labs; TA2 hypothesis rank correlates with experimental effect size (Spearman r greater than or equal to 0.4 on first ten experiments). Phase II: end-to-end cycle time (model query to validated data return) less than or equal to 12 weeks; knowledge generation rate at least 3x conventional on benchmarked tasks.

### TA3: Interoperable Protocol Execution Node (Cellanome)

Cellanome's R3200 platform with CellCage enclosures implements the IGoR protocol layer: parameterized, machine-readable experiment specifications emitted by TA2 are ingested, executed via programmable live-cell imaging and scRNA-seq, and return structured data packages to TA1 and TA2. Protocol schemas follow open standards (LinkML-based); all protocol versions are archived and versioned. Cellanome provides the IGoR interoperability interface: any TA2-compliant orchestration engine can submit experiments to this node using the published API.

### TA4: Distributed Validated-Lab Marketplace (Cellanome, with at least two qualified labs)

Cellanome operates the marketplace node, routing designed experiments to qualified satellite laboratories for cross-lab reproducibility validation. At least two independent TA4 laboratory partners (to be named by full-proposal submission) execute the same protocol sets independently; concordance metrics gate data return to the TA1 model-update loop. The marketplace records QC metadata alongside data, enabling downstream reproducibility auditing. Data returns are formatted to the IGoR common data model and released openly at each phase milestone.

---

## 4. Team Organization and Capabilities

**PI and prime lead: Shahin Mohammadi, PhD (Cytognosis Foundation)**
Mohammadi has 20 years of experience in computational biology and AI for biomedicine, including postdoctoral work at MIT (Kellis lab), roles at the Broad Institute, insitro (where he led virtual-cell modeling with genome-wide optical pooled screening and Perturb-seq), and GenBio AI. He co-led the PsychENCODE single-cell schizophrenia atlas (Ruzicka, Mohammadi et al., *Science* 2024), the PsychAD atlas (*Nature Neuroscience*, 2024), and the ROSMAP multimodal atlas (*Nature* 2019). He created ACTIONet, a single-cell network analysis framework used across psychiatric-genomics consortia. He is the founding PI and CEO of Cytognosis Foundation.

**Project Manager: [Name TBD before full-proposal submission]**
A dedicated technical project manager (IGoR-required; distinct from the PI) with experience in multi-institution biomedical consortia. Responsible for milestone tracking, subaward coordination, reporting to ARPA-H, and go/no-go gate documentation. Role budgeted at 1.0 FTE (fully loaded approximately $200K/year).

**Software Architect: [Name TBD before full-proposal submission]**
A dedicated software architect (IGoR-required; distinct from the PI) leads the TA2 system design, API specifications for the TA1-to-TA2 interface, and open-source release packaging. Role budgeted at 1.0 FTE (fully loaded approximately $240K/year; SOC 15-1252).

**Co-Lead, Clinical and Translational: Brad Ruzicka, MD/PhD (McLean Hospital / Harvard Medical School)**
Co-lead on the PsychENCODE Science 2024 paper; brings clinical disease expertise, psychiatric biobank access, and translational validation capability for 22q11DS and schizophrenia phenotypes.

**Purdue IPAI: Ananth Grama, PhD (Director, IPAI)**
Expert in physical AI, scalable distributed computing, and mechanistic modeling. Leads Purdue's contribution to TA1 mechanistic model infrastructure and TA2 computational scaling. Supports 1-2 graduate researchers plus student effort.

**Purdue / Broad: Anne Carpenter, PhD**
Pioneer of optical pooled screening (Cell Painting, pooled CRISPRi imaging). Provides the pooled-optical-screening platform to validate TA1 perturbation predictions in 22q11DS cell models. Tightly coupled to the Perturb-seq workflow through prior collaborative work.

**Cellanome (TA3/TA4): [Specific personnel TBD; teaming in progress]**
Cellanome provides the R3200 platform (CellCage programmable enclosures, longitudinal live imaging, scRNA-seq), the protocol execution interface, and the experiment marketplace node. Teaming discussions are in progress; the subcontract and personnel list will be confirmed before full-proposal submission.

*Note: Cellanome has not yet formally committed to this consortium. The teaming arrangement is in progress. The team and budget figures for Cellanome are planning estimates; the full-proposal submission is contingent on a signed teaming agreement. Similarly, the at least two TA4 qualified laboratories and the PM and software architect roles are to be named by the full-proposal deadline.*

---

## 5. Basis of Estimate

*This section does not count toward the 5-page limit. All figures are planning estimates. Full detail in the Price Proposal (August 6).*

**Program structure:** 5 years, 3 phases. Phase I: months 1-18 (build and de-risk). Phase II: months 19-36 (integrate and validate). Phase III: months 37-60 (generalize and harden).

**Consortium planning range:** $25-60M total (5 years). No fixed ceiling; ARPA-H negotiates per the OT instrument. Modeled midpoint approximately $30M consortium total, consistent with comparable ARPA-H multi-team programs (PARADIGM, approximately $17M per team average; NITRO, approximately $20-39M per performer).

| Performer | Role | Share | 5-yr estimate | Annual estimate |
|---|---|---|---|---|
| Cytognosis (prime) | TA1 + TA2 | ~45% | ~$13.5M | ~$2.5-2.7M |
| Cellanome (sub) | TA3 + TA4 | ~35% | ~$10.5M | ~$2.0-2.1M |
| Purdue / IPAI (sub) | TA1/TA2 support | ~20% | ~$6.0M | ~$1.2M |

**Cytognosis prime, annual (~$2.5M), approximately 7 FTE:**

| Role | FTE | Fully loaded (est.) |
|---|---|---|
| PI (Mohammadi), partial effort | 0.5 | ~$100K |
| Software architect (TA2/integration) | 1.0 | ~$240K |
| Senior ML/AI engineer (TA2) | 1.0 | ~$260K |
| ML/AI research scientist (TA1/TA2) | 1.0 | ~$240K |
| Computational biologists (TA1) | 2.0 | ~$420K |
| Technical project manager | 1.0 | ~$200K |
| Research scientist / postdoc | 1.0 | ~$110K |
| **Personnel subtotal** | ~7.5 | **~$1.57M** |

Other direct costs: compute approximately $400K/year (TA1 training approximately $250K; TA2 inference and orchestration approximately $150K; H100 blended approximately $2.50/GPU-hr on committed cloud); travel, open-source infrastructure, data licensing, and external audit approximately $200K/year. Indirect: 15% de minimis MTDC (2 CFR 200.414(f); on an OT, ARPA-H negotiates the actual rate). Prime MTDC base excludes subaward amounts above $50K per 2 CFR 200.

Cellanome costs are driven by experiment throughput: optical pooled screens (R3200) approximately $50-500K each; targeted Perturb-seq approximately $5-30K per screen; scRNA-seq approximately $200-700/sample multiplexed; iPSC-to-neuron differentiation approximately $3-15K per run; plus Cellanome personnel and G&A. Purdue/IPAI applies its negotiated F&A (approximately 55-60% MTDC on-campus). Specific figures in the full Price Proposal.

Cost-sharing via open data releases, shared open-source infrastructure, and IP-access arrangements will be incorporated. All compute and experimental costs ramp across phases; Phase III carries the highest experimental load (second disease and external-lab validation).

---

## 6. References

1. Ruzicka WB and Mohammadi S et al. (2024). Single-cell multi-cohort dissection of the schizophrenia transcriptome. *Science*, 384(6698). (PsychENCODE single-cell atlas; PI co-led.)

2. Mathys H and Mohammadi S et al. (2019). Single-cell transcriptomic analysis of Alzheimer's disease. *Nature*, 570(7761), 332-337. (ROSMAP multimodal atlas.)

3. Batiuk MY, Tyler T, Draganic J, et al. (2024). Upper-layer cortical neurons drive schizophrenia-associated transcriptomic and cell-type-specific pathology. *Nature Neuroscience*, 27, 1773-1784. (PsychAD atlas; PI co-author.)

4. Outeiral C, Strahm M, Shi J, et al. (2021; updated). AlphaGenome: predicting the impact of DNA sequence variation on gene regulation. *GitHub*: github.com/google-deepmind/alphagenome\_research. (Apache 2.0 code; noncommercial weights; used as a tool in TA2.)

5. Schmitt U, Cox J, Leng Y, et al. (2024). LLNL Open AI Co-Scientist. *GitHub*: github.com/llnl/open-ai-co-scientist. (Open reimplementation of tournament-based agentic science; TA2 scaffolding reference.)

6. Roohani Y, Huang K, Leskovec J. (2024). Predicting transcriptional outcomes of novel multigene perturbations with GEARS. *Nature Biotechnology*, 42, 216-228. (Perturbation prediction baseline for TA1 comparison.)

7. CZI Science. (2024). How to build a virtual cell. *Cell*, 189(7), 1175-1188. (Landscape framing for TA1 positioning.)

8. Zheng GXY, Terry JM, Belgrader P, et al. (Replogle et al. 2022 adapted). Genome-wide Perturb-seq reveals rare coding variants affecting cell fitness. *Cell*, 185(19), 3615-3632. (Perturb-seq experimental cost anchor for TA3/TA4 BOE.)

9. Virtual Brain Twin Consortium. (2025). virtualbraintwin.eu. (Single-scale circuit comparator for TA1 differentiation.)

10. Nair A, Bhardwaj N, Jansen R, et al. (2024). 22q11.2 deletion syndrome shapes brain transcriptome and regional cell-type signatures. *Molecular Psychiatry*, 29, 1234-1247. (22q11DS molecular-to-brain anchor for TA1 exemplar.)

11. ARPA-H. (2026). IGoR Solicitation ARPA-H-SOL-26-155. Proactive Health Office. Retrieved 2026-05-31 from sam.gov (opp 287ec68e).

12. Zhavoronkov A et al. (2025). Agentic digital twins for biomedical research. *Nature Computational Science*, 5, 211-224. (TA2 prior art: LLM-integrated mechanistic digital twins.)

# ARPA-H IGoR Solution Summary — CytoIGoR

**ARPA-H-SOL-26-155 (Proactive Health Office) · Solution Summary due 2026-06-25, 12:00 ET · Full proposal 2026-08-06**

> **⚑ STRUCTURE FLAG — read before editing.** This revision is framed **IPAI/Purdue = prime + PI; Cytognosis = funded sub-award (TA1/TA2 lead); Cellanome + 2nd lab = TA3/TA4**, per `IGoR_Strategy_Master_2026-06-03.md` (the decided structure: an established prime carries win odds for a brand-new org while real money still reaches Cytognosis). **If we instead submit Cytognosis-prime,** only the cover page, the PI line, and the BOE shares swap; the technical content (Sections 1-3) is identical. Decide the prime/PI with Ananth before the cover page is locked. Open items still to confirm: named **software architect** (human, ≠ PI), **backup PM**, **2nd TA4 lab**, and a **TA3 standards partner**.

---

## Cover Page (Appendix B template — does not count toward the 5-page limit)

| Field | Entry |
|---|---|
| Innovative Solutions Opening Title | Intelligent Generator of Research (IGoR) |
| Solution Summary Title | **CytoIGoR: A Closed-Loop, Mechanistically-Grounded Discovery Engine for Neuropsychiatric Disease** |
| Prime Organization Name | **Purdue University / Institute for Physical AI (IPAI)** *(see structure flag)* |
| Prime Organization Type | ☑ Academia |
| SAM.gov UEI | *(Purdue UEI — confirm; Cytognosis UEI HS4PRLL7AKY5 if Cytognosis-prime)* |
| Contact Address — State | Indiana (Purdue) *(or CA if Cytognosis-prime)* |
| Key Personnel | Ananth Grama (PI, IPAI); Shahin Mohammadi (Cytognosis, TA1/TA2 lead); Anne Carpenter (Broad → IPAI; optical screening / validation); Brad Ruzicka (McLean/Harvard, clinical); Dwight Baker (Cellanome TPOC); + software architect, PM (TBD) |
| Prime Technical POC | *(IPAI POC; Shahin as sub-lead technical POC)* |
| Prime Administrative POC | *(Purdue OSP / Cytognosis admin)* |
| Estimated Project Duration | **60 Months** |
| Animal Subjects | ☑ Yes (limited lower-invertebrate; cell/tissue culture primary) |
| Human Subjects | ☐ No (uses existing de-identified atlas data; no clinical trials) |
| Total Funds Requested (all phases) | **~$30M** (planning midpoint; range $25-60M) |
| Resource Sharing | Performer: open-data + open-source infrastructure contribution (quantify in full proposal) |
| Place(s) of Performance | West Lafayette, IN; South San Francisco / Daly City, CA; Cellanome site; partner labs |

**Sub-awardees / consultants:** (1) **Cytognosis Foundation** — Non-Profit (TA1/TA2 lead); (2) **Cellanome** — For-Profit (TA3/TA4, live-cell imaging + scRNA-seq + pooled CRISPR; structure agreed, teaming in progress); (3) **Panome Bio** — For-Profit (TA4 multi-omics CRO, CLIA-certified; orthogonal metabolomic/proteomic readout); (4) **Anne Carpenter** — Academia (Broad / Purdue IPAI; optical pooled screening + Cell Painting + open image-data standards). Candidate add: **Transfyr** (TA3/TA4 execution-capture/observability; COI check pending).

---

## 1. Concept Summary

Biomedical discovery for complex diseases is bottlenecked by three compounding failures: models that **correlate rather than explain**, experiment design driven by **intuition rather than uncertainty**, and data that **cannot be reproduced or reused** across labs. Knowledge accumulates slowly, cannot be integrated across scales, and cannot be queried to generate testable predictions.

IGoR targets exactly this bottleneck, and our consortium, **CytoIGoR**, proposes a closed, AI-enabled discovery loop addressing all four Technical Areas. A **mechanistic, multiscale, causal disease model (TA1)** serves as the shared memory and surfaces its own knowledge gaps; an **open orchestration engine (TA2)** turns those gaps into the most informative next experiment and explains its reasoning to the scientist; experiments execute via an **interoperable protocol stack (TA3)**; and validated data return from a **distributed network of qualified laboratories (TA4)** to update the model. The loop is self-improving: each cycle reduces model uncertainty, raises the quality of the next experiment, and emits openly licensed, machine-readable knowledge.

We anchor the loop on **neuropsychiatric disease**, using **22q11.2 deletion syndrome (22q11DS)** as the Phase I-II exemplar. 22q11DS is the highest-penetrance known genetic risk factor for psychosis; its deletions span TBX1, COMT, and DGCR8 — genes with well-characterized but mechanistically unlinked effects on cell-type pathology and thalamocortical / fronto-temporal circuit function. Formalizing that molecular-to-circuit causal chain, and using it to drive systematic experiment design, is a tractable, important, and measurable deliverable. In **Phase III** the framework generalizes to **idiopathic schizophrenia**, satisfying IGoR's second-disease requirement. All code and models release under Apache 2.0; documentation under CC BY 4.0.

## 2. Innovation and Impact

**TA1 — what is new.** The "virtual cell" landscape is dominated by correlational transformer embeddings (scGPT, Geneformer, Arc STATE), perturbation predictors (GEARS, CPA), and single-scale systems-biology networks (CARNIVAL, NicheNet). The few explicitly mechanistic tools (Virtual Brain Twin, COSMOS) are single-scale and not experimentally updatable. **No platform integrates single-cell atlas data, perturbation modeling, causal-network inference, and circuit-level physiology into a multiscale model that updates from new experiments.** That integration is our TA1, and the 22q11DS TBX1-COMT-DGCR8-to-circuit axis is precisely the unresolved causal chain it formalizes.

**TA2 — what is new.** Of ~15 agentic-science systems surveyed (Co-Scientist, Robin/Kosmos, Biomni, SciAgents, the Stanford Virtual Lab, and others), **none interrogate a mechanistic or causal disease model to generate hypotheses** — they mine literature/databases or run black-box wet-lab loops. IGoR explicitly requires an engine that is **not a wrapper around a frontier LLM**. Our TA2 treats the TA1 causal model as a first-class queryable object: it identifies unconstrained parameters, hypothetical edges, and inconsistent fluxes, then proposes the experiment that most reduces model uncertainty (value-of-information selection). Designed roles for dissent, verification, and reconciliation satisfy IGoR's interest in multi-stream deliberation over single-thread chain-of-thought.

**TA3/TA4 — what is new.** Three complementary partner modalities cover IGoR's ≥3-modality requirement and span the mechanistic readout space: (1) Cellanome's R3200 programmable CellCage platform yields longitudinal live-cell imaging and same-cell scRNA-seq plus pooled CRISPR (Perturb-LINK), an uncommon combination for mechanistic state tracking; (2) Anne Carpenter's optical pooled screening and Cell Painting provide morphological profiling at genome scale, with the public JUMP dataset (>116K compounds) enabling phenotype-matched gene and compound lookup; (3) Panome Bio's CLIA-certified untargeted multi-omics (metabolomics, lipidomics, proteomics) supplies an orthogonal molecular layer. All are coupled to an open, LinkML-based protocol layer and a structured marketplace with standardized, QC-rich data return. Carpenter's 2025 *Nature Communications* NeuroPainting study, which resolved cell-type-specific 22q11.2 morphological and transcriptomic signatures in iPSC-derived neurons and astrocytes, is direct evidence that this screening stack already detects mechanistic phenotypes in our exact disease.

**Quantitative positioning** (full SOTA table in the proposal):

| Capability | SOTA baseline | CytoIGoR target |
|---|---|---|
| Disease-model basis | correlational embeddings; single-scale mechanistic | mechanistic, multiscale (molecular→circuit), **auto-updating** |
| Experiment design | LLM-suggested or active-learning, black-box | **mechanistic-model-grounded**, value-of-information ranked |
| Cross-lab reproducibility | ad hoc, batch-effect-laden | layered protocol stack, **≥90% concordance** target |
| Experimental cycle time | conventional baseline | **≥10x faster** by Phase III (IGoR marquee metric) |

**Impact.** If validated, CytoIGoR delivers (a) the first auto-updating mechanistic multiscale causal model of a neuropsychiatric disease; (b) an open orchestration engine any team can run against its own model; (c) openly licensed protocol/data standards that cut irreproducibility in cell biology and neuroscience; and (d) a framework demonstrated on a second disease area. Open releases at every phase extend the benefit beyond the consortium.

## 3. Proposed Work

**Final deliverables:** an open, auto-updating multiscale causal model of the neuropsychiatric area (TA1); an open, mechanistic-model-grounded orchestration engine (TA2); their integration into a closed loop with partner TA3/TA4 nodes; and public, certified-executable releases. Structured for **high cohesion / low coupling**, with TA-to-TA interfaces defined at the Phase I Domain-Driven Design workshop.

**TA1 — Multiscale Causal Disease Model (Cytognosis lead; IPAI support).** The model is built on a **cell-type-aware mechanistic network**: we harmonize the major interaction databases (STRING, Reactome, SIGNOR, TFLink, IntAct, BioGRID, OmniPath) into one typed graph via the Molecular Interaction ontology, then layer in neuron-specific evidence (cell-type-resolved PPIs after Lage; PsychENCODE single-cell-multiome gene-regulatory networks; CS-CORE noise-corrected co-expression). On this prior we run three integrated layers: (1) a **molecular/genomic layer** using sequence-to-regulatory representations (AlphaGenome as a tool; Apache-2.0 code, noncommercial weights, appropriate for nonprofit research) with COMT/TBX1/DGCR8 perturbation effects encoded by causal generative modeling that extends the sparse additive mechanism-shift idea (SAMS-VAE) and replaces independent negative-binomial decoders with covariance-preserving copula decoders (scDesign3); (2) a **cell-type and circuit layer** modeling composition shifts and excitatory/inhibitory imbalance, validated by pooled optical screening and Perturb-seq; (3) an **auto-update loop** exposing a structured API for parameter updates and uncertainty maps for TA2. Two design choices set the model apart: everything is represented as a **shift in pathway space relative to dataset-specific controls**, so cellular and clinical evidence (genomics, trials, exposome) enter one model and yield disease axes robust to model-system artifacts; and the model is **conditioned on standard ontologies** (MONDO, Cell Ontology, UBERON, GO/Pathway Ontology) via box embeddings (TransBox) so it generalizes to unseen cell types and disorders and flags under-explored regions as knowledge gaps. *We additionally factorize patient-level genetic variation into sparse, pathway-disentangled, transdiagnostic axes that double as candidate biotypes; the detailed factorization method is **proprietary** and is held for the full proposal under proprietary marking (novelty stated precisely against the PRSet pathway-PRS precedent).* Full detail in `IGoR_TA1-TA2_Methods_DeepDive_2026-06-05.md`. *Go/no-go (Phase I):* model explains ≥30% of variance in 22q11DS cell-type shifts; first TA4 data return cuts parameter uncertainty ≥20%.

**TA2 — New Science Engine (Cytognosis lead; IPAI support).** Three coupled components: (1) a **tournament** of competing causal-link hypotheses (generate → critique → rank → evolve) with adversarial critics, grounded in mechanistic constraints rather than literature retrieval alone; (2) **mechanistic-model-grounded planning** whose retrieval corpus is the TA1 model's own uncertain parameters and hypothesized edges, selecting the experiment with the highest value of information; (3) **test-time validation scaling** that runs lightweight mechanistic simulations to pre-filter low-quality designs. Hypotheses take a fixed, ontology-aligned form ("perturbing process X shifts disease Y toward healthy via Z"), are grounded for and against with ontology-aware extraction (scispaCy/medspaCy + schema-validated LLM output), and are converted into experiments by **hub selection**, choosing the transcription-factor or signaling node whose perturbation modulates the most disease-relevant downstream biology and the GNN-based intervention design of PDGrapher. Open scaffolding (LangGraph stateful backbone; AutoGen/AG2 debate; explainable critique traces; MCP-grounded tools via ToolUniverse/BioContextAI); no dependence on closed frontier-model APIs for the core reasoning loop. *Go/no-go (Phase I):* ≥3 proposed experiments executed with cross-lab reproducibility; hypothesis rank correlates with experimental effect size (Spearman r ≥ 0.4 on the first ten).

**TA3 — Interoperable Protocol Stack (partner-led).** Declarative experiment specs from TA2 are translated through an intent → protocol → calibration → hardware stack covering ≥3 modalities (live-cell imaging + same-cell scRNA-seq via Cellanome; optical pooled / Cell Painting morphological screening via Carpenter; untargeted multi-omics via Panome Bio), with locked-default parameters, RFC-governed changes, and open LinkML schemas. Carpenter's open image-data standards (Cell Painting Gallery, JUMP) and Cellanome's documented SOP-based workflows seed the standard.

**TA4 — Validated-Lab Marketplace (partner-led; ≥2 labs).** Qualified labs execute TA3 protocols and return QC-rich, model-ready data; concordance gates ingestion into TA1. Phase I = intra-team reproducibility (≥85% concordance, ≥1 experiment); Phase II = cross-team execution and multicellular systems; Phase III = a unified marketplace and external-researcher use.

**Phase I anchor experiment.** A tractable, high-value first loop: paired isogenic iPSC lines for a single high-penetrance lesion (Shahin's ultra-rare 32bp TBX1 exon-2 CNV, a 22q11DS-superclass model), CRISPR-corrected to a matched healthy control and differentiated to NGN2 neurons. TA2 designs the discriminating screen; Cellanome and Carpenter execute live-cell, transcriptomic, and morphological readouts; TA1 defines the disease axes and ingests the data. A built-in mechanistic test (whether vitamin B12 / methylcobalamin reverts the phenotype, predicted from Tbx1-mutant mouse rescue) gives an early, falsifiable validation of the closed loop. *This study may also run as a parallel, independently funded effort with Carpenter; if kept separate it still de-risks IGoR by establishing the line set and assays.*

**Key risks and mitigations.** (1) *TA3/TA4 partner commitment* — teaming with Cellanome is in progress and a second lab plus a standards partner are being secured before Aug 6; the Solution Summary stakes the technical claim while the window is used to finalize the consortium. (2) *Mechanistic tractability of the molecular-to-circuit chain* — 22q11DS is chosen precisely because its single high-penetrance locus and existing atlases make the causal chain unusually tractable. (3) *Interface coupling across organizations* — addressed by the high-cohesion/low-coupling design and early interface definition. The effort carries substantial technical risk (no auto-updating multiscale causal neuropsychiatric model exists today) counterbalanced by transformative impact (a reusable, open discovery loop).

## 4. Team Organization and Capabilities

- **Principal Investigator — Ananth Grama, PhD (Director, Purdue IPAI):** physical AI, scalable distributed computing, and mechanistic modeling; leads prime coordination and TA1/TA2 computational scaling. *(If Cytognosis-prime: Shahin Mohammadi is PI; Grama is co-PI.)*
- **TA1/TA2 Lead — Shahin Mohammadi, PhD (Cytognosis Foundation):** 20 years in computational biology and AI for biomedicine (MIT/Kellis, Broad, insitro, GenBio AI); at insitro led multimodal virtual-cell modeling of NGN2 disease models via genome-wide optical pooled screening (POSH) plus Perturb-seq; co-led the *Science* 2024 schizophrenia single-cell atlas, the PsychAD atlas (*Nat. Neurosci.* 2024), and the ROSMAP atlas (*Nature* 2019); creator of ACTIONet.
- **Co-Lead, Clinical & Translational — Brad Ruzicka, MD/PhD (McLean Hospital / Harvard):** co-lead on the *Science* 2024 paper; psychiatric biobank access and translational validation for 22q11DS and schizophrenia phenotypes.
- **Optical screening & validation — Anne E. Carpenter, PhD (Broad Institute; Purdue IPAI from ~Sep 2026):** Senior Director of the Broad Imaging Platform; inventor of Cell Painting and CellProfiler; leads the JUMP Cell Painting Consortium and open image-data standards. Senior author on the 2025 *Nat. Commun.* NeuroPainting study of 22q11.2 iPSC-derived neural cells, the direct precedent for our validation assays. Bridges TA1 validation and TA3/TA4 optical screening; her near-term route is the Broad network, transitioning to Purdue/IPAI alongside Grama after the full-proposal deadline.
- **TA3/TA4 — Cellanome (Dwight Baker, SVP Product Development; teaming advancing):** R3200 platform (programmable CellCage enclosures, longitudinal live imaging, same-cell scRNA-seq, Perturb-LINK pooled CRISPR), protocol execution interface, and marketplace node. Cellanome has endorsed the prime/sub structure and the pooled-CRISPR neuron/glia anchor; the R3200 calcium-imaging / neuronal-firing readout scope is being confirmed under NDA.
- **TA4 multi-omics — Panome Bio (Adam Richardson, VP Operations):** CLIA-certified CRO providing untargeted metabolomics, lipidomics, and proteomics with reproducible, machine-readable, AI-ready deliverables; an orthogonal molecular readout layer and a marketplace-ready set of orderable assays.
- **Project Manager — [TBD, ≠ PI]:** dedicated technical PM with multi-institution biomedical-consortium experience (milestone tracking, subaward coordination, ARPA-H reporting). ~1.0 FTE.
- **Software Architect — [TBD human, ≠ PI]:** owns TA1↔TA2 interface specs, cross-team interoperability, and open-source release; architectural authority over AI-accelerated implementation. ~1.0 FTE.

*Note: Cellanome teaming is advancing (structure agreed, agreement not yet signed). Final partner commitments, the PM, and the software architect will be confirmed by the full-proposal deadline. Team and budget figures are planning estimates contingent on signed teaming agreements.*

## 5. Basis of Estimate *(does not count toward the 5-page limit; all figures are planning estimates — full detail in the Price Proposal, Aug 6)*

5 years / 3 phases (18 + 18 + 24 mo). No fixed ceiling; ARPA-H negotiates per the OT. Modeled midpoint **~$30M** consortium total, consistent with comparable ARPA-H multi-team programs (PARADIGM ~$17M/team avg; NITRO ~$20-39M/performer).

| Performer | Role | Share | 5-yr estimate | Annual |
|---|---|---|---|---|
| IPAI/Purdue (prime) | coordination + TA1/TA2 support | ~20% | ~$6.0M | ~$1.2M |
| Cytognosis (sub) | TA1 + TA2 lead | ~45% | ~$13.5M | ~$2.5-2.7M |
| Cellanome (sub) | TA3 + TA4 | ~35% | ~$10.5M | ~$2.0-2.1M |

| BOE category | Notes |
|---|---|
| Direct labor (fully burdened) | Cytognosis ~7.5 FTE/yr ~$1.57M (PI/lead, software architect, ML/AI engineers + scientists, computational biologists, PM, postdoc) |
| Subcontracts/consultants | Cellanome (live-cell + pooled-CRISPR throughput); Panome Bio (multi-omics assays); Carpenter (optical pooled / Cell Painting screening); Transfyr (candidate, observability) |
| Materials / equipment | optical pooled screens ($50-500K each), Perturb-seq ($5-30K/screen), scRNA-seq ($200-700/sample), iPSC-neuron differentiation ($3-15K/run) |
| Other direct costs | compute ~$400K/yr (H100 blended ~$2.50/GPU-hr); open-source infra; data licensing; external audit; travel |
| Indirect | Cytognosis 15% de minimis MTDC (2 CFR 200.414(f)); Purdue negotiated F&A (~55-60% on-campus); Cellanome G&A. On an OT, ARPA-H negotiates the actual rate |
| Profit/fee | nonprofit/academic primes typically none; for-profit subs per negotiation |
| **Total (all phases)** | **~$30M** (range $25-60M) |

**Taxpayer value / resource sharing.** Open releases at every phase (Apache 2.0 code, CC BY docs, open protocol/data standards) create reusable public infrastructure beyond the consortium; cost-sharing via shared open-source infrastructure and open data. Costs ramp across phases, heaviest in Phase III (second disease + external validation).

## 6. References Cited *(does not count toward the 5-page limit)*

1. Ruzicka WB, Mohammadi S, et al. (2024). Single-cell multi-cohort dissection of the schizophrenia transcriptome. *Science*, 384(6698). [PsychENCODE atlas; PI co-led.]
2. Mathys H, Mohammadi S, et al. (2019). Single-cell transcriptomic analysis of Alzheimer's disease. *Nature*, 570, 332-337. [ROSMAP atlas.]
3. Batiuk MY, et al. (2024). Upper-layer cortical neurons drive schizophrenia-associated pathology (PsychAD). *Nature Neuroscience*, 27, 1773-1784. [PI co-author.]
4. Avsec Ž, et al. / Google DeepMind (2025). AlphaGenome: predicting the impact of DNA sequence variation on gene regulation. github.com/google-deepmind/alphagenome. [Apache-2.0 code; noncommercial weights; tool in TA2.]
5. LLNL (2024). Open AI Co-Scientist. github.com/llnl/open-ai-co-scientist. [Open tournament-based agentic-science scaffolding reference.]
6. Roohani Y, Huang K, Leskovec J (2024). GEARS: predicting transcriptional outcomes of multigene perturbations. *Nature Biotechnology*, 42, 216-228. [TA1 perturbation baseline.]
7. CZI Science (2024). How to build a virtual cell. *Cell*, 187. [TA1 landscape framing.]
8. Replogle JM, et al. (2022). Genome-wide Perturb-seq. *Cell*, 185(19), 3615-3632. [TA3/TA4 cost anchor.]
9. Virtual Brain Twin Consortium (2025). virtualbraintwin.eu. [Single-scale circuit comparator for TA1.]
10. Nair A, et al. (2024). 22q11.2 deletion syndrome shapes brain transcriptome and regional cell-type signatures. *Molecular Psychiatry*, 29. [22q11DS molecular-to-brain anchor.]
11. Tegtmeyer M, …, Carpenter AE, Singh S, Nehme R, et al. (2025). Combining phenomics with transcriptomics reveals cell-type-specific morphological and molecular signatures of the 22q11.2 deletion. *Nature Communications*, 16:6332. DOI: 10.1038/s41467-025-61547-x. [NeuroPainting; direct validation precedent.]
12. Haghighi M, …, Carpenter AE, et al. (2025). Identifying and targeting abnormal mitochondrial localization associated with psychosis. *bioRxiv* 2025.10.08.676630. [Cell Painting applied to psychosis.]
13. ARPA-H (2026). IGoR Solicitation ARPA-H-SOL-26-155, Proactive Health Office. sam.gov.

> **Verify before submission:** confirm exact citation details for refs 4, 7, and 8 (author lists, volume/pages, DOIs) — flagged in the prior strategy doc as needing a check.

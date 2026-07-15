# ARPA-H IGoR Solution Summary

*Superseded for submission by IGoR_Solution_Summary_SUBMISSION_2026-06-19.md (this is the long internal working draft).*

**Innovative Solutions Opening:** ARPA-H-SOL-26-155 (Intelligent Generator of Research, IGoR), Proactive Health Office.
**Title:** PsychIGoR: Intelligence Generation of Disease Mechanisms for Psychiatric Disorders. A self-updating, mechanistic causal model of psychiatric disease with a validated closed-loop experiment engine.
**Team:** PsychIGoR. **Solution Summary due:** 2026-06-25, 12:00 PM ET. **Full proposal due:** 2026-08-06, 12:00 PM ET.

> Revision 2026-06-19. Expanded working draft (the 5-page limit applies to Sections 1 to 4 in the submitted version; this draft runs longer to carry the full substance for internal review). Title and team configuration updated to PsychIGoR; team confirmed (Grama, Carpenter, Tegtmeyer at Purdue/IPAI; Ruzicka; SIFT with Bryce and Goldman; Purcell as Project Manager (hired via Cytognosis); systems architect to be hired via Cytognosis (Elham Jebalbarezi interim); Cellanome as the industry execution arm (cost estimate to be verified with Cellanome)). Contributions are described by work focus rather than TA labels.

## Cover and company profile

| Field | Entry |
|---|---|
| Team name | PsychIGoR |
| Prime organization | Institute for Physical AI (IPAI), Purdue University |
| Organization type | Academia |
| SAM.gov UEI | Not required at Solution Summary stage (prime UEI: Purdue University [to confirm]) |
| Principal Investigator | Ananth Grama (IPAI, Purdue) |
| Computational disease modeling and hypothesis generation (sub-awardee co-lead) | Cytognosis Foundation (Shahin Mohammadi) with IPAI, Purdue |
| Prime Technical POC | Ananth Grama, IPAI, Purdue (ayg@purdue.edu) |
| Subawardee Technical POC | Shahin Mohammadi, Cytognosis Foundation, mohammadi@cytognosis.org |
| Prime Administrative POC | Tabitha M. Cinowski, Operations Manager, IPAI, Purdue (cinowski@purdue.edu) |
| Estimated project duration | 60 months (Phase I 18, Phase II 18, Phase III 24) |
| Animal subjects | No |
| Human subjects | No (secondary analysis of existing, de-identified cohort data and established or engineered iPSC lines; final determination confirmed with counsel and the IRB of record) |
| Total funds requested from ARPA-H (all phases) | $50,000,000 |
| Resource sharing | ~$4.0M Performer in-kind (data access, sequencing credits, instrument access, cloud credits); total project value ~$54.0M |
| Place(s) of performance | Purdue University (IN); Cytognosis Foundation (CA); McLean Hospital (MA); additional validated laboratories (in discussion) |

**Sub-awardees and team members.**

| Organization | Technical POC | Org type | Focus |
|---|---|---|---|
| Cytognosis Foundation | Shahin Mohammadi | Non-profit | Computational disease modeling (lead); hypothesis and experiment-intent generation (lead); semantic foundation (co-lead) |
| McLean Hospital / Harvard Medical School | W. Brad Ruzicka | Academia | Clinical and translational disease modeling; data governance |
| SIFT | Daniel Bryce (lead), Robert Goldman (advisory) | For-profit | Interoperable perturbation protocols (lead); semantic foundation (co-lead) |
| Cellanome | [POC to confirm] | For-profit | Experimental execution and marketplace (industry arm); live-cell imaging and same-cell Perturb-seq |
| Illumina (optional) | James Han, Michael Mehan | For-profit | Sequencing and cloud platform; Billion Cell Atlas resource sharing |

**Matthew Tegtmeyer's lab (academic execution arm)** and **Cellanome (industry execution arm)** are the two validated execution laboratories, meeting the program's requirement of two or more. Tegtmeyer's wet-lab at Purdue/IPAI runs the iPSC-neuron disease models with multi-modal fixed-cell high-plex readouts (RNA, protein, morphology, and in-situ CRISPR-guide sequencing); Cellanome provides the complementary live-cell imaging and same-cell Perturb-seq arm (R3200). **Anne Carpenter (IPAI/Purdue)** provides the computational morphology and imaging-model layer (no wet bench), consuming outputs from both arms.

## 1. Concept Summary

IGoR calls for a closed loop that turns hypotheses into validated knowledge **at least 10x faster**: mechanistic disease models, an AI engine that designs experiments, interoperable protocols, and a marketplace of validated laboratories. We propose that loop for **psychiatric disease, beginning with schizophrenia in Phases I and II and extending to bipolar disorder in Phase III**, a domain where mechanism is poorly understood and where a model that learns causally from every experiment would change how the field works.

Our distinctive idea is to treat **disease-associated genetic variation as the perturbation** that drives cellular biology, and to build a **mechanistic, multiscale, self-updating causal model** of how that perturbation moves cells from health toward disease. A **New Science Engine** interrogates that model itself, not just the literature, to find the most informative knowledge gap and design the next experiment. **Interoperable perturbation protocols** carry that experiment to **validated laboratories** that return model-ready data, which updates the model and closes the loop.

Because schizophrenia is largely polygenic and hard to model in a dish, we begin from its **penetrant, near-Mendelian forms** (the 22q11.2 deletion and large-effect rare-variant genes), engineered as **isogenic iPSC pairs**, exactly as familial Alzheimer and Parkinson variants made those diseases tractable in cells. One architectural decision threads through the whole loop: a **single semantic foundation** (one shared vocabulary and identifier system, authored once and used across every focus area) so that an experiment transfers between the model, the protocol, and the laboratory without translation at the seams. The proposal addresses all of the program's interest areas, with our deepest contribution in disease-mechanism modeling.

## 2. Innovation and Impact

**Why genetics, and why it is not enough.** Drug targets with human genetic support reach approval roughly **twice** as often as targets without it (Nelson et al. 2015), a multiplier that rises to about **2.6x** with a decade of added evidence and climbs further as confidence in the causal gene increases (Minikel et al. 2024). Yet most psychiatric signal is noncoding with ambiguous variant-to-gene mapping, and even an unambiguous gene rarely hands over a mechanism. The standard repair, statistical-genetics and machine-learning target discovery validated after the fact in cellular models, confirms that a variant does something but seldom explains how it drives disease, whether that axis is the disease-relevant one, or what else in the pathway is easier to drug.

**What current approaches miss.** Foundation cell models (scGPT, Geneformer, STATE) are correlational and static; perturbation predictors are narrow and single-scale; agentic-science systems (Co-Scientist, Biomni, the Virtual Lab) wrap a language model around a literature search. None integrate atlas-scale data, causal-network inference, and circuit-scale physiology into a model that **updates from new experiments**, and none distinguish a therapeutic effect from a side effect.

**Our innovations.**

1. **Dual grounding in two complementary experiments.** We model cellular and clinical evidence in one shared pathway space. Engineered cellular perturbations give a **known causal intervention** that acts directly on genes but lives in an artificial system; natural population genetics give **real, population-scale causal evidence** through inheritance but cannot be experimentally tested and miss the exposome. Each covers the other's blind spot, so the model surfaces disease axes that are mechanistic, population-relevant, and robust to culture artifacts. Genomic factorization (pathway-PRS lineage; method proprietary) aggregates weak, convergent variants into these interpretable axes.
2. **Disease as the causal perturbation operator.** We invert the virtual-cell paradigm (Bunne et al. 2024) so that disease-associated genetic variation acts as a soft intervention on a latent causal model of cellular processes, for which identifiability guarantees exist (Zhang et al. 2023).
3. **A three-latent structural causal model** that separates a cell's **basal state**, the **disease effect** (causal on the cell state), and a **treatment effect** that acts either **directly** on the cell (a side-effect route) or by **modulating the disease** (the therapeutic route). This makes "does an intervention correct the disease or merely move the cell" an identifiable question, and it makes efficacy versus side-effect liability a prediction the model can be tested on.
4. **A self-updating, multiscale, mechanistic disease model**, grounded in human genetics and clinical cohorts and paired with isogenic cellular models, rather than a static foundation model.
5. **Interoperability as an Internet-style protocol stack for laboratories.** Interoperable perturbation protocols layer intent, process, calibration, and hardware so an experiment moves between laboratories as easily as a data file, governed by a Request-for-Comments process and tested in bake-offs. This is not invented from scratch; it extends **LabOP** (Bartley et al. 2023), the open lab-protocol standard our SIFT partner co-authored, plus the **SiLA 2** device-driver standard, and adds the one missing piece, evidence-based parameter governance.

| Capability | Foundation cell models | Perturbation predictors | Agentic-science systems | IGoR (this proposal) |
|---|---|---|---|---|
| Mechanistic and causal | No | Partial | No | **Yes** |
| Multiscale (molecule to circuit) | No | No | No | **Yes** |
| Self-updating from new experiments | No | No | Partial | **Yes** |
| Disease genotype as the perturbation | No | No | No | **Yes** |
| Grounded in both cellular and clinical evidence | No | No | No | **Yes** |
| Separates therapy from side effect | No | No | No | **Yes** |
| Portable protocols across laboratories | No | No | No | **Yes** |
| Closed loop to validated laboratories | No | No | Partial | **Yes** |

**Quantitative metrics, against the state of the art.**

| Metric | SOTA baseline today | Phase I target | Phase II target | Phase III target |
|---|---|---|---|---|
| Experimental cycle time (hypothesis to model update) | weeks to months, manual | baseline established | >=4x faster | **>=10x faster** |
| Inter-laboratory concordance | not systematically measured; reproducibility often <50% | >=80% (two labs) | >=90% (cross-team) | >=90% (marketplace) |
| Disease-model variance explained in 22q11DS cell-type shifts | literature-only, low | >=30% | improved over literature-only | >=2x Phase I |
| Model update latency (data return to refreshed model) | n/a (models are static) | baseline | <=24 h | <=4 h |
| Experiment-design engine experiments rated high-value by expert panel | n/a | >=50% | >=75% | >=85% |
| Mechanistic sub-models across biological scales | single-scale | >=3 sub-models | >=10 across >=2 scales | >=15 across >=3 scales |
| Novel predictions experimentally confirmed | rare, post-hoc | design and baseline | >=1 confirmed | both disease areas |
| Disease areas covered | one at a time | 1 (schizophrenia) | 1 | 2nd (bipolar) added |

**Impact.** Targets that emerge from a model carrying human genetic support are roughly two to three times more likely to reach the clinic, and that multiplier rises with confidence in the causal gene, which is exactly what dual grounding delivers. Penetrant forms calibrate disease axes that **generalize to idiopathic schizophrenia** and span **bipolar disorder** as transdiagnostic coordinates, and the therapy-versus-side-effect distinction directly serves drug discovery. The marquee outcome is **at least 10x faster validated knowledge** by Phase III, with the model, the protocol stack, and the marketplace interfaces deposited openly so the same infrastructure accelerates discovery across many diseases.

## 3. Proposed Work

**Final deliverable.** A closed-loop IGoR system demonstrated on schizophrenia and extended to bipolar disorder: a self-updating causal disease-mechanism model, an experiment-design engine that designs its own experiments, and an interoperable perturbation-protocol stack with validated laboratories that execute them, reaching the 10x cycle-time target. **Phase I is anchored by a phenotypic-triage screen** that empirically selects the genetic forms and cellular phenotypes the model is built on. The task structure below mirrors the Task Description Document (Appendix C.2) and is cross-walked to the Cost Proposal (Appendix C.3).

### Disease-mechanism modeling (primary contribution; Cytognosis with IPAI)

Disease-mechanism modeling is built in four pillars: a cell-type-aware mechanistic network, a causal generative model, a joint cellular-clinical shift space, and ontology-conditioned experiment design. Four elements carry the depth of this proposal.

- **Paired clinical and cellular modeling.** Isogenic iPSC pairs and patient clinical cohorts are represented in **one pathway-space shift model**, so cellular and clinical evidence constrain the same disease axes and culture artifacts do not masquerade as disease signal.
- **Genomic factorization (the input building blocks).** We initialize from **pretrained genomic foundation models** (AlphaGenome, VariantFormer, Evo 2) to embed gene bodies and regulatory regions, contextualize them on a gene functional network through multiresolution graph diffusion, and factor the result into a small set of **sparse, interpretable, transdiagnostic disease-axis factors** that double as candidate biotypes. The detailed method is proprietary; novelty is claimed precisely against the PRSet pathway-PRS precedent.
- **Causal modeling with virtual-cell perturbation models.** A **three-latent structural causal model** separates the cell's basal state, the disease effect, and a treatment effect that acts either directly on the cell or by modulating the disease. This extends sparse-mechanism-shift and soft-intervention identifiability (SAMS-VAE; Zhang et al. 2023) to disease and treatment as separate, composable operators. The disease-axis factors condition a compositional, multimodal conditional-flow-matching generative model and enter the structural causal model as the disease-effect operator, so the model learns how the axes causally interact.
- **Phenotypic-triage screen (the Phase I anchor).** Across the penetrant-variant panel (the 22q11.2 deletion and TBX1, plus high-odds-ratio SCHEMA genes such as SETD1A, GRIN2A, GRIA3, and CUL1), engineered as **isogenic pairs** (a healthy line with each variant introduced by CRISPR), we measure **transcriptomic, morphological, and functional calcium-imaging** phenotypes, systematically extending the 22q11.2 phenomics precedent (Tegtmeyer et al. 2025) to select the lines and disease axes that anchor the model.

Disease-mechanism modeling is built only by Cytognosis, IPAI, and students, to keep the mission-critical core focused.

### Experiment-design engine and hypothesis generation (IPAI lead, with Cytognosis)

A non-LLM-wrapper engine that interrogates the disease model's own uncertain parameters and conflicting edges to choose the highest-value experiment, through a hypothesis tournament with adversarial critics grounded in mechanistic constraints, mechanistic-model-grounded retrieval-augmented planning whose corpus is the structured output of the disease model rather than literature alone, and test-time validation in which lightweight simulations pre-screen designs. The engine runs on open, swappable scaffolding so future models can be incorporated without re-engineering, and it explains its reasoning so the researcher directs the work; consequential actions require human authorization. Phylo (creator of Biomni) is an optional experiment-design engine collaborator; SIFT can additionally contribute a scoped value-of-information planning layer.

### Interoperable perturbation protocols (SIFT lead)

The interoperable perturbation protocols define a **layered protocol stack** so the same experiment runs at any qualified laboratory. It is borrowed, not invented: we adopt **LabOP** (the SD2-era open standard SIFT co-authored), add **SiLA 2** at the hardware layer, and contribute the missing governance layer.

| Layer | Plain meaning | We build it with |
|---|---|---|
| **Intent** | what the scientist wants (declarative) | LabOP protocol objects, written from the experiment-design engine's ExperimentIntent object |
| **Process** | the recipe with trusted parameters, no instrument detail | LabOP primitives plus LinkML-described metadata |
| **Calibration** | shared standards so two machines mean the same thing | our **RFC governance** plus IV&V reference artifacts (the novel contribution) |
| **Hardware** | machine-specific settings, hidden behind a common interface | LabOP specialization to SiLA 2, Opentrons, Autoprotocol, and Illumina |

Two design commitments make the stack distinctive. First, a **single semantic foundation across all four technical areas**: every schema is authored once in **LinkML**, every entity grounded in the **Biolink model and OBO ontologies**, and **Python (Pydantic) and RDF generated from that one source**, so a gene is the same identifier in the disease-model graph, the experiment-design engine's design, the perturbation protocol, and the laboratory data record, with no translation at the seams. Natural variants use GA4GH VRS and HGVS; engineered CRISPRi/a perturbations carry the same locus plus a Sequence-Ontology modality tag, which is what lets the model treat natural and induced variation in one coordinate system. Second, we **extend LabOP from synthetic biology to perturbation biology in three phases**, each with a quantitative quality-control gate so a downstream failure can be traced to its cause:

| Phase of an experiment | Makes | New LabOP primitives | QC gate to advance |
|---|---|---|---|
| Cellular model | the cells (iPSC neurons) | InduceDifferentiation, MatureCulture | maturity markers MAP2+/TUJ1+ >=0.85, NeuN >=0.80 |
| Perturbation | the change (CRISPRi/a or compound) | DeliverGuideRNA, TreatCompound | knockdown log2FC <=-1.5; activation >=3x; viability >=0.90 |
| Readout | the measurement | CalciumImagingAcquisition, ScRNAseqLibraryPrep, CellPaintingStain | genes/cell >=1000; doublets <=5%; stable calcium baseline |

The interfaces are concrete deliverables and open standards in their own right: the experiment-design engine hands the protocol layer an **ExperimentIntent** object (a small set of URI-bound fields plus a value-of-information score and human authorization), and each laboratory declares a **LabCapabilityProfile** so the protocol layer matches a protocol's needs to the laboratories that can run them. SIFT estimates two to three full-time engineers for interoperable perturbation protocols and participates in the program bake-offs and connect-a-thon. LLM-based extraction (Instructor with Pydantic, DSPy as backup) onboards laboratories and parses published protocols into the schema.

### Experimental execution and validated-lab marketplace (academic and industry arms)

The validated-lab marketplace executes interoperable perturbation protocols and returns model-ready data through two independent experimental arms. The **academic arm** is **Matthew Tegtmeyer's lab (Purdue/IPAI)**, which runs all wet-lab experiments: iPSC-derived NGN2 neuron disease models (22q11.2 and isogenic controls) with multi-modal fixed-cell high-plex readouts (RNA, protein, morphology, and in-situ CRISPR-guide sequencing), building directly on Tegtmeyer et al. 2025. The **industry arm** is **Cellanome**, contributing live-cell imaging, same-cell scRNA-seq, and pooled CRISPR on the R3200 (Perturb-LINK). The academic arm (fixed-cell, high-plex) and Cellanome (live-cell, temporal) are orthogonal, enabling a designed **cross-arm concordance milestone** aligned with the program's 85% concordance gates. **Anne Carpenter (IPAI/Purdue)** provides the common computational layer: interpretable morphology and cellular-imaging models (no bench) that consume readouts from both arms and serve as the disease-model and experiment-design engine analysis bridge. **Illumina** adds high-throughput sequencing and Billion Cell Atlas resource sharing.

### Milestones (phase-gated, quantitative)

| Metric | Phase I | Phase II | Phase III |
|---|---|---|---|
| Experimental cycle time | baseline established | >=4x | >=10x |
| Disease-model variance explained in 22q11DS cell-type shifts | >=30% | improved over literature-only | >=2x Phase I |
| Model update latency | baseline | <=24 h | <=4 h |
| Cross-laboratory concordance | >=80% (>=2 labs) | >=90% (cross-team) | >=90% (marketplace) |
| Experiment-design engine experiments rated high-value | >=50% | >=75% | >=85% |
| Novel predictions experimentally confirmed | design and baseline | >=1 | both disease areas |
| Disease areas | 1 (schizophrenia) | 1 | 2nd (bipolar) |

### Alternatives and risk

We considered a foundation-model-only disease model and rejected it as correlational and non-updating, and patient lines alone, rejected for lacking genetically matched controls, which is why we engineer isogenic pairs. The central risk, that polygenic disease resists in-dish modeling, is mitigated by **starting from penetrant forms** and by the phenotypic-triage screen that empirically selects strong-signal lines. Cross-laboratory concordance is mitigated by the calibration layer, reference materials, IV&V artifacts, and RFC governance. ARPA-H expects substantial technical risk; here it is counterbalanced by transformative upside, a causal, self-updating disease model that distinguishes therapy from side effect, built on infrastructure that compounds in value as data accrue.

## 4. Team Organization and Capabilities

We propose as **Team PsychIGoR**, one integrated performer under a single Principal Investigator. Confirmed members appear without a status note; roles still being finalized are marked.

| Focus area / role | Member and capability | Status |
|---|---|---|
| Principal Investigator and prime | **Ananth Grama, IPAI, Purdue.** Computational science at scale, systems integration, and program management; computational disease modeling and the experiment-design engine | Confirmed |
| Computational disease modeling; hypothesis and experiment-intent generation; semantic foundation (co-lead) | **Shahin Mohammadi, Cytognosis Foundation, with IPAI, Purdue.** Single-cell atlases, causal and perturbation modeling, psychiatric genetics; co-author, schizophrenia single-cell atlas | Confirmed |
| Experimental disease modeling (academic execution arm) | **Matthew Tegtmeyer lab, Purdue.** iPSC-derived NGN2 neuron disease models, 22q11.2 phenomics and transcriptomics; with multi-modal fixed-cell high-plex readouts (RNA, protein, morphology, and in-situ CRISPR-guide sequencing) | Confirmed |
| Computational disease modeling (morphology and imaging models) | **Anne Carpenter, IPAI/Purdue.** Inventor of Cell Painting and CellProfiler; interpretable models for morphology and cellular-imaging data; common analysis layer across the execution arms (no wet bench) | Confirmed |
| Clinical and translational disease modeling | **W. Brad Ruzicka, McLean Hospital and HMS.** Psychiatric single-cell genomics, cohort interpretation, and data governance | Confirmed |
| Interoperable perturbation protocols; semantic foundation (co-lead) | **SIFT; Daniel Bryce (lead), Robert Goldman (advisory).** LabOP co-authors; protocol semantics, automated planning, and standards delivery | Confirmed |
| Software and Systems Architect | **Cytognosis hire (recruiting).** Interoperability and open-source systems architecture; interim coverage via IPAI (Elham Jebalbarezi Sarbijan) | Recruiting |
| Project Manager | **Patricia Purcell (hired via Cytognosis).** Multi-team program and delivery management | Confirmed |
| Experimental execution and marketplace (industry arm) | Cellanome (live-cell imaging, same-cell scRNA-seq and Perturb-seq) | Confirmed (cost and partnership documents pending) |
| Sequencing and cloud platform (optional) | Illumina (James Han, Michael Mehan) | Optional |

Every confirmed member sits directly on the critical path: genome-scale single-cell and psychiatric-genetics modeling (Cytognosis and IPAI), iPSC-neuron disease-model execution and multi-modal readouts (Tegtmeyer, academic execution arm), computational morphology and imaging models (Carpenter, no wet bench), interoperable perturbation-protocol design (SIFT), and clinical and cohort expertise (McLean). Tegtmeyer and Carpenter cover complementary, non-overlapping ground: wet-lab experiments versus computational morphology and imaging-model analysis. The Project Manager (Purcell) and the Software and Systems Architect (Jebalbarezi) are distinct roles from the PI, as the ISO requires, and the computational disease-modeling core is staffed in-house to protect the mission-critical work.

## 5. Basis of Estimate (not counted in the page limit)

Total request: **$50.0M over 60 months**, with ~$4.0M Performer in-kind resource sharing for a total project value of ~$54.0M. Phase allocation: **$13.5M, $15.0M, $21.5M** for Phases I, II, and III. The team fields approximately **26 funded full-time-equivalents per year**, ramping from about 24.7 in Phase I to about 27.9 in Phase III as the second disease area and scaled experimentation come online.

**Consolidated basis of estimate by category.**

| Category | Amount | Basis of estimate |
|---|---|---|
| Direct labor (fully burdened, ~147,000 hours) | $22.0M | ~26 funded FTE/yr blended across performers at 2026 loaded rates; faculty at 2 to 3 person-months/yr, with postdocs, students, staff scientists, and engineers at full time |
| Subcontracts and consultants | $0.7M | Clinical co-lead (Ruzicka) effort, biostatistics, ethics and IRB, standards consultants |
| Materials and supplies | $6.0M | iPSC lines and NGN2 differentiation, CRISPRi/a libraries and lentivirus, Perturb-seq kits, Cell Painting reagents, sequencing consumables |
| Equipment | $2.8M | Phase I imaging stand-up at Purdue for the Tegtmeyer wet-lab and Carpenter computational-imaging work (high-content imager, confocal and calcium-imaging rig, liquid handlers), plus compute hardware; items over $10K carry vendor quotes |
| Travel | $1.0M | DDD workshop (kickoff), protocol bake-offs, Phase III connect-a-thon, biannual IV&V reviews, dissemination; each trip tied to a milestone |
| Other direct costs | $7.0M | GPU and cloud compute (disease-model training and experiment-design engine inference), sequencing as a service, storage, software and API licenses, graduate tuition, part-time project management |
| Indirect (F&A / overhead) | $9.0M | Cytognosis 15% de minimis MTDC (2 CFR 200.414(f)); Purdue ~57% on-campus F&A; commercial subs' overhead embedded in loaded rates |
| Profit and fee | $1.5M | Commercial subs (SIFT, Cellanome, Illumina, Phylo) ~7 to 10% on cost base; none for non-profit or academia |
| **Total, all phases** | **$50.0M** | |
| Resource sharing (in-kind, Performer) | ~$4.0M | Illumina Billion Cell Atlas data and sequencing credits, Cellanome instrument access, cloud research credits, open JUMP Cell Painting reference data |

**Per-performer allocation (ARPA-H request).**

| Performer | Role / focus | 5-yr total | Phase I | Phase II | Phase III |
|---|---|---|---|---|---|
| IPAI / Purdue (Prime) | Coordination, PI, software architecture, disease-model and experiment-design engine support, **in-house academic execution arm**: Tegtmeyer (academic experimental arm, iPSC-neuron + fixed-cell high-plex readouts), Carpenter (computational morphology/imaging models) | $15.5M | $4.5M | $4.4M | $6.6M |
| Cytognosis (sub) | Disease-model and experiment-design engine co-leads; computational and AI core | $14.0M | $4.0M | $4.2M | $5.8M |
| SIFT (sub) | Interoperable perturbation protocols lead (LabOP protocol stack; approx. 1 Staff-plus/Principal FTE, 70% Bryce/30% Goldman) | $5.0M | $1.5M | $1.5M | $2.0M |
| Cellanome (sub) | Industry execution arm, live-cell and Perturb-seq (confirmed; cost and partnership docs pending) | $8.0M | $2.0M | $2.4M | $3.6M |
| Illumina (sub) | Sequencing and cloud platform, optional (James Han, Michael Mehan) | $4.0M | $0.9M | $1.2M | $1.9M |
| McLean / HMS (sub) | Clinical and cohort interpretation | $0.7M | $0.2M | $0.2M | $0.3M |
| Phylo (sub, optional) | Experiment-design engine agentic-science collaborator | $4.0M | $1.1M | $1.2M | $1.7M |
| Cross-team, integration, reserve | DDD workshop, bake-offs, connect-a-thon, management reserve | $2.8M | $0.8M | $0.9M | $1.1M |
| **Total** | | **$50.0M** | **$13.5M** | **$15.0M** | **$21.5M** |

**Salary cap.** All ARPA-H-funded direct salary is capped at the Federal Executive Schedule Level II rate, **$228,000** for 2026 obligations (effective 2026-01-11). The cap applies only to the federally funded portion of direct salary, not to total institutional compensation, so senior faculty whose institutional base exceeds the cap (Grama, Carpenter, Ruzicka) are funded at the capped rate prorated to their small effort fractions (0.2 to 0.25 FTE), with no distortion to the budget. All Cytognosis hires, the Software and Systems Architect, SIFT staff, and external-laboratory personnel are below the cap.

**Equipment and space.** Because Tegtmeyer is establishing his wet-lab at Purdue and Carpenter is setting up her computational-imaging infrastructure at IPAI/Purdue, the budget includes a Phase I equipment stand-up (~$0.95 to 1.35M: high-content imager, spinning-disk confocal with a calcium-imaging rig, liquid handlers, and core cell-culture instruments for Tegtmeyer's bench). No direct space-rental line is required for any performer; laboratory and office space is covered by institutional F&A (Purdue, McLean) or by commercial overhead (SIFT, Cellanome, Illumina). Any Purdue laboratory build-out is treated as institutional cost-share, not a direct cost.

**Value to the U.S. taxpayer.** The deliverables are open: a self-updating causal disease model, an experiment-design engine, open protocol standards (LabOP extensions, the ExperimentIntent and LabCapabilityProfile schemas), and a validated-laboratory loop, all deposited in a public repository under permissive licenses. Because the targets the engine surfaces carry human-genetic support, they are roughly two to three times more likely to reach the clinic, and the same platform generalizes across psychiatric and, ultimately, other complex diseases, multiplying the return on a single investment.

## 6. References Cited (not counted in the page limit)

1. Bunne C, et al. How to build the virtual cell with artificial intelligence. *Cell* 2024;187(25):7045-7063. doi:10.1016/j.cell.2024.11.015.
2. Zhang J, et al. Identifiability guarantees for causal disentanglement from soft interventions. NeurIPS 2023. arXiv:2307.06250.
3. Bereket M, Karaletsos T. Modelling cellular perturbations with the sparse additive mechanism shift VAE (SAMS-VAE). NeurIPS 2023. arXiv:2311.02794.
4. de la Fuente J, et al. Interpretable causal representation learning in pathway space (SENA-discrepancy-VAE). ICLR 2025. arXiv:2506.12439.
5. Gonzalez G, et al. Combinatorial prediction of therapeutic perturbations (PDGrapher). *Nat Biomed Eng* 2025. doi:10.1038/s41551-025-01481-x.
6. Singh T, et al. Rare coding variants in ten genes confer substantial risk for schizophrenia (SCHEMA). *Nature* 2022;604:509-516. doi:10.1038/s41586-022-04556-w (PMID:35396579).
7. Trubetskoy V, et al. Mapping genomic loci implicates genes and synaptic biology in schizophrenia. *Nature* 2022;604:502-508. doi:10.1038/s41586-022-04434-5.
8. Schneider M, et al. Psychosis in 22q11.2 deletion syndrome: meta-analysis. *Br J Psychiatry* 2023 (PMID:36786112).
9. Murphy KC, et al. Schizophrenia in 22q11.2 deletion syndrome. *Arch Gen Psychiatry* 1999 (PMID:10199234).
10. Tegtmeyer M, et al. Combining phenomics with transcriptomics reveals cell-type-specific morphological and molecular signatures of the 22q11.2 deletion. *Nat Commun* 2025;16:6332. doi:10.1038/s41467-025-61547-x.
11. Ruzicka WB, Mohammadi S, et al. Single-cell multi-cohort dissection of the schizophrenia transcriptome. *Science* 2024;384:eadg5136. doi:10.1126/science.adg5136.
12. Emani PS, et al. Single-cell genomics and regulatory networks for 388 human brains (PsychENCODE). *Science* 2024;384:eadi5199. doi:10.1126/science.adi5199.
13. Minikel EV, et al. Refining the impact of genetic evidence on clinical success. *Nature* 2024;629:624-629. doi:10.1038/s41586-024-07316-0.
14. Paylor R, et al. Tbx1 haploinsufficiency and behavioral phenotypes. *PNAS* 2006 (PMID:16684884).
15. Nelson MR, et al. The support of human genetic evidence for approved drug indications. *Nat Genet* 2015;47(8):856-860. doi:10.1038/ng.3314.
16. Bartley B, et al. The Laboratory Open Protocol language (LabOP / PAML). *ACM JETC* 2023. doi:10.1145/3604568.
17. Juchli M. SiLA 2: standardized device interfaces for laboratory automation. 2022. doi:10.1007/10_2022_204.

Full reference list and verification status are maintained in the research master, section 99, and the fact-check file `research/FACT_CHECK_AND_CAPABILITIES_2026-06-16.md`.

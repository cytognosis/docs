# PsychIGoR Solution Summary

**Innovative Solutions Opening:** ARPA-H-SOL-26-155 (Intelligent Generator of Research, IGoR), Proactive Health Office.
**Solution Summary title:** PsychIGoR: Intelligence Generation of Disease Mechanisms for Psychiatric Disorders. A self-updating, mechanistic causal model of psychiatric disease with a validated closed-loop experiment engine.
**Solution Summary due:** 2026-06-25, 12:00 PM ET. **Full proposal due:** 2026-08-06, 12:00 PM ET.

<!-- SUBMISSION VERSION 2026-06-19. Formatting target: 8.5x11, 1-inch margins, Inter (sans serif) 11pt body per Appendix B; Sections 1 to 4 fit within 5 pages; cover/profile, Section 5 (Basis of Estimate), and Section 6 (References) are excluded from the page limit. Brand: Cytognosis design system applied with restraint (Inter, brand heading colors, no em dashes) on a Purdue/IPAI-prime document. -->

## Cover and Company Profile (not counted in the page limit)

| Field | Entry |
|---|---|
| Team name | PsychIGoR |
| Prime organization | Institute for Physical AI (IPAI), Purdue University |
| Organization type | Academia |
| SAM.gov UEI | Not required at Solution Summary stage (prime UEI: Purdue University, to confirm) |
| Principal Investigator | Ananth Grama (IPAI, Purdue) |
| Prime Technical POC | Ananth Grama, IPAI, Purdue (ayg@purdue.edu) |
| Subawardee Technical POC | Shahin Mohammadi, Cytognosis Foundation (mohammadi@cytognosis.org) |
| Prime Administrative POC | Tabitha M. Cinowski, Operations Manager, IPAI, Purdue (cinowski@purdue.edu) |
| Estimated project duration | 60 months (Phase I 18, Phase II 18, Phase III 24) |
| Animal subjects | No |
| Human subjects | No (secondary analysis of existing de-identified cohort data and established or engineered iPSC lines; final determination confirmed with counsel and the IRB of record) |
| Total funds requested from ARPA-H (all phases) | ~$42,900,000 (~$43M; bottom-up planning estimate, Appendix C.4 workbook controlling) |
| Resource sharing | ~$2.3M Performer in-kind (IPAI/Purdue HPC compute, Purdue wet-lab facilities, Cellanome instrument and run credits); total project value ~$45.2M |
| Place(s) of performance | Purdue University (IN); Cytognosis Foundation (CA); McLean Hospital (MA); additional validated laboratories |

**Sub-awardees and team members.**

| Organization | Technical POC | Org type | Focus |
|---|---|---|---|
| Cytognosis Foundation | Shahin Mohammadi | Non-profit | Disease-model and TA1-TA2 hypothesis lead; experiment-design engine (TA2) co-lead; semantic foundation co-lead |
| McLean Hospital / Harvard Medical School | W. Brad Ruzicka | Academia | Clinical and translational disease modeling; data governance |
| SIFT | Daniel Bryce (lead), Robert Goldman (advisory) | For-profit | Interoperable perturbation protocols (lead); scoped value-of-information planning layer; semantic foundation (co-lead) |
| Cellanome | POC to confirm | For-profit | Industry execution arm; live-cell imaging and same-cell Perturb-seq (R3200) |
| Illumina (optional) | James Han, Michael Mehan | For-profit | Sequencing and cloud platform; Billion Cell Atlas resource sharing |

## 1. Concept Summary

IGoR calls for a closed loop that turns hypotheses into validated knowledge at least 10x faster: mechanistic disease models, an AI engine that designs experiments, interoperable protocols, and a marketplace of validated laboratories. We propose that loop for psychiatric disease, beginning with schizophrenia in Phases I and II and extending to bipolar disorder in Phase III, a domain where mechanism is poorly understood and where a model that learns causally from every experiment would change how the field works. The proposal addresses all of the program's interest areas, with our deepest contribution in disease-mechanism modeling.

Our distinctive idea is to treat disease-associated genetic variation as the perturbation that drives cellular biology, and to build a mechanistic, multiscale, self-updating causal model of how that perturbation moves cells from health toward disease. A New Science Engine interrogates that model itself, not just the literature, to find the most informative knowledge gap and design the next experiment. Interoperable perturbation protocols carry that experiment to validated laboratories that return model-ready data, which updates the model and closes the loop. Because schizophrenia is largely polygenic and hard to model in a dish, we begin from its penetrant, near-Mendelian forms (the 22q11.2 deletion and large-effect rare-variant genes), engineered as isogenic iPSC pairs, exactly as familial Alzheimer and Parkinson variants made those diseases tractable in cells. One architectural decision threads through the whole loop: a single semantic foundation, one shared vocabulary and identifier system authored once and used across every focus area, so an experiment transfers between the model, the protocol, and the laboratory without translation at the seams.

## 2. Innovation and Impact

**Why genetics, and why it is not enough.** Drug targets with human genetic support reach approval roughly twice as often as targets without it (Nelson et al. 2015), a multiplier that rises to about 2.6x with a decade of added evidence and climbs further as confidence in the causal gene increases (Minikel et al. 2024). Yet most psychiatric signal is noncoding with ambiguous variant-to-gene mapping, and even an unambiguous gene rarely hands over a mechanism. Statistical-genetics and machine-learning target discovery, validated after the fact in cellular models, confirms that a variant does something but seldom explains how it drives disease, whether that axis is the disease-relevant one, or what else in the pathway is easier to drug.

**What current approaches miss.** Foundation cell models (Geneformer, scFoundation, and similar) are correlational and static (Theodoris et al. 2023; Hao et al. 2024); perturbation predictors are narrow and single-scale (Roohani et al. 2024); agentic-science systems wrap a language model around a literature search (Boiko et al. 2023; Swanson et al. 2025). None integrate atlas-scale data, causal-network inference, and circuit-scale physiology into a model that updates from new experiments, and none distinguish a therapeutic effect from a side effect.

**Our innovations.** First, dual grounding: engineered cellular perturbations give a known causal intervention on genes but in an artificial system, while natural population genetics give real, population-scale causal evidence that cannot be experimentally tested; each covers the other's blind spot, surfacing disease axes that are mechanistic, population-relevant, and robust to culture artifacts (genomic factorization, pathway-PRS lineage, aggregates weak convergent variants into interpretable axes; method proprietary, novelty claimed against the PRSet precedent, Choi et al. 2020). Second, disease as the causal perturbation operator: we invert the virtual-cell paradigm (Bunne et al. 2024) so disease-associated variation acts as a soft intervention on a latent causal model with identifiability guarantees (Schölkopf et al. 2021; Zhang et al. 2023). Third, a three-latent structural causal model separating basal state, disease effect, and a treatment effect that acts either directly (a side-effect route) or by modulating the disease (the therapeutic route), making efficacy versus side-effect liability a testable prediction. Fourth, a self-updating, multiscale, mechanistic model grounded in human genetics and clinical cohorts and paired with isogenic cellular models, not a static foundation model. Fifth, an Internet-style protocol stack for laboratories that extends LabOP (Bartley et al. 2023) and the SiLA 2 device-driver standard (Juchli 2022) and adds the missing piece, evidence-based parameter governance.

No prior foundation cell model, perturbation predictor, or agentic-science system combines these properties: IGoR is at once mechanistic and causal, multiscale from molecule to circuit, self-updating, genotype-driven, dually grounded in cellular and clinical evidence, able to separate therapy from side effect, and closed-loop to validated laboratories.

**Quantitative metrics, against the state of the art.**

| Metric | SOTA baseline today | Phase I target | Phase II target | Phase III target |
|---|---|---|---|---|
| Experimental cycle time (hypothesis to model update) | weeks to months, manual | baseline established | >=4x faster | **>=10x faster** |
| Inter-laboratory concordance | not systematically measured; reproducibility often <50% | >=80% (two labs) | >=90% (cross-team) | >=90% (marketplace) |
| Variance explained in 22q11DS cell-type shifts | literature-only, low | >=30% | improved | >=2x Phase I |
| Model update latency (data return to refreshed model) | n/a (models are static) | baseline | <=24 h | <=4 h |
| Engine experiments rated high-value by expert panel | n/a | >=50% | >=75% | >=85% |
| Novel predictions experimentally confirmed | rare, post-hoc | design and baseline | >=1 confirmed | both disease areas |
| Disease areas covered | one at a time | 1 (schizophrenia) | 1 | 2nd (bipolar) added |

**Impact.** Targets with human genetic support reach the clinic roughly two to three times more often, and the multiplier rises with confidence in the causal gene, which is what dual grounding delivers. Penetrant forms calibrate disease axes that generalize to idiopathic schizophrenia and span bipolar disorder, and the therapy-versus-side-effect distinction directly serves drug discovery. The marquee outcome is at least 10x faster validated knowledge by Phase III, with the model, protocol stack, and marketplace interfaces deposited openly so the same infrastructure accelerates discovery across many diseases.

## 3. Proposed Work

> **[ FIGURE 1 placeholder, reserve ~1/3 page. ]**
> *Figure 1. The PsychIGoR closed loop. A self-updating causal disease-mechanism model feeds a New Science Engine that designs the highest-value experiment; interoperable perturbation protocols carry it to validated academic and industry laboratories; model-ready data returns and updates the model. A single semantic foundation (LinkML and Biolink) spans every stage.* (Drop-in asset: the annotated closed-loop diagram in `figures/`.)

**Final deliverable.** A closed-loop IGoR system demonstrated on schizophrenia and extended to bipolar disorder: a self-updating causal disease-mechanism model, an experiment-design engine that designs its own experiments, and an interoperable perturbation-protocol stack with validated laboratories that execute them, reaching the 10x cycle-time target. Phase I is anchored by a phenotypic-triage screen that empirically selects the genetic forms and cellular phenotypes the model is built on. The task structure mirrors the Task Description Document (Appendix C.2) and is cross-walked to the Cost Proposal (Appendix C.3).

**Disease-mechanism modeling (primary contribution; co-led by Cytognosis and IPAI).** We represent isogenic iPSC pairs and patient clinical cohorts in one pathway-space shift model and align their disease axes in residual space by optimal transport, so cellular and clinical evidence constrain the same axes and culture artifacts do not masquerade as disease signal. We initialize from pretrained genomic foundation models to embed gene bodies and regulatory regions (the Enformer and AlphaGenome lineage; Avsec et al. 2021), contextualize them on a gene functional network, and factor the result into sparse, interpretable, transdiagnostic disease-axis factors that double as candidate biotypes (method proprietary; novelty claimed against the PRSet pathway-PRS precedent, Choi et al. 2020). A three-latent structural causal model separates basal state, disease effect, and treatment effect, extending soft-intervention identifiability (Zhang et al. 2023) to disease and treatment as separate, composable operators. The Phase I anchor is a phenotypic-triage screen across the penetrant-variant panel (the 22q11.2 deletion and TBX1, plus high-odds-ratio SCHEMA genes such as SETD1A, GRIN2A, and GRIA3; Singh et al. 2022), engineered as isogenic pairs and measured by transcriptomic, morphological, and functional calcium-imaging phenotypes, systematically extending the 22q11.2 phenomics precedent (Tegtmeyer et al. 2025). The experimental program runs in three stages mapped to the phases: Phase I creates and prioritizes the disease models (the penetrant panel plus SCHEMA and PsyGene/SSPsyGene-nominated genes, triaged to the five to ten genes with the most robust, reproducible phenotypic shifts, which set the Phase I milestones); Phase II runs disease-model-specific unbiased pooled Perturb-seq in those lines to learn treatment embeddings; and Phase III performs targeted, combinatorial perturbation of the pathways the model and engine nominate.

**Experiment-design engine and hypothesis generation (co-led by IPAI and Cytognosis).** A non-LLM-wrapper engine interrogates the disease model's own uncertain parameters and conflicting edges to choose the highest-value experiment, through a hypothesis tournament with adversarial critics grounded in mechanistic constraints, mechanism-grounded retrieval whose corpus is the structured output of the disease model rather than literature alone, and lightweight simulations that pre-screen designs. The engine runs on open, swappable scaffolding and explains its reasoning so the researcher directs the work; consequential actions require human authorization. Phylo (creator of Biomni) is an optional collaborator, and SIFT contributes a scoped value-of-information planning and scheduling layer under the Cytognosis and IPAI lead.

**Interoperable perturbation protocols (SIFT lead).** The protocols define a layered stack so the same experiment runs at any qualified laboratory: an intent layer (LabOP protocol objects written from the engine's ExperimentIntent), a process layer (LabOP primitives with LinkML-described metadata), a calibration layer (our RFC governance plus IV&V reference artifacts, the novel contribution), and a hardware layer (LabOP specialized to SiLA 2, Opentrons, Autoprotocol, and Illumina). Two commitments make the stack distinctive. A single semantic foundation runs across all focus areas: every schema is authored once in LinkML, every entity grounded in the Biolink model and OBO ontologies, with Python and RDF generated from one source, so a gene is the same identifier in the model, the design, the protocol, and the laboratory record. We extend LabOP from synthetic biology to perturbation biology in three phases (cellular model, perturbation, readout), each with a quantitative quality-control gate so a downstream failure can be traced to its cause. SIFT estimates two to three full-time engineers and participates in the program bake-offs and connect-a-thon.

**Experimental execution and validated-lab marketplace (academic and industry arms).** The marketplace executes interoperable protocols and returns model-ready data through two independent arms, meeting the program's two-or-more-laboratory requirement. The academic arm is Matthew Tegtmeyer's lab at Purdue, which runs the wet-lab experiments: iPSC-derived NGN2 neuron disease models with multi-modal readouts (RNA ~350-plex, protein ~50-plex, Cell-Painting-style morphology, and in-situ CRISPR-guide sequencing). As the developer of NeuroPainting (Tegtmeyer et al. 2025), Tegtmeyer also contributes to TA1 disease modeling at the cellular-phenotype-to-mechanism interface. The industry arm is Cellanome, contributing live-cell imaging, same-cell scRNA-seq, and pooled CRISPR on the R3200, with Phase I functional neuronal activity read out by single-cell calcium imaging. The two arms are orthogonal (fixed-cell high-plex versus live-cell temporal), enabling a designed cross-arm concordance milestone. Anne Carpenter (IPAI/Purdue), a TA1 co-lead, provides the common computational morphology and imaging-model layer that consumes readouts from both arms with no wet bench; she and Tegtmeyer co-authored NeuroPainting, built on the Broad Imaging Platform Cell Painting foundation (Tegtmeyer et al. 2025; Emani et al. 2024). Sequencing runs through a dedicated service line, with Illumina as an optional in-kind sequencing and cloud contributor.

**Alternatives and risk.** We rejected a foundation-model-only approach as correlational and non-updating, and patient lines alone for lacking matched controls, which is why we engineer isogenic pairs. The central risk, that polygenic disease resists in-dish modeling, is mitigated by starting from penetrant forms and the phenotypic-triage screen; cross-laboratory concordance is mitigated by the calibration layer, reference materials, IV&V artifacts, and RFC governance. ARPA-H expects substantial technical risk, counterbalanced here by transformative upside: a causal, self-updating disease model that distinguishes therapy from side effect, on infrastructure that compounds in value as data accrue. Phase-gated milestones are the metrics in Section 2.

## 4. Team Organization and Capabilities

We propose as Team PsychIGoR, one integrated performer under a single Principal Investigator. Uniquely, the team unites world-class expertise in both the clinical (Mohammadi, Ruzicka) and the cellular (Tegtmeyer, Carpenter) dimensions of psychiatric disease, capabilities usually pursued in separate organizations with different methods and literatures; here they sit on one team, and the cellular pair has already published together. Confirmed members appear without a status note; roles still being finalized are marked.

| Focus area / role | Member and capability | Status |
|---|---|---|
| Principal Investigator and prime | **Ananth Grama, IPAI, Purdue.** Computational science at scale, systems integration, and program management; disease modeling and the experiment-design engine | Confirmed |
| TA1 disease-model and TA1-TA2 hypothesis lead; experiment-design engine (TA2) co-lead; semantic foundation co-lead | **Shahin Mohammadi, Cytognosis Foundation, with IPAI.** Single-cell atlases, causal and perturbation modeling, psychiatric genetics; co-author, schizophrenia single-cell atlas | Confirmed |
| Academic execution arm (TA4) and TA1 disease-modeling contributor | **Matthew Tegtmeyer lab, Purdue.** Developer of NeuroPainting; iPSC-derived NGN2 neuron disease models, 22q11.2 phenomics and transcriptomics, multi-modal high-plex readouts | Confirmed |
| TA1 co-lead: computational morphology and imaging models | **Anne Carpenter, IPAI/Purdue.** Inventor of Cell Painting and CellProfiler; co-author of NeuroPainting with Tegtmeyer; interpretable morphology and cellular-imaging models as the common analysis layer across both execution arms (no wet bench) | Confirmed |
| Clinical and translational disease modeling | **W. Brad Ruzicka, McLean Hospital and HMS.** Psychiatric single-cell genomics, cohort interpretation, and data governance | Confirmed |
| Interoperable perturbation protocols; semantic foundation (co-lead) | **SIFT; Daniel Bryce (lead), Robert Goldman (advisory).** LabOP co-authors; protocol semantics, automated planning, and standards delivery | Confirmed |
| Software and Systems Architect | **Cytognosis hire (recruiting); IPAI interim (Elham Jebalbarezi Sarbijan).** Interoperability and open-source systems architecture | Recruiting |
| Project Manager | **Patricia Purcell (hired via Cytognosis).** Multi-team program and delivery management | Confirmed |
| Experimental execution (industry arm) | **Cellanome.** Live-cell imaging, same-cell scRNA-seq and Perturb-seq (R3200) | Confirmed (cost and partnership documents pending) |
| Sequencing and cloud platform | **Illumina** (James Han, Michael Mehan) | Optional |

Every confirmed member sits on the critical path, and Tegtmeyer and Carpenter cover complementary, non-overlapping ground (wet-lab execution versus computational morphology and imaging-model analysis). The Project Manager and the Software and Systems Architect are distinct roles from the PI, as the ISO requires, and the disease-modeling core is staffed in-house to protect the mission-critical work.

## 5. Basis of Estimate (not counted in the page limit)

Total request: **~$43M over 60 months** (bottom-up planning estimate; the Appendix C.4 workbook is controlling and finalizes F&A), with ~$2.3M Performer in-kind resource sharing for a total project value of ~$45.2M. Phase allocation: **~$11.5M, ~$13.1M, ~$18.4M** for Phases I, II, and III. The team fields roughly 25 funded full-time-equivalents per year, ramping into Phase III as the second disease area and scaled experimentation come online.

**Consolidated basis of estimate by category.**

| Category | Amount | Basis of estimate |
|---|---|---|
| Direct labor (fully burdened) | $18.8M | Blended across performers at 2026 loaded rates; faculty at 2 to 3 person-months/yr, with postdocs, students, staff scientists, and engineers at full time; rates set by experience level, consistent across organizations and locality-adjusted (Bay Area versus West Lafayette) |
| Materials and supplies | $2.4M | iPSC lines and NGN2 differentiation, CRISPRi/a libraries and lentivirus, Perturb-seq kits, Cell-Painting-style reagents, sequencing consumables |
| Equipment | $1.4M | Phase I imaging stand-up at the Tegtmeyer wet-lab (high-content imager, confocal with calcium-imaging rig, liquid handlers); items over $10K carry vendor quotes |
| Travel | $0.9M | DDD workshop, protocol bake-offs, Phase III connect-a-thon, biannual IV&V reviews; each trip tied to a milestone |
| Subcontracts and consultants | $2.2M | Sequencing service and CRO ($2.0M); legal and IP counsel, Duane Valz ($0.2M) |
| Other direct costs | $6.9M | Shared GPU and cloud compute for model training and engine inference ($2.5M); Cellanome live-cell runs and same-cell sequencing service ($4.4M); storage, software, and API licenses |
| Indirect (F&A / overhead) | $7.4M | Purdue ~57% on-campus F&A; Cytognosis 15% de minimis MTDC (2 CFR 200.414(f)); commercial subs' overhead embedded in loaded rates |
| Profit and fee | $1.2M | Commercial subs (SIFT, Cellanome) ~7 to 10% on cost base; none for non-profit or academia |
| Cross-team, integration, and reserve | $1.7M | Domain-Driven Design workshop, bake-offs, connect-a-thon, and a ~6% management reserve |
| **Total, all phases** | **~$42.9M** | |
| Resource sharing (in-kind, Performer) | ~$2.3M | IPAI/Purdue HPC compute (~$2.0M at NSF ACCESS rates), Purdue wet-lab facilities (~$0.15M), Cellanome instrument and run credits (~$0.16M); not requested from ARPA-H |

**Per-performer allocation (planning).** Figures are bottom-up planning estimates; the Appendix C.4 workbook is controlling and finalizes F&A. Purdue is the prime and the largest performer, as expected, with each major organization running roughly $1.2 to 2.5M per year.

| Performer | Role / focus | 5-yr total | Phase I | Phase II | Phase III |
|---|---|---|---|---|---|
| Purdue / IPAI, computational (Prime) | PI Grama; TA1 disease-model and TA2 experiment-design-engine co-lead; Carpenter computational morphology (TA1 co-lead; in-house, no Broad sub-award) | $6.5M | $1.8M | $2.0M | $2.7M |
| Purdue, Tegtmeyer lab (academic execution arm) | TA4 academic wet-lab: iPSC-neuron disease models with multi-modal readouts; also a TA1 disease-modeling contributor; Phase I equipment stand-up | $6.0M | $2.0M | $1.7M | $2.3M |
| Cytognosis (sub) | TA1 disease-model lead and TA1-TA2 hypothesis lead; TA2 co-lead; semantic foundation co-lead | $9.5M | $2.4M | $2.9M | $4.2M |
| SIFT (sub) | TA2-TA3, TA3 interoperable protocols (LabOP stack), and TA3-TA4 lead; scoped value-of-information layer | $7.0M | $2.0M | $2.2M | $2.8M |
| Cellanome (sub) | TA4 industry execution arm: live-cell imaging, same-cell scRNA-seq, Perturb-seq (R3200); RENT-and-run base, confirming via quote | $6.0M | $1.4M | $1.8M | $2.8M |
| Shared program compute | GPU and cloud for disease-model training and engine inference; program line, partially shiftable to IPAI HPC in-kind | $2.5M | $0.6M | $0.8M | $1.1M |
| TA4 sequencing (service / CRO) | scRNA-seq and Perturb-seq sequencing; Illumina optional in-kind | $2.0M | $0.4M | $0.6M | $1.0M |
| McLean / HMS (sub) | Clinical and cohort interpretation; data governance | $0.7M | $0.2M | $0.2M | $0.3M |
| Duane Valz, legal/IP (consultant) | OT agreement, IP and field-of-use strategy, subaward and teaming, OSS licensing | $0.2M | $0.08M | $0.06M | $0.06M |
| Cross-team, integration, reserve | DDD workshop, bake-offs, connect-a-thon, management reserve | $2.5M | $0.6M | $0.8M | $1.1M |
| **Total ARPA-H request** | | **~$42.9M** | **~$11.5M** | **~$13.1M** | **~$18.4M** |

Phylo, an optional TA2 collaborator, and Illumina are not budgeted as performers; Illumina participates as optional in-kind sequencing and cloud, and Phylo may be added on TA2 before the full proposal. Final per-performer F&A and the resource-sharing percentage are set with Purdue Sponsored Programs and the C.4 workbook.

**Salary cap.** All ARPA-H-funded direct salary is capped at the Federal Executive Schedule Level II rate, $228,000 for 2026 obligations (effective 2026-01-11; NIH NOT-OD-26-034). The cap applies only to the federally funded portion of direct salary, not to total institutional compensation, so senior faculty whose institutional base exceeds the cap (Grama, Carpenter, Ruzicka) are funded at the capped rate prorated to their small effort fractions (0.2 to 0.25 FTE), with no distortion to the budget. The CEO of Cytognosis, Shahin Mohammadi, is also funded at the cap: his compensation Rung 1 is pegged to the $228,000 HHS Executive Level II rate, so the ARPA-H charge is $228,000 × 0.5 FTE = ~$114,000/yr base before fringe. Rungs 2 and 3 of his compensation ladder (above the cap) are funded exclusively from unrestricted funds, never from this award. Other Cytognosis hires have institutional base salaries below the cap and are funded normally.

**Equipment and space.** The budget includes a Phase I equipment stand-up at Purdue for the Tegtmeyer wet-lab (~$0.95 to 1.35M: high-content imager, spinning-disk confocal with a calcium-imaging rig, liquid handlers, and core cell-culture instruments). Carpenter's footprint is computational (personnel and compute), not wet-lab capex. No direct space-rental line is required for any performer; laboratory and office space is covered by institutional F&A (Purdue, McLean) or by commercial overhead (SIFT, Cellanome, Illumina). Any Purdue laboratory build-out is treated as institutional cost-share, not a direct cost.

**Value to the U.S. taxpayer.** The deliverables are open: a self-updating causal disease model, an experiment-design engine, open protocol standards (LabOP extensions, the ExperimentIntent and LabCapabilityProfile schemas), and a validated-laboratory loop, all deposited in a public repository under permissive licenses. Because the targets the engine surfaces carry human-genetic support, they are roughly two to three times more likely to reach the clinic, and the same platform generalizes across psychiatric and, ultimately, other complex diseases, multiplying the return on a single investment.

## 6. References Cited (not counted in the page limit)

Format: first author, title, source, year, volume and pages where available, and a persistent identifier (DOI or PMID).

1. Nelson MR, Tipney H, Painter JL, et al. The support of human genetic evidence for approved drug indications. *Nat Genet* 2015;47(8):856-860. doi:10.1038/ng.3314.
2. Minikel EV, Painter JL, Dong CC, Nelson MR. Refining the impact of genetic evidence on clinical success. *Nature* 2024;629(8012):624-629. doi:10.1038/s41586-024-07316-0.
3. Bunne C, Roohani Y, Rosen Y, et al. How to build the virtual cell with artificial intelligence: priorities and opportunities. *Cell* 2024;187(25):7045-7063. doi:10.1016/j.cell.2024.11.015.
4. Schölkopf B, Locatello F, Bauer S, et al. Toward causal representation learning. *Proc IEEE* 2021;109(5):612-634. doi:10.1109/JPROC.2021.3058954.
5. Zhang J, Greenewald K, Squires C, et al. Identifiability guarantees for causal disentanglement from soft interventions. NeurIPS 2023. arXiv:2307.06250.
6. Bereket M, Karaletsos T. Modelling cellular perturbations with the sparse additive mechanism shift VAE (SAMS-VAE). NeurIPS 2023. arXiv:2311.02794.
7. Theodoris CV, Xiao L, Bhatt P, et al. Transfer learning enables predictions in network biology (Geneformer). *Nature* 2023;618(7965):616-624. doi:10.1038/s41586-023-06139-9.
8. Hao M, Gong J, Zeng X, et al. Large-scale foundation model on single-cell transcriptomics (scFoundation). *Nat Methods* 2024;21:1481-1491. doi:10.1038/s41592-024-02305-7.
9. Roohani Y, Huang K, Leskovec J. Predicting transcriptional outcomes of novel multigene perturbations with GEARS. *Nat Biotechnol* 2024;42:216-228. doi:10.1038/s41587-023-01905-6.
10. Boiko DA, MacKnight R, Kline B, Gomes G. Autonomous chemical research with large language models. *Nature* 2023;624(7992):570-578. doi:10.1038/s41586-023-06792-0.
11. Swanson K, Wu T, Bulaong NL, et al. The Virtual Lab: AI agents design new SARS-CoV-2 nanobodies with experimental validation. *Nat Biomed Eng* 2025. arXiv:2408.09618.
12. Avsec Z, Agarwal V, Visentin D, et al. Effective gene expression prediction from sequence by integrating long-range interactions (Enformer). *Nat Methods* 2021;18(10):1196-1203. doi:10.1038/s41592-021-01252-x.
13. Choi SW, Mak TSH, O'Reilly PF. Tutorial: a guide to performing polygenic risk score analyses (PRSet / PRSice-2). *Nat Protoc* 2020;15(9):2759-2772. doi:10.1038/s41596-020-0353-1.
14. Replogle JM, Saunders RA, Pogson AN, et al. Mapping information-rich genotype-phenotype landscapes with genome-scale Perturb-seq. *Cell* 2022;185(19):3615-3632. doi:10.1016/j.cell.2022.05.013.
15. Singh T, Poterba T, Curtis D, et al. Rare coding variants in ten genes confer substantial risk for schizophrenia (SCHEMA). *Nature* 2022;604(7906):509-516. doi:10.1038/s41586-022-04556-w (PMID:35396579).
16. Trubetskoy V, Pardinas AF, Qi T, et al. Mapping genomic loci implicates genes and synaptic biology in schizophrenia (PGC). *Nature* 2022;604(7906):502-508. doi:10.1038/s41586-022-04434-5.
17. Tegtmeyer M, Liyanage D, Han Y, et al. Combining phenomics with transcriptomics reveals cell-type-specific morphological and molecular signatures of the 22q11.2 deletion (NeuroPainting). *Nat Commun* 2025;16(1):6332. doi:10.1038/s41467-025-61547-x.
18. Ruzicka WB, Mohammadi S, Fullard JF, et al. Single-cell multi-cohort dissection of the schizophrenia transcriptome. *Science* 2024;384(6698):eadg5136. doi:10.1126/science.adg5136.
19. Emani PS, Liu JJ, Clarke D, et al. Single-cell genomics and regulatory networks for 388 human brains (PsychENCODE brainSCOPE). *Science* 2024;384(6698):eadi5199. doi:10.1126/science.adi5199.
20. Schneider M, Debbané M, Bassett AS, et al. Psychiatric disorders in 22q11.2 deletion syndrome (International Consortium). *Am J Psychiatry* / meta-analysis. PMID:36786112.
21. Murphy KC, Jones LA, Owen MJ. High rates of schizophrenia in adults with velo-cardio-facial syndrome. *Arch Gen Psychiatry* 1999;56(10):940-945. PMID:10199234.
22. Paylor R, Glaser B, Mupo A, et al. Tbx1 haploinsufficiency is linked to behavioral disorders in mice and humans. *PNAS* 2006;103(20):7729-7734. doi:10.1073/pnas.0600206103 (PMID:16684884).
23. Bartley B, Beal J, Karr JR, et al. The Laboratory Open Protocol language (LabOP / PAML). *ACM JETC* 2023. doi:10.1145/3604568.
24. Juchli M. SiLA 2: standardized device interfaces for laboratory automation. 2022. doi:10.1007/10_2022_204.

<!-- Citation verification: items 1-19, 23, 24 carry confirmed DOIs/PMIDs from research/sections/99_references.md. Items 20-22 carry PMIDs; confirm exact journal/year for item 20 (Schneider; BJPsych 2023 vs Am J Psychiatry per fact-check flag 7) before the Aug 6 full proposal. Full master list: research/sections/99_references.md; verification log: research/FACT_CHECK_AND_CAPABILITIES_2026-06-16.md. -->

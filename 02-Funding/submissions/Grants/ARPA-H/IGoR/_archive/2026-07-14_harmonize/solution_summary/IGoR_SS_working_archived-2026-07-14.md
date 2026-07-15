# PsychIGoR Solution Summary

**Innovative Solutions Opening:** ARPA-H-SOL-26-155 (Intelligent Generator of Research, IGoR), Proactive Health Office.
**Solution Summary title:** PsychIGoR: Intelligence Generation of Disease Mechanisms for Psychiatric Disorders. A self-updating, mechanistic causal model of psychiatric disease with a validated closed-loop experiment engine.
**Solution Summary due:** 2026-06-25, 12:00 PM ET. **Full proposal due:** 2026-08-06, 12:00 PM ET.



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
| Total funds requested from ARPA-H (all phases) | $50,000,000 |
| Resource sharing | ~$4.0M Performer in-kind (data access, sequencing credits, instrument access, cloud credits); total project value ~$54.0M |
| Place(s) of performance | Purdue University (IN); Cytognosis Foundation (CA); McLean Hospital (MA); additional validated laboratories |

**Sub-awardees and team members.**

| Organization | Technical POC | Org type | Focus |
|---|---|---|---|
| Cytognosis Foundation | Shahin Mohammadi | Non-profit | Computational disease modeling (lead); hypothesis and experiment-intent generation (lead); semantic foundation (co-lead) |
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

**Our innovations.** First, dual grounding in two complementary experiments: engineered cellular perturbations give a known causal intervention that acts directly on genes but lives in an artificial system, while natural population genetics give real, population-scale causal evidence through inheritance but cannot be experimentally tested; each covers the other's blind spot, so the model surfaces disease axes that are mechanistic, population-relevant, and robust to culture artifacts. Genomic factorization (pathway-PRS lineage, novelty claimed precisely against the PRSet precedent of Choi et al. 2020; method proprietary) aggregates weak, convergent variants into interpretable axes. Second, disease as the causal perturbation operator: we invert the virtual-cell paradigm (Bunne et al. 2024) so that disease-associated variation acts as a soft intervention on a latent causal model, for which identifiability guarantees exist (Schölkopf et al. 2021; Zhang et al. 2023). Third, a three-latent structural causal model that separates a cell's basal state, the disease effect, and a treatment effect acting either directly on the cell (a side-effect route) or by modulating the disease (the therapeutic route), which makes efficacy versus side-effect liability a prediction the model can be tested on. Fourth, a self-updating, multiscale, mechanistic disease model grounded in human genetics and clinical cohorts and paired with isogenic cellular models, rather than a static foundation model. Fifth, interoperability as an Internet-style protocol stack for laboratories that extends LabOP (Bartley et al. 2023), the open standard our SIFT partner co-authored, plus the SiLA 2 device-driver standard (Juchli 2022), and adds the one missing piece, evidence-based parameter governance.

| Capability | Foundation cell models | Perturbation predictors | Agentic-science systems | IGoR (this proposal) |
|---|---|---|---|---|
| Mechanistic and causal | No | Partial | No | **Yes** |
| Multiscale (molecule to circuit) | No | No | No | **Yes** |
| Self-updating from new experiments | No | No | Partial | **Yes** |
| Disease genotype as the perturbation | No | No | No | **Yes** |
| Grounded in both cellular and clinical evidence | No | No | No | **Yes** |
| Separates therapy from side effect | No | No | No | **Yes** |
| Portable protocols across laboratories | No | No | No | **Yes** |

**Quantitative metrics, against the state of the art.**

| Metric | SOTA baseline today | Phase I target | Phase II target | Phase III target |
|---|---|---|---|---|
| Experimental cycle time (hypothesis to model update) | weeks to months, manual | baseline established | >=4x faster | **>=10x faster** |
| Inter-laboratory concordance | not systematically measured; reproducibility often <50% | >=80% (two labs) | >=90% (cross-team) | >=90% (marketplace) |
| Variance explained in 22q11DS cell-type shifts | literature-only, low | >=30% | improved | >=2x Phase I |
| Model update latency (data return to refreshed model) | n/a (models are static) | baseline | <=24 h | <=4 h |
| Engine experiments rated high-value by expert panel | n/a | >=50% | >=75% | >=85% |
| Mechanistic sub-models across biological scales | single-scale | >=3 sub-models | >=10 across >=2 scales | >=15 across >=3 scales |
| Novel predictions experimentally confirmed | rare, post-hoc | design and baseline | >=1 confirmed | both disease areas |
| Disease areas covered | one at a time | 1 (schizophrenia) | 1 | 2nd (bipolar) added |

**Impact.** Targets that emerge from a model carrying human genetic support are roughly two to three times more likely to reach the clinic, and that multiplier rises with confidence in the causal gene, which is exactly what dual grounding delivers. Penetrant forms calibrate disease axes that generalize to idiopathic schizophrenia and span bipolar disorder as transdiagnostic coordinates, and the therapy-versus-side-effect distinction directly serves drug discovery. The marquee outcome is at least 10x faster validated knowledge by Phase III, with the model, the protocol stack, and the marketplace interfaces deposited openly so the same infrastructure accelerates discovery across many diseases.

## 3. Proposed Work

![Figure 1: The PsychIGoR closed loop.](IGoR_TA_loop_diagram.png){width=4.0in}

*Figure 1. The PsychIGoR closed loop. A self-updating causal disease-mechanism model feeds a New Science Engine that designs the highest-value experiment; interoperable perturbation protocols carry it to validated academic and industry laboratories; model-ready data returns and updates the model. A single semantic foundation (LinkML and Biolink) spans every stage.*

**Final deliverable.** A closed-loop IGoR system demonstrated on schizophrenia and extended to bipolar disorder: a self-updating causal disease-mechanism model, an experiment-design engine that designs its own experiments, and an interoperable perturbation-protocol stack with validated laboratories that execute them, reaching the 10x cycle-time target. Phase I is anchored by a phenotypic-triage screen that empirically selects the genetic forms and cellular phenotypes the model is built on. The task structure mirrors the Task Description Document (Appendix C.2) and is cross-walked to the Cost Proposal (Appendix C.3).

**Disease-mechanism modeling (primary contribution; Cytognosis with IPAI).** We represent isogenic iPSC pairs and patient clinical cohorts in one pathway-space shift model, so cellular and clinical evidence constrain the same disease axes and culture artifacts do not masquerade as disease signal. We initialize from pretrained genomic foundation models to embed gene bodies and regulatory regions (the Enformer and AlphaGenome lineage; Avsec et al. 2021), contextualize them on a gene functional network, and factor the result into sparse, interpretable, transdiagnostic disease-axis factors that double as candidate biotypes (method proprietary; novelty claimed against the PRSet pathway-PRS precedent, Choi et al. 2020). A three-latent structural causal model separates basal state, disease effect, and treatment effect, extending soft-intervention identifiability (Zhang et al. 2023) to disease and treatment as separate, composable operators. The Phase I anchor is a phenotypic-triage screen across the penetrant-variant panel (the 22q11.2 deletion and TBX1, plus high-odds-ratio SCHEMA genes such as SETD1A, GRIN2A, and GRIA3; Singh et al. 2022), engineered as isogenic pairs and measured by transcriptomic, morphological, and functional calcium-imaging phenotypes, systematically extending the 22q11.2 phenomics precedent (Tegtmeyer et al. 2025).

**Experiment-design engine and hypothesis generation (IPAI lead, with Cytognosis).** A non-LLM-wrapper engine interrogates the disease model's own uncertain parameters and conflicting edges to choose the highest-value experiment, through a hypothesis tournament with adversarial critics grounded in mechanistic constraints, mechanism-grounded retrieval whose corpus is the structured output of the disease model rather than literature alone, and lightweight simulations that pre-screen designs. The engine runs on open, swappable scaffolding and explains its reasoning so the researcher directs the work; consequential actions require human authorization. Phylo (creator of Biomni) is an optional collaborator, and SIFT contributes a scoped value-of-information planning and scheduling layer under the Cytognosis and IPAI lead.

**Interoperable perturbation protocols (SIFT lead).** The protocols define a layered stack so the same experiment runs at any qualified laboratory: an intent layer (LabOP protocol objects written from the engine's ExperimentIntent), a process layer (LabOP primitives with LinkML-described metadata), a calibration layer (our RFC governance plus IV&V reference artifacts, the novel contribution), and a hardware layer (LabOP specialized to SiLA 2, Opentrons, Autoprotocol, and Illumina). Two commitments make the stack distinctive. A single semantic foundation runs across all focus areas: every schema is authored once in LinkML, every entity grounded in the Biolink model and OBO ontologies, with Python and RDF generated from one source, so a gene is the same identifier in the model, the design, the protocol, and the laboratory record. We extend LabOP from synthetic biology to perturbation biology in three phases (cellular model, perturbation, readout), each with a quantitative quality-control gate so a downstream failure can be traced to its cause. SIFT estimates two to three full-time engineers and participates in the program bake-offs and connect-a-thon.

**Experimental execution and validated-lab marketplace (academic and industry arms).** The marketplace executes interoperable protocols and returns model-ready data through two independent arms, meeting the program's two-or-more-laboratory requirement. The academic arm is Matthew Tegtmeyer's lab (Purdue/IPAI), which runs all wet-lab experiments: iPSC-derived NGN2 neuron disease models with multi-modal fixed-cell high-plex readouts (RNA ~350-plex, protein ~50-plex, Cell-Painting-style morphology, and in-situ CRISPR-guide sequencing), building on Tegtmeyer et al. 2025. The industry arm is Cellanome, contributing live-cell imaging, same-cell scRNA-seq, and pooled CRISPR on the R3200. The two arms are orthogonal (fixed-cell high-plex versus live-cell temporal), enabling a designed cross-arm concordance milestone. Anne Carpenter (IPAI/Purdue) provides the common computational layer, interpretable morphology and cellular-imaging models that consume readouts from both arms with no wet bench (Tegtmeyer et al. 2025; Emani et al. 2024). Illumina adds high-throughput sequencing and Billion Cell Atlas resource sharing.

**Alternatives and risk.** We considered a foundation-model-only disease model and rejected it as correlational and non-updating, and patient lines alone, rejected for lacking genetically matched controls, which is why we engineer isogenic pairs. The central risk, that polygenic disease resists in-dish modeling, is mitigated by starting from penetrant forms and by the phenotypic-triage screen that empirically selects strong-signal lines. Cross-laboratory concordance is mitigated by the calibration layer, reference materials, IV&V artifacts, and RFC governance. ARPA-H expects substantial technical risk; here it is counterbalanced by transformative upside, a causal, self-updating disease model that distinguishes therapy from side effect, built on infrastructure that compounds in value as data accrue. Phase-gated quantitative milestones are the metrics in Section 2.

## 4. Team Organization and Capabilities

We propose as Team PsychIGoR, one integrated performer under a single Principal Investigator. Confirmed members appear without a status note; roles still being finalized are marked.

| Focus area / role | Member and capability | Status |
|---|---|---|
| Principal Investigator and prime | **Ananth Grama, IPAI, Purdue.** Computational science at scale, systems integration, and program management; disease modeling and the experiment-design engine | Confirmed |
| Computational disease modeling; hypothesis and experiment-intent generation; semantic foundation (co-lead) | **Shahin Mohammadi, Cytognosis Foundation, with IPAI.** Single-cell atlases, causal and perturbation modeling, psychiatric genetics; co-author, schizophrenia single-cell atlas | Confirmed |
| Experimental disease modeling (academic execution arm) | **Matthew Tegtmeyer lab, Purdue.** iPSC-derived NGN2 neuron disease models, 22q11.2 phenomics and transcriptomics, fixed-cell high-plex multi-modal readouts | Confirmed |
| Computational morphology and imaging models | **Anne Carpenter, IPAI/Purdue.** Inventor of Cell Painting and CellProfiler; interpretable morphology and cellular-imaging models; common analysis layer across the execution arms (no wet bench) | Confirmed |
| Clinical and translational disease modeling | **W. Brad Ruzicka, McLean Hospital and HMS.** Psychiatric single-cell genomics, cohort interpretation, and data governance | Confirmed |
| Interoperable perturbation protocols; semantic foundation (co-lead) | **SIFT; Daniel Bryce (lead), Robert Goldman (advisory).** LabOP co-authors; protocol semantics, automated planning, and standards delivery | Confirmed |
| Software and Systems Architect | **Cytognosis hire (recruiting); IPAI interim (Elham Jebalbarezi Sarbijan).** Interoperability and open-source systems architecture | Recruiting |
| Project Manager | **Patricia Purcell (hired via Cytognosis).** Multi-team program and delivery management | Confirmed |
| Experimental execution (industry arm) | **Cellanome.** Live-cell imaging, same-cell scRNA-seq and Perturb-seq (R3200) | Confirmed (cost and partnership documents pending) |
| Sequencing and cloud platform | **Illumina** (James Han, Michael Mehan) | Optional |

Every confirmed member sits on the critical path: genome-scale single-cell and psychiatric-genetics modeling (Cytognosis and IPAI), iPSC-neuron disease-model execution and multi-modal readouts (Tegtmeyer), computational morphology and imaging models (Carpenter, no wet bench), interoperable perturbation-protocol design (SIFT), and clinical and cohort expertise (McLean). Tegtmeyer and Carpenter cover complementary, non-overlapping ground. The Project Manager (Purcell) and the Software and Systems Architect are distinct roles from the PI, as the ISO requires, and the computational disease-modeling core is staffed in-house to protect the mission-critical work.


\newpage

## 5. Basis of Estimate (not counted in the page limit)

Total request: **$50.0M over 60 months**, with ~$4.0M Performer in-kind resource sharing for a total project value of ~$54.0M. Phase allocation: **$13.5M, $15.0M, $21.5M** for Phases I, II, and III. The team fields approximately 26 funded full-time-equivalents per year, ramping from about 24.5 in Phase I to about 27.8 in Phase III as the second disease area and scaled experimentation come online.

**Consolidated basis of estimate by category.**

| Category | Amount | Basis of estimate |
|---|---|---|
| Direct labor (fully burdened, ~147,000 hours) | $22.0M | ~26 funded FTE/yr blended across performers at 2026 loaded rates; faculty at 2 to 3 person-months/yr, with postdocs, students, staff scientists, and engineers at full time |
| Subcontracts and consultants | $0.7M | Clinical co-lead (Ruzicka) effort, biostatistics, ethics and IRB, standards consultants |
| Materials and supplies | $6.0M | iPSC lines and NGN2 differentiation, CRISPRi/a libraries and lentivirus, Perturb-seq kits, Cell Painting reagents, sequencing consumables |
| Equipment | $2.8M | Phase I imaging stand-up at Purdue for the Tegtmeyer wet-lab (high-content imager, confocal and calcium-imaging rig, liquid handlers), plus compute hardware; items over $10K carry vendor quotes |
| Travel | $1.0M | DDD workshop, protocol bake-offs, Phase III connect-a-thon, biannual IV&V reviews, dissemination; each trip tied to a milestone |
| Other direct costs | $7.0M | GPU and cloud compute (disease-model training and engine inference), sequencing as a service, storage, software and API licenses, graduate tuition, part-time project management |
| Indirect (F&A / overhead) | $9.0M | Cytognosis 15% de minimis MTDC (2 CFR 200.414(f)); Purdue ~57% on-campus F&A; commercial subs' overhead embedded in loaded rates |
| Profit and fee | $1.5M | Commercial subs (SIFT, Cellanome, Illumina, Phylo) ~7 to 10% on cost base; none for non-profit or academia |
| **Total, all phases** | **$50.0M** | |
| Resource sharing (in-kind, Performer) | ~$4.0M | Illumina Billion Cell Atlas data and sequencing credits, Cellanome instrument access, cloud research credits, open JUMP Cell Painting reference data |

**Per-performer allocation.** Rows show total project value including in-kind and sum to ~$54.0M; the ARPA-H request is $50.0M ($13.5M / $15.0M / $21.5M by phase), with the ~$4.0M difference being Performer in-kind embedded in the rows. Per-performer ARPA-H-only splits are itemized in the Appendix C.4 workbook (controlling).

| Performer | Role / focus | 5-yr total | Phase I | Phase II | Phase III |
|---|---|---|---|---|---|
| IPAI / Purdue (Prime) | Coordination, PI, software architecture, modeling and engine support, in-house academic execution arm: Tegtmeyer (iPSC-neuron with fixed-cell high-plex readouts), Carpenter (computational morphology and imaging models; Anne in-house, no separate Broad sub-award) | $15.5M | $4.5M | $4.4M | $6.6M |
| Cytognosis (sub) | Disease-model and engine co-leads; computational and AI core | $14.0M | $4.0M | $4.2M | $5.8M |
| SIFT (sub) | Interoperable perturbation protocols lead (LabOP stack); scoped value-of-information layer | $5.0M | $1.5M | $1.5M | $2.0M |
| Cellanome (sub) | Industry execution arm, live-cell and Perturb-seq (confirmed; cost and partnership docs pending; held pending June 23 response and capex-vs-opex decision) | $8.0M | $2.0M | $2.4M | $3.6M |
| Illumina (sub) | Sequencing and cloud platform (optional) | $4.0M | $0.9M | $1.2M | $1.9M |
| McLean / HMS (sub) | Clinical and cohort interpretation | $0.7M | $0.2M | $0.2M | $0.3M |
| Phylo (sub, optional) | Experiment-design engine agentic-science collaborator | $4.0M | $1.1M | $1.2M | $1.7M |
| Cross-team, integration, reserve | DDD workshop, bake-offs, connect-a-thon, management reserve | $2.8M | $0.8M | $0.9M | $1.1M |
| **Total project value (incl. ~$4.0M in-kind)** | | **$54.0M** | **$15.0M** | **$16.0M** | **$23.0M** |
| **ARPA-H request only** | | **$50.0M** | **$13.5M** | **$15.0M** | **$21.5M** |

**Salary cap.** All ARPA-H-funded direct salary is capped at the Federal Executive Schedule Level II rate, $228,000 for 2026 obligations (effective 2026-01-11; NIH NOT-OD-26-034). The cap applies only to the federally funded portion of direct salary, not to total institutional compensation, so senior faculty whose institutional base exceeds the cap (Grama, Carpenter, Ruzicka) are funded at the capped rate prorated to their small effort fractions (0.2 to 0.25 FTE), with no distortion to the budget.

**Equipment and space.** The budget includes a Phase I equipment stand-up at Purdue for the Tegtmeyer wet-lab (~$0.95 to 1.35M: high-content imager, spinning-disk confocal with a calcium-imaging rig, liquid handlers, and core cell-culture instruments). Carpenter's footprint is computational (personnel and compute), not wet-lab capex. No direct space-rental line is required for any performer; laboratory and office space is covered by institutional F&A (Purdue, McLean) or by commercial overhead (SIFT, Cellanome, Illumina). Any Purdue laboratory build-out is treated as institutional cost-share, not a direct cost.

**Value to the U.S. taxpayer.** The deliverables are open: a self-updating causal disease model, an experiment-design engine, open protocol standards (LabOP extensions, the ExperimentIntent and LabCapabilityProfile schemas), and a validated-laboratory loop, all deposited in a public repository under permissive licenses. Because the targets the engine surfaces carry human-genetic support, they are roughly two to three times more likely to reach the clinic, and the same platform generalizes across psychiatric and, ultimately, other complex diseases, multiplying the return on a single investment.


\newpage

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



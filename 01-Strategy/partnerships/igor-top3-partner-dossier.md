# ARPA-H IGoR — Top-3 TA3/TA4 Partner Dossier

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: leadership
> **Tags**: `strategy`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)

Prepared for Cytognosis Foundation (TA1/TA2 prime candidate). Sources: ARPA-H IGoR teaming page (retrieved 2026-06-03) + web research (2026-06-04). All three list themselves as **TA3 (Interoperable Experimental Procedures) + TA4 (Experiment Marketplace)** and seek a TA1/TA2 prime.

**Reading time: ~7 min. If you read one thing:** all three are complementary, not competing. Cellanome = functional single-cell + CRISPR phenotyping; Panome Bio = multi-omics CRO (metabolomics/proteomics); Transfyr = lab-execution capture / reproducibility, founded by the former ARPA-H director.

## Snapshot

| | Cellanome | Panome Bio | Transfyr |
|---|---|---|---|
| **HQ** | Foster City + San Diego, CA | St. Louis, MO | Cambridge, MA |
| **Founded** | 2020 | ~2020–21 | 2025 |
| **Stage / raised** | Series B, ~$216M | Series A, ~$12M | Seed, ~$25.6M (PitchBook, unconfirmed) |
| **Core modality** | Live-cell imaging + scRNA-seq + CRISPR-seq | Untargeted multi-omics (LC/MS) | Multimodal sensor capture of lab execution |
| **CRO/marketplace model** | Concierge CRISPR screens + instrument sale | Pure-play sample-in/report-out CRO | Deployable sensors + reproducibility data |
| **Gov credibility** | None confirmed | CLIA-certified; WashU/NIH consortium | Founders = ex-ARPA-H director + ex-Ginkgo; ex-DoD contact |
| **Shared contact** | Dwight Baker, VP Eng & Informatics | Adam Richardson, VP Operations | Casandra Philipson (title unconfirmed) |
| **Best-fit TA** | TA3 + TA4 | TA4 (strong) + TA3 | TA3 + TA4 |

---

## 1. Cellanome — https://www.cellanome.com

**Teaming-page entry (verbatim):**
- Contact: **Dwight Baker** · dwight.baker@cellanome.com · San Diego, CA · Own TA: **TA3 + TA4**
- Description: "Cellanome's R3200 is an integrated cell biology platform combining programmable CellCage enclosures, longitudinal live-cell fluorescence imaging, and scRNA-seq to characterize individual cells across time. CellCages capture and retain targeted cells for continuous phenotypic monitoring and downstream sequencing, enabling time-resolved phenotypic and transcriptomic characterization of single cells and cell-cell interactions at scale across any cell type with reproducible workflow protocols."
- Seeking: "...as a TA3 - TA4 performer... Seeking a prime performer with TA1 mechanistic disease modeling and TA2 agentic AI orchestration capabilities."

**What they do:** Life-science tools company built around dynamic, longitudinal single-cell biology — observing how individual cells behave and transition over days/weeks, then linking that to matched transcriptomic and CRISPR-guide data from the same cell. Positioned as "the data infrastructure biology has been missing" for AI-driven discovery.

**Core technology:**
- **R3200 platform** — integrated instrument: fluorescent live-cell imaging, AI real-time cell segmentation/targeting, a digital micromirror device that photopolymerizes CellCage enclosures around selected cells in seconds, plus sequencing integration.
- **CellCage enclosures (CCEs)** — micro-3D-printed, semipermeable microstructures formed around live cells; tunable size/permeability; tens of thousands form in <15 min; coordinate-linked so each image ties to its RNA-seq output; support extended culture, dosing, washout, sequential treatments.
- **Perturb-LINK** — pooled CRISPR screen reading guide identity + same-cell transcriptome + live-cell morphology/function + surface markers simultaneously. Directly measures functional phenotype (phagocytosis, secretion, T-cell priming, CAR-T potency) rather than proxies. Validated with the Spitzer Lab (UCSF) on DC/T-cell priming.

**Service model:** (A) concierge — Cellanome runs the screen end-to-end (Phase 1 workflow build → Phase 2 full screen with checkpoints); or (B) customer buys the R3200 and runs in-house with field-scientist support. Cell types: neurons, T cells, macrophages, dendritic cells, solid-tumor cells, fibroblasts, glia, iPSC-derived, CAR-T. Areas: oncology, immunology, neurobiology, aging/metabolic.

**Funding:** ~$216M total. Series B **$150M (Jan 2024)**, led by DFJ Growth (with Premji Invest, 8VC); earlier backing from Decheng Capital, DCVC.

**Leadership (heavy ex-Illumina bench):** CEO **Omead Ostadan** (ex-Illumina EVP); co-founder **Mostafa Ronaghi** (ex-Illumina CTO, pyrosequencing co-inventor); Chairman **Jay Flatley** (ex-Illumina CEO). Plus ex-Illumina/Element execs across CTO, CSO, scientific affairs.

**Shared contact — Dwight Baker:** **VP Engineering & Informatics, Advanced R&D.** Prior: VP Engineering at Resilience; engineering at Illumina; instructor at UC San Diego Extension. Hardware/data-pipeline interface specialist. LinkedIn: linkedin.com/in/dwightbaker

**Government track record:** None confirmed — all VC-funded. Academic partnerships only (UCSF Spitzer Lab; Perturb-LINK macrophage preprint, Orcutt-Jahns et al. 2026; showcased at AGBT 2026).

**IGoR fit:** Strong TA3/TA4. Generates coordinate-linked, AI-ready "unified data objects" (image + RNA-seq + CRISPR-seq); locked, documented SOP-based workflows; functional + transcriptomic phenotyping at scale incl. adherent cells (a gap for suspension-only competitors). This is your CRISPR KO/KD execution node from the prior analysis.

---

## 2. Panome Bio — https://panomebio.com

**Teaming-page entry (verbatim):**
- Contact: **Adam Richardson** · adam.richardson@panomebio.com · St Louis, MO · Own TA: **TA3 + TA4**
- Description: "Panome Bio is a WashU-affiliated CRO specializing in untargeted, single-sample multi-omics—metabolomics, lipidomics, and proteomics. Unlike global (large-library) approaches, untargeted profiling captures unknown, undiscovered molecules... We already apply ML to our data and engineer gold-standard protocols and reproducible, machine-readable data—produced across multiple sites and structured to be AI- and automation-ready..."
- Seeking: "...join a team as a subcontractor delivering TA3 and TA4... We are not the AI experts—we are the wet-lab partner that understands them... We seek a prime and collaborators strong in TA1 disease modeling and TA2 AI orchestration, plus data engineering and lab automation."

**What they do:** Discovery-services CRO spun out of **Dr. Gary Patti's lab at Washington University**, co-founded with BioGenerator Ventures (BioSTL). Sample-in / interpretable-report-out model. **CLIA-certified as of July 2025** (clinical-grade, government-contract-relevant credential). Address shared with BioGenerator Labs (4340 Duncan Ave, St. Louis).

**Core technology & services:**
- **Next-Generation Metabolomics (NGM)** — untargeted LC/MS not limited by a predefined library; **MassID** ML workflow scores identifications against a 280,000+ compound database for reproducible IDs.
- Full menu: untargeted metabolomics & lipidomics, metabolic flux (¹³C tracing), targeted metabolomics, **TissueBridge FFPE metabolomics**, microbiome function, discovery + targeted proteomics, **global phosphoproteomics** (launched Apr 2025), **transcriptomics/RNA-seq** (May 2025), **integrated multi-omics** pipeline (can ingest customer datasets), exposomics.
- Sample types: plasma, serum, urine, CSF, fresh-frozen and FFPE tissue, cell pellets, dried blood spots, animal-model samples. **~4-week turnaround**; report + raw data.

**Funding:** ~$12M reported. Series A **$6M (Mar 2023)**, led by Telegraph Hill Partners with BioGenerator Ventures.

**Leadership:** CEO/co-founder **Edward Weinstein, Ph.D.**; Chief Scientific Advisor **Gary Patti, Ph.D.** (WashU Powell Professor, NGM co-inventor); President/co-founder **Tom Cohen, Ph.D.**; co-founder **Dave Smoller, Ph.D.**

**Shared contact — Adam Richardson:** **VP of Operations** (prior: Study Director at Panome). Background in metabolomics/proteomics; earlier roles incl. lab director positions and cancer-metabolism research at Sanford Burnham Prebys (founded an NCI Shared Resource there). LinkedIn: linkedin.com/in/adrphd

**Government track record:** CLIA certification + WashU/NIH multi-omics production-center affiliation (institutional, via Patti lab); publishes an FCOI policy. No direct ARPA-H/DARPA contracts confirmed.

**IGoR fit:** Strong **TA4** (each assay is a defined, orderable marketplace unit with documented inputs/SOPs/standardized deliverables) and solid **TA3** (integrated pipeline harmonizes cross-site + customer data). CLIA + 4-week cadence de-risk government work. **Orthogonal to Cellanome** — provides the metabolic/proteomic layer Cellanome's transcriptomics platform does not.

---

## 3. Transfyr — https://transfyr.ai

**Teaming-page entry (verbatim):**
- Contact: **Casandra Philipson** · casandra@transfyr.ai · Cambridge, MA · Own TA: **TA3 + TA4**
- Description: "Transfyr is building the physical AI infrastructure for scientific observability to make science understandable, transferable, and reproducible (TA3, TA4). Most AI Scientists are trained on lossy published literature, we use a multimodal sensor stack to capture science in the lab as it happens. Layers of physical intelligence and computer vision power self-evolving models to provide ground truth..."
- Seeking: "...partners developing TA1 (Mechanistic Disease Models) and TA2 (New Science Engine)... support reproducibility testing across multiple sites for TA4 partners through our deployable sensors and agentic AI-powered tools... or directly serve as part of the TA4 experimental network through our testbed laboratory in Cambridge, MA."

**What they do:** Physical-AI infrastructure to capture the *tacit knowledge* of how experiments are actually executed — protocol drift, why runs fail — which they frame as the root of the reproducibility crisis. Deploy multimodal sensor stacks into active labs, then turn the recordings into durable, machine-readable operational knowledge ("the world's largest commercial dataset on real-world scientific execution").

**Core technology (built vs. aspirational):**
- *Built / deploying:* edge multimodal sensor stacks (vision, audio, sensor, metadata, outcomes) in a **Cambridge, MA testbed lab**; data-capture pipelines over high-volume streams incl. live video.
- *In development:* ML models reasoning over partial observability and protocol drift; credit-assignment (why an experiment succeeded/failed); cross-site generalization; a future robotic-automation layer. No publicly named product yet; **pre-product at scale, ~12 months old.**

**Funding:** ~$25.6M (PitchBook; no press release — treat as unconfirmed). Investors cited: The Engine, Underscore VC, Neo (General Catalyst / Breakout also appear, possibly as job-board hosts).

**Leadership — exceptionally well-connected to ARPA-H:**
- **Anna Marie Wagner** — Co-founder & CEO. Ex-Ginkgo SVP Corporate Development & Head of AI; ran Ginkgo's $1.6B 2021 go-public; ex-Bain Capital PE. Harvard (Applied Math/Econ) + HBS Baker Scholar.
- **Dr. Renee Wegrzyn** — Co-founder & Chief Innovation Officer. **First Director of ARPA-H (2022–2025)**, ran its ~$4B portfolio; 10+ yrs DARPA program manager; ex-Ginkgo Biosecurity VP; IARPA advisor. Ph.D. Georgia Tech.

**Shared contact — Casandra Philipson, Ph.D.:** **Title at Transfyr unconfirmed** (LinkedIn shows "Stealth Startup"); she is the active IGoR business-development contact. Career: Ph.D. Genetics/Bioinformatics & Computational Biology (Virginia Tech/NIMML) → Managing Director, Biotherapeutics Inc. → **Bioinformatician, DTRA/DoD (2016–2019)** → **Director of Bioinformatics, Concentric by Ginkgo** (biosecurity) → Transfyr. 77 publications (host-microbe, biosurveillance, phage annotation, SARS-CoV-2 phylogenetics). LinkedIn: linkedin.com/in/casandra-washington-philipson

**Government track record:** Strongest of the three by *relationships*: founder built ARPA-H; 10+ yrs DARPA; contact spent 3 yrs at DoD/DTRA. But **no awards to Transfyr itself confirmed** (and Wegrzyn's recency as ARPA-H director warrants a conflict-of-interest/recusal check before formal teaming).

**IGoR fit:** Thesis maps directly onto **TA3** (execution capture → interoperable, standardized procedures) and **TA4** (execution dataset + Cambridge testbed as a marketplace node, multi-site reproducibility testing). Caveats: youngest and least-proven; pre-product at scale; no public customers; funding unconfirmed.

---

## Recommendation

For a CRISPR-KO/KD-anchored IGoR proposal, **Cellanome is the priority outreach** (only verified CRISPR-screen executor; deep instrumentation; well-capitalized). **Panome Bio** is the complementary multi-omics readout layer (CLIA-certified, marketplace-ready). **Transfyr** is a strategic add for reproducibility/observability and unmatched ARPA-H relationships — verify the conflict-of-interest posture given Wegrzyn's recent ARPA-H directorship.

## Sources
ARPA-H IGoR teaming page (https://arpa-h.gov/explore-funding/programs/igor/teaming); company sites cellanome.com, panomebio.com, transfyr.ai; DFJ Growth, Crunchbase, GenomeWeb (Cellanome); BioGenerator Ventures, BioSTL, PRNewswire, WashU Source, The Org (Panome Bio); PitchBook, Hacker News, SynBioBeta, ResearchGate, AIChE, NIMML, LinkedIn (Transfyr). Full URL list available in the research logs.

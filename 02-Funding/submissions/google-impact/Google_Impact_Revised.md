# **Google.org Impact Challenge: AI for Science (Revised v4)**

## Cytognosis Foundation, Neuroverse track

## II. Impact

### Title

Neuroverse: Realizing Precision Psychiatry Through a Multimodal Map of Brain Circuit Variation

### Problem Statement

#### The Challenge (75 words)

Mental healthcare treats psychiatric conditions as discrete categorical diagnoses defined by symptom checklists, despite evidence from diverse cohorts showing psychiatric manifestations span a continuum of severity, are highly comorbid, and driven by shared molecular and circuit-level mechanisms crossing diagnostic boundaries. Individuals with identical diagnoses show substantial heterogeneity in phenotypes and treatment responses. Misdiagnosis and treatment failure remain common for those who need help most.

#### Significance (75 words)

First-line psychiatric treatments fail in 47 to 58 percent of patients; relapse climbs from 40 to 71 percent across trials. The cost is $528 billion annually on suboptimal therapy within a $5.3 trillion healthcare system. Data-driven biotypes predict treatment response (e.g., Drysdale depression subtypes), but each is single-disease, single-modality, and inconsistent across cohorts, blocking clinical adoption. Our unified multimodal map of brain-circuit variation bridges this gap, making transdiagnostic precision psychiatry actionable for patients.

#### Core Research Questions (75 words)

Four questions guide the work: (1) Can the model uncover shared and unique mechanisms within and across traditional diagnostic categories, resolving the heterogeneity within each? (2) Is the map sensitive enough to capture clinically relevant shifts in an individual's mental state, including treatment effects? (3) Can it predict individual mental-health trajectories? (4) Can it recommend personalized treatments that improve outcomes beyond group-matched standards? The answers let clinicians treat the person, not the label.

### Proposed Solution

#### Solution Overview (75 words)

Neuroverse replaces categorical psychiatric labels with continuous coordinates capturing individual variation across biological scales. We harmonize population-scale genomics, neuroimaging, and clinical data into a multimodal, multiscale map of the brain and behavior. We build on modality-specific foundation models, fine-tune them on disease-specific molecular and cellular atlases our team generated, and align them across modalities and scales to capture neurobehavioral phenotypes alongside the circuits (endophenotypes) and genotypic factors (endotypes) that drive psychiatric variation.

#### Tools, Methods, and Techniques (75 words)

We model brain connectivity as a sparse graph from spatio-temporal fMRI, using efficient multi-resolution graph neural networks with low-rank polynomial approximations to capture short- and long-range activity cascades whole-brain at 1M-node scale. Instead of predefined atlases, we inject an ensemble (PET neurotransmitter tracers, FOCUS subcortical) as node attributes regularizing embeddings, while the model attends to the most informative atlas per task. Pretraining: subgraph-masked self-supervision on HCP, UKBB, ABCD, ENIGMA, OpenNeuro.

#### Evidence of Feasibility (75 words)

Our team developed the first single-cell Alzheimer's atlas (Mathys, Davila-Velderrain, Mohammadi et al.; Nature, 2019) and the largest multi-cohort schizophrenia atlas (Ruzicka, Mohammadi et al.; Science, 2024), demonstrating continuous disease axes within categorical diagnoses at molecular level. Independent studies corroborate this dimensional structure: genomic modeling across 14 disorders explains 66 percent of psychiatric genetic variance; data-driven neuroimaging bifactor models outperform theory-driven approaches; validated neurotransmitter receptor atlases provide molecular priors extending these findings to whole-brain circuitry.

#### Force Multiplier Effect (75 words)

Open release of FAIR datasets and pretrained foundation models puts precision-psychiatry tooling within reach of rare-disease communities and data-scarce, under-resourced patient populations long left behind by big-cohort science. Transfer learning from well-powered substrates lets small consortia extend the map to their conditions in months, not decades. The patient-advocacy council (One Mind, Center for Digital Mental Health, APA Council on Digital Health, ASAM) translates discoveries and tools into clinical adoption channels, turning open science into patient impact.

### End Beneficiaries

#### Target Populations (75 words)

Fifty-three million U.S. adults live with mental illness, including 14.1 million with serious conditions, and often receive ineffective treatments due to categorical misdiagnosis. Rural counties average only 3.5 psychiatrists per 100,000 people, compared to 13.0 in urban areas, and 65 percent have no psychiatrist. Racial and ethnic minorities experience 30 to 50 percent higher misdiagnosis rates. Neuroverse could bring precision psychiatry to resource-limited settings globally, where neuroimaging infrastructure is growing but specialist access remains limited.

#### Beneficiary Engagement (75 words)

Our Patient Advocacy Council convenes representatives from One Mind (transdiagnostic), the Center for Digital Mental Health (Harvard / MGH, 125-plus scientist-clinician network), the APA Council on Digital Health, Innovation, and Technology, and ASAM (SUD-specific privacy and adoption). Members surface patient needs during development and serve as adoption hubs post-development, delivering models into the communities they represent. Clinician partners at McLean and Mount Sinai co-develop validation protocols. Findings reach participants in aggregated, deidentified form before release.

#### Project Reach (75 words)

The patient-advocacy council members are dissemination hubs: One Mind funnels findings to transdiagnostic patient communities; the Center for Digital Mental Health pushes tools through 125-plus scientist-clinician collaborators at Harvard/MGH; the APA Council on Digital Health drives clinical adoption through psychiatry's largest professional body; ASAM reaches the SUD population. Each connects core team output to thousands of patients and clinicians, exponentially multiplying the project's impact across geographies, conditions, and care settings within the 36-month window.

### Expected Outcomes

#### Success Metrics (75 words)

Scientific gates: learned axes explain over 50 percent of cross-disorder variance and correlate at r > 0.5 with HiTOP and the Grotzinger 2026 five-factor; cross-scale AUC ≥ 0.75 on PsychENCODE 388 paired held-out donors; harmonized release reaches 10,000-plus scans across 6-plus disorders. Impact gates: at least two patient-advocacy council partners run pilot evaluations by Month 24, returning diagnostic-accuracy, differential-treatment-response, and patient-reported-outcome data; ancestry-disaggregated demographic-performance cards ship with every release.

#### Failure Indicators (75 words)

Scientific failures: learned axes fail to replicate across sites; cross-disorder models perform no better than single-disorder baselines; cross-scale predictions underperform random baselines; NBB-internal replication of the PGC five-factor structure misses the pre-registered threshold. Impact failures: no council partner integrates the model into a pilot by Month 24; council pilots show no effect on diagnostic accuracy, treatment response, or patient-reported outcomes; demographic audits reveal unmitigated disparities; community adoption stalls below 100 downloads.

#### Expected Changes from Baseline (75 words)

For patients: from categorical labels to individual-grain coordinates matching each person to the right treatment, with measurable improvement in treatment-response rates beyond group-matched standards, validated through patient-advocacy council pilots. For clinicians: from months of per-lab preprocessing to minutes via pretrained harmonization; from imaging-only to imaging-plus-molecular cross-scale prediction. For the field: from single-disorder neuroimaging silos to a unified cross-disorder atlas (10,000-plus scans) benchmarked against HiTOP and Grotzinger 2026, with 30 to 50 percent better cross-site prediction.

## III. Innovative Use of Technology

### Technology Stack and Implementation (100 words)

PyTorch Geometric implements multi-resolution graph diffusion wavelets (Coifman, 2006) with cross-resolution attention; candidates include WaveGC, Hypergraph Wavelets (Sun 2024), InfoGain Wavelets (Johnson, 2025). fMRIPrep, QSIPrep, FreeSurfer standardize to BIDS / FAIR; neuromaps and the Allen Human Brain Atlas anchor learnable molecular priors. A geometric description-logic ontology-embedding stack (e.g., TransBox over EL++ ontologies) builds the continuous phenotypic coordinate backbone. Gemma 4, fine-tuned with LoRA and DPO and deployed via LiteRT, powers the on-device interviewer-supervisor multi-agent stack; Flutter ships it to phones. TPU v4 / v5 trains; Hugging Face plus AnnData / Zarr distribute. AlphaGenome-based molecular encoders (parallel-funded) plug into the same coordinate space.

### Custom Solution Development (100 words)

Existing tools fall short in four ways. Standard harmonization (ComBat, CovBat) discards biological variance; we replace it with a learned in-model layer. Single-resolution, single-disorder graph networks (BrainNetCNN, BrainGNN) miss multi-scale, cross-disorder structure; multi-resolution graph diffusion wavelets (Coifman 2006, with WaveGC and similar wavelet-GNN variants as candidates) address both. Symptom-checklist phenotyping discards dimensional structure; geometric EL++ ontology embeddings (e.g., TransBox) over a unified neuro-ontology stack build the continuous coordinate backbone. Cloud LLMs cannot meet sub-300ms speech-interjection latency without leaking voice; Gemma 4 plus LiteRT plus the supervisor-and-interviewer multi-agent architecture meets both. (AlphaGenome molecular-encoder extensions are parallel-funded.)

### Datasets (100 words)

Connectomic core (Google.org-funded), accessed under their respective Data Use Agreements: HCP (1,200 healthy adults, ConnectomeDB DUA); UK Biobank (50,000+ imaging subset, application plus access fees); ABCD (12,000 youth, NIMH Data Archive DUA, demographically diverse by design); ENIGMA federated working groups across SZ, BD, MDD, PTSD, OCD; disorder-specific BIDS-compliant studies on OpenNeuro. Cross-ancestry: NeuroGAP-Psychosis (Stanley Center DUA, Ethiopia, Kenya, South Africa, Uganda), H3Africa. Open atlases: neuromaps (19 PET receptor maps); Allen Human Brain Atlas. Phenotype: HiTOP, Grotzinger 2026 PGC five-factor across 14 disorders. PsychENCODE 388 paired WGS plus single-cell anchors the parallel-funded cross-scale track.

### Ethical Considerations (100 words)

Our design aligns with Google's AI Principles. Social benefit: open release reaches underserved communities. Avoiding unfair bias: training on demographically diverse cohorts (ABCD, NeuroGAP-Psychosis, H3Africa, ENIGMA) with disaggregated demographic audits. Safety: coordinates augment, never replace, clinician judgment; because individualized psychiatric predictions can produce catastrophic errors (LLM-therapy chatbots have already been linked to suicidal ideation), every clinical-facing output gates behind clinician review with explicit uncertainty disclosure and no autonomous diagnostic claims. Privacy: the on-device Gemma 4 + LiteRT + Flutter stack keeps voice and behavioral signals on the phone; membership-inference probes gate releases. Model and data cards ship with every release.

### Google.org Accelerator Participation (100 words)

We benefit most from Google's expertise in three areas. First, TPU optimization for large-scale graph neural networks plus LiteRT optimization for Gemma 4: scaling graph diffusion wavelets to 1M-node and on-device multi-agent inference both require Google-engineer-level acceleration to hit our latency and throughput targets. Second, large-scale data-pipeline engineering: harmonizing 10,000+ scans across formats, sites, and ontology vocabularies is where Google Cloud best practices reduce iteration cycles. Third, foundation-model architecture guidance: porting graph foundation models from language and vision to brain connectome topology, and aligning connectomic with phenotypic coordinate spaces, where DeepMind's AlphaFold and AlphaGenome work is directly relevant.

## IV. Feasibility

### Organizational Positioning (150 words)

Cytognosis Foundation uniquely combines personnel with a published track record building molecular atlases of brain disease, existing consortium access to the datasets this project requires, and an institutional commitment to open release that ensures results drive distributed innovation.

Our PI led the first multi-cohort single-cell schizophrenia atlas (Ruzicka, Mohammadi et al.; Science, 2024), identifying continuous disease axes within a single DSM diagnosis: Neuroverse's direct scientific foundation. He co-led the first single-cell Alzheimer's atlas (Mathys, Davila-Velderrain, Mohammadi et al.; Nature, 2019) and contributed to the PsychENCODE capstone integrating 388 brains (Emani et al.; Science, 2024). These are molecular-scale proof that the dimensional axes this project maps at connectomic and cross-scale resolution are real and discoverable.

Our Co-Lead at Human Technopole bridges molecular and circuit neuroscience. Our Senior Advisor at Purdue directs the Institute for Physical AI, providing foundation-model and scalable-computing expertise. The team spans computational neuroscience, AI systems, and open-source infrastructure.

### AI Maturity

AI First.

### Technical Feasibility (100 words)

Our Science 2024 publication demonstrated continuous disease axes are discoverable within single DSM diagnoses and replicate across independent cohorts; this is the dimensional-axis principle Neuroverse extends to whole-brain connectomes. The neuromaps atlas (Hansen et al.; Nature Methods, 2022) validates neurotransmitter receptor maps as reliable molecular priors. Grotzinger et al. (2025, Nature) independently confirmed a five-factor structure explaining 66 percent of psychiatric genetic variance; Quah et al. (2025) showed data-driven neuroimaging bifactor models outperform theory-driven frameworks. A tau-PET imputation result (Nature Communications, 2025) demonstrates cross-modal prediction tractability, supporting the parallel-funded cross-scale extension.

### Risk Management and Mitigation (200 words)

**Patients at under-resourced sites get predictions reflecting scanner brand more than biology.** fMRIPrep / QSIPrep plus an in-model learned harmonization layer preserves variance; held-out-site replication gates release; site-aware fallbacks model site explicitly.

**Patients are matched to coordinates no clinician can act on.** Axes must hit r > 0.5 against HiTOP and Grotzinger 2026 on at least 3 of 5 / 6 dimensions; single-benchmark hits release as provisional only.

**Patients receive catastrophically wrong personalized predictions.** LLM-therapy chatbots have been linked to suicidal ideation. Outputs gate behind clinician review with uncertainty disclosure; no autonomous diagnostic claims; red-team failure-mode model cards ship with every release; the Council vets patient-facing messaging before pilots.

**Patients from underrepresented ancestries get the worst predictions.** PGC / HiTOP lean European-ancestry; validation anchors on NeuroGAP-Psychosis (Ethiopia, Kenya, South Africa, Uganda), H3Africa, and ABCD's diverse-by-design sampling, with ancestry-disaggregated performance cards as a hard release gate.

**Patients lose cross-scale molecular precision.** Genome-to-Connectome integration is in the parallel-funded molecular track (PsychENCODE 388 paired donors); if it slips, Neuroverse v1.0 ships the connectomic-plus-phenotype core unchanged.

**Patients face delays from access or hiring.** Open datasets (HCP, ABCD, OpenNeuro) drive initial work; IRB initiates Month 1; deep ML background covers solo development with a 3-month hiring buffer.

### Key Team Members (100 words)

**PI: Shahin Mohammadi, PhD** (50%; externally funded via Astera Residency). 20 years in AI for biology (MIT, Broad, insitro, GenBio AI); led Nature 2019 and Science 2024 single-cell atlases; creator of ACTIONet.

**Co-Lead: Jose Davila-Velderrain, PhD** (advisory; Group Leader, Human Technopole). PsychAD atlas (Science, 2024); molecular-to-circuit bridge.

**Clinical Collaborator: Brad Ruzicka, MD/PhD** (McLean / HMS). HBTRC NeuroBioBank liaison; co-led the schizophrenia atlas (Science, 2024); anchors clinical validation and NBB cohort access.

**Senior Advisor: Ananth Grama, PhD** (8%; Director, Purdue Institute for Physical AI). Foundation-model architecture; scalable computing.

**AI / ML Engineer (hire, 100%):** geometric deep learning, graph diffusion wavelets, Gemma 4 LoRA + DPO.

### Partner Organizations

**Partner 1: Human Technopole.** Website: [https://humantechnopole.it](https://humantechnopole.it). Role (50 words): Co-Lead Jose Davila-Velderrain provides cross-scale neuroscience expertise bridging molecular and circuit-level analysis, contributing directly to model design and the cross-scale Genome-to-Connectome validation. Human Technopole offers access to European cohorts, high-performance computing, and the European computational neuroscience network, enabling validation across diverse international scanner configurations. Status: Existing partner.

**Partner 2: Purdue University, Institute for Physical AI.** Website: [https://www.purdue.edu/ipai/](https://www.purdue.edu/ipai/). Role (50 words): Senior Advisor Ananth Grama provides strategic guidance on foundation-model architecture, scalable computing optimization, and AI interpretability methods critical for biological applications. Purdue's IPAI offers high-performance computing infrastructure and a multidisciplinary network spanning AI, physics, and life sciences, strengthening the project's computational foundations and providing the redundant compute fabric our risk plan requires. Status: Existing partner.

**Partner 3: McLean Hospital / Harvard Medical School.** Website: [https://www.mcleanhospital.org](https://www.mcleanhospital.org). Role (50 words): McLean Hospital, Harvard Medical School's largest psychiatric affiliate, provides clinical neuroscience expertise for validating dimensional axes against patient outcomes. As the lead site of the Harvard Brain Tissue Resource Center (NeuroBioBank), McLean offers postmortem brain tissue and clinical data that enable molecular validation of connectomic findings and bridge imaging to cellular resolution. Status: Existing partner.

## V. Scalability

### Scalability Strategies Selected

Geographic transfer to new regions; sector adaptation to related fields; ecosystem integration with existing infrastructure; community-driven expansion; open-source adoption.

### Team Evolution for Scale (150 words)

Scale-up follows our three-horizon strategy. Horizon 1 (Years 1 to 5): the Cytognosis Foundation derisks the platform; this proposal lands the connectomic-plus-phenotype map as the proof-of-concept in mental health, with a dedicated open-models team in the Foundation continuously refreshing it every 6 to 12 months on clinical-grade public and open data. Horizon 2 (Years 5 to 10): IP licenses to an impact-aligned PBC execution arm that builds the Cytoscope (wearable sensors continuously locating individuals on the map) and the Cytonome (a personal health companion that not only tracks mental-health states but recommends noninvasive interventions to navigate and adjust trajectories). Horizon 3 (Years 10 to 15): the blueprint extends stepwise to immune, microbiome, and other systems, then their cross-system interactions. A post-Month-36 longitudinal pilot pairs wearable EEG plus fNIRS with WGS, physiology, and neuro-behavior in the same individuals over time, validating wearable-to-clinical mapping, sensitivity to interventions, and pre-symptomatic trajectory tracking years before symptoms surface.

### Financial Sustainability (50 words)

ARPA-H Mission Office ISO submission (PHO or HSF) targets $20-30M for clinical-scale validation. NSF Tech Labs five-year center grant, independently or as a Cytognosis-Convergent-Research joint center, sustains the open infrastructure. A future public benefit corporation subsidiary may commercialize diagnostic applications on top of the open core, without closing it.

### Technical Sustainability (50 words)

Google.org funding establishes research-grade baselines: harmonized datasets, pretrained connectomic foundation models, the phenotypic coordinate backbone, validated dimensional axes, and evaluation benchmarks. The parallel-funded molecular track plugs into the same coordinate space. Additional ARPA-H, NSF, and NIH support sustains active development; GitHub-hosted open source ensures evolution beyond any single funding cycle.

### Knowledge Sharing and Learning (100 words)

Knowledge sharing tracks the three Council stages. **Stage 1 (M1), requirements**: Council requirements brief co-authored with One Mind, Center for Digital Mental Health, APA Council on Digital Health, and ASAM, plus the open harmonized substrate (BIDS, Phenopacket, CELLxGENE / TileDB-SOMA pipeline code). **Stage 2 (M4), prototype feedback**: validated coordinates released to Council partners with a feedback brief; preprints on cross-site axis recoverability and dimensional-model benchmarks. **Stage 3 (M5), adoption and iteration**: Council pilots return diagnostic-accuracy and patient-reported-outcome data feeding a v1.1 cycle; Helix Framework cross-institution recipe co-authored with Astera. bioRxiv preprints, quarterly blog posts, OHBM / SfN workshops, GitHub plus Hugging Face releases.

### Public Visibility and Press

**Publications:** Ruzicka, Mohammadi et al. (Science 2024); Mathys, Davila-Velderrain, Mohammadi et al. (Nature 2019); Emani et al. incl. Mohammadi (Science, 2024); 40-plus publications with 4,000-plus citations.

**Open-source tools:** ACTIONet (github.com / shmohammadi / ACTIONet, 500-plus stars), adopted by PsychENCODE and ROSMAP consortia.

**Conference presentations:** PsychENCODE annual meetings, ASHG, SfN, OHBM.

**Organization:** Cytognosis Foundation (cytognosis.org), 501(c)(3) nonprofit incorporated in Delaware, founded in 2024.

## VI. Project Budget and Timeline

### Funding Request

**Amount Requested:** $2,493,200

### Budget Breakdown

The $2,493,200 budget is sized to deliver the connectomic-plus-phenotype core: a Neuroverse v1.0 release at Month 36 validated against two independent dimensional frameworks (HiTOP and Grotzinger, 2026), with the parallel-funded molecular track plugging into the same coordinate space when ready (cross-scale Genome-to-Connectome bridge over PsychENCODE 388 paired donors is anchored but not funded from this budget). Allocation: Personnel 68.9%, Compute and Data Infrastructure 11.6%, Technology Development and Equipment 6.6%, Project Amplification and Community 3.8%, Indirect 9.1%. The PI's effort (50%) is supported externally through the Astera Residency and carries no Google budget line, ensuring nearly the entirety of Google.org's investment flows directly into hires, compute, equipment, and community engagement. The split aligns with Google.org's typical impact-grant guidance (Personnel 60-75%, Indirect 10-12%) and with peer open-science nonprofit benchmarks (comparable Chan Zuckerberg Initiative and Wellcome Leap awards). Specialized cross-scale and open-source roles join in later phases as the work composition shifts.

#### Category 1: Personnel and Staffing

**Total Allocation:** $1,718,000

**Description and Details (100 words):** Salaries benchmarked vs. 2026 Bay-area Pave / levels.fyi / BLS OEWS 15-2051 / 19-1042, nonprofit-adjusted; 30% fringe (HHS). AI / ML Engineer 100% × 36m, $565K ($145K base). Clinical Data Scientist 100% × 36m, $293K ($75K base). Computational Neuroscientist 100% × 30m from M6, $228K ($70K base). Multimodal Integration Scientist 50% × 18m from M18, $127K ($130K base). Open-Source / Edge AI Engineer 50% × 24m from M12, $150K ($115K base). Project Manager 50% × 36m, $215K ($110K base). Purdue subaward (Grama, Physical AI / HPC) 8% × 36m, $140K. PI (50%) and the AlphaGenome-based genotype FM are externally funded.

#### Category 2: Compute and Data Infrastructure

**Total Allocation:** $290,000

**Description and Details (100 words):** GCP TPU v4 / v5 over 36m: ~160K chip-hours at effective $1.30 to $1.50 per chip-hour (basis: GCP list $3.22 on-demand and $2.03 with 1-year v4 commitment, partially offset by Google.org Accelerator + TPU Research Cloud credits Months 1-6) for graph-diffusion-wavelet training, EL++ ontology-embedding over the unified neuro-ontology stack, cross-resolution coordinate fusion, and inference at scale = $215K. Cloud storage (GCS Standard $0.020 per GB-month over ~100 TB active plus Coldline archival) = $55K. Restricted-data access fees: UK Biobank Tier-3 imaging £15K = $20K, ENIGMA membership €50/yr = $0.2K. AlphaGenome embedding compute is parallel-funded.

#### Category 3: Technology Development and Equipment

**Total Allocation:** $163,500

**Description and Details (100 words):** Wearables (Month-18+ wearable-to-fMRI pilot), per vendor list: 2x g.Nautilus ($34K), 3x Muse S Athena ($1.5K), 2x Emotiv EPOC X ($2K). Workstations: 6 hire laptops ($18K, ~$3K each); 2x NVIDIA DGX Spark (GB10) for local AI development ($8K). Edge-deployment: iOS / Android test devices, Apple / Google developer accounts, code-signing ($5K). IRB submission via Salus IRB plus amendments ($15K, Salus rate card). Consultant Pool: legal counsel (Duane Valz, $500/hr × 50h, $25K; DUAs, OpenRAIL-M, FAIR contracts); Privacy, UX/Fairness audit, Biostatistics ($25K). Open-source infrastructure ($30K): CI / CD, Hugging Face hosting, MkDocs / RO-Crate / Copier / SPDX, synthetic-data substitutes.

#### Category 4: Project Amplification and Community

**Total Allocation:** $95,000

**Description and Details (100 words):** Travel to scientific conferences (OHBM, SfN, NeurIPS, Hugging Face Open Source AI, ASHG) for dissemination: $20K per year × 3 years = $60K (basis: GSA federal per-diem rates plus published conference registration fees). Collaborator exchange visits (Human Technopole Milan, Purdue West Lafayette, McLean Boston) included. Workshop hosting at OHBM 2029 ($10K, basis: prior OHBM workshop budgets). Patient Advocacy Council coordination, member time, and pilot-evaluation support: $200 per meeting × 12 members × 12 quarterly meetings = $28.8K, $25K budgeted with partner-organization contributions balancing (basis: published patient-advisory council compensation guidelines, e.g., PCORI). The Council line ensures findings reach the advocacy organizations driving adoption.

#### Category 5: Indirect Costs

**Total Allocation:** $226,700

**Description and Details (100 words):** Organizational overhead at approximately 10 percent of total direct costs ($2,266,500). Covers shared organizational infrastructure: office space, insurance, accounting, legal compliance, IT security, and administrative support. Cytognosis Foundation maintains a lean operational model as a 501(c)(3) nonprofit with no federally negotiated indirect rate; the 10 percent rate reflects actual administrative burden and remains within Google.org's 10 to 12 percent guideline. With the PI line carried externally through the Astera Residency, approximately 91 percent of Google.org's investment flows directly into research personnel, compute, equipment, and community engagement.

### Project Timeline and Milestones

The five milestones progress from a patient-data foundation to patient-advocacy adoption: harmonized data and patient-advocacy partnerships; a continuous coordinate system patients can be matched to; a healthy-baseline brain map at individual resolution; individualized coordinates validated and delivered to advocacy partners; and feedback-driven adoption through patient-advocacy hubs. The Patient Advocacy Council (One Mind, Center for Digital Mental Health, APA Council on Digital Health, ASAM) is engaged across three stages: requirements gathering at the start (M1), prototype access for early feedback at validation (M4), and adoption-plus-iteration at release (M5). Every milestone carries a primary external benchmark, a NeuroBioBank-internal replication metric where applicable, and a pre-registered Go / No-Go decision rule.

#### Milestone 1: Foundation Ready, with Harmonized Patient Data and Patient-Advocacy Partnerships in Place

**Timeframe:** Months 1 to 3

**Activities (150 words):** Hire the engineering staff and stand up FAIR, model-training-ready patient-data resources. (i) **Neuroimaging**: BIDS-curated raw (CuBIDS, BIDS Validator, HeuDiConv) and BIDS-Derivatives via fMRIPrep, sMRIPrep, QSIPrep, and MRIQC with ICA-AROMA / ICA-FIX denoising, emitted as 2 mm MNI152 4D voxel volumes alongside the Schaefer-400 + Tian-III + Buckner-7 parcellation triple, DataLad-versioned and Zenodo-DOI'd, across HCP (YA, D, A, BCP), ABCD, OpenNeuro, ENIGMA rs-fMRI groups (SZ, MDD, PTSD, OCD), and NeuroGAP-Psychosis (cross-ancestry). (ii) **Phenotypes**: GA4GH Phenopackets. (iii) **Variants**: GA4GH VRS / VRS-Cat in TileDB-VCF. (iv) **Single-cell**: CELLxGENE-schema TileDB-SOMA. Convene the Patient Advocacy Council (One Mind, Center for Digital Mental Health, APA Council on Digital Health, ASAM) for Stage-1 requirements: priorities, adoption barriers, fairness concerns, and patient-facing communication standards that shape downstream model targets and release gates. Publish QC protocols, demographic-balance audits, site-effect quantification, and a harmonization-v1 report. Begin Google.org Accelerator engagement on TPU sparse-graph kernels, LiteRT preparation, and data-pipeline engineering.

**Outcomes / Key Milestones (100 words):** Open release, tiered. CC BY 4.0: harmonization-v1, QC/demographic audits, crosswalks, group-level maps. Apache 2.0: code. Subject-level BIDS, Phenopackets, VCF, single-cell stay under upstream DUAs (HCP, ABCD, ENIGMA, NeuroGAP, dbGaP, CELLxGENE). ≥3,500 BIDS rs-fMRI scans across ≥4 disorders (SZ, MDD, PTSD, OCD) plus lifespan controls; ≥90% MRIQC-pass; fMRIPrep / sMRIPrep / QSIPrep derivatives (2 mm MNI152; Schaefer-400 + Tian-III + Buckner-7), DataLad-versioned; TileDB-VCF / SOMA plug-ins live. PAC seated (One Mind, CDMH, APA Council on Digital Health, ASAM), ≥3 sessions, ≥30 participants; Stage-1 brief (CC BY 4.0) gates every release. IRBs: primary approved, ≥2 pending. AI / ML Engineer and Clinical Data Scientist onboarded. Google.org engagement opened on TPU sparse-graph kernels, LiteRT, pipelines.

#### Milestone 2: From Symptom Checklists to a Phenotypic Foundation Model for Patients

**Timeframe:** Months 3 to 6

**Activities (150 words):** Build the disease-and-phenotype semantic embedding space that replaces categorical labels with a continuous coordinate system capturing patient-specific variation. Curate uPheno and HP in Protégé using ROBOT, integrating EL++ axioms and sub-ontologies from neuro-specific sources (NBO, NIFSTD, MFO, MFOMD, CogPO, Cognitive Atlas, MFOEM, ASDPTO) to cover neuro-behavioral terms not yet captured. Embed the unified EL++ stack (GO-Plus with UBERON and Cell Ontology subsumptions; HP; uPheno-extended; MONDO; DOID; SNOMED CT) into one shared semantic space using a geometric description-logic method (e.g., TransBox), validated via link prediction, concept similarity, and refinement consistency on held-out term and disorder splits. Translate UMLS Metathesaurus and cross-ontology bridges into LinkML-compatible SSSOM tables, accessed via OAK (Ontology Access Kit). Map and harmonize heterogeneous disease/phenotype annotations from ENIGMA and NeuroBioBank into the unified space using NeuroComBat for site-effect correction. Translate Stage-1 Patient Advocacy Council requirements into adoption-readiness targets (fairness, interpretability, clinician-facing labels) for the coordinate space.

**Outcomes / Key Milestones (100 words):** **First open release of phenotypic embeddings and model (CC0 weights, MIT code).** Apache 2.0: TransBox ontology embedding model. CC BY 4.0: ontology-term embeddings for MONDO, HP, uPheno-extended, GO-Plus, DOID, NBO, NIFSTD; SNOMED-CT embeddings restricted to SNOMED affiliates. CC BY 4.0: SSSOM cross-ontology mappings, bias-audit framework v1 with demographic performance cards, harmonization-v2 report. uPheno extension upstreamed to OBO Foundry. Subject-level vectors stay under upstream DUAs; aggregated vectors released after re-id sign-off. Quantitative success: Gromov-Wasserstein optimal transport between MONDO-term and pooled-phenotype embedding spaces aligns ≥50% of disorders across domains. Stage-1 Council targets met. 6-month deliverable shared verbatim with Astera Round-2.

#### Milestone 3: First Open Map of Healthy Brain Function at Individual Resolution

**Timeframe:** Months 6 to 12

**Activities (150 words):** Hire the Computational Neuroscientist at Month 6. Build the connectomic foundation model: multi-resolution graph diffusion wavelets (Coifman, 2006) with cross-resolution attention over the whole-brain graph at 1M-node scale. Inject the Schaefer-400 + Tian-III + Buckner-7 parcellation triple as learnable node attributes rather than collapsing dimension. Train on ≥5,000 harmonized cross-disorder rs-fMRI scans drawn from the M1 substrate. Regularize axes with 19 neuromaps PET-derived neurotransmitter receptor maps and Allen Human Brain Atlas regional expression so axes reflect neurobiology, not scanner artifacts, while improving interpretability. Replace ComBat with an in-model learned harmonization layer preserving biologically meaningful variance. Run ablations: wavelet versus single-resolution GNN baselines (BrainNetCNN, BrainGNN); with versus without molecular priors; single-disorder versus cross-disorder regimes. Continue Accelerator engagement on distributed TPU sparse-graph kernels. Submit a preprint to bioRxiv documenting harmonization layer, architecture, and preliminary axis discovery.

**Outcomes / Key Milestones (100 words):** **First open release of the multi-resolution connectomic foundation model mapping healthy brain function at individual resolution.** Apache 2.0: model code; MIT: training/inference scripts; CC0: pretrained weights; CC BY 4.0: ablation report, generalization metrics. Subject-level scans stay under upstream DUAs; group-level connectivity maps released. Quantitative gates: trained on ≥5,000 harmonized cross-disorder scans; held-out cross-site generalization MAE within 10% of within-site baseline; aging-signature recovery r > 0.7 against chronological age; ablation deltas: ≥+15% AUC for multi-resolution over single-resolution GNNs, ≥+10% for molecular priors, ≥+5% for cross-disorder pooling. Preprint on bioRxiv. Team operational: PI, AI / ML Engineer, Clinical Data Scientist, Computational Neuroscientist, Project Manager.

#### Milestone 4: Individualized Coordinates Validated and Delivered to Patient-Advocacy Partners

**Timeframe:** Months 12 to 18

**Activities (150 words):** Fine-tune the connectomic foundation model on disease-anchored cohorts via ENIGMA federated queries across SZ, BD, MDD, PTSD, OCD, autism, and ADHD working groups. Validate learned axes against two independent external frameworks: HiTOP dimensional spectra and the Grotzinger 2026 five-factor PGC architecture across 14 disorders. Test cross-site generalization by holding out sites. Run NeuroBioBank-internal replication on the McLean MRI overlap with HBTRC postmortem data: recompute axes on NBB samples aggregated by 14 PGC diagnoses; require directional agreement and within-bound effect-size recovery for HiTOP correlations. Initiate UK Biobank imaging access (50,000+ scans) for large-scale replication. Apply the bias-audit framework and publish demographic-performance cards. Submit first peer-reviewed manuscript and preprint. **Stage 2, prototype access for the Patient Advocacy Council:** package validated coordinates plus model and data cards as a partner-only preview; structured feedback sessions surface adoption blockers, patient-facing language gaps, and pilot-design needs.

**Outcomes / Key Milestones (100 words):** **Go / No-Go decision: axes correlate with HiTOP and Grotzinger 2026 at r > 0.5 on ≥3 of 5/6 dimensions; NBB-internal replication confirms signal recovery on independent samples; cross-site generalization confirmed biological, not scanner-specific.** Tiered open release v1.0: Apache 2.0 (training/eval code); MIT (inference); CC0 (pretrained disease-aware connectomic checkpoint weights); CC BY 4.0 (evaluation benchmarks, model and data cards, demographic-performance cards). Subject-level scans stay under DUA; harmonized derivatives released where DUA permits. **Stage-2 partner-only preview** delivered to ≥3 Council partners; feedback brief (CC BY 4.0) published. Internal wearable-to-fMRI pilot (3-5 team members) ramps cross-scale work.

#### Milestone 5: From Research Tool to Clinical Adoption Through Patient-Advocacy Hubs

**Timeframe:** Months 18 to 36

**Activities (150 words):** Align pretrained per-scale models (connectomic, phenotypic, plus the parallel-funded genotypic FM) into Neuroverse v1.0 via cross-resolution attention with subspace-alignment regularization, using bridge datasets with paired modalities from the same individuals (e.g., ENIGMA fMRI + genotypes; PsychENCODE single-cell RNA-seq + genotype). Build the Neuroverse edge layer: the Open-Source / Edge AI Engineer fine-tunes Gemma 4 via LoRA + DPO into the on-device interviewer voice agent and supervisor thinking agent, deployed via LiteRT with Flutter shipping the multi-agent stack to phones; the layered three-tier privacy architecture is exercised end-to-end. **Stage 3, adoption and feedback through patient-advocacy hubs:** Council partners (One Mind, Center for Digital Mental Health, APA Council on Digital Health, ASAM) run a 15 to 20-participant external pilot (MDD, GAD, schizophrenia, controls); adoption telemetry and patient-reported outcomes feed a v1.1 refinement cycle. Scale repository past 10,000 scans via UK Biobank. Host the Neuroverse OHBM 2029 workshop. Submit ARPA-H PHO and NSF Tech Labs follow-ons.

**Outcomes / Key Milestones (100 words):** **Neuroverse v1.0 released and adopted through patient-advocacy hubs.** Open release: Apache 2.0 (code); MIT (Flutter app, edge stack); CC0 (cross-scale alignment weights, Gemma 4 LoRA adapters); CC BY 4.0 (model/data cards, NeuroGAP-anchored ancestry-disaggregated performance cards). Subject-level data stays under DUAs. **Quantitative gates:** ≥2 Council partners run external pilots (15-20 participants each across MDD, GAD, schizophrenia, controls), returning diagnostic-accuracy, differential-treatment-response, and patient-reported-outcome data into v1.1; edge stack hits sub-300ms speech latency, ≥95% accuracy vs. cloud inference, zero raw-signal egress; repository exceeds 10,000 scans across ≥8 disorders; ≥1,000 unique downloads, ≥50 institutions, 3-5 publications; ARPA-H PHO and NSF Tech Labs follow-ons submitted.

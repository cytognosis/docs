# **Google.org Impact Challenge: AI for Science (Revised v3)**

## Cytognosis Foundation, Neuroverse track

## II. Impact

### Title

Neuroverse: Realizing Precision Psychiatry Through a Multimodal Map of Brain Circuit Variation

### 

### Problem Statement

#### The Challenge (75 words)

Mental healthcare treats psychiatric conditions as discrete categorical diagnoses, defined by symptom checklists, despite years of evidence across diverse cohorts indicating that psychiatric manifestations span a continuum of severity, are highly comorbid, and are driven by shared molecular and circuit-level mechanisms that cut across diagnostic boundaries. Even worse, individuals with identical diagnoses exhibit substantial heterogeneity in phenotypic manifestations and treatment responses. Misdiagnosis and treatment failure remain the norm for the people who need help most.

#### Significance (75 words)

First-line psychiatric treatments fail in 47 to 58 percent of patients; relapse climbs from 40 to 71 percent across trials. The cost: $528 billion annually on suboptimal therapy within a $5.3 trillion healthcare system. Data-driven biotypes predict treatment response and patient outcome (e.g., Drysdale depression subtypes), but each is single-disease, single-modality, and inconsistent across cohorts, blocking clinical adoption. Our unified multimodal map of brain-circuit variation bridges this gap, making transdiagnostic precision psychiatry actionable for patients.

#### Core Research Questions (75 words)

Four questions guide the work: (1) Can the model uncover shared and unique mechanisms within and across traditional diagnostic categories, resolving the heterogeneity within each? (2) Is the map sensitive enough to capture clinically relevant shifts in an individual's mental state, including treatment effects? (3) Can it predict individual mental-health trajectories? (4) Can it recommend personalized treatments that improve outcomes above and beyond group-matched standards? The answers let clinicians treat the person, not the label.

### Proposed Solution

#### Solution Overview (75 words)

Neuroverse replaces categorical psychiatric labels with continuous, individual-grain coordinates so clinicians can match patients to the treatment most likely to work, not just the one labeled for their diagnosis. Google.org funds the core: a connectomic foundation model paired with a continuous phenotypic coordinate space, harmonized across population-scale neuroimaging and clinical cohorts. A parallel molecular-and-genomic track, funded separately, develops cross-scale bridges synergistic with this work; we describe the integration here so reviewers can see the full trajectory.

#### Tools, Methods, and Techniques (75 words)

We model brain connectivity as a sparse graph from spatio-temporal fMRI; efficient multi-resolution graph neural networks (with polynomial approximations) capture short- and long-range activity cascades whole-brain at 1M-node scale. Rather than predefined atlases collapsing dimension (information loss, premature bias), we inject an ensemble (neuromaps PET, Allen Brain Atlas transcriptomics, FOCUS subcortical) as node attributes regularizing embeddings; the model attends to the most informative atlas per task. Pretraining: subgraph-masked self-supervision on HCP, UKBB, ABCD, ENIGMA, OpenNeuro.

#### Evidence of Feasibility (75 words)

Our team developed the first single-cell Alzheimer's atlas (Mathys, Davila-Velderrain, Mohammadi et al.; Nature, 2019) and the largest multi-cohort schizophrenia atlas (Ruzicka, Mohammadi et al.; Science, 2024), demonstrating that continuous disease axes exist within categorical diagnoses at the molecular level. Independent studies have corroborated this dimensional structure: genomic modeling across 14 disorders explains 66 percent of the genetic variance in psychiatric disorders, data-driven neuroimaging bifactor models outperform theory-driven approaches, and validated neurotransmitter receptor atlases provide the molecular priors necessary to extend these findings to whole-brain circuitry.

#### Force Multiplier Effect (75 words)

Open-release of harmonized FAIR datasets and pretrained cross-scale foundation models gives every neuroimaging lab worldwide a shared substrate that previously took months of per-site preprocessing, while smaller groups gain transfer-learning paths to rare disorders without the data scale only well-funded centers had. The patient-advocacy council (One Mind, Center for Digital Mental Health, APA Council on Digital Health, ASAM) propagates discoveries and tools from researchers directly into clinical adoption channels, turning open science into patient impact.

### End Beneficiaries

#### Target Populations (75 words)

Fifty-three million U.S. adults live with mental illness, including 14.1 million with serious conditions, and often receive ineffective treatments due to categorical misdiagnosis. Rural counties average only 3.5 psychiatrists per 100,000 people, compared to 13.0 in urban areas, and 65 percent have no psychiatrist. Racial and ethnic minorities experience 30 to 50 percent higher misdiagnosis rates. Neuroverse could bring precision psychiatry to resource-limited settings globally, where neuroimaging infrastructure is growing but specialist access remains limited.

#### Beneficiary Engagement (75 words)

Our Patient Advocacy Council convenes representatives from One Mind (transdiagnostic), the Center for Digital Mental Health (Harvard / MGH, 125-plus scientist-clinician network), the APA Council on Digital Health, Innovation, and Technology, and ASAM (for SUD-specific privacy and adoption). Members surface patient needs during development and serve as adoption hubs post-development, delivering models into the communities they represent. Clinician partners at McLean and Mount Sinai co-develop validation protocols. Findings reach participants in aggregated, deidentified form before release.

#### Project Reach (75 words)

The patient-advocacy council members are dissemination hubs: One Mind funnels findings across transdiagnostic patient communities; the Center for Digital Mental Health pushes tools through 125-plus scientist-clinician collaborators at Harvard / MGH; the APA Council on Digital Health drives clinical adoption through psychiatry's largest professional body; ASAM reaches the SUD population. Each connects core team output to thousands of patients and clinicians, multiplying the project's impact exponentially across geographies, conditions, and care settings within the 36-month window.

### Expected Outcomes

#### Success Metrics (75 words)

Scientific gates: learned axes explain over 50 percent of cross-disorder variance and correlate at r > 0.5 with HiTOP and the Grotzinger 2026 five-factor; cross-scale AUC ≥ 0.75 on PsychENCODE 388 paired held-out donors; harmonized release reaches 10,000-plus scans across 6-plus disorders. Impact gates: at least two patient-advocacy council partners run pilot evaluations by Month 24, returning diagnostic-accuracy, differential-treatment-response, and patient-reported-outcome data; ancestry-disaggregated demographic-performance cards ship with every release.

#### Failure Indicators (75 words)

Scientific failures: learned axes fail to replicate across sites; cross-disorder models perform no better than single-disorder baselines; cross-scale predictions underperform random baselines; NBB-internal replication of the PGC five-factor structure misses the pre-registered threshold. Impact failures: no council partner integrates the model into a pilot by Month 24; council pilots return null effects on diagnostic accuracy, treatment response, or patient-reported outcomes; demographic audits surface unmitigated disparities; community adoption stalls below 100 downloads.

#### Expected Changes from Baseline (75 words)

For patients: from categorical labels to individual-grain coordinates matching each person to the right treatment, with measurable improvement in treatment-response rates beyond group-matched standards, validated through patient-advocacy council pilot evaluations. For clinicians: from months of per-lab preprocessing to minutes via pretrained harmonization; from imaging-only to imaging-plus-molecular cross-scale prediction. For the field: from single-disorder neuroimaging silos to a unified cross-disorder atlas (10,000-plus scans) benchmarked against HiTOP and Grotzinger 2026, with 30 to 50 percent better cross-site prediction.

## III. Innovative Use of Technology

### Technology Stack and Implementation (100 words)

PyTorch Geometric implements multi-resolution graph diffusion wavelets (Coifman, 2006) with cross-resolution attention; specific candidates include WaveGC, Hypergraph Wavelets (Sun 2024), and InfoGain Wavelets (Johnson, 2025). fMRIPrep, QSIPrep, and FreeSurfer standardize to BIDS/FAIR; neuromaps and the Allen Human Brain Atlas anchor learnable molecular priors. A geometric description-logic ontology embedding stack (e.g., TransBox over EL++ ontologies) builds the continuous phenotypic coordinate backbone. Gemma 4, fine-tuned with LoRA and DPO and deployed via LiteRT, powers the on-device interviewer-plus-supervisor multi-agent stack; Flutter ships it to phones. TPU v4 / v5 trains; Hugging Face plus AnnData / Zarr distribute. AlphaGenome-based molecular encoders (parallel-funded) plug into the same coordinate space.

### Custom Solution Development (100 words)

Existing tools fall short in four ways. Standard harmonization (ComBat, CovBat) discards biological variance; we replace it with a learned layer within the model. Single-resolution, single-disorder graph networks (BrainNetCNN, BrainGNN) miss multi-scale, cross-disorder structure; multi-resolution graph diffusion wavelets (Coifman 2006, with WaveGC and similar wavelet-GNN variants as candidates) address both. Symptom-checklist phenotyping discards the dimensional structure psychiatry needs; geometric EL++ ontology embeddings (e.g., TransBox) over a unified neuro-ontology stack build the continuous coordinate backbone. Cloud-API LLMs cannot meet sub-300ms speech-interjection latency without leaking voice; Gemma 4 plus LiteRT plus the multi-agent supervisor-and-interviewer architecture meets both. (Molecular-encoder extensions to AlphaGenome are developed in a parallel, separately-funded track and reuse the same coordinate space.)

### Datasets (100 words)

Connectomic core (Google.org-funded), accessed under their respective Data Use Agreements: HCP (1,200 healthy adults, ConnectomeDB DUA); UK Biobank (50,000+ imaging subset, application plus access fees); ABCD (12,000 youth, NIMH Data Archive DUA, demographically diverse by design); ENIGMA federated working groups across SZ, BD, MDD, PTSD, OCD; disorder-specific BIDS-compliant studies on OpenNeuro. Cross-ancestry: NeuroGAP-Psychosis (Stanley Center DUA, Ethiopia, Kenya, South Africa, Uganda), H3Africa. Open atlases as molecular priors: neuromaps (19 PET receptor maps); Allen Human Brain Atlas (regional gene expression). Phenotype: HiTOP, Grotzinger 2026 PGC five-factor across 14 disorders. PsychENCODE 388 paired WGS plus single-cell (consortium DUA) anchors the parallel-funded molecular track for cross-scale integration.

### Ethical Considerations (100 words)

Our design aligns with Google's AI Principles. Social benefit: open release reaches underserved communities. Avoiding unfair bias: training on demographically diverse cohorts (ABCD, NeuroGAP-Psychosis, H3Africa, ENIGMA) with disaggregated demographic audits. Safety: coordinates augment, never replace, clinician judgment; because individualized psychiatric predictions can produce catastrophic errors (LLM-therapy chatbots have already been linked to suicidal ideation), every clinical-facing output gates behind clinician review and explicit uncertainty disclosure, with no autonomous diagnostic claims. Privacy: on-device Gemma 4 + LiteRT + Flutter stack keeps voice and behavioral signals on the phone; membership-inference probes gate releases. Model and data cards ship with every release.

### Google.org Accelerator Participation (100 words)

We benefit most from Google's expertise in three areas. First, TPU optimization for graph networks plus LiteRT optimization for Gemma 4: graph diffusion wavelet kernels and on-device multi-agent inference both require Google-engineer-level acceleration to hit our latency and throughput targets. Second, large-scale data pipeline engineering: harmonizing 10,000-plus scans across formats, sites, and ontology vocabularies is where Google Cloud best practices reduce iteration cycles. Third, foundation model architecture guidance: porting graph foundation models from language and vision to brain connectome topology, and aligning the connectomic and phenotypic coordinate spaces, where DeepMind's AlphaFold and AlphaGenome architectural work is directly relevant for our cross-scale roadmap (parallel-funded molecular extensions reuse this guidance).

## IV. Feasibility

### Organizational Positioning (150 words)

Cytognosis Foundation uniquely combines personnel with a published track record building molecular atlases of brain disease, existing consortium access to the datasets this project requires, and an institutional commitment to open release that ensures results drive distributed innovation.

Our PI led the first multi-cohort single-cell schizophrenia atlas (Ruzicka, Mohammadi et al.; Science, 2024), identifying continuous disease axes within a single DSM diagnosis: Neuroverse's direct scientific foundation. He co-led the first single-cell Alzheimer's atlas (Mathys, Davila-Velderrain, Mohammadi et al.; Nature, 2019) and contributed to the PsychENCODE capstone integrating 388 brains (Emani et al.; Science, 2024). These constitute molecular-scale proof that the dimensional axes this project maps at connectomic and cross-scale resolution are real and discoverable.

Our Co-Lead at Human Technopole bridges molecular and circuit neuroscience. Our Senior Advisor at Purdue directs the Institute for Physical AI, providing foundation-model and scalable-computing expertise. The team spans computational neuroscience, AI systems, and open-source infrastructure.

### AI Maturity

AI First.

### Technical Feasibility (100 words)

Our Science 2024 publication demonstrated that continuous disease axes are discoverable within single DSM diagnoses and replicate across independent cohorts; this is the dimensional-axis principle Neuroverse extends to whole-brain connectomes. The neuromaps atlas (Hansen et al.; Nature Methods, 2022) validates neurotransmitter receptor maps as reliable molecular priors for connectomic models. Grotzinger et al. (2025, Nature) independently confirmed a five-factor structure explaining 66 percent of psychiatric genetic variance; Quah et al. (2025) showed data-driven neuroimaging bifactor models outperform theory-driven frameworks. A tau-PET imputation result (Nature Communications, 2025) demonstrates cross-modal prediction tractability, supporting the parallel-funded cross-scale extension.

### Risk Management and Mitigation (200 words)

**Patients in under-resourced sites get predictions reflecting scanner brand more than biology.** fMRIPrep / QSIPrep plus an in-model learned harmonization layer preserves variance; held-out-site replication is a release gate; site-aware fallbacks model site explicitly.

**Patients are matched to coordinates no clinician can act on.** Axes must hit r > 0.5 against HiTOP and the Grotzinger 2026 five-factor on at least 3 of 5 / 6 dimensions; single-benchmark hits release as provisional only.

**Patients receive catastrophically wrong personalized predictions.** LLM-therapy chatbots have been linked to suicidal ideation. Clinical-facing outputs gate behind clinician review with explicit uncertainty disclosure; no autonomous diagnostic claims; red-team failure-mode model cards ship with every release; the Patient Advocacy Council reviews patient-facing messaging before any pilot.

**Patients from under-represented ancestries get the worst predictions.** PGC / HiTOP benchmarks lean European-ancestry; cross-ancestry validation anchors on NeuroGAP-Psychosis (Ethiopia, Kenya, South Africa, Uganda), H3Africa, and ABCD's diverse-by-design sampling, with ancestry-disaggregated performance cards as a hard release gate.

**Patients lose the cross-scale molecular precision the roadmap promises.** Genome-to-Connectome integration is in the parallel, separately-funded molecular track (PsychENCODE 388 paired donors); if it slips, Neuroverse v1.0 still ships the connectomic-plus-phenotype core unchanged.

**Patients face delays from access or hiring slips.** Open datasets (HCP, ABCD, OpenNeuro) drive initial work; IRB initiates Month 1; PI's 20-year ML background covers solo development with a 3-month hiring buffer.

### Key Team Members (100 words)

**PI: Shahin Mohammadi, PhD** (50%). 20 years in AI for biology (MIT, Broad, insitro, GenBio AI). Led single-cell atlases in Nature (2019) and Science (2024); creator of ACTIONet.

**Co-Lead: Jose Davila-Velderrain, PhD** (advisory; Group Leader, Human Technopole). Co-developed PsychAD atlas (Science, 2024); bridges molecular and circuit neuroscience.

**Clinical Collaborator: Brad Ruzicka, MD/PhD** (McLean Hospital / Harvard Medical School). HBTRC NeuroBioBank liaison; co-led the multi-cohort schizophrenia atlas (Science, 2024): anchors clinical validation and NBB cohort access.

**Senior Advisor: Ananth Grama, PhD** (8%; Distinguished Professor, Purdue; Director, Institute for Physical AI). Foundation-model architecture and scalable computing.

**AI / ML Engineer (hire, 100%):** geometric deep learning, graph diffusion wavelet implementation, AlphaGenome fine-tune, Gemma 4 LoRA plus DPO.

### Partner Organizations

**Partner 1: Human Technopole.** Website: [https://humantechnopole.it](https://humantechnopole.it). Role (50 words): Co-Lead Jose Davila-Velderrain provides cross-scale neuroscience expertise bridging molecular and circuit-level analysis, contributing directly to model design and the cross-scale Genome-to-Connectome validation. Human Technopole offers access to European cohorts, high-performance computing, and the European computational neuroscience network, enabling validation across diverse international scanner configurations. Status: Existing partner.

**Partner 2: Purdue University, Institute for Physical AI.** Website: [https://www.purdue.edu/ipai/](https://www.purdue.edu/ipai/). Role (50 words): Senior Advisor Ananth Grama provides strategic guidance on foundation-model architecture, scalable computing optimization, and AI interpretability methods critical for biological applications. Purdue's IPAI offers high-performance computing infrastructure and a multidisciplinary network spanning AI, physics, and life sciences, strengthening the project's computational foundations and providing the redundant compute fabric our risk plan requires. Status: Existing partner.

**Partner 3: McLean Hospital / Harvard Medical School.** Website: [https://www.mcleanhospital.org](https://www.mcleanhospital.org). Role (50 words): McLean Hospital, Harvard Medical School's largest psychiatric affiliate, provides clinical neuroscience expertise for validating dimensional axes against patient outcomes. As the lead site of the Harvard Brain Tissue Resource Center (NeuroBioBank), McLean offers postmortem brain tissue and clinical data that enable molecular validation of connectomic findings and bridge imaging to cellular resolution. Status: Existing partner.

## V. Scalability

### Scalability Strategies Selected

Geographic transfer to new regions; sector adaptation to related fields; ecosystem integration with existing infrastructure; community-driven expansion; open-source adoption.

### Team Evolution for Scale (150 words)

Scale-up follows our three-horizon strategy. Horizon 1 (Years 1 to 5): the Cytognosis Foundation derisks the platform; this proposal lands the connectomic-plus-phenotype map as the proof-of-concept in mental health, with a dedicated open-models team in the Foundation continuously refreshing it every 6 to 12 months on clinical-grade public and open data. Horizon 2 (Years 5 to 10): IP licenses to an impact-aligned PBC execution arm that builds the Cytoscope (wearable sensors continuously locating individuals on the map) and the Cytonome (navigation that not only tracks but recommends intervention; the GPS-for-health analogy). Horizon 3 (Years 10 to 15): the blueprint extends stepwise to immune, microbiome, and other systems, then their cross-system interactions. A post-Month-36 longitudinal pilot pairs wearable EEG plus fNIRS with WGS, physiology, and neuro-behavior in the same individuals over time, validating wearable-to-clinical mapping, sensitivity to interventions, and pre-symptomatic trajectory tracking years before symptoms surface.

### Financial Sustainability (50 words)

ARPA-H Mission Office ISO submission (PHO or HSF) targets $20-30M for clinical-scale validation. NSF Tech Labs five-year center grant, independently or as a Cytognosis-Convergent-Research joint center, sustains the open infrastructure. A future public benefit corporation subsidiary may commercialize diagnostic applications on top of the open core, without closing it.

### Technical Sustainability (50 words)

Google.org funding establishes research-grade baselines: harmonized datasets, pretrained connectomic foundation models, the phenotypic coordinate backbone, validated dimensional axes, and evaluation benchmarks. The parallel-funded molecular track plugs into the same coordinate space. Additional ARPA-H, NSF, and NIH support sustains active development; GitHub-hosted open source ensures evolution beyond any one funding cycle.

### Knowledge Sharing and Learning (100 words)

Knowledge sharing tracks the three Council stages. **Stage 1 (M1), requirements**: published Council requirements brief co-authored with One Mind, Center for Digital Mental Health, APA Council on Digital Health, and ASAM, plus the open harmonized substrate (BIDS, Phenopacket, CELLxGENE / TileDB-SOMA pipeline code). **Stage 2 (M4), prototype feedback**: validated coordinates released to Council partners with a published feedback brief; preprints on cross-site axis recoverability and dimensional-model benchmarks. **Stage 3 (M5), adoption and iteration**: Council pilots return diagnostic-accuracy and patient-reported-outcome data feeding a v1.1 refinement cycle; Helix Framework cross-institution recipe co-authored with Astera. bioRxiv preprints, quarterly technical blog posts, OHBM / SfN workshops, GitHub plus Hugging Face releases.

### Public Visibility and Press

**Publications:** Ruzicka, Mohammadi et al. (Science 2024); Mathys, Davila-Velderrain, Mohammadi et al. (Nature 2019); Emani et al. incl. Mohammadi (Science, 2024); 40-plus publications with 4,000-plus citations.

**Open-source tools:** ACTIONet (github.com / shmohammadi / ACTIONet, 500-plus stars), adopted by PsychENCODE and ROSMAP consortia.

**Conference presentations:** PsychENCODE annual meetings, ASHG, SfN, OHBM.

**Organization:** Cytognosis Foundation (cytognosis.org), 501(c)(3) nonprofit incorporated in Delaware, founded in 2024.

## VI. Project Budget and Timeline

### Funding Request

**Amount Requested:** $2,500,000

### Budget Breakdown

The $2,500,000 budget is sized to deliver the connectomic-plus-phenotype core: a Neuroverse v1.0 release at Month 36 validated against two independent dimensional frameworks (HiTOP and Grotzinger, 2026), with the parallel-funded molecular track plugging into the same coordinate space when ready (cross-scale Genome-to-Connectome bridge over PsychENCODE 388 paired donors is anchored but not funded from this budget). Allocation: Personnel 70.0%, Compute and Data Infrastructure 12.8%, Technology Development and Equipment 4.3%, Project Amplification and Community 3.8%, Indirect 9.1%. The PI is budgeted at the discounted-fees consulting tier ($165K/year, $13,750/month) per executed CEO Contractor Agreement effective 2025-10-01 (the full $270K/year tier requires $5M cumulative external funding, which Google.org's $2.5M alone does not reach); PI is a 1099 independent contractor without employer-paid fringe per Section 7 of the agreement. The split aligns with Google.org's typical impact-grant guidance (Personnel 60-75%, Indirect at 10-12%) and with peer open-science research nonprofit benchmarks (comparable Chan Zuckerberg Initiative and Wellcome Leap awards). Specialized cross-scale and open-source roles join in later phases as the work composition shifts.

#### Category 1: Personnel and Staffing

**Total Allocation:** $1,750,500

**Description and Details (100 words):** PI 50% effort × 36m at $165K/year (discounted-fees consulting tier per executed CEO Contractor Agreement; full $270K/year tier requires $5M cumulative external funding which Google.org alone does not reach): $247.5K, 1099 contractor no fringe per agreement Section 7. Hire salaries benchmarked against 2026 SF Bay-area Pave / levels.fyi / BLS OEWS 15-2051 / 19-1042 nonprofit-adjusted; 30% fringe per HHS. AI / ML Engineer 100% 36m, $565K ($145K base; graph diffusion wavelets, EL++ ontology embeddings, Gemma 4 LoRA + DPO, cross-scale coordinate fusion). RA1 Neuroimaging 100% 36m, $293K ($75K). RA2 Comp Neuro 100% 30m from M6, $228K ($70K). Multimodal Scientist 50% 18m from M18, $127K ($130K). Open-Source / Mobile Edge Engineer 50% 24m from M12, $150K ($115K). Purdue subaward (Grama) 8% 36m, $140K. AlphaGenome / molecular-encoder work is parallel-funded and not on this line.

#### Category 2: Compute and Data Infrastructure

**Total Allocation:** $320,000

**Description and Details (100 words):** GCP TPU v4 / v5 across 36 months: approximately 160K chip-hours at effective $1.30 to $1.50 per chip-hour (basis: GCP list price $3.22 on-demand and $1.93 with 1-year commitment for v4, partially offset by Google.org Accelerator credits during Months 1-6) for graph-diffusion-wavelet training, EL++ ontology-embedding training over the unified neuro-ontology stack, cross-resolution coordinate fusion, and inference at scale = $215K. Cloud storage at GCS Standard $0.020 per GB-month over ~100 TB active plus Coldline archival = $55K. GPU workstations (5x H100-class at $5K each, vendor list) = $25K. Restricted-data access fees (UK Biobank ~$15K, ENIGMA federated infrastructure ~$10K) = $25K. Total $320K, 12.8% of budget. AlphaGenome embedding compute is parallel-funded.

#### Category 3: Technology Development and Equipment

**Total Allocation:** $108,000

**Description and Details (100 words):** Wearable EEG / fNIRS headsets for the Month-18+ Meso-scale wearable-to-fMRI pilot (no physiology / HRV in Google scope; physiology lives in the Foresight track), based on published vendor list prices: 2x g.Nautilus ($34K), 3x Muse S Athena ($1.5K), 2x Emotiv EPOC X ($2K). Edge-deployment infrastructure: iOS plus Android test devices for the Flutter Neuroverse app, Apple Developer plus Google Play Console accounts, code-signing certificates ($5K). IRB submission via Salus IRB plus periodic amendments ($15K, basis: Salus published rate card). Legal counsel for DUAs, OpenRAIL-M license review, FAIR-compliance contracts ($20.5K, basis: ~100 hours at $200/hr). Open-source infrastructure (CI / CD, Hugging Face hosting, MkDocs / RO-Crate / Copier / SPDX, synthetic-data substitutes): $30K. Total $108K, 4.3% of budget.

#### Category 4: Project Amplification and Community

**Total Allocation:** $95,000

**Description and Details (100 words):** Travel to scientific conferences (OHBM, SfN, NeurIPS, Hugging Face Open Source AI, ASHG) for dissemination and community building: $20K per year x 3 years = $60K (basis: GSA federal per-diem rates plus published conference registration fees). Collaborator exchange visits (Human Technopole Milan, Purdue West Lafayette, McLean Boston) included. Workshop hosting at OHBM 2029 ($10K, basis: prior OHBM workshop budgets). Patient Advocacy Council coordination, member time, and pilot-evaluation support: $200 per meeting x 12 members x 12 quarterly meetings = $28.8K, $25K budgeted with partner-organization contributions balancing (basis: published patient-advisory council compensation guidelines, e.g., PCORI). Total $95K, 3.8% of budget; council amplification ensures findings reach the patient-advocacy organizations driving clinical adoption.

#### Category 5: Indirect Costs

**Total Allocation:** $226,500

**Description and Details (100 words):** Organizational overhead is approximately 10 percent of total direct costs ($2,273.5K). Covers shared organizational infrastructure: office space, insurance, accounting, legal compliance, IT security, and administrative support. Cytognosis Foundation maintains a lean operational model as a 501(c)(3) nonprofit with no federally negotiated indirect rate; the 10 percent rate reflects actual administrative burden and remains within Google.org's 10 to 12 percent guideline. This lean structure plus the contractually-grounded modest PI line (1099 discounted-fees tier rather than the full $5M-threshold tier) ensures that approximately 91 percent of Google.org's investment flows directly into research personnel, compute, equipment, and community engagement.

### Project Timeline and Milestones

The five milestones progress from patient-data foundation to patient-advocacy adoption: harmonized data plus patient-advocacy partnerships; a continuous coordinate system patients can be matched to; a healthy-baseline brain map at individual resolution; individualized coordinates validated and delivered to advocacy partners; and feedback-driven adoption through patient-advocacy hubs. The Patient Advocacy Council (One Mind, Center for Digital Mental Health, APA Council on Digital Health, ASAM) is engaged across three stages: requirements gathering at the start (M1), prototype access for early feedback at validation (M4), and adoption-plus-iteration at release (M5). Every milestone includes a primary external benchmark, a NeuroBioBank-internal replication metric where applicable, and a pre-registered Go / No-Go decision rule.

#### Milestone 1: Foundation Ready, with Harmonized Patient Data and Patient-Advocacy Partnerships in Place

**Timeframe:** Months 1 to 3

**Activities (150 words):** Hire AI / ML Engineer and RA1 (M1 to 3). Initiate IRB through Salus IRB. Stand up the patient-data substrate every downstream deliverable depends on: BIDS-standard FAIR neuroimaging via fMRIPrep / QSIPrep across HCP, ABCD, OpenNeuro, ENIGMA (SZ, BD, MDD, PTSD, OCD), and NeuroGAP-Psychosis for cross-ancestry coverage; GA4GH Phenopacket-conformant phenotype records; GA4GH VRS / VRS-Cat variants in TileDB-VCF and CELLxGENE-schema TileDB-SOMA single-cell stores prepared as plug-in points for the parallel-funded molecular track. Convene the Patient Advocacy Council (One Mind, Center for Digital Mental Health, APA Council on Digital Health, ASAM) for **Stage 1, requirements gathering**: structured sessions surface patient priorities, adoption barriers, fairness concerns, and patient-facing communication standards that shape downstream model targets and release gates. Publish quality-control protocols, demographic-balance audits, site-effect quantification, and harmonization-v1 report. Begin Google.org Accelerator engagement on TPU sparse-graph kernels, LiteRT preparation, and data-pipeline engineering.

**Outcomes / Key Milestones (100 words):** **First open release of harmonized, FAIR-compliant, standards-conformant patient-data substrate under CC BY 4.0**, anchoring every downstream deliverable; identical 3-month substrate shared word-for-word with the parallel-funded Astera Round-2 effort. BIDS imaging at over 3,000 scans across 4-plus disorders; GA4GH Phenopacket phenotype records; molecular-track plug-ins ready (TileDB-VCF, TileDB-SOMA). Quality-control pipeline with documented site-effect metrics. **Patient Advocacy Council convened; Stage-1 requirements brief published**, defining patient priorities, adoption barriers, and patient-facing communication standards that will gate every model release. IRB approved or in final review. Core team operational.

#### Milestone 2: From Symptom Checklists to a Continuous Coordinate System Patients Can Be Matched To

**Timeframe:** Months 3 to 6

**Activities (150 words):** Build the disease-and-phenotype semantic embedding space that replaces categorical labels with a continuous coordinate system patients can be located in. Curate uPheno and HP via Protégé and ROBOT, integrating EL++ axioms and sub-ontologies from neuro-specific source ontologies (NBO, NIFSTD, MFO, MFOMD, CogPO, Cognitive Atlas, MFOEM, ASDPTO, others) covering behavioral terms not yet captured. Embed the unified EL++ stack (GO-Plus with UBERON and Cell Ontology subsumptions; HP; uPheno-extended; MONDO; DOID; SNOMED CT) into one shared semantic space using a geometric description-logic embedding method (TransBox among candidates benchmarked in parallel), validated via link-prediction, concept-similarity, and refinement-consistency metrics. Generate SSSOM cross-mappings to UMLS and ICD-10 F-G via OLS4 plus Cytognosis-curated mappings. Map ENIGMA diagnostic labels and the Grotzinger 2026 14-disorder PGC set into the space. Validate against Grotzinger's five-factor and HiTOP. Translate Stage-1 requirements from the Council into adoption-readiness targets for the coordinate space.

**Outcomes / Key Milestones (100 words):** **First open release of the continuous phenotypic coordinate space (v1.0)** patients can be matched to: pretrained EL++ ontology embeddings (CC0 weights, MIT code) over the unified stack. SSSOM cross-mappings to UMLS and ICD-10 F-G via OLS4. Curated uPheno extension contributed upstream to the OBO Foundry. Validation report: disease-level Frechet means match the PGC five-factor and at least 3 of 5 / 6 HiTOP dimensions at r > 0.5; embedding metrics meet pre-registered thresholds. Stage-1 Council requirements translated into adoption-readiness targets. Bias-audit framework v1 with demographic performance cards. Identical 6-month deliverable shared word-for-word with the parallel-funded Astera Round-2 effort.

#### Milestone 3: First Open Map of Healthy Brain Function at Individual Resolution

**Timeframe:** Months 6 to 12

**Activities (150 words):** Hire Research Associate 2 (computational neuroscience) at Month 6. Implement multi-resolution graph diffusion wavelets (Coifman, 2006) with cross-resolution attention on the whole-brain graph; parcellation atlases (Schaefer, AAL, Brainnetome, Glasser-360) inject as node attributes rather than collapsing dimension. Train on more than 5,000 harmonized cross-disorder fMRI scans from the open substrate. Integrate 19 neuromaps PET-derived neurotransmitter maps and Allen Human Brain Atlas regional expression as learnable molecular constraints so axes reflect neurobiology, not scanner artifacts. Replace ComBat with an in-model learned harmonization layer preserving biologically meaningful variance. Run systematic ablations: multi-resolution wavelets versus single-resolution GNN baselines (BrainNetCNN, BrainGNN), with versus without neurotransmitter priors, single-disorder versus cross-disorder regimes. Continue Accelerator engagement on distributed TPU strategies. Submit first preprint to bioRxiv documenting harmonization, architecture, and preliminary axis discovery.

**Outcomes / Key Milestones (100 words):** **First open release of a multi-resolution connectomic foundation model that maps healthy brain function at individual resolution**, trained on more than 5,000 harmonized cross-disorder scans with neuromaps PET priors and Allen Human Brain Atlas regional features. Initial transdiagnostic axes identified and visualized. Ablations quantify the contribution of (a) multi-resolution wavelets over single-resolution GNNs, (b) neurotransmitter priors over unconstrained models, and (c) cross-disorder versus single-disorder regimes. Preprint submitted to bioRxiv. Full team (PI, AI / ML Engineer, RA1, RA2) operational. Aging-signature recovery validates as a sanity check. Cross-site held-out generalization metrics published.

#### Milestone 4: Individualized Coordinates Validated and Delivered to Patient-Advocacy Partners

**Timeframe:** Months 12 to 18

**Activities (150 words):** Fine-tune the connectomic foundation model on disease-anchored cohorts via ENIGMA federated queries across SZ, BD, MDD, PTSD, OCD, autism, and ADHD working groups. Validate learned axes against two independent external frameworks: HiTOP dimensional spectra and the Grotzinger 2026 five-factor PGC architecture across 14 disorders. Test cross-site generalization by holding out entire sites. Run NeuroBioBank-internal replication on the McLean MRI overlap with HBTRC postmortem data: recompute axes on NBB samples aggregated by the 14 PGC diagnoses; require directional agreement and within-bound effect-size recovery for NBB-internal HiTOP correlations. Initiate UK Biobank imaging access (50,000-plus scans) for large-scale replication. Apply the bias-audit framework; publish demographic-performance cards. Submit first peer-reviewed manuscript and preprint. **Stage 2, prototype access for the Patient Advocacy Council:** package validated coordinates plus model and data cards as a partner-only preview; structured feedback sessions surface adoption blockers, patient-facing language gaps, and pilot-design needs.

**Outcomes / Key Milestones (100 words):** **Go / No-Go decision recorded:** learned axes correlate with HiTOP and the Grotzinger five-factor at r > 0.5 on at least 3 of 5 / 6 dimensions, with NBB-internal replication confirming signal recovery on independent samples. Cross-site generalization confirmed as biological, not scanner-specific. **Validated, individualized coordinate system delivered to patient-advocacy partners as a Stage-2 preview**, with feedback brief published. Open release v1.0 on GitHub and Hugging Face: harmonized data (where DUA permits), pretrained disease-aware connectomic checkpoints, evaluation benchmarks, model and data cards, demographic-performance cards. Initial wearable-to-fMRI correlation pilot on internal team members (3 to 5) ramps the cross-scale pilot.

#### Milestone 5: From Research Tool to Clinical Adoption Through Patient-Advocacy Hubs

**Timeframe:** Months 18 to 36

**Activities (150 words):** Fuse per-scale connectomic and phenotypic encoders into Neuroverse v1.0 via cross-resolution attention with subspace-alignment regularization, trained on paired plus unimodal sets via modality-dropout; the parallel-funded molecular track integrates through the same coordinate space when ready (Genome-to-Connectome bridge over PsychENCODE 388 paired donors anchors that integration but is not a Google.org-funded deliverable). Build the Neuroverse edge layer: fine-tune Gemma 4 via LoRA plus DPO into the on-device interviewer voice agent and supervisor thinking agent, deployed via LiteRT with Flutter shipping the multi-agent stack to phones; exercise the layered three-tier privacy architecture end-to-end. **Stage 3, adoption and feedback through patient-advocacy hubs:** Council partners (One Mind, Center for Digital Mental Health, APA Council on Digital Health, ASAM) run a 15 to 20-participant external pilot (MDD, GAD, schizophrenia, controls) and feed adoption telemetry plus patient-reported outcomes back into a v1.1 refinement cycle. Scale repository past 10,000 scans via UK Biobank. Host the Neuroverse OHBM 2029 workshop. Submit ARPA-H PHO and NSF Tech Labs follow-ons.

**Outcomes / Key Milestones (100 words):** **Neuroverse v1.0 released and adopted through patient-advocacy hubs**: at least two Council partners run pilots with diagnostic-accuracy, differential-treatment-response, and patient-reported-outcome data returning to a v1.1 refinement cycle. **Neuroverse edge layer** ships as the Gemma 4 fine-tuned interviewer-plus-supervisor stack on LiteRT inside a Flutter app, with sub-300ms speech latency, accuracy within 95 percent of cloud inference, and zero raw-signal egress. Repository exceeds 10,000 scans across 8-plus disorders. Ancestry-disaggregated demographic-performance cards anchored on NeuroGAP-Psychosis. Over 1,000 unique downloads; over 50 institutions; 3 to 5 publications. Cross-scale Genome-to-Connectome integration delivered if the parallel molecular track lands on schedule. ARPA-H and NSF follow-ons submitted.

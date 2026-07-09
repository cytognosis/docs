# Google.org Impact Challenge: AI for Science (Revised v2)

## Cytognosis Foundation, Neuroverse track

This revision rewrites the milestones, costs, scope of work, and technology sections of the Google.org Impact Challenge proposal, and meticulously refines every other section to remain consistent with the new milestone cadence ($2.5M / 36 months, five milestones at 3 / 6 / 12 / 18 / 36 months) and the harmonized Cytognosis Horizon-1 roadmap (M1 through M6 in the canonical milestone document). All scientific anchors, validation gates, and openness commitments are preserved; the new version replaces narrative throughout the application to align with the harmonized roadmap and to use Cytognosis brand voice.

## II. Impact

### Title

Neuroverse: An Open, Continuous Map of Brain Circuit Variation in Mental Health

### Problem Statement

#### The Challenge (75 words)

Modern medicine treats symptoms rather than causes, reduces biology to single targets, and intervenes only after disease manifests. Psychiatry epitomizes all three failures. Categorical DSM diagnoses impose artificial boundaries on conditions that genomic and neuroimaging evidence reveal are continuously distributed, highly comorbid, and mechanistically shared across disorders. Within any single diagnosis, individuals differ so profoundly in etiology and treatment response that the label itself obscures more than it clarifies, driving widespread misdiagnosis and therapeutic failure.

#### Significance (75 words)

First-line psychiatric treatments fail 47 to 58 percent of patients, with relapse climbing from 40 percent to 71 percent across sequential trials, contributing $528 billion annually in non-optimized therapy within a system spending $5.3 trillion, 90 percent on chronic conditions. The failure is structural: overlapping symptoms and shifting presentations make categorical diagnoses unreliable for treatment selection. Genomic modeling across 14 disorders and data-driven neuroimaging now confirm the dimensional architecture these categories obscure, yet no system translates that evidence into clinical tools.

#### Core Research Questions (75 words)

Psychiatry treats disorders as discrete categories, overlooking shared circuit-level mechanisms; applies population averages, overlooking individual heterogeneity; and relies on episodic snapshots, overlooking how neural signatures evolve. These failures motivate three questions. (1) Can AI trained on cross-disorder connectomics recover a continuous map of transdiagnostic brain circuit variation? (2) Does integrating connectomics with cell-resolved molecular biology improve predictions of individual illness trajectories? (3) Can such a multi-scale map predict treatment response where categorical diagnoses fail?

### Proposed Solution

#### Solution Overview (75 words)

Neuroverse replaces categorical psychiatric labels with continuous coordinates of brain circuit variation, then bridges those coordinates to molecular biology so noninvasive imaging complements specialist measurements (PET tracer studies, postmortem molecular analysis) restricted today to a few academic centers. We harmonize multi-site connectomics into FAIR repositories, train a multi-resolution graph foundation model anchored by neurotransmitter molecular priors, and fuse the result with paired single-cell and genome data to release Neuroverse v1.0 as an open, multi-scale community platform.

#### Tools, Methods, and Techniques (75 words)

Our backbone uses multi-resolution graph diffusion wavelets (Coifman 2006) on the full brain graph, with parcellation atlases as node attributes; WaveGC and related wavelet-GNN variants are specific candidates we benchmark in parallel. Foundation pretraining pools HCP, UKBB, ABCD, ENIGMA cohorts plus BIDS-compliant disorder-specific studies hosted on the OpenNeuro repository. Neuromaps PET-derived neurotransmitter receptor maps and Allen Human Brain Atlas regional expression act as learnable molecular priors. Cross-scale fusion against PsychENCODE 388 paired WGS plus single-cell transcriptomes anchors the connectomic-to-molecular bridge.

#### Evidence of Feasibility (75 words)

Our team built the first single-cell Alzheimer's atlas (Mathys, Davila-Velderrain, Mohammadi et al., Nature 2019) and the largest multi-cohort schizophrenia atlas (Ruzicka, Mohammadi et al., Science 2024), proving continuous disease axes exist within categorical diagnoses at the molecular scale. Independent groups confirmed this dimensional architecture: genomic modeling across 14 disorders explains 66 percent of psychiatric genetic variance; data-driven neuroimaging bifactor models outperform theory-driven frameworks; validated neurotransmitter receptor atlases provide the molecular priors needed to extend our findings to whole-brain circuitry.

#### Force Multiplier Effect (75 words)

Our harmonized open dataset accelerates training of transdiagnostic models across sites. Pretrained connectomic foundation models give neuroimaging labs worldwide representations that eliminate months of per-site preprocessing. Open-weight cross-scale models enable transfer learning to rare disorders where small samples have historically precluded precision approaches, democratizing access beyond well-funded centers. Because the architecture is disease-agnostic and FAIR-compliant, every field that maps continuous biological variation, from autoimmune to neurodegenerative indications, inherits the full open infrastructure.

### End Beneficiaries

#### Target Populations (75 words)

The 53 million U.S. adults living with mental illness, particularly the 14.1 million with serious mental illness, cycle through ineffective treatments due to categorical misdiagnosis. Rural counties average 3.5 psychiatrists per 100,000 compared with 13.0 in urban counties, and 65 percent lack any psychiatrist. Racial and ethnic minorities experience 30 to 50 percent higher misdiagnosis rates. Open-source dimensional tools extend precision psychiatry to resource-limited settings globally, where neuroimaging infrastructure is expanding and specialist access remains nonexistent.

#### Beneficiary Engagement (75 words)

A Lived Experience Advisory Council of 8 to 12 individuals with psychiatric diagnoses spanning the disorders our models address (MDD, GAD, PTSD, schizophrenia, bipolar disorder) meets quarterly to review research priorities, model outputs, and communication materials. Clinician partners at McLean Hospital and Mount Sinai co-design clinical validation protocols. Open-source community governance ensures external researchers shape platform priorities. All findings are shared with participants in aggregated, deidentified form before public release, with model cards documenting demographic performance.

#### Project Reach (75 words)

Direct impact over 36 months: 500-plus neuroimaging researchers across 50-plus institutions gain access to harmonized cross-disorder connectome datasets, pretrained connectomic and cross-scale foundation models, and validated dimensional benchmarks. Indirect impact: five clinical research groups integrate dimensional axes into ongoing trials, reaching 2,000 to 5,000 study participants. Geographic reach spans North America, Europe, and East Asia. Public release of datasets, pretrained models, and the Neuroverse edge-AI components removes barriers, enabling unlimited downstream reuse via community contribution.

### Expected Outcomes

#### Success Metrics (75 words)

Learned axes explain over 50 percent of cross-disorder variance in held-out fMRI data and correlate at r > 0.5 with the HiTOP dimensional spectra and the Grotzinger 2026 five-factor genomic architecture across 14 disorders. By Month 36, the platform releases over 10,000 harmonized scans across 6-plus disorders, hosts over 1,000 unique downloads, and accumulates over 50 citing publications within 12 months. Cross-scale validation: predicting molecular subtype from connectome alone reaches AUC at least 0.75 on PsychENCODE 388 paired held-out donors.

#### Failure Indicators (75 words)

Learned axes fail to replicate across independent sites, indicating a harmonization failure rather than biological signal. Models trained on cross-disorder data perform no better than single-disorder baselines, suggesting shared mechanisms are not recoverable at connectomic resolution. Cross-scale predictions from connectome to molecular subtype underperform random baselines, breaking the imaging-to-biology bridge. Community adoption stalls below 100 downloads after six months, suggesting documentation barriers. NBB-internal replication of the PGC five-factor structure misses the pre-registered effect-size threshold.

#### Expected Changes from Baseline (75 words)

From zero to the first open, harmonized, cross-disorder connectome dataset at scale, over 10,000 scans. From categorical-only psychiatric classification to validated dimensional coordinates at circuit resolution, benchmarked against two independent frameworks (HiTOP and the Grotzinger 2026 five-factor genomic architecture). From months of per-lab preprocessing to minutes via pretrained harmonization. From single-disorder neuroimaging silos to a unified cross-disorder atlas with an estimated 30 to 50 percent improvement in cross-site prediction accuracy. From imaging-only to imaging-to-molecular cross-scale prediction.

## III. Innovative Use of Technology

### Technology Stack and Implementation (100 words)

PyTorch Geometric implements multi-resolution graph diffusion wavelets (Coifman 2006) with cross-resolution attention; specific candidates include WaveGC, Hypergraph Wavelets (Sun 2024), and InfoGain Wavelets (Johnson 2025). fMRIPrep, QSIPrep, FreeSurfer standardize into BIDS / FAIR; neuromaps and the Allen Human Brain Atlas anchor learnable molecular priors. AlphaGenome (Google DeepMind) anchors the cross-scale molecular encoder, fine-tuned via geometric description-logic ontology embeddings (e.g., TransBox over EL++ ontologies). Gemma 4 fine-tuned through LoRA plus DPO and deployed via LiteRT powers the on-device interviewer plus supervisor multi-agent stack; Flutter ships it to phones. TPU v4 / v5 trains; Hugging Face plus AnnData / Zarr distribute.

### Custom Solution Development (100 words)

Existing tools fall short four ways. Standard harmonization (ComBat, CovBat) discards biological variance; we replace it with an in-model learned layer. Single-resolution single-disorder graph networks (BrainNetCNN, BrainGNN) miss multi-scale cross-disorder structure; multi-resolution graph diffusion wavelets (Coifman 2006, with WaveGC and similar wavelet-GNN variants as candidate instantiations) fix both. AlphaGenome ships with only GTEx tissue tracks; we extend to 24 BICCN brain cell types via geometric EL++ ontology embeddings (e.g., TransBox), the molecular encoder our cross-scale bridge requires. Cloud-API LLMs cannot meet sub-300ms speech-interjection latency without leaking voice; Gemma 4 plus LiteRT plus the multi-agent supervisor-and-interviewer architecture meets both.

### Datasets (100 words)

We leverage neuroimaging cohorts spanning multiple psychiatric disorders, accessed under their respective Data Use Agreements: HCP (1,200 healthy adults, ConnectomeDB DUA); UK Biobank (50,000-plus imaging subset, application plus access fees); ABCD (12,000 youth, NIMH Data Archive DUA, demographically diverse by design); ENIGMA federated working groups across SZ, BD, MDD, PTSD, OCD; and disorder-specific BIDS-compliant studies hosted on the OpenNeuro repository. NeuroGAP-Psychosis (Stanley Center DUA, Ethiopia / Kenya / South Africa / Uganda) and H3Africa anchor cross-ancestry generalization. Open atlases: neuromaps (19 PET receptor maps); Allen Human Brain Atlas (regional gene expression). PsychENCODE (consortium DUA) delivers 388 donors paired WGS plus single-cell transcriptomes.

### Ethical Considerations (100 words)

Our design aligns with Google's AI Principles across four dimensions. Social benefit: open release reaches underserved communities, not only well-funded centers. Avoiding unfair bias: we train on demographically diverse cohorts (ABCD, NeuroGAP-Psychosis, H3Africa, ENIGMA cross-site) and audit performance across age, sex, ancestry, and scanner type with disaggregated metrics. Safety: coordinates augment clinician judgment; no autonomous diagnostic claims. Privacy: deidentified data under institutional DUAs; the on-device Gemma 4 plus LiteRT plus Flutter stack means voice and behavioral signals never leave the user's phone; membership-inference probes gate every release. Model and data cards ship with every release.

### Google.org Accelerator Participation (100 words)

We benefit most from Google's expertise in three areas. First, TPU optimization for graph networks plus LiteRT optimization for Gemma 4: graph diffusion wavelet kernels and on-device multi-agent inference both require Google-engineer-level acceleration to hit our latency and throughput targets. Second, large-scale data pipeline engineering: harmonizing 10,000-plus scans across formats and sites is where Google Cloud best practices reduce iteration cycles. Third, foundation model architecture guidance: extending AlphaGenome from GTEx tissue tracks to 24 BICCN brain cell types and porting graph foundation models from language and vision to brain connectome topology, where DeepMind's AlphaFold and AlphaGenome work is directly relevant.

## IV. Feasibility

### Organizational Positioning (150 words)

Cytognosis Foundation uniquely combines personnel with a published track record building molecular atlases of brain disease, existing consortium access to the datasets this project requires, and an institutional commitment to open release that ensures results drive distributed innovation.

Our PI led the first multi-cohort single-cell schizophrenia atlas (Ruzicka, Mohammadi et al., Science 2024), identifying continuous disease axes within a single DSM diagnosis: Neuroverse's direct scientific foundation. He co-led the first single-cell Alzheimer's atlas (Mathys, Davila-Velderrain, Mohammadi et al., Nature 2019) and contributed to the PsychENCODE capstone integrating 388 brains (Emani et al., Science 2024). These constitute molecular-scale proof that the dimensional axes this project maps at connectomic and cross-scale resolution are real and discoverable.

Our Co-Lead at Human Technopole bridges molecular and circuit neuroscience. Our Senior Advisor at Purdue directs the Institute for Physical AI, providing foundation-model and scalable-computing expertise. The team spans computational neuroscience, AI systems, and open-source infrastructure.

### AI Maturity

AI First.

### Technical Feasibility (100 words)

Our Science 2024 publication proved continuous disease axes are discoverable within single DSM diagnoses using single-cell transcriptomics, replicated across independent cohorts. The neuromaps atlas (Hansen et al., Nature Methods 2022) validates neurotransmitter receptor maps as reliable molecular priors. Grotzinger et al. (2025, Nature) independently confirmed five genomic factors explaining 66 percent of psychiatric genetic variance; Quah et al. (2025) showed data-driven neuroimaging bifactor models outperform theory-driven frameworks. A recent tau-PET imputation result (Nature Communications 2025) demonstrates the tractability of imaging-to-molecular cross-modal prediction. These convergent findings provide external validation benchmarks and confirm the multi-scale dimensional architecture our approach maps.

### Risk Management and Mitigation (200 words)

**Cross-site harmonization removes biological signal alongside scanner artifacts.** fMRIPrep / QSIPrep preprocessing plus an in-model learned harmonization layer preserves variance; learned axes must replicate on held-out sites; if not, site-aware architectures explicitly model site as a confound.

**Learned axes lack clinical meaning.** We require r > 0.5 against both HiTOP and Grotzinger 2026 five-factor on at least 3 of 5 / 6 dimensions before claiming validity; single-benchmark failures are flagged provisional and investigated.

**Cross-scale Genome-to-Connectome bridge underperforms.** PsychENCODE 388 paired donors anchor leave-one-individual-out validation; if AUC < 0.75, the cross-scale deliverable downgrades to a published negative result and Neuroverse v1.0 ships without the cross-scale claim.

**Demographic and equity bias in axis discovery and clinical inference.** PGC and HiTOP benchmarks were derived from primarily European-ancestry cohorts; learned axes may underperform on other ancestries. We anchor cross-ancestry validation on NeuroGAP-Psychosis (Ethiopia, Kenya, South Africa, Uganda), H3Africa genomics, and ABCD's stratified diverse-by-design sampling, with ancestry-disaggregated demographic-performance cards as a hard release-gate.

**DUA delays.** We prioritize open datasets (HCP, ABCD, OpenNeuro) for initial development; restricted sets (UKBB, PsychENCODE, ENIGMA) serve as validation. IRB initiates Month 1.

**Specialized hiring slips.** PI's 20-year ML engineering background sustains initial development independently; permanent hiring proceeds with a 3-month buffer.

### Key Team Members (100 words)

**PI: Shahin Mohammadi, PhD** (50%). 20 years in AI for biology (MIT, Broad, insitro, GenBio AI). Led single-cell atlases in Nature (2019) and Science (2024). Creator of ACTIONet.

**Co-Lead: Jose Davila-Velderrain, PhD** (advisory; Group Leader, Human Technopole). Co-developed PsychAD atlas (Science 2024); bridges molecular and circuit neuroscience.

**Clinical Collaborator: Brad Ruzicka, MD/PhD** (McLean Hospital / Harvard Medical School). HBTRC NeuroBioBank liaison; co-led the multi-cohort schizophrenia atlas (Science 2024). Anchors clinical validation and NBB cohort access.

**Senior Advisor: Ananth Grama, PhD** (8%; Distinguished Professor, Purdue; Director, Institute for Physical AI). Foundation-model architecture and scalable computing.

**AI / ML Engineer (hire, 100%):** geometric deep learning, graph diffusion wavelet implementation, AlphaGenome fine-tune, Gemma 4 LoRA plus DPO.

### Partner Organizations

**Partner 1: Human Technopole.** Website: https://humantechnopole.it. Role (50 words): Co-Lead Jose Davila-Velderrain provides cross-scale neuroscience expertise bridging molecular and circuit-level analysis, contributing directly to model design and the cross-scale Genome-to-Connectome validation. Human Technopole offers access to European cohorts, high-performance computing, and the European computational neuroscience network, enabling validation across diverse international scanner configurations. Status: Existing partner.

**Partner 2: Purdue University, Institute for Physical AI.** Website: https://www.purdue.edu/ipai/. Role (50 words): Senior Advisor Ananth Grama provides strategic guidance on foundation-model architecture, scalable computing optimization, and AI interpretability methods critical for biological applications. Purdue's IPAI offers high-performance computing infrastructure and a multidisciplinary network spanning AI, physics, and life sciences, strengthening the project's computational foundations and providing the redundant compute fabric our risk plan requires. Status: Existing partner.

**Partner 3: McLean Hospital / Harvard Medical School.** Website: https://www.mcleanhospital.org. Role (50 words): McLean Hospital, Harvard Medical School's largest psychiatric affiliate, provides clinical neuroscience expertise for validating dimensional axes against patient outcomes. As lead site of the Harvard Brain Tissue Resource Center (NeuroBioBank), McLean offers postmortem brain tissue and clinical data enabling molecular validation of connectomic findings and bridging imaging to cellular resolution. Status: Existing partner.

## V. Scalability

### Scalability Strategies Selected

Geographic transfer to new regions; sector adaptation to related fields; ecosystem integration with existing infrastructure; community-driven expansion; open-source adoption.

### Team Evolution for Scale (150 words)

Scaling from psychiatric connectomics to a disease-agnostic, multi-scale platform requires three expansions. First, domain scientists: extending to autoimmune (Year 4, via University of Manchester) and neurodegenerative indications requires immunologists and clinical neuroscientists at each frontier. Second, data engineers: 10,000 to 100,000-plus scans demands an infrastructure team (2 to 3 engineers) maintaining pipelines and standards conformance (BIDS, GA4GH VRS, Phenopacket, CELLxGENE / TileDB-SOMA). Third, community managers: 500-plus researchers requires developer relations, documentation, and training. Governance evolves: a Scientific Advisory Board (5 to 7 members from HiTOP, ENIGMA, PsychENCODE) plus an external Ethics Review Panel. The Helix Framework, an organizational-infrastructure recipe Cytognosis is co-developing with Astera Open Science, Convergent Research, and Speculative Tech, gives partner moonshots reusable scaffolding (federated DUAs, shared evaluation harnesses, common reproducibility tooling, licensing patterns) so cross-institution scaling is operational, not bespoke. Technical scaling proceeds via federated learning plus automated CI / CD toward a self-sustaining open-science ecosystem.

### Financial Sustainability (50 words)

ARPA-H Mission Office ISO submission (PHO or HSF) targets $20 to 30M for clinical-scale validation. NSF Tech Labs five-year center grant, independently or as a Cytognosis-Convergent-Research joint center, sustains the open infrastructure. A future public benefit corporation subsidiary may commercialize diagnostic applications atop the open core, never by closing it.

### Technical Sustainability (50 words)

Google.org funding establishes research-grade baselines: harmonized datasets, pretrained connectomic and cross-scale models, validated axes, and evaluation benchmarks. These open artifacts seed ongoing community work. Additional funding from ARPA-H, NSF, and NIH sustains active development, and open-source contributions through GitHub ensure the platform evolves beyond any single funding cycle.

### Knowledge Sharing and Learning (100 words)

Key learnings: (1) standards-conformant cross-site neuroimaging plus genomics plus single-cell plus phenotype harmonization, published as an open protocol with reusable BIDS, GA4GH VRS, Phenopacket, CELLxGENE plus TileDB-SOMA pipeline code; (2) evidence for or against recoverability of transdiagnostic axes at connectomic resolution and across the imaging-to-molecular bridge, published as preprints; (3) benchmarks comparing data-driven and theory-driven dimensional models against genomic ground truth as reproducible evaluation suites; (4) the Helix Framework cross-institution organizational-infrastructure recipe, co-authored with Astera. All preprints on bioRxiv. Quarterly technical blog posts. Annual OHBM and SfN workshops. Releases on GitHub and Hugging Face with full documentation.

### Public Visibility and Press

**Publications:** Ruzicka, Mohammadi et al. (Science 2024); Mathys, Davila-Velderrain, Mohammadi et al. (Nature 2019); Emani et al. incl. Mohammadi (Science 2024); 40-plus publications with 4,000-plus citations.

**Open-source tools:** ACTIONet (github.com / shmohammadi / ACTIONet, 500-plus stars), adopted by PsychENCODE and ROSMAP consortia.

**Conference presentations:** PsychENCODE annual meetings, ASHG, SfN, OHBM.

**Organization:** Cytognosis Foundation (cytognosis.org), 501(c)(3) nonprofit incorporated in Delaware, founded 2024.

## VI. Project Budget and Timeline

### Funding Request

**Amount Requested:** $2,500,000

### Budget Breakdown

The $2,500,000 budget is sized to deliver the harmonized roadmap: a Neuroverse v1.0 multi-scale foundation model release at Month 36, validated against two independent dimensional frameworks (HiTOP and Grotzinger 2026), with cross-scale connectomic-to-molecular bridging anchored on PsychENCODE 388 paired donors. Allocation: Personnel 70.0%, Compute and Data Infrastructure 12.8%, Technology Development and Equipment 4.3%, Project Amplification and Community 3.8%, Indirect 9.1%. The PI is budgeted at the discounted-fees tier ($165K/year, $13,750/month) per executed CEO Contractor Agreement effective 2025-10-01 (the full $270K/year tier requires $5M cumulative external funding, which Google.org's $2.5M alone does not reach); PI is a 1099 independent contractor without employer-paid fringe per Section 7 of the agreement. The split aligns with Google.org's typical impact-grant guidance (Personnel 60-75%, Indirect ≤ 10-12%) and with peer open-science research nonprofit benchmarks (e.g., comparable Chan Zuckerberg Initiative and Wellcome Leap awards). Specialized cross-scale and open-source roles join in later phases as the work composition shifts.

#### Category 1: Personnel and Staffing

**Total Allocation:** $1,750,500

**Description and Details (100 words):** PI 50% effort × 36m at $165K/year (discounted-fees consulting tier per executed CEO Contractor Agreement; full $270K/year tier requires $5M cumulative external funding which Google.org alone does not reach): $247.5K, 1099 contractor no fringe per agreement Section 7. Hire salaries benchmarked against 2026 SF Bay-area Pave / levels.fyi / BLS OEWS 15-2051 / 19-1042 nonprofit-adjusted; 30% fringe per HHS. AI / ML Engineer 100% 36m, $565K ($145K base; graph diffusion wavelets, AlphaGenome fine-tune, Gemma 4 LoRA + DPO, cross-scale fusion). RA1 Neuroimaging 100% 36m, $293K ($75K). RA2 Comp Neuro 100% 30m from M6, $228K ($70K). Multimodal Scientist 50% 18m from M18, $127K ($130K). Open-Source / Mobile Edge Engineer 50% 24m from M12, $150K ($115K). Purdue subaward (Grama) 8% 36m, $140K.

#### Category 2: Compute and Data Infrastructure

**Total Allocation:** $320,000

**Description and Details (100 words):** GCP TPU v4 / v5 across 36 months: approximately 160K chip-hours at effective $1.30 to $1.50 per chip-hour (basis: GCP list price $3.22 on-demand and $1.93 with 1-year commitment for v4, partially offset by Google.org Accelerator credits during Months 1-6) for graph-diffusion-wavelet training, AlphaGenome embedding generation across PsychENCODE 388 paired donors, cross-scale fusion, and inference at scale = $215K. Cloud storage at GCS Standard $0.020 per GB-month over ~100 TB active plus Coldline archival = $55K. GPU workstations (5x H100-class at $5K each, vendor list) = $25K. Restricted-data access fees (UK Biobank ~$15K, PsychENCODE secure-enclave ~$10K) = $25K. Total $320K, 12.8% of budget.

#### Category 3: Technology Development and Equipment

**Total Allocation:** $108,000

**Description and Details (100 words):** Wearable EEG / fNIRS headsets for the Month-18+ Meso-scale wearable-to-fMRI pilot (no physiology / HRV in Google scope; physiology lives in the Foresight track), basis published vendor list prices: 2x g.Nautilus ($34K), 3x Muse S Athena ($1.5K), 2x Emotiv EPOC X ($2K). Edge-deployment infrastructure: iOS plus Android test devices for the Flutter Neuroverse app, Apple Developer plus Google Play Console accounts, code-signing certificates ($5K). IRB submission via Salus IRB plus periodic amendments ($15K, basis: Salus published rate card). Legal counsel for DUAs, OpenRAIL-M license review, FAIR-compliance contracts ($20.5K, basis: ~100 hours at $200/hr). Open-source infrastructure (CI / CD, Hugging Face hosting, MkDocs / RO-Crate / Copier / SPDX, synthetic-data substitutes): $30K. Total $108K, 4.3% of budget.

#### Category 4: Project Amplification and Community

**Total Allocation:** $95,000

**Description and Details (100 words):** Travel to scientific conferences (OHBM, SfN, NeurIPS, Hugging Face Open Source AI, ASHG) for dissemination and community building: $20K per year x 3 years = $60K (basis: GSA federal per-diem rates plus published conference registration fees). Collaborator exchange visits (Human Technopole Milan, Purdue West Lafayette, McLean Boston) included. Workshop hosting at OHBM 2029 ($10K, basis: prior OHBM workshop budgets). Lived Experience Advisory Council compensation: $200 per meeting x 12 members x 12 quarterly meetings = $28.8K, $25K budgeted with partner contributions balancing (basis: published patient-advisory council compensation guidelines, e.g., PCORI). Total $95K, 3.8% of budget; community amplification ensures findings reach patient-advocacy organizations.

#### Category 5: Indirect Costs

**Total Allocation:** $226,500

**Description and Details (100 words):** Organizational overhead at approximately 10 percent of total direct costs ($2,273.5K). Covers shared organizational infrastructure: office space, insurance, accounting, legal compliance, IT security, and administrative support. Cytognosis Foundation maintains a lean operational model as a 501(c)(3) nonprofit with no federally negotiated indirect rate; the 10 percent rate reflects actual administrative burden and remains within Google.org's 10 to 12 percent guideline. This lean structure ensures approximately 91 percent of Google.org's investment flows directly into research personnel, compute, equipment, and community engagement that advance the project's scientific and public-benefit mission.

### Project Timeline and Milestones

The five milestones build the platform progressively: open multi-site data substrate; continuous phenotypic coordinate backbone; healthy connectomic foundation model; disease-aware connectomic foundation model with cross-disorder dimensional validation; and the multi-scale Neuroverse v1.0 release with Genome-to-Connectome cross-scale bridging. Every milestone carries a primary external benchmark, a NeuroBioBank-internal replication metric where applicable, and a pre-registered Go / No-Go decision rule.

#### Milestone 1: Open Multi-Site Atlas and Compute Substrate

**Timeframe:** Months 1 to 3

**Activities (150 words):** Hire AI / ML Engineer and RA1 (M1 to 3). Initiate IRB through Salus IRB. Stand up the four-modality data substrate: BIDS-standard FAIR neuroimaging repositories via fMRIPrep / QSIPrep across HCP, ABCD, OpenNeuro, ENIGMA (SZ, BD, MDD, PTSD, OCD) and ABCD plus NeuroGAP-Psychosis for cross-ancestry coverage; GA4GH VRS / VRS-Cat-normalized variants in TileDB-VCF for PsychENCODE WGS; extended CELLxGENE schema in TileDB-SOMA for single-cell with cell-type-ontology cross-mapping; GA4GH Phenopacket-conformant phenotype records. Configure TPU v4 / v5 plus AnnData / Zarr distribution. Integrate neuromaps (19 PET-derived neurotransmitter maps) and Allen Human Brain Atlas regional expression as molecular priors. Publish quality-control protocols: artifact detection, demographic-balance audits, site-effect quantification, harmonization-v1 report. Begin Google.org Accelerator engagement (2 to 4 hours / week, two team members) focused on TPU sparse-graph kernels, LiteRT preparation, and data-pipeline engineering.

**Outcomes / Key Milestones (100 words):** Fully staffed core team (PI, AI / ML Engineer, RA1) operational. Four-modality FAIR data substrate live: BIDS imaging at over 3,000 scans across 4-plus disorders; GA4GH-VRS variants in TileDB-VCF; CELLxGENE schema plus TileDB-SOMA single-cell store; GA4GH Phenopacket phenotype records. Quality-control pipeline with documented site-effect metrics. TPU training environment benchmarked. IRB approved or in final review. Accelerator engagement producing initial TPU optimization gains. Wearable inventory acquired. **First release of harmonized, FAIR-compliant, standards-conformant datasets and the harmonization-v1 report under CC BY 4.0**, anchoring every downstream model release. Identical 3-month substrate deliverable shared word-for-word with Astera Round-2.

#### Milestone 2: Continuous Phenotypic Coordinate Backbone (Disease-and-Phenotype Semantic Embedding Space)

**Timeframe:** Months 3 to 6

**Activities (150 words):** Build the disease-and-phenotype semantic embedding space and knowledge graph. Curate uPheno and HP using Protégé and ROBOT to integrate EL++ axioms and sub-ontologies from neuro-specific source ontologies (NBO, NIFSTD, MFO, MFOMD, CogPO, Cognitive Atlas, MFOEM, ASDPTO, and others) covering neuro-behavioral terms not yet captured. Embed the unified EL++ ontology stack (GO-Plus with its UBERON and Cell Ontology subsumptions; HP; uPheno-extended; MONDO; DOID; SNOMED CT) into one shared semantic space using a geometric description-logic embedding method (specific candidates include TransBox alongside other EL++-respecting embedding families benchmarked in parallel), validated via standard EL++-embedding metrics (link-prediction, concept-similarity, refinement-consistency). Generate SSSOM cross-mappings linking every embedded ontology plus the non-EL++ vocabularies (UMLS, ICD-10 F and G), leveraging OLS4 plus Cytognosis-curated mappings. Map ENIGMA diagnostic labels and the Grotzinger 2026 14-disorder PGC set into the embedding space. Validate against Grotzinger five-factor and HiTOP. Launch Lived Experience Advisory Council. Begin the AlphaGenome cell-type fine-tune via the genomicsxai PyTorch port as the cross-scale molecular encoder.

**Outcomes / Key Milestones (100 words):** **First open release of the disease-and-phenotype semantic embedding space and knowledge graph (v1.0).** Pretrained EL++ ontology embeddings (CC0 weights, Apache 2.0 code) over the unified stack (GO-Plus, HP, uPheno-extended, MONDO, DOID, SNOMED CT). SSSOM cross-mappings to UMLS, ICD-10 F-G, and across ontologies, leveraging OLS4. Curated uPheno extension contributed upstream to the OBO Foundry. Validation report: disease-level Frechet means match PGC five-factor and at least 3 of 5 / 6 HiTOP dimensions at r > 0.5; embedding link-prediction and concept-similarity meet pre-registered thresholds. Lived Experience Advisory Council convened. Bias-audit framework v1 with demographic performance cards. Identical 6-month deliverable shared word-for-word with Astera Round-2.

#### Milestone 3: Multi-Resolution Connectomic Foundation Model, Healthy Baseline

**Timeframe:** Months 6 to 12

**Activities (150 words):** Hire Research Associate 2 (computational neuroscience) at Month 6. Implement multi-resolution graph diffusion wavelets (Coifman 2006) with cross-resolution attention on the full brain graph, with specific candidate algorithms including WaveGC and related wavelet-GNN variants; parcellation atlases (Schaefer, AAL, Brainnetome, Glasser-360) inject as node attributes. Train on more than 5,000 harmonized cross-disorder fMRI scans from the open substrate. Integrate the 19 neuromaps PET-derived neurotransmitter maps and Allen Human Brain Atlas regional expression as learnable molecular constraints, ensuring learned axes reflect neurobiology rather than scanner artifacts. Replace ComBat with an in-model learned harmonization layer that preserves biologically meaningful variance. Run systematic ablations: multi-resolution wavelets versus standard single-resolution GNN baselines (BrainNetCNN, BrainGNN), with versus without neurotransmitter priors, single-disorder versus cross-disorder regimes. Continue Accelerator engagement on distributed TPU strategies. Submit first preprint to bioRxiv documenting the harmonization pipeline, the wavelet architecture, and preliminary axis discovery.

**Outcomes / Key Milestones (100 words):** **First open release of the multi-resolution connectomic foundation model**, trained on more than 5,000 harmonized cross-disorder scans, with neuromaps PET priors and Allen Human Brain Atlas regional features. Initial transdiagnostic axes identified and visualized. Ablation results quantify the contribution of (a) multi-resolution wavelets over single-resolution GNNs, (b) neurotransmitter priors over unconstrained models, and (c) cross-disorder versus single-disorder regimes. Preprint submitted to bioRxiv. Full team (PI, AI / ML Engineer, RA1, RA2) operational. Aging-signature recovery validated on the cohort age range as a sanity check. Cross-site held-out generalization metrics published.

#### Milestone 4: Disease-Aware Connectomic Foundation Model with ENIGMA Cross-Disorder Validation

**Timeframe:** Months 12 to 18

**Activities (150 words):** Fine-tune the connectomic foundation model on disease-anchored cohorts via ENIGMA federated queries across SZ, BD, MDD, PTSD, OCD, autism, ADHD working groups. Validate learned axes against two independent external frameworks: (1) HiTOP dimensional spectra (Internalizing, Thought Disorder, Disinhibited Externalizing, Antagonistic Externalizing, Detachment, Somatoform), and (2) the Grotzinger 2026 five-factor genomic architecture across 14 disorders (Compulsive, Schizophrenia-Bipolar, Neurodevelopmental, Internalizing, Substance Use). Test cross-site generalization by holding out entire sites during training. Run NeuroBioBank-internal replication on the McLean MRI overlap with HBTRC postmortem data: recompute learned axes on NBB samples aggregated by the same 14 PGC diagnoses; require directional agreement and within-bound effect-size recovery for the NBB-internal HiTOP correlations. Initiate UK Biobank imaging access (50,000-plus scans) for large-scale replication. Apply the bias-audit framework, publishing demographic-performance cards. Submit first peer-reviewed manuscript and preprint.

**Outcomes / Key Milestones (100 words):** **Go / No-Go decision recorded:** learned axes correlate with both HiTOP and the Grotzinger five-factor structure at r > 0.5 on at least 3 of 5 / 6 dimensions, with NBB-internal replication confirming the signal recovers on independent NBB samples. Cross-site generalization metrics published, confirming biological rather than scanner-specific signal. **Open-source release v1.0** on GitHub and Hugging Face: harmonized data (where DUA permits), pretrained disease-aware connectomic foundation model checkpoints, evaluation benchmarks, model and data cards, demographic-performance cards. Initial wearable-to-fMRI correlation pilot data collected on internal team members (3 to 5 people) as the cross-scale pilot ramps up.

#### Milestone 5: Neuroverse v1.0, Multi-Scale Foundation Model and Open Community Platform

**Timeframe:** Months 18 to 36

**Activities (150 words):** Anchor the cross-scale Genome-to-Connectome bridge: integrate PsychENCODE 388 paired WGS plus single-cell transcriptomes; develop cross-modal predictors via leave-one-individual-out validation; report tau-PET-imputation analog as the cross-modal feasibility benchmark. Fuse per-scale models into Neuroverse v1.0: per-scale encoders plus cross-scale attention with subspace-alignment regularization across the three coordinate subspaces; train on paired plus unimodal sets via modality-dropout. Build the Neuroverse edge layer: fine-tune Gemma 4 via LoRA plus DPO into the on-device interviewer voice agent and the supervisor thinking agent, deployed via LiteRT, with Flutter shipping the multi-agent stack to phones, exercising the layered three-tier privacy architecture end-to-end. Run a 15 to 20-participant external pilot (MDD, GAD, schizophrenia, controls) on the full stack. Scale repository past 10,000 scans via UK Biobank integration. Host the Neuroverse OHBM 2029 workshop. Submit ARPA-H PHO and NSF Tech Labs follow-ons.

**Outcomes / Key Milestones (100 words):** **Neuroverse v1.0 released as an open multi-scale foundation model and community platform.** Cross-scale validation: predicting molecular subtype from connectome alone reaches AUC at least 0.75 on PsychENCODE 388 paired held-out donors. **Neuroverse edge layer** ships as the Gemma 4 fine-tuned interviewer plus supervisor multi-agent stack on LiteRT inside a Flutter app, with sub-300ms speech latency, accuracy within 95 percent of cloud Neuroverse inference, and zero raw-signal egress. Repository exceeds 10,000 scans across 8-plus disorders. Demographic-performance cards published with ancestry-disaggregated metrics anchored on NeuroGAP-Psychosis. Over 1,000 unique downloads; over 50 institutions; 3 to 5 publications. ARPA-H and NSF follow-ons submitted.

## Notes on revision scope

This v2 revision rewrites the milestones (Section VI Project Timeline), the budget (Section VI Budget Breakdown), the technology stack and custom-solution sections (Section III), and the dataset, ethics, and Accelerator answers. It carefully refines (a) the proposed-solution and tools-methods narratives to reflect the multi-scale Neuroverse v1.0 endpoint at Month 36, (b) the success metrics and failure indicators to cover the new cross-scale bridge, (c) the technical-feasibility and risk-management text to map onto the new milestones, and (d) the team-evolution and partner narratives to reference the new role timing (Multimodal / Cross-Scale Scientist joining at Month 18, Open-Source / Mobile Edge Engineer joining at Month 12). The v2.1 update threads the AlphaGenome (Google DeepMind) anchor through Tools / Methods, Custom Solution, and Accelerator; adds NeuroGAP-Psychosis and H3Africa as cross-ancestry validation cohorts; adds a sixth risk on demographic and equity bias; and integrates the Neuroverse edge layer (Gemma 4 fine-tuned via LoRA plus DPO, deployed via LiteRT, with a Flutter user-facing app implementing the layered multi-agent supervisor-and-interviewer architecture) as a named Milestone 5 deliverable. The v2.2 update adds (a) explicit data-standards conformance (BIDS for neuroimaging, GA4GH VRS / VRS-Cat plus TileDB-VCF for genomics, GA4GH Phenopacket for phenotypes, extended CELLxGENE schema plus TileDB-SOMA for single-cell) to Milestone 1; (b) the disease-and-phenotype ontology backbone (MONDO, DOID, HP, uPheno, with Cytognosis-led extensions cross-mapped to UMLS, SNOMED CT, and ICD-10 chapters F and G) to Milestone 2; (c) NSF Tech Labs (independently or as a Cytognosis-Convergent-Research joint center) and ARPA-H Mission Office ISO (PHO or HSF) framing to Financial Sustainability; (d) the Helix Framework cross-institution organizational-infrastructure recipe, co-developed with Astera Open Science, Convergent Research, and Speculative Tech, as a deliverable in Team Evolution and Knowledge Sharing. The v2.3 update reframes Milestone 2 as the disease-and-phenotype semantic embedding space and knowledge graph rather than a flat ontology list: we curate and extend uPheno and HP using Protégé and ROBOT to integrate EL++ axioms drawn from a long list of neuro-specific source ontologies (NBO, NIFSTD, MFO, MFOMD, CogPO, Cognitive Atlas, MFOEM, ASDPTO, COGITO, NIO, ONTOPSYCHIA, and others) rather than embedding each ontology directly; we then TransBox-embed the unified EL++ ontology stack (GO-Plus, which already subsumes UBERON and Cell Ontology, alongside HP, uPheno-extended, MONDO, DOID, and SNOMED CT) into one shared semantic space, validated using TransBox-paper metrics; cross-mappings across embedded ontologies plus the non-EL++ vocabularies (UMLS, ICD-10 F and G) are produced as SSSOM (Simple Standard for Sharing Ontological Mappings) artifacts leveraging OLS4 (Ontology Lookup Service v4) cross-references where they exist and Cytognosis-curated mappings where they do not; the curated uPheno extension is contributed upstream to the OBO Foundry community. The detailed AlphaGenome fine-tuning specification (TransBox-conditioned ontology embeddings replacing variantFormer's free-parameter tissue tokens, two-phase BICCN curriculum, scDesign3 vine-copula optional decoder, MAE / RMSE baseline plus cosine-similarity / hypergeometric-sign-consistency stretch metrics) is captured in the standalone AlphaGenome_FineTuning_Technical_Spec.md document and summarized in proposal-track form in Tools / Methods, Custom Solution, and Milestone 5. The 3-month M1 substrate and 6-month M2 phenotypic-backbone deliverables share word-for-word language with the Astera Round-2 response so the jointly-produced substrate is unambiguously single-funded and reusable across both tracks. Word counts respect the original application limits. Cytognosis brand voice rules apply throughout.

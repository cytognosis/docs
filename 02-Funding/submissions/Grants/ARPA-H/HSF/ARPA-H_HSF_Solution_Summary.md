# ARPA-H Solution Summary: Health Science Futures (HSF) Mission Office

**Submission target:** ARPA-H Health Science Futures (HSF) Mission Office ISO, ARPA-H-SOL-24-104
**Format note:** Transfer this content into the Appendix A Solution Summary template (sans serif, 11 pt minimum) before submission. Delete all template guidance (blue) text. Body Sections 1 to 5 must fit six (6) pages; the cover page, sub-awardee table, and citations do not count toward the limit.

---

## COVER PAGE (excluded from page count)

| Field | Entry |
|---|---|
| ISO title | Health Science Futures Mission Office ISO (ARPA-H-SOL-24-104) |
| Solution title | Psychoverse: A Multiscale Genomic-Connectomic Biotyping Platform to Resolve Individual Variation in Mental Health and Treatment Response |
| Submitter organization | Cytognosis Foundation |
| Organization type | Non-Profit, 501(c)(3) |
| Technical POC | Shahin Mohammadi, PhD, Founder and CEO; [address]; [phone]; mohammadi@cytognosis.org |
| Administrative POC | [Name]; [address]; [phone]; [email] |
| Estimated project duration | 60 months |
| Total basis of estimate | $33.0M (ARPA-H request ~$29.0M; proposed resource sharing ~$4.0M) |
| Place(s) of performance | San Francisco Bay Area, CA; clinical sites (Boston, MA; New York, NY) |

**Sub-Awardee and Consultant Team Members (excluded from page count)**

| Organization | Technical POC | Organization type |
|---|---|---|
| Deep-tissue optical spectroscopy company (stealth; Marie-Nelly) | Hervé Marie-Nelly, PhD | For-Profit |
| McLean Hospital / Harvard Medical School | Brad Ruzicka, MD, PhD | Academia / Hospital |
| Icahn School of Medicine at Mount Sinai | [Clinical PI] | Academia / Hospital |
| Patient Advocacy Council (One Mind; Center for Digital Mental Health, Harvard/MGH; APA Council on Digital Health; ASAM) | [Council Chair] | Non-Profit |

---

## 1. Concept Summary

Psychiatry still defines illness by symptom checklists. Two people who carry the same DSM label often have different underlying biology, which is why first-line treatments fail 47 to 58 percent of the time and care proceeds by trial and error. Cytognosis Foundation will build **Psychoverse**, a measurement and AI platform that replaces categorical labels with continuous, biologically anchored coordinates. The platform integrates three scales that today live in separate silos: the genome, the brain connectome, and continuous behavior. From these it learns transdiagnostic axes that place each person at a precise location in a shared "map" of mental health, and it tracks movement along those axes over time.

This directly answers the HSF interest area in "technologies that expand the precision, scale, and accessibility of brain circuit mapping technologies that enable causative neuropsychiatric links to mental health disorders leading to definitive diagnosis and reliable therapeutic monitoring." Two capabilities make the map causal rather than descriptive. First, the platform disentangles the part of each connectomic signature that is driven by inherited genotype from the part driven by the exposome (lived environment), so clinicians can separate stable biology from modifiable history. Second, it translates coordinates learned from research-grade imaging onto wearable sensors (optical, electrophysiological, and voice), so individual variation can be measured continuously outside the clinic, which is the Cytognosis mission of detecting and intercepting disease years before symptoms become disabling.

The work is deliberately complementary to ARPA-H's EVIDENT program. EVIDENT generates objective response data for rapid-acting treatments such as neuroplastogens and neuromodulation, but its solicitations list genotype, neurotrophic factors, and network connectivity only as "data of interest" and fund no framework to integrate them. Psychoverse is that framework: the biotyping layer that explains who responds to a given rapid-acting treatment and why. EVIDENT measures the response; we map the person.

## 2. Innovation and Impact

**Problem and limits of current practice.** Mental disorders are now the leading global contributor to years lived with disability, with 1.17 billion people affected (GBD 2023, Lancet 2026). Suboptimal therapy costs an estimated $528B annually in the United States. The root cause is mechanistic: the DSM collapses biological heterogeneity into population averages, so STAR*D relapse climbed from 40 to 71 percent across treatment steps. Four gaps follow. (1) Diagnosis is categorical, not dimensional. (2) Genomics and connectomics are modeled in isolation, so no platform separates heritable from environmentally driven brain signatures. (3) Measurement is episodic, captured in brief clinic visits rather than continuously. (4) Treatment selection is trial and error, because no deployed system predicts individual response from biology.

**What is new.** Psychoverse advances five capabilities beyond the state of the art. First, it learns continuous transdiagnostic axes from pairwise genomic-connectomic geometry rather than from DSM supervision, so it does not inherit the heterogeneity it is trying to resolve. Second, it explicitly decomposes connectomic variance into a genotype-aligned component (anchored by polygenic risk scores and heritability priors) and an exposome-aligned residual, validated on family and longitudinal cohorts. Third, it aligns genotype, connectome, and behavior into a single model using paired-modality bridge datasets (for example ENIGMA imaging with genotypes, and PsychENCODE single-cell data with genotypes), rather than concatenating unaligned features. Fourth, it ports coordinates from research-grade functional MRI onto wearable optical, EEG, and voice sensors through a biotype-driven forward model. Fifth, it produces the first multimodal, multiscale, longitudinal dataset of this kind at scale, which becomes durable national infrastructure regardless of any single clinical result.

**Why now, and why us.** Three external advances converge. Grotzinger et al. (Nature 2025) showed that 66 percent of cross-disorder psychiatric genetic variance reduces to a five-factor structure, giving an external anchor for our axes. Biotype-matched intervention nearly doubled depression remission from 30 to 55 percent (iMAP; Williams, Tozzi et al., NPP Digital Psychiatry and Neuroscience 2026). The April 2026 Executive Order on Accelerating Medical Treatments for Serious Mental Illness directs ARPA-H to invest in psychedelic and neuroplastogen therapies and to expand data sharing and real-world evidence; biotyping is the missing layer that makes that acceleration precise. The PI co-led the first multi-cohort single-cell atlas of schizophrenia (Science 2024) and contributed to the PsychENCODE capstone (Science 2024) and the first single-cell study of Alzheimer's disease (Nature 2019), establishing the molecular foundation the platform builds on.

**Quantitative targets.**

| Metric | Current state of the art | Year 1 | Year 2 | Year 3 | Proposed outcome (M60) |
|---|---|---|---|---|---|
| Diagnostic unit | DSM categories | Continuous coordinates, 5 disorders | 10+ disorders | Transdiagnostic axes validated vs. HiTOP / Grotzinger (r > 0.5 on >= 3 of 5 dimensions) | Continuous biotype coordinates that complement and begin to replace DSM in research and trial use |
| Scales integrated in one model | Single modality (imaging or genomics) | Connectome foundation model (fMRI) | + genotype alignment on bridge cohorts | + behavior / wearable layer | Genotype to connectome to behavior to wearable, jointly modeled |
| Exposome vs. genotype decomposition | None | Method prototyped | Validated on family / longitudinal cohorts | Quantified per axis | Per-individual heritable vs. exposomic connectomic decomposition |
| Continuous measurement | Episodic clinic visits | fMRI-anchored | fNIRS forward model | Wearable pilot | Continuous at-home multimodal monitoring |
| Treatment-response stratification | Trial and error (47 to 58% fail) | Retrospective biotype-response association | Prospective hypotheses (e.g., bipolar mood biotype to neuroplastogens) | Clinical-cohort test | Biotype-matched response prediction; remission target ~30% toward ~55%+ |

**Impact.** If the map is sensitive to individual variation, every downstream actor benefits: clinicians gain a biological basis for treatment selection, trialists (including EVIDENT performers) gain a stratifying variable that explains response heterogeneity, and people in care gain continuous insight instead of waiting for the next crisis. The end state is a measurement standard that complements and, over time, can replace categorical diagnosis, delivered with the openness and patient governance that keep it a public good.

## 3. Proposed Work

**Final deliverables.** (1) Psychoverse v1.0: an open, multiscale foundation model mapping genotype, connectome, and behavior to continuous transdiagnostic coordinates, with per-individual exposome-vs-genotype decomposition. (2) A validated wearable translation stack that reproduces map coordinates from optical, EEG, and voice sensors, with quantified accuracy and characterized depth limits. (3) The first multimodal, multiscale, longitudinal clinical dataset linking biotype coordinates to rapid-acting treatment response. (4) An FDA regulatory package (De Novo strategy) and an openly released biotype taxonomy.

**Phased plan and key milestones.**

*Phase 1, Build the map (M1 to M36).* Train the connectome model using multi-resolution graph diffusion wavelets and graph neural networks over million-node whole-brain functional graphs, harmonized across HCP, UK Biobank, ABCD, ENIGMA, and OpenNeuro. Anchor axes to neurobiology with molecular priors (neuromaps, PET receptor maps, Allen Human Brain Atlas). Build the phenotype backbone from geometric ontology embeddings, and align a genomic encoder through cross-resolution attention on paired-modality bridge datasets. Milestones: M12 connectome model v0.5 (5 disorders); M24 genotype-connectome alignment on bridge cohorts; M36 map v1.0 with biotype taxonomy validated against HiTOP and Grotzinger axes and against the PI's single-cell atlases. A featured Phase 1 result: our in-progress single-cell and genomic analysis of bipolar disorder resolves two biotypes, a "thought" biotype whose genetics align with schizophrenia (shared schizophrenia-bipolar genomic factor; CACNA1C, ANK3, excitatory-neuron biology) and a "mood" biotype that overlaps major depression and shows BDNF dysregulation. Because BDNF-dependent neuroplasticity is the convergent mechanism of the neuroplastogens EVIDENT studies, this yields a falsifiable, mechanistically grounded prediction: the mood biotype should respond to rapid-acting neuroplastogens, the thought biotype should not.

*Phase 2, Regulatory and preclinical (M36 to M42).* File an FDA Q-Submission with a De Novo strategy, complete analytical validation of coordinate estimation, and validate the wearable forward model that translates fMRI-derived coordinates to functional near-infrared spectroscopy (fNIRS). Characterize and correct for modality differences, including the 3 to 4 cm optical depth limit that constrains readout of deep regions such as subgenual cingulate and ventral striatum.

*Phase 3, Clinical validation and at-scale data (M42 to M60).* Run clinical studies using wearable forms of each modality: time-domain fNIRS with diffuse correlation spectroscopy for cortical hemodynamics and metabolism, the Marie-Nelly ultrasound-aided optical module for depth to 2 to 3 cm, an optional low-channel EEG layer for excitation-inhibition balance, and an on-device voice and speech mood tracker. The trials serve three purposes: identify and adjust for differences between modalities (including fNIRS depth limits) so wearable coordinates match the imaging ground truth; test whether map coordinates track individual variation in response to rapid-acting treatments, using EVIDENT's rapid-acting-only design as a clean, fast-readout test bed; and assemble the first multimodal, multiscale dataset at this scale to retrain and sharpen the clinical models continuously. The Patient Advocacy Council (One Mind; the Center for Digital Mental Health at Harvard/MGH; the APA Council on Digital Health; ASAM) sets release gates, pressure-tests outputs with the communities they represent, and disseminates validated tools.

**Technical approach and supporting evidence.** The architecture reuses validated components (graph diffusion wavelets, ontology embeddings, edge inference via compact on-device models) and is grounded in the PI's published multi-scale atlases and in the external five-factor genomic result. Privacy is built in: voice and behavioral inference runs on-device, and raw signals are never centralized.

**Alternatives considered.** Single-modality models (imaging-only or genomics-only) cannot separate heritable from exposomic signal and were rejected. DSM-supervised models reproduce the heterogeneity problem and were rejected. A purely research-grade imaging endpoint was rejected because it cannot scale to continuous monitoring; hence the wearable translation layer.

**Adoption challenges.** Optical depth limits constrain deep-structure readout; we mitigate with the Marie-Nelly depth-zoom module, OPM-MEG and fMRI reference anchoring, and biotype-driven optode targeting. Melanin and skin-tone optical bias is a documented equity risk, mitigated with short-separation reference channels and explicit equity validation. Clinical trust is built through clinician co-development at McLean and Mount Sinai and Council governance.

**Key technical risks and mitigations (Plan B).** If cross-modal alignment underperforms, we fall back to per-scale models with late fusion, preserving each scale's standalone value. If wearables cannot resolve deep biotype regions, we use cortical proxies plus the EEG excitation-inhibition axis and the depth-zoom module. If biotypes do not predict treatment response, the validated map and the first at-scale multimodal dataset remain durable infrastructure, de-risking the program's core deliverable independent of the clinical hypothesis.

**Transition and commercialization.** At M42, when clinical data generation begins, the program bifurcates. All clinical-trial data and all models trained on it are owned by Cytognosis Foundation, which keeps the core map and taxonomy open. The Foundation then licenses sensor and device intellectual property to an impact-aligned for-profit (public benefit corporation) arm that manufactures the wearable Psychoscope sensors and earns revenue through device sales and subscriptions, following an open-core model comparable to OpenBCI. This keeps the scientific map a public good while giving the hardware a self-sustaining path to scale and to the population reach the Executive Order envisions.

## 4. Team Organization and Capabilities

**4.1 Roles and responsibilities.** Cytognosis Foundation is the prime, responsible for the Psychoverse model, biotype discovery and validation, the exposome-genotype decomposition, regulatory strategy, data governance, and open release. A stealth deep-tissue optical company (Marie-Nelly) provides the depth-zoom sensing module under a perpetual, royalty-free license to the Foundation for mental-health use. Clinical partners at McLean and Mount Sinai design and run validation protocols and host the wearable studies. The Patient Advocacy Council governs release gates, equity review, and dissemination.

**4.2 Key personnel.**

| Name | Position | Institution | Skills and experience |
|---|---|---|---|
| Shahin Mohammadi, PhD | Founder and CEO; PI | Cytognosis Foundation | Co-first author on the first multi-cohort single-cell atlas of schizophrenia (Science 2024) and the bipolar atlas (Eur. Neuropsychopharmacology 2024); contributor to the first single-cell Alzheimer's study (Nature 2019) and PsychENCODE; built ACTIONet; 20 years in multi-scale brain mapping and AI for biological systems. |
| Hervé Marie-Nelly, PhD | Co-PI, sensing hardware | Deep-tissue optical company (stealth) | Demonstrated noninvasive single-cell-class optical spectroscopy at 2 to 3 cm depth in adult tissue; hardware team with prior Openwater and Kernel experience. |
| Ananth Grama, PhD | Senior Scientific Advisor | Purdue University, Institute for Physical AI | Advises on graph learning and large-scale AI architecture; 16-year collaboration with the PI. |
| Brad Ruzicka, MD, PhD | Co-Lead | McLean Hospital / Harvard Medical School | Co-first author with the PI on the single-cell schizophrenia atlas (Ruzicka, Mohammadi et al., Science 2024); Assistant Professor; Harvard Brain Tissue Resource Center / NeuroBioBank liaison; anchors clinical validation, the IRB pathway, and clinical ground truth. |

**Why this is not a fit for a conventional research organization.** The platform requires industrial-scale integration of genomics, connectomics, sensor engineering, edge AI, regulatory science, and patient governance under one open, mission-locked roof. Academia lacks the engineering capacity, and industry is structurally incentivized toward closed, single-modality products. A nonprofit prime with a licensed commercial arm is the structure ARPA-H is positioned to enable.

## 5. Basis of Estimate (BOE)

**5.1 Cost narrative.** The estimate covers a 60-month program across three phases. Phase 1 (M1 to M36, ~$16.0M) funds the multiscale model build: high-performance compute and TPU training, machine-learning and computational-neuroscience labor, data harmonization and licensing, and genomic integration. Phase 2 (M36 to M42, ~$3.0M) funds regulatory science (FDA Q-Submission, analytical validation) and wearable forward-model validation. Phase 3 (M42 to M60, ~$14.0M) funds clinical studies and site costs, wearable hardware development including the optical depth-zoom module, clinical machine-learning labor, data infrastructure, and Patient Advocacy Council operations. Costs include direct labor, materials and supplies, compute and equipment, clinical and IRB costs, travel, and indirect costs. The budget is sized to the technical risk of the program rather than to a conservative floor.

**5.2 BOE summary.**

| Basis of Estimate (BOE) | Amount |
|---|---|
| Total project cost | $33.0M |
| Resource sharing (in-kind compute, licensed optical IP, philanthropic co-funding) | $4.0M |
| ARPA-H request | $29.0M |

---

## Citations (excluded from page count)

1. Ruzicka WB, Mohammadi S, et al. Single-cell multi-cohort dissection of the schizophrenia transcriptome. *Science* 384(6698), 2024.
2. Emani PS, et al. (PsychENCODE Consortium). Single-cell genomics of the human brain. *Science* 384(6698), 2024.
3. Mathys H, Davila-Velderrain J, ..., Mohammadi S, et al. Single-cell transcriptomic analysis of Alzheimer's disease. *Nature* 570:332-337, 2019.
4. Grotzinger AD, et al. Mapping the genetic landscape across 14 psychiatric disorders. *Nature*, DOI 10.1038/s41586-025-09820-3, 2025.
5. GBD 2023 Mental Disorders Collaborators. Global prevalence and burden of mental disorders, 1990-2023. *The Lancet*, DOI 10.1016/S0140-6736(26)00519-2, 2026.
6. Williams LM, Tozzi L, et al. Personalized machine-learning-guided intervention for depression (iMAP). *NPP Digital Psychiatry and Neuroscience*, 2026.
7. Nan J, et al. Personalized machine-learning guided intervention for lifestyle optimization in depression: a pilot study. *NPP Digital Psychiatry and Neuroscience* 4:10, 2026.
8. Cole EJ, et al. Stanford Neuromodulation Therapy (SAINT) for treatment-resistant depression. *Am J Psychiatry*, 2022.
9. Rush AJ, et al. STAR*D treatment outcomes. *Am J Psychiatry*, 2006.
10. Executive Order, Accelerating Medical Treatments for Serious Mental Illness, April 18, 2026.
11. ARPA-H EVIDENT program solicitations (ARPA-H-CXHUB-26-109; -26-110).
12. ARPA-H Health Science Futures Mission Office ISO (ARPA-H-SOL-24-104).

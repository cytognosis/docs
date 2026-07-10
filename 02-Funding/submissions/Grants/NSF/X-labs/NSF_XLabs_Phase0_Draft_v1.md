# Psychoscope: An Adaptive Spectroscopy Platform for Personalized Mental Health Sensing

**Lead Organization: Cytognosis Foundation (501(c)(3))**

**Topic 2: Scientific Instrumentation for Sensing and Imaging**

Written Proposal to the NSF X-Labs Initiative, Phase 0

<!-- FORMATTING: 8 single-sided pages, 12pt, single-spaced, 1" margins, 8.5x11. COI is a separate PDF. Tables may use smaller font. -->

---

## 1. Mission

### 1.1 Vision Statement

Build the first wearable platform that places each person on a continuous mental-health coordinate spanning the major psychiatric disorders, then zooms into the specific brain circuits and connections that define their condition, at cellular-scale resolution, longitudinally, and at consumer cost. We call this instrument **Psychoscope**. It is the sensor layer of a "GPS for mental health": a system that detects deviations from a person's healthy trajectory years before psychiatric symptoms become disabling, and that tells closed-loop neuromodulation where to act. The coordinate is grounded in a transdiagnostic evidence base we assembled across 14 disorders and three measurement scales (molecular, connectomic, phenotypic), so the platform reads the same shared circuits that recur across diagnoses rather than chasing one disease label at a time. We exist so no one else waits decades for answers.

### 1.2 Platform Technology

Psychoscope is an adaptive multi-chromophore optical spectroscopy headset. It integrates three sensing layers that no commercial system currently combines:

1. **Coarse whole-cortex mapping** via high-density time-domain functional near-infrared spectroscopy (TD-fNIRS) plus diffuse correlation spectroscopy (DCS), measuring hemodynamics, mitochondrial cytochrome-c-oxidase, and cerebral blood flow at 1-second resolution across the cortex (Tachtsidis 2025; Eggebrecht 2014).
2. **Biotype-driven target selection** on the Psychoverse (the mental-health coordinate map), a foundation-model representation built across the three RDoC-style scales (molecular, connectomic, phenotypic) that places each person on a small set of latent psychiatric axes (negative affect, reward, cognitive control, salience, vigilance, sensory gating; Williams 2024; Drysdale 2017; B-SNIP 2016). We derived the targets from a transdiagnostic synthesis across 14 disorders anchored to the Grotzinger and Smoller five-factor genomic structure (Nature 2025), with every connectomic finding mapped to the Allen Human Reference Atlas. The coordinate prioritizes not just **nodes** (regions such as anterior insula, implicated in 11 of 14 disorders) but **edges** (connections such as the dlPFC-to-sgACC anticorrelation that powers Stanford SAINT), because edges separate disorders and map onto interventions where nodes alone do not.
3. **Fine-grained zoom** via ultrasound-aided optical focusing (Marie-Nelly stealth program, 2024-2026, single-cell-class spectroscopy at 2-3 cm depth in vivo), spatially-offset Raman, and Openwater-class phase-conjugation optics, targeting the roughly two dozen anchor regions and the highest-reproducibility edges that dominate transdiagnostic biotype variance.

The instrument is engineered around the AI model from inception. Sensor channels, sampling rates, and optode steering are reconfigurable from software, allowing each device to adapt its readout schedule to the specific biotype-relevant regions for its user. The platform produces continuous, paired sensor-plus-coordinate-plus-outcome data: a longitudinal training corpus that no static MRI cohort can match.

### 1.3 Unmet Need

Mental disorders are the world's leading cause of years lived with disability. The 2026 GBD update reports 1.17 billion people affected and 171 million DALYs in 2023 (the fifth-leading cause group globally; Patel et al., *Lancet* 2026). Anxiety DALYs rose 47% since 2019 alone. The April 2026 White House Executive Order on Accelerating Medical Treatments for Serious Mental Illness states explicitly that "our medical research system has yet to produce approved therapies that promote enduring improvements" and calls for "innovative methods beyond existing prescription medications."

Three structural blindspots define this failure and persist because no existing entity is structurally equipped to close them:

- **Detection blindspot.** Psychiatry has no objective biomarker. Diagnosis depends on symptom report. Suicide is the leading cause of death in U.S. adolescents and has no biomarker predictor.
- **Personalization blindspot.** STAR\*D reports first-line SSRI response of 42-53%. The 2026 iMAP work (Williams, Tozzi et al., *NPP Digital Psychiatry and Neuroscience*, a Nature Portfolio journal, 2026, pilot study) demonstrates that biotype-matched ML intervention doubles depression remission from 30% to 55%. The biology supports stratification. The clinic does not operationalize it.
- **Feedback blindspot.** Diabetes has continuous glucose monitoring (CGM). Cardiology has continuous ECG patches. Oncology has circulating tumor DNA (ctDNA). Psychiatry has clinician scales administered weeks apart. People deteriorate between appointments without anyone knowing.

These are one structural failure: the absence of a brain-level, biotype-resolved, continuous, scalable wearable sensor. Academia produces fragmentary biotypes that fail to replicate at scale. Industry (Kernel, Openwater, Mendi) ships fixed-geometry hemodynamic devices without biotype personalization or closed-loop capacity, because biotype science and adaptive sensing require coordinated, mission-driven, long-horizon work that neither venture capital nor university structures support. Psychoscope can only be built by a dedicated, full-time, autonomous team funded on a 5-7 year horizon. That is the X-Lab structure.

---

## 2. Technology Landscape

### 2.1 Current State of the Art

We surveyed every credible noninvasive wearable brain-sensing platform and every commercial spectroscopy program targeting deep tissue (full review in `research/wearables-comparative.md` and `research/fnirs-deep-dive.md`).

EEG offers millisecond resolution but cortical-surface signals smeared across centimeters; commercial wearable EEG (Muse, Dreem, Neurable) has not produced a replicable psychiatric biomarker at the individual level. OPM-MEG provides better spatial-temporal balance but requires magnetic shielding incompatible with wearability at population scale; Kernel discontinued its Flux OPM-MEG program in 2022 for exactly this reason. fNIRS and adjacent diffuse optical methods (TD-fNIRS, HD-DOT, DCS, broadband NIRS) deliver 3-4 cm cortical sensitivity, tolerate motion, and run at consumer-feasible cost. They are the only noninvasive wearable substrate with a plausible path to brain-level molecular readout.

Three programs define the current optical-wearable frontier. **Kernel** ships Flow2, a TD-fNIRS headset with a "Neuroscience as a Service" data model; its architecture is fixed-geometry and offers no biotype personalization. **Openwater** open-sourced its TRUE platform (focused-ultrasound plus optical phase conjugation) under AGPL in January 2024 and pivoted to a therapy device for stroke and depression; it offers the only deployed depth-targeted optical "zoom," but is not personalized to biotype and does not integrate biotype inference. **Hervé Marie-Nelly's stealth program** (founded 2024, the team's co-PI) has demonstrated 2-3 cm in vivo depth with single-cell-class spectroscopic readout in adult human tissue.

The personalization frontier is moving in parallel. Stanford's SAINT/SNT protocol (Cole, Williams, et al., *Am J Psychiatry* 2022) achieves 79% remission in treatment-resistant depression versus 28% for standard rTMS by using individualized resting-state fMRI (rsfMRI) to identify each patient's anti-correlated dlPFC target. Drysdale's four-biotype depression model and the Williams 2024 six-biotype scaffold demonstrate that biotype-defined stratification predicts treatment response. ABCD, IMAGEN, B-SNIP, and PRONIA produce circuit-level subtypes for psychosis, addiction, and anxiety.

We consolidated this fragmented literature into a transdiagnostic biotype atlas across 14 disorders (schizophrenia, bipolar, depression, PTSD, anxiety, autism, ADHD, OCD, Tourette, anorexia, and four substance use disorders), harmonized to three ontologies: Gene Ontology for molecular biotypes, the Allen Human Reference Atlas for connectomic nodes and edges, and SNOMED CT and HPO for phenotypes. Three findings shape the instrument. First, a small set of connectome **edges** recurs across disorders and maps directly onto interventions: the dlPFC-sgACC anticorrelation (depression, the SAINT target), the amygdala-vmPFC threat-regulation edge (anxiety, PTSD), the NAc-OFC reward edge (all substance use disorders, ADHD, anorexia), and the OFC-caudate cortico-striato-thalamo-cortical (CSTC) loop (OCD, Tourette). Second, a small set of **molecular axes** recurs across nearly all 14: BDNF/TrkB plasticity (the convergent mechanism of SSRIs, ketamine, psilocybin, ECT, and TMS; Castren 2022, Moliner 2023), excitatory-inhibitory imbalance, mitochondrial and oxidative stress, and inflammation. Several of these have noninvasive wearable readouts: cytochrome-c-oxidase (CCO) by broadband NIRS for the mitochondrial axis, and the EEG aperiodic 1/f slope plus the 40 Hz auditory steady-state response (ASSR) for the excitatory-inhibitory axis. Third, the same psychosis-distinguishing signatures (reduced 40 Hz ASSR, reduced sleep spindle density) localize to specific Allen regions, which tells the sensor where to listen. A multi-scale causal foundation model that unifies these scales is under development at Cytognosis, with a pending submission to ARPA-H Health Science Futures (HSF) planned for 2026; this model, if funded, would provide the coordinate infrastructure onto which Psychoscope's readouts attach.

### 2.2 Technology Gaps and Bottlenecks

The current state of the art leaves five gaps open:

1. **No platform integrates multi-chromophore readout.** No commercial fNIRS device shipped today measures cytochrome-c-oxidase as a mitochondrial marker, despite published evidence that broadband NIRS makes it feasible at wearable scale.
2. **No platform does adaptive region selection.** Optode geometry is fixed at manufacture. There is no closed-loop "zoom" from a coarse map to a biotype-relevant region.
3. **No platform integrates the biotype layer, and none senses edges.** Williams's iMAP, Drysdale's biotypes, and B-SNIP's connectomic subtypes have not been operationalized into a wearable sensing strategy. Existing devices report single-region (node) activity; none measures the connectome edges (functional connectivity between regions) that actually predict treatment response, and none integrates the molecular, connectomic, and phenotypic scales into one coordinate.
4. **No platform handles skin-tone equity as a first-class signal.** Kwasa et al. (*Nat Hum Behav* 2023) and subsequent *Neurophotonics* work show fNIRS systematically underperforms in higher-melanin skin. No vendor builds melanin handling into device firmware.
5. **No platform produces the longitudinal paired data** that next-generation foundation models for mental health require. Existing optical brain datasets are static research cohorts (HCP, UK Biobank fMRI), not continuous-readout, biotype-tagged, outcome-paired streams.

### 2.3 Proposed Advancement

Psychoscope closes all five gaps in one platform:

- **Multi-chromophore optical stack**: HbO2, HbR, CCO (broadband NIRS), water and lipid (short-wave infrared, SWIR), cerebral blood flow (DCS/SCOS), with cortical-surface protein-aggregate spectral features (spatially offset Raman spectroscopy, SORS, and surface-enhanced spatially offset Raman spectroscopy, SESORS) as a Phase 2 stretch goal (detailed below).
- **Adaptive node-and-edge selection from a biotype prior**: a 60-second coarse whole-cortex scan triangulates the user's coordinate on the Psychoverse map, then optode driver firmware re-weights and re-focuses to the highest-yield anchor regions (DLPFC, dACC/dmPFC, vmPFC/OFC, anterior insula, sgACC, superior temporal cortex, posterior cingulate, ventral striatum and amygdala via cortical effectors, plus STS, fusiform, IFG, and lateral cerebellum for the neurodevelopmental disorders). Beyond single-region activity, the platform measures the transdiagnostic edge biomarkers (dlPFC-sgACC, amygdala-vmPFC, NAc-OFC, OFC-caudate) by acquiring the paired regions simultaneously and computing their functional connectivity.
- **Multi-scale molecular readout**: the optical stack quantifies the mitochondrial axis (cytochrome-c-oxidase) directly, and an optional low-channel EEG layer adds the excitatory-inhibitory axis (aperiodic 1/f slope, 40 Hz ASSR) and the reward and error signatures (reward positivity, error-related negativity) that localize to the same anchor regions. This makes Psychoscope a coordinate sensor across all three scales, not a hemodynamics-only device.
- **AI-native instrument design with skull as a learnable transform (Topic 2 differentiator)**: the Psychoscope architecture reframes the skull not as opaque noise, but as a largely static, deterministic aberrating layer whose transfer function can be learned, calibrated, and inverted. This is a core innovation enabling adaptive AI-based sensing and AI-driven computational imaging (see Topic 2 alignment below and the expanded passage in this section).
- **Melanin-equity as a first-class signal**: built-in spectral calibration per user, with melanin channel quantified rather than treated as noise.
- **Marie-Nelly depth-zoom integration**: the fine-grained sensing layer uses ultrasound-aided optical focusing to push functional readout into the 2-3 cm depth band, accessing the cortical-subcortical boundary at single-cell-class spectroscopic resolution. Internal validation data on this depth and resolution claim will be shared under NDA at the Oral Proposal stage.

#### Skull as a Learnable Transform: An AI-Native Sensing Differentiator

The dominant assumption in transcranial optical imaging is that the skull is the enemy: an attenuating, scattering layer that destroys signal. We invert this assumption. The skull's optical speckle decorrelation time is on the order of tens of seconds, roughly 3-4 orders of magnitude more stable than vascularized scalp, hair follicles, and brain tissue, where blood flow drives decorrelation times in the millisecond range (Woo et al., 2015; Sutin et al., 2016). Skin and hair are fast-changing, hard-to-predict contributors to wavefront distortion, whereas the skull's hydroxyapatite mineral microstructure is near-stationary and approximately deterministic, and therefore learnable and invertible.

The analogy to astronomical adaptive optics is direct and accurate. Conventional adaptive optics corrects atmospheric turbulence using a guide star and a deformable mirror; multi-conjugate adaptive optics uses multiple guide stars to tomographically reconstruct and correct turbulence layer by layer. We treat the skull as a structured aberrating layer whose transfer function can be estimated from a subject-specific structural prior (CT or MRI), refined by in situ wavefront sensing, and inverted computationally, so that the bone acts as a calibration target rather than a noise floor. This approach has direct precedent: transcranial focused ultrasound (TcFUS) routinely uses CT-derived skull models for patient-specific acoustic aberration correction, and deterministic ray-tracing models of optical skull aberration have been demonstrated (Mohammadi et al., *Sensors* 2019, DOI 10.3390/s19020345). Optical through-skull imaging via transmission-matrix adaptive optics has been demonstrated in vivo in animals (Jo et al., *Science Advances* 2022, DOI 10.1126/sciadv.abo4366), and time-reversed ultrasonically encoded (TRUE) focusing through scattering media has been shown to exploit the ultrasound guide-star principle analogously (Si et al., *Science Advances* 2018).

Three hard limits govern our engineering design and must be acknowledged honestly. First, the adult-skull optical isoplanatic patch (the region over which a single correction applies) is approximately 1 micrometer in diameter (Forouhesh Tehrani et al., *J. Biophotonics* 2021, DOI 10.1002/jbio.202000160), meaning that corrections must be applied patch by patch across the illumination field, not globally. Second, photon attenuation through skull plus cortex requires pulsed or heterodyne detection rather than continuous-wave illumination. Third, individual skull thickness and trabecular architecture vary substantially across subjects, requiring subject-specific adaptation rather than a population-average model. These constraints set the engineering requirements for Phase 1: build the skull-model pipeline, validate wavefront-estimation accuracy on ex vivo specimens, and demonstrate closed-loop correction gain on a phantom before translating to in vivo at Phase 2. Current technology readiness for through-skull adaptive optics in living humans is TRL 2-4. The Psychoscope architecture is designed to benefit from each incremental advance in this space, because the skull-as-learnable-transform concept is built into the AI sensing stack from the beginning.

The foundation model underlying Psychoscope LEARNS each subject's skull transfer function, converting a classic physical obstacle into a per-subject calibration input. This is the core claim for the Topic 2 "Adaptive AI-based sensing algorithms" and "AI-driven computational imaging" challenge areas.

#### Phase 2 Stretch Goal: Protein-Aggregate Sensing for Neurodegeneration

The same adaptive spectroscopy platform that monitors functional brain states for mental health extends, in principle, to sensing pathological protein aggregates associated with neurodegenerative disease. We describe this as a Phase 2 stretch goal, properly caveated, because the translational path from the established ex vivo science to noninvasive in vivo human detection is long and the current technology readiness is low.

The physical basis is as follows. Pathological aggregates are micron-scale objects, within the resolution range that Psychoscope targets at Phase 2: amyloid-beta plaques range from approximately 10-50 micrometers (dense-core and diffuse plaques), neurofibrillary tau tangles from approximately 5-30 micrometers, and alpha-synuclein Lewy bodies from approximately 8-30 micrometers. A system resolving down to a few microns can detect these structures as objects; individual amyloid fibrils at 10-20 nm diameter are far below optical resolution and cannot be resolved. This supports co-PI Marie-Nelly's observation that the planned resolution regime can capture aggregate-scale objects. Label-free Raman and stimulated Raman scattering (SRS) imaging of amyloid plaques ex vivo has been established at TRL 4-5 (Ji et al., *Science Advances* 2018, DOI 10.1126/sciadv.aat7715; Lochocki et al., *Communications Biology* 2021, DOI 10.1038/s42003-021-01981-x), exploiting the beta-sheet amide-I Raman signature near 1665 cm-1, though this band partially overlaps signals from other proteins and requires spectral decomposition. Transcranial molecular sensing via SESORS through intact skull has been demonstrated in animal models at TRL 3 (Sharma et al., *Anal. Chem.* 2017, DOI 10.1021/acs.analchem.7b00985).

We must be direct about what remains unproven: direct, noninvasive, transcranial detection of protein aggregates in the living human brain is at TRL 1-2. The two critical barriers are (a) achieving sufficient photon budget in the near-infrared tissue window after transmission through skull and cortex, and (b) discriminating the aggregate Raman signal from the skull's intrinsic background (autofluorescence and Raman from hydroxyapatite and collagen are strong interferers). Phase 1 will focus entirely on the core mental-health sensing mission. If the skull-model pipeline and photon-budget engineering reach the targets needed for functional spectroscopy, Phase 2 will pursue a specifically scoped validation study of aggregate sensing ex vivo, then in animal models, before any human claim is made. Independent replication will be required. This extension broadens the Psychoscope platform from psychiatry to neurodegeneration (Alzheimer's disease, Parkinson's disease), but remains secondary to the core mental-health mission and contingent on Phase 1 success.

### 2.4 Alignment with Topic 2 Challenge Areas

Psychoscope is designed against the five Topic 2 challenge areas with one subsystem per area:

| Topic 2 area | Psychoscope subsystem |
|---|---|
| Adaptive AI-based sensing algorithms | Coordinate-driven optode steering and channel weighting that adapts each device's readout schedule to the user's inferred biotype; skull transfer-function learning that converts bone anatomy into a per-subject calibration target rather than noise |
| AI-driven computational imaging | End-to-end-differentiable reconstruction of multi-chromophore tomograms, with the foundation model jointly optimized over instrument and inference; skull-as-learnable-transform pipeline inverts patch-wise wavefront aberrations estimated from structural prior and in situ wavefront sensing |
| MRI-free deep-tissue imaging | Multi-chromophore TD-fNIRS, DCS, and ultrasound-aided optical focusing (Marie-Nelly depth-zoom) reach cortical and shallow-subcortical targets without MRI infrastructure |
| Instruments engineered for next-generation AI training pipelines | Every fielded device contributes continuous, paired sensor-plus-coordinate-plus-outcome data into a federated training corpus |
| Whole-brain activity at cellular resolution across long timescales | Cellular-class spectroscopic resolution achieved in cortex during Phase 1; longitudinal continuous monitoring extends across years per user |

### 2.5 Technology Landscape Figure

*[Figure 1: Two-axis landscape of noninvasive brain-sensing modalities. X-axis: spatial resolution (cm to single-cell). Y-axis: biological specificity (hemodynamics only, multi-chromophore, molecular). Existing modalities cluster in the low-specificity/coarse-resolution corner (EEG, fNIRS-Kernel) or the high-specificity/non-wearable corner (PET, fMRI). Psychoscope occupies the empty quadrant: multi-chromophore, adaptive, sub-millimeter cortical zoom, wearable, longitudinal.]*

---

## 3. Outcomes

### 3.1 Target Outcomes (5-7 Year Timescale)

| # | Outcome | Performance Benchmark | Timeline |
|---|---------|----------------------|----------|
| 1 | Psychoscope v1.0 wearable headset with multi-chromophore optical stack (HbO2, HbR, CCO, DCS, SWIR water/lipid) | >= 4 chromophores quantified continuously at >= 1 Hz; signal-to-noise within 10% across Fitzpatrick I-VI skin types | Phase 1, Month 24 |
| 2 | Adaptive coarse-to-fine node-and-edge selection from biotype prior | < 90 seconds from headset-on to biotype-coordinate inference and zoom target list; targeting accuracy >= 80% match to rsfMRI ground truth across the anchor regions; recovery of >= 4 transdiagnostic edge biomarkers (incl. dlPFC-sgACC, amygdala-vmPFC) at group level | Phase 1, Month 30 |
| 3 | Psychoverse coordinate model, trained on the 14-disorder, 3-scale atlas; compatible with the planned ARPA-H HSF foundation-model layer if that submission is funded | >= 6 latent axes recovered; predicts SSRI response (AUC >= 0.75 vs ~0.55 baseline) and TMS response (AUC >= 0.80) in held-out cohorts of N >= 500 each; transdiagnostic generalization tested on >= 3 disorders beyond depression | Phase 1, Month 30 |
| 4 | Pilot closed-loop demonstration: Psychoscope-targeted TMS in treatment-resistant depression | Demonstration cohort N = 20-30 showing Psychoscope-derived target matches rsfMRI-derived SAINT target with >= 80% spatial concordance; remission rate >= 60% at 4 weeks; cost per session < 10% of SAINT | Phase 2, Month 60 |
| 5 | Open data and model release | >= 10,000-person longitudinal Psychoscope dataset; foundation model weights released under Apache-2.0; device firmware OSS by Phase 2 close | Phase 2, Month 72 |
| 6 | Manufacturing scale and regulatory pathway, with Cytognosis retaining IP and mission control | < $500 bill-of-materials per device at 100k-unit scale; FDA Q-Submission filed for De Novo pathway with regulatory strategy memo; Public Benefit Corporation structure designed for Phase 2-plus commercial scale | Phase 2, Month 84 |
| 7 | *[Phase 2 stretch]* Protein-aggregate sensing validation (ex vivo then animal model) for Alzheimer's and Parkinson's applications, contingent on Phase 1 photon-budget and skull-model results | Positive signal/background ratio for beta-sheet Raman signature in ex vivo human cortex specimens; replication in at least one independent animal model; explicit statement of remaining barriers to in vivo human translation | Phase 2, Month 72 (stretch) |

### 3.2 Scientific and Technical Performance Benchmarks

**Sensor.** Multi-chromophore readout meeting the chromophore-count and SNR targets above, in a < 500 g head-mounted form factor, with >= 4-hour continuous battery, and at < $5k cost-of-goods at pilot scale (target < $500 at consumer scale). Cytochrome-c-oxidase quantification reproducible at within-subject SD < 10% over 30-day longitudinal monitoring.

**Coordinate model.** Biotype-coordinate inference predicts treatment response across SSRI, TMS, ketamine, and neuroplastogen cohorts with AUC >= 0.75 at internal validation and AUC >= 0.70 at external validation (held-out site). The coordinate space is RDoC- and HiTOP-compatible at the latent-axis level, is built on the 14-disorder transdiagnostic atlas, and reports both nodes (Allen-atlas regions) and edges (functional connections). The molecular axes (cytochrome-c-oxidase for mitochondrial state, EEG 1/f for excitatory-inhibitory balance) are validated against established reference assays.

**Adaptive sensing loop.** Coarse-to-fine targeting decision under 90 seconds; closed-loop adjustment of stimulation parameters (TMS coil placement; tDCS montage; LIFU target) within 1 minute of sensor inference.

**Longitudinal data.** N >= 1,000 participants enrolled by Phase 1 close, N >= 10,000 by Phase 2 close, with paired clinical outcomes and informed consent for open release in compliance with the Cytognosis Data Management and Privacy Plan.

### 3.3 Field-Reshaping Impact

Psychoscope shifts mental health care from interval-based symptom reporting to continuous biological monitoring, the same shift that CGM produced in diabetes (HbA1c reduction of ~0.6% over standard care in the DIAMOND trial, Beck et al., *JAMA* 2017) and that ambulatory ECG produced in cardiology. It operationalizes the personalization research that Williams and Tozzi (iMAP, 2026) and Cole and Williams (SAINT, 2022) have shown works in the lab but cannot reach the clinic without an accessible, wearable sensor.

The platform creates two downstream sectors. **Closed-loop noninvasive neuromodulation** (TMS, tES, LIFU, tVNS) requires personalized targeting that is currently bottlenecked on offline rsfMRI; Psychoscope removes the bottleneck. **AI-native digital therapeutics** for psychiatry, conditioned on continuous neural readout rather than survey responses, become a new product class. Both sectors are nascent in 2026 and have no incumbent sensor.

Field-reshaping precedents this work intentionally models: CGM (diabetes), ctDNA (oncology), pulse oximetry (respiratory medicine), and the personal-genomics era. In each case a continuous, personalized, accessible sensor reshaped clinical practice, research, and consumer expectations.

---

## 4. Senior/Key Personnel Qualifications

> **[ELIGIBILITY — INTERNAL NOTE; REMOVE BEFORE SUBMISSION]**
>
> NSF X-Labs Sections 6.2-6.3 bar "citizens of ... the Islamic Republic of Iran" from serving as Senior/Key Personnel on X-Labs awards. Under the plain text of the restriction, this applies to nationals and citizens of the four listed countries; legal interpretations differ on whether it also covers US/Iran dual citizens, but the most conservative and prudent reading includes them. Shahin Mohammadi is a dual US/Iran citizen. Therefore, under a strict reading of the eligibility requirements, he likely cannot be listed as Senior/Key Personnel on an X-Labs submission.
>
> The viable path for pursuing X-Labs, if the team decides to proceed, is the following: an eligible individual serves as PI of record and is designated Senior/Key Personnel (for example, Hervé Marie-Nelly, contingent on confirming that his citizenship is not one of the four restricted countries listed in NSF X-Labs Sections 6.2-6.3; his citizenship has not been verified here and must not be assumed). Shahin Mohammadi would serve as Founder/CEO and organizational lead, with a role clearly described in the proposal but NOT designated Senior/Key Personnel under the NSF X-Labs definition. This must reflect genuine roles, not relabeling; the organizational and scientific contributions of each person must be described accurately and cannot inflate the non-Senior/Key role to circumvent the intent of the restriction.
>
> Recommended actions before submission: (1) Request a written interpretation from NSF's Office of the Chief of Research Security Strategy and Policy (OCRSSP) at researchsecurity@nsf.gov regarding the dual-citizenship question; (2) Engage independent research-security counsel familiar with CHIPS Act Section 10636/10632 and NSF's implementing guidance; (3) Confirm Hervé Marie-Nelly's citizenship eligibility with him directly and in writing; (4) Revise the personnel section to reflect the genuine PI of record once eligibility is confirmed.
>
> Do not submit this proposal with Shahin Mohammadi designated as Senior/Key Personnel before receiving a written NSF interpretation confirming eligibility. The Foundation's general counsel should review the final submission.

### Shahin Mohammadi, PhD, Founder and CEO / Organizational Lead

**Affiliation:** Cytognosis Foundation (Founder & CEO)

**Role:** Organizational lead; scientific direction; Psychoverse foundation-model and biotype-coordinate workstreams; X-Lab governance. (See eligibility note above regarding Senior/Key Personnel designation.)

**Qualifications:** Twenty years in computational biology and machine learning for human disease. Previously at the Broad Institute, MIT, insitro, and GenBio AI. Co-first-author work on single-cell atlas of schizophrenia (*Science*, psychiatric genomics special issue, 2024) and bipolar disorder (*European Neuropsychopharmacology*, vol. 87, p. 48, 2024, co-first author); contributed to the single-cell atlas of Alzheimer's disease (Mathys et al., *Nature* 2019). Foundation-model architectures for biology (AIDO, GenBio AI 2023). Founder of Cytognosis Foundation, the nonprofit Focused Research Organization (FRO) building the Psychoverse coordinate system. ACTIONet computational framework (github.com/shmohammadi86/ACTIONet, Apache 2.0). Over 40 peer-reviewed publications; approximately 4,000+ citations (Google Scholar). Personal expertise spans pairwise disease geometry, disentangled representation learning, causal inference in biological systems, and large-scale longitudinal data infrastructure. Patient-advocate by lived experience: identified a single ultra-rare TBX1 coding variant underlying a decade-long misdiagnosis odyssey across ten specialties, the experience that motivates the Cytognosis mission. Cytognosis has a pending submission planned to ARPA-H Health Science Futures (HSF) in 2026 for the multi-scale foundation-model layer onto which Psychoscope's readouts would attach; this funding is not yet awarded.

### Hervé Marie-Nelly, PhD, Co-Principal Investigator

**Affiliation:** Founder, deep-tissue spectroscopy company (currently in stealth; collaboration confirmed under a mutual NDA, with company name to be disclosed at oral-proposal stage under appropriate confidentiality safeguards)

**Role:** Co-PI; instrument hardware and optical physics; ultrasound-aided optical focusing; depth-zoom integration; manufacturing scale

**Qualifications:** Trained in biophysics and quantitative optics; previous work at insitro (where the lead PI collaborated with him) developing computational microscopy and machine-learning-driven optical systems for cell biology. Founded his current company in 2024 after demonstrating noninvasive single-cell-class spectroscopic readout at 2-3 cm depth in adult human tissue, a result without published parallel in the open literature. Brings deep optical physics, ultrasound-modulated optics, and hardware engineering scale-up expertise. Has assembled a hardware team with prior experience at Openwater and Kernel.

### Additional Senior Personnel (Identified, to Be Confirmed Full-Time by Phase 1)

**Computational Biology and Foundation Models.** Two senior research scientists with experience training large-scale biological foundation models (single-cell and neuroimaging modalities) at the GenBio AI and Cytognosis collaboration network.

**Clinical Neuroscience and Biotype Validation.** One senior clinical neuroscientist with TMS-and-fMRI biotype experience (Stanford-network alumnus); one senior psychiatrist with treatment-resistant depression trial experience; both identified, full-time commitment subject to Phase 1 award.

**Optical Engineering and Manufacturing.** Two senior optical engineers from the Marie-Nelly team, plus a manufacturing scale lead recruited at Phase 1 from a high-volume consumer-electronics background.

**Health Equity and Regulatory.** One senior advisor on melanin-equity and inclusive device design (recruiting from the Kwasa lab network); regulatory and clinical-trial lead recruited at Phase 1.

All named Senior/Key Personnel meet CHIPS and Science Act Section 10636/10632 research-security requirements, subject to the eligibility review described in the note above. None appear on restricted-party lists. None participate in Malign Foreign Talent Recruitment Programs. Final personnel disclosures will be provided at the Oral Proposal stage under SciENcv.

---

## 5. Team Capabilities Statement

### 5.1 Complementary Expertise

The team unites four capabilities that no single institution currently houses. (1) Computational biology and foundation-model expertise at the level required to build the Psychoverse coordinate system, contributed by Cytognosis. (2) Optical physics and single-cell-class deep-tissue spectroscopy hardware, contributed by Marie-Nelly. (3) Clinical psychiatry and TMS-biotype validation, contributed through the Stanford-network alumni already identified. (4) Manufacturing and regulatory experience for consumer medical devices, recruited at Phase 1. The lead PI and co-PI worked together previously at insitro and share an established collaboration model, removing the most common cause of cross-institutional X-Lab failure.

### 5.2 Governance Structure

**Phase 0.** Cytognosis Foundation acts as the lead organization, with Marie-Nelly's company under subcontract. Decisions on technical direction, hiring, partnerships, and budget reallocation are made by a two-person Executive Committee (Mohammadi, Marie-Nelly) within 48 hours, reporting monthly to the Cytognosis Board of Directors. The Foundation's existing 501(c)(3) structure provides full operational autonomy and IP ownership today.

**Phase 1.** Cytognosis will spin out a dedicated Psychoscope program within the Foundation, governed by an independent Psychoscope Steering Committee. The Steering Committee will hold full internal control of funding allocation, research direction, IP, hiring, contracting, and partnership negotiation, satisfying all six conditions of the Autonomy Factor Test (Section 6.1.1 of the OTASO):

| Autonomy Factor | How Satisfied |
|---|---|
| Decision-making (days, not weeks) | Two-person Executive Committee at Phase 0; Steering Committee with delegated authority at Phase 1 |
| Funding allocation | Cytognosis Foundation 501(c)(3) controls all funding internally; no parent institution |
| Research direction | Same |
| IP ownership and control | Foundation owns IP; no parent institution claim; Apache-2.0 release model for open components per Cytognosis Openness Policy |
| Hiring, salary, contracting | Foundation has full internal control |
| Independent leadership boards | Psychoscope Steering Committee independent of Foundation Board, with rotating clinical and scientific advisors |

A Public Benefit Corporation may be incorporated at Phase 2 to handle commercial manufacturing scale, with Cytognosis retaining IP and mission control through the established nonprofit-to-PBC commercial pathway in our Openness Policy.

### 5.3 Networks, Partnerships, and Resources

| Partner | Type | Contribution |
|---|---|---|
| ARPA-H Health Science Futures (HSF) | Federal (pending submission, 2026) | Planned multi-scale foundation-model (genomic, connectomic, phenotypic) for the Psychoverse coordinate; not yet awarded; no overlap with X-Labs scope |
| Stanford Center for Precision Mental Health (Williams lab network) | Academic | iMAP biotype validation cohorts; TMS personalization expertise; clinical trial site for Outcomes 3-4 |
| Massachusetts General Hospital, Athinoula A. Martinos Center | Academic | TD-fNIRS expertise (Boas, Sassaroli); diffuse optical imaging validation |
| Marie-Nelly's stealth company | Industry (subcontract) | Optical hardware; ultrasound-aided focusing; depth-zoom integration; manufacturing engineering |
| Schmidt Futures and the Patrick J. McGovern Foundation* | Philanthropy | Bridging capital and Psychoverse infrastructure |
| Veterans Affairs Office of Mental Health and Suicide Prevention | Federal partner | Validation cohorts for PTSD biotype and treatment-stratification arms (Outcome 3); aligns with the April 2026 EO's veteran-suicide priorities |
| NIMH Biomarker Consortium and PsychENCODE Phase II | Federal partner | Reference biotype datasets and benchmark protocols |

*Partnerships marked with an asterisk are in active development at the time of submission; final commitments will be reflected in Letters of Collaboration at the Oral Proposal stage.

Cytognosis Foundation is a lean, founder-led 501(c)(3) bootstrapped organization. The founding team consists of the PI/founder, co-PI, and named advisors identified above; external grant applications are pending and no external funding has been committed at the time of submission. The Foundation has already assembled the transdiagnostic biotype atlas described in Section 2 (14 disorders, three scales, harmonized to Gene Ontology, the Allen Human Reference Atlas, and SNOMED CT/HPO), which de-risks the coordinate model and defines the sensor target list before Phase 0 begins. The Foundation is registered in SAM.gov and meets all CHIPS Act eligibility conditions, subject to the personnel eligibility review described in Section 4.

---

<!-- SEPARATE PDF DOCUMENT, DO NOT INCLUDE IN PAGE COUNT -->

## Conflicts of Interest Statement

### Lead Organization Conflicts

Cytognosis Foundation is a 501(c)(3) nonprofit with no shareholders, no equity holders, and no commercial revenue stream at time of this submission. The Foundation's open-science and open-source release commitments (Apache-2.0 for code and models; CC BY for data and documents where consented; Cytognosis Openness Policy 2026) further reduce the surface area for organizational financial conflict. A Phase 2 spin-out Public Benefit Corporation, if pursued, would be governed by an arms-length licensing agreement with the Foundation, preserving mission control and equity-of-access provisions.

### Senior/Key Personnel Conflicts

**Shahin Mohammadi (organizational lead; see Section 4 eligibility note).** Founder and CEO of Cytognosis Foundation. Holds no equity in any for-profit entity related to the proposed work. Past employment at insitro (2020-2022), Broad Institute (2014-2020), and GenBio AI (2022-2023) created no continuing financial interests beyond standard alumni equity in publicly disclosed entities, with all positions fully disclosed in SciENcv.

**Hervé Marie-Nelly (co-PI).** Founder and equity holder in a deep-tissue spectroscopy company (currently in stealth). This entity is the proposed subcontractor for hardware deliverables and the source of the Marie-Nelly depth-zoom IP integrated into Psychoscope. This creates a structural organizational conflict of interest (OCI) that we mitigate as follows: (i) full disclosure of the company name and Marie-Nelly's equity position at the Oral Proposal stage under appropriate confidentiality; (ii) all subcontract pricing benchmarked to independent third-party optical engineering comparables, reviewed annually; (iii) IP integration covered by a perpetual, royalty-free, sublicensable license to Cytognosis Foundation, with field-of-use restricted to mental-health applications and with explicit non-compete carveouts for other diagnostic domains; (iv) Marie-Nelly recused from any subcontract-renewal vote of the Psychoscope Steering Committee.

**All other Senior/Key Personnel.** Standard academic affiliations to be disclosed at SciENcv stage. No anticipated material OCIs.

### Mitigation Plan

The mitigation plan above applies to identified OCIs. Cytognosis will publish a public OCI Disclosure Register, updated quarterly, listing any newly identified conflicts and their mitigation. Any post-award OCI will be reported to NSF within 10 business days of discovery, with a written mitigation plan attached, per FAR Subpart 9.5 framework guidance. Cytognosis's Openness Policy and Data Management and Privacy Plan, both published openly, further constrain undisclosed financial interests in the program.

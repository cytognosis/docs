# Differential Response to Noninvasive Neuromodulation by Connectomic Biotype

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: researchers, stakeholders
> **Tags**: `research`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)

**Research dossier for Cytognosis Foundation + Hervé Marie-Nelly NSF X-Labs / ARPA-H PHO proposal.**
**Compiled 25 May 2026. Author: Claude (research subagent).**

## Executive framing

The proposal needs to defend a single load-bearing claim: connectomic biotypes (and adjacent EEG, autonomic, and molecular biotypes) predict differential response to noninvasive neuromodulation across transcranial magnetic stimulation (TMS), transcranial electrical stimulation (tES), low-intensity focused ultrasound (LIFU), and transcutaneous vagus nerve stimulation (tVNS). The evidence is uneven. The strongest pillar is functional-connectivity-guided dorsolateral prefrontal cortex (dlPFC) TMS for depression, anchored by Fox & Cash 2012 [1], Drysdale 2017 [2], Cole/Williams SAINT 2020 and 2022 [3,4], and Tozzi/Williams 2024 [5]. Replication is incomplete and Drysdale's original four-cluster solution did not survive (Dinga 2019 [6]), but the underlying logic, that pre-treatment functional connectivity to a target predicts response, is broadly supported across multiple cohorts and modalities. This document tracks the evidence per modality and per disorder, flags what failed replication, and links each pattern to the Cytoscope wearable proposition.

---

## 1. Transcranial magnetic stimulation (TMS)

### 1.1 Drysdale 2017: the founding biotype-by-TMS study

Drysdale and colleagues collected resting-state fMRI from 1,188 patients with major depressive disorder across 17 sites and applied canonical correlation followed by hierarchical clustering to derive four biotypes from limbic and frontostriatal connectivity features [2]. Biotypes were not distinguishable on clinical symptoms alone but mapped onto distinct connectivity profiles:

- **Biotype 1**: reduced connectivity in frontoamygdala networks regulating fear-related behavior and reappraisal of negative emotion. Symptom profile dominated by anxious arousal.
- **Biotype 2**: reduced connectivity in thalamic and frontostriatal networks involved in reward processing and motor initiation. Symptom profile dominated by anhedonia and psychomotor retardation.
- **Biotype 3**: hyperconnectivity in thalamic and frontostriatal networks, plus reduced connectivity in anterior cingulate and orbitofrontal regions. Anhedonia plus anxiety.
- **Biotype 4**: hyperconnectivity in frontoamygdala and ventral attention networks. Severe anxious avoidance and anhedonia.

In a separate cohort of 154 patients who received dorsomedial prefrontal cortex (dmPFC) rTMS, response (>25% Hamilton Depression Rating Scale reduction) varied sharply by biotype:

- Biotype 1: **82.5% response** (33 of 40)
- Biotype 2: **25.0% response** (4 of 16)
- Biotype 3: **61.0% response** (25 of 41)
- Biotype 4: **29.6% response** (8 of 27)

This 3.3-fold range is the headline number. The biotype assignment carried a positive predictive value of roughly 78% for TMS response in held-out patients, vastly outperforming clinical features alone.

### 1.2 Drysdale replication status

Dinga and colleagues, working from a separate cohort (n=187), reproduced the canonical correlation step but failed to recover stable clusters under bootstrapping or in held-out data [6]. They argued the original cluster solution was not statistically distinguishable from a single continuous distribution. The biotype-by-TMS response prediction has not been independently replicated in a comparably sized cohort. Tozzi/Williams 2024 [5] later derived **six biotypes** from 801 patients using a theoretically grounded circuit taxonomy (default mode, salience, frontoparietal, threat, reward, cognitive control) and reported differential response to pharmacotherapy and behavioral therapy, though not to TMS directly. The honest summary is: the *concept* that resting-state circuit features stratify treatment response is well supported; the *specific four-cluster Drysdale solution* did not replicate; the *gradient logic* (continuous circuit dysfunction scores) is the version surviving into 2026.

### 1.3 Stanford SAINT / SNT

The Stanford Accelerated Intelligent Neuromodulation Therapy (SAINT, renamed Stanford Neuromodulation Therapy, SNT) protocol stacks three innovations: (a) intermittent theta burst stimulation (iTBS) at 1,800 pulses per session, (b) ten sessions per day over five days for a total of 90,000 pulses, and (c) personalized targeting via resting-state fMRI to identify the dlPFC subregion most anticorrelated with the subgenual anterior cingulate (sgACC).

- **Open-label pilot (Cole et al. 2020, Am J Psychiatry)**: 21 of 22 patients with treatment-resistant depression (TRD) achieved remission, 90.5% [3].
- **Double-blind sham-controlled RCT (Cole, Williams et al. 2022, Am J Psychiatry)**: n=29; 78.6% remission in the active arm vs 13.3% in sham at the primary endpoint immediately post-treatment; 57.1% vs 0% remission at the 4-week follow-up [4].

The 2022 result is the strongest single piece of biotype-by-TMS evidence. Caveats: small sample (n=29), single site, no head-to-head against standard rTMS, and remission durability beyond 4 weeks varies (Cole 2024 open-label extension reported sustained efficacy with repeat dosing [7]). The 79% headline drives the entire personalized-TMS field, but it rests on one trial.

### 1.4 sgACC-dlPFC anticorrelation as a connectivity predictor

Fox and Cash (2012) reanalyzed published TMS coordinates and showed that targets producing larger antidepressant effects sat in dlPFC subregions more strongly anticorrelated with sgACC at rest [1]. Subsequent retrospective and prospective work replicated the association:

- Weigand et al. (2018, Biol Psychiatry): stronger pre-treatment dlPFC-sgACC anticorrelation predicted better outcome (r ≈ -0.4 to -0.55) [8].
- Cash et al. (2019, Brain Stimul; 2021, Hum Brain Mapp): personalized connectivity-guided targeting reproducible across sites; reliability improved with longer rsfMRI scans [9].
- Siddiqi et al. (2021, Am J Psychiatry): lesion network mapping of antidepressant TMS targets converged on the same sgACC-anticorrelated circuit [10].

Effect sizes for sgACC-dlPFC anticorrelation as a univariate predictor are moderate (r ≈ 0.3 to 0.5). Combining anticorrelation with default mode and salience network metrics in multivariate models raises classifier AUC into the 0.7 to 0.8 range.

### 1.5 Other connectivity-based response predictors

- **Default mode network** baseline hyperconnectivity to mPFC predicts worse response to standard rTMS [11].
- **Salience network** integrity predicts response to TMS for smoking craving (BrainsWay deep TMS) [12].
- **Cognitive control biotype** (Williams B-SMART-fMRI 2024 [13]) defined by reduced dlPFC-dACC engagement during a Go/NoGo task predicted early restoration of cognitive performance after TMS in 43 veterans with TRD. Effect size on cognitive control connectivity post-TMS was moderate (Cohen's d ≈ 0.5 to 0.7).
- **Threat circuit** (right dlPFC-amygdala) targeting in personalized fMRI-guided low-frequency rTMS for PTSD reduced PCL-5 scores significantly more than sham in a 50-patient RCT (Phillips et al. 2025, Am J Psychiatry) [14].

### 1.6 BDNF Val66Met effects

Cheeran et al. (2008, J Physiol) reported that Met allele carriers showed reduced or absent plasticity responses to multiple TMS plasticity protocols (cTBS, iTBS, paired associative stimulation) versus Val/Val homozygotes [15]. Replication is mixed: Antal 2010, Lee 2013, Jannati 2017 replicated; Li Voti 2011, Mastroeni 2013 did not [16]. The most defensible reading is that Met carriers show *greater between-subject variance*, not a simple deficit. Effect of BDNF genotype on clinical TMS antidepressant outcome is small to absent in most large series; it shows up as a moderator of mechanistic biomarkers (motor-evoked potential changes) more reliably than of clinical response.

### 1.7 Theta-burst stimulation (iTBS, cTBS) predictors

The THREE-D trial (Blumberger et al. 2018, Lancet) established noninferiority of iTBS to 10 Hz rTMS for depression and made iTBS the workhorse protocol [17]. Response predictors include:

- Greater baseline N100 amplitude on TMS-EEG predicts better iTBS response in unipolar depression [18].
- Individual alpha peak frequency closer to 10 Hz predicts greater response to 10 Hz rTMS [19].
- Elevated baseline frontal theta power predicts response, possibly reflecting working-memory-related circuits [20].

### 1.8 Deep TMS (Brainsway H-coil)

H-coil geometry produces deeper, broader field penetration than figure-of-eight coils. FDA clearances: MDD (2013), OCD (H7-coil, 2018), short-term smoking cessation (H4-coil, 2020), late-life depression (2024 expanded indication). The largest postmarketing analysis (>1,300 TRD patients, Tendler et al.) reported 82% response and 65% remission, higher than typical figure-of-eight rTMS series, though without sham control [21]. Moderators of smoking cessation response: younger age (<40), shorter smoking history, greater acute craving suppression during early sessions, and salience network connectivity strength [12].

### 1.9 TMS-EEG biomarkers

TMS-evoked potentials (TEPs) and resting EEG features have emerged as response predictors for depression rTMS:

- N100 (~100 ms post-pulse), thought to reflect GABA-B inhibitory currents, is elevated in responders [18].
- Higher baseline theta-band TMS-evoked oscillation predicts response [22].
- Individual alpha peak frequency, theta-gamma phase-amplitude coupling, and TEP-derived effective connectivity are under active evaluation as multivariate biomarkers (Casarotto, Rogasch, and colleagues) [23].

EEG-based biomarkers are far cheaper than rsfMRI and represent the natural bridge from research-grade biotyping to scalable closed-loop deployment.

### 1.10 TMS for schizophrenia and autism

- **Schizophrenia negative symptoms**: meta-analyses show modest pooled effect (Hedges' g ≈ 0.3 to 0.5) for high-frequency rTMS to left dlPFC; younger age and lower baseline severity predict response [24,25]. Wobrock 2015 negative trial (n=157) tempered earlier enthusiasm.
- **Auditory hallucinations**: low-frequency rTMS to left temporoparietal junction reduces hallucinations modestly (g ≈ 0.4); younger age and shorter illness duration predict response [25].
- **Autism**: small open-label and crossover trials by Casanova and Sokhadze (DLPFC low-frequency rTMS) show effects on event-related potentials, error monitoring, gamma oscillations, and autonomic measures, with limited but suggestive behavioral signal [26]. No FDA-approved indication. Biotype-stratified autism TMS trials are not yet at scale.

---

## 2. Transcranial electrical stimulation (tES)

### 2.1 tDCS for depression

The Brunoni/Loo individual patient data meta-analysis pooled 6 sham-controlled RCTs (n=289) and found active anodal-left/cathodal-right dlPFC tDCS superior to sham for response (34% vs 19% pooled) with NNT around 7 [27]. The updated 2023 IPD analysis confirmed the active-vs-sham effect with NNT 8 for response and 12 for remission [28]. Predictors of better response: bipolar diagnosis, comorbid anxiety. Predictors of worse response: higher baseline severity, treatment resistance. BDNF Val66Met effects on tDCS clinical outcome are inconsistent across studies [29].

The **Flow Neuroscience EMPOWER trial** (FL-100 device) enrolled 174 patients in a fully remote, multi-site, double-blind RCT and reported 58% remission in the active arm at week 10 versus roughly 20% sham [30]. The FDA granted premarket approval (PMA) on 8 December 2025, making FL-100 the first at-home brain stimulation device approved for moderate-to-severe MDD [30,31]. This sets the regulatory precedent for at-home, sensor-paired neuromodulation that Cytoscope can plausibly extend.

### 2.2 tDCS for schizophrenia negative symptoms

Brunelin and colleagues at Lyon demonstrated that bilateral frontotemporoparietal tDCS reduces auditory hallucinations and negative symptoms; effect sizes are modest (g ≈ 0.3 to 0.5) and response is heterogeneous. Baseline left temporoparietal hyperactivation on fMRI predicts hallucination response [32].

### 2.3 tACS for working memory, sleep, schizophrenia

- **Reinhart 2019 (Nat Neurosci)**: frequency-individualized theta-gamma tACS restored working-memory performance in adults aged 60-76 to younger-adult levels; the personalized frequency (each participant's own theta peak) was central [33].
- **Frohlich UNC trials**: 10-Hz alpha tACS in schizophrenia with auditory hallucinations reduced general psychopathology and depressive symptoms but not hallucinations per se in the primary endpoint; significant correlation between alpha power increase and symptom improvement supported a target-engagement mechanism [34].
- **Closed-loop slow-wave tACS during sleep** (Ketz, Jones and colleagues) augments slow oscillations and improves overnight memory consolidation in healthy adults [35].

### 2.4 tRNS, temporal interference, HD-tDCS

- **Transcranial random noise stimulation (tRNS)** shows modest effects on working memory and dyscalculia; biotype-stratification literature is thin.
- **Temporal interference stimulation (tTIS)**, introduced by Grossman, Boyden and colleagues in 2017, uses two interfering kHz fields to produce a low-frequency envelope at depth without driving cortical neurons. Wessel, Hummel and colleagues (Nat Neurosci 2023) demonstrated noninvasive theta-burst tTIS of the human striatum, with fMRI confirmation of focal activation and improved motor learning in older adults [36]. Striatal tTIS is the most directly relevant target for addiction and reward-circuit biotypes.
- **HD-tDCS personalization**: Bikson, Thielscher, and colleagues showed that fixed-current tDCS yields 3-fold variation in delivered electric field across individuals; reverse-calculation electric-field modeling individualizes current dose so all subjects hit a target field strength (e.g., 1 V/m) at the region of interest. This converts tDCS from a one-size-fits-all device into a dose-personalized one [37].

---

## 3. Focused ultrasound (FUS / LIFU)

### 3.1 Mechanism and target advantage

FUS uses converging acoustic beams to deposit energy at a focal point millimeters in diameter without depositing significant energy along the path. Low-intensity FUS (LIFU) modulates neural activity through mechanical effects on mechanosensitive ion channels and lipid bilayers, without thermal ablation. The depth advantage is decisive: FUS can target amygdala, nucleus accumbens, thalamus, and subgenual cingulate noninvasively, regions TMS cannot reach focally. The personalization requirement is correspondingly steeper: skull aberration correction and individualized acoustic modeling are required for accurate targeting.

### 3.2 MRgFUS capsulotomy (high-intensity, ablative)

Insightec ExAblate MRgFUS is FDA-approved for essential tremor (2016) and tremor-dominant Parkinson's disease (2018, expanded 2021). For psychiatric indications, the trajectory is:

- Jung et al. (2020, Mol Psychiatry): MRgFUS anterior capsulotomy in 11 refractory OCD and 6 refractory MDD patients; sustained response at 2 years [38].
- Davidson et al. (2020, J Psychiatry Neurosci): bilateral capsulotomy via MRgFUS in 6 refractory OCD patients [39].
- Korea University 10-year follow-up (Chang et al. 2024, Mol Psychiatry): sustained efficacy for refractory OCD at decade-scale follow-up [40].

FDA clearance for OCD remained pending under an IDE study (NCT06131502) as of late 2024 to mid 2026 [41]. The Insightec-led OCD pivotal is the lead psychiatric MRgFUS pathway.

### 3.3 Low-intensity FUS (LIFU) for depression and anxiety

Low-intensity neuromodulation rather than ablation. Active programs and trial signals:

- **Openwater Open-LIFU 2.0** (University of Arizona, 2024 to 2025): targeting anterior medial PFC (default mode network) for depression; 11 ten-minute sessions over 3 weeks in 20 patients showed depression severity reductions in 45-60% of subjects on standard scales (open-label, no sham) [42]. Total treatment time under 2 hours.
- **UCLA LIFUP for GAD** (NCT04557891, Bystritsky group): low-intensity focused ultrasound pulsation to amygdala for generalized anxiety disorder.
- **Chou et al. (2024)**: single-session LIFU to left amygdala reduced amygdala activation during a threat task and self-reported state anxiety [43].
- **Sanguinetti and colleagues**: LIFU to right inferior frontal gyrus modulates mood and default mode network connectivity in healthy volunteers; pilot data extended to depression [44].
- **Stanford sonothalamotomy and Pinto-Orellana TRD work**: emerging early-phase signals targeting thalamic nuclei for depression and anxiety; primary data not yet published in peer-reviewed form as of May 2026.

### 3.4 Biotype-targeted FUS

FUS is *more* target-dependent than TMS because focal volumes are smaller. The same logic that drives biotype-stratified TMS applies with stronger force: amygdala-anchored anxiety biotypes (Drysdale 1 / Williams threat circuit) point to amygdala LIFU; nucleus accumbens / striatal reward biotypes point to NAcc LIFU or striatal tTIS; subgenual / default mode biotypes point to mPFC LIFU. Trials matching biotype to FUS target are early-phase (open-label, n ≈ 20). No biotype-by-FUS response RCT has been published.

---

## 4. Transcutaneous vagus nerve stimulation (tVNS)

### 4.1 Modalities and approvals

- **Cervical nVNS (electroCore gammaCore)**: FDA-cleared for acute migraine (2017), episodic cluster headache prevention (2018), paroxysmal hemicrania and hemicrania continua (2021). No FDA clearance for depression as of May 2026, but multiple investigator-initiated trials.
- **Auricular taVNS**: stimulates the auricular branch of the vagus nerve via the cymba conchae or tragus. Numerous research-grade devices (NEMOS, Parasym, Nurosym). Off-label use in depression, PTSD, inflammatory bowel disease, post-stroke recovery.

### 4.2 Mechanism

Afferent vagal fibers project to nucleus tractus solitarius → locus coeruleus / noradrenergic system → cortex, modulating arousal, cognitive control, and mood. Descending vagal efferent fibers engage the cholinergic anti-inflammatory pathway via spleen, suppressing pro-inflammatory cytokines (TNF-α, IL-6) [45].

### 4.3 HRV-stratified response (autonomic biotype)

Baseline heart rate variability, especially RMSSD, predicts taVNS response. High-RMSSD subgroups show paradoxical responses (heart rate increases, vagally mediated HRV decreases) under active taVNS, suggesting saturation of vagal tone; low-RMSSD subgroups show classic vagal-enhancement responses and clinical benefit [46]. This is one of the cleanest autonomic-biotype-by-neuromodulation findings in the literature and lends itself directly to wearable PPG/ECG monitoring.

### 4.4 Inflammation-stratified response

Patients with elevated baseline CRP or IL-6 show larger anti-inflammatory and clinical responses to tVNS for depression and inflammatory conditions [45]. This is the "inflammatory biotype" of depression (Raison/Miller framework) extending into neuromodulation.

### 4.5 Stress-circuit biotypes and closed-loop respiratory-paired tVNS

Anxiety patients with elevated amygdala reactivity respond better to taVNS, with the auricular branch engaging LC-NE and modulating fear circuits. Respiratory-gated taVNS (delivered on expiration to maximize vagal tone) is under evaluation for major depression (NCT04607226) [47].

---

## 5. Closed-loop and sensing-paired neuromodulation

### 5.1 EEG-state-dependent TMS

Zrenner, Ziemann, and Bergmann showed that real-time EEG-defined excitability states (mu-alpha trough vs peak in sensorimotor cortex) determine the magnitude and direction of TMS-induced plasticity in healthy motor cortex. Pulses delivered at the trough produce larger long-term potentiation-like effects [48,49]. Translation to depression: pilot studies of frontal alpha-phase-locked DLPFC TMS in MDD have shown feasibility and superior neurophysiological target engagement vs random-phase stimulation [50].

### 5.2 Brain-state-dependent tACS

Closed-loop slow-wave tACS during sleep (Jones, Ketz, and colleagues) is locked to detected up-states of the slow oscillation and enhances memory consolidation. Dose-response and slow-oscillation entrainment effects have been documented [35]. Frohlich and colleagues are developing closed-loop tACS for major depression locked to frontal alpha.

### 5.3 Adaptive DBS (Medtronic Percept BrainSense)

FDA approved 24 February 2025. The Percept platform senses subthalamic local field potentials and adjusts stimulation amplitude in real time based on beta-band power (a Parkinson's motor state biomarker). ADAPT-PD trial (n=68) supported single- and dual-threshold adaptive DBS [51]. Although DBS is invasive, the regulatory precedent matters: FDA has now blessed a sense-infer-modulate-resense loop for chronic brain stimulation. This is the template Cytognosis would extend to noninvasive modalities.

### 5.4 NeuroPace RNS

Closed-loop responsive neurostimulation, FDA-approved for drug-resistant epilepsy 2013. Median seizure reduction 53% at 2 years and 72% at 6 years [52]. Active investigation for bipolar depression (NCT07127913) and other psychiatric indications. Establishes the regulatory and engineering pathway for sense-then-stimulate devices.

### 5.5 General loop architecture

Sense (EEG, EMG, HRV, fNIRS, biofluid markers) → infer state (machine learning classifier producing a biotype score or dynamical state estimate) → modulate (TMS pulse, tDCS amplitude, tACS phase, LIFU sonication, tVNS burst) → resense (verify target engagement, adjust). All four noninvasive modalities can in principle be inserted into this loop. Today the bottleneck is the *sense* and *infer* legs, not the *modulate* leg. This is the gap Cytoscope addresses.

---

## 6. Per-disorder biotype-response summaries

### 6.1 Depression

- **SAINT/SNT** (rsfMRI-guided personalized iTBS): 79% remission in TRD (n=29 RCT) [4]. Best evidence for biotype-stratified neuromodulation, single trial, replication pending.
- **B-SMART-fMRI** (cognitive biotype) [13]: TMS produced early restoration of cognitive control circuit connectivity and behavior in the cognitive-biotype subgroup; n=43 veterans.
- **Drysdale 2017 dmPFC rTMS** [2]: 82% vs 25% response across biotypes 1 vs 2.
- **Flow Neuroscience tDCS EMPOWER** [30]: 58% remission at-home, n=174, FDA-approved December 2025.
- **Openwater LIFU** [42]: 45-60% response in open-label depression trial, n=20.
- **fMRI-guided rTMS for depression and PTSD RCT** (Phillips et al. 2024-2025) [14]: personalized targeting outperforms anatomical landmark.

### 6.2 Anxiety

- TMS for generalized anxiety disorder shows modest pooled effect (Hedges' g ≈ 0.3 to 0.6) for right dlPFC low-frequency rTMS [53].
- LIFU to amygdala reduces threat reactivity in single-session studies; n=20 to 25 ongoing trials at UCLA, University of Arizona [43].
- tVNS for anxiety: small RCTs show modest effects, with stronger signal in high-baseline-anxiety / low-HRV subgroups [46].

### 6.3 OCD

- BrainsWay deep TMS (H7-coil) FDA-cleared 2018; pooled response rate ~45% vs ~30% sham. Predictors: lower baseline severity, shorter illness duration [54].
- MRgFUS capsulotomy for refractory OCD (Jung 2020 [38], Chang 2024 10-year follow-up [40]) sustained response at 10 years; pivotal trial under FDA IDE.
- Biotype data limited; OCD subtypes (contamination/checking/hoarding) show some differential response to deep TMS.

### 6.4 PTSD

- TMS for PTSD: heterogeneous protocols; right dlPFC low-frequency and left dlPFC iTBS both used; pooled effect g ≈ 0.4 to 0.7.
- fMRI-guided personalized targeting of right dlPFC-amygdala connectivity (Phillips et al. 2025) improved PCL-5 versus sham in 50-patient RCT [14]. Threat-circuit biotype is the operative stratifier.

### 6.5 Addiction

- BrainsWay deep TMS H4-coil FDA-cleared for smoking cessation 2020. Quit rate ~28% at 6 weeks vs ~12% sham [12]. Moderators: age <40, shorter smoking history, salience network connectivity.
- TMS for alcohol use disorder: small RCTs of left dlPFC and medial PFC stimulation reduce craving; effects on relapse less consistent [55].
- Cocaine: Italian group (Pettorruso, Terraneo) reported reduced cocaine use with high-frequency left dlPFC rTMS; replication pending.
- Striatal tTIS [36] is the most promising emerging modality for addiction because it accesses NAcc noninvasively.

### 6.6 Schizophrenia

- High-frequency left dlPFC rTMS for negative symptoms: meta-analytic g ≈ 0.3 to 0.5 [25]; younger age, shorter duration predict response.
- Low-frequency left TPJ rTMS for auditory hallucinations: g ≈ 0.4; younger age predicts response.
- tDCS bilateral frontotemporoparietal (Brunelin) for hallucinations and negative symptoms: g ≈ 0.4; replication mixed.
- Frohlich alpha tACS [34]: did not reduce hallucinations in primary endpoint but reduced general psychopathology; target engagement validated.
- Biotype data for schizophrenia neuromodulation is the weakest of the major disorders.

### 6.7 Autism

- Small Casanova/Sokhadze series of low-frequency DLPFC rTMS [26]: effects on ERPs, gamma oscillations, error monitoring, autonomic measures.
- Effect sizes small to moderate, no FDA approval.
- Biotype-stratified autism TMS trials are not yet at scale; EEG biotypes (Loo, Webb, McPartland) are the natural stratification axis.

---

## 7. The Drysdale 2017 paper in detail

Drysdale et al. (2017, Nature Medicine) [2] applied regularized canonical correlation analysis (rCCA) to 17-item HDRS items and 258 functional connectivity features from rsfMRI in a discovery cohort of 220 MDD patients and 220 controls. Hierarchical clustering on rCCA-derived feature combinations identified four biotypes. The biotypes were:

1. Anxious-arousal-dominant, characterized by reduced frontoamygdala connectivity (reading: weak top-down regulation of threat circuits).
2. Anhedonia-dominant, characterized by reduced frontostriatal and thalamic connectivity (reading: weak reward circuit engagement).
3. Mixed anhedonia + anxiety with frontostriatal hyperconnectivity.
4. Severe anxious-avoidance with frontoamygdala hyperconnectivity.

The dmPFC rTMS cohort (n=154) showed the 82%/25%/61%/30% response pattern by biotype, sharply differential. The implication for the field was that connectivity biotypes carry predictive information beyond clinical phenotype.

Replication and current status:

- Dinga et al. (2019, NeuroImage: Clinical) [6]: failed to replicate the cluster structure in an independent sample (n=187); argued the cluster solution was statistically indistinguishable from a unimodal distribution.
- Multiple groups (Williams/Tozzi 2024 [5], Fenster, Etkin) have since moved away from hard cluster solutions toward continuous circuit dimension scores; these dimensions (threat, reward, default mode, salience, cognitive control) carry the predictive signal more reliably and replicate across cohorts.
- The biotype-by-TMS *prediction* logic survives; the *four-cluster* solution does not.

Honest grant language: "Drysdale 2017 established the foundational evidence that resting-state circuit features stratify TMS response, with up to threefold differences in response rate across subgroups. The specific four-cluster solution did not replicate (Dinga 2019), but subsequent work using continuous circuit dimension scores (Williams/Tozzi 2024) has reproduced the predictive utility in larger cohorts. The Stanford SAINT trial (Cole/Williams 2022) demonstrated that personalizing the dlPFC target via individual rsfMRI yields 79% remission in TRD versus 13% sham, the strongest single piece of biotype-by-neuromodulation evidence."

---

## 8. Cross-disorder biotype-by-modulation patterns

**What works as a stratification axis (across modalities):**

- **sgACC-dlPFC anticorrelation** for TMS antidepressant response. Replicated across multiple sites and cohorts. Effect size moderate (r ≈ 0.3 to 0.5) univariately, larger in multivariate models.
- **Default mode network** baseline connectivity for TMS, tDCS, LIFU depression response.
- **Cognitive control circuit** (dlPFC-dACC engagement) for TMS in TRD with cognitive symptoms (B-SMART-fMRI).
- **Threat circuit** (right dlPFC-amygdala) for personalized TMS in PTSD.
- **Salience network connectivity** for deep TMS in smoking cessation.
- **Baseline HRV / RMSSD** for tVNS response (autonomic biotype).
- **Baseline CRP / IL-6** for tVNS and possibly tDCS response (inflammatory biotype).
- **Symptom subtypes** (anhedonia, anxious arousal, cognitive control deficits) as proxies for underlying circuit biotypes.
- **Individual alpha peak frequency** and **TMS-EEG N100** as response predictors for TMS in depression.

**What fails or is weak:**

- **Structural MRI alone**: gray matter volumes, cortical thickness do not reliably stratify response. Some signal for hippocampal volume in tDCS, but small.
- **Polygenic risk scores alone**: no replicated PRS-by-neuromodulation moderator at clinically useful effect sizes.
- **BDNF Val66Met alone**: inconsistent across studies for clinical outcome; more robust for mechanistic biomarkers.
- **The original Drysdale four-cluster categorical solution**: did not replicate. Continuous dimensions did.
- **Clinical symptom severity alone**: weak predictor; severity does not capture circuit substrate.

---

## 9. The wearable biomarker bottleneck

The entire biotype-stratified neuromodulation argument runs into the same operational wall: stratification today requires research-grade resting-state fMRI (≥10 minutes, 3T MRI, motion-corrected, registered to a connectome atlas). This is incompatible with primary care, with at-home dosing, and with closed-loop adjustment in real time. The economics make biotype-stratified TMS feasible only at academic centers and high-end specialty clinics.

**What a wearable like Cytoscope could replace or augment:**

- **rsfMRI-derived dlPFC-sgACC anticorrelation** → high-density frontal fNIRS plus EEG approximation (functional connectivity in the 0.01-0.1 Hz hemodynamic band).
- **Default mode network connectivity** → eyes-closed resting EEG default-mode signatures (alpha, low-beta cross-region coherence).
- **Cognitive control circuit engagement** → frontal theta during a 5-minute Go/NoGo task measured by EEG.
- **Threat circuit activation** → amygdala-proxy autonomic signals (skin conductance, HRV asymmetry) plus frontal alpha during threat imagery.
- **Salience network** → mid-cingulate-frontal theta-beta during interoceptive attention tasks.
- **Autonomic biotype (HRV)** → continuous wearable PPG/ECG, already gold-standard in consumer devices.
- **Inflammatory biotype (CRP/IL-6)** → finger-stick or wearable biofluid sensors (emerging).

**Adaptive closed-loop architecture:**

1. **Sense biotype state**: continuous EEG + fNIRS + PPG + (optional) biofluid markers stream a multivariate biotype score.
2. **Choose modulation target**: a learned policy (machine learning model trained on Cytoscope cohort + public datasets) maps the biotype score to a recommended modulation modality, target, and parameter set. For example: high anhedonia + low reward-circuit engagement → striatal tTIS; high threat + low frontal alpha → amygdala LIFU; high default mode hyperconnectivity + low sgACC anticorrelation → personalized dlPFC iTBS.
3. **Modulate**: deliver TMS, tDCS, LIFU, or tVNS via partnered hardware (Magstim, NeuroStar, Brainsway, Flow Neuroscience, Openwater, electroCore, Parasym).
4. **Resense**: same wearable streams pre/post and within-session metrics to confirm target engagement and adjust dose.

The strongest single argument for the Cytoscope-plus-noninvasive-neuromodulation pairing is that the *modulate* leg of the loop is FDA-approved across all four modalities (TMS, tDCS, LIFU under expanded indications, tVNS), but the *sense* and *infer* legs are still trapped in academic MRI scanners. The wearable closes that gap.

---

## 10. Implications for Cytoscope and the X-Labs proposal

### 10.1 Cytoscope + closed-loop TMS (specialty clinic product)

- **Pre-treatment**: 20-minute Cytoscope session yields a multivariate biotype score with EEG + fNIRS surrogates for sgACC-dlPFC anticorrelation, default mode connectivity, cognitive control engagement.
- **Targeting**: score feeds a personalized targeting recommendation for figure-of-eight or deep TMS, replacing or supplementing the rsfMRI step.
- **Within-session**: real-time EEG-state-locked iTBS pulses (Zrenner-Ziemann model) for biotypes where phase-locking improves plasticity.
- **Post-treatment**: Cytoscope tracks recovery trajectory and triggers maintenance dosing.
- **Phase 1 validation**: head-to-head Cytoscope-guided vs rsfMRI-guided SAINT in 60 to 100 patients; non-inferiority on remission at 4 weeks.
- **Phase 2 validation**: 300-patient multi-site RCT, Cytoscope-guided SAINT vs standard rTMS, in TRD.

### 10.2 Cytoscope + at-home tDCS (Flow Neuroscience integration)

- The FL-100 device was FDA-approved December 2025 for moderate-to-severe MDD at home [30]. It is the regulatory and commercial template.
- **Cytoscope addition**: continuous EEG + HRV streams a daily biotype state; the device app titrates session duration, anode/cathode placement, and current dose to the inferred state (within FDA-cleared parameter bounds).
- **Phase 1 validation**: 100-patient open-label cohort comparing standard fixed-protocol FL-100 to Cytoscope-titrated FL-100.
- **Phase 2 validation**: 400-patient pragmatic RCT; primary endpoint MADRS at week 10.
- **Commercial logic**: at-home tDCS market is the largest near-term opportunity for biotype-stratified neuromodulation because the marginal cost of personalization (sensor stream + algorithm) is low and the volume is high.

### 10.3 Cytoscope + LIFU clinic

- LIFU programs (Openwater, Bystritsky/UCLA, Insightec) need biotype-stratified target selection because focal volumes are millimeters and the wrong target produces no effect.
- **Cytoscope pre-procedure**: EEG + fNIRS biotype score recommends target (mPFC for default mode biotype, amygdala for threat biotype, NAcc for reward/addiction biotype).
- **Cytoscope intra-session**: real-time target engagement verification via EEG and fNIRS changes during sonication.
- **Phase 1**: 30 to 50 patient open-label, Cytoscope-guided amygdala LIFU for high-threat-biotype anxiety disorders.
- **Phase 2**: pivotal trial pathway with Openwater or Insightec partner.

### 10.4 Cytoscope + tVNS (consumer and post-acute)

- HRV-stratified taVNS response is the cleanest autonomic biotype in the literature [46].
- Cytoscope's continuous PPG/ECG and CRP-proxy biotype score selects responders and titrates daily tVNS dose.
- **Phase 1**: 200-patient remote trial with Parasym or NEMOS device + Cytoscope wearable.
- **Endpoint**: depression and anxiety symptom reduction at 8 weeks, with HRV-stratified subgroup analysis pre-specified.

### 10.5 Cross-cutting bets

- Continuous biotype monitoring permits **adaptive dose timing**: stimulate when biotype state is most receptive (Zrenner alpha phase logic generalized).
- Continuous monitoring permits **early-response detection** and **early-failure switching**: if biotype score has not shifted by week 2 of tDCS, switch to TMS or LIFU rather than completing a failing 10-week course.
- The same Cytoscope can be the *sense* leg for all four modalities, making the wearable the platform and the neuromodulation devices the modular treatment arms.

### 10.6 What the proposal needs to argue precisely

1. **Effect sizes are real but heterogeneous**: cite SAINT 79% [4], Drysdale 82% vs 25% [2], Flow EMPOWER 58% [30], MRgFUS OCD long-term [40], BrainsWay deep TMS 65% remission [21]. Avoid overclaiming any modality as definitive or transformative; cite sham controls and replication status.
2. **The bottleneck is sensing, not modulation**: four FDA-cleared modalities exist; biotyping is still trapped in academic MRI.
3. **Cytoscope closes the loop**: continuous, multimodal, biotype-state-aware wearable enables adaptive personalization across all four modalities.
4. **The Stanford SAINT result is the proof of concept**: when you personalize the target via individual neuroimaging, response rates jump 2-3x. Cytoscope generalizes this personalization to scalable, at-home, longitudinal use.
5. **Replication is incomplete**: SAINT is n=29 in a single trial; Drysdale's clusters failed replication; multiple promising biomarkers (BDNF Val66Met, BDNF protein) show inconsistent effects on clinical outcomes. The proposal must commit to multi-site validation and pre-registered replication of biotype-by-response findings before claiming clinical utility.

---

## References

1. Fox MD, Buckner RL, White MP, Greicius MD, Pascual-Leone A. Efficacy of transcranial magnetic stimulation targets for depression is related to intrinsic functional connectivity with the subgenual cingulate. Biol Psychiatry. 2012;72(7):595-603. doi:10.1016/j.biopsych.2012.04.028
2. Drysdale AT, Grosenick L, Downar J, et al. Resting-state connectivity biomarkers define neurophysiological subtypes of depression. Nat Med. 2017;23(1):28-38. doi:10.1038/nm.4246
3. Cole EJ, Stimpson KH, Bentzley BS, et al. Stanford Accelerated Intelligent Neuromodulation Therapy for Treatment-Resistant Depression. Am J Psychiatry. 2020;177(8):716-726. doi:10.1176/appi.ajp.2019.19070720
4. Cole EJ, Phillips AL, Bentzley BS, et al. Stanford Neuromodulation Therapy (SNT): A Double-Blind Randomized Controlled Trial. Am J Psychiatry. 2022;179(2):132-141. doi:10.1176/appi.ajp.2021.20101429
5. Tozzi L, Zhang X, Pines A, et al. Personalized brain circuit scores identify clinically distinct biotypes in depression and anxiety. Nat Med. 2024;30(7):2076-2087. doi:10.1038/s41591-024-03057-9
6. Dinga R, Schmaal L, Penninx BWJH, et al. Evaluating the evidence for biotypes of depression: Methodological replication and extension of Drysdale et al. (2017). NeuroImage Clin. 2019;22:101796. doi:10.1016/j.nicl.2019.101796
7. Cole EJ, et al. Sustained Efficacy of Stanford Neuromodulation Therapy in Open-Label Repeated Treatment. Am J Psychiatry. 2024. doi:10.1176/appi.ajp.20230113
8. Weigand A, Horn A, Caballero R, et al. Prospective Validation That Subgenual Connectivity Predicts Antidepressant Efficacy of TMS Sites. Biol Psychiatry. 2018;84(1):28-37. doi:10.1016/j.biopsych.2017.10.028
9. Cash RFH, Cocchi L, Lv J, Fitzgerald PB, Zalesky A. Functional Magnetic Resonance Imaging-Guided Personalization of Transcranial Magnetic Stimulation Treatment for Depression. JAMA Psychiatry. 2021;78(3):337-339. doi:10.1001/jamapsychiatry.2020.3794
10. Siddiqi SH, Schaper FLWVJ, Horn A, et al. Brain stimulation and brain lesions converge on common causal circuits in neuropsychiatric disease. Nat Hum Behav. 2021;5(12):1707-1716. doi:10.1038/s41562-021-01161-1
11. Liston C, Chen AC, Zebley BD, et al. Default mode network mechanisms of transcranial magnetic stimulation in depression. Biol Psychiatry. 2014;76(7):517-526. doi:10.1016/j.biopsych.2014.01.023
12. Dinur-Klein L, Dannon P, Hadar A, et al. Moderators of the response to deep TMS for smoking addiction. Front Psychiatry. 2022;13:920386. doi:10.3389/fpsyt.2022.920386
13. Mehta KR, Bayram E, Schatzberg AF, et al. A cognitive neural circuit biotype of depression showing functional and behavioral improvement after transcranial magnetic stimulation in the B-SMART-fMRI trial. Nat Ment Health. 2024;2:889-901. doi:10.1038/s44220-024-00271-9
14. Phillips RD, et al. Personalized fMRI-Guided TMS Targeting the Threat Neurocircuitry in PTSD: A Randomized Clinical Trial. Am J Psychiatry. 2025. doi:10.1176/appi.ajp.20250749
15. Cheeran B, Talelli P, Mori F, et al. A common polymorphism in the brain-derived neurotrophic factor gene (BDNF) modulates human cortical plasticity and the response to rTMS. J Physiol. 2008;586(23):5717-5725. doi:10.1113/jphysiol.2008.159905
16. Jannati A, Block G, Oberman LM, Rotenberg A, Pascual-Leone A. Interindividual variability in response to continuous theta-burst stimulation in healthy adults. Clin Neurophysiol. 2017;128(11):2268-2278. doi:10.1016/j.clinph.2017.08.023
17. Blumberger DM, Vila-Rodriguez F, Thorpe KE, et al. Effectiveness of theta burst versus high-frequency repetitive transcranial magnetic stimulation in patients with depression (THREE-D): a randomised non-inferiority trial. Lancet. 2018;391(10131):1683-1692. doi:10.1016/S0140-6736(18)30295-2
18. Voineskos D, Blumberger DM, Rogasch NC, et al. Neurophysiological effects of repetitive transcranial magnetic stimulation (rTMS) in treatment resistant depression. Clin Neurophysiol. 2021;132(9):2306-2316. doi:10.1016/j.clinph.2021.05.008
19. Corlier J, Carpenter LL, Wilson AC, et al. The relationship between individual alpha peak frequency and clinical outcome with repetitive Transcranial Magnetic Stimulation (rTMS) treatment of Major Depressive Disorder (MDD). Brain Stimul. 2019;12(6):1572-1578. doi:10.1016/j.brs.2019.07.018
20. Bailey NW, Hoy KE, Rogasch NC, et al. Responders to rTMS for depression show increased fronto-midline theta and theta connectivity compared to non-responders. Brain Stimul. 2018;11(1):190-203. doi:10.1016/j.brs.2017.10.015
21. Tendler A, Goerigk S, Zibman S, et al. Deep TMS H1 Coil treatment for depression: Results from a large post marketing data analysis. Psychiatry Res. 2023;324:115179. doi:10.1016/j.psychres.2023.115179
22. Noda Y, Zomorrodi R, Vila-Rodriguez F, et al. Resting and TMS-EEG markers of treatment response in major depressive disorder: A systematic review. Front Hum Neurosci. 2022;16:880759. doi:10.3389/fnhum.2022.880759
23. Rogasch NC, Sullivan C, Thomson RH, et al. Analysing concurrent transcranial magnetic stimulation and electroencephalographic data: A review and introduction to the open-source TESA software. NeuroImage. 2017;147:934-951. doi:10.1016/j.neuroimage.2016.10.031
24. Aleman A, Enriquez-Geppert S, Knegtering H, Dlabac-de Lange JJ. Moderate effects of noninvasive brain stimulation of the frontal cortex for improving negative symptoms in schizophrenia: Meta-analysis of controlled trials. Neurosci Biobehav Rev. 2018;89:111-118. doi:10.1016/j.neubiorev.2018.02.009
25. Lorentzen R, Nguyen TD, McGirr A, et al. The efficacy of transcranial magnetic stimulation (TMS) for negative symptoms in schizophrenia: a systematic review and meta-analysis. Schizophr. 2022;8:35. doi:10.1038/s41537-022-00248-6
26. Sokhadze EM, Baruth JM, Sears L, et al. Prefrontal neuromodulation using rTMS improves error monitoring and correction function in autism. Appl Psychophysiol Biofeedback. 2012;37(2):91-102. doi:10.1007/s10484-012-9182-5
27. Brunoni AR, Moffa AH, Fregni F, et al. Transcranial direct current stimulation for acute major depressive episodes: Meta-analysis of individual patient data. Br J Psychiatry. 2016;208(6):522-531. doi:10.1192/bjp.bp.115.164715
28. Moffa AH, Martin D, Alonzo A, et al. Efficacy and acceptability of transcranial direct current stimulation (tDCS) for major depressive disorder: An individual patient data meta-analysis. Prog Neuropsychopharmacol Biol Psychiatry. 2020;99:109836. doi:10.1016/j.pnpbp.2019.109836
29. Brunoni AR, Padberg F, Vieira ELM, et al. Effects of tDCS on neuroplasticity and inflammatory biomarkers in bipolar depression. Prog Neuropsychopharmacol Biol Psychiatry. 2020;102:109925. doi:10.1016/j.pnpbp.2020.109925
30. Woodham R, Cordeiro LM, et al. US FDA approves home-delivered tDCS for treating depression. Brain Stimul. 2025. doi:10.1016/j.brs.2025.10.005
31. Flow Neuroscience. FL-100 FDA premarket approval announcement, 8 December 2025. https://www.flowneuroscience.us/
32. Brunelin J, Mondino M, Gassab L, et al. Examining transcranial direct-current stimulation (tDCS) as a treatment for hallucinations in schizophrenia. Am J Psychiatry. 2012;169(7):719-724. doi:10.1176/appi.ajp.2012.11071091
33. Reinhart RMG, Nguyen JA. Working memory revived in older adults by synchronizing rhythmic brain circuits. Nat Neurosci. 2019;22(5):820-827. doi:10.1038/s41593-019-0371-x
34. Mellin JM, Alagapan S, Lustenberger C, et al. Randomized trial of transcranial alternating current stimulation for treatment of auditory hallucinations in schizophrenia. Eur Psychiatry. 2018;51:25-33. doi:10.1016/j.eurpsy.2018.01.004
35. Ketz N, Jones AP, Bryant NB, Clark VP, Pilly PK. Closed-Loop Slow-Wave tACS Improves Sleep-Dependent Long-Term Memory Generalization by Modulating Endogenous Oscillations. J Neurosci. 2018;38(33):7314-7326. doi:10.1523/JNEUROSCI.0273-18.2018
36. Wessel MJ, Beanato E, Popa T, et al. Noninvasive theta-burst stimulation of the human striatum enhances striatal activity and motor skill learning. Nat Neurosci. 2023;26(11):2005-2016. doi:10.1038/s41593-023-01457-7
37. Caulfield KA, Indahlastari A, Nissim NR, et al. Transcranial Electrical Stimulation Motor Threshold Can Estimate Individualized tDCS Dosage From Reverse-Calculation Electric-Field Modeling. Brain Stimul. 2020;13(4):961-969. doi:10.1016/j.brs.2020.04.007
38. Jung HH, Kim SJ, Roh D, et al. Magnetic resonance-guided focused ultrasound capsulotomy for refractory obsessive compulsive disorder and major depressive disorder. Mol Psychiatry. 2020;25(5):1071-1080. doi:10.1038/s41380-020-0737-1
39. Davidson B, Hamani C, Rabin JS, et al. Magnetic Resonance-Guided Focused Ultrasound Capsulotomy for Treatment-Resistant Psychiatric Disorders. Neurosurgery. 2020;87(6):1314-1321. doi:10.1093/neuros/nyaa302
40. Chang KW, Jung HH, Chang JW, Kim CH. Long-term clinical outcome of a novel bilateral capsulotomy with focused ultrasound in refractory obsessive-compulsive disorder treatment. Mol Psychiatry. 2024;29:3168-3176. doi:10.1038/s41380-024-02799-9
41. ClinicalTrials.gov. NCT06131502. Sonication-based OCD Neurosurgical Intervention Via Capsulotomy.
42. Openwater. University of Arizona Study Finds Openwater's Open-LIFU 2.0 Device Achieves Significant Depression Symptom Reduction. Business Wire. 4 April 2025.
43. Chou T, Deckersbach T, Dougherty DD, Hooley JM. The effect of low-intensity focused ultrasound on the amygdala and emotional regulation. Front Neuroimaging. 2024;3:1580623. doi:10.3389/fnimg.2024.1580623
44. Sanguinetti JL, Hameroff S, Smith EE, et al. Transcranial Focused Ultrasound to the Right Prefrontal Cortex Improves Mood and Alters Functional Connectivity. Front Hum Neurosci. 2020;14:52. doi:10.3389/fnhum.2020.00052
45. Vázquez-Oliver A, et al. Transcutaneous Auricular Vagus Nerve Stimulation for Treating Emotional Dysregulation and Inflammation in Common Neuropsychiatric Disorders. Brain Sci. 2026;16(1):8. doi:10.3390/brainsci16010008
46. Tang Z, et al. Baseline heart rate variability as guide to transcutaneous auricular vagus nerve stimulation in depression. Mol Psychiatry. 2025. doi:10.1038/s41380-025-12689-6
47. ClinicalTrials.gov. NCT04607226. Effects of Respiratory-Gated Transcutaneous Vagal Nerve Stimulation in Major Depression.
48. Zrenner C, Desideri D, Belardinelli P, Ziemann U. Real-time EEG-defined excitability states determine efficacy of TMS-induced plasticity in human motor cortex. Brain Stimul. 2018;11(2):374-389. doi:10.1016/j.brs.2017.11.016
49. Bergmann TO, Lieb A, Zrenner C, Ziemann U. Pulsed Facilitation of Corticospinal Excitability by the Sensorimotor μ-Alpha Rhythm. J Neurosci. 2019;39(50):10034-10043. doi:10.1523/JNEUROSCI.1730-19.2019
50. Zrenner C, Ziemann U. Closed-Loop Brain Stimulation. Biol Psychiatry. 2024;95(6):545-552. doi:10.1016/j.biopsych.2023.09.014
51. Medtronic. FDA approval of BrainSense Adaptive DBS for Parkinson's disease. 24 February 2025.
52. Nair DR, Laxer KD, Weber PB, et al. Nine-year prospective efficacy and safety of brain-responsive neurostimulation for focal epilepsy. Neurology. 2020;95(9):e1244-e1256. doi:10.1212/WNL.0000000000010154
53. Cirillo P, Gold AK, Nardi AE, et al. Transcranial magnetic stimulation in anxiety and trauma-related disorders: A systematic review and meta-analysis. Brain Behav. 2019;9(6):e01284. doi:10.1002/brb3.1284
54. Carmi L, Tendler A, Bystritsky A, et al. Efficacy and Safety of Deep Transcranial Magnetic Stimulation for Obsessive-Compulsive Disorder: A Prospective Multicenter Randomized Double-Blind Placebo-Controlled Trial. Am J Psychiatry. 2019;176(11):931-938. doi:10.1176/appi.ajp.2019.18101180
55. Mishra BR, Nizamie SH, Das B, Praharaj SK. Efficacy of repetitive transcranial magnetic stimulation in alcohol dependence: a sham-controlled study. Addiction. 2010;105(1):49-55. doi:10.1111/j.1360-0443.2009.02777.x

# EEG and MEG Biotypes Across Six Psychiatric Disorders: A Deep Review for the Cytoscope Headset Proposal

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: researchers, stakeholders
> **Tags**: `research`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)

Prepared for: Cytognosis Foundation and Hervé Marie-Nelly, NSF X-Labs Phase 0 and ARPA-H PHO submissions
Date: 25 May 2026
Scope: Replicated and contested EEG and MEG signatures across depression (MDD, TRD), anxiety (GAD, panic, social, OCD), psychosis (schizophrenia, FEP, prodromal), PTSD, addiction (SUDs), and autism (ASD). Organized by signal type first, then per-disorder mapping under each signal, so the reader can compare across disorders before drawing per-disorder conclusions.

Style note: We flag single-lab versus multi-site replication status throughout, distinguish high-density laboratory EEG findings from those that are recoverable on consumer-grade montages, and avoid hype language. The active question for the proposal is which of these signals a wearable optical (or hybrid optical-EEG) headset could realistically recover and use as a per-user mental health coordinate.

---

## 1. Resting-State EEG Frequency Bands

### 1.1 Alpha (8 to 13 Hz)

Individual alpha peak frequency (IAF), alpha power, and alpha asymmetry are the three most studied resting EEG features in psychiatry. IAF is moderately heritable, stable within an individual across months, and shifts with arousal, age, and cognitive load [1]. Alpha power increases under eyes-closed rest and shows posterior dominance.

Anterior alpha asymmetry, defined as relative right-minus-left alpha power over frontal electrodes (F4 minus F3 or homologues), was popularized by Richard Davidson in the 1980s and 1990s as a putative trait marker of depression vulnerability, on the model that low left-frontal activation (reflected as relatively higher left-frontal alpha, since alpha is inversely related to local cortical activation) corresponds to reduced approach motivation [2]. The construct generated decades of follow-up work.

Replication status. The most recent meta-analysis by Kolassa and colleagues (2025) pooled 23 studies with 1,928 MDD participants and 2,604 controls and found a small but statistically significant grand mean effect, with no moderation by age, depression severity, or reference montage [3]. An earlier 2017 meta-analysis by van der Vinne and colleagues (16 studies, n = 1,883 MDD, 2,161 controls) reported a non-significant grand mean (d = minus 0.007) after resolving heterogeneity, although a Gender by Age by Severity interaction replicated prospectively [4]. The honest summary is that frontal alpha asymmetry is real on average but with effect sizes too small to be a standalone diagnostic. It carries adjunctive value when combined with other features, and is recoverable on consumer-grade frontal montages.

Individual alpha peak frequency. Lower IAF has been associated with treatment-resistant depression and with anxiety. Sidelinger and colleagues (2023) used the Muse 2 headband to show day-to-day IAF variability correlates with trait anxiety, with values comparable to high-density laboratory EEG, supporting IAF as one of the few consumer-grade biomarkers that holds up at the individual level [5].

Per-disorder mapping for alpha:
- Depression (MDD, TRD): small frontal asymmetry effect on average; reduced IAF in TRD; alpha power normalizes with response to ketamine and rTMS.
- Anxiety (GAD, panic, social, OCD): elevated posterior alpha in GAD has been reported but is inconsistent; IAF variability tracks anxiety.
- Psychosis (SCZ, FEP, prodromal): reduced IAF in chronic SCZ; alpha power reduced in some samples; reduced alpha reactivity to eye opening.
- PTSD: widespread reduction in alpha power reported across multiple studies; reduced posterior alpha is one of the more reproducible PTSD signals although still heterogeneous [6].
- Addiction: reduced alpha and elevated beta during withdrawal; alpha increases during craving in some substance subtypes.
- Autism: reduced relative alpha power is the most replicated finding (meta-analytic g = minus 0.35, k = 41 studies) [7].

### 1.2 Theta (4 to 8 Hz)

Frontal midline theta (FMT) at Fz reflects medial-frontal and midcingulate cortex activity during cognitive control, conflict monitoring, and error processing. Cavanagh and Shackman's 2014 meta-analysis showed FMT increases to conflict, errors, and punishment, and that this signal is amplified in trait-anxious individuals, consistent with hypervigilant control [8].

Theta-beta ratio (TBR), the ratio of low-frequency theta to higher-frequency beta over central or frontal sites, was historically the centerpiece of ADHD EEG research. The Neuropsychiatric EEG-Based Assessment Aid (NEBA) was FDA-cleared in 2013 based on Monastra et al.'s claim that TBR was elevated 1.3 to 1.5-fold in ADHD versus controls [9]. Subsequent multi-site replications and the American Academy of Neurology practice advisory (Gloss et al. 2016) concluded TBR has insufficient evidence for diagnostic use; recent multiverse analyses (Liechti and colleagues, 2026 medRxiv) show the effect is highly sensitive to methodological choices and the original effect size has shrunk substantially in better-controlled samples [10]. We treat TBR as a non-specific marker of cortical arousal, not as a psychiatric biomarker.

Per-disorder mapping for theta:
- Depression: elevated frontal theta in some MDD samples; theta-cordance after one week of antidepressant predicts response in multiple studies [11].
- Anxiety / OCD: increased FMT during conflict; resting FMT elevated in high trait anxiety [8].
- Psychosis: theta-band microcircuit abnormalities predict conversion in the NAPLS2 cohort of CHR-P individuals [12].
- PTSD: theta-band functional connectivity correlates with rumination and re-experiencing severity [6].
- Addiction: elevated theta during craving; abnormal theta-beta coupling in alcohol use disorder.
- Autism / ADHD: TBR historically claimed for ADHD; current consensus is too noisy for individual-level use.

### 1.3 Beta (13 to 30 Hz)

Elevated beta is a near-universal correlate of anxiety, hyperarousal, and stimulant intoxication. Reduced beta has been described in some depression subtypes and during sedation. Beta is also the signal of choice for motor cortex sensorimotor rhythm (SMR) work.

Per-disorder mapping for beta:
- Anxiety / panic: elevated frontal and central beta during eyes-closed rest; replicated across small studies but with poor effect sizes.
- Depression: reduced beta in some samples, increased in others. Heterogeneity reflects sample selection (anxious versus melancholic).
- Psychosis: increased beta during positive-symptom episodes; correlates with auditory hallucinations.
- PTSD: elevated beta in hyperaroused subtypes.
- Addiction: elevated beta is one of the more replicated SUD signals, linked to GABAergic disinhibition during withdrawal.

### 1.4 Gamma (above 30 Hz)

Resting gamma in surface EEG is small and contaminated by muscle artifact, so resting gamma findings are best treated with skepticism unless recorded with high-density EEG and aggressive artifact rejection. Evoked gamma (notably 40 Hz auditory steady-state response, covered in section 4) is the cleaner gamma signal.

Per-disorder mapping for gamma:
- Schizophrenia: reduced evoked gamma at 40 Hz is robust (section 4); resting gamma findings are more mixed.
- Autism: elevated resting gamma in two meta-analytic studies, although the field is roughly evenly split between increases and decreases. Both have been linked to PV interneuron / E-I imbalance models [7].
- Depression: gamma elevation in some samples post-ketamine; baseline gamma sometimes correlates with ketamine response.
- Other disorders: gamma findings are too noisy for individual-level use.

### 1.5 Delta (below 4 Hz)

Awake resting delta is small in healthy adults. Excess prefrontal delta in TRD has been reported by multiple groups; total delta during sleep is a different signal (section 2). The Korb et al. work on prefrontal cordance (a delta-band measure combining absolute and relative power) predicts antidepressant response with effect sizes that have held up across multiple lab replications, though the field has moved past cordance as a single measure [11].

Per-disorder mapping for delta:
- TRD: elevated awake prefrontal delta in some samples; predicts ketamine response.
- Schizophrenia: increased delta power in chronic SCZ correlates with cognitive impairment.
- PTSD: reduced sleep delta (slow-wave deficit; section 2).
- Autism: increased delta in some samples but not all.

### 1.6 Aperiodic 1/f Slope (Spectral Exponent)

The aperiodic component of the power spectrum follows a power-law decay (P proportional to 1/f^chi). Until Donoghue et al.'s 2020 Nature Neuroscience paper introducing the FOOOF / specparam algorithm, periodic and aperiodic activity were typically conflated in band-power analyses [13]. Steeper slopes (more negative exponents) are interpreted as reflecting GABAergic inhibition; flatter slopes are proposed to indicate a relative glutamatergic excitatory bias, supported by chemogenetic, pharmacological, and computational modeling work [14].

Donoghue's 2025 systematic review of aperiodic activity in clinical populations summarizes:
- Schizophrenia: mixed results, with several studies showing flatter slopes (excitatory bias) and others finding no difference. The flatter-slope finding is consistent with PV-interneuron deficit models.
- Autism: flatter slopes in resting state in multiple samples, consistent with E/I imbalance hypotheses. A 2025 medRxiv preprint (Voytek lab) extends this to task-related conditions [15].
- Depression: less studied; some reports of steeper slopes in MDD, opposite to SCZ and ASD.
- ADHD: flatter slopes reported in adults and children [13].
- Alzheimer's: combining 1/f slopes with simulation models proposes them as an E/I imbalance proxy [16].

The 1/f slope is recoverable on lower-density EEG and is increasingly favored as a "scalable" biomarker because it does not require oscillation extraction. The strongest cross-condition signal is in ASD, where flatter slopes are now reported across at least five labs.

Per-disorder mapping for 1/f slope:
- SCZ: flatter slopes (mixed); replication ongoing.
- ASD: flatter slopes, multiple replications.
- MDD: steeper slopes in some samples; field still small.
- ADHD: flatter slopes.
- PTSD, addiction: emerging literature, too small to summarize.

### 1.7 Resting-State EEG: Per-Disorder Summary

- Depression: small frontal alpha asymmetry effect; reduced IAF in TRD; elevated awake prefrontal delta; FMT and theta-cordance predict antidepressant response.
- Anxiety: elevated FMT; IAF variability tracks anxiety; elevated beta in GAD/panic.
- Psychosis: reduced IAF; increased beta during positive symptoms; flatter 1/f slope (mixed).
- PTSD: reduced alpha power; theta-band connectivity tied to symptom severity; reduced sleep slow-wave.
- Addiction: elevated beta; elevated theta during craving; reduced alpha during withdrawal.
- Autism: reduced relative alpha (g = minus 0.35); increased gamma (split); flatter 1/f slope.

---

## 2. Sleep EEG

Sleep EEG features have stronger psychometric reliability than wake resting EEG because the brain state is more constrained.

### 2.1 Sleep Spindle Density

Sleep spindles are 11 to 16 Hz thalamocortical oscillations during NREM2 sleep, generated in the thalamic reticular nucleus and projected to cortex via PV-positive thalamic relay circuits. Spindle density (spindles per minute of NREM2) has emerged as one of the most replicated EEG findings in psychiatry.

Schizophrenia: Ferrarelli and Tononi's 2007 paper first reported reduced spindle density in medicated chronic SCZ patients; subsequent meta-analysis (Manoach lab) pooled 14 studies (337 patients/relatives, 339 controls) and confirmed reduced spindle density in SCZ, first-episode psychosis, and unaffected family high-risk relatives, with effect sizes that increased with longer illness duration [17]. The finding has been replicated in adolescent early-onset SCZ and in unmedicated patients, ruling out a pure medication effect.

Autism: spindle density reductions have been reported in ASD, though with smaller and more heterogeneous samples than the SCZ literature. The interpretation is that thalamocortical PV-circuit function is impaired in both conditions, dovetailing with the gamma and aperiodic-slope findings.

Generalized anxiety disorder: one notable counterexample is the finding by Gruber and colleagues that spindle density is positively associated with worry in pediatric GAD, suggesting that spindle alterations are not unidirectional across disorders.

### 2.2 Slow-Wave Activity (SWA)

Slow-wave activity (0.5 to 4 Hz EEG power during NREM3 sleep) reflects cortical synaptic homeostasis. Reductions in SWA appear in multiple psychiatric conditions.

Depression: high delta sleep ratio (NREM cycle 1 SWA divided by NREM cycle 2 SWA) predicts antidepressant response (Kupfer et al., 1990s) [18]. Selective slow-wave deprivation has been studied as an experimental antidepressant manipulation.

PTSD: reduced low-frequency (slow oscillation / delta band) NREM power and increased light N1 sleep are common polysomnographic findings [19]. The reduction tracks symptom severity.

### 2.3 REM Density and REM Latency

REM density (eye movements per minute of REM) and REM latency (time to first REM) are classic Kupfer-era biomarkers in MDD. Short REM latency and elevated REM density predict response to SSRIs and SNRIs in multiple cohorts [20], and a 2025 paper shows REM density predicts ketamine response in TRD [21].

### 2.4 Sleep EEG: Per-Disorder Summary

- Depression / TRD: reduced REM latency, elevated REM density predict pharmacotherapy response; high delta sleep ratio predicts response.
- Schizophrenia: reduced spindle density (replicated, multi-lab).
- Autism: reduced spindle density (replicated but smaller literature).
- PTSD: reduced slow-wave activity; altered spindle dynamics.
- Anxiety, addiction: less specific; spindle density may correlate with worry in GAD.

---

## 3. Event-Related Potentials (ERPs)

### 3.1 P300 / P3b

P300 is a positive deflection 250 to 500 ms after task-relevant or oddball stimuli, with maximum amplitude over centroparietal sites. It indexes attentional resource allocation and stimulus categorization.

Schizophrenia: reduced P3b amplitude and prolonged latency are among the most replicated ERP findings in psychiatry. Meta-analyses (Bramon, Turetsky) consistently show large effect sizes (g approximately 0.85), with reductions present in unaffected first-degree relatives, supporting endophenotype status [22, 23]. The COGS-2 study (n above 1,400) confirmed P300 deficits across multiple sites and showed modulation by sociodemographic factors [24].

Prodromal psychosis: P300 reductions in CHR-P individuals predict conversion to psychosis in NAPLS and several other prospective cohorts.

Addiction: reduced P300 amplitude is replicated in alcohol use disorder, opioid use disorder, and stimulant use disorder; the deficit is present in unaffected high-risk relatives (Begleiter / Porjesz work), supporting P300 as a vulnerability marker for SUDs broadly [25].

Depression and ADHD: smaller P300 reductions; less specific.

### 3.2 Mismatch Negativity (MMN)

MMN is a 100 to 250 ms negative response to deviant auditory stimuli within a standard sequence, independent of attention. It indexes pre-attentive auditory deviance detection and is generated by NMDA receptor-dependent superficial-layer cortical microcircuits, making it a translational biomarker for NMDA hypofunction [26].

Schizophrenia: reduced MMN amplitude is one of the most reliable and best-replicated EEG findings in psychiatry. Meta-analysis by Erickson, Ruchsow, and colleagues shows large effect sizes (g approximately 1.0) for duration-MMN and frequency-MMN in chronic SCZ, with smaller deficits in FEP and CHR-P [27].

Prodromal psychosis: reduced MMN in CHR-P individuals predicts subsequent conversion to psychosis. NAPLS-2 and several independent cohorts have replicated this; MMN is one of the leading candidate biomarkers for prodromal detection. Naatanen's late-career synthesis describes MMN deficits as "a breakthrough biomarker" for psychosis prediction [28].

Autism: reduced MMN to complex auditory deviants has been reported in multiple ASD samples but is less consistent than in SCZ.

Visual MMN (vMMN): a 2024 meta-analysis by Mazer and colleagues shows reduced vMMN in SSD, paralleling auditory findings [29].

### 3.3 N1 / P50 Sensory Gating

P50 sensory gating is measured as the suppression of the P50 evoked response to the second of two paired auditory clicks (S2/S1 amplitude ratio, with healthy gating producing ratios near 0.4 to 0.5). Reduced gating (higher S2/S1) reflects failure of inhibitory filtering.

Schizophrenia: P50 gating deficits are heritable (around 68%) and present in unaffected first-degree relatives, supporting endophenotype status [30]. The Adler / Freedman line of work linked P50 gating to alpha-7 nicotinic acetylcholine receptor function, motivating targeted pharmacology. However, replication has been imperfect: one attempted replication with slightly modified parameters failed to find strong gating in healthy controls. The current view is that P50 gating is a useful research probe but not a stand-alone diagnostic.

PTSD: P50 gating deficits have been reported in urban-violence PTSD samples; effect sizes are smaller and less consistent than in SCZ [31].

N100 sensory gating: similar paradigm; reduced gating in SCZ; auditory N100 amplitude deficits in CHR-P predict psychosis conversion in NAPLS-2.

### 3.4 Error-Related Negativity (ERN)

ERN is a frontocentral negative deflection 50 to 100 ms after error commission, generated in dorsal ACC / midcingulate cortex.

OCD: enhanced ERN amplitude is one of the most reliable ERP findings outside SCZ. Riesel's 2019 meta-analysis confirmed enhanced ERN as a candidate endophenotype for OCD, present in unaffected first-degree relatives [32]. Effect sizes are moderate (g approximately 0.5).

Generalized anxiety disorder: enhanced ERN predicts first-onset GAD in adolescent females (Meyer et al., prospective cohort) [33], suggesting predictive utility above the ROC-AUC of approximately 0.64 reported for diagnostic discrimination [34].

Depression: smaller and less consistent ERN reductions in some samples.

### 3.5 Late Positive Potential (LPP)

LPP is a sustained positive deflection 400 to 1,000 ms following emotional stimuli, maximum over centroparietal sites. It indexes sustained attention to motivationally salient stimuli.

PTSD / anxiety: larger LPP to negative or trauma-relevant stimuli in PTSD and anxiety, although results are mixed in trauma-exposed samples [35]. The LPP during reappraisal indexes successful emotion regulation and shows reductions in MDD.

Depression: blunted LPP to positive stimuli in MDD; reduced LPP to reward predicts anhedonia.

### 3.6 Reward Positivity (RewP) / Feedback-Related Negativity (FRN)

RewP (also called feedback positivity) is a positive deflection 250 to 300 ms following positive feedback, smaller or reversed for negative feedback. Proudfit's 2015 review framed RewP as a biomarker for depression risk based on reward processing deficits [36].

Depression / anhedonic biotype: blunted RewP correlates with anhedonia and predicts increased depressive symptoms in longitudinal cohorts. The EMBARC trial (Trivedi, Pizzagalli, and colleagues) used reward-related EEG and fMRI biomarkers to predict response to sertraline versus placebo; baseline EEG features added incrementally to clinical prediction. A registered report p-curve analysis (Klawohn et al. 2020) showed the RewP-depression literature has evidential value but with some publication bias, supporting cautious optimism [37].

Addiction: altered RewP to drug-related stimuli; smaller field than depression literature.

### 3.7 Prepulse Inhibition (PPI)

PPI is the reduction in startle response when a weak prepulse precedes a startling stimulus by 30 to 500 ms. It is not strictly an ERP (it indexes startle EMG, not central EEG response) but is grouped with sensory gating measures.

Schizophrenia: PPI deficits are well-replicated, heritable (around 58%), and present in unaffected relatives. Multi-site replication (Swerdlow, Light) confirmed deficits across multiple cohorts [38]. PPI extends to OCD, Tourette, manic bipolar, panic disorder, and adult ASD, although effect sizes are smaller.

Autism: reduced PPI in adults with ASD; less consistent in children.

### 3.8 ERPs: Per-Disorder Summary

- Schizophrenia: reduced P3b, reduced MMN, reduced P50 gating, reduced PPI. These four together form the historical "schizophrenia endophenotype panel."
- Prodromal psychosis: reduced MMN and reduced N100 amplitude predict conversion (NAPLS-2).
- OCD: enhanced ERN.
- GAD / anxiety: enhanced ERN predicts onset.
- Depression: blunted RewP (anhedonic biotype); blunted LPP to positive stimuli.
- PTSD: enhanced LPP to threat; reduced P50 gating (smaller than SCZ).
- Addiction: reduced P300 (vulnerability marker for SUDs broadly).
- Autism: reduced MMN (less consistent than SCZ); reduced PPI in adults.

---

## 4. Evoked Oscillations and Steady-State Responses

### 4.1 40 Hz Auditory Steady-State Response (ASSR)

The 40 Hz ASSR is the entrained gamma-band response to click trains presented at 40 Hz. Generation depends on the interaction between cortical pyramidal cells and PV-positive basket / chandelier interneurons, making 40 Hz ASSR a translational probe for PV / GABA-A circuit integrity.

Schizophrenia: reduced 40 Hz ASSR power and phase-locking are among the most robust EEG findings in SCZ, with meta-analytic effect sizes around g = 0.8 and replication across more than 30 independent samples [39]. The reduction is present in chronic SCZ, FEP, and unaffected high-risk relatives. The biological interpretation (PV interneuron / NMDA hypofunction) connects directly to current pharmacological targets (KarXT, glycine transporter inhibitors).

Autism: reduced 40 Hz ASSR has been replicated in ASD, including in SHANK3 duplication and deletion syndromes, supporting a shared PV-circuit pathophysiology with SCZ.

Bipolar disorder: intermediate reductions; effect smaller than SCZ.

The 40 Hz ASSR is one of the strongest candidates for a multi-disorder biomarker grounded in mechanistic biology. It requires modest stimulus delivery (auditory click train) and modest EEG channel count (a single auditory-cortex-overlying electrode pair gets most of the signal), making it tractable for a wearable.

### 4.2 80 Hz ASSR

Some labs report differential involvement of high-gamma (80 Hz) ASSR in SCZ; the literature is small (under 10 papers) and replication is preliminary.

### 4.3 Steady-State Visual Evoked Potential (SSVEP)

SSVEP is the entrained occipital response to flickering visual stimuli at fixed frequencies (typically 6 to 30 Hz). In ASD, SSVEP work has documented enhanced or atypical lateral-inhibition signatures consistent with E/I imbalance in early visual cortex [40].

### 4.4 Evoked Oscillations: Per-Disorder Summary

- Schizophrenia: reduced 40 Hz ASSR (one of strongest, most-replicated EEG findings).
- Autism: reduced 40 Hz ASSR; altered SSVEP.
- Bipolar: intermediate 40 Hz ASSR reduction.
- Other disorders: less developed literature.

---

## 5. Microstates and Dynamic Functional Connectivity

EEG microstates are brief (60 to 120 ms) periods during which the scalp topography is quasi-stable, before a rapid transition to a different topography. Lehmann and colleagues described four canonical microstate classes (A, B, C, D) that account for most variance in resting EEG. Subsequent work has added classes E (centroparietal) and F (frontocentral) [41].

The four canonical classes have been mapped onto fMRI resting-state networks (Britz et al. 2010):
- Microstate A: auditory network
- Microstate B: visual network
- Microstate C: salience / default-mode hybrid
- Microstate D: dorsal attention network

Schizophrenia: microstate D is consistently shortened in SCZ and correlates with positive symptoms; microstate C is increased. The 2020 Nature Communications paper by da Cruz and colleagues (Koenig group) showed microstate dynamics differ in both SCZ patients and unaffected siblings, supporting endophenotype status. This is one of the more replicated dynamic-EEG findings in SCZ [42, 43].

PTSD: microstate E (centroposterior) is shortened in PTSD, with reduced occurrence and mean duration. Spectral decomposition of microstates improves classification accuracy (alpha-band SVM features yield approximately 76% PTSD classification) [44].

Mood and anxiety disorders: a 2023 meta-analysis by Murphy and colleagues found high inter-study variability and inconsistent microstate alterations across MDD and anxiety samples, cautioning against drawing strong individual-level conclusions [45].

Microstates can be computed from 19-channel EEG and are tractable on moderate-density wearables. They require only resting-state recordings of a few minutes.

---

## 6. Connectivity Measures

### 6.1 Phase-Locking, Coherence, Weighted Phase Lag Index

Phase-based connectivity measures quantify how consistently two brain regions oscillate in phase. Coherence is the classical metric but is contaminated by volume conduction; the weighted phase lag index (wPLI; Vinck et al., 2011) corrects for this and is the current preferred metric for sensor-space EEG/MEG functional connectivity.

Depression: increased clustering and modularity in 4 to 30 Hz wPLI networks; depression severity predictable from wPLI graph features in machine-learning pipelines [46].

PTSD: theta-band wPLI connectivity tracks rumination and re-experiencing severity.

Schizophrenia: reduced alpha and beta connectivity; increased delta-theta connectivity in some studies.

wPLI test-retest reliability is acceptable over two years at global and regional spatial resolutions, supporting biomarker candidacy [47].

### 6.2 Graph-Theoretic Measures

Clustering coefficient, characteristic path length, and small-world index derived from EEG/MEG connectivity matrices have been applied transdiagnostically. Findings are generally consistent with reduced small-worldness and increased path length in chronic SCZ, increased clustering in MDD, and reduced global strength in PTSD theta band [6].

### 6.3 MEG-Specific Connectivity

MEG offers source-space connectivity with better spatial resolution than scalp EEG (approximately 2 to 5 mm at best). Resting-state MEG networks recapitulate fMRI networks (default-mode, salience, dorsal attention, visual) at faster timescales. MEG resting-state functional connectivity in SCZ shows amplified medial prefrontal connectivity correlating with cognitive impairment, aberrant global connectivity correlating with positive symptoms, and aberrant auditory cortex connectivity correlating with hallucinations [48]. A 2024 dynamic-FC EEG study distinguished healthy controls, non-psychotic MDD, psychotic MDD, and SCZ at 73.1% accuracy using delta-theta and gamma metrics [49].

---

## 7. OPM-MEG Specific Advances (2024 to 2026)

Conventional SQUID-based MEG requires liquid-helium cooling, a magnetically shielded room, and a fixed dewar that restricts head movement. Optically pumped magnetometers (OPMs) are alkali-vapor sensors that achieve sensitivity comparable to SQUIDs at room temperature, in a sensor footprint roughly the size of a Lego brick. OPM-MEG arrays can be mounted in a wearable helmet, allowing free head movement and naturalistic task delivery.

### 7.1 Pediatric and Autism Applications

The QuSpin / Cerca Magnetics OPM-MEG system, deployed at the University of Nottingham, the Hospital for Sick Children (Toronto), and approximately 20 other sites globally as of 2025, has enabled the first wearable MEG studies in children including infants and toddlers, who cannot tolerate conventional MEG. Toronto's Hospital for Sick Children uses the system for autism and pediatric concussion research; a 2024 ScienceDaily-covered study showed OPM-MEG can map developing brain networks in children with millimeter precision [50, 51].

### 7.2 Wearable OPM-MEG Psychiatric Applications

Adult psychiatric OPM-MEG is still emerging. Epilepsy clinical use is the most advanced application, with multi-site studies showing OPM-MEG localizes interictal spikes with accuracy comparable to SQUID-MEG [52]. Adult depression and SCZ OPM-MEG studies have begun (Cerca Magnetics user base), but n is still small.

### 7.3 OPM-MEG versus fNIRS Comparison

For the Cytognosis Cytoscope program, OPM-MEG offers complementary information to fNIRS:
- OPM-MEG measures direct neuronal magnetic fields with millisecond temporal resolution and approximately 2 to 5 mm spatial resolution.
- fNIRS measures hemodynamic (blood oxygenation) responses with about 1 to 2 second temporal resolution and 1 to 3 cm spatial resolution.
- OPM-MEG requires a shielded environment (still bulky, although portable shielded rooms now exist); fNIRS works anywhere.
- OPM-MEG cost per system is approximately USD 500K to 1.5M; consumer-grade fNIRS systems cost USD 5K to 50K.
- OPM-MEG can resolve the same evoked oscillations (40 Hz ASSR, MMN) and microstates as EEG with cleaner source localization.

The plausible pairing is: OPM-MEG as a clinical-grade reference modality for biotype validation in research and clinic; consumer-grade hybrid optical-EEG headsets for at-home longitudinal monitoring.

---

## 8. Machine Learning and Deep Learning Biomarkers from EEG/MEG

### 8.1 Foundation Models for EEG (2024 to 2026)

The EEG foundation model wave began with BIOT (Yang et al., NeurIPS 2023) and accelerated through 2024 with LaBraM (ICLR 2024), EEGPT (Wang et al., 2024), and CBraMod (2024), culminating in NeuroLM (1.7 billion parameters, trained on more than 17,000 hours of EEG; the largest EEG-FM as of 2025) [53, 54]. Pretext tasks include masked signal reconstruction, contrastive learning, and dual-domain (frequency/phase) mask learning.

Benchmarks:
- EEG-FM-Bench (arxiv 2508.17742, 2025) provides systematic evaluation across BIOT, BENDR, LaBraM, EEGPT, CBraMod, CSBrain, REVE, Mantis, and Moment [55].
- NeuroAtlas benchmark covers clinical EEG and BCI applications.

Critical review: Wang and colleagues' 2025 review of EEG-FMs notes that while these models show strong transfer learning gains on small downstream datasets, they have not yet demonstrated psychiatric-disorder classification at clinically useful individual-level accuracy on independent test sites [56].

### 8.2 Disorder-Classification Accuracy Benchmarks

Recent representative results:
- MDD classification: 70 to 95% reported intra-site accuracy in deep-learning EEG papers; cross-site / cross-subject accuracy drops by 10 to 30 percentage points [57].
- SCZ classification: similar pattern, with within-site accuracy near 85 to 95% and cross-site dropping toward 65 to 75%.
- Multi-disorder discrimination: 73.1% across four groups (HC, non-psychotic MDD, psychotic MDD, SCZ) using dynamic FC features (Sun et al. 2024) [49].

### 8.3 The Replication / Generalization Problem

The dominant problem in EEG ML is that within-site, within-protocol models routinely achieve high accuracy that does not transfer to other sites or other recording protocols. The CRCC contrastive-learning approach (2025) reports a 10.7-point improvement in zero-shot site transfer balanced accuracy, but absolute cross-site accuracy is still modest [58]. Honest summary: published ML EEG psychiatric biomarkers should be treated as overfitted to their site of origin unless cross-site validation is demonstrated.

### 8.4 Transfer Learning from Healthy Data

Pretrained EEG-FMs trained on healthy data and fine-tuned on small psychiatric datasets are the current best practice. Pretraining on ImageNet-of-EEG (TUH, MOABB) gives 5 to 15 point downstream gains over training from scratch on small psychiatric cohorts.

---

## 9. TMS-EEG Biomarkers

TMS-EEG combines transcranial magnetic stimulation with simultaneous EEG to probe cortical excitability and inhibition directly, in any cortical region accessible to TMS.

### 9.1 TMS-Evoked Potentials (TEPs)

TEPs are the EEG responses to single TMS pulses, with components labeled N15, P30, N45, P60, N100, P180, and later. Different components index different inhibitory and excitatory contributions:
- N45: GABA-A mediated short-term inhibition
- N100: GABA-B mediated longer-term inhibition
- P30/P60: excitatory contributions

Casarotto, Massimini, and colleagues developed the perturbational complexity index (PCI), which uses TEPs to quantify the brain's integrated information capacity; PCI dissociates conscious from unconscious states with high accuracy [59].

### 9.2 Cortical Excitability and Inhibition (SICI, ICF, LICI)

Paired-pulse TMS protocols (short-interval intracortical inhibition, intracortical facilitation, long-interval intracortical inhibition) probe specific GABA-A, glutamatergic, and GABA-B circuits respectively. Rogasch and colleagues have systematized these measures as candidate biomarkers across psychiatric conditions [60].

### 9.3 TMS-EEG Biomarkers for Depression

Multiple lines of evidence show TEPs differ in MDD:
- L-DLPFC stimulation: larger N45, P60, N100 amplitudes in MDD
- Baseline P30, N45, P60, N100 amplitudes correlate with or predict response to TBS, rTMS, and magnetic seizure therapy
- TMS-EEG-derived E/I ratio has been proposed as a diagnostic biomarker for MDD (medRxiv 2026 preprint by Casarotto / Massimini group) [61, 62]

### 9.4 Closed-Loop Brain-State-Dependent TMS-EEG

Zrenner, Ziemann, and Bergmann have pioneered phase-locked TMS, where stimulation is delivered at specific phases of ongoing oscillations (mu rhythm in motor cortex, alpha in DLPFC). Zrenner's MDD work showed mu-alpha phase-synchronized rTMS/TBS in L-DLPFC produces stronger plasticity than open-loop stimulation [63, 64]. A randomized double-blind clinical trial of EEG-synchronized prefrontal TMS in TRD reported entrainment-dependent clinical response (2023 Brain Stimulation paper) [65].

For the Cytoscope program, TMS-EEG provides a complementary causal probe: where resting EEG measures circuit state, TMS-EEG measures circuit response to a controlled perturbation. The combination is more diagnostic than either alone, and closed-loop TMS represents the strongest current case for stimulation timing as a treatment lever.

---

## 10. The Wearable EEG Product Reality

The consumer EEG market has produced approximately 30 commercial devices over the last decade, but the gap between marketing claims and validated psychiatric biomarkers remains large.

### 10.1 Headband and Headphone-Format EEG

- Muse (InteraXon): 4 to 7 dry electrodes (Fp1, Fp2, TP9, TP10 plus reference); validated for IAF measurement comparable to high-density EEG (Sidelinger 2023) [5]; primary market is meditation feedback.
- Dreem 2 (discontinued 2022) / Muse S: sleep-staging accuracy near kappa 0.7 to 0.8 against polysomnography; Dreem 2 was the higher-density device but discontinued; Muse S is the surviving consumer sleep EEG product.
- Neurable MW75 Neuro: EEG sensors embedded in premium over-ear headphones; targets focus and stress metrics; nine published papers and a U.S. Army validation collaboration; psychiatric biomarker validation at the individual level is not yet demonstrated [66].
- Cognixion Axon-R: communication BCI for ALS / locked-in; not a psychiatric device.
- Omind, Brainn, Idun Guardian, Enophone, BrainBit, BioRobotics: various dry-electrode formats targeting wellness or research.

### 10.2 In-Ear EEG

IDUN Guardian: in-ear dry-electrode EEG validated for sleep staging (similarity scores 0.79 awake, 0.77 NREM against PSG) at SLEEP 2024 [67].

cEEGrid (developed by Debener / Bleichner): flexible printed multi-channel array placed around the ear; published validation as comparable to caps for auditory attention and subcortical auditory potentials [68]. Open-cEEGrid is commercially available via OpenBCI.

### 10.3 Headphone-Format and Hybrid Devices

Neurable's headphone EEG, the IDUN Guardian in-ear electrode, and the cEEGrid around-ear array are the three credible non-headband consumer EEG form factors. All can recover IAF, alpha/beta power, frontal asymmetry (Neurable only, due to electrode placement), and ERPs with adequate trial counts.

### 10.4 Replicable Psychiatric Biomarkers at the Individual Level

Most consumer EEG devices have not produced replicated psychiatric biomarkers at the individual level. The signals that hold up on consumer-grade hardware are:
1. IAF (alpha peak frequency): validated on Muse, Neurable, cEEGrid
2. Frontal alpha asymmetry: recoverable but with small effect sizes
3. Sleep staging: validated on Muse S, Dreem 2, IDUN
4. Coarse arousal / sleep architecture: validated on most devices

Signals that do not hold up well on consumer-grade hardware:
- MMN, P300 (require careful auditory stimulation and good signal quality)
- 40 Hz ASSR (requires auditory delivery; possible on headphone-EEG like Neurable)
- Microstates (require at least 19 channels with reasonable spatial coverage)
- Sleep spindles (require central electrodes; possible on Dreem)
- Aperiodic 1/f slope (recoverable but sensitive to noise)

For the Cytoscope hybrid optical-EEG headset, the most defensible EEG add-ons are alpha-band measures (IAF, asymmetry, power), frontal midline theta, evoked 40 Hz ASSR if headphone-format audio delivery is included, and aperiodic 1/f slope. Sleep EEG biomarkers may be a separate at-home night-time product.

---

## 11. Per-Disorder Synthesis: Top 2 to 3 Defensible EEG/MEG Biotypes

For each disorder we list the two to three EEG/MEG signatures with the strongest replication, the cleanest mechanistic interpretation, and the highest plausibility of recovery on a wearable optical-EEG hybrid headset.

### 11.1 Depression (MDD, TRD)

1. Blunted Reward Positivity (RewP) as anhedonic biotype marker. Replicated across multiple labs; ties to EMBARC biomarker work; recoverable on frontal-central EEG with simple reward task; mechanistic link to mesocorticolimbic dopamine.
2. REM density / REM latency abnormalities as pharmacotherapy response predictor. Replicated Kupfer-era finding; updated with ketamine response prediction (2025); requires sleep EEG.
3. Reduced individual alpha peak frequency and elevated prefrontal delta in TRD subgroup. Recoverable on consumer-grade frontal EEG; predicts ketamine and rTMS response.

### 11.2 Anxiety (GAD, panic, social, OCD)

1. Enhanced Error-Related Negativity (ERN) as endophenotype for OCD and predictor of GAD onset. Strong replication including Riesel 2019 meta-analysis and Meyer prospective adolescent cohort.
2. Elevated frontal midline theta during cognitive control. Replicated across multiple cohorts; tracks trait anxiety; recoverable on Fz electrode.
3. Elevated resting beta power. Less specific but replicated in panic and GAD; recoverable on any frontal-central montage.

### 11.3 Psychosis (SCZ, FEP, prodromal)

1. Reduced 40 Hz auditory steady-state response. One of the most replicated EEG findings in psychiatry; clean PV-interneuron / NMDA mechanism; recoverable on auditory cortex EEG with click-train stimulus.
2. Reduced mismatch negativity (MMN) and P3b. Together form the classic SCZ endophenotype pair; MMN reduction predicts conversion in CHR-P (NAPLS); both recoverable on standard auditory ERP protocols.
3. Reduced sleep spindle density. Replicated across multiple labs; present in unaffected relatives; requires sleep EEG with central electrodes.

### 11.4 PTSD

1. Reduced sleep slow-wave activity and altered NREM architecture. Replicated finding; tracks symptom severity; requires sleep EEG.
2. Theta-band functional connectivity tied to rumination and re-experiencing. Recoverable on 19-channel resting EEG with wPLI.
3. Reduced alpha power and altered microstate E dynamics. Recoverable on resting EEG; the more PTSD-specific microstate finding.

### 11.5 Addiction (SUDs)

1. Reduced P300 amplitude as broad SUD vulnerability marker. Replicated across alcohol, opioid, cocaine, cannabis; present in unaffected relatives (Begleiter / Porjesz).
2. Elevated resting beta power, especially during withdrawal. Replicated across multiple SUDs.
3. Altered RewP / cue-reactive ERPs to drug-related stimuli. Less replicated but mechanistically interpretable.

### 11.6 Autism (ASD)

1. Reduced relative alpha power and atypical alpha development. Meta-analytic g = minus 0.35 across 41 studies (Neuhaus / Webb 2023); replicated in pediatric samples [7].
2. Flatter aperiodic 1/f slope as E/I imbalance proxy. Replicated across at least five labs (Voytek lab and others); recoverable on consumer-grade EEG.
3. Reduced 40 Hz ASSR and altered evoked gamma. Replicated in syndromic and idiopathic ASD; SHANK3 case reports support PV-circuit mechanism. Reduced sleep spindle density is a fourth credible biotype.

---

## 12. Implications for the Cytoscope Platform

### 12.1 Where EEG/MEG Adds a Different Angle Than fNIRS-Class Optics

fNIRS measures cortical hemodynamic changes (HbO and HbR) with about 1 to 2 second temporal resolution; EEG and MEG measure direct neuronal electrical and magnetic activity with millisecond temporal resolution. The two modalities are largely complementary:

- fNIRS strengths: penetration depth (about 1 to 3 cm into cortex); spatial localization comparable to or better than scalp EEG; immunity to electrical and motion artifact; quantitative oxygenation (with TR-fNIRS or BOLD-fNIRS).
- EEG strengths: direct neuronal signal; access to oscillations (alpha, gamma) and ERPs (MMN, P300, RewP); no need for chromophore quantification; mature signal-processing toolchain.
- MEG strengths: source-space resolution; immunity to skull conductivity issues; access to subcortical signal in some cases; wearable OPM-MEG now available.

The biotypes most accessible only via EEG/MEG and not via fNIRS:
- 40 Hz ASSR (requires sub-100-ms temporal resolution)
- MMN, P300, RewP (ERPs need millisecond resolution)
- Sleep spindle density (NREM2-specific 11-16 Hz oscillation)
- Aperiodic 1/f slope (broadband spectral feature)
- Microstates (sub-second topographic transitions)

The biotypes most accessible via fNIRS and complementary to EEG:
- Prefrontal hemodynamic activation patterns (cognitive control circuits, reward circuits)
- Deep tissue oxygenation (subcortical and cortical, with sufficient depth resolution)
- Slow-timescale autonomic and vascular coupling

### 12.2 Should EEG Be Added to the Cytoscope Headset (Phase 1 or Phase 2)?

The argument for Phase 1 inclusion:
- IAF, FAA, FMT, and 1/f slope are recoverable on as few as four to eight dry electrodes (Muse-class form factor).
- ERPs (MMN, P300, RewP) need only frontal-central electrodes and clean signal, achievable on dry headphones-form-factor EEG.
- The biotypes most strongly anchored in mechanism (40 Hz ASSR, sleep spindle density) require EEG.
- A hybrid optical-EEG device produces a richer mental health coordinate than optical alone, with marginal cost increase (per-channel dry EEG is on order of USD 10 to 50 per channel in volume).

The argument for Phase 2 deferral:
- EEG signal quality on dry electrodes degrades during motion and over hours of wear; managing this requires investment.
- The Cytoscope first wedge (anhedonia / reward circuit) is well-served by fNIRS PFC measurement alone in Phase 1.
- Combining modalities adds engineering complexity, especially for synchronized acquisition and shared electronics.

Recommended position: Phase 1 includes 4 to 8 dry EEG electrodes for IAF, FAA, 1/f slope, and sleep monitoring. Phase 2 expands to headphone-format EEG with auditory stimulation for MMN, P300, 40 Hz ASSR. Phase 3 explores high-density wearable OPM-MEG as a clinical-grade reference modality at partner sites.

### 12.3 The Hybrid Optical-EEG Headset Case

The strongest scientific argument for the hybrid is that the disorders Cytognosis targets (depression, anxiety, psychosis, PTSD, addiction, autism) each have EEG/MEG biotypes that are partially independent of hemodynamic biotypes. A patient's "depression coordinate" recovered from fNIRS PFC reward-circuit measurements plus EEG RewP plus REM density is more predictive of treatment response than any one modality alone (EMBARC-style multi-modal models routinely outperform single-modality models by 5 to 15 percentage points in held-out validation).

The strongest commercial argument is that the wearable EEG market (Muse, Neurable, IDUN) has proven users will wear EEG devices for monitoring; adding fNIRS optics expands the signal envelope at acceptable form-factor cost. The combined device is more defensible than fNIRS alone in scientific reviews and FDA submissions.

### 12.4 OPM-MEG as Complementary Clinical-Grade Reference

For the X-Labs Phase 0 and ARPA-H PHO programs, OPM-MEG fits as:
- A reference modality for validating wearable-derived biotypes (compare OPM-MEG MMN and 40 Hz ASSR to wearable-EEG-recovered equivalents).
- A clinical-grade tool deployed at partner sites (Hospital for Sick Children Toronto; University of Nottingham; current sites approximately 20 globally) for high-precision biotype work.
- An eventual long-term roadmap target if OPM sensors reach price points and shielding requirements that make wearable home use feasible (Cerca Magnetics roadmap targets 2027 to 2029 for next-generation systems).

The realistic 2026 to 2028 path is: hybrid wearable optical-EEG headset for at-home longitudinal monitoring, with OPM-MEG used in research and clinic for validation and biotype refinement. This is the path Cytognosis can pursue with the X-Labs and ARPA-H portfolio without overcommitting to a particular hardware bet.

---

## References

[1] Klimesch W. EEG alpha and theta oscillations reflect cognitive and memory performance. Brain Research Reviews. 1999;29(2-3):169-95. doi:10.1016/S0165-0173(98)00056-3

[2] Davidson RJ. Anterior cerebral asymmetry and the nature of emotion. Brain and Cognition. 1992;20(1):125-51. doi:10.1016/0278-2626(92)90065-T

[3] Meta-analysis of resting frontal alpha asymmetry as a biomarker of depression. npj Mental Health Research. 2025. https://www.nature.com/articles/s44184-025-00117-x

[4] van der Vinne N, et al. Frontal alpha asymmetry as a diagnostic marker in depression: Fact or fiction? A meta-analysis. NeuroImage Clinical. 2017;16:79-87. https://pmc.ncbi.nlm.nih.gov/articles/PMC5524421/

[5] Sidelinger E, et al. Day-to-day individual alpha frequency variability measured by a mobile EEG device relates to anxiety. European Journal of Neuroscience. 2023. doi:10.1111/ejn.16002

[6] Characterizing PTSD Using Electrophysiology: Towards A Precision Medicine Approach. PMC12130596. 2025. https://pmc.ncbi.nlm.nih.gov/articles/PMC12130596/

[7] Neuhaus E, Webb SJ, et al. Resting-state EEG power differences in autism spectrum disorder: a systematic review and meta-analysis. Translational Psychiatry. 2023;13:389. https://www.nature.com/articles/s41398-023-02681-2

[8] Cavanagh JF, Shackman AJ. Frontal midline theta reflects anxiety and cognitive control: meta-analytic evidence. Journal of Physiology Paris. 2015;109(1-3):3-15. https://pmc.ncbi.nlm.nih.gov/articles/PMC4213310/

[9] Monastra VJ, et al. The development of a quantitative electroencephalographic scanning process for ADHD. Neuropsychology. 2001;15(1):136-44.

[10] Theta-Beta Ratio in Attention Deficit Hyperactivity Disorder: A Multiverse Analysis. medRxiv. 2026. https://www.medrxiv.org/content/10.64898/2026.01.08.26343676

[11] Cook IA, Leuchter AF, et al. Quantitative EEG biomarkers for predicting likelihood and speed of achieving sustained remission in major depression. Translational Psychiatry. 2013.

[12] Atypical prediction error learning is associated with prodromal symptoms in individuals at clinical high risk for psychosis. PMC9700713. https://pmc.ncbi.nlm.nih.gov/articles/PMC9700713/

[13] Donoghue T, Haller M, Peterson EJ, et al. Parameterizing neural power spectra into periodic and aperiodic components. Nature Neuroscience. 2020;23(12):1655-65. doi:10.1038/s41593-020-00744-x

[14] Gao R, Peterson EJ, Voytek B. Inferring synaptic excitation/inhibition balance from field potentials. NeuroImage. 2017;158:70-78.

[15] Donoghue T. A Systematic Review of Aperiodic Neural Activity in Clinical Investigations. European Journal of Neuroscience. 2025. doi:10.1111/ejn.70255

[16] Martinez-Canada P, et al. Combining aperiodic 1/f slopes and brain simulation: An EEG/MEG proxy marker of excitation/inhibition imbalance in Alzheimer's disease. Alzheimer's & Dementia: DADM. 2023. doi:10.1002/dad2.12477

[17] Investigating Sleep Spindle Density and Schizophrenia: A Meta-Analysis. Psychiatry Research. 2021. https://www.sciencedirect.com/science/article/abs/pii/S0165178121005606

[18] Kupfer DJ, Foster FG. Interval between onset of sleep and rapid-eye-movement sleep as an indicator of depression. Lancet. 1972;2(7779):684-6.

[19] Sleep Power Spectral Density and Spindles in PTSD and Their Relationship to Symptom Severity. Frontiers in Psychiatry. 2021. https://pmc.ncbi.nlm.nih.gov/articles/PMC8640175/

[20] REM density is associated with treatment response in major depression: Antidepressant pharmacotherapy vs. psychotherapy. Journal of Psychiatric Research. 2021.

[21] REM density predicts rapid antidepressant response to ketamine in individuals with treatment-resistant depression. Translational Psychiatry. 2025. https://pubmed.ncbi.nlm.nih.gov/39955416/

[22] Bramon E, et al. Meta-analysis of P300 and schizophrenia: Patients, paradigms, and practical implications. Biological Psychiatry. 2004.

[23] Earls HA, et al. Meta-analytic Review of Auditory Event-Related Potential Components as Endophenotypes for Schizophrenia. Schizophrenia Bulletin. 2016;42(6):1504-16. https://academic.oup.com/schizophreniabulletin/article/42/6/1504/2399394

[24] The Utility of P300 as a Schizophrenia Endophenotype and Predictive Biomarker: Clinical and Socio-Demographic Modulators in COGS-2. PMC4382423.

[25] Porjesz B, Begleiter H. Genetic basis of event-related potentials and their relationship to alcoholism and alcohol use. Journal of Clinical Neurophysiology. 2003;15(1):44-57.

[26] Light GA, Naatanen R. Mismatch negativity is a breakthrough biomarker for understanding and treating psychotic disorders. PNAS. 2013;110(38):15175-6.

[27] A Meta-Analysis of Mismatch Negativity in Schizophrenia: From Clinical Risk to Disease Specificity and Progression. Biological Psychiatry. 2016. https://pubmed.ncbi.nlm.nih.gov/26444073/

[28] Naatanen R, et al. Mismatch negativity (MMN) deficiency: A break-through biomarker in predicting psychosis onset. International Journal of Psychophysiology. 2015. https://www.sciencedirect.com/science/article/abs/pii/S0167876014016742

[29] Mazer P, et al. Systematic review and meta-analysis of the visual mismatch negativity in schizophrenia. European Journal of Neuroscience. 2024. doi:10.1111/ejn.16355

[30] Adler LE, et al. Schizophrenia, sensory gating, and nicotinic receptors. Schizophrenia Bulletin. 1998;24(2):189-202.

[31] Impaired P50 sensory gating in post-traumatic stress disorder secondary to urban violence. PMID 14962572.

[32] Riesel A. The erring brain: Error-related negativity as an endophenotype for OCD-A review and meta-analysis. Psychophysiology. 2019. https://pubmed.ncbi.nlm.nih.gov/30838682/

[33] Meyer A, et al. A neural biomarker, the error-related negativity, predicts the first onset of generalized anxiety disorder in a large sample of adolescent females. Journal of Child Psychology and Psychiatry. 2018. https://pmc.ncbi.nlm.nih.gov/articles/PMC6192876/

[34] A Diagnostic Biomarker for Pediatric Generalized Anxiety Disorder Using the Error-Related Negativity. PMC7529976. 2020.

[35] Associations between the late positive potential and PTSD, anxiety, and depressive symptoms among trauma-exposed undergraduates. Psychophysiology. 2023. https://pubmed.ncbi.nlm.nih.gov/36669617/

[36] Proudfit GH. The reward positivity: from basic research on reward to a biomarker for depression. Psychophysiology. 2015;52(4):449-59. doi:10.1111/psyp.12370

[37] Klawohn J, et al. A registered report of error-related negativity and reward positivity as biomarkers of depression: P-Curving the evidence. International Journal of Psychophysiology. 2020.

[38] Swerdlow NR, et al. Deficient prepulse inhibition in schizophrenia in a multi-site cohort: Internal replication and extension. Schizophrenia Research. 2017. https://pubmed.ncbi.nlm.nih.gov/28549722/

[39] The 40-Hz Auditory Steady-State Response in Patients With Schizophrenia: A Meta-analysis. JAMA Psychiatry. 2016. https://pubmed.ncbi.nlm.nih.gov/27732692/

[40] Lateral inhibition in the autism spectrum: An SSVEP study of visual cortical lateral interactions. Neuropsychologia. 2018. https://www.sciencedirect.com/science/article/abs/pii/S0028393218300757

[41] Lehmann D, Strik WK, Henggeler B, et al. EEG microstates: classification and connection with clinical psychiatric conditions. International Journal of Psychophysiology. 1998.

[42] da Cruz JR, et al. EEG microstates are a candidate endophenotype for schizophrenia. Nature Communications. 2020;11:3089. https://www.nature.com/articles/s41467-020-16914-1

[43] Microstate D as a Biomarker in Schizophrenia: Insights from Brain State Transitions. PMC11505886. 2024.

[44] Spectral decomposition of EEG microstates in post-traumatic stress disorder. NeuroImage Clinical. 2022. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9421541/

[45] Murphy M, et al. EEG Microstates in Mood and Anxiety Disorders: A Meta-analysis. Brain Topography. 2023. doi:10.1007/s10548-023-00999-0

[46] Resting-state EEG networks characterized by intramodular and global hyperconnectivity in depressive sample. PMC9566570.

[47] Hardmeier M, et al. Reproducibility of Functional Connectivity and Graph Measures Based on the Phase Lag Index (PLI) and Weighted Phase Lag Index (wPLI) Derived from High Resolution EEG. PLoS ONE. 2014. https://pmc.ncbi.nlm.nih.gov/articles/PMC4186758/

[48] Abnormal resting-state functional connectivity underlies cognitive and clinical symptoms in patients with schizophrenia. Frontiers in Human Neuroscience. 2023.

[49] Resting-state EEG dynamic functional connectivity distinguishes non-psychotic major depression, psychotic major depression and schizophrenia. Translational Psychiatry. 2024. https://pubmed.ncbi.nlm.nih.gov/38267620/

[50] Wearable Scanner Maps Children's Brain Activity. Neuroscience News (covering Boto et al. Nottingham). 2024. https://neurosciencenews.com/wearable-neuroimaging-neurodeveopment-26244/

[51] Cerca OPM-MEG System. Cerca Magnetics. https://www.cercamagnetics.com/cerca-opm-meg

[52] Wearable OPM-MEG: A changing landscape for epilepsy. PMC9805039. 2022.

[53] Yang C, et al. BIOT: Biosignal Transformer for Cross-data Learning in the Wild. NeurIPS 2023.

[54] Jiang W-B, et al. LaBraM: Large Brain Model for Learning Generic Representations with Tremendous EEG Data in BCI. ICLR 2024.

[55] EEG-FM-Bench: A Comprehensive Benchmark for the Systematic Evaluation of EEG Foundation Models. arXiv 2508.17742. 2025. https://arxiv.org/html/2508.17742v1

[56] EEG Foundation Models: A Critical Review of Current Progress and Future Directions. arXiv 2507.11783. 2025.

[57] Resting-State Electroencephalogram Depression Diagnosis Based on Traditional Machine Learning and Deep Learning: A Comparative Analysis. PMC11548331.

[58] CRCC: Contrast-Based Robust Cross-Subject and Cross-Site Representation Learning for EEG. arXiv 2602.19138. 2026.

[59] Casarotto S, Comanducci A, Rosanova M, Sarasso S, Massimini M. Stratification of unresponsive patients by an independently validated index of brain complexity. Annals of Neurology. 2016;80(5):718-29.

[60] Rogasch NC, Fitzgerald PB. Assessing cortical network properties using TMS-EEG. Human Brain Mapping. 2013.

[61] TMS-EEG-derived excitation/inhibition ratio as a diagnostic biomarker for major depressive disorder. medRxiv. 2026. https://www.medrxiv.org/content/10.64898/2026.01.22.26344599

[62] Transcranial Magnetic Stimulation-Electroencephalography for Biomarker Discovery in Psychiatry. Biological Psychiatry. 2024. https://www.biologicalpsychiatryjournal.com/article/S0006-3223(23)01795-X

[63] Zrenner C, Desideri D, Belardinelli P, Ziemann U. Real-time EEG-defined excitability states determine efficacy of TMS-induced plasticity in human motor cortex. Brain Stimulation. 2018;11(2):374-89.

[64] Zrenner C, Ziemann U. Closed-Loop Brain Stimulation. Biological Psychiatry. 2024. https://www.sciencedirect.com/science/article/pii/S0006322323015895

[65] EEG synchronized left prefrontal transcranial magnetic stimulation (TMS) for treatment resistant depression is feasible and produces an entrainment dependent clinical response. Brain Stimulation. 2023.

[66] Neurable MW75 Neuro published validation studies. Neurable Inc. https://neurable.com

[67] IDUN Technologies / Cerebra collaboration. SLEEP 2024 conference presentation. https://iduntechnologies.com/science

[68] cEEGrid Around-the-Ear EEG validation. Acquisition of Subcortical Auditory Potentials With Around-the-Ear cEEGrid Technology. PMC6646709.

# Problem and Gap Statement: Mental Health

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: researchers, stakeholders
> **Tags**: `research`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)

*Cytognosis Foundation, in collaboration with Hervé Marie-Nelly. Prepared for NSF X-Labs (Phase 0, May 2026) and the parallel ARPA-H PHO submission.*

---

## 1. Executive Summary

Mental illness is the defining chronic-disease crisis of 2026. The Global Burden of Disease Study 2023, published in *The Lancet* in May 2026, estimates that 1.17 billion people now live with a mental disorder, an increase of 95.5% in prevalent cases since 1990, and mental disorders account for 171 million disability-adjusted life-years globally, ranking fifth among 22 cause groups for total burden and second only to musculoskeletal disorders for years lived with disability (1). In the United States, more than 14 million adults live with serious mental illness, suicide rates rose 37% from 2000 to 2018 before peaking again in 2022, and the veteran suicide rate runs more than twice the non-veteran adult rate, with over 6,000 veteran suicides each year for more than two decades (2). The April 18, 2026 Executive Order on Accelerating Medical Treatments for Serious Mental Illness states the federal position plainly: despite massive Federal investment, the medical research system has yet to produce approved therapies that promote enduring improvements for the most complex patients, and innovative methods are needed beyond existing prescription medications (2).

Behind these numbers sits a structural failure. Psychiatry is the only branch of medicine that selects treatment from a categorical label produced by a 30-minute symptom interview, with no objective biological assay to confirm the label and no continuous physiological readout to confirm whether the treatment is working. Translated into the Cytognosis blindspot frame, reactive psychiatry suffers three convergent structural limits.

**The Detection blindspot.** Mental illness has no clinical biomarker. Diagnosis depends on self-report, and the average lag between symptom onset and first evidence-based treatment runs eight to eleven years for depression and an even longer interval for psychosis. The biological precursors of depression, psychosis, suicidal crisis, and relapse are real and measurable in research settings, yet clinically invisible at the population scale.

**The Personalization blindspot.** First-line antidepressant response sits at 42 to 53%; STAR*D showed relapse rates climbing from 40% to 71% across four sequential treatment steps (3). Treatment selection is essentially trial and error. The biological substrate for stratification exists: Drysdale and colleagues identified four resting-state connectivity biotypes of depression in 2017 (4), B-SNIP defined three psychosis biosignatures across the schizophrenia-bipolar spectrum, and the personalized N-of-1 machine-learning iMAP work published in May 2026 by Mishra and colleagues nearly doubled the standard 30% depression remission rate to 55% (5, 6). The biology supports stratification; clinical practice does not operationalize it.

**The Feedback blindspot.** Diabetes has continuous glucose monitoring. Cardiology has continuous ECG and remote hemodynamic sensing. Oncology has circulating tumor DNA. Psychiatry has the PHQ-9, administered every few weeks, with no objective continuous signal in between. People deteriorate, stabilize, and relapse without anyone knowing until the next appointment, or until a 911 call.

Cytognosis is building the platform that closes all three gaps in mental health first: a wearable, AI-native, on-device system that detects pre-crisis states, personalizes intervention to individual biology, and provides continuous feedback to the person and the care team. The parallel ARPA-H PHO effort builds the multi-scale map (micro, meso, macro) that anchors the platform to dimensional psychiatric biology. The NSF X-Labs effort builds the new sensing instrument that operationalizes the map at the point of life. Together they translate the dimensional biology established by Grotzinger et al. (2025), Beam et al. (2021), and Quah et al. (2025) (7, 8, 9) into the first continuous, personalized, longitudinal readout of mental health.

---

## 2. The Scale of the Problem

### 2.1 Global prevalence: more than one billion affected

The GBD 2023 collaborator analysis published in *The Lancet* in May 2026 provides the most current global picture (1). In 2023, an estimated **1.17 billion people** (95% UI 1.06 to 1.31 billion) lived with a mental disorder, equivalent to an age-standardized prevalence of 14,210.7 per 100,000 population. This represents a **95.5% increase in prevalent cases since 1990** and a 24.2% rise in age-standardized prevalence rate over the same period. Among major individual disorders in 2023:

- **Anxiety disorders**: 470 million prevalent cases globally (age-standardized rate 5,722.4 per 100,000), a 158.6% increase since 1990 and 64.9% rise in age-standardized prevalence; **DALY rate rose 47.1% since 2019**, the largest pandemic-era jump of any mental disorder (1).
- **Major depressive disorder**: 236 million prevalent cases (2,815.8 per 100,000), a 131.3% increase since 1990 and a 41.3% rise in age-standardized rate; DALYs rose 24.5% since 2019 alone (1).
- **Schizophrenia**: 26.9 million prevalent cases, a 79.1% increase since 1990 (1).
- **Bipolar disorder**: 35.7 million prevalent cases, a 68.7% increase since 1990 (1).
- **Dysthymia (persistent depressive disorder)**: 89.3 million prevalent cases (1).
- **ADHD**: 86.3 million prevalent cases (1).
- **Eating disorders (anorexia + bulimia nervosa)**: roughly 18 million combined; bulimia rose 75.1% since 1990 (1).
- **Autism spectrum disorders**: 52.3 million prevalent cases, up 72.4% since 1990 (1).

### 2.2 Disability burden: fifth-leading cause group worldwide

Mental disorders contributed **171 million DALYs in 2023** (age-standardized rate 2,070.5 per 100,000), accounting for 6.1% of all-cause DALYs and ranking **fifth among the 22 GBD cause groups, up from twelfth in 1990** (1). Within non-communicable diseases, mental disorders explain 9.5% of all NCD DALYs, ranking third behind cardiovascular disease and neoplasms. Mental disorders are now the **leading cause of years lived with disability globally**, explaining 17.3% of all-cause YLDs in 2023 (up from second in 1990) and 22.3% of NCD YLDs (1).

The burden is disproportionately concentrated in young people. DALYs peak in the **15 to 19 year age group** at 2,617.3 per 100,000, dominated by anxiety disorders (5.96 million DALYs in this age band) and major depressive disorder (5.49 million DALYs) (1). For ages 10 to 14, anxiety, autism spectrum disorders, and conduct disorder lead the burden. From age 20 onward, major depressive disorder and anxiety disorders together drive most of the total. Females experience a 27.6% higher age-standardized DALY rate than males (2,239.6 vs 1,900.2 per 100,000), with the gap largest for depression, anxiety, and eating disorders.

### 2.3 Trajectory: post-pandemic surge with no plateau

GBD 2023 quantifies the COVID-19 effect directly. For major depressive disorder, the age-standardized DALY rate rose from 2,261.0 per 100,000 in 2019 by 24.1% to 2,806.3 in 2020, then peaked at 2,819.3 in 2021. For anxiety disorders, the rate rose from 3,891.2 in 2019 by 21.5% to 4,728.6 in 2020, peaked in 2023 at 5,722.4, and shows no sign of returning to pre-pandemic levels (1). Every WHO region shows increased mental disorder DALY rates in 2023 compared with 1990; the magnitude varies from 1,302.4 per 100,000 (Vietnam) to 3,555.8 (Netherlands), with rates ranging from 1,853.0 in low-SDI to 2,184.1 in high-SDI countries.

### 2.4 United States: the crisis at home

The April 2026 Executive Order cites the most recent federal statistics (2):

- **Over 14 million American adults** have a serious mental illness defined as a diagnosable mental, behavioral, or emotional disorder that substantially interferes with life and ability to function.
- **About 8 million Americans** are on prescription medication for these conditions.
- **Suicide rates rose 37% from 2000 to 2018**, dropped 5% during 2018 to 2020, then **rebounded to a peak in 2022**.
- **Veteran suicide rate runs more than twice the non-veteran adult rate**, with over 6,000 veteran suicides per year for more than 20 years.

To this the broader US picture adds (10, 11, 12, 13):

- Approximately **53 million US adults** live with any mental illness.
- The US drug-overdose death toll has remained above **70,000 per year** since 2019, dominated by synthetic opioids; substance use disorder is itself a transdiagnostic psychiatric condition with shared genetic architecture with internalizing disorders (7).
- More than **20% of US adults** report a depressive episode in the past year; among young adults aged 18 to 25 the figure is approximately **21%** (14).
- The US economic burden of major depressive disorder alone is estimated at **over $380 billion per year**, with healthcare costs as the leading direct driver (15).
- Mental health professional shortages are severe: rural US counties average **3.5 psychiatrists per 100,000 residents** versus 13.0 in urban counties, and **65% of rural counties have no psychiatrist at all** (16, 17).

### 2.5 The treatment gap

Globally, the WHO Mental Health Action Plan 2013 to 2030 called for a doubling of mental health services coverage by 2030 (1). That target is not on track. The treatment gap, the proportion of affected people who do not receive evidence-based care, exceeds 50% in high-income countries and 75% in low- and middle-income countries. Even within the United States, where coverage is comparatively high, the EO acknowledges that current treatments leave the most complex patients without enduring improvement, motivating the federal pivot to psychedelics, ibogaine, and breakthrough therapy designation (2). Racial and ethnic minorities face **30 to 50% higher psychiatric misdiagnosis rates** in the US, with Black Americans up to four times more likely to be misdiagnosed with schizophrenia rather than a mood disorder (18, 19).

### 2.6 The federal framing

The April 2026 Executive Order signals the political climate in which any new mental health technology will be evaluated. The EO frames the problem as one of **innovation failure** ("our medical research system has yet to produce approved therapies that promote enduring improvements"), prioritizes **breakthrough therapy designation** and **right-to-try access** for novel modalities, and directs ARPA-H to allocate **at least $50 million** for state-collaboration on advancing innovative mental health treatments (2). It explicitly endorses partnership with the VA and private sector for "real-world evidence generation." A platform that produces longitudinal, continuous, person-level outcome data for mental health is exactly the kind of real-world evidence engine the EO contemplates. Cytognosis and the X-Labs effort are aligned by design with this framing.

---

## 3. The Three Structural Limits in Detail

### 3.1 The Detection Blindspot: psychiatry has no biomarker

Psychiatry is the only major branch of medicine that diagnoses by symptom report alone. There is no blood test for depression. There is no scan that distinguishes bipolar disorder from unipolar depression in clinical use. There is no objective marker for schizophrenia, PTSD, or addiction. The Diagnostic and Statistical Manual lists symptom criteria; a clinician applies them in a 30-minute interview; the resulting label drives treatment selection (20).

The clinical consequences are well documented:

- **Diagnostic delay.** The mean delay between onset of major depression symptoms and first evidence-based treatment is **roughly 8 years** in the US, and approximately **11 years** for bipolar disorder, with longer delays in low- and middle-income countries (21). For first-episode psychosis, the duration of untreated psychosis averages **1 to 2 years** in high-income countries; **longer DUP predicts worse functional outcome at five years** independent of other factors.
- **Pre-symptomatic biology is measurable in research settings.** Resting-state functional connectivity changes precede first depressive episodes by years (4). Cortisol awakening response, polygenic risk scores, and inflammatory markers stratify risk for first onset of psychosis and depression in prospective cohorts. The van de Leemput et al. PNAS study demonstrated that temporal autocorrelation, variance, and emotional correlation in passively collected mood data predict transitions between depressed and non-depressed states days to weeks before they clinically manifest (22). The signal exists. Clinical practice does not capture it.
- **Suicide is the leading cause of death in US adolescents and there are no clinical biomarkers to predict it.** Existing screeners (Columbia Suicide Severity Rating Scale, PHQ-9 item 9) have positive predictive value below 5% at population scale. The April 2026 EO calls this out explicitly as the central tragedy the administration is trying to address (2).
- **Prodromal psychosis is biologically detectable but clinically siloed.** The Clinical High Risk (CHR) framework identifies people with attenuated psychotic symptoms, of whom roughly 20% transition to full psychosis within two years; multivariate prediction combining clinical, cognitive, and neuroimaging features reaches AUC ~0.8 in research cohorts (23). None of this is deployed in primary care or in the community.
- **Addiction relapse is preceded by measurable craving and cue-reactivity signatures in laboratory paradigms** that have never been operationalized as continuous monitoring (24).

Without a clinical biomarker, psychiatry cannot detect and intercept. It can only wait for crisis.

### 3.2 The Personalization Blindspot: one-size-fits-all care for biologically heterogeneous conditions

When a person with depression receives a first prescription, the choice between an SSRI, an SNRI, bupropion, mirtazapine, or psychotherapy is essentially **a population-level guess**. The landmark STAR*D trial showed that the cumulative remission rate climbed from approximately 33% after the first treatment step to 67% after four sequential steps, but with relapse rates rising in parallel from 40% to 71% (3). The mean time per failed step is 6 to 12 weeks. The mean time to find an effective regimen, for those who find one at all, can run more than a year.

The biological evidence that this is wrong is now overwhelming:

- **Depression biotypes (Drysdale 2017).** Resting-state functional connectivity in 1,188 participants defined four biotypes of depression with distinct symptom profiles and divergent responses to transcranial magnetic stimulation (4). Subsequent work has refined the biotype count and stability, but the central finding holds: people with the same DSM diagnosis have biologically distinct illnesses.
- **Williams six-biotype framework (Stanford).** The Williams group at Stanford has integrated task-based fMRI of six neurocognitive circuits (default mode, salience, attention, threat, reward, cognitive control) into a six-biotype classification of mood and anxiety disorders; biotype predicts differential response to SSRIs, behavioral activation, and cognitive therapy (25). The iMAP work published in NPP Digital Psychiatry and Neuroscience in May 2026 by Mishra and colleagues at UCSD demonstrates the clinical impact of person-level personalization at scale: **N-of-1 machine learning models identified each individual's top mood-predictive lifestyle factor from two weeks of smartwatch and ecological momentary assessment data, and personalized iMAPs implemented over six weeks doubled the standard 30% depression remission rate to 55% (PHQ-9 score below 5), with sustained benefit at 12 weeks** (5, 6). Anxiety symptoms dropped 36%; clinician-rated depression (HDRS) showed Cohen's d of -1.03; quality of life, selective attention, interference processing, and working memory all improved significantly. The effect size is equivalent to combining the best evidence-based behavioral interventions with the precision of personalized targeting.
- **Psychosis biosignatures (B-SNIP).** The Bipolar and Schizophrenia Network on Intermediate Phenotypes consortium has defined three biotypes spanning the schizophrenia-bipolar spectrum using cognitive, neurophysiological, and neuroimaging measures; the biotypes do not align with DSM categories but predict differential clinical course and family aggregation (26).
- **Cross-disorder genomic factor structure (Grotzinger 2025).** Genomic structural equation modeling across 14 psychiatric disorders identified five latent factors (Compulsive, Schizophrenia-Bipolar, Neurodevelopmental, Internalizing, Substance Use) that explain ~66% of genetic variance, with **divergent neurobiological substrates**: the Schizophrenia-Bipolar factor is enriched in excitatory neurons (hippocampal CA1/CA3), while the Internalizing factor is enriched in oligodendrocytes and their precursors (7). Over 99% of case-case GWAS hits separate disorders that load on different factors. Genetic biology says these are different illnesses; clinical practice treats them with overlapping medications selected without reference to the underlying axis.
- **Pharmacogenomics use is minimal.** Despite FDA-cleared CYP2D6 and CYP2C19 panels for antidepressant metabolism, pharmacogenomic testing penetrates fewer than 5% of new antidepressant prescriptions in the US, and existing panels capture only a fraction of the heritable variation in response.

The Personalization blindspot is the most expensive of the three failures because the technology to close it now exists at the algorithmic level (iMAP achieving 55% remission demonstrates this), and the biological substrate for stratification is established (Drysdale, B-SNIP, Williams, Grotzinger). What is missing is the continuous, scalable sensing layer that delivers the personalization signal in daily life rather than during a 2-hour Stanford research scan.

### 3.3 The Feedback Blindspot: weeks-long sparse outcomes in a continuous illness

Every other field of medicine has built a continuous biological feedback channel.

- **Diabetes: continuous glucose monitoring.** CGM yields a 66% reduction in diabetes events and 1.1% reduction in HbA1c versus fingersticks (27).
- **Cardiology: continuous ECG and remote hemodynamic monitoring.** Wearable atrial fibrillation detection shows a 3.2-fold higher detection rate than routine care (28). Remote heart failure monitoring reduces hospitalizations by 87% and deaths by 77% (29).
- **Oncology: circulating tumor DNA.** ctDNA detects recurrence 3.1 to 3.5 years before standard imaging (30).
- **Sleep medicine: continuous polysomnography, then wearable derivatives.** Obstructive sleep apnea is now routinely diagnosed by home wearable devices.

**Psychiatry has none of this.** The standard clinical outcome instrument is the PHQ-9, a nine-item self-report administered every two to four weeks at best, more typically every three months. The Hamilton Depression Rating Scale is administered by a clinician, requires 20 to 30 minutes, and is performed even less frequently. Between visits there is no objective signal. People deteriorate, recover, relapse, and reach suicidal crisis with no biological readout that the care team or the person can see.

The consequences are quantitative. Without continuous feedback:

- **Treatment response cannot be measured until ~6 weeks** after starting an antidepressant, the latency to clinical effect plus the latency to clinic visit. Every failed trial therefore costs 6 to 12 weeks of suffering before the next decision.
- **Relapse prediction is poor.** Roughly 50% of people who remit from a depressive episode relapse within two years; current clinical practice has no continuous early-warning signal.
- **Sub-syndromal deterioration is invisible.** People who slide from euthymia toward depression, or from stable schizophrenia toward acute psychosis, are not detected until the slide is far advanced.
- **Suicidal crisis windows are short and unmonitored.** Most suicide attempts are preceded by hours to days of acute crisis with measurable physiological correlates (sleep disruption, autonomic dysregulation, social withdrawal) that wearables can in principle detect but current systems do not act on.

The continuous monitoring paradigm worked in diabetes (a 66% event reduction) and in cardiology (an 87% hospitalization reduction). Translated to psychiatry, the same paradigm shift would change the clinical contract from "see me in three weeks" to "we see your trajectory now."

---

## 4. What Current Technology Gets Wrong

A wearable mental health platform must compete with and outperform every existing modality. None of the current tools, alone or combined, closes the three blindspots.

### 4.1 MRI: powerful, but unscalable

Functional MRI underpins the biotype science that justifies personalization (Drysdale, Williams, B-SNIP). It produces brain-level signal with millimeter spatial resolution and reasonable temporal resolution, and it has produced the strongest published biological evidence in psychiatry. But MRI is **immobile, expensive (>$500 per scan), and discrete**. A person gets scanned once or twice in a research protocol and not at all in clinical care. MRI cannot detect a trajectory; it can only photograph a moment. The biotype findings remain trapped in research because the imaging modality does not scale.

### 4.2 EEG and MEG: limited resolution, limited deployment

Electroencephalography has decades of psychiatric research behind it (P300 in schizophrenia, error-related negativity in OCD, frontal alpha asymmetry in depression) and is portable. Magnetoencephalography is even more sensitive but stationary. Both share core limits: **EEG measures surface electrical activity with poor spatial resolution and high susceptibility to muscle and motion artifact**; consumer-grade EEG headbands underperform research-grade systems by a wide margin, and even research-grade EEG does not reach the subcortical structures (amygdala, hippocampus, ventral striatum) that drive the strongest biotype findings.

### 4.3 Wearables (Apple Watch, Oura, WHOOP, Fitbit)

Consumer wearables now reach 30%+ of US adults and measure heart-rate variability, sleep architecture, activity, and skin temperature. They are useful proxies for autonomic state and circadian rhythm and have demonstrated value in atrial fibrillation detection (28) and, in the iMAP work, as lifestyle inputs to N-of-1 mood models (5, 6). **They are not brain measurements.** Heart-rate variability is a distal correlate of autonomic tone; sleep architecture is a downstream consequence of central nervous system state. For mental health they capture the consequences of brain dysregulation, not the dysregulation itself. The iMAP doubling of remission rates is the ceiling of what behavioral-proxy wearables alone can achieve: it is real and important, but it leaves the brain unmeasured.

### 4.4 Smartphone digital phenotyping

Apps that infer mood from typing speed, voice prosody, GPS movement, and social interaction patterns (Mindstrong, Ginger, replacement startups) showed early promise but have largely failed to deliver clinical-grade signal. The behavioral signals are noisy, drift with phone use habits, and again measure consequences of brain state rather than brain state itself. The leading "digital phenotyping" platforms have either pivoted to coaching (away from biomarker claims) or shut down.

### 4.5 fNIRS and HD-DOT: the closest available, still inadequate

Functional near-infrared spectroscopy measures cerebral hemodynamics through the skull and scalp using near-infrared light. Kernel Flow, the Mass General OpenCap consortium, and the Bostonian HD-DOT systems represent the current state of the art. fNIRS is portable, non-invasive, and provides genuine cortical signal. But existing fNIRS systems share three limits: **shallow penetration (~1.5 cm, cortical surface only); no single-cell-class specificity (bulk hemodynamic signal); and no personalization (one-size-fits-all sensor placement and source-detector geometry)**. None of the existing fNIRS or HD-DOT systems offers continuous closed-loop operation tied to neuromodulation. Hervé Marie-Nelly's stealth spectroscopy work targets 2 to 3 cm depth with single-cell-class optical readout, a step change beyond current fNIRS that Cytognosis and the X-Labs effort propose to operationalize as a wearable.

### 4.6 PET: molecular but unrepeatable

Positron emission tomography produces molecular, receptor-level signal (dopamine D2/3, serotonin transporter, neuroinflammation via TSPO). For psychiatric biotyping this is the gold standard at the molecular level. But PET requires **radioactive tracer, $3,000+ per scan, hours of acquisition, and a cyclotron-equipped center**. It cannot be longitudinal. It is research-only at the population scale.

### 4.7 The void

Across these modalities, **no current system simultaneously delivers** (a) brain-level signal, (b) personalization to the individual's biology, (c) continuous longitudinal acquisition, and (d) scalability to a wearable form factor at consumer cost. MRI has (a) but not (b through d). Wearables have (c) and (d) but not (a). PET has (a) for molecular state but neither (c) nor (d). fNIRS has (c) and (d) but not (a) at meaningful depth. The combination needed to close the Detection, Personalization, and Feedback blindspots in mental health does not exist on the market or in the academic literature today.

---

## 5. The Opportunity

The convergence that makes a wearable, AI-native, continuous, personalized mental-health platform feasible in 2026 (and not in 2016) rests on five enabling shifts.

### 5.1 Biotype science has matured

Drysdale (2017), B-SNIP (multiple papers 2014 to 2024), the Williams six-biotype framework, and the Grotzinger cross-disorder genomic structural equation modeling published in *Science* in 2025 collectively define the **dimensional architecture** that psychiatric care should target (4, 7, 26). Beam et al. (2021) and Quah et al. (2025) used data-driven neuroimaging to recover the same dimensional structure from brain activation patterns (8, 9). The biology is no longer contested. What is missing is the operational layer that translates dimensional biology into continuous personalized intervention.

### 5.2 Optical sensing has matured

TD-fNIRS, HD-DOT, ultrasound-modulated optics, and the deeper-penetration spectroscopy approaches under development (Openwater, Kernel, Hervé Marie-Nelly's stealth work) have crossed thresholds in source/detector density, photon-counting electronics, and tissue-modeling that put 2 to 3 cm depth optical brain sensing within reach of a wearable form factor. The same trajectory that took CGM from research curiosity to 20%+ market penetration in diabetes (2010 to 2025) is now beginning for non-invasive brain optical sensing.

### 5.3 AI has matured

Foundation models for biomedical signals (sleep staging, ECG, EEG) now match or exceed expert performance, and the architectures generalize across modalities. The iMAP work used per-person N-of-1 machine learning with SHAP-based explainability to identify each individual's top lifestyle predictor of mood; a decision algorithm matched expert coach assignment in 87.5% of cases, and a large-language-model approach reached 92.5% (5, 6). The same per-person machine-learning approach applied to brain-level continuous sensing could reach the kind of clinical accuracy that has been theoretically possible for a decade and operationally absent.

### 5.4 Closed-loop neuromodulation has matured

Stanford SAINT, a personalized accelerated TMS protocol targeting an individual's functional connectivity between subgenual cingulate and dorsolateral prefrontal cortex, achieved **~79% remission for treatment-resistant depression at 1-month follow-up** in a randomized double-blind trial (31). Closed-loop deep brain stimulation for OCD (Mayberg, Dougherty groups) and emerging closed-loop TMS protocols depend on real-time biomarker readout. The neuromodulation field needs the sensor that Cytognosis and the X-Labs project are building.

### 5.5 Policy has aligned

The April 2026 Executive Order directs ARPA-H, FDA, HHS, and the VA to accelerate innovative mental health interventions, prioritize breakthrough therapy designation, and generate real-world evidence at scale (2). The federal posture is no longer "we have the tools we need." The federal posture is "we do not have the tools we need; bring us the new ones." A continuous longitudinal sensing platform that closes the Detection, Personalization, and Feedback blindspots in mental health is the strongest possible answer to that posture.

### 5.6 The trillion-dollar opportunity

Solving the Personalization blindspot alone, on the iMAP demonstration of doubling remission from 30% to 55%, would translate into roughly an additional **100 million people moving from active depression to remission worldwide each year** if deployed at the population level. Solving the Detection blindspot, even partially, would compress the 8-year diagnostic delay for depression and the 1-to-2-year duration of untreated psychosis by an order of magnitude. Solving the Feedback blindspot would let the field manage psychiatric illness the way diabetes is now managed: continuously, personally, and with measurable trajectories rather than appointment-to-appointment guesses.

This is exactly the kind of high-risk, high-reward, AI-native, healthcare-blindspot problem that NSF X-Labs Phase 0 was designed for. The combined Cytognosis + Marie-Nelly platform is the right instrument for the right problem at the right time.

---

## 6. Strategic Framing

Cytognosis approaches mental health as the **sharpest test case** for its general "GPS for Health" platform, the goal of which is to detect and intercept disease before it entrenches by mapping continuous health coordinates across molecular, cellular, circuit, and behavioral scales. The mental-health-specific implementation closes all three blindspots through a coordinated technical program.

**Detection.** Continuous brain-level optical sensing, combined with peripheral wearable and behavioral signals, builds a longitudinal baseline against which deviations are detectable. The platform learns each person's normal variance and flags departures that precede clinical crises, addressing the 8-year diagnostic delay for depression, the 1-to-2-year duration of untreated psychosis, and the unmonitored suicidal-crisis window.

**Personalization.** Per-person machine learning, built on the iMAP architecture demonstrated by Mishra et al. (5, 6) but extended from peripheral lifestyle data to brain-level optical signal, identifies each individual's most predictive features and the intervention to which they are most likely to respond. The biotype science (Drysdale, Williams, B-SNIP, Grotzinger) supplies the dimensional priors; the platform refines them at the individual level.

**Feedback.** Continuous longitudinal sensing turns mental health into a quantitatively managed illness, like diabetes or atrial fibrillation. Clinicians, the person, and the AI agent see trajectories, not snapshots.

**Joint architecture.** The parallel ARPA-H PHO submission builds the **multi-scale map**: the micro-scale endotypic layer (cell-type-specific dysregulation from single-cell genomics), the meso-scale endophenotypic layer (circuit and connectomic biotypes from multimodal imaging), and the macro-scale phenotypic layer (dimensional axes from HiTOP and RDoC) (8, 9, 20). The map anchors the platform to the biological reality of dimensional psychiatry. The NSF X-Labs Phase 0 effort builds the **wearable sensor that operationalizes the map at the point of life**, in joint work with Hervé Marie-Nelly's stealth spectroscopy program (2 to 3 cm depth optical single-cell-class readout). Together the two efforts make dimensional psychiatry accessible to millions of people rather than dozens of research subjects.

**Privacy and openness.** All on-device, AI-native, person-first. Psychological data does not leave the device. Models, methods, and data infrastructure are released under permissive open-source and FAIR-data terms, consistent with the Cytognosis Foundation's openness commitment.

This is the platform that the dimensional-biology evidence has demanded for a decade. The technology to build it now exists. The federal policy environment now demands it. The opportunity to build it is open.

---

## References

1. GBD 2023 Mental Disorder Collaborators. Updated trends in the global prevalence and burden of mental disorders, 1990 to 2023: a systematic analysis for the Global Burden of Disease Study 2023. *The Lancet*. 2026;407:2040-2064. DOI: 10.1016/S0140-6736(26)00xxx.

2. The White House. Accelerating Medical Treatments for Serious Mental Illness. Executive Order, April 18, 2026. https://www.whitehouse.gov/presidential-actions/2026/04/accelerating-medical-treatments-for-serious-mental-illness/

3. Rush AJ, Trivedi MH, Wisniewski SR, et al. Acute and longer-term outcomes in depressed outpatients requiring one or several treatment steps: a STAR*D report. *American Journal of Psychiatry*. 2006;163(11):1905-1917.

4. Drysdale AT, Grosenick L, Downar J, et al. Resting-state connectivity biomarkers define neurophysiological subtypes of depression. *Nature Medicine*. 2017;23(1):28-38.

5. Nan J, Purpura S, Jaiswal S, Afshar H, Maric V, Manchanda JK, Taylor CT, Ramanathan D, Mishra J. Personalized machine learning guided intervention for optimizing lifestyle behaviors in depression: a pilot study. *NPP - Digital Psychiatry and Neuroscience*. 2026. DOI: 10.1038/s44277-026-00062-3.

6. Bard S. Machine Learning Doubles Depression Remission Rate. *Neuroscience News*. May 21, 2026. https://neurosciencenews.com/machine-learning-imap-depression-30744/

7. Grotzinger AD, Werme J, de Leeuw CA, et al. Cross-disorder genomic factor structure of 14 psychiatric disorders identifies a hierarchical model of psychopathology. *Science*. 2025.

8. Beam E, Potts C, Poldrack RA, Etkin A. A data-driven framework for mapping domains of human neurobiology. *Nature Neuroscience*. 2021;24(12):1733-1744.

9. Quah SKL, Jo HJ, Chai XJ, et al. Data-driven evaluation of the Research Domain Criteria using neuroimaging. *bioRxiv*. 2025.

10. National Institute of Mental Health. Mental Illness Statistics. 2023.

11. Substance Abuse and Mental Health Services Administration. Key Substance Use and Mental Health Indicators in the United States. 2023.

12. CDC. Drug Overdose Deaths in the United States, 2003 to 2023. *NCHS Data Brief*. 2024.

13. Centers for Medicare and Medicaid Services. National Health Expenditure Data, 2024. Published January 2025.

14. Centers for Disease Control and Prevention. Symptoms of Depression Among Adults: United States, 2020. *NCHS Data Brief* No. 379.

15. Greenberg PE, Chitnis A, Louie D, Suthoff E, Chen SY, Maitland J, et al. The economic burden of adults with major depressive disorder in the United States (2019). *Advances in Therapy*. 2023;40:4460-4479.

16. Andrilla CHA, Patterson DG, Garberson LA, Coulthard C, Larson EH. Geographic variation in the supply of selected behavioral health providers. *American Journal of Preventive Medicine*. 2018;54(6S3):S199-S207.

17. Health Resources and Services Administration. Mental Health Professional Shortage Areas. 2022.

18. Schwartz RC, Blankenship DM. Racial disparities in psychotic disorder diagnosis: a review of empirical literature. *World Journal of Psychiatry*. 2014;4(4):133-140.

19. Olbert CM, Nagendra A, Buck B. Meta-analysis of black vs. white racial disparity in schizophrenia diagnosis in the United States. *Journal of Abnormal Psychology*. 2018;127(1):104-115.

20. American Psychiatric Association. *Diagnostic and Statistical Manual of Mental Disorders* (5th ed.). 2013.

21. Wang PS, Berglund P, Olfson M, Pincus HA, Wells KB, Kessler RC. Failure and delay in initial treatment contact after first onset of mental disorders in the National Comorbidity Survey Replication. *Archives of General Psychiatry*. 2005;62(6):603-613.

22. van de Leemput IA, Wichers M, Cramer AOJ, et al. Critical slowing down as early warning for the onset and termination of depression. *Proceedings of the National Academy of Sciences*. 2014;111(1):87-92.

23. Fusar-Poli P, Salazar de Pablo G, Correll CU, et al. Prevention of psychosis: advances in detection, prognosis, and intervention. *JAMA Psychiatry*. 2020;77(7):755-765.

24. Sinha R. Modeling stress and drug craving in the laboratory: implications for addiction treatment development. *Addiction Biology*. 2009;14(1):84-98.

25. Williams LM. Precision psychiatry: a neural circuit taxonomy for depression and anxiety. *The Lancet Psychiatry*. 2016;3(5):472-480.

26. Clementz BA, Sweeney JA, Hamm JP, et al. Identification of distinct psychosis biotypes using brain-based biomarkers. *American Journal of Psychiatry*. 2016;173(4):373-384.

27. Journal of Managed Care and Specialty Pharmacy. Real-world outcomes of continuous glucose monitoring in adults with type 2 diabetes. 2024;30(4):372-382.

28. Perez MV, Mahaffey KW, Hedlin H, et al. Large-scale assessment of a smartwatch to identify atrial fibrillation. *New England Journal of Medicine*. 2019;381(20):1909-1917.

29. Ong MK, Romano PS, Edgington S, et al. Effectiveness of remote patient monitoring after discharge of hospitalized patients with heart failure: the BEAT-HF randomized clinical trial. *JAMA Internal Medicine*. 2016;176(3):310-318.

30. Cristiano S, Leal A, Phallen J, et al. Genome-wide cell-free DNA fragmentation in patients with cancer. *Cancer Discovery*. 2025 (advance online).

31. Cole EJ, Phillips AL, Bentzley BS, et al. Stanford Neuromodulation Therapy (SNT): a double-blind randomized controlled trial. *American Journal of Psychiatry*. 2022;179(2):132-141.

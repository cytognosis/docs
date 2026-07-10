# Transdiagnostic MACRO synthesis: symptom dimensions across 14 psychiatric disorders

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: researchers, stakeholders
> **Tags**: `literature-synthesis`, `disease-biotypes`, `transdiagnostic`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)

Scope: this document synthesizes the MACRO (symptom, behavior, phenotype) sections of the 14 per-disorder biotype docs in `../disease-biotypes/`, harmonized to SNOMED CT and the Human Phenotype Ontology (HPO). It identifies the symptom dimensions that recur across disorders, maps which disorders express each, and aligns those dimensions to Research Domain Criteria (RDoC) domains, Hierarchical Taxonomy of Psychopathology (HiTOP) spectra, and the five genomic factors from Grotzinger et al., "Mapping the genetic landscape across 14 psychiatric disorders," Nature 2025 (doi:10.1038/s41586-025-09820-3).

The 14 disorders: schizophrenia, bipolar disorder, major depressive disorder (MDD), PTSD, anxiety disorders, autism spectrum disorder (ASD), ADHD, OCD, Tourette syndrome (TS), anorexia nervosa (AN), and four substance use disorders (alcohol, opioid, nicotine, cannabis).

---

## 1. Framing: dimensional vs categorical psychiatry

Categorical diagnosis (DSM-5, ICD-11) assigns people to discrete disorders. The categorical model is operationally useful but maps poorly onto biology: diagnoses overlap heavily (TS clinic samples carry roughly 50 percent OCD and 50 percent ADHD; PTSD and MDD share large polygenic load; bipolar and schizophrenia share the SB genomic factor), single diagnoses split into biologically distinct subtypes (MDD melancholic vs atypical), and DSM presentations are unstable over development (ADHD children shift from combined to inattentive). A dimensional view treats psychopathology as continuous traits that cut across categories.

Two complementary dimensional frameworks anchor this synthesis:

**RDoC domains** (NIMH Research Domain Criteria). Six domains organize function from circuits to behavior:
- **Negative Valence Systems**: responses to threat, loss, frustrative non-reward (anxiety, threat-reactivity).
- **Positive Valence Systems**: reward valuation, effort, learning (anhedonia, reward dysfunction).
- **Cognitive Systems**: attention, working memory, cognitive control (executive dysfunction).
- **Social Processes**: affiliation, social communication, perception of self/others.
- **Arousal and Regulatory Systems**: arousal, circadian rhythm, sleep-wake.
- **Sensorimotor Systems**: motor actions, sensory gating, agency (added 2019).

**HiTOP spectra** (Hierarchical Taxonomy of Psychopathology). Empirically derived from symptom covariation:
- **Internalizing** (distress, fear): MDD, anxiety, PTSD.
- **Thought disorder** (psychoticism): schizophrenia, bipolar with psychosis.
- **Disinhibited externalizing**: ADHD, substance use disorders, impulsivity.
- **Antagonistic externalizing**: hostility, antisocial traits.
- **Detachment**: social withdrawal, anhedonia, restricted affect.
- **Somatoform**: bodily distress.

**Mapping to the Nature 2025 genomic factors.** The five factors give a genetic scaffold the symptom dimensions can be checked against:
1. **SB factor** (schizophrenia + bipolar): aligns with the HiTOP thought-disorder spectrum and the RDoC psychosis/reality-distortion dimension.
2. **Internalizing factor** (MDD + PTSD + anxiety): aligns with HiTOP internalizing and the RDoC Negative Valence domain (threat, negative affect) plus shared anhedonia.
3. **Neurodevelopmental factor** (ASD + ADHD + TS): aligns with social-communication and cognitive-control dimensions, and (via the externalizing edge) impulsivity.
4. **Compulsive/eating factor** (OCD + AN + TS): aligns with the compulsivity/repetitive-behavior dimension.
5. **Substance use factor** (alcohol + opioid + nicotine + cannabis): aligns with HiTOP disinhibited externalizing and the RDoC Positive Valence (reward/craving) dimension.

No dimension maps cleanly onto exactly one factor. Anhedonia, for example, spans the internalizing factor (MDD, PTSD), the SB factor (schizophrenia negative symptoms), and the substance use factor (withdrawal-stage reward deficit). This cross-loading is the central finding of the MACRO synthesis and is consistent with the Nature 2025 observation that signal shared across all 14 disorders was enriched for broad transcriptional regulation while factor-specific pathways were narrower.

---

## 2. Cross-cutting symptom dimensions

Each subsection harmonizes one recurring dimension across the 14 disorders. Confidence ratings: HIGH (core, criterion-level, multi-disorder replication), MEDIUM (well-documented but secondary or single-construct), LOW (contested or sparse). SNOMED/HPO IDs are taken from the per-disorder docs; "approx, needs curation" carries forward where the source flagged it.

### 2.1 Anhedonia / reward dysfunction (HP:0033676)

RDoC: Positive Valence Systems. HiTOP: detachment (and internalizing). The single most broadly distributed dimension in the set: reduced reward responsiveness, blunted reward-prediction signaling, ventral-striatal hypoactivation, and reduced motivation.

| Disorder | How it manifests | SNOMED CT / HPO term + ID | Confidence |
|---|---|---|---|
| MDD | Core criterion; blunted RewP, ventral-striatal hypoactivation | Anhedonia 28669007; Anhedonia HP:0033676 | HIGH |
| Schizophrenia | Negative-dimension avolition/anhedonia/alogia | Negative symptom 16990005 (approx); Anhedonia HP:0033676 | HIGH |
| Bipolar | Depressive-episode anhedonia, reward-circuit blunting | Bipolar depressive episode 191627008; Depressivity HP:0000716 | HIGH |
| PTSD | Dysphoric/negative-mood cluster; blunted reward reactivity | Anhedonia HP:0033676; Depressivity HP:0000716 (approx) | MEDIUM |
| Opioid UD | Protracted dysphoria, reward deficit in withdrawal/abstinence | Anhedonia 66704007 (approx); Anhedonia HP:0033676 (approx) | MEDIUM |
| Cannabis UD | Amotivational/anhedonic features (contested) | Apathy 84660005 (approx); Anhedonia HP:0033676 | LOW |
| Alcohol UD | Withdrawal-stage dysphoria/negative affect | Anhedonia HP:0033676 (approx, via withdrawal) | MEDIUM |
| Nicotine UD | Withdrawal negative affect (reward deficit component) | Anhedonia HP:0033676 (approx) | LOW |
| ADHD | Reward hyposensitivity, steep temporal discounting | Impulsivity HP:0100710 (delay-aversion proxy) | MEDIUM |
| Anorexia | Reward "contamination" / altered food reward valuation | (no clean term; relate to reward dimension) | MEDIUM |
| Anxiety | Reduced positive affect in some presentations | (no clean term; approx) | LOW |
| ASD / OCD / TS | Not a core feature; present via comorbid depression | Anhedonia HP:0033676 (comorbid only) | LOW |

### 2.2 Negative affect / threat / anxiety (HP:0000739)

RDoC: Negative Valence Systems (acute and sustained threat, loss). HiTOP: internalizing (fear and distress subfactors). Maps tightly to the internalizing genomic factor.

| Disorder | How it manifests | SNOMED CT / HPO term + ID | Confidence |
|---|---|---|---|
| Anxiety | Core: worry (GAD), panic, social-evaluative fear | Generalized anxiety disorder 21897009; Anxiety HP:0000739 | HIGH |
| PTSD | Threat-reactivity, hypervigilance, fear-conditioning failure | Hypervigilance 247803003 (approx); Anxiety HP:0000739 | HIGH |
| MDD | Anxious distress; reduced fronto-amygdala regulation | Anxiety 48694002; Anxiety HP:0000739 | HIGH |
| Anorexia | Intense fear of weight gain; premorbid harm avoidance | Fear of weight gain (approx); Anxiety HP:0000739 | HIGH |
| OCD | Anxiety driven by obsessions | Anxiety HP:0000739 (via obsessions) | HIGH |
| ASD | Co-occurring anxiety, prominent in masked/adult presentations | Anxiety disorder 197480006; Anxiety HP:0000739 | MEDIUM |
| Alcohol UD | Late-onset/Type A anxiety-driven (Cloninger/Babor) | Anxiety HP:0000739 (approx) | MEDIUM |
| Bipolar | Anxious comorbidity, mixed-features dysphoria | Anxiety HP:0000739 (approx) | MEDIUM |
| Cannabis / Nicotine / Opioid UD | Withdrawal-related negative affect/irritability | Irritability HP:0000737; Anxiety HP:0000739 (approx) | MEDIUM |
| Schizophrenia | Anxiety secondary to paranoia/prodrome | Anxiety HP:0000739 (secondary) | LOW |
| ADHD / TS | Comorbid anxiety | Anxiety HP:0000739 (comorbid) | LOW |

### 2.3 Compulsivity / repetitive behavior (HP:0000722)

RDoC: spans Positive Valence (habit), Cognitive Systems (cognitive control), Sensorimotor. HiTOP: a compulsivity dimension nested under internalizing/thought-disorder in some models. Maps to the compulsive/eating genomic factor (OCD + AN + TS), with a habit-formation arm reaching into the substance use factor.

| Disorder | How it manifests | SNOMED CT / HPO term + ID | Confidence |
|---|---|---|---|
| OCD | Core: repetitive acts to neutralize obsessions; CSTC drive | Compulsive behavior 247843008; Obsessive-compulsive behavior HP:0000722 | HIGH |
| TS | Comorbid OC features (~50%); shared compulsive factor | Obsessive-compulsive disorder 191736004; HP:0000722 | HIGH |
| Anorexia | Compulsive restriction, exercise, ritualized eating, over-control | Excessive exercise (approx); relate to HP:0000722 | HIGH |
| ASD | Restricted/repetitive behaviors, insistence on sameness | Restrictive behavior HP:0000753; Stereotypy HP:0000733 | HIGH |
| Substance UDs (all 4) | Compulsive use despite harm; ventral-to-dorsal striatal habit | Compulsive drug use (approx); Compulsive behaviors HP:0000722 (approx) | MEDIUM |
| Schizophrenia / MDD / anxiety / bipolar / ADHD / PTSD | Comorbid OC features in subsets only | HP:0000722 (comorbid) | LOW |

### 2.4 Impulsivity / disinhibition (HP:0100710)

RDoC: Positive Valence (reward/response) and Cognitive Systems (response inhibition). HiTOP: disinhibited externalizing (core). Maps to the substance use factor and the externalizing edge of the neurodevelopmental factor.

| Disorder | How it manifests | SNOMED CT / HPO term + ID | Confidence |
|---|---|---|---|
| ADHD | Core: poor stop-signal/go-no-go, right-IFG/fronto-striatal hypoactivation | Impulsivity 29164008 (approx); Impulsivity HP:0100710 | HIGH |
| Substance UDs (all 4) | Loss of control / impaired control over use | Impaired control (approx); Impulsivity HP:0100710 (approx) | HIGH |
| Alcohol UD | Early-onset/Type B externalizing, novelty-seeking | Antisocial behavior HP:0100716 (approx); Impulsivity HP:0100710 | HIGH |
| Bipolar | Manic risk-taking, increased goal-directed activity | Mania HP:0100754 (risk-taking component) | HIGH |
| Anorexia | Binge-purge subtype: higher impulsivity | (relate to Impulsivity HP:0100710) | MEDIUM |
| PTSD | Reckless/self-destructive behavior (DSM-5 cluster E) | Impulsivity HP:0100710 (approx) | MEDIUM |
| TS | Tic disinhibition; comorbid ADHD impulsivity | Impulsivity HP:0100710 (via ADHD) | MEDIUM |
| Schizophrenia / MDD / OCD / anxiety / ASD | Generally low; impulsivity not core | Impulsivity HP:0100710 (absent/secondary) | LOW |

Note the compulsivity-impulsivity axis: OCD and AN sit at the compulsive pole, ADHD and SUDs at the impulsive pole, and the substance use trajectory moves from impulsive initiation to compulsive maintenance over time.

### 2.5 Cognitive control / executive dysfunction (HP:0033694 / HP:0100543)

RDoC: Cognitive Systems (cognitive control, working memory, attention). HiTOP: cuts across spectra (a general "p-factor" correlate). Genetically diffuse; strongest in the SB and neurodevelopmental factors.

| Disorder | How it manifests | SNOMED CT / HPO term + ID | Confidence |
|---|---|---|---|
| Schizophrenia | Broad neurocognitive deficit; working memory, processing speed; DLPFC/PV-gamma | Cognitive impairment 386806002; Cognitive impairment HP:0100543; Impaired working memory HP:0500024 (approx) | HIGH |
| ADHD | Inattention, distractibility, fronto-parietal underconnectivity, DMN intrusion | Short attention span HP:0000736; ADHD HP:0007018 | HIGH |
| Bipolar | Inter-episode cognitive impairment, attention/EF | Cognitive impairment HP:0100543 (approx) | MEDIUM |
| MDD | Concentration/decision impairment; dlPFC-dACC underengagement | Impaired concentration 60032008 (approx); Impaired executive functioning HP:0033694 (approx) | MEDIUM |
| ASD | Cognitive inflexibility; intellectual disability co-occurrence in a fraction | Intellectual disability HP:0001249 (subset) | MEDIUM |
| Alcohol UD | Wernicke-Korsakoff, alcohol-related cognitive impairment | Memory impairment HP:0002354; Confusion HP:0001289 | MEDIUM |
| Cannabis UD | Working memory / attention deficits (partly reversible) | Cognitive impairment 386806002; HP:0100543 | MEDIUM |
| Nicotine UD | Withdrawal difficulty concentrating (reversible) | Poor concentration HP:0033223 (approx) | LOW |
| PTSD | Attention/concentration disruption (hyperarousal cluster) | (relate to HP:0033694) | MEDIUM |
| Anorexia | Set-shifting/cognitive rigidity (over-control) | (no clean term; relate to HP:0033694) | MEDIUM |
| OCD / TS | Executive/inhibitory differences; error-monitoring | (relate to HP:0033694) | MEDIUM |
| Anxiety | Worry-related attentional capture, enhanced error-monitoring | (relate to HP:0033694) | LOW |

### 2.6 Social-communication dysfunction (HP:0000735)

RDoC: Social Processes. HiTOP: detachment. Maps to the neurodevelopmental factor (ASD primary), with secondary expression via negative symptoms and withdrawal.

| Disorder | How it manifests | SNOMED CT / HPO term + ID | Confidence |
|---|---|---|---|
| ASD | Core: reduced reciprocal interaction, gaze, joint attention, pragmatics | Autism spectrum disorder 35919005; Impaired social interactions HP:0000735; Autistic behavior HP:0000729 | HIGH |
| Schizophrenia | Negative-symptom social withdrawal, alogia, social-cognition deficit | Negative symptom 16990005 (approx); relate to HP:0000735 | MEDIUM |
| Social anxiety | Fear/avoidance of social-evaluative situations | Social phobia 25501002; HP:0000735 (approx) | MEDIUM |
| MDD | Social withdrawal during episodes | (relate to HP:0000735) | LOW |
| PTSD | Detachment, estrangement (negative-mood cluster) | (relate to HP:0000735) | LOW |
| TS / ADHD | Peer/social difficulties (neurodevelopmental) | (relate to HP:0000735) | LOW |
| Anorexia / SUDs | Social impairment criterion (relationship/role disruption) | (relate to HP:0000735) | LOW |

### 2.7 Sensory / interoceptive atypicality

RDoC: Sensorimotor Systems and the interoception construct under Arousal/Regulatory. HiTOP: poorly represented (a gap). No single clean ontology term, so most cells are approx.

| Disorder | How it manifests | SNOMED CT / HPO term + ID | Confidence |
|---|---|---|---|
| ASD | Sensory over-/under-responsivity, sensory seeking; enhanced perceptual functioning | Sensory processing disorder 23476006 (approx); Abnormal nervous system physiology HP:0012638 (approx) | HIGH |
| Schizophrenia | Reduced sensory gating (P50), reduced PPI | (no precise SNOMED; abnormal sensory gating, approx) | MEDIUM |
| Anorexia | Body-image disturbance, altered interoception (precuneus/parietal) | Disturbance of body image 247852005 (approx); Abnormal self-image (approx) | MEDIUM |
| Anxiety | Somatic/autonomic interoceptive hyperawareness (insula) | Palpitations 80313002; Tachycardia HP:0001649 | MEDIUM |
| Substance UDs | Interoceptive craving (anterior insula) | (no clean term; relate to insula craving) | MEDIUM |
| PTSD | Heightened bodily threat sensing; dissociative depersonalization | Depersonalization 19006008 (approx); HP:0009800 (approx) | MEDIUM |
| TS | Premonitory urge (interoceptive antecedent to tic) | (no precise SNOMED/HPO; approx) | MEDIUM |
| OCD | "Not just right" sensory experiences (symmetry dimension) | (relate to HP:0000722, sensory CSTC) | LOW |

### 2.8 Psychosis / reality distortion (HP:0000709)

RDoC: spans Cognitive Systems and Positive Valence (aberrant salience). HiTOP: thought disorder. Maps to the SB genomic factor.

| Disorder | How it manifests | SNOMED CT / HPO term + ID | Confidence |
|---|---|---|---|
| Schizophrenia | Core: hallucinations, delusions, disorganization | Hallucinations 7011001; Delusions 2073000; Hallucinations HP:0000738; Delusion HP:0000746 | HIGH |
| Bipolar | Mood-congruent psychotic features during episodes | Psychosis HP:0000709 | HIGH |
| Cannabis UD | Acute psychotomimetic effects, elevated longitudinal psychosis risk | Cannabis-induced psychotic disorder 31898009 (approx); Psychosis HP:0000709 | MEDIUM |
| MDD | Psychotic depression (severe subset) | Psychosis HP:0000709 (subset) | LOW |
| Alcohol UD | Korsakoff psychosis, withdrawal-related | Korsakoff's psychosis 37439000 | LOW |
| PTSD / anxiety / ASD / OCD | Rare; transient or trauma-related perceptual disturbance | Psychosis HP:0000709 (rare) | LOW |

### 2.9 Arousal / sleep dysregulation (HP:0100785 family)

RDoC: Arousal and Regulatory Systems (arousal, circadian, sleep-wake). HiTOP: cuts across internalizing and thought disorder. Genetically diffuse; prominent in internalizing and SB factors.

| Disorder | How it manifests | SNOMED CT / HPO term + ID | Confidence |
|---|---|---|---|
| PTSD | Hyperarousal, exaggerated startle; trauma nightmares, REM disruption | Hypervigilance 247803003 (approx); Nightmares 247960002 (approx); Sleep disturbance 39898005 | HIGH |
| Bipolar | Decreased need for sleep (mania); hypersomnia (depression); circadian shift | Mania HP:0100754; Bipolar depressive episode 191627008 | HIGH |
| MDD | Insomnia (melancholic) vs hypersomnia (atypical) | Insomnia HP:0100785; Hypersomnia HP:0033813 | HIGH |
| Anxiety | Autonomic hyperarousal, sleep-onset difficulty | Anxiety state 48694002; relate to HP:0100785 | HIGH |
| Substance UDs | Withdrawal sleep disturbance, autonomic arousal (opioid storm) | Insomnia HP:0100785 (cannabis); Opioid withdrawal 33807004 | HIGH |
| Schizophrenia | Sleep architecture abnormalities, reduced sleep spindles | (relate to HP:0100785) | MEDIUM |
| ADHD | Sleep-onset delay, circadian phase delay | (relate to HP:0100785) | MEDIUM |
| Anorexia | Sleep disruption, leptin-driven hyperactivity | (relate to HP:0100785) | LOW |
| ASD / TS / OCD | Frequent sleep difficulties | (relate to HP:0100785) | MEDIUM |

### 2.10 Mood instability / cycling (HP:0100754 + HP:0000716)

RDoC: Negative Valence and Positive Valence (valence dysregulation). HiTOP: internalizing with a bipolar/thought-disorder bridge. Maps primarily to the SB factor (bipolar) and internalizing factor.

| Disorder | How it manifests | SNOMED CT / HPO term + ID | Confidence |
|---|---|---|---|
| Bipolar | Core: cycling between mania/hypomania and depression; rapid cycling, mixed features | Bipolar I disorder 371596008; Mania HP:0100754; Depressivity HP:0000716 | HIGH |
| MDD | Sustained low mood; recurrent episodes | Depressed mood 366979004; Depressivity HP:0000716 | HIGH |
| PTSD | Affective lability, irritability (negative-mood and arousal clusters) | Irritability HP:0000737 (approx); HP:0000716 | MEDIUM |
| Anorexia | Mood lability in starvation state | (relate to HP:0000716) | LOW |
| Substance UDs | Mood swings across intoxication/withdrawal cycle | Irritability HP:0000737 | MEDIUM |
| ADHD | Emotional dysregulation, irritability | Irritability HP:0000737 (approx) | MEDIUM |
| Schizophrenia | Affective flattening (opposite pole: restricted, not labile) | (relate to negative symptom) | LOW |
| TS / OCD / anxiety / ASD | Irritability/lability in subsets | Irritability HP:0000737 (subset) | LOW |

---

## 3. Master matrix

Rows = 14 disorders. Columns = the 10 dimensions. Cells: **P** = prominent/core (criterion-level), **+** = present/secondary, **o** = comorbid/subset only, **-** = not characteristic. Confidence suffix: H/M/L. Dimension keys: ANH = anhedonia/reward, NEG = negative affect/threat, CMP = compulsivity, IMP = impulsivity/disinhibition, COG = cognitive control, SOC = social-communication, SEN = sensory/interoceptive, PSY = psychosis, ARO = arousal/sleep, MOO = mood instability.

| Disorder | ANH | NEG | CMP | IMP | COG | SOC | SEN | PSY | ARO | MOO |
|---|---|---|---|---|---|---|---|---|---|---|
| Schizophrenia | P/H | +/L | o/L | -/L | P/H | +/M | +/M | P/H | +/M | +/L |
| Bipolar | P/H | +/M | o/L | P/H | +/M | -/L | -/L | P/H | P/H | P/H |
| MDD | P/H | P/H | o/L | -/L | +/M | +/L | +/L | o/L | P/H | P/H |
| PTSD | +/M | P/H | o/L | +/M | +/M | +/L | +/M | o/L | P/H | +/M |
| Anxiety | +/L | P/H | +/H | -/L | +/L | +/M | +/M | o/L | P/H | +/L |
| ASD | o/L | +/M | P/H | -/L | +/M | P/H | P/H | o/L | +/M | +/L |
| ADHD | +/M | o/L | o/L | P/H | P/H | +/L | -/L | -/L | +/M | +/M |
| OCD | o/L | P/H | P/H | -/L | +/M | -/L | +/L | -/L | +/M | +/L |
| Tourette | o/L | o/L | P/H | +/M | +/M | +/L | P/M | -/L | +/M | +/L |
| Anorexia | +/M | P/H | P/H | +/M | +/M | +/L | P/M | -/L | +/L | +/L |
| Alcohol UD | +/M | +/M | +/M | P/H | +/M | +/L | +/M | o/L | P/H | +/M |
| Opioid UD | +/M | +/M | +/M | P/H | +/L | +/L | +/M | -/L | P/H | +/M |
| Nicotine UD | +/L | +/M | +/M | P/H | +/L | -/L | +/M | -/L | P/H | +/M |
| Cannabis UD | +/L | +/M | +/M | P/H | +/M | +/L | +/M | +/M | +/H | +/M |

Reading the matrix by column: arousal/sleep (ARO) and negative affect (NEG) are the most universally present dimensions; psychosis (PSY) is the most disorder-restricted; compulsivity (CMP) and impulsivity (IMP) sort the set into two opposing externalizing/internalizing poles that nonetheless co-occur in substance use disorders.

---

## 4. Most reproducible transdiagnostic phenotype dimensions (ranked)

Ranking criteria: breadth (how many of the 14 express it), criterion-level prominence, replication across the source docs, and measurement clarity. Each row notes the RDoC domain, HiTOP spectrum, the genomic factor it tracks, and whether it is remotely/passively measurable via digital phenotyping (sleep actigraphy, activity/movement, speech/acoustic features, heart-rate variability, keystroke/usage logs).

| Rank | Dimension | Breadth (of 14) | RDoC | HiTOP | Genomic factor(s) | Passively measurable? |
|---|---|---|---|---|---|---|
| 1 | Arousal / sleep dysregulation | ~14 | Arousal/Regulatory | cross-spectrum | internalizing + SB + substance | YES, strongest: actigraphy sleep timing/duration/fragmentation, HRV, resting heart rate |
| 2 | Negative affect / threat / anxiety | ~13 | Negative Valence | internalizing | internalizing | PARTIAL: HRV (low HF-HRV), elevated heart rate, speech prosody, reduced activity range |
| 3 | Anhedonia / reward dysfunction | ~11 | Positive Valence | detachment | internalizing + SB + substance | PARTIAL: reduced movement/activity, reduced social-app/communication frequency, flattened speech |
| 4 | Impulsivity / disinhibition | ~8 | Positive Valence + Cognitive | disinhibited externalizing | substance + neurodevelopmental | PARTIAL: irregular activity bursts, erratic usage patterns, response-timing on tasks |
| 5 | Compulsivity / repetitive behavior | ~7 | Cognitive + Sensorimotor | compulsivity | compulsive/eating + substance | WEAK: repetitive movement patterns (accelerometry), ritualized timing |
| 6 | Cognitive control / executive dysfunction | ~12 (variable severity) | Cognitive | cross-spectrum | SB + neurodevelopmental | PARTIAL: keystroke dynamics, ambulatory cognitive tasks, speech complexity |
| 7 | Mood instability / cycling | ~7 | Negative + Positive Valence | internalizing/thought bridge | SB + internalizing | YES: longitudinal actigraphy and circadian shift, speech-sentiment trajectory, usage rhythm |
| 8 | Social-communication dysfunction | ~5 core | Social Processes | detachment | neurodevelopmental | PARTIAL: communication-log frequency, speech turn-taking, voice acoustics |
| 9 | Sensory / interoceptive atypicality | ~9 (sparse terms) | Sensorimotor | (HiTOP gap) | neurodevelopmental | WEAK: HRV as interoceptive proxy; otherwise lab-bound (P50, PPI) |
| 10 | Psychosis / reality distortion | ~3 core | Cognitive + Positive Valence | thought disorder | SB | WEAK: speech-coherence NLP markers (research-stage); otherwise clinician-rated |

**The passively-measurable subset.** Four dimensions are recoverable from continuous, low-burden sensor streams without a clinical visit:
- **Sleep/circadian (dimension 1)**: actigraphy and consumer wearables capture sleep onset, duration, fragmentation, and phase shift. This is the single most digitally tractable dimension and is altered in essentially all 14 disorders.
- **Autonomic arousal (dimensions 1, 2)**: HRV (especially HF-HRV), resting heart rate, and electrodermal activity index threat-reactivity and arousal. Low HF-HRV recurs across PTSD, anxiety, and depression.
- **Activity/motor (dimensions 3, 4, 7)**: accelerometry captures psychomotor retardation (anhedonia/depression), hyperactivity (ADHD, mania), and activity-rhythm instability (mood cycling).
- **Speech/language acoustics (dimensions 2, 3, 6, 8, 10)**: prosody, pause structure, semantic coherence, and turn-taking index negative affect, anhedonia (flattened affect), executive/cognitive load, social communication, and (research-stage) thought disorder.

Compulsivity, fine sensory gating (P50/PPI), and frank psychosis remain largely lab- or clinician-bound and are the weakest targets for passive digital phenotyping today.

---

## 5. Honest limits

**Self-report reliability.** Most MACRO phenotypes rest on patient self-report and clinician interview. Anhedonia, anxiety, craving, and intolerance of uncertainty are introspective constructs with state-dependent recall and demand characteristics. The same word ("anhedonia") spans consummatory vs anticipatory and motivational vs hedonic subcomponents that self-report does not separate.

**Diagnostic overlap inflates and confounds dimensions.** Because the source docs include heavily comorbid disorders (TS with ~50% OCD and ~50% ADHD; PTSD with MDD), a dimension marked "present" in a disorder may reflect a comorbid condition rather than the disorder's core biology. The matrix uses the "o" (comorbid/subset) code to flag this, but the boundary between intrinsic and comorbid expression is often unresolvable at the phenotype level.

**Ontology coverage is uneven.** SNOMED CT covers diagnostic syndromes and many symptoms well (PTSD ~91% term coverage), but HPO was built for Mendelian/rare-disease phenotyping and has sparse, sometimes mismatched coverage of psychiatric constructs. The clearest example: HPO "Anorexia" (HP:0002039) means loss of appetite, which is NOT the anorexia nervosa syndrome (appetite is often intact but fear-suppressed). Several research constructs (intolerance of uncertainty, premonitory urge, insistence on sameness, error-monitoring/ERN, body-image disturbance) have no clean single concept in either ontology and are carried as "approx, needs curation." All such flags from the source docs are preserved here; none of these IDs should be treated as curation-verified.

**Measurement validity of the passive subset.** Digital phenotyping markers (HRV, actigraphy, speech) are correlates, not direct readouts of the RDoC construct. They are nonspecific (low HF-HRV indexes arousal across many disorders and confounds), sensitive to context (caffeine, exertion, medication, device differences), and mostly validated in small or single-site cohorts. Speech-coherence markers of thought disorder remain research-stage. The ranking in Section 4 reflects current tractability, not established clinical validity.

**Dimensions are not orthogonal.** Anhedonia, negative affect, and arousal covary; compulsivity and impulsivity are poles of one axis that co-occur within substance use disorders over time. Treating them as 10 independent columns is a useful approximation, not a claim of statistical independence. A general psychopathology ("p") factor likely accounts for part of every column's cross-disorder spread.

---

## References

- Grotzinger AD, Werme J, Peyrot WJ, ... Smoller JW. Mapping the genetic landscape across 14 psychiatric disorders. Nature 2025. doi:10.1038/s41586-025-09820-3.
- Per-disorder MACRO sections and their cited primary sources: `../disease-biotypes/{schizophrenia, bipolar, mdd, ptsd, anxiety, asd, adhd, ocd, tourette, anorexia, sud-alcohol, sud-opioid, sud-nicotine, sud-cannabis}.md`.
- RDoC: NIMH Research Domain Criteria matrix (Negative Valence, Positive Valence, Cognitive Systems, Social Processes, Arousal/Regulatory, Sensorimotor).
- HiTOP: Kotov R, et al. The Hierarchical Taxonomy of Psychopathology (HiTOP). J Abnorm Psychol 2017.
- SNOMED CT and Human Phenotype Ontology (HPO) concept IDs as cited in the source docs; items flagged "approx, needs curation" require terminologist verification against current ontology releases.

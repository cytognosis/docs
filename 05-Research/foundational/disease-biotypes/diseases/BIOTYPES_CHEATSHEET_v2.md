# Mental Health Biotypes: Cheat Sheet v2

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: researchers, stakeholders
> **Tags**: `literature-synthesis`, `disease-biotypes`, `index`, `cheatsheet`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)

## Canonical per-disorder index

> This cheat sheet is the **canonical index** for disease biotypes. Each per-disorder dossier follows the Literature Synthesis template (cytognosis-doc skill v5.6.0).

| Disorder | Dossier |
|----------|---------|
| ADHD | [adhd.md](adhd.md) |
| Anorexia nervosa | [anorexia.md](anorexia.md) |
| Anxiety disorders | [anxiety.md](anxiety.md) |
| Autism (ASD) | [asd.md](asd.md) |
| Autism research brief | [asd-research-brief.md](asd-research-brief.md) |
| Bipolar disorder | [bipolar.md](bipolar.md) |
| Major depressive disorder | [mdd.md](mdd.md) |
| OCD | [ocd.md](ocd.md) |
| PTSD | [ptsd.md](ptsd.md) |
| Schizophrenia | [schizophrenia.md](schizophrenia.md) |
| SUD: alcohol | [sud-alcohol.md](sud-alcohol.md) |
| SUD: cannabis | [sud-cannabis.md](sud-cannabis.md) |
| SUD: nicotine | [sud-nicotine.md](sud-nicotine.md) |
| SUD: opioid | [sud-opioid.md](sud-opioid.md) |
| Tourette syndrome | [tourette.md](tourette.md) |
| Cross-scale: molecular/cellular | [../molecular-cellular-biotypes.md](../molecular-cellular-biotypes.md) |
| Cross-scale: multiscale biomarkers | [../multiscale-biomarkers.md](../multiscale-biomarkers.md) |
| Transdiagnostic: micro | [../transdiagnostic/transdiagnostic-micro.md](../transdiagnostic/transdiagnostic-micro.md) |
| Transdiagnostic: meso | [../transdiagnostic/transdiagnostic-meso.md](../transdiagnostic/transdiagnostic-meso.md) |
| Transdiagnostic: macro | [../transdiagnostic/transdiagnostic-macro.md](../transdiagnostic/transdiagnostic-macro.md) |
| Transdiagnostic: connectomic synthesis | [../transdiagnostic/transdiagnostic-connectomic-synthesis.md](../transdiagnostic/transdiagnostic-connectomic-synthesis.md) |


> **The expanded, multi-modal, transdiagnostic biotype reference.** Now covers 6 disorders (added autism), 4 evidence layers (connectomic, EEG/MEG, molecular/cellular, treatment-response), and explicit links between layers. ADHD-friendly format: scan first, drill down only where needed.
>
> **Sources (all in `research/`):**
> - `biotypes-{depression,anxiety,psychosis,ptsd,addiction,autism}.md`
> - `eeg-meg-biotypes.md`
> - `molecular-cellular-biotypes.md`
> - `neuroplastogen-response.md`
> - `neuromodulation-response.md`
> - `transdiagnostic-connectomic-synthesis.md`
> - `wearables-comparative.md`, `fnirs-deep-dive.md`, `neuromodulation.md`, `targeted-noninvasive-scanning.md`

---

## 60-second read

1. **6 disorders, 4 evidence layers, ~25 anchored biotypes.** Connectomic, EEG/MEG, molecular/cellular, and treatment-response biotypes converge on the same small number of brain circuits and molecular axes.
2. **One unifying mechanism keeps showing up: plasticity.** Castren framework. SSRIs, ketamine, psilocybin, ECT, and TMS all converge on BDNF/TrkB signaling. Olson + Castren (Moliner 2023 *Nat Neurosci*) showed psychedelics bind TrkB directly at ~1000x SSRI affinity. **"Low-BDNF / plasticity-deficit" is the strongest single transdiagnostic biotype.**
3. **Six molecular axes carry the heaviest cross-disorder load:** BDNF/TrkB plasticity, E/I imbalance (PV interneurons + gamma + 1/f slope), oxidative stress / mitochondria, dopaminergic, serotonergic, inflammatory.
4. **EEG/MEG adds two psychosis-distinguishing signatures that fNIRS cannot easily reach:** 40Hz auditory steady-state response and reduced sleep spindle density. Aperiodic 1/f slope is a portable E/I proxy for any wearable.
5. **Treatment-stratification is most mature for TMS (sgACC-dlPFC anticorrelation; 79% SAINT remission) and ketamine (anxious-anhedonic biotype responds best). Psychedelic stratification is emerging from the BDNF/plasticity-readiness story.**
6. **Drysdale's four biotypes remain a motivating example, not a clinical reality.** Dinga 2019 replication failed. Williams 2024 six-axis scaffold (n=801) is the better current framework.
7. **Headset target list expands from 8 to 12 anchor regions** to absorb autism (STS, FFA, IFG, right cerebellar Crus I/II).

---

## Master biotype table (transdiagnostic, multi-modal)

> **Layer** is the strongest evidence type. **Confidence**: HIGH = multi-cohort/multi-site replication; MEDIUM = single-consortium; LOW = single-lab or failed external replication.

| # | Biotype | Layer | Disorders | Anchor regions / signals | Confidence | Headline source |
|---|---------|-------|-----------|--------------------------|------------|-----------------|
| 1 | **Low-BDNF / plasticity-deficit** | Molecular | MDD-TRD, chronic SCZ, BD-depressive, PTSD, alcohol use disorder | Serum/plasma BDNF; postmortem TrkB; DLPFC + sgACC connectivity | HIGH | Castren 2022; Moliner 2023 *Nat Neurosci* |
| 2 | **PV-interneuron / E/I imbalance / gamma-deficit** | Molecular + EEG | SCZ (g = -0.27), ASD, MDD-cognitive subset | 40Hz ASSR, aperiodic 1/f, PV postmortem, MRS glutamate | HIGH | Lewis; Sohal & Rubenstein 2019 |
| 3 | **Oxidative stress / mitochondrial** | Molecular | SCZ subset, BD, ~30% ASD, MDD subset | Glutathione, 8-OHdG, in vivo CCO (broadband NIRS) | HIGH | Berk; Frye-Rossignol; Tachtsidis 2025 |
| 4 | **Hyperdopaminergic striatal (Howes Type A)** | Molecular + connectomic | SCZ treatment-responsive, addiction, psychotic mania | Associative striatum DA, anterior hippocampus CA1 | HIGH | Howes & McCutcheon |
| 5 | **Inflammatory / cytokine** | Molecular | MDD subset, SCZ subset, PTSD, AUD | CRP, IL-6, kynurenine | HIGH (biology); MEDIUM (operationalization) | Raison & Miller; Felger |
| 6 | **Serotonergic / SSRI-responsive** | Molecular | MDD, anxiety, OCD; 5-HT3 in AUD | 5-HTT, 5-HTTLPR, baseline 5-HT2A | MEDIUM | Moncrieff 2022 critique acknowledged |
| 7 | **DMN-rumination / subgenual hyperconnectivity** | Connectomic | MDD, PTSD | sgACC, PCC, mPFC, dlPFC | HIGH | Mayberg; Fox & Cash; Sheline |
| 8 | **Cognitive-control / dlPFC-dACC** | Connectomic + EEG | MDD, anxiety, SCZ, addiction, ASD | dlPFC (BA 46/9), dACC; frontal theta | HIGH | Williams iMAP 2024; B-SMART-fMRI |
| 9 | **Anhedonic / reward-deficit** | Connectomic + EEG | MDD, addiction, PTSD-dysphoric, SCZ negative | Ventral striatum, vmPFC, OFC; blunted RewP | HIGH | Pizzagalli EMBARC; Proudfit |
| 10 | **Threat-reactive / amygdala-vmPFC** | Connectomic + EEG | Anxiety (GAD), PTSD-hyperaroused, MDD-anxious | Amygdala, vmPFC, pregenual ACC; enhanced LPP | HIGH | Etkin; LeDoux; Stevens AURORA |
| 11 | **Salience / interoceptive (insula)** | Connectomic | Anxiety-panic, addiction-craving, MDD-somatic | Anterior insula, mid-insula, dACC | HIGH | Paulus, Khalsa, Naqvi |
| 12 | **B-SNIP 1: cognitive-deficit psychosis** | Connectomic + EEG | SCZ, schizoaffective | DLPFC, sup temporal, anterior hippocampus, MD thalamus; reduced P300 | HIGH | Clementz & Tamminga 2016 |
| 13 | **B-SNIP 2: sensory-hyperresponsive psychosis** | Connectomic + EEG | SCZ | Heschl's, planum temporale, sensorimotor; **reduced 40Hz ASSR + MMN** | HIGH | Clementz & Tamminga 2016 |
| 14 | **Treatment-resistant glutamatergic (Howes Type B)** | Molecular | SCZ (clozapine-responsive) | ACC, DLPFC, thalamus; elevated MRS glutamate | MEDIUM | Egerton STRATA |
| 15 | **Dissociative PTSD (Lanius)** | Connectomic | PTSD | Amygdala (overmodulated), mPFC, posterior insula | HIGH | Lanius 2010, 2020 |
| 16 | **VAN-deficit treatment-resistant** | Connectomic | PTSD, MDD | Right TPJ, anterior insula | MEDIUM | Etkin & Maron-Katz |
| 17 | **CSTC dysregulation (OCD)** | Connectomic | OCD | OFC, dACC, caudate head, MD thalamus; enhanced ERN | HIGH | Saxena; Riesel ERN meta |
| 18 | **Hyperreactive incentive-salience** | Connectomic + EEG | All SUDs, esp stimulants | NAc, OFC, anterior insula; cue-reactive ERPs | HIGH | Volkow; Goldstein iRISA |
| 19 | **Stress-driven negative-affect** | Connectomic | All SUDs, esp alcohol | Amygdala, BNST, insula | HIGH | Koob; Crews |
| 20 | **ASD-A: PV / gamma-deficit autism** | EEG + molecular | ASD | Auditory cortex, DLPFC, sensorimotor; reduced 40Hz ASSR + flat 1/f | HIGH | Sohal; Donoghue/Voytek; Edden MRS |
| 21 | **ASD-B: social brain hypoactivation** | Connectomic | ASD | STS, FFA, right IFG, amygdala, TPJ, mPFC | HIGH | EU-AIMS LEAP; ABIDE |
| 22 | **ASD-C: cerebellar-cortical** | Connectomic | ASD | Right Crus I/II, lobules VI/VII | HIGH | Tsai; Stoodley |
| 23 | **ASD-D: mTOR / synaptopathy** | Molecular | ASD (genetic subset) | PTEN, TSC1/2, SHANK3, FMR1 carriers | HIGH (for carriers) | SFARI; Sahin |
| 24 | **Sleep-spindle deficit** | EEG | SCZ, ASD, PTSD | NREM spindle density; sleep stages | HIGH | Manoach; Tononi; PTSD slow-wave |
| 25 | **HRV / autonomic dysregulation** | Physiological | Anxiety, PTSD, MDD, AUD | Reduced RMSSD; predicts tVNS response | HIGH | Thayer; Tang 2025 |

---

## Per-disorder cards (now 6)

### Depression (MDD, TRD)

> **What to bet on:** anhedonic, cognitive-control, DMN-rumination, anxious, inflammatory. Plus EEG: blunted RewP, REM density, low alpha peak. Molecular: low-BDNF / plasticity-deficit is the central transdiagnostic mechanism.

**Top connectomic biotypes:** anhedonic (ventral striatum, vmPFC), cognitive-control (dlPFC, dACC), DMN-rumination (sgACC, PCC), anxious-fronto-amygdala (amygdala, vmPFC).

**Top EEG/MEG signatures:**
1. **Blunted Reward Positivity (RewP/FRN)**: anhedonic biotype marker, EMBARC-replicated, single-task frontal-central EEG.
2. **REM density / REM latency**: pharmacotherapy and ketamine response predictor (Kupfer; 2025 ketamine work).
3. **Reduced individual alpha peak + elevated prefrontal delta**: TRD subgroup; theta-cordance predicts antidepressant response.

**Top molecular:** low-BDNF (serum or genotype Val66Met); CRP-stratified inflammatory; PV/gamma deficit in cognitive subtype.

**Treatment-stratified:**
- **Ketamine responders**: anxious-anhedonic biotype + low baseline ACC glutamate.
- **Psilocybin responders**: plasticity-deficit / low BDNF profile; DMN desynchronization during dose.
- **TMS responders**: strong sgACC-dlPFC anticorrelation (Fox & Cash; SAINT 79% remission).
- **SSRI responders**: 5-HTTLPR L/L, no clear connectomic predictor.

**Open:** `biotypes-depression.md`, plus EEG section of `eeg-meg-biotypes.md`, BDNF section of `molecular-cellular-biotypes.md`.

---

### Anxiety (GAD, panic, social, OCD)

> **What to bet on:** threat-dysregulation, salience-hyperconnectivity, BNST-sustained threat, CSTC (OCD). EEG: enhanced ERN (OCD endophenotype), frontal midline theta, elevated resting beta.

**Top connectomic biotypes:** threat-dysregulation (amygdala-vmPFC, GAD), salience-hyperconnectivity (insula-dACC, panic), BNST sustained-threat (right DLPFC, GAD-pure), CSTC (OFC-caudate-thalamus, OCD).

**Top EEG/MEG signatures:**
1. **Enhanced Error-Related Negativity (ERN)**: OCD endophenotype (Riesel 2019 meta); predicts first-onset GAD in adolescents.
2. **Frontal midline theta during cognitive control**: Cavanagh-Shackman meta-analysis; tracks trait anxiety.
3. **Elevated resting beta power**: panic/GAD.

**Top molecular:** serotonergic (SSRI responsive); GABA-deficit (zuranolone-relevant); glutamate elevations in CSTC (OCD).

**Treatment-stratified:**
- **TMS for OCD**: FDA-cleared 2018 (Brainsway H-coil, dorsal mPFC + ACC); CSTC biotype responder.
- **LSD (MM120)**: MindMed phase 2b for GAD positive 2024; plasticity-deficit predictor likely.
- **tDCS for anxiety**: BDNF Val66Met effects on response, conflicting evidence.

**Open:** `biotypes-anxiety.md`, plus EEG and treatment sections.

---

### Psychosis (SCZ, FEP, prodromal)

> **What to bet on:** B-SNIP 1 (cognitive-deficit) and B-SNIP 2 (sensory-hyperresponsive); Howes Type A and Type B. EEG signatures are the strongest psychiatric EEG findings overall (40Hz ASSR, MMN, P3b, sleep spindles).

**Top connectomic biotypes:** B-SNIP 1 (DLPFC, sup temporal, anterior hippocampus CA1), B-SNIP 2 (Heschl's, sensorimotor, MD thalamus), Howes Type A (associative striatum, hippocampus), Howes Type B (ACC, DLPFC), C4-pruned (cortical pruning).

**Top EEG/MEG signatures (most replicated in psychiatry):**
1. **Reduced 40Hz auditory steady-state response (ASSR)**: clean PV-interneuron/NMDA mechanism, 30+ replications, B-SNIP 2 marker.
2. **Reduced MMN + P3b**: classic endophenotype pair; MMN predicts CHR-P conversion (NAPLS).
3. **Reduced sleep spindle density**: replicated; present in unaffected relatives; thalamic reticular nucleus marker.

**Top molecular:** PV/gamma deficit; oxidative stress (glutathione); hyperdopaminergic (Type A); glutamatergic (Type B); C4-pruned inflammatory.

**Treatment-stratified:**
- **Antipsychotic response**: Type A predicts D2 antagonist response; Type B predicts clozapine need.
- **TMS for negative symptoms / hallucinations**: limited but emerging; biotype data thin.
- **NAC**: oxidative-stress biotype responders (modest effect).
- **Pomaglumetad failure**: cautionary tale of stratification failure (negative pivotal trial in mGluR2/3 strata that didn't replicate).

**Open:** `biotypes-psychosis.md`, plus EEG and molecular sections.

---

### PTSD

> **What to bet on:** threat-reactive, dissociative (Lanius), VAN-deficit, dysphoric/low-reward, inflammaging. EEG: reduced sleep slow-wave, theta wPLI, microstate E dynamics.

**Top connectomic biotypes:** hyperaroused threat-reactive (amygdala, vmPFC), dissociative (Lanius overmodulation), VAN-deficit (right TPJ; Etkin), dysphoric/low-reward (overlaps MDD anhedonic).

**Top EEG/MEG signatures:**
1. **Reduced slow-wave activity + altered NREM architecture**: sleep is the most reproducible PTSD biomarker layer.
2. **Theta-band wPLI connectivity**: rumination/re-experiencing index.
3. **Reduced alpha power + altered microstate E dynamics**.

**Top molecular:** HPA axis (low cortisol; Yehuda); FKBP5 methylation (Klengel-Binder); inflammaging (Wolf accelerated epigenetic aging); BDNF Val66Met effects on exposure therapy.

**Treatment-stratified:**
- **MDMA-AT**: dissociative subtype shows numerically larger response; MAPP1/MAPP2 pooled subgroup data confirms childhood trauma does NOT attenuate response (unusual).
- **TMS for PTSD**: Phillips 2025 *Am J Psych* (n=50) showed right dlPFC-amygdala threat-circuit targeting outperformed sham; threat biotype responder.
- **Prazosin**: nightmares subtype; HRV-stratified response.

**Open:** `biotypes-ptsd.md`, plus EEG and treatment sections.

---

### Addiction (SUDs)

> **What to bet on:** hyperreactive incentive-salience, reward-deficiency/PFC hypofunction, stress-driven negative-affect. EEG: reduced P300 (broad vulnerability marker), elevated beta, cue-reactive ERPs.

**Top connectomic biotypes:** hyperreactive incentive-salience (NAc, OFC, insula), reward-deficiency/PFC hypofunction (dlPFC, ACC), stress-driven negative-affect (amygdala, BNST, insula), neuroinflammatory (alcohol-dominant), adolescent developmental risk (pre-initiation).

**Top EEG/MEG signatures:**
1. **Reduced P300 amplitude**: broad vulnerability marker present in unaffected relatives (Begleiter, Porjesz).
2. **Elevated resting beta power**: withdrawal signature.
3. **Cue-reactive ERPs**: drug-stimulus-specific.

**Top molecular:** dopaminergic (Volkow); BDNF (drug-specific: cocaine ↑ vs alcohol ↓ striatal BDNF); OPRM1 A118G (opioid response, naltrexone in AUD); ADH1B/ALDH2 (alcohol metabolism); neuroinflammatory (TLR4, alcohol).

**Treatment-stratified:**
- **Deep TMS for smoking**: FDA-cleared 2020 (Brainsway H4-coil); salience network connectivity moderator (Dinur-Klein 2022).
- **TMS for alcohol craving**: insula-targeted; emerging.
- **Ondansetron in AUD**: 5-HTTLPR L/L responders (Johnson trials).
- **Naltrexone in AUD**: OPRM1 A118G responders.
- **Psilocybin in AUD**: Bogenschutz 2022 *JAMA Psych* positive trial.

**Open:** `biotypes-addiction.md`, plus EEG and treatment sections.

---

### Autism (ASD) (new in v2)

> **What to bet on:** PV/gamma-deficit (most replicated EEG psychiatric finding outside of SCZ); social brain hypoactivation; cerebellar-cortical; mTOR/synaptopathy (single-gene subtypes); sensory perception subtype. Neurodiversity framing: biotypes for personalized support, not for "fixing" autism.

**Top connectomic biotypes:** social brain hypoactivation (STS, FFA, IFG, amygdala), cerebellar-cortical (Crus I/II), DMN/developmental-trajectory (Bethlehem-Lombardo normative deviation), sensory perception / EPF (Mottron; posterior cortical hyperactivity).

**Top EEG/MEG signatures:**
1. **Reduced relative alpha power**: meta-analytic g = -0.35 across 41 studies.
2. **Flatter aperiodic 1/f slope**: E/I imbalance proxy, replicated across 5+ labs; **the most portable cross-disorder biomarker in this whole document**.
3. **Reduced 40Hz ASSR + altered evoked gamma; reduced sleep spindle density**: shared signature with SCZ.

**Top molecular:** mTOR/PTEN/TSC1/2 (single-gene); SHANK1/2/3; NLGN/NRXN/CNTNAP2; PV/SST GABAergic deficits; ~30% mitochondrial subtype (Frye-Rossignol).

**Treatment-stratified:**
- **Risperidone / aripiprazole**: irritability subtype.
- **Balovaptan**: failed phase 3 despite promising oxytocin/vasopressin biology (cautionary tale on social-brain biotype stratification).
- **Everolimus in TSC-ASD**: null cognitive outcomes despite molecular fit (cautionary tale on mTOR stratification at endpoint level).
- **SSRIs for repetitive behaviors**: mixed evidence, subtype-dependent.
- **Psilocybin in ASD**: very early, Imperial work in adjacent populations.

**Open:** `biotypes-autism.md`.

---

## Cross-disorder molecular axes (6 axes, the unifying layer)

> **These are the molecular biotypes that cut across the 6 disorders. They are the operational backbone of the molecular-cellular layer of the Cytoverse coordinate.**

| Axis | What it indexes | Disorders most loaded | Wearable readout pathway |
|------|-----------------|----------------------|--------------------------|
| **BDNF/TrkB plasticity** | Synaptic plasticity capacity; psychedelic / ketamine / SSRI / TMS / ECT all converge here | MDD-TRD, SCZ, BD, PTSD, AUD | Serum BDNF (finger-prick); Val66Met genotype (cheek swab); functional EEG plasticity probes |
| **E/I imbalance (PV / gamma)** | Parvalbumin interneuron function; cortical inhibition | SCZ, ASD, MDD-cognitive | **Aperiodic 1/f slope (any EEG)**; 40Hz ASSR; MRS glutamate/GABA |
| **Oxidative stress / mitochondrial** | Mitochondrial ATP production, ROS, glutathione | SCZ subset, BD, ~30% ASD, MDD subset | **Cytochrome-c-oxidase via broadband NIRS** (Tachtsidis); 8-OHdG; lactate |
| **Dopaminergic** | Striatal vs cortical DA; D1/D2 balance | SCZ Type A, addiction, MDD-anhedonic | RewP EEG signature; HRV; eye-blink rate (D2 proxy) |
| **Serotonergic** | 5-HT2A/5-HT1A/5-HTT; psychedelic and SSRI target | MDD, anxiety, OCD; AUD via 5-HT3 | Limited direct wearable readouts; pharmacogenomics |
| **Inflammatory** | CRP, IL-6, kynurenine, TLR4 | MDD subset, SCZ subset, PTSD, AUD | CRP finger-prick; IL-6; cytokine panels |

**The cross-cutting integration:** Castren framework says SSRIs, ketamine, psilocybin, ECT, and TMS all increase plasticity by upregulating BDNF/TrkB. **Plasticity restoration is the transdiagnostic mechanism.** Olson + Castren (Moliner 2023 *Nat Neurosci*) showed psilocin and LSD bind TrkB directly at ~1000x SSRI affinity, at residues Y433/A434/V436/V437. Y433F knockout abolishes plasticity effects but preserves 5-HT2A head-twitch in mice. **This argues psychedelics' antidepressant mechanism is TrkB-mediated even more than 5-HT2A-mediated.**

---

## Cross-disorder connectomic axes (5–6 axes)

| Axis | What it indexes | Disorders most loaded | Anchor regions |
|------|-----------------|----------------------|----------------|
| **Negative affect / threat** | Amygdala hyperreactivity, weak PFC control | Anxiety, PTSD, anxious MDD | Amygdala, vmPFC, pregenual ACC |
| **Reward / anhedonia** | Ventral striatum hypofunction, OFC valuation deficits | MDD, addiction-reward-deficit, PTSD-dysphoric, SCZ-negative | Ventral striatum, vmPFC, OFC, VTA |
| **Cognitive control** | dlPFC executive load, dACC monitoring | All 6 disorders | dlPFC (BA 46/9), dACC |
| **Salience / interoception** | Anterior insula and dACC switching | Anxiety-panic, addiction-craving, MDD, ASD-sensory | Anterior insula, dACC |
| **Attention / vigilance** | DMN, VAN, dorsal attention | PTSD VAN-deficit, MDD DMN-rumination, SCZ attention, ASD-DMN | PCC, precuneus, right TPJ |
| **Sensory gating** | Auditory/sensorimotor hyperresponsiveness | SCZ (B-SNIP 2), ASD-sensory | Heschl's, planum temporale, sensorimotor |

Sensory gating is the most psychosis-distinguishing axis; autism shares some sensory features but with a different signature (posterior cortical hyperactivity rather than sensorimotor gating failure).

---

## Cross-disorder EEG/MEG layer (top signatures, ranked by replication strength)

| Signature | Disorder(s) | Notes | Wearable feasibility |
|-----------|-------------|-------|----------------------|
| **40Hz auditory steady-state response (ASSR)** | SCZ, ASD | 30+ replications in SCZ; clean PV/gamma mechanism | Yes (low-channel EEG with auditory stim) |
| **Reduced MMN** | SCZ, prodromal psychosis, ASD | Predicts CHR-P conversion (NAPLS) | Yes (paradigm-driven) |
| **Reduced sleep spindle density** | SCZ, ASD, PTSD | Endophenotype; present in unaffected relatives | Yes (sleep EEG; in-home overnight) |
| **Aperiodic 1/f slope (flatter)** | SCZ, ASD, MDD-cognitive | The most portable E/I proxy; replicates across 5+ labs | **Yes (any EEG, including consumer)**: strong candidate |
| **Reduced Reward Positivity (RewP)** | MDD-anhedonic | EMBARC-replicated; single-task | Yes (consumer EEG with reward task) |
| **Enhanced ERN** | OCD, anxiety | Riesel meta-analysis; predicts onset | Yes (consumer EEG with flanker task) |
| **Reduced P300** | SCZ, addiction (vulnerability) | Classic endophenotype; broad | Yes (oddball paradigm; standard EEG) |
| **REM density / latency** | MDD | Predicts pharmacotherapy + ketamine response | Yes (in-home sleep EEG) |
| **Frontal midline theta** | Anxiety, cognitive control | Cavanagh-Shackman | Yes |
| **Reduced relative alpha (ASD)** | ASD | Meta g = -0.35 | Yes |

**Implication for Cytoscope:** the optical-EEG hybrid headset (Cytoscope variant 2) gets very high biotype-coverage value from adding **aperiodic 1/f slope, RewP, and 40Hz ASSR** as standard EEG channels. These three alone cover ~70% of the EEG/MEG signature value.

---

## Treatment-stratified biotypes: neuroplastogens

> **The 5 most actionable biotype-by-drug patterns from `neuroplastogen-response.md`.**

| Pattern | Biotype | Drug | Evidence |
|---------|---------|------|----------|
| **1. Plasticity-deficit is the unifying responder signature** | Low BDNF, Val66Met Met-carriers respond LESS, low ACC glutamate predicts better ketamine response | Ketamine, psilocybin, MDMA, LSD | Moliner 2023; Castren 2022; multiple meta-analyses |
| **2. Anxious-anhedonic depression → ketamine responder** | Pizzagalli NAc D1-MSN; Williams 6-biotype anxious-anhedonic | Ketamine, esketamine | TRD ketamine meta-analyses; anxious-depression subgroup |
| **3. Dissociative PTSD → MDMA responder** | Lanius dissociative subtype | MDMA-AT | MAPP1, MAPP2 pooled subgroup; childhood trauma does NOT attenuate (unusual) |
| **4. DMN desynchronization during dose = response biomarker** | Acute DMN modularity reduction predicts sustained response | Psilocybin, LSD, DMT | Imperial trials; Carhart-Harris REBUS |
| **5. Critical-period reopening is drug-specific** | Window depth & duration: ket ~48h, psi ~2wk, MDMA ~2wk, LSD ~3wk, ibog ~4wk (mouse) | All neuroplastogens | Dölen lab |

**The big mechanism story:** SSRIs, ketamine, ECT, TMS, AND psychedelics all converge on BDNF/TrkB plasticity restoration. Psychedelics may work via direct TrkB binding (Moliner 2023) more than via 5-HT2A. **This collapses the apparent diversity of antidepressants into one mechanism.**

---

## Treatment-stratified biotypes: neuromodulation

> **The 5 most actionable biotype-by-modulation patterns from `neuromodulation-response.md`.**

| Pattern | Biotype | Modality | Evidence |
|---------|---------|----------|----------|
| **1. sgACC-dlPFC anticorrelation → TMS responder** | Stronger pre-treatment anticorrelation predicts response (r ≈ 0.3–0.5) | rTMS, iTBS, SAINT | Fox & Cash 2012; Weigand 2018; Cash 2021; SAINT 79% remission (n=29) |
| **2. Threat-circuit (right dlPFC-amygdala) → PTSD TMS responder** | Threat biotype operative for PTSD and high-anxiety depression | Personalized fMRI-guided rTMS; LIFU to amygdala | Phillips 2025 *Am J Psych* (n=50); UCLA + U Arizona LIFU |
| **3. Salience network → addiction TMS responder** | Younger age, shorter smoking history, salience network connectivity | Deep TMS H4-coil (FDA-cleared smoking 2020); striatal tTIS emerging | Dinur-Klein 2022; Wessel & Hummel 2023 |
| **4. Cognitive-control biotype → cognitive-deficit MDD TMS responder** | dlPFC-dACC connectivity restoration + Go/NoGo improvement | iTBS biotype-matched | B-SMART-fMRI 2024 (n=43 veterans) |
| **5. Low HRV (RMSSD) → tVNS responder** | Low baseline vagal tone benefits most | taVNS / cVNS | Tang 2025 *Mol Psych* |

**The Drysdale 2017 TMS-by-biotype data in detail:**
- Biotype 1 (anxious-arousal): 82.5% TMS response
- Biotype 2 (anhedonia): 25.0% TMS response
- Biotype 3: 61.0%
- Biotype 4: 29.6%

Dinga 2019 failed to replicate the 4 clusters themselves, so these specific percentages must be interpreted as a motivating example, not a current clinical fact. The **biology** of biotype-stratified TMS response is supported by SAINT and B-SMART; the **specific Drysdale clusters** are not.

---

## Headset target list v2 (expanded for autism, now 12 anchors)

> **The 8 anchors from v1 plus 4 added for autism social brain and cerebellar coverage.**

| Priority | Region | Disorders it serves | Why |
|----------|--------|---------------------|-----|
| 1 | **DLPFC (BA 46/9)** | All 6 | Cognitive control biotype; canonical TMS target |
| 2 | **dACC / dorsomedial PFC** | All 6 | Salience switching, threat monitoring |
| 3 | **vmPFC / OFC** | MDD, anxiety, PTSD, addiction, ASD | Reward, emotion regulation, valuation |
| 4 | **Anterior insula** | Anxiety, addiction, MDD, ASD-sensory | Interoceptive vigilance, craving |
| 5 | **Subgenual ACC** | MDD, PTSD | Indexed via dlPFC anticorrelation |
| 6 | **Superior temporal / Heschl's** | Psychosis, **ASD-A (PV/gamma)** | The psychosis-specific target; also autism sensory |
| 7 | **Posterior cingulate / precuneus** | MDD, PTSD, ASD-DMN | DMN rumination hub |
| 8 | **Ventral striatum + amygdala** (via cortical effectors) | MDD, addiction, anxiety, PTSD | Depth-limited; index indirectly |
| **9 (NEW)** | **Superior temporal sulcus (STS)** | **ASD-B (social brain)** | Social cognition; biological motion |
| **10 (NEW)** | **Fusiform face area (FFA)** | **ASD-B (social brain)** | Face processing |
| **11 (NEW)** | **Right inferior frontal gyrus (IFG)** | **ASD-B; language**, addiction (inhibitory control) | Mirror neuron system; response inhibition |
| **12 (NEW)** | **Right cerebellar Crus I/II** | **ASD-C**, addiction-alcohol, psychosis cognitive dysmetria | Cerebellar cognitive contributions |
| Tier 2 | Lateral cerebellum | Psychosis, addiction-alcohol | Cognitive dysmetria, cerebellar atrophy |

---

## The wearable readout stack (what Cytoscope needs to acquire)

> **For each of the 6 molecular axes plus the connectomic and EEG layers, here is what the Cytoscope hybrid headset would need to measure.**

| Layer | Axis / signal | Acquisition method | Phase |
|-------|---------------|-------------------|-------|
| Connectomic | Cortical hemodynamics (HbO2, HbR) | TD-fNIRS, HD-DOT | Phase 0–1 |
| Connectomic | Cerebral blood flow | DCS / SCOS | Phase 1 |
| Molecular | Mitochondrial function (CCO) | Broadband NIRS (Tachtsidis) | Phase 1 |
| Molecular | E/I balance | EEG aperiodic 1/f slope (FOOOF) | Phase 1 |
| Molecular | Gamma function (PV interneuron) | 40Hz ASSR via EEG with auditory click train | Phase 1 |
| Connectomic | Default mode dynamics | Multi-channel fNIRS + EEG microstates | Phase 1 |
| EEG | Reward Positivity (RewP) | Consumer-grade EEG + reward task | Phase 1 |
| EEG | ERN | Consumer-grade EEG + flanker task | Phase 1 |
| EEG | MMN | Auditory oddball EEG paradigm | Phase 1 |
| EEG | P300 | Standard oddball EEG | Phase 1 |
| EEG | Sleep spindles | In-home overnight EEG headband | Phase 2 |
| Molecular | BDNF serum | Finger-prick lateral flow (off-headset) | Phase 2 |
| Molecular | CRP, IL-6 | Finger-prick + lateral flow (off-headset) | Phase 2 |
| Physiological | HRV (RMSSD) | PPG or ECG patch | Phase 0 |
| Molecular | Cortisol / alpha-amylase | Saliva (off-headset) | Phase 2 |
| Genetic | Val66Met, 5-HTTLPR, COMT, MTHFR, CYP2D6/2C19 | One-time cheek-swab pharmacogenomics panel | Phase 0 (off-headset) |

**Five of six molecular axes are addressable by a Cytoscope hybrid stack today.** The serotonergic axis remains the hardest noninvasive readout (5-HT2A occupancy needs PET).

---

## Things to be honest about (expanded for v2)

- **Drysdale 2017 four-biotype model**: Dinga 2019 replication failed. The biology of stratification is real; the specific clusters are not.
- **Williams 2024 six-biotype scaffold**: best current framework; not yet independently replicated outside the Stanford network.
- **AURORA PTSD biotypes (Stevens & Ressler)**: Ben-Zion 2024 replication failed.
- **TSPO PET microglial activation in psychosis**: less robust than initial reports suggested.
- **Structural-MRI-only biotypes**: Cohen's d ≈ 0.1–0.14, too small for individual-level inference.
- **Polygenic risk scores**: explain only 1–3% of variance in 2026.
- **Microbiome biotypes for psychiatry**: real biology, weak effect sizes, no clinical operationalization.
- **EROS (event-related optical signal)**: 30 years of mostly single-lab findings. Not a defensible primary technical claim.
- **Serum BDNF**: assay variability is huge; serum doesn't faithfully reflect brain BDNF.
- **Psychedelic-TrkB direct binding (Moliner 2023)**: single-lab finding so far; needs independent replication. The Y433F knockout result is compelling but rests on one paper.
- **Pomaglumetad failure (mGluR2/3)**: cautionary tale of stratification at the wrong endpoint.
- **Balovaptan in autism**: failed phase 3 despite promising oxytocin biology; cautionary tale on social-brain biotype stratification.
- **Everolimus in TSC-ASD**: null cognitive outcomes despite molecular fit.
- **Functional unblinding in psychedelic trials**: confounds effect size estimation across the entire field.
- **SAINT (n=29)**: one landmark trial. Replication and scale-up pending.

---

## How to use this doc

- **For the NSF X-Labs Phase 0 proposal:** the 12-region headset target list (above) feeds §1.2. The molecular-axis table feeds §2.3 (the multi-chromophore stack). The treatment-stratification tables feed §3 Outcomes 3 and 4. The "what to bet on" lines on each disorder card feed the executive framing.
- **For the ARPA-H PHO map work:** the master biotype table (25 entries) defines the supervised heads of the multi-scale foundation model. The molecular axes define the molecular feature panels. The honest-limits section defines the analysis plan and replication checks.
- **For neuroplastogen / neuromodulation trial design:** the treatment-stratified tables define the prospective stratification arms.
- **For internal calibration:** if someone proposes a biotype that's not in the master table, the default answer is "single-lab finding, insufficient evidence." Use the honest-limits section as the conservative prior.

---

## Files referenced

- Depression biotypes (target archived/removed)
- Anxiety biotypes (target archived/removed)
- Psychosis biotypes (target archived/removed)
- PTSD biotypes (target archived/removed)
- Addiction biotypes (target archived/removed)
- Autism biotypes (target archived/removed) (NEW)
- [EEG/MEG biotypes across all disorders](../../neurosensing/eeg-meg-biotypes.md) (NEW)
- [Molecular/cellular cross-cutting biotypes](../molecular-cellular-biotypes.md) (NEW)
- [Neuroplastogen differential response](../../treatment/neuromodulation/neuroplastogen-response.md) (NEW)
- [Neuromodulation differential response](../../treatment/neuromodulation/neuromodulation-response.md) (NEW)
- [Transdiagnostic connectomic synthesis (v1)](../transdiagnostic/transdiagnostic-connectomic-synthesis.md)
- [Research SYNTHESIS](../../../../02-Funding/submissions/Grants/NSF/X-labs/SYNTHESIS.md)
- v1 cheatsheet (now superseded but kept for reference) (target archived/removed)

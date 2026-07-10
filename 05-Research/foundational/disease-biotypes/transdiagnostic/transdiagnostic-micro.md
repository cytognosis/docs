# Transdiagnostic MICRO synthesis: molecular, genetic, cellular, and immune biotypes across 14 psychiatric disorders

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: researchers, stakeholders
> **Tags**: `literature-synthesis`, `disease-biotypes`, `transdiagnostic`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)

Prepared for Cytognosis Foundation. Date: 25 May 2026. This document synthesizes the MICRO-scale sections of the 14 per-disorder biotype docs (schizophrenia, bipolar disorder, MDD, PTSD, anxiety, ASD, ADHD, OCD, Tourette, anorexia nervosa, and alcohol/opioid/nicotine/cannabis use disorders). It identifies the molecular and cellular dysregulations that recur ACROSS disorders, harmonizes them to Gene Ontology (GO), maps each axis onto the Nature 2025 five-factor genomic structure, and ranks the most reproducible transdiagnostic molecular biotypes. Confidence ratings follow the shared convention: HIGH (multi-cohort/multi-site replication), MEDIUM (single-consortium or moderate effect), LOW (single-lab or failed external replication). Replication failures are flagged. No em dashes are used.

---

## 1. Framing: five genomic factors and how molecular axes distribute across them

Grotzinger, Werme, Peyrot, ... Smoller (Nature 2025, doi:10.1038/s41586-025-09820-3; 1,056,201 cases) resolved the genetic landscape of 14 psychiatric disorders into 5 genomic factors that explain roughly 66 percent of genetic variance across 238 pleiotropic loci:

1. **SB factor** (schizophrenia + bipolar disorder): shared signal enriched in genes expressed in **excitatory neurons**.
2. **Internalizing factor** (major depression + PTSD + anxiety): shared signal associated with **oligodendrocyte** biology.
3. **Neurodevelopmental factor** (ASD + ADHD + Tourette, childhood-onset; spans into others).
4. **Compulsive/eating factor** (OCD + anorexia + Tourette).
5. **Substance-use factor** (alcohol + opioid + nicotine + cannabis).

The signal shared across all 14 disorders is enriched for broad transcriptional regulation; factor-specific pathways are narrower. The single most useful framing fact for a molecular sensing platform is that the two largest factors carry different CELL-TYPE signatures: the SB factor is excitatory-neuron-centric (schizophrenia snRNA-seq confirms excitatory neurons as the most transcriptionally altered cell class, Ruzicka 2024), whereas the internalizing factor is oligodendrocyte/myelin-centric (consistent with the long-standing glial-loss postmortem findings in MDD and PTSD). The neurodevelopmental and compulsive factors converge on synaptic and interneuron developmental programs (cell-adhesion, GABAergic interneuron migration), and the substance-use factor carries reward-dopaminergic plus metabolic/pharmacogenetic biology that the other factors lack.

The molecular AXES described below cut across these factors rather than respecting them. BDNF/TrkB plasticity, E/I imbalance, oxidative/mitochondrial stress, immune/microglial activation, and the five classical neurotransmitter families each recur in multiple factors. The job of this synthesis is to identify which of these axes are reproducible enough, and shared widely enough, to define transdiagnostic biotypes worth sensing.

---

## 2. Cross-cutting molecular axes

### 2.1 BDNF/TrkB neurotrophin signaling and neuroplasticity (GO:0048011 neurotrophin TRK receptor signaling; GO:0048167 regulation of synaptic plasticity; GO:1900273 positive regulation of LTP)

The BDNF/TrkB axis is the most mechanistically central transdiagnostic molecular axis because it is the convergent pivot of effective treatment, not because it is the strongest risk locus. The Castren and Saarma groups (Moliner et al. 2023, doi:10.1038/s41593-023-01316-5; Casarotto, Umemori, Castren 2022) showed that SSRIs, ketamine, and classical psychedelics all bind directly to the transmembrane domain of TrkB dimers and allosterically potentiate endogenous BDNF signaling. LSD and psilocin bind TrkB with affinity roughly 1,000-fold higher than fluoxetine (K_i ~3 to 7 nM vs ~4.8 microM), and the Y433F point mutation abolishes binding of all four drug classes while sparing BDNF itself. This is the "iPlasticity" framework: ECT, ketamine, psilocybin, LSD, SSRIs, exercise, and VNS all elevate BDNF/TrkB signaling and induce a juvenile-like plasticity state. A low-BDNF/plasticity-deficit biotype therefore predicts poorer response across all of these and recurs across disorders.

| Disorder | Specific finding | Direction | Confidence |
|---|---|---|---|
| Schizophrenia | Reduced peripheral BDNF (smaller effect than MDD); reduced BDNF mRNA in DLPFC/hippocampus; BDNF x TNF haplotype tracks cognition | Low (trait-like) | MEDIUM |
| Bipolar | Peripheral BDNF falls in BOTH mania and depression, recovers in euthymia; m-BDNF/pro-BDNF ratio separates BD from MDD | Low (state-dependent) | MEDIUM-HIGH |
| MDD | Reduced serum/plasma BDNF recovering with response; Val66Met (rs6265) Met carriers show blunted release and reduced ketamine/SSRI response; TrkB is the convergent antidepressant pivot | Low | HIGH (mechanism) |
| PTSD | BDNF Val66Met Met allele tied to impaired fear extinction and poorer exposure-therapy response; BDNF gates extinction plasticity | Low/dysfunctional extinction | MEDIUM |
| Anxiety | Val66Met modulates extinction and amygdala-vmPFC function; lower peripheral BDNF in some samples; neuroplastogen (MM120/LSD, ketamine) mechanism via TrkB-mTOR | Low | MEDIUM |
| ASD | Reduced TrkB-PI3K-AKT1 signaling in idiopathic brain tissue; serum BDNF heterogeneous (elevated/reduced/unchanged, assay-dependent) | Mixed/reduced signaling | LOW (serum heterogeneous) |
| ADHD | Val66Met association inconsistent; BDNF tied to cortical-maturation timing (delayed-maturation model) | Unclear | LOW (gene), MEDIUM (developmental) |
| OCD | Val66Met inconsistent; plasticity central to ERP/CBT extinction learning and to rapid ketamine anti-obsessional effect | Modulatory | LOW (gene), MEDIUM (plasticity mechanism) |
| Tourette | BDNF not a primary TS gene; interneuron maturation is plasticity-relevant | Not primary | MEDIUM (developmental) |
| Anorexia | BDNF (11p14.1) is a metabolic-neurological hub in 2026 MTAG; serum BDNF reduced in acute AN, partial recovery with weight; hypothalamic BDNF-TrkB regulates feeding. NOTE: Val66Met candidate-gene claim FAILED meta-analytic replication | Low (state) | MEDIUM (hub/state), LOW (Val66Met, flagged) |
| Alcohol UD | Alcohol DECREASES dorsal-striatal BDNF (opposite to cocaine); restoring BDNF reduces drinking in rodents | Decreased (drug-specific) | MEDIUM-HIGH |
| Opioid UD | Opioids DECREASE VTA BDNF (opposite to stimulants); shrinks dopamine soma, shifts reward signaling | Decreased (drug-specific) | MEDIUM |
| Nicotine UD | Not a primary axis; nAChR-driven plasticity dominates | Not primary | LOW |
| Cannabis UD | Not a primary axis; eCB-LTD impairment dominates plasticity story | Not primary | LOW |

Reading: low or dysfunctional BDNF/TrkB recurs in essentially every disorder where it has been studied, but with two distinct flavors. A trait-like low-BDNF picture (chronic SCZ) versus a state-dependent drop that tracks the episode (BD, MDD, AN, acute SUD). The PTSD/anxiety/OCD signal is specifically about BDNF-gated EXTINCTION plasticity rather than circulating level. The substance disorders show a drug-specific DECREASE in striatal/VTA BDNF (alcohol, opioids) that de-represses intake, which inverts the "more BDNF is better" logic and is an important caveat.

### 2.2 Excitatory/inhibitory (E/I) imbalance, with region (GO:0035249 glutamatergic synaptic transmission; GO:0051932 GABAergic synaptic transmission; parvalbumin interneurons; gamma oscillations)

E/I imbalance is the most regionally specific transdiagnostic axis, and the region matters functionally. The recurring cellular substrate is the parvalbumin-positive (PV) fast-spiking GABAergic interneuron, whose loss or hypofunction disinhibits pyramidal cells, degrades gamma-band synchrony, and shifts the balance toward excitation. PV cells are also oxidatively vulnerable, which links this axis to 2.3.

| Disorder | Specific finding | Direction + region | Confidence |
|---|---|---|---|
| Schizophrenia | NMDA hypofunction on PV interneurons; reduced PV density and GAD67; elevated ACC glutamate (MRS) in treatment-resistant cases | I-down (PV) in DLPFC and hippocampal CA1; E-up; glutamate up in ACC | HIGH |
| Bipolar | Elevated Glx on MRS across states; GABAergic deficits; CACNA1C/ANK3 excitatory-neuron excitability | E-up in ACC and prefrontal cortex | MEDIUM |
| MDD | Reduced cortical GABA (MRS) in prefrontal/occipital cortex; ketamine produces transient glutamate surge in ACC/PFC; zuranolone (GABA-A PAM) works | I-down in PFC | MEDIUM |
| PTSD | Postmortem downregulated interneuron module (ELFN1); single-cell localizes to inhibitory interneurons | I-down in prefrontal cortex (dlPFC) | MEDIUM-HIGH |
| Anxiety | Reduced GABA-A binding (flumazenil PET) in PD/GAD; elevated prefrontal/parietal Glu/Gln (MRS); SV2A interneuron signal in amygdala | I-down in PFC and amygdala; E-up prefrontal/parietal | MEDIUM (PET/MRS), LOW (cellular) |
| ASD | Reduced PV and SST interneuron counts; Rubenstein-Merzenich elevated E/I ratio (region/circuit-specific, not global) | I-down (PV/SST) in prefrontal, auditory, sensorimotor cortex | HIGH |
| ADHD | Catecholamine tuning of prefrontal signal-to-noise; not the classic interneuron E/I story; glutamate alterations unsettled | Not primary; direction unsettled | LOW-MEDIUM |
| OCD | Elevated caudate/striatal Glx (MRS), normalizes with SRI; secondary GABA reduction in ACC | E-up in caudate/striatum and OFC; I-down in ACC | HIGH (glutamate), LOW (GABA) |
| Tourette | 50-60 percent loss of PV fast-spiking interneurons in caudate/putamen; reduced SMA GABA+ (MRS) tracks premonitory urge | I-down in striatum and SMA | HIGH (postmortem), MEDIUM (MRS) |
| Anorexia | Single-cell risk enrichment in limbic and striatal GABAergic neurons; MRS heterogeneous | GABAergic limbic/striatal involvement; direction unsettled | MEDIUM (genetic), LOW (MRS) |
| Alcohol UD | Ethanol potentiates GABA-A acutely; chronic use downregulates GABA-A; withdrawal NMDA/GluN2B upregulation and glutamatergic hyperexcitability | Acute I-up; chronic I-down; E-up in withdrawal (cortex, hippocampus, striatum) | HIGH |
| Opioid UD | Mu-receptors on VTA GABA interneurons disinhibit dopamine; postmortem loss of DLPFC GABAergic interneuron markers | I-down in VTA and DLPFC | MEDIUM |
| Nicotine UD | nAChR desensitization on VTA GABA interneurons disinhibits dopamine; alpha7 nAChR enhances VTA glutamate | I-down in VTA, net E-up of dopamine neurons | MEDIUM (rodent) |
| Cannabis UD | CB1 on CCK+ GABAergic terminals; chronic THC alters depolarization-induced suppression of inhibition (DSI) | Candidate I-down in hippocampus, cortex | LOW-MEDIUM |

Reading: an E/I imbalance is reported in 13 of 14 disorders (ADHD being the partial exception, where catecholamine tuning rather than interneuron loss dominates). The PV-interneuron deficit with cortical disinhibition is the most reproducible MICRO finding in the whole set, anchored by HIGH-confidence postmortem evidence in schizophrenia, ASD, and Tourette, and by single-cell interneuron-module evidence in PTSD. The REGION differs by disorder and by factor: SB and neurodevelopmental disorders show cortical PV deficits (DLPFC, auditory cortex); compulsive disorders show striatal disinhibition (caudate/striatum in OCD, caudate/putamen and SMA in Tourette); substance disorders show VTA disinhibition driving reward plus withdrawal-phase cortical/hippocampal hyperexcitability. This region-dependence is why E/I cannot be read as a single scalar and is paired with a region label everywhere below.

### 2.3 Oxidative stress and mitochondrial dysfunction (GO:0006979 response to oxidative stress; mitochondrial ATP synthesis)

Oxidative/mitochondrial stress recurs as a SECONDARY axis in most disorders and a near-primary axis in a few. Its sensing value is unusually high because cytochrome-c-oxidase (CCO), the terminal mitochondrial electron-transport enzyme, is measurable in vivo by broadband near-infrared spectroscopy (fNIRS-CCO), the single cleanest wearable mitochondrial readout (Holper et al. 2019 distinguished MDD from controls and tracked state with brain CCO).

| Disorder | Specific finding | Direction | Confidence |
|---|---|---|---|
| Schizophrenia | Reduced/high-variance ACC glutathione (MRS); redox damage to PV interneurons (Do/Cabungcal model) | GSH down, ROS up (subset) | MEDIUM |
| Bipolar | Elevated lipid peroxides, 8-OHdG, protein carbonyls in mania and depression; reduced antioxidant defense; NAC-responsive | ROS up, antioxidant down | MEDIUM-HIGH |
| MDD | Elevated 8-OHdG (most consistent peripheral marker), lipid peroxides; small NAC effect | ROS up (subset) | MEDIUM |
| PTSD | Oxidative-stress component of accelerated DNAm aging / inflammaging | ROS up | MEDIUM (within inflammaging) |
| Anxiety | Not a primary axis | Not reported | LOW |
| ASD | Frye-Rossignol mitochondrial subgroup (~5-30 percent); elevated lactate/pyruvate, ROS, glutathione depletion; regression often inflammation-triggered | ROS up, mito dysfunction (subset) | MEDIUM |
| ADHD | Not a primary axis | Not primary | LOW |
| OCD | Lower glutathione, higher malondialdehyde in peripheral blood; nonspecific | ROS up (peripheral) | LOW |
| Tourette | Not a primary axis | Not reported | LOW |
| Anorexia | Metabolic rather than classical ROS; lipid/glycemic | Metabolic | (see 2.4 below) |
| Alcohol UD | CYP2E1 and acetaldehyde metabolism generate ROS; glutathione depletion, lipid peroxidation, mitochondrial damage (cortex, cerebellum); thiamine deficiency | ROS up (strong) | MEDIUM-HIGH |
| Opioid UD | Candidate microglial ROS within neuroinflammation | ROS up (candidate) | MEDIUM |
| Nicotine UD | AHRR/aryl-hydrocarbon oxidative pathway (exposure marker) | Oxidative (exposure) | HIGH (as exposure marker) |
| Cannabis UD | NAC antioxidant rationale; cannabinoids often anti-inflammatory | Weak/uncertain | LOW |

Reading: oxidative/mitochondrial stress is detectable in most disorders but is rarely a clean standalone biotype. It is strongest and most defensible in bipolar disorder (Berk/Kato neuroprogression model, NAC-responsive), alcohol use disorder (direct metabolic ROS load), and the ASD mitochondrial subgroup. In schizophrenia it concentrates on PV-cell redox vulnerability, tying 2.3 back to 2.2. The recurring intervention signal is N-acetylcysteine (glutathione precursor), which shows modest group-level benefit in SCZ, BD, MDD, and OCD, consistent with a redox-positive subgroup in each rather than a whole-disorder effect.

### 2.4 Immune / inflammatory axis (GO:0006954 inflammatory response; GO:0006956 complement activation; GO:0001774 microglial cell activation; kynurenine GO:0019441/GO:0097052)

Inflammation is the most broadly distributed transdiagnostic axis but also the one most confounded by comorbidity (obesity, smoking, depression). It appears in three mechanistically distinct forms: (a) peripheral cytokine elevation (IL-6, CRP, TNF-alpha), (b) microglial/complement-mediated synaptic remodeling in the CNS, and (c) the kynurenine shunt, in which inflammation diverts tryptophan from serotonin toward NMDA-active metabolites.

| Disorder | Specific finding | Direction | Confidence |
|---|---|---|---|
| Schizophrenia | C4A copy-number-driven synaptic over-pruning (microglia); elevated IL-6/CRP/TNF (subset ~30-40 percent); elevated kynurenic acid; childhood IL-6 predicts psychosis (MR) | Up; complement + cytokine | HIGH (C4 genetics, IL-6 MR), MEDIUM (subset) |
| Bipolar | IL-6, TNF, CRP elevated especially in mania; MHC locus genome-wide significant (Mullins 2021) | Up (state-dependent) | MEDIUM |
| MDD | CRP > 3 mg/L in ~25-30 percent; IL-6/TNF; kynurenine shunt; CSF quinolinic acid up in suicide attempters; tracks atypical/immunometabolic features | Up (subset) | HIGH (biotype exists) |
| PTSD | IL-6 (largest, most consistent), IL-1beta, TNF, CRP; inflammaging / accelerated GrimAge; microglial state shift (postmortem) | Up | HIGH (IL-6), LOW (PTSD-specificity) |
| Anxiety | CRP elevated (UK Biobank), GAD CRP d~0.38 with high heterogeneity; much attributable to comorbid depression/obesity | Up (subgroup) | LOW (no cutpoint) |
| ASD | Maternal immune activation models; microglial activation (TSPO PET subsets); IL-6, IL-1beta, TNF, IL-8 candidate panel; overlaps mito-regressive subtype | Up (subset) | MEDIUM (behavior robust, cellular variable) |
| ADHD | Modestly elevated IL-6/TNF; weak atopy/MIA association; likely nonspecific | Up (weak) | LOW |
| OCD | PANDAS/PANS post-streptococcal autoimmune subtype with anti-neuronal antibodies; MHC genes among Strom 2025 loci. CONTESTED causal model | Up (contested subgroup) | LOW (causal model disputed) |
| Tourette | Postmortem microglial activation in basal ganglia (replicable); PANDAS/PANS streptococcal subtype contested | Up (microglia), contested (PANDAS) | MEDIUM (microglia), LOW (PANDAS) |
| Anorexia | TNF, IL-6, IL-1beta elevated despite low BMI but largely STATE-dependent; IL-6 normalizes with refeeding | Up (starvation-coupled) | MEDIUM |
| Alcohol UD | HMGB1/TLR4 on microglia, NF-kB/NLRP3, IL-1beta/TNF/IL-6 in PFC and hippocampus; the most developed neuroinflammatory case of any SUD | Up (strong) | HIGH |
| Opioid UD | Morphine binds TLR4 (MD2 site), activates microglia (IL-1beta, TNF, IL-6, BDNF); postmortem neuroinflammatory module | Up | MEDIUM-HIGH |
| Nicotine UD | AHRR hypomethylation modulates inflammatory signaling (exposure marker) | Up (exposure) | HIGH (exposure) |
| Cannabis UD | TSPO/cytokine signals sparse and inconsistent; cannabinoids often anti-inflammatory; NO robust biotype | None/uncertain | LOW |

Reading: a peripheral inflammatory subgroup recurs in 12 of 14 disorders, with the strongest causal evidence being IL-6 Mendelian randomization in schizophrenia and CRP-stratified infliximab response in MDD (Raison 2013: 62 percent vs 33 percent response in the CRP > 5 mg/L subgroup). The TLR4/microglial mechanism is shared and well-developed across alcohol and opioid use disorders. The honest limit is that CRP/IL-6 elevation lacks a deployed clinical cutpoint in most disorders and is heavily confounded by metabolic comorbidity; cannabis use disorder has no defensible immune biotype.

### 2.5 Neurotransmitter families (one table per family across 14 disorders)

Each family below marks which disorders show reproducible dysregulation and the direction. Anchor GO terms: GABA receptor activity GO:0016917 and GABAergic transmission GO:0051932; glutamate receptor signaling GO:0007215 and glutamatergic transmission GO:0035249; dopamine receptor signaling GO:0007212 and dopamine secretion GO:0014046; serotonin receptor signaling GO:0007210; norepinephrine secretion GO:0048243 and adrenergic receptor signaling GO:0071875.

**GABA (GO:0051932)**

| Disorder | Direction | Confidence |
|---|---|---|
| Schizophrenia | Down (PV/GAD67 deficit, DLPFC/CA1) | HIGH |
| Bipolar | Down (reported, heterogeneous) | MEDIUM |
| MDD | Down (cortical GABA reduced) | MEDIUM |
| PTSD | Down (interneuron module, dlPFC) | MEDIUM-HIGH |
| Anxiety | Down (GABA-A binding, PD/GAD) | MEDIUM |
| ASD | Down (PV/SST interneuron loss) | HIGH |
| OCD | Down (ACC, secondary) | LOW |
| Tourette | Down (striatal PV loss, SMA GABA+) | HIGH |
| Anorexia | Implicated (GABAergic-neuron cell-type enrichment) | MEDIUM |
| Alcohol UD | Acute potentiation, chronic down | HIGH |
| Opioid UD | Down (VTA disinhibition, DLPFC markers) | MEDIUM |
| Nicotine UD | Down (VTA disinhibition) | MEDIUM |
| Cannabis UD | CB1-gated, down (DSI) | LOW-MEDIUM |

GABA dysregulation, almost always a reduction in inhibitory tone, is the single most widely shared neurotransmitter abnormality, present in 13 of 14 disorders (ADHD the exception).

**Glutamate (GO:0035249)**

| Disorder | Direction | Confidence |
|---|---|---|
| Schizophrenia | Up in ACC (treatment-resistant); NMDA hypofunction on PV | HIGH |
| Bipolar | Up (Glx across states) | MEDIUM |
| MDD | Modulated (ketamine glutamate surge) | HIGH (mechanism) |
| PTSD | Extinction-circuit (NMDA-dependent) | MEDIUM |
| Anxiety | Up (prefrontal/parietal Glu/Gln) | MEDIUM |
| ASD | Synaptopathy (SHANK1-3, mGluR) | HIGH (Mendelian) |
| ADHD | Altered frontostriatal Glx (unsettled) | MEDIUM |
| OCD | Up in caudate/striatum (CENTRAL axis) | HIGH |
| Tourette | Corticostriatal drive (altered) | MEDIUM |
| Anorexia | Heterogeneous (MRS) | LOW-MEDIUM |
| Alcohol UD | Up in withdrawal (NMDA/GluN2B) | HIGH |
| Opioid UD | NMDA plasticity (tolerance/dependence) | MEDIUM |
| Nicotine UD | alpha7-facilitated VTA glutamate | MEDIUM |
| Cannabis UD | Altered (NAC target, mixed) | LOW-MEDIUM |

Glutamate dysregulation is present in all 14. It is the CENTRAL molecular axis in OCD and a treatment-resistance marker (elevated ACC glutamate) in schizophrenia.

**Dopamine (GO:0007212)**

| Disorder | Direction | Confidence |
|---|---|---|
| Schizophrenia | Up (associative-striatal presynaptic hyperdopaminergia, CENTRAL) | HIGH |
| Bipolar | Up in mania, down in depression (state) | MEDIUM |
| MDD | Down (anhedonic/reward-deficit, ventral striatum) | MEDIUM-HIGH |
| ASD | Not core | LOW |
| ADHD | Dysregulated (CENTRAL; midbrain DA GWAS, DAT/DRD4) | HIGH (framework) |
| OCD | Tic-related subtype (D1/D2 MSN; augmentation pharmacology) | MEDIUM |
| Tourette | Up (hyperdopaminergic, CENTRAL; antipsychotic/VMAT2 anchor) | HIGH (pharmacology) |
| Anorexia | Altered D2/D3 (anxious response to reward) | MEDIUM |
| Alcohol UD | Down (striatal D2/D3 with OFC hypometabolism) | HIGH |
| Opioid UD | Down (reward hypofunction; VTA disinhibition) | HIGH |
| Nicotine UD | Mesolimbic reward (nAChR-driven phasic release) | HIGH (mechanism) |
| Cannabis UD | Blunted striatal DA (amotivational) | MEDIUM |

Dopamine is the organizing axis of the SB-factor positive symptoms (schizophrenia), the neurodevelopmental ADHD framework, the Tourette tic mechanism, and the entire substance-use factor (reward, where most SUDs show reward hypofunction/D2 reduction with chronicity). PTSD and anxiety are not centered on dopamine.

**Serotonin (GO:0007210)**

| Disorder | Direction | Confidence |
|---|---|---|
| Schizophrenia | Modulatory (5-HT2A, KYNA) | MEDIUM |
| Bipolar | Modulatory | LOW-MEDIUM |
| MDD | Dysregulated (SSRI target; candidate-gene 5-HTTLPR not replicated) | MEDIUM (mechanism HIGH, genetics LOW) |
| PTSD | SSRI-responsive subgroup (~60 percent) | MEDIUM |
| Anxiety | Dysregulated (SSRI/SNRI first-line; 5-HT1A/2A) | HIGH (pharmacology), LOW (genetics) |
| ASD | Elevated whole-blood serotonin in ~25 percent (hyperserotonemia) | MEDIUM |
| OCD | SRI-specific (only serotonergic agents work; CENTRAL pharmacology) | HIGH (pharmacology), LOW (genetics) |
| Tourette | Mostly OCD-mediated | LOW-MEDIUM |
| Anorexia | Trait-like 5-HT1A up / 5-HT2A down (persists after recovery) | MEDIUM-HIGH |
| Alcohol UD | 5-HT3 signaling (ondansetron-responder, 5-HTTLPR LL) | MEDIUM |
| Nicotine/Opioid/Cannabis UD | Not core | LOW |

Serotonin's transdiagnostic signature is pharmacological (SSRI/SRI response in MDD, anxiety, OCD, PTSD) more than genetic; candidate-gene 5-HTTLPR claims largely failed to replicate. The anorexia 5-HT pattern is notable for being trait-like and persisting after weight recovery.

**Norepinephrine (GO:0048243 / GO:0071875)**

| Disorder | Direction | Confidence |
|---|---|---|
| PTSD | Up (central NE hyperdrive; prazosin target, nightmare-dominant) | MEDIUM |
| Anxiety | Up (locus coeruleus hyperarousal; panic, startle) | MEDIUM |
| ADHD | Dysregulated (prefrontal NE; atomoxetine/guanfacine target) | HIGH (mechanism) |
| Opioid UD | Up in withdrawal (locus coeruleus surge; clonidine/lofexidine) | HIGH |
| Nicotine UD | DBH locus, withdrawal irritability (bupropion) | MEDIUM |
| Bipolar | Modulatory | LOW |
| Schizophrenia, MDD, ASD, OCD, Tourette, anorexia, alcohol/cannabis UD | Not a primary axis | LOW |

Norepinephrine is the arousal/withdrawal axis: it is central to PTSD hyperarousal, panic, ADHD prefrontal tuning, and the opioid-withdrawal locus-coeruleus surge, and otherwise peripheral.

---

## 3. Master matrix

Cells give brief direction and confidence (H/M/L). E/I cells include the region. Blank-equivalent entries marked "ns" (not a primary/reported axis).

| Disorder | BDNF | E/I (+region) | Oxidative | Immune | GABA | Glutamate | Dopamine | Serotonin | NE |
|---|---|---|---|---|---|---|---|---|---|
| Schizophrenia | low M | I-down PV, DLPFC/CA1 H | GSH-down M | C4/IL-6 H | down H | up ACC H | up striatum H | mod M | ns |
| Bipolar | low (state) M-H | E-up ACC/PFC M | ROS-up M-H | up (state) M | down M | up M | up mania M | mod L-M | mod L |
| MDD | low H | I-down PFC M | 8-OHdG up M | CRP-high H | down M | mod (ketamine) H | down (reward) M-H | dysreg M | ns |
| PTSD | extinction-low M | I-down dlPFC M-H | inflammaging M | IL-6 up H | down M-H | extinction M | ns | SSRI-subgroup M | up M |
| Anxiety | low M | I-down PFC/amygdala M; E-up parietal | ns | CRP subgroup L | down M | up prefrontal M | ns | dysreg H(pharm) | up M |
| ASD | reduced signaling L | I-down PV/SST, multi-cortical H | mito subgroup M | MIA/microglia M | down H | synaptopathy H | ns | hyperserotonemia M | ns |
| ADHD | unclear L-M | catecholamine tuning (not interneuron) L-M | ns | weak L | ns | unsettled M | dysreg H | ns | dysreg H |
| OCD | modulatory M | E-up caudate/striatum H; I-down ACC L | peripheral L | PANDAS contested L | down L | up CENTRAL H | tic-subtype M | SRI CENTRAL H(pharm) | ns |
| Tourette | developmental M | I-down striatum/SMA H | ns | microglia M; PANDAS L | down H | corticostriatal M | up CENTRAL H | OCD-mediated L-M | ns |
| Anorexia | hub/state M; Val66Met L | GABAergic limbic/striatal M | metabolic | state-dependent M | implicated M | heterogeneous L-M | D2/D3 altered M | trait 5-HT M-H | ns |
| Alcohol UD | striatal DECREASE M-H | acute I-up, chronic I-down; E-up withdrawal H | ROS strong M-H | TLR4/microglia H | acute up/chronic down H | up withdrawal H | down D2/D3 H | ns |
| Opioid UD | VTA DECREASE M | I-down VTA/DLPFC M | microglial ROS M | TLR4 M-H | down M | NMDA plasticity M | down H | ns | up withdrawal H |
| Nicotine UD | ns L | I-down VTA, net E-up H | oxidative (exposure) H | AHRR (exposure) H | down M | alpha7 VTA M | reward H | ns | DBH M |
| Cannabis UD | ns L | CB1 I-down hippocampus/cortex L-M | weak L | none L | down L-M | altered L-M | blunted M | ns | ns |

---

## 4. The most reproducible transdiagnostic molecular biotypes (ranked)

These rank by cross-disorder breadth multiplied by replication confidence. Each lists the disorders that load, the dominant genomic factor(s), and whether a wearable can measure it.

**Biotype 1: PV-interneuron / cortical-disinhibition E/I biotype (most reproducible).**
The reduction of parvalbumin fast-spiking interneuron function with consequent cortical (or striatal) disinhibition and degraded gamma synchrony is the single most replicated MICRO finding across the set. Loads strongly in schizophrenia, ASD, Tourette (HIGH postmortem in all three), PTSD (interneuron module), and more weakly in MDD, anxiety, bipolar, and the substance disorders (VTA variant). Genomic factors: SB (excitatory-neuron-enriched, but the lesion is on the interneurons regulating them) and neurodevelopmental, with internalizing contributing the PTSD signal. **Wearable-measurable: YES.** EEG aperiodic 1/f slope (flatter = excitatory bias) is the leading noninvasive E/I proxy; 40-Hz auditory steady-state response (ASSR) and resting gamma index PV/GABA microcircuit integrity and run on consumer-grade EEG. Confidence HIGH for the biotype, MEDIUM for the 1/f proxy (mixed replication, Donoghue 2025).

**Biotype 2: BDNF/TrkB plasticity-deficit biotype.**
Low or dysfunctional BDNF/TrkB signaling that predicts poorer response to all iPlasticity-inducing treatments (SSRIs, ketamine, psychedelics, ECT). Loads in MDD (HIGH mechanism), bipolar depression, chronic schizophrenia, PTSD and anxiety (extinction-gating flavor), anorexia (hub/state), and inverts in alcohol/opioid use disorders (drug-specific striatal/VTA DECREASE that promotes intake). Genomic factors: spans internalizing, SB, compulsive/eating, and substance-use. **Wearable-measurable: PARTIALLY.** Peripheral (capillary/finger-prick) serum BDNF tracks state and recovery; BDNF Val66Met genotype from a cheek swab stratifies responders. Confidence HIGH for the mechanism, MEDIUM for peripheral BDNF as a faithful CNS readout.

**Biotype 3: Peripheral inflammatory / CRP-high biotype.**
A cytokine-elevated subgroup (CRP > 3 mg/L, IL-6, TNF) recurs in MDD, schizophrenia, PTSD, bipolar, ASD, anorexia (state), and the alcohol/opioid TLR4-microglial disorders. Genomic factors: all except (cannabis, where it is absent). Strongest causal anchors are IL-6 MR in schizophrenia and CRP-stratified infliximab response in MDD. **Wearable-measurable: YES (peripheral).** CRP and IL-6 are standard finger-prick/point-of-care assays; this is the most clinically deployable peripheral molecular biotype. Confidence HIGH that the subgroup exists, LOW-MEDIUM that a single cutpoint generalizes across disorders.

**Biotype 4: Oxidative-stress / mitochondrial biotype.**
A redox-positive subgroup with glutathione depletion, elevated 8-OHdG and lipid peroxidation, and mitochondrial dysfunction. Loads most strongly in bipolar (neuroprogression, NAC-responsive), alcohol use disorder (metabolic ROS), the ASD mitochondrial subgroup, and the PV-redox subset of schizophrenia. Genomic factors: SB, substance-use, neurodevelopmental. **Wearable-measurable: YES (the platform anchor).** Broadband fNIRS-CCO (cytochrome-c-oxidase) is the cleanest in vivo wearable mitochondrial readout (Holper 2019); capillary 8-OHdG and lactate add specificity; HRV is a secondary autonomic proxy. Confidence MEDIUM for the biotype, MEDIUM-HIGH for CCO as a state-tracking signal.

**Biotype 5: Dopaminergic reward / salience biotype.**
Dopamine dysregulation organizing into two poles: hyperdopaminergic salience (schizophrenia associative striatum, Tourette tics, bipolar mania) versus reward-deficit/hypodopaminergic (MDD anhedonia, all SUDs with chronicity, cannabis amotivational). Genomic factors: SB, neurodevelopmental, compulsive (tic-OCD), and the entire substance-use factor. **Wearable-measurable: NO directly.** Striatal dopamine requires PET; wearable proxies are indirect (EEG reward positivity / RewP for the reward-deficit pole, pupillometry). Confidence HIGH for the axis, but the lack of a noninvasive molecular readout is a real limit.

**Biotype 6: Glutamatergic / NMDA biotype.**
Elevated or dysregulated glutamatergic tone, most defensibly elevated ACC glutamate in treatment-resistant schizophrenia and elevated caudate Glx in OCD, plus the withdrawal hyperexcitability of alcohol use disorder. Genomic factors: SB, compulsive, substance-use. **Wearable-measurable: NO directly** (requires MRS); EEG mismatch negativity (NMDA-dependent) is a partial functional proxy. Confidence HIGH for the axis in SCZ/OCD.

**Biotype 7: Microglial / complement synaptic-remodeling biotype (CNS arm of inflammation).**
Distinct from peripheral CRP, this is the central microglial/complement mechanism: C4-mediated over-pruning in schizophrenia, TLR4-microglial activation in alcohol and opioid use disorders, and microglial activation in Tourette basal ganglia and ASD subsets. Genomic factors: SB, substance-use, neurodevelopmental. **Wearable-measurable: NO** (TSPO PET only, and TSPO is not robustly replicated). Confidence MEDIUM (mechanism), with the sensing limit flagged.

**Biotype 8: Metabo-psychiatric biotype (disorder-concentrated but conceptually transdiagnostic).**
Anorexia is the prototype, with negative genetic correlations to insulin resistance and fasting glucose that exceed the BMI signal (Watson 2019), but the metabolic/pharmacogenetic layer also defines the substance-use factor (ALDH2/ADH1B alcohol-metabolism aversion, CYP2A6 nicotine metabolism). Genomic factors: compulsive/eating and substance-use. **Wearable-measurable: YES (peripheral).** Continuous glucose monitoring, capillary insulin/glucose, and nicotine-metabolite ratio are deployable; this overlaps the foundation's fNIRS-CGM sensing interest. Confidence MEDIUM-HIGH for anorexia glycemics, HIGH for the SUD pharmacogenetic markers.

**The wearable-measurable subset.** Of the eight, four have a defensible noninvasive molecular or electrophysiological readout today: E/I via EEG aperiodic slope and 40-Hz ASSR (Biotype 1), oxidative/mitochondrial via fNIRS-CCO (Biotype 4), inflammation via peripheral CRP/IL-6 (Biotype 3), and BDNF via finger-prick serum BDNF plus Val66Met genotype (Biotype 2). The metabo-psychiatric markers (Biotype 8) add CGM and pharmacogenetics. This converges on the four-channel molecular biotype signature proposed in the molecular-cellular review: capillary BDNF + EEG aperiodic slope + fNIRS-CCO + peripheral CRP, with cheek-swab Val66Met and CGM as add-ons. Dopaminergic, glutamatergic, and microglial biotypes (5, 6, 7) currently require PET or MRS and are the clearest sensing gaps.

---

## 5. Honest limits

- **Subgroup, not whole-disorder.** Almost every axis above (inflammation, oxidative stress, even BDNF) defines a SUBSET of patients within each disorder, not the whole diagnosis. The CRP-high subgroup is ~25-30 percent of MDD; the mitochondrial subgroup is ~5-30 percent of ASD; the inflammatory subset of schizophrenia is ~30-40 percent. Treating any axis as a per-disorder constant would be wrong.

- **Peripheral-to-central inference is fragile.** Serum BDNF, CRP, and 8-OHdG are peripheral proxies for central processes. The correlation between peripheral and brain BDNF is imperfect, and peripheral inflammation is heavily confounded by obesity and smoking. fNIRS-CCO measures cortical surface mitochondria, not deep structures.

- **State versus trait.** Several axes flip or normalize with clinical state: BDNF and inflammatory markers in bipolar and anorexia recover in euthymia/refeeding; alcohol E/I inverts between acute use and withdrawal. A single-timepoint reading can mislead. These are trajectory signals, not static signatures.

- **Direction reversals across factors.** The substance-use disorders invert the BDNF logic (striatal/VTA DECREASE promotes intake), so a "low BDNF = treat with plastogen" rule does not transfer cleanly from MDD to AUD. Bipolar adds a manic-switch hazard that contraindicates unopposed serotonergic plastogens.

- **Flagged replication failures.** The anorexia BDNF Val66Met candidate-gene association failed meta-analytic replication. The PANDAS/PANS autoimmune model in OCD and Tourette is clinically defined but mechanistically contested, with antibody assays that do not predict treatment response. The ADHD theta-beta ratio failed rigorous replication. Frontal alpha asymmetry in MDD is a small, inconsistent effect. TSPO microglial PET is not robustly replicated. The EEG aperiodic 1/f slope, although the leading E/I proxy, has mixed replication and the strongest aperiodic signal sits in ASD rather than across the board.

- **GWAS does not yet stratify clinically.** Polygenic risk scores explain only 1 to 10 percent of liability and cannot define a biotype alone. The genomic factors organize biology at the population level; they weight priors over biotype membership but do not assign individuals.

- **GO harmonization is partial.** Several GO IDs carried from the disease docs are marked "approx, needs curation" (gamma-oscillation, acid-sensing, histamine-secretion, FAAH-catabolic, several mitochondrial subterms) and require ontology-team verification before grant or clinical use.

---

## References (organizing and axis anchors)

1. Grotzinger AD, Werme J, Peyrot WJ, ... Smoller JW. Mapping the genetic landscape across 14 psychiatric disorders. Nature. 2025. doi:10.1038/s41586-025-09820-3
2. Moliner R, Girych M, Brunello CA, et al. Psychedelics promote plasticity by directly binding to BDNF receptor TrkB. Nat Neurosci. 2023;26:1032-1041. doi:10.1038/s41593-023-01316-5
3. Casarotto PC, Umemori J, Castren E. BDNF receptor TrkB as the mediator of the antidepressant drug action. Front Mol Neurosci. 2022;15:1032224. doi:10.3389/fnmol.2022.1032224
4. Castren E, Antila H. Neuronal plasticity and neurotrophic factors in drug responses. Mol Psychiatry. 2017;22:1085-1095.
5. Sekar A, Bialas AR, de Rivera H, et al. Schizophrenia risk from complex variation of complement component 4. Nature. 2016;530:177-183. doi:10.1038/nature16549
6. Raison CL, et al. A randomized controlled trial of infliximab for treatment-resistant depression. JAMA Psychiatry. 2013;70(1):31-41.
7. Crews FT, et al. The role of neuroimmune signaling in alcoholism. Psychopharmacology. 2017. doi:10.1007/s00213-017-4560-6
8. Watson HJ, et al. GWAS identifies eight risk loci and implicates metabo-psychiatric origins for anorexia nervosa. Nat Genet. 2019;51:1207-1214. doi:10.1038/s41588-019-0439-2
9. Holper L, et al. Brain cytochrome-c-oxidase as a marker of mitochondrial function: a pilot study in major depression using NIRS. Depress Anxiety. 2019;36:766-779.
10. Donoghue T. A Systematic Review of Aperiodic Neural Activity in Clinical Investigations. Eur J Neurosci. 2025. doi:10.1111/ejn.70255
11. Per-disorder MICRO sections: schizophrenia.md, bipolar.md, mdd.md, ptsd.md, anxiety.md, asd.md, adhd.md, ocd.md, tourette.md, anorexia.md, sud-alcohol.md, sud-opioid.md, sud-nicotine.md, sud-cannabis.md (this folder), and molecular-cellular-biotypes.md (parent review). Individual GWAS, postmortem, and PET citations are given in those source docs.

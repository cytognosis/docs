# Transdiagnostic Connectomic Synthesis: A Mental Health Coordinate Map for Adaptive Spectroscopy Sensing

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: researchers, stakeholders
> **Tags**: `literature-synthesis`, `disease-biotypes`, `transdiagnostic`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)

Prepared for: Cytognosis Foundation + Hervé Marie-Nelly NSF X-Labs Phase 0 proposal
Date: 25 May 2026
Scope: Synthesis across five per-disorder biotype reviews (depression, anxiety, psychosis, PTSD, substance use disorders) compiled for this proposal. The goal is to identify shared and disjoint connectomic patterns that justify a coarse-to-fine "zoom" sensing strategy for a wearable optical headset.

---

## 1. Framing: from disorder labels to a connectomic coordinate system

### 1.1 The Drysdale insight, recontextualized

Drysdale and colleagues (2017) argued that within Major Depressive Disorder, four resting-state connectivity biotypes predicted differential response to transcranial magnetic stimulation, with biotype-stratified response rates differing by a factor of three (roughly 80% vs 25% for the best and worst responding biotypes on dorsomedial prefrontal cortex rTMS) (see biotypes-depression.md, Section 1.1). Although Dinga et al. (2019) showed that the specific four-cluster solution fails to survive proper nested cross-validation (see biotypes-depression.md, Section 1.2), the deeper claim remains intact across the literature: within any DSM category, circuit-level subtypes predict treatment response better than the diagnostic label itself. The Williams 2024 six-biotype scaffold across depression and anxiety (see biotypes-depression.md, Section 1.3; biotypes-anxiety.md, Section 1.3) replicates internally and shows that connectivity profiles, not diagnosis, separate venlafaxine responders from behavioral-therapy responders. B-SNIP psychosis biotypes (see biotypes-psychosis.md, Section 1.1) cross DSM lines between schizophrenia, schizoaffective disorder, and psychotic bipolar I, with first-degree relatives showing intermediate profiles consistent with a heritable bio-factor structure that is not captured by categorical diagnosis. The Lanius dissociative subtype of PTSD (see biotypes-ptsd.md, Section 1.1), the only PTSD subtype formally recognized in DSM-5, is the cleanest single example of a brain-derived biotype that became clinical nosology.

### 1.2 The transdiagnostic extension

The five per-disorder reviews converge on a small number of circuits that recur across disorders, often with the same direction of effect (default mode hyperconnectivity, salience hyperreactivity, prefrontal control hypofunction). They also identify a smaller set of patterns that genuinely distinguish disorders (hippocampal CA1 hyperactivity in psychosis vs hippocampal volume loss in PTSD and depression; insular craving signatures in addiction; BNST sustained vigilance in GAD; dissociative overmodulation in a PTSD subtype). Together these patterns suggest a low-dimensional latent space, a "mental health coordinate," in which biotypes from different DSM categories occupy partially overlapping and partially disjoint regions. The Williams lab framing (see biotypes-anxiety.md, Section 1.3) treats six standardized circuits as the basis for this coordinate; the Cytognosis platform extends the same logic to addiction, psychosis, and trauma.

### 1.3 Why this matters for a wearable sensing platform

A spectroscopy headset cannot scan every voxel at every moment. It must allocate optode density and sampling cadence to the regions most likely to carry information for a given user. Knowing the person's diagnostic profile plus their current state (medicated, abstinent, in early prodrome, in protracted withdrawal, in dissociative episode) constrains the prior over which biotype they are likely to occupy, which in turn constrains which cortical and shallow-subcortical regions are most informative to monitor. The coarse-to-fine zoom is conceptually simple: start with the user's biotype prior, allocate sensor density to the anchor regions of that biotype, and refine the biotype estimate longitudinally as the headset accumulates within-person data that no cross-sectional MRI study can match. The remainder of this document inventories shared and disjoint circuits across the five disorders, names a 6 to 8 region anchor list that maximizes biotype coverage, and identifies the latent axes that organize the coordinate space.

---

## 2. Cross-disorder shared circuits and biotypes

### 2.1 Default Mode Network: rumination, self-referential thought, and symptom maintenance

The DMN (medial prefrontal cortex, posterior cingulate cortex, precuneus, angular gyrus, anterior hippocampus) recurs across all five disorders with broadly convergent direction of effect, although the precise sub-network signature differs.

In depression, Sheline's "dorsal nexus" finding (see biotypes-depression.md, Section 1.6) showed elevated DMN connectivity and DMN hyperactivity during self-referential and negative-affect tasks. The Williams DC+SC+AC+ biotype (DMN, salience, and attention hyperconnected; see biotypes-depression.md, Section 1.3) shows slowed emotional and attentional reactions and responds preferentially to behavioral therapy.

In anxiety, GAD shows DMN-salience cross-talk with reduced DMN-executive separation (see biotypes-anxiety.md, Section 1.4). The worry-prone phenotype shows increased coupling between DMN and threat-monitoring nodes.

In psychosis, DMN hyperconnectivity is one of the most reproducible resting-state findings in schizophrenia, present in chronic SCZ, first-episode psychosis, clinical high-risk youth, and unaffected first-degree relatives, making it an endophenotype rather than a state marker (see biotypes-psychosis.md, Section 1.6). Pre-treatment DMN hyperconnectivity predicts antipsychotic response in medication-naive first-episode patients.

In PTSD, DMN within-network connectivity is reduced (posterior cingulate to medial PFC), with increased coupling of DMN nodes to the salience network (see biotypes-ptsd.md, Section 1.6). Within-DMN connectivity correlates inversely with symptom severity, the opposite-direction signal from depression and psychosis.

In addiction, DMN-salience anti-correlation failures predict craving and relapse risk (see biotypes-addiction.md, Section 1.5); the transdiagnostic craving CPM (Garrison, Sinha, Potenza) identified a network spanning DMN, salience, and frontoparietal nodes that generalized across alcohol, cocaine, and food craving (see biotypes-addiction.md, Section 1.7).

Shared anchor regions: posterior cingulate cortex / precuneus and medial prefrontal cortex. Effect sizes vary from small (Cohen's d around 0.2 for individual links) to moderate at the network level. Replication is high.

### 2.2 Salience Network: anterior insula, dACC, interoceptive vigilance and switching

The salience network (anterior insula, dorsal anterior cingulate cortex) acts as the Menon "triple network" switch between DMN and executive control. Hyperconnectivity within and from salience to limbic regions is the most consistent transdiagnostic functional signature.

In depression it associates with anxious-ruminative distress (see biotypes-depression.md, Section 1.6). In anxiety it is the core "anxious-arousal" signature, with sustained anterior insula and dorsal ACC engagement during uncertainty in the BNST-driven worry biotype (see biotypes-anxiety.md, Sections 1.2 and 1.4). In psychosis, salience hyperreactivity is the proposed mechanism for aberrant attribution to neutral stimuli (Kapur), and the cingulo-opercular system links to the cortico-striatal-thalamic central pathway described by Peters, Dunlop, and Downar (see biotypes-psychosis.md, Section 1.6). In PTSD, anterior insula hyperreactivity to threat is the classic profile; the Etkin VAN-deficit biotype shows reduced salience connectivity and predicts poor exposure therapy response (see biotypes-ptsd.md, Section 1.4). In addiction, insula activation tracks cue-induced craving across alcohol, cocaine, nicotine, and opioids; the Naqvi insula-lesion finding (smokers with insular damage quit easily) is among the strongest single causal claims in addiction neuroscience (see biotypes-addiction.md, Section 1.5).

Shared anchor regions: anterior insula, dorsal anterior cingulate cortex. Effect sizes for salience-amygdala coupling in anxiety reach Cohen's d around 0.5; the insula craving signature in addiction reproduces across substance classes.

### 2.3 Central Executive / Cognitive Control: dlPFC, posterior parietal

Cognitive control hypofunction (reduced dlPFC and dACC engagement during Go/NoGo, Stop Signal, working memory) recurs across disorders. In depression, the Williams CA+ cognitive overactivity biotype responds preferentially to venlafaxine (see biotypes-depression.md, Section 1.3); the Goldstein-Piekarski cognitive-control mapping (see biotypes-depression.md, Section 1.4) plus the B-SMART-fMRI trial (cognitive-biotype-positive patients respond to left-dlPFC TMS) supports this circuit as a treatment-stratification axis. In anxiety, lateral PFC hypoactivation modulates outcome prediction across SSRI and CBT (see biotypes-anxiety.md, Section 8.1); right DLPFC hyperactivation underlies the inhibitory rTMS biotype for GAD. In psychosis, prefrontal thinning and frontoparietal hypoconnectivity are core ENIGMA findings (see biotypes-psychosis.md, Section 1.4). In PTSD, dorsolateral and dorsomedial PFC engagement predicts prolonged exposure response (see biotypes-ptsd.md, Section 9.3). In addiction, dlPFC and ACC hypofunction during inhibitory control is the third pillar of the Goldstein iRISA model and the Volkow-Koob preoccupation stage (see biotypes-addiction.md, Sections 1.1 and 1.2).

Shared anchor region: dorsolateral prefrontal cortex (Brodmann 46/9). This is the single most-targeted region across noninvasive neuromodulation trials in psychiatry.

### 2.4 Threat / fear circuit: amygdala, vmPFC, BNST

The LeDoux scaffold (lateral amygdala learns threat; central amygdala drives autonomic output; vmPFC regulates extinction) is the most thoroughly characterized circuit in psychiatric neuroscience (see biotypes-anxiety.md, Section 1.1).

Amygdala hyperreactivity with vmPFC hypoactivation recurs in depression (Drysdale biotypes 1 and 4; see biotypes-depression.md, Section 1.1), in anxiety (the central convergent biotype across GAD, SAD, panic), in canonical PTSD (Shin and Liberzon; see biotypes-ptsd.md, Section 1.5), and in early-stage addiction during cue-reactivity tasks. The dissociative PTSD subtype inverts the pattern (see biotypes-ptsd.md, Section 1.1): mPFC and dorsomedial PFC overmodulate the limbic system, producing hypoarousal and reduced amygdala activation.

The BNST contribution (sustained, temporally diffuse threat; see biotypes-anxiety.md, Section 1.2) is most prominent in GAD and in the addiction "stress-driven, negative-affect" biotype (Koob extended amygdala; see biotypes-addiction.md, Sections 1.2 and 9). The Shackman-Fox formulation distinguishes central amygdala (phasic) from BNST (sustained) contributions.

Shared anchor region: ventromedial PFC as the cortical effector. Amygdala and BNST are too deep for current optical methods; vmPFC and subgenual/pregenual ACC act as accessible proxies.

### 2.5 Reward circuit: ventral striatum, OFC, vmPFC

Reward circuit dysfunction takes the form of either hyperreactivity to disorder-specific cues or hyporeactivity to general reward.

In depression, Pizzagalli's anhedonic biotype is the most coherent reward signature in psychiatry (see biotypes-depression.md, Section 1.5). The EMBARC trial showed that pretreatment ventral striatum reward activity moderates sertraline-over-placebo response, and Felger's work linked elevated CRP and IL-6 to reduced ventral striatum-vmPFC connectivity (see biotypes-depression.md, Section 3.1), bridging inflammation and reward.

In anxiety, reward dysfunction is less prominent except in comorbid depression. In psychosis, ventral striatum and associative-striatum dopamine elevations underlie the Howes-McCutcheon hyperdopaminergic Type A biotype (see biotypes-psychosis.md, Section 1.9). The mechanism via the Grace hippocampus-subiculum-accumbens-pallidum-VTA loop (see biotypes-psychosis.md, Section 1.7) provides the most replicated circuit-level model of positive symptoms.

In PTSD, the Stevens AURORA "low-reward / high-threat" cluster and the PTSD-MDD overlap (anhedonic dysphoria) point to ventral striatal hyporeactivity in a substantial subgroup (see biotypes-ptsd.md, Sections 1.2 and 10).

In addiction, the dual-phenotype split (incentive sensitization vs reward deficiency; see biotypes-addiction.md, Section 1.4) recapitulates the same dimension: ventral striatum hyperreactive to drug cues and hyporeactive to non-drug rewards. D2/D3 PET reductions across cocaine, methamphetamine, alcohol, and heroin replicate strongly (Volkow; see biotypes-addiction.md, Section 1.1).

Shared anchor regions: ventral striatum (subcortical, depth-limited), orbitofrontal cortex, ventromedial PFC. The cortical proxies are accessible.

### 2.6 Subgenual ACC and the depression-anxiety-PTSD overlap

The subgenual anterior cingulate cortex (Brodmann 25) is the single most-validated treatment target in depression: Mayberg's DBS work in the subcallosal white matter convergence point produces sustained response in roughly 81.8% of TRD patients at one year with appropriate tractography-guided targeting (see biotypes-depression.md, Section 1.7). The Fox-Cash sgACC anticorrelation finding (left-dlPFC TMS sites whose resting-state activity is most anticorrelated with sgACC produce the strongest antidepressant effects) is now the basis for FDA-cleared personalized TMS targeting (SAINT). In anxiety, sgACC contributes to the central amygdala-prefrontal regulation circuit (see biotypes-anxiety.md, Section 1.1). In PTSD, sgACC volume predicts CBT response (Bryant et al.; see biotypes-ptsd.md, Section 9.3), and sgACC connectivity with amygdala predicts ketamine response in TRD with comorbid PTSD features. In addiction, sgACC is implicated in the stress-driven biotype, particularly in protracted withdrawal.

Shared anchor region: subgenual ACC (deep, midline, optically challenging but functionally indexable via dlPFC anticorrelation).

### 2.7 Hippocampus and the depression-PTSD-psychosis overlap

The hippocampus features in all five disorders but with strikingly different mechanisms.

In depression, ENIGMA-MDD reports smaller hippocampal volume in recurrent and early-onset cases with Cohen's d around -0.14 (see biotypes-depression.md, Section 1.8). Hippocampal subfield volumes (CA1, CA3, GCL) predict ECT response with high accuracy in one study (r = 0.81; see biotypes-depression.md, Section 8.4).

In PTSD, smaller hippocampal volume is a robust ENIGMA-PGC finding (d = -0.17, p = 0.00054 across 1,868 subjects; see biotypes-ptsd.md, Section 1.8). The Gilbertson twin study shows that smaller hippocampal volume is at least partly a predisposing trait rather than solely a consequence of trauma.

In psychosis, the direction inverts. Anterior hippocampal hyperactivity in CA1 is one of the most robust circuit findings in schizophrenia (Schobel, Heckers, Small; see biotypes-psychosis.md, Section 1.7). Increased CA1 cerebral blood volume is detectable in prodromal high-risk individuals who later convert. The mechanism (parvalbumin interneuron loss disinhibits pyramidal cells, driving VTA via subiculum-accumbens-pallidum) is the most replicated upstream mechanism for positive symptoms.

In anxiety, the hippocampal contextual-fear axis differentiates PTSD-spectrum from cue-driven anxiety (see biotypes-anxiety.md, Section 1.5).

In addiction, hippocampal volume reductions occur in alcohol and methamphetamine dependence; cannabis effects are less consistent (see biotypes-addiction.md, Section 1.8).

Anchor region: anterior hippocampus. Currently inaccessible to optical methods; the headset relies on indirect indexing via medial parietal DMN nodes and medial PFC.

### 2.8 Striatal-prefrontal loops in addiction, psychosis, and OCD

Cortico-striato-thalamo-cortical (CSTC) loops link OFC and ACC through the head of caudate and ventral striatum to mediodorsal thalamus and back. In OCD this is the dominant biotype family (see biotypes-anxiety.md, Section 1.8), with symptom-dimension splits: medial OFC for symmetry / contamination, lateral OFC for harm / checking. In psychosis, the associative striatum (dorsal caudate, anterior putamen) shows elevated dopamine synthesis in the hyperdopaminergic Type A subtype; thalamocortical hyperconnectivity to sensorimotor cortex with hypoconnectivity to prefrontal cortex is robust across cohorts (Anticevic, Woodward; see biotypes-psychosis.md, Section 1.8). In addiction, the Belin-Everitt ventral-to-dorsal striatal devolution (see biotypes-addiction.md, Section 1.3) captures the impulsivity-to-compulsivity transition, and the dorsolateral striatum becomes the habit substrate.

Shared anchor regions: OFC, dACC, associative striatum (dorsal caudate, anterior putamen; depth-limited).

### 2.9 Cerebellar contributions

Andreasen's cognitive dysmetria framework places cortico-thalamo-cerebellar disconnection at the center of schizophrenia phenomenology (see biotypes-psychosis.md, Section 1.10). Cerebellar volume reductions, weaker cerebellocortical connectivity, and aberrant motor and association connectivity replicate across cohorts. ENIGMA-PGC PTSD has reported smaller total and posterior-lobule cerebellar volumes (see biotypes-ptsd.md, Section 1.9). In alcohol use disorder, cerebellar gray-matter loss is among the most consistent structural findings (see biotypes-addiction.md, Section 1.9). The cerebellum is a tier-2 target for the proposal: feasible with caudal optode placement but not in the first-priority set.

---

## 3. Disjoint and disorder-specific signatures

The convergence above must not erase the patterns that genuinely separate disorders, several of which are large in effect size and clinically important.

### 3.1 Hippocampal hyperactivity (CA1) in psychosis vs hippocampal volume loss in PTSD and depression

The hippocampal inversion is the single largest disorder-separating signal. Psychosis shows anterior CA1 hyperactivity (functional) and surface deformations (structural), with the Grace model proposing a direct mechanistic link between CA1 disinhibition and VTA dopamine drive (see biotypes-psychosis.md, Section 1.7). PTSD and depression show volume reduction with deficits in fear-extinction recall and contextual learning, with the Gilbertson twin study suggesting a vulnerability rather than purely a sequela in PTSD (see biotypes-ptsd.md, Section 1.8; biotypes-depression.md, Section 1.8). A coordinate system that places hippocampal function on a single axis would mislabel one of these populations. The headset needs to read the direction of hippocampal engagement, not just its presence.

### 3.2 Sensorimotor and auditory cortex hyperresponsiveness in psychosis (B-SNIP Biotype 2)

B-SNIP Biotype 2 (see biotypes-psychosis.md, Section 1.1) is defined by overactive sensory neural responses and poor P50 gating, with intrinsic cortical activity elevated. The thalamus-sensorimotor hyperconnectivity finding (Anticevic; see biotypes-psychosis.md, Section 1.8) is transdiagnostic across psychotic disorders but does not appear in depression, anxiety, PTSD, or addiction in this direction. Primary auditory cortex (Heschl's gyrus, planum temporale) and adjacent sensorimotor cortex are the anchor regions, and they are uniquely psychosis-distinguishing among the disorders considered here. They are also among the most optically accessible regions in the brain.

### 3.3 BNST sustained vigilance in GAD

The Shackman-Fox extended-amygdala model places BNST at the center of sustained, temporally diffuse threat processing, distinguishable from central amygdala phasic responses (see biotypes-anxiety.md, Section 1.2). The worry-prone GAD phenotype maps preferentially onto BNST-driven sustained vigilance, distinguished from panic disorder (more phasic amygdala, more respiratory-CO2 sensitivity) and from PTSD (intermittent threat reactivity rather than tonic). BNST is millimeter-scale and optically inaccessible; its cortical correlate (sustained anterior insula and dorsal ACC engagement during uncertainty) is partly reachable.

### 3.4 Dissociative amygdala overmodulation in PTSD (Lanius)

The dissociative PTSD subtype (see biotypes-ptsd.md, Section 1.1) is the cleanest example of a disorder-specific circuit inversion: mPFC, dorsomedial PFC, and medial frontal regions overmodulate amygdala and limbic system, producing emotional disengagement and reduced (rather than elevated) amygdala activation, with increased connectivity to precuneus, posterior cingulate, and posterior insula. Dynamic causal modeling confirms top-down inhibitory drive (the inverse of classic PTSD bottom-up amygdala drive). 12-30% of PTSD patients show this signature, enriched in women and survivors of early childhood abuse. No other disorder in this synthesis shows this specific overmodulation pattern.

### 3.5 Insula craving signature in addiction (Naqvi)

The Naqvi insula-lesion finding (smokers with insular damage quit easily and without persistent urges; see biotypes-addiction.md, Section 1.5) plus convergent fMRI cue-reactivity data establishes insula as an addiction-specific craving substrate. Although the insula features in anxiety (interoceptive subtype) and in PTSD (salience reactivity), the cue-driven craving phenotype is addiction-specific. The BrainsWay H4 deep TMS coil targeting bilateral insula achieved FDA clearance for smoking cessation based on a 28.4% vs 11.7% sham continuous quit rate.

### 3.6 Cortico-striato-thalamo-cortical loops in OCD

OCD is the cleanest single-circuit disorder in this synthesis. The CSTC model anchors on OFC, dorsal ACC, head of caudate, and mediodorsal thalamus (see biotypes-anxiety.md, Section 1.8). Frontal-striatal functional connectivity differentiates "checker" from "washer" symptom subtypes. The lateral OFC (harm avoidance / checking) versus medial OFC (symmetry / contamination) distinction is the most reproducible symptom-dimension split. No other disorder in this synthesis shows this specific CSTC dominance, although addiction's compulsivity biotype borrows machinery from this loop family.

### 3.7 Other disorder-specific signals worth flagging

In addiction: the gut-immune-brain axis (Leclercq leaky-gut subtype in AUD; methamphetamine TLR4 microglial activation; see biotypes-addiction.md, Sections 3 and 5) is more developed than in the other disorders. In psychosis: complement component C4A-mediated synaptic pruning (Sekar; see biotypes-psychosis.md, Section 3.2), the most mechanistic genetic-to-circuit link in psychiatry. In PTSD: the FKBP5 methylation gene-by-environment-by-epigenome cascade (Klengel, Binder; see biotypes-ptsd.md, Section 3.1), the cleanest stress-trauma-epigenome mechanism. In panic disorder: the respiratory subtype with CO2-induction sensitivity around 93% (vs 43% for non-respiratory panic; see biotypes-anxiety.md, Section 4.1), one of the strongest single laboratory-induced subtype validations in psychiatry.

---

## 4. The mental health coordinate map

### 4.1 Latent axes

Across the five disorders, the recurring circuits and biotypes collapse onto roughly five to six latent axes. These are not orthogonal; they correlate at the level of underlying neurobiology. They are the axes a wearable coordinate system should attempt to track per user:

1. Negative affect / threat axis (amygdala-vmPFC-ACC; central to anxiety, classic PTSD, depression with anxious features, addiction stress-driven biotype). Effect direction is hyperreactive in most disorders, inverted in the Lanius PTSD dissociative subtype.

2. Reward / anhedonia axis (ventral striatum, OFC, vmPFC; central to depression anhedonic biotype, addiction reward-deficiency biotype, PTSD-MDD overlap biotype, psychosis Type A hyperdopaminergic biotype, schizophrenia negative symptoms). Direction differs by disorder (hyporeactive in anhedonic depression, hyperreactive to drug cues in addiction, hyperdopaminergic in associative striatum in psychosis).

3. Cognitive control axis (dlPFC, dACC, posterior parietal; central to depression cognitive-control biotype, anxiety treatment-response stratification, psychosis cortical thinning, PTSD treatment response, addiction iRISA).

4. Salience / interoception axis (anterior insula, dACC, mid-insula; central to anxiety arousal biotype, panic interoceptive biotype, addiction craving biotype, PTSD salience signatures, psychosis aberrant salience).

5. Attention / vigilance axis (dorsal attention network, ventral attention network; the Williams attention-circuit dimension, the Etkin VAN-deficit PTSD biotype, the BNST-driven sustained vigilance biotype in GAD).

6. Sensory gating axis (primary auditory cortex, sensorimotor cortex, thalamocortical sensorimotor coupling; B-SNIP Biotype 2 in psychosis, sensorimotor thalamic hyperconnectivity transdiagnostic in psychotic disorders). This axis is partially separable from the others and is the most psychosis-distinguishing.

The first four axes correspond roughly to the Williams 2024 six-biotype scaffold projected onto its principal dimensions (default-mode and attention as related, negative-affect as a threat dimension, salience and positive-affect as separable). The fifth and sixth extend the scaffold to capture vigilance and sensory dimensions that the Williams depression-and-anxiety taxonomy under-samples.

### 4.2 RDoC and HiTOP alignment

The NIMH Research Domain Criteria framework (see biotypes-depression.md, Section 7.2) organizes psychiatry around negative valence, positive valence, cognitive systems, social processes, arousal-regulatory, and sensorimotor domains. The latent axes above map closely (negative affect onto negative valence, reward onto positive valence, cognitive control onto cognitive systems, attention-vigilance onto arousal-regulatory, sensory gating onto sensorimotor). RDoC has been a useful research scaffold but has not yet produced clinical biotypes by itself.

The HiTOP framework (Hierarchical Taxonomy of Psychopathology) places symptoms into internalizing, externalizing, thought disorder, and detachment spectra. The coordinate axes above cut across HiTOP spectra: negative-affect biotypes appear in internalizing (depression, anxiety, PTSD) and externalizing (addiction stress-driven); reward biotypes appear in internalizing (anhedonic depression) and externalizing (addiction); sensory gating is largely thought-disorder localized.

### 4.3 Causal modeling: connectomic mediator between genome and phenome

The coordinate map serves a second function beyond zoom targeting: it provides a connectomic mediator layer for causal inference between genomic priors (purely inherited, fixed at conception) and phenotypic outcomes (symptoms, function, treatment response). Polygenic risk scores explain at most a few percent of variance in any single disorder, but they shift the prior over biotype membership in informative ways: high MDD-PRS shifts probability toward the depressive-class PTSD biotype (see biotypes-ptsd.md, Section 2); 22q11.2 deletion shifts probability toward atrophy-dominant cognitive-deficit psychosis; ADH1B and ALDH2 variants shift addiction risk and biotype expression in East Asian populations (see biotypes-addiction.md, Section 2.3). Connectomic measurements sit between genotype and phenotype and allow disentanglement of exposome contributions (childhood adversity, trauma, drug exposure, inflammation, infection, gut dysbiosis) from inherited contributions. This is the architecture of the parallel ARPA-H PHO precision health map work being developed in collaboration with this proposal: a layered causal graph where the connectomic coordinate is the testable mediator.

### 4.4 The Williams six-biotype scaffold as starting basis

The Tozzi-Williams 2024 six-biotype solution (see biotypes-depression.md, Section 1.3; biotypes-anxiety.md, Section 1.3) is the strongest current empirical scaffold for the depression-anxiety portion of the coordinate space. It clusters 801 patients on six circuit scores (default mode, salience, attention, negative affect, positive affect, cognitive control), validates by silhouette index, leave-one-out cross-validation, and split-half replication, and links specific biotypes to treatment response (CA+ to venlafaxine, DC+SC+AC+ to behavioral therapy). It is not yet independently replicated by an outside group on independent data, and the Stanford pipeline is partly a closed commercial system, but it is the best operationalized starting point. The B-SNIP three biotypes (see biotypes-psychosis.md, Section 1.1) extend the scaffold into psychotic disorders. The Lanius dissociative subtype, the Stevens-Ressler AURORA biotypes (qualified by failed external replication; see biotypes-ptsd.md, Section 1.2), and the Volkow-Koob three-stage circuit framework for addiction provide further per-disorder lattice points.

---

## 5. Implications for a personalized zoom sensor

### 5.1 Coverage table: biotype to priority regions

The following table consolidates the defensible biotypes from the five per-disorder reviews and identifies the priority brain regions to allocate sensor density to per biotype. "Shallow" means accessible to fNIRS-class spectroscopy at typical 2 to 3 cm depths. "Deep" indicates regions effectively beyond optical reach with current methods, where the headset would rely on indirect indexing through surface proxies. The headset prioritizes shallow targets but tracks cortical signals that index deep regions (for example, dlPFC functional connectivity as a surface proxy for sgACC engagement; medial parietal DMN as a proxy for anterior hippocampus).

| Biotype label | Disorders | Priority cortical / shallow regions | Priority deep regions (index by surface proxy) |
|---|---|---|---|
| Anhedonic / reward-deficit | Depression (Pizzagalli, EMBARC), addiction (reward-deficiency), PTSD (low-reward), psychosis (negative symptoms) | vmPFC, OFC, rACC, medial parietal | Ventral striatum, NAc, VTA |
| Cognitive-control / dlPFC-dACC | Depression (Williams CA+), psychosis (atrophy-dominant), addiction (iRISA), PTSD (treatment response) | dlPFC (Brodmann 46/9), dACC | None primary |
| DMN-rumination / sgACC hyperconnectivity | Depression (Sheline, Fox-Mayberg, Williams DC+SC+AC+), anxiety (worry-DMN cross-talk), PTSD (DMN disruption inverted), addiction (DMN-salience failure) | Posterior cingulate / precuneus, dmPFC, dlPFC | sgACC (Brodmann 25, deep midline) |
| Anxious / fronto-amygdala threat | Depression (Drysdale 1/4), anxiety (central GAD/SAD), PTSD (canonical Biotype A), addiction (stress-driven) | vmPFC, pregenual ACC, sgACC | Amygdala, BNST |
| Salience-interoceptive / craving | Anxiety (panic, somatic GAD), addiction (Naqvi insula), PTSD (salience reactivity), depression (anxious distress) | Anterior insula, dACC | Mid-insula |
| BNST-sustained-threat (worry) | Anxiety (GAD-pure) | Dorsal ACC, right dlPFC, anterior insula | BNST |
| OCD CSTC | Anxiety (OCD washers / checkers) | Medial OFC, lateral OFC, dACC | Head of caudate, ventral striatum, mediodorsal thalamus |
| Dissociative overmodulated | PTSD (Lanius) | dmPFC, mPFC, precuneus, posterior cingulate, posterior insula | Amygdala (inverted activation) |
| Hyperdopaminergic Type A | Psychosis (Howes-McCutcheon Type A) | dACC, dlPFC, ventral pallidum (proxy via dlPFC) | Associative striatum, anterior hippocampus CA1, VTA |
| Glutamatergic / treatment-resistant Type B | Psychosis (Howes Type B, clozapine-eligible) | Anterior cingulate cortex, dlPFC | Thalamus (mediodorsal, pulvinar), hippocampus |
| Sensory-hyperresponsive / gating-impaired | Psychosis (B-SNIP Biotype 2) | Primary auditory cortex (Heschl, planum temporale), sensorimotor cortex, dlPFC | Mediodorsal thalamus |
| Inflammation-linked / immunometabolic | Depression (CRP-high), psychosis (C4-pruned), PTSD (inflammaging), addiction (alcohol neuroinflammation) | vmPFC, anterior insula, white-matter tracts | Ventral striatum, hippocampus (peripheral CRP entry biomarker) |

### 5.2 Honest depth limit

Current diffuse optical and fNIRS methods penetrate roughly 1.5 to 3 cm from scalp under good conditions, which restricts direct observation to cortex (gyral peaks more easily than sulcal walls). Subcortical targets that recur in this synthesis (ventral striatum, anterior hippocampus, amygdala, BNST, mediodorsal thalamus, sgACC at midline depths) are effectively out of direct optical reach today. The proposal honestly cannot promise direct subcortical resolution. What it can promise is shallow-subcortical and cortical-surface coverage of the regions that mediate or index these deep structures: vmPFC and OFC as cortical effectors of amygdala and reward circuits; posterior cingulate / precuneus and medial PFC as DMN hubs that index hippocampus; dlPFC as the anticorrelation index for sgACC; sensorimotor cortex as the thalamic-projection target in psychosis. The "coarse-to-fine zoom" framing rests on this proxy strategy: the headset zooms cortical sampling density to surface regions whose connectivity fingerprints index the deep biotype-relevant nodes.

### 5.3 Anchor region list

A six- to eight-region anchor set covers the bulk of the defensible biotype literature across all five disorders. Listed in priority order:

1. Dorsolateral prefrontal cortex (Brodmann 46/9). Appears in cognitive-control biotype, DMN-rumination biotype, TMS-target biotypes, addiction iRISA, psychosis cortical thinning, PTSD treatment response. Shallow, midline-frontal-lateral, easy optical target.

2. Dorsal anterior cingulate cortex and dorsomedial PFC. Cognitive control, salience hub, central executive, attention dimension. Midline, accessible from above.

3. Ventromedial prefrontal cortex and frontal pole / orbitofrontal cortex. Reward valuation, fear extinction, OCD CSTC, depression-anxiety-PTSD overlap. Frontal-pole access; obstructed somewhat by sinus cavities but functional signal is reachable.

4. Anterior insula (lateral frontal-temporal junction proxy). Salience hub, interoception, addiction craving, panic somatic. Lateral, partially accessible with appropriate optode layout.

5. Subgenual ACC (Brodmann 25). Deep midline, optically challenging but functional fingerprint indexed via dlPFC anticorrelation; not a direct sensor target but a derived coordinate from the dlPFC channel.

6. Superior temporal cortex / primary auditory cortex (Heschl's gyrus, planum temporale). Sensory gating biotype, B-SNIP Biotype 2, hallucination phenomenology. Highly accessible laterally.

7. Posterior cingulate cortex / precuneus. DMN posterior hub, rumination, dissociation-overmodulation, hippocampal proxy. Midline-parietal access.

8. Ventral striatum (surface) and amygdala (effectively out of optical reach). The most clinically actionable subcortical regions, both depth-limited. The headset relies on cortical proxies (vmPFC for amygdala, OFC and dlPFC connectivity for ventral striatum reward) rather than direct measurement.

This eight-region target list maps to the convergent regions identified independently in the depression review (see biotypes-depression.md, Section 9), the anxiety review (see biotypes-anxiety.md, Section 9), the psychosis review (see biotypes-psychosis.md, Section 9), the PTSD review (see biotypes-ptsd.md, Section 10), and the addiction review (see biotypes-addiction.md, Section 9). The cerebellum (lateral hemispheres Crus I/II, vermis) is a tier-2 anchor relevant to psychosis cognitive dysmetria and to alcohol use disorder cerebellar gray-matter loss; it is feasible with caudal optode placement but not in the first-priority set.

---

## 6. Limits and honest assessment

### 6.1 Replication realities

The Drysdale-4 biotypes failed permutation testing in the Dinga 2019 replication and are not currently considered standalone diagnostic biotypes (see biotypes-depression.md, Section 1.2). The Stevens AURORA acute-trauma biotypes failed external replication in Ben-Zion et al. (see biotypes-ptsd.md, Section 1.2). The Etkin VAN-deficit PTSD biotype is supported by within-Stanford-lab cross-cohort consistency but has not been independently replicated by an outside group (see biotypes-ptsd.md, Section 1.4). The Williams 2024 six-biotype solution has been internally cross-validated but not prospectively replicated by an independent multi-site cohort outside the Williams group. The B-SNIP three-biotype solution is the most replicated transdiagnostic biotype framework in psychiatry but is built on EEG and cognition more than connectomics per se.

The proposal should not promise that any specific published biotype is "real" in the sense of clinical deployment-ready. The defensible claim is weaker and more useful: a small number of circuits and a small number of latent axes recur across independent samples, modalities, and diagnostic categories, with effect sizes in the small to moderate range at the individual link level and moderate to large at the network level. These axes constrain where to look. They do not yet tell us what a person's final clinical fate will be.

### 6.2 Replication-by-design

A wearable platform that captures longitudinal within-person trajectories transforms biotyping from a one-shot inference problem to a continuous estimation problem. Per-user circuit coordinates become trajectories with characteristic dynamics (responsivity to sleep, stress, drug effects, social context, medication state). The same biotype may present differently in different patients depending on baseline; the same patient may move between biotypes during illness episodes, treatment, or developmental phases. The platform must be designed with biotypes as Bayesian priors, not labels: each session updates the posterior over biotype membership for the user. Over weeks and months, the user's coordinate trajectory becomes a higher-resolution descriptor than any cross-sectional MRI study can produce.

This is also the right framing for honest replication. The current literature is built on cross-sectional samples of typically 200 to 1,200 participants per study, with multi-site mega-analyses approaching 5,000 to 10,000 (ENIGMA-MDD, ENIGMA-SCZ, ENIGMA-Anxiety, ENIGMA-PGC PTSD, ENIGMA-Addiction). A wearable headset deployed at population scale generates orders of magnitude more within-person samples per individual than any cross-sectional study and avoids between-subject confounds for individual stratification. The longitudinal data argument is not optional rhetoric: it is the only path by which biotype refinement at the individual level becomes statistically tractable.

### 6.3 What the proposal commits to

The Phase 0 proposal commits to: (a) anchor the headset on the eight-region target list above; (b) report circuit-coordinate estimates on the five to six latent axes per user per session; (c) treat the published biotypes (Williams six, B-SNIP three, Drysdale four, Lanius dissociative, Howes Type A/B, Volkow-Koob three-stage) as starting priors that the longitudinal pipeline will refine, not as fixed labels; (d) prospectively replicate the prior structure within the platform's cohort and report concordance and discrepancies transparently; (e) be honest that direct subcortical optical imaging is not feasible at current depths and rely on surface-proxy indexing for amygdala, BNST, ventral striatum, hippocampus, and mediodorsal thalamus.

### 6.4 What the proposal does not promise

The proposal does not promise that any single published biotype is a deployable clinical diagnostic. It does not promise that the headset will resolve subcortical targets at MRI-equivalent spatial resolution. It does not promise that the latent axes will be orthogonal or that the coordinate system will be unique across labs. It promises a defensible scientific foundation and a pathway by which longitudinal wearable data can refine biotype estimates beyond what cross-sectional MRI has produced over the last fifteen years.

---

## 200-word consolidated summary

The headset's anchor target list across biotypes and disorders comprises eight cortical and shallow-subcortical regions: (1) dorsolateral prefrontal cortex (Brodmann 46/9); (2) dorsal anterior cingulate cortex and dorsomedial PFC; (3) ventromedial PFC and orbitofrontal cortex; (4) anterior insula (lateral frontal-temporal junction); (5) subgenual ACC (indexed indirectly via dlPFC anticorrelation, as Mayberg DBS and Fox-Cash TMS targeting both rely on); (6) superior temporal / primary auditory cortex (Heschl's gyrus, planum temporale); (7) posterior cingulate cortex and precuneus; (8) ventral striatum and amygdala, both depth-limited and indexed by their cortical effectors (vmPFC for amygdala; OFC and dlPFC connectivity for ventral striatum). A tier-2 anchor at lateral cerebellum extends coverage for psychosis cognitive dysmetria and alcohol-related cerebellar atrophy.

The mental health coordinate space sits on five to six latent axes: negative affect / threat (amygdala-vmPFC), reward / anhedonia (ventral striatum-OFC), cognitive control (dlPFC-dACC), salience / interoception (anterior insula-dACC), attention / vigilance (dorsal and ventral attention networks), and sensory gating (auditory and sensorimotor cortex, the most psychosis-distinguishing dimension). These axes align with RDoC domains, cut across HiTOP spectra, and provide the connectomic mediator layer between genomic priors and phenotypic outcomes that the parallel ARPA-H precision health map work requires.

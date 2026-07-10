# Biotypes: Major Depressive Disorder

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: researchers, stakeholders
> **Tags**: `literature-synthesis`, `disease-biotypes`, `mdd`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)

Genomic factor loading (Nature 2025): **Internalizing factor** (major depression + PTSD + anxiety), the factor that Grotzinger and colleagues uniquely associated with **oligodendrocyte biology** rather than excitatory-neuron biology [1]. This places MDD in the same genomic neighborhood as PTSD and anxiety and reframes the long-standing glial / myelin findings in depression (section MICRO) as the cell-type signature of a shared internalizing liability.

This document harmonizes molecular findings to Gene Ontology (GO), connectomic findings to the Allen Human Reference Atlas 3D (2020), and phenotype findings to SNOMED CT and the Human Phenotype Ontology (HPO). It follows the shared template in `_TEMPLATE_AND_CONVENTIONS.md`. MDD biotyping is unusually mature in some respects (CRP-stratified inflammation, sgACC-dlPFC anticorrelation for TMS targeting) and unusually fragile in others (the Drysdale four-biotype clustering failed external replication). Both states are flagged explicitly.

## Seed papers

- Grotzinger AD, Werme J, Peyrot WJ, ... Smoller JW. Mapping the genetic landscape across 14 psychiatric disorders. Nature. 2025 (publ. 10 Dec 2025). doi:10.1038/s41586-025-09820-3. [1] (organizing reference; 1,056,201 cases; internalizing-oligodendrocyte factor)
- Drysdale AT, Grosenick L, Downar J, et al. Resting-state connectivity biomarkers define neurophysiological subtypes of depression. Nat Med. 2017;23(1):28-38. doi:10.1038/nm.4246. [2] (four-biotype CCA framework; replication failed)
- Dinga R, Schmaal L, Penninx BWJH, et al. Evaluating the evidence for biotypes of depression. NeuroImage Clin. 2019;22:101796. doi:10.1016/j.nicl.2019.101796. [3] (the negative replication)
- Tozzi L, Zhang X, Pines A, et al. Personalized brain circuit scores identify clinically distinct biotypes in depression and anxiety. Nat Med. 2024;30:2076-2087. doi:10.1038/s41591-024-03057-9. [4] (Williams iMAP six-biotype taxonomy)
- Pizzagalli DA, Webb CA, Dillon DG, et al. Pretreatment rostral anterior cingulate cortex theta activity in relation to symptom improvement in depression. JAMA Psychiatry. 2018;75(6):547-554. [5] (reward / rACC theta)
- Moliner R, Girych M, Brunello CA, et al. Psychedelics promote plasticity by directly binding to BDNF receptor TrkB. Nat Neurosci. 2023;26:1032-1041. doi:10.1038/s41593-023-01316-5. [6] (TrkB plasticity mechanism)
- Raison CL, Rutherford RE, Woolwine BJ, et al. A randomized controlled trial of infliximab for treatment-resistant depression. JAMA Psychiatry. 2013;70(1):31-41. [7] (CRP-stratified inflammation)
- Cole EJ, Phillips AL, Bentzley BS, et al. Stanford Neuromodulation Therapy (SNT): a double-blind randomized controlled trial. Am J Psychiatry. 2022;179(2):132-141. [8] (SAINT, 79% remission, sgACC-dlPFC targeting)

---

## MICRO scale (molecular / genetic / cellular / immune) vs GO-harmonized

The molecular landscape of MDD is best understood as several partially overlapping dysregulations rather than a single lesion. The plasticity-deficit (BDNF/TrkB) axis is the most mechanistically central because all effective antidepressants, including SSRIs, ketamine, psychedelics, ECT, and exercise, converge on potentiating BDNF/TrkB signaling [6]. The Nature 2025 internalizing-oligodendrocyte signature [1] and the postmortem glial-loss literature point to myelin and glial support cells as a second, genetically anchored axis. The remaining axes (serotonergic, inflammatory, kynurenine, oxidative, glutamatergic, GABAergic, dopaminergic) are dimensional and frequently co-occur.

| Biotype / dysregulation | GO term(s) + ID | Specific finding (genes, variants, molecules) | Neurotransmitter family | BDNF / neurotrophin + plasticity | E/I imbalance (+ region) | Oxidative / mito / ROS | Immune / inflammatory | Confidence | Source |
|---|---|---|---|---|---|---|---|---|---|
| Plasticity-deficit (BDNF / TrkB) | neurotrophin TRK receptor signaling (GO:0048011); regulation of synaptic plasticity (GO:0048167); positive regulation of long-term synaptic potentiation (GO:1900273) | Reduced serum/plasma BDNF in MDD, recovering with response; rs6265 (Val66Met) Met carriers show blunted activity-dependent BDNF release and reduced ketamine/SSRI response; antidepressants, ketamine and psychedelics bind TrkB transmembrane domain (residues Y433/A434/V436/V437) and potentiate endogenous BDNF; Y433F mutation abolishes the antidepressant-like effect | none reported (the pivot is downstream of multiple transmitters) | YES vs central. BDNF/TrkB-dependent dendritic spinogenesis and "iPlasticity"; LSD/psilocin K_i ~3-7 nM vs fluoxetine ~4.8 µM | indirect: TrkB activation in PV interneurons disinhibits pyramidal cells, raising cortical gamma (Winkel 2021) | BDNF-TrkB upregulates PGC-1alpha and mitochondrial biogenesis; low-BDNF likely low-mito-reserve | cytokines (IL-6, TNF) downregulate BDNF | HIGH | [6,9,10] |
| Serotonergic (5-HTT / SERT) | serotonin transport (GO:0006837); serotonin receptor signaling pathway (GO:0007210) | SLC6A4 (5-HTT) is the SSRI target; 5-HTTLPR association with stress-reactive depression is contested and largely non-replicated at the candidate-gene level; PGC-MDD GWAS does not center serotonergic genes; Als et al. implicate serotonergic among broader neuronal subtypes | **Serotonin** | SSRIs elevate brain BDNF (original neurotrophic hypothesis, Duman 1997); links serotonergic to plasticity axis | none specific | none specific | downregulated by inflammation via IDO shunt | MEDIUM (mechanism HIGH; candidate-gene LOW) | [9,11] |
| Inflammatory / immunometabolic (CRP-high) | inflammatory response (GO:0006954); cytokine-mediated signaling pathway (GO:0019221) | ~25-30% of MDD have CRP > 3 mg/L; elevated IL-6, TNF-alpha; converges with atypical-features MDD (weight gain, hypersomnia, fatigue, anhedonia); positive genetic correlation of atypical MDD with BMI, CRP, triglycerides (Milaneschi immunometabolic depression) | dopamine (downstream: inflammation reduces striatal DA / reward signaling) | inflammation suppresses BDNF | E-effects via QUIN at NMDA (see kynurenine row) | TNF/IL-6 raise ROS | YES vs central; CRP, IL-6, TNF-alpha; microglial activation in TRD/suicidal MDD (PET TSPO, mixed) | HIGH (biotype exists); MEDIUM (clinical actionability) | [7,12,13,14] |
| Kynurenine / tryptophan-metabolic | tryptophan catabolic process to kynurenine (GO:0019441); response to cytokine (GO:0034097) | IDO shifts tryptophan from serotonin to kynurenine under inflammation; decreased plasma kynurenine and kynurenic acid (KYNA) in MDD; increased quinolinic acid (QUIN)/KYNA ratio in suicidal patients; CSF QUIN elevated in suicide attempters (Erhardt) | **Serotonin** (depleted precursor); **Glutamate** (QUIN is an NMDA agonist, KYNA an NMDA antagonist) | none direct | E-up via QUIN at NMDA receptors (excitotoxic); region-nonspecific | QUIN promotes ROS | YES vs driven by IDO induction downstream of cytokines | MEDIUM | [15] |
| Oxidative stress / mitochondrial | response to oxidative stress (GO:0006979); mitochondrial ATP synthesis coupled electron transport (GO:0042775) | Elevated 8-OHdG (DNA oxidative damage) most consistent peripheral marker; lipid peroxides; N-acetylcysteine (NAC) shows small group-level effect, consistent with an oxidative-positive subgroup | none specific | low-BDNF couples to low mitochondrial reserve | links to PV-interneuron oxidative vulnerability (Cabungcal/Do model) | YES vs central | secondary to inflammation | MEDIUM | [16] |
| Glutamatergic (NMDA / rapid plasticity) | glutamatergic synaptic transmission (GO:0035249); NMDA selective glutamate receptor signaling (GO:0098989) | Ketamine/esketamine block NMDA, producing a glutamate surge, AMPA throughput and rapid synaptogenesis; lower baseline ACC glutamate and larger post-infusion pregenual-ACC glutamate rise predict ketamine response; Glx/GABA ratio in dorsal ACC proposed as proxy | **Glutamate** | YES vs ketamine's antidepressant effect is BDNF/TrkB-dependent and Met-carrier-blunted | E-modulation in ACC/PFC; the mechanism is a transient glutamate surge | mitochondrial coupling via plasticity | none direct | HIGH (mechanism); MEDIUM (as standalone biotype) | [6,9,17] |
| GABAergic (reduced cortical inhibition) | GABAergic synaptic transmission (GO:0051932); gamma-aminobutyric acid signaling pathway (GO:0007214) | Reduced MRS-measured GABA in prefrontal/occipital cortex in MDD (Sanacora-line findings); reduced inhibitory tone; zuranolone (GABA-A PAM) FDA-approved 2023 for postpartum depression with rapid effect | **GABA** | TrkB in PV (GABAergic) interneurons mediates iPlasticity | I-down in PFC (reduced GABA → disinhibition) | none specific | none specific | MEDIUM | [9,18] |
| Dopaminergic (anhedonic / reward-deficit) | dopamine receptor signaling pathway (GO:0007212); dopamine secretion (GO:0014046) | Ventral striatal / mesocorticolimbic hypofunction underlies anhedonia; ketamine reward rescue localizes to D1-MSN strengthening in NAc (rodent); Als et al. implicate medium spiny neurons (MSNs) among causal subtypes | **Dopamine** | BDNF in NAc shell paradoxically increases depression-like behavior (Eisch 2003); regional, not global | none specific | none specific | inflammation reduces striatal DA / reward connectivity (Felger) | MEDIUM-HIGH | [9,14,19] |
| Glial / oligodendrocyte / myelin | oligodendrocyte differentiation (GO:0048709); myelination (GO:0042552); glial cell development (GO:0021782) | Internalizing genomic factor uniquely enriched for oligodendrocyte genes (Nature 2025); postmortem reduced astrocyte and oligodendrocyte density in dlPFC, OFC, subgenual cingulate and amygdala; reduced GFAP; Nagy et al. 2020 snRNA-seq of dlPFC in MDD-suicide implicates deep-layer excitatory neurons and oligodendrocyte-precursor cells (OPCs) | none reported | reduced glial support degrades synaptic maintenance | possible E/I effect via impaired myelination of interneurons | none specific | microglial findings mixed | MEDIUM-HIGH (genetic + postmortem converge) | [1,20] |
| Polygenic burden (PGC-MDD) | (no single GO term; broad transcriptional regulation, GO:0006355) | Howard 2019: 102 independent variants, 269 genes, SNP-h² ≈ 0.089 (liability scale), enrichment for prefrontal/anterior-cingulate/frontal-cortex tissue. Als et al. (685,808 cases): 697 independent associations / 636 loci, causal enrichment in excitatory + inhibitory midbrain/forebrain neurons, peptidergic neurons and MSNs; antidepressant-target enrichment | mixed (serotonergic, dopaminergic, glutamatergic) | not centered in GWAS | not localized | not centered | not centered | HIGH (GWAS robust); LOW (clinical stratification: PRS explains 1-3%) | [1,9,21] |

GO IDs given without flag are ones I am confident in; pathway-level GO terms (kynurenine, oligodendrocyte) are anchored to standard GO biological-process classes but specific sub-process curation may refine them. Do not treat any ID here as a substitute for ontology-team verification.

---

## MESO scale (connectomic) vs Allen Atlas nodes + edges

The connectomic literature in MDD converges on a short list of regions despite framework disagreement. The crucial point for a sensing platform is in the EDGES table: the single most validated MDD connectomic biomarker is not a regional abnormality but an **edge sign**, the resting-state anticorrelation between dlPFC and sgACC, which underpins personalized TMS targeting (SAINT/SNT) [8]. Functional regions (dlPFC, sgACC, DMN) are not 1:1 with Allen anatomical parcels; each is mapped below to its containing Allen structure with the functional label in parentheses.

### NODES

| Allen region (functional label) | Observed change | Modality | Confidence | Source |
|---|---|---|---|---|
| cingulate gyrus, subgenual part (sgACC / Brodmann 25) | hyperactivity / hypermetabolism; central node of TRD severity and DBS targeting | fMRI / PET / structural | HIGH | [22,23,2] |
| frontal lobe, dorsolateral prefrontal cortex (dlPFC / BA46/9) | hypoactivity; reduced cognitive-control engagement; TMS target | fMRI / EEG | HIGH | [4,8,24] |
| frontal lobe, medial orbital / ventromedial sector (vmPFC / OFC) | thinner cortex (ENIGMA-MDD); altered reward valuation | structural / fMRI | MEDIUM | [25,26] |
| cingulate gyrus, anterior part (dACC) | salience-network and cognitive-control node; altered engagement | fMRI / EEG | MEDIUM | [4,24] |
| accumbens / ventral striatum | hypoactivation to reward (anhedonia); inflammation reduces reward connectivity | fMRI | MEDIUM-HIGH | [5,14,19] |
| amygdala | altered reactivity; surface deformation (ENIGMA shape); larger pretreatment volume predicts ECT response | fMRI / structural | MEDIUM | [25,27] |
| hippocampus | smaller volume (ENIGMA Cohen's d ≈ -0.14), driven by recurrent/early-onset MDD | structural | MEDIUM (group); LOW (individual) | [25] |
| posterior cingulate cortex / precuneus | DMN posterior hub; hyperconnectivity associated with rumination | fMRI | MEDIUM | [28,29] |
| insula, anterior part | salience-network node; interoception; cortical thinning | fMRI / structural | MEDIUM | [26,29] |
| cingulate gyrus, rostral anterior / pregenual (rACC) | pretreatment theta / activity predicts broad antidepressant response | EEG / fMRI | HIGH (as predictor) | [5] |

### EDGES

| Region A vs Region B (functional labels) | Association sign | Observed change in disorder | Modality | Confidence | Source |
|---|---|---|---|---|---|
| dlPFC (BA46) vs sgACC (BA25) | negative (anticorrelation) | normally anticorrelated; **stronger baseline anticorrelation predicts better TMS response**; SAINT/SNT targets the dlPFC voxel most anticorrelated with sgACC (79% remission) | fMRI (targeting) | HIGH | [8,22,24,30] |
| posterior cingulate / precuneus vs medial PFC (DMN core) | positive | DMN hyperconnectivity; tracks rumination and self-referential negative processing | fMRI | MEDIUM-HIGH | [28,29] |
| dorsomedial PFC vs DMN / cognitive-control / affective nodes ("dorsal nexus") | positive | abnormal cross-network hyperconnectivity converging on dmPFC in MDD | fMRI | MEDIUM | [28] |
| amygdala vs ventromedial / prefrontal cortex (fronto-limbic) | mixed (normally negative top-down) | reduced fronto-amygdala connectivity in anxious/anhedonic presentations (Drysdale axis) | fMRI | MEDIUM (axis); LOW (Drysdale clusters) | [2,3] |
| amygdala vs sgACC (right) | positive | reduced baseline amygdala-sgACC connectivity predicted ketamine response (88.9% sens / 100% spec, single small cohort) | fMRI | LOW (single lab) | [31] |
| ventral striatum vs ventromedial PFC (reward circuit) | positive | reduced corticostriatal reward connectivity scales with CRP/IL-6 (inflammation-reward bridge) | fMRI | MEDIUM | [14] |
| dlPFC vs dACC (cognitive-control circuit) | positive | reduced engagement during cognitive control defines Williams "cognitive biotype"; predicts TMS-induced cognitive improvement (B-SMART-fMRI) | fMRI (task) | MEDIUM | [4,24] |

**EEG/MEG meso findings (electrophysiology):**

- **Blunted Reward Positivity (RewP / feedback positivity)**: smaller 250-300 ms positive deflection to reward; replicated across labs as an anhedonic / reward-deficit marker (Proudfit 2015; EMBARC-linked). Recoverable on frontal-central EEG with a simple reward task. Confidence MEDIUM-HIGH. [32,33]
- **REM density / REM latency**: short REM latency and elevated REM density (classic Kupfer-era markers) predict SSRI/SNRI response across cohorts; a 2025 paper reports REM density predicting ketamine response in TRD. Requires sleep EEG. Confidence MEDIUM. [34,35]
- **Frontal alpha asymmetry**: historically proposed (relatively reduced left-frontal activity); 2017 and 2025 meta-analyses find a **small and inconsistent effect** at the group level. Flagged as low-effect; not reliable for individual stratification. Confidence LOW. [36,37]
- **rACC theta / theta-cordance**: higher pretreatment rACC theta and prefrontal cordance predict antidepressant response across SSRIs, TMS, and sleep deprivation; one of the most replicated electrophysiological predictors in depression. Confidence HIGH (as a treatment-response predictor). [5,38]

No Allen 141-region parcel needs to be supplemented for MDD; sgACC maps to "cingulate gyrus, subgenual part" and dlPFC to the dorsolateral sector of the frontal lobe within the Allen scheme. Where a finding is reported at finer functional resolution (e.g., a specific dlPFC subvoxel for TMS targeting), that resolution exceeds the Allen anatomical parcel and is treated as a within-region functional coordinate.

---

## MACRO scale (phenotype) vs SNOMED CT / HPO

MDD phenotypes map onto symptom dimensions that recur across the biotype frameworks: anhedonia (reward axis), depressed mood, neurovegetative disturbance (sleep/appetite, splitting into melancholic vs atypical poles), cognitive impairment, anxious distress, and suicidality. The melancholic/atypical split is the phenotype layer that most cleanly aligns with biology, because atypical features (hypersomnia, weight gain, leaden paralysis, fatigue) track the inflammatory/immunometabolic biotype.

| Biotype phenotype | SNOMED CT term + ID | HPO term + ID | Short description of observations that led to this mapping | Source |
|---|---|---|---|---|
| Major depressive disorder (umbrella) | Major depressive disorder (370143000) | Major depressive disorder (HP:0007302); Depressivity (HP:0000716) | Core diagnostic anchor for the disorder set | [9] |
| Anhedonia / reward-deficit | Anhedonia (28669007) | Anhedonia (HP:0033676) | Reduced reward responsiveness; blunted RewP; ventral-striatal hypoactivation; tracks dopaminergic and inflammatory biotypes | [5,32,14] |
| Depressed mood (core affective) | Depressed mood (366979004) | Depressivity (HP:0000716) | Sustained low mood, negative self-referential processing; DMN hyperconnectivity / rumination | [28,29] |
| Neurovegetative, melancholic features | Melancholia (45007003); Major depression, melancholic type (191610000, approx, needs curation) | Insomnia (HP:0100785); Weight loss (HP:0001824) | Early-morning waking, weight loss, psychomotor change, non-reactive mood, diurnal variation; HPA-axis dysregulation, less inflammation-linked | [12,18] |
| Neurovegetative, atypical / immunometabolic | Atypical depressive disorder (35489007, approx, needs curation) | Hypersomnia (HP:0033813); Increased body weight (HP:0004324); Fatigue (HP:0012378) | Hypersomnia, weight gain, leaden paralysis, mood reactivity, rejection sensitivity; maps to CRP-high / immunometabolic biotype | [7,12,13] |
| Cognitive impairment (concentration, decisions) | Impaired concentration (60032008, approx, needs curation) | Impaired executive functioning (HP:0033694, approx, needs curation) | Reduced cognitive-control circuit engagement (dlPFC-dACC); predicts treatment resistance and TMS-responsive cognitive biotype | [4,24] |
| Anxious distress / fronto-limbic | Anxiety (48694002) | Anxiety (HP:0000739) | Comorbid anxious arousal; reduced fronto-amygdala regulation; overlaps internalizing-factor genetics | [2,4] |
| Suicidality | Suicidal thoughts (6471006); Suicidal ideation (225457007, approx, needs curation) | Suicidal ideation (HP:0031589, approx, needs curation) | Elevated CSF QUIN and QUIN/KYNA ratio in suicide attempters; distinct neurochemical signature | [15] |
| Fatigue / psychomotor slowing | Fatigue (84229001); Psychomotor retardation (62718007, approx, needs curation) | Fatigue (HP:0012378) | Anergia and slowing; concentrated in inflammatory and anhedonic biotypes | [7,14] |

SNOMED and HPO IDs given without a flag are ones I am confident in (e.g., Major depressive disorder 370143000; Anhedonia HP:0033676). Several subtype codes are marked "approx, needs curation" because SNOMED's melancholic/atypical hierarchy and some HPO neuropsychiatric terms shift between releases and should be verified against the current edition.

---

## Interventional studies (incl. neuromodulation, DBS, neuroplastogens)

This table links each interventional finding to the biotype it most plausibly targets. The strongest biotype-stratified evidence in MDD is for TMS targeting via sgACC-dlPFC anticorrelation, CRP-stratified anti-inflammatory response, and reward-circuit moderation of SSRI-over-placebo benefit. Psychedelic and ketamine plasticity mechanisms point at the BDNF/TrkB axis but per-biotype clinical stratification remains preliminary.

| Biotype it targets | Intervention (class + specific) | Study (author year, design, n) | Outcome | Confidence | Source |
|---|---|---|---|---|---|
| Serotonergic / anxious | SSRI (sertraline, escitalopram); SNRI (venlafaxine) | EMBARC (Greenberg/Pizzagalli 2020, RCT, n=296 sertraline vs placebo); RAINBOW/iMAP (Tozzi 2024, n=250) | Higher ventral-striatal reward activity moderates sertraline-over-placebo benefit; Williams cognitive-overactivity biotype ~2x remission on venlafaxine | MEDIUM | [5,4] |
| Anxious-anhedonic + low ACC glutamate | NMDA antagonist: IV racemic ketamine; intranasal esketamine (FDA-approved Spravato 2019) | Multiple TRD RCTs; mechanistic MRS cohorts | Lower baseline ACC glutamate + larger post-infusion pregenual-ACC glutamate rise predict response; high baseline anhedonia over-represented among responders; Met (rs6265) carriers respond less | MEDIUM | [6,9,17,31] |
| Plasticity-deficit (BDNF/TrkB) | Neuroplastogen: psilocybin (COMP360) | Compass COMP005 (phase 3, n≈258, 2025) primary MADRS endpoint met; COMP006 (phase 3, two 25 mg doses, 2026) -3.8 MADRS vs 1 mg, p<0.001 (first replicated phase-3 psychedelic readout); Usona (phase 2, JAMA 2023) | Statistically significant MADRS reduction; durability data (26-wk) pending Q3 2026; mechanism is TrkB-dependent plasticity, plus acute DMN desynchronization predicting response | MEDIUM-HIGH (efficacy); MEDIUM (biotype link) | [6,39,40] |
| Plasticity-deficit (non-hallucinogenic) | TrkB-PAM / engineered psychoplastogen: DLX-001 (zalsupindole) | Delix phase 1 in MDD (ongoing Jan 2026) | Early-stage; rational target for patients with deep plasticity deficits and intact 5-HT2A | LOW | [6] |
| sgACC-dlPFC anticorrelation circuit | rTMS / iTBS, fMRI-personalized: Stanford SAINT/SNT (accelerated iTBS, 90,000 pulses, target = dlPFC voxel most anticorrelated with sgACC) | Cole 2022 (double-blind RCT, n=29) | 79% remission in TRD vs ~13% sham; single site, single trial, durability requires re-dosing | HIGH (within trial); MEDIUM (replication pending) | [8,30] |
| Cognitive-control (dlPFC-dACC) biotype | rTMS, left dlPFC | B-SMART-fMRI (Tozzi/Williams 2024, n=43 TRD veterans) | Only "cognitive-biotype-positive" subgroup (reduced baseline dlPFC-dACC engagement) showed circuit + behavioral improvement | MEDIUM | [4,24] |
| dmPFC / fronto-amygdala biotype | dmPFC rTMS | Drysdale 2017 (n=154 by biotype) | Biotype 1 ~80% vs worst biotype ~25% response; **but biotype clustering failed external replication (Dinga 2019)** | LOW (biotype clusters); flagged | [2,3] |
| Broad MDD (cortical-excitability) | tDCS, at-home: Flow Neuroscience FL-100 | EMPOWER (remote double-blind RCT, n=174) | 58% remission active vs ~20% sham at week 10; FDA premarket approval 8 Dec 2025 (first at-home brain-stimulation device for moderate-severe MDD) | MEDIUM-HIGH | [41] |
| Treatment-resistant depression (TRD) | DBS, subcallosal cingulate (sgACC white-matter convergence) | Riva-Posse/Mayberg 2018 (connectomic targeting, n=11); Crowell 2019 (8-yr follow-up) | 81.8% responders / 54.5% remitters at 1 yr with tractography targeting; durable at 8 yr in initial responders. **BROADEN trial (fixed gray-matter coordinate, no individualized tractography) failed futility analysis**; the precise white-matter convergence point matters | MEDIUM (tractography cohorts); flagged BROADEN caveat | [22,23] |
| TRD (FDA-approved adjunct) | VNS, implanted cervical (left vagus) | FDA-approved 2005 (adjunct, ≥4 failed treatments); RECOVER trial (Conway et al. 2024, double-blind, n=493) | RECOVER missed the primary acute endpoint but showed improvement on secondary symptom, QoL, and functioning measures over 12 months; durable benefit in extension | MEDIUM | [42,43] |
| Inflammatory / CRP-high | Anti-TNF: infliximab | Raison 2013 (RCT, n=60) | No main effect; in prespecified CRP > 5 mg/L subgroup, 62% response vs 33% placebo (NNT ~4-5). Canonical stratified-biomarker study; infliximab not clinically deployed for MDD | MEDIUM-HIGH (stratification); LOW (deployability) | [7] |
| GABAergic / perinatal | GABA-A PAM: zuranolone | FDA approval 2023 (postpartum depression) | Rapid antidepressant effect via GABA-A; indication limited to PPD | MEDIUM | [18] |
| Anxious / fronto-amygdala (structural) | ECT | Joshi 2016; Cao 2018 (ML on hippocampal subfields) | Larger pretreatment amygdala volume predicts ECT response; hippocampal subfield ML predicted response (r≈0.81); ECT raises BDNF/neuroplasticity | MEDIUM | [27,44] |

---

## Most defensible biotypes (cross-scale synthesis)

Integrating across scales, five MDD biotypes survive scrutiny. Confidence reflects multi-lab/multi-modal convergence, with replication failures flagged.

1. **Plasticity-deficit (BDNF/TrkB) biotype.** MICRO: low BDNF, Met-carrier blunting, TrkB as the convergent pivot for all effective antidepressants [6]. MESO: less circuit-specific, but indexed indirectly by cortical excitability and DMN reorganization under psilocybin. MACRO: treatment resistance. Interventions: psychedelics (COMP006 replicated phase 3), ketamine, ECT. Confidence HIGH for mechanism, MEDIUM for clinical operationalization.

2. **Anhedonic / reward-deficit biotype.** MICRO: dopaminergic + inflammatory convergence; MSN enrichment in GWAS [19,14]. MESO: ventral-striatum hypoactivation, blunted RewP, reduced VS-vmPFC connectivity. MACRO: anhedonia (HP:0033676), psychomotor slowing. Interventions: ventral-striatal reward activity moderates sertraline benefit; ketamine rescues reward. Confidence MEDIUM-HIGH.

3. **DMN-rumination / sgACC-dlPFC circuit biotype.** MESO is the anchor: the dlPFC-sgACC anticorrelation (the SAINT/SNT targeting biomarker, 79% remission) and DMN hyperconnectivity [8,28]. MACRO: rumination, depressed mood. Interventions: personalized TMS, sgACC DBS for TRD (tractography-targeted; BROADEN failed without it). Confidence HIGH for the circuit, MEDIUM for it being a discrete biotype versus a continuum.

4. **Inflammatory / immunometabolic biotype.** MICRO: CRP > 3 mg/L in ~25-30%, IL-6/TNF, kynurenine shunt [7,12,15]. MESO: reduced corticostriatal reward connectivity. MACRO: atypical features (hypersomnia, weight gain, fatigue). Interventions: infliximab in CRP > 5 mg/L subgroup (62% vs 33%). Confidence HIGH for existence.

5. **Cognitive-control (dlPFC-dACC) biotype.** MESO: reduced dlPFC-dACC engagement [4,24]. MACRO: cognitive impairment, treatment resistance. Interventions: TMS-responsive cognitive improvement (B-SMART-fMRI); venlafaxine advantage in the overactivity variant. Confidence MEDIUM (one strong lab plus a small TMS trial).

**Not defensible as standalone biotypes:** the specific Drysdale-4 cluster labels (Dinga 2019 replication failure, flagged throughout) [2,3]; polygenic-only stratification (PRS explains 1-3%); frontal alpha asymmetry as an individual marker (small, inconsistent effect).

**Genomic factor statement:** MDD loads on the **Internalizing factor** (shared with PTSD and anxiety), uniquely associated with **oligodendrocyte biology** in the Grotzinger Nature 2025 analysis [1], which reframes the glial/myelin postmortem findings as the cell-type signature of a shared internalizing liability.

---

## References

1. Grotzinger AD, Werme J, Peyrot WJ, et al. Mapping the genetic landscape across 14 psychiatric disorders. Nature. 2025 (publ. 10 Dec 2025). doi:10.1038/s41586-025-09820-3. https://pubmed.ncbi.nlm.nih.gov/41372416/
2. Drysdale AT, Grosenick L, Downar J, et al. Resting-state connectivity biomarkers define neurophysiological subtypes of depression. Nat Med. 2017;23(1):28-38. doi:10.1038/nm.4246. https://pubmed.ncbi.nlm.nih.gov/27918562/
3. Dinga R, Schmaal L, Penninx BWJH, et al. Evaluating the evidence for biotypes of depression: Methodological replication and extension of Drysdale et al. (2017). NeuroImage Clin. 2019;22:101796. doi:10.1016/j.nicl.2019.101796. https://pmc.ncbi.nlm.nih.gov/articles/PMC6543446/
4. Tozzi L, Zhang X, Pines A, et al. Personalized brain circuit scores identify clinically distinct biotypes in depression and anxiety. Nat Med. 2024;30:2076-2087. doi:10.1038/s41591-024-03057-9. https://www.nature.com/articles/s41591-024-03057-9
5. Pizzagalli DA, Webb CA, Dillon DG, et al. Pretreatment rostral anterior cingulate cortex theta activity in relation to symptom improvement in depression. JAMA Psychiatry. 2018;75(6):547-554. https://pubmed.ncbi.nlm.nih.gov/29641834/
6. Moliner R, Girych M, Brunello CA, et al. Psychedelics promote plasticity by directly binding to BDNF receptor TrkB. Nat Neurosci. 2023;26:1032-1041. doi:10.1038/s41593-023-01316-5. https://pubmed.ncbi.nlm.nih.gov/37280397/
7. Raison CL, Rutherford RE, Woolwine BJ, et al. A randomized controlled trial of the tumor necrosis factor antagonist infliximab for treatment-resistant depression: the role of baseline inflammatory biomarkers. JAMA Psychiatry. 2013;70(1):31-41. doi:10.1001/2013.jamapsychiatry.4.
8. Cole EJ, Phillips AL, Bentzley BS, et al. Stanford Neuromodulation Therapy (SNT): a double-blind randomized controlled trial. Am J Psychiatry. 2022;179(2):132-141. doi:10.1176/appi.ajp.2021.20101429.
9. Als TD, Kurki MI, Grove J, et al. Depression pathophysiology, risk prediction of recurrence and comorbid psychiatric disorders using genome-wide analyses. Nat Med. 2023;29:1832-1844 (and PGC-MDD 685,808-individual meta-analysis; medRxiv 2024 doi:10.1101/2024.04.29.24306535). https://pmc.ncbi.nlm.nih.gov/articles/PMC11092713/
10. Castrén E, Antila H. Neuronal plasticity and neurotrophic factors in drug responses. Mol Psychiatry. 2017;22(8):1085-1095. doi:10.1038/mp.2017.61.
11. Duman RS, Heninger GR, Nestler EJ. A molecular and cellular theory of depression. Arch Gen Psychiatry. 1997;54(7):597-606.
12. Milaneschi Y, Lamers F, Berk M, Penninx BWJH. Depression heterogeneity and its biological underpinnings: toward immunometabolic depression. Biol Psychiatry. 2020;88(5):369-380. doi:10.1016/j.biopsych.2020.01.014.
13. Milaneschi Y, Simmons WK, van Rossum EFC, Penninx BWJH. Depression and obesity: evidence of shared biological mechanisms. Mol Psychiatry. 2019;24(1):18-33. doi:10.1038/s41380-018-0017-5.
14. Felger JC, Li Z, Haroon E, et al. Inflammation is associated with decreased functional connectivity within corticostriatal reward circuitry in depression. Mol Psychiatry. 2016;21(10):1358-1365. doi:10.1038/mp.2015.168.
15. Ogyu K, Kubo K, Noda Y, et al. Kynurenine pathway in depression: a systematic review and meta-analysis. Neurosci Biobehav Rev. 2018;90:16-25. doi:10.1016/j.neubiorev.2018.03.023.
16. Black CN, Bot M, Scheffer PG, et al. Is depression associated with increased oxidative stress? A systematic review and meta-analysis. Psychoneuroendocrinology. 2015;51:164-175.
17. Abdallah CG, De Feyter HM, Averill LA, et al. The effects of ketamine on prefrontal glutamate neurotransmission in healthy and depressed subjects. Neuropsychopharmacology. 2018;43(10):2154-2160.
18. Sanacora G, Mason GF, Rothman DL, et al. Reduced cortical gamma-aminobutyric acid levels in depressed patients determined by proton magnetic resonance spectroscopy. Arch Gen Psychiatry. 1999;56(11):1043-1047.
19. Pizzagalli DA. Depression, stress, and anhedonia: toward a synthesis and integrated model. Annu Rev Clin Psychol. 2014;10:393-423. https://pmc.ncbi.nlm.nih.gov/articles/PMC3972338/
20. Nagy C, Maitra M, Tanti A, et al. Single-nucleus transcriptomics of the prefrontal cortex in major depressive disorder implicates oligodendrocyte precursor cells and excitatory neurons. Nat Neurosci. 2020;23(6):771-781. doi:10.1038/s41593-020-0621-y.
21. Howard DM, Adams MJ, Clarke TK, et al. Genome-wide meta-analysis of depression identifies 102 independent variants and highlights the importance of the prefrontal brain regions. Nat Neurosci. 2019;22(3):343-352. https://pmc.ncbi.nlm.nih.gov/articles/PMC6522363/
22. Riva-Posse P, Choi KS, Holtzheimer PE, et al. A connectomic approach for subcallosal cingulate deep brain stimulation surgery: prospective targeting in treatment-resistant depression. Mol Psychiatry. 2018;23(4):843-849. doi:10.1038/mp.2017.59.
23. Crowell AL, Riva-Posse P, Holtzheimer PE, et al. Long-term outcomes of subcallosal cingulate deep brain stimulation for treatment-resistant depression. Am J Psychiatry. 2019;176(11):949-956. https://pubmed.ncbi.nlm.nih.gov/31581800/
24. Tozzi L, Bertrand C, Hack LM, et al. A cognitive neural circuit biotype of depression showing functional and behavioral improvement after transcranial magnetic stimulation in the B-SMART-fMRI trial. Nat Mental Health. 2024. doi:10.1038/s44220-024-00271-9.
25. Schmaal L, Veltman DJ, van Erp TGM, et al. Subcortical brain alterations in major depressive disorder: findings from the ENIGMA Major Depressive Disorder working group. Mol Psychiatry. 2016;21(6):806-812. https://pmc.ncbi.nlm.nih.gov/articles/PMC4879183/
26. Schmaal L, Hibar DP, Sämann PG, et al. Cortical abnormalities in adults and adolescents with major depression based on brain scans from 20 cohorts worldwide in the ENIGMA MDD Working Group. Mol Psychiatry. 2017;22(6):900-909. https://pmc.ncbi.nlm.nih.gov/articles/PMC5444023/
27. Joshi SH, Espinoza RT, Pirnia T, et al. Structural plasticity of the hippocampus and amygdala induced by electroconvulsive therapy in major depression. Biol Psychiatry. 2016;79(4):282-292. https://pmc.ncbi.nlm.nih.gov/articles/PMC4244657/
28. Sheline YI, Price JL, Yan Z, Mintun MA. Resting-state functional MRI in depression unmasks increased connectivity between networks via the dorsal nexus. Proc Natl Acad Sci USA. 2010;107(24):11020-11025.
29. Kaiser RH, Andrews-Hanna JR, Wager TD, Pizzagalli DA. Large-scale network dysfunction in major depressive disorder: a meta-analysis of resting-state functional connectivity. JAMA Psychiatry. 2015;72(6):603-611.
30. Fox MD, Buckner RL, White MP, Greicius MD, Pascual-Leone A. Efficacy of transcranial magnetic stimulation targets for depression is related to intrinsic functional connectivity with the subgenual cingulate. Biol Psychiatry. 2012;72(7):595-603. https://pmc.ncbi.nlm.nih.gov/articles/PMC4120275/
31. Nakamura T, Tomita M, Horikawa N, et al. Functional connectivity between the amygdala and subgenual cingulate gyrus predicts the antidepressant effects of ketamine in patients with treatment-resistant depression. Neuropsychopharmacol Rep. 2021;41(2):168-178. https://pubmed.ncbi.nlm.nih.gov/33615749/
32. Proudfit GH. The reward positivity: from basic research on reward to a biomarker for depression. Psychophysiology. 2015;52(4):449-459. doi:10.1111/psyp.12370.
33. Klawohn J, Burani K, Bruchnak A, et al. Reduced neural response to reward and pleasant pictures independently relate to depression. Psychol Med. 2021;51(5):741-749.
34. Kupfer DJ, Foster FG. Interval between onset of sleep and rapid-eye-movement sleep as an indicator of depression. Lancet. 1972;2(7779):684-686.
35. Duncan WC, et al. REM density predicts rapid antidepressant response to ketamine in individuals with treatment-resistant depression. Transl Psychiatry. 2025. https://pubmed.ncbi.nlm.nih.gov/39955416/
36. van der Vinne N, Vollebregt MA, van Putten MJAM, Arns M. Frontal alpha asymmetry as a diagnostic marker in depression: fact or fiction? A meta-analysis. NeuroImage Clin. 2017;16:79-87. https://pmc.ncbi.nlm.nih.gov/articles/PMC5524421/
37. Meta-analysis of resting frontal alpha asymmetry as a biomarker of depression. npj Mental Health Research. 2025. https://www.nature.com/articles/s44184-025-00117-x
38. Cook IA, Hunter AM, Korb AS, Leuchter AF. Quantitative EEG biomarkers for predicting likelihood and speed of achieving sustained remission in major depression. Transl Psychiatry. 2013.
39. Compass Pathways. Topline phase 3 COMP005 results (COMP360 psilocybin 25 mg, n≈258, MADRS primary endpoint met). 2025. https://ir.compasspathways.com/
40. Compass Pathways. Topline phase 3 COMP006 results (two 25 mg doses, -3.8 MADRS vs 1 mg, p<0.001; first replicated phase-3 psychedelic readout). 2026. https://ir.compasspathways.com/
41. Woodham RD, Selvaraj S, Lajmi N, et al. Home-based transcranial direct current stimulation treatment for major depressive disorder (EMPOWER): a fully remote, double-blind, sham-controlled RCT. Nat Med. 2025. (Flow Neuroscience FL-100; FDA PMA 8 Dec 2025.)
42. Conway CR, Aaronson ST, Sackeim HA, et al. Vagus nerve stimulation in treatment-resistant depression: a one-year, randomized, sham-controlled trial (RECOVER). Brain Stimul. 2024;17(6). doi:10.1016/j.brs.2024.11.006. https://pubmed.ncbi.nlm.nih.gov/39706521/
43. US FDA. Approval of vagus nerve stimulation (VNS) as adjunctive long-term therapy for chronic or recurrent treatment-resistant depression. 2005.
44. Cao B, Luo Q, Fu Y, et al. Predicting individual responses to the electroconvulsive therapy with hippocampal subfield volumes in major depression disorder. Sci Rep. 2018;8:5434. https://www.nature.com/articles/s41598-018-23685-9

# Biotypes: Autism Spectrum Disorder

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: researchers, stakeholders
> **Tags**: `literature-synthesis`, `disease-biotypes`, `asd`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)

Genomic factor loading (Nature 2025): **Neurodevelopmental factor** (ASD + ADHD + Tourette; childhood-onset). ASD anchors this factor alongside ADHD and Tourette syndrome, with the shared signal enriched in genes governing neurodevelopment and broad transcriptional regulation. Per Grotzinger et al., the neurodevelopmental factor also spans into other conditions, consistent with the extensive polygenic overlap between ASD, ADHD, schizophrenia, and educational attainment (Grotzinger et al., Nature 2025, doi:10.1038/s41586-025-09820-3).

## Framing note

Autism is constitutionally heterogeneous, spanning nonspeaking individuals with profound support needs to adults diagnosed in midlife. Decades of attempts to find a single biological signature for "autism" have failed, and current consensus across basic science and the autistic community treats autism as a family of overlapping neurodevelopmental conditions with shared surface behaviours. Stratification, not unification, is the productive direction. We frame biotypes as serving personalized support, accommodation, and (where wanted) targeted treatment of co-occurring conditions, not the elimination of autism itself. We use person-first and identity-first language interchangeably, reflecting genuine community division. Two historically influential frameworks reviewed below, the extreme male brain hypothesis (Baron-Cohen) and the intense world theory (Markram), have drawn substantive critique from autistic researchers for over-extrapolating from limited evidence; we flag these where relevant.

## Seed papers

- Grotzinger AD, Werme M, Peyrot WJ, ... Smoller JW. Mapping the genetic landscape across 14 psychiatric disorders. Nature. 2025. doi:10.1038/s41586-025-09820-3. (Organizing reference; ASD on neurodevelopmental factor.)
- Grove J, Ripke S, Als TD, et al. Identification of common genetic risk variants for autism spectrum disorder. Nat Genet. 2019;51:431-44. doi:10.1038/s41588-019-0344-8. (PGC-ASD GWAS, n=18,381 cases.)
- Velmeshev D, Schirmer L, Jung D, et al. Single-cell genomics identifies cell type-specific molecular changes in autism. Science. 2019;364:685-9. doi:10.1126/science.aav8130.
- Wamsley B, ... Geschwind DH (Sestan/Geschwind groups). Molecular cascades and cell type-specific signatures in ASD revealed by single-cell genomics. Science. 2024;384:eadh2602. doi:10.1126/science.adh2602.
- Rubenstein JLR, Merzenich MM. Model of autism: increased ratio of excitation/inhibition in key neural systems. Genes Brain Behav. 2003;2:255-67. (E/I imbalance founding paper.)
- Zabihi M, Floris DL, Kia SM, et al. Fractionating autism based on neuroanatomical normative modeling. Transl Psychiatry. 2020;10:384. doi:10.1038/s41398-020-01057-0.
- Internal: `research/biotypes-autism.md` (full ASD multi-modal brief, 127 refs); `research/eeg-meg-biotypes.md` (cross-disorder EEG/MEG signal library).

---

## MICRO scale (molecular / genetic / cellular / immune) vs GO-harmonized

E/I imbalance is the central organizing molecular biotype for autism. Rubenstein and Merzenich proposed in 2003 that an elevated cortical excitation-to-inhibition ratio is a core feature of at least a subset of autism; two decades of work support but qualify this, showing the imbalance is region- and circuit-specific (not global) and that different genetic subtypes shift E/I in different directions (Lee 2017; Sohal & Rubenstein 2019). The marked regions below (auditory cortex, sensorimotor cortex, DLPFC) are where E/I dysregulation is most reproducibly reported via convergent GABA, gamma, ASSR, and aperiodic-slope measures.

| Biotype / dysregulation | GO term(s) + ID | Specific finding (genes, variants, molecules) | Neurotransmitter family | BDNF / neurotrophin + plasticity? | E/I imbalance (+ region) | Oxidative / mito / ROS? | Immune / inflammatory? | Confidence | Source |
|---|---|---|---|---|---|---|---|---|---|
| GABAergic (PV/SST) interneuron deficit | GABAergic synaptic transmission (GO:0051932); inhibitory synapse assembly (GO:1904862) | Reduced parvalbumin (PV) interneuron and PV+ chandelier cell counts in prefrontal and multiple cortical areas; reduced somatostatin (SST) density in some samples | **GABA** (reduced inhibitory tone) | none reported (primary) | **I-down**; prefrontal cortex, auditory cortex, broadly cortical | none direct | PV cells vulnerable to oxidative/immune insult (indirect) | HIGH | Hashemi 2017; Ariza 2022; Sohal 2009 |
| Glutamatergic synaptopathy (SHANK1-3) | glutamatergic synaptic transmission (GO:0035249); postsynaptic density (GO:0014069); regulation of synaptic plasticity (GO:0048167) | SHANK3 mutations cause Phelan-McDermid syndrome and a fraction of severe idiopathic ASD; Shank3B-null mice show repetitive grooming, social deficits, enhanced gamma (enhanced inhibitory tone); SHANK2 rat shows striatal mGluR1 hyperactivation | **Glutamate** | none reported (scaffolding, not neurotrophin) | mixed; SHANK3 models show enhanced inhibitory tone cortically | none direct | none direct | HIGH (Mendelian); MEDIUM (idiopathic fraction) | Durand 2007; Shank3B 2017 (doi:10.1186/s13229-017-0142-z); Modi 2018 |
| mTOR / PTEN / TSC1-2 synaptopathy | TOR signaling (GO:0031929); regulation of dendritic spine morphogenesis (GO:0061002); regulation of synaptic plasticity (GO:0048167) | PTEN, TSC1/TSC2, NF1 are negative regulators of PI3K-mTOR; heterozygous mutation produces Mendelian autisms (tuberous sclerosis, NF1, PTEN hamartoma); altered dendritic spine density; pharmacological probes rapamycin/everolimus | **Glutamate** (excitatory synapse overgrowth) | none direct (PI3K-AKT downstream overlaps TrkB) | E/I shift via altered spine density; cortex-wide | none direct | none direct | HIGH (Mendelian) | Sato 2016; Sahin & Sur 2015 (doi:10.1126/science.aab3897) |
| Cell-adhesion (NLGN/NRXN/CNTNAP2) | synapse organization (GO:0050808); synaptic membrane adhesion (GO:0099560) | Neuroligin-neurexin transsynaptic complexes specify E vs I synapses (NLGN1 excitatory, NLGN2 inhibitory); recurrent mutations in NLGN3/4, NRXN1, CNTNAP2; CNTNAP2 knockout shows core domains + cortical migration defects | **Glutamate** + **GABA** (specifies both) | none reported | direct E/I specification defect; cortex-wide | none direct | none direct | HIGH (Mendelian) | Bourgeron synaptic review 2024 (doi:10.31083/j.jin2310184) |
| Mitochondrial / oxidative subtype | response to oxidative stress (GO:0006979); mitochondrial ATP synthesis coupled electron transport (GO:0042775); aerobic respiration (GO:0009060) | Frye-Rossignol mitochondrial subgroup (~5-30% of cases, ~30% prevalence estimate); elevated lactate/pyruvate, ultrastructural mito abnormalities, regression often triggered by inflammation; 2024 meta-analysis confirms reproducible biochemical markers | none direct | none reported | none direct (energetic) | **YES** elevated lactate, ROS, glutathione depletion; muscle/brain | overlaps with immune-triggered regression | MEDIUM | Rossignol & Frye 2012; Frye 2020; Mito meta-analysis 2024 (doi:10.1016/j.mito.2024) |
| Maternal immune activation / microglia | inflammatory response (GO:0006954); microglial cell activation (GO:0001774); cytokine-mediated signaling (GO:0019221) | MIA rodent/NHP models reliably produce ASD-relevant offspring behaviours (cellular replication variable); postmortem + TSPO PET microglial activation in subsets; elevated IL-6, IL-1beta, TNF-alpha, IL-8/CXCL8; candidate immune subtype panel (TNF-alpha, IL-6, CXCL8) | none direct | none reported | microglia shape E/I via synaptic pruning (indirect) | overlaps mito-regressive subtype | **YES** IL-6, IL-1beta, TNF-alpha, IL-8, microglial activation; maternal autoimmunity | MEDIUM (behaviour robust; cellular variable) | Estes & McAllister 2015/2016; Suzuki 2013; cytokine meta Saghazadeh 2021; immune panel 2024 (PMC11432970) |
| BDNF / TrkB plasticity (limited) | neurotrophin TRK receptor signaling (GO:0048011); BDNF receptor signaling; regulation of synaptic plasticity (GO:0048167); positive regulation of LTP (GO:1900273) | Serum BDNF variably elevated/reduced/unchanged (age- and assay-dependent); reduced TrkB-PI3K-AKT1 signaling in idiopathic ASD brain tissue; relevant to psychedelic/ketamine plasticity mechanisms | none direct (modulatory) | **YES** TrkB-PI3K-AKT1 reduced; plasticity-targeted intervention rationale | indirect (BDNF modulates inhibitory maturation) | none direct | none direct | LOW (serum heterogeneous) | Camuso 2022 (doi:10.1038/s41598-022-17503-6); BDNF review 2026 |
| Single-cell convergence (L2/3 neurons, glia) | regulation of gene expression (GO:0010468); synaptic signaling (GO:0099536); gliogenesis (GO:0042063) | snRNA-seq: synaptic genes in upper-layer (L2/3) cortico-cortical projection neurons + microglial activation-state genes correlate with severity; 2024 Science adh2602 implicates interhemispheric/callosal-projecting neurons, superficial interneurons, reactive oligodendrocyte/microglia/astrocyte states; GRN drivers enriched for rare + common risk | **Glutamate** (L2/3 projection) + **GABA** (superficial interneurons) | none direct | converges on E/I + glial dysfunction | reactive glial states | reactive microglia/astrocytes | HIGH (multi-sample convergence) | Velmeshev 2019 (doi:10.1126/science.aav8130); Wamsley/Sestan 2024 (doi:10.1126/science.adh2602) |
| Polygenic + CNV architecture | nervous system development (GO:0007399) | PGC-ASD GWAS (Grove 2019): 5 GW-significant loci, n=18,381 cases; polygenic overlap with ADHD, SCZ, MDD, educational attainment; SFARI >1000 scored genes (Q1 2025: 1136 + 94 candidates); recurrent CNVs 16p11.2 (most frequent de novo), 22q11.2, 15q11-13 (Dup15q), 7q11.23 (dup-del sociability polarity), 17q12 | broad | broad | broad (cell-type expressed) | broad | broad | HIGH | Grove 2019 (doi:10.1038/s41588-019-0344-8); Sanders 2011; SFARI Gene Q1 2025 |

GO IDs marked above are confident anchors except mitochondrial subtype-specific and immune-panel terms (use as approximate, needs curation for exact subterms). E/I imbalance regions to flag explicitly: **auditory cortex** (40 Hz ASSR, language correlation), **sensorimotor cortex** (MRS GABA, tactile discrimination), **DLPFC** (gamma, PV loss).

---

## MESO scale (connectomic) vs Allen Atlas nodes + edges

Allen Human Reference Atlas 3D (2020), 141 anatomical regions. Functional labels in parentheses. Several social-brain functional regions (FFA, TPJ, sgACC equivalents) are not 1:1 Allen anatomical parcels; the containing Allen anatomical structure is given. The cerebellar lobular nomenclature (Crus I/II, lobules VI/VII) is finer than the Allen single "cerebellum" parcels; flagged where finer atlas needed.

### NODES table

| Allen region (functional label) | Observed change | Modality | Confidence | Source |
|---|---|---|---|---|
| Superior temporal sulcus / superior temporal gyrus (STS, social brain hub), right-lateralised | hypoactivation to faces and biological motion | fMRI | HIGH | Hadjikhani 2007; Pelphrey 2003 |
| Fusiform gyrus (fusiform face area / FFA), right ventral temporal | hypoactivation to faces; face processing occurs outside FFA | fMRI | HIGH | Pierce 2001; Hadjikhani 2007 |
| Inferior frontal gyrus, pars opercularis (IFG; mirror neuron/language), right | reduced activation during action/emotion observation | fMRI | MEDIUM | Hadjikhani 2007 (social brain) |
| Amygdala | reduced discrimination social vs nonsocial; reduced social-stimulus activation | fMRI | MEDIUM | Green 2015; Uddin & Menon 2009 |
| Cingulate gyrus, anterior part (mPFC / DMN anterior hub) | atypical age-trajectory; reduced long-range coupling | fMRI | HIGH | Washington 2014; Bethlehem 2020 |
| Inferior parietal lobule, angular gyrus (TPJ / DMN posterior hub) | atypical connectivity; mentalizing alterations | fMRI | MEDIUM | Washington 2014 |
| Posterior cingulate cortex (PCC; DMN core) | cross-study convergent intrinsic connectivity decrease | fMRI | HIGH | Di Martino 2014 (ABIDE); King 2019 |
| Insula, anterior (salience network) | reduced coupling to amygdala/mPFC/STS; altered from infancy | fMRI | MEDIUM-HIGH | Ciarrusta 2024; Uddin & Menon 2009 |
| Insula, mid/posterior | convergent intrinsic connectivity decrease | fMRI | MEDIUM | Di Martino 2014 |
| Transverse temporal gyrus (Heschl's gyrus, auditory cortex), left | reduced 40 Hz ASSR power; correlates with language ability | EEG/MEG | HIGH | ASSR meta 2026 (doi:10.1038/s41380-026-03452-3); medRxiv 2025 |
| Precentral + postcentral gyrus (sensorimotor cortex) | reduced GABA+ tracks tactile discrimination; cortical thickening subtype | MRS/structural | MEDIUM | Puts 2014; Zabihi 2020 |
| Cerebellum, posterior lobe (right Crus I/II; non-Allen finer lobular label) | structural/functional abnormality; reduced grey matter correlates with worse communication | structural/fMRI | MEDIUM-HIGH | D'Mello 2015; Stoodley 2017; Tsai 2012 |
| Cerebellum, lobules VI/VII (vermis VI/VIII; finer than Allen parcel) | increased sensorimotor cerebral coupling, reduced supramodal coupling; reduced grey matter | structural/fMRI | MEDIUM | D'Mello 2015; Hampson 2015 |
| Frontal cortex (broad) | greater cortical thickness (ENIGMA-ASD) | structural | HIGH (group), small d | van Rooij 2018 (ENIGMA) |
| Temporal cortex (broad) | lower cortical thickness; reduced leftward asymmetry | structural | HIGH (group), small d | van Rooij 2018 |
| Thalamus | small/inconsistent hyperconnectivity (subcortical) | fMRI | LOW | Di Martino 2014; King 2019 |
| Locus coeruleus (NE source nucleus) | tonic upregulation linked to auditory information processing | fMRI/pupillometry | MEDIUM (LEAP) | LEAP 2024-25 |

### EDGES table

The long-range under-connectivity / local over-connectivity hypothesis is the principal organizing connectomic frame. Most large studies find reduced long-distance DMN connectivity plus increased local connectivity in childhood; the pattern is age- and method-dependent and partly normalises or inverts in adults under rigorous motion control. ABIDE I/II mega-analyses (>2000 participants) show ASD-related decreases dominate cortico-cortical edges (unimodal association + paralimbic), while subcortical hyperconnectivity is smaller and less consistent.

| Region A vs Region B (functional labels) | Association sign | Observed change in disorder | Modality | Confidence | Source |
|---|---|---|---|---|---|
| mPFC vs posterior cingulate cortex (DMN anterior-posterior, long-range) | positive (normal) | reduced long-range connectivity; attenuated maturation peaking ages 11-13 | fMRI | HIGH | Washington 2014; Di Martino 2014 |
| Posterior cingulate vs angular gyrus/TPJ (DMN long-range) | positive (normal) | reduced long-range connectivity in childhood | fMRI | HIGH | Just 2004; King 2019 |
| Within-DMN node local edges; within visual/motor networks | positive | increased local connectivity (over-connectivity) in childhood | fMRI | MEDIUM | Hull 2017; Di Martino 2014 |
| Anterior insula vs amygdala / mPFC / STS (salience-to-social) | positive (normal) | reduced coupling; salience-to-sensory predicts sensory hypersensitivity | fMRI | MEDIUM-HIGH | Ciarrusta 2024; Uddin & Menon 2009 |
| Within-salience network (anterior insula vs dorsal ACC), infants | positive | enhanced within-salience coupling but reduced salience-to-orbitofrontal in 6-week elevated-likelihood infants | fMRI | MEDIUM | Ciarrusta 2024 |
| STS vs fusiform (FFA) / amygdala (social brain effective connectivity) | positive (normal) | reduced STS modulatory input to FFA/amygdala | fMRI (effective conn.) | MEDIUM | Hadjikhani 2007 |
| Cerebellum (right Crus I/II) vs neocortex (cerebro-cerebellar) | positive (normal) | reduced supramodal coupling; increased sensorimotor coupling; optogenetic Crus I activation rescues behaviour in mice | fMRI / causal mouse | MEDIUM-HIGH | Stoodley 2017; D'Mello 2015 |
| Lobules VI/VII vs sensorimotor vs association cortex | mixed | shift toward sensorimotor and away from supramodal coupling | fMRI | MEDIUM | D'Mello 2015 |

### EEG / MEG biotype rows (cross-cut with eeg-meg-biotypes.md)

| Signal | ASD finding | Direction / region | Confidence | Source |
|---|---|---|---|---|
| Relative alpha power (8-13 Hz) | reduced relative alpha is the single most replicated resting EEG finding | reduced; posterior/global (meta g = -0.35, k=41) | HIGH | eeg-meg-biotypes.md ref 7; Neuhaus 2022 |
| Alpha peak frequency (PAF/IAF) | atypical PAF developmental trajectory; lower PAF tracks lower IQ within ASD | reduced/atypical; occipital | MEDIUM-HIGH | Dickinson 2018; Neuhaus 2022 |
| Aperiodic 1/f slope (E/I proxy) | flatter slopes (relative excitation) in multiple labs; infant slope-change predicts later diagnosis + 18-mo language; task-related steepening in adults differs from neurotypicals | flatter (E/I-up); global; FXS divergent | HIGH (resting, >=5 labs) | Donoghue 2020; Manyukhina 2022; medRxiv 2024/2025 |
| Gamma (30-80 Hz) | reduced induced/phase-locked gamma in perceptual tasks; resting gamma split (elevated in some meta-analyses) | mixed (task reduced; resting split); frontal-posterior | MEDIUM | Sun 2012; Maxwell 2015 |
| 40 Hz ASSR | reduced power/phase-locking; PV-NMDA circuit probe; SHANK3 dup case; testable in young/ID children | reduced; left auditory cortex; correlates language | HIGH | ASSR meta 2026; Sivarao 2016; SHANK3 2021 |
| Mismatch negativity (MMN) | reduced amplitude (children/adolescents, multifeature); transdiagnostic, not ASD-specific | reduced; frontocentral | MEDIUM (less consistent than SCZ) | MMN meta 2025 (doi:10.1002/aur.70131); Lassen 2022 |
| Sleep spindles (11-16 Hz) | reduced frontal/central spindle density; reduced spindle-slow-oscillation coupling; pronounced in Dup15q | reduced; frontal/central (thalamocortical PV) | MEDIUM (smaller literature) | sleep microarch 2023; Lehoux 2019; Dup15q 2021 |
| PPI / P50 gating | mixed; reduced PPI in some adults, often null in well-matched pediatric samples | mixed | LOW | Madsen 2014; Oranje 2013 |

OPM-MEG (wearable optically-pumped magnetometer MEG) is operationally important for pediatric ASD imaging: motion-tolerant, head-size-adaptive, less aversive than cryogenic MEG/MRI, and recovers the same gamma, ASSR, MMN, and aperiodic signatures with cleaner source localization. 2024-25 work pushed OPM-MEG toward newborn and wireless recording (Hill 2024; Boto 2018).

---

## MACRO scale (phenotype) vs SNOMED CT / HPO

SNOMED CT parent concept: Autism spectrum disorder = 35919005 (Autistic disorder of childhood onset 43614003; Infantile autism 408857007; Atypical autism 231536004; parent Pervasive developmental disorder 408856003). HPO parent: Autism HP:0000717; Autistic behavior HP:0000729.

| Biotype phenotype | SNOMED CT term + ID | HPO term + ID | Short description / dimension | Source |
|---|---|---|---|---|
| Social-communication differences (social brain biotype) | Autism spectrum disorder 35919005 | Impaired social interactions HP:0000735; Autistic behavior HP:0000729 | Reduced reciprocal social interaction, gaze, joint attention, pragmatic language; maps to social-brain hypoactivation (STS/FFA/IFG/amygdala) | van Rooij 2018; Hadjikhani 2007; DSM-5 criterion A |
| Restricted / repetitive behaviours (RRBs) | Autism spectrum disorder 35919005 | Restrictive behavior HP:0000753; Stereotypy HP:0000733 | Stereotyped movements, repetitive speech, ritualized patterns; links to striatal mGluR1 (SHANK2), cerebellar circuits | DSM-5 criterion B; Modi 2018 |
| Insistence on sameness / cognitive inflexibility | Autism spectrum disorder 35919005 | Restrictive behavior HP:0000753 (approx, needs curation for sameness subterm) | Distress at change, rigid routines; overlaps compulsive dimension and predictive-coding (weak priors) framing | DSM-5 criterion B; Lawson 2014 |
| Sensory over-/under-responsivity (sensory/EPF biotype) | Sensory processing disorder 23476006 (approx, needs curation) | Abnormal nervous system physiology HP:0012638 (sensory; approx, needs curation) | Hyper-/hyporeactivity to sensory input, sensory seeking; maps to anterior insula, OFC, primary sensory cortices; enhanced perceptual functioning | Green 2015; Mottron 2006; Dunn framework |
| Intellectual disability co-occurrence | Intellectual disability 110359009 | Intellectual disability HP:0001249 | Present in a substantial fraction; co-varies with PAF, aperiodic slope, ASSR, de novo LoF burden | Manyukhina 2022; Satterstrom 2020 |
| Language impairment / regression | Developmental regression 62014002 (approx) | Delayed speech and language development HP:0000750; Developmental regression HP:0002376 | Language correlates with left-auditory ASSR; ~25-30% show 15-30 mo regression (trajectory variant, not categorical) | Ozonoff 2018; ASSR language medRxiv 2025 |
| Co-occurring anxiety / internalizing | Anxiety disorder 197480006 | Anxiety HP:0000739 | Elevated lifespan anxiety/depression; prominent in masked/female-phenotype and adult-diagnosed presentations | Lai 2017; lifespan cohorts |

Person-first/identity-first language used per community preference; biotypes framed for personalized support, not cure.

---

## Interventional studies (incl. neuromodulation, DBS, neuroplastogens)

| Biotype it targets | Intervention (class + specific) | Study (author year, design, n) | Outcome | Confidence | Source |
|---|---|---|---|---|---|
| Irritability / aggression (transdiagnostic, partly immune-stratified) | Atypical antipsychotic: risperidone, aripiprazole (only two FDA-approved ASD drugs) | Multiple RCTs; BAART biomarker study NCT01333072 | Moderate reduction in irritability; weight gain/metabolic side effects common; IL-5 + cytokine markers differ responder vs non-responder | HIGH (efficacy for irritability); MEDIUM (immune stratifier) | RCTs (Psychopharm Institute review); BAART NCT01333072 |
| Repetitive behaviours / comorbid anxiety (serotonergic) | SSRI: citalopram, fluoxetine | STAART citalopram (King 2009, RCT, pediatric); fluoxetine adult RCT (Hollander 2012); meta 2024 | No group benefit for RRB in children; modest in some adults; insufficient for core symptoms, supports comorbid anxiety/depression use | MEDIUM (mixed; responder subgroup unidentified) | King 2009; Hollander 2012; SSRI review 2025 (PMC11990048) |
| Social-communication (oxytocin-vasopressin) | Intranasal oxytocin | SOARS-B (Sikich 2021, RCT, n=277, 24 wk) | **No significant primary/secondary benefit; no subgroup effect** | HIGH (null) | Sikich 2021 NEJM (doi:10.1056/NEJMoa2103583) |
| Social-communication (vasopressin V1a) | Balovaptan, V1a receptor antagonist | VANILLA phase 2 (Bolognani 2019, promising Vineland-II) -> **V1aduct phase 3 FAILED**; Roche discontinued ASD programme | **Phase 3 failure; no consistent responder biotype on post-hoc** | HIGH (failure flagged) | Bolognani 2019; balovaptan program review 2022 (doi:10.1186/s13229-022-00505-6) |
| mTOR / TSC synaptopathy biotype | mTOR inhibitor: everolimus (rapamycin analog) | Overwater 2019 (RCT, n=32, ages 4-17, TSC, 12 mo) | **No significant benefit on full-scale IQ, autism behaviours, neuropsych outcomes** despite strong preclinical rationale (timing/critical-period hypothesis) | HIGH (null flagged) | Overwater 2019 Neurology (doi:10.1212/WNL.0000000000007749) |
| Mitochondrial / regressive subtype | Mitochondrial cocktails; (exploratory) microbiota transfer therapy | MTT open-label (Kang 2017/2019, n=18 + 2-yr follow-up) | ~47% symptom reduction, sustained GI improvement; **open-label, needs placebo-controlled replication** | LOW (uncontrolled) | Kang 2017/2019 (doi:10.1186/s40168-016-0225-7) |
| Developmental/social engagement (behavioural) | Early Intensive Behavioral Intervention (EIBI); Early Start Denver Model (naturalistic developmental) | Reichow 2018 Cochrane; ESDM vs EIBI predictors 2022 | Large gains in some children; higher intake IQ, younger age, early joint attention predict response; community critiques of compliance-focused ABA | MEDIUM-HIGH (responder-stratified) | Reichow 2018 (PMC6494600); Brain Sci 2022 |
| PV / E-I, social, DLPFC circuits | rTMS: low-freq right DLPFC (RRB/irritability), high-freq left DLPFC (social); bilateral protocols | Open-label + small RCTs; bilateral protocol improved eye fixation/core scores; large sham-controlled pediatric RCTs now running | Modest effects; evidence limited | LOW-MEDIUM | rTMS protocol 2025 (doi:10.1186/s13063-025-08946-z); JMIR 2026 |
| Serotonergic function (experimental) | Psilocybin (neuroplastogen) | PSILAUT experimental-medicine study (KCL/Compass, completed Aug 2024, low-dose probe); preclinical sociability rescue | **Not an efficacy trial**; mechanism probe only; full-dose adult ASD trials absent; sensory/anxiety risk noted | LOW (very early) | PSILAUT 2024 (PMC11044362); preclinical 2020 |
| Severe refractory self-injurious behaviour | Deep brain stimulation (DBS): basolateral amygdala, NAc/ALIC, GPi (rare case reports) | Individual case reports/small series in profound ASD with intractable self-injury | Partial reduction of self-injury in some cases; not population-level; ethically scrutinized | LOW (rare cases) | DBS case literature (self-injury) |

---

## Most defensible biotypes (cross-scale synthesis)

Six biotypes integrate convergently across at least two scales and link to specific Allen anchor regions for an adaptive multi-modal coordinate space.

**Biotype A. PV interneuron / E-I imbalance / gamma-ASSR.** The central molecular biotype. MICRO: reduced PV/SST interneuron counts, reduced GABA tone, SHANK3/NLGN E/I specification defects. MESO: reduced 40 Hz ASSR (left transverse temporal gyrus / Heschl's), flatter aperiodic 1/f slope (global), reduced task gamma, MRS GABA reductions in sensorimotor cortex. Anchor regions: **transverse temporal gyrus (auditory cortex), precentral/postcentral gyrus (sensorimotor), DLPFC.** Bridges to schizophrenia via shared PV biology. Confidence HIGH.

**Biotype B. Social brain hypoactivation.** MESO: reduced activation and effective connectivity across the social network; reduced gaze on eye-tracking. MACRO: social-communication differences (HP:0000735). Anchor regions: **right superior temporal sulcus/gyrus, fusiform gyrus (FFA), right inferior frontal gyrus, amygdala, angular gyrus (TPJ), anterior cingulate (mPFC).** Confidence HIGH.

**Biotype C. Cerebellar-cortical.** MESO + causal mouse: right Crus I/II and lobules VI/VII structural/functional abnormality; Purkinje-cell Tsc1 deletion produces ASD behaviours; optogenetic Crus I activation rescues. Anchor regions: **cerebellum posterior lobe (right Crus I/II), lobules VI/VII, cerebello-thalamo-cortical loop.** Confidence MEDIUM-HIGH.

**Biotype D. Sensory perception / enhanced perceptual functioning (EPF).** MICRO/MESO: posterior cortical hyperactivity on perceptual tasks, sensory over-responsivity amygdala-OFC signatures, salience-network alterations from infancy, sensory-subtype cortical thickening. MACRO: sensory over/under-responsivity. Anchor regions: **primary visual, somatosensory, auditory cortices; anterior insula; orbitofrontal cortex.** EPF is well-supported and reframes perceptual differences as features; distinct from the critiqued intense-world theory. Confidence MEDIUM-HIGH.

**Biotype E. mTOR / synaptopathy (molecular Mendelian).** MICRO: causal genes (PTEN, TSC1/2, SHANK3, NLGN3/4, NRXN1, CNTNAP2, FMR1, MECP2) with distinctive EEG signatures (Fragile X aperiodic/alpha; SHANK3 ASSR) and partial preclinical reversibility. Note the everolimus phase-3 null in TSC and balovaptan/oxytocin failures: molecular tractability has not yet translated to cognitive/social efficacy, likely from critical-period timing and pathway redundancy. Anchor: cortex-wide with gene-specific patterns. Confidence HIGH (genetics); LOW (therapeutic translation).

**Biotype F. DMN / developmental trajectory.** MESO: long-range DMN under-connectivity with local over-connectivity in childhood (age- and method-dependent), atypical DMN maturation, Bethlehem-Lombardo normative deviation subtypes, reduced sleep spindle density. Anchor regions: **anterior cingulate (mPFC), posterior cingulate cortex, angular gyrus (TPJ).** Confidence HIGH (childhood); MEDIUM (adult inversion).

Recommended headset anchor additions beyond the existing eight Cytognosis regions: right STS, fusiform/FFA, right inferior frontal gyrus, right cerebellar Crus I/II.

**Genomic factor:** Autism loads on the **neurodevelopmental factor** (with ADHD and Tourette) in Grotzinger et al., Nature 2025.

---

## References

1. Grotzinger AD, Werme M, Peyrot WJ, ... Smoller JW. Mapping the genetic landscape across 14 psychiatric disorders. Nature. 2025. doi:10.1038/s41586-025-09820-3
2. Rubenstein JLR, Merzenich MM. Model of autism: increased ratio of excitation/inhibition in key neural systems. Genes Brain Behav. 2003;2:255-67.
3. Lee E, Lee J, Kim E. Excitation/inhibition imbalance in animal models of autism spectrum disorders. Biol Psychiatry. 2017;81:838-47. https://doi.org/10.1016/j.biopsych.2016.05.011
4. Sohal VS, Rubenstein JLR. Excitation-inhibition balance as a framework for investigating mechanisms in neuropsychiatric disorders. Mol Psychiatry. 2019;24:1248-57.
5. Hashemi E, Ariza J, Rogers H, Noctor SC, Martinez-Cerdeno V. The number of parvalbumin-expressing interneurons is decreased in the prefrontal cortex in autism. Cereb Cortex. 2017;27:1931-43.
6. Ariza J, et al. Parvalbumin and parvalbumin chandelier interneurons in autism and other psychiatric disorders. Front Mol Neurosci. 2022. https://pmc.ncbi.nlm.nih.gov/articles/PMC9597886/
7. Sohal VS, Zhang F, Yizhar O, Deisseroth K. Parvalbumin neurons and gamma rhythms enhance cortical circuit performance. Nature. 2009;459:698-702.
8. Durand CM, et al. Mutations in SHANK3 are associated with autism spectrum disorders. Nat Genet. 2007;39:25-7.
9. Replicable in vivo physiological and behavioral phenotypes of the Shank3B null mutant mouse. Mol Autism. 2017. https://doi.org/10.1186/s13229-017-0142-z
10. Modi B, et al. Hyperactivity and hypermotivation associated with increased striatal mGluR1 signaling in a Shank2 rat model. Front Behav Neurosci. 2018. https://pmc.ncbi.nlm.nih.gov/articles/PMC6018399/
11. Sato A, et al. mTOR, a potential target to treat autism spectrum disorder. CNS Neurol Disord Drug Targets. 2016. https://pmc.ncbi.nlm.nih.gov/articles/PMC5070418/
12. Sahin M, Sur M. Genes, circuits, and precision therapies for autism. Science. 2015;350:aab3897. https://doi.org/10.1126/science.aab3897
13. Key synaptic pathology in autism: genetic mechanisms and recent advances. J Integr Neurosci. 2024. https://doi.org/10.31083/j.jin2310184
14. Rossignol DA, Frye RE. Mitochondrial dysfunction in autism: a systematic review and meta-analysis. Mol Psychiatry. 2012;17:290-314.
15. Frye RE. Mitochondrial dysfunction in autism: unique abnormalities and targeted treatments. Semin Pediatr Neurol. 2020;35:100829.
16. Biomarkers of mitochondrial dysfunction in autism: a systematic review and meta-analysis. Mitochondrion. 2024. https://www.sciencedirect.com/science/article/pii/S1569997224001190
17. Estes ML, McAllister AK. Maternal immune activation: implications for neuropsychiatric disorders. Science. 2016;353:772-7.
18. Estes ML, McAllister AK. Immune mediators in the brain and peripheral tissues in autism. Nat Rev Neurosci. 2015;16:469-86.
19. Suzuki K, et al. Microglial activation in young adults with autism. JAMA Psychiatry. 2013;70:49-58.
20. Saghazadeh A, et al. Association of peripheral cytokines with autism: a meta-analysis. Front Psychiatry. 2021. https://www.frontiersin.org/journals/psychiatry/articles/10.3389/fpsyt.2021.670200/full
21. Immunological biomarkers in autism: TNF-alpha and IL-6/CXCL8 trends. 2024. https://pmc.ncbi.nlm.nih.gov/articles/PMC11432970/
22. Camuso S, et al. BDNF, proBDNF and IGF-1 serum levels in autism. Sci Rep. 2022;12:13658. https://doi.org/10.1038/s41598-022-17503-6
23. Decoding BDNF in neurodevelopmental, neurodegenerative, and neurological disorders. Mol Biol Rep. 2026. https://doi.org/10.1007/s11033-026-11485-8
24. Velmeshev D, Schirmer L, Jung D, et al. Single-cell genomics identifies cell type-specific molecular changes in autism. Science. 2019;364:685-9. https://doi.org/10.1126/science.aav8130
25. Wamsley B, et al. Molecular cascades and cell type-specific signatures in ASD revealed by single-cell genomics. Science. 2024;384:eadh2602. https://doi.org/10.1126/science.adh2602
26. Grove J, Ripke S, Als TD, et al. Identification of common genetic risk variants for autism. Nat Genet. 2019;51:431-44. https://doi.org/10.1038/s41588-019-0344-8
27. Sanders SJ, et al. Multiple recurrent de novo CNVs, including 7q11.23 duplications, are strongly associated with autism. Neuron. 2011;70:863-85.
28. Satterstrom FK, et al. Large-scale exome sequencing implicates developmental and functional changes in autism. Cell. 2020;180:568-84.
29. SFARI Gene scoring module. gene.sfari.org (Q1 2025 release: 1136 scored genes, 94 candidates).
30. Hadjikhani N, Joseph RM, Snyder J, Tager-Flusberg H. Abnormal activation of the social brain during face perception in autism. Hum Brain Mapp. 2007;28:441-9.
31. Pierce K, Muller RA, Ambrose J, Allen G, Courchesne E. Face processing occurs outside the fusiform 'face area' in autism. Brain. 2001;124:2059-73.
32. Pelphrey KA, et al. Brain activation evoked by perception of gaze shifts. Neuropsychologia. 2003;41:156-70.
33. Green SA, Hernandez L, Tottenham N, et al. Neurobiology of sensory overresponsivity in youth with autism. JAMA Psychiatry. 2015;72:778-86.
34. Uddin LQ, Menon V. The anterior insula in autism: under-connected and under-examined. Neurosci Biobehav Rev. 2009;33:1198-203.
35. Washington SD, et al. Dysmaturation of the default mode network in autism. Hum Brain Mapp. 2014;35:1284-96.
36. Just MA, Cherkassky VL, Keller TA, Minshew NJ. Cortical activation and synchronization during sentence comprehension in high-functioning autism: underconnectivity. Brain. 2004;127:1811-21.
37. Di Martino A, Yan CG, Li Q, et al. The autism brain imaging data exchange (ABIDE). Mol Psychiatry. 2014;19:659-67.
38. King JB, Prigge MBD, et al. Generalizability and reproducibility of functional connectivity in autism. Mol Autism. 2019;10:27.
39. Hull JV, et al. Resting-state functional connectivity in autism: a review. Front Psychiatry. 2017;7:205.
40. Ciarrusta J, et al. Salience network connectivity is altered in 6-week-old infants at heightened likelihood for autism. Commun Biol. 2024. https://www.nature.com/articles/s42003-024-06016-9
41. Tsai PT, Hull C, Chu Y, et al. Autistic-like behaviour and cerebellar dysfunction in Purkinje cell Tsc1 mutant mice. Nature. 2012;488:647-51. https://doi.org/10.1038/nature11310
42. Stoodley CJ, D'Mello AM, et al. Altered cerebellar connectivity in autism and cerebellar-mediated rescue. Nat Neurosci. 2017;20:1744-51. https://doi.org/10.1038/s41593-017-0004-1
43. D'Mello AM, Crocetti D, Mostofsky SH, Stoodley CJ. Cerebellar gray matter and lobular volumes correlate with core autism symptoms. Neuroimage Clin. 2015;7:631-9.
44. Hampson DR, Blatt GJ. Autism spectrum disorders and neuropathology of the cerebellum. Front Neurosci. 2015;9:420.
45. van Rooij D, Anagnostou E, Arango C, et al. Cortical and subcortical morphometry differences in autism: ENIGMA ASD. Am J Psychiatry. 2018;175:359-69.
46. Zabihi M, Floris DL, Kia SM, et al. Fractionating autism based on neuroanatomical normative modeling. Transl Psychiatry. 2020;10:384. https://doi.org/10.1038/s41398-020-01057-0
47. Bethlehem RAI, et al. A normative modelling approach reveals age-atypical cortical thickness in autism. Commun Biol. 2020;3:486.
48. Mottron L, Dawson M, Soulieres I, et al. Enhanced perceptual functioning in autism: eight principles. J Autism Dev Disord. 2006;36:27-43.
49. Samson F, Mottron L, et al. Enhanced visual functioning in autism: an ALE meta-analysis. Hum Brain Mapp. 2012;33:1553-81.
50. Lawson RP, Rees G, Friston KJ. An aberrant precision account of autism. Front Hum Neurosci. 2014;8:302.
51. Dickinson A, DiStefano C, Senturk D, Jeste SS. Peak alpha frequency is a neural marker of cognitive function across the autism spectrum. Eur J Neurosci. 2018;47:643-51.
52. Neuhaus E, et al. Resting state EEG power spectrum and functional connectivity in autism. Mol Autism. 2022;13:33.
53. Donoghue T, Haller M, et al. Parameterizing neural power spectra into periodic and aperiodic components. Nat Neurosci. 2020;23:1655-65.
54. Manyukhina VO, et al. Globally elevated excitation-inhibition ratio in children with autism and below-average intelligence. Mol Autism. 2022;13:20. https://molecularautism.biomedcentral.com/articles/10.1186/s13229-022-00498-2
55. Task-related aperiodic EEG (1/f) activity in autism. medRxiv. 2025. https://www.medrxiv.org/content/10.1101/2025.10.16.25338172v1.full
56. Change in aperiodic activity over first year of life is associated with later autism diagnosis. medRxiv. 2024. https://www.medrxiv.org/content/10.1101/2024.12.15.24319061v1.full
57. Sun L, et al. Impaired gamma-band activity during perceptual organization in adults with autism. J Neurosci. 2012;32:9563-73.
58. Maxwell CR, et al. Atypical laterality of resting gamma oscillations in autism. J Autism Dev Disord. 2015.
59. Sivarao DV, et al. 40 Hz auditory steady-state response is a pharmacodynamic biomarker for cortical NMDA receptors. Neuropsychopharmacology. 2016;41:2232-40.
60. Systematic review and meta-analysis of the auditory steady-state response in schizophrenia, bipolar disorder, and ASD. Mol Psychiatry. 2026. https://www.nature.com/articles/s41380-026-03452-3
61. Auditory sustained potential as a biomarker of language functioning in autism. medRxiv. 2025. https://www.medrxiv.org/content/10.1101/2025.10.22.25338568v1.full
62. SHANK3 partial duplication 40 Hz ASSR case report. Int J Mol Sci. 2021;22:1898. https://www.mdpi.com/1422-0067/22/4/1898
63. Systematic review and meta-analysis of mismatch negativity in autism. Autism Res. 2025. https://onlinelibrary.wiley.com/doi/10.1002/aur.70131
64. Lassen J, et al. Reduced MMN in children/adolescents with autism is associated with impaired adaptive functioning. Autism Res. 2022.
65. Identification of atypical sleep microarchitecture biomarkers in children with autism. Front Psychiatry. 2023.
66. Lehoux T, et al. NREM sleep EEG slow waves in autistic and typically developing children. Sleep Med. 2019;52:90-7.
67. Abnormal sleep physiology in children with 15q11.2-13.1 duplication (Dup15q) syndrome. 2021. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8336244/
68. Madsen GF, et al. Prepulse inhibition of the acoustic startle reflex in high functioning autism. PLoS One. 2014;9:e92372.
69. Oranje B, et al. Sensory and sensorimotor gating in children with MCDD and autism. Psychiatry Res. 2013;206:177-82.
70. Hill RM, et al. A robust, portable platform for MEG using optically-pumped magnetometers. Imaging Neurosci. 2024. https://direct.mit.edu/imag/article/doi/10.1162/imag_a_00283/124093/
71. Boto E, et al. Moving magnetoencephalography towards real-world applications with a wearable system. Nature. 2018;555:657-61.
72. Puts NAJ, Wodka EL, Tommerdahl M, Mostofsky SH, Edden RAE. Impaired tactile processing in children with autism. J Neurophysiol. 2014;111:1803-11.
73. Sikich L, Kolevzon A, King BH, et al. Intranasal oxytocin in children and adolescents with autism. N Engl J Med. 2021;385:1462-73. https://doi.org/10.1056/NEJMoa2103583
74. Bolognani F, et al. A phase 2 trial of a vasopressin V1a receptor antagonist (balovaptan) shows improved adaptive behaviors in men with autism. Sci Transl Med. 2019;11:eaat7838.
75. Large multicenter randomized trials in autism: insights from the balovaptan clinical development program. Mol Autism. 2022. https://doi.org/10.1186/s13229-022-00505-6
76. Overwater IE, et al. A randomized controlled trial with everolimus for IQ and autism in tuberous sclerosis complex. Neurology. 2019;93:e200-9. https://doi.org/10.1212/WNL.0000000000007749
77. King BH, Hollander E, Sikich L, et al. Lack of efficacy of citalopram in children with autism and high repetitive behavior. Arch Gen Psychiatry. 2009;66:583-90.
78. Hollander E, et al. Fluoxetine for repetitive behaviors and global severity in adult autism. Am J Psychiatry. 2012;169:292-9.
79. Selective serotonin reuptake inhibitors (SSRIs) for autism spectrum disorders. 2025. https://pmc.ncbi.nlm.nih.gov/articles/PMC11990048/
80. Biomarkers in Autism of Aripiprazole and Risperidone Treatment (BAART). ClinicalTrials.gov NCT01333072.
81. Kang DW, Adams JB, et al. Microbiota transfer therapy alters gut ecosystem and improves GI and autism symptoms: open-label study. Microbiome. 2017;5:10. https://doi.org/10.1186/s40168-016-0225-7
82. Kang DW, et al. Long-term benefit of microbiota transfer therapy on autism symptoms and gut microbiota. Sci Rep. 2019;9:5821.
83. Reichow B, et al. Early intensive behavioral intervention (EIBI) for young children with autism. Cochrane Database Syst Rev. 2018;5:CD009260.
84. Differential predictors of response to ESDM vs EIBI in young children with autism. Brain Sci. 2022. https://www.mdpi.com/2076-3425/12/11/1499
85. rTMS in children and adolescents with autism: study protocol for a sham-controlled RCT. Trials. 2025. https://doi.org/10.1186/s13063-025-08946-z
86. rTMS combined with auditory integration training for children with autism. JMIR Res Protoc. 2026. https://www.researchprotocols.org/2026/1/e80243
87. The PSILAUT protocol: experimental medicine study of autistic differences in brain serotonin targets of psilocybin. 2024. https://pmc.ncbi.nlm.nih.gov/articles/PMC11044362/
88. Ozonoff S, et al. Onset patterns in autism: variation across informants, methods, and timing. Autism Res. 2018;11:788-97.
89. Lai MC, Lombardo MV, et al. Quantifying and exploring camouflaging in men and women with autism. Autism. 2017;21:690-702.
90. Baron-Cohen S. The extreme male brain theory of autism. Trends Cogn Sci. 2002;6:248-54. (Critiqued; see amniotic testosterone systematic review, Front Neuroendocrinol 2020.)
91. SNOMED CT International Edition: Autism spectrum disorder 35919005; Autistic disorder of childhood onset 43614003; Infantile autism 408857007; Atypical autism 231536004; Pervasive developmental disorder 408856003.
92. Human Phenotype Ontology: Autism HP:0000717; Autistic behavior HP:0000729; Restrictive behavior HP:0000753; Stereotypy HP:0000733; Impaired social interactions HP:0000735.

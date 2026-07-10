# Biotypes: ADHD (attention-deficit/hyperactivity disorder)

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: researchers, stakeholders
> **Tags**: `literature-synthesis`, `disease-biotypes`, `adhd`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)

Genomic factor loading (Nature 2025): **Neurodevelopmental factor** (ASD + ADHD + Tourette; childhood-onset). ADHD is a defining member of this factor, which spans into other disorders and is enriched for genes expressed in early brain development.

ADHD is a heritable neurodevelopmental disorder of inattention, hyperactivity, and impulsivity. The genetics point firmly toward catecholamine biology and early neural development, the connectomics point toward weak fronto-striatal control circuits and intrusive default-mode activity during tasks, and the structural data point toward delayed maturation rather than fixed lesion. This document harmonizes molecular findings to Gene Ontology (GO), connectomic findings to the Allen Human Reference Atlas 3D (2020), and phenotypes to SNOMED CT and the Human Phenotype Ontology (HPO). We flag two contested markers explicitly: the theta-beta ratio (TBR) and theta-beta neurofeedback.

## Seed papers

- Grotzinger AD, Werme J, Peyrot WJ, ... Smoller JW. Mapping the genetic landscape across 14 psychiatric disorders. Nature. 2025. doi:10.1038/s41586-025-09820-3. (Organizing reference; places ADHD on the neurodevelopmental factor.)
- Demontis D, Walters GB, Rajagopal VM, ... Borglum AD. Genome-wide analyses of ADHD identify 27 risk loci, refine the genetic architecture, and implicate several cognitive domains. Nat Genet. 2023;55(2):198-208. doi:10.1038/s41588-022-01285-8. (PGC-ADHD GWAS; 38,691 cases, 186,843 controls; 27 loci; midbrain dopaminergic and early-development enrichment.)
- Hoogman M, Muetzel R, Guimaraes JP, ... Franke B. Brain imaging of the cortex in ADHD: a coordinated analysis of large-scale clinical and population-based samples. Am J Psychiatry. 2019;176(7):531-542. doi:10.1176/appi.ajp.2019.18091033. (ENIGMA-ADHD cortex; lower surface area in children, frontal/cingulate/temporal.)
- Hoogman M, Bralten J, Hibar DP, ... Franke B. Subcortical brain volume differences in participants with ADHD in children and adults: a cross-sectional mega-analysis. Lancet Psychiatry. 2017;4(4):310-319. doi:10.1016/S2215-0366(17)30049-4. (ENIGMA-ADHD subcortical; smaller accumbens, amygdala, caudate, hippocampus, putamen, ICV; delayed maturation.)
- Sonuga-Barke EJS, Castellanos FX. Spontaneous attentional fluctuations in impaired states and pathological conditions: a neurobiological hypothesis. Neurosci Biobehav Rev. 2007;31(7):977-986. doi:10.1016/j.neubiorev.2007.02.005. (Default-mode interference hypothesis.)

## MICRO scale (molecular / genetic / cellular / immune) vs GO-harmonized

ADHD is highly heritable. Twin studies converge on a heritability near 0.74 [1,2]. The PGC-ADHD GWAS (Demontis et al. 2023) identified 27 genome-wide significant loci across 38,691 cases and 186,843 controls, with SNP heritability near 0.14 and a strongly polygenic architecture in which roughly 7,000 common variants explain about 90% of SNP heritability [2]. Gene-set and partitioned-heritability analyses implicated genes expressed in early brain development and, notably, midbrain dopaminergic neurons, which gives the dopamine hypothesis a genome-wide anchor that the older candidate-gene era lacked [2]. The Nature 2025 cross-disorder factor analysis places ADHD on the neurodevelopmental factor and confirms that shared signal across the 14 disorders is enriched for broad transcriptional regulation, while factor-specific pathways are narrower [3].

The catecholamine hypothesis remains the central molecular framework. Stimulant efficacy (methylphenidate blocks the dopamine transporter; amphetamine reverses it and promotes release) and atomoxetine efficacy (selective norepinephrine reuptake inhibition, with downstream prefrontal dopamine elevation because the cortex clears dopamine partly via the NE transporter) both implicate dopamine and norepinephrine in prefrontal-striatal circuits [4,5]. Candidate-gene work on SLC6A3 (DAT1) and DRD4 is among the most-replicated in psychiatric genetics, though individual effect sizes are small and pharmacogenetic prediction is weak [6,7].

| Biotype / dysregulation | GO term(s) + ID | Specific finding | Neurotransmitter family | BDNF / neurotrophin + plasticity | E/I imbalance (+ region) | Oxidative / mito / ROS | Immune / inflammatory | Confidence | Source |
|---|---|---|---|---|---|---|---|---|---|
| Dopaminergic dysregulation (CENTRAL) | dopamine transport (GO:0015872); dopamine receptor signaling pathway (GO:0007212); dopamine metabolic process (GO:0042417) | SLC6A3/DAT1 3'UTR VNTR (10-repeat) association; DRD4 exon-3 48-bp VNTR 7-repeat allele (stronger in combined type); GWAS enrichment in midbrain dopaminergic neurons; methylphenidate blocks DAT, amphetamine reverses it | **Dopamine** | not primary; indirect | not the primary E/I story | not primary | none reported | HIGH (mechanism), MEDIUM (specific genes) | Demontis 2023 [2]; Gizer 2009 [6]; Smith 2010 [7] |
| Noradrenergic / prefrontal NE | norepinephrine transport (GO:0015874); adrenergic receptor signaling pathway (GO:0071875) | Atomoxetine inhibits NET (SLC6A2), raising prefrontal NE and DA; guanfacine/clonidine are alpha-2A agonists strengthening prefrontal network connections (Arnsten model) | **Norepinephrine** | not primary | NE tunes prefrontal signal-to-noise; not classic E/I | none reported | none reported | HIGH (mechanism) | Bymaster 2002 [5]; Arnsten 2011 [8] |
| Catecholamine hypothesis (integrated) | catecholamine biosynthetic process (GO:0042423); response to amphetamine (GO:0001975) | Low tonic / dysregulated phasic catecholamine signaling in prefrontal-striatal circuits; converging pharmacology of all first-line agents | **Dopamine; Norepinephrine** | not primary | prefrontal tuning, not interneuron E/I | not primary | none reported | HIGH (framework) | Del Campo 2011 [9] |
| Glutamatergic signaling | glutamate receptor signaling pathway (GO:0007215); glutamatergic synaptic transmission (GO:0035249) | GWAS and rare-variant work implicate glutamate-receptor and synaptic genes (e.g., GRM, metabotropic glutamate networks; CDH13, FOXP2 among loci); MRS shows altered frontostriatal glutamate/Glx in some samples | **Glutamate** | possible (synaptic genes) | possible cortical glutamatergic alteration; direction unsettled | not primary | none reported | MEDIUM | Demontis 2023 [2]; Naaijen 2017 [10] |
| BDNF / neurotrophin and plasticity | neurotrophin TRK receptor signaling (GO:0048011); regulation of synaptic plasticity (GO:0048167); positive regulation of long-term synaptic potentiation (GO:1900273) | BDNF Val66Met (rs6265) studied in ADHD with inconsistent association; neurodevelopmental factor enriched for early-development and synaptic genes; relevance to delayed cortical maturation | none reported (neurotrophin axis) | YES; BDNF signaling tied to cortical maturation timing; plasticity relevant to delayed-maturation model | not primary | not primary | none reported | LOW (specific gene), MEDIUM (developmental relevance) | Demontis 2023 [2]; Bobinska 2017 [11] |
| Mild immune / inflammatory (secondary) | inflammatory response (GO:0006954); microglial cell activation (GO:0001774) | Meta-analyses report modestly elevated peripheral cytokines (IL-6, TNF-alpha) and weak associations with maternal immune activation and atopy/allergy; signal is small and likely non-specific | none reported | not primary | not primary | not primary | YES (weak, likely non-specific) | LOW | Leffa 2018 [12]; Dunn 2019 [13] |
| Early-development / cell-type program | nervous system development (GO:0007399); neuron differentiation (GO:0030182) | PGC-ADHD genes enriched in early brain development; consistent with a maturational-timing rather than fixed-lesion model | none reported | partial overlap with neurotrophin axis | not primary | not primary | none reported | MEDIUM | Demontis 2023 [2] |

GO IDs above are drawn from standard GO term names. The neurotransmitter mapping is deliberate: dopamine is marked CENTRAL, norepinephrine is the second clearly implicated family (and the primary target of the leading non-stimulants), glutamate is a plausible third, while GABA and serotonin are not core to ADHD molecular biology. The immune row is included for completeness but rated LOW and flagged as likely non-specific.

## MESO scale (connectomic) vs Allen Atlas nodes + edges

The dominant circuit model is prefrontal-striatal, now extended to include cerebellum and parietal attention systems [14]. Two functional themes recur: (1) weak fronto-striatal cognitive control, with the right inferior frontal gyrus as the canonical response-inhibition hub, and (2) intrusive default-mode network (DMN) activity during tasks, the "default-mode interference" account, in which the normal anticorrelation between DMN and task-positive networks weakens or fails [15,16]. Structurally, ENIGMA-ADHD frames the disorder as delayed maturation: smaller subcortical volumes and lower cortical surface area in children that normalize by adulthood [17,18].

Functional labels are mapped to their containing Allen anatomical structures. Where a network (DMN, frontoparietal attention) has no single Allen parcel, we note the network in parentheses and anchor it to representative Allen regions.

### NODES

| Allen region (functional label) | Observed change | Modality | Confidence | Source |
|---|---|---|---|---|
| Frontal lobe, middle frontal gyrus (DLPFC) | hypoactivation during executive/working-memory tasks; lower surface area in children | fMRI; structural | HIGH | Hart 2013 [19]; Hoogman 2019 [18] |
| Frontal lobe, inferior frontal gyrus, pars opercularis/triangularis (right IFG, response-inhibition hub) | hypoactivation during go/no-go and stop-signal; reduced within-network coupling | fMRI | HIGH | Hart 2013 [19]; Aron 2014 [20] |
| Frontal lobe, orbital/medial frontal gyrus (vmPFC / OFC, reward valuation) | altered activation to reward and delay; relevant to delay aversion | fMRI | MEDIUM | Plichta 2014 [21] |
| Cingulate gyrus, anterior part (dACC, conflict/performance monitoring) | hypoactivation during attention/interference tasks | fMRI | MEDIUM-HIGH | Hart 2013 [19] |
| Caudate nucleus (dorsal striatum) | smaller volume in children (d approx -0.13); hypoactivation during inhibition/timing | structural; fMRI | HIGH (volume) | Hoogman 2017 [17] |
| Putamen (dorsal striatum) | smaller volume in children (d approx -0.18) | structural | HIGH | Hoogman 2017 [17] |
| Nucleus accumbens (ventral striatum, reward) | smaller volume in children (d approx -0.19, largest subcortical effect) | structural | HIGH | Hoogman 2017 [17] |
| Amygdala | smaller volume in children (d approx -0.18) | structural | MEDIUM-HIGH | Hoogman 2017 [17] |
| Hippocampus | smaller volume in children (d approx -0.12) | structural | MEDIUM | Hoogman 2017 [17] |
| Cerebellum, vermis (posterior-inferior lobules) | reduced volume; one of the most consistent cerebellar findings | structural | MEDIUM-HIGH | Stoodley 2016 [22] |
| Parietal lobe, superior/inferior parietal lobule (dorsal attention network) | hypoactivation during attention reorienting and sustained attention | fMRI | MEDIUM | Cortese 2012 [23] |
| Precuneus / posterior cingulate (DMN core hub) | failure to deactivate during tasks; intrusive activity | fMRI | MEDIUM-HIGH | Sonuga-Barke 2007 [15]; Cortese 2012 [23] |
| Cortex (whole, surface area) | lower total surface area in children (d approx -0.21); fusiform/temporal-pole thinning | structural | HIGH | Hoogman 2019 [18] |

### EDGES

| Region A vs Region B (functional labels) | Association sign | Observed change in ADHD | Modality | Confidence | Source |
|---|---|---|---|---|---|
| Inferior frontal gyrus / DLPFC (frontal control) vs caudate/putamen (dorsal striatum): **fronto-striatal control loop** | positive (normally coupled) | reduced fronto-striatal functional and structural connectivity; the core ADHD circuit deficit | fMRI; DTI | HIGH | Hart 2013 [19]; Castellanos 2012 [24] |
| Precuneus/PCC (DMN) vs DLPFC/dorsal attention regions (task-positive network) | negative (anticorrelation) | anticorrelation reduced or failing; DMN intrudes during tasks (default-mode interference) | fMRI | MEDIUM-HIGH | Sonuga-Barke 2007 [15]; Sun 2021 [16] |
| DMN nodes (precuneus/PCC) vs task-relevant control regions (right IFG) | positive | increased DMN-to-task-network integration correlates with worse response control / higher ADHD severity | fMRI | MEDIUM | Sun 2021 [16] |
| Inferior frontal gyrus / DLPFC vs superior/inferior parietal lobule: **fronto-parietal attention network** | positive | reduced coupling within the fronto-parietal/dorsal attention system | fMRI | MEDIUM | Cortese 2012 [23] |
| Prefrontal cortex vs cerebellum (vermis/posterior lobes): fronto-cerebellar timing loop | positive | reduced fronto-cerebellar connectivity; relevant to timing and prediction deficits | fMRI; structural | MEDIUM | Stoodley 2016 [22] |
| Ventral striatum (NAc) vs vmPFC/OFC: reward-valuation loop | positive | altered coupling tied to delay aversion and reward hyposensitivity | fMRI | MEDIUM | Plichta 2014 [21] |

### EEG / MEG markers

ADHD has a long electrophysiological literature, and honesty about replication is essential here.

- **Theta-beta ratio (TBR).** TBR was the centerpiece of ADHD EEG research and the basis for FDA clearance of the Neuropsychiatric EEG-Based Assessment Aid (NEBA) in 2013, on Monastra et al.'s claim of a 1.3 to 1.5-fold elevation in ADHD versus controls [25,26]. Subsequent multi-site work and the American Academy of Neurology practice advisory (Gloss et al. 2016) concluded the evidence is insufficient for diagnostic use, and a 2026 multiverse analysis (Liechti and colleagues, medRxiv) showed the effect is highly sensitive to analytic choices and has shrunk substantially in better-controlled samples [27,28]. We treat TBR as a non-specific marker of cortical arousal, **not** as a validated ADHD biomarker. Confidence in TBR as a diagnostic marker: LOW (failed rigorous replication).
- **Aperiodic (1/f) slope.** Flatter aperiodic slopes have been reported in children and adults with ADHD, consistent with an arousal/E-I interpretation, but the strongest cross-condition aperiodic signal is in autism, not ADHD [29]. Confidence: LOW-MEDIUM.
- **P300 (P3b).** Reduced P300 amplitude during attention and oddball tasks is reported but smaller and less specific than in addiction or schizophrenia [30]. Confidence: MEDIUM (non-specific).
- **CNV / preparatory activity.** Reduced contingent negative variation and weaker preparatory/orienting potentials index deficient response preparation and timing [31]. Confidence: MEDIUM.

The EEG story is best read as supporting a general arousal-regulation and preparatory-control deficit rather than supplying a clean diagnostic marker. The structural MRI story (ENIGMA delayed maturation) and the fMRI circuit story (fronto-striatal weakness plus DMN intrusion) are far more defensible than any single EEG metric.

## MACRO scale (phenotype) vs SNOMED CT / HPO

ADHD presents along three core symptom dimensions (inattention, hyperactivity, impulsivity) that combine into DSM-5 presentations: predominantly inattentive, predominantly hyperactive-impulsive, and combined. These presentations are unstable over development (children frequently shift from combined to inattentive), which is one reason imaging/biology-based biotyping is being pursued as an alternative to symptom-count subtyping.

| Biotype phenotype | SNOMED CT term + ID | HPO term + ID | Short description of observations that led to this mapping | Source |
|---|---|---|---|---|
| ADHD, combined presentation | Attention deficit hyperactivity disorder (406506008); Combined type ADHD (192133008, approx, needs curation) | Attention deficit hyperactivity disorder (HP:0007018) | Co-occurring inattention plus hyperactivity-impulsivity; most studied; strongest DRD4 7-repeat association | DSM-5; Smith 2010 [7] |
| ADHD, predominantly inattentive | Attention deficit hyperactivity disorder, predominantly inattentive type (192132003, approx, needs curation) | Short attention span (HP:0000736); Attention deficit hyperactivity disorder (HP:0007018) | Distractibility, poor sustained attention, organizational difficulty without prominent motor overactivity; ties to DMN-intrusion and fronto-parietal attention findings | DSM-5; Cortese 2012 [23] |
| ADHD, predominantly hyperactive-impulsive | Attention deficit hyperactivity disorder, predominantly hyperactive-impulsive type (approx, needs curation) | Hyperactivity (HP:0000752) | Motor overactivity, fidgeting, restlessness; more common in younger children | DSM-5 |
| Impulsivity / response-inhibition deficit | Impulsivity (29164008, approx, needs curation) | Impulsivity (HP:0100710) | Poor stop-signal and go/no-go performance; maps to right-IFG and fronto-striatal hypoactivation | Aron 2014 [20] |
| Inattention dimension | Attention concentration difficulty (60032008, approx, needs curation) | Short attention span (HP:0000736) | Lapses of sustained attention; maps to DMN interference and fronto-parietal underconnectivity | Sonuga-Barke 2007 [15] |
| Hyperactivity dimension | Hyperactive behavior (38717003, approx, needs curation) | Hyperactivity (HP:0000752) | Motor restlessness; maps partly to striatal and cerebellar findings | DSM-5 |
| Delay aversion / reward hyposensitivity | (no precise SNOMED concept; approx, needs curation) | Impulsivity (HP:0100710) | Preference for immediate over delayed reward, steep temporal discounting; maps to NAc-vmPFC reward loop | Plichta 2014 [21] |

SNOMED concept IDs marked "approx, needs curation" require verification against a current SNOMED CT release; the root ADHD concept (406506008) and the HPO terms are reliable. We deliberately do not invent precise IDs for the presentation subtypes.

## Interventional studies (incl. neuromodulation, DBS, neuroplastogens)

First-line treatment is pharmacological and targets catecholamines. Neuromodulation evidence is weaker and, for several modalities, contested. We flag those honestly.

| Biotype it targets | Intervention (class + specific) | Study (author year, design, n) | Outcome | Confidence | Source |
|---|---|---|---|---|---|
| Dopaminergic / fronto-striatal control | Stimulant: methylphenidate (DAT blockade) | MTA Cooperative Group 1999 (RCT, n=579); decades of replication | Large symptom reduction; effect sizes among the largest in psychiatry (SMD approx 0.8-1.0) | HIGH | MTA 1999 [32] |
| Dopaminergic + noradrenergic | Stimulant: amphetamine (DAT reversal, catecholamine release) | Network meta-analysis Cortese et al. 2018 (Lancet Psychiatry) | Amphetamines most efficacious in adults; methylphenidate first-line in children | HIGH | Cortese 2018 [33] |
| Noradrenergic (prefrontal NE) | Non-stimulant: atomoxetine (NET inhibition) | Multiple RCTs; Cortese 2018 meta-analysis | Moderate efficacy (smaller than stimulants); useful where stimulants contraindicated | HIGH | Cortese 2018 [33]; Bymaster 2002 [5] |
| Prefrontal network strengthening (alpha-2A) | Alpha-2 agonist: guanfacine ER, clonidine ER | RCTs; Arnsten mechanistic model | Moderate efficacy as monotherapy/adjunct; strengthens prefrontal connectivity | HIGH (efficacy), MEDIUM (mechanism) | Arnsten 2011 [8]; Cortese 2018 [33] |
| Fronto-striatal control (right IFG / DLPFC) | tDCS: anodal left DLPFC (often + cognitive training) | Westwood & Rubia meta-analysis 2021; Westwood RCT 2023 (double-blind, sham) | Trend-level gains in inhibition/processing speed; little clinical-symptom benefit; **mixed evidence** | LOW-MEDIUM | Westwood 2021 [34]; Westwood 2023 [35] |
| Prefrontal hypoactivation | rTMS: prefrontal targets | Small RCTs; systematic reviews | Inconsistent; insufficient evidence for clinical use | LOW | Westwood 2021 [34] |
| Arousal/theta regulation (TBR) | Neurofeedback: theta downtraining / beta uptraining | Arnold et al. 2021 double-blind 2-site RCT (n=144), 13- and 25-month follow-up | Blinded improvements **not** attributable to deliberate TBR change; equal to sham on the targeted mechanism; **efficacy contested** | LOW (mechanism refuted) | Arnold 2021 [36]; Sonuga-Barke 2013 [37] |
| Trigeminal-nerve / brainstem arousal pathway | eTNS: Monarch external trigeminal nerve stimulator (FDA-cleared, ages 7-12) | McGough et al. 2019 (double-blind sham RCT, n=62, 4 weeks) | Reduced ADHD-RS symptoms vs sham, Cohen's d approx 0.5 (similar to non-stimulants); FDA de novo clearance Apr 2019; mild AEs | MEDIUM | McGough 2019 [38] |
| Severe/refractory ADHD circuits | DBS | No established ADHD indication | Not trialed as a primary ADHD treatment; impulsivity changes observed incidentally in OCD/movement-disorder DBS | LOW (no ADHD evidence) | vs |
| Reward / plasticity | Neuroplastogens (ketamine, psilocybin) | No controlled ADHD trials | Not an evidence-based ADHD treatment; included only to note absence of data | LOW (no evidence) | vs |

The interventional evidence reinforces the molecular picture: every first-line agent acts on dopamine and/or norepinephrine, and effect sizes are largest for the dopaminergic stimulants. Among device therapies, eTNS (Monarch) is the one with a positive sham-controlled pediatric RCT and FDA clearance, making it the most defensible neuromodulation option, while tDCS is mixed and theta-beta neurofeedback's targeted mechanism failed under blinding.

## Most defensible biotypes (cross-scale synthesis)

1. **Fronto-striatal control deficit (the core ADHD biotype).** Anchor Allen nodes: inferior frontal gyrus (right IFG), middle frontal gyrus (DLPFC), caudate, putamen. Anchor edge: IFG/DLPFC vs caudate/putamen, positive coupling that is reduced (the canonical ADHD circuit). Micro: dopaminergic, stimulant-responsive. Macro: impulsivity, response-inhibition failure. Confidence: HIGH.

2. **Default-mode interference biotype.** Anchor Allen nodes: precuneus/posterior cingulate (DMN), DLPFC and parietal task-positive regions. Anchor edge: precuneus/PCC vs DLPFC/dorsal attention regions, normally negative (anticorrelation), reduced or failing so DMN intrudes during tasks. Macro: inattention, lapses. Confidence: MEDIUM-HIGH.

3. **Delayed-maturation structural biotype.** Anchor Allen nodes: nucleus accumbens, caudate, putamen, amygdala (smaller in children, largest at NAc), plus reduced total cortical surface area. The ENIGMA case-control differences are present in children and absent in adults, supporting a maturational-timing rather than fixed-lesion model. Confidence: HIGH.

4. **Reward / delay-aversion biotype.** Anchor Allen nodes: nucleus accumbens (ventral striatum), vmPFC/OFC. Anchor edge: NAc vs vmPFC, positive reward-valuation loop, altered. Macro: delay aversion, steep temporal discounting, reward hyposensitivity. Confidence: MEDIUM.

5. **Fronto-cerebellar timing biotype.** Anchor Allen nodes: prefrontal cortex, cerebellar vermis. Anchor edge: prefrontal vs cerebellum, positive, reduced. Macro: timing deficits, variable reaction time. Confidence: MEDIUM.

Genomic factor: ADHD loads on the **neurodevelopmental factor** (with ASD and Tourette) in the Nature 2025 cross-disorder analysis, consistent with its GWAS enrichment in early brain development and midbrain dopaminergic neurons.

## References

[1] Faraone SV, Larsson H. Genetics of attention deficit hyperactivity disorder. Mol Psychiatry. 2019;24(4):562-575. doi:10.1038/s41380-018-0070-0

[2] Demontis D, Walters GB, Rajagopal VM, et al. Genome-wide analyses of ADHD identify 27 risk loci, refine the genetic architecture, and implicate several cognitive domains. Nat Genet. 2023;55(2):198-208. doi:10.1038/s41588-022-01285-8

[3] Grotzinger AD, Werme J, Peyrot WJ, et al. Mapping the genetic landscape across 14 psychiatric disorders. Nature. 2025. doi:10.1038/s41586-025-09820-3

[4] Volkow ND, Wang GJ, Kollins SH, et al. Evaluating dopamine reward pathway in ADHD: clinical implications. JAMA. 2009;302(10):1084-1091. doi:10.1001/jama.2009.1308

[5] Bymaster FP, Katner JS, Nelson DL, et al. Atomoxetine increases extracellular levels of norepinephrine and dopamine in prefrontal cortex of rat. Neuropsychopharmacology. 2002;27(5):699-711. doi:10.1016/S0893-133X(02)00346-9

[6] Gizer IR, Ficks C, Waldman ID. Candidate gene studies of ADHD: a meta-analytic review. Hum Genet. 2009;126(1):51-90. doi:10.1007/s00439-009-0694-x

[7] Smith AK, et al. Meta-analysis of the heterogeneity in association of DRD4 7-repeat allele and AD/HD: stronger association with AD/HD combined type. Am J Med Genet B. 2010;153B(6):1189-1199. doi:10.1002/ajmg.b.31090

[8] Arnsten AFT. Catecholamine influences on dorsolateral prefrontal cortical networks. Biol Psychiatry. 2011;69(12):e89-e99. doi:10.1016/j.biopsych.2011.01.027

[9] Del Campo N, Chamberlain SR, Sahakian BJ, Robbins TW. The roles of dopamine and noradrenaline in the pathophysiology and treatment of ADHD. Biol Psychiatry. 2011;69(12):e145-e157. doi:10.1016/j.biopsych.2011.02.036

[10] Naaijen J, Lythgoe DJ, Amiri H, Buitelaar JK, Glennon JC. Fronto-striatal glutamatergic compounds in compulsive and impulsive syndromes: a review of magnetic resonance spectroscopy studies. Neurosci Biobehav Rev. 2015;52:74-88. doi:10.1016/j.neubiorev.2015.02.009

[11] Bobinska K, Galecka E, et al. Brain-derived neurotrophic factor and neuroplasticity in ADHD: a review. (Representative review.) 2017.

[12] Leffa DT, Torres ILS, Rohde LA. A review on the role of inflammation in attention-deficit/hyperactivity disorder. Neuroimmunomodulation. 2018;25(5-6):328-333. doi:10.1159/000489635

[13] Dunn GA, Nigg JT, Sullivan EL. Neuroinflammation as a risk factor for attention deficit hyperactivity disorder. Pharmacol Biochem Behav. 2019;182:22-34. doi:10.1016/j.pbb.2019.05.005

[14] Bu X, Xia M, Cui Z, He Y. Toward individual heterogeneity and neurobiological subtypes in attention-deficit/hyperactivity disorder. Sage / journal of psychiatry research. 2025. doi:10.1177/18344909241308101

[15] Sonuga-Barke EJS, Castellanos FX. Spontaneous attentional fluctuations in impaired states and pathological conditions: a neurobiological hypothesis. Neurosci Biobehav Rev. 2007;31(7):977-986. doi:10.1016/j.neubiorev.2007.02.005

[16] Sun H, et al. Increased integration between default mode and task-relevant networks in children with ADHD is associated with impaired response control. Dev Cogn Neurosci. 2021;49:100959. doi:10.1016/j.dcn.2021.100959

[17] Hoogman M, Bralten J, Hibar DP, et al. Subcortical brain volume differences in participants with ADHD in children and adults: a cross-sectional mega-analysis. Lancet Psychiatry. 2017;4(4):310-319. doi:10.1016/S2215-0366(17)30049-4

[18] Hoogman M, Muetzel R, Guimaraes JP, et al. Brain imaging of the cortex in ADHD: a coordinated analysis of large-scale clinical and population-based samples. Am J Psychiatry. 2019;176(7):531-542. doi:10.1176/appi.ajp.2019.18091033

[19] Hart H, Radua J, Nakao T, Mataix-Cols D, Rubia K. Meta-analysis of functional magnetic resonance imaging studies of inhibition and attention in ADHD. JAMA Psychiatry. 2013;70(2):185-198. doi:10.1001/jamapsychiatry.2013.277

[20] Aron AR, Robbins TW, Poldrack RA. Inhibition and the right inferior frontal cortex: one decade on. Trends Cogn Sci. 2014;18(4):177-185. doi:10.1016/j.tics.2013.12.003

[21] Plichta MM, Scheres A. Ventral-striatal responsiveness during reward anticipation in ADHD and its relation to trait impulsivity in the healthy population: a meta-analytic review. Neurosci Biobehav Rev. 2014;38:125-134. doi:10.1016/j.neubiorev.2013.07.012

[22] Stoodley CJ. The cerebellum and neurodevelopmental disorders. Cerebellum. 2016;15(1):34-37. doi:10.1007/s12311-015-0715-3

[23] Cortese S, Kelly C, Chabernaud C, et al. Toward systems neuroscience of ADHD: a meta-analysis of 55 fMRI studies. Am J Psychiatry. 2012;169(10):1038-1055. doi:10.1176/appi.ajp.2012.11101521

[24] Castellanos FX, Proal E. Large-scale brain systems in ADHD: beyond the prefrontal-striatal model. Trends Cogn Sci. 2012;16(1):17-26. doi:10.1016/j.tics.2011.11.007

[25] Monastra VJ, Lubar JF, Linden M. The development of a quantitative electroencephalographic scanning process for ADHD. Neuropsychology. 2001;15(1):136-144. doi:10.1037/0894-4105.15.1.136

[26] US FDA. NEBA System 510(k) De Novo clearance. 2013. https://www.fda.gov

[27] Gloss D, Varma JK, Pringsheim T, Nuwer MR. Practice advisory: the utility of EEG theta/beta power ratio in ADHD diagnosis. Neurology. 2016;87(22):2375-2379. doi:10.1212/WNL.0000000000003265

[28] Liechti M, et al. Theta-beta ratio in attention deficit hyperactivity disorder: a multiverse analysis. medRxiv. 2026. https://www.medrxiv.org/content/10.64898/2026.01.08.26343676

[29] Ostlund BD, et al. Aperiodic EEG activity in ADHD across the lifespan: flatter 1/f slopes in children and adults. (Representative report of flatter aperiodic slope in ADHD.) 2021.

[30] Johnstone SJ, Barry RJ, Clarke AR. Ten years on: a follow-up review of ERP research in ADHD. Clin Neurophysiol. 2013;124(4):644-657. doi:10.1016/j.clinph.2012.09.006

[31] Banaschewski T, Brandeis D. Annotation: what electrical brain activity tells us about brain function in ADHD. J Child Psychol Psychiatry. 2007;48(5):415-435. doi:10.1111/j.1469-7610.2006.01681.x

[32] MTA Cooperative Group. A 14-month randomized clinical trial of treatment strategies for ADHD. Arch Gen Psychiatry. 1999;56(12):1073-1086. doi:10.1001/archpsyc.56.12.1073

[33] Cortese S, Adamo N, Del Giovane C, et al. Comparative efficacy and tolerability of medications for ADHD in children, adolescents, and adults: a systematic review and network meta-analysis. Lancet Psychiatry. 2018;5(9):727-738. doi:10.1016/S2215-0366(18)30269-4

[34] Westwood SJ, Radua J, Rubia K. Noninvasive brain stimulation in children and adults with ADHD: a systematic review and meta-analysis. J Psychiatry Neurosci. 2021;46(1):E14-E33. doi:10.1503/jpn.190179

[35] Westwood SJ, Criaud M, Lam SL, et al. Transcranial direct current stimulation (tDCS) combined with cognitive training in adolescent boys with ADHD: a double-blind, randomised, sham-controlled trial. Psychol Med. 2023;53(2):497-512. doi:10.1017/S0033291721001859

[36] Arnold LE, Arns M, Barterian J, et al. Double-blind placebo-controlled randomized clinical trial of neurofeedback for ADHD with 13-month follow-up. J Am Acad Child Adolesc Psychiatry. 2021;60(7):841-855. doi:10.1016/j.jaac.2020.07.906

[37] Sonuga-Barke EJS, Brandeis D, Cortese S, et al. Nonpharmacological interventions for ADHD: systematic review and meta-analyses of randomized controlled trials of dietary and psychological treatments. Am J Psychiatry. 2013;170(3):275-289. doi:10.1176/appi.ajp.2012.12070991

[38] McGough JJ, Sturm A, Cowen J, et al. Double-blind, sham-controlled, pilot study of trigeminal nerve stimulation for ADHD. J Am Acad Child Adolesc Psychiatry. 2019;58(4):403-411. doi:10.1016/j.jaac.2018.11.013

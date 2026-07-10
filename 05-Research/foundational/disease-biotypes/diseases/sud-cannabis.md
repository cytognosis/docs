# Biotypes: Cannabis Use Disorder (CUD)

Genomic factor loading (Nature 2025): **Substance use factor** (alcohol + opioid + nicotine + cannabis use disorders), the cross-disorder genetic axis shared across the four substance use disorders. Cannabis use disorder is the smallest and most weakly powered loader on this factor, and the cannabis biotype literature is correspondingly the thinnest of any substance use disorder covered in this set. Where the alcohol and opioid docs can anchor biotypes in PET dopamine, structural ENIGMA mega-analyses, and treatment-stratified imaging, the cannabis evidence base is dominated by single-lab or single-cohort findings, mixed replication, and a near-total absence of approved pharmacotherapy to provide treatment-response validation. This document states that limitation throughout (Grotzinger et al., Nature 2025, doi:10.1038/s41586-025-09820-3).

This document harmonizes cannabis use disorder biotype evidence across three scales: MICRO (molecular/genetic/cellular/immune, mapped to Gene Ontology), MESO (connectomic fMRI/EEG/MEG, mapped to the Allen Human Reference Atlas 3D 2020), and MACRO (phenotype, mapped to SNOMED CT and HPO). It reuses findings from the parent substance use disorder review (biotypes-addiction.md) and updates them with 2023 to 2026 literature. The defining and best-replicated molecular feature of CUD is exogenous overdrive and adaptive downregulation of the endocannabinoid (eCB) system, which I mark explicitly as a distinct neuromodulatory system alongside the classical neurotransmitter families.

---

## Seed papers

- Levey DF, Galimberti M, Deak JD, et al. Multi-ancestry genome-wide association study of cannabis use disorder yields insight into disease biology and public health implications. Nat Genet. 2023;55:2094-2103. doi:10.1038/s41588-023-01563-z (Million Veteran Program, 22 loci, CHRNA2-schizophrenia colocalization)
- Johnson EC, Demontis D, Thorgeirsson TE, et al. A large-scale genome-wide association study meta-analysis of cannabis use disorder. Lancet Psychiatry. 2020;7:1032-1045. doi:10.1016/S2215-0366(20)30339-4 (PGC + iPSYCH + deCODE; CADM2, FOXP2; schizophrenia genetic correlation)
- Grotzinger AD, Werme J, Peyrot WJ, et al. Mapping the genetic landscape across 14 psychiatric disorders. Nature. 2025. doi:10.1038/s41586-025-09820-3
- Hirvonen J, Goodwin RS, Li CT, et al. Reversible and regionally selective downregulation of brain cannabinoid CB1 receptors in chronic daily cannabis smokers. Mol Psychiatry. 2012;17:642-649. doi:10.1038/mp.2011.82 (CB1 PET downregulation, reverses with abstinence)
- Boileau I, Mansouri E, Williams B, et al. Fatty acid amide hydrolase binding in brain of cannabis users: imaging with [11C]CURB PET. Biol Psychiatry. 2016;80:691-701. doi:10.1016/j.biopsych.2016.04.012 (FAAH downregulation)
- Freeman TP, Hindocha C, Baio G, et al. Cannabidiol for the treatment of cannabis use disorder: a phase 2a, double-blind, placebo-controlled, randomised, adaptive Bayesian trial. Lancet Psychiatry. 2020;7:865-874. doi:10.1016/S2215-0366(20)30290-X
- D'Souza DC, Cortes-Briones J, Creatura G, et al. Efficacy and safety of a fatty acid amide hydrolase inhibitor (PF-04457845) in the treatment of cannabis withdrawal and dependence in men: a phase 2a RCT. Lancet Psychiatry. 2019;6:35-45. doi:10.1016/S2215-0366(18)30427-9
- Hatoum AS, Colbert SMC, Johnson EC, et al. Multivariate GWAS of over 1 million subjects identifies loci underlying multiple substance use disorders. Nat Ment Health. 2023;1:210-223. doi:10.1038/s44220-023-00034-y (general addiction factor, PDE4B)

---

## MICRO scale (molecular / genetic / cellular / immune) vs GO-harmonized

Each neurotransmitter family is marked individually, and the **endocannabinoid (eCB) system** is marked as a separate neuromodulatory system because it is the mechanistic spine of CUD biology and is not one of the five classical transmitter families. The recurring molecular logic is: chronic exogenous THC (a partial CB1/CB2 agonist) drives sustained CB1 activation, which produces adaptive CB1 receptor downregulation and desensitization (most marked in neocortex) and altered tone of the endogenous ligands anandamide (AEA) and 2-arachidonoylglycerol (2-AG). Because CB1 sits presynaptically and gates glutamate, GABA, and dopamine release, eCB adaptation propagates into blunted striatal dopamine signaling (the reward/amotivational pole) and into glutamate/GABA imbalance. The genetics are dominated by CADM2 and FOXP2 (Johnson 2020) and CHRNA2 (Levey 2023), with a robust positive genetic correlation to schizophrenia that is the single most important transdiagnostic genetic signal for this disorder.

| Biotype / dysregulation | GO term(s) + ID | Specific finding (genes, variants, molecules) | Neurotransmitter family / system | BDNF / neurotrophin + plasticity? | E/I imbalance (+ region) | Oxidative / mito / ROS? | Immune / inflammatory? | Confidence | Source (author year, DOI) |
|---|---|---|---|---|---|---|---|---|---|
| CB1 receptor downregulation / desensitization (eCB) | G protein-coupled receptor signaling pathway GO:0007186; cannabinoid receptor activity (approx, needs curation; relates to G protein-coupled receptor activity GO:0004930); retrograde trans-synaptic signaling by endocannabinoid GO:0098921 | [18F]FMPEP-d2 PET: ~20% lower cortical CB1 density in chronic daily smokers; correlates with years of use; reverses after ~4 weeks monitored abstinence; regionally selective to neocortex | **Endocannabinoid system (CB1 / CNR1)**; gates Glutamate, GABA, Dopamine release | CB1 supports retrograde plasticity and LTD; downregulation impairs eCB-LTD | CB1 loss disinhibits and dysregulates E/I at glutamatergic and GABAergic terminals; cortical | no | no | HIGH (PET, reversible, replicated direction) | Hirvonen 2012 doi:10.1038/mp.2011.82; D'Souza 2016 (PMC) |
| FAAH downregulation and altered AEA/2-AG tone (eCB) | fatty acid amide catabolic process GO:0052651 (approx, needs curation); long-chain fatty-acyl-CoA metabolic process (related); arachidonic acid metabolic process GO:0019369 | [11C]CURB PET: FAAH binding ~14-20% lower in chronic users, negatively correlated with blood/urine THC-COOH; abstinent CUD shows 31-40% higher circulating AEA, OEA, DHEA; baseline 2-AG inversely tracks use frequency | **Endocannabinoid system (FAAH; AEA, 2-AG, OEA)** | AEA/2-AG are activity-dependent retrograde messengers; tonic-vs-phasic shift | indirect (eCB tone modulates synaptic gain) | no | no | MEDIUM (small samples; suggestive, not a clinical biomarker) | Boileau 2016 doi:10.1016/j.biopsych.2016.04.012; Cuttler 2023 (PMC10605789) |
| Blunted striatal dopamine signaling (reward/amotivational) | dopamine receptor signaling pathway GO:0007212; regulation of dopamine secretion GO:0014059 | PET: reduced striatal dopamine synthesis capacity and blunted stimulant-induced DA release in chronic heavy users; smaller effect than stimulant/alcohol SUD; anchors the reward-deficit / amotivational pattern | **Dopamine** (downstream of eCB) | not central | downstream of CB1 modulation of midbrain DA | no | no | MEDIUM (PET, smaller and more variable than other SUDs) | parent doc; Bloomfield 2016 Nature review doi:10.1038/nature21369 |
| Glutamatergic dysregulation (NAC target) | glutamate receptor signaling pathway GO:0007215; glutamate secretion GO:0014047; cystine-glutamate antiporter activity (approx, needs curation) | NAC restores cystine-glutamate exchange and glutamate homeostasis in addiction models; 1H-MRS shows altered prefrontal/striatal glutamate in chronic users (mixed); rationale for NAC trials | **Glutamate** | none direct | candidate E/I shift, prefrontal/striatal (under-characterized) | NAC also acts via glutathione/antioxidant pathway | partial (NAC antioxidant action) | LOW-MEDIUM (mechanistic; clinical NAC signal weak, see interventions) | Gray 2012 doi:10.1176/appi.ajp.2012.12010055; MRS literature (mixed) |
| GABAergic modulation via CB1 on interneurons | GABAergic synaptic transmission GO:0051932; retrograde endocannabinoid signaling GO:0098921 | CB1 is densely expressed on CCK+ GABAergic interneuron terminals; chronic THC alters depolarization-induced suppression of inhibition (DSI); contributes to cortical/hippocampal E/I change | **GABA** (CB1-gated) | none direct | candidate I-down via altered DSI; hippocampus, cortex | no | no | LOW-MEDIUM (mostly preclinical) | Katona & Freund 2012 (review); preclinical |
| Common-variant polygenic risk (substance use factor) | regulation of trans-synaptic signaling GO:0099177; nervous system development GO:0007399 | Johnson 2020: CADM2 (synaptic cell adhesion) and FOXP2 (transcription factor, neurodevelopment/speech) lead loci; Levey 2023 MVP: 22 loci incl. CHRNA2; substance use factor (Grotzinger 2025) | **mixed / synaptic, neurodevelopmental** | synaptic adhesion (CADM2) | broad synaptic genes | no | no | HIGH (large multi-ancestry GWAS) | Johnson 2020 doi:10.1016/S2215-0366(20)30339-4; Levey 2023 doi:10.1038/s41588-023-01563-z |
| Cannabis-schizophrenia genetic overlap (psychosis risk) | regulation of dopamine secretion GO:0014059; cholinergic receptor signaling (CHRNA2; GO:0007271 synaptic transmission, cholinergic) | Positive genetic correlation CUD-schizophrenia (rg ~0.3-0.5); CHRNA2 variant colocalizes and is shared in local genetic correlation (Levey 2023); MR supports causal influence of schizophrenia liability on cannabis use | **Dopamine, Acetylcholine (CHRNA2)** | none direct | psychosis-relevant cortical/striatal | no | no | HIGH (genetic correlation); MEDIUM (causal direction) | Johnson 2020; Levey 2023; Pasman 2018 doi:10.1038/s41593-018-0206-1 |
| General addiction polygenic factor | response to drug GO:0042493; cyclic-nucleotide phosphodiesterase activity (PDE4B; GO:0004114) | Hatoum 2023: 19-locus addiction-rf across alcohol/tobacco/cannabis/opioid; PDE4B significant cross-ancestry; DRD2, FTO gene-based hits | **Dopamine (DRD2)**; cAMP signaling (PDE4B) | none direct | none direct | no | no | HIGH (>1M subjects) | Hatoum 2023 doi:10.1038/s44220-023-00034-y |
| Neuroinflammation (uncertain / weak) | inflammatory response GO:0006954; microglial cell activation GO:0001774 | TSPO-PET and cytokine signals in CUD are sparse and inconsistent; cannabinoids are often anti-inflammatory; no robust CUD neuroinflammatory biotype | none (immune-glial) | none | none | no | weak / inconsistent | LOW (no robust signal) | parent doc (negative/uncertain) |

Notes on GO IDs: "retrograde trans-synaptic signaling by endocannabinoid" maps to GO:0098921 (confirmed against AmiGO as retrograde trans-synaptic signaling by endocannabinoid). GO:0007186 (GPCR signaling), GO:0007212 (dopamine receptor signaling), GO:0007215 (glutamate receptor signaling), GO:0051932 (GABAergic synaptic transmission), GO:0006954 (inflammatory response), GO:0001774 (microglial activation), GO:0099177 (regulation of trans-synaptic signaling) are confirmed. The cannabinoid-receptor-activity and FAAH-catabolic terms are flagged approx, needs curation pending direct ontology lookup. Unlike alcohol (neuroinflammation) or methamphetamine (TSPO microglial activation), CUD has no defensible immune biotype, and many cannabinoids are anti-inflammatory; this column is deliberately near-empty.

---

## MESO scale (connectomic) vs Allen Atlas nodes + edges

Functional labels are given in parentheses after the containing Allen Human Reference Atlas 3D (2020) anatomical structure. CUD imaging is the least consistent of the substance use disorders: structural findings (especially hippocampal volume) replicate poorly across cohorts, and reward-task fMRI is split between blunted and intact ventral striatal responses. The most reproducible meso-scale features are CB1-density-weighted regional involvement (hippocampus, cerebellum, neocortex are highest-CB1) and altered fronto-striatal connectivity, rather than any single robust activation finding. I flag mixed replication explicitly per row.

### NODES

| Allen region (functional label) | Observed change | Modality | Confidence | Source |
|---|---|---|---|---|
| Caudate nucleus and putamen, accumbens (ventral striatum / nucleus accumbens, NAc) | Blunted reward-anticipation response in some cohorts (general anhedonia correlate); other cohorts show intact or increased response | fMRI (MID) | LOW-MEDIUM (mixed; the amotivational pattern is not robustly supported) | Martz 2016 (PMC4972653); Skumlien 2023 review (Front Behav Neurosci) |
| Orbital gyri (orbitofrontal cortex, OFC / BA11) | Reduced gray matter / altered reward valuation; cue reactivity | structural / fMRI | LOW-MEDIUM | ENIGMA-Addiction (Mackey 2019); cue-reactivity meta-analyses |
| Gyrus rectus / medial orbital (ventromedial prefrontal cortex, vmPFC) | Altered valuation and drug-cue reactivity | fMRI | LOW-MEDIUM | cue-reactivity literature |
| Middle frontal gyrus / superior frontal gyrus (dorsolateral prefrontal cortex, dlPFC / BA9, BA46) | Reduced activation during inhibitory control / working memory; rTMS target | fMRI | MEDIUM | Kober 2014; rTMS trial rationale (Sahlem 2023) |
| Cingulate gyrus, anterior part (anterior cingulate cortex, ACC / BA24, BA32) | Altered conflict-monitoring and error activation; cue reactivity | fMRI / EEG | MEDIUM | cue-reactivity and iRISA literature |
| Amygdala | Heightened reactivity to threat/negative cues in withdrawal; altered cue reactivity | fMRI | LOW-MEDIUM | withdrawal/negative-affect literature |
| Hippocampal formation (hippocampus; very high CB1 density) | Volume reduction reported but inconsistent across cohorts; parahippocampal atrophy in some heavy/early-onset users; memory-circuit relevance | structural / fMRI | LOW (inconsistent replication, flagged in parent doc) | Yucel 2008; Lorenzetti 2019 review; ENIGMA mixed |
| Cerebellar hemisphere and vermis (cerebellum; very high CB1 density) | Altered structure/function; high CB1 makes it a candidate node; coordination and timing | structural / fMRI | LOW-MEDIUM | CB1-distribution literature; imaging (sparse) |
| Precuneus / posterior cingulate gyrus (posterior DMN hub) | Altered DMN connectivity and DMN-salience switching (more consistent than structural findings) | fMRI | MEDIUM | parent doc; Zhang & Volkow 2019 DMN review |

### EDGES

| Region A vs Region B (functional labels) | Association sign | Observed change in disorder | Modality | Confidence | Source |
|---|---|---|---|---|---|
| Ventral striatum / NAc vs orbitofrontal/vmPFC (reward circuit) | positive (normally) | Blunted NAc reactivity to non-drug reward in a subset (anhedonia/amotivational pattern); replication mixed, effect smaller than other SUDs | fMRI | LOW-MEDIUM (mixed) | Martz 2016; Skumlien 2023 |
| Dorsal striatum vs ventral striatum vs prefrontal reward/regulatory regions (fronto-striatal habit shift) | mixed | Shifted balance toward dorsal-striatal (habit) over ventral-striatal communication with frontal regions in cannabis dependence | fMRI | MEDIUM (single-cohort, directionally consistent with SUD habit model) | Zhou et al. 2018 (bioRxiv 282939) |
| dlPFC / ACC vs ventral striatum (cognitive control over reward) | negative (anticorrelation, normally) | Weakened top-down control coupling; reduced inhibitory-control engagement | fMRI | LOW-MEDIUM | iRISA framework; Kober 2014 |
| Hippocampus vs prefrontal cortex (memory circuit) | positive (normally) | Altered hippocampal-prefrontal coupling; memory-circuit involvement given high hippocampal CB1; preclinical peri-adolescent CB1 activation disrupts hippocampal network function | fMRI / preclinical | LOW-MEDIUM | preclinical 2025 (PMC12734249); human memory literature |
| Default mode network (precuneus/PCC vs medial PFC) vs salience network | mixed | Altered DMN-salience switching predicts craving; more consistent than structural findings (parent doc) | fMRI | MEDIUM | parent doc; Zhang & Volkow 2019 |

### EEG/MEG evoked and oscillatory markers (cortical-source, mapped to nodes above)

| Marker | Direction | Allen source region | Mechanistic anchor | Confidence | Source |
|---|---|---|---|---|---|
| P300 (P3a novelty / P3b target) amplitude | reduced (dose-dependent with THC; more pronounced in early-onset users) | precuneus / inferior parietal + middle frontal gyrus | context updating, attentional allocation; overlaps schizophrenia P300 endophenotype | MEDIUM (replicated direction, modest samples) | acute-THC and chronic-user EEG studies; review (PMC1764544) |
| Drug-cue reactivity (late positive potential, LPP) | enhanced to cannabis cues; blunted to natural-reward cues (in cannabis-using psychotic patients) | occipito-parietal + vmPFC source | incentive salience to drug over natural reward | LOW-MEDIUM | cue-reactivity LPP literature |
| Resting alpha/theta changes | altered (inconsistent) | broadband cortical | nonspecific arousal/attention | LOW (mixed) | scattered EEG reports |

Adolescent-exposure neurodevelopmental note: the strongest developmental signal is that adolescent and peri-adolescent cannabis exposure is associated with later psychotic-disorder risk (consistent, dose-responsive, biologically plausible via CB1-mediated disruption of an active eCB-dependent developmental window). Adolescent users show more pronounced P300 reduction and candidate hippocampal/prefrontal effects. This is a developmental-vulnerability axis rather than a clean structural biotype, and structural findings remain inconsistent.

---

## MACRO scale (phenotype) vs SNOMED CT / HPO

CUD phenotypes are well-defined clinically (DSM-5 cannabis use disorder, ICD-11 6C41) even though the underlying biotypes are immature. SNOMED CT covers the disorder and dependence cleanly; HPO has limited substance-use coverage (HPO is oriented toward rare/Mendelian disease), so most HPO mappings here are general behavioral terms and are flagged approx, needs curation.

| Biotype phenotype | SNOMED CT term + ID | HPO term + ID | Short description of observations that led to this mapping | Source |
|---|---|---|---|---|
| Cannabis use disorder / dependence (umbrella) | Cannabis dependence 268766005 (approx, needs curation; ICD-11 6C41.2) | Substance abuse HP:0031507 (approx, needs curation) | Problematic pattern of cannabis use with impaired control, salience, and continued use despite harm | findacode SNOMEDCT; HPO |
| Craving | Drug craving 36556007 (approx, needs curation) | (no precise HPO term; approx, needs curation) | Strong urge to use; the most discriminating DSM-5 criterion; maps to drug-cue reactivity (LPP, vmPFC/striatal) | DSM-5; cue-reactivity literature |
| Tolerance | Drug tolerance 62164002 (approx, needs curation) | (no precise HPO term) | Diminished effect at constant dose; maps to CB1 downregulation/desensitization | Hirvonen 2012 |
| Cannabis withdrawal (irritability, sleep disturbance, appetite/weight change, restlessness) | Cannabis withdrawal (approx, needs curation; recognized DSM-5/ICD-11, precise SNOMED concept uncertain) | Irritability HP:0000737; Insomnia HP:0100785; Decreased appetite HP:0004396 | Time-limited syndrome on cessation in dependent users; maps to eCB rebound and amygdala/negative-affect circuitry | DSM-5; Allsop 2012; D'Souza 2019 |
| Amotivational / anhedonic features | Apathy 84660005 (approx, needs curation); Anhedonia (approx) | Apathy HP:0000741 (approx); Anhedonia HP:0033676 | Reduced goal-directed behavior and pleasure; maps to blunted striatal reward (note: the amotivational syndrome is contested and not robustly supported) | Skumlien 2023; Martz 2016 |
| Cannabis-induced / associated psychosis risk | Cannabis-induced psychotic disorder 31898009 (approx, needs curation) | Psychosis HP:0000709 | Acute psychotomimetic effects and elevated longitudinal psychosis risk, especially high-potency products and early-onset use; genetic overlap with schizophrenia | Johnson 2020; Levey 2023; psychosis epidemiology |
| Cognitive / attentional impairment | Cognitive impairment 386806002 (general) | Cognitive impairment HP:0100543 | Working memory and attention deficits; overlaps P300 reduction; partially reversible with abstinence | EEG/cognition literature |

HPO note: HPO substance-use coverage is sparse, so craving, tolerance, and cannabis-specific terms are marked approx, needs curation. SNOMED 386806002 (Cognitive impairment) is confirmed; cannabis-specific SNOMED IDs (268766005 dependence, 31898009 cannabis-induced psychosis) are provided as best matches and flagged for curation. A precise SNOMED concept for cannabis withdrawal was not confidently resolved and is marked accordingly.

---

## Interventional studies (incl. neuromodulation, DBS, neuroplastogens)

The defining clinical fact for CUD, and the largest gap in this disorder set, is that **there is no FDA-approved pharmacotherapy for cannabis use disorder.** Behavioral interventions (CBT, motivational enhancement therapy, contingency management) remain the only evidence-based mainstay, and even these produce modest, often non-durable effects. Because there is no approved drug, CUD lacks the treatment-stratified imaging biotypes that anchor the alcohol (naltrexone, acamprosate) and opioid (buprenorphine) docs. The pharmacology table below is therefore a table of trials, most small, several null, and none registered.

| Biotype it targets | Intervention (class + specific) | Study (author year, design, n) | Outcome | Confidence | Source |
|---|---|---|---|---|---|
| Behavioral mainstay (all biotypes) | CBT + motivational enhancement therapy + contingency management | Multiple RCTs and meta-analyses | Best available evidence; modest effect sizes, high relapse; CM adds abstinence benefit during treatment | MEDIUM-HIGH (efficacy modest, durability limited) | Cochrane and meta-analytic reviews; parent doc |
| Glutamatergic / oxidative (NAC) | N-acetylcysteine 1200 mg BID (glutamate homeostasis, antioxidant) | Gray 2012 RCT adolescents (n=116, + contingency management): positive (OR 2.4 for abstinence). Gray 2017 adults (n=302): null. Gray 2025 youth without robust behavioral platform (n=192): null (RR 0.93) | Positive only in the original adolescent trial that included contingency management; not replicated in adults; the 2025 youth replication without a strong behavioral platform was also null | LOW-MEDIUM (developmental-/context-specific at best; not a reliable pharmacotherapy) | Gray 2012 doi:10.1176/appi.ajp.2012.12010055; Gray 2017 doi:10.1016/j.drugalcdep.2017.06.014; Gray 2025 doi:10.1038/s41386-025-02061-y |
| Withdrawal / eCB tone (CBD) | Cannabidiol 400 mg and 800 mg/day | Freeman 2020 phase 2a adaptive Bayesian RCT (n=82) | 400 mg and 800 mg safe and more efficacious than placebo at reducing cannabis use (urinary THC-COOH, abstinence days); 200 mg eliminated as inefficacious; short (4-week) trial, magnitude/durability not established | MEDIUM (positive phase 2a; needs phase 3) | Freeman 2020 doi:10.1016/S2215-0366(20)30290-X |
| eCB system / withdrawal (FAAH inhibition) | FAAH inhibitor PF-04457845 (raises anandamide) | D'Souza 2019 phase 2a RCT in men (n=70) | Reduced withdrawal symptoms, reduced self-reported use, and reduced urinary THC-COOH vs placebo; not psychoactive/abusable; men only, single site | MEDIUM (positive, emerging mechanism; not yet replicated/registered) | D'Souza 2019 doi:10.1016/S2215-0366(18)30427-9 |
| Withdrawal / GABAergic (gabapentin) | Gabapentin 1200 mg/day | Mason 2012 pilot RCT (n=50) | Reduced withdrawal, craving, and use, improved cognition in a small pilot; not replicated at scale; abuse-liability concerns limit enthusiasm | LOW (single small pilot) | Mason 2012 doi:10.1038/npp.2012.14 |
| Withdrawal symptom relief (cannabinoid agonist / substitution) | Nabiximols (THC:CBD), dronabinol, nabilone | Several trials (e.g., Allsop 2014 nabiximols) | Reduce withdrawal severity and retention; limited effect on long-term abstinence; substitution-pharmacotherapy logic | LOW-MEDIUM | Allsop 2014; reviews |
| Cognitive-control / craving (dlPFC) | Repetitive TMS, 10 Hz left dlPFC (Beam-F3), with cannabis cues + MET | Sahlem 2023 two-site phase 2 RCT (n=72, active vs sham) + MET | Preliminary; primary craving outcome change examined; limited and not definitive evidence; small sample | LOW (very limited; preliminary) | Sahlem 2023 doi:10.1016/j.drugalcdep.2023.111035 |
| Deep brain stimulation | DBS (NAc / ventral striatum) | No controlled CUD trials | No DBS evidence in cannabis use disorder; not trialed beyond general SUD discussion | NONE (not studied in CUD) | parent doc |
| Neuroplastogens (psilocybin, ketamine) | Psychedelic-assisted therapy | No completed CUD RCTs (early/observational only) | No CUD-specific efficacy evidence; psilocybin SUD evidence is in alcohol, not cannabis | LOW/NONE (not established for CUD) | parent doc; Bogenschutz 2022 (AUD, not CUD) |

DBS and neuroplastogen note: unlike alcohol use disorder (psilocybin phase 2 positive) or the DBS literature for OCD/AUD, cannabis use disorder has essentially no neuromodulation or neuroplastogen evidence beyond a single small preliminary rTMS trial. This absence is itself a defining feature of the CUD evidence landscape.

---

## Most defensible biotypes (cross-scale synthesis)

These integrate the three scales. They are weaker and more provisional than the biotypes in the alcohol, opioid, or schizophrenia docs, and I label them candidate biotypes accordingly. A single person may load on more than one.

### Biotype 1: Endocannabinoid-adaptation biotype (the strongest CUD-specific candidate)
- **MICRO:** CB1 receptor downregulation/desensitization (reversible, PET-measured, replicated direction), FAAH downregulation, altered AEA/2-AG tone. This is the only molecular feature that is both CUD-specific and reasonably reproducible.
- **MESO (anchor Allen regions):** neocortex broadly, hippocampal formation, cerebellum (the three highest-CB1 regions).
- **MACRO:** tolerance, withdrawal (irritability, sleep, appetite).
- **Treatment lever:** FAAH inhibition (PF-04457845, D'Souza 2019) and CBD (Freeman 2020) both engage the eCB system and are the two positive trials in the disorder.
- **Why defensible:** PET CB1 downregulation reverses with abstinence and scales with use; eCB-targeting drugs are the only ones with positive RCT signals. Confidence MEDIUM (the strongest CUD biotype, still single-mechanism).

### Biotype 2: Reward-deficit / amotivational biotype (contested)
- **MICRO:** blunted striatal dopamine signaling downstream of eCB adaptation; anhedonia.
- **MESO (anchor Allen regions):** ventral striatum / NAc, OFC, vmPFC; edge: blunted NAc reactivity to non-drug reward.
- **MACRO:** amotivational/anhedonic features.
- **Why defensible:** plausible and mechanistically coherent, but the fMRI reward literature is genuinely split and the "amotivational syndrome" is not robustly supported. Confidence LOW-MEDIUM; flag mixed replication.

### Biotype 3: Cognitive-control / fronto-striatal biotype
- **MICRO:** glutamatergic/GABAergic modulation via CB1; CADM2 synaptic-adhesion risk.
- **MESO (anchor Allen regions):** dlPFC, ACC, dorsal striatum; edge: weakened dlPFC/ACC top-down control, dorsal-over-ventral striatal shift (habit). EEG: reduced P300.
- **MACRO:** impaired inhibitory control, craving, cognitive/attentional deficits.
- **Why defensible:** consistent with the transdiagnostic SUD iRISA/habit model and the one preliminary rTMS target (dlPFC); P300 reduction replicates in direction. Confidence MEDIUM.

### Biotype 4: Psychosis-risk / schizophrenia-overlap biotype
- **MICRO:** CUD-schizophrenia genetic correlation (rg ~0.3-0.5), CHRNA2 colocalization, MR evidence; dopamine/cholinergic relevance.
- **MESO (anchor Allen regions):** striatum (dopamine), prefrontal cortex, hippocampus; EEG: P300 reduction overlapping the schizophrenia endophenotype.
- **MACRO:** cannabis-induced/associated psychosis, elevated longitudinal psychosis risk (high-potency products, early onset).
- **Why defensible:** the genetic overlap is the single best-powered transdiagnostic signal for CUD and is epidemiologically corroborated; mechanistically the most important link to the broader disorder set. Confidence HIGH (genetic correlation); MEDIUM (individual-level biotype operationalization).

### Biotype 5: Adolescent neurodevelopmental-exposure biotype (axis, not a clean structural type)
- **MICRO:** CB1-mediated disruption of an eCB-dependent developmental window; FOXP2 neurodevelopmental risk.
- **MESO (anchor Allen regions):** hippocampus, prefrontal cortex; more pronounced P300 reduction in early-onset users; preclinical peri-adolescent hippocampal network disruption.
- **MACRO:** earlier onset, greater cognitive impact, elevated psychosis risk.
- **Why defensible:** developmental timing effects are epidemiologically consistent, but human structural findings (hippocampal volume) replicate poorly. Confidence LOW-MEDIUM; honest about inconsistent structural data.

**Anchor Allen regions across the candidate biotypes for an adaptive headset:** neocortex (broad, highest CB1), hippocampal formation, cerebellum, caudate/putamen and accumbens (ventral and dorsal striatum), and middle/superior frontal gyrus (dlPFC) with cingulate gyrus anterior part (ACC). The eCB-weighted regions (cortex, hippocampus, cerebellum) and the fronto-striatal reward/control regions cover most of what replicates.

**Honest evidence-gap statement:** cannabis use disorder has the thinnest biotype evidence of the substance use disorders. Its structural imaging is the most inconsistent, its reward fMRI is split, it has no neuroinflammatory biotype, no DBS or neuroplastogen evidence, and crucially no approved pharmacotherapy to provide treatment-response validation. The two pillars that are genuinely defensible are the endocannabinoid-adaptation molecular biotype (CB1/FAAH PET plus eCB-targeting drug response) and the schizophrenia genetic-overlap biotype. Everything else is a candidate.

**Genomic factor statement:** cannabis use disorder loads on the **substance use factor** of the Nature 2025 five-factor model (alcohol + opioid + nicotine + cannabis), as the smallest and most weakly powered of the four contributing disorders.

---

## References

1. Grotzinger AD, Werme J, Peyrot WJ, et al. Mapping the genetic landscape across 14 psychiatric disorders. Nature. 2025. https://doi.org/10.1038/s41586-025-09820-3

2. Levey DF, Galimberti M, Deak JD, et al. Multi-ancestry genome-wide association study of cannabis use disorder yields insight into disease biology and public health implications. Nat Genet. 2023;55:2094-2103. https://doi.org/10.1038/s41588-023-01563-z

3. Johnson EC, Demontis D, Thorgeirsson TE, et al. A large-scale genome-wide association study meta-analysis of cannabis use disorder. Lancet Psychiatry. 2020;7:1032-1045. https://doi.org/10.1016/S2215-0366(20)30339-4

4. Hatoum AS, Colbert SMC, Johnson EC, et al. Multivariate genome-wide association meta-analysis of over 1 million subjects identifies loci underlying multiple substance use disorders. Nat Ment Health. 2023;1:210-223. https://doi.org/10.1038/s44220-023-00034-y

5. Pasman JA, Verweij KJH, Gerring Z, et al. GWAS of lifetime cannabis use reveals new risk loci, genetic overlap with psychiatric traits, and a causal influence of schizophrenia. Nat Neurosci. 2018;21:1161-1170. https://doi.org/10.1038/s41593-018-0206-1

6. Hirvonen J, Goodwin RS, Li CT, et al. Reversible and regionally selective downregulation of brain cannabinoid CB1 receptors in chronic daily cannabis smokers. Mol Psychiatry. 2012;17:642-649. https://doi.org/10.1038/mp.2011.82

7. Boileau I, Mansouri E, Williams B, et al. Fatty acid amide hydrolase binding in brain of cannabis users: imaging with [11C]CURB positron emission tomography. Biol Psychiatry. 2016;80:691-701. https://doi.org/10.1016/j.biopsych.2016.04.012

8. Cuttler C, Stueber A, Cooper ZD, et al. Circulating endocannabinoids and N-acylethanolamines in individuals with cannabis use disorder. Cannabis Cannabinoid Res. 2023. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10605789/

9. Bloomfield MAP, Ashok AH, Volkow ND, Howes OD. The effects of delta-9-tetrahydrocannabinol on the dopamine system. Nature. 2016;539:369-377. https://doi.org/10.1038/nature21369

10. Martz ME, Trucco EM, Cope LM, et al. Association of marijuana use with blunted nucleus accumbens response to reward anticipation. JAMA Psychiatry. 2016;73:838-844. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4972653/

11. Skumlien M, Mokrysz C, Freeman TP, et al. Brain reward function in people who use cannabis: a systematic review. Front Behav Neurosci. 2023;17:1323609. https://www.frontiersin.org/journals/behavioral-neuroscience/articles/10.3389/fnbeh.2023.1323609/full

12. Mackey S, Allgaier N, Chaarani B, et al. Mega-analysis of gray matter volume in substance dependence. Am J Psychiatry. 2019;176:119-128. https://doi.org/10.1176/appi.ajp.2018.17040415

13. Zhang R, Volkow ND. Brain default-mode network dysfunction in addiction. Neuroimage. 2019;200:313-331. https://doi.org/10.1016/j.neuroimage.2019.06.036

14. Lorenzetti V, Chye Y, Silva P, et al. Does regular cannabis use affect neuroanatomy? An updated systematic review. Eur Arch Psychiatry Clin Neurosci. 2019;269:59-71. https://doi.org/10.1007/s00406-019-00979-1

15. Freeman TP, Hindocha C, Baio G, et al. Cannabidiol for the treatment of cannabis use disorder: a phase 2a, double-blind, placebo-controlled, randomised, adaptive Bayesian trial. Lancet Psychiatry. 2020;7:865-874. https://doi.org/10.1016/S2215-0366(20)30290-X

16. D'Souza DC, Cortes-Briones J, Creatura G, et al. Efficacy and safety of a fatty acid amide hydrolase inhibitor (PF-04457845) in the treatment of cannabis withdrawal and dependence in men: a double-blind, placebo-controlled, parallel group, phase 2a single-site randomised controlled trial. Lancet Psychiatry. 2019;6:35-45. https://doi.org/10.1016/S2215-0366(18)30427-9

17. Gray KM, Carpenter MJ, Baker NL, et al. A double-blind randomized controlled trial of N-acetylcysteine in cannabis-dependent adolescents. Am J Psychiatry. 2012;169:805-812. https://doi.org/10.1176/appi.ajp.2012.12010055

18. Gray KM, Sonne SC, McClure EA, et al. A randomized placebo-controlled trial of N-acetylcysteine for cannabis use disorder in adults. Drug Alcohol Depend. 2017;177:249-257. https://doi.org/10.1016/j.drugalcdep.2017.06.014

19. Gray KM, Tomko RL, Baker NL, et al. N-acetylcysteine for youth cannabis use disorder: randomized controlled trial main findings. Neuropsychopharmacology. 2025. https://doi.org/10.1038/s41386-025-02061-y

20. Mason BJ, Crean R, Goodell V, et al. A proof-of-concept randomized controlled study of gabapentin: effects on cannabis use, withdrawal and executive function deficits in cannabis-dependent adults. Neuropsychopharmacology. 2012;37:1689-1698. https://doi.org/10.1038/npp.2012.14

21. Allsop DJ, Copeland J, Lintzeris N, et al. Nabiximols as an agonist replacement therapy during cannabis withdrawal: a randomized clinical trial. JAMA Psychiatry. 2014;71:281-291. https://doi.org/10.1001/jamapsychiatry.2013.3947

22. Sahlem GL, Caruso M, Short EB, et al. A preliminary randomized controlled trial of repetitive transcranial magnetic stimulation applied to the left dorsolateral prefrontal cortex in treatment-seeking participants with cannabis use disorder. Drug Alcohol Depend. 2023;253:111035. https://doi.org/10.1016/j.drugalcdep.2023.111035

23. Kober H, DeVito EE, DeLeone CM, et al. Cannabis abstinence during treatment and one-year follow-up: relationship to neural activity in men. Neuropsychopharmacology. 2014;39:2288-2298. https://doi.org/10.1038/npp.2014.82

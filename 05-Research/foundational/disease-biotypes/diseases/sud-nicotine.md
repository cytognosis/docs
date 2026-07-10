# Biotypes: Nicotine / Tobacco Use Disorder

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: researchers, stakeholders
> **Tags**: `literature-synthesis`, `disease-biotypes`, `sud-nicotine`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)

Genomic factor loading (Nature 2025): **Substance-use factor** (shared with alcohol, opioid, and cannabis use disorders; the factor groups the four addictive disorders and is the most distinct of the five). Grotzinger et al., Mapping the genetic landscape across 14 psychiatric disorders, Nature 2025 (doi:10.1038/s41586-025-09820-3, 1,056,201 cases, 5 genomic factors, 238 pleiotropic loci).

Nicotine use disorder occupies a privileged place in addiction biology for two reasons that the other substance docs cannot match. First, the strongest, most replicated addiction-genetics association anywhere is the CHRNA5 missense variant rs16969968 in the chromosome-15 nicotinic receptor cluster, a finding that converges molecular pharmacology, GWAS, and the receptor mechanism nicotine acts on directly. Second, a single pharmacogenetic axis, the rate of nicotine metabolism set largely by CYP2A6, has produced one of the few prospective, biomarker-stratified randomized trials in all of psychiatry (Lerman et al. 2015), giving nicotine use disorder a deployable treatment-matching biotype that most psychiatric disorders lack. The insula provides the connectomic anchor: the Naqvi lesion study showed that damage to the insula abolishes the urge to smoke, and the insula is the explicit target of the only FDA-cleared deep TMS device for an addiction. This document harmonizes the molecular, connectomic, and phenotypic evidence to Gene Ontology, the Allen Human Reference Atlas 3D (2020), and SNOMED CT / HPO respectively, and closes with the most defensible cross-scale biotypes. Replication status is explicit throughout.

## Seed papers

- Naqvi, Rudrauf, Damasio, Bechara 2007 (insula lesion abolishes smoking addiction), Science, doi:10.1126/science.1135926; Naqvi & Bechara 2010 (interoceptive view), Brain Struct Funct, doi:10.1007/s00429-010-0268-7.
- Saunders et al. (GSCAN) 2022 (multi-ancestry tobacco/alcohol GWAS, ~3.4M), Nature, doi:10.1038/s41586-022-05477-4; Liu et al. (GSCAN) 2019, Nat Genet, doi:10.1038/s41588-018-0307-5.
- Hancock/Bierut et al. (iNDiGO) 2018 (nicotine-dependence GWAS, six reproducible loci), bioRxiv/Mol Psychiatry; Bierut et al. 2008 (rs16969968 functional), Am J Psychiatry, doi:10.1176/appi.ajp.2008.07111711.
- Lerman et al. 2015 (NMR-stratified patch vs varenicline RCT, the PNGM trial), Lancet Respir Med, doi:10.1016/S2213-2600(14)70294-2.
- Zangen, Moshe, Martinez et al. 2021 (BrainsWay H4 deep TMS pivotal RCT, FDA-cleared 2020), World Psychiatry, doi:10.1002/wps.20905; Dinur-Klein et al. 2014 (deep TMS prefrontal+insula), Biol Psychiatry, doi:10.1016/j.biopsych.2014.05.020.
- Fowler & Kenny / Frahm et al. (medial habenula-interpeduncular CHRNA5/CHRNB4 aversion circuit), reviews PMC4452453; Frahm et al. 2011, Neuron.
- Morales, Ghahremani, London et al. 2014 (insula cortical thickness scales with dependence), Neuropsychopharmacology, doi:10.1038/npp.2014.48.

---

## MICRO scale (molecular / genetic / cellular / immune) vs GO-harmonized

The shared signal across all 14 disorders in Grotzinger et al. 2025 was enriched for broad transcriptional regulation; the Substance-use-factor-specific biology that nicotine use disorder loads on is dominated by the direct molecular target of the drug, the neuronal nicotinic acetylcholine receptor (nAChR). This is the central organizing fact of nicotine biology and distinguishes it from every other psychiatric disorder in the set: the genomic, pharmacologic, and circuit evidence all converge on the same receptor family. Acetylcholine (cholinergic, nicotinic) is therefore the primary neurotransmitter system, with dopamine (reward), glutamate, and GABA as downstream effectors. Molecular biotyping centers on five axes: the CHRNA5-A3-B4 nicotinic receptor cluster, the high-affinity alpha4-beta2 receptor (the desensitization and upregulation substrate), nicotine pharmacokinetics via CYP2A6, mesolimbic dopamine reward signaling, and the habenular aversion/withdrawal circuit.

| Biotype / dysregulation | GO term(s) + ID | Specific finding (genes, variants, molecules) | Neurotransmitter family | BDNF / neurotrophin + plasticity? | E/I imbalance (+ region) | Oxidative / mito / ROS? | Immune / inflammatory? | Confidence | Source (author year, DOI) |
|---|---|---|---|---|---|---|---|---|---|
| **CHRNA5-A3-B4 nicotinic receptor cluster (the primary, strongest signal)** | acetylcholine receptor signaling pathway (GO:0095500, approx, needs curation); nicotinic acetylcholine-activated cation-selective channel activity (GO:0022848); excitatory chemical synaptic transmission (GO:0098976, approx) | **rs16969968 (CHRNA5 D398N)** is the strongest and most replicated addiction-genetics association anywhere; the risk A-allele reduces alpha5-containing receptor function, raises cigarettes-per-day, nicotine dependence, and lung-cancer risk; alpha3 (CHRNA3) and beta4 (CHRNB4) co-segregate in the chr15q25 cluster | **Acetylcholine (nicotinic; the primary receptor system)** | not direct | candidate E-up via reduced inhibitory/aversion gating (habenula-IPN; see below) | not reported | not reported | HIGH (genome-wide, multi-cohort, functionally validated) | Bierut et al. 2008, doi:10.1176/appi.ajp.2008.07111711; Saccone et al. 2007 |
| **alpha4-beta2 high-affinity nAChR upregulation / desensitization** | nicotinic acetylcholine receptor activity (GO:0004889, approx, needs curation); receptor internalization (GO:0031623); regulation of postsynaptic membrane neurotransmitter receptor levels (GO:0099072) | Chronic nicotine desensitizes then upregulates high-affinity alpha4-beta2 receptors (the varenicline and PET [11C]nicotine/2-FA target); CHRNA4 splice variant (iNDiGO) associated with dependence; receptor upregulation underlies withdrawal and craving | **Acetylcholine (nicotinic)** | not direct | E-up on VTA dopamine neurons (presynaptic facilitation) | not reported | not reported | HIGH (pharmacology + PET) | Hancock/iNDiGO 2018; Brody et al. PET occupancy work |
| **Nicotine metabolism / clearance (CYP2A6 vs the pharmacogenetic treatment-matching biotype)** | xenobiotic metabolic process (GO:0006805); oxidoreductase activity, acting on paired donors (GO:0016712, approx); response to nicotine (GO:0035094) | **CYP2A6** activity sets nicotine clearance and the nicotine metabolite ratio (NMR, 3'-hydroxycotinine:cotinine); fast metabolizers (high NMR) smoke more, are more dependent, and respond better to varenicline; slow metabolizers do well on the patch and get more side effects from varenicline; defines the only prospectively validated psychiatric treatment-matching biomarker | none direct (metabolic; modulates nicotine exposure to all systems) | not direct | not reported (CYP is oxidative metabolism but not CNS ROS) | not reported | HIGH (prospective RCT) | Lerman et al. 2015, doi:10.1016/S2213-2600(14)70294-2 |
| **Mesolimbic dopamine reward signaling** | dopamine secretion (GO:0014046); regulation of dopamine secretion (GO:0014059); positive regulation of dopamine secretion (GO:0033603) | Nicotine activates alpha4-beta2 (and alpha6) nAChRs on VTA dopamine neurons, driving phasic dopamine release in NAc; DRD2/ANKK1 Taq1A weakly implicated; addiction-rf gene-based hits include DRD2 | **Dopamine** (reward); facilitated by **Acetylcholine** | not direct | E-up of VTA dopamine output | not reported | not reported | HIGH (mechanism); MEDIUM (human genetic) | Hatoum et al. 2023, doi:10.1038/s44220-023-00034-y; Volkow & Koob 2016 |
| **Glutamatergic facilitation of dopamine release** | glutamatergic synaptic transmission (GO:0035249); regulation of glutamate secretion (GO:0014048) | Presynaptic alpha7 nAChRs on glutamate terminals in VTA enhance glutamate release and contribute to long-term potentiation of dopamine-neuron excitability (sensitization substrate) | **Glutamate**; **Acetylcholine (alpha7)** | yes vs nAChR-gated LTP of VTA inputs (plasticity of reward learning) | E-up in VTA | not reported | not reported | MEDIUM (rodent mechanism, human inferential) | Mansvelder & McGehee 2000 (Neuron); reviews |
| **GABAergic disinhibition in VTA** | GABAergic synaptic transmission (GO:0051932); inhibitory postsynaptic potential (GO:0060080, approx) | Nicotine initially excites then desensitizes nAChRs on VTA GABA interneurons, producing net disinhibition of dopamine neurons; shifts E/I balance toward dopamine output | **GABA**; **Acetylcholine** | not direct | I-down in VTA (interneuron desensitization) -> net E-up of dopamine neurons | not reported | not reported | MEDIUM (rodent mechanism) | Mansvelder, Keath, McGehee 2002 (Neuron) |
| **Habenular aversion / withdrawal circuit (CHRNB4, CHRNA5, CHRNA3)** | acetylcholine receptor signaling pathway (GO:0095500, approx); response to nicotine (GO:0035094); negative regulation of behavior (GO:0048521, approx) | Medial habenula -> interpeduncular nucleus expresses alpha5/alpha3/beta4; alpha5 knockdown abolishes nicotine aversion at high doses and increases intake; beta4 overexpression increases aversion; the molecular substrate of the dose-limiting and withdrawal-anxiety signal | **Acetylcholine (nicotinic)**; downstream **GABA** in IPN | not direct | balance of aversion gating; alpha5 loss reduces inhibitory aversion signal | not reported | not reported | HIGH (rodent causal); MEDIUM (human variant link) | Fowler, Lu, Kenny et al. 2011 (Nature); Frahm et al. 2011 (Neuron); review PMC4452453 |
| **Polygenic smoking-behavior architecture (GSCAN / iNDiGO)** | regulation of synaptic transmission (GO:0050804); neuron differentiation (GO:0030182) | GSCAN multi-ancestry (~3.4M) found 1,346 loci for smoking initiation and 140 for cigarettes-per-day; iNDiGO found six reproducible nicotine-dependence loci: CHRNB3-CHRNA6, DBH, CHRNA5-A3-B4, DNMT3B, NOL4L, CHRNA4; highly polygenic beyond the nicotinic cluster | **Acetylcholine** (cluster loci); **Norepinephrine** (DBH) | not direct | not specified | not reported | not reported | HIGH (GWAS); polygenic score weak alone | Saunders et al. 2022, doi:10.1038/s41586-022-05477-4; Liu et al. 2019, doi:10.1038/s41588-018-0307-5 |
| **Noradrenergic clearance / withdrawal (DBH)** | norepinephrine metabolic process (GO:0042415, approx); catecholamine biosynthetic process (GO:0042423) | DBH (dopamine beta-hydroxylase) is a reproducible nicotine-dependence locus; influences noradrenergic tone, withdrawal irritability, and bupropion mechanism (NE/DA reuptake inhibition) | **Norepinephrine**; **Dopamine** | not direct | not specified | not reported | not reported | MEDIUM (GWAS locus + pharmacology) | iNDiGO 2018; Liu et al. 2019 |
| **Smoking-induced AHRR hypomethylation (epigenetic exposure marker)** | DNA methylation (GO:0006306); response to toxic substance (GO:0009636) | AHRR cg05575921 hypomethylation is the most robust epigenetic biomarker of tobacco smoke exposure; tracks pack-years and partially reverses with cessation; an exposure marker, not a vulnerability biotype | none reported | not direct | not reported | yes (aryl-hydrocarbon / oxidative stress pathway) | yes (AHRR modulates inflammatory signaling) | HIGH (replicated EWAS) | Joubert et al. 2016; Philibert et al. methylation work |

**GWAS anchor.** The GSCAN consortium (Saunders et al. 2022) meta-analyzed ~3.4 million individuals across multiple ancestries, identifying 1,346 loci for smoking initiation and 140 for cigarettes-per-day, with the chr15q25 CHRNA5-A3-B4 cluster remaining the dominant heaviness signal across ancestries. The Nicotine Dependence GenOmics consortium (iNDiGO) defined six reproducible genome-wide-significant nicotine-dependence loci (CHRNB3-CHRNA6, DBH, CHRNA5-A3-B4, DNMT3B, NOL4L, CHRNA4). Within this architecture, two molecular facts carry disproportionate weight for biotyping: rs16969968 (CHRNA5 D398N) is the single strongest replicated addiction variant, and CYP2A6-set metabolism (NMR) is the actionable pharmacogenetic axis. Polygenic scores explain only ~1 to 4 percent of variance and cannot define a biotype alone, but they weight priors over biotype membership when fused with the metabolism and circuit readouts.

---

## MESO scale (connectomic) vs Allen Atlas nodes + edges

Reference: Allen Human Reference Atlas 3D 2020 (141 anatomical regions). Functional labels and Brodmann areas appear in parentheses; the Allen anatomical container is named first. The defining connectomic feature of nicotine use disorder is the disproportionate causal weight of the **anterior insula**: Naqvi et al. showed that smokers who acquired insula damage quit smoking easily and lost the urge, far more often than smokers with non-insula lesions, the landmark finding in the field. Insula cortical thickness scales with dependence severity (Morales et al. 2014). The salience network anchored on anterior insula and dorsal ACC carries both the craving signal and the moderator of deep TMS response. The medial habenula and interpeduncular nucleus are small but mechanistically central for aversion and withdrawal; they fall below the resolution of the Allen 141-region set and are flagged as sub-parcel additions.

### NODES

| Allen region (functional label) | Observed change | Modality | Confidence | Source |
|---|---|---|---|---|
| Insula, anterior part (anterior insula / agranular) | **Hyperreactivity** to smoking cues (cue-induced craving); cortical thickness scales with dependence severity and craving; lesion abolishes the urge to smoke | fMRI (task) + structural + lesion | HIGH (cue reactivity, lesion, thickness all converge) | Naqvi et al. 2007, doi:10.1126/science.1135926; Morales et al. 2014, doi:10.1038/npp.2014.48 |
| Insula, posterior part (posterior insula / interoceptive) | Altered interoceptive signaling; engaged during bodily withdrawal sensations | fMRI | MEDIUM | Naqvi & Bechara 2010, doi:10.1007/s00429-010-0268-7 |
| Striatum, ventral (nucleus accumbens / ventral striatum) | **Increased** dopamine release and cue reactivity acutely; **blunted** response to non-drug reward in dependence; reduced D2/D3 availability | fMRI + PET | HIGH (PET dopamine); MEDIUM (reward blunting) | Volkow & Koob 2016, doi:10.1056/NEJMra1511480 |
| Frontal cortex, orbital part (OFC / BA11, BA47) | Cortical thinning; **hyperreactivity** to smoking cues (valuation); the most consistent structural finding in nicotine vs other substances | structural + fMRI | MEDIUM-HIGH | Mackey et al. 2019 (ENIGMA), doi:10.1176/appi.ajp.2018.17040415 |
| Frontal cortex, medial prefrontal / ventromedial (vmPFC / BA10, BA32) | **Hyperreactivity** to cues (craving valuation); hypofunction during inhibitory control | fMRI | MEDIUM | Zilverstand et al. 2018, doi:10.1016/j.neuron.2018.03.048 |
| Frontal cortex, dorsolateral prefrontal (dlPFC / BA9, BA46) | **Hypoactivation** during inhibitory control; the deep-TMS excitatory target | fMRI + TMS | MEDIUM-HIGH | Zangen et al. 2021, doi:10.1002/wps.20905 |
| Cingulate gyrus, dorsal anterior part (dACC / BA24, BA32) | **Hyperreactivity** to cues; salience-network node; reduced engagement during control | fMRI | MEDIUM-HIGH | Zilverstand et al. 2018 |
| Amygdala (basolateral + centromedial) | **Hyperreactivity** to negative affect and withdrawal; smaller volume across substances | fMRI + structural | MEDIUM | Mackey et al. 2019 (ENIGMA) |
| Epithalamus, medial habenula (MHb; sub-parcel, non-Allen-resolved addition) | Aversion/withdrawal signaling via alpha5/beta4 nAChRs; **hyperactivity** during withdrawal in rodents; human resting connectivity altered | fMRI (rodent + emerging human) | MEDIUM (rodent causal); LOW-MEDIUM (human) | Fowler et al. 2011 (Nature); review PMC4452453 |
| Midbrain, interpeduncular nucleus (IPN; sub-parcel, non-Allen-resolved addition) | GABAergic withdrawal-expression node downstream of MHb | rodent electrophysiology/fMRI | MEDIUM (rodent) | Zhao-Shea / IPN GABA work, doi:10.1038/s41386-021-01107-1 |
| Midbrain, ventral tegmental area (VTA; small Allen parcel) | **Increased** dopamine-neuron excitability (nAChR-driven disinhibition + glutamatergic LTP) | rodent + inferential human | MEDIUM | Mansvelder & McGehee 2000/2002 (Neuron) |
| Scalp EEG (centroparietal Pz; not an Allen parcel) | **Reduced P300 amplitude** to standard oddball; **enhanced P300 / LPP to smoking cues** (cue-reactivity ERP); P300 indexes dependence and predicts relapse | EEG (ERP) | MEDIUM-HIGH (cue-P300 robust; baseline-P300 mixed) | Littel et al. 2012 (cue-reactivity ERP meta-analysis), doi:10.1016/j.neubiorev.2012.05.001 |

### EDGES

| Region A vs Region B (functional labels) | Association sign | Observed change in disorder | Modality | Confidence | Source |
|---|---|---|---|---|---|
| Insula, anterior part vs striatum ventral (anterior insula vs NAc; insula-based craving network) | normally `positive` | **Increased** insula-striatal/reward connectivity tracks cigarette craving and cue reactivity; the insula-based network central to urge | fMRI (rest + cue) | MEDIUM-HIGH | Janes et al. 2010; Sutherland et al. 2012 review, doi:10.1016/j.neuropharm.2011.12.020 |
| Insula, anterior part vs cingulate gyrus dorsal anterior (anterior insula vs dACC; salience network) | normally `positive` | **Increased** salience-network connectivity correlates with craving and predicts/moderates deep TMS smoking-cessation response; the salience network is the key response moderator | fMRI | MEDIUM-HIGH (craving HIGH; TMS-moderator MEDIUM) | Dinur-Klein-line / insula-network cessation work, doi:10.1038/npp.2015.114; Zangen et al. 2021 |
| Insula, anterior part vs frontal cortex dlPFC (insula vs dlPFC; salience-to-control) | normally `mixed` | Altered insula-prefrontal coupling; greater pretreatment insula-network connectivity associated with better cessation outcomes | fMRI | MEDIUM | Addicott et al. 2015, doi:10.1038/npp.2015.114 |
| Striatum ventral vs frontal cortex orbital/ventromedial (NAc vs OFC/vmPFC; reward circuit) | normally `positive` | **Heightened** cue-driven coupling in reward/valuation circuit; blunted to non-drug reward | fMRI | MEDIUM-HIGH | Volkow & Koob 2016; Zilverstand et al. 2018 |
| Frontal cortex dlPFC/ACC vs striatum (fronto-striatal control loop) | normally `negative (anticorrelation)` (cortical control over striatal drive) | **Weakened** top-down fronto-striatal control; reduced inhibitory regulation of incentive drive | fMRI | MEDIUM | Goldstein & Volkow 2011, doi:10.1038/nrn3119 |
| Default-mode network vs salience network (DMN vs SN switching) | normally `negative (anticorrelation)` | **Impaired** DMN-salience anticorrelation/switching; insula withdrawal connectivity to DMN increases; predicts craving and relapse | fMRI | MEDIUM | Zhang & Volkow 2019, doi:10.1016/j.neuroimage.2019.06.036; Lerman et al. 2014 (abstinence connectivity) |
| Medial habenula vs interpeduncular nucleus (MHb vs IPN; aversion/withdrawal) | normally `positive` (cholinergic drive) | **Engaged** during withdrawal; alpha5/beta4-dependent; loss of alpha5 reduces aversion signal and increases intake | rodent circuit + emerging human | MEDIUM (rodent causal) | Fowler et al. 2011 (Nature); Frahm et al. 2011 (Neuron) |

**Replication note.** The insula's centrality (cue reactivity, lesion abolition of urge, thickness-dependence scaling) is the most robust connectomic finding for nicotine use disorder and is multi-method. The salience-network connectivity moderator of deep TMS response is supported but rests on a smaller set of studies; treat the TMS-prediction direction as MEDIUM. The MHb-IPN aversion circuit is causally robust in rodents but human imaging is limited by the small size of these nuclei relative to the Allen 141-region resolution.

---

## MACRO scale (phenotype) vs SNOMED CT / HPO

Nicotine/tobacco use disorder phenotype dimensions map to the DSM-5 / ICD-11 substance use disorder criteria, with tobacco-specific severity markers. The single most useful clinical severity index is time-to-first-cigarette after waking (the heaviness-of-smoking and Fagerstrom item most predictive of dependence and quit difficulty). HPO coverage of substance-use phenomenology is sparse, so several HPO cells are marked approx/needs curation and mapped to the nearest superordinate concept.

| Biotype phenotype | SNOMED CT term + ID | HPO term + ID | Short description of observations that led to this mapping | Source |
|---|---|---|---|---|
| Nicotine/tobacco use disorder (diagnosis anchor) | Nicotine dependence (56294008); Tobacco dependence syndrome (89765005, approx, needs curation) | Tobacco use disorder (HP:0500142, approx, needs curation) | Full DSM-5/ICD-11 syndrome; compulsive use despite harm; loads on the Substance-use genomic factor | Grotzinger et al. 2025, doi:10.1038/s41586-025-09820-3 |
| Craving (cue-induced urge) | Craving for tobacco (404674008, approx, needs curation); Drug craving (713583000, approx) | (no specific HPO; approx -> Behavioral abnormality HP:0000708) | Insula/salience-network-driven urge; enhanced cue-P300/LPP on EEG; the deep-TMS and insula target dimension | Naqvi et al. 2007; Littel et al. 2012 |
| Tolerance | Drug tolerance (76604000, approx, needs curation) | (no specific HPO; approx) | Reduced effect over time; nAChR upregulation/desensitization substrate; higher cigarettes-per-day | Saunders et al. 2022 |
| Withdrawal: irritability / negative affect | Nicotine withdrawal (191837009, approx, needs curation); Irritability (24199005) | Irritability (HP:0000737) | Habenula-IPN aversion circuit; noradrenergic (DBH) tone; relieved by NRT and bupropion | Fowler et al. 2011; review PMC4452453 |
| Withdrawal: difficulty concentrating | Difficulty concentrating (60032008, approx, needs curation) | Poor concentration (HP:0033223, approx, needs curation) | Cholinergic withdrawal cognitive symptom; reversible with nicotine | Hughes 2007 (withdrawal symptomatology) |
| Compulsive use despite harm (impaired control) | Compulsive drug use (approx, needs curation) | Compulsive behaviors (HP:0000722, approx, needs curation) | Continued smoking despite known harm; fronto-striatal control failure; iRISA salience/inhibition | Goldstein & Volkow 2011 |
| Dependence severity / time-to-first-cigarette | Severe nicotine dependence (approx, needs curation) | (no specific HPO; approx) | Time-to-first-cigarette after waking is the strongest single Fagerstrom severity item; tracks insula thickness and CYP2A6/NMR | Morales et al. 2014; Lerman et al. 2015 |
| Fast vs slow metabolizer treatment-response stratum | (pharmacogenetic stratum; no clean SNOMED concept; approx, needs curation) | (no HPO) | NMR (CYP2A6) divides patients into a patch-responsive slow stratum and a varenicline-responsive fast stratum; a treatment-matching phenotype, not a symptom | Lerman et al. 2015, doi:10.1016/S2213-2600(14)70294-2 |

---

## Interventional studies (incl. neuromodulation, DBS, neuroplastogens)

Nicotine use disorder has the strongest treatment-biotype evidence base of any addiction: a prospectively validated pharmacogenetic stratifier (NMR/CYP2A6), the only FDA-cleared deep TMS device for an addiction, and direct pharmacology against the causal receptor (varenicline, cytisine as nAChR partial agonists). Pharmacology is more mechanistically anchored here than for any other substance because the drugs act on the same receptors the GWAS implicates.

| Biotype it targets | Intervention (class + specific) | Study (author year, design, n) | Outcome | Confidence | Source |
|---|---|---|---|---|---|
| Withdrawal / dependence severity (general) | Nicotine replacement therapy (patch, gum, lozenge; agonist substitution) | Cochrane meta-analyses, many RCTs | Increases quit rates ~50-60% vs placebo; combination NRT superior to single | HIGH | Cochrane NRT reviews |
| nAChR-mediated reward/craving; fast-metabolizer stratum | Varenicline (alpha4-beta2 nAChR partial agonist; the most effective single agent) | EAGLES and pivotal RCTs; large meta-analyses | Most effective monotherapy; CHRNA5 rs16969968 and CYP2A6/NMR moderate response | HIGH | Anthenelli et al. 2016 (EAGLES); Lerman et al. 2015 |
| **Fast vs slow metabolizer (CYP2A6/NMR) treatment-matching biotype** | NMR-guided matching: varenicline for fast (normal) metabolizers, nicotine patch for slow metabolizers | Lerman et al. 2015, NMR-stratified double-blind placebo-controlled RCT, n=1,246 | Varenicline > patch in normal metabolizers; no varenicline advantage in slow metabolizers, who had more varenicline side effects; matching optimizes efficacy and tolerability | HIGH (prospective, stratified) | Lerman et al. 2015, doi:10.1016/S2213-2600(14)70294-2 |
| Noradrenergic/dopaminergic withdrawal; comorbid depression | Bupropion (NE/DA reuptake inhibitor + weak nAChR antagonist) | RCTs and meta-analyses | Roughly doubles quit rates vs placebo; less effective than varenicline; helps depressed/withdrawal-irritability subgroup | HIGH | Cochrane bupropion reviews |
| nAChR-mediated reward/craving (low-cost agonist) | Cytisine / cytisinicline (alpha4-beta2 partial agonist) | RAUORA and ORCA-2/3 RCTs (2023-2024) | Effective and low-cost; cytisinicline ORCA-2 showed higher abstinence vs placebo; comparable to varenicline in some head-to-head data | HIGH | Rigotti et al. 2023 (ORCA-2, JAMA), doi:10.1001/jama.2023.10042 |
| Insula/PFC craving circuit; salience-network connectivity moderator | **Deep TMS, BrainsWay H4 coil (FDA-cleared 2020 for smoking cessation)**, bilateral lateral PFC + insula, cue-provoked | Zangen et al. 2021, pivotal multicenter double-blind RCT, n=262, 18 sessions | 4-week continuous quit rate 28.4% active vs 11.7% sham; salience-network connectivity moderates response | HIGH (pivotal RCT, FDA clearance) | Zangen et al. 2021, doi:10.1002/wps.20905; Dinur-Klein et al. 2014, doi:10.1016/j.biopsych.2014.05.020 |
| Insula/PFC craving circuit (adjunct) | Insula deep rTMS combined with varenicline | RCT, insula dTMS + varenicline (2023) | Combination signal for improved abstinence vs sham + varenicline | MEDIUM | Brain Stimul 2023, doi:10.1016/j.brs.2023.11.005 (approx) |
| Prefrontal control / craving (non-invasive, lower intensity) | tDCS over dlPFC | Multiple small RCTs and meta-analyses | Reduces craving short-term; cessation evidence inconsistent | LOW-MEDIUM | Kang et al. meta-analyses |
| Severe, treatment-refractory addiction (rare, experimental) | Deep brain stimulation, nucleus accumbens | Case reports / small series (incidental smoking cessation in NAc DBS for other indications) | Anecdotal smoking cessation in patients receiving NAc DBS; not an established nicotine indication | LOW (case-level) | Kuhn et al. NAc DBS case reports |
| Craving rigidity / comorbid depression (hypothesized) | Neuroplastogens (psilocybin) for smoking cessation | Johnson et al. 2014, open-label pilot, n=15 | 80% biologically confirmed abstinence at 6 months in pilot; no controlled nicotine RCT yet; signal preliminary | LOW-MEDIUM (uncontrolled pilot) | Johnson et al. 2014, doi:10.1177/0269881114548296 |

---

## Most defensible biotypes (cross-scale synthesis)

Five biotypes are defensible from the literature and map cleanly to brain regions a Cytognosis-style spectroscopy headset could target. Two are nicotine-specific and carry unusual weight because the genetics, pharmacology, and circuit evidence converge on the same molecular target.

**Biotype 1: Insula-anchored interoceptive craving (the central nicotine biotype).** Anterior-insula hyperreactivity to smoking cues, insula cortical thickness scaling with dependence, and the Naqvi lesion finding that insula damage abolishes the urge. Edges: insula-striatal craving network and insula-dACC salience network, the latter moderating deep TMS response. Anchor Allen regions: insula anterior part, NAc/ventral striatum, dACC. Treatment lever: BrainsWay H4 deep TMS (FDA-cleared), insula-targeted neuromodulation. Confidence HIGH.

**Biotype 2: CHRNA5 nicotinic-receptor-cluster vulnerability.** The rs16969968 (CHRNA5 D398N) risk allele, the strongest replicated addiction variant anywhere, reduces alpha5-receptor function, raises cigarettes-per-day and dependence, and moderates varenicline response. Anchor regions: VTA/mesolimbic dopamine axis and the medial habenula-interpeduncular aversion circuit (alpha5/beta4). Treatment lever: varenicline (nAChR partial agonist), genotype-weighted matching. Confidence HIGH (genetics), MEDIUM (clinical prediction).

**Biotype 3: CYP2A6 metabolism treatment-matching biotype (the deployable pharmacogenetic biotype).** The nicotine metabolite ratio divides patients into a slow-metabolizer stratum that does well on the patch and a fast-metabolizer stratum that does best on varenicline (Lerman 2015, the only prospectively validated psychiatric treatment-matching biomarker). Not a circuit biotype but the most actionable. Treatment lever: NMR-guided patch-vs-varenicline selection. Confidence HIGH.

**Biotype 4: Habenular aversion/withdrawal biotype.** Medial habenula-interpeduncular alpha5/beta4 signaling sets the aversion ceiling and the withdrawal-anxiety/irritability signal; loss of alpha5 function increases intake. Maps to withdrawal-dominant clinical presentations. Anchor regions: medial habenula, interpeduncular nucleus (sub-Allen resolution). Treatment lever: NRT, bupropion, partial agonists. Confidence MEDIUM (rodent-causal, human-inferential).

**Biotype 5: Fronto-striatal control deficit / reward-deficiency.** Hypoactive dlPFC and weakened fronto-striatal control with blunted non-drug reward, the iRISA salience-and-inhibition failure shared across substances. Anchor regions: dlPFC, ACC, NAc, OFC. Treatment lever: deep TMS to dlPFC, contingency management, behavioral control training. Confidence MEDIUM.

Genomic factor: nicotine/tobacco use disorder loads on the **Substance-use factor** (with alcohol, opioid, and cannabis use disorders) in Grotzinger et al. 2025. Among the four, nicotine is the disorder whose causal molecular target (the nicotinic acetylcholine receptor) is most directly identified by its own GWAS, making the CHRNA5 cluster and CYP2A6-metabolism biotypes the most mechanistically grounded treatment-matching tools in the entire 14-disorder set.

---

## References

1. Grotzinger AD, Werme J, Peyrot WJ, et al. Mapping the genetic landscape across 14 psychiatric disorders. Nature. 2025. https://doi.org/10.1038/s41586-025-09820-3

2. Naqvi NH, Rudrauf D, Damasio H, Bechara A. Damage to the insula disrupts addiction to cigarette smoking. Science. 2007;315(5811):531-534. https://doi.org/10.1126/science.1135926

3. Naqvi NH, Bechara A. The insula and drug addiction: an interoceptive view of pleasure, urges, and decision-making. Brain Struct Funct. 2010;214(5-6):435-450. https://doi.org/10.1007/s00429-010-0268-7

4. Saunders GRB, Wang X, Chen F, et al. Genetic diversity fuels gene discovery for tobacco and alcohol use. Nature. 2022;612:720-724. https://doi.org/10.1038/s41586-022-05477-4

5. Liu M, Jiang Y, Wedow R, et al. Association studies of up to 1.2 million individuals yield new insights into the genetic etiology of tobacco and alcohol use. Nat Genet. 2019;51(2):237-244. https://doi.org/10.1038/s41588-018-0307-5

6. Bierut LJ, Stitzel JA, Wang JC, et al. Variants in nicotinic receptors and risk for nicotine dependence. Am J Psychiatry. 2008;165(9):1163-1171. https://doi.org/10.1176/appi.ajp.2008.07111711

7. Saccone SF, Hinrichs AL, Saccone NL, et al. Cholinergic nicotinic receptor genes implicated in a nicotine dependence association study. Hum Mol Genet. 2007;16(1):36-49.

8. Lerman C, Schnoll RA, Hawk LW Jr, et al. Use of the nicotine metabolite ratio as a genetically informed biomarker of response to nicotine patch or varenicline for smoking cessation: a randomised, double-blind placebo-controlled trial. Lancet Respir Med. 2015;3(2):131-138. https://doi.org/10.1016/S2213-2600(14)70294-2

9. Zangen A, Moshe H, Martinez D, et al. Repetitive transcranial magnetic stimulation for smoking cessation: a pivotal multicenter double-blind randomized controlled trial. World Psychiatry. 2021;20(3):397-404. https://doi.org/10.1002/wps.20905

10. Dinur-Klein L, Dannon P, Hadar A, et al. Smoking cessation induced by deep repetitive transcranial magnetic stimulation of the prefrontal and insular cortices: a prospective, randomized controlled trial. Biol Psychiatry. 2014;76(9):742-749. https://doi.org/10.1016/j.biopsych.2014.05.020

11. Fowler CD, Lu Q, Johnson PM, Marks MJ, Kenny PJ. Habenular alpha5 nicotinic receptor subunit signalling controls nicotine intake. Nature. 2011;471(7340):597-601. https://doi.org/10.1038/nature10009

12. Frahm S, Slimak MA, Ferrarese L, et al. Aversion to nicotine is regulated by the balanced activity of beta4 and alpha5 nicotinic receptor subunits in the medial habenula. Neuron. 2011;70(3):522-535. https://doi.org/10.1016/j.neuron.2011.04.013

13. Antolin-Fontes B, Ables JL, Gorlich A, Ibanez-Tallon I. The habenulo-interpeduncular pathway in nicotine aversion and withdrawal. Neuropharmacology. 2015;96(Pt B):213-222. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4452453/

14. Zhao-Shea R, DeGroot SR, Liu L, et al. Dynamic activity of interpeduncular nucleus GABAergic neurons controls expression of nicotine withdrawal. Neuropsychopharmacology. 2021;46(11):1925-1934. https://doi.org/10.1038/s41386-021-01107-1

15. Morales AM, Ghahremani D, Kohno M, Hellemann GS, London ED. Cigarette exposure, dependence, and craving are related to insula thickness in young adult smokers. Neuropsychopharmacology. 2014;39(8):1816-1822. https://doi.org/10.1038/npp.2014.48

16. Hatoum AS, Colbert SMC, Johnson EC, et al. Multivariate genome-wide association meta-analysis of over 1 million subjects identifies loci underlying multiple substance use disorders. Nat Ment Health. 2023;1:210-223. https://doi.org/10.1038/s44220-023-00034-y

17. Volkow ND, Koob GF, McLellan AT. Neurobiologic advances from the brain disease model of addiction. N Engl J Med. 2016;374(4):363-371. https://doi.org/10.1056/NEJMra1511480

18. Goldstein RZ, Volkow ND. Dysfunction of the prefrontal cortex in addiction: neuroimaging findings and clinical implications. Nat Rev Neurosci. 2011;12(11):652-669. https://doi.org/10.1038/nrn3119

19. Zilverstand A, Huang AS, Alia-Klein N, Goldstein RZ. Neuroimaging impaired response inhibition and salience attribution in human drug addiction: a systematic review. Neuron. 2018;98(5):886-903. https://doi.org/10.1016/j.neuron.2018.03.048

20. Zhang R, Volkow ND. Brain default-mode network dysfunction in addiction. Neuroimage. 2019;200:313-331. https://doi.org/10.1016/j.neuroimage.2019.06.036

21. Mansvelder HD, McGehee DS. Long-term potentiation of excitatory inputs to brain reward areas by nicotine. Neuron. 2000;27(2):349-357.

22. Mansvelder HD, Keath JR, McGehee DS. Synaptic mechanisms underlie nicotine-induced excitability of brain reward areas. Neuron. 2002;33(6):905-919.

23. Littel M, Euser AS, Munafo MR, Franken IHA. Electrophysiological indices of biased cognitive processing of substance-related cues: a meta-analysis. Neurosci Biobehav Rev. 2012;36(8):1803-1816. https://doi.org/10.1016/j.neubiorev.2012.05.001

24. Sutherland MT, McHugh MJ, Pariyadath V, Stein EA. Resting state functional connectivity in addiction: lessons learned and a road ahead. Neuropharmacology. 2012;62(7):2281-2295. https://doi.org/10.1016/j.neuropharm.2011.12.020

25. Addicott MA, Sweitzer MM, Froeliger B, Rose JE, McClernon FJ. Increased functional connectivity in an insula-based network is associated with improved smoking cessation outcomes. Neuropsychopharmacology. 2015;40(11):2648-2656. https://doi.org/10.1038/npp.2015.114

26. Mackey S, Allgaier N, Chaarani B, et al. Mega-analysis of gray matter volume in substance dependence: general and substance-specific regional effects. Am J Psychiatry. 2019;176(2):119-128. https://doi.org/10.1176/appi.ajp.2018.17040415

27. Anthenelli RM, Benowitz NL, West R, et al. Neuropsychiatric safety and efficacy of varenicline, bupropion, and nicotine patch in smokers with and without psychiatric disorders (EAGLES): a randomised, double-blind, placebo-controlled clinical trial. Lancet. 2016;387(10037):2507-2520. https://doi.org/10.1016/S0140-6736(16)30272-0

28. Rigotti NA, Benowitz NL, Prochaska JJ, et al. Cytisinicline for smoking cessation: the ORCA-2 randomized clinical trial. JAMA. 2023;330(2):152-160. https://doi.org/10.1001/jama.2023.10042

29. Johnson MW, Garcia-Romeu A, Cosimano MP, Griffiths RR. Pilot study of the 5-HT2AR agonist psilocybin in the treatment of tobacco addiction. J Psychopharmacol. 2014;28(11):983-992. https://doi.org/10.1177/0269881114548296

30. Hancock DB, Guo Y, Reginsson GW, et al. Genome-wide association study across European and African American ancestries identifies a SNP in DNMT3B contributing to nicotine dependence (iNDiGO Consortium). Mol Psychiatry. 2018;23(9):1911-1919. https://doi.org/10.1038/mp.2017.193

31. Joubert BR, Felix JF, Yousefi P, et al. DNA methylation in newborns and maternal smoking in pregnancy: genome-wide consortium meta-analysis. Am J Hum Genet. 2016;98(4):680-696. https://doi.org/10.1016/j.ajhg.2016.02.019

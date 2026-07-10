# Biotypes: Opioid Use Disorder (OUD)

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: researchers, stakeholders
> **Tags**: `literature-synthesis`, `disease-biotypes`, `sud-opioid`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)

Genomic factor loading (Nature 2025): **Substance use factor** (shared with alcohol, nicotine, and cannabis use disorders). Grotzinger et al., Mapping the genetic landscape across 14 psychiatric disorders, Nature 2025 (doi:10.1038/s41586-025-09820-3, 1,056,201 cases). The substance use factor groups alcohol, opioid, nicotine, and cannabis use disorders; the shared signal across all 14 disorders was enriched for broad transcriptional regulation, while the substance use factor carries more specific reward and addiction biology.

Opioid use disorder is distinctive among substance use disorders because its primary pharmacological lever, the mu-opioid receptor, is also its strongest genetic signal, and because the syndrome is dominated by a physiologically severe withdrawal state driven by central noradrenergic hyperactivity. This combination makes OUD the substance use disorder with the clearest molecular target (OPRM1), the clearest medication-defined biotypes (response to methadone, buprenorphine, and naltrexone), and a withdrawal phenotype that maps onto a specific brainstem node (locus coeruleus) rather than only cortical and striatal circuitry. The document harmonizes molecular, connectomic, and phenotypic evidence to Gene Ontology, the Allen Human Reference Atlas 3D (2020), and SNOMED CT/HPO respectively, and ends with the most defensible cross-scale biotypes. Replication status is flagged throughout. Person-first language is used: people with opioid use disorder, not "addicts."

## Seed papers

- Koob & Volkow 2016 (three-stage neurocircuitry: binge/intoxication, withdrawal/negative affect, preoccupation/anticipation), Lancet Psychiatry, doi:10.1016/S2215-0366(16)00104-8.
- Zhou et al. 2020 (OPRM1 functional coding variant rs1799971 GWAS, Million Veteran Program), Mol Psychiatry, doi:10.1038/s41380-020-0677-9.
- Kember, Gelernter et al. 2022 (cross-ancestry OUD meta-analysis, 14 loci, predominant brain effects, OPRM1 + FURIN), Nat Neurosci, doi:10.1038/s41593-022-01160-z.
- Deak et al. 2022 (multi-trait GWAS of opioid addiction, OPRM1 and beyond, 19 loci), Mol Psychiatry, doi:10.1038/s41380-022-01709-1.
- Lichenstein, Scheinost, Potenza, Carroll, Yip 2021 (dissociable opioid vs cocaine connectome substrates), Mol Psychiatry, doi:10.1038/s41380-019-0586-y.
- Hutchinson & Watkins 2014 (TLR4 microglial neuroimmune signaling in opioids), Neuropharmacology, doi:10.1016/j.neuropharm.2013.05.043.
- Seney et al. 2021 (postmortem DLPFC/NAc transcriptomics, neuroinflammation, synaptic remodeling in OUD), Biol Psychiatry, doi:10.1016/j.biopsych.2021.06.007.
- Gondre-Lewis et al. / Wang et al. on NAc DBS for refractory OUD 2023 (Journal of Neurosurgery), doi:10.3171/2023.3.JNS222112.

---

## MICRO scale (molecular / genetic / cellular / immune) vs GO-harmonized

OUD molecular biotyping centers on six axes: the mu-opioid receptor system (the defining and pharmacologically actionable axis), dopaminergic reward signaling, glutamatergic plasticity that underlies tolerance and dependence, central noradrenergic drive that produces the withdrawal syndrome, neuroinflammatory TLR4/microglial signaling, and neurotrophin-gated reward plasticity in the ventral tegmental area. The substance use factor in Grotzinger et al. 2025 anchors the shared genetic reward biology; OUD-specific signal converges on OPRM1.

| Biotype / dysregulation | GO term(s) + ID | Specific finding (genes, variants, molecules) | Neurotransmitter family | BDNF / neurotrophin + plasticity? | E/I imbalance (+ region) | Oxidative / mito / ROS? | Immune / inflammatory? | Confidence | Source (author year, DOI) |
|---|---|---|---|---|---|---|---|---|---|
| Mu-opioid receptor signaling (CENTRAL, pharmacologically actionable) | G protein-coupled opioid receptor signaling pathway (GO:0038003); mu-type opioid receptor activity (GO:0004988, approx, needs curation) | OPRM1 rs1799971 (A118G, N40D): the key OUD variant; G allele alters receptor expression/beta-endorphin binding; genome-wide significant for OUD in MVP. OPRD1 (delta), OPRK1 (kappa, withdrawal/dysphoria) implicated secondarily | none reported (opioidergic; modulates dopamine, GABA, glutamate downstream) | not direct | indirect: mu-receptor on GABAergic VTA interneurons -> disinhibits dopamine (E/I shift in VTA) | not reported | not direct | HIGH (OPRM1 GWAS-significant, replicated cross-ancestry) | Zhou et al. 2020, doi:10.1038/s41380-020-0677-9; Kember et al. 2022, doi:10.1038/s41593-022-01160-z |
| Dopaminergic reward hypofunction (incentive sensitization + reward deficit) | dopamine receptor signaling pathway (GO:0007212); dopamine secretion (GO:0014046) | Reduced striatal D2/D3 availability and blunted ventral striatal reward response in OUD; DRD2 implicated in cross-substance addiction factor; opioids disinhibit VTA dopamine via mu-receptors on GABA interneurons | **Dopamine** | not direct | indirect (VTA disinhibition) | not reported | not direct | HIGH (cross-substance dopamine model); MEDIUM for opioid-specific PET (radioligand competition harder to interpret) | Koob & Volkow 2016, doi:10.1016/S2215-0366(16)00104-8; Volkow & Koob 2016, doi:10.1056/NEJMra1511480 |
| Glutamatergic NMDA plasticity (tolerance, dependence, sensitization) | glutamatergic synaptic transmission (GO:0035249); NMDA glutamate receptor activity (GO:0004972, approx, needs curation); regulation of synaptic plasticity (GO:0048167) | Chronic opioids drive NMDA-dependent plasticity underlying tolerance and physical dependence; GRIN/GRIA candidate genes; postmortem OUD shows altered glutamatergic pyramidal-neuron gene expression in DLPFC | **Glutamate** | yes (NMDA-dependent LTP/LTD; substrate of tolerance) | candidate E-up in NAc/VTA glutamatergic afferents | not reported | not reported | MEDIUM (strong rodent mechanism; human evidence transcriptomic) | Seney et al. 2021, doi:10.1016/j.biopsych.2021.06.007 |
| Central noradrenergic hyperdrive (CENTRAL to withdrawal) | norepinephrine secretion (GO:0048243, approx, needs curation); adrenergic receptor signaling pathway (GO:0071875); response to morphine (GO:0043278) | Locus coeruleus NE neurons are suppressed by acute opioids (presynaptic mu-receptor) and undergo compensatory hyperactivity; withdrawal triggers LC-NE surge driving autonomic storm; the alpha-2 agonist target for clonidine/lofexidine | **Norepinephrine** | not direct | LC-NE hyperexcitability (region: locus coeruleus -> cortical/limbic NE surge) | not reported | not direct | HIGH (classic LC mechanism, strong rodent + pharmacological validation) | Koob & Volkow 2016, doi:10.1016/S2215-0366(16)00104-8; Aghajanian noradrenergic withdrawal model (see refs) |
| Endogenous opioid / enkephalin and dynorphin-kappa tone (negative affect) | opioid receptor signaling pathway (GO:0038003); neuropeptide signaling pathway (GO:0007218) | Withdrawal/negative-affect stage shows increased dynorphin/kappa-opioid tone in striatum and extended amygdala; reduced enkephalin reward signaling; PENK/PDYN candidate genes | none reported (opioid peptides) | not direct | not direct | not reported | not direct | MEDIUM (rodent-anchored; human kappa-PET emerging) | Koob 2015, doi:10.1016/j.ejphar.2014.11.044 |
| GABAergic disinhibition (VTA) and cortical GABA deficit | GABAergic synaptic transmission (GO:0051932) | Mu-receptors on VTA GABAergic interneurons mediate dopamine disinhibition (the core reward mechanism); postmortem OUD shows decreased GABAergic interneuron markers in DLPFC | **GABA** (+ glutamate at affected synapses) | not direct | **I-down** in DLPFC (interneuron marker loss); disinhibition in VTA | not reported | not reported | MEDIUM (VTA mechanism HIGH in rodents; human postmortem MEDIUM) | Seney et al. 2021, doi:10.1016/j.biopsych.2021.06.007 |
| Neuroinflammation: TLR4 / microglial activation | toll-like receptor 4 signaling pathway (GO:0034142); microglial cell activation (GO:0001774); inflammatory response (GO:0006954) | Morphine binds TLR4 at the MD2 site, activating microglia to release IL-1beta, TNF-alpha, IL-6, and BDNF, modulating reward and tolerance; (+)-naloxone (TLR4 antagonist enantiomer) reduces opioid reinforcement; gut-microglia TLR4 axis via LPS | none reported | yes (microglial BDNF release modulates reward plasticity) | not direct | candidate (microglial ROS) | **yes** (TLR4, IL-1beta, TNF-alpha, IL-6, microglia) | MEDIUM-HIGH (robust rodent mechanism; human postmortem converging) | Hutchinson & Watkins 2014, doi:10.1016/j.neuropharm.2013.05.043; Salvo et al. 2022, doi:10.3389/fnins.2022.1050661 |
| VTA BDNF / neurotrophin plasticity (opioid-specific reversal) | neurotrophin TRK receptor signaling pathway (GO:0048011); positive regulation of long-term synaptic potentiation (GO:1900273) | Opioids paradoxically DECREASE BDNF in VTA (opposite to stimulants which increase it); reduced VTA BDNF shrinks dopamine soma size and shifts reward signaling; chronic morphine alters BDNF-TrkB in NAc | **Dopamine** (downstream); **Glutamate** (plasticity) | **yes** vs opioid-specific decrease in VTA BDNF; distinguishes opioids from psychostimulants | not direct | not reported | not reported | MEDIUM (replicated rodent finding; human data sparse) | Koo et al. 2012 BDNF-VTA opioid work (see refs) |
| Postmortem transcriptomic signature (neuroinflammation + synaptic remodeling, sex-specific) | inflammatory response (GO:0006954); synapse organization (GO:0050808) | DLPFC and NAc in OUD show upregulated neuroinflammatory genes and dysregulated synaptic/myelin genes; striatal transcriptional signatures are sex-specific and partly concordant with rodent models | none reported | not direct | not reported | not reported | **yes** (microglial/inflammatory module) | MEDIUM (single-consortium postmortem) | Seney et al. 2021, doi:10.1016/j.biopsych.2021.06.007; Mews et al. 2023 (sex-specific striatal concordance) |

**GWAS anchor.** Opioid use disorder is among the most heritable substance use disorders (twin estimates ~50 percent) but has been gene-hunting-limited by case ascertainment. Zhou et al. 2020 (Million Veteran Program plus Yale-Penn and SAGE, ~10,544 cases of European ancestry plus African-ancestry samples) reported the OPRM1 functional coding variant rs1799971 (A118G) at genome-wide significance, the first robust single-variant OUD association, with the locus tagging mu-opioid receptor biology directly (doi:10.1038/s41380-020-0677-9). Kember, Gelernter et al. 2022 conducted a cross-ancestry meta-analysis in the Million Veteran Program (n approximately 425,944) and identified 14 OUD loci (12 novel), confirming OPRM1 and identifying FURIN, with effects predominantly enriched in brain regions associated with addiction (doi:10.1038/s41593-022-01160-z). Deak et al. 2022 applied multi-trait analysis of GWAS (MTAG) across opioid-related phenotypes (effective n drawing on >639,000 samples) and recovered 19 independent loci including OPRM1, FURIN, PPP6C, RABEPK, FBXW4, NCAM1, and KCNN1 (doi:10.1038/s41380-022-01709-1). Across all three, OPRM1 is the load-bearing, biology-anchored signal, and OUD heritability is highly polygenic beyond it. Polygenic scores explain only a small fraction of variance and weight priors over biotype membership rather than defining a biotype alone. The Hatoum et al. 2023 cross-substance addiction-rf (PDE4B, DRD2, FTO) places OUD on the shared substance use factor (doi:10.1038/s44220-023-00034-y).

---

## MESO scale (connectomic) vs Allen Atlas nodes + edges

Reference: Allen Human Reference Atlas 3D 2020 (141 anatomical regions). Functional labels and Brodmann areas appear in parentheses; the Allen anatomical container is named first. OUD shows less gray-matter loss than alcohol or stimulant use disorders; its signature is predominantly in CONNECTIVITY between prefrontal control regions and ventral striatum, plus a distinctive brainstem withdrawal node (locus coeruleus) not prominent in other substance use disorders. The Volkow-Koob three-node scaffold (ventral/dorsal striatum, prefrontal control, extended amygdala/insula) applies, with the addition of periaqueductal gray and locus coeruleus for the pain/withdrawal axis.

### NODES

| Allen region (functional label) | Observed change | Modality | Confidence | Source |
|---|---|---|---|---|
| Striatum, ventral (nucleus accumbens) | **Blunted** response to non-drug reward; **exaggerated** response to drug cues (incentive sensitization); reduced D2/D3 binding | fMRI (task), PET | HIGH (cross-substance); MEDIUM (opioid-specific PET) | Koob & Volkow 2016, doi:10.1016/S2215-0366(16)00104-8 |
| Striatum, dorsal (caudate + putamen) | **Recruitment** with chronic use (habit/compulsive transition, ventral-to-dorsal shift) | fMRI, PET | MEDIUM (clearer for cocaine/alcohol than opioids) | Everitt & Robbins 2013, doi:10.1016/j.neubiorev.2013.02.010 |
| Frontal cortex, orbital part (OFC / BA11, BA47) | **Hyperreactivity** to drug cues; reduced metabolism at rest (valuation dysfunction) | fMRI, PET | MEDIUM-HIGH | Goldstein & Volkow 2011, doi:10.1038/nrn3119 |
| Frontal cortex, medial prefrontal, ventral (vmPFC / BA10, BA32) | **Altered** valuation and cue reactivity; reduced control over striatal drive | fMRI | MEDIUM | Goldstein & Volkow 2011, doi:10.1038/nrn3119 |
| Frontal cortex, dorsolateral prefrontal (dlPFC / BA9, BA46) | **Hypofunction** during inhibitory control (Go/NoGo, Stop Signal); the rTMS/deep-TMS craving target | fMRI, TMS | MEDIUM-HIGH | Zilverstand et al. 2018, doi:10.1016/j.neuron.2018.03.048 |
| Insula, anterior part (anterior insula) | **Hyperreactivity** during cue-induced craving (interoceptive urge); coupling scales with craving | fMRI | HIGH (insula-craving robust across substances) | Naqvi & Bechara 2010, doi:10.1007/s00429-010-0268-7 |
| Amygdala + extended amygdala (central nucleus; BNST as adjacent node) | **Hyperreactivity** to negative cues; elevated CRF/dynorphin tone in withdrawal/negative-affect stage | fMRI | MEDIUM-HIGH | Koob 2015, doi:10.1016/j.ejphar.2014.11.044 |
| Periaqueductal gray (PAG, midbrain) | **Altered** descending pain modulation; hyperalgesia in withdrawal and protracted abstinence; mu-receptor-dense | fMRI, mechanistic | MEDIUM (mechanistically central; human imaging sparse) | Koob & Volkow 2016, doi:10.1016/S2215-0366(16)00104-8 |
| Locus coeruleus (pons; OPIOID-DISTINCTIVE withdrawal node) | **Hyperactivity** during withdrawal (NE surge); the clonidine/lofexidine target; suppressed by acute opioids | fMRI, mechanistic | HIGH (classic mechanism; human LC imaging emerging) | Aghajanian LC withdrawal model (see refs); Koob & Volkow 2016 |
| Thalamus (mediodorsal + intralaminar) | **Altered** connectivity with prefrontal and striatal nodes; arousal/salience relay | fMRI | MEDIUM | Lichenstein et al. 2021, doi:10.1038/s41380-019-0586-y |
| Scalp EEG (frontocentral; not an Allen parcel) | **P300 amplitude reduction** to target/oddball stimuli; **altered cue-reactivity** (enhanced LPP/P300 to drug cues) | EEG (ERP) | MEDIUM (P300 reduction replicated across SUDs) | EEG addiction ERP literature (see refs) |

### EDGES

| Region A vs Region B (functional labels) | Association sign | Observed change in disorder | Modality | Confidence | Source |
|---|---|---|---|---|---|
| Nucleus accumbens vs frontal cortex orbital part (ventral striatum vs OFC; reward/valuation circuit) | normally `positive` | OUD: **altered** reward-circuit coupling; the predominant opioid structural-functional change is in PFC-ventral striatum connectivity rather than gray-matter loss | fMRI | MEDIUM-HIGH | Lichenstein et al. 2021, doi:10.1038/s41380-019-0586-y; Koob & Volkow 2016 |
| Frontal cortex dorsolateral prefrontal vs striatum (dlPFC vs striatum; fronto-striatal control) | normally `negative (anticorrelation)` (top-down control over striatal drive) | OUD: **weakened** fronto-striatal control (control deficit), reduced prefrontal regulation of incentive drive | fMRI | MEDIUM-HIGH | Zilverstand et al. 2018, doi:10.1016/j.neuron.2018.03.048 |
| Anterior insula vs nucleus accumbens / OFC (insula vs reward circuit; craving) | normally `positive` | OUD: **increased** insula-reward coupling during cue-induced craving (interoceptive urge drives reward circuit) | fMRI | MEDIUM-HIGH | Naqvi & Bechara 2010, doi:10.1007/s00429-010-0268-7 |
| Locus coeruleus vs cortex/limbic (NE projection; withdrawal) | normally `positive` (arousal) | Withdrawal: **surge** of LC-NE output drives autonomic storm; alpha-2 agonists (clonidine/lofexidine) suppress this edge | mechanistic, fMRI | HIGH (mechanism); MEDIUM (human connectivity) | Aghajanian LC model; Koob & Volkow 2016 |
| Whole-brain connectome vs opioid treatment outcome (CPM fingerprint) | n/a (predictive network) | A pretreatment functional connectivity pattern predicts OUD treatment outcome; DISSOCIABLE from the cocaine-predictive network (limited cross-substance generalization, supporting substance-specific biotypes) | fMRI (connectome-based predictive modeling) | MEDIUM (modest samples, limited prospective external validation) | Lichenstein, Scheinost, Potenza, Carroll, Yip 2021, doi:10.1038/s41380-019-0586-y |
| Default mode network (precuneus/PCC vs mPFC) vs salience network | normally `negative (anticorrelation)` | SUDs including OUD: **altered** DMN-salience anti-correlation predicts craving/relapse; transdiagnostic craving network spans DMN, salience, frontoparietal | fMRI | MEDIUM | Garrison et al. 2023, doi:10.1176/appi.ajp.21121207; Zhang & Volkow 2019, doi:10.1016/j.neuroimage.2019.06.036 |

**Connectome-based predictive modeling (the strongest individualized-biotype case).** Lichenstein, Scheinost, Potenza, Carroll, and Yip 2021 derived dissociable whole-brain functional fingerprints for opioid versus cocaine use using connectome-based predictive modeling, finding limited cross-substance generalization and supporting substance-specific neural biotypes (doi:10.1038/s41380-019-0586-y). These models are the strongest case for individualized functional biotyping in OUD, but most CPM studies use modest samples (n approximately 40 to 150) and few have prospective external validation in independent clinics. Treat them as state-of-art directional evidence, not deployment-ready biomarkers. The NIH HEAL Initiative is funding individual-level predictive modeling of OUD treatment outcome to address the sample-size and external-validation gaps.

**Replication caveat.** Robust cross-cohort findings: insula-craving coupling, blunted ventral-striatal non-drug reward response, fronto-striatal control deficits, and the locus coeruleus NE withdrawal mechanism. The CPM opioid-treatment fingerprint has only modest-sample within-consortium support. P300 reduction is replicated broadly across substance use disorders but is not opioid-specific.

---

## MACRO scale (phenotype) vs SNOMED CT / HPO

OUD phenotype dimensions map onto the DSM-5/ICD-11 criteria (impaired control, social impairment, risky use, pharmacological criteria of tolerance and withdrawal) and onto the Koob three-stage cycle. HPO coverage of addiction-specific psychiatric phenotypes is sparse, so several HPO cells are marked approx/needs curation and mapped to the nearest superordinate concept. SNOMED CT has good coverage of opioid dependence, withdrawal, and overdose.

| Biotype phenotype | SNOMED CT term + ID | HPO term + ID | Short description of observations that led to this mapping | Source |
|---|---|---|---|---|
| Opioid use disorder (diagnosis anchor) | Opioid dependence (75544000); Opioid use disorder (1259360002, approx, needs curation) | Drug dependence (HP:0030858, approx, needs curation) | Full DSM-5/ICD-11 syndrome; substance use factor; loads on shared addiction biology | Grotzinger et al. 2025, doi:10.1038/s41586-025-09820-3 |
| Craving (preoccupation/anticipation stage) | Craving (713346003, approx, needs curation); Drug craving (711021008, approx, needs curation) | (no precise HPO term; map to Drug dependence HP:0030858, needs curation) | Cue-induced urge; insula and reward-circuit reactivity; transdiagnostic craving network; predicts relapse | Naqvi & Bechara 2010; Garrison et al. 2023, doi:10.1176/appi.ajp.21121207 |
| Compulsive use despite harm (impaired control) | Compulsive drug use (terminology under opioid dependence categories, approx, needs curation) | (map to Drug dependence HP:0030858, needs curation) | Continued use despite negative consequences; ventral-to-dorsal striatal habit transition; fronto-striatal control deficit | Everitt & Robbins 2013, doi:10.1016/j.neubiorev.2013.02.010 |
| Tolerance (pharmacological criterion) | Drug tolerance (62014003, approx, needs curation) | Drug tolerance (no precise HPO; needs curation) | Need for increasing dose; NMDA-dependent plasticity; reduced mu-receptor signaling efficacy | Seney et al. 2021, doi:10.1016/j.biopsych.2021.06.007 |
| Opioid withdrawal syndrome (CENTRAL, severe; withdrawal/negative-affect stage) | Opioid withdrawal syndrome (33807004); Neonatal opioid withdrawal (NAS, 88476002, approx) | (map to Drug withdrawal; no precise HPO, needs curation) | Autonomic storm (sweating, piloerection, mydriasis, tachycardia, diarrhea, myalgia), dysphoria; locus coeruleus NE surge; clonidine/lofexidine target | Koob & Volkow 2016, doi:10.1016/S2215-0366(16)00104-8 |
| Opioid-induced hyperalgesia / protracted dysphoria | Opioid-induced hyperalgesia (approx, needs curation); Anhedonia (66704007, approx) | Anhedonia (HP:0033676, approx, needs curation) | Heightened pain sensitivity and negative affect in withdrawal/abstinence; PAG descending modulation, dynorphin/kappa tone, reward deficit | Koob 2015, doi:10.1016/j.ejphar.2014.11.044 |
| Opioid overdose (respiratory depression) | Opioid overdose (242253008, approx, needs curation); Poisoning by opiate (242253008 family) | (no precise HPO; map to Respiratory insufficiency HP:0002093, needs curation) | Mu-receptor-mediated brainstem respiratory depression; the overdose-risk dimension; naloxone reversal target | clinical; Volkow & Koob 2016, doi:10.1056/NEJMra1511480 |

**Koob three-stage mapping.** The macro phenotype organizes onto Koob & Volkow's three stages: (1) binge/intoxication (basal ganglia; dopamine release in NAc shell, drug-cue reactivity), (2) withdrawal/negative affect (extended amygdala + locus coeruleus; CRF and dynorphin/kappa tone, NE surge, anhedonia, dysphoria), and (3) preoccupation/anticipation (prefrontal cortex; craving, control deficits) (doi:10.1016/S2215-0366(16)00104-8). The cycle is heuristic, not strict staging; most people show signatures of all three stages simultaneously with shifting relative weights. The opioid-distinctive emphasis is the severity of the stage-2 withdrawal physiology and the overdose-risk overlay that no other substance use disorder carries to the same degree.

---

## Interventional studies (incl. neuromodulation, DBS, neuroplastogens)

Medication for opioid use disorder (MOUD) is the gold standard and is itself the strongest source of treatment-defined biotypes: full agonist (methadone), partial agonist (buprenorphine), and antagonist (naltrexone) responders. Pharmacogenetic modulation by OPRM1 A118G is the leading molecular stratifier, though clinical utility remains contested. Neuromodulation (TMS) and experimental DBS target the craving and control circuits; neuroplastogens are early-stage with anti-addictive signals.

| Biotype it targets | Intervention (class + specific) | Study (author year, design, n) | Outcome | Confidence | Source |
|---|---|---|---|---|---|
| Mu-receptor / full-agonist responder (the largest MOUD group) | Full mu agonist: methadone (maintenance) | Decades of RCT and cohort evidence; CYP2B6/CYP3A4 metabolic variants modulate dose | Gold-standard reduction in illicit use, overdose, and mortality; retention superior to many alternatives | HIGH (gold standard) | Crist et al. 2018, doi:10.1080/00952990.2018.1454934 |
| Mu-receptor / partial-agonist responder (OPRM1 A118G may modulate) | Partial mu agonist: buprenorphine (with naloxone) | Multiple RCTs; pharmacogenetic work on OPRM1 A118G; plasma 2-3 ng/ml optimizes outcomes | Reduces use, craving, withdrawal, overdose; OPRM1 G allele alters buprenorphine efficacy in allele-specific manner (animal/in vitro), but no clinical pharmacogenomic guideline exists | HIGH (efficacy); LOW-MEDIUM (OPRM1 stratification clinical utility contested) | Hser et al. 2022, doi:10.3389/fpsyt.2022.1085877; buprenorphine pharmacogenomics review, doi:10.1038/s41397-020-00198-1 |
| Mu-receptor / antagonist responder (OPRM1 effects; high-control, motivated abstainers) | Antagonist: extended-release naltrexone (XR-naltrexone) | RCT evidence; OPRM1 A118G G-carriers reported to respond better (parallels alcohol naltrexone work, contested) | Blocks reward, prevents relapse once detoxified; requires opioid-free induction; OPRM1 G-allele subgroup signal not consistently replicated prospectively | MEDIUM (efficacy in abstinent patients); LOW (OPRM1 stratification) | OPRM1 review, doi:10.2147/PGPM.S210600 |
| Noradrenergic withdrawal biotype (locus coeruleus NE surge) | Alpha-2 adrenergic agonist: lofexidine (FDA-approved), clonidine (off-label) | Lofexidine RCTs for opioid withdrawal | Reduces withdrawal-stage autonomic symptoms by suppressing LC-NE surge; adjunct, not maintenance | HIGH (lofexidine FDA-approved for withdrawal) | clinical; Koob & Volkow 2016, doi:10.1016/S2215-0366(16)00104-8 |
| Craving / prefrontal-control biotype (dlPFC, insula) | rTMS / deep TMS to left dlPFC | Mixed RCTs: single-blind rTMS showed craving reduction (Shen et al.); accelerated deep TMS double-cone (Guldas et al. 2025) reduced craving and limited buprenorphine dose escalation but did not reach significance | Emerging; craving-reduction signal inconsistent at controlled-trial level | LOW-MEDIUM (emerging, mixed) | Guldas et al. 2025, doi:10.1111/adb.70057; single-blind rTMS trial, PMC9795937 |
| Refractory OUD (reward circuit; experimental) | DBS: nucleus accumbens / ventral capsule (NAc/VC) | Open-label single-arm safety/feasibility trial in treatment-refractory OUD (Journal of Neurosurgery 2023); fentanyl-use-disorder case report 2024 | Safe and feasible; two participants sustained abstinence >1150 and >520 days with reduced craving, anxiety, depression; relapses still common; sham-controlled RCT initiating | LOW (small, open-label, experimental) | NAc DBS trial 2023, doi:10.3171/2023.3.JNS222112; systematic review, doi:10.1038/s41398-024-03060-1 |
| Reward circuit (experimental, noninvasive) | Low-intensity focused ultrasound (LIFU) to NAc | Safety/feasibility trial of NAc LIFU for substance use disorder | Reduced cue-induced craving; safe and feasible; very early | LOW (single feasibility study) | LIFU NAc trial, PMC10540197 |
| Anti-addictive neuroplastogen (experimental; cardiac caution) | Ibogaine / 18-MC (oneirogen, mu and NMDA/nicotinic activity) | Cherian et al. 2024: magnesium-ibogaine in 30 special-operations veterans with TBI (primary outcomes PTSD/depression/cognition, NOT an OUD RCT); historical observational ibogaine opioid-detox reports (Brown & Alper 2018) | Veteran study: large PTSD/depression reductions, increased theta (neuroplasticity), no serious adverse events with magnesium co-administration; observational opioid reports show strong withdrawal/craving reduction from single dosing; QT prolongation/cardiac arrhythmia is the limiting safety concern | LOW (anti-addictive signal observational; cardiac safety constrains development) | Cherian et al. 2024, doi:10.1038/s41591-023-02705-w; Brown & Alper 2018, doi:10.1080/00952990.2017.1320802 |
| Neuroinflammatory biotype (TLR4/microglia) | TLR4 antagonist (preclinical); ibudilast (glial modulator, repurposed) | Preclinical (+)-naloxone TLR4 antagonism; early ibudilast signals in SUD | Reduces opioid reinforcement/tolerance in rodents; human translation early | LOW (preclinical/early) | Hutchinson & Watkins 2014, doi:10.1016/j.neuropharm.2013.05.043 |

**Note on ibogaine framing.** The Stanford Cherian et al. 2024 Nature Medicine study (Nolan Williams group) treated special-operations veterans with traumatic brain injury and used PTSD, depression, and cognition as primary outcomes, not opioid use. It is included here because ibogaine's mechanism (theta-mediated neuroplasticity, multi-receptor including mu and NMDA action) underlies its longstanding observational anti-addictive reputation for opioid detoxification (Brown & Alper 2018), and because the magnesium co-administration protocol addresses the QT-prolongation cardiac risk that has constrained ibogaine development. It is not an OUD efficacy trial.

---

## Most defensible biotypes (cross-scale synthesis)

Five biotypes are defensible from the OUD literature and map cleanly to anchor Allen regions a Cytognosis-style spectroscopy headset could target. Three share substrate with the cross-substance biotypes in the broader addiction synthesis; two are opioid-distinctive.

**Biotype 1: Mu-opioid / pharmacogenetic responder (OPRM1 A118G).** OPRM1 rs1799971 genotype interacts with mu-receptor signaling to shape response to buprenorphine and naltrexone. MICRO: OPRM1 A118G, mu-receptor GPCR signaling. MESO anchor: ventral striatum (NAc), VTA disinhibition. MACRO: craving, impaired control. Lever: MOUD selection (methadone/buprenorphine/naltrexone); OPRM1 stratification is the leading but contested molecular biotype. Confidence: HIGH for OPRM1 GWAS signal, LOW-MEDIUM for clinical pharmacogenetic stratification.

**Biotype 2: Noradrenergic withdrawal (opioid-distinctive).** Locus coeruleus NE hyperactivity produces the severe autonomic withdrawal syndrome unique in its prominence to opioids. MICRO: noradrenergic hyperdrive, alpha-2 adrenergic signaling. MESO anchor: locus coeruleus (pons), periaqueductal gray. MACRO: opioid withdrawal syndrome, hyperalgesia. Lever: lofexidine/clonidine. Confidence: HIGH (mechanism and pharmacology).

**Biotype 3: Craving / insula-reward (cross-substance).** Anterior insula hyperreactivity drives cue-induced craving coupled to the reward circuit. MICRO: dopaminergic reward, glutamatergic cue plasticity. MESO anchor: anterior insula, NAc, OFC. MACRO: craving, relapse risk. Lever: rTMS/deep TMS to dlPFC (emerging, mixed), cue-exposure therapy. Confidence: HIGH (insula-craving); LOW-MEDIUM (TMS).

**Biotype 4: Fronto-striatal control deficit (cross-substance).** Weakened dlPFC top-down control over striatal incentive drive; the preoccupation/anticipation stage. MICRO: cortical GABAergic interneuron deficit, glutamatergic dysregulation. MESO anchor: dlPFC, dorsal/ventral striatum, thalamus. MACRO: compulsive use despite harm. Lever: dlPFC neuromodulation, contingency management. Confidence: MEDIUM-HIGH.

**Biotype 5: Neuroinflammatory (TLR4/microglial; shared with alcohol and methamphetamine).** Morphine-TLR4 microglial activation modulating reward and tolerance, with a gut-microglia axis. MICRO: TLR4 signaling, IL-1beta/TNF-alpha/IL-6, microglial activation, paradoxical VTA BDNF decrease. MESO anchor: insula (interoceptive readout), VTA. MACRO: tolerance, dysphoria. Lever: glial modulators (ibudilast), TLR4 antagonists (preclinical). Confidence: MEDIUM-HIGH (mechanism); LOW (human therapeutic translation).

**Genomic factor statement.** Opioid use disorder loads on the **substance use factor** (alcohol + opioid + nicotine + cannabis) in Grotzinger et al. 2025, with OPRM1 as the opioid-distinctive, biology-anchored signal layered on the shared cross-substance reward genetics (DRD2, PDE4B, FTO).

---

## References

1. Grotzinger AD, Werme J, Peyrot WJ, et al. Mapping the genetic landscape across 14 psychiatric disorders. Nature. 2025. https://doi.org/10.1038/s41586-025-09820-3

2. Koob GF, Volkow ND. Neurobiology of addiction: a neurocircuitry analysis. Lancet Psychiatry. 2016;3(8):760-773. https://doi.org/10.1016/S2215-0366(16)00104-8

3. Volkow ND, Koob GF, McLellan AT. Neurobiologic advances from the brain disease model of addiction. N Engl J Med. 2016;374(4):363-371. https://doi.org/10.1056/NEJMra1511480

4. Zhou H, Rentsch CT, Cheng Z, et al. Association of OPRM1 functional coding variant with opioid use disorder: a genome-wide association study. Mol Psychiatry. 2020. https://doi.org/10.1038/s41380-020-0677-9

5. Kember RL, Vickers-Smith R, Xu H, et al. Cross-ancestry meta-analysis of opioid use disorder uncovers novel loci with predominant effects in brain regions associated with addiction. Nat Neurosci. 2022;25(10):1279-1287. https://doi.org/10.1038/s41593-022-01160-z

6. Deak JD, Zhou H, Galimberti M, et al. Genome-wide association study in individuals of European and African ancestry and multi-trait analysis of opioid use disorder identifies 19 independent genome-wide significant risk loci. Mol Psychiatry. 2022;27(10):3970-3979. https://doi.org/10.1038/s41380-022-01709-1

7. Lichenstein SD, Scheinost D, Potenza MN, Carroll KM, Yip SW. Dissociable neural substrates of opioid and cocaine use identified via connectome-based modelling. Mol Psychiatry. 2021;26(8):4383-4393. https://doi.org/10.1038/s41380-019-0586-y

8. Koob GF. The dark side of emotion: the addiction perspective. Eur J Pharmacol. 2015;753:73-87. https://doi.org/10.1016/j.ejphar.2014.11.044

9. Goldstein RZ, Volkow ND. Dysfunction of the prefrontal cortex in addiction: neuroimaging findings and clinical implications. Nat Rev Neurosci. 2011;12(11):652-669. https://doi.org/10.1038/nrn3119

10. Zilverstand A, Huang AS, Alia-Klein N, Goldstein RZ. Neuroimaging impaired response inhibition and salience attribution in human drug addiction: a systematic review. Neuron. 2018;98(5):886-903. https://doi.org/10.1016/j.neuron.2018.03.048

11. Everitt BJ, Robbins TW. From the ventral to the dorsal striatum: devolving views of their roles in drug addiction. Neurosci Biobehav Rev. 2013;37(9 Pt A):1946-1954. https://doi.org/10.1016/j.neubiorev.2013.02.010

12. Naqvi NH, Bechara A. The insula and drug addiction: an interoceptive view of pleasure, urges, and decision-making. Brain Struct Funct. 2010;214(5-6):435-450. https://doi.org/10.1007/s00429-010-0268-7

13. Hutchinson MR, Watkins LR. Why is neuroimmunopharmacology crucial for the future of addiction research? Neuropharmacology. 2014;76 Pt B:218-227. https://doi.org/10.1016/j.neuropharm.2013.05.043

14. Salvo E, Stokes P, Keogh CE, et al. Linking the gut microbiome to microglial activation in opioid use disorder. Front Neurosci. 2022;16:1050661. https://doi.org/10.3389/fnins.2022.1050661

15. Seney ML, Kim SM, Glausier JR, et al. Transcriptional alterations in dorsolateral prefrontal cortex and nucleus accumbens implicate neuroinflammation and synaptic remodeling in opioid use disorder. Biol Psychiatry. 2021;90(8):550-562. https://doi.org/10.1016/j.biopsych.2021.06.007

16. Hatoum AS, Colbert SMC, Johnson EC, et al. Multivariate genome-wide association meta-analysis of over 1 million subjects identifies loci underlying multiple substance use disorders. Nat Ment Health. 2023;1:210-223. https://doi.org/10.1038/s44220-023-00034-y

17. Crist RC, Li J, Doyle GA, et al. Pharmacogenetic analysis of opioid dependence treatment dose and dropout rate. Am J Drug Alcohol Abuse. 2018;44(4):431-440. https://doi.org/10.1080/00952990.2018.1454934

18. Hser YI, Saxon AJ, Mooney LJ, et al. Buprenorphine exposure levels to optimize treatment outcomes in opioid use disorder. Front Psychiatry. 2022;13:1085877. https://doi.org/10.3389/fpsyt.2022.1085877

19. Brown TK, Alper K. Treatment of opioid use disorder with ibogaine: detoxification and drug use outcomes. Am J Drug Alcohol Abuse. 2018;44(1):24-36. https://doi.org/10.1080/00952990.2017.1320802

20. Cherian KN, Keynan JN, Anker L, et al. Magnesium-ibogaine therapy in veterans with traumatic brain injuries. Nat Med. 2024;30(2):373-381. https://doi.org/10.1038/s41591-023-02705-w

21. Wang TR, Moosa S, Dallapiazza RF, et al. Safety and feasibility clinical trial of nucleus accumbens deep brain stimulation for treatment-refractory opioid use disorder. J Neurosurg. 2023;140(1):231-239. https://doi.org/10.3171/2023.3.JNS222112

22. Guldas A, et al. Deep transcranial magnetic stimulation in patients with opioid use disorder: a double-blind, placebo-controlled randomized trial. Addict Biol. 2025;30(6):e70057. https://doi.org/10.1111/adb.70057

23. Garrison KA, Sinha R, Potenza MN, et al. Transdiagnostic connectome-based prediction of craving. Am J Psychiatry. 2023;180(6):445-453. https://doi.org/10.1176/appi.ajp.21121207

24. Zhang R, Volkow ND. Brain default-mode network dysfunction in addiction. Neuroimage. 2019;200:313-331. https://doi.org/10.1016/j.neuroimage.2019.06.036

25. OPRM1 A118G polymorphisms and its role in opioid addiction: implication on severity and treatment approaches. Pharmgenomics Pers Med. 2019;12:361-372. https://doi.org/10.2147/PGPM.S210600

26. Kong X, et al. A review of the existing literature on buprenorphine pharmacogenomics. Pharmacogenomics J. 2021;21(2):128-139. https://doi.org/10.1038/s41397-020-00198-1

27. Coles AS, et al. A systematic review of deep brain stimulation for substance use disorders. Transl Psychiatry. 2024;14:341. https://doi.org/10.1038/s41398-024-03060-1

28. Mahoney JJ, Haut MW, Carpenter J, et al. Low-intensity focused ultrasound targeting the nucleus accumbens as a potential treatment for substance use disorder: safety and feasibility clinical trial. Front Psychiatry. 2023;14:1211566. https://pmc.ncbi.nlm.nih.gov/articles/PMC10540197/

29. Mews P, Cunningham AM, Scarpa J, et al. Sex-specific concordance of striatal transcriptional signatures of opioid addiction in human and rodent brains. (PMC11469374). https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11469374/

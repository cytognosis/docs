# Molecular and Cellular Cross-Cutting Biotypes for the Cytognosis + Marie-Nelly Mental-Health Coordinate Proposal

Author: Cytognosis Foundation research synthesis (NSF X-Labs Phase 0 / ARPA-H PHO supporting evidence)
Date: 25 May 2026

## Purpose and scope

The connectomic biotype layer in the parent synthesis (`transdiagnostic-connectomic-synthesis.md`) describes patients in terms of large-scale brain network state. That layer is necessary but not sufficient. Connectomic biotypes sit at the top of a causal cascade that runs genes -> molecules -> cells -> circuits -> behavior. The Cytoverse map needs explicit molecular and cellular axes so that two patients with apparently similar connectomic biotypes can still be distinguished by the molecular driver (and therefore the rational treatment match). This document specifies six cross-cutting molecular and cellular axes, maps each axis across the six disorders in the proposal (MDD, SCZ, BD, anxiety/OCD, PTSD, addiction; with autism noted where relevant), and proposes 5-8 cross-disorder molecular biotypes that complement the connectomic biotypes.

Effect sizes are reported where the underlying meta-analysis quantifies them. Single-lab claims and questionable replication are flagged. The molecular axis treatment of psychedelics relies on the four foundational papers in this proposal's PDF library (Shkundin and Halaris 2023; Moliner et al. 2023; Casarotto, Umemori, Castren 2022; Park et al. 2025) read in full.

---

## 1. BDNF / TrkB neurotrophin signaling: the big one

### 1.1 Biology in one paragraph

Brain-derived neurotrophic factor (BDNF) is a neurotrophin encoded on chromosome 11p14.1 with two principal forms: pro-BDNF, which binds the p75 neurotrophin receptor (p75NTR) and its co-receptor sortilin to drive long-term depression and apoptosis, and mature BDNF (m-BDNF), which binds tropomyosin receptor kinase B (TrkB; gene NTRK2) and drives dendritic outgrowth, synaptogenesis, LTP, and synaptic plasticity (Shkundin and Halaris 2023, doi:10.3390/jpm13091395). Pro-BDNF is cleaved intracellularly into m-BDNF; their relative proportion shifts across development from pro-BDNF dominant in early postnatal life to m-BDNF dominant in adulthood. BDNF expression is regulated by neuronal activity, and BDNF antisense lncRNA (BDNF-AS / BDNFOS) suppresses BDNF mRNA. The BDNF/BDNF-AS locus thus operates as a balance, and SNPs in either gene shift it.

### 1.2 The Val66Met polymorphism (rs6265)

rs6265 (C>T, G196A, Val66Met) is the most studied missense variant in human neurobiology. It changes valine to methionine at codon 66 in the prodomain of pro-BDNF, disrupting activity-dependent transport of BDNF mRNA to dendrites and reducing regulated BDNF secretion (Shkundin and Halaris 2023). The Met allele is essentially absent in Native American and most African populations, has a frequency of ~20-30% in Europeans, and reaches >40-50% in some East Asian populations (Shkundin and Halaris 2023). This explains a substantial fraction of the cross-study heterogeneity in BDNF psychiatric genetic literature; pooled effects ignoring ethnicity are biased.

Pharmacogenetic findings most relevant to the proposal:

- SSRI response: a 2014 meta-analysis (Niitsu et al., reviewed in Shkundin and Halaris 2023; see also Yan et al., doi:10.1016/j.pharmthera.2014.05.003) finds Met carriers respond modestly better than Val/Val, but the effect is small (OR roughly 1.3) and is concentrated in Asian samples; mixed-ancestry trials show no effect. Pathak et al. 2022 reported Met carriers had a more favorable response to antidepressant treatment in an Indian MDD cohort.
- Ketamine response: Laje et al. 2012 (PMC3569155) and Chen et al. 2021 reported that Val/Val carriers respond better to subanesthetic ketamine than Met carriers in treatment-resistant depression. Rodrigues et al. 2024 (J Psychopharmacol) failed to replicate in a larger repeated-IV-ketamine TRD sample, suggesting the effect is real but small.
- ECT response: Pathak et al. 2022 (Behav Brain Res) found lower serum BDNF in MDD patients correlated with greater post-ECT improvement; Viikki et al. 2013 reported rs11030101 TA carriers had diminished ECT response.
- TMS response: Heterogeneous; Cheeran et al. 2008 found Met carriers showed reduced plasticity-like responses to TMS in healthy humans, an effect that has been replicated patchily.
- Exercise response: Szuhany et al. 2015 meta-analysis (J Psychiatr Res) shows BDNF responsiveness to exercise is modulated by Val66Met; some studies show Met carriers benefit less from exercise-induced cognitive improvement, but Soler et al. 2022 found AA carriers (recessive Met homozygotes by a different SNP coding) actually benefited more from physical activity against childhood stress.
- Cognitive flexibility: Met carriers show smaller hippocampus and PFC, lower episodic memory, and reduced fractional anisotropy of the uncinate fasciculus (Carballedo et al. 2012; Shen et al. 2020).

The treatment-stratified picture is that Val/Val and Met/Met carriers represent two pharmacogenetic biotypes whose response curves to BDNF-engaging treatments differ. In the proposal's framework, this is a wearable-genome integration point: cheek-swab genotype paired with serum BDNF, fNIRS-CCO, and EEG aperiodic slope would stratify treatment selection.

### 1.3 Other BDNF/BDNF-AS SNPs across MDD, SCZ, BD (extracted from Shkundin and Halaris 2023)

The Loyola review screened 14 BDNF/BDNF-AS SNPs against MDD, SCZ, and BD. Key findings beyond rs6265:

- rs11030101 (BDNF intron / BDNF-AS non-coding transcript variant, alleles A>G/A>T): AT genotype associated with diminished ECT response in TRD (Viikki et al. 2013); the AA genotype at rs11030101 is enriched among SCZ patients with prominent negative symptoms (Ping et al. 2022).
- rs11030104 (A>G, intron in both BDNF and BDNF-AS): T/T genotype overrepresented among antipsychotic responders in European SCZ (Zai et al. 2012); minor allele predicts antipsychotic resistance on clozapine therapy (Zhang et al. 2013), with high LD to rs10501087 and rs6265.
- rs10835210 (C>A/C>G): CA genotype enriched among BD and SCZ versus MDD and controls (Pae et al. 2012); the A allele drives positive symptoms in Han Chinese SCZ (Zhang et al. 2016).
- rs2049046 (T>A, BDNF intron): T allele predicts antidepressant response in acute MDD and is associated with lower post-treatment cortisol on the dex/CRH test (Hennings et al. 2019), suggesting BDNF-HPA axis crosstalk biotype.
- rs61888800 (G>C/G>T): T carriers shift toward novelty-seeking temperament during recovery from MDD on SSRI (Andre et al. 2018); T allele linked to lower BDNF expression in frontal cortex.
- rs2030324 (A>G): CC/CT genotypes overrepresented in Han Chinese SCZ; combined effects with NOTCH4 rs520688 (Yang et al. 2013); drug-naive first-episode SCZ patients with TT/TC perform worse on language and attention.
- rs28383487 (G>T, 5' UTR): CA variant correlates with delayed onset of paranoid SCZ in Polish men (Suchanek et al. 2012); strong LD with Val66Met.
- rs16917237 (G>T): G allele more frequent in BD-I, BD-II, and schizoaffective bipolar (Ivanova et al. 2013).
- rs11030094 (BDNF-AS intron, G>A): G allele beneficial for antidepressant response in MDD and modulates HPA axis regulation (Hennings et al. 2019).
- rs1519480 (BDNF-AS intron): A/A genotype associated with antipsychotic-induced weight gain (Zai et al. 2012); T allele linked to lower BDNF mRNA in prefrontal cortex and lower NAA levels in PFC (Salehi et al. 2013), suggesting it taps mitochondrial / myelin readouts (NAA is a neuronal-mitochondrial integrity marker).
- rs10501087 (BDNF-AS intron, T>C/T>G): minor allele increases antipsychotic resistance in Caucasian SCZ (Zhang et al. 2013); haplotypic association with suicidality in TRD.

Across MDD, SCZ, and BD the picture from Shkundin and Halaris is that no single BDNF SNP is monogenic for any disorder, but haplotype combinations and gene-gene interactions (e.g., BDNF x NTRK2 in TRD per Li et al. 2013; BDNF x DRD3 in BD with comorbid anxiety per Chang et al. 2013; BDNF x COMT in BD-II per Lee et al. 2013) define risk and treatment-response strata. The recurring theme is that the SAME locus (BDNF) tilts risk for THREE syndromically distinct disorders, which is exactly what a cross-disorder molecular biotype framework needs.

### 1.4 The psychedelic-TrkB mechanism (Moliner et al. 2023; Casarotto, Umemori, Castren 2022; Park et al. 2025)

The Castren and Saarma groups have established that classical psychedelics, ketamine, and conventional antidepressants (SSRIs, tricyclics) converge on a single molecular pivot: direct binding to the transmembrane domain (TMD) of TrkB dimers, which allosterically potentiates endogenous BDNF signaling. Key results:

- LSD and psilocin bind TrkB with affinities ~1,000-fold higher than fluoxetine and ketamine: K_i for LSD ~3.38 nM, psilocin ~6.73 nM, fluoxetine ~4.77 microM, ketamine ~21 microM at TrkB (Moliner et al. 2023, doi:10.1038/s41593-023-01316-5, Fig. 1b; Park et al. 2025 Tables 2-3).
- The binding site is at residues Y433, A434, V436, V437 of the TrkB TMD. Point mutation Y433F (a single tyrosine-to-phenylalanine substitution) abolishes binding of LSD, psilocin, fluoxetine, and ketamine to TrkB, while preserving BDNF binding and downstream signaling. In heterozygous Y433F+/- mice, the antidepressant-like behavioral effects of LSD and fluoxetine are lost, but BDNF responses are intact (Moliner et al. 2023, Casarotto, Umemori, Castren 2022 doi:10.3389/fnmol.2022.1032224).
- The plasticity-promoting effects of psychedelics on TrkB dimerization, dendritic spine density, dendritic arbor complexity, and BDNF-dependent neurite outgrowth are INDEPENDENT of 5-HT2A activation: the 5-HT2A antagonist M100907 and ketanserin do not block LSD/psilocin-induced TrkB dimerization or spinogenesis. By contrast, the head-twitch response (rodent proxy for hallucinogenic activity) is BLOCKED by M100907 (5-HT2A antagonist) and INTACT in Y433F+/- mice (Moliner et al. 2023, Figs 4-7).
- Mechanistically, psychedelics stabilize the crossed conformation of the TrkB TMD dimer at C-alpha distance ~17 Angstroms; fluoxetine binds deeper at C-alpha ~20 Angstroms, locking a different conformation. So all four drug classes converge on TrkB but produce subtly different conformations, which may explain the divergent kinetics.

This is one of the most important transdiagnostic mechanistic findings of the past decade because it implies that:
1. The hallucinogenic and antidepressant effects of psychedelics are dissociable in principle (Casarotto, Umemori, Castren 2022 discussion; Park et al. 2025 section on biased 5-HT2A agonism).
2. A high-affinity TrkB positive allosteric modulator without 5-HT2A activity would retain plasticity-promoting and antidepressant effects without hallucinations. This is the rational basis for "non-hallucinogenic psychedelics" (Olson lab; Lumateperone, IHCH-7086).
3. The shared mechanism explains why ECT, ketamine, psilocybin, LSD, SSRIs, exercise, and even VNS all elevate BDNF/TrkB signaling and induce iPlasticity, a state of juvenile-like enhanced plasticity (Umemori et al. 2018; Castren and Antila 2017).

### 1.5 Per-disorder mapping

MDD: low serum BDNF in active MDD is one of the most replicated peripheral biomarkers in psychiatry; Molendijk et al. 2014 meta-analysis (N=9484, 179 associations) found a moderate effect size (d~0.5) for reduced serum BDNF in unmedicated MDD versus controls. Antidepressant treatment, ECT, and rTMS all normalize serum BDNF (Polyakova et al. 2015 meta-analysis, doi:10.1016/j.jad.2014.10.023; Rocha et al. 2016, doi:10.1016/j.jpsychires.2016.08.004). Higher baseline serum BDNF predicts better antidepressant response (Halaris et al. 2015). The honest limit: serum BDNF derives largely from platelets and assays vary by 5-10x across labs; serum BDNF is at best a noisy proxy for brain BDNF (Naegelin et al. 2018 eNeuro; Seifert et al. 2010).

SCZ: peripheral BDNF reductions in SCZ are real but smaller than in MDD (Fernandes et al. 2015 Mol Psychiatry meta-analysis); postmortem brain shows mixed findings, with reduced BDNF mRNA in DLPFC and hippocampus in some studies (Ray et al. 2011, 2014, doi:10.1038/tp.2014.26). BDNF + TNF-alpha haplotype combinations predict cognitive impairment in SCZ (Zhang et al. 2018).

BD: BDNF decreases in plasma during depressive and manic episodes and recovers in euthymia (Fernandes et al. 2015 BMC Med meta-analysis, 52 studies). The m-BDNF/pro-BDNF ratio differentiates BD from MDD in depressive episodes (Zhao et al. 2017, doi:10.1007/s12035-016-0098-6), a potential differential-diagnosis biomarker.

PTSD: literature is sparser; Felmingham et al. 2013 and Nicholson et al. 2023 (Sci Rep) suggest the Val66Met polymorphism moderates emotional recognition memory and exposure therapy response. Met carriers show poorer extinction learning in lab paradigms, consistent with the role of BDNF in fear extinction (Soliman et al. 2010; Casarotto et al. 2021 showed fear extinction depends on TrkB binding).

Addiction: this is where BDNF gets disorder-specific and even drug-specific in an important way. The Russo and Nestler line of work shows:
- Cocaine increases striatal BDNF (especially in nucleus accumbens shell), which promotes cocaine seeking (Graham et al. 2007 Nat Neurosci). Cocaine and BDNF have a positive feedback in mesolimbic circuits.
- Alcohol DECREASES dorsolateral striatal BDNF; restoration of BDNF/TrkB signaling in DLS suppresses compulsive alcohol intake (Ron lab, e.g., Logrip et al. 2009; Hopkins et al. 2025 review).
- This drug-specific divergence kills any naive "BDNF is good or BDNF is bad" framing for addiction. The proposal should treat addiction as a regional-BDNF-signature biotype rather than a global one.

Autism: limited evidence; some studies report altered pro-BDNF/m-BDNF proteolytic balance in postmortem ASD brain (Garcia et al. 2012, doi:10.1097/NEN.0b013e31824b1c69), but the literature is small.

### 1.6 Treatment-stratified biotypes

We can identify candidate molecular biotypes of treatment response that the Cytoverse should commit to:

- BDNF-high, plasticity-competent biotype: better response to SSRIs, ketamine, psychedelics, TMS, and ECT. Wearable proxy: high baseline serum BDNF, Val/Val genotype, intact fNIRS hemodynamic responsivity.
- BDNF-low, plasticity-deficit biotype: poorer response to all of the above; may need higher-dose, longer-duration, or combination therapy (e.g., psychedelic + behavioral activation). This biotype overlaps with the Castren "iPlasticity-resistant" phenotype and probably defines treatment-resistant depression and a fraction of negative-symptom-dominant SCZ.

### 1.7 Honest limits

Serum BDNF assays vary by manufacturer (R&D vs. Promega ELISA kits give different absolute values; Polacchini et al. 2015 Sci Rep). Platelet activation during venipuncture inflates serum BDNF. Plasma BDNF is closer to brain release but is much lower and noisier. Capillary serum BDNF from finger-prick is a Cytognosis-feasible wearable readout but has not been validated against brain BDNF; this is an open methodological question that the Cytoverse program should fund.

---

## 2. Excitatory / inhibitory (E/I) imbalance

### 2.1 Background

E/I imbalance refers to disturbed ratio of glutamatergic (excitatory; NMDA, AMPA, kainate, mGluR receptors) to GABAergic (inhibitory; GABA-A, GABA-B receptors) signaling, often analyzed at the level of cortical interneuron subtypes. The three main cortical interneuron classes:
- Parvalbumin (PV) fast-spiking interneurons: provide perisomatic inhibition and pace gamma oscillations (30-80 Hz).
- Somatostatin (SST) interneurons: provide dendritic inhibition.
- Vasoactive intestinal peptide (VIP) interneurons: disinhibit principal cells by inhibiting SST/PV cells.

The original Rubenstein-Merzenich 2003 framework (Genes Brain Behav, doi:10.1034/j.1601-183x.2003.00037.x) proposed E/I imbalance as a unifying mechanism for autism. Sohal and Rubenstein 2019 Mol Psych (doi:10.1038/s41380-019-0426-0) extended this to schizophrenia, intellectual disability, and stress-related disorders. PV deficits, gamma oscillation abnormalities, and impaired plasticity now constitute a transdiagnostic axis.

### 2.2 In vivo readouts

- MRS-measured glutamate (Glu), glutamine (Gln), and GABA in vivo at 3T or 7T.
- Aperiodic 1/f EEG slope: the Donoghue / Voytek FOOOF algorithm (Donoghue et al. 2020 Nat Neurosci) separates aperiodic (1/f) and periodic (oscillatory) EEG components. Steeper (more negative) aperiodic exponent indicates stronger inhibition; flatter slope indicates more excitation, validated against MEG, ECoG, and computational models (Gao et al. 2017 NeuroImage). Aperiodic slope is wearable-feasible with low-channel-count consumer EEG and is the single most promising in vivo E/I biomarker for the Cytoscope platform.
- TMS-EEG paired-pulse paradigms (short-interval intracortical inhibition, SICI; long-interval, LICI) measure GABA-A and GABA-B mediated inhibition, respectively.

### 2.3 Per-disorder

SCZ: postmortem meta-analysis (Kaar et al. 2019 J Neural Transm, PMC6856257) shows PV interneuron density reduction in prefrontal cortex with Hedges' g = -0.27 (p=0.03, N=274 patients vs 275 controls); PV mRNA reduction Hedges' g = -0.44 (non-significant, p=0.12). This is a small effect at the group level but is replicated across many cohorts (Lewis group at Pittsburgh; Glausier and Lewis 2017). MRS shows elevated cortical glutamate/glutamine in early SCZ (Marsman et al. 2013, doi:10.1093/schbul/sbr069) and Marsman et al. 2014 Schiz Bull found medial frontal cortex glutamate moderated by measurement quality. Treatment-resistant SCZ (no clozapine response) shows persistent ACC glutamate elevations (Egerton et al. 2018 Mol Psych; Mouchlianitis et al. 2016).

ASD: extensive evidence for E/I imbalance across genetic syndromes - SHANK3, NLGN3/4, NRXN1, MeCP2, TSC1/2 (tuberous sclerosis), FMR1 (fragile X) - all converge on synaptic balance via mTOR or synaptic adhesion (Bourgeron 2015 Nat Rev Neurosci). MEG and EEG show reduced gamma-band coherence and altered aperiodic slope in ASD (Wilson et al. 2007; Edgar et al. 2015; Manyukhina et al. 2022).

MDD: reduced GABA in occipital and PFC (Sanacora et al. 1999, 2004 Arch Gen Psych; Sanacora and Saricicek 2007 review). Meta-analysis (Romeo et al. 2018 Am J Psychiatry; Schur et al. 2016) confirms cortical GABA reductions. Ketamine's antidepressant mechanism involves a transient NMDA-receptor-mediated glutamate surge (mGluR2-disinhibition hypothesis, Moghaddam and Adams 1998; Duman lab; Park et al. 2025) followed by AMPAR-mediated synaptogenesis and BDNF release via TrkB - tying E/I axis back to axis 1.

Anxiety / OCD: glutamate elevations in cortico-striato-thalamo-cortical (CSTC) circuits in OCD (Pittenger et al. 2011; Brennan et al. 2015 Biol Psychiatry).

PTSD: hippocampal glutamate elevations in some studies (Rosso et al. 2014 Biol Psychiatry); GABA-A receptor decrease on PET.

Addiction: striatal glutamate elevations during craving (Kalivas 2009 Nat Rev Neurosci).

### 2.4 Treatment implications

NMDA modulators: ketamine, esketamine (FDA-approved), AV-101 (kynurenine pathway prodrug, Phase 2 failure), NRX-101, MK-0657 (NR2B antagonist), dextromethorphan-bupropion combination, GLYX-13 / rapastinel (NMDA partial agonist, Phase 3 failure). The trial track record is mixed and stratification has been weak (Park et al. 2025 Table 1).

mGluR2/3 agonists: pomaglumetad methionil (LY2140023, Eli Lilly) had a positive Phase 2 in SCZ but failed three Phase 3 trials in 2012 and was discontinued (Stauffer et al. 2013, doi:10.1371/journal.pone.0080112; Adams et al. 2014, PMC3977437). The likely explanation is that pomaglumetad helps an mGluR2-defined subgroup but not the broader population - a stratification failure consistent with the proposal's molecular-biotype thesis.

GABA-A positive modulators: zuranolone (FDA-approved 2023 for postpartum depression) targets GABA-A and shows rapid effects.

PV-specific interventions: the Castren group's optoTrkB activation specifically in PV interneurons replicates iPlasticity (Winkel et al. 2021 Mol Psychiatry). PV-targeting is the next-generation TrkB story.

---

## 3. Oxidative stress / mitochondrial dysfunction

### 3.1 Background

Brain consumes ~20% of resting oxygen and is exquisitely sensitive to redox imbalance. Glutathione (GSH) is the brain's principal antioxidant; ROS (reactive oxygen species) generated by mitochondrial complexes I and III oxidize lipids, proteins, and DNA. Mitochondrial dysfunction includes reduced ATP production, increased ROS, decreased mitochondrial membrane potential, and impaired mitophagy.

### 3.2 Per-disorder

SCZ: reduced anterior cingulate GSH on MRS, modest effect (Das et al. 2018 Neurosci Biobehav Rev; Iwata et al. 2018 J Psychopharmacol meta-analysis); a separate variance meta-analysis (Murray et al. 2022, PMC8669304) shows SCZ INCREASES the VARIANCE of brain GSH, suggesting a subset of patients are dramatically GSH-deficient. The Geneva group's MDC1 gene-environment model (Cabungcal, Do) supports a PV-interneuron-oxidative-stress vulnerability axis.

BD: oxidative stress markers (lipid peroxides, 8-OHdG, protein carbonyls) elevated in active mania and depression (Berk et al. 2011 Neurosci Biobehav Rev; Yao group). Lithium's mechanism includes antioxidant effects and GSK3-beta inhibition that supports mitochondrial biogenesis.

ASD: Rossignol and Frye 2012 Mol Psychiatry meta-analysis (doi:10.1038/mp.2010.136) found that ~5% of children with ASD meet criteria for classical mitochondrial disease, but ~30% show biomarker evidence of mitochondrial dysfunction (elevated lactate 78%, pyruvate 45%; reduced ATP). This defines the "mitochondrial ASD subtype," a clear molecular biotype with high prevalence among ASD individuals with regression, seizures, and GI symptoms.

MDD: meta-analytic evidence for oxidative stress markers (Black et al. 2015 Psychoneuroendocrinology; Liu et al. 2015 Sci Rep). 8-OHdG (DNA damage marker) is the most consistent peripheral finding.

PTSD: mitochondrial dysfunction in peripheral immune cells (Mellon et al. 2018, 2019 Mol Psychiatry).

Addiction: alcohol is direct mitochondrial toxin via acetaldehyde and complex I inhibition (Hoek et al. 2002).

### 3.3 Treatment

N-acetylcysteine (NAC) as a glutathione precursor:
- SCZ: Berk et al. 2008 Biol Psychiatry RCT positive; 2020 meta-analysis (Yolland et al. J Psychopharmacol, doi:10.1177/0269881119899428) shows modest benefit for total symptoms and negative symptoms at >=24 weeks. Effect is concentrated in chronic SCZ.
- BD: Berk et al. 2008 multicenter RCT showed NAC benefit for depressive symptoms (effect size d~0.7).
- Trichotillomania, gambling, cannabis use: small but positive trials.
- The replication picture is mixed and the NAC effect is small at the group level; this is exactly the pattern expected if NAC is highly effective in an oxidative-stress-positive subgroup and ineffective elsewhere.

CoQ10, l-carnitine, and Frye's "mitochondrial cocktail" for ASD have small open-label and single RCT evidence; replication is poor.

Lithium's mitochondrial actions: lithium increases mitochondrial complex I/III activity and reduces lipid peroxidation (Maurer et al. 2009; Andreazza et al. 2010). The "lithium responder" biotype in BD may overlap with the mitochondrial biotype.

### 3.4 The Cytoscope wearable readout: cytochrome-c-oxidase

This is the single most important integration point for the proposal. Cytochrome-c-oxidase (CCO) is the terminal enzyme of the mitochondrial respiratory chain and accounts for >95% of cellular oxygen consumption. Its redox state (oxidized vs. reduced) directly reports mitochondrial energy metabolism. CCO has distinct absorption peaks in the near-infrared (775-870 nm region) that can be resolved by broadband NIRS. The Tachtsidis group at UCL (Bale et al. 2016 J Biomed Opt; Kaynezhad et al. 2018 Adv Exp Med Biol PMC6716511) has pioneered both benchtop and wearable broadband NIRS for cerebral CCO measurement. The MW-FlexNIRS system (2024) is an LED-based wearable multi-wavelength NIRS device that can recover CCO in neonates and adults.

A pilot MDD study (Holper et al. 2019 Sci Rep PMC6716511) demonstrated that brain CCO measured by broadband NIRS distinguishes MDD patients from controls and tracks state changes. This is the cleanest in vivo wearable mitochondrial readout available.

For the Cytoverse map: pair finger-prick capillary BDNF + saliva cortisol + broadband fNIRS-CCO + low-channel EEG aperiodic slope = a four-channel molecular biotype signature that runs on a wearable.

---

## 4. Dopaminergic dysfunction

### 4.1 Background

Dopamine has D1-D5 receptors organized into D1-like (D1, D5; Gs-coupled) and D2-like (D2, D3, D4; Gi-coupled) families. Striatal DA originates from substantia nigra pars compacta (nigrostriatal, motor) and ventral tegmental area (mesolimbic, reward; mesocortical, cognition). Presynaptic DA synthesis capacity, vesicular packaging, release, and reuptake (DAT) are all separately measurable with PET (e.g., [18F]-DOPA for synthesis; [11C]-raclopride for D2 displacement).

### 4.2 Per-disorder

SCZ: presynaptic striatal hyperdopaminergia is the most robust finding in psychiatric neuroimaging (Howes and Kapur 2009 Schiz Bull; Howes et al. 2012 Arch Gen Psych meta-analysis effect size d~0.8). Howes proposed that the final common pathway from genetic and environmental risk factors converges on increased presynaptic striatal DA. Cortical hypodopaminergia in DLPFC contributes to negative and cognitive symptoms (Davis et al. 1991; Goldman-Rakic). Treatment-resistant SCZ may have a different DA biotype: a Demjaha et al. 2012 study suggested non-responders to first-line antipsychotics do NOT show striatal DA elevation, indicating a distinct mechanism (glutamate or PV/inhibition). Howes' Type A / Type B nomenclature (proposed in several reviews) maps responders to typical antipsychotics (Type A, hyperdopaminergic) vs. treatment-resistant (Type B, glutamate-driven).

Parkinson's disease: nigrostriatal DA loss; included here for contrast with SCZ.

ADHD: prefrontal hypodopaminergia is the dominant model (Volkow et al. 2009); supports stimulant treatment.

MDD: anhedonic / reward-deficit biotype is dopaminergic. Treadway and Zald 2011 mapped anhedonia to ventral striatum DA. Bupropion (DA/NE reuptake inhibitor) and pramipexole (D3 agonist) target this biotype. The Drysdale 2017 connectomic biotype 3 with anhedonia-dominant symptoms likely overlaps.

Addiction: Volkow framework (Volkow et al. 1997 Nature; Volkow and Morales 2015 Cell): acute drug effects increase mesolimbic DA; chronic addiction depletes striatal D2/D3 receptors, especially in dorsal striatum. The shift from ventral (reward) to dorsal (habit) striatal control of behavior is a core feature.

PTSD: limited direct DA evidence; some COMT and DRD2 SNP findings.

ASD: striatal DA findings limited and inconsistent.

### 4.3 Treatment-stratified

Amphetamine response: SCZ patients with hyperdopaminergic biotype paradoxically show worsened symptoms with amphetamine challenge (Lieberman et al. 1987); this challenge could in principle stratify Type A vs. Type B.

Modafinil: weak DA reuptake inhibition; works in narcolepsy and ADHD.

Aripiprazole: D2 partial agonist; works across SCZ, BD mania, MDD augmentation. Its broad cross-diagnostic utility makes sense as a "stabilizer" of an axis that runs across disorders.

---

## 5. Serotonergic dysregulation

### 5.1 Background

5-HT has 14 receptor subtypes across seven families. Most relevant to psychiatry:
- 5-HT1A: autoreceptor (raphe), heteroreceptor (cortex, hippocampus); buspirone partial agonist
- 5-HT1B: presynaptic autoreceptor on serotonergic terminals; potential antidepressant target (Park et al. 2025; Fleury et al. 2024 bioRxiv)
- 5-HT2A: target of classical psychedelics; cortical glutamatergic neurons; mediates head-twitch in rodents and hallucinogenic effects in humans
- 5-HT2C: GABAergic neurons in VTA; suppresses DA release; mediates dose-dependent psychedelic effects
- 5-HT3: ligand-gated cation channel; ondansetron antagonist; expressed in cortical and limbic GABAergic interneurons
- 5-HTT (SERT): the SSRI target

### 5.2 The 5-HT2A receptor and psychedelics

Classical psychedelics (LSD, psilocybin / psilocin, DMT) are partial agonists at 5-HT2A. Affinities from Park et al. 2025 Table 3: psilocin K_i ~25 nM at 5-HT2A (rat) and ~120-478 nM at human; LSD ~3.38 nM at TrkB but also nanomolar at 5-HT2A. Two binding modes at 5-HT2A: the orthosteric pocket (canonical, Gq-biased, hallucinogenic) and an extended binding pocket (EBP) at residue L362 (beta-arrestin-biased, non-hallucinogenic) (Cao et al. 2022 Science doi:10.1126/science.abl8615; Wallach et al. 2023 Nat Commun PMC10325044). This biased agonism is the basis for non-hallucinogenic psychedelics: lumateperone, IHCH-7086, and TBG (Olson lab) preferentially engage beta-arrestin and produce antidepressant-like effects in rodents without head-twitch responses.

The Castren and Park et al. reviews argue that 5-HT2A activation is NOT required for psychedelic antidepressant effects in animal models because 5-HT2A antagonists (ketanserin, M100907) fail to block all of: TrkB dimerization, dendritic spine increases, dendritic arbor complexity, BDNF gene expression, and antidepressant-like behavioral changes (Moliner et al. 2023; Hesselgrave et al. 2021 PNAS; Cameron et al. 2021 Nature). Hutten et al. 2019 also reported that microdose LSD elevates plasma BDNF in humans without producing subjective psychedelic effects.

In contrast, other studies argue 5-HT2A activation IS necessary for human therapeutic effects (Olson 2018; Vargas et al. 2023 Science doi:10.1126/science.adf0435 showed psychedelics work via INTRACELLULAR 5-HT2A receptors, and that intracellular delivery is the relevant compartment). The Vargas finding that psilocin (membrane-permeable) but not serotonin (not permeable) reaches intracellular 5-HT2A receptors is one reconciling model.

For the proposal: the two mechanisms (5-HT2A and TrkB) are best understood as parallel, mutually compatible, and probably synergistic, and the relative contribution may itself define biotypes - patients with low-TrkB-affinity ligand response and high-5-HT2A response would benefit more from classical psilocybin sessions plus psychotherapy; patients with intact TrkB signaling but blunted plasticity from depression might respond to non-hallucinogenic TrkB-PAMs without subjective effects.

### 5.3 Per-disorder

MDD: the 5-HT hypothesis (Coppen 1967; Schildkraut 1965) drove the development of SSRIs. Moncrieff et al. 2022 Mol Psych umbrella review (doi:10.1038/s41380-022-01661-0) concluded that direct 5-HT measures do not support a simple deficiency model; their critics (King's College London 2022 response; Jauhar et al. 2023) noted the umbrella review confounded "no convincing evidence" with "evidence of no effect," and that tryptophan-depletion studies in remitted MDD patients DO produce relapse, supporting some role for serotonin. The honest synthesis: 5-HT is one of several modulators, and SSRI response is heterogeneous - which is the central biotype claim.

Anxiety: SSRIs and SNRIs are first-line for generalized anxiety, panic, and social anxiety; effect sizes modest (d~0.3-0.4 in meta-analyses).

SCZ: 5-HT2A is a key target of atypical antipsychotics (clozapine, olanzapine, risperidone); the 5-HT2A/D2 affinity ratio defines "atypical."

OCD: SRI specificity - tricyclics with serotonergic action (clomipramine) and SSRIs work, but noradrenergic tricyclics (desipramine) do not. This pharmacological dissociation supports a 5-HT subtype in OCD.

PTSD: SSRI evidence is weaker than for MDD; sertraline and paroxetine FDA-approved but effect sizes small (d~0.2-0.3).

Addiction: ondansetron (5-HT3 antagonist) reduces alcohol intake in a 5'-HTTLPR-LL/rs1042173-TT pharmacogenetic subgroup (Johnson et al. 2011, 2013 Am J Psych doi:10.1176/appi.ajp.2013.12091163). Combining HTR3A/HTR3B + SLC6A4 genotypes expands the target cohort from ~20% to ~34% of alcoholics with predicted ondansetron response. This is the clearest example in psychiatry of a molecular biotype that maps directly to a drug response.

ASD: SSRIs for repetitive behaviors - mixed evidence; STAART meta-analysis showed no significant benefit (King et al. 2009 Arch Gen Psych).

---

## 6. Cross-axis convergence

Genes -> molecules -> cells -> circuits -> behavior is the explicit causal chain. The five axes above co-vary in real patients:

- BDNF / TrkB and E/I converge in PV interneurons: TrkB activation in PV cells reduces PV excitability via Kv3.1 downregulation, disinhibiting pyramidal cells and increasing gamma oscillations (Winkel et al. 2021). This is one molecular pathway that ties iPlasticity to gamma-band EEG.
- BDNF and oxidative stress converge in mitochondrial biogenesis: BDNF-TrkB signaling upregulates PGC-1alpha and increases mitochondrial biogenesis (Cheng et al. 2012 J Neurosci). A low-BDNF biotype is also probably a low-mitochondrial-reserve biotype.
- BDNF and dopamine converge in nucleus accumbens: BDNF in NAc shell INCREASES depression-like behavior (Eisch et al. 2003); the dopaminergic anhedonia biotype is partly a BDNF/NAc biotype.
- 5-HT and BDNF: SSRIs elevate brain BDNF; this was the original "neurotrophic hypothesis" of antidepressants (Duman, Heninger, Nestler 1997).
- Inflammation and BDNF/oxidative stress: pro-inflammatory cytokines (IL-6, TNF-alpha) downregulate BDNF and increase ROS via indoleamine 2,3-dioxygenase (IDO) shifting tryptophan from 5-HT to kynurenine, with kynurenine metabolites including quinolinic acid (NMDA agonist) and kynurenic acid (NMDA antagonist).

The Castren "plasticity restoration" framework (Castren and Antila 2017 Mol Psychiatry; Casarotto, Umemori, Castren 2022) argues that all proven effective antidepressant interventions converge on iPlasticity: SSRIs (binding TrkB), ketamine (binding TrkB), psychedelics (binding TrkB at 1,000-fold higher affinity), ECT (BDNF gene induction), exercise (BDNF), VNS (BDNF), and TMS (BDNF). The proposal should foreground this as a transdiagnostic plasticity axis.

---

## 7. Molecular and cellular biotype proposals

The following six biotypes are proposed for explicit inclusion in the Cytoverse mental-health coordinate map. They are not meant to be mutually exclusive; a single patient may sit high on two or three. Each biotype is named, defined by molecular signatures, mapped across disorders, paired with candidate wearable readouts, and matched to differential treatments.

### Biotype A: Low-BDNF / plasticity-deficit biotype

Defining signature: low serum or plasma BDNF (lower tertile); Val66Met Met/Met or Met/Val genotype; reduced fractional anisotropy in uncinate fasciculus; reduced hippocampal volume; impaired motor cortex plasticity to TMS (cTBS, iTBS).

Cross-disorder map: MDD (treatment-resistant subset), SCZ (chronic, negative-symptom-dominant), BD (during depressive episodes), PTSD (poor extinction learners), addiction-alcohol (DLS-BDNF deficit phenotype).

Wearable readout: capillary serum BDNF (finger-prick), Val66Met genotype, fNIRS-CCO mitochondrial reserve, EEG aperiodic slope (likely flatter in plasticity-deficit state).

Differential treatment: longer-duration SSRI plus exercise plus behavioral activation; psilocybin-assisted therapy at full hallucinogenic dose to engage maximum TrkB activation; ECT for severe cases; non-hallucinogenic TrkB-PAMs (Olson lab) when available.

### Biotype B: PV-interneuron / gamma-deficit / E-I-imbalance biotype

Defining signature: reduced PV interneuron function inferred from flat EEG aperiodic slope; reduced 40-Hz auditory steady-state response (ASSR); reduced gamma-band MEG/EEG during cognitive tasks; reduced cortical GABA on MRS; impaired short-interval intracortical inhibition (SICI) on TMS.

Cross-disorder map: SCZ (especially with cognitive symptoms and negative symptoms; well-replicated), ASD (with social-communication and sensory abnormalities), MDD (subset with cognitive symptoms; Sanacora's reduced-GABA depression).

Wearable readout: low-channel resting EEG aperiodic slope; auditory-evoked 40-Hz ASSR (achievable with consumer EEG); pupillometry as inhibitory-control proxy.

Differential treatment: zuranolone (GABA-A PAM) and other neurosteroids; potential TrkB-PV-targeted therapeutics; chondroitinase ABC to disrupt PNNs in animal models (Lesnikova et al. 2021); cognitive training with closed-loop neurofeedback on gamma.

### Biotype C: Oxidative-stress / mitochondrial biotype

Defining signature: low brain GSH on MRS (or high variance); elevated 8-OHdG, lipid peroxides, protein carbonyls in plasma; reduced platelet mitochondrial complex I activity; abnormal CCO redox state on broadband fNIRS; elevated lactate (suggestive of mitochondrial bottleneck).

Cross-disorder map: SCZ (subset, ~20-30%), BD (during mood episodes), ASD (~30% per Rossignol-Frye), MDD (subset), addiction-alcohol (mitochondrial toxicity phenotype).

Wearable readout: broadband fNIRS-CCO is the single best wearable in vivo mitochondrial readout for the Cytoscope. Capillary lactate and 8-OHdG add specificity. Heart rate variability (autonomic mitochondrial reserve) is a secondary proxy.

Differential treatment: N-acetylcysteine (long-duration, >=24 weeks per Yolland 2020 meta-analysis); lithium for BD with mitochondrial signature; CoQ10 and L-carnitine combinations for ASD with mitochondrial features (evidence weak); ketogenic diet as emerging metabolic intervention.

### Biotype D: Hyperdopaminergic biotype

Defining signature: elevated presynaptic striatal DA synthesis capacity on [18F]-DOPA PET (clinical research; not wearable yet); positive symptoms (delusions, hallucinations) with prominent paranoia; first-episode psychosis with rapid antipsychotic response; impulsivity and reward sensitivity in addiction.

Cross-disorder map: SCZ Type A (Howes; responders to first-line antipsychotics), psychotic mania in BD, stimulant addiction (in chronic state, dorsal striatum dominant; in acute use, ventral striatum dominant).

Wearable readout: harder than other biotypes. Candidates include pupillometry (locus coeruleus / NE proxy, indirect), salivary alpha-amylase, smartphone-based reaction time variability, EEG P300 amplitude (DA-related). The proposal should flag that no wearable directly measures striatal DA today; this is a Cytoscope target.

Differential treatment: D2 antagonists (haloperidol, risperidone) for hyperdopaminergic SCZ; partial agonists (aripiprazole, brexpiprazole, cariprazine) for the spectrum; NOT to be used for treatment-resistant SCZ where the biotype is glutamatergic.

### Biotype E: Inflammatory / cytokine biotype

Defining signature: elevated hs-CRP (>3 mg/L), IL-6, TNF-alpha; elevated kynurenine / tryptophan ratio (IDO activation); sickness-behavior symptom cluster (anergy, anhedonia, hypersomnia, anorexia).

Cross-disorder map: MDD subset (~30% per Raison and Miller; Raison et al. 2013 infliximab trial showed antidepressant effect ONLY in subjects with baseline hs-CRP > 5 mg/L), SCZ subset (Miller et al. 2011 meta-analysis), addiction-alcohol (alcoholic liver disease drives systemic inflammation), PTSD (immune dysregulation).

Wearable readout: capillary hs-CRP (finger-prick, validated), salivary IL-6 (less validated), continuous body temperature, sleep stage and HRV as autonomic-inflammatory readouts.

Differential treatment: anti-inflammatories in the high-CRP subgroup (infliximab, celecoxib, minocycline, omega-3); SSRIs may be less effective in this biotype; psychedelics may have anti-inflammatory effects (psilocybin reduces inflammatory cytokines in some studies; emerging).

### Biotype F: Serotonergic-deficit / 5-HT3-specific biotype

Defining signature: anxious and obsessive features predominate; family history of SSRI response; rs1042173-TT and 5-HTTLPR-LL genotypes in addiction context; tryptophan depletion induces symptom relapse.

Cross-disorder map: MDD subset (responsive SSRI biotype), anxiety/OCD (clearer 5-HT involvement), PTSD subset, alcohol use disorder (ondansetron-responsive 5-HTTLPR-LL subgroup, ~20-34% of alcoholics).

Wearable readout: cheek-swab pharmacogenomic panel including 5-HTTLPR, rs1042173, HTR3A, HTR3B, CYP2D6, CYP2C19 (last two for SSRI metabolism); diet-derived tryptophan availability via food log; heart rate variability changes during stress.

Differential treatment: SSRIs for the SSRI-responsive subset; ondansetron for the alcoholism subset with right 5-HTTLPR genotype; psilocybin-assisted therapy for the OCD subset (Moreno et al. 2006 J Clin Psych).

### Optional Biotype G: HPA-axis dysregulation biotype

Defining signature: blunted cortisol awakening response and/or non-suppression on dex/CRH test; high hair cortisol or chronic stress markers; rs2049046 or rs11030094 BDNF-AS genotype (which Hennings et al. 2019 linked to HPA axis - BDNF crosstalk in MDD).

Cross-disorder map: MDD (especially melancholic / treatment-resistant), PTSD (with chronic stress dysregulation), addiction (stress-induced craving and relapse).

Wearable readout: salivary cortisol (multiple daily samples), continuous HRV, sleep architecture from wearable EEG, smartphone-based daily stress sampling.

Differential treatment: mifepristone (GR antagonist) in psychotic depression; HPA-stabilizing behavioral interventions (CBT-I for sleep; mindfulness for HPA modulation); ketamine for cortisol-non-suppressors.

### Optional Biotype H: Glutamatergic excitotoxicity / NMDA-dysfunction biotype

Defining signature: elevated ACC glutamate/glutamine on MRS; family history of treatment-resistant SCZ; rapid ketamine response in MDD; reduced NMDA receptor function (e.g., anti-NMDA encephalitis-like at the extreme).

Cross-disorder map: SCZ Type B / treatment-resistant SCZ, MDD ketamine responders, BD-I, anti-NMDA receptor encephalitis (psychiatric phenocopy).

Wearable readout: this is the hardest axis to capture noninvasively; EEG aperiodic slope captures part of it; the Cytoscope would need MR spectroscopy infrastructure to fully resolve. A wearable proxy might be EEG gamma response to mismatch negativity paradigms (NMDA-dependent).

Differential treatment: ketamine and esketamine; AMPA modulators; rapastinel-class drugs in development; ECT for crisis cases.

---

## 8. Implications for the proposal

### 8.1 Why molecular biotypes complement connectomic biotypes

Connectomic biotypes (Drysdale, Tozzi, Williams, Goldstein) describe what brain networks are doing under stress. They are descriptive at the systems level. Molecular biotypes describe WHY a network is doing it. The causal chain runs genes -> molecules -> cells -> circuits -> behavior. The Cytoverse map will be more useful if it offers both: a connectomic biotype tells the clinician what state the patient is in; a molecular biotype tells the clinician why and what to do about it.

A concrete example: two patients both present with a Drysdale Biotype 1 (anhedonia-dominant, reduced reward-circuit connectivity). Patient X has low serum BDNF, Val/Val genotype, and elevated CRP. Patient Y has normal BDNF, Met/Met genotype, and elevated kynurenine/tryptophan ratio. Patient X is a candidate for ketamine plus anti-inflammatory; Patient Y is a candidate for psilocybin plus behavioral activation. The connectomic biotype alone could not make that distinction.

### 8.2 Wearable readouts the Cytoverse needs

The proposal should commit to a minimum viable molecular sensing stack:
1. Low-channel resting + task EEG with FOOOF aperiodic slope extraction
2. Broadband fNIRS-CCO (Tachtsidis MW-FlexNIRS class)
3. Capillary blood spot panel: BDNF, hs-CRP, kynurenine/tryptophan, 8-OHdG
4. Salivary panel: cortisol (4x daily), alpha-amylase
5. Cheek-swab pharmacogenomic panel: BDNF Val66Met + linked SNPs, 5-HTTLPR + linked, COMT Val158Met, MTHFR C677T, CYP2D6 and CYP2C19
6. HRV continuous from wrist or chest

This stack covers all six axes at a wearable price point and could be rolled out in a Phase 1 / Phase 2 Cytoscope deployment.

### 8.3 What this means for the NSF X-Labs / ARPA-H pitch

The proposal can credibly claim that:
- Six molecular and cellular axes are now mechanistically grounded enough to anchor cross-disorder biotype mapping.
- BDNF/TrkB has a unifying role as the proximal molecular target of all proven antidepressant treatments (Castren, Casarotto, Moliner, Park).
- The Cytoscope wearable stack can resolve five of six axes today; the sixth (presynaptic striatal DA) is a research target.
- 5-8 cross-disorder molecular biotypes are scientifically defensible and treatment-actionable.

The proposal should not over-claim. The honest framing: molecular biotypes are hypotheses validated to varying degrees, ranging from "well-replicated, modest effect" (PV deficit in SCZ Hedges' g = -0.27) to "well-replicated, large effect" (Howes striatal DA in SCZ d~0.8) to "single-lab, transformative if true" (psychedelic-TrkB direct binding; needs additional independent groups to replicate Moliner et al.). The Cytoverse map's value is in operationalizing these molecular dimensions for clinical use, not in claiming the underlying neuroscience is finished.

---

## References (Vancouver-style; not exhaustive)

1. Shkundin A, Halaris A. Associations of BDNF/BDNF-AS SNPs with Depression, Schizophrenia, and Bipolar Disorder. J Pers Med. 2023;13:1395. doi:10.3390/jpm13091395.
2. Moliner R, Girych M, Brunello CA, et al. Psychedelics promote plasticity by directly binding to BDNF receptor TrkB. Nat Neurosci. 2023;26:1032-1041. doi:10.1038/s41593-023-01316-5.
3. Casarotto PC, Umemori J, Castren E. BDNF receptor TrkB as the mediator of the antidepressant drug action. Front Mol Neurosci. 2022;15:1032224. doi:10.3389/fnmol.2022.1032224.
4. Park D, Lee G, Lee WG, Kim B, Lee Y, Kim JW. The therapeutic potential of psilocybin beyond psychedelia through shared mechanisms with ketamine. Mol Psychiatry. 2025;30:4910-4927. doi:10.1038/s41380-025-03100-2.
5. Casarotto PC, Girych M, Fred SM, et al. Antidepressant drugs act by directly binding to TRKB neurotrophin receptors. Cell. 2021;184:1299-1313.e19. doi:10.1016/j.cell.2021.01.034.
6. Castren E, Monteggia LM. Brain-derived neurotrophic factor signaling in depression and antidepressant action. Biol Psychiatry. 2021;90:128-136. doi:10.1016/j.biopsych.2021.05.008.
7. Castren E, Antila H. Neuronal plasticity and neurotrophic factors in drug responses. Mol Psychiatry. 2017;22:1085-1095.
8. Umemori J, Winkel F, Didio G, Llach Pou M, Castren E. iPlasticity: induced juvenile-like plasticity in the adult brain as a mechanism of antidepressants. Psychiatry Clin Neurosci. 2018;72:633-653. doi:10.1111/pcn.12683.
9. Winkel F, Ryazantseva M, Voigt MB, et al. Pharmacological and optical activation of TrkB in Parvalbumin interneurons regulate intrinsic states to orchestrate cortical plasticity. Mol Psychiatry. 2021;26:7247-7256. doi:10.1038/s41380-021-01211-0.
10. Molendijk ML, Spinhoven P, Polak M, Bus BAA, Penninx BWJH, Elzinga BM. Serum BDNF concentrations as peripheral manifestations of depression: evidence from a systematic review and meta-analyses on 179 associations (N=9484). Mol Psychiatry. 2014;19:791-800.
11. Fernandes BS, Steiner J, Berk M, et al. Peripheral brain-derived neurotrophic factor in schizophrenia and the role of antipsychotics: meta-analysis and implications. Mol Psychiatry. 2015;20:1108-1119.
12. Fernandes BS, Molendijk ML, Kohler CA, et al. Peripheral brain-derived neurotrophic factor (BDNF) as a biomarker in bipolar disorder: a meta-analysis of 52 studies. BMC Med. 2015;13:289.
13. Polyakova M, Stuke K, Schuemberg K, et al. BDNF as a biomarker for successful treatment of mood disorders: a systematic and quantitative meta-analysis. J Affect Disord. 2015;174:432-440.
14. Rocha RB, Dondossola ER, Grande AJ, et al. Increased BDNF levels after electroconvulsive therapy in patients with major depressive disorder: a meta-analysis study. J Psychiatr Res. 2016;83:47-53.
15. Polacchini A, Metelli G, Francavilla R, et al. A method for reproducible measurements of serum BDNF. Sci Rep. 2015;5:17989.
16. Naegelin Y, Dingsdale H, Sauberli K, Schadelin S, Kappos L, Barde YA. Measuring and validating the levels of brain-derived neurotrophic factor in human serum. eNeuro. 2018;5:ENEURO.0419-17.2018.
17. Sohal VS, Rubenstein JLR. Excitation-inhibition balance as a framework for investigating mechanisms in neuropsychiatric disorders. Mol Psychiatry. 2019;24:1248-1257. doi:10.1038/s41380-019-0426-0.
18. Rubenstein JL, Merzenich MM. Model of autism: increased ratio of excitation/inhibition in key neural systems. Genes Brain Behav. 2003;2:255-267.
19. Bourgeron T. From the genetic architecture to synaptic plasticity in autism spectrum disorder. Nat Rev Neurosci. 2015;16:551-563.
20. Donoghue T, Haller M, Peterson EJ, et al. Parameterizing neural power spectra into periodic and aperiodic components. Nat Neurosci. 2020;23:1655-1665.
21. Gao R, Peterson EJ, Voytek B. Inferring synaptic excitation/inhibition balance from field potentials. NeuroImage. 2017;158:70-78.
22. Kaar SJ, Angelescu I, Marques TR, Howes OD. Pre-frontal parvalbumin interneurons in schizophrenia: a meta-analysis of post-mortem studies. J Neural Transm. 2019;126:1637-1651.
23. Glausier JR, Lewis DA. Mapping pathologic circuitry in schizophrenia. Handb Clin Neurol. 2018;150:389-417.
24. Sanacora G, Treccani G, Popoli M. Towards a glutamate hypothesis of depression: an emerging frontier of neuropsychopharmacology for mood disorders. Neuropharmacology. 2012;62:63-77.
25. Marsman A, van den Heuvel MP, Klomp DWJ, Kahn RS, Luijten PR, Hulshoff Pol HE. Glutamate in schizophrenia: a focused review and meta-analysis of 1H-MRS studies. Schizophr Bull. 2013;39:120-129.
26. Marsman A, Mandl RCW, Klomp DWJ, et al. GABA and glutamate in schizophrenia: a 7 T 1H-MRS study. NeuroImage Clin. 2014;6:398-407.
27. Egerton A, Brugger S, Raffin M, et al. Anterior cingulate glutamate levels related to clinical status following treatment in first-episode schizophrenia. Neuropsychopharmacology. 2018;43:2503-2509.
28. Howes OD, Kapur S. The dopamine hypothesis of schizophrenia: version III - the final common pathway. Schizophr Bull. 2009;35:549-562.
29. Howes OD, Kambeitz J, Kim E, et al. The nature of dopamine dysfunction in schizophrenia and what this means for treatment: meta-analysis of imaging studies. Arch Gen Psychiatry. 2012;69:776-786.
30. Demjaha A, Murray RM, McGuire PK, Kapur S, Howes OD. Dopamine synthesis capacity in patients with treatment-resistant schizophrenia. Am J Psychiatry. 2012;169:1203-1210.
31. Stauffer VL, Millen BA, Andersen S, et al. Pomaglumetad methionil: no significant difference as an adjunctive treatment for patients with prominent negative symptoms of schizophrenia compared to placebo. Schizophr Res. 2013;150:434-441.
32. Adams DH, Kinon BJ, Baygani S, et al. A long-term, phase 2, multicenter, randomized, open-label, comparative safety study of pomaglumetad methionil (LY2140023 monohydrate) versus atypical antipsychotic standard of care in patients with schizophrenia. BMC Psychiatry. 2014;13:143.
33. Rossignol DA, Frye RE. Mitochondrial dysfunction in autism spectrum disorders: a systematic review and meta-analysis. Mol Psychiatry. 2012;17:290-314. doi:10.1038/mp.2010.136.
34. Berk M, Copolov DL, Dean O, et al. N-acetyl cysteine as a glutathione precursor for schizophrenia - a double-blind, randomized, placebo-controlled trial. Biol Psychiatry. 2008;64:361-368.
35. Yolland COB, Hanratty D, Neill E, et al. Meta-analysis of randomised controlled trials with N-acetylcysteine in the treatment of schizophrenia. Aust N Z J Psychiatry. 2020;54:453-466. doi:10.1177/0004867419893439.
36. Das TK, Javadzadeh A, Dey A, et al. Antioxidant defense in schizophrenia and bipolar disorder: a meta-analysis of MRS studies of anterior cingulate glutathione. Prog Neuropsychopharmacol Biol Psychiatry. 2019;91:94-102.
37. Murray AJ, Rogers JC, Katshu MZUH, Liddle PF, Upthegrove R. Oxidative stress and the pathophysiology and symptom profile of schizophrenia spectrum disorders. Front Psychiatry. 2021;12:703452.
38. Holper L, Lan MJ, Brown PJ, Sublette ME, Burke A, Mann JJ. Brain cytochrome-c-oxidase as a marker of mitochondrial function: a pilot study in major depression using NIRS. Depress Anxiety. 2019;36:766-779.
39. Kaynezhad P, Mitra S, Bainbridge A, et al. Quantification of the severity of hypoxic-ischemic brain injury in a neonatal preclinical model using measurements of cytochrome-c-oxidase from a miniature broadband-near-infrared spectroscopy system. Neurophotonics. 2019;6:045009.
40. Bale G, Mitra S, Meek J, Robertson N, Tachtsidis I. A new broadband near-infrared spectroscopy system for in-vivo measurements of cerebral cytochrome-c-oxidase changes in neonatal brain injury. Biomed Opt Express. 2014;5:3450-3466.
41. Raison CL, Rutherford RE, Woolwine BJ, et al. A randomized controlled trial of the tumor necrosis factor antagonist infliximab for treatment-resistant depression: the role of baseline inflammatory biomarkers. JAMA Psychiatry. 2013;70:31-41.
42. Miller AH, Maletic V, Raison CL. Inflammation and its discontents: the role of cytokines in the pathophysiology of major depression. Biol Psychiatry. 2009;65:732-741.
43. Moncrieff J, Cooper RE, Stockmann T, Amendola S, Hengartner MP, Horowitz MA. The serotonin theory of depression: a systematic umbrella review of the evidence. Mol Psychiatry. 2023;28:3243-3256. doi:10.1038/s41380-022-01661-0.
44. Jauhar S, Cowen PJ, Browning M. Fifty years on: serotonin and depression. J Psychopharmacol. 2023;37:467-471.
45. Johnson BA, Seneviratne C, Wang XQ, et al. Determination of genotype combinations that can predict the outcome of the treatment of alcohol dependence using the 5-HT3 antagonist ondansetron. Am J Psychiatry. 2013;170:1020-1031. doi:10.1176/appi.ajp.2013.12091163.
46. Cao D, Yu J, Wang H, et al. Structure-based discovery of nonhallucinogenic psychedelic analogs. Science. 2022;375:403-411. doi:10.1126/science.abl8615.
47. Wallach J, Cao AB, Calkins MM, et al. Identification of 5-HT2A receptor signaling pathways associated with psychedelic potential. Nat Commun. 2023;14:8221.
48. Vargas MV, Dunlap LE, Dong C, et al. Psychedelics promote neuroplasticity through the activation of intracellular 5-HT2A receptors. Science. 2023;379:700-706. doi:10.1126/science.adf0435.
49. Olson DE. Psychoplastogens: a promising class of plasticity-promoting neurotherapeutics. J Exp Neurosci. 2018;12:1179069518800508.
50. Cameron LP, Tombari RJ, Lu J, et al. A non-hallucinogenic psychedelic analogue with therapeutic potential. Nature. 2021;589:474-479.
51. Hesselgrave N, Troppoli TA, Wulff AB, Cole AB, Thompson SM. Harnessing psilocybin: antidepressant-like behavioral and synaptic actions of psilocybin are independent of 5-HT2R activation in mice. Proc Natl Acad Sci USA. 2021;118:e2022489118.
52. Liu RJ, Lee FS, Li XY, Bambico F, Duman RS, Aghajanian GK. Brain-derived neurotrophic factor Val66Met allele impairs basal and ketamine-stimulated synaptogenesis in prefrontal cortex. Biol Psychiatry. 2012;71:996-1005.
53. Laje G, Lally N, Mathews D, et al. Brain-derived neurotrophic factor Val66Met polymorphism and antidepressant efficacy of ketamine in depressed patients. Biol Psychiatry. 2012;72:e27-e28.
54. Rodrigues NB, Chen-Li D, Di Vincenzo JD, et al. Brain-derived neurotrophic factor Val66Met and CYP2B6 polymorphisms as predictors for ketamine effectiveness in patients with treatment-resistant depression. J Psychopharmacol. 2024;38:558-568.
55. Niitsu T, Fabbri C, Bentini F, Serretti A. Pharmacogenetics in major depression: a comprehensive meta-analysis. Prog Neuropsychopharmacol Biol Psychiatry. 2013;45:183-194.
56. Halaris A, Sharma A, Meresh E, et al. Serum BDNF: a potential biomarker for major depressive disorder and antidepressant response prediction. J Depress Anxiety. 2015;4:1000179.
57. Volkow ND, Wang GJ, Telang F, et al. Profound decreases in dopamine release in striatum in detoxified alcoholics: possible orbitofrontal involvement. J Neurosci. 2007;27:12700-12706.
58. Eisch AJ, Bolanos CA, de Wit J, et al. Brain-derived neurotrophic factor in the ventral midbrain-nucleus accumbens pathway: a role in depression. Biol Psychiatry. 2003;54:994-1005.
59. Logrip ML, Janak PH, Ron D. Dynorphin is a downstream effector of striatal BDNF regulation of ethanol intake. FASEB J. 2008;22:2393-2404.
60. Hopkins JL, et al. BDNF in ventrolateral orbitofrontal cortex to dorsolateral striatum circuit moderates alcohol consumption, seeking and relapse. PMC12824369. 2025.

---

## Summary of biotypes for the proposal (~300 words)

For the NSF X-Labs Phase 0 and ARPA-H PHO proposal, the Cytoverse map should commit to six molecular and cellular biotypes that cut across the six target disorders (MDD, SCZ, BD, anxiety/OCD, PTSD, addiction; with autism noted under E/I and oxidative-stress axes), with two further biotypes flagged as optional. The six core biotypes are:

A. Low-BDNF / plasticity-deficit biotype. Defined by low serum BDNF, Val66Met Met carrier status, reduced fractional anisotropy and hippocampal volume, blunted TMS plasticity. Spans MDD treatment-resistant, chronic SCZ, BD depressive, PTSD poor-extinction, alcohol DLS-BDNF deficit. Differential treatment: psilocybin (Moliner-Castren TrkB pivot), full-dose ECT, longer-duration SSRI + exercise.

B. PV-interneuron / gamma-deficit / E-I imbalance biotype. Defined by flat EEG aperiodic slope, reduced 40-Hz ASSR, low cortical GABA. Spans SCZ (Hedges' g = -0.27 PV reduction), ASD, MDD with cognitive symptoms. Differential treatment: zuranolone, GABA-A neurosteroids, future PV-TrkB therapeutics, gamma-band neurofeedback.

C. Oxidative-stress / mitochondrial biotype. Defined by low brain GSH, abnormal CCO redox on fNIRS, elevated lactate. Spans SCZ subset, BD, ~30% of ASD (Rossignol-Frye), MDD subset, alcohol use disorder. Differential treatment: long-duration NAC, lithium for BD, ketogenic interventions. Wearable: broadband fNIRS-CCO (Tachtsidis class).

D. Hyperdopaminergic biotype. Striatal DA elevation (PET-defined). Maps to SCZ Type A (Howes responders), psychotic mania, chronic dorsal-striatum addiction. Differential treatment: D2 antagonists and partial agonists.

E. Inflammatory / cytokine biotype. Elevated hs-CRP, IL-6, TNF-alpha; sickness-behavior cluster. ~30% of MDD (Raison), SCZ subset, PTSD, alcohol-liver-disease. Differential treatment: anti-inflammatories in high-CRP subgroup, omega-3, possibly psychedelics.

F. Serotonergic-deficit / 5-HT3-specific biotype. SSRI-responsive MDD, OCD, alcohol use disorder with 5-HTTLPR-LL / rs1042173-TT (ondansetron-responsive in ~20-34% of alcoholics; Johnson 2013). Differential treatment: SSRIs for the responsive subset, ondansetron for the alcoholism subgroup, psilocybin for OCD.

Optional biotypes G (HPA-axis) and H (NMDA / glutamatergic excitotoxicity) are flagged for future inclusion as the wearable readouts mature. The Cytoverse stack can resolve five of six axes today with the proposed wearable panel; presynaptic striatal DA remains a research target.

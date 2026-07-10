# Biotypes: Post-Traumatic Stress Disorder (PTSD)

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: researchers, stakeholders
> **Tags**: `literature-synthesis`, `disease-biotypes`, `ptsd`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)

Genomic factor loading (Nature 2025): **Internalizing factor** (shared with major depression and anxiety; the factor is associated with oligodendrocyte biology). Grotzinger et al., Mapping the genetic landscape across 14 psychiatric disorders, Nature 2025 (doi:10.1038/s41586-025-09820-3).

PTSD is among the most biologically heterogeneous DSM-5 and ICD-11 diagnoses. Two people with the same diagnosis can show opposite autonomic tone, opposite prefrontal activity profiles, opposite endocrine signatures, and divergent treatment responses. The dissociative subtype is the only PTSD subtype with a formal DSM-5 and ICD-11 home, and it inverts much of the canonical circuit picture. This document harmonizes the molecular, connectomic, and phenotypic evidence to Gene Ontology, the Allen Human Reference Atlas 3D (2020), and SNOMED CT/HPO respectively, and ends with the most defensible cross-scale biotypes. Throughout, replication status is explicit; PTSD biotype work is in an early and contested phase, and at least one prominent acute-imaging biotype set failed independent replication (Ben-Zion 2023).

## Seed papers

- Lanius et al. 2010 (dissociative subtype, fronto-limbic overmodulation), Am J Psychiatry, doi:10.1176/appi.ajp.2009.09081168.
- Stevens, Ressler et al. 2021 (AURORA acute biotypes), Am J Psychiatry, doi:10.1176/appi.ajp.2021.20101526; Ben-Zion et al. 2023 replication failure, Am J Psychiatry, doi:10.1176/appi.ajp.20220271.
- Etkin, Maron-Katz et al. 2019 (ventral attention network deficit, treatment resistance), Sci Transl Med, doi:10.1126/scitranslmed.aal3236.
- Nievergelt et al. 2024 (PGC-PTSD GWAS, 95 loci, ~1.2M), Nat Genet, doi:10.1038/s41588-024-01707-9.
- Klengel/Binder 2013 (FKBP5 allele-specific demethylation), Nat Neurosci, doi:10.1038/nn.3275; Wolf et al. 2018 (accelerated DNAm aging, inflammaging), Psychoneuroendocrinology, doi:10.1016/j.psyneuen.2017.12.007.
- Girgenti et al. 2021 (postmortem interneuron module, ELFN1), Nat Neurosci, doi:10.1038/s41593-020-00748-7; Hicks et al. 2025 (single-cell PTSD/MDD), Nature, doi:10.1038/s41586-025-09083-y.
- Philip et al. 2025 (fMRI-guided amygdala-circuit TMS RCT), Am J Psychiatry, doi:10.1176/appi.ajp.20250749.
- Mitchell et al. 2021/2023 (MAPP1/MAPP2 MDMA-assisted therapy), Nat Med, doi:10.1038/s41591-021-01336-3, doi:10.1038/s41591-023-02565-4.

---

## MICRO scale (molecular / genetic / cellular / immune) vs GO-harmonized

The shared signal across all 14 disorders in Grotzinger et al. 2025 was enriched for broad transcriptional regulation; the Internalizing-factor-specific biology that PTSD loads on points to oligodendrocyte processes. PTSD-specific molecular biotyping centers on five axes: glucocorticoid/HPA negative feedback, central noradrenergic drive, neurotrophin-gated extinction plasticity, immune/inflammaging, and a GABAergic interneuron deficit recovered in postmortem tissue.

| Biotype / dysregulation | GO term(s) + ID | Specific finding (genes, variants, molecules) | Neurotransmitter family | BDNF / neurotrophin + plasticity? | E/I imbalance (+ region) | Oxidative / mito / ROS? | Immune / inflammatory? | Confidence | Source (author year, DOI) |
|---|---|---|---|---|---|---|---|---|---|
| HPA negative-feedback hypersensitivity (low basal cortisol, enhanced DEX suppression) | cellular response to glucocorticoid stimulus (GO:0071385); regulation of glucocorticoid receptor signaling pathway (GO:2000322) | Lower basal cortisol vs trauma-exposed controls; enhanced low-dose dexamethasone suppression; enhanced GR sensitivity at pituitary; predicts onset prospectively (Yehuda phenotype) | none reported (endocrine; downstream of cortisol) | not direct | not reported | not direct | indirect (glucocorticoids modulate immune tone) | HIGH (multi-cohort, prospective) | Yehuda & Bierer 2009 review (no single DOI; see refs) |
| FKBP5 methylation, gene-by-environment-by-epigenome | response to glucocorticoid (GO:0051384); DNA methylation (GO:0006306) | rs1360780 risk T-allele + childhood maltreatment -> allele-specific demethylation of FKBP5 intron 7 -> GR-induced FKBP5 upregulation, blunted negative feedback | none reported | not direct | not reported | not reported | indirect (FKBP5-NF-kB cross-talk) | HIGH (mechanistically clean, replicated) | Klengel et al. 2013, doi:10.1038/nn.3275 |
| NR3C1 (glucocorticoid receptor) promoter methylation, intergenerational | DNA methylation (GO:0006306); glucocorticoid receptor binding (GO:0035259, approx, needs curation) | Altered GR exon 1F promoter methylation in Holocaust offspring; direction depends on parental PTSD status | none reported | not direct | not reported | not reported | not direct | MEDIUM (single-lab lineage, small n) | Yehuda et al. 2014, doi:10.1176/appi.ajp.2014.13121571 |
| Central noradrenergic hyperdrive | norepinephrine secretion (GO:0048243, approx, needs curation); adrenergic receptor signaling pathway (GO:0071875) | Elevated CSF norepinephrine correlating with symptom severity; disrupts REM, drives nightmares; alpha-1 adrenergic target for prazosin | **Norepinephrine** | not direct | possible cortical E-up via LC-NE arousal (region: prefrontal/limbic, approx) | not reported | not direct | MEDIUM (replicated CSF finding, small samples) | Geracioti et al. 2001 (Am J Psychiatry 158:1227) |
| Serotonergic dysregulation (SSRI-responsive subgroup) | serotonin receptor signaling pathway (GO:0007210); serotonin reuptake (GO:0051610, approx, needs curation) | SSRI response ~60%, remission ~30%; SLC6A4 / 5-HTTLPR x trauma interactions reported but weakly replicated | **Serotonin** | indirect (SSRIs raise BDNF over weeks) | not direct | not reported | not direct | MEDIUM (treatment-defined, not a clean biomarker) | MacNamara et al. 2016, doi:10.1038/npp.2015.190 |
| BDNF / neurotrophin signaling and extinction plasticity | neurotrophin TRK receptor signaling pathway (GO:0048011); regulation of synaptic plasticity (GO:0048167); positive regulation of long-term synaptic potentiation (GO:1900273) | BDNF Val66Met (rs6265) Met allele associated with impaired fear extinction and poorer exposure-therapy response; BDNF dynamics on MRS track TMS response | **Glutamate** (extinction is NMDA/glutamatergic) | **yes** vs BDNF/TrkB gates fear-extinction learning, the substrate of exposure therapy | not direct | not reported | not reported | MEDIUM (Met effect replicated in extinction; clinical prediction weaker) | Felmingham/Bryant extinction work; see refs |
| Glutamatergic / NMDA fear-extinction circuit | glutamatergic synaptic transmission (GO:0035249); NMDA glutamate receptor activity (GO:0004972, approx, needs curation) | GWAS-prioritized ion channels and synaptic genes; ketamine (NMDA antagonist) preliminary signal; MRS glutamate dynamics during TMS | **Glutamate** | yes (NMDA-dependent plasticity) | candidate E-up in amygdala / E-down in vmPFC (region-specific, model-level) | not reported | not reported | MEDIUM | Nievergelt et al. 2024, doi:10.1038/s41588-024-01707-9 |
| Peripheral inflammation (IL-6 dominant) | inflammatory response (GO:0006954); interleukin-6 production (GO:0032635) | Meta-analytic elevations of IL-6 (largest, most consistent), IL-1beta, TNF-alpha, IFN-gamma, CRP; stratifies a worse cardiometabolic/treatment subgroup; MDMA response tracks IL-6/TNF reduction | none reported | not direct | not reported | yes (inflammaging convergence) | **yes** (IL-6, TNF-alpha, CRP) | HIGH for IL-6 elevation; LOW that it is PTSD-specific (shared with MDD) | Passos et al. 2015, doi:10.1016/S2215-0366(15)00309-0 |
| Inflammaging / accelerated epigenetic aging | aging (GO:0007568); response to oxidative stress (GO:0006979) | Accelerated Hannum and GrimAge DNAm age with symptom severity and childhood trauma; converges inflammation + oxidative stress + cellular aging; AHRR cg05575921 hypomethylation (smoking-confounded) | none reported | not direct | not reported | **yes** (oxidative stress component) | **yes** (microglia, complement candidates) | HIGH (meta-analytic) | Wolf et al. 2018, doi:10.1016/j.psyneuen.2017.12.007 |
| GABAergic interneuron deficit (postmortem) | GABAergic synaptic transmission (GO:0051932); inhibitory synapse assembly (GO:1904862, approx) | Downregulated interneuron-gene module is the most PTSD-associated network in PFC; GWAS-integration prioritized interneuron synaptic gene ELFN1; single-cell localizes change to inhibitory interneurons + microglia + endothelium with upregulated glucocorticoid signaling | **GABA** (+ glutamate at affected synapses) | not direct | **I-down** (interneuron deficit) in prefrontal cortex (dlPFC) | not reported | yes (microglial state shift) | MEDIUM-HIGH (two postmortem consortia converge) | Girgenti et al. 2021, doi:10.1038/s41593-020-00748-7; Hicks et al. 2025, doi:10.1038/s41586-025-09083-y |
| Hippocampal microglial / immune imbalance (postmortem) | microglial cell activation (GO:0001774); inflammatory response (GO:0006954) | Single-nucleus hippocampal transcriptomics shows immune imbalance and microglial state shifts in PTSD | none reported | not direct | not reported | not reported | **yes** (microglia) | LOW-MEDIUM (single study) | Front Immunol 2025 (PMC, see refs) |

**GWAS anchor.** Nievergelt et al. 2024 meta-analyzed 1,222,882 European-ancestry individuals (137,136 cases) plus 58,051 admixed African and Native American ancestry individuals (13,624 cases), identifying 95 genome-wide significant loci (80 novel) and prioritizing 43 candidate causal genes enriched for neurotransmitter receptors, ion channels, axon-guidance and synaptic proteins, and stress/immune/threat pathways. SNP-heritability is ~5 to 20 percent on the liability scale, below twin estimates (~30 percent in men, higher in women). Polygenic risk scores explain ~1 to 2 percent of variance and are too noisy to define a biotype alone, but weight priors over biotype membership when fused with imaging; in latent-class work the dysphoric class carried the highest MDD polygenic load while the threat-reactivity class carried less psychiatric polygenic burden but the most combat exposure.

---

## MESO scale (connectomic) vs Allen Atlas nodes + edges

Reference: Allen Human Reference Atlas 3D 2020 (141 anatomical regions). Functional labels and Brodmann areas are given in parentheses; the Allen anatomical container is named first. Many PTSD findings are reported for functional networks (DMN, salience/ventral-attention, central executive) that are not 1:1 with Allen anatomical parcels. The defining feature of the dissociative subtype is that several nodes and the amygdala-vmPFC edge **invert** relative to canonical (threat-reactive) PTSD: amygdala becomes overmodulated rather than hyperreactive.

### NODES

| Allen region (functional label) | Observed change | Modality | Confidence | Source |
|---|---|---|---|---|
| Amygdala, basolateral + centromedial complexes | **Hyperreactivity** to threat (canonical/threat-reactive); **OVERmodulated / reduced activation** in dissociative subtype | fMRI (task) | HIGH (canonical hyperreactivity); MEDIUM-HIGH (dissociative inversion) | Shin & Liberzon 2010; Lanius et al. 2010, doi:10.1176/appi.ajp.2009.09081168 |
| Cingulate gyrus, subgenual + rostral part (vmPFC / rACC / BA25, BA32) | **Hypoactivation** during threat (failure to inhibit amygdala) in canonical PTSD | fMRI | HIGH | Shin & Liberzon 2010, doi:10.1038/npp.2009.83 |
| Frontal cortex, medial prefrontal (mPFC / dmPFC) | **Overmodulation** (hyperengagement) of limbic system in dissociative subtype | fMRI | MEDIUM-HIGH | Lanius et al. 2010; Nicholson et al. 2017, Hum Brain Mapp |
| Cingulate gyrus, dorsal anterior part (dACC / BA24, BA32) | **Hyperreactivity** to threat in canonical; reduced engagement in dissociative; sharper ventral-ACC habituation predicts poor recovery | fMRI | MEDIUM-HIGH | Stevens et al. 2017, doi:10.1016/j.biopsych.2016.11.015 |
| Hippocampus (anterior; CA3, dentate gyrus) | **Atrophy** (volume loss; ENIGMA-PGC d = -0.17); partly a predisposing trait per twin study; functional deficit in extinction recall | structural + fMRI | HIGH (volume); MEDIUM (function) | Logue et al. 2018, doi:10.1016/j.biopsych.2017.09.006; Gilbertson et al. 2002, doi:10.1038/nn958 |
| Insula, anterior part (anterior insula) | **Hyperreactivity** + increased amygdala coupling in canonical (salience); **reduced engagement / interoceptive blunting** in dissociative | fMRI | MEDIUM-HIGH | Akiki et al. 2017; Etkin & Maron-Katz 2019 |
| Inferior parietal lobule, supramarginal gyrus + temporoparietal junction (right TPJ / VAN node) | **Reduced functional connectivity** within ventral attention network in treatment-resistant subgroup | fMRI + TMS/EEG | MEDIUM (within-lab cross-cohort only) | Etkin & Maron-Katz et al. 2019, doi:10.1126/scitranslmed.aal3236 |
| Frontal cortex, middle frontal gyrus, anterior part (right anterior MFG / VAN node) | **Reduced connectivity** (VAN deficit) | fMRI | MEDIUM | Etkin & Maron-Katz 2019 |
| Precuneus + posterior cingulate cortex (DMN posterior hub) | **Reduced within-DMN connectivity**; increased amygdala-precuneus coupling in dissociative | fMRI | MEDIUM-HIGH | Nicholson et al. 2015, doi:10.1038/npp.2015.79; Akiki et al. 2017 |
| Insula, posterior part (posterior insula) | Increased amygdala coupling in dissociative (proprioceptive/interoceptive disconnection) | fMRI | MEDIUM | Lanius et al. 2010; Nicholson et al. 2015 |
| Cerebellum, posterior lobules | **Smaller volume** (ENIGMA-PGC mega-analysis) | structural | MEDIUM-HIGH | Huggins et al. 2024, doi:10.1038/s41380-023-02352-0 |
| Striatum, ventral (nucleus accumbens) | **Low reward reactivity** in low-reward/dysphoric biotype (monetary incentive delay) | fMRI (task) | LOW-MEDIUM (AURORA cluster did not externally replicate) | Stevens et al. 2021, doi:10.1176/appi.ajp.2021.20101526 |
| Frontal cortex, inferior frontal gyrus + pre-supplementary motor area (rIFG / preSMA, inhibition) | Reduced inhibitory engagement in reactive-disinhibited AURORA cluster | fMRI (Go/No-Go) | LOW (failed external replication) | Stevens et al. 2021; Ben-Zion et al. 2023 |
| Scalp EEG (centroposterior; not an Allen parcel) | **Reduced slow-wave / delta NREM power**, reduced alpha power, shortened microstate E; theta-band wPLI tracks rumination/re-experiencing | EEG / PSG | MEDIUM (sleep slow-wave HIGH; microstate single-lab) | Sleep PSD/spindles 2021 (PMC8640175); Characterizing PTSD using electrophysiology 2025 (PMC12130596) |

### EDGES

| Region A vs Region B (functional labels) | Association sign | Observed change in disorder | Modality | Confidence | Source |
|---|---|---|---|---|---|
| Amygdala vs cingulate gyrus subgenual/rostral part (amygdala vs vmPFC/rACC) | normally `negative (anticorrelation)` (vmPFC inhibits amygdala) | Canonical PTSD: anticorrelation **weakened / fails** (reduced top-down regulation), bottom-up amygdala drive; the core threat-regulation edge | fMRI (rest + task), DCM | HIGH | Stevens et al. 2013, doi:10.1016/j.jpsychires.2013.05.031; Shin & Liberzon 2010 |
| Amygdala vs frontal cortex medial prefrontal (amygdala vs mPFC/dmPFC) | normally `negative (anticorrelation)` | Dissociative subtype: connectivity becomes **increased / positive** (top-down overmodulation, inhibitory prefrontal control dominates); inverts the canonical sign | fMRI, DCM | MEDIUM-HIGH | Lanius et al. 2010; Nicholson et al. 2017 |
| Amygdala vs precuneus / posterior cingulate (amygdala vs DMN posterior) | normally weak/`mixed` | Dissociative subtype: **increased** amygdala-precuneus/posterior-insula connectivity (depersonalization, derealization) | fMRI | MEDIUM | Nicholson et al. 2015, doi:10.1038/npp.2015.79 |
| Anterior insula / dACC vs amygdala (salience network vs amygdala) | normally `positive` | Canonical: **increased** salience-amygdala coupling (threat hypervigilance); inverted/reduced in dissociative | fMRI | MEDIUM-HIGH | Akiki et al. 2017; salience-network reviews |
| Within-DMN: precuneus/PCC vs mPFC | normally `positive` | **Reduced** within-DMN connectivity; correlates negatively with symptom severity; DMN nodes show increased coupling to salience network | fMRI | MEDIUM-HIGH | Nicholson et al. 2020, NeuroImage Clin (PMC7240193) |
| Right anterior insula vs dACC vs anterior MFG vs supramarginal (within ventral attention network) | normally `positive` | **Reduced** intra-VAN connectivity in treatment-resistant subgroup; doubled TMS/EEG recovery time (impaired information propagation) | fMRI + TMS/EEG | MEDIUM (within-lab cross-cohort; not independently replicated) | Etkin & Maron-Katz et al. 2019, doi:10.1126/scitranslmed.aal3236 |
| Right DLPFC vs amygdala (TMS target edge) | normally `positive` (used to engage amygdala via cortex) | Individualized positively amygdala-connected rDLPFC site used as accelerated-TMS target; larger medial-anterior target shift predicts greater symptom improvement | fMRI-guided TMS RCT | MEDIUM (single RCT, positive) | Philip et al. 2025, doi:10.1176/appi.ajp.20250749 |

**Replication caveat (flagged).** Robust, cross-consortium edges/nodes: amygdala-vmPFC connectivity reduction, smaller hippocampal volume, the dissociative overmodulation pattern, and within-DMN disruption. The **AURORA acute fMRI biotype clustering (Stevens et al. 2021) did NOT externally replicate** when Ben-Zion et al. 2023 applied the same approach to an independent acutely traumatized cohort; treat the ventral-striatum reward and rIFG/preSMA inhibition nodes as LOW confidence. The Etkin VAN-deficit biotype has only within-lab cross-cohort replication.

---

## MACRO scale (phenotype) vs SNOMED CT / HPO

PTSD phenotype dimensions map to the DSM-5 symptom clusters: re-experiencing/intrusion, avoidance, hyperarousal, negative cognitions/mood, and the dissociative specifier. SNOMED CT covers ~91 percent of clinician PTSD terms (Trusko et al. 2010); HPO coverage of trauma-specific psychiatric symptoms is sparse, so several HPO cells are marked approx/needs curation and mapped to the nearest superordinate concept.

| Biotype phenotype | SNOMED CT term + ID | HPO term + ID | Short description of observations that led to this mapping | Source |
|---|---|---|---|---|
| PTSD (diagnosis anchor) | Posttraumatic stress disorder (47505003); Chronic post-traumatic stress disorder (313182004) | Post-traumatic stress disorder (HP:0410291, approx, needs curation) | Full DSM-5/ICD-11 syndrome; threat-reactivity dimension | Trusko et al. 2010, doi:10.1002/jts.20591 |
| Re-experiencing / intrusion | Flashback (313179001, approx, needs curation); Recurrent intrusive recollections | Recurrent intrusive thoughts (HP:0033051, approx, needs curation) | Involuntary trauma-relevant memory intrusion; DMN/autobiographical-memory fragmentation; enhanced LPP to threat cues on EEG | Akiki et al. 2017; LPP work 2023 |
| Hyperarousal / hypervigilance | Hypervigilance (247803003, approx, needs curation) | Hypervigilance (HP:5200401, approx, needs curation) | Exaggerated startle, scanning for threat; low HF-HRV, elevated heart rate, central NE drive; threat-reactivity dimension | Schneider & Schwerdtfeger 2020, doi:10.1017/S003329172000207X |
| Trauma-related nightmares / sleep disturbance | Nightmares (247960002, approx, needs curation); Sleep disturbance (39898005) | Nightmares (HP:0002360, approx, needs curation); Sleep disturbance (HP:0002360 family) | REM disruption by central noradrenergic drive; reduced slow-wave NREM; the prazosin target dimension | Geracioti et al. 2001; PSG 2021 (PMC8640175) |
| Avoidance | Avoidance behavior (225457007, approx, needs curation) | Behavioral abnormality (HP:0000708, approx, superordinate) | Effortful avoidance of trauma reminders; maintained by failed extinction (BDNF/glutamate); avoidance dimension | Shin & Liberzon 2010 |
| Negative cognitions / mood (dysphoric) | Depressed mood (366979004); Negative cognition (approx, needs curation) | Anhedonia (HP:0033676); Depressivity (HP:0000716, approx) | Anhedonia, guilt, blunted reward reactivity (ventral striatum); high MDD polygenic load; PTSD-MDD overlap dimension | Stevens et al. 2021; Misganaw et al. 2021 |
| Dissociation (DSM-5 dissociative specifier) | Depersonalization (19006008, approx, needs curation); Derealization (76104007, approx, needs curation) | Depersonalization (HP:0009800, approx, needs curation); Derealization (approx, needs curation) | Persistent/recurrent depersonalization or derealization with otherwise full PTSD; fronto-limbic overmodulation; female and early-childhood-abuse enrichment | Lanius et al. 2012; Merck Manual D-PTSD |
| Cardiometabolic / accelerated-aging comorbidity | Metabolic syndrome (237602007, approx); Cardiovascular disease risk | Abnormal inflammatory marker (HP:0012647 family, approx) | Elevated CRP/IL-6, accelerated GrimAge, increased cardiovascular mortality in chronic PTSD; inflammaging dimension | Wolf et al. 2018, doi:10.1016/j.psyneuen.2017.12.007 |

---

## Interventional studies (incl. neuromodulation, DBS, neuroplastogens)

| Biotype it targets | Intervention (class + specific) | Study (author year, design, n) | Outcome | Confidence | Source |
|---|---|---|---|---|---|
| Canonical threat-reactive; serotonergic subgroup | SSRI (sertraline, paroxetine) vs only FDA-approved PTSD pharmacotherapies | Pooled RCTs; MacNamara et al. 2016 prediction study (n=36) | Response ~60%, remission ~30%; higher pretreatment mPFC activation + lower amygdala reactivity predicts response | HIGH (efficacy); MEDIUM (predictor) | MacNamara et al. 2016, doi:10.1038/npp.2015.190 |
| Central noradrenergic / nightmare-dominant subgroup | Alpha-1 adrenergic antagonist (prazosin) | Raskind et al. 2007 RCT (combat veterans); VA CSP #563 Raskind et al. 2018 RCT (n=304) | Early trials: strong nightmare reduction. **CSP #563 NEGATIVE on primary endpoint**, indicating response is biotype-dependent (high central-NE subgroup), not general | MEDIUM (subgroup effect real; no validated stratifier) | Raskind et al. 2018, doi:10.1056/NEJMoa1507598 |
| Dissociative subtype; severe/treatment-resistant PTSD | Neuroplastogen vs MDMA-assisted therapy (entactogen) | MAPP1 Mitchell et al. 2021 (RCT n=90, severe); MAPP2 Mitchell et al. 2023 (RCT n=104, moderate-severe) | 67% lost PTSD diagnosis vs 32% placebo (MAPP1, d~0.9); 71.2% vs 47.6% (MAPP2, d~0.7). Pooled: dissociative subtype responds at least equally, numerically larger CAPS-5 reduction; IL-6/TNF reductions track response. **FDA Complete Response Letter issued (CRL published Sept 2025) on trial-conduct grounds, not efficacy; program being re-run** | HIGH (efficacy); MEDIUM (dissociative-subgroup signal) | Mitchell et al. 2021/2023, doi:10.1038/s41591-021-01336-3, doi:10.1038/s41591-023-02565-4; FDA CRL 2025 |
| Dysphoric / low-reward; dissociative (preliminary) | Neuroplastogen vs ketamine (NMDA antagonist) | Repeated-dose RCTs (Feder et al.) | Rapid symptom reduction in chronic PTSD; preliminary signal in dissociative/anhedonic profiles | MEDIUM | Feder et al. (see refs) |
| Treatment-resistant; ibogaine-tractable veterans (TBI overlap) | Neuroplastogen vs magnesium-ibogaine | MISTIC Stanford, Nat Med 2024 (open-label, n=30 Special Forces veterans) | 88% no longer met PTSD criteria at 1 month; depression/anxiety reductions >80%; open-label, selection bias | LOW-MEDIUM (uncontrolled) | MISTIC 2024, Nat Med |
| Canonical threat-reactive; amygdala-circuit | TMS vs fMRI-guided accelerated, individualized amygdala-connected rDLPFC | Philip et al. 2025 RCT (n~50) | Active TMS reduced PTSD symptoms; target topography shift (medial-anterior) correlated with greater improvement; individualized targeting needed because optimal DLPFC-amygdala node varies per person | MEDIUM (single positive RCT) | Philip et al. 2025, doi:10.1176/appi.ajp.20250749 |
| Treatment-resistant VAN-deficit (Etkin) | TMS vs right dorsomedial PFC (alternative to standard rDLPFC) | Etkin & Maron-Katz 2019; conventional rTMS meta-analysis (d~0.5) | VAN-deficit subgroup hypothesized to respond better to right dmPFC TMS; intact VAN predicts standard rTMS response | MEDIUM (rTMS efficacy); LOW (VAN-stratified claim) | Etkin & Maron-Katz 2019, doi:10.1126/scitranslmed.aal3236; Cirillo et al. 2019 |
| Threat-reactive; anxiety/interoceptive amygdala overactivity | LIFU (low-intensity focused ultrasound) vs amygdala / ventral ACC (emerging) | tFUS target-engagement study mood/anxiety/trauma (N=29 + 23 controls), Mol Psychiatry 2025; GAD trial (n=25, right amygdala); active PTSD trial NCT07164105 (vACC) recruiting | Amygdala activation to threat decreased after LIFU, tracking reduced anxiety; PTSD-specific RCT not yet read out | LOW-MEDIUM (emerging; PTSD-specific pending) | Mol Psychiatry 2025, doi:10.1038/s41380-025-03033-w |
| Canonical threat-reactive (good-prognosis); intact salience network | Trauma-focused psychotherapy (prolonged exposure, CPT, EMDR) | Fonzo et al. 2017; Pannekoek et al. 2019 | Lower baseline amygdala reactivity, greater vmPFC/dlPFC engagement, intact salience-network connectivity, greater amygdala habituation predict response; Etkin VAN-deficit + impaired verbal memory predicts poor PE response | MEDIUM-HIGH (efficacy); MEDIUM (predictors) | Fonzo et al. 2017, doi:10.1176/appi.ajp.2017.16091073; Etkin & Maron-Katz 2019 |
| Severe treatment-resistant (experimental) | DBS vs amygdala (basolateral) / bed nucleus of the stria terminalis (BNST) | Case series and small pilots (Langevin et al., amygdala DBS for combat PTSD) | Symptom reduction in single cases; investigational only, no controlled efficacy data | LOW (experimental) | Langevin et al. amygdala DBS pilot (see refs) |

---

## Most defensible biotypes (cross-scale synthesis)

Each biotype below integrates MICRO, MESO, and MACRO evidence with a treatment handle and the Allen regions/edges a sensing-plus-modulation platform could target. Confidence reflects cross-consortium replication.

1. **Canonical hyperaroused threat-reactive PTSD (HIGH).** MICRO: central NE hyperdrive, IL-6 elevation, normal-to-low cortisol. MESO anchors: amygdala (basolateral) hyperreactivity, cingulate gyrus subgenual/rostral part (vmPFC/rACC) hypoactivation; defining EDGE is the amygdala-vmPFC anticorrelation that weakens or fails. MACRO: hypervigilance, intrusion, nightmares. Treatments: prolonged exposure/EMDR, SSRI, prazosin if nightmare-dominant, fMRI-guided amygdala-circuit TMS (Philip 2025).

2. **Dissociative / overmodulated subtype (HIGH; the most defensible).** The only DSM-5/ICD-11-formalized subtype, with convergent imaging, autonomic, and clinical evidence. MESO: amygdala OVERmodulated (reduced activation), mPFC/dmPFC overengagement; the amygdala-mPFC EDGE inverts from anticorrelation to increased/positive connectivity, plus increased amygdala-precuneus/posterior-insula coupling. MACRO: depersonalization, derealization (SNOMED 19006008/76104007), female and early-childhood-abuse enrichment. Treatment: phased trauma therapy; MDMA-assisted therapy responds at least equally well (MAPP pooled).

3. **GABAergic-interneuron / neuroinflammatory cellular biotype (MEDIUM-HIGH).** Postmortem-defined: downregulated interneuron module (ELFN1), I-down imbalance in dlPFC, microglial activation, upregulated glucocorticoid signaling (Girgenti 2021; Hicks 2025). Anchors to FKBP5/HPA and inflammaging at the systems level. Allen anchor: frontal cortex (dlPFC); no in-vivo edge yet.

4. **Treatment-resistant ventral-attention-deficit (Etkin) (MEDIUM; within-lab only).** Reduced intra-VAN connectivity (right anterior insula, dACC, right anterior MFG, supramarginal/TPJ), impaired verbal memory, doubled TMS/EEG recovery, poor PE response; candidate right dmPFC TMS target. Flag: not independently replicated outside Stanford.

5. **Inflammaging / cardiometabolic biotype (MEDIUM).** Elevated CRP/IL-6/TNF-alpha, accelerated GrimAge, FKBP5 and AHRR hypomethylation, low cortisol with enhanced DEX suppression. Principally peripheral; CNS correlate is microglial activation. Best paired with peripheral inflammation sensing rather than imaged directly.

**Explicitly flagged replication failures/limits:** the AURORA acute fMRI biotype clustering (Stevens 2021) did not externally replicate (Ben-Zion 2023), so the reward/inhibition acute clusters are NOT included as defensible biotypes; the Etkin VAN biotype has within-lab replication only; prazosin and SSRI response are real in aggregate but lack validated individual-level stratifiers (VA CSP #563 was negative on its primary endpoint).

---

## References

1. Grotzinger AD, Werme J, Peyrot WJ, et al. Mapping the genetic landscape across 14 psychiatric disorders. Nature. 2025. doi:10.1038/s41586-025-09820-3
2. Lanius RA, Vermetten E, Loewenstein RJ, et al. Emotion modulation in PTSD: clinical and neurobiological evidence for a dissociative subtype. Am J Psychiatry. 2010;167(6):640-647. doi:10.1176/appi.ajp.2009.09081168
3. Lanius RA, Brand B, Vermetten E, Frewen PA, Spiegel D. The dissociative subtype of PTSD: rationale, clinical and neurobiological evidence, and implications. Depress Anxiety. 2012;29(8):701-708. doi:10.1002/da.21889
4. Nicholson AA, Densmore M, Frewen PA, et al. The dissociative subtype of PTSD: unique resting-state functional connectivity of basolateral and centromedial amygdala complexes. Neuropsychopharmacology. 2015;40(10):2317-2326. doi:10.1038/npp.2015.79
5. Nicholson AA, Friston KJ, Zeidman P, et al. Dynamic causal modeling in PTSD and its dissociative subtype. Hum Brain Mapp. 2017;38(11):5551-5561. doi:10.1002/hbm.23748
6. Stevens JS, Harnett NG, Lebois LAM, et al. Brain-based biotypes of psychiatric vulnerability in the acute aftermath of trauma. Am J Psychiatry. 2021;178(11):1037-1049. doi:10.1176/appi.ajp.2021.20101526
7. Ben-Zion Z, Korem N, Spiller TR, et al. Evaluating the evidence for brain-based biotypes of psychiatric vulnerability in the acute aftermath of trauma. Am J Psychiatry. 2023. doi:10.1176/appi.ajp.20220271
8. Stevens JS, Kim YJ, Galatzer-Levy IR, et al. Amygdala reactivity and anterior cingulate habituation predict PTSD symptom maintenance after acute civilian trauma. Biol Psychiatry. 2017;81(12):1023-1029. doi:10.1016/j.biopsych.2016.11.015
9. Etkin A, Maron-Katz A, Wu W, et al. Using fMRI connectivity to define a treatment-resistant form of PTSD. Sci Transl Med. 2019;11(486):eaal3236. doi:10.1126/scitranslmed.aal3236
10. Maron-Katz A, Zhang Y, Narayan M, et al. Individual patterns of abnormality in resting-state functional connectivity reveal two data-driven PTSD subgroups. Am J Psychiatry. 2020;177(3):244-253. doi:10.1176/appi.ajp.2019.19010060
11. Shin LM, Liberzon I. The neurocircuitry of fear, stress, and anxiety disorders. Neuropsychopharmacology. 2010;35(1):169-191. doi:10.1038/npp.2009.83
12. Stevens JS, Jovanovic T, Fani N, et al. Disrupted amygdala-prefrontal functional connectivity in civilian women with PTSD. J Psychiatr Res. 2013;47(10):1469-1478. doi:10.1016/j.jpsychires.2013.05.031
13. Akiki TJ, Averill CL, Abdallah CG. A network-based neurobiological model of PTSD. Curr Psychiatry Rep. 2017;19(11):81. doi:10.1007/s11920-017-0840-4
14. Nicholson AA, Densmore M, McKinnon MC, et al. Classifying heterogeneous presentations of PTSD via the default mode, central executive, and salience networks with machine learning. NeuroImage Clin. 2020. (PMC7240193)
15. Logue MW, van Rooij SJH, Dennis EL, et al. Smaller hippocampal volume in PTSD: a multisite ENIGMA-PGC study. Biol Psychiatry. 2018;83(3):244-253. doi:10.1016/j.biopsych.2017.09.006
16. Gilbertson MW, Shenton ME, Ciszewski A, et al. Smaller hippocampal volume predicts pathologic vulnerability to psychological trauma. Nat Neurosci. 2002;5(11):1242-1247. doi:10.1038/nn958
17. Huggins AA, Baird CL, Briggs M, et al. Smaller total and subregional cerebellar volumes in PTSD: ENIGMA-PGC mega-analysis. Mol Psychiatry. 2024. doi:10.1038/s41380-023-02352-0
18. Nievergelt CM, Maihofer AX, Atkinson EG, et al. Genome-wide association analyses identify 95 risk loci and provide insights into the neurobiology of PTSD. Nat Genet. 2024;56(5):792-808. doi:10.1038/s41588-024-01707-9
19. Misganaw B, Yang R, Gautam A, et al. Machine learning for symptom-severity military PTSD subtypes and their biological correlates. Transl Psychiatry. 2021. doi:10.1038/s41398-021-01324-8
20. Klengel T, Mehta D, Anacker C, et al. Allele-specific FKBP5 DNA demethylation mediates gene-childhood trauma interactions. Nat Neurosci. 2013;16(1):33-41. doi:10.1038/nn.3275
21. Yehuda R, Daskalakis NP, Lehrner A, et al. Influences of maternal and paternal PTSD on epigenetic regulation of the glucocorticoid receptor gene in Holocaust offspring. Am J Psychiatry. 2014;171(8):872-880. doi:10.1176/appi.ajp.2014.13121571
22. Geracioti TD, Baker DG, Ekhator NN, et al. CSF norepinephrine concentrations in PTSD. Am J Psychiatry. 2001;158(8):1227-1230. doi:10.1176/appi.ajp.158.8.1227
23. Passos IC, Vasconcelos-Moreno MP, Costa LG, et al. Inflammatory markers in PTSD: systematic review, meta-analysis, and meta-regression. Lancet Psychiatry. 2015;2(11):1002-1012. doi:10.1016/S2215-0366(15)00309-0
24. Wolf EJ, Logue MW, Stoop TB, et al. Traumatic stress and accelerated DNA methylation age: a meta-analysis. Psychoneuroendocrinology. 2018. doi:10.1016/j.psyneuen.2017.12.007
25. Girgenti MJ, Wang J, Ji D, et al. Transcriptomic organization of the human brain in PTSD. Nat Neurosci. 2021;24(1):24-33. doi:10.1038/s41593-020-00748-7
26. Hicks EM, et al. Single-cell transcriptomic and chromatin dynamics of the human brain in PTSD. Nature. 2025;643:744. doi:10.1038/s41586-025-09083-y
27. Jaffe AE, et al. Single-nucleus transcriptome profiling of DLPFC: neuronal gene expression including 17q21.31 in PTSD. Am J Psychiatry. 2023. doi:10.1176/appi.ajp.20220478
28. Immune imbalance in the human hippocampus in PTSD revealed by single-nucleus transcriptomics. Front Immunol. 2025. (PMC, fimmu.2025.1697171)
29. Schneider M, Schwerdtfeger A. Autonomic dysfunction in PTSD indexed by heart rate variability: a meta-analysis. Psychol Med. 2020;50(12):1937-1948. doi:10.1017/S003329172000207X
30. Trusko BE, et al. Are PTSD mental health terms found in SNOMED-CT medical terminology. J Trauma Stress. 2010. doi:10.1002/jts.20591
31. MacNamara A, Rabinak CA, Kennedy AE, et al. Emotion regulatory brain function and SSRI treatment in PTSD. Neuropsychopharmacology. 2016;41(2):611-618. doi:10.1038/npp.2015.190
32. Raskind MA, Peskind ER, Chow B, et al. Trial of prazosin for PTSD in military veterans (VA CSP #563). N Engl J Med. 2018;378(6):507-517. doi:10.1056/NEJMoa1507598
33. Mitchell JM, Bogenschutz M, Lilienstein A, et al. MDMA-assisted therapy for severe PTSD: phase 3 RCT (MAPP1). Nat Med. 2021;27(6):1025-1033. doi:10.1038/s41591-021-01336-3
34. Mitchell JM, et al. MDMA-assisted therapy for moderate to severe PTSD: phase 3 RCT (MAPP2). Nat Med. 2023;29:2473-2480. doi:10.1038/s41591-023-02565-4
35. FDA Complete Response Letter to Lykos Therapeutics, published September 2025. https://psychedelicalpha.com/news/breaking-fda-publishes-lykos-therapeutics-mdma-complete-response-letter-crl
36. Philip NS, et al. Personalized fMRI-guided TMS targeting the threat neurocircuitry in PTSD: a randomized clinical trial. Am J Psychiatry. 2025. doi:10.1176/appi.ajp.20250749
37. Philip NS, et al. Advancing TMS for PTSD - from networks to individuals. Transcranial Magnetic Stimulation. 2025. (PMC12499369)
38. Fonzo GA, Goodkind MS, Oathes DJ, et al. PTSD psychotherapy outcome predicted by brain activation during emotional reactivity and regulation. Am J Psychiatry. 2017;174(12):1175-1184. doi:10.1176/appi.ajp.2017.16091073
39. Cirillo P, Gold AK, Nardi AE, et al. TMS in anxiety and trauma-related disorders: systematic review and meta-analysis. Brain Behav. 2019. doi:10.1002/brb3.1284
40. Low-intensity transcranial focused ultrasound amygdala neuromodulation: double-blind sham-controlled target engagement and single-arm clinical trial. Mol Psychiatry. 2025. doi:10.1038/s41380-025-03033-w
41. Sleep Power Spectral Density and Spindles in PTSD and Their Relationship to Symptom Severity. Front Psychiatry. 2021. (PMC8640175)
42. Characterizing PTSD Using Electrophysiology: Towards a Precision Medicine Approach. 2025. (PMC12130596)
43. SNOMED CT: Posttraumatic stress disorder 47505003; Chronic post-traumatic stress disorder 313182004. https://www.findacode.com/snomed/47505003
44. MISTIC: Magnesium-Ibogaine: The Stanford Experience. Nat Med. 2024.
45. Feder A, et al. Repeated-dose intravenous ketamine for chronic PTSD: randomized clinical trial. (see PMC)
46. Langevin J-P, et al. Deep brain stimulation of the basolateral amygdala for treatment-refractory combat PTSD. Biol Psychiatry. (pilot)

---

*Prepared for Cytognosis Foundation, 14-disorder multi-scale biotype set. Ontology IDs marked "approx, needs curation" require verification against current SNOMED CT, HPO, and GO releases before clinical or grant use.*

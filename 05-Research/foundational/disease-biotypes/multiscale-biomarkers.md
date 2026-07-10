# Multi-Scale and Multimodal Biomarker Studies: Prior Art for a Genome-Connectome-Phenotype Platform

Prepared for: Cytognosis Foundation, X-Labs platform positioning
Date: 25 May 2026
Scope: A documented review of prior work that links biological scales (genome, connectome, phenotype) in the same individuals. The goal is to position a new multi-scale, continuous, individual-level platform against the existing literature and to integrate the key quantitative findings (sample sizes, effect sizes, reproducibility) into an honest educational summary. Citation style is inline Vancouver-like with DOI or URL. Effect sizes and reproducibility limits are reported plainly, because they are the load-bearing facts for any platform claim.

---

## 0. Framing: what "multi-scale" actually means here

Three biological scales recur throughout this document:

- **Genome**: fixed, inherited germline variation, typically summarized as common-variant GWAS hits, heritability estimates (SNP-h2), genetic correlations (rg), or polygenic scores (PGS).
- **Connectome**: the wiring and dynamic coordination of the brain, measured in living humans almost exclusively by MRI (structural T1, diffusion MRI tractography, resting-state and task functional MRI). Imaging-derived phenotypes (IDPs) are the standard summary.
- **Phenotype**: observable traits, including cognition, behavior, lifestyle, demographics, psychiatric diagnosis, and symptom dimensions.

The Cytognosis framing treats the connectome as a **mediator**: the genome is fixed at conception, the connectome develops under both genetic and environmental influence, and phenotype emerges from the connectome plus ongoing environment. This is a causal-chain framing (genome to connectome to phenotype), and Section 8 evaluates how much of the prior literature actually supports treating the connectome as a mediator rather than a correlate.

Two cross-cutting facts shape everything below:

1. **Effect sizes linking the connectome to behavior are small.** The largest replicable univariate brain-behavior correlation is roughly r = 0.14, and the largest replicable multivariate one is roughly r = 0.34 (Marek et al. 2022, Section 5). Structural case-control differences in psychiatric disorders sit at Cohen d of about 0.1 to 0.5 (Section 2).
2. **Almost all of this work is cross-sectional and group-level.** It compares groups at one or two MRI snapshots. None of it provides continuous, longitudinal, individual connectome readout (Section 9). This is the central gap.

---

## 1. Imaging-genetics in population biobanks

Population biobanks recruit from the general population rather than from a clinic. The dominant resource is UK Biobank, which has paired genome-wide genotyping with multimodal brain MRI in tens of thousands of largely healthy adults. This makes it the canonical setting for linking the genome to the connectome at scale.

### 1.1 UK Biobank brain imaging GWAS: Elliott et al. 2018

Elliott and colleagues ran the first large GWAS of brain IDPs in UK Biobank, using a discovery sample of 8,428 participants and 3,144 functional and structural IDPs (Elliott et al. 2018, Nature, doi:10.1038/s41586-018-0571-7). Key results:

- Many IDPs are heritable. The study reported 148 clusters of SNP-IDP associations that replicated at P < 0.05, against an expected 21 by chance.
- Interpretable biology emerged: iron-handling genes (for example genes related to iron transport and storage) associated with magnetic susceptibility of subcortical tissue; extracellular-matrix and epidermal-growth-factor genes associated with white-matter microstructure and white-matter hyperintensities; and midline axon-guidance genes associated with the organization of the pontine crossing tract.

The headline is that the living human connectome and brain structure carry a measurable, interpretable genetic signal, but individual SNP effects are small and require thousands of scans to detect.

### 1.2 The BIG40 resource: Smith et al. 2021

Smith and colleagues expanded the same approach using the 2020 imaging release, roughly tripling the discovery sample and increasing the IDP count to almost 4,000 (Smith et al. 2021, Nature Neuroscience, doi:10.1038/s41593-021-00826-4). This produced the open BIG40 server (https://open.oxcin.ox.ac.uk/ukbiobank/big40/). Key results:

- 692 replicated clusters of genetic associations across the IDPs, including 12 on the X chromosome.
- Heritable signal spans structural, diffusion (connectome wiring), and functional IDPs, with diffusion and structural traits generally more heritable than task-fMRI traits.

| Study | Year | Sample (discovery) | IDPs | Replicated association clusters | Resource |
|---|---|---|---|---|---|
| Elliott et al. | 2018 | 8,428 | 3,144 | 148 (vs 21 expected) | doi:10.1038/s41586-018-0571-7 |
| Smith et al. (BIG40) | 2021 | ~22,000 | ~3,900 | 692 (incl. 12 on X) | doi:10.1038/s41593-021-00826-4 |

### 1.3 Genetic correlations between brain IDPs and psychiatric or behavioral traits

The biobank GWAS resources support genetic-correlation analyses, which ask whether the same common variants influence both a brain trait and a disorder. From the cortical-architecture work (Grasby et al. 2020, Section 2.3) and the biobank IDP GWAS, brain structural variation is genetically correlated with cognitive function, Parkinson disease, insomnia, depression, neuroticism, and ADHD, among others. These genetic correlations are typically modest (rg often well below 0.3 in absolute value) and establish shared genetic architecture, not a causal route. Mendelian randomization (Section 8.3) is the tool used to push toward causal claims.

### 1.4 The general-population vs disease-cohort distinction

This is a structural feature of the field worth stating explicitly:

- **Population biobanks** (UK Biobank, and developmentally ABCD) sample mostly healthy people. They are well powered for heritability, genetic correlation, and normative-range estimation, but contain relatively few cases of any single disorder.
- **Disease cohorts and meta-analytic consortia** (ENIGMA, B-SNIP, clinical-trial samples) enrich for cases. They are well powered for case-control contrasts but are less representative of the population and often lack genome-wide data on the same individuals.

A multi-scale platform that wants both representativeness and disease signal has to bridge these two worlds. Normative modeling (Section 6) is the main statistical bridge built so far.

---

## 2. ENIGMA Consortium: the disease-focused neuroimaging network

ENIGMA (Enhancing NeuroImaging Genetics through Meta-Analysis) is the largest distributed neuroimaging meta-analysis network. Rather than centralizing raw data, it distributes standardized analysis protocols to dozens of sites, which return harmonized summary statistics. This is how it reaches sample sizes in the tens of thousands for disorders that no single site could power.

### 2.1 Structure

ENIGMA is organized into disease working groups plus methodological cores. Disease working groups include Major Depressive Disorder (MDD), Schizophrenia (SCZ), Bipolar Disorder (BD), Post-Traumatic Stress Disorder (PTSD), Obsessive-Compulsive Disorder (OCD), Autism Spectrum Disorder (ASD), Attention-Deficit/Hyperactivity Disorder (ADHD), Addiction, Anxiety, and 22q11.2 deletion syndrome, among others. The ENIGMA-Genetics working group runs the imaging-genetics GWAS, frequently in partnership with the CHARGE consortium.

### 2.2 Cross-disorder convergence: the transdiagnostic gray-matter finding

Goodkind and colleagues conducted a voxel-based morphometry meta-analysis of 193 studies comprising 15,892 individuals across six diagnostic groups (schizophrenia, bipolar disorder, depression, addiction, OCD, anxiety) (Goodkind et al. 2015, JAMA Psychiatry, doi:10.1001/jamapsychiatry.2014.2206). Gray-matter loss converged across all six diagnoses in three regions: the dorsal anterior cingulate cortex, the right insula, and the left insula. In independent healthy samples these regions formed a tightly interconnected network engaged during cognitive control, and lower gray matter there tracked poorer executive function. Diagnosis-specific effects were few. This is the foundational quantitative evidence that distinct DSM categories share a common structural substrate, which motivates transdiagnostic biotyping.

A parallel literature on cortical thinning reinforces the same point: across disorders, the regions that thin most overlap substantially, consistent with a shared cortical-control axis.

### 2.3 ENIGMA imaging-genetics: subcortical and cortical GWAS

ENIGMA-Genetics produced three landmark imaging-genetics papers:

- **Subcortical volumes (Hibar et al. 2015, Nature, doi:10.1038/nature14101).** GWAS of seven subcortical regional volumes plus intracranial volume in 30,717 individuals from 50 cohorts (ENIGMA with CHARGE). Identified novel loci for putamen and caudate volume and confirmed loci for hippocampal and intracranial volume. A follow-up expanded this to 38,851 individuals (Satizabal et al. 2019, Nature Genetics, doi:10.1038/s41588-019-0511-y).
- **Cortical surface area and thickness (Grasby et al. 2020, Science, doi:10.1126/science.aay6690).** GWAS meta-analysis in 51,665 individuals across the whole cortex and 34 regions. Identified 199 significant loci. Total surface-area loci were enriched in regulatory elements active during prenatal cortical development (supporting the radial-unit hypothesis), and regional surface-area loci clustered near Wnt-signaling genes. Cortical structure was genetically correlated with cognition and with several disorders.

The biological takeaway is that the connectome's structural scaffold (subcortical volumes, cortical area and thickness) is partly under common-variant genetic control, and that the genetics points to neurodevelopmental mechanisms (progenitor expansion, areal patterning).

### 2.4 Effect sizes and what they imply

ENIGMA case-control structural differences are small to moderate. In the schizophrenia cortical meta-analysis (van Erp et al. 2018, Biological Psychiatry, doi:10.1016/j.biopsych.2018.04.023; 4,474 cases, 5,098 controls), widespread cortical thinning reached Cohen d of about -0.53 hemisphere-wide, with regional effects ranging from about -0.54 (right fusiform) to -0.08 (left pericalcarine). Schizophrenia is among the largest structural effects in psychiatry. For MDD and anxiety, effects are typically Cohen d of about 0.1 to 0.3.

| Disorder (ENIGMA) | Typical structural Cohen d | Notes |
|---|---|---|
| Schizophrenia | ~0.3 to 0.5 (up to ~0.54 regionally) | Largest psychiatric structural effects; medication inflates effect |
| Bipolar disorder | ~0.2 to 0.3 | Cortical thinning overlapping SCZ |
| MDD | ~0.1 to 0.2 | Small; hippocampal and cortical thinning |
| Anxiety / OCD / PTSD | ~0.1 to 0.3 | Small, region-specific |

**Implication.** A Cohen d of 0.2 means group distributions overlap by roughly 92 percent. A structural IDP that separates a disorder group from controls at d = 0.2 cannot classify an individual reliably. This is the core reason group-level imaging biomarkers have not translated into individual diagnostic tools, and it sets the bar a new platform must clear: individual-level, longitudinal signal that exceeds these cross-sectional group contrasts.

---

## 3. ABCD Study (Adolescent Brain Cognitive Development)

The ABCD Study is the largest long-term study of brain development and child health in the United States, following roughly 11,800 to 11,900 youth recruited at ages 9 to 10 across 21 sites, with planned follow-up across a decade (https://abcdstudy.org/; Casey et al. 2018, Dev Cogn Neurosci, doi:10.1016/j.dcn.2018.03.001).

### 3.1 What ABCD measures and enables

ABCD is genuinely multi-scale within individuals: genome-wide genotyping, multimodal MRI (structural, diffusion, resting-state and task fMRI), extensive cognitive and behavioral assessment, mental-health measures, and detailed environmental and social data, repeated longitudinally. This combination, in one cohort, supports:

- **Developmental trajectories.** Because it is longitudinal, ABCD can chart within-person change, not just cross-sectional group differences. This is rare among multi-scale resources.
- **Genome plus brain plus behavior models.** Polygenic scores, brain IDPs, and behavior can be modeled jointly in the same children.

### 3.2 Key biotype and prediction findings

- Structural MRI IDPs are the most heritable modality in ABCD, accounting for roughly 63 percent of heritable traits, followed by diffusion measures (about 34 percent for fractional anisotropy), with task-fMRI measures far less heritable (about 3 to 4 percent) (polygenic-architecture analysis, Nature Communications 2025, doi:10.1038/s41467-025-63312-6).
- Polygenic scores for educational attainment, IQ, and depression covary with brain volume and surface area; internalizing-trait PGS (anxiety, neuroticism, depression) show inverse relationships with brain measures. Effect sizes are small, consistent with the BWAS findings in Section 5.
- ABCD has been central to demonstrating that brain-based predictive models of childhood cognition are reproducible only at large sample sizes and that they partially mediate relationships between cognition and socio-demographic, psychological, and genetic factors.

ABCD is the closest existing approximation to the genome-connectome-phenotype chain in a single longitudinal cohort. Its limitation for the present purpose is that the connectome readout is still a handful of MRI snapshots over years, not continuous monitoring.

---

## 4. Human Connectome Project and connectome-behavior association

The Human Connectome Project (HCP) collected very high-quality multimodal MRI in roughly 1,200 healthy young adults, with rich behavioral, cognitive, and demographic measures, and made it openly available (Van Essen et al. 2013, NeuroImage, doi:10.1016/j.neuroimage.2013.05.041). HCP became the testbed for methods linking the connectome to phenotype.

### 4.1 The positive-negative mode: Smith et al. 2015

Smith and colleagues applied canonical correlation analysis (CCA) to link individual resting-state functional connectomes to 280 behavioral and demographic measures in 461 HCP subjects (Smith et al. 2015, Nature Neuroscience, doi:10.1038/nn.4125). They found a single dominant mode of population covariation, a "positive-negative" axis: one end associated with positive traits (higher fluid intelligence, more education, better memory, life satisfaction) and the other with negative traits (substance use, anger, rule-breaking). A specific connectivity pattern (strong in default-mode and frontoparietal regions) loaded on this axis. This was an influential demonstration that a low-dimensional latent axis can link the connectome to a broad swath of lifestyle and behavior, which is conceptually aligned with a "mental health coordinate." However, the original CCA was later shown to be unstable at this sample size and required larger samples to replicate (see Section 5), an important caution.

### 4.2 Connectome fingerprinting and connectome-based predictive modeling

- **Fingerprinting (Finn et al. 2015, Nature Neuroscience, doi:10.1038/nn.4135).** An individual's functional connectivity profile is stable and distinctive enough to identify that person from a group, across sessions and across rest vs task. The frontoparietal network was most distinctive. The same individuating networks were also most predictive of fluid intelligence. This establishes that the functional connectome has a reliable individual signature, a precondition for individual-level monitoring.
- **Connectome-based predictive modeling (CPM; Shen, Finn, Scheinost et al. 2017, Nature Protocols, doi:10.1038/nprot.2016.178).** A standardized pipeline that builds predictive models of behavior from whole-connectome data using cross-validation. CPM has been applied to fluid intelligence, attention, and transdiagnostic constructs such as craving.
- **Connectome-wide association studies (CWAS).** Multivariate distance-based approaches that test every connectome edge for association with a phenotype, the connectome analog of GWAS.

The recurring lesson from HCP-era work is that the functional connectome carries individual and predictive signal, but the effect sizes for behavior are modest and the multivariate methods are powerful enough to overfit small samples, which sets up Section 5.

---

## 5. The reproducibility reckoning (read this section carefully)

This is the most important section for an honest platform claim. The field went through a correction between roughly 2019 and 2022 that reset expectations about how large brain-behavior effects really are and how many people are needed to measure them reliably.

### 5.1 Marek, Tervo-Clemmens, Dosenbach et al. 2022: BWAS need thousands

Marek, Tervo-Clemmens, and colleagues analyzed the three largest neuroimaging datasets available (ABCD, 11,874; UK Biobank, 35,375; HCP, 1,200) to estimate the true size and reproducibility of brain-wide association studies (BWAS) (Marek, Tervo-Clemmens et al. 2022, Nature, doi:10.1038/s41586-022-04492-9). Findings:

- The largest **replicable** brain-behavior associations were about **r = 0.14 for univariate** methods and about **r = 0.34 for multivariate** methods.
- In the small samples typical of past neuroimaging studies (tens to low hundreds), inflated and irreproducible effect sizes were ubiquitous, regardless of method. Statistically significant associations in small samples were frequently in the wrong direction on replication.
- Reaching reliable, reproducible univariate brain-behavior associations requires samples in the thousands.

| Method | Largest replicable effect (Marek 2022) | Sample needed for reproducibility |
|---|---|---|
| Univariate (single edge or region vs behavior) | r ~ 0.14 | thousands |
| Multivariate (whole-connectome model vs behavior) | r ~ 0.34 | high hundreds to thousands |

**Implication for biotyping.** Any biotype defined by a brain-behavior or brain-symptom correlation in a few hundred people is at high risk of being a sampling artifact. A platform claiming individual biotype assignment must either operate in the large-N regime, use multivariate models with honest cross-validation, or exploit within-person longitudinal data (which trades cross-sectional N for repeated measures per person, a different and underexploited route).

### 5.2 The Drysdale-Dinga case: a specific replication failure

Drysdale and colleagues reported four resting-state connectivity biotypes of depression that predicted differential rTMS response (Drysdale et al. 2017, Nature Medicine, doi:10.1038/nm.4246), an influential and widely cited result. Dinga and colleagues attempted to reproduce the clustering with proper nested cross-validation and null testing and found that the specific four-cluster solution did not survive: the data did not support discrete clusters, and the apparent biotypes reflected analytic flexibility rather than stable structure (Dinga et al. 2019, NeuroImage Clinical, doi:10.1016/j.nicl.2019.101796). The deeper transdiagnostic claim (that circuit-level subtypes carry treatment-relevant information) remains plausible and is supported by other work, but the specific discrete-cluster biotype did not replicate. This is the canonical cautionary tale for connectome-based biotyping.

### 5.3 What sample sizes and designs actually deliver reproducible associations

Synthesizing Sections 1 to 5:

- **Cross-sectional univariate** brain-behavior associations: need thousands of people; expect r near 0.1 to 0.15.
- **Cross-sectional multivariate** (CCA, CPM): can reach r near 0.3, but require large N and strict out-of-sample validation to avoid the Smith-2015 and Drysdale instability.
- **Longitudinal within-person designs**: largely unexploited at scale for the connectome. Dense within-person sampling (many measurements per individual) can in principle detect individual-level effects that cross-sectional designs cannot, because each person serves as their own control. This is the regime a continuous-monitoring platform would occupy, and it is precisely the regime the existing MRI-snapshot literature does not cover.

---

## 6. Normative modeling and brain charts

Normative modeling reframes the question. Instead of asking "is this group different from controls," it asks "where does this individual sit relative to a population reference," analogous to pediatric height-and-weight growth charts.

### 6.1 Brain charts for the human lifespan: Bethlehem, Seidlitz, Alexander-Bloch et al. 2022

This work aggregated 123,984 MRI scans from 101,457 participants across more than 100 studies, spanning 115 days post-conception to 100 years of age, to build normative growth curves (centile trajectories) for brain structural metrics (Bethlehem, Seidlitz, Alexander-Bloch et al. 2022, Nature, doi:10.1038/s41586-022-04554-y; resource at http://www.brainchart.io/). It provides an open reference against which any new scan can be assigned a centile, and it characterized non-linear trajectories of growth and decline (rapid early growth, slow later decline). Individual centile deviations were associated with neurological and psychiatric conditions.

### 6.2 The Marquand normative-deviation framework

Marquand and colleagues introduced the statistical framework that underpins this shift (Marquand et al. 2016, Biological Psychiatry, doi:10.1016/j.biopsych.2015.12.023; conceptual extension Marquand et al. 2019, Molecular Psychiatry, doi:10.1038/s41380-019-0441-1). The core idea: model the full population range of a brain measure as a function of age and other covariates, then express each individual as a deviation (z-score) from that normative pattern. This handles the heterogeneity that defeats case-control designs, because two patients with the same diagnosis may have deviations in entirely different regions.

### 6.3 Why this reframes biotypes

Normative modeling reframes a "biotype" not as membership in a discrete cluster (the approach that failed in Drysdale-Dinga) but as a **pattern of deviations from a reference** in a continuous space. This sidesteps the cluster-stability problem and aligns naturally with an individualized coordinate: a person is located by their vector of normative deviations, which can be tracked over time. For a platform built around a personalized health coordinate, normative modeling is the most directly relevant statistical prior art, because it provides the reference frame against which a continuous individual readout would be scored.

| Approach | Question asked | Output | Relevance to a coordinate |
|---|---|---|---|
| Case-control | Group A vs group B | Mean difference, Cohen d | Low (group-level only) |
| Discrete clustering | Which cluster | Cluster label | Low (often unstable) |
| Normative modeling | Where vs reference | Per-region deviation z-scores | High (individual coordinate) |

---

## 7. Multivariate genome-to-phenotype methods

The genome-to-phenotype link is rarely one gene to one trait. Multivariate methods model many variants and many traits jointly.

### 7.1 Genomic SEM and the cross-disorder genetic factor structure

Genomic structural equation modeling (Genomic SEM; Grotzinger et al. 2019, Nature Human Behaviour, doi:10.1038/s41562-019-0566-x) models the joint genetic architecture of multiple traits from GWAS summary statistics, estimating latent genetic factors that explain shared heritability across disorders. Applications:

- An 11-disorder analysis identified higher-order genetic factors across psychiatric conditions and linked them to functional-genomic and molecular levels (Grotzinger et al. 2022, Nature Genetics, doi:10.1038/s41588-022-01057-4).
- The recent 14-disorder analysis used Genomic SEM on GWAS from more than one million people and found five genomic factors (compulsive disorders; schizophrenia and bipolar disorder; neurodevelopmental conditions; internalizing conditions; substance-use conditions) that explained on average about 66 percent of the per-disorder genetic variance and were associated with 238 pleiotropic loci, with signal concentrated early in brain development (Grotzinger et al. 2025, Nature, doi:10.1038/s41586-025-09820-3).

This is the genome-scale analog of the transdiagnostic structural convergence in Section 2: at the genetic level, psychiatric disorders share a low-dimensional latent factor structure, not independent etiologies.

### 7.2 Multimodal fusion methods (linked ICA, PLS, CCA)

For fusing modalities within individuals:

- **Linked independent component analysis (linked ICA; Groves et al. 2011, NeuroImage, doi:10.1016/j.neuroimage.2011.03.034).** Jointly decomposes multiple imaging modalities (for example structural plus diffusion plus functional) into shared components, used in UK Biobank to relate multimodal IDPs to non-imaging variables.
- **Partial least squares (PLS) and canonical correlation analysis (CCA).** Find latent dimensions that maximally covary between two data blocks (for example connectome and behavior, Smith 2015 in Section 4.1, or gene expression and imaging in Section 8.2). Powerful but, as Section 5 stresses, prone to overfitting without large N and rigorous out-of-sample validation.

### 7.3 Mendelian randomization for causal inference

Mendelian randomization (MR) uses germline genetic variants as instrumental variables to test whether an exposure (for example a brain IDP) causally affects an outcome (for example a disorder), exploiting the fact that genotype is fixed at conception and not confounded by lifestyle. Applied to imaging:

- MR has supported causal effects of specific brain IDPs on psychiatric disorder risk (Guo et al. 2022, doi:10.1016/j.biopsych.2022.08.024) and bidirectional MR has linked white-matter structural-connectivity phenotypes (206 connectivity traits, n = 26,333 UK Biobank) to several disorders, including a negative association between frontoparietal-to-default-mode connectivity and autism risk (Xiao et al. 2025, Psychiatry Clin Neurosci, doi:10.1111/pcn.13897). MR is the main existing tool for pushing genome-brain-behavior associations toward causal claims, and it directly serves the genome-to-connectome-to-phenotype framing.

---

## 8. Causal multi-scale work: the connectome as mediator

This section evaluates how much prior work actually treats the connectome as a causal mediator between the (fixed) genome and (genome-plus-environment) phenotype, which is the Cytognosis framing.

### 8.1 The connectome as mediator: limited but emerging

A genuine mediation framing requires showing genome to connectome to phenotype as a directed chain in the same individuals. The pieces exist separately (genome to connectome: Sections 1, 2.3; connectome to phenotype: Sections 4, 5; genome to phenotype: Section 7), but full triadic mediation analyses are rare. The strongest examples come from MR network analyses (Section 7.3), which sequence genome to brain to disorder, and from large-cohort path models in ABCD and UK Biobank that estimate brain mediation of genome-behavior links (for example brain-based predictive models partially mediating cognition-genetics relationships, Section 3.2). The mediated fraction is typically small, consistent with the small connectome-behavior effects in Section 5, which means the connectome explains only part of the genome-phenotype link as currently measured by cross-sectional MRI.

### 8.2 Imaging transcriptomics: linking gene expression to the connectome

Imaging transcriptomics links the Allen Human Brain Atlas (AHBA), a spatial map of gene expression across cortical regions, to macroscale neuroimaging patterns (reviewed by Fornito, Arnatkeviciute and colleagues). Key references:

- A practical guide to linking brain-wide gene expression and neuroimaging (Arnatkeviciute, Fulcher, Fornito 2019, NeuroImage, doi:10.1016/j.neuroimage.2019.01.011).
- Best-practices review (Fornito et al. 2023, Biological Psychiatry, doi:10.1016/j.biopsych.2022.10.016), which catalogs how analytic choices in atlas processing, spatial-autocorrelation null models, and enrichment testing affect conclusions.

The field correlates regional gene-expression profiles with regional connectome properties (for example hub regions express specific metabolic and synaptic gene sets) and with disorder-related imaging maps, connecting the molecular and macroscale levels. Caveats are substantial: the AHBA derives from only six donor brains, sampling is uneven, and spatial-autocorrelation confounds inflate naive correlations, so conclusions depend heavily on null models.

### 8.3 Disentangling genetic vs environmental contributions to the connectome

Twin and family designs (for example within HCP, which oversampled twins and siblings) estimate the heritability of connectome features and partition variance into genetic vs shared and unique environmental components. Functional-connectivity heritability is modest and edge-dependent; structural-connectivity and white-matter traits are more heritable. This work establishes that the connectome is shaped by both genome and environment, which is the premise of treating it as a mediator (an inherited substrate modified by experience), but it does not by itself trace the causal chain to phenotype.

---

## 9. What is missing: the gap for a new platform

The prior art is impressive at group level and cross-sectional scale, but it leaves a specific, well-defined gap.

### 9.1 No continuous longitudinal connectome readout in the general population

Every resource above measures the connectome with MRI, which is a cross-sectional snapshot (or a handful of snapshots, in ABCD and UK Biobank repeat imaging). There is no general-population cohort with **continuous, longitudinal connectome readout**. MRI cannot be worn, cannot run all day, and is captured at most a few times per person over years. The dynamic, state-dependent behavior of the connectome (across sleep, stress, treatment, relapse) is therefore largely unmeasured at the individual level over time.

### 9.2 Most multi-scale work is cross-sectional and group-level

As Section 5 establishes, cross-sectional group-level designs deliver small, hard-to-reproduce effects and cannot reliably locate an individual. The within-person longitudinal regime, where each person is their own reference and dense repeated measures can detect individual effects, is essentially unexploited for the connectome because the measurement technology (MRI) does not support it.

### 9.3 Causal mediation is asserted more than measured

Treating the connectome as a mediator between genome and phenotype is biologically reasonable and partly supported by MR (Section 7.3), but full triadic, longitudinal, individual-level mediation has not been demonstrated, because the connectome term has only ever been a snapshot.

### 9.4 The opportunity

The gap a new platform addresses is the intersection of four properties that no existing resource combines:

| Property | UK Biobank | ENIGMA | ABCD | HCP | A continuous platform |
|---|---|---|---|---|---|
| Individual-level (not just group) | partial | no | partial | partial | yes |
| Longitudinal | sparse | no | sparse | no | continuous |
| Continuous connectome readout | no | no | no | no | yes |
| Genome-connectome-phenotype in same person | yes | partial | yes | partial | yes |
| Causal-chain (mediation) capable | weak | no | partial | no | designed for it |

A platform that delivers **wearable, continuous, individual, multi-scale, causal** readout would occupy the empty cell: it would supply the within-person longitudinal connectome data that converts the small cross-sectional effects of the prior literature into potentially detectable individual-level signal, and it would let the connectome be measured densely enough over time to test, rather than assume, its role as mediator between a fixed genome and an evolving phenotype.

---

## 10. Summary table

| Study / consortium | Scales linked | Sample size | Key finding | Key limitation |
|---|---|---|---|---|
| Elliott et al. 2018 (UK Biobank) | genome + connectome | 8,428 | 148 replicated SNP-IDP clusters; brain IDPs are heritable with interpretable biology | Cross-sectional; small per-SNP effects |
| Smith et al. 2021 (BIG40) | genome + connectome | ~22,000 | 692 replicated association clusters across ~3,900 IDPs | Cross-sectional; population-only (few cases) |
| Goodkind et al. 2015 (meta-analysis) | connectome + phenotype (Dx) | 15,892 | Transdiagnostic gray-matter loss in dACC and bilateral insula | Structural only; group-level |
| Hibar et al. 2015 (ENIGMA/CHARGE) | genome + connectome | 30,717 | Common variants influence subcortical volumes | Volumes only; no phenotype mediation |
| Grasby et al. 2020 (ENIGMA) | genome + connectome | 51,665 | 199 loci for cortical area/thickness; neurodevelopmental enrichment; rg with disorders | Cross-sectional; genetic correlation, not causation |
| van Erp et al. 2018 (ENIGMA-SCZ) | connectome + phenotype (Dx) | 9,572 | Widespread cortical thinning, Cohen d up to ~0.54 | Group-level; medication confound |
| ABCD Study | genome + connectome + phenotype + environment | ~11,800 | Multi-scale longitudinal youth cohort; sMRI most heritable; small PGS-brain links | Connectome = few MRI snapshots over years |
| Smith et al. 2015 (HCP) | connectome + phenotype | 461 | Single positive-negative mode links connectivity to behavior/lifestyle | Unstable at this N; needs large samples to replicate |
| Finn et al. 2015 (HCP) | connectome + phenotype | ~126 | Connectome "fingerprint" identifies individuals; predicts fluid intelligence | Small N; healthy adults |
| Marek et al. 2022 (BWAS) | connectome + phenotype | 48,000+ pooled | Replicable effects only r~0.14 (univariate), r~0.34 (multivariate); need thousands | Establishes the limit, not a new biomarker |
| Drysdale 2017 / Dinga 2019 | connectome + phenotype (Dx, treatment) | ~1,200 / reanalysis | 4 depression biotypes proposed; discrete clusters did not replicate | Cautionary tale for clustering biotypes |
| Bethlehem et al. 2022 (brain charts) | connectome (normative) + phenotype | 101,457 | Lifespan normative growth curves; centile deviations track disorders | Cross-sectional aggregate; structural metrics |
| Marquand et al. 2016/2019 | connectome (normative) + phenotype | varies | Normative-deviation framework reframes biotypes as deviations, not clusters | Reference frame, not a measurement device |
| Grotzinger et al. 2025 (Genomic SEM) | genome + phenotype | 1,056,201 | 5 genomic factors explain ~66% of per-disorder genetic variance; 238 pleiotropic loci | Genome-to-phenotype; connectome inferred, not measured |
| Xiao et al. 2025 (MR connectome) | genome + connectome + phenotype (causal) | 26,333 (+ disorder GWAS) | MR supports causal effects of white-matter connectivity on disorders | Instrument assumptions; group-level |
| Imaging transcriptomics (Fornito et al.) | molecular (gene expr.) + connectome | 6 donor brains (AHBA) | Regional gene expression correlates with connectome organization | 6 donors; spatial-autocorrelation confounds |

---

## Sources

- Elliott LT et al. 2018, Nature. doi:10.1038/s41586-018-0571-7. https://www.nature.com/articles/s41586-018-0571-7
- Smith SM et al. 2021, Nat Neurosci. doi:10.1038/s41593-021-00826-4. https://www.nature.com/articles/s41593-021-00826-4 (BIG40: https://open.oxcin.ox.ac.uk/ukbiobank/big40/)
- Goodkind M et al. 2015, JAMA Psychiatry. doi:10.1001/jamapsychiatry.2014.2206. https://pmc.ncbi.nlm.nih.gov/articles/PMC4791058/
- Hibar DP et al. 2015, Nature. doi:10.1038/nature14101. https://www.nature.com/articles/nature14101
- Satizabal CL et al. 2019, Nat Genet. doi:10.1038/s41588-019-0511-y
- Grasby KL et al. 2020, Science. doi:10.1126/science.aay6690
- van Erp TGM et al. 2018, Biol Psychiatry. doi:10.1016/j.biopsych.2018.04.023
- Casey BJ et al. 2018, Dev Cogn Neurosci (ABCD). doi:10.1016/j.dcn.2018.03.001. https://abcdstudy.org/
- ABCD polygenic architecture 2025, Nat Commun. doi:10.1038/s41467-025-63312-6
- Van Essen DC et al. 2013, NeuroImage (HCP). doi:10.1016/j.neuroimage.2013.05.041
- Smith SM et al. 2015, Nat Neurosci. doi:10.1038/nn.4125. https://www.nature.com/articles/nn.4125
- Finn ES et al. 2015, Nat Neurosci. doi:10.1038/nn.4135. https://www.nature.com/articles/nn.4135
- Shen X et al. 2017, Nat Protoc (CPM). doi:10.1038/nprot.2016.178
- Marek S, Tervo-Clemmens B et al. 2022, Nature. doi:10.1038/s41586-022-04492-9. https://pubmed.ncbi.nlm.nih.gov/35296861/
- Drysdale AT et al. 2017, Nat Med. doi:10.1038/nm.4246
- Dinga R et al. 2019, NeuroImage Clin. doi:10.1016/j.nicl.2019.101796
- Bethlehem RAI, Seidlitz J, Alexander-Bloch AF et al. 2022, Nature. doi:10.1038/s41586-022-04554-y. https://www.nature.com/articles/s41586-022-04554-y (http://www.brainchart.io/)
- Marquand AF et al. 2016, Biol Psychiatry. doi:10.1016/j.biopsych.2015.12.023
- Marquand AF et al. 2019, Mol Psychiatry. doi:10.1038/s41380-019-0441-1
- Grotzinger AD et al. 2019, Nat Hum Behav (Genomic SEM). doi:10.1038/s41562-019-0566-x
- Grotzinger AD et al. 2022, Nat Genet. doi:10.1038/s41588-022-01057-4
- Grotzinger AD et al. 2025, Nature. doi:10.1038/s41586-025-09820-3. https://pubmed.ncbi.nlm.nih.gov/41372416/
- Groves AR et al. 2011, NeuroImage (linked ICA). doi:10.1016/j.neuroimage.2011.03.034
- Guo J et al. 2022, Biol Psychiatry (MR imaging). doi:10.1016/j.biopsych.2022.08.024
- Xiao Y et al. 2025, Psychiatry Clin Neurosci (MR connectome). doi:10.1111/pcn.13897. https://pmc.ncbi.nlm.nih.gov/articles/PMC11875323/
- Arnatkeviciute A, Fulcher BD, Fornito A 2019, NeuroImage. doi:10.1016/j.neuroimage.2019.01.011
- Fornito A et al. 2023, Biol Psychiatry (imaging transcriptomics best practices). doi:10.1016/j.biopsych.2022.10.016

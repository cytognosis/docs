# Noninvasive Molecular Measurement in the Human Brain: MRS, PET, SPECT, and Emerging Modalities

Technology deep-dive for the Cytognosis Foundation NSF X-Labs / ARPA-H work. Compiled 25 May 2026.

## Scope and how this extends the seed work

The companion document `targeted-noninvasive-scanning.md` covers the optical path to molecular brain readouts (fNIRS, SWIR, SORS/SESORS, photoacoustic, Raman) and concludes, honestly, that outside hemoglobin and cytochrome-c-oxidase no specific molecule is measured transcranially in the human brain by purely optical means today. This document covers the established and emerging non-optical and hybrid methods that DO measure specific molecules in the living human brain: magnetic resonance spectroscopy (MRS), positron emission tomography (PET), single-photon emission computed tomography (SPECT), and a set of emerging techniques (hyperpolarized 13C MRI, deuterium metabolic imaging, CEST, photoacoustic, transcranial Raman/SORS/SESORS, functional ultrasound, magnetic particle imaging). The companion document `molecular-cellular-biotypes.md` defines which molecules matter: amyloid-beta, tau, alpha-synuclein, presynaptic dopamine and the dopamine transporter, synaptic density (SV2A), neuroinflammation (TSPO), and the MRS-visible metabolites NAA, glutamate/Glx, GABA, glutathione, lactate, and myo-inositol.

The two questions this document is organized around are the two the program keeps returning to. First, what is the lowest molecular concentration each modality can detect, and at what spatial resolution? Second, can a modality zoom into one region at higher resolution (targeted/focused), or is it inherently whole-brain? A dedicated final section addresses the hardest version of the first question: the gap between voxel resolution (millimeters) and the size of the protein aggregates that drive neurodegeneration (nanometers to microns), and what that gap means for early detection of the small, soluble, most toxic species.

A note on units that recurs throughout. MRS detects molecules at millimolar (mM, 10^-3 mol/L) concentrations. PET detects tracers at picomolar to nanomolar (10^-12 to 10^-9 mol/L) concentrations. That is a difference of roughly nine orders of magnitude in sensitivity, and it is the single most important fact in molecular brain imaging. MRS sees the abundant metabolites; PET sees the scarce receptors and pathological deposits. No emerging technology has closed this gap without either a radiotracer or hyperpolarization.

---

## 1. Magnetic Resonance Spectroscopy (MRS)

### 1.1 What it measures and how

MRS exploits the same nuclear magnetic resonance physics as MRI but resolves the chemical-shift spectrum rather than forming an anatomical image. Different molecules containing the observed nucleus resonate at slightly different frequencies because of their local electronic environment, producing a spectrum whose peaks identify metabolites and whose peak areas scale with concentration. Proton (1H) MRS is the workhorse; phosphorus (31P) and carbon (13C) MRS access energy metabolism and the TCA cycle. MRS is label-free: it reports endogenous molecules with no injected probe and no ionizing radiation.

The fundamental constraint is sensitivity. MRS can only see molecules present at roughly 1 mM or higher in a voxel measured in seconds to minutes. Below that the signal disappears into noise. This restricts MRS to abundant metabolites and excludes receptors, transporters, and pathological aggregates, which sit at nanomolar to micromolar levels (1, 2).

### 1.2 Proton (1H) MRS: NAA, Glx, GABA, glutathione, lactate, myo-inositol

The 1H spectrum from brain contains N-acetylaspartate (NAA, a neuronal-mitochondrial integrity marker, roughly 8 to 12 mM), total creatine (PCr + Cr, often used as an internal reference), choline-containing compounds, myo-inositol (a glial/osmolyte marker), glutamate and glutamine (Glx, roughly 6 to 12 mM combined), GABA (roughly 1 mM, the lowest routinely measured), glutathione (GSH, roughly 1 to 3 mM), and lactate (normally low, rising in hypoxia and mitochondrial dysfunction). GABA and GSH overlap with stronger neighbors and require spectral editing sequences (MEGA-PRESS) or ultra-high field to resolve (1, 3).

Two acquisition modes define the targeted-vs-whole-brain answer for MRS. Single-voxel spectroscopy (SVS) places one cubic voxel, typically 8 cm^3 (2 x 2 x 2 cm) at 3T down to roughly 1 to 3.4 cm^3 at 7T, on a chosen region and delivers the highest-quality spectrum from that region. This is the most focused molecular measurement available in the human brain: the operator can target anterior cingulate, hippocampus, or occipital cortex specifically. Magnetic resonance spectroscopic imaging (MRSI, or chemical-shift imaging) acquires a grid of spectra across a slice or volume, trading per-voxel quality for spatial coverage, with nominal MRSI voxels of roughly 1 cm^3 but effective resolution degraded by point-spread blurring. So MRS is the rare modality that is natively both: SVS for one region at best quality, MRSI for maps at lower per-voxel quality (1).

### 1.3 7T and ultra-high-field MRS

At 7T, chemical shift dispersion increases linearly with field and signal-to-noise super-linearly, so peaks that overlap at 3T separate. Glutamate resolves cleanly from glutamine, and GABA and GSH become measurable with better precision. A 2024 review of metabolite-selective MRS precision reported maximal Cramer-Rao lower bounds at 7T of roughly 2.0% for glutamate, 8.0% for glutathione, and 14.0% for GABA, with reliable single-voxel quantification of all three from posterior cingulate and precuneus (3, 4). The 7T cost is the same as the 7T benefit's limit: voxels remain on the order of 1 to 8 cm^3 because even at 7T the detection floor stays near 1 mM. Ultra-high field improves which metabolites are resolvable and the precision of their quantification; it does not move MRS into the nanomolar regime where receptors and aggregates live (3, 5).

Subcortical and brainstem MRS remains hard. Feasibility studies at 3T and 7T report glutamate and GABA detection in pons (voxel roughly 10.5 x 12.5 x 22 mm^3) and thalamus (16 x 12 x 16 mm^3), but B0/B1 inhomogeneity and motion degrade deep-region spectra relative to cortex (6).

### 1.4 31P and 13C MRS

31P MRS measures phosphocreatine (PCr), ATP, inorganic phosphate (Pi), phosphomonoesters and phosphodiesters (membrane turnover), NAD+ and NADH, and intracellular pH and Mg2+. It directly reports mitochondrial energy state, which ties to the oxidative-stress/mitochondrial biotype in the seed work. Concentrations are low: ATP near 3 mM, PCr near 3 to 5 mM, and total NAD in the sub-millimolar range, so 31P MRS uses large voxels and long acquisitions. 7T 31P MRSI has mapped intracellular NAD content across the whole brain, and 2025 functional 31P work resolved NAD dynamics during visual stimulation, but spatial resolution is coarse (several cm^3 voxels) (7, 8, 9).

13C MRS at natural abundance is extremely insensitive (13C is roughly 1.1% of carbon) and historically required infused 13C-labeled substrates (glucose, acetate) to trace the TCA cycle and glutamate/glutamine cycling over tens of minutes. This is powerful for metabolic flux but slow, low-resolution, and demanding. Hyperpolarized 13C (Section 7.1) and deuterium metabolic imaging (Section 7.2) are the modern routes around 13C insensitivity.

### 1.5 MRS in neurodegenerative and psychiatric disease

In Alzheimer's, decreased NAA (neuronal loss) and increased myo-inositol (gliosis) are the most consistent MRS findings, with the NAA/myo-inositol ratio tracking progression. In Parkinson's, MRS findings are more variable; reduced NAA in basal ganglia and elevated lactate in some cohorts. In the psychiatric disorders central to this proposal: elevated anterior cingulate glutamate/glutamine in early and treatment-resistant schizophrenia, reduced cortical GABA in major depression, and reduced anterior cingulate glutathione (or increased variance) in schizophrenia subsets, all as documented in `molecular-cellular-biotypes.md`. Lactate elevation flags mitochondrial bottlenecks across disorders. The honest summary is that MRS metabolites are sensitive but not specific: they report tissue state (neuronal integrity, E/I balance, redox, energy) rather than disease-defining pathology.

### Table 1.1: MRS at a glance

| Parameter | 1H SVS (3T) | 1H SVS (7T) | 1H MRSI | 31P MRSI | 13C MRS (infused) |
|---|---|---|---|---|---|
| Typical voxel | 8 cm^3 (2x2x2 cm) | 1 to 3.4 cm^3 | ~1 cm^3 nominal | several cm^3 | large/whole-slab |
| Best voxel | ~3.4 cm^3 | ~1 cm^3 | sub-cm^3 (degraded by PSF) | ~5 to 8 cm^3 | coarse |
| Temporal resolution | minutes (3 to 10 min) | minutes | 5 to 20 min | 5 to 30 min | 30+ min (flux) |
| Targeted vs whole-brain | Targeted (one region) | Targeted | Whole-slice/volume map | Map (coarse) | Coarse/regional |
| Detection limit | ~1 mM | ~1 mM (better precision) | ~1 to 2 mM | ~1 mM | depends on label |
| Molecules | NAA, Glx, Cr, Cho, mI, GABA (edited), GSH (edited), lactate | + resolved Glu/Gln, GABA, GSH | metabolite maps | PCr, ATP, Pi, NAD, pH | TCA flux, Glu/Gln cycling |
| Radiation | None | None | None | None | None |
| Key limits | low sensitivity (mM floor), overlap | cost, availability, deep regions | per-voxel SNR, PSF blur | low SNR, coarse | slow, expensive, insensitive |

---

## 2. Positron Emission Tomography (PET)

### 2.1 What it measures and the sensitivity advantage

PET injects a tracer carrying a positron-emitting isotope (18F half-life 110 min, 11C half-life 20 min, 68Ga). Positron-electron annihilation produces coincident 511 keV photon pairs detected in a ring. Because detection is essentially background-free (the body emits no 511 keV coincidences before injection), PET reaches picomolar to nanomolar tracer concentrations, roughly nine orders of magnitude below the MRS floor (10). This is why PET, not MRS, is the reference standard for receptors, transporters, and pathological aggregates: those targets exist at exactly the concentrations PET can see and MRS cannot.

Molecular specificity comes entirely from the tracer chemistry, not the scanner. The scanner reports where the radiolabel is; whether that location means "amyloid plaque" or "dopamine transporter" depends on what molecule the chemists attached the isotope to.

### 2.2 Spatial resolution and the physics floor

Clinical whole-body PET resolves roughly 4 to 6 mm. The fundamental limits are positron range (the distance the positron travels before annihilating, isotope-dependent, smallest for 18F) and photon non-collinearity (annihilation photons depart slightly off 180 degrees). These set a practical floor near 1 to 2 mm even for ideal detectors (11).

The 2024 NeuroEXPLORER, a dedicated brain PET/CT from Yale, UC Davis, and United Imaging, pushes close to that floor: radial/tangential resolution of 1.64 to 2.51 mm FWHM across the field, with roughly 10-fold higher sensitivity (11.8% at center) and over twice the spatial resolution of the previous best brain scanner (the HRRT). Higher sensitivity matters as much as resolution: it allows lower injected dose, shorter scans, or detection of lower-density targets (11, 12). Even so, PET resolution remains millimeter-scale, orders of magnitude coarser than the nanometer-to-micron scale of individual protein aggregates (Section 9).

### 2.3 Targeted vs whole-brain

PET is acquired as a whole-brain (or whole-body) 3D volume; the scanner does not "zoom" optically. Regional focus comes from analysis: standardized uptake value ratios (SUVR) and dynamic kinetic modeling are computed in anatomically defined regions of interest (entorhinal cortex, striatum, substantia nigra). So PET is whole-brain in acquisition, region-targeted in analysis. A focal high-resolution insert or a dedicated brain scanner like NeuroEXPLORER improves resolution everywhere in the field, not selectively in one region.

### 2.4 PET in neurodegenerative disease (the tracer families)

**Glucose metabolism.** 18F-FDG reports regional glucose use; hypometabolism patterns distinguish Alzheimer's, frontotemporal dementia, and dementia with Lewy bodies.

**Amyloid.** 11C-PiB was the first widely used amyloid tracer (2004) and revealed in vivo amyloid decades before symptoms. The 18F agents florbetapir (Amyvid, FDA 2012), florbetaben (Neuraceq), and flutemetamol (Vizamyl) are clinically approved. Amyloid PET now gates anti-amyloid antibody therapy: lecanemab (FDA 2023) and donanemab (FDA 2024) require amyloid-PET (or CSF) confirmation, and amyloid PET, expressed in Centiloid units, is used to define treatment thresholds and to confirm plaque clearance (13, 14). Crucially, these tracers bind dense fibrillar plaque, the aggregate burden in a voxel, not individual soluble oligomers (Section 9).

**Tau.** 18F-flortaucipir (Tauvid, FDA 2020) was the first approved tau tracer. Second-generation 18F tracers MK-6240 and PI-2620 offer improved signal and less off-target binding; flortaucipir and MK-6240 bind Alzheimer paired-helical-filament tau strongly but non-AD (3R or 4R) tauopathies weakly, and flortaucipir shows off-target neuromelanin and hemorrhage binding (15, 16). A 2024 study found the spatial extent of MK-6240 tau (how widespread) correlated with cognition better than peak SUVR (how intense), a notable shift toward distribution metrics (17).

**Dopaminergic.** 18F-DOPA PET measures presynaptic dopamine synthesis capacity (decreased in Parkinson's, increased in striatum in schizophrenia, the d~0.8 finding in the seed work). 11C-raclopride measures D2 receptor availability and displacement. These are the molecular complement to DAT-SPECT (Section 3).

**Synaptic density.** SV2A tracers image presynaptic terminals. 11C-UCB-J was first; 18F-SynVesT-1 and -2 are fluorinated analogs with higher binding potential and 18F's longer half-life. 2024-2025 work in aging and Alzheimer's shows SV2A loss correlating negatively with tau and amyloid burden, and SV2A PET is being applied in multiple sclerosis and stroke (18, 19, 20). Synaptic density is arguably the most direct in vivo readout of the synaptic injury that precedes neuronal death.

**Neuroinflammation.** TSPO (translocator protein) tracers image activated microglia/astrocytes. Second-generation tracers (11C-DPA-713, 18F-DPA-714, 18F-GE-180, 18F-FEPPA) improved brain uptake but suffer a major limitation: binding depends on the rs6971 TSPO genotype (high/mixed/low affinity binders), confounding quantification. Third-generation tracers aiming to remove genotype dependence are in development (21, 22).

**Alpha-synuclein.** The hardest target, and the most active 2023-2026 frontier. Alpha-synuclein aggregates sit at lower density than amyloid and tau and are often intracellular, demanding higher-affinity tracers. The first-in-class 18F-ACI-12589 (AC Immune) was the first to visualize alpha-synuclein pathology in living human brain (Nature Communications 2023), clearly distinguishing multiple system atrophy (strong cerebellar white-matter and middle-cerebellar-peduncle binding) from controls and other neurodegeneration, but with limited binding in Parkinson's disease itself, where aggregate density is lower (23, 24, 25). The optimized follow-up candidate 18F-ACI-15916 targets improved sensitivity for the lower-burden Parkinson's and Lewy-body settings (24). As of 2026 there is no clinically approved alpha-synuclein tracer with reliable Parkinson's sensitivity; this is the clearest example of the burden-vs-resolution problem in Section 9.

### 2.5 Limitations

Ionizing radiation (a brain PET delivers roughly 5 to 10 mSv depending on tracer, limiting repeat scans), tracer cost and availability (11C requires an on-site cyclotron given its 20-min half-life; even 18F needs a regional radiopharmacy), scanner cost and scarcity, blood-brain-barrier permeability requirements for every candidate tracer, off-target binding, and a regulatory path that is effectively a new IND per tracer. PET is the gold standard for molecular specificity and sensitivity but is the opposite of a continuous, population-scale, wearable monitor.

### Table 2.1: PET at a glance

| Parameter | Clinical PET | NeuroEXPLORER (dedicated brain) |
|---|---|---|
| Typical resolution | 4 to 6 mm FWHM | 1.6 to 2.5 mm FWHM |
| Physics floor | ~1 to 2 mm (positron range, non-collinearity) | approaching floor |
| Temporal resolution | seconds to minutes per frame (dynamic); static scans 10 to 30 min | similar, higher sensitivity allows shorter frames |
| Targeted vs whole-brain | Whole-brain acquisition, region-targeted analysis | same |
| Detection limit (concentration) | picomolar to nanomolar tracer | picomolar to nanomolar, ~10x more sensitive |
| Molecules | FDG, amyloid, tau, DOPA, D2, SV2A, TSPO, alpha-synuclein | same tracers, better images |
| Radiation | ~5 to 10 mSv | lower dose possible due to sensitivity |
| Key limits | radiation, cost, cyclotron/radiopharmacy, BBB, off-target | cost, scarcity, still mm resolution |

---

## 3. Single-Photon Emission Computed Tomography (SPECT)

### 3.1 What it measures

SPECT uses single-photon emitters (123I half-life 13 h, 99mTc half-life 6 h) and a rotating gamma camera with collimators. Because collimators reject most photons to define direction, SPECT is roughly one to two orders of magnitude less sensitive than PET and has coarser resolution, typically 8 to 12 mm for brain SPECT (versus 4 to 6 mm clinical PET). It detects nanomolar to low-micromolar tracer concentrations, below PET but far above MRS. Its advantages are isotope logistics (123I and 99mTc do not need an on-site cyclotron) and lower cost.

### 3.2 The dominant clinical application: DAT-SPECT (DaTscan)

123I-ioflupane (DaTscan, FP-CIT) binds the presynaptic dopamine transporter (DAT) in the striatum. Loss of striatal DAT signal (reduced putamen uptake, "comma to dot" pattern) supports nigrostriatal degeneration and distinguishes Parkinson's and related parkinsonian syndromes from essential tremor, drug-induced parkinsonism, and psychogenic tremor. A 2024 systematic review confirmed DaTscan's role in clinically uncertain parkinsonism, and CZT (cadmium-zinc-telluride) detector cameras with deep-learning reconstruction are halving scan times while preserving image quality (26, 27). DAT-SPECT is the most widely used molecular dopaminergic imaging worldwide because it is cheaper and more available than 18F-DOPA PET, even though PET offers better resolution and quantification. 99mTc-TRODAT-1 is an alternative DAT tracer in some regions. SPECT perfusion agents (99mTc-HMPAO, 99mTc-ECD) and 123I-IMP map regional cerebral blood flow in dementia and epilepsy.

### Table 3.1: SPECT at a glance

| Parameter | Brain SPECT |
|---|---|
| Typical resolution | 8 to 12 mm |
| Best resolution | ~6 to 8 mm (CZT, dedicated brain) |
| Temporal resolution | minutes (static); CZT + DL reduces scan time |
| Targeted vs whole-brain | Whole-brain acquisition, region-targeted analysis (striatum for DAT) |
| Detection limit | nanomolar to low-micromolar tracer (below PET, above MRS) |
| Molecules | DAT (ioflupane), perfusion (HMPAO/ECD), receptors |
| Radiation | ~3 to 7 mSv (plus thyroid blockade for 123I) |
| Key limits | lower resolution and sensitivity than PET; collimator inefficiency |

---

## 4. Emerging: Hyperpolarized 13C MRI

Dissolution dynamic nuclear polarization transiently boosts 13C signal by four to five orders of magnitude, making real-time metabolic imaging of an injected 13C substrate possible. Hyperpolarized [1-13C]pyruvate is the dominant agent: after IV injection it is converted to lactate, bicarbonate, and alanine, and the rate of pyruvate-to-lactate conversion reports metabolic state (Warburg-like glycolysis in tumors, altered redox in disease). It has translated to human studies at roughly 15 centers, with a 2024 UCSF consensus meeting and 2024-2025 methods and consensus papers standardizing acquisition (28, 29, 30).

The constraints are severe. The hyperpolarized signal decays with the T1 (roughly 30 to 60 s), so the entire experiment, from injection to imaging, must complete in under about two minutes, fixing temporal resolution at the few-second-per-frame scale and limiting total observation. Spatial resolution is coarse: recent human brain studies used roughly 7.5 x 7.5 mm^2 for pyruvate and 15 x 15 mm^2 for downstream lactate and bicarbonate (30, 31). It requires a polarizer, a sterile injectable, and multinuclear MRI hardware. It measures metabolic flux (a rate), not a static concentration, and is label-dependent (it sees only the injected 13C molecule and its products), so it does not image receptors or aggregates. It is whole-brain/regional, not selectively focusable.

### Table 4.1: Hyperpolarized 13C MRI

| Parameter | Value |
|---|---|
| Typical resolution | 7.5 to 15 mm (pyruvate vs products) |
| Temporal resolution | seconds per frame; total window < ~2 min (T1 decay) |
| Targeted vs whole-brain | Regional/whole-brain volume, not selectively focusable |
| Detection | flux of injected 13C substrate (effective sensitivity boosted 10^4 to 10^5) |
| Molecules | pyruvate to lactate/bicarbonate/alanine (metabolic rate) |
| Radiation | None (13C is stable) |
| Key limits | < 2 min window, coarse resolution, polarizer + injectable + multinuclear MRI |

---

## 5. Emerging: Deuterium Metabolic Imaging (DMI)

DMI administers oral or IV 2H-labeled glucose (typically [6,6'-2H2]glucose) and maps deuterium signal as glucose is taken up and converted to Glx (glutamate+glutamine) and lactate, giving a noninvasive, non-radioactive map of glucose uptake and downstream metabolism, conceptually an FDG-PET analog without radiation. It is an active 2024-2025 area at 7T. Balanced steady-state free precession (bSSFP) and concentric-ring-trajectory readouts have raised SNR roughly threefold and doubled achievable spatial resolution, and indirect 1H detection (QELT) at clinical 3T reproduces 7T 2H concentration estimates without extra hardware, suggesting a path to wider clinical use (32, 33, 34). Resolution remains coarse (several cm^3 voxels) and temporal resolution is minutes, with metabolite concentrations in the low-mM range. Like hyperpolarized 13C it is label-dependent metabolic mapping, not receptor or aggregate imaging, and is regional rather than selectively focusable.

### Table 5.1: Deuterium metabolic imaging

| Parameter | Value |
|---|---|
| Typical resolution | several cm^3 voxels; ~2x improvement with bSSFP-CRT |
| Temporal resolution | minutes (dynamic uptake over tens of minutes) |
| Targeted vs whole-brain | Whole-brain/regional map |
| Detection | low-mM labeled metabolites |
| Molecules | 2H-glucose to Glx and lactate (glucose metabolism) |
| Radiation | None (2H stable, minimally toxic) |
| Key limits | coarse resolution, minutes temporal, needs labeled glucose; 7T preferred (3T indirect emerging) |

---

## 6. Emerging: Chemical Exchange Saturation Transfer (CEST)

CEST indirectly amplifies the signal of low-concentration molecules with exchangeable protons by saturating those protons and watching the saturation transfer to the abundant water pool, multiplying sensitivity. GluCEST images glutamate (asymmetry near 3 ppm) at higher spatial resolution and sensitivity than 1H MRS, and is one of the only ways to map glutamate's spatial distribution in human brain noninvasively at 7T; it has been applied to nicotine dependence and other clinical populations, with 2025 work building calibrated quantitative multi-pool models (35, 36). Amide proton transfer (APT) CEST images mobile protein/peptide content and pH (used in tumor and stroke). CEST's advantages are MRI-grade spatial resolution (roughly 1 to 3 mm in-plane, far better than MRS voxels) with sensitivity to mM and even sub-mM exchangeable-proton pools. Its limits are specificity (overlapping CEST pools, confounds from pH, temperature, B0/B1 inhomogeneity), heavy dependence on 7T for clean glutamate contrast, and the fact that it still targets relatively abundant molecules, not nanomolar receptors or aggregates. It is acquired as a map (whole-slice/volume) at MRI resolution.

### Table 6.1: CEST

| Parameter | GluCEST (7T) | APT-CEST |
|---|---|---|
| Typical resolution | ~1 to 3 mm in-plane (MRI-grade) | ~1 to 3 mm |
| Temporal resolution | minutes | minutes |
| Targeted vs whole-brain | Map (slice/volume) | Map |
| Detection | mM to sub-mM (sensitivity-amplified) | mobile protein/peptide pool, pH |
| Molecules | glutamate (distribution) | amide protons (protein, pH) |
| Radiation | None | None |
| Key limits | specificity, 7T-dependent, B0/B1 confounds | specificity, pH/temperature confounds |

---

## 7. Emerging: Photoacoustic Imaging

Photoacoustic (optoacoustic) imaging illuminates tissue with pulsed light; absorbed energy creates thermoelastic ultrasound waves detected acoustically, so resolution follows ultrasound rather than diffuse-optical limits. As detailed in `targeted-noninvasive-scanning.md`, the leading clinical platform (MSOT) reaches roughly 10 to 30 mm depth, and the first in-human transcranial functional photoacoustic computed tomography (Wang lab, 2022) recovered functional signals through a hemicraniectomy patient's skull-intact hemisphere with skull-induced aberration. In Alzheimer's mouse models, volumetric optoacoustic tomography detects amyloid and tau with targeted probes at roughly 110 micrometer resolution, and label-free polarization-sensitive approaches exploit the optical anisotropy of cross-beta-sheet aggregates. Endogenous contrast (hemoglobin, melanin/neuromelanin, lipid, water) is the near-term human story; molecular aggregate imaging requires either probes (reintroducing BBB and biodistribution problems) or unproven label-free contrast. Through-skull human molecular protein imaging by photoacoustics has not been demonstrated. Photoacoustics can be focused (it images a defined field/region) and offers good resolution at shallow depth, but depth and transcranial molecular specificity are the unsolved problems.

### Table 7.1: Photoacoustic imaging

| Parameter | Value |
|---|---|
| Typical resolution | ~100 micrometer to sub-mm at shallow depth; degraded transcranially |
| Depth | ~10 to 30 mm (handheld MSOT); transcranial human only proof-of-concept |
| Temporal resolution | real-time to seconds (functional) |
| Targeted vs whole-brain | Focal/regional field of view |
| Detection | endogenous chromophores (Hb, melanin, lipid, water); molecular only with probes |
| Molecules (human, noninvasive) | hemoglobin, oxygenation; aggregates NOT demonstrated transcranially |
| Radiation | None |
| Key limits | skull aberration/absorption, depth, no transcranial human molecular imaging |

---

## 8. Emerging: Transcranial Raman / SORS / SESORS

Raman spectroscopy reads molecule-specific vibrational fingerprints label-free, including the cross-beta-sheet amide bands that distinguish misfolded aggregates from native protein. The cross section is tiny (roughly 10 orders of magnitude below fluorescence), so deep transcranial detection is the challenge. Spatially offset Raman spectroscopy (SORS) collects scattered light at a lateral offset to recover subsurface signal, pushing depth from millimeters toward centimeters in turbid media. Surface-enhanced Raman (SERS) boosts signal 10^6 to 10^10 with metal nanostructures; combined as SESORS it has detected neurotransmitters at roughly 100 micromolar through cat skull in tissue mimics and glioblastoma through intact mouse skull with targeted nanotags, with 2023-2024 frameworks improving in vivo sampling. The decisive caveat, as the seed work states, is that SERS/SESORS requires nanoparticle delivery to the target, reintroducing the BBB and biodistribution problems a probe-free approach was meant to avoid. No human transcranial SESORS measurement of amyloid, tau, or alpha-synuclein has been reported. SORS can in principle be spatially offset to interrogate a chosen subsurface region (focusable in depth), but spatial resolution is poor (centimeter-scale) and molecular specificity transcranially in humans is unproven.

### Table 8.1: Transcranial Raman / SORS / SESORS

| Parameter | SORS | SESORS |
|---|---|---|
| Typical resolution | cm-scale (poor) | cm-scale |
| Depth | mm to ~cm (up to ~5 cm in mimics) | through-skull (animal) |
| Temporal resolution | seconds to minutes | seconds (with nanotags, animal) |
| Targeted vs whole-brain | depth-offset interrogation of a region | regional |
| Detection | label-free vibrational (weak) | ~100 micromolar (enhanced) |
| Molecules (human) | bone/tissue composition; brain aggregates NOT shown | requires injected nanotags; no human brain aggregate |
| Radiation | None | None |
| Key limits | tiny cross section, depth, poor resolution | requires nanoparticle delivery (BBB), no human brain demo |

---

## 9. Emerging: Functional Ultrasound (fUS)

Functional ultrasound images cerebral blood volume changes (a hemodynamic proxy for neural activity) via ultrafast plane-wave Doppler, with high sensitivity to small-vessel flow. It is fundamentally a hemodynamic, not a molecular, modality, but it is included because of its rapid 2024-2025 progress and relevance to functional sensing. Through an acoustically transparent cranial window it reaches roughly 100 to 200 micrometer spatial and roughly 100 ms temporal resolution over centimeters of depth, far better than fMRI resolution, and a 2024 Science Translational Medicine study demonstrated human-brain fUS through such a window. Fully transcranial human fUS (intact skull) remains the barrier; 2024-2025 work uses microbubble contrast and multi-array probes for transcranial whole-brain fUS and ultrasound localization microscopy, and 2025 acoustic-transparency approaches target imaging through intact skull. For molecular work, fUS contributes the vascular/hemodynamic axis, not aggregate or receptor detection.

### Table 9.1: Functional ultrasound

| Parameter | Value |
|---|---|
| Typical resolution | ~100 to 200 micrometer (through cranial window) |
| Temporal resolution | ~100 ms |
| Targeted vs whole-brain | Focal field of view (steerable); whole-brain emerging with multi-array |
| Detection | cerebral blood volume (hemodynamic), not molecular |
| Molecules | none directly (vascular proxy) |
| Radiation | None |
| Key limits | transcranial through intact skull unsolved; hemodynamic not molecular |

---

## 10. Emerging: Magnetic Particle Imaging (MPI)

MPI directly images the nonlinear magnetization of injected superparamagnetic iron oxide nanoparticle (SPION) tracers using a field-free region scanned through the body. The signal is background-free (no native SPION signal in the body before injection), giving high sensitivity, and is quantitative (signal scales linearly with tracer mass). A human-scale brain MPI system from the Martinos Center achieves roughly 6 mm spatial resolution at 5 s temporal resolution with a detection limit near 150 ng Fe (SNR = 1), and a 2024 head-sized scanner reaches 3D imaging at 4 Hz within peripheral-nerve-stimulation safety limits using a clinically approved tracer. Estimates suggest a first-generation human MPI brain scanner could offer roughly tenfold higher sensitivity than fMRI contrast detection at similar spatial resolution (37, 38, 39). The molecular caveat is decisive: MPI sees only the SPION tracer, so its molecular specificity depends entirely on functionalizing nanoparticles to bind a target and getting them across the BBB. Today it is used for blood-pool/perfusion and stroke; targeted molecular brain MPI is the same probe-delivery problem that constrains optical and SESORS approaches. MPI is whole-field-of-view, not selectively focusable, though the field-free region defines a localized sensitive zone.

### Table 10.1: Magnetic particle imaging

| Parameter | Value |
|---|---|
| Typical resolution | ~6 mm (human-scale brain) |
| Temporal resolution | 5 s (current); 4 Hz (newer head-sized) |
| Targeted vs whole-brain | Whole-field; field-free-region localization |
| Detection | ~150 ng Fe (SNR=1); background-free, quantitative |
| Molecules | SPION tracer only (perfusion/blood pool today) |
| Radiation | None |
| Key limits | needs injected SPIONs; targeted molecular binding + BBB unsolved |

---

## 11. Protein aggregates and the resolution problem

This is the core scientific question. Neurodegeneration is driven by misfolded protein aggregates, and the most toxic, earliest species are the smallest and most soluble. The technologies above either detect the late, large, abundant deposits (PET, by burden) or cannot reach the target noninvasively at all. Here are the aggregates, their sizes, how burden changes with stage, and the resolution-and-sensitivity gap.

### 11.1 The major aggregates and their sizes

**Amyloid-beta (Alzheimer's).** Monomer ~4 kDa, a few nm. Soluble oligomers (dimers to dodecamers, including ~5 nm ADDLs) are spherical, roughly 3 to 10 nm, and are the most synaptotoxic species; toxicity is inversely related to size (smaller oligomers are more potent) (40, 41). Protofibrils are rod-like, ~3.1 nm diameter and 60 to 400 nm long. Mature fibrils assemble into plaques tens to hundreds of microns across (dense-core plaques commonly 10 to 50 micrometer, diffuse plaques larger) (42).

**Tau (Alzheimer's, FTD).** Monomer is intrinsically disordered. Pathological oligomers and small fibrils are sub-250 nm; paired helical filaments have a regular width averaging ~15 nm; these bundle into neurofibrillary tangles filling neuronal somata, on the order of tens of microns. 2024 super-resolution work characterized nanoscale tau aggregate hyperphosphorylation below 250 nm, the seeds that precede large tangles (43, 44).

**Alpha-synuclein (Parkinson's, DLB, MSA).** Monomer ~14 kDa. Oligomers nm-scale; fibrils are two-protofilament structures resolved to ~2 angstrom by 2024 cryo-EM, microns long; they accumulate in Lewy bodies (~5 to 25 micrometer in neurons) and in MSA in glial cytoplasmic inclusions (45, 46).

**Mutant huntingtin (Huntington's).** Polyglutamine-expansion aggregates form intranuclear and cytoplasmic inclusions; oligomers nm-scale, inclusions up to micron-scale.

**TDP-43 (ALS, FTD).** Cytoplasmic phosphorylated inclusions; oligomers and aggregates nm to micron-scale. No clinically validated TDP-43 PET tracer exists as of 2026, a major gap.

**Prion (PrP-Sc).** Misfolded prion protein forms oligomers and amyloid fibrils nm to micron-scale; imaged today mainly indirectly (MRI diffusion, FDG).

### 11.2 How burden changes across disease stage

The disease course runs preclinical to prodromal to clinical. In the preclinical stage the dominant species are soluble monomers and small oligomers at low total burden, biologically the most important because oligomers drive synaptic injury and seed further aggregation (40). As disease advances, aggregates grow and accumulate: protofibrils and fibrils form, plaques and tangles deposit, and total aggregate mass per unit tissue rises by orders of magnitude into the clinical stage. So the pathology that matters earliest (small soluble oligomers) is exactly the pathology that is least abundant and smallest, while the pathology imaging detects best (large fibrillar burden) appears late. Amyloid burden in particular tends to plateau relatively early in the clinical course even as tau and neurodegeneration continue, which is why tau extent and synaptic-density loss track cognition better than amyloid load at later stages (17, 18).

### 11.3 Why PET detects burden, not individual aggregates

A PET voxel is roughly 2 to 6 mm on a side, that is, 8 to 200+ mm^3 of tissue containing billions of cells. An individual amyloid plaque is ~10 to 50 micrometer; a neurofibrillary tangle is tens of microns; a soluble oligomer is ~5 nm. PET cannot resolve a single aggregate; the gap between voxel size (mm) and aggregate size (nm to micron) is three to six orders of magnitude. What PET actually measures is the aggregate-bound tracer concentration averaged over the voxel, that is, the burden or load of fibrillar target in that volume. The signal rises when enough high-affinity binding sites (dense fibrillar plaque or PHF-tau) exist per voxel to lift tracer concentration above the detection floor. This is why amyloid and tau PET report regional burden maps, not aggregate counts, and why they require a substantial fibrillar load to turn positive.

It is also why the small soluble oligomers, the earliest and most toxic species, are the hardest to image. They present few stable high-affinity binding sites, exist at low concentration, and are dispersed rather than concentrated, so they do not raise voxel-averaged tracer concentration enough to detect. Current amyloid and tau tracers were selected for fibrillar (cross-beta) binding precisely because that is the abundant, high-density target; they largely miss oligomers. Alpha-synuclein illustrates the burden problem at its starkest: 18F-ACI-12589 detects MSA (very high aggregate density in glial inclusions) but largely misses Parkinson's disease (lower-density neuronal aggregates), because the per-voxel binding-site concentration in PD falls near or below the detection floor (23, 24).

### 11.4 What spatial resolution and sensitivity would early oligomer detection require

To image individual oligomers you would need spatial resolution near their physical size (~5 to 10 nm), six orders of magnitude finer than a PET voxel, which is the domain of electron microscopy and single-molecule super-resolution, not any in vivo human modality. That is not the realistic target. The realistic target is detecting low-concentration, dispersed soluble oligomer burden, which requires two things: an oligomer-selective probe (a tracer that binds soluble oligomeric conformations, not just fibrillar cross-beta), and sensitivity sufficient to detect that probe at the very low concentrations oligomers present, likely sub-nanomolar to picomolar bound concentration. PET's intrinsic sensitivity (picomolar) is in principle adequate; the binding chemistry is the bottleneck. Oligomer-selective PET tracers are an active development area but none is clinically validated as of 2026. CSF and plasma assays (p-tau217, Abeta42/40, alpha-synuclein seed amplification) currently outperform imaging for the earliest, soluble, dispersed pathology because fluid biomarkers integrate over the whole brain and do not face the per-voxel concentration threshold; they sacrifice spatial localization for sensitivity to diffuse low-burden disease.

### 11.5 Honest statement of what is and is not detectable noninvasively today

Detectable today noninvasively in human brain:
- Fibrillar amyloid-beta burden (amyloid PET, clinically validated, gates anti-amyloid therapy).
- Paired-helical-filament tau burden in Alzheimer's (tau PET, clinically validated; weaker in non-AD tauopathies).
- Alpha-synuclein burden in MSA (18F-ACI-12589, research; not yet in Parkinson's).
- Presynaptic dopamine synthesis (18F-DOPA PET) and dopamine transporter (DAT-SPECT).
- Synaptic density (SV2A PET, research-to-early-clinical).
- Neuroinflammation/microglial burden (TSPO PET, genotype-confounded).
- Abundant metabolites at mM (MRS): NAA, Glx, GABA, GSH, lactate, myo-inositol; energy metabolites (31P); glucose flux (DMI); glutamate distribution (GluCEST).

Not detectable noninvasively today:
- Small soluble oligomers of any aggregate (the earliest, most toxic species).
- Alpha-synuclein in Parkinson's disease at reliable sensitivity.
- TDP-43 aggregates (no validated tracer).
- Any aggregate at the level of individual particles (a fundamental resolution gap, not just an engineering gap).
- Any specific aggregate transcranially by purely optical, Raman/SESORS, photoacoustic, or MPI means in humans (all are probe-limited, depth-limited, or both).

The frontier: oligomer-selective and conformation-selective PET tracers, higher-affinity alpha-synuclein and first-in-class TDP-43 tracers, higher-sensitivity dedicated brain PET (NeuroEXPLORER class) to lower the per-voxel detection floor, and the complementary fluid-biomarker route (seed amplification, p-tau217) that detects diffuse low-burden pathology earlier than imaging but without spatial localization. For Cytognosis's continuous-monitoring thesis, the realistic near-term molecular axes are the abundant-metabolite (MRS/CEST/DMI) and hemodynamic/metabolic readouts, with PET/SPECT remaining the reference standard for scarce aggregate and receptor targets that no noninvasive continuous method can yet reach.

---

## References

1. Öz G, Alger JR, Barker PB, et al. Clinical proton MR spectroscopy in central nervous system disorders. Radiology. 2014;270(3):658-679. doi:10.1148/radiol.13130531

2. de Graaf RA. In Vivo NMR Spectroscopy: Principles and Techniques. 3rd ed. Wiley; 2019.

3. Kanagasabai T, Palaniyappan L, Théberge J. Precision of metabolite-selective MRS measurements of glutamate, GABA and glutathione: a review of human brain studies. NMR Biomed. 2024;37(9):e5071. doi:10.1002/nbm.5071. https://analyticalsciencejournals.onlinelibrary.wiley.com/doi/10.1002/nbm.5071

4. Prinsen H, de Graaf RA, Mason GF, et al. Reproducibility of glutamate, glutathione, and GABA measurements in vivo by single-voxel STEAM MRS at 7-Tesla in healthy individuals. https://pmc.ncbi.nlm.nih.gov/articles/PMC7522573/

5. Terpstra M, Cheong I, Lyu T, et al. Test-retest reproducibility of neurochemical profiles with short-echo, single-voxel MRS at 3T and 7T. Magn Reson Med. 2016;76(4):1083-1091.

6. Feasibility of glutamate and GABA detection in pons and thalamus at 3T and 7T by proton MRS. Front Neurosci. 2020;14:559314. https://www.frontiersin.org/journals/neuroscience/articles/10.3389/fnins.2020.559314/full

7. Ren J, Sherry AD, Malloy CR. 31P-MRS of healthy human brain: ATP synthesis, metabolite concentrations, pH, and T1 relaxation times. NMR Biomed. 2015;28(11):1455-1462. https://pmc.ncbi.nlm.nih.gov/articles/PMC4772768/

8. Mapping intracellular NAD content in entire human brain using phosphorus-31 MR spectroscopic imaging at 7 Tesla. Front Neurosci. 2024;18:1389111. https://www.frontiersin.org/journals/neuroscience/articles/10.3389/fnins.2024.1389111/full

9. Ultra-high field 31P functional MRS reveals NAD+ dynamics in brain energy metabolism during visual stimulation. bioRxiv. 2025. https://www.biorxiv.org/content/10.1101/2025.11.02.686085v1.full

10. Phelps ME. PET: the merging of biology and imaging into molecular imaging. J Nucl Med. 2000;41(4):661-681.

11. Li H, Badawi RD, Cherry SR, et al. Performance characteristics of the NeuroEXPLORER, a next-generation human brain PET/CT imager. J Nucl Med. 2024. https://jnm.snmjournals.org/content/early/2024/06/13/jnumed.124.267767. See also: New Horizons in Brain PET Instrumentation. https://pmc.ncbi.nlm.nih.gov/articles/PMC10840690/

12. Quantitative accuracy assessment of the NeuroEXPLORER for diverse imaging applications. https://pmc.ncbi.nlm.nih.gov/articles/PMC11705792/

13. Expert opinion on Centiloid thresholds suitable for initiating anti-amyloid therapy: 2024 Alzheimer's Association Research Roundtable. https://pmc.ncbi.nlm.nih.gov/articles/PMC12183938/

14. Updated appropriate use criteria for amyloid and tau PET: Alzheimer's Association and SNMMI workgroup. J Nucl Med. 2025;66(Suppl 2):S5. https://jnm.snmjournals.org/content/66/Supplement_2/S5

15. Leuzy A, Smith R, Cullen NC, et al. A review of the flortaucipir literature for PET imaging of tau neurofibrillary tangles. Brain Commun. 2024;6(1):fcad305. doi:10.1093/braincomms/fcad305

16. Head-to-head comparison of [18F]-flortaucipir, [18F]-MK-6240 and [18F]-PI-2620 postmortem binding across neurodegenerative diseases. Acta Neuropathol. 2023. https://pmc.ncbi.nlm.nih.gov/articles/PMC10822013/

17. The spatial extent of tauopathy on [18F]MK-6240 tau PET shows stronger association with cognition than SUVR in Alzheimer's disease. Eur J Nucl Med Mol Imaging. 2024. doi:10.1007/s00259-024-06603-2. https://pmc.ncbi.nlm.nih.gov/articles/PMC11043108/

18. Imaging synaptic density in aging and Alzheimer disease with [18F]SynVesT-1. J Nucl Med. 2025;66(4):620. https://pmc.ncbi.nlm.nih.gov/articles/PMC11960604/

19. SV2A PET imaging in human neurodegenerative diseases. https://pmc.ncbi.nlm.nih.gov/articles/PMC11064927/

20. SV2A PET reveals synaptic density loss in experimental autoimmune encephalomyelitis and in a pilot multiple sclerosis study. PNAS. https://www.pnas.org/doi/10.1073/pnas.2517709123

21. Emerging TSPO-PET radiotracers for imaging neuroinflammation: a critical analysis. 2024. https://pubmed.ncbi.nlm.nih.gov/39477764/

22. Recent progress in the development of TSPO PET ligands for neuroinflammation imaging. https://pmc.ncbi.nlm.nih.gov/articles/PMC5721086/

23. Smith R, Capotosti F, Schain M, et al. The alpha-synuclein PET tracer [18F]ACI-12589 distinguishes multiple system atrophy from other neurodegenerative diseases. Nat Commun. 2023;14:6750. doi:10.1038/s41467-023-42305-3. https://www.nature.com/articles/s41467-023-42305-3

24. Alpha-synuclein PET imaging: from clinical utility in MSA to the possible diagnosis of Parkinson's disease. https://pmc.ncbi.nlm.nih.gov/articles/PMC12155244/

25. New PET ligand captures alpha-synuclein in Parkinson's, MSA brains. ALZFORUM. https://www.alzforum.org/news/research-news/new-pet-ligand-captures-synuclein-parkinsons-msa-brains

26. Quintas S, et al. I123-FP-CIT (DaTSCAN) SPECT beyond the most common causes of parkinsonism: a systematic review. Mov Disord Clin Pract. 2024. doi:10.1002/mdc3.14055

27. Practical overview of 123I-ioflupane imaging in parkinsonian syndromes. RadioGraphics. https://pubs.rsna.org/doi/full/10.1148/rg.230133

28. Larson PEZ, et al. Current methods for hyperpolarized [1-13C]pyruvate MRI human studies. Magn Reson Med. 2024. doi:10.1002/mrm.29875. https://onlinelibrary.wiley.com/doi/10.1002/mrm.29875

29. Punwani S, et al. Consensus recommendations for hyperpolarized [1-13C]pyruvate MRI multi-center human studies. Magn Reson Med. 2025. doi:10.1002/mrm.30570. https://onlinelibrary.wiley.com/doi/10.1002/mrm.30570

30. Kinetic analysis of multi-resolution hyperpolarized 13C human brain MRI to study cerebral metabolism. https://pmc.ncbi.nlm.nih.gov/articles/PMC9420752/

31. Super-resolution hyperpolarized 13C imaging of human brain using patch-based algorithm. https://pmc.ncbi.nlm.nih.gov/articles/PMC7744189/

32. Deuterium metabolic imaging (DMI) of the human brain in vivo at 7T. https://pmc.ncbi.nlm.nih.gov/articles/PMC9756916/

33. Balanced steady state free precession enables high-resolution dynamic 3D deuterium metabolic imaging of the human brain at 7T. medRxiv. 2025. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11838661/

34. Reproducibility of 3D MRSI for imaging human brain glucose metabolism using direct (2H) and indirect (1H) detection at 7T and clinical 3T. https://pmc.ncbi.nlm.nih.gov/articles/PMC11019874/

35. Cember ATJ, Nanga RPR, Reddy R. Glutamate-weighted CEST (gluCEST) imaging for mapping neurometabolism: state of the art and emerging in vivo findings. NMR Biomed. 2023. doi:10.1002/nbm.4780

36. Application of glutamate-weighted CEST in brain imaging of nicotine-dependent participants in vivo at 7T. PLoS One. 2024. https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0297310

37. Mason EE, et al. Design analysis of an MPI human functional brain scanner. https://pmc.ncbi.nlm.nih.gov/articles/PMC5526464/. Human-sized magnetic particle imaging for brain applications. https://pmc.ncbi.nlm.nih.gov/articles/PMC6486595/

38. System characterization of a human-sized 3D real-time MPI scanner for cerebral applications. Commun Eng. 2024. https://www.nature.com/articles/s44172-024-00192-6

39. A human-scale magnetic particle imaging system for functional neuroimaging. Int J Magn Part Imaging. https://www.journal.iwmpi.org/index.php/iwmpi/article/view/707

40. Tolar M, Abushakra S, Sabbagh M. Neurotoxic soluble amyloid oligomers drive Alzheimer's pathogenesis and represent a clinically validated target for slowing disease progression. https://pmc.ncbi.nlm.nih.gov/articles/PMC8231952/

41. Sakono M, Zako T. Amyloid oligomers: formation and toxicity of Abeta oligomers. FEBS J. 2010;277(6):1348-1358. doi:10.1111/j.1742-4658.2010.07568.x

42. Amyloid-beta protofibrils: size, morphology and synaptotoxicity of an engineered mimic. PLoS One. 2013;8(6):e66101. https://pmc.ncbi.nlm.nih.gov/articles/PMC3699592/

43. Super-resolution imaging uncovers nanoscale tau aggregate hyperphosphorylation patterns in human Alzheimer's disease brain tissue. bioRxiv. 2024. https://www.biorxiv.org/content/10.1101/2024.04.24.590893

44. Morphological and hyperphosphorylation transitions of nanoscale tau aggregates in Alzheimer's disease. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12866830/

45. High-resolution cryo-EM structure determination of alpha-synuclein, a prototypical amyloid fibril. 2024. https://pmc.ncbi.nlm.nih.gov/articles/PMC11825309/

46. Guerrero-Ferreira R, Taylor NM, Mona D, et al. Cryo-EM structure of alpha-synuclein fibrils. eLife. 2018;7:e36402. https://elifesciences.org/articles/36402

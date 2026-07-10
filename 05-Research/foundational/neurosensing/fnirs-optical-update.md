# Technology Deep-Dive Update: Noninvasive fNIRS and Optical Wearables (2024 to 2026)

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: researchers, stakeholders
> **Tags**: `research`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)

*Prepared for Cytognosis Foundation NSF X-Labs / ARPA-H work. Compiled May 25, 2026. This file extends three existing seed documents (fnirs-deep-dive.md, wearables-comparative.md, and the CGM section of targeted-noninvasive-scanning.md). It does not repeat their full contents; it consolidates the engineering parameters that those documents treat in scattered form, adds 2024 to 2026 advances, and answers the specific questions of spatial resolution, temporal resolution, depth, tissue penetration profile, depth/location adjustability, commercial availability with prices, and known biases. It then covers the non-brain optical wearable landscape, anchored on optical continuous glucose monitoring (CGM), and asks what transfers to brain optical sensing.*

A note on terminology and honesty. Optical neuroimaging has a long history of strong claims followed by quiet retractions of scope (the fast optical signal, see below; transcranial single-cell readout; noninvasive glucose). Throughout, demonstrations are marked RESEARCH-only vs CLINICAL-cleared, single-lab findings are flagged as such, and company press claims are separated from peer-reviewed primary endpoints. Where a number is a best-case single demonstration rather than a routine capability, that is stated.

---

## PART A. BRAIN OPTICAL NEUROIMAGING

### A.1 The modality families, in one place

Near-infrared optical neuroimaging splits by how light is delivered and how returning photons are timed. The physics common to all of them: near-infrared light (roughly 650 to 950 nm, the "optical window" where hemoglobin and water absorption are both low enough to let photons travel centimeters) is launched into the scalp, diffuses through tissue along a banana-shaped path, and a fraction returns to a detector. Differential absorption at two or more wavelengths yields oxy- and deoxy-hemoglobin (HbO2, HbR); broadband detection adds cytochrome-c-oxidase (CCO), water, and lipid; coherent-light methods add blood flow.

| Family | What it measures | How it gets depth info | Maturity |
|---|---|---|---|
| CW-fNIRS (continuous wave) | HbO2, HbR (relative) | Source-detector (S-D) separation only | Mature, commercial, consumer |
| FD-fNIRS (frequency domain) | HbO2, HbR (absolute), scattering | RF phase shift = mean photon time-of-flight | Mature, niche commercial |
| TD-fNIRS / TD-DOT (time domain) | HbO2, HbR, CCO (absolute) | Picosecond pulses + photon time-of-flight gating | Maturing fast, commercial (Kernel) + research |
| HD-DOT (high-density DOT) | Tomographic HbO2/HbR maps | Dense overlapping multi-distance channels + forward model | Research, one commercial wearable (Gowerlabs) |
| DCS / SCOS / iDWS (speckle/correlation) | Cerebral blood flow (CBF) | Speckle decorrelation; longer S-D + time-gating for depth | Research, rapid 2024 to 2026 progress |
| Broadband NIRS (bNIRS) | CCO redox + Hb + water + lipid | Many wavelengths, model inversion | Research, neonatal clinical use |
| Acousto-optic / UOT, wavefront shaping | Absorption/scattering at acoustic-focus resolution | Focused ultrasound tags a voxel; phase conjugation | Pre-clinical (ex vivo skull, mouse); one company deploying |

### A.2 Spatial resolution: typical and best-achieved, and what limits it

The fundamental limit on optical spatial resolution in the brain is not the detector or the wavelength; it is scattering. Once a photon has scattered many times (the reduced scattering coefficient mu_s' in adult scalp/skull/cortex is roughly 0.7 to 1.2 per mm at 800 nm), its trajectory is randomized and the spatial origin of any given absorption event is blurred into a diffuse sensitivity profile. This is why optical methods are diffuse: the resolution is set by photon-transport physics, not optics.

- **Sparse CW-fNIRS** (standard 30 mm S-D arrays): spatial scale roughly 2 to 3 cm. Each channel reports a weighted average over a banana-shaped volume; adjacent channels overlap heavily.
- **HD-DOT** (about 13 mm spacing, overlapping multi-distance measurements, model-based image reconstruction): roughly 13 to 16 mm localization in outer cortex, approximately half the resolution of fMRI (Eggebrecht et al. 2014, doi:10.1038/nphoton.2014.107).
- **Ultra-high-density DOT** (about 6.5 mm spacing): a 2025 prototype reported 30 to 50 percent better spatial resolution and 19 to 35 percent lower decoding error than prior HD-DOT (White et al. 2025, Sci Rep, doi:10.1038/s41598-025-85858-7). A whole-head very-high-density DOT system was also reported in Imaging Neuroscience in 2025 (doi:10.1162/IMAG.a.54).
- **Micro-DOT** (Boas/BU-class wearable HD TD-DOT, RESEARCH-only): a 2025 preprint packs 256 time-domain channels into a tissue area where prior commercial TD modules offered 6, with about 10x less volume per module, using VCSEL sources and SPAD detectors (Micro-DOT, bioRxiv 2025.04.22.649003). The combination of HD geometry and TD gating is the most credible all-optical route to simultaneously better resolution and depth.
- **Best-case (research):** sub-centimeter (roughly 6 to 8 mm) functional localization in outer cortex under ultra-high-density geometry with anatomical priors. This is a best-case demonstration, not a routine number.

What limits it: multiple scattering blurs the sensitivity kernel; the ill-posed nature of the tomographic inverse problem (many tissue states map to similar measurements) requires regularization that further smooths the image; partial-volume effects mean a small focal activation is diluted by surrounding inactive tissue in the diffuse sampling volume. Anatomical priors (a subject MRI to anchor the photon-transport forward model) materially improve resolution but require an MRI, which most deployments do not have.

### A.3 Temporal resolution: typical and best

Two distinct limits must be separated: instrument sampling rate, and the bandwidth of the underlying biological signal.

- **Instrument sampling:** trivial. CW systems sample at 10 to 100 Hz routinely. Kernel Flow2 builds time-of-flight histograms at 285.7 Hz per wavelength and produces spectroscopic measures at 142.9 Hz, with a whole-head cortical-image frame rate of about 3.76 Hz (Flow2 spec, ResearchGate fig 378993435; consistent with the Flow validation paper, von Lühmann/Ortega-Martinez et al. 2022, doi:10.1117/1.NPh.9.2.026004). A TD-fNIRS device achieving a reliable 20 Hz acquisition rate for resting-state oscillation studies was reported (PMC9823873).
- **Biological bandwidth (hemodynamic):** this is the real constraint. The neurovascular response peaks 4 to 8 seconds after neural activity, giving an effective bandwidth of roughly 0.5 to 1 Hz for stimulus-evoked work. No amount of fast sampling changes this; you are oversampling a slow signal to denoise it.
- **Fast neuronal optical signal (EROS), best-case sub-100 ms:** if real, EROS would index scattering changes tied to neuronal firing at millisecond scale. Honest replication picture: EROS has remained a single-lab to small-consortium finding (Gratton/Fabiani group) for roughly 30 years, with signal amplitude on the order of 1/10000 of noise per trial, requiring thousands of averages and very short S-D distances. A handful of independent replications exist, but the broader fNIRS field has not adopted it and no product uses it. Treat as RESEARCH-only and unreliable for individual subjects.
- **Blood-flow methods (DCS/SCOS):** can resolve the cardiac pulsatile waveform (about 1 Hz fundamental plus harmonics), so effective bandwidth a few Hz, useful for autoregulation and pulsatility analysis but still slow relative to electrophysiology.

Bottom line: optical neuroimaging is fast to sample but slow in biology. For anything requiring millisecond neural timing, EEG or OPM-MEG remain superior; optical's advantage is molecular and metabolic specificity, not speed.

### A.4 Maximum depth in adult human brain, and what physically limits it

This is the single most important and most over-claimed parameter.

| Method | Typical brain-tissue depth (adult) | Best-case demonstrated | Limiting factor |
|---|---|---|---|
| CW-fNIRS | 1.5 to 2.5 cm beneath scalp; sensitivity dominated by outer 0.5 cm | ~2.5 cm | Scalp/skull absorption; photon budget |
| FD-fNIRS | 2 to 3 cm | ~3 cm | Phase SNR at depth |
| TD-fNIRS / TD-DOT | ~3 cm typical | ~4 cm under favorable anatomy | Late-photon count rate (shot noise) |
| DCS (800 nm) | ~1.5 cm S-D usable | extended by parallelization | Speckle SNR through skull |
| iDWS / LW-iDCS (1064 nm) | 3 to 3.5 cm | 4 to 4.5 cm S-D with 0.125 s integration | Detector shot noise (mitigated by interferometry) |
| TD-DCS at 1064 nm | depth-resolved cortical CBF | research demonstrations | Late-photon coherence + count rate |
| Acousto-optic / TRUE (Openwater) | claimed several cm to a focal voxel | sub-mm voxel at focal depth (company claim) | Speckle decorrelation time; SNR after skull |

**Consensus practical limit for robust functional cortical readout: 3 to 4 cm beneath the scalp, which reaches outer cortex only.** This has not been credibly broken in adult human brain by fNIRS alone. Truly subcortical readout (hippocampus at roughly 3 to 4 cm, thalamus deeper, substantia nigra at 7 to 9 cm) is out of reach for routine all-optical sensing as of May 2026.

What physically limits depth: it is a photon-budget problem, not a wavelength or detector problem alone. Light attenuates roughly exponentially with path length; at 810 nm only about 2 to 5 percent of incident NIR reaches the cortical surface, and the photons that probe deeper tissue are an exponentially smaller subset of an already small population. Detecting them requires either more source power (capped by skin safety limits, roughly the ANSI maximum permissible exposure), longer integration (which kills temporal resolution and is defeated by motion), or fundamentally better detection (single-photon counting, interferometric gain). Time-gating in TD selects late (deep-traveling) photons but cannot create photons that scattered back before reaching depth. Longer wavelengths (1000 to 1100 nm) reduce scattering and tissue absorption from hemoglobin, which is why 1064 nm iDWS is the most promising depth extender, but water absorption rises in that band, partially offsetting the gain.

### A.5 Tissue penetration profile: where light goes best vs worst, and where readouts are noisiest

Optical light does not penetrate all head tissues equally, and the readout noise is dominated by the tissues nearest the source and detector.

| Tissue | Optical behavior at 700 to 900 nm | Effect on the measurement |
|---|---|---|
| Scalp/skin | Moderate absorption, high scattering; contains melanin (epidermis) and dense vasculature | The largest single noise source. Scalp blood flow and systemic hemodynamics contaminate the signal; melanin attenuates and biases |
| Hair | Strong absorption and scattering, worst for dark/coarse/curly hair | Blocks optode-scalp coupling; the dominant subject-screening criterion |
| Skull (bone) | High scattering, moderate absorption; thickness 4 to 8 mm in adults | More than 99 percent of NIR is absorbed or scattered by adult skull; the main attenuator; thickness varies by site and subject |
| CSF | Low absorption, low scattering (nearly clear) | Acts as a light pipe/leak that smears the photon path laterally and complicates the forward model |
| Gray matter (cortex) | The target; moderate absorption (Hb-rich), high scattering | Where the signal of interest originates; only the outer 1 to 2 cm is reached |
| White matter | High scattering (myelin lipid), strong lipid absorption near 930 nm | Mostly beyond reach; contributes scattering background |
| Blood | Strong, wavelength-dependent absorption (HbO2 vs HbR is the whole basis of fNIRS) | The desired contrast in cortex, but a confound when in scalp/skull |
| Melanin | Broad absorption rising toward shorter wavelengths; concentrated in epidermis | Attenuates incident and emergent light; systematic skin-tone bias (see A.8) |

Best-penetrated: CSF (nearly transparent) and, relatively, gray matter once light arrives. Worst: hair, melanin-rich epidermis, and thick skull. Noisiest readouts: anything dominated by the superficial scalp layer, which is why short-separation reference channels (8 to 13 mm, sampling scalp only) are now standard for regressing out extracerebral hemodynamics (Saager and Berger 2008, doi:10.1364/JOSAA.25.001874). The deepest, most brain-specific channels are also the lowest-SNR, so there is an unavoidable depth-vs-noise tradeoff.

### A.6 Ability to adjust depth and location: state of the art

Five mechanisms exist to steer optical sensing in depth or location. Their real-world maturity differs sharply.

1. **Source-detector separation (depth, deployed today).** Longer S-D separation samples deeper, because the banana-shaped path arcs deeper for wider separations. HD-DOT exploits a continuum of separations (10 to 50 mm in Gowerlabs LUMO; up to 70 mm cross-tile) to recover depth tomographically. This is the workhorse and is fully commercial.
2. **Time-gating (depth, deployed in TD systems).** Selecting late-arriving photons in the DTOF emphasizes deeper tissue. Commercial in Kernel Flow2 and research TD-DOT. Real and routine, but bounded by the photon budget at long gates.
3. **Wavelength selection (molecular targeting, deployed).** Choosing wavelengths tunes which chromophore dominates (HbO2 vs HbR vs CCO vs water vs lipid). This is "molecular steering" and is the unique optical lever; broadband systems sweep roughly 120 wavelengths.
4. **Optode placement (location, deployed but static).** Today, location targeting means where you put the optodes against an atlas (10-5 system) or a subject MRI. This is set before recording and does not change during it. No commercial platform offers programmable, within-session optode steering (deciding which sources/detectors/wavelengths to read based on the prior measurement); this remains the open architectural niche.
5. **Ultrasound focusing and wavefront shaping (location + depth, pre-clinical to single-company).** Time-reversed ultrasonically encoded (TRUE) focusing tags a voxel with focused ultrasound and uses optical phase conjugation to focus light there; ultrasound-modulated optical tomography (UOT) isolates the acoustically tagged photons. TRUE with about 1.1 mm acoustic axial resolution is demonstrated in turbid media; UOT through ex vivo human skull is published (Opt Lett 2020, doi:10.1364/OL.392894); in vivo human brain UOT/TRUE is not credibly published as of May 2026. The fundamental obstacle is speckle decorrelation time in living tissue (microseconds), which forces extremely fast phase conjugation, plus SNR after skull attenuation. Openwater's platform is the only deployable head-worn implementation; its sub-millimeter focal-voxel-at-depth claim is a single-company claim awaiting independent peer-reviewed validation in human brain.

State-of-the-art summary on adjustability: depth adjustment is real and routine via S-D separation and time-gating (out to the 3 to 4 cm wall); molecular adjustment is real via wavelength; lateral location adjustment is static (you place optodes, you do not steer them mid-session); and true voxel-targeted focusing at depth through intact human skull is not yet a validated, deployable capability. The honest framing: nobody has shown noninvasive, voxel-targeted optical readout from a defined deep brain region in a freely behaving human.

### A.7 Commercial availability, clinical status, and prices

Marked CLINICAL (regulatory-cleared for a clinical indication somewhere) vs RESEARCH-only (research/investigational) vs CONSUMER (wellness, not a medical device). Prices are approximate, from vendor quotes and trade reporting; treat as limited evidence and ranges.

| System / vendor | Type | Status | Approx. price | Notes |
|---|---|---|---|---|
| Kernel Flow2 (Kernel, LA) | Whole-head TD-fNIRS + 4-ch dry EEG | RESEARCH-only | reported ~$50k (Flow1); Flow2 via partner programs | ~3500 channels/system; 2.5 kg helmet; 52 to 62 cm head; "Neuroscience as a Service" model; depression/MCI biomarker pipelines |
| NIRx NIRSport2 / WINGS2 (NIRx, Berlin/LA) | CW-fNIRS, wearable to lab | RESEARCH-only | ~$60k to $200k by channel count | Largest research CW vendor; allied with Artinis since 2024-2025 |
| Artinis Brite / OctaMon / OxyMon (NL) | CW-fNIRS, wearable + benchtop | RESEARCH-only | ~$30k to $120k | OctaMon-style short channels; NIRx alliance |
| Gowerlabs LUMO (UK, UCL spinout) | Wearable HD-DOT | RESEARCH-only | est. ~$100k to $250k (config-dependent; not publicly listed) | 6 g hexagonal tiles (3 sources, 4 detectors each), 10 to 50 mm intra/up to 70 mm cross-tile, fMRI-comparable cortical resolution, <60 s setup; SOTA wearable HD-DOT |
| Cortivision Photon Cap (Poland) | Wearable CW-fNIRS | RESEARCH-only | est. ~$40k to $80k | Up to 16 sources (760/850 nm), 10 detectors, ~37 channels, 86 Hz, 6 h battery, ~230 g; flown on ISS AX-3 (2024) |
| Shimadzu OMM / LIGHTNIRS (Japan) | CW-fNIRS | RESEARCH + clinical-adjacent in Japan | ~$80k to $200k | Japan is the largest clinical-fNIRS market |
| Hitachi ETG-7100 (Japan, legacy) | CW-fNIRS | CLINICAL (Japan PMDA, mood-disorder differential diagnosis); being phased out | legacy/used market | Basis of the only national-regulator-cleared psychiatric fNIRS use (Takizawa et al. 2014, doi:10.1016/j.neuroimage.2013.05.126) |
| PIONIRS (Italy) | Compact TD-fNIRS modules | RESEARCH-only | est. tens of $k per module | Politecnico di Milano lineage |
| Openwater Open-Motion / Open-LIFU (SF) | Optical + focused ultrasound | RESEARCH/investigational | AGPL open-source hardware/firmware | Open-Motion LVO stroke: 79% sensitivity / 84% specificity in prehospital reporting (company/trial); UPenn/Brown 151-patient LVO study; Birmingham rehab trial 2025; therapy not imaging is its main clinical thrust |
| Mendi (Sweden) | 2-ch prefrontal CW neurofeedback | CONSUMER (not FDA-cleared, not clinically peer-reviewed) | $299 | Marketing-claimed focus gains; treat as wellness |
| Brite / FocusCalm | Consumer fNIRS-like wellness | CONSUMER | ~$200 to $500 | Less validated than Mendi |

Key 2024 to 2026 commercial movement: Kernel shipping Flow2 and pivoting to data/biomarker services; NIRx and Artinis consolidating the research CW market; Gowerlabs LUMO remains the only wearable HD-DOT product; Openwater moved volume production to Taiwan (2025) under AGPL and continues to emphasize therapeutic LIFU and stroke triage over imaging. No fNIRS system outside Japan's legacy ETG clearance carries a clinical clearance for a psychiatric indication; everything else in the West is research/investigational.

### A.8 Known biases and noise sources

These are first-class design constraints, not footnotes, and several map directly onto equity.

- **Motion artifact.** Optode movement against the scalp causes large, abrupt intensity changes. Optical is far more motion-tolerant than EEG (it is not voltage-sensitive), but motion remains a major artifact, addressed by accelerometers, spline/wavelet correction, and short-channel regression.
- **Scalp and systemic hemodynamics (extracerebral contamination).** Scalp blood flow, blood pressure, heart rate, respiration, and Mayer waves (~0.1 Hz) all produce signals that masquerade as brain activation. Short-separation channels and global-signal regression are the standard correction. Single-distance CW is most vulnerable; TD and HD geometries are more robust.
- **Melanin / skin-tone bias.** NIR is attenuated by epidermal melanin, which is accounted for in neither standard fNIRS hardware nor analysis. This biases signal quality and hemodynamic estimates in darker-skinned participants and drives phenotypic exclusion from studies (Kwasa et al. 2023, doi:10.1038/s41562-023-01524-w; Webb et al. 2024, doi:10.1117/1.NPh.11.S1.S11510). A 2025 study (n = 115) quantified hair, pigmentation, head size, sex, and age effects on signal quality and issued practical recommendations (Quantifying impact of hair and skin on fNIRS, PubMed 40897802; bioRxiv 2024.10.28.620644). Treating melanin as a measured quantity rather than a noise term is both an accuracy and an equity requirement.
- **Hair.** Dark, coarse, curly hair blocks optode-scalp coupling; parted-braiding and optode-combing mitigate but do not eliminate it. The dominant practical screening criterion.
- **Optode coupling and pressure.** Coupling quality varies with cap fit and contact pressure; poor coupling raises noise and can drift over a session.
- **Partial-volume effect.** A focal activation is diluted within the large diffuse sampling volume, so concentration changes are underestimated and depend on assumed path length (the differential path-length factor), which itself varies by age, wavelength, and region.
- **Rayleigh and Mie scattering.** Tissue scattering (Mie-dominated by cell-scale structures, with a Rayleigh component) is the root cause of the diffuse limit on resolution and depth; it is wavelength-dependent (decreasing toward longer wavelengths), which motivates 1000 to 1100 nm methods.
- **Differential path-length and absolute-quantification error.** CW cannot recover absolute optical properties; it reports relative changes scaled by an assumed path length. FD and TD recover absolute properties and reduce this bias.

### A.9 Most promising mature vs upcoming technologies

- **Mature and ready for product-grade engineering:** CW-fNIRS and HD-DOT for outer-cortex hemodynamics; TD-fNIRS (Kernel-class) for absolute optical properties and better cortical specificity; broadband NIRS for CCO (neonatal clinical precedent). These are extensions of established physics with realistic engineering paths.
- **Upcoming and credible (2024 to 2026 momentum):** massively parallelized SCOS and interferometric DCS/iDWS for cerebral blood flow (the most active area, with reported 5x to 20x SNR gains and S-D separations pushed to 4 to 4.5 cm); wearable HD TD-DOT at high channel density (Micro-DOT, 256 TD channels); whole-head TD-DOT and very-high-density DOT systems. The CBF axis (DCS/SCOS) plus the metabolic axis (CCO) plus hemoglobin is the most powerful all-optical readout combination now reachable.
- **Aspirational and not yet validated in human brain:** acousto-optic/TRUE voxel focusing through intact skull, wavefront shaping through skull, and any noninvasive single-cell or molecular-specific (tau, neuromelanin) deep readout. The closest single-cell demonstration (MIT photoacoustic microscopy, 2025) reached single-cell resolution to ~1.1 mm in living mouse brain, not human, not wearable. Subcortical molecular imaging at PET-equivalent specificity remains out of reach noninvasively and will likely stay so through the near term.

---

## PART B. OTHER OPTICAL WEARABLES (NON-BRAIN)

The non-brain optical-wearable landscape matters to a brain-sensing platform for one reason: it is the field's longest and most honest stress-test of whether you can read a specific molecule through skin with light. The answer, after three decades, is "barely, and not yet at clinical accuracy." Those failure modes transfer almost directly to deep brain optical sensing.

### B.1 The optical CGM landscape

Continuous glucose monitoring is the canonical hard problem. Glucose has no strong, isolated NIR absorption peak; it has weak combination and overtone vibrations that overlap heavily with water, hemoglobin, fat, and protein. Mid-IR fundamental bands are stronger but penetrate skin only 50 to 100 micrometers, forcing photothermal or photoacoustic geometries. Physiological confounders (skin temperature, hydration, sweat, perfusion, motion, food) routinely exceed the glucose signal, and calibration drifts. Two FDA-cleared/CE-marked predecessors (GlucoWatch via reverse iontophoresis, 2001; Pendra via impedance, 2003) both failed in the field, the latter with a post-release correlation of about 35 percent (Klonoff, J Diabetes Sci Technol, PMC8655290).

| Company | Technology | Best reported MARD | Regulatory status (May 2026) | Notes |
|---|---|---|---|---|
| DiaMonTech (DE) | Mid-IR photothermal deflection | ~11.3% (published); ~20% over 10 days with 3 reference calibrations in a 2024-2025 Ulm study (n=36) | CE-marked as medical device (2019, D-Base benchtop) | Wearable D-Pocket in development; CE refers to the device, not iCGM-grade accuracy (Commun Med 2025, doi:10.1038/s43856-025-01241-7) |
| Know Labs (US) | Radiofrequency dielectric (NOT optical) | 11.1% (2024) | FDA submission planned for KnowU; not cleared | Included because frequently grouped with optical; mechanism is RF |
| GlucoModicum (FI) | Magnetohydrodynamic ISF extraction (needle-free; not purely optical) | 11.5% on mass-manufactured devices, 646 visits (Jul 2025) | EU IVDR pathway; FIMEA filing 2H 2025 | Talisman device with Phillips-Medisize; approaches but does not beat the ~10% benchmark |
| Rockley Photonics (UK/US) | SWIR photonic-integrated-circuit spectrometer | ~5 mg/dL in simulated skin (benchtop, not field MARD) | None | Emerged from Chapter 11 (2023, ~$35M); Apple-linked reporting; multiple analyses say years from commercial |
| Movano (US, EvieRing) | RF + planned optical | Not commercialized for glucose | None for glucose | Completed a second T1D pilot; women's-health ring shipping |
| Occuity (UK) | Non-contact handheld optical (confocal/pachymetry-derived) | Not yet a field MARD | None | Indigo handheld; non-contact eye/skin optics |
| CNoga (IL) | Visible-light multispectral imaging | Mixed/contested independent reports | Some CE marks claimed | Independent accuracy reports inconsistent |
| Apple / Samsung (research) | Silicon photonics / optical absorption | Not disclosed | None | Apple proof-of-concept reported 2023; Samsung announced intent; no FDA-cleared product. FDA issued a 2024 safety communication that it has cleared no smartwatch/ring for noninvasive glucose |

**Why optical glucose has been so hard, and where the field stands.** No truly noninvasive optical CGM has FDA clearance as of May 2026. The best independently reported MARDs cluster around 11 to 12 percent, comparable to first-generation invasive CGM (Dexcom G4 ~13%) but well short of current invasive systems (Dexcom G7, Libre 3 at roughly 7 to 9 percent) and short of the FDA iCGM standard (MARD typically under 10 percent with tight outlier bounds). The non-purely-optical needle-free entrants (GlucoModicum at 11.5%, Know Labs RF at 11.1%) currently match or slightly lead the purely optical entrants, which is itself a tell: multimodal and fluid-extraction approaches are doing better than light-through-skin alone.

### B.2 Resolution, depth, specificity limits, and what transfers to brain sensing

Optical CGM operates at shallow depth (dermis/superficial capillary bed, sub-millimeter to a few millimeters), so it does not face the brain's skull and centimeter-depth problem. Its hard limit is chemical specificity against a dominating water/Hb/lipid background at low analyte concentration. That specificity problem is exactly the brain problem minus the depth, which makes CGM the cleaner natural experiment for the spectroscopy half of the challenge.

Direct lessons that transfer to brain optical sensing:

1. **Few-wavelength approaches fail; hyperspectral is required** to separate a weak target from confounders. This argues for broadband/many-wavelength brain systems (CCO-grade), not 2-wavelength fNIRS, whenever molecular specificity beyond Hb is the goal.
2. **Calibration drift is the silent killer.** A wearable brain platform needs a stable internal reference (a structural landmark, a blood-flow baseline, or a metabolic anchor) to self-calibrate, or it will drift like every failed CGM.
3. **Free-living physiological variation exceeds bench noise by roughly an order of magnitude.** Lab-bench demonstrations (Rockley's 5 mg/dL in simulated skin) collapse in real wearers. Brain claims must be validated on freely behaving subjects, not phantoms.
4. **Multimodal beats single-modality.** The needle-free leaders fuse modalities. A brain platform should plan optical-plus-motion-plus-physiology fusion from the start.
5. **Machine learning rescues weak signals only when training matches deployment;** otherwise the model becomes a calibration crutch that hides drift. This caution applies equally to fNIRS foundation models.
6. **Regulators favor equivalence to an established reference.** CGM-to-blood-glucose maps onto optical-to-fMRI or optical-to-PET for brain; paired-reference validation is the credible path.

The sobering transfer: brain molecular targets are harder than glucose by every axis (greater depth, lower concentration, intervening bone, stricter regulatory standards). Three decades have not produced an FDA-cleared optical glucose monitor; this should calibrate any timeline for noninvasive deep molecular brain readout.

### B.3 Other optical wearables as proof of multi-analyte feasibility

Despite the glucose difficulty, several optical analytes are routinely measured noninvasively, which is the existence proof that multi-analyte optical wearables are feasible for the right targets:

- **SpO2 (pulse oximetry):** mature, ubiquitous, FDA-cleared in clinical devices. The cautionary note is that pulse oximetry itself carries a documented skin-tone bias (overestimation of oxygenation in darker skin), the same melanin problem that affects fNIRS, reinforcing that melanin must be handled explicitly.
- **Tissue oxygenation / muscle metabolism (NIRS for sports and clinical):** commercial wearable NIRS (Moxy, Artinis PortaLite) measures muscle StO2 and is a direct cousin of brain fNIRS.
- **Lactate:** optical-spectroscopy plus multivariate analysis has been proposed for noninvasive blood-lactate estimation (e.g., toward early sepsis recognition, PMC7570541); still research-grade, not a cleared wearable.
- **Bilirubin:** transcutaneous bilirubinometry is an established, FDA-cleared optical measurement (neonatal jaundice screening), one of the clearest successes of noninvasive optical chemistry, because bilirubin is a strong, accessible, superficial chromophore.
- **Hydration:** spectroscopic and photonic hydration monitoring is an active 2025 wearable area (JMIR mHealth scoping review 2025), still maturing.

The pattern across these: optical wearables succeed when the analyte is a strong, accessible chromophore at adequate concentration near the surface (SpO2, bilirubin) and struggle when it is a weak chromophore buried under a dominating background (glucose). Brain CCO sits in between, which is why it is the most distinctive but also the most demanding endogenous brain target. Multi-analyte optical sensing is proven in principle; the question is always whether the specific target clears the SNR-and-specificity bar.

---

## Synthesis for the proposal

The defensible position is unchanged and reinforced by 2024 to 2026 data: optical neuroimaging is a wearable chemistry instrument with molecular specificity (HbO2, HbR, CCO, water, lipid) and blood-flow capability (DCS/SCOS) that EEG and OPM-MEG cannot match, but it is bounded by a hard 3 to 4 cm depth wall, centimeter-to-sub-centimeter spatial resolution, and slow hemodynamic bandwidth. The credible near-term contribution is integrated multi-channel (Hb + CCO + CBF) wearable sensing of outer cortex with honest, equity-aware handling of melanin, hair, and scalp confounds, plus a software stack for adaptive, personalized region/wavelength scheduling, an architectural gap no vendor fills. Voxel-targeted deep focusing (Openwater-style) and noninvasive molecular/single-cell readout should be framed as long-horizon north stars, not Phase 0 deliverables. The CGM precedent is the governing cautionary tale: hyperspectral measurement, self-calibration, free-living validation, multimodal fusion, and equivalence-to-reference validation are mandatory, and timelines should be stated conservatively.

---

## References (this file; see seed docs for fuller bibliography)

1. Eggebrecht AT, et al. Mapping distributed brain function and networks with diffuse optical tomography. Nat Photonics. 2014;8:448-454. doi:10.1038/nphoton.2014.107
2. White BR, et al. Ultra-high density imaging arrays in DOT improve image quality and decoding. Sci Rep. 2025;15:7415. doi:10.1038/s41598-025-85858-7
3. Functional brain mapping using whole-head very high-density diffuse optical tomography. Imaging Neurosci. 2025. doi:10.1162/IMAG.a.54
4. Micro-DOT: Wearable, High-Density, Time-Domain Diffuse Optical Tomography Array for Functional Neuroimaging. bioRxiv. 2025. doi:10.1101/2025.04.22.649003
5. A compact time-domain diffuse optical tomography system for cortical neuroimaging. Imaging Neurosci. 2024. doi:10.1162/imag_a_00475
6. von Lühmann A, Ortega-Martinez A, et al. Kernel Flow: a high channel count scalable TD-fNIRS system. Neurophotonics. 2022;9(2):026004. doi:10.1117/1.NPh.9.2.026004 (and Kernel Flow2 spec sheet, ResearchGate fig 378993435)
7. Reliable fast (20 Hz) acquisition by a TD-fNIRS device. PMC9823873.
8. Saager RB, Berger AJ. Two-detector corrected NIRS for short-channel subtraction. J Opt Soc Am A. 2008;25:1874. doi:10.1364/JOSAA.25.001874
9. Robinson MB, et al. Mapping human cerebral blood flow with high-density multi-channel SCOS. Commun Biol. 2025. doi:10.1038/s42003-025-08915-x (bioRxiv 2025.03.03.638332)
10. Comparison of DCS, iDWS, and SCOS for blood flow monitoring. 2025. PMC12340614 (2.5 cm S-D for all three).
11. Comparative validation of SCOS against DCS for human cerebral blood flow. 2025. PMC13086003.
12. Long wavelength interferometric DCS (LW-iDCS) at 1064 nm; ~5x SNR. Sci Rep. 2023. doi:10.1038/s41598-023-36074-8. IEEE 20x iDWS follow-up (EurekAlert 1119268, 2026).
13. Bale G, Elwell CE, Tachtsidis I. Clinical NIRS of cytochrome-c-oxidase. J Biomed Opt. 2016;21(9):091307. doi:10.1117/1.JBO.21.9.091307
14. Kwasa J, et al. Demographic representation / phenotypic exclusion in fNIRS. Nat Hum Behav. 2023;7:1735-1741. doi:10.1038/s41562-023-01524-w; Front Neurosci 2023 PMC10203458.
15. Webb J, et al. Skin tone fairness in fNIRS. Neurophotonics. 2024;11(S1):S11510. doi:10.1117/1.NPh.11.S1.S11510
16. Quantifying impact of hair and skin characteristics on fNIRS signal quality (n=115). PubMed 40897802; bioRxiv 2024.10.28.620644.
17. Takizawa R, et al. Neuroimaging-aided differential diagnosis of the depressive state (Japan PMDA basis). NeuroImage. 2014;85:498-507. doi:10.1016/j.neuroimage.2013.05.126
18. Imaging through scattering human skulls with UOT. Opt Lett. 2020;45(11):2973. doi:10.1364/OL.392894
19. Openwater Open-Motion LVO stroke detection (prehospital 79% sens / 84% spec); medRxiv 2023.12.14.23299992; breath-hold validation medRxiv 2023.10.11.23296612 (PMC10923543); Birmingham rehab trial 2025.
20. Klonoff DC. Noninvasive glucose monitoring: in God we trust, all others bring data. J Diabetes Sci Technol. PMC8655290.
21. DiaMonTech mid-IR photothermal CGM validation. Commun Med. 2025. doi:10.1038/s43856-025-01241-7.
22. GlucoModicum needle-free CGM, MARD 11.5%, 646 visits, IVDR. Company release Jul 2025; pharmaphorum.
23. Know Labs RF glucose monitor, MARD 11.1%. BusinessWire 2024.
24. Rockley Photonics SWIR PIC glucose (~5 mg/dL simulated skin). 2023; Chapter 11 emergence BusinessWire 2023.
25. FDA safety communication: no cleared smartwatch/ring noninvasive glucose monitor. FierceBiotech 2024.
26. Minimally and non-invasive glucose monitoring: road to commercialization. Sensors & Diagnostics (RSC). 2025. doi:10.1039/D4SD00360H
27. Wearable hydration-monitoring technologies scoping review. JMIR mHealth uHealth. 2025;13:e60569.
28. Noninvasive optical lactate estimation toward sepsis recognition. PMC7570541.
29. MIT photoacoustic microscopy single-cell to ~1.1 mm in living brain (mouse). MIT News, Aug 2025.

# Targeted Noninvasive Optical Scanning: Toward a PET-Free Path to Molecular Brain Readouts

Background research for the Cytognosis Foundation and Hervé Marie-Nelly NSF X-Labs Phase 0 proposal. Compiled May 2026.

## 1. The Molecular-Imaging Analog in PET

Positron emission tomography (PET) made specific molecules visible in living human brains by tagging them with positron-emitting radioisotopes. The pharmaceutical core is the tracer: a small molecule (or peptide, antibody, nanoparticle) that selectively binds a target and carries a radiolabel (typically 18F, 11C, 68Ga). After intravenous injection and brain entry, positrons emitted by the decaying isotope annihilate with electrons to produce coincident 511 keV photon pairs detected externally. Without the tag, the same biology is invisible to PET; molecular specificity is conferred entirely by the tracer.

Four tracer families anchor the clinical landscape. 18F-FDG (fluorodeoxyglucose), in use since the 1970s, reports regional cerebral glucose metabolism and remains the most ordered PET study globally (1). 11C-PIB (Pittsburgh compound B), introduced in 2004, was the first widely used amyloid tracer and revealed in vivo amyloid pathology decades before clinical Alzheimer's symptoms (2). 18F-florbetapir (Amyvid), 18F-florbetaben, and 18F-flutemetamol followed, with FDA approval of florbetapir in 2012 for amyloid plaque imaging (3). 18F-flortaucipir (Tauvid), FDA-approved in 2020, was the first tau PET tracer for clinical use; autoradiography shows strong grey-matter signal in tau-positive brains and weak signal in tau-negative brains (4, 5). Beyond these, tracers exist for translocator protein (TSPO) as a neuroinflammation marker, dopamine transporter (DaT-SPECT 123I-ioflupane) for Parkinson's, and synaptic vesicle protein 2A (11C-UCB-J).

The conceptual question for an optical platform is whether the same molecule-tag-detect logic can run without ionizing radiation. The answer separates into three regimes: (a) molecules that already produce detectable optical signals without any added probe (intrinsic chromophores and autofluorophores); (b) molecules accessible only with an exogenous probe that crosses the blood-brain barrier (BBB), binds the target, and reports through skull and scalp; and (c) molecules currently out of reach noninvasively because their concentration, depth, or spectral overlap with background defeats existing instruments.

## 2. Intrinsic Noninvasive Optical Readouts of Disease-Relevant Molecules

A handful of endogenous chromophores generate sufficient optical contrast through scalp and skull to be measured externally with diffuse optical spectroscopy or related modalities.

**Oxy- and deoxy-hemoglobin (HbO2 / HbR).** Functional near-infrared spectroscopy (fNIRS) and diffuse optical tomography exploit the spectrally distinct absorption of HbO2 and HbR in the 650 to 900 nm window. This is the established backbone of cortical hemodynamic imaging in adults and infants. High-density diffuse optical tomography (HD-DOT) now produces cortical maps that approach the spatial resolution of fMRI in superficial cortex (6).

**Cytochrome-c-oxidase (CCO).** CCO is the terminal enzyme of the mitochondrial electron transport chain. Its oxidized form has a broad absorption band near 830 nm that overlaps with hemoglobin but is spectrally separable using broadband NIRS. CCO concentration in vivo is roughly 10 percent that of hemoglobin, so reliable separation demands many wavelengths rather than the two or four wavelengths of conventional fNIRS (7). Systems such as CYRIL have demonstrated continuous bedside measurement of oxidized CCO changes over days in neonatal encephalopathy, where the metabolic readout adds prognostic value beyond hemoglobin alone (7, 8). For functional brain activation, broadband NIRS of oxidized CCO is more brain-specific than the hemoglobin signal because CCO concentration in extracerebral tissue is far lower than in cortex (9).

**Water and lipids.** Both have characteristic absorption peaks in the short-wave infrared (SWIR, roughly 1000 to 2000 nm): water near 1150, 1450, and 1900 nm; lipids near 1040, 1200, 1400, and 1700 nm (10, 11). Hemoglobin no longer dominates absorption in this window, so SWIR diffuse optical spectroscopy and SWIR photoacoustic imaging can recover tissue water fraction and lipid content. Because brain lipid composition changes with aging and with Alzheimer's pathology, SWIR is a plausible label-free axis for monitoring tissue composition, though no human in vivo brain-imaging system yet maps brain lipids transcranially.

**Melanin and neuromelanin.** Neuromelanin is a pigment synthesized by oxidation of catecholamines and accumulates in substantia nigra dopaminergic and locus coeruleus noradrenergic neurons. Its loss tracks neuronal death in Parkinson's disease (12). Neuromelanin-sensitive MRI (a T1-weighted spin-echo sequence) is now a validated biomarker showing volume loss in both substantia nigra and locus coeruleus in cohort studies (13). The substantia nigra sits roughly 70 to 90 mm beneath the scalp at the midbrain; this depth, combined with intervening bone and tissue, places noninvasive optical detection of neuromelanin beyond conventional fNIRS reach. The chromophore does absorb broadly across visible and NIR, but reaching it requires either deep penetration techniques (SORS, photoacoustic) or scalp/skin neuromelanin proxies, which are not pathophysiologically equivalent.

**Glucose.** Glucose has weak combination and overtone vibrational absorption features in NIR and stronger fundamental bands in mid-IR. Despite three decades of work it remains the canonical "almost there" target (Section 6).

**Lactate, NADH, FAD.** NADH and FAD are intrinsically fluorescent and report cellular redox state. Their excitation maxima (around 340 nm for NADH, 450 nm for FAD) sit in the UV-blue range with very poor tissue penetration, so the technique works for ex vivo biopsies, intraoperative tumor margin imaging, and microscopy through cranial windows, but not for transcranial human imaging (14, 15). Lactate has no useful direct optical signature in vivo; its detection in brain currently requires MR spectroscopy.

**Protein aggregates: amyloid, tau, alpha-synuclein.** Misfolded protein aggregates differ from native protein primarily in secondary structure: amyloid plaques and tau neurofibrillary tangles are rich in cross-beta-sheet structure. Beta-sheet conformations generate characteristic Raman signatures in the amide I (1665 to 1680 cm-1) and amide III (1230 to 1245 cm-1) regions. Raman microspectroscopy can fingerprint tau variants by their secondary structure (16), and Raman studies of alpha-synuclein aggregation document the spectral shift from alpha-helix-dominated monomer (49 percent alpha-helix in solution) to beta-sheet-dominated mature fibrils, with characteristic amide I changes from 1655, 1664, 1680 cm-1 in controls to 1650, 1670, 1687 cm-1 in PD subjects in skin biopsy studies (17, 18). These are intrinsic signals (no probe needed) but they are weak; conventional spontaneous Raman scattering has a cross section roughly 10 orders of magnitude smaller than fluorescence, so direct transcranial Raman detection of brain protein aggregates has not been demonstrated in humans. SESORS and CARS/SRS variants (Section 4) are attempts to bridge that sensitivity gap.

## 3. Exogenous Probes for Noninvasive Optical Brain Imaging

Where intrinsic contrast fails, the PET playbook says: add a tagged probe. The optical equivalent is a fluorescent or absorbing probe that crosses the BBB, binds a target, and emits in a window where skull and scalp transmit some light.

**CRANAD series (curcumin-based, donor-acceptor-donor architecture).** Moore and colleagues engineered difluoroboronate-modified curcumins with NIR emission around 715 to 805 nm and amyloid binding affinity. CRANAD-2 increases fluorescence 70-fold and blue-shifts 90 nm on binding insoluble Aβ but misses soluble oligomers (19). CRANAD-3 and CRANAD-58 detect both soluble and insoluble Aβ; in 4-month-old APP/PS1 transgenic mice, in vivo NIR signal was 2.29-fold higher than wild-type, distinguishing transgenic mice as young as 4 months (20, 21). These probes work transcranially in mice (millimeter-thin skull) but no equivalent human study exists.

**Methoxy-X04 and Congo red derivatives.** Methoxy-X04, derived from the Chrysamine G and Congo red scaffold, crosses the BBB and binds beta-sheet structures in dense-core Aβ plaques with affinity Ki of 26.8 nM (22). It is a workhorse for two-photon microscopy through cranial windows in mice but emits in the blue (around 450 nm), so it has no plausible transcranial application in humans.

**Aza-BODIPY and BODIPY molecular rotors.** BODIPY-based amyloid probes use molecular rotor mechanisms (intramolecular rotation suppressed on binding leads to fluorescence turn-on) and offer high molar extinction, high quantum yield, and good photostability. Aza-BODIPY variants shift emission into NIR (23). Mouse studies are encouraging; human translation has not occurred.

**THK-565 and tau probes.** THK-565 has been reported as an NIR fluorescent probe for in vivo amyloid deposit detection in AD mouse models, with the same caveats as CRANAD (24). The THK series originally aimed at tau imaging in PET was largely supplanted by flortaucipir for clinical use; the analogous optical probes remain preclinical.

**Voltage-sensitive and calcium-sensitive dyes; GEVI/GECI.** These genetically encoded indicators have transformed rodent and zebrafish neuroscience but they require viral transfection and excitation in the visible range. Two limits make them inapplicable to noninvasive human readout. First, they require gene delivery, which is not an acceptable risk-benefit tradeoff for general human imaging. Second, even where deployed, GEVIs photobleach rapidly (ASAP and JEDI series show 30 percent signal loss within 5 seconds at 0.32 W/cm2 blue-light illumination) and are roughly two orders of magnitude dimmer than calcium indicators, limiting in vivo use even in animals (25, 26).

**FDA-approved or in-trial systemic NIR probes.** Indocyanine green (ICG) is FDA-approved for ophthalmic angiography and cardiac output measurement and has off-label use in fluorescence-guided neurosurgery. ICG is a passive marker that reaches tumor tissue only when the BBB is disrupted (27, 28). 5-aminolevulinic acid (5-ALA, Gleolan) is FDA-approved for glioma fluorescence-guided resection and works by intracellular conversion to fluorescent protoporphyrin IX in tumor cells. Neither targets a specific neurodegenerative biomarker. No NIR probe specific to amyloid, tau, or alpha-synuclein has reached human clinical use.

**Limitations.** The combined failure modes are well known: poor BBB crossing, low specificity (off-target binding to other beta-sheet structures), autofluorescence background from endogenous flavins and porphyrins, photobleaching under sustained illumination, and dilution of probe concentration during the long transit from injection site to brain target. Even an ideal probe must compete with the optical losses of skull and scalp (Section 5).

## 4. Beyond Fluorescence: Raman, SERS, Photoacoustic, Hyperspectral

When fluorescence is too sensitive to background or lacks specificity, alternative contrast mechanisms can help.

**Spontaneous Raman spectroscopy.** Inelastic scattering provides molecule-specific vibrational fingerprints without labels. The cross section is small, so spontaneous Raman struggles with deep tissue. The technique excels in microscopy and intraoperative settings, including label-free brain-tumor margin detection during surgery.

**Spatially offset Raman spectroscopy (SORS).** Introduced by Pavel Matousek in 2005, SORS separates surface and subsurface Raman signals by collecting scattered light at a lateral offset from the illumination spot. SORS pushes Raman depth penetration from millimeters to centimeters, with reports of useful signal at up to 5 cm in turbid media (29). Inverse SORS uses a ring-shaped illumination with central detection for further depth gains. SORS is used clinically for transcutaneous bone-quality assessment and is moving toward transcranial applications.

**Surface-enhanced Raman scattering (SERS) and SESORS.** SERS uses metal nanostructures (typically gold or silver) to enhance Raman cross sections by 10^6 to 10^10. Combined with SORS, SESORS has demonstrated detection of neurotransmitters (melatonin, serotonin, epinephrine) at 100 micromolar in brain-tissue mimics through cat skull (30, 31). In mouse models, SESORS has detected glioblastoma through intact skull in as little as 6 seconds using targeted nanotag probes (32). The crucial caveat is that SERS requires nanoparticle delivery to the target, which reintroduces the BBB and biodistribution challenges that motivate a probe-free approach in the first place. No human transcranial SESORS measurement of amyloid or tau has been reported.

**Photoacoustic imaging.** Pulsed light absorbed by tissue chromophores creates thermoelastic expansion and ultrasound waves; detection is acoustic, so resolution scales with ultrasound rather than diffuse optical limits. iThera Medical's MSOT (multispectral optoacoustic tomography) is the leading clinical platform, reaching roughly 10 to 30 mm depth with handheld curved-array probes (33). Lihong Wang's group demonstrated the first in-human transcranial functional photoacoustic computed tomography (PACT) in 2022 in a hemicraniectomy patient, with finger-tapping and tongue-tapping responses visible on the skull-intact hemisphere, though scattered by skull aberration (34, 35). In Alzheimer's mouse models, volumetric multispectral PA tomography detects tau accumulation using probes such as PBB5 at 110 micrometer resolution (36), and OR-PAM detects amyloid plaques through cranial windows (37). Through-skull human brain protein imaging by photoacoustic methods has not been demonstrated.

**Polarization-sensitive photoacoustic Mueller matrix tomography.** A 2022 preprint demonstrated label-free visualization of amyloid plaques using polarization contrast, exploiting the optical anisotropy of cross-beta-sheet structures (38). The work is preclinical and in ex vivo or thin-section samples.

**Hyperspectral diffuse optical tomography.** Continuous-wave DOT with many spectral channels recovers absorption and scattering across wavelengths, supporting multi-chromophore separation (HbO2, HbR, CCO, water, lipid). 2024 to 2025 work includes whole-head very-high-density DOT for functional mapping and frequency-domain plus broadband systems for hyperspectral optical-property estimation (39, 40, 41).

**Coherent Raman methods: CARS and SRS.** Coherent anti-Stokes Raman scattering (CARS) and stimulated Raman scattering (SRS) drive vibrational transitions coherently, boosting signal by orders of magnitude over spontaneous Raman. SRS microscopy is used clinically for intraoperative brain-tumor margin imaging (FDA-cleared SRH systems exist), and CARS visualizes brain lipids label-free (42, 43). Both are inherently nonlinear (requiring high peak power) and short-working-distance microscopies; transcranial human application is not currently feasible.

**Ultrasound-aided optical focusing.** Time-reversed ultrasonically encoded (TRUE) focusing and ultrasound-modulated optical tomography (UMOT) use focused ultrasound to "tag" photons in a small voxel; the tagged light can then be selectively detected or wavefront-shaped to focus inside scattering tissue. TRUE focusing with roughly 1.1 mm acoustic axial resolution has been demonstrated in turbid media (44, 45). Openwater's platform is built on this principle (see Section 5). Adaptive optics approaches with reflection-matrix microscopy at 1.3 micrometer wavelength have achieved imaging through intact mouse skull to 1.1 mm below pia (46, 47).

## 5. The Depth and Specificity Boundary

Where does noninvasive molecular imaging stop working today, and why?

**Optical losses through scalp and skull.** A reasonable rule of thumb at 810 nm: roughly 2 to 5 percent of incident NIR light reaches the cortical surface; more than 99 percent of emitted NIR is absorbed or scattered by an adult human skull (48). Penetration in the visible and traditional NIR (400 to 900 nm) is limited to 1 to 2 mm of effective focused depth before scattering dominates. Diffuse imaging reaches 20 to 30 mm into superficial cortex but at the cost of spatial resolution (centimeter scale, not millimeter). Longer wavelengths (1000 to 1700 nm SWIR, the so-called "NIR-II window") suffer less scattering but more water absorption (49). Detection of any specific molecule in deep subcortical structures such as substantia nigra, hippocampus, or thalamus is currently impossible by purely optical means.

**Probe-delivery challenges for the brain.** Even an excellent BBB-permeable probe is diluted across the entire body before reaching brain, with target concentration in the nanomolar to low-micromolar range. Off-target binding to other beta-sheet structures, vascular amyloid, and lipofuscin reduces specificity. PET's advantage is twofold: positron-photon detection is essentially background-free, and the radioactive label persists with known kinetics; an optical probe must beat tissue autofluorescence, photobleach slowly, and emit in a window where skull transmits.

**What has been demonstrated in vivo in human brain noninvasively for specific molecules beyond HbO2, HbR, and CCO?** Honestly, very little. fNIRS and HD-DOT map cortical hemodynamics and CCO. Two reports suggest fNIRS distinguishes amyloid-positive from amyloid-negative subjects using spectral features near 768 and 891 nm (50), but these claims are based on a small number of studies and have not been independently replicated at the scale of PET. No transcranial human in vivo measurement of tau, alpha-synuclein, neuromelanin, or any synaptic marker by an optical method has reached the clinic. The honest assessment is that intrinsic optical molecular imaging of the human brain remains in proof-of-concept stages outside of the hemoglobin and CCO channels.

**Key 2023 to 2026 advances pushing the boundary.**

- Openwater's wearable platform, built around focused ultrasound combined with NIR optics and computational imaging, has moved from cart-sized prototypes to volume-production wearables in Taiwan in 2025. Investment exceeded 100 million USD by early 2024 (51). The platform targets stroke detection, depression treatment via low-intensity focused ultrasound, and neurodegenerative diagnostics, all under an AGPL open-source model. A small open-label depression trial reported BDI scores moving from severe depression to remission in roughly one week with 10 minutes of daily LIFU therapy, with more than one-third of 20 patients reaching remission; this is therapeutic neuromodulation, not molecular imaging (52, 53).

- Transcranial PACT in human (Wang lab, 2022). First functional PACT in a hemicraniectomy patient; serves as proof that photoacoustic signals can be recovered through human skull, with caveats (35).

- SESORS in vivo imaging frameworks (2023 to 2024). Improved sampling-frequency frameworks for in vivo SESORS imaging have been published in npj Imaging, though they remain in animal models (32, 54).

- Adaptive-optics three-photon imaging through intact rodent skull (2024 to 2025). ALPHA-FSS and MeNet-AO systems demonstrate aberration correction enabling sub-pia imaging at depths of 750 micrometers to 1.1 mm in mice. Skull thickness in mice is roughly 100 micrometers; scaling to 6 to 8 mm of adult human skull is not yet demonstrated (46, 47).

- Shortwave-infrared meso-patterned imaging for label-free water and lipid mapping (2020 to 2024) (10). Provides a path to tissue-composition mapping that does not depend on probes.

## 6. Application Case Study: Noninvasive Continuous Glucose Monitoring

Optical glucose monitoring is the longest-running attempt to read out a specific molecule noninvasively, with three decades of failed and pending products. The history is the most informative real-world case for any spectroscopic biomarker platform.

**Why it has been hard.** Glucose has no strong, isolated absorption peak in NIR; it has weak combination and overtone vibrations that overlap heavily with water, hemoglobin, fat, and proteins. Mid-IR fundamental bands are stronger but penetrate skin only 50 to 100 micrometers, requiring photothermal or photoacoustic detection geometries. Physiological variables (skin temperature, hydration, sweat, blood flow, perfusion, food, motion) introduce confounders larger than the glucose signal. Calibration drifts. Even when bench-top results look good, real-world performance in free-living conditions collapses.

**Lessons from prior failures.**

- GlucoWatch (Cygnus, 2001) used reverse iontophoresis. FDA-approved, satisfactory accuracy in trials, but skin irritation, burns, and reliability issues killed it (55).
- Pendra (Pendragon Medical, 2003) used impedance spectroscopy. CE-approved, but post-release correlation with reference glucose was 35 percent. Company bankrupt in 2005 (55).
- The general lesson: when publicity outruns data, the resulting patient and clinician disappointment damages the entire field's credibility.

**Current efforts (status as of 2025 to 2026).**

- *Rockley Photonics*. SWIR photonic-integrated-circuit spectrometer in a miniaturized wearable format. Benchtop glucose prediction accuracy of 5 mg/dL in simulated skin. 40-subject 10-week IRB study with Type 1 and Type 2 diabetics showed progress, not clinical readiness (56). Rockley emerged from Chapter 11 in June 2023 with around 35 million USD additional funding (57). Apple has reportedly partnered with Rockley; multiple analyses through 2025 indicate Apple's noninvasive glucose feature remains several years from commercial release.
- *Movano Health (Movano / EvieRing)*. RF-based, with optical sensors planned for glucose. Has shipped a women's-health wearable; glucose feature not commercialized.
- *Samsung and Apple research*. Samsung announced 2025 glucose monitoring intent; no FDA-cleared product as of May 2026. Industry consensus is that accuracy and regulatory hurdles remain unresolved.
- *DiaMonTech*. Mid-IR photothermal deflection spectroscopy in a benchtop D-Base device, CE-approved as medical device in 2019 with MARD around 12 percent in initial validation. A 2024 to 2025 prospective study at the Institute for Diabetes Technology in Ulm with 36 individuals showed MARD around 20 percent over 10 days with three reference calibration measurements (58, 59). Wearable form factor (D-Pocket) is in development.
- *Know Labs*. RF-based, not optical. KnowU wearable announced for FDA submission; published MARD of 11.1 percent in 2024 (60).
- *GlucoModicum*. Magnetohydrodynamic interstitial fluid extraction approach. Early-stage clinical work.
- *CNoga*. Photonic device using visible spectroscopy; mixed independent accuracy reports.

**Where the field stands.** No truly noninvasive optical CGM has FDA clearance as of May 2026. The best reported MARDs hover around 11 to 12 percent under controlled calibration; this is comparable to first-generation invasive CGM (Dexcom G4 at around 13 percent) but well below current Dexcom G7 and Libre 3 performance (around 7 to 9 percent MARD). The FDA's iCGM standard requires MARD typically under 10 percent with tight bounds on outliers, which no purely optical system has hit in independent multicenter trials.

**Lessons transferable to brain biomarker readout.**

1. Single-wavelength or few-wavelength approaches fail; hyperspectral measurement is required to disentangle target from confounders.
2. Calibration drift is the silent killer; the system must be self-calibrating against a stable reference (a structural anatomy landmark, a blood-flow signal, or a metabolic baseline).
3. Real-world physiological variation (motion, temperature, perfusion, sweat) often exceeds laboratory-bench noise floors by an order of magnitude. Wearable validation in free-living conditions is essential.
4. Multi-modal sensing (optical plus RF plus pressure plus motion plus skin parameters) consistently outperforms single-modality systems, and GlucoTrack's three-technology fusion is the canonical example.
5. Machine learning can rescue weak signals only when the training distribution matches deployment; otherwise the model becomes a calibration crutch that hides drift.
6. The regulatory pathway favors devices that demonstrate equivalence to a clinically established measurement (CGM-to-blood-glucose, or in brain context: optical-to-PET, or optical-to-CSF biomarker).

The transfer to brain biomarker readout is direct. Replace "glucose" with "amyloid signature in cortex" or "neuromelanin in midbrain" and most of the failure modes carry over. The implication is not that the goal is unreachable; it is that incremental, multi-modal, well-calibrated demonstrations on robustly established intermediate biomarkers (cortical hemodynamics, CCO, regional tissue water and lipid) must precede attempts on harder targets.

## 7. Implications for the Cytognosis Plus Hervé Proposal

**Realistic 5 to 10 year envelope.** The honest envelope for noninvasive targeted brain readout, given current physics and biology, is:

- *Year 1 to 3 reachable.* Cortical HbO2, HbR, CCO; tissue water and lipid in superficial cortex via SWIR; regional cerebral blood flow via speckle contrast or diffuse correlation spectroscopy; cortical mitochondrial function via broadband NIRS of CCO. These are extensions of established physics with realistic engineering paths.

- *Year 3 to 7 plausible with hard work.* Cortical-surface amyloid load via hyperspectral diffuse optical features (extending the 768 and 891 nm work) combined with cortical structural priors from concurrent MRI calibration in a subset of participants. Photoacoustic cortical vascular and structural imaging at a few-millimeter depth. SORS for skull-bone composition (relevant to depth normalization) and, with development, for cortical molecular signatures. Wearable hyperspectral DOT with hundreds of channels and on-board machine learning.

- *Year 7 to 10 aspirational.* Transcranial photoacoustic detection of cortical amyloid signature using endogenous polarization or absorption contrast plus a tested, BBB-permeable optical probe analogous to florbetapir but optical. Possibly SESORS through skull with engineered safe nanotags. Ultrasound-aided optical focusing (Openwater-style) reaching subcortical structures for blood-flow and metabolic readouts; molecular targeting at subcortical depth remains uncertain.

- *Likely still out of reach by 2036 noninvasively.* Subcortical molecular imaging at PET-equivalent specificity (tau in entorhinal cortex, alpha-synuclein in substantia nigra at sub-millimeter resolution, individual synaptic-density quantification). For these the radiotracer plus PET pipeline will remain the reference standard.

**Targets reachable first (priority order for a wearable spectroscopy headset).**

1. *Hemoglobin and CCO mapping.* Already feasible, ready for product-grade engineering and large-cohort validation against fMRI.
2. *Regional tissue water and lipid via SWIR.* Achievable with current photodetector and laser technology; produces a label-free aging biomarker.
3. *Neuromelanin (indirect).* Reaching the substantia nigra directly is implausible; cortical and skin neuromelanin signatures may serve as Parkinson-related proxies, with validation against neuromelanin MRI as ground truth.
4. *Cortical amyloid load.* The 768 and 891 nm spectral features are a tantalizing starting point but require independent multicenter replication. Realistic intermediate target with a 5-year horizon, contingent on replication.
5. *Cortical protein aggregates via SORS-class methods.* Transcranial SORS for cortical signatures is a 7- to 10-year target, contingent on advances in detector sensitivity and depth-resolved deconvolution.
6. *Optical tracer (BBB-permeable, NIR, specific).* Highest scientific payoff if successful; highest regulatory and pharmacological risk. CRANAD-class compounds are the obvious starting chemistry but none have entered human trials.

**Honest gaps and risks.**

- *Skull-induced aberration and absorption* is the single hardest unsolved problem for transcranial molecular imaging. Adaptive optics works in mice; scaling to adult human skull thickness is unproven.
- *Specificity in vivo* is harder than specificity in vitro. Beta-sheet signatures appear in many proteins, lipofuscin autofluorescence overlaps amyloid emission bands, and cerebrovascular amyloid mimics parenchymal plaques in any line-of-sight modality.
- *Validation against PET* requires paired studies with concurrent amyloid or tau PET, which constrains the trial design to centers with PET access and adds regulatory and cost complexity.
- *The CGM precedent* is sobering. Three decades of effort have not produced an FDA-cleared optical glucose monitor. Brain molecular targets are harder by every measure (depth, concentration, intervening tissue, regulatory standards).
- *Probes' regulatory path* is essentially a new IND for each candidate compound, with all the timelines and costs that implies; the optical platform alone does not shortcut that.

**Strategic framing for the proposal.** The defensible pitch is not "noninvasive PET-equivalent imaging in 5 years." It is: "a closed-loop, multi-modal spectroscopic headset that today reads hemodynamic and metabolic state robustly, that ships with the engineering headroom to add SWIR, photoacoustic, and SORS channels as components mature, and that uses adaptive signal-processing and physiologically calibrated machine learning to push the specificity envelope along a credible 10-year roadmap." Focus the X-Labs Phase 0 work on demonstrating: (a) multi-chromophore separation including CCO and SWIR water and lipid in a wearable form factor; (b) replication of the amyloid-discriminating spectral feature; (c) integration of structural priors (MRI calibration in a subset) to anchor optical inversion; and (d) a clearly stated, honest depth-and-specificity boundary that distinguishes near-term clinical claims from long-term aspirational targets.

The proposal should explicitly position the Cytognosis platform as complementary to (not a replacement for) PET in the near term, and as a path toward continuous monitoring at population scale that PET cannot economically provide.

---

## References

1. Mosconi L, Berti V, Glodzik L, et al. Pre-clinical detection of Alzheimer's disease using FDG-PET, with or without amyloid imaging. J Alzheimers Dis. 2010;20(3):843-854.

2. Klunk WE, Engler H, Nordberg A, et al. Imaging brain amyloid in Alzheimer's disease with Pittsburgh Compound-B. Ann Neurol. 2004;55(3):306-319. doi:10.1002/ana.20009

3. Cure Alzheimer's Fund. FDA Approves First Tau Imaging Agent For PET Scans For Diagnosis of Alzheimer's Disease. https://curealz.org/news-and-events/fda-approves-first-tau-imaging-agent-for-pet-scans-for-diagnosis-of-alzheimers-disease/

4. Mintun MA, Lo AC, Duggan Evans C, et al. Tauvid: The First FDA-Approved PET Tracer for Imaging Tau Pathology in Alzheimer's Disease. https://pmc.ncbi.nlm.nih.gov/articles/PMC7911942/

5. Leuzy A, Smith R, Cullen NC, et al. A review of the flortaucipir literature for positron emission tomography imaging of tau neurofibrillary tangles. Brain Commun. 2024;6(1):fcad305. doi:10.1093/braincomms/fcad305. https://academic.oup.com/braincomms/article/6/1/fcad305/7424837

6. Eggebrecht AT, Ferradal SL, Robichaux-Viehoever A, et al. Mapping distributed brain function and networks with high-density diffuse optical tomography. Nat Photonics. 2014;8(6):448-454. See also: High-density diffuse optical tomography for imaging human brain function. Rev Sci Instrum. 2019;90(5):051101. https://pmc.ncbi.nlm.nih.gov/articles/PMC6533110/

7. Bale G, Mitra S, Meek J, Robertson N, Tachtsidis I. A new broadband near-infrared spectroscopy system for in-vivo measurements of cerebral cytochrome-c-oxidase changes in neonatal brain injury. Biomed Opt Express. 2014;5(10):3450-3466. https://pmc.ncbi.nlm.nih.gov/articles/PMC4206316/

8. Mitra S, Bale G, Meek J, Tachtsidis I, Robertson NJ. Interrelationship Between Broadband NIRS Measurements of Cerebral Cytochrome C Oxidase and Systemic Changes Indicates Injury Severity in Neonatal Encephalopathy. https://pmc.ncbi.nlm.nih.gov/articles/PMC6126436/

9. Phan P, et al. Functional NIRS Measurement of Cytochrome-C-Oxidase Demonstrates a More Brain-Specific Marker of Frontal Lobe Activation. https://pmc.ncbi.nlm.nih.gov/articles/PMC6126217/

10. Wilson RH, Nadeau KP, Jaworski FB, Tromberg BJ, Durkin AJ. Review of short-wave infrared spectroscopy and imaging methods for biological tissue characterization. J Biomed Opt. 2015;20(3):030901. https://pmc.ncbi.nlm.nih.gov/articles/PMC4370890/

11. Wilson RH, et al. Shortwave-infrared meso-patterned imaging enables label-free mapping of tissue water and lipid content. Nat Commun. 2020;11:5302. https://www.nature.com/articles/s41467-020-19128-7

12. Sulzer D, Cassidy C, Horga G, et al. Neuromelanin detection by magnetic resonance imaging (MRI) and its promise as a biomarker for Parkinson's disease. NPJ Parkinsons Dis. 2018;4:11. https://www.nature.com/articles/s41531-018-0047-3

13. Cassidy CM, Zucca FA, Girgis RR, et al. In vivo detection of substantia nigra and locus coeruleus volume loss in Parkinson's disease using neuromelanin-sensitive MRI. https://pmc.ncbi.nlm.nih.gov/articles/PMC10101455/

14. Skala MC, et al. Evaluating Cell Metabolism Through Autofluorescence Imaging of NAD(P)H and FAD. https://pmc.ncbi.nlm.nih.gov/articles/PMC6352511/

15. Label-Free Optical Metabolic Imaging in Cells and Tissues. https://pmc.ncbi.nlm.nih.gov/articles/PMC10733979/

16. Devitt G, et al. Conformational fingerprinting of tau variants and strains by Raman spectroscopy. https://pmc.ncbi.nlm.nih.gov/articles/PMC8330415/

17. Apetri MM, et al. Marker-free imaging of alpha-Synuclein aggregates in a rat model of Parkinson's disease using Raman microspectroscopy. https://pmc.ncbi.nlm.nih.gov/articles/PMC8461246/

18. León-Bejarano F, et al. Raman Spectroscopy Study of Skin Biopsies from Patients with Parkinson's Disease: Trends in Alpha-Synuclein Aggregation from the Amide I Region. Applied Spectroscopy. 2022. https://journals.sagepub.com/doi/abs/10.1177/00037028221101634

19. Ran C, Xu X, Raymond SB, et al. Design, synthesis, and testing of difluoroboron-derivatized curcumins as near-infrared probes for in vivo detection of amyloid-beta deposits. J Am Chem Soc. 2009;131(42):15257-15261. https://pmc.ncbi.nlm.nih.gov/articles/PMC2784241/

20. Zhang X, Tian Y, Li Z, et al. Design and synthesis of curcumin analogues for in vivo fluorescence imaging and inhibiting copper-induced cross-linking of amyloid beta species in Alzheimer's disease. J Am Chem Soc. 2013. https://pmc.ncbi.nlm.nih.gov/articles/PMC3927838/

21. Zhang X, Tian Y, Yuan P, et al. Near-infrared fluorescence molecular imaging of amyloid beta species and monitoring therapy in animal models of Alzheimer's disease. PNAS. 2015. https://www.pnas.org/doi/10.1073/pnas.1505420112

22. Klunk WE, Bacskai BJ, Mathis CA, et al. Imaging Abeta plaques in living transgenic mice with multiphoton microscopy and methoxy-X04, a systemically administered Congo red derivative. J Neuropathol Exp Neurol. 2002;61(9):797-805.

23. Near-Infrared Bodipy-Based Molecular Rotors for beta-Amyloid Imaging In Vivo. https://pmc.ncbi.nlm.nih.gov/articles/PMC11468675/

24. A Novel Near-Infrared Fluorescence Probe THK-565 Enables In Vivo Detection of Amyloid Deposits in Alzheimer's Disease Mouse Model. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10728248/

25. Knöpfel T, Song C. Genetically Encoded Voltage Indicators: Opportunities and Challenges. J Neurosci. 2016;36(39):9977-9989. https://www.jneurosci.org/content/36/39/9977

26. Bright and sensitive red voltage indicators for imaging action potentials in brain slices and pancreatic islets. Sci Adv. https://www.science.org/doi/10.1126/sciadv.adi4208

27. Acerbi F, Restelli F, Broggi M, et al. Indocyanine-Green for Fluorescence-Guided Surgery of Brain Tumors. Front Surg. 2019;6:11. https://www.frontiersin.org/journals/surgery/articles/10.3389/fsurg.2019.00011/full

28. Fluorescence-Guided Surgery: A Review on Timing and Use in Brain Tumor Surgery. Front Neurol. 2021;12:682151. https://www.frontiersin.org/journals/neurology/articles/10.3389/fneur.2021.682151/full

29. Matousek P, Stone N. Spatially offset Raman spectroscopy for biomedical applications. https://pmc.ncbi.nlm.nih.gov/articles/PMC8323810/

30. Moody AS, Sharma B. Surface Enhanced Spatially Offset Raman Spectroscopy Detection of Neurochemicals Through the Skull. Anal Chem. 2017;89(11):5688-5692. https://pubs.acs.org/doi/full/10.1021/acs.analchem.7b00985

31. Moody AS, Sharma B. Surface-enhanced spatially-offset Raman spectroscopy (SESORS) for detection of neurochemicals through the skull at physiologically relevant concentrations. https://pubmed.ncbi.nlm.nih.gov/31971169/

32. In vivo imaging using surface enhanced spatially offset Raman spectroscopy (SESORS): balancing sampling frequency to improve overall image acquisition. NPJ Imaging. 2024. https://www.nature.com/articles/s44303-024-00011-9

33. Liu YH, Xu Y, Liao LD, Chan KC, Thakor NV. A handheld real-time photoacoustic imaging system for animal neurological disease models: from simulation to realization. Sensors. iThera Medical MSOT references via https://onlinelibrary.wiley.com/doi/full/10.1002/VIW.20240023

34. Photoacoustic computed tomography for functional human brain imaging [Invited]. Biomed Opt Express. 2021. https://pmc.ncbi.nlm.nih.gov/articles/PMC8367226/

35. Zhang Y, Na S, Sastry K, et al. Transcranial photoacoustic computed tomography of human brain function. arXiv:2206.00248 (2022). https://arxiv.org/abs/2206.00248

36. Whole brain optoacoustic tomography reveals strain-specific regional beta-amyloid densities in Alzheimer's disease amyloidosis models. https://www.academia.edu/144850847/

37. Hu S, Yan P, Maslov K, Lee JM, Wang LV. Intravital imaging of amyloid plaques in a transgenic mouse model using optical-resolution photoacoustic microscopy. Opt Lett. 2009;34(24):3899-3901. https://pmc.ncbi.nlm.nih.gov/articles/PMC2854007/

38. Label-free visualization of amyloid plaques in Alzheimer's disease with polarization-sensitive photoacoustic Mueller matrix tomography. arXiv:2207.13271. https://arxiv.org/pdf/2207.13271

39. Functional brain mapping using whole-head very high-density diffuse optical tomography. Imaging Neuroscience. https://direct.mit.edu/imag/article/doi/10.1162/IMAG.a.54/131219/

40. Continuous Wave-Diffuse Optical Tomography (CW-DOT) in Human Brain Mapping: A Review. Sensors. 2025;25(7):2040. https://www.mdpi.com/1424-8220/25/7/2040

41. Validation of a Combined Frequency-Domain and Broadband Diffuse Optical Spectroscopy System for Hyperspectral Estimation of Optical Properties. OPTICA Biomedical Optics Congress 2024. https://opg.optica.org/abstract.cfm?uri=BRAIN-2024-JS4A.28

42. Le TT, Yue S, Cheng JX. Shedding new light on lipid biology with coherent anti-Stokes Raman scattering microscopy. J Lipid Res. 2010;51:3091-3102. https://www.jlr.org/article/S0022-2275(20)40943-5/fulltext

43. Ji M, Orringer DA, Freudiger CW, et al. Rapid, label-free detection of brain tumors with stimulated Raman scattering microscopy. Sci Transl Med. 2013;5(201):201ra119. https://pmc.ncbi.nlm.nih.gov/articles/PMC3806096/

44. Ruan H, Brake J, Robinson JE, et al. Deep tissue optical focusing and optogenetic modulation with time-reversed ultrasonically encoded light. Sci Adv. 2017. https://www.science.org/doi/10.1126/sciadv.aao5520

45. Camera-based ultrasound-modulated optical tomography with isometric resolution. Appl Phys Lett. 2024. https://pubs.aip.org/aip/apl/article/124/25/253701/

46. Streich L, Boffi JC, Wang L, et al. Through-skull brain imaging in vivo at visible wavelengths via dimensionality reduction adaptive-optical microscopy. https://pubmed.ncbi.nlm.nih.gov/35895824/

47. Qin Z, et al. Adaptive optics three-photon microscopy with analog lock-in phase detection (ALPHA-FSS). Nat Biotechnol. 2022. https://www.nature.com/articles/s41587-022-01343-w

48. Can infrared light really be doing what we claim it is doing? Infrared light penetration principles, practices, and limitations. Front Neurol. 2024;15:1398894. https://www.frontiersin.org/journals/neurology/articles/10.3389/fneur.2024.1398894/full

49. Hong G, Antaris AL, Dai H. Near-infrared fluorophores for biomedical imaging. Nat Biomed Eng. 2017;1:0010. Through-skull fluorescence imaging of the brain in a new near-infrared window. Nat Photonics 2014;8:723-730. https://www.nature.com/articles/nphoton.2014.166

50. Hanlon EB, Itzkan I, Dasari RR, et al. NEAR-INFRARED SPECTROSCOPY IN VIVO DISTINGUISHES AMYLOID DEPOSITION IN SUBJECTS WITH ALZHEIMER'S DISEASE. https://pmc.ncbi.nlm.nih.gov/articles/PMC10738425/

51. Openwater. Press release archive and clinical pages. https://www.openwater.health/clinical and https://www.openwater.health/pressrelease

52. UK Researchers to Study Stroke Recovery with Openwater's Open-Motion Device. DAIC. https://www.dicardiology.com/content/uk-researchers-study-stroke-recovery-openwaters-open-motion-device

53. Openwater LIFU technology adoption at MIT for consciousness and neurological care. NeurologyLive. https://www.neurologylive.com/view/openwater-lifu-technology-at-mit-new-era-consciousness-neurological-care

54. Advancing Brain Research through Surface-Enhanced Raman Spectroscopy (SERS): Current Applications and Future Prospects. Biosensors. 2024;14(1):33. https://www.mdpi.com/2079-6374/14/1/33

55. Klonoff DC. Noninvasive Glucose Monitoring: In God We Trust, All Others Bring Data. J Diabetes Sci Technol. https://pmc.ncbi.nlm.nih.gov/articles/PMC8655290/

56. Rockley Photonics. Rockley Photonics Advances Non-Invasive Blood Glucose Monitoring. 2023. https://rockleyphotonics.com/2023/09/26/rockley-photonics-advances-non-invasive-blood-glucose-monitoring/

57. Rockley Photonics Completes Financial Restructure, Emerges from Chapter 11. Business Wire. 2023. https://www.businesswire.com/news/home/20230605005121/en/Rockley-Photonics-Completes-Financial-Restructure-Emerges-from-Chapter-11

58. DiaMonTech. Clinical validation of noninvasive blood glucose measurements by mid-infrared spectroscopy. Commun Med. 2025. https://www.nature.com/articles/s43856-025-01241-7

59. Workshop on Noninvasive Glucose Monitoring 2024. J Diabetes Sci Technol. 2025. https://journals.sagepub.com/doi/full/10.1177/19322968251329371

60. Know Labs. Non-Invasive Glucose Monitor Achieves 11.1% MARD in Latest Clinical Research Study. Business Wire. 2024. https://www.businesswire.com/news/home/20240306519289/en/

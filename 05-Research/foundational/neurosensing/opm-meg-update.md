# OPM-MEG and the Wearable Magnetoencephalography Landscape: A 2024 to 2026 Technology Deep-Dive

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: researchers, stakeholders
> **Tags**: `research`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)

Prepared for: Cytognosis Foundation, NSF X-Labs Phase 0 and ARPA-H PHO/HSF work
Author context: Herve Marie-Nelly / Cytognosis
Date: 25 May 2026
Scope: Optically pumped magnetometer magnetoencephalography (OPM-MEG) as a noninvasive brain-sensing modality, benchmarked against cryogenic SQUID-MEG and EEG, with an honest read on whether it can ever become a free-living psychiatric wearable and how it compares to functional near-infrared spectroscopy (fNIRS) for that role. Research-only versus clinical status is flagged throughout.

A note on framing: this document treats OPM-MEG as a clinical-grade reference and validation modality for the Cytoscope program, not as the wearable substrate itself. The reasons are spelled out in the final section. Everything below is consistent with the comparative review (wearables-comparative.md) and the EEG/MEG biotypes review (eeg-meg-biotypes.md); this file goes deeper on physics, vendors, prices, and the wearability question.

---

## 1. How OPM-MEG works

### 1.1 The signal being measured

All MEG measures the tiny magnetic field produced outside the head by intracellular (primarily dendritic) currents flowing in synchronously active cortical pyramidal neurons. The signal is small. A typical evoked cortical response produces a field on the order of tens to hundreds of femtotesla (fT) at the scalp, against an ambient (unshielded) geomagnetic field on the order of 50 microtesla, a difference of roughly nine orders of magnitude. Earth's field and urban magnetic noise are therefore the central engineering problem of all MEG. The key advantage of magnetic over electric (EEG) measurement is that magnetic permeability is essentially uniform across scalp, skull, and brain, so magnetic fields are not smeared by the low-conductivity skull the way scalp voltages are. This gives MEG cleaner forward models and better spatial reconstruction than EEG (Boto et al. 2018, doi:10.1038/nature26147; Brookes et al. 2022, doi:10.1016/j.tins.2022.05.008).

### 1.2 Alkali-vapor magnetometers and the SERF (zero-field) regime

A modern OPM is a sensor about the size of a sugar cube or a few stacked Lego bricks. Inside is a sealed glass cell containing a vapor of alkali atoms, most commonly rubidium-87 (87-Rb), heated to roughly 150 degrees Celsius so enough atoms enter the vapor phase. A circularly polarized laser tuned to an atomic transition "optically pumps" the atoms into a spin-polarized state. In the presence of a magnetic field, the atomic spins precess, which changes how much pump light the vapor transmits. A photodetector reads that transmitted light, so the optical signal becomes a direct readout of the local magnetic field.

The crucial trick is the spin-exchange relaxation-free (SERF) regime. At high atomic density and very low ambient field (below roughly 1 to 10 nanotesla), spin-exchange collisions that would normally destroy spin coherence stop limiting sensitivity, and the magnetometer becomes extraordinarily sensitive, into the few-fT/root-Hz range. The catch is built into the name: SERF only works in a near-zero field. That single physical requirement is why OPM-MEG still needs magnetic shielding, and it propagates through every deployment decision below. The sensor must be held within a few nT of zero field, both the static background and any field that changes as the head moves.

Helium-4 (4-He) OPMs are an important alternative that relaxes some of these constraints (Section 7). They use a metastable helium vapor sustained by a radio-frequency discharge rather than a heated alkali cell, so they run at room temperature, tolerate a far larger dynamic range, and reach DC-to-2-kHz bandwidth, at the cost of a higher intrinsic noise floor (Labyt et al. 2023, doi:10.3390/s23052801).

### 1.3 OPM-MEG versus SQUID-MEG versus EEG

Conventional MEG uses superconducting quantum interference devices (SQUIDs) immersed in liquid helium at 4 Kelvin inside a fixed dewar. The dewar wall plus the cryogenic gap forces the sensors to sit 2 to 4 cm from the scalp, and the head must stay still inside a rigid one-size helmet. OPMs replace both the SQUID and the cryogenics with a room-temperature (or near-room-temperature) sensor that can sit directly on the scalp, 6 to 10 mm from the cortex versus 25 to 40 mm for SQUIDs. Because the field of a current dipole falls steeply with distance, halving the distance roughly quadruples to quintuples the signal amplitude and sharpens the spatial pattern. The sensors mount in a lightweight 3D-printed or fabric helmet that moves with the head, so the subject can move, turn, and even walk, provided the ambient field is held near zero.

| Property | EEG | SQUID-MEG | OPM-MEG |
|---|---|---|---|
| Physical quantity | Scalp voltage | Magnetic field (SQUID at 4 K) | Magnetic field (atomic vapor) |
| Sensor-to-cortex distance | 0 (on scalp) but skull-blurred | 25 to 40 mm | 6 to 10 mm |
| Skull/scalp distortion | Severe (volume conduction) | None | None |
| Cryogenics | None | Liquid helium, ongoing refills | None |
| Head movement | Tolerated, but motion artifact | Restricted (fixed dewar) | Tolerated inside shielding |
| Helmet fit | Caps scale to head | One rigid size (poor for children) | Reconfigurable, scales to child or adult |
| Noise floor | 0.4 to 2.5 uV/root-Hz | 2 to 3 fT/root-Hz | 7 to 30 fT/root-Hz |
| Shielding | None | Magnetically shielded room (MSR) | MSR or lightly shielded room plus active nulling |
| Bandwidth | No intrinsic limit | No intrinsic limit | Below ~130 Hz (alkali); DC to 2 kHz (helium) |
| Dynamic range | Not limited | About +/- 20 nT | +/- 5 nT (alkali open loop) up to +/- 150 to 200 nT |

Noise floor, dynamic range, and bandwidth figures are drawn from the Uhlhaas et al. comparison table (Uhlhaas et al. 2024, doi:10.1038/s41398-024-03047-y) and helium-OPM specifications (Labyt et al. 2023, doi:10.3390/s23052801). The honest summary: a single SQUID is still a quieter sensor than a single OPM, but the OPM's proximity to the cortex more than compensates for evoked-field SNR, while EEG remains the cheapest and most deployable but the spatially blurriest of the three.

---

## 2. Spatial resolution

### 2.1 Typical and best achievable

Spatial resolution in MEG has two meanings: how accurately a single source can be localized, and how well two nearby sources can be separated. OPM-MEG outperforms EEG on both and meets or exceeds SQUID-MEG for superficial cortical sources.

- Phantom (best case): A 2025 triaxial whole-head system reported dipole localization accuracy better than 1 mm on a current phantom (Rea, Boto, Brookes et al., toward a 384-channel system, arXiv:2509.03107, 2025). Phantom numbers are an upper bound; they exclude brain noise and co-registration error.
- In vivo cortical: Reported localization for sensorimotor, visual, and auditory evoked fields lands at roughly 4 to 8 mm with whole-head arrays of 64 to 128 sensors (Brookes et al. 2022, doi:10.1016/j.tins.2022.05.008). Source-space connectivity work has quoted 2 to 5 mm at best for well-constrained tangential cortical sources (eeg-meg-biotypes.md, Section 6.3).
- Single-region demonstrations: An 8-sensor array over visual cortex localized grating-induced gamma comparably to a 306-channel SQUID system, and a single OPM moved across 13 positions matched a 174-sensor SQUID system for the somatosensory N20 (Uhlhaas et al. 2024, doi:10.1038/s41398-024-03047-y, citing Boto and Tierney work).

### 2.2 What limits spatial resolution

The fundamental limit is the MEG inverse problem: infinitely many source configurations can produce the same external field, so localization always depends on a forward model plus priors (beamformers, minimum-norm, dipole fits). Practical limits compound this: the number and geometry of channels, sensor-to-scalp coregistration error (an OPM that is 5 mm off its assumed position injects localization error), helmet fit, and co-registration of sensor positions to the subject's anatomical MRI. Triaxial sensors (Section 7) help by packing three independent field-axis measurements into each scalp location, which raises channel density and improves beamformer performance without adding scalp footprint.

### 2.3 Source-localization accuracy in clinical context

For epilepsy (RESEARCH-led, moving toward CLINICAL), multi-site work shows OPM-MEG localizes interictal epileptiform discharges with accuracy comparable to SQUID-MEG, and the movement tolerance is decisive for children who cannot hold still in a fixed dewar (eeg-meg-biotypes.md, Section 7.2; wearable OPM-MEG epilepsy review PMC9805039, 2022). No OPM-MEG system holds clinical regulatory clearance as of May 2026; epilepsy localization is the closest application to clinical maturity.

---

## 3. Temporal resolution

OPM-MEG, like EEG and SQUID-MEG, measures electrophysiology directly, so its temporal resolution is set by the sampling rate, not by any biological lag. This is its defining advantage over every hemodynamic modality (fMRI, fNIRS).

- Typical: sub-millisecond, with sampling commonly at 1,000 to 2,000 Hz. This resolves event-related fields, oscillatory dynamics, and cross-frequency coupling on the timescale of neuronal communication.
- Sensor bandwidth: the practical ceiling for alkali OPMs is roughly 100 to 150 Hz, which clips high-gamma and high-frequency oscillations (relevant to epilepsy ripples and to some psychiatric gamma markers).
- Best (helium and next-gen): helium-4 OPMs reach DC to 2 kHz bandwidth, and 2-kHz-bandwidth alkali sensors are in development, restoring access to high-gamma and pathological high-frequency oscillations (Labyt et al. 2023, doi:10.3390/s23052801; Uhlhaas et al. 2024, doi:10.1038/s41398-024-03047-y).

For the psychiatric biotypes that need millisecond timing (40 Hz ASSR, MMN, P300, microstates; see eeg-meg-biotypes.md), OPM-MEG is fully capable, and the helium variant removes the bandwidth concern for 40 Hz and above.

---

## 4. Depth sensitivity

### 4.1 The physics of depth

Magnetic field from a current dipole falls off with distance faster than the electric potential does (roughly as 1/r-squared to 1/r-cubed for the relevant near-field geometry). A source in the hippocampus or thalamus is several centimeters from any scalp sensor, so its external field is far weaker than a cortical source's and competes with both sensor noise and the much larger fields of overlying cortex. MEG is also blind to perfectly radial sources in a spherical conductor and weakest for deep sources whose fields are spread diffusely. These are physical constraints, not engineering ones, and they apply to OPM-MEG and SQUID-MEG alike.

### 4.2 Can OPM-MEG read subcortical and deep sources?

This is the most over-claimed area in the field, so the framing matters. OPM-MEG improves the deep-source situation relative to SQUID-MEG for one concrete reason: putting sensors on the scalp raises the deep-source field amplitude, and putting sensors in unconventional places (the mouth, the back of the neck) shortens the path to specific deep structures. But routine, single-subject, reliable subcortical localization is not established.

| Deep structure | OPM-MEG evidence (2019 to 2025) | Status |
|---|---|---|
| Hippocampus | Tierney et al. placed OPMs in the mouth plus over the temporal lobe to record hippocampal activity ("mouth-MEG"), and Barry et al. imaged the hippocampus with OPMs (Tierney et al. 2021, doi:10.1016/j.neuroimage.2020.117443; Barry et al. 2019, doi:10.1016/j.neuroimage.2019.04.013) | RESEARCH, single-lab, special sensor placement |
| Cerebellum | Lin et al. measured cerebellar MEG by placing OPMs at the lower back of the head and neck (Lin et al. 2019, doi:10.1113/JP277947) | RESEARCH, single-lab |
| Thalamus / subthalamic nucleus | Subcortical oscillatory connectivity demonstrated mainly with invasive recordings (Litvak, van Wijk); OPM-MEG thalamic localization is simulation-and-inference, not direct single-subject demonstration | UNPROVEN noninvasively |
| Brainstem | No credible noninvasive OPM-MEG demonstration | NOT DEMONSTRATED |

The Uhlhaas review's own comparison table classifies "localization of deep sources" for OPM-MEG as "under investigation," not "yes" (Uhlhaas et al. 2024, doi:10.1038/s41398-024-03047-y). A 2025 simulation modeled laminar specificity but did not demonstrate it in vivo (Imaging Neuroscience 2025, doi:10.1162/imag_a_00538). The honest position for a proposal: OPM-MEG extends the depth envelope at the margins and gives the best noninvasive shot at hippocampus and cerebellum, but anyone claiming routine thalamic or brainstem readout from a scalp helmet is ahead of the evidence.

### 4.3 What limits depth in practice

Three factors stack: signal amplitude falling with distance; the ambiguity of the inverse problem getting worse for deep sources (small changes in data produce large changes in inferred deep-source location); and cortical sources swamping deep ones. Larger channel counts, triaxial sensors, and reference-sensor noise suppression all help marginally. None of them defeat the 1/r-cubed physics.

---

## 5. Tissue and physics constraints: the shielding reality

### 5.1 Why shielding is unavoidable for SERF OPMs

The SERF regime only exists near zero field. The geomagnetic field is roughly 50,000 nT, urban magnetic noise from elevators, vehicles, and power lines adds large slow-varying components, and an alkali OPM in open-loop mode saturates beyond about +/- 5 nT. So the ambient field must be suppressed by four to five orders of magnitude before the sensor will function at all. This is done in layers.

### 5.2 The shielding stack

| Layer | What it does | Typical cost (RESEARCH) |
|---|---|---|
| Magnetically shielded room (MSR) | Mu-metal plus aluminum walls reduce static field and AC noise by 100x to 1000x | $200k to $1M depending on layers and size |
| Active shielding / matrix coils | Coils inside the MSR null residual field and, critically, cancel the field change as the head moves, enabling free movement | Adds tens to hundreds of thousands of dollars |
| Field nulling at the sensor (on-board coils) | Each OPM has internal coils to zero the field at the cell | Built into the sensor |

The MSR is the dominant deployment barrier. It is heavy, fixed, and expensive, and it is the single reason OPM-MEG is not a take-home device.

### 5.3 The path toward lighter shielding (and the lack of a path to none)

Real 2024 to 2026 progress has been on making shielding lighter and cheaper, not on eliminating it:

- Biplanar nulling coils on printed circuit boards (2025) replaced hand-wound copper with manufacturable PCBs, reduced the largest background-field component from 21 nT to 2 nT, and let OPMs record somatosensory evoked fields in a lightly shielded room (background varying 6.5 to 108 nT) comparable to a 3-layer MSR. The hardware and software were released open-source as opmcoils (Sensors 2025, doi:10.3390/s25092759; bioRxiv 2025.02.19.638883).
- Helium-4 OPMs tolerate +/- 200 nT, which can enable recordings with reduced or simpler nulling and better movement tolerance (Labyt et al. 2023, doi:10.3390/s23052801).
- Mobile and lightweight shielded enclosures are being developed, including a UK Ministry of Defence program for a mobile quantum brain scanner to measure blast effects, but these are reduced shielding, not no shielding (gov.uk, 2024).

There is no demonstrated route to shielding-free SERF OPM-MEG in an ordinary room. The physics of the SERF regime forbids it. Helium OPMs and clever nulling shrink the shield; they do not remove it. Any roadmap that promises a shielding-free wearable MEG should be treated as aspirational.

### 5.4 Movement tolerance

Inside an MSR with matrix-coil active shielding, subjects have performed naturalistic tasks: walking, head-turning, ball games, and two-person hyperscanning (Holmes et al. 2023, doi:10.1162/imag_a_00006). This is the headline advantage over fixed SQUID systems. But the freedom ends at the MSR wall.

---

## 6. Adjustability and array reconfiguration

OPM-MEG's modular, on-scalp design is genuinely flexible, and this is one of its strongest practical features.

- On-scalp placement: each sensor sits directly on the scalp in a helmet slot, so coverage can be concentrated where the science needs it.
- Child versus adult: the same sensors fit child-sized helmets, including infants and toddlers, the populations conventional MEG cannot serve. Pediatric whole-head arrays for early human life have been demonstrated (Imaging Neuroscience 2025, doi:10.1162/imag_a_00489), and the Hospital for Sick Children (Toronto) runs pediatric autism and concussion research on Cerca/QuSpin systems (eeg-meg-biotypes.md, Section 7.1).
- Whole-head versus targeted arrays: a small targeted array (8 sensors over visual cortex, or sensors at the neck for cerebellum) can match a full SQUID system for a focal source, so studies can trade coverage for cost. Optimal sensor placement for a fixed channel budget is itself an active research topic (Imaging Neuroscience, doi:10.1162/IMAG.a.22, 2025).
- Reconfiguration: arrays are re-laid out between studies; the helmet, not the cryostat, defines geometry.

---

## 7. Most promising mature versus upcoming technology

### 7.1 Mature (deployable in research today)

- Rubidium SERF OPMs (QuSpin QZFM): the workhorse. Single-axis sensitivity 7 to 12 fT/root-Hz, dual-axis 10 to 15 fT/root-Hz (QuSpin QZFM Gen-3 specifications, quspin.com). The dominant sensor in whole-head research arrays of 32 to 128 modules.
- Whole-head Cerca/Nottingham systems built on QuSpin sensors, installed at roughly 20-plus sites globally (Cerca Magnetics, cercamagnetics.com).

### 7.2 Upcoming and recently demonstrated (2024 to 2026)

- Triaxial sensors: QuSpin's triaxial QZFM measures all three field components per location (sensitivity below 30 fT/root-Hz per axis in triax mode). Triaxial packing maximizes channel density per scalp area and improves source reconstruction and interference rejection (quspin.com, New Triaxial QZFM).
- Larger channel counts: a 384-channel system (128 triaxial sensors) was demonstrated in 2025, the first OPM-MEG with more channels than a typical SQUID system (about 300), with sub-1-mm phantom localization and improved in vivo gamma and movie-watching sensitivity (arXiv:2509.03107, 2025). For comparison, the historical Kernel Flux was a 432-magnetometer whole-head OP-MEG system (Pratt, Ledbetter et al., SPIE 2021, doi:10.1117/12.2581794).
- Helium-4 OPMs (cryogen-free, room-temperature, large bandwidth): Mag4Health's whole-head 4-He system uses 96 triaxial sensors (288 channels), measured noise around 30 fT/root-Hz per axis, +/- 200 nT dynamic range, DC-to-2-kHz bandwidth, distributed via Brainbox. Because helium needs no heating, there is no hot cell to insulate, the sensor can sit closer to the scalp, and there is no sensor-heating artifact pathway. A 2025 performance assessment compared a fully integrated whole-head helium system against cryogenic MEG (Frontiers in Medical Technology 2025, doi:10.3389/fmedt.2025.1548260; PMC12006120; mag4health.com).
- Miniaturized integrated electronics: shrinking the control electronics from rack-mounted boxes toward head-mounted units is what makes higher channel counts and true mobility feasible.

### 7.3 The realistic trajectory

The near-term frontier is more channels, triaxial sensing, and lighter shielding, not a take-home device. Helium OPMs are the most credible step toward simpler deployment because they cut the heating and dynamic-range constraints at once. Room-temperature and cryogen-free are already real (helium); shielding-free is not.

---

## 8. Known biases and noise sources

OPM-MEG carries a distinctive artifact profile, some shared with all MEG and some specific to atomic magnetometers.

| Noise / bias source | Mechanism | Mitigation |
|---|---|---|
| Ambient magnetic noise | Geomagnetic field plus urban interference dwarfs the brain signal | MSR, active matrix coils, reference sensors, signal-source separation |
| Movement artifact | As the helmet moves through any residual field gradient, each sensor sees a changing field | Matrix-coil field control inside the MSR; helium's larger dynamic range |
| Cross-talk | Adjacent OPMs' on-board nulling coils perturb each other's local field | Calibration matrices; triaxial sensors with internal cross-axis removal |
| Sensor calibration / gain errors | Gain and orientation errors per axis distort the forward model and localization | Per-sensor calibration; phantom validation; triaxial cross-axis correction |
| Sensor heating (alkali only) | The 150 C rubidium cell must be thermally isolated from the scalp; thermal drift can couple into the signal | Insulation and standoff (which increases sensor-to-scalp distance); eliminated in room-temperature helium OPMs |
| Coregistration error | Uncertainty in sensor position relative to the head and MRI | Optical scanning, helmet digitization, careful pipelines |
| Cardiac (MCG) interference | The heart's magnetic field is far larger than the brain's and reaches the head sensors | Reference sensors, ICA, signal-space projection |
| Muscle / ocular | Neck, jaw, and eye activity produce magnetic and movement artifacts | Artifact rejection; the Uhlhaas table still lists OPM artifacts as "under investigation" |
| Limited bandwidth and dynamic range (alkali) | Below ~130 Hz bandwidth, +/- 5 nT open-loop range clip high-frequency and large signals | Closed-loop operation (to ~+/- 150 nT), helium OPMs |

Two biases deserve emphasis for a psychiatric platform. First, the heating artifact is unique to alkali sensors and is one more reason helium OPMs are attractive. Second, the field's own perspective (Uhlhaas et al. 2024) lists OPM-MEG artifacts and deep-source localization as "under investigation," which is an honest flag that the noise characterization is less mature than for decades-old SQUID-MEG.

---

## 9. Honest comparison to fNIRS for a wearable psychiatric platform

This is the decision-relevant section for Cytognosis. The question is not "which modality is better science," it is "which can be a wearable, free-living, longitudinal mental-health sensor," and there OPM-MEG and fNIRS sit on opposite sides of a hard line.

### 9.1 Why Kernel killed Flux

Kernel built Flux, a 432-magnetometer whole-head OP-MEG system, then discontinued it and refocused the company on Flow, a time-domain fNIRS platform (wearables-comparative.md, Section 3; Pratt et al., SPIE 2021, doi:10.1117/12.2581794). The publicly stated reasons map exactly onto the constraints above:

1. The shielded room is a deployment killer. Kernel's goal was a widely accessible brain-assessment tool, and the MSR requirement was incompatible with that.
2. Most target use was superficial cortex, where fNIRS gives competitive spatial information without a shielded room.
3. fNIRS uses standard optoelectronic manufacturing that scales; OPM-MEG manufacturing does not scale the same way.

Kernel's pivot is the single most informative datapoint in this whole analysis. A well-capitalized company that built one of the largest OPM-MEG arrays in the world concluded that the road to a consumer brain wearable runs through optics, not magnetometry.

### 9.2 Head-to-head for the wearable use case

| Criterion | OPM-MEG | fNIRS / DOT |
|---|---|---|
| Signal | Direct neuronal magnetic field | Hemodynamic (HbO2/HbR), plus CCO, blood flow |
| Temporal resolution | Sub-ms (its great strength) | ~0.5 to 1 Hz biological (hemodynamic lag) |
| Spatial resolution | 4 to 8 mm cortical; sub-1 mm phantom | 13 to 16 mm HD-DOT; ~6.5 mm prototypes |
| Molecular specificity | None (electrophysiology only) | Yes (HbO2, HbR, CCO, water, lipid) |
| Free-living wearable | No: requires MSR plus active shielding | Yes: fabric cap, normal rooms, outdoors |
| Setup | 10 to 20 min in an MSR | 5 to 15 min anywhere |
| System cost | $1M to $3M plus MSR | $0.3k (consumer) to $1M (TD research) |
| Consumer products today | None | Yes (Mendi, Brite) |
| Manufacturing scalability | Low | High (standard optoelectronics) |
| Path to take-home | None for SERF; helium shrinks but does not remove shielding | Already there |

### 9.3 Can OPM-MEG ever be a consumer wearable?

Short answer: not as a free-living, anywhere device, and not because of cost or channel count, but because of physics. The SERF regime requires near-zero field, and there is no demonstrated way to deliver that in an arbitrary room. The credible 2024 to 2026 advances all reduce the shield (PCB nulling coils, helium dynamic range, mobile enclosures); none remove it. Even an optimistic helium-plus-lightweight-enclosure future yields a portable or transportable system, not a hat you wear to work. A "personal MSR" or wearable shield around the head is not on any credible near-term roadmap.

Where OPM-MEG does win, decisively, is millisecond electrophysiology with clean source localization and child-compatibility. Those are reference-grade capabilities. fNIRS cannot recover the 40 Hz ASSR, MMN, P300, or microstates that several psychiatric biotypes depend on, because hemodynamics is too slow (eeg-meg-biotypes.md, Section 12.1). So the two modalities are complements, not competitors, for the program.

### 9.4 Recommended role in the Cytognosis Cytoscope program

The role that survives honest scrutiny is the one already in the seed docs: OPM-MEG as a clinical-grade reference and validation modality at partner sites, used to ground-truth the millisecond electrophysiological biotypes (40 Hz ASSR, MMN, P300, microstates) that a wearable optical-plus-dry-EEG headset will attempt to recover in cheaper, deployable form. fNIRS-class spectroscopy is the wearable substrate; OPM-MEG is the bench reference that tells you whether the wearable is reading the right thing. Wearable dry EEG covers the fast-electrophysiology biotypes in the field, with OPM-MEG validating those recordings against a gold-standard magnetic measurement. This pairing avoids betting the platform on a modality whose own most-funded champion (Kernel) walked away from the wearable dream.

---

## 10. Vendor and price summary

All systems below are RESEARCH-only unless noted. No OPM-MEG system holds clinical regulatory clearance as of May 2026; Cerca states explicitly that its system has no medical or regulatory approvals in any jurisdiction and is pursuing UK and US clinical pathways with recently raised capital (cercamagnetics.com; Cerca 4.3M EUR raise, sci-tech-today.com 2025).

| Vendor / system | Type | Sensor / channels | Price (where findable) | Status |
|---|---|---|---|---|
| QuSpin (Boulder, US) | Sensor maker | Rb QZFM Gen-3, single/dual/triaxial; 7 to 30 fT/root-Hz | ~$5k to $10k per sensor; ~$6,890 avg per unit (2024 market est.) | RESEARCH |
| FieldLine (Boulder, US) | Sensor + systems | Rb OPM modules, HEDscan whole-head | Per-sensor in QuSpin range; system not publicly priced | RESEARCH |
| Mag4Health (Grenoble, FR) | Helium systems | 4-He, 96 triaxial sensors (288 ch), 30 fT/root-Hz, +/- 200 nT, DC to 2 kHz | System not publicly priced; sold via Brainbox | RESEARCH |
| Cerca Magnetics (Nottingham, UK) | System integrator | QuSpin-based whole-head 32 to 128 sensors | System ~$0.5M to $1.5M; whole package $1M to $3M with MSR | RESEARCH (pursuing clinical) |
| Twinleaf (US) | Sensor maker | OPM modules | Per-sensor range | RESEARCH |
| Sandia National Labs (US) | Sensor R&D | Microfabricated OPMs | Not commercial | RESEARCH |
| Kernel (Los Angeles, US) | Former OPM-MEG | Flux: 432 magnetometers (discontinued) | N/A, product retired | DISCONTINUED (pivoted to Flow fNIRS) |

Cost stack, typical whole-head research deployment:

- Per OPM sensor: roughly $5k to $10k (market average about $6,890 per unit in 2024).
- 64-sensor whole-head system: roughly $0.5M to $1.5M.
- Magnetically shielded room: $200k to $1M.
- Active shielding / matrix coils: adds tens to hundreds of thousands.
- Total turnkey system: roughly $1M to $3M, about an order of magnitude below cryogenic MEG (>$3M with high ongoing helium and maintenance costs), but far above EEG ($0.2k to $100k) or fNIRS ($0.3k to $1M).
- Per-subject cost after capital: negligible (no consumables, no cryogen).

---

## 11. Bottom line for the proposal

OPM-MEG in 2026 is a maturing, room-temperature (helium) or near-room-temperature (alkali), wearable-helmet electrophysiology technology that beats EEG on spatial resolution and meets SQUID-MEG on cortical SNR while being cheaper and child-friendly. Its temporal resolution is excellent (sub-ms; helium reaches 2 kHz). Its depth reach is improving at the margins (best noninvasive shot at hippocampus and cerebellum with special sensor placement) but is unproven for thalamus and brainstem. Its hard limit is the SERF zero-field requirement, which keeps it inside a shielded room and off the free-living wearable roadmap, exactly the wall Kernel hit. For Cytognosis it belongs as a clinical-grade reference and validation modality at partner sites, paired with fNIRS-class optics and wearable dry EEG as the deployable wearable substrate.

---

## References (this file)

1. Barry DN, Tierney TM, Holmes N, et al. Imaging the human hippocampus with optically-pumped magnetometers. NeuroImage. 2019;203:116192. doi:10.1016/j.neuroimage.2019.04.013
2. Boto E, Holmes N, Leggett J, et al. Moving magnetoencephalography towards real-world applications with a wearable system. Nature. 2018;555:657-661. doi:10.1038/nature26147
3. Brookes MJ, Leggett J, Rea M, et al. Magnetoencephalography with optically pumped magnetometers (OPM-MEG): the next generation of functional neuroimaging. Trends Neurosci. 2022;45(8):621-634. doi:10.1016/j.tins.2022.05.008
4. Cerca Magnetics. Cerca OPM-MEG System (research use; no regulatory approval). https://www.cercamagnetics.com/cerca-opm-meg
5. Cerca Magnetics secures 4.3M EUR for wearable brain imaging. Sci-Tech Today. 2025. https://www.sci-tech-today.com/news/cerca-magnetics-secures-4-3m/
6. Holmes N, Rea M, Hill RM, et al. Naturalistic hyperscanning with wearable magnetoencephalography. Imaging Neurosci. 2023. doi:10.1162/imag_a_00006
7. Labyt E, Corsi MC, Fourcault W, et al. A new generation of OPM for high dynamic and large bandwidth MEG: the 4He OPMs, first applications in healthy volunteers. Sensors. 2023;23(5):2801. doi:10.3390/s23052801
8. Lin CH, Tierney TM, Holmes N, Boto E, Leggett J, Bestmann S, et al. Using optically pumped magnetometers to measure magnetoencephalographic signals in the human cerebellum. J Physiol. 2019;597(16):4309-4324. doi:10.1113/JP277947
9. Mag4Health. Fully integrated whole-head helium OPM-MEG technology. https://www.mag4health.com/technology/
10. Whole-head helium OPM MEG: a performance assessment compared to cryogenic MEG. Front Med Technol. 2025. doi:10.3389/fmedt.2025.1548260 (PMC12006120)
11. Optimal configuration of on-scalp OPMs with fixed channel counts. Imaging Neurosci. 2025. doi:10.1162/IMAG.a.22 (PMC12320008)
12. Pratt EH, Ledbetter M, et al. Kernel Flux: a whole-head 432-magnetometer optically-pumped magnetoencephalography (OP-MEG) system for brain activity imaging during natural human experiences. Proc SPIE. 2021;11700:1170032. doi:10.1117/12.2581794
13. QuSpin. QZFM Gen-3 and Triaxial QZFM specifications. https://quspin.com/qzfm-gen-3/ ; https://quspin.com/new-triaxial-qzfm/
14. Rea M, Boto E, Brookes MJ, et al. Towards a 384-channel magnetoencephalography system based on optically pumped magnetometers. arXiv:2509.03107. 2025. (PMC12723407)
15. Biplanar nulling coil system for OPM-MEG using printed circuit boards (opmcoils). Sensors. 2025;25(9):2759. doi:10.3390/s25092759 (bioRxiv 2025.02.19.638883; PMC12074179)
16. Tierney TM, Levy A, Barry DN, Meyer SS, Shigihara Y, Everatt M, et al. Mouth magnetoencephalography: a unique perspective on the human hippocampus. NeuroImage. 2021;225:117443. doi:10.1016/j.neuroimage.2020.117443
17. Uhlhaas PJ, et al. Applications of OPM-MEG for translational neuroscience: a perspective. Transl Psychiatry. 2024;14:341. doi:10.1038/s41398-024-03047-y (PMC11344782)
18. Wearable OPM-MEG: a changing landscape for epilepsy. 2022. PMC9805039
19. World's first mobile quantum brain scanner being developed to measure blast effects on troops. GOV.UK. 2024. https://www.gov.uk/government/news/worlds-first-mobile-quantum-brain-scanner-being-developed-to-measure-blast-effects-on-troops
20. Pediatric whole-head OPM-MEG array for early human life. Imaging Neurosci. 2025. doi:10.1162/imag_a_00489
21. OPM-MEG laminar simulation. Imaging Neurosci. 2025. doi:10.1162/imag_a_00538

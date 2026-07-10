# Cross-Modality Comparison: Brain Sensing, Molecular Imaging, and Neuromodulation

> One table per question, across every modality in the four tech deep-dives. Numbers are best-achievable unless marked "routine". Sources: `fnirs-optical-update.md`, `opm-meg-update.md`, `molecular-imaging-update.md`, `neuromodulation-update.md`, plus `wearables-comparative.md`. Confidence and research-vs-clinical status are flagged where they matter.

## How to read this

Two physical truths govern everything below.

First, for sensing there is a **sensitivity-versus-localization tradeoff**: the modalities that detect molecules at the lowest concentration (PET, at picomolar) have coarse spatial resolution (millimeters) and need radiation, while the modalities that are wearable and continuous (fNIRS, EEG) read only indirect or surface signals. No single modality is sensitive, high-resolution, deep, and wearable at once.

Second, for both sensing and modulation, **depth costs focality**. Reaching deep structures noninvasively (tTIS, focused ultrasound, OPM with special placement) is hard, and the deeper you go the harder it is to stay focal or to localize the source.

---

## Table 1: Brain SENSING modalities

| Modality | Spatial resolution | Temporal resolution | Max noninvasive depth | What it measures | Wearable? | Cost (system) | Status |
|---|---|---|---|---|---|---|---|
| **EEG** | 5 to 10 mm at scalp (smeared; poor without source modeling) | sub-ms (excellent) | cortical surface only | electrical population activity | Yes (mature) | $0.3k consumer to $100k research | Both |
| **fNIRS (CW)** | 20 to 30 mm routine | ~1 Hz useful (hemodynamic) | 1.5 to 2.5 cm | hemoglobin (HbO2/HbR) | Yes | $40k to $200k | Mostly research |
| **fNIRS (TD) / HD-DOT** | 13 to 16 mm routine; 6 to 8 mm best (2025 UHD) | ~0.5 to 1 Hz useful | 3 to 4 cm (the hard wall) | HbO2, HbR, + cytochrome-c-oxidase (broadband) | Yes | $50k to $250k | Research |
| **DCS / SCOS / iDWS** | ~cm | ~Hz | 4 to 4.5 cm (blood flow, 1064 nm) | cerebral blood flow | Yes (emerging) | research builds | Research |
| **OPM-MEG** | 4 to 8 mm cortical; 2 to 5 mm well-constrained | sub-ms (excellent) | cortex routine; hippocampus/cerebellum single-lab; thalamus unproven | magnetic fields from neural currents | No (needs shielded room) | $0.5M to $3M incl. room | Research |
| **fMRI (BOLD)** | 1 to 3 mm (sub-mm at 7T) | ~1 to 2 s | whole brain | blood-oxygen hemodynamics | No (fixed scanner) | $1M to $3M+ scanner | Clinical + research |
| **functional ultrasound (fUS)** | ~100 to 300 microns | ~ms to sub-s | needs thin/absent skull (intraop, infant) | cerebral blood volume | No (transcranial limited) | research | Research |

Key limits. EEG and fNIRS are surface-only because of physics (volume conduction for EEG; photon attenuation through skull for fNIRS). OPM-MEG can in principle reach deeper than EEG/fNIRS but the field falls off with the cube of distance and the inverse problem makes deep-source localization unreliable. fMRI is the spatial gold standard but is immobile, expensive, and not longitudinal at scale.

---

## Table 2: Brain MOLECULAR imaging modalities

| Modality | Spatial resolution | Detection limit (concentration) | Targeted vs whole-brain | What it measures | Radiation? | Cost / access | Status |
|---|---|---|---|---|---|---|---|
| **MRS (1H, 3T)** | 8 cm3 voxel (large) | ~1 mM (floor) | both: single-voxel zoom or MRSI map | NAA, glutamate/Glx, GABA, glutathione, lactate, myo-inositol | No | uses MRI scanner | Clinical + research |
| **MRS (7T)** | ~1 cm3 voxel | ~1 mM (floor unchanged; better separation) | both | more metabolites resolved | No | rare 7T sites | Research mostly |
| **PET** | 4 to 6 mm clinical; 1.6 to 2.5 mm (2024 NeuroEXPLORER) | picomolar to nanomolar (very sensitive) | whole-brain acquire, region-analyze | tracer-defined target (dopamine, amyloid, tau, TSPO, SV2A) | Yes (ionizing) | $3M+ scanner + cyclotron | Clinical |
| **SPECT** | 8 to 12 mm | nanomolar to micromolar | whole-brain acquire, region-analyze | tracer-defined (DaTscan dopamine transporter) | Yes (ionizing) | cheaper than PET | Clinical |
| **Hyperpolarized 13C MRI** | 7.5 to 15 mm | flux, not concentration; <2 min window | regional map | real-time metabolism (pyruvate to lactate) | No | very few sites | Research |
| **CEST / GluCEST** | 1 to 3 mm (MRI-grade) | still mM targets | map | glutamate, other exchangeable protons | No | research | Research |
| **Transcranial Raman / SORS / SESORS** | sub-mm (in principle) | probe-dependent | focal/offset | molecular vibrational signatures | No | research | Preclinical / early |
| **Photoacoustic (transcranial)** | sub-mm to mm | probe/chromophore-dependent | focal field | optical absorbers (hemoglobin; probes) | No | research | Preclinical / early |

Key limits. MRS is the only label-free, radiation-free molecular method, but its millimolar floor means it sees only abundant metabolites, not trace signaling molecules. PET is about nine orders of magnitude more sensitive (it can see picomolar tracer), which is why it dominates molecular neuroimaging, but it needs a radioactive tracer, a cyclotron, and accepts a radiation dose, and its resolution cannot resolve individual molecular aggregates (see Table 4).

---

## Table 3: NEUROMODULATION modalities

| Modality | Spatial focality | Temporal control | Max noninvasive depth | Node vs edge capability | Wearable / home? | Status |
|---|---|---|---|---|---|---|
| **TMS (figure-8)** | 1 to 3 cm patch | sub-ms pulse timing | 1.5 to 2.5 cm | node; edge via connectivity-seeded targeting (SAINT) | clinic only | FDA-cleared (MDD, OCD, smoking) |
| **Deep TMS (H-coil)** | broader, less focal | sub-ms | 3 to 4 cm | node (broad) | clinic only | FDA-cleared |
| **tDCS** | diffuse; HD ~1 to 2 cm | slow (minutes) | superficial cortex | weak node | Yes (home, Flow) | FDA-approved home (Flow, Dec 2025) |
| **tACS** | diffuse | oscillation-locked | superficial | strongest direct EDGE tool (phase/frequency coupling) | Yes (emerging) | Research |
| **tTIS (temporal interference)** | ~cm (variable) | envelope-tunable | deep: striatum, hippocampus, STN | node at depth; emerging edge | research | Research |
| **Focused ultrasound (LIFU)** | few mm3 (most focal) | ms | anywhere in brain | node (focality leader) | wearable arrays emerging | Research / early clinical |
| **tVNS** | peripheral nerve | breath/burst-paired | n/a (vagal afferents) | neuromodulatory, diffuse central effect | Yes (home) | FDA-cleared (migraine) |
| **DBS (invasive comparator)** | sub-mm | ms; adaptive | any depth | node, and adaptive closed-loop | implanted | FDA-approved (incl. aDBS Feb 2025) |

The node-vs-edge headline. Noninvasive **edge** (connection/subnetwork) modulation is demonstrated mechanistically by phase- and frequency-controlled tACS (the cleanest direct edge tool) and by multi-site TMS, but the only clinically validated edge strategy so far is connectivity-seeded single-node stimulation (Stanford SAINT targets the dlPFC voxel most anticorrelated with sgACC). Focused ultrasound is the focality and depth leader but is a node tool. The field cannot yet reliably steer a specific deep edge on demand.

---

## Table 4: The protein-aggregate resolution gap (why early molecular detection is hard)

| Aggregate (disease) | Species and size | What current imaging sees | The gap |
|---|---|---|---|
| **Amyloid-beta (AD)** | monomer ~1 nm; soluble oligomers ~5 to 10 nm; protofibrils; plaques tens of microns | amyloid PET (florbetapir, PiB) sees plaque BURDEN in a mm voxel | misses early soluble oligomers (smallest, scarcest, most toxic) |
| **Tau (AD, FTD)** | monomer; oligomers; paired helical filaments; neurofibrillary tangles ~microns | tau PET (flortaucipir, MK-6240, PI-2620) sees tangle burden | misses early/soluble tau |
| **Alpha-synuclein (PD, LBD, MSA)** | monomer; oligomers; Lewy-body fibrils | new PET tracers (18F-ACI-12589) detect high-density MSA, largely miss PD | density too low in PD for voxel-averaged signal |
| **Mutant huntingtin (HD)** | expanded polyQ aggregates | no validated clinical aggregate tracer; imaging tracks downstream atrophy/metabolism | direct aggregate imaging not clinical |
| **TDP-43 (ALS, FTD)** | cytoplasmic inclusions | no validated PET tracer in clinic | no probe |

The core gap. A PET voxel (mm) is three to six orders of magnitude larger than the aggregates (nm to tens of microns). PET therefore reports voxel-averaged binding (how much fibrillar target sits in a chunk of tissue), not individual aggregates. The earliest, most toxic species (small soluble oligomers) are the smallest, scarcest, and most dispersed, so they fail to raise the voxel-averaged signal. Early detection needs not nanometer resolution but oligomer-selective probes plus picomolar sensitivity. None is clinically validated yet, and fluid assays (plasma p-tau217, CSF seed amplification) currently outperform imaging for diffuse low-burden pathology by trading spatial localization for whole-brain integration.

---

## Table 5: The strategic summary (where each modality wins and loses)

| Modality | Wins on | Loses on | Right role in a platform |
|---|---|---|---|
| EEG | temporal resolution, cost, wearability | spatial resolution, depth | wearable companion channel (E/I via 1/f, ASSR, ERPs) |
| fNIRS / HD-DOT | wearability, continuous, multi-chromophore, cost | depth (3 to 4 cm wall), spatial vs fMRI | the deployable continuous backbone |
| OPM-MEG | spatial + temporal balance, some deep reach | needs shielded room, not wearable, cost | clinical-grade reference at partner sites |
| fMRI | spatial gold standard, whole-brain | immobile, expensive, not longitudinal | one-time anchor / ground truth |
| PET | molecular sensitivity (picomolar) | radiation, cost, mm resolution, not longitudinal | molecular ground truth, sparingly |
| MRS | label-free metabolites | mM floor, large voxel | molecular reference for abundant metabolites |
| TMS / tES / FUS / tVNS | actuation (treatment) | targeting needs offline imaging today | the intervention arm a sensor would steer |

The platform thesis in one line. A wearable, continuous, multi-chromophore optical sensor (fNIRS-class) plus a low-channel EEG layer covers the deployable middle of this space, and pairing it with a clinical-grade reference (OPM-MEG or fMRI) at validation sites and with a steerable intervention (TMS, tES, FUS) closes the sense-to-act loop that no current product spans.

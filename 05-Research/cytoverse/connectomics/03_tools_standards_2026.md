# fMRI tools, libraries, and standards (FAIR, open, community-curated)

Tools, libraries, and standards used for storage, preprocessing, harmonisation, and FAIR sharing of fMRI data, organised by the standard and ecosystem that owns each piece. Synthesised from the six reviewed papers (Taylor 2026 HCP, NeuroSTORM, Brain-Semantoks, SLIM-Brain, Omni-fMRI, BrainGFM) and from the curated catalogues at <https://nwb.org>, <https://bids.neuroimaging.io>, and <https://www.hedtags.org>.

The emphasis throughout is on the FAIR-compliant, openly licensed, community-curated stack that the field has converged on. Where the curated catalogues nominate a specific tool for a specific stage, that nomination is the default below.

---

## 1. The three first-class community standards

| Standard | Owner | Spec licence | What it covers |
|---|---|---|---|
| **BIDS** (Brain Imaging Data Structure) | bids-standard.github.io | CC0 | Filesystem layout, sidecar metadata, derivatives, BIDS-Apps, Stats Models for raw and derived MRI / EEG / MEG / iEEG / PET / behaviour |
| **HED** (Hierarchical Event Descriptors) | hedtags.org | CC0 | Controlled-vocabulary tagging of events in time-locked recordings; first-class BIDS extension via the events.tsv HED column |
| **NWB** (Neurodata Without Borders) | nwb.org | CC-BY 4.0 (spec) | HDF5- or Zarr-backed standard for neurophysiology (ephys, ophys, behaviour); complement to BIDS for non-BOLD modalities |

These three are designed to compose. BIDS is the dominant standard for MRI / EEG / MEG. NWB is the dominant standard for neurophysiology (intracranial ephys, two-photon ophys, behaviour). HED tags ride inside both, in BIDS via the events.tsv HED column and in NWB via the ndx-hed extension. All three specifications are openly licensed and openly governed.

---

## 2. The BIDS ecosystem

Top-level entry points:

* Home: <https://bids.neuroimaging.io/>
* Getting started: <https://bids.neuroimaging.io/getting_started/index.html>
* Standards portal: <https://bids.neuroimaging.io/standards/index.html>

### 2.1 Specifications

| Spec | URL | Licence |
|---|---|---|
| BIDS specification (rendered) | <https://bids.neuroimaging.io/standards/bids_specification/index.html> | CC0 |
| BIDS specification (read the docs) | <https://bids-specification.readthedocs.io/> | CC0 |
| BIDS Schema (machine-readable YAML, embedded in the spec) | <https://bids.neuroimaging.io/standards/schema/index.html> | CC0 |
| BIDS Stats Models | <https://bids.neuroimaging.io/standards/bids_stats_model/index.html> | CC0 |
| BIDS App Specification | <https://bids.neuroimaging.io/standards/bids_app_specification/index.html> | CC0 |

### 2.2 Reference repositories

| Repo | Role | Licence |
|---|---|---|
| <https://github.com/bids-standard/bids-specification> | The spec itself | CC0 |
| <https://github.com/bids-standard/bids-schema> | Machine-readable YAML schema embedded in bids-specification | CC0 |
| <https://github.com/bids-standard/bids-validator> | Official validator (Deno + JS) | MIT |
| <https://github.com/bids-standard/pybids> | Python interface inside BIDS-Apps | MIT |

### 2.3 BIDS-aware preprocessing pipelines (BIDS-Apps)

All four foundation-model preprocessing paths converge on these:

| Pipeline | Domain | Licence | Container |
|---|---|---|---|
| fMRIPrep (NIPRePs) | rs / task fMRI | Apache 2.0 | nipreps/fmriprep |
| sMRIPrep (NIPRePs) | structural MRI | Apache 2.0 | nipreps/smriprep |
| QSIPrep (PennLINC) | dMRI | BSD-3 | pennlinc/qsiprep |
| MRIQC (NIPRePs) | QC, raw and derivatives | Apache 2.0 | nipreps/mriqc |
| HCP minimal preprocessing pipeline | HCP-family rs / tfMRI / sMRI | BSD-3 | bids/hcppipelines |
| ABCD-HCP pipeline (DCAN) | ABCD | BSD-3 | dcanumn/abcd-hcp-pipeline |
| C-PAC (FCP-INDI) | rs-fMRI, ABIDE / ADHD-200 derivatives | BSD-3 | fcpindi/cpac |
| FitLins | first-level GLMs against BIDS Stats Models | Apache 2.0 | poldracklab/fitlins |

All eight emit BIDS-Derivatives output and run as containerised BIDS-Apps. They are the only tools every paper in this review either uses directly or relies on transitively.

### 2.4 BIDS data archives

| Archive | URL | Default licence |
|---|---|---|
| OpenNeuro | <https://openneuro.org/> | CC0 default |
| Reproducible Brain Corpus (RBC) | <https://reprobrainchart.github.io/> | CC-BY for derivatives, DUA for raw |
| BIDS Apps catalogue | <https://bids-apps.neuroimaging.io/> | reference index |

OpenNeuro and RBC are the two BIDS-native archives. RBC is the only one that publishes harmonised cross-cohort BIDS-Derivatives with a single pipeline-version stamp; this is the model Cytognosis should imitate.

### 2.5 BIDS curation and conversion utilities

| Tool | Role | Type | Install |
|---|---|---|---|
| dcm2niix | DICOM-to-NIfTI binary | system binary | `apt install dcm2niix` |
| HeuDiConv | DICOM-to-BIDS converter (Python wrapper around dcm2niix) | Python | `pip install heudiconv` |
| dcm2bids | alternative simpler DICOM-to-BIDS | Python | `pip install dcm2bids` |
| BIDScoin | DICOM-to-BIDS GUI plus Python | Python | `pip install bidscoin` |
| CuBIDS (PennLINC) | Heterogeneity audit, key-grouping, batch validation | Python | `pip install cubids` |

CuBIDS in particular is the curated default for cross-cohort BIDS hygiene. It identifies acquisition-protocol heterogeneity (a recurring source of harmonisation pain in cross-cohort foundation-model corpora), groups sessions into "key groups", and emits per-key validator reports.

---

## 3. The HED ecosystem

Top-level entry points:

* Home: <https://www.hedtags.org/>
* Resources hub: <https://www.hedtags.org/hed-resources/index.html>
* Schema browser: <https://www.hedtags.org/hed-schema-browser/schema-browser.html>

### 3.1 What HED is and why it matters now

HED is a controlled vocabulary that turns ad-hoc events.tsv columns into machine-readable, semantically aligned annotations. It is a first-class BIDS extension: the events.tsv HED column validates against the official HED schema, and the schema itself is versioned.

The 2026 foundation-model literature highlights an event-annotation harmonisation gap that HED was designed to close. NeuroSTORM's 23-way HCP-task classification, Omni-fMRI's 23-way HCP-task benchmark, SLIM-Brain's emotion-block decoding on StudyForrest, and the Hariri emotion task in Brain-Semantoks all use cohort-idiosyncratic event labels. HED tagging at ingest is the cleanest path to a future task-aware foundation model that shares trial-structure semantics across cohorts.

### 3.2 HED reference repositories

| Repo | Role | Licence |
|---|---|---|
| <https://github.com/hed-standard/hed-specification> | The spec itself | CC0 |
| <https://github.com/hed-standard/hed-schemas> | Versioned schemas (HED v8.x and successors) | CC0 |
| <https://github.com/hed-standard/hed-python> | Python validator and processor | MIT |
| <https://github.com/hed-standard/ndx-hed> | NWB extension that integrates HED into NWB files | BSD-3 |

### 3.3 Practical HED resources curated by the standard

| Resource | URL |
|---|---|
| HED introduction | <https://www.hedtags.org/hed-resources/index.html> |
| HED annotation quickstart | (HED resources) |
| HED validation guide | (HED resources) |
| HED search guide | (HED resources) |
| HED summary guide | (HED resources) |
| BIDS HED quickstart | (HED resources) |
| NWB HED quickstart | (HED resources) |
| HED Python tools (full) | <https://www.hedtags.org/hed-resources/hed-python/index.html> |
| HED online tools | (HED resources, browser-based validator) |

The "BIDS HED quickstart" and "NWB HED quickstart" are the two pages a Cytognosis engineer should bookmark. Both walk through the events.tsv (BIDS) and ndx-hed (NWB) integration with worked examples.

### 3.4 HED implementation defaults

* **Specification version pin:** HED v8.x at dataset_description.json level. Pin in CI.
* **Validator:** hed-python (`pip install hedtools`) on every commit.
* **NWB integration:** ndx-hed (`pip install ndx-hed`) when (and only when) Cytognosis adds a non-BOLD modality and starts emitting NWB.

---

## 4. The NWB ecosystem (in depth)

Top-level entry points:

* Home: <https://www.nwb.org/>
* About NWB: <https://www.nwb.org/about-nwb/>
* Software ecosystem overview: <https://nwb.org/nwb-software/>
* Documentation hub (read-the-docs): <https://nwb-overview.readthedocs.io/en/latest/>
* Core tools catalogue: <https://nwb.org/tools/core/>
* Community tools catalogue: <https://nwb.org/tools/community/>
* Extensions catalogue: <https://nwb-extensions.github.io/>
* Schema (read-the-docs): <https://nwb-schema.readthedocs.io/en/stable/>
* Schema language (read-the-docs): <https://schema-language.readthedocs.io/en/latest/>
* PyNWB documentation: <https://pynwb.readthedocs.io/en/stable/>

The NWB community organises its software into six concerns: data standard schema, data API(s), specification language, data storage, conversion to NWB, and validation. Each concern has a curated default tool. Below, every tool is in one of four NWB-curated tiers: Core (officially maintained by the NWB project), Community (third-party but listed on nwb.org/tools/community), Extension (NDX catalogue), or Archive (DANDI).

### 4.1 Read / write APIs (Core tier)

| Tool | Language | Role | Repo | Licence |
|---|---|---|---|---|
| **PyNWB** | Python | Python reference API for NWB read / write | <https://github.com/NeurodataWithoutBorders/pynwb> | BSD-3 |
| **MatNWB** | MATLAB | MATLAB API | <https://github.com/NeurodataWithoutBorders/matnwb> | BSD-3 |
| **AqNWB** | C++ | C++ API for direct acquisition into NWB | <https://github.com/NeurodataWithoutBorders/aqnwb> | BSD-3 |

PyNWB is the canonical default. MatNWB exists for legacy MATLAB pipelines. AqNWB is for hardware-side acquisition (extracellular ephys rigs writing NWB at the source).

### 4.2 Conversion to NWB (Core tier)

| Tool | Role | Repo | Licence |
|---|---|---|---|
| **NeuroConv** | Python library for automatic conversion from > 40 proprietary acquisition formats (Open Ephys, Spike2, Plexon, Neuropixels, etc.) to NWB. The curated NWB-stack default for ingest. | <https://github.com/catalystneuro/neuroconv> | BSD-3 |
| **NWB GUIDE** | Desktop app providing a no-code GUI for NWB conversion. For collaborators who do not write Python. | <https://github.com/NeurodataWithoutBorders/nwb-guide> | BSD-3 |

### 4.3 Validation (Core tier)

| Tool | Role | Repo | Licence |
|---|---|---|---|
| **NWB Inspector** | Schema validation plus best-practice linting (analogue of bids-validator) | <https://github.com/NeurodataWithoutBorders/nwbinspector> | BSD-3 |

DANDI Archive uses NWB Inspector at ingest as a hard gate. Cytognosis CI should mirror this.

### 4.4 Schema and specification language (Core tier)

| Tool | Role | Repo |
|---|---|---|
| **NWB Schema** | Canonical schema for NWB neurodata types | <https://github.com/NeurodataWithoutBorders/nwb-schema> |
| **HDMF Common Schema** | Common data structures used across the NWB schema | <https://github.com/hdmf-dev/hdmf-common-schema> |
| **HDMF Specification Language** | Formal language for describing NWB-style hierarchical data | <https://github.com/hdmf-dev/hdmf-schema-language> |
| **HDMF Documentation Utilities** | Tools for generating NWB extension documentation | <https://github.com/hdmf-dev/hdmf-docutils> |

The HDMF (Hierarchical Data Modeling Framework) layer is what makes NWB extensible. It is essentially the "metaschema" that the NWB schema is written in.

### 4.5 Data storage backends (Core tier)

| Backend | Role | Repo |
|---|---|---|
| **HDF5** (default) | Original NWB on-disk format; HDF5 hierarchical storage | (HDF Group) |
| **HDMF-Zarr** | Zarr backend for NWB; cloud-friendly chunked array storage | <https://github.com/hdmf-dev/hdmf-zarr> |
| **HDMF** | Core hierarchical-data engine | <https://github.com/hdmf-dev/hdmf> |

HDMF-Zarr is the most consequential 2025–2026 NWB development for Cytognosis: it lets the same NWB-formatted neurodata live in Zarr v3 chunks with cloud-friendly random access, while remaining DANDI-conformant. It collapses the long-standing tension between "FAIR archive format" and "model-training-tier format" into a single artefact.

### 4.6 Extensions (NDX Catalog)

The Neurodata Extensions catalogue (<https://nwb-extensions.github.io>) is a community-curated registry of typed extensions to the NWB schema. Each extension is a versioned schema fragment plus its Python class hierarchy. Authoring an extension is the alternative to forking NWB.

| Extension authoring tool | Role | Repo |
|---|---|---|
| **NDX Catalog** | Browse community extensions | <https://github.com/nwb-extensions/> |
| **NDX Template** | Cookiecutter-style scaffold for a new extension | <https://github.com/nwb-extensions/ndx-template> |
| **Staged Extensions** | GitHub repo for registering new extensions for publication in the NDX Catalog | <https://github.com/nwb-extensions/staged-extensions> |
| **ndx-hed** | NWB extension that integrates HED tags | <https://github.com/hed-standard/ndx-hed> |

### 4.7 Visualisation and analysis (Community tier)

The full Community tier on <https://nwb.org/tools/community/> contains > 30 tools. Highlights relevant to Cytognosis:

| Tool | Role | Domain |
|---|---|---|
| **NWB Widgets** | Jupyter widgets for navigating and visualising NWB files | Python |
| **Neurosift** | Browser-based interactive NWB and DANDI viewer (local + remote) | Web |
| **NWB Explorer** (MetaCell) | Web app for reading, visualising, exploring NWB 2 files; ships with built-in data-type visualisations | Web |
| **HDF Tools** (HDFView, HDF5 plugins for Jupyter / VSCode) | Generic HDF5 inspection | various |
| **Spyglass** | Pipeline + reproducibility framework for analysis on top of NWB + DataJoint | Python |
| **DataJoint** | Open-source data-pipeline definition and execution framework | Python |
| **CaImAn / Suite2p / EXTRACT / CIAtah / OptiNiSt** | Calcium imaging | Python / MATLAB |
| **SpikeInterface / Open Ephys GUI / CellExplorer / MIES** | Extracellular ephys | Python / MATLAB / Igor |
| **EEGLAB** | EEG / iEEG / ECoG | MATLAB |
| **EcogVIS** | ECoG visualiser | Python |
| **Movement / DeepLabCut / SLEAP** | Animal behaviour and pose estimation | Python |
| **CEBRA** | Behavioural-neural latent-space modelling | Python |
| **Pynapple** | Unified analysis toolbox over ephys / ophys / motion-capture | Python |
| **Brain Modeling Toolkit (BMTK)** | Network simulations | Python |
| **Visiomode / ArControl** | Behavioural rigs that emit NWB | Python / Arduino |
| **Neo** | Neurophysiology I/O for many file formats | Python |

For Cytognosis, the immediately relevant Community tools are NWB Widgets, Neurosift, Spyglass, and DataJoint. The rest become relevant only when Cytognosis adds the corresponding modality.

### 4.8 Archive (Core tier)

| Archive | Role | Licence |
|---|---|---|
| **DANDI Archive** | The NIH BRAIN Initiative archive for publishing NWB data; BIDS-equivalent for neurophysiology | <https://dandiarchive.org/> | per-dataset |

The dandi CLI (`pip install dandi`) is the official submission path. DANDI runs NWB Inspector at ingest as a hard gate.

### 4.9 NWB recommendations for Cytognosis

* Keep NWB out of the v0.1 fMRI release; BIDS suffices for MRI alone.
* Pin specific schema versions (NWB schema, HDMF, HDMF-common, HDMF-zarr) in dataset description.
* Stage NWB for v0.2 when Cytognosis adds the first non-BOLD modality (likely simultaneous EEG-fMRI, eye-tracking, or pupillometry alongside task-fMRI).
* Use HDMF-Zarr from day one of NWB adoption to avoid the HDF5-to-Zarr migration that other groups have hit.
* Author extensions, do not fork. If Cytognosis needs new typed neural-data fields, write an NDX extension via ndx-template and contribute it upstream to nwb-extensions/staged-extensions.
* Use ndx-hed as the bridge between BIDS events.tsv and NWB event annotation.

---

## 5. Preprocessing pipelines used in the six papers

Per-paper pipeline path:

| Paper | Pipeline used | Tools transitively |
|---|---|---|
| Taylor (HCP) | Custom HCP-style: FSL mcflirt + topup + BBR + ICA-AROMA, ANTs, Spherical Demons, surface alignment to age-matched template | FSL, ANTs, Spherical Demons, BrainSpace |
| NeuroSTORM | Per-dataset standard pipelines with MNI152 alignment + Z-norm; TCP via HCP-MPP + ICA-FIX | FSL, fMRIPrep, HCP-MPP, ABCD-HCP, ICA-FIX |
| Brain-Semantoks | Standard rs-fMRI on UKB-derived parcel time series | UKB pipeline derivatives |
| SLIM-Brain | HCP / CHCP via HCP-MPP; ABCD via ABCD-HCP; AOMIC via fMRIPrep; ABIDE / ADHD via PCP / C-PAC | HCP-MPP, ABCD-HCP, fMRIPrep, C-PAC |
| Omni-fMRI | Per-dataset standard (HCP-MPP, fMRIPrep, PCP); resampling and Z-scoring uniform across cohorts | HCP-MPP, fMRIPrep, PCP, RBC for NKI / BHRC |
| BrainGFM | fMRIPrep across all cohorts: T1 N4 + skull-strip, ANTs nonlinear normalisation to MNI152NLin2009cAsym, FSL tissue segmentation, fieldmap distortion correction, BBR coregistration (Greve & Fischl 2009), MCFLIRT motion, slice-time correction, ICA-AROMA (Pruim 2015), 6 mm FWHM Gaussian smoothing | fMRIPrep, ANTs, FSL, ICA-AROMA |

The convergence is clear: fMRIPrep and the HCP family (HCP-MPP, ABCD-HCP) absorb almost all preprocessing across the literature. C-PAC and PCP cover the legacy ABIDE / ADHD-200 derivatives.

### 5.1 Underlying engines

| Engine | Role | Licence |
|---|---|---|
| FSL | mcflirt, topup, BBR, MELODIC, ICA-AROMA, ICA-FIX, FIRST | FSL licence (free academic) |
| ANTs | symmetric normalisation, N4 bias correction | BSD-3 |
| FreeSurfer | cortical surface reconstruction, vertex resampling | non-commercial |
| AFNI | 3dDespike, 3dvolreg, 3dTproject | GPL-3 |
| Connectome Workbench | GIFTI / CIFTI / dtseries handling | GPL-2.0 |
| Spherical Demons | spherical surface registration | GPL-2.0 |

FreeSurfer and FSL carry non-commercial-only clauses. Any future Cytognosis PBC commercialisation needs a re-licence step. ANTs, AFNI, Connectome Workbench are permissive enough for PBC distribution.

---

## 6. Atlases and parcellations

Used by the six reviewed papers, plus those nominated by BrainGFM as multi-atlas pretraining inputs:

| Atlas | Type | Parcels | Used by | Licence |
|---|---|---|---|---|
| Schaefer-100 / 200 / 300 / 400 (Schaefer 2018) | functional, gradient-weighted clustering | 100 / 200 / 300 / 400 | Brain-Semantoks (400), Taylor (400 for Neurosynth), BrainGFM (100/200/300), several baselines | CC-BY 4.0 |
| Tian-III subcortical (Tian 2020) | functional, subcortical | scale III | Brain-Semantoks | academic |
| Buckner-7 cerebellar (Buckner 2011) | functional, cerebellar | 7 | Brain-Semantoks | academic |
| Yeo-7 / Yeo-17 networks (Yeo 2011) | functional networks | 7 / 17 | Brain-Semantoks (tokeniser), Taylor (Schaefer-7 group summaries) | academic |
| Shen-268 (Shen 2013) | functional, ICA-based | 268 | BrainGFM | academic |
| Power-264 (Power 2011) | functional hubs, spherical | 264 | BrainGFM | academic |
| Gordon-333 (Gordon 2016) | functional, gradient + network | 333 | BrainGFM, Brain-Semantoks ablation | academic |
| AAL-116 (Tzourio-Mazoyer 2002) | anatomical | 116 | BrainGFM, NeuroSTORM baselines, default in SPM | academic |
| AAL3v1 (Rolls 2020) | anatomical, finer subcortex / cerebellum | 170+ | BrainGFM | academic |
| CC200 (Craddock 2012) | functional, ABIDE-derived | 200 | NeuroSTORM ROI baselines | academic |
| Harvard-Oxford (Desikan 2006) | anatomical, FSL-bundled | varies | NeuroSTORM ROI baselines | academic |
| Desikan-Killiany | anatomical, FreeSurfer-bundled | 68 | NeuroSTORM ROI baselines | included with FreeSurfer |

BrainGFM's strongest 2026 result is that pretraining on multiple atlases simultaneously is strictly better than any single atlas. Cytognosis should therefore plan to emit at least three parcellations per subject (Schaefer-400 + Tian-III + Buckner-7 as the Brain-Semantoks default; Schaefer-100 / 200 / 300 + AAL116 to mirror the BrainGFM corpus; Gordon-333 as a robustness check). The cost is trivial relative to running preprocessing once.

### 6.1 Standard MNI templates

| Template | Role | Source |
|---|---|---|
| MNI152NLin6Asym | 6th-generation symmetric MNI152 | TemplateFlow `tpl-MNI152NLin6Asym` |
| MNI152NLin2009cAsym | 2009c asymmetric (used by BrainGFM, fMRIPrep default) | TemplateFlow `tpl-MNI152NLin2009cAsym` |
| fsLR (32k / 91k grayordinates) | HCP cortical surface | TemplateFlow `tpl-fsLR` |
| fsaverage / fsaverage5 | FreeSurfer surface templates | TemplateFlow `tpl-fsaverage` |

[TemplateFlow](https://www.templateflow.org/) is the curated open-archive registry for these (see §10).

---

## 7. Versioning, sharing, persistent IDs

| Tool | Role | Licence |
|---|---|---|
| **DataLad** (built on git-annex) | Content-addressable dataset versioning, sub-dataset hierarchies, FAIR distribution | MIT |
| **git-annex** | DataLad backend, large-file handling | GPL-3 |
| **OpenNeuro** | BIDS-native public archive, CC0 default | open access |
| **DANDI Archive** | NWB-native public archive | per-dataset |
| **Reproducible Brain Corpus (RBC)** | BIDS-Derivatives multi-cohort harmonised release | CC-BY for derivatives |
| **Zenodo** | Persistent DOI service for tagged releases | CC variants |
| **TemplateFlow** | Open-archive registry of standard MRI templates | CC-BY |

DataLad is the missing link in all six reviewed papers' FAIR stories. None of the four foundation-model papers publishes its preprocessed pretraining corpus as a DataLad-versioned release with persistent DOIs. This is exactly the gap the Cytognosis Milestone 1 substrate should fill.

---

## 8. Site / scanner / acquisition harmonisation

Applied at use time (analysis or fine-tuning), not baked into stored derivatives:

| Method | Role | Implementation |
|---|---|---|
| ComBat (original) | empirical-Bayes site-effect correction | various |
| NeuroComBat | ComBat tailored to neuroimaging | <https://github.com/Jfortin1/ComBatHarmonization> |
| NeuroHarmonize | ComBat with covariate-aware harmonisation | `pip install neuroHarmonize` |
| longitudinal-ComBat (Pomponio) | longitudinal extension | <https://github.com/jcbeer/longCombat> |
| CovBat | covariance-preserving extension | <https://github.com/andy1764/CovBat_Harmonization> |
| DeepCombat | deep learning extension | (research code) |
| Yamashita 2019 | sampling-bias separation across sites | (PLoS Biology, used by SRPBS) |

Cytognosis policy (per the master defaults companion): apply harmonisation at the analysis layer, never at storage. Store all per-scan covariates needed for ComBat (scanner, model, software, head coil, TR, TE, voxel, slice timing, multiband, PE direction, AP/PA polarity, mean FD, % FD > 0.5 mm, tSNR, ICA-AROMA component count) as first-class metadata in BIDS-Derivatives sidecars. Document scanner / site identity with the BIDS InstitutionName + InstitutionalDepartmentName + DeviceSerialNumber fields so that batch variables can be defined unambiguously.

---

## 9. Python and CLI tools used in the foundation-model papers

| Tool | Role | Used by |
|---|---|---|
| Python 3.10+ | language | all |
| nibabel | NIfTI / GIFTI / CIFTI I/O | all |
| nilearn | atlas download, ROI extraction, masking | all |
| MONAI | medical-imaging deep learning | NeuroSTORM, Omni-fMRI |
| TorchIO | volumetric ML data loading | (not directly cited but the natural default) |
| PyTorch + PyTorch Lightning | training | all |
| mamba-ssm | Mamba SSM kernels | NeuroSTORM |
| numpy, scipy, scikit-learn, pandas | scientific stack | all |
| BrainSpace | diffusion-map embedding for FC gradients | Taylor |
| abagen | AHBA gene-expression workflow | Taylor |
| Neurosynth / NiMARE | meta-analytic term maps | Taylor, SLIM-Brain |
| BioClinicalBERT | clinical-text encoder for [T/D] and [A/P] tokens | BrainGFM |

These are all permissively licensed and pip-installable (BioClinicalBERT via Hugging Face).

---

## 10. Standard templates and registries

| Resource | URL | Role |
|---|---|---|
| TemplateFlow | <https://www.templateflow.org/> | Open registry of MNI152, fsLR, fsaverage, MNIInfant, etc. |
| Neurosynth | <https://neurosynth.org/> | Meta-analytic term maps |
| NiMARE | <https://github.com/neurostuff/NiMARE> | Successor to Neurosynth |
| Allen Human Brain Atlas | <https://human.brain-map.org/> | Gene expression mapping (used via abagen) |

---

## 11. Per-stage default tool (one-line summary)

For a Cytognosis cross-cohort fMRI dataset, the FAIR-compliant, openly licensed defaults are:

| Stage | Default | Type |
|---|---|---|
| DICOM to NIfTI | dcm2niix | system |
| DICOM to BIDS | HeuDiConv | Python |
| BIDS curation | CuBIDS | Python |
| BIDS validation | bids-validator + pybids | system + Python |
| BIDS template management | TemplateFlow | Python |
| Raw QC | MRIQC | BIDS-App |
| HCP-family preprocessing | HCP minimal preprocessing pipeline | BIDS-App |
| ABCD preprocessing | ABCD-HCP pipeline (DCAN) | BIDS-App |
| Generic rs / task fMRI preprocessing | fMRIPrep | BIDS-App |
| Structural | sMRIPrep | BIDS-App |
| dMRI | QSIPrep | BIDS-App |
| Denoising | ICA-AROMA + ICA-FIX | bundled |
| Surface I/O | Connectome Workbench, nibabel | system + Python |
| Atlas / ROI extraction | nilearn maskers + Schaefer + Tian + Buckner + Yeo (+ Shen + Power + Gordon + AAL for multi-atlas) | Python |
| Task GLM | FitLins on BIDS Stats Models | BIDS-App |
| Event annotation | hed-python (`hedtools`) | Python |
| Site harmonisation (at use time) | NeuroHarmonize | Python |
| Versioning | DataLad + git-annex | Python + system |
| Cloud-friendly storage | Zarr v3 (4D voxel), Parquet (parcellated) | Python |
| Publish persistent DOI | Zenodo, OpenNeuro for raw, RBC pattern for derivatives | web |
| NWB conversion (later) | NeuroConv | Python |
| NWB no-code GUI | NWB GUIDE | system |
| NWB validation | NWB Inspector | Python |
| NWB Zarr backend | HDMF-Zarr | Python |
| NWB Python API | PyNWB | Python |
| HED-in-NWB | ndx-hed | Python |
| NWB visualisation | NWB Widgets, Neurosift | Python + web |
| NWB pipeline framework | Spyglass + DataJoint | Python |
| NWB archive submission | dandi CLI | Python |

(Detailed install commands are in the companion file `fMRI_pipeline_defaults_2026.md`.)

---

## 12. License and openness summary

| Layer | Licence(s) |
|---|---|
| BIDS, BIDS-Schema, BIDS Stats Models, BIDS App Specification | CC0 |
| HED specification, HED schemas | CC0 |
| NWB specification | CC-BY 4.0 |
| BIDS code (validator, pybids, fMRIPrep, MRIQC, QSIPrep, FitLins) | MIT or Apache 2.0 |
| HED tools (hed-python) | MIT |
| NWB tools (PyNWB, MatNWB, AqNWB, NeuroConv, NWB Inspector, HDMF, HDMF-Zarr, ndx-hed) | BSD-3 |
| DataLad | MIT |
| FSL | free for academic use; commercial requires permission |
| FreeSurfer | non-commercial research |
| ANTs, AFNI, Connectome Workbench, C-PAC | BSD-3, GPL-3, GPL-2, BSD-3 |
| Atlases (Schaefer 2018, Tian, Buckner, Yeo, Shen, Power, Gordon, AAL, AAL3v1) | CC-BY 4.0 (Schaefer); academic with citation (others) |

Two non-commercial-only clauses (FSL, FreeSurfer) are the only items in the stack that may require re-licensing for a future Cytognosis PBC subsidiary. Everything else, including all three first-class community standards (BIDS, HED, NWB), is open-source under permissive or copyleft licences compatible with the Cytognosis openness skill.

---

## 13. Closing note

The 2025–2026 fMRI literature has converged on a small, well-curated stack: BIDS for layout, HED for events, NWB for non-BOLD modalities, fMRIPrep / HCP-MPP / ABCD-HCP for preprocessing, the Schaefer + Tian + Buckner + Yeo / Power / Shen / Gordon / AAL family for parcellation, DataLad + Zenodo for FAIR distribution, and a handful of Python libraries (nibabel, nilearn, MONAI, PyTorch) for analysis. Every piece is openly licensed and openly governed. The single biggest open gap, that none of the foundation-model papers publishes its preprocessed corpus as a FAIR-compliant DataLad-versioned BIDS-Derivatives release, is exactly the gap the Cytognosis Milestone 1 substrate is positioned to close.

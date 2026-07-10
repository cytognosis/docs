# Cytognosis fMRI pipeline: nominated defaults (2026)

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: researchers, stakeholders
> **Tags**: `research`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)

Synthesised from the five-paper review (`fMRI_papers_review_2026.md`) and the curated tool catalogues at the BIDS, HED, and NWB community sites (`nwb.org/tools/core`, `nwb.org/tools/community`, `nwb.org/nwb-software`, `nwb-overview.readthedocs.io`, `bids.neuroimaging.io`, `hedtags.org/hed-resources`).

For each pipeline stage there is one nominated default. Alternatives are listed only where the choice is genuinely live. Tools are split into two groups:

* **Python packages**: install via `pip` (or `uv pip`); pinned in `pyproject.toml` of every Cytognosis preprocessing or analysis repo.
* **System / containerised tools**: not pip-installable, distributed as Docker/Singularity images, native binaries, or NPM/Deno binaries; pulled at container build time or installed on the workstation.

No em dashes anywhere; pin a single version of every default in `dataset_description.json`.

---

## 1. End-to-end stage table

| # | Stage | Default | Type | Install |
|---|---|---|---|---|
| 1 | DICOM read + NIfTI conversion | dcm2niix | system | `apt install dcm2niix` or conda-forge |
| 2 | DICOM-to-BIDS curation | HeuDiConv | python | `pip install heudiconv` |
| 3 | BIDS heterogeneity audit and key-grouping | CuBIDS | python | `pip install cubids` |
| 4 | BIDS validation in CI | deno-bids-validator (official) | system | `deno install -A -g -n bids-validator jsr:@bids/validator` (or use `pip install bids-validator-deno`) |
| 5 | BIDS programmatic queries inside pipelines | PyBIDS | python | `pip install pybids` |
| 6 | Standard-template management (MNI152NLin6Asym, fsLR, etc.) | TemplateFlow | python | `pip install templateflow` |
| 7 | Raw + derivatives QC reports | MRIQC | system (BIDS-App) | `docker pull nipreps/mriqc` (also `pip install mriqc` if running natively) |
| 8 | rs/tfMRI preprocessing, generic cohort | fMRIPrep | system (BIDS-App) | `docker pull nipreps/fmriprep` |
| 9 | rs/tfMRI preprocessing, HCP-family cohort | HCP minimal preprocessing pipeline | system | `docker pull bids/hcppipelines` |
| 10 | rs/tfMRI preprocessing, ABCD | ABCD-HCP (DCAN) pipeline | system | `docker pull dcanumn/abcd-hcp-pipeline` |
| 11 | dMRI preprocessing | QSIPrep | system (BIDS-App) | `docker pull pennlinc/qsiprep` |
| 12 | Cortical surface reconstruction (transitive via fMRIPrep / HCP-MPP) | FreeSurfer | system | non-commercial license, `docker pull freesurfer/freesurfer` |
| 13 | Linear / nonlinear MR registration | ANTs | system | `apt install ants` or `docker pull antsx/ants` |
| 14 | Motion / distortion / ICA / artefact denoising | FSL (mcflirt, topup, BBR, MELODIC) + ICA-AROMA + ICA-FIX | system | `docker pull bids/fsl` (FSL has its own license); ICA-AROMA via `pip install aroma`; ICA-FIX bundled in HCP-MPP |
| 15 | Surface I/O, GIFTI / CIFTI, dtseries handling | Connectome Workbench | system | `apt install connectome-workbench` |
| 16 | NIfTI / GIFTI / CIFTI Python I/O | nibabel | python | `pip install nibabel` |
| 17 | Atlas download, ROI extraction, masking, NIfTI maths | nilearn | python | `pip install nilearn` |
| 18 | Parcellation triple (cortex, subcortex, cerebellum) | Schaefer-400 + Tian-III + Buckner-7 | data | fetched via nilearn / templateflow scripts; pin SHA in dataset description |
| 19 | First-level fMRI GLMs against BIDS Stats Models | FitLins | python | `pip install fitlins` |
| 20 | Meta-analytic interpretation maps | NiMARE (Neurosynth backend) | python | `pip install nimare` |
| 21 | FC gradients, diffusion-map embeddings | BrainSpace | python | `pip install brainspace` |
| 22 | Site / scanner harmonisation, applied at analysis time | NeuroHarmonize (NeuroComBat family) | python | `pip install neuroHarmonize` |
| 23 | Confound modelling helper | fmriprep-confound or nilearn confound utilities | python | already in `nilearn` |
| 24 | Event annotation in events.tsv | HED + hedtools | python | `pip install hedtools` |
| 25 | Pipeline orchestration (workflow engine) | Nipype (for in-process); Nextflow / Snakemake (for batch) | python + system | `pip install nipype`; Nextflow native binary |
| 26 | Containerised analysis (BIDS Apps spec) | Docker / Singularity / Apptainer | system | `apt install docker.io` or `apt install apptainer` |
| 27 | Dataset versioning + content-addressable storage | DataLad (built on git-annex) | python + system | `pip install datalad`; system `git-annex` |
| 28 | Cloud-friendly chunked array storage for the model-training tier | Zarr v3 | python | `pip install "zarr>=3"` |
| 29 | HDF5 storage and inspection | h5py + HDFView | python + system | `pip install h5py`; HDFView download |
| 30 | Tabular per-ROI per-timepoint storage | PyArrow (Parquet) | python | `pip install pyarrow` |
| 31 | Labelled multi-dimensional array I/O (NetCDF) | xarray + netCDF4 | python | `pip install xarray netCDF4` |
| 32 | Persistent DOIs and open release | Zenodo + DataLad publish | system | web upload + `datalad publish` |
| 33 | NWB read/write API (planned for v0.2 multi-modal) | PyNWB | python | `pip install pynwb` |
| 34 | Automatic conversion from proprietary acquisition formats to NWB | NeuroConv | python | `pip install neuroconv` |
| 35 | No-code GUI for NWB conversion (for collaborators) | NWB GUIDE | system | `nwb-guide` desktop app download |
| 36 | NWB schema validation and best-practice linting | NWB Inspector | python | `pip install nwbinspector` |
| 37 | NWB Zarr backend (replaces HDF5 inside NWB) | HDMF-Zarr | python | `pip install hdmf-zarr` |
| 38 | NWB extension authoring scaffold | ndx-template | python (cookiecutter) | `pip install cookiecutter && cookiecutter gh:nwb-extensions/ndx-template` |
| 39 | HED inside NWB (event tagging across modalities) | ndx-hed | python | `pip install ndx-hed` |
| 40 | NWB visualisation in Jupyter | NWBWidgets | python | `pip install nwbwidgets` |
| 41 | NWB browser-based exploration | Neurosift | system (web app) | `npx neurosift` or web hosted |
| 42 | Pipeline + reproducibility framework over NWB | Spyglass + DataJoint | python | `pip install spyglass-neuro datajoint` |
| 43 | DANDI archive submission CLI | dandi | python | `pip install dandi` |
| 44 | OpenNeuro CLI submission | openneuro-cli | system | `npm install -g @openneuro/cli` |
| 45 | Volumetric ML data loaders for PyTorch | TorchIO | python | `pip install torchio` |
| 46 | Medical-imaging deep learning toolkit | MONAI | python | `pip install monai` |
| 47 | Probabilistic / variational analysis | scvi-tools (for any single-cell side) | python | `pip install scvi-tools` |
| 48 | AHBA gene expression workflow | abagen | python | `pip install abagen` |
| 49 | NIfTI-style 3D viewer in browser | NiiVue | system | `npm install -g niivue` |
| 50 | Workspace-wide BIDS app catalogue browser | BIDS Apps catalogue | reference | <https://bids-apps.neuroimaging.io/> |

---

## 2. Single-line pip install for the Cytognosis fMRI Python stack

Pin in a `pyproject.toml`; this is the working default for any Cytognosis preprocessing, analysis, or model-training repo. Versions are intentionally permissive at the floor and capped at the next major where the project has stable APIs.

```bash
pip install \
  "heudiconv>=1.3" \
  "cubids>=1.2" \
  "pybids>=0.16" \
  "templateflow>=24.2" \
  "mriqc>=24.0" \
  "fmriprep>=24.1" \
  "qsiprep>=0.23" \
  "nibabel>=5.3" \
  "nilearn>=0.11" \
  "fitlins>=0.12" \
  "nimare>=0.4" \
  "brainspace>=0.1.10" \
  "neuroHarmonize>=2.4" \
  "hedtools>=0.5" \
  "nipype>=1.10" \
  "datalad>=1.1" \
  "zarr>=3.0" \
  "h5py>=3.12" \
  "pyarrow>=18.0" \
  "xarray>=2024.10" \
  "netCDF4>=1.7" \
  "pynwb>=2.8" \
  "neuroconv>=0.7" \
  "nwbinspector>=0.6" \
  "hdmf-zarr>=0.10" \
  "ndx-hed>=0.1" \
  "nwbwidgets>=0.11" \
  "spyglass-neuro>=0.5" \
  "datajoint>=0.14" \
  "dandi>=0.65" \
  "torchio>=0.20" \
  "monai>=1.4" \
  "abagen>=0.1.4"
```

Where the project is heavy enough to warrant separate optional groups, split into `[imaging]`, `[nwb]`, `[ml]`, `[harmonization]`, `[stats]` extras. Default `pip install cytognosis-fmri` should pull only `pybids`, `nibabel`, `nilearn`, `templateflow`, `pyarrow`, `zarr`, and `datalad`; everything heavier goes behind extras.

---

## 3. System-level installs (one container, one workstation init)

These are the things `pip` cannot give you. Do them once, in a container Dockerfile, or once on a developer workstation.

| Tool | Purpose | Install |
|---|---|---|
| dcm2niix | DICOM to NIfTI binary | `apt install dcm2niix` (Ubuntu) or conda `-c conda-forge dcm2niix` |
| FSL 6.0.7+ | mcflirt, topup, BBR, MELODIC, FIRST, randomise | <https://fsl.fmrib.ox.ac.uk/fsldownloads> (own license) |
| FreeSurfer 7.x | Surface reconstruction, recon-all, mri_convert | non-commercial license, <https://surfer.nmr.mgh.harvard.edu/> |
| ANTs | Symmetric normalisation, N4 bias correction | `apt install ants` or build from source |
| AFNI | 3dDespike, 3dvolreg, 3dTproject | `apt install afni` |
| Connectome Workbench | wb_command, dtseries / GIFTI / CIFTI manipulation | `apt install connectome-workbench` |
| Singularity / Apptainer | Run BIDS-Apps reproducibly | `apt install apptainer` |
| Docker | Run BIDS-Apps locally | <https://docs.docker.com/engine/install/> |
| git-annex | DataLad backend | `apt install git-annex` |
| Deno + bids-validator | Official BIDS validator | `apt install deno`, then `deno install -A -g -n bids-validator jsr:@bids/validator` |
| Nextflow | Cohort-scale BIDS-App orchestration | `curl -s https://get.nextflow.io \| bash` |
| Snakemake (CLI) | Alternative orchestrator | also `pip install snakemake` |
| Node.js | OpenNeuro CLI, NiiVue | `apt install nodejs npm` |
| OpenNeuro CLI | Submission to OpenNeuro | `npm install -g @openneuro/cli` |
| HDFView | GUI HDF5 inspector | <https://www.hdfgroup.org/downloads/hdfview/> |
| NWB GUIDE | No-code NWB conversion app for collaborators | <https://nwb-guide.readthedocs.io/> |
| Neurosift | Browser NWB / DANDI viewer | `npx neurosift` |
| NiiVue | Browser NIfTI viewer | `npm install -g niivue` or web-hosted |

### Containerised BIDS-Apps to keep ready

Pull these once into the Cytognosis container registry; pin tags by SHA, never `latest`.

```bash
docker pull nipreps/mriqc:24.0.2
docker pull nipreps/fmriprep:24.1.1
docker pull nipreps/smriprep:0.16.1
docker pull pennlinc/qsiprep:0.23.0
docker pull bids/hcppipelines:v4.7.0
docker pull dcanumn/abcd-hcp-pipeline:v0.1.3
docker pull poldracklab/fitlins:0.12.0
```

---

## 4. Stage-by-stage rationale for the tougher choices

* **fMRIPrep over a hand-rolled FSL pipeline.** All four 2026 foundation-model papers either use fMRIPrep directly (SLIM-Brain on AOMIC, Omni-fMRI on AOMIC) or use HCP-MPP, which fMRIPrep mirrors closely. fMRIPrep is the only widely adopted pipeline that is BIDS-App-native, ships a reproducible Singularity image, and emits a confound TSV in the format every downstream consumer expects.
* **HCP-MPP for the HCP family, ABCD-HCP for ABCD.** Use the canonical pipeline for the canonical cohort. Mixing pipelines inside one cohort is a documented source of cross-paper irreproducibility (see RBC's harmonisation strategy). The cost of running two more pipelines is trivial; the cost of remixing later is large.
* **NeuroConv over hand-rolled converters.** NeuroConv (CatalystNeuro) is the curated default in the NWB ecosystem and supports more than 40 proprietary acquisition formats (Open Ephys, Spike2, Plexon, NeuroData, Neuropixels, etc.). When Cytognosis adds a non-BOLD modality, NeuroConv is the cheapest path to NWB conformance.
* **HDMF-Zarr instead of NWB-on-HDF5 for the model-training tier.** HDMF-Zarr is officially curated by the NWB team as the Zarr backend for NWB. Storing NWB-formatted data in Zarr v3 chunks gives both NWB schema conformance (so DANDI accepts it) and the cloud-friendly chunked I/O that PyTorch DataLoaders want. This collapses the tension between "FAIR archive format" and "model-training format" into a single artefact.
* **HED + hedtools as the only event-annotation default.** All four foundation-model papers benchmark on task-fMRI but each uses cohort-idiosyncratic event labels. HED is the only standard that is a first-class BIDS extension, has a CC0 specification, has a maintained Python validator (`hedtools`), and has an NWB bridge (`ndx-hed`). No other candidate covers all four properties.
* **NeuroHarmonize over plain ComBat.** NeuroHarmonize implements ComBat with covariate-aware harmonisation suitable for site / scanner effects in cross-cohort fMRI, and is the most actively maintained Python implementation. Apply at use-time, never at storage-time, as recommended in §7.5 of the review.
* **DataLad + git-annex over plain git-LFS.** Git-LFS does not handle the per-cohort sub-dataset pattern that BIDS naturally has, and OpenNeuro / RBC are both DataLad-native. Persistent DOIs from Zenodo wrap cleanly around DataLad releases.
* **TorchIO + MONAI for ML loading, in that order.** TorchIO is BIDS-aware and integrates cleanly with PyTorch DataLoaders for 3D/4D volumes; MONAI is a richer medical-imaging deep-learning toolkit but slightly heavier. Default to TorchIO for data ingestion; reach for MONAI when training augmentations or transforms get sophisticated.
* **FitLins for first-level GLMs.** FitLins is the BIDS-App that consumes BIDS Stats Models JSON and emits BIDS-Derivatives statistical maps, closing the loop with the §7.1 recommendation to ship Stats Models alongside task-fMRI derivatives.

---

## 5. What is NOT recommended as a default (and why)

* **DPABI / DPARSF.** Closed source, MATLAB-only, not BIDS-native. Use only if a specific dataset already ships its derivatives in DPABI format.
* **CONN toolbox.** MATLAB-based, not BIDS-App. Acceptable for analysis-only workflows but not as a Cytognosis default.
* **Custom AFNI-only or SPM-only pipelines.** Both are excellent toolkits but are not BIDS-App-native by default. Run their underlying tools through fMRIPrep / FitLins instead.
* **NWB before BIDS for fMRI v0.1.** BIDS is the dominant standard for MRI; NWB for non-BOLD modalities, layered later.
* **CC0 for trained model weights or subject-level embeddings without a re-id risk assessment.** Use Apache 2.0 or OpenRAIL-style licences after assessment.

---

## 6. Single-page summary

For any new Cytognosis fMRI repo, the floor is:

```bash
pip install pybids nibabel nilearn templateflow pyarrow "zarr>=3" datalad hedtools pynwb neuroconv nwbinspector hdmf-zarr ndx-hed dandi torchio monai
```

…on top of a container image that has dcm2niix, FSL, FreeSurfer, ANTs, AFNI, Connectome Workbench, Apptainer, git-annex, Deno + bids-validator, and the seven pinned BIDS-App images listed in §3.

Everything else in §1 is reachable from these defaults; everything outside §1 needs a written justification in the dataset description.

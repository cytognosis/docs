# Cytognosis Python defaults for neuroimaging and neuroelectrophysiology (2026)

Org-wide nominated Python defaults for the connectomic layer (MRI, fMRI, EEG, fNIRS, and future ephys / ophys), synthesised from the six-paper review, the BIDS / HED / NWB curated catalogues, the LinkML and LaminDB architecture discussions, and the Cytos / Cytocast design notes.

The initial five groups suggested (storage, preprocessing, nwb, bids, ml) are extended to eight because three roles do not belong inside any of those five: **schemas and standards** (LinkML, ontology, GA4GH), **HED event annotation** (a cross-cutting BIDS extension that also lives inside NWB), and **provenance and catalog** (LaminDB, DataLad, DANDI). The eight groups, ordered from source-of-truth to model training, are:

1. Schemas and standards (the typed source of truth)
2. Storage backends (the bytes)
3. BIDS ecosystem (filesystem layout + validation + curation for MRI)
4. NWB ecosystem (neurophysiology + multimodal beyond BIDS)
5. Preprocessing (transformations from raw to model-ready)
6. HED event annotation (semantic event layer, cross-cuts BIDS and NWB)
7. ML training and analytics (foundation-model-ready)
8. Provenance, catalog, distribution (governance and lineage)

Every package below is nominated as an org-wide default. Pin floors are intentional, ceilings are intentionally absent; tighten in the project `pyproject.toml` as needed.

All packages are open-source under permissive or copyleft licences compatible with the Cytognosis openness policy.

---

## 1. Schemas and standards

The source of truth for every Cytognosis data layer. Author once in LinkML, generate everything downstream.

| Package | pip name | Pin floor | Role | Why default |
|---|---|---|---|---|
| LinkML | `linkml` | `>=1.8` | Schema authoring, multi-target code generation (Pydantic, JSON Schema, GraphQL, SHACL, RDF, Protobuf, SQL DDL, TileDB) | Source of truth across all four Cytognosis data layers; matches the CELLxGENE and GA4GH direction of travel |
| LinkML runtime | `linkml-runtime` | `>=1.7` | Runtime validation against LinkML schemas | Pair with LinkML for in-pipeline checks |
| Pydantic | `pydantic` | `>=2.6` | Typed records generated from LinkML | Default Python type system |
| OAKlib (OAK) | `oaklib` | `>=0.6` | Ontology Access Kit; programmatic access to MONDO, HP, UBERON, GO, CL, NCIT, etc. | Ontology resolution in pipelines and bionty alternative for non-LaminDB code paths |
| HED schemas | `hedtools` | `>=0.5` | HED schema browser + validator + processor (also appears in §6) | Mandatory event annotation layer |
| Phenopackets | `phenopackets` | `>=2.0` | GA4GH Phenopackets Python (subject + phenotype + clinical) | Canonical cross-layer subject record |
| GA4GH VRS | `ga4gh.vrs` | `>=2.0` | GA4GH Variation Representation Spec | Variant normalisation upstream of TileDB-VCF |
| GA4GH VRS-Cat | `ga4gh.vrs-anvil` or `ga4gh.cat-vrs` (preferred when available) | latest | VRS Categorical Variation | Variant category modelling |
| jsonschema | `jsonschema` | `>=4.21` | JSON Schema validation (target of LinkML compile) | Fallback validator for non-Pydantic consumers |
| rdflib | `rdflib` | `>=7.0` | RDF / Turtle / JSON-LD | Materialise LinkML to RDF for triple-store ingestion |

**Alternatives considered and not chosen:**
- Frictionless Data Package: weaker ontology support than LinkML.
- Protobuf as schema source of truth: less ontology-native than LinkML; LinkML can compile to Protobuf when needed.
- pyld / Owlready2: less mature than oaklib for OBO Foundry traversal.

---

## 2. Storage backends

Chunked, cloud-native, foundation-model-ready. TileDB and Zarr beat HDF5 wherever distributed training is in scope; HDF5 (via h5py) stays available for legacy analysis paths.

| Package | pip name | Pin floor | Role | Why default |
|---|---|---|---|---|
| Zarr v3 | `zarr` | `>=3.0` | Cloud-native chunked array storage | Default for 4D fMRI volumes + general training-tier arrays |
| HDMF-Zarr | `hdmf-zarr` | `>=0.10` | NWB Zarr backend | Curated NWB cloud-friendly storage; replaces HDF5 for NWB-on-cloud |
| h5py | `h5py` | `>=3.12` | HDF5 access for legacy NWB and AnnData h5ad | Required for ecosystem interop |
| PyArrow | `pyarrow` | `>=18.0` | Parquet / Arrow | Default for tabular per-ROI per-timepoint stores, Phenopacket tables |
| xarray | `xarray` | `>=2024.10` | Labelled N-D arrays over Zarr / NetCDF | Time-series and atlas-projected derivatives |
| netCDF4 | `netCDF4` | `>=1.7` | NetCDF format | xarray backend, multi-cohort fMRI summary tables |
| TileDB | `tiledb` | `>=0.32` | Cloud-native array storage with ACID + versioning | Primary substrate for genomic / cellular / future connectomic |
| TileDB-SOMA | `tiledbsoma` | `>=1.13` | Cellular omics (AnnData / MuData on TileDB) | Cellular layer default; cellxgene-schema compliant |
| TileDB-VCF | `tiledbvcf` | `>=0.34` | Genomic variants on TileDB | Variant layer default |
| polars | `polars` | `>=1.10` | Faster pandas-style dataframe | Default for in-memory large-table operations |
| fsspec + s3fs / gcsfs | `fsspec`, `s3fs`, `gcsfs` | latest | Cloud filesystem access | Required by Zarr, PyArrow, etc. for S3 / GCS |

**Alternatives considered:**
- Plain HDF5 as default for NWB: rejected because cloud parallel reads / writes are poor; HDMF-Zarr replaces it.
- Apache Iceberg / Delta Lake for tabular: overkill at current scale; Parquet on object storage with PyArrow is enough.

---

## 3. BIDS ecosystem

The filesystem and validation contract for MRI raw and derivatives.

| Package | pip name | Pin floor | Role | Why default |
|---|---|---|---|---|
| PyBIDS | `pybids` | `>=0.16` | Programmatic queries inside BIDS-Apps and notebooks | Default BIDS Python interface |
| bids-validator (Python wrapper) | `bids-validator` | `>=2.0` | Python wrapper around the official Deno validator | CI gate; pair with the system-level Deno binary |
| CuBIDS | `cubids` | `>=1.2` | Heterogeneity audit, key-grouping, batch validation | Cross-cohort hygiene; the only tool that handles acquisition-protocol drift well |
| HeuDiConv | `heudiconv` | `>=1.3` | DICOM-to-BIDS converter (wraps dcm2niix) | Default DICOM ingest path |
| dcm2bids | `dcm2bids` | `>=3.2` | Simpler DICOM-to-BIDS alternative for small datasets | Recommended for one-off conversions |
| TemplateFlow | `templateflow` | `>=24.2` | Curated registry of MNI152, fsLR, fsaverage templates | Required for fMRIPrep + MRIQC + atlas resampling |
| BIDS Stats Models (FitLins) | `fitlins` | `>=0.12` | First-level GLMs against BIDS Stats Models JSON | Default task-fMRI GLM emitter |
| ancpbids | `ancpbids` | `>=0.2` | Schema-aware BIDS dataset API alternative to PyBIDS | Use only when PyBIDS limits are hit |
| bidsschematools | `bidsschematools` | latest | Programmatic access to bids-schema | Schema pinning and CI checks |

**Alternatives considered:**
- BIDScoin (`bidscoin`): GUI-focused; HeuDiConv covers headless automation better.
- mri-bids: not maintained.

---

## 4. NWB ecosystem

Neurophysiology and any non-BOLD modality beyond BIDS. Default to HDMF-Zarr backend from day one.

| Package | pip name | Pin floor | Role | Why default |
|---|---|---|---|---|
| PyNWB | `pynwb` | `>=2.8` | Python reference API for NWB read / write | NWB core; default for all NWB code paths |
| HDMF | `hdmf` | `>=3.14` | Hierarchical Data Modeling Framework underneath NWB | Required dependency of PyNWB |
| HDMF Common Schema | `hdmf-common-schema` | (bundled) | Common data structures | Bundled with HDMF |
| HDMF-Zarr | `hdmf-zarr` | `>=0.10` | Zarr backend for HDMF / NWB | Default backend (also in §2 storage) |
| HDMF docutils | `hdmf-docutils` | `>=0.4` | Documentation generation for NWB extensions | Used when authoring extensions |
| NeuroConv | `neuroconv` | `>=0.7` | Auto-conversion from > 40 proprietary formats (Open Ephys, Spike2, Plexon, Neuropixels, etc.) to NWB | Default ingest for non-NIfTI proprietary acquisitions |
| NWB Inspector | `nwbinspector` | `>=0.6` | Schema + best-practice validator (analogue of bids-validator) | CI gate before DANDI submission |
| ndx-template | `ndx-template` | latest | Cookiecutter scaffold for NWB extensions | Use when authoring a typed extension |
| ndx-hed | `ndx-hed` | `>=0.1` | HED tags inside NWB (also in §6) | Bridge between BIDS events.tsv and NWB |
| NWB Widgets | `nwbwidgets` | `>=0.11` | Jupyter widgets for NWB navigation | Default in-notebook NWB visualisation |
| dandi | `dandi` | `>=0.65` | DANDI archive CLI | Default NWB submission path |

**Alternatives considered:**
- MatNWB / AqNWB: not Python, kept available for legacy MATLAB code and hardware-side acquisition respectively.
- Direct HDF5 / Zarr writes bypassing PyNWB: rejected because they lose NWB Inspector validation and DANDI conformance.

---

## 5. Preprocessing

The transformation layer from raw BIDS to model-ready arrays. Most preprocessing is delegated to containerised BIDS-Apps (Docker / Singularity); the Python packages below either invoke those containers, post-process their outputs, or do in-process operations that do not need a full BIDS-App.

| Package | pip name | Pin floor | Role | Why default |
|---|---|---|---|---|
| fMRIPrep | `fmriprep` | `>=24.1` | rs / task fMRI preprocessing (BIDS-App) | Default for non-HCP cohorts |
| MRIQC | `mriqc` | `>=24.0` | Raw + derivative QC (BIDS-App) | Default QC step |
| sMRIPrep | `smriprep` | `>=0.16` | Structural MRI preprocessing | Pairs with fMRIPrep |
| QSIPrep | `qsiprep` | `>=0.23` | dMRI preprocessing (BIDS-App) | Default for diffusion |
| nibabel | `nibabel` | `>=5.3` | NIfTI / GIFTI / CIFTI I/O | Universal Python neuroimaging I/O |
| nilearn | `nilearn` | `>=0.11` | Atlas download, ROI extraction, NIfTI maths, plotting | Universal default |
| Nipype | `nipype` | `>=1.10` | In-process workflow engine over FSL / ANTs / AFNI / FreeSurfer | Used inside fMRIPrep; available standalone |
| NeuroHarmonize | `neuroHarmonize` | `>=2.4` | ComBat with covariate-aware harmonisation | Default harmonisation, applied at use time |
| BrainSpace | `brainspace` | `>=0.1.10` | FC gradients via diffusion-map embedding | Default for FC-gradient analyses (Taylor 2026 lineage) |
| DiPy | `dipy` | `>=1.9` | Diffusion MRI analysis | Default for dMRI analytical work |
| BrainStat | `brainstat` | `>=0.4` | Cortical surface statistics | Default for vertex-wise mass-univariate |
| FitLins | `fitlins` | `>=0.12` | BIDS Stats Models GLM (also in §3) | Task-fMRI first-level |
| NiMARE | `nimare` | `>=0.4` | Meta-analytic term maps (Neurosynth successor) | Default interpretability tool |
| abagen | `abagen` | `>=0.1.4` | AHBA gene expression workflow | Required for gene-imaging integration |
| TemplateFlow | `templateflow` | (in §3) | Template registry | Required by all of the above |

**Alternatives considered:**
- C-PAC Python (`cpac`): kept for ABIDE / ADHD-200 derivative ingestion only.
- AFNI / FSL Python wrappers: invoked transitively via fMRIPrep; not org-wide defaults on their own.

---

## 6. HED event annotation

A cross-cutting standard. Lives inside BIDS (events.tsv HED column) and inside NWB (ndx-hed). Separated into its own group because it is mandatory for task-fMRI cross-cohort harmonisation and the foundation-model literature explicitly calls it out as the missing piece.

| Package | pip name | Pin floor | Role | Why default |
|---|---|---|---|---|
| hedtools | `hedtools` | `>=0.5` | HED validator, processor, search, summary in Python | Default validator; runs in CI |
| ndx-hed | `ndx-hed` | `>=0.1` | NWB extension that integrates HED tags into NWB files | Required when emitting NWB with task events |
| hed-schema (pinned in metadata) | (no pip; pinned in `dataset_description.json`) | latest HED v8.x | Versioned HED schemas | Pin in dataset description |

**Implementation rule:** every task-fMRI `events.tsv` that ships in a Cytognosis BIDS dataset MUST carry HED tags validated by hedtools in CI against a pinned HED schema version recorded in `dataset_description.json`.

---

## 7. ML training and analytics

Foundation-model-ready stack, including the parameter-efficient adaptation tools the 2026 literature standardised on.

| Package | pip name | Pin floor | Role | Why default |
|---|---|---|---|---|
| PyTorch | `torch` | `>=2.4` | Default DL framework | Standard across the foundation-model papers |
| PyTorch Lightning | `lightning` | `>=2.4` | Training loop, mixed precision, distributed training | Bound in Cytos generation profile |
| JAX + Flax | `jax`, `flax` | latest | Alternative DL stack for selected workloads | Bound in Cytos generation profile |
| Hugging Face Transformers | `transformers` | `>=4.45` | BioClinicalBERT, BERT, biomedical encoders used by BrainGFM | Default text-encoder source |
| accelerate | `accelerate` | `>=0.34` | Distributed training, FSDP, DeepSpeed glue | Default training accelerator |
| PEFT | `peft` | `>=0.13` | Parameter-efficient fine-tuning (LoRA, prefix-tuning, prompt-tuning) | Default fine-tuning library |
| TorchIO | `torchio` | `>=0.20` | BIDS-aware volumetric ML DataLoaders | Default for 3D / 4D MRI loaders |
| MONAI | `monai` | `>=1.4` | Medical-imaging deep-learning toolkit | Default for medical-imaging models |
| PyTorch Geometric | `torch-geometric` | `>=2.6` | Graph neural networks (brain-graph foundation models, BrainGFM lineage) | Default for connectome / brain-graph models |
| DGL | `dgl` | `>=2.4` | Alternative GNN library | Use only when torch-geometric limits are hit |
| scvi-tools | `scvi-tools` | `>=1.2` | Variational + deep generative models for single-cell | Required for the cellular layer; reused for some MR latent models |
| timm | `timm` | `>=1.0` | Vision transformer model zoo | Backbone library for SLIM-Brain / Omni-fMRI-style 4D MAE |
| mamba-ssm | `mamba-ssm` | `>=2.2` | Selective state-space kernels | Required for NeuroSTORM-style Mamba backbones |
| learn2learn | `learn2learn` | `>=0.2` | MAML and related meta-learning | Required for BrainGFM-style few-shot |
| safetensors | `safetensors` | `>=0.4` | Safe + fast tensor serialisation | Default model-weight format |
| weights and biases / mlflow | `wandb` or `mlflow` | latest | Experiment tracking | Reference from LaminDB Run records |
| optuna | `optuna` | `>=4.0` | Hyperparameter sweeps | Default sweeper |
| einops | `einops` | `>=0.8` | Tensor manipulation | Universal default |
| scikit-learn | `scikit-learn` | `>=1.5` | Classical ML baselines | Universal default |

**Alternatives considered:**
- TensorFlow: ecosystem momentum has moved to PyTorch in neuroimaging; keep available for legacy code only.
- Hugging Face Datasets: useful but its data model does not fit BIDS / NWB cleanly; prefer TorchIO + native loaders.

---

## 8. Provenance, catalog, distribution

Governance, lineage, dataset distribution. Scoped per the LaminDB discussion: LaminDB at the catalog and run-lineage tier; DataLad at the raw dataset versioning tier; DANDI for NWB submission; OpenNeuro for BIDS submission.

| Package | pip name | Pin floor | Role | Why default |
|---|---|---|---|---|
| LaminDB | `lamindb` | `>=0.76` | Artifact registry + Run / Transform lineage + Feature curation | Default provenance / catalog layer |
| bionty | `bionty` | `>=0.50` | LaminDB plugin for biomedical ontologies (MONDO, HP, NCIT, UBERON, CL, NCBI Taxon, Ensembl, etc.) | Default ontology resolver inside LaminDB |
| DataLad | `datalad` | `>=1.1` | Git-annex-based dataset versioning | Default for raw BIDS distribution; pair with system git-annex |
| DataLad-next | `datalad-next` | `>=1.5` | Modern DataLad extensions | Recommended companion |
| DANDI client | `dandi` | `>=0.65` | DANDI archive submission (also in §4) | Default NWB submission path |
| OpenNeuro Python client | `openneuro-py` | `>=2024.2` | Programmatic OpenNeuro pull | Default for OpenNeuro dataset acquisition |
| Pooch | `pooch` | `>=1.8` | Lightweight downloads with checksum verification | Default for non-DataLad small-data downloads |
| Zenodo API client | `zenodopy` or `pyzenodo3` | latest | Zenodo DOI minting | Default for tagged releases |

**Alternatives considered:**
- MLflow tracking server as primary provenance: too coarse on data lineage; use it for ML experiments and reference it from LaminDB.
- DVC: less biomedical-aware than LaminDB; DataLad covers the dataset-versioning role better.
- Pachyderm / Quilt / Polyaxon: heavyweight relative to the LaminDB + DataLad pair.

---

## 9. Single-line install for the org-wide default Python stack

For any new Cytognosis neuroimaging / neuroelectrophysiology repo, this is the floor. Extras (`[ml]`, `[nwb]`, `[graph]`, `[ephys]`) split heavier optional sets in `pyproject.toml`.

```bash
pip install \
  "linkml>=1.8" "linkml-runtime>=1.7" "pydantic>=2.6" "oaklib>=0.6" \
  "phenopackets>=2.0" "ga4gh.vrs>=2.0" "jsonschema>=4.21" "rdflib>=7.0" \
  "zarr>=3.0" "hdmf-zarr>=0.10" "h5py>=3.12" "pyarrow>=18.0" \
  "xarray>=2024.10" "netCDF4>=1.7" "tiledb>=0.32" "tiledbsoma>=1.13" \
  "tiledbvcf>=0.34" "polars>=1.10" "fsspec" "s3fs" "gcsfs" \
  "pybids>=0.16" "bids-validator>=2.0" "cubids>=1.2" "heudiconv>=1.3" \
  "templateflow>=24.2" "fitlins>=0.12" "bidsschematools" \
  "pynwb>=2.8" "hdmf>=3.14" "neuroconv>=0.7" "nwbinspector>=0.6" \
  "ndx-hed>=0.1" "nwbwidgets>=0.11" "dandi>=0.65" \
  "fmriprep>=24.1" "mriqc>=24.0" "smriprep>=0.16" "qsiprep>=0.23" \
  "nibabel>=5.3" "nilearn>=0.11" "nipype>=1.10" "neuroHarmonize>=2.4" \
  "brainspace>=0.1.10" "dipy>=1.9" "brainstat>=0.4" "nimare>=0.4" "abagen>=0.1.4" \
  "hedtools>=0.5" \
  "torch>=2.4" "lightning>=2.4" "transformers>=4.45" "accelerate>=0.34" \
  "peft>=0.13" "torchio>=0.20" "monai>=1.4" "torch-geometric>=2.6" \
  "scvi-tools>=1.2" "timm>=1.0" "mamba-ssm>=2.2" "learn2learn>=0.2" \
  "safetensors>=0.4" "einops>=0.8" "scikit-learn>=1.5" "optuna>=4.0" \
  "lamindb>=0.76" "bionty>=0.50" "datalad>=1.1" "datalad-next>=1.5" \
  "openneuro-py>=2024.2" "pooch>=1.8"
```

Heavy optionals (do not include by default):
- `wandb` or `mlflow` (pick one per repo, reference from LaminDB Runs)
- `jax`, `flax` (only when a project actually uses them)
- `dgl` (only when torch-geometric does not cover the use case)
- `tensorflow` (legacy only)

---

## 10. System-level dependencies (not pip-installable)

These are non-Python and must be available in the container or workstation image. Listed in full for cross-reference; rationale in `fMRI_pipeline_defaults_2026.md`.

| Tool | Role | Install |
|---|---|---|
| dcm2niix | DICOM-to-NIfTI binary | `apt install dcm2niix` or conda-forge |
| FSL 6.0.7+ | mcflirt, topup, BBR, MELODIC, ICA-FIX | own license; FSL installer |
| FreeSurfer 7.x | surface reconstruction | non-commercial license |
| ANTs | symmetric normalisation, N4 | `apt install ants` |
| AFNI | 3dDespike, 3dvolreg, 3dTproject | `apt install afni` |
| Connectome Workbench | GIFTI / CIFTI / dtseries | `apt install connectome-workbench` |
| Apptainer / Singularity | run BIDS-Apps | `apt install apptainer` |
| Docker | run BIDS-Apps locally | docker.com installer |
| git-annex | DataLad backend | `apt install git-annex` |
| Deno + bids-validator | official BIDS validator | `apt install deno`; `deno install -A -g -n bids-validator jsr:@bids/validator` |
| Nextflow | cohort-scale BIDS-App orchestration | `curl -s https://get.nextflow.io \| bash` |
| Node.js | OpenNeuro CLI, NiiVue | `apt install nodejs npm` |
| OpenNeuro CLI | submission to OpenNeuro | `npm install -g @openneuro/cli` |
| NWB GUIDE | no-code NWB conversion app | desktop installer |
| Neurosift | browser NWB / DANDI viewer | `npx neurosift` |
| HDFView | GUI HDF5 inspector | HDF Group download |

---

## 11. Versioning policy

* **Pin floors, not ceilings**, in repo-level `pyproject.toml`. Ceilings live in lock files (`uv.lock` or `poetry.lock`).
* **Reproducibility tier**: every published Cytognosis dataset stamps the exact pinned versions of fMRIPrep, MRIQC, QSIPrep, sMRIPrep, NWB schema, HED schema, BIDS schema, and the LinkML schema commit in its `dataset_description.json`. This matches the RBC pattern.
* **Container hashes**: every BIDS-App invocation records the Docker / Singularity SHA256 in a sidecar; LaminDB Run captures it automatically when called via `ln.track()`.
* **Schema bumps**: a Cytognosis Schema Review Board (one open issue + 48 hr review) signs off on major LinkML schema changes; minor changes are squashed monthly. Generated artifacts (Pydantic, JSON Schema, LaminDB migrations, TileDB schemas) regenerate on every PR via CI.
* **Atlas, HED, NWB, BIDS schema versions** pin in dataset description, never inferred from "latest".

---

## 12. Cross-references

* Pipeline rationale and BIDS-App container tags: `papers/fMRI/fMRI_pipeline_defaults_2026.md`.
* Per-paper architecture and methodology survey: `papers/fMRI/01_methods_architectures_2026.md`.
* Cross-paper dataset and cohort matrix: `papers/fMRI/02_data_cohorts_2026.md`.
* Tools and standards survey including NWB curated catalogues: `papers/fMRI/03_tools_standards_2026.md`.
* Cytognosis dev-standards (cookiecutter, ruff, mypy, nox, pre-commit) skill in the workspace lives under `.config/Claude/.../skills/dev-standards/`.
* Cytos package design notes (`cytos.yaml` profile bound to ROCm + PyTorch + Lightning + JAX): see `schema-survey-2026-05/cytos_design/`.

---

## 13. Short rationale for the revised grouping

The five groups proposed in the prompt (storage, preprocessing, nwb, bids, ml) cover the bulk of what a neuroimaging Python stack needs, but they leave three roles homeless. The eight-group structure above maps cleanly onto the four-layer Cytognosis architecture (schemas, storage, transformation, governance), each of which has a Python tier:

* **Schemas and standards** is the layer where LinkML, ontology toolkits, Phenopackets, and GA4GH VRS / VRS-Cat / VA live. None of those fit inside "storage" or "ML" but they are part of every Cytognosis dataset.
* **HED event annotation** is a cross-cutting standard that touches BIDS (events.tsv) and NWB (ndx-hed) and is now mandatory for task-fMRI work. It deserves its own group because skipping it would be the single largest predictable Milestone 1 omission.
* **Provenance, catalog, distribution** is where LaminDB and DataLad live. LaminDB provides the run-lineage graph that none of the other groups produce; DataLad provides the dataset-versioning that none of the others produce.

Net: eight groups, sixty-something pip packages, one consolidated install line, one versioning policy, one set of generated artifacts driven by LinkML. This is the org-wide default surface; project-level `pyproject.toml` extras compose against it.

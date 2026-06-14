# Component Restructure — Implementation Status

> Branch: `feat/component-restructure` | Pushed to `origin`

## Phase 1: Component Restructuring ✅

| Change | Status |
|--------|--------|
| `core/` → `base/`, `base.yaml` → `core.yaml` | ✅ |
| Jinja2 extras in `dev.yaml` | ✅ |
| `datascience/` → `data/`, remove `datascience.yaml` | ✅ |
| `schema.yaml` moved to `data/`, updated deps | ✅ |
| `databases.yaml` created (zenodopy, pyDataverse, etc.) | ✅ |
| DL consolidation (`dl.yaml` + `dl-core.yaml` + `ot.yaml` → `dl.yaml`) | ✅ |
| `flash-attn.yaml` created (conditional CUDA/ROCm) | ✅ |
| ROCm `pip_args` in `model-viz.yaml` | ✅ |
| Storage renames (`genomics-store`, `neuro-store`) | ✅ |
| Bio analytics modality folders (`genomics/`, `sc/`, `neuro/`) | ✅ |
| `neuro-bids.yaml`, `neuro-nwb.yaml`, `bio-schemas.yaml` created | ✅ |
| Framework components no longer extend `dl-core` | ✅ |

## Phase 2: Environment Hierarchy ✅

**New hierarchy:**
```
base → data → omics (genomics + single-cell)
             → neuro (neuroimaging)
       ml → graph-ml (interactome graph)
       cytognosis = graph-ml + omics + neuro + *-ml components
```

| Environment | Inherits | Status |
|-------------|----------|--------|
| `base` | — | ✅ |
| `data` | base | ✅ |
| `omics` | data | ✅ |
| `neuro` | data | ✅ |
| `ml` | data | ✅ |
| `graph-ml` | ml | ✅ |
| `cytognosis` | graph-ml, omics, neuro | ✅ |

**Removed:** datascience, etl, bio, bio-interactome, bio-ml, ml-base, interactome

**env_manager upgrades:**
- Direct `dependencies:` and `pip_args:` in environment configs
- New `sync` CLI command with auto-detect lockfile

## Phase 3: Dependency Conflict Resolution ✅

| Package | Issue | Resolution |
|---------|-------|------------|
| `linkml-arrays` | numpy<2, zarr<3 | Excluded, install separately |
| `learn2learn` | qpth broken metadata | Excluded |
| `mamba-ssm` | Build issues | Excluded |
| `fmriprep/mriqc/qsiprep` | scikit-learn<=1.4 | Excluded (isolated envs) |
| `cubids` | numpy<=2.2.4 | Excluded |
| `nwbwidgets` | plotly==5.x | Excluded |
| `bids-validator>=2` | Node.js tool | Removed |
| `fitlins>=0.12` | Not published | Removed |
| `hdmf-common-schema` | Not a pip package | Removed |
| `linkml-phenopackets` | Not on PyPI | Removed |
| `pygeos` | Python 3.13 incompatible | Removed from locks |
| `onnxruntime-rocm` | Cross-compile platform mismatch | Use base onnxruntime for lock |
| `squidpy` | Relaxed to >=1.5 | ✅ |

## Phase 4: Lock Generation & Environment Sync ✅

| Lockfile | Lines | Status |
|----------|-------|--------|
| `cytognosis-linux-rocm-py313.uv.lock` | 4,905 | ✅ |
| `cytognosis-linux-cpu-py313.uv.lock` | 4,913 | ✅ |
| `data-linux-py313.uv.lock` | 3,050 | ✅ |

| Mamba Env | Packages | Status |
|-----------|----------|--------|
| `cytognosis` (ROCm) | ~1,000 | ✅ Synced |
| `etl` (data lockfile) | ~724 | ✅ Synced |

## Tests

- **812 passed**, 0 failed (excluding slow network-dependent resolution tests)
- All config validation, component graph, and when-block tests pass

## Commits

1. `feat: restructure components and environments` (57 files)
2. `feat: add 'sync' CLI command with auto-detect lockfile`
3. `fix: resolve dependency conflicts in bio/neuro components`
4. `fix: add 'build' subcommand to test_resolve helper`
5. `fix: remove pygeos from lockfiles (Python 3.13 incompatible)`

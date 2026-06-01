# End-to-End Platform Validation & Tutorial Generation

> **Status:** DEFERRED — Resume after Cytoskeleton Structural Refactor is complete.
> **Depends on:** Cytoskeleton Refactor (assets/, VFS, manifests, adapter system)

## Goal

Create a reproducible, end-to-end tutorial using `cytocast` to validate Strix Halo hardware, query the massive semantic KG, and process Brain Cell Atlas single-cell data.

## Prerequisites (from Refactor)

- [ ] `assets/` folder structure finalized and DVC-tracked in cytoskeleton
- [ ] VFS adapter system working with GCS and local backends
- [ ] Manifest format finalized with SWHID identity
- [ ] `cytos` dataset ingestion tooling updated to use new asset/adapter patterns
- [ ] `cytoskeleton` installable as dependency across all repos

---

## Workstream 5A: `cytocast` Package Creation & Hardware Validation

### Steps
1. Create a new package using `cytocast` with `data` and `ml` components enabled (which includes `scvi-tools`, `jax`, `pytorch`).
2. Ensure the package correctly identifies `strix-halo` architecture.
3. Validate locked environments are detected and installed correctly.
4. Run `python -c "import scvi"` to verify scvi loads.
5. Verify PyTorch and JAX both see the GPU.
6. Run small matrix-vector and matrix-matrix benchmarks to confirm GPU acceleration.

### Validation Script
- Move `scripts/check_rocm.py` logic into `src/cytoskeleton/hardware/` module.
- Expose via `nox -s hardware_check`.

---

## Workstream 5B: Knowledge Graph Subgraph Extraction

### Data Source
Use the **final, massive semantic KG** (with all node types including semantic and molecular) previously generated and loaded into Neo4j on `cytohost`.

### Steps
1. Ensure `cytos` is installable via `pip install cytos` from internal PyPI.
2. Connect to the central Neo4j database on `cytohost`.
3. Extract the induced subgraph and 1-hop neighborhood of 14 psychiatric disorders:
   ```python
   disorders = [
       "MONDO:0007661", "MONDO:0005351", "MONDO:0008114",
       "MONDO:0002009", "MONDO:0005618", "MONDO:0005146",
       "MONDO:0005258", "MONDO:0007743", "MONDO:0007079",
       "MONDO:0005530", "MONDO:0008575", "MONDO:0005015",
       "MONDO:0005180", "MONDO:0004975"
   ]
   ```
4. Track the extraction via DVC.

---

## Workstream 5C: Brain Cell Atlas Single-Cell Ingestion

### Data Source
[Brain Cell Atlas](https://www.braincellatlas.org/) — specifically the **ADULT BRAIN** dataset.

### Steps
1. **[NEW]** `cytos/data/brain_cell_atlas.py` — Add a function to download datasets from the Brain Cell Atlas, parameterized by dataset type (`ADULT_BRAIN`, `FETAL_BRAIN`, `TUMOUR`, `ORGANOID`).
2. Track raw downloads via DVC for digestion.
3. Fully harmonize the dataset using `cytos` tooling:
   - Map to HRA/CCF coordinates
   - Normalize cell type annotations
   - Apply standard QC filters
4. Store the harmonized dataset as a **TileDB-SOMA** database on the GCP storage bucket.

---

## Workstream 5D: Tutorial Notebooks

### Tutorial 1: Hardware & Package Setup
- **[NEW]** `cytos/docs/tutorials/01_hardware_and_package_setup.ipynb`
- Demonstrates: package creation via `cytocast`, pip install from internal PyPI, environment locking, hardware validation.

### Tutorial 2: KG & Single-Cell Workflows
- **[NEW]** `cytos/docs/tutorials/02_kg_and_single_cell_workflows.ipynb`
- Demonstrates: extracting the 14-disorder subgraph from cytohost Neo4j, `ADULT BRAIN` TileDB-SOMA ingestion/harmonization.

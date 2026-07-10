# Data: Storage, Format, and Metadata Mapping

Scope: how to describe a dataset so a system can find it, load it, validate it, and feed it to a model. Five sub-questions:

1. Where does the data live (storage location and access)?
2. What is the on-disk and in-memory format?
3. What is the nature of the data (omics, imaging, EHR, networks, time series)?
4. How do data dimensions map to metadata (which axis is "samples" and what is the schema for sample-level annotation)?
5. How are units, types, and value semantics encoded?

## 1. Storage location and access

### Cloud-native and chunked formats win

The 2025 reality for datasets that are too big for local disk is: chunked + columnar + cloud-native. The two dominant patterns are:

- **Zarr** (and **OME-NGFF / OME-Zarr** for imaging): chunked N-dim arrays, accessed over S3/GCS/Azure via `fsspec`. Each chunk is a key in object storage. [OME-NGFF / OME-Zarr](https://ngff.openmicroscopy.org/) is reaching [version 1.0 in 2025](https://gerbi-gmb.de/2025/07/02/next-generation-file-formats-for-bioimaging/), the long-awaited stable spec.
- **Apache Parquet** (with **Arrow** in memory): columnar tabular at scale. Used everywhere from genomic VCF replacement to EHR warehouses. [Arrow 22.0](https://dev.to/alexmercedcoder/2025-year-in-review-apache-iceberg-polaris-parquet-and-arrow-4l1p) shipped in 2025.

For tabular sparse "cells x genes" data at census scale, **TileDB-SOMA** is purpose-built: cloud-native, AnnData-compatible, used for the CZ CELLxGENE Census of 44M cells. [TileDB-SOMA repo](https://github.com/single-cell-data/TileDB-SOMA).

### Recommendation for storage

- **Bulk omics, in development**: AnnData h5ad on local disk or a shared volume.
- **Bulk omics, at scale or shared**: AnnData-Zarr or TileDB-SOMA on S3/GCS.
- **Imaging**: OME-Zarr on S3/GCS.
- **Spatial omics**: SpatialData on S3/GCS (Zarr+Parquet, OME-NGFF aligned).
- **Tabular and time series**: Parquet partitioned by a sensible key, queried via DuckDB / Arrow / Polars.
- **Clinical**: FHIR resources in a dedicated server (HAPI/Smile/Firely) or OMOP CDM in a Postgres/BigQuery/Snowflake warehouse. Both have well-known cloud deployments.
- **Provenance and packaging**: RO-Crate as the wrapper for any data export, regardless of storage backend.

## 2. On-disk and in-memory format

### scverse data structures (the omics core)

| Structure | What it stores | Backed by |
|---|---|---|
| **AnnData** | One assay: cells x features, with obs/var/obsm/varm/obsp/varp/layers/uns | h5ad (HDF5), AnnData-Zarr |
| **MuData** | Multiple AnnData assays under one observation index (multimodal: RNA + ADT + ATAC) | h5mu (HDF5) |
| **SpatialData** | Spatial omics with raster images, label masks, points, shapes, tables | Zarr + Parquet, OME-NGFF aligned |
| **TileDB-SOMA** | Tabular single-cell at any scale, cloud-native | TileDB |
| **NWB (Neurodata Without Borders)** | Electrophysiology + behavior + imaging in neuroscience | HDF5 |
| **Loom** | Predecessor to AnnData; still used in Linnarsson lab pipelines | HDF5 |

The AnnData structure is the lingua franca:

- `X`: the main data matrix (`n_obs x n_vars`)
- `obs`: per-observation (cell/sample) annotations as a DataFrame
- `var`: per-variable (gene/feature) annotations as a DataFrame
- `obsm` / `varm`: aligned multi-dim arrays (embeddings, PCA, UMAP)
- `obsp` / `varp`: aligned square matrices (neighborhood graphs, distances)
- `layers`: alternative same-shape matrices (raw, normalized, log, denoised)
- `uns`: unstructured metadata (DE results, dictionaries, model run logs)

This decomposition is what makes AnnData the right shape for "data the model can plug into directly". Every model output is either a new `obsm` (embedding), a new `obs` column (predicted label), a new `layer` (denoised counts), or a new `uns` entry (model card reference).

[anndata docs](https://anndata.readthedocs.io/), [scverse packages](https://scverse.org/packages/), [SpatialData paper, Nat Methods 2024](https://www.nature.com/articles/s41592-024-02212-x).

### General-purpose formats

| Format | Use case | Strengths | Limits |
|---|---|---|---|
| **HDF5** | Local, large arrays, hierarchical | Mature, widely supported | Not cloud-native; concurrent writes hard |
| **Zarr** | Same shape as HDF5 but cloud-native | S3/GCS friendly, parallel read/write | Newer ecosystem |
| **Parquet** | Columnar tabular | Fast scans, predicate pushdown | Not great for dense N-dim arrays |
| **Arrow** | In-memory, zero-copy | Cross-language, GPU-friendly | Not on-disk persistent |
| **Feather** | Arrow on disk | Fast | Less ecosystem than Parquet |
| **Iceberg / Delta / Hudi** | Lakehouse table formats | Schema evolution, time travel, transactions | Heavyweight for research |
| **NetCDF / xarray** | Multi-dim labeled arrays (climate, neuro) | Mature labeled-axis semantics | Not as cloud-native as Zarr (though netCDF-Zarr exists) |

### Clinical formats

- **FHIR** (HL7): JSON or XML resources, REST API. Best for live clinical data exchange.
- **OMOP CDM v5.4** (OHDSI): SQL-table layout, built for retrospective observational research. The standardized vocabularies are the hard part to model around.
- **CDISC SDTM** (Study Data Tabulation Model): the regulatory submission format (FDA, PMDA). [SDTM site](https://www.cdisc.org/standards/foundational/sdtm).
- **CDISC ADaM** (Analysis Data Model): one step downstream, for analysis-ready datasets and traceability to SDTM.
- **CDISC 360i (2025)**: standards-driven automation initiative, worth tracking but not yet mature.

### Recommendation for format

- **In-memory model-ready**: AnnData / MuData / SpatialData (scverse).
- **On-disk archival**: AnnData-Zarr or TileDB-SOMA for omics; OME-Zarr for imaging; Parquet for tabular sensors and EHR exports; FHIR Bundle JSON when interoperating with clinical systems.
- **Lakehouse, when the team adopts one**: Iceberg over Parquet for the warehouse layer.

## 3. Nature of data: domain typing

A dataset registry needs a controlled vocabulary for "what kind of data is this". Existing options:

### EDAM Data and Format

[EDAM Data](https://edamontology.org) covers the *what is the data* axis (sequence, alignment, annotation, gene expression matrix, image, network), and EDAM Format covers the *how is it serialized* axis (FASTQ, BAM, GFF3, MTX, h5ad, Zarr, OME-Zarr). Both are Bioregistry-resolvable. For a Cytognosis dataset, an EDAM Data + EDAM Format pair plus an EDAM Topic (the application domain) gives discoverability across bio.tools, Galaxy, and other EDAM-aware tooling.

### schema.org / Bioschemas

[Bioschemas](https://bioschemas.org) extends schema.org with life-sciences profiles: `Sample`, `BioChemEntity`, `Gene`, `Protein`, `Taxon`. Useful for SEO-style discoverability and aligns with Croissant.

### Croissant `RecordSet` typing

Croissant 1.x lets you type each `RecordSet` (a logical table) and each `Field` semantically (input/label/weight, plus a domain term). The life-sciences extension to Croissant is the right place to add bio-specific semantic typing.

### Recommendation for nature

Tag every Cytognosis dataset with:
- An EDAM Data CURIE.
- An EDAM Format CURIE.
- A Croissant `dct:conformsTo` reference if a domain profile (single-cell-curation, BIDS, OMOP) applies.
- Bioschemas annotations for any web-published resource.

## 4. Dimension-to-metadata mapping

This is the part that AnnData solves elegantly and that ad-hoc CSV pipelines do badly. The principle: for every axis of the data tensor, there should be an aligned annotation table.

### AnnData and its descendants

AnnData enforces:
- Every entry in `obsm`, `obsp`, `layers` is shape-aligned to `n_obs`.
- Every entry in `varm`, `varp` is shape-aligned to `n_vars`.
- Pandas index alignment for `obs` / `var`.

This is the mapping the user references in the prompt and is the right pattern. Replicate it for non-omics data structures:

- **MuData**: each modality is its own AnnData, with a `mod` dict and a global `obs` index that joins across modalities (where samples are shared).
- **SpatialData**: five primitive elements (Images, Labels, Points, Shapes, Tables), each with their own coordinate system and transformations. The Tables can be AnnData/MuData and can reference Shapes (e.g., spatial points).
- **NWB**: per-modality "interfaces" with shared time alignment.
- **BIDS**: directory structure encodes the alignment; sidecar JSONs carry per-axis metadata.

For tabular non-omics data (a sensor stream, a lab panel time series), the analog is "Parquet table with a well-typed schema and a sidecar manifest". Frictionless Data Package and Croissant both fill that role; LinkML lets you author the schema once and emit both.

### LinkML and the meta-schema

[LinkML](https://linkml.io/) is the right authoring layer. You write classes, slots, and enumerations once, with semantic anchors (CURIEs from CL, UBERON, EFO, etc.), and get JSON Schema, SHACL, OWL, Pydantic, Python classes, SQL DDL, GraphQL out of it. The Biolink Model, NMDC, NCATS Translator, Monarch, and the Center for Cancer Data Harmonization all use it.

[LinkML paper, GigaScience 2025](https://academic.oup.com/gigascience/article/doi/10.1093/gigascience/giaf152/8378082).

### Frictionless Data Package

[Frictionless Table Schema](https://specs.frictionlessdata.io/table-schema/) is a lightweight JSON descriptor (`name`, `type`, `format`, `unit`, `constraints`) for tabular data. It is fine for simple cases and integrates well with R and Python via the `frictionless` packages. For any non-trivial Cytognosis use case, prefer LinkML and let LinkML emit a Frictionless descriptor as one of its outputs.

### Recommendation for dimension mapping

- **Omics**: AnnData / MuData / SpatialData (scverse).
- **Other**: a LinkML-authored class hierarchy that mirrors the AnnData pattern (an axis class with an aligned annotation class), with Croissant export for ML and Frictionless export for general tooling.

## 5. Units, types, and value semantics

Already covered in [sensors.md](../../../05-Research/neuroverse/schema-survey/sensors.md) section 3. The same model applies at the data layer: per-column or per-channel `value_type`, `unit` (UCUM), `range`, `transformation`, `missing_value_encoding`. These belong on the `var` (or column-level) annotation in AnnData, on the SpatialData Table, on the BIDS sidecar JSON, on the FHIR Observation `valueQuantity`, on the OMOP `unit_concept_id`, etc.

## Provenance, packaging, and identifiers

### RO-Crate and Workflow Run RO-Crate

[RO-Crate](https://www.researchobject.org/ro-crate/) packages a research artifact (data + code + metadata) with JSON-LD over schema.org. [Workflow Run RO-Crate](https://www.researchobject.org/workflow-run-crate/) extends it for execution provenance. Already supported by Nextflow (nf-prov), Snakemake, Galaxy, WfExs. Aligns with [W3C PROV-O](https://www.w3.org/TR/prov-o/).

### PROV-O

The W3C provenance ontology models `Entity`, `Activity`, `Agent`, with `wasGeneratedBy`, `used`, `wasDerivedFrom`. RO-Crate consumes PROV-O. Use it whenever the answer to "where did this dataset come from" matters more than 6 months later, which is always.

### DCAT v3

[DCAT v3](https://www.w3.org/TR/vocab-dcat-3/) became a W3C Recommendation in 2024. It is the dataset catalog vocabulary: `Catalog`, `Dataset`, `DataService`, `Distribution`. Use it for the Cytognosis-internal data portal and for any external data publication.

### DataCite

DOI registration for datasets. Use whenever a Cytognosis dataset needs a citation footprint outside the lab.

### Bioregistry

[Bioregistry](https://bioregistry.io/) is the canonical CURIE prefix registry. Validate every identifier (dataset, sample, gene, ontology term) against it.

### BioCompute Object (BCO)

[IEEE 2791 BioCompute Object](https://www.biocomputeobject.org/) is the FDA-aligned standard for capturing the computational provenance of bioinformatics analyses, especially regulatory ones (NGS-based diagnostics). Heavyweight; adopt only when filing.

### Recommendation for provenance and identifiers

- **Always**: PROV-O metadata embedded in dataset records, Bioregistry CURIEs for every identifier, schema-validated by LinkML.
- **At publication or handoff**: RO-Crate (Workflow Run RO-Crate when from a workflow runner), DCAT entry in any catalog the org maintains, DataCite DOI when the dataset deserves a citation.
- **For regulated work**: BioCompute Object.

## Combined: what a "dataset manifest" looks like

```yaml
identifiers:
  primary: cytognosis.dataset:0001               # Cytognosis-internal CURIE
  doi: 10.0000/example                           # if DOI registered
  bioregistry_validated: true
classification:
  edam_data: data:0918                           # gene expression matrix
  edam_format: format:3590                       # h5ad
  edam_topic: topic:3170                         # transcriptomics
  conforms_to: cellxgene-schema:7.1.0            # single-cell-curation
storage:
  primary_uri: s3://cytognosis-data/...zarr      # AnnData-Zarr
  secondary_uri: gs://cytognosis-mirror/...      # mirror
  size_bytes: 142589321024
  chunks:                                        # chunking spec for Zarr
    obs: 16384
    var: 4096
in_memory:
  format: AnnData
  axes:
    obs:                                         # cells
      n: 1289341
      annotation_class: cytognosis:CellAnnotation
    var:                                         # genes
      n: 38244
      annotation_class: cytognosis:GeneAnnotation
      identifier_scheme: ensembl.gene
      annotation_version: ensembl:111
      canonical_order_sha256: 0xdeadbeef...
sample_metadata_schema: cytognosis:CellAnnotation # LinkML class
feature_metadata_schema: cytognosis:GeneAnnotation
value_semantics:
  X:
    value_type: int                              # raw counts
    unit: '1'
    transformation: identity
  layers.normalized:
    value_type: float
    unit: '1'
    transformation: log1p_cp10k
context:
  sensors:                                       # one or more AssayManifest refs
    - cytognosis.assay:0001
provenance:
  prov_o: ...
  ro_crate: s3://cytognosis-data/.../ro-crate-metadata.json
  generated_by_workflow: nf-core/scrnaseq:2.6.0
  generated_at: 2026-04-15T...Z
license: CC-BY-4.0
access:
  duo_codes: [DUO:0000004]                       # data use restrictions
  controlled: false
```

This is what a model resolves against at match time. The model card declares "I expect data conforming to schema X with feature_axis schema Y at annotation_version Z"; the dataset manifest declares its actual `feature_metadata_schema` and `annotation_version`; the platform's match function compares and either greenlights, transforms, or rejects.

## Sources

- [AnnData docs](https://anndata.readthedocs.io/), [scverse](https://scverse.org/), [scverse packages](https://scverse.org/packages/)
- [MuData GitHub](https://github.com/scverse/mudata)
- [SpatialData docs](https://spatialdata.scverse.org/), [SpatialData paper, Nat Methods 2024](https://www.nature.com/articles/s41592-024-02212-x)
- [TileDB-SOMA](https://github.com/single-cell-data/TileDB-SOMA), [TileDB-SOMA Py docs](https://tiledbsoma.readthedocs.io/)
- [OME-NGFF](https://ngff.openmicroscopy.org/), [OME-Zarr paper](https://link.springer.com/article/10.1007/s00418-023-02209-1), [OME-NGFF Nat Methods 2021](https://www.nature.com/articles/s41592-021-01326-w)
- [Apache Arrow](https://arrow.apache.org/), [Arrow Columnar format](https://arrow.apache.org/docs/format/Columnar.html), [2025 Year in Review](https://dev.to/alexmercedcoder/2025-year-in-review-apache-iceberg-polaris-parquet-and-arrow-4l1p)
- [LinkML site](https://linkml.io/), [LinkML paper, GigaScience 2025](https://academic.oup.com/gigascience/article/doi/10.1093/gigascience/giaf152/8378082), [arXiv 2511.16935](https://arxiv.org/pdf/2511.16935)
- [DCAT v3](https://www.w3.org/TR/vocab-dcat-3/), [DCAT v3 W3C announcement](https://www.w3.org/news/2024/data-catalog-vocabulary-dcat-version-3-is-a-w3c-recommendation/)
- [Frictionless Table Schema](https://specs.frictionlessdata.io/table-schema/), [Frictionless Framework](https://framework.frictionlessdata.io/)
- [PROV-O](https://www.w3.org/TR/prov-o/), [RO-Crate](https://www.researchobject.org/ro-crate/), [Workflow Run RO-Crate](https://www.researchobject.org/workflow-run-crate/)
- [Bioregistry](https://bioregistry.io/), [Bioregistry paper, Sci Data 2022](https://www.nature.com/articles/s41597-022-01807-3)
- [FAIR Genomes Sci Data 2022](https://www.nature.com/articles/s41597-022-01265-x), [FAIR principles](https://www.nature.com/articles/sdata201618)
- [OMOP CDM v5.4](https://ohdsi.github.io/CommonDataModel/cdm54.html), [OHDSI](https://www.ohdsi.org/)
- [CDISC SDTM](https://www.cdisc.org/standards/foundational/sdtm), [CDISC ADaM](https://www.cdisc.org/standards/foundational/adam)
- [single-cell-curation latest](https://chanzuckerberg.github.io/single-cell-curation/latest-schema.html), [repo](https://github.com/chanzuckerberg/single-cell-curation)

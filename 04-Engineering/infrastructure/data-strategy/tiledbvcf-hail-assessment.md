# TileDB-VCF and Hail Assessment: Cytos GenomeKG Storage Architecture

> **Status**: Active
> **Date**: 2026-06-14
> **Author**: @mohammadi
> **Audience**: engineers, computational biologists
> **Tags**: `tiledb`, `vcf`, `hail`, `genomics`, `storage`, `decision`

**Origin**: Imported from `https://github.com/cytognosis/cytos/blob/main/docs/checkpoint/chats/antigravity_raw/b591c0f4-734e-4f01-9f22-9a59ec524204/tiledbvcf_hail_assessment.md` (Antigravity session, 2026-05-~24). This document informs Track 9 storage architecture decisions for cytos GenomeKG.

> [!NOTE]
> **If you only read one section**: §3 (Decision table) and §7 (Decision summary) give you the full picture in under 5 minutes.

---

## 1. TileDB-VCF: what it provides

TileDB-VCF models population-scale VCF data as a **3D sparse array** with dimensions:

- `contig` (chromosome)
- `pos_start` (1-based genomic position)
- `sample` (sample name string)

Each cell stores all VCF fields for that `(position, sample)` combination: `alleles`, `fmt_GT`, `fmt_DP`, `fmt_GQ`, `info_AF`, etc. INFO and FORMAT fields can be materialized as first-class attributes at dataset creation for faster queries.

### What it does well

| Capability | Detail |
|-----------|--------|
| Incremental ingestion | New samples added without re-merging existing data — critical for growing cohorts |
| Region slicing | Fast random access by `chr:start-end` — sub-second for large datasets |
| Sample filtering | Query subset of samples without loading full array |
| Memory-managed batching | `read()` + `continue_read()` for queries exceeding RAM budget |
| Cloud-native | Native S3/GCS support; no local download needed |
| Arrow output | `read_arrow()` to Apache Arrow to Polars/pandas zero-copy conversion |
| Lossless export | Back to VCF/BCF via CLI `tiledbvcf export` |
| gVCF support | Reference blocks stored as sparse ranges |
| CLI + Python + C++ | Three-tier API; C++ core means no JVM overhead |

### Python API surface

```python
import tiledbvcf

ds = tiledbvcf.Dataset(uri="path/to/dataset", mode="r")

df = ds.read(
    attrs=["sample_name", "contig", "pos_start", "alleles", "fmt_GT", "fmt_DP", "info_AF"],
    regions=["chr22:19000000-20000000"],
    samples=["Olivia", "Shahin"]
)

arrow_table = ds.read_arrow(attrs=[...], regions=[...])
```

### Confirmed gaps (must be built)

| Gap | Impact | Mitigation |
|-----|--------|-----------|
| No VRS IDs | Variants have no globally unique IDs | Build VRS annotation layer on top |
| No SO type classification | Variant types not stored semantically | Add SO type at ingestion |
| No KG bridge | No path from TileDB-VCF to Neo4j | Build `cytos.genomics.vcf` bridge layer |
| No pangenome support | Linear-reference only | Use GBZ/GFA for pangenome separately |
| No signal tracks | BigWig/coverage not in scope | Separate TileDB arrays |
| No conditional annotations | No cell-type/tissue context per variant | Store in Neo4j as relationship properties |
| Returns pandas DataFrames | Requires manual conversion to Polars | Wrap `read_arrow()` to `pl.from_arrow()` |

---

## 2. Hail (MatrixTable and VDS): full assessment

Hail is a **Spark-based distributed genomics compute platform**. It is not primarily a storage format — it is an analytics framework. The file formats (MatrixTable, VDS) are storage artifacts of the Hail ecosystem.

### MatrixTable (MT)

- Dense matrix: rows = variants, columns = samples, entries = genotype calls.
- Stored as Hail-partitioned directories (Parquet-like shards).
- **Limitation**: grows super-linearly with cohort size (the N+1 problem).
- Pan-UKBB summary statistics are distributed as MTs on GCS.

### VDS (Variant Dataset) — the sparse replacement

Split into two MatrixTables:

1. **`variant_data`**: rows = variant sites, cols = samples, entries = non-ref calls only. Uses Local Alleles (LA) indexing.
2. **`reference_data`**: rows = reference blocks (gVCF-style), cols = samples.

### Hail trade-off analysis for Cytos

| Dimension | Hail | Verdict |
|-----------|------|---------|
| Scale | Designed for 500K+ samples on cloud clusters | Overkill for personal and cohort scale |
| Local use | Requires JVM + Spark init (slow startup, memory overhead) | Acceptable for batch Pan-UKBB access |
| Format portability | MatrixTable/VDS are Hail-proprietary (no C++ reader) | **Problem**: not language-agnostic |
| Pan-UKBB access | The only practical way to access summary stats | **Must support** as a reader |
| All-of-Us | AoU uses VDS natively; expanding to millions of WGS | Good to support for future scaling |
| Analysis expressiveness | Rich: GWAS, burden tests, PCA, kinship | Useful for batch analytics passes |
| Storage standard | MatrixTable = Hail-only; VDS = Hail-only | Not our canonical format |

**Verdict**: Hail is an analytics execution engine and data exchange format, not a storage standard. We use it to **read** Pan-UKBB and other Hail-distributed data, convert to our canonical formats (Parquet for summary stats, TileDB-VCF for genotypes), and never store anything long-term in Hail format.

---

## 3. Decision table

| Component | Decision | Rationale |
|-----------|----------|-----------|
| **VCF storage (cohort + personal)** | Use `tiledbvcf` as-is | Mature, C++ core, incremental ingest, Arrow output |
| **VCF multi-type (SNP/CNV/SV)** | Separate named TileDB-VCF datasets | `tiledb/vcf/Olivia_snp/`, `tiledb/vcf/Olivia_sv/` |
| **VRS ID annotation** | Build on top, NOT inside TileDB-VCF | Add `vrs_id` as a materialized attribute at ingest time |
| **SO type annotation** | Build on top, stored as `so_term` attribute | Infer at ingest; store in TileDB-VCF + Neo4j |
| **Pan-UKBB summary stats** | Hail reader, convert to GWAS-SSF Parquet | Read MatrixTable once, store as Parquet; no ongoing Hail dep |
| **Pan-UKBB LD matrices** | Hail BlockMatrix reader, convert to TileDB dense | Needs Hail; one-time conversion |
| **All-of-Us / future large WGS** | VDS reader wrapper in `cytos.genomics.vcf` | Support VDS as input format; stub now |
| **Forking TileDB-VCF** | NO — build extension layer instead | Fork maintenance cost too high; use Python wrapper |

### Why NOT to fork TileDB-VCF

1. Core is C++ — fork maintenance is extremely expensive.
2. Our gaps are all at the Python/semantic layer, not the storage engine level.
3. Extension via Python wrapper achieves 100% of our goals without C++ maintenance.
4. We can contribute VRS annotation support upstream if it gains traction.

---

## 4. The `cytos-vcf` extension layer

Instead of forking, build `src/cytos/genomics/vcf.py` as an extension wrapper:

```python
class CytosVCFDataset:
    """
    Extension of tiledbvcf.Dataset with Cytos-specific capabilities:
    - VRS 2.0 ID generation and annotation
    - SO type classification
    - Multi-type VCF management (SNP/CNV/SV as named partitions)
    - Polars-native output
    - KG bridge: variant nodes to Neo4j
    - CRAM co-location
    """

    def __init__(self, base_uri: Path, sample_id: str):
        self._snp = tiledbvcf.Dataset(f"{base_uri}/snp")
        self._cnv = tiledbvcf.Dataset(f"{base_uri}/cnv")
        self._sv  = tiledbvcf.Dataset(f"{base_uri}/sv")

    def ingest_vcf(self, vcf_path, variant_type, annotate_vrs=True, annotate_so=True): ...
    def read(self, regions, variant_types=("snp",), attrs=None) -> pl.DataFrame: ...
    def to_vrs_alleles(self, regions) -> list[VRSAllele]: ...
    def to_kg_nodes(self, regions) -> tuple[list, list]: ...
```

---

## 5. Storage architecture

```
TileDB storage layer (cytos canonical):
├── vcf/
│   ├── Olivia/
│   │   ├── snp/          # tiledbvcf.Dataset — SNP+INDEL VCF
│   │   ├── cnv/          # tiledbvcf.Dataset — CNV VCF
│   │   └── sv/           # tiledbvcf.Dataset — SV VCF
│   ├── Shahin/
│   │   └── snp/
│   └── PEC/
│       └── snp/          # 388-sample cohort
├── ldgm/
│   └── {ancestry}/       # TileDB SPARSE arrays — LDGM precision matrix R⁻¹
├── ld_dense/
│   └── {ancestry}/       # TileDB DENSE arrays — LD covariance matrix R (for SuSiE fine-mapping)
├── haplotypes/
│   └── {sample}/         # Phased haplotype: dim=(chrom,pos,copy), attr=allele
├── tracks/
│   └── {track_id}/       # TileDB arrays for BigWig signals
├── sumstats/
│   └── panukbb/          # Parquet (converted from Hail MatrixTable once)
└── eqtl/
    └── gtex_v10/         # Parquet (eQTL summary stats)

Hail (transient — only for Pan-UKBB ingest):
  gs://ukb-diverse-pops-public/sumstats_release/*.mt  ← read once, convert to Parquet
  s3://pan-ukb-us-east-1/ld_release/                 ← read once, convert to TileDB dense LD

Neo4j (semantic layer on top):
  Variant nodes with vrs_id, so_term, from TileDB-VCF records
  Haplotype nodes linked to Sample and Variant nodes
  All relationships (eQTL, GWAS, precision LD edges from LDGM, CRE)
```

---

## 6. Implementation tasks

### Task 9.12 — TileDB-VCF setup and CytosVCFDataset

```bash
conda install -c tiledb -c conda-forge -c bioconda tiledbvcf
```

- Create dataset schema with VRS + SO materialized attributes.
- Implement `CytosVCFDataset` wrapper class.
- Ingest: Olivia (3 partitions), Shahin (1 partition), PEC cohort (1 partition).

### Task 9.13 — VRS annotation at ingest

- At ingest time: for each VCF record, compute VRS 2.0 ID using `ga4gh.vrs` `vcf_annotator`.
- Store `vrs_id` and `so_term` as materialized attributes.

### Task 9.14 — Hail bridge for Pan-UKBB

- Install Hail in dedicated `pixi` environment (heavy JVM dep — isolate from main env).
- Implement `read_panukbb_sumstats()` — write to `tiledb/sumstats/panukbb/*.parquet`.
- Run once per Pan-UKBB release.

### Task 9.15 — Pan-UKBB LD matrix conversion

- Pan-UKBB `ld_release` contains dense LD covariance matrices (R, not R⁻¹) for fine-mapping.
- Read Hail BlockMatrix format from S3, convert to TileDB dense arrays at `tiledb/ld_dense/{ancestry}/`.
- Note: LDGM precision matrices (R⁻¹) are TileDB sparse; these are complementary, not redundant.

---

## 7. Decision summary

| Question | Decision |
|----------|----------|
| Fork TileDB-VCF? | **No** — extend via Python wrapper (`CytosVCFDataset`) |
| TileDB-VCF for VCF storage? | **Yes** — use upstream, unmodified |
| Hail as canonical storage? | **No** — read-only, transient, convert to Parquet/TileDB |
| Pan-UKBB access? | **Hail reader, one-time convert to GWAS-SSF Parquet** |
| Pan-UKBB LD covariance matrices (R)? | **Hail BlockMatrix to TileDB dense** — used for SuSiE fine-mapping |
| LDGM precision matrices (R⁻¹)? | **TileDB sparse** — graphLD edgelist; sparse inverse of R |
| Haplotype storage? | **TileDB dense per sample** — phased from VCF GT; dim=(chrom,pos,copy) |
| VRS IDs in TileDB-VCF? | **Yes** — materialized attribute added at ingest by our layer |
| SO types in TileDB-VCF? | **Yes** — materialized `so_term` attribute added at ingest |
| Multi-type VCF (SNP/CNV/SV)? | **Separate named TileDB-VCF datasets per type** |
| VDS support (All-of-Us)? | **Stub now, implement when needed** |

---

## 8. Dependencies

```toml
[project.optional-dependencies]
vcf = [
    "tiledbvcf>=0.30",        # install via conda, not pip
    "ga4gh.vrs[extras]>=2.0", # VRS ID generation at ingest
    "cyvcf2>=0.31",           # VCF parsing
    "pysam>=0.22",            # CRAM + tabix
]
hail = [
    # Hail installed separately via conda (JVM + Spark deps)
    # NOT in main pyproject.toml
]
```

System requirements:
- `conda install -c tiledb -c conda-forge tiledbvcf` (includes libtiledbvcf C++ lib)
- Java 11+ (for Hail only — isolated environment)
- `libhts-dev` (for pysam/CRAM support)

---

## Related docs

- [data-infrastructure-overview.md](data-infrastructure-overview.md)
- [lamindb-analysis.md](lamindb-analysis.md)
- [storage-architecture.md](../storage-architecture.md)
- [reproducibility/artifact-vfs-swhid.md](../reproducibility/artifact-vfs-swhid.md)

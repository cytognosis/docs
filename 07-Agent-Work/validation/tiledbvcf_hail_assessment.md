# TileDB-VCF & Hail Assessment for Cytos GenomeKG

> Research assessment — informs Track 9 storage architecture decisions

---

## 1. TileDB-VCF: What It Provides

### Data model
TileDB-VCF models population-scale VCF data as a **3D sparse array** with dimensions:
- `contig` (chromosome)
- `pos_start` (1-based genomic position)
- `sample` (sample name string)

Each cell stores all VCF fields for that (position, sample) combination: `alleles`, `fmt_GT`, `fmt_DP`, `fmt_GQ`, `info_AF`, etc. INFO and FORMAT fields can be **materialized** as first-class attributes at dataset creation for faster queries.

### What it does well (keep as-is)

| Capability | Detail |
|-----------|--------|
| Incremental ingestion | New samples added without re-merging existing data — critical for growing cohorts |
| Region slicing | Fast random access by `chr:start-end` — sub-second for large datasets |
| Sample filtering | Query subset of samples without loading full array |
| Memory-managed batching | `read()` + `continue_read()` for queries exceeding RAM budget |
| Cloud-native | Native S3/GCS support; no local download needed |
| Arrow output | `read_arrow()` → Apache Arrow → Polars/pandas zero-copy conversion |
| Lossless export | Back to VCF/BCF via CLI `tiledbvcf export` |
| gVCF support | Reference blocks stored as sparse ranges (gVCF-aware) |
| CLI + Python + C++ | Three-tier API; C++ core means no JVM overhead |

### Python API surface (confirmed features)
```python
import tiledbvcf

ds = tiledbvcf.Dataset(uri="path/to/dataset", mode="r")

# Query with region + sample + attribute filtering
df = ds.read(
    attrs=["sample_name", "contig", "pos_start", "alleles",
           "fmt_GT", "fmt_DP", "info_AF"],
    regions=["chr22:19000000-20000000"],
    samples=["Olivia", "Shahin"]
)

# Batched reads for large queries
while not ds.read_completed():
    batch = ds.continue_read()

# Arrow output (zero-copy to Polars)
arrow_table = ds.read_arrow(attrs=[...], regions=[...])

# Dataset introspection
print(ds.samples())          # list all samples
print(ds.attributes())       # list all queryable fields
```

### Confirmed gaps (must be built)

| Gap | Impact | Mitigation |
|-----|--------|-----------|
| **No VRS IDs** | Variants have no globally unique IDs | Build VRS annotation layer on top |
| **No SO type classification** | Variant types not stored semantically | Add SO type at ingestion |
| **No KG bridge** | No path from TileDB-VCF → Neo4j | Build `cytos.genomics.vcf` bridge layer |
| **No pangenome support** | Linear-reference only | Use GBZ/GFA for pangenome separately |
| **No signal tracks** | BigWig/coverage not in scope | Separate TileDB arrays (our design) |
| **No multi-type VCF** | One dataset per VCF file; SNP/CNV/SV must be separate datasets | Manage as named datasets in our layer |
| **No conditional annotations** | No cell-type/tissue context per variant | Store in Neo4j/SurrealDB as relationship properties |
| **Returns pandas DataFrames** | Requires manual conversion to Polars | Wrap `read_arrow()` → `pl.from_arrow()` |
| **TileDB Cloud required for distributed ingest** | Local parallel ingest limited | Use CLI `--threads` for local ingest |

---

## 2. Hail (MatrixTable + VDS): Full Assessment

### What Hail is
A **Spark-based distributed genomics compute platform**. Not primarily a storage format — it is an analytics framework. The file formats (MatrixTable, VDS) are storage artifacts of the Hail ecosystem.

### MatrixTable (MT) — the original format
- Dense matrix: rows = variants, columns = samples, entries = genotype calls
- Stored as Hail-partitioned directories (Parquet-like shards under the hood)
- **Limitation**: grows super-linearly with cohort size (the N+1 problem)
- Pan-UKBB summary statistics are distributed as MTs on GCS (`gs://ukb-diverse-pops-public/sumstats_release/`)

### VDS (Variant Dataset) — the sparse replacement
Split into two MatrixTables:
1. **`variant_data`**: rows = variant sites, cols = samples, entries = non-ref calls only
   - Uses **Local Alleles (LA)** indexing: each sample stores which alleles from the site it carries
   - Prevents storage explosion at multiallelic sites
2. **`reference_data`**: rows = reference blocks (gVCF-style), cols = samples
   - Stores `END`, `DP`, `GQ` for reference intervals
   - Keyed by locus only (no allele dimension)

```python
import hail as hl

vds = hl.vds.read_vds("gs://path/to/vds")

# Access components
variant_mt = vds.variant_data      # non-ref calls
reference_mt = vds.reference_data  # reference blocks

# Densify (expensive — converts to dense MatrixTable)
dense_mt = hl.vds.to_dense_mt(vds)

# Sample QC without densification
sample_qc = hl.vds.sample_qc(vds)

# Filter samples
vds_filtered = hl.vds.filter_samples(vds, samples_to_keep)
```

### Pan-UKBB access via Hail
```python
# Summary statistics in MatrixTable format
mt = hl.read_matrix_table(
    "gs://ukb-diverse-pops-public/sumstats_release/results_full.mt"
)
# Columns: phenotype metadata
# Rows: variant (locus, alleles)
# Entries: BETA, SE, Pvalue, AF, N per phenotype-ancestry combination

# Helper from pan_ancestry repo
from ukb_common import load_final_sumstats_mt
mt = load_final_sumstats_mt(filter_sumstats=True, filter_variants=True)
```

LD matrices also on S3: `s3://pan-ukb-us-east-1/ld_release/` in Hail BlockMatrix format.

### Hail trade-off analysis for Cytos

| Dimension | Hail | Our verdict |
|-----------|------|------------|
| **Scale** | Designed for 500K+ samples on cloud clusters | Overkill for our personal + cohort scale |
| **Local use** | Requires JVM + Spark init (slow startup, memory overhead) | Acceptable for batch Pan-UKBB access |
| **Format portability** | MatrixTable/VDS are Hail-proprietary (no C++ reader) | **Problem**: not language-agnostic |
| **Pan-UKBB access** | The only practical way to access summary stats | **Must support** as a reader |
| **All-of-Us** | AoU uses VDS natively; expanding to millions of WGS | Good to support for future scaling |
| **Analysis expressiveness** | Rich: GWAS, burden tests, PCA, kinship, annotation joins | Useful for batch analytics passes |
| **Interop with TileDB-VCF** | No native bridge; both use Arrow as a common denominator | Arrow as the bridge layer |
| **Storage standard** | MatrixTable = Hail-only; VDS = Hail-only | Not our canonical format |

**Verdict**: Hail is an **analytics execution engine and data exchange format**, not a storage standard. We use it to **read** Pan-UKBB and other Hail-distributed data, convert to our canonical formats (Parquet for summary stats, TileDB-VCF for genotypes), and never store anything long-term in Hail format.

---

## 3. Strategy: What to Build vs. Adopt

### Decision table

| Component | Decision | Rationale |
|-----------|----------|-----------|
| **VCF storage (cohort + personal)** | Use `tiledbvcf` as-is | Mature, C++ core, incremental ingest, Arrow output |
| **VCF multi-type (SNP/CNV/SV)** | Separate named TileDB-VCF datasets | e.g., `tiledb/vcf/Olivia_snp/`, `tiledb/vcf/Olivia_sv/` |
| **VRS ID annotation** | Build on top — NOT inside TileDB-VCF | Add `vrs_id` as a materialized attribute at ingest time |
| **SO type annotation** | Build on top — stored as `so_term` attribute | Infer at ingest; store in TileDB-VCF + Neo4j |
| **Pan-UKBB summary stats** | Hail reader → convert to GWAS-SSF Parquet | Read MatrixTable once, store as Parquet; no ongoing Hail dep |
| **Pan-UKBB LD matrices** | Hail BlockMatrix reader → convert to TileDB | Needs Hail; one-time conversion |
| **All-of-Us / future large WGS** | VDS reader wrapper in `cytos.genomics.vcf` | Support VDS as input format |
| **Pangenome graph** | GBZ + GFA (separate from TileDB-VCF) | TileDB-VCF is linear-reference only |
| **Signal tracks (BigWig)** | TileDB core arrays (not TileDB-VCF) | Already in our design; separate array type |
| **LDGM sparse matrices** | TileDB core sparse arrays | Already decided; not TileDB-VCF's scope |
| **Forking TileDB-VCF** | **NO** — build an extension layer instead | Fork maintenance cost too high; use Python wrapper |

### Why NOT to fork TileDB-VCF
1. Core is C++ — fork maintenance is extremely expensive
2. Our gaps are all at the Python/semantic layer, not at the storage engine level
3. Extension via Python wrapper achieves 100% of our goals without C++ maintenance
4. We can contribute VRS annotation support upstream if it gains traction

### The `cytos-vcf` extension layer

Instead of forking, build `src/cytos/genomics/vcf.py` as an **extension wrapper** that:

```python
# src/cytos/genomics/vcf.py

class CytosVCFDataset:
    """
    Extension of tiledbvcf.Dataset with Cytos-specific capabilities:
    - VRS 2.0 ID generation and annotation
    - SO type classification
    - Multi-type VCF management (SNP/CNV/SV as named partitions)
    - Polars-native output (not pandas)
    - KG bridge: variant nodes → Neo4j
    - CRAM co-location
    """

    def __init__(self, base_uri: Path, sample_id: str):
        self._snp = tiledbvcf.Dataset(f"{base_uri}/snp")
        self._cnv = tiledbvcf.Dataset(f"{base_uri}/cnv")
        self._sv  = tiledbvcf.Dataset(f"{base_uri}/sv")
        self.sample_id = sample_id

    def ingest_vcf(
        self,
        vcf_path: Path,
        variant_type: Literal["snp", "cnv", "sv"],
        annotate_vrs: bool = True,
        annotate_so: bool = True,
    ) -> None:
        """Ingest VCF with VRS ID computation and SO type annotation."""
        ...

    def read(
        self,
        regions: list[str],
        variant_types: list[str] = ("snp",),
        attrs: list[str] | None = None,
    ) -> pl.DataFrame:
        """Polars-native query across multiple variant type partitions."""
        ...

    def to_vrs_alleles(self, regions: list[str]) -> list[VRSAllele]:
        """Return VRS 2.0 Allele objects for variants in region."""
        ...

    def to_kg_nodes(self, regions: list[str]) -> tuple[list, list]:
        """Convert to KGX-compatible node/edge lists for Neo4j."""
        ...

    def read_cram_region(
        self,
        cram_path: Path,
        region: str,
        reference: Path,
    ) -> pl.DataFrame:
        """Co-locate CRAM read-level data with VCF variant calls."""
        ...
```

### Hail reader module

```python
# src/cytos/genomics/hail_bridge.py

def read_panukbb_sumstats(
    gcs_uri: str,
    phenocodes: list[str] | None = None,
    ancestries: list[str] | None = None,
    filter_qc: bool = True,
) -> pl.DataFrame:
    """Read Pan-UKBB MatrixTable → GWAS-SSF Parquet (convert once)."""
    import hail as hl
    hl.init(quiet=True, spark_conf={"spark.driver.memory": "8g"})
    mt = hl.read_matrix_table(gcs_uri)
    # Filter → collect → convert to Polars → write Parquet
    ...
    hl.stop()

def read_vds(vds_uri: str) -> "hl.vds.VariantDataset":
    """Open a Hail VDS (All-of-Us, AoU, etc.)."""
    import hail as hl
    hl.init(quiet=True)
    return hl.vds.read_vds(vds_uri)

def vds_to_tiledb_vcf(
    vds: "hl.vds.VariantDataset",
    output_uri: str,
    samples: list[str] | None = None,
) -> None:
    """Convert VDS → VCF → TileDB-VCF (one-time migration)."""
    ...
```

---

## 4. Updated Storage Architecture

```
TileDB storage layer (cytos canonical):
├── vcf/
│   ├── Olivia/
│   │   ├── snp/          # tiledbvcf.Dataset — SNP+INDEL VCF
│   │   ├── cnv/          # tiledbvcf.Dataset — CNV VCF
│   │   └── sv/           # tiledbvcf.Dataset — SV VCF
│   ├── Shahin/
│   │   └── snp/          # tiledbvcf.Dataset — HC VCF
│   └── PEC/
│       └── snp/          # tiledbvcf.Dataset — 388-sample cohort
├── ldgm/
│   └── {ancestry}/   # TileDB SPARSE arrays — LDGM precision matrix R⁻¹ (NOT LD correlation)
├── ld_dense/
│   └── {ancestry}/   # TileDB DENSE arrays — LD covariance matrix R (for fine-mapping)
│                     # Source: Pan-UKBB ld_release, PLINK2 .bcor, etc.
├── haplotypes/
│   └── {sample}/     # Phased haplotype TileDB array: dim=(chrom,pos,copy), attr=allele
├── tracks/
│   └── {track_id}/   # TileDB dense/sparse arrays for BigWig signals
├── sumstats/
│   └── panukbb/      # Parquet (converted from Hail MatrixTable once)
│       └── {phenocode}/
└── eqtl/
    └── gtex_v10/     # Parquet (eQTL summary stats)
        └── {tissue}/

Hail (transient — only for Pan-UKBB ingest):
  gs://ukb-diverse-pops-public/sumstats_release/*.mt  ← read once, convert to Parquet
  s3://pan-ukb-us-east-1/ld_release/                 ← read once, convert to TileDB dense LD

Neo4j (semantic layer on top):
  Variant nodes with vrs_id, so_term, from TileDB-VCF records
  Haplotype nodes linked to Sample and Variant nodes
  All relationships (eQTL, GWAS, precision LD edges from LDGM, CRE)
```

---

## 5. Implementation Tasks (additions to Track 9)

### 9.12 TileDB-VCF setup and CytosVCFDataset
- Install: `conda install -c tiledb -c conda-forge -c bioconda tiledbvcf`
- Create dataset schema with VRS + SO materialized attributes
- Implement `CytosVCFDataset` wrapper class
- Ingest: Olivia (3 partitions), Shahin (1 partition), PEC cohort (1 partition)
- Test: region query, Arrow output, Polars conversion

### 9.13 VRS annotation at ingest
- At ingest time: for each VCF record, compute VRS 2.0 ID, store as `vrs_id` materialized attribute
- Use `ga4gh.vrs` `vcf_annotator` module (already handles batch VCF annotation)
- Store SO term as `so_term` attribute (inferred from record structure)

### 9.14 Hail bridge for Pan-UKBB
- Install Hail in dedicated `pixi` environment (heavy JVM dep — isolate from main env)
- Implement `read_panukbb_sumstats()` → write to `tiledb/sumstats/panukbb/*.parquet`
- Run once per Pan-UKBB release, then decommission Hail for that dataset
- Add `cytos ingestion panukbb` CLI command

### 9.15 Pan-UKBB LD matrix conversion
- Pan-UKBB `ld_release` contains **dense LD covariance matrices** (R, not R⁻¹) for fine-mapping
- These are different from LDGM (which is R⁻¹, the sparse precision matrix)
- Read Hail BlockMatrix format from S3 → convert to TileDB dense arrays at `tiledb/ld_dense/{ancestry}/`
- Used for SuSiE fine-mapping (requires R directly) — graphLD LDGM used for heritability/PRS (requires R⁻¹)
- Both are needed; they are complementary, not redundant

### 9.16 VDS reader for All-of-Us / future large WGS
- Implement `read_vds()` wrapper in `hail_bridge.py`
- Output: `vds_to_tiledb_vcf()` for local storage of sample subsets
- Not needed for current data — implement stub with TODO

---

## 6. Dependency Summary

```toml
[project.optional-dependencies]
vcf = [
    "tiledbvcf>=0.30",        # core VCF storage — install via conda
    "ga4gh.vrs[extras]>=2.0", # VRS ID generation at ingest
    "cyvcf2>=0.31",           # VCF parsing (pre-ingest processing)
    "pysam>=0.22",            # CRAM + tabix
]
hail = [
    # Hail installed separately via conda (JVM + Spark deps)
    # NOT in main pyproject.toml — in pixi/conda environment only
    # "hail>=0.2.130",
]
```

System requirements:
- `conda install -c tiledb -c conda-forge tiledbvcf` (includes libtiledbvcf C++ lib)
- Java 11+ (for Hail only — isolated environment)
- `libhts-dev` (for pysam/CRAM support)

---

## 7. Decision Summary

| Question | Decision |
|----------|----------|
| Fork TileDB-VCF? | **No** — extend via Python wrapper (`CytosVCFDataset`) |
| TileDB-VCF for VCF storage? | **Yes** — use upstream, unmodified |
| Hail as canonical storage? | **No** — read-only, transient, convert to Parquet/TileDB |
| Pan-UKBB access? | **Hail reader → one-time convert to GWAS-SSF Parquet** |
| Pan-UKBB LD covariance matrices (R)? | **Hail BlockMatrix → TileDB dense** — used for SuSiE fine-mapping |
| LDGM precision matrices (R⁻¹)? | **TileDB sparse** — graphLD edgelist; sparse inverse of R, NOT LD correlation |
| Haplotype storage? | **TileDB dense per sample** — phased from VCF GT; dim=(chrom,pos,copy) |
| VRS IDs in TileDB-VCF? | **Yes** — materialized attribute added at ingest by our layer |
| SO types in TileDB-VCF? | **Yes** — materialized `so_term` attribute added at ingest |
| Multi-type VCF (SNP/CNV/SV)? | **Separate named TileDB-VCF datasets per type** |
| VDS support (All-of-Us)? | **Stub now, implement when needed** |

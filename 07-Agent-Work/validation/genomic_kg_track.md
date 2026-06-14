# Track 9 — Genomic Knowledge Graph (GenomeKG)

> Supplement to the main implementation plan. This is the largest single track.
> Covers: SO ingestion, full GA4GH stack, genome entity model, pangenome, region/signal/interaction layers.

---

## Overview

The GenomeKG is a dedicated knowledge graph sub-system within Cytos that models:

1. **Reference genomes** — linear (GRCh38/hg19) and pangenome (HPRC)
2. **Variants** — typed via Sequence Ontology, identified via VRS 2.0 globally unique IDs
3. **Genomic regions** — CREs, gene bodies, TADs, peaks; conditional + unconditional annotations
4. **Signals** — BigWig/BigBed tracks mapped as node properties on regions
5. **Interactions** — eQTL, LDGM LD blocks, TF→CRE→TG, Hi-C, variant→disease (GWAS/rare)
6. **Individuals/cohorts** — GA4GH Phenopackets + Pedigree linking samples to variants

This is stored across three backends:
- **Neo4j**: semantic entity graph (nodes, relationships, ontology hierarchy)
- **SurrealDB**: observation-level records (sample genotypes, study metadata)
- **TileDB**: bulk numerical data (variant arrays, signal tracks, LDGM matrices)

---

## 9.1 Sequence Ontology Integration

SO is the backbone type system for all genomic features.

### Ingestion pipeline
```
OBO Foundry SO release (so.obo) → pronto parser → SO hierarchy in Neo4j
```

```python
# src/cytos/ontology/so.py  [NEW]
load_so_obo(path: Path) -> nx.DiGraph          # parse SO OBO into NetworkX DAG
so_to_neo4j(graph: nx.DiGraph) -> None         # write SO:XXXXXXX nodes + is_a edges
get_so_term(accession: str) -> SOTerm          # lookup by SO:0001583
get_so_children(term: str, depth: int) -> list # subtree traversal
is_a(child: str, parent: str) -> bool          # subsumption check
```

### Key SO branches used in GenomeKG

| SO branch | SO root term | Examples |
|-----------|-------------|---------|
| sequence_variant | SO:0001060 | SNV, indel, CNV, SV, frameshift, missense |
| structural_variant | SO:0001537 | deletion, duplication, inversion, translocation |
| regulatory_region | SO:0005836 | enhancer, promoter, silencer, insulator |
| gene | SO:0000704 | protein_coding_gene, lncRNA_gene, pseudogene |
| transcript | SO:0000233 | mRNA, ncRNA, primary_transcript |
| sequence_feature | SO:0000110 | exon, intron, UTR, CDS, binding_site |
| chromosomal_structural_variant | SO:1000183 | chromosomal_deletion, ring_chromosome |

SO terms are the `so_term` property on every variant and region node in Neo4j.

---

## 9.2 GA4GH Full Stack

### Standards integrated

| Standard | Version | Purpose | Python package |
|----------|---------|---------|---------------|
| VRS | 2.0 | Globally unique variant IDs + normalization | `ga4gh.vrs[extras]` |
| Cat-VRS | 1.0 (June 2025) | Categorical variant representation (gene-level, class-level) | `cat-vrs-python` |
| VA-Spec | 1.0 (June 2025) | Variant annotation with provenance | `va-spec-python` |
| Phenopackets | 2.0 | Clinical phenotype + genotype packaging | `phenopackets` |
| Pedigree | GA4GH draft | Family structure / inheritance | `phenopackets` (embedded) |
| GWAS-SSF | 1.0 | GWAS summary stats file format | (cytos internal) |
| GWAS-VCF | MRCIEU spec | VCF with FORMAT fields ES/SE/LP | `pysam` |

### VRS 2.0 variant type mapping

```python
# src/cytos/genomics/vrs.py  [NEW — replaces stub in io.py]
from ga4gh.vrs import models

def vcf_record_to_vrs(record, assembly="GRCh38") -> models.Variation:
    """Map cyvcf2 record to correct VRS 2.0 type by SO class."""
    so_class = infer_so_class(record)
    match so_class:
        case "SNV" | "MNV" | "insertion" | "deletion":
            return build_allele(record, assembly)        # VRS Allele
        case "copy_number_gain" | "copy_number_loss":
            return build_cnv(record)                     # VRS CopyNumberChange
        case "translocation" | "inversion":
              return build_adjacency(record)             # VRS Adjacency
        case "tandem_duplication":
            return build_copy_number_count(record)       # VRS CopyNumberCount

def compute_vrs_id(variation: models.Variation) -> str:
    """GA4GH digest-based globally unique ID."""
    from ga4gh.core import ga4gh_identify
    return ga4gh_identify(variation)
```

### Cat-VRS: variant categories
Used for population-level variant classes (e.g., "TP53 loss-of-function variants", "GWAS credible set at locus 22q11"):
```python
# CategoricalVariant node in Neo4j
# Links: (CategoricalVariant)-[:INCLUDES]->(VRSAllele)
#        (CategoricalVariant)-[:DEFINED_BY]->(GWASCredibleSet)
```

### VA-Spec: variant annotations with provenance
```python
# src/cytos/genomics/va.py  [NEW]
build_variant_pathogenicity(vrs_id, classification, evidence_codes, source)
build_variant_functional_impact(vrs_id, so_consequence, vep_score, source)
build_population_frequency(vrs_id, gnomad_af, population_hancestro, source)
```

### Phenopackets ingestion
```python
# src/cytos/genomics/phenopacket.py  [NEW]
load_phenopacket(path: Path) -> Phenopacket
phenopacket_to_kg_nodes(pp: Phenopacket) -> tuple[list[Node], list[Edge]]
# Produces: Individual, Disease, PhenotypicFeature(HPO), GenomicInterpretation nodes
# Monarch phenopacket-ingest pattern: Biolink-compliant mapping

load_pedigree(ped_path: Path) -> list[Individual]
# Maps PED format → GA4GH Pedigree → KG FamilyRelationship edges
```

---

## 9.3 Genome Entity Model

### Node types in Neo4j

```
GenomeAssembly       (GRCh38, GRCh37, T2T-CHM13, HPRC-v1)
Chromosome           (chr1..chrY + alt contigs)
GenomicRegion        (arbitrary interval, base class)
  ├── Gene           (SO:0000704, GENCODE/Ensembl)
  │   ├── Transcript (SO:0000233)
  │   │   ├── Exon   (SO:0000147)
  │   │   └── CDS    (SO:0000316)
  ├── RegulatoryRegion (SO:0005836)
  │   ├── Enhancer   (SO:0000165)
  │   ├── Promoter   (SO:0000167)
  │   ├── CTCF_binding_site
  │   └── TAD_boundary
  └── LDBlock        (graphLD LD block boundary — genomic interval, NOT the matrix)

Variant              (base — has VRS 2.0 ID, SO term, location)
  ├── SNV            (SO:0001483)
  ├── Indel          (SO:1000032)
  ├── StructuralVariant (SO:0001537)
  │   ├── CNV
  │   ├── Inversion
  │   └── Translocation
  └── TandemRepeat   (SO:0000705)

Haplotype            (phased sequence of alleles on one chromosome copy)
  ├── LinearHaplotype    (ordered list of Variant nodes on a contig)
  └── PangenomeHaplotype (path through HPRC variation graph; SO:0001024)

CategoricalVariant   (Cat-VRS — e.g., credible set, gene-level class)
VariantAnnotation    (VA-Spec — pathogenicity, consequence, frequency)
Sample               (Individual or cohort member)
Phenotype            (HPO term)
Disease              (MONDO term)
Study                (GWAS, eQTL, rare variant)
```

### Core relationships

```
(Variant)-[:LOCATED_IN]->(GenomicRegion)
(Variant)-[:IS_A]->(SOTerm)                        # SO subsumption
(Variant)-[:HAS_VRS_ID]->(VRSAllele)
(Variant)-[:ANNOTATED_BY]->(VariantAnnotation)
(Variant)-[:IN_PRECISION_LD {precision_ij, block_id, ancestry}]->(Variant)
  # Edges from LDGM (sparse INVERSE covariance / precision matrix)
  # NOT the raw LD correlation r² — see LD matrix section
(Variant)-[:ASSOCIATED_WITH {p, beta, study}]->(Disease)   # GWAS
(Variant)-[:IS_EQTL_FOR {tissue, pip, beta}]->(Gene)       # eQTL
(Variant)-[:IN_CREDIBLE_SET]->(CategoricalVariant)
(Variant)-[:ON_HAPLOTYPE {phase, source}]->(Haplotype)     # phased haplotype
(Haplotype)-[:BELONGS_TO]->(Sample)
(Haplotype)-[:TRAVERSES {order}]->(PangenomeSegment)       # pangenome path
(Gene)-[:HAS_TRANSCRIPT]->(Transcript)
(Transcript)-[:HAS_EXON]->(Exon)
(RegulatoryRegion)-[:REGULATES {context, evidence}]->(Gene)
(RegulatoryRegion)-[:INTERACTS_WITH {score, assay}]->(RegulatoryRegion)  # Hi-C
(RegulatoryRegion)-[:OVERLAPS]->(Variant)
(Sample)-[:HAS_GENOTYPE {GT, DP, GQ}]->(Variant)
(Sample)-[:HAS_HAPLOTYPE {chrom, copy}]->(Haplotype)       # diploid: copy 1 or 2
(Sample)-[:HAS_PHENOTYPE]->(Phenotype)
(Sample)-[:HAS_DISEASE]->(Disease)
(Sample)-[:MEMBER_OF]->(Cohort)
```

---

## 9.4 Reference Genome & Pangenome

### Linear reference (GRCh38 + T2T-CHM13)
```python
# src/cytos/genomics/reference.py  [NEW]
load_assembly_metadata(assembly: str) -> AssemblyNode
load_chromosomes(assembly: str, fai_path: Path) -> list[ChromosomeNode]
load_gencode_gtf(gtf_path: Path, assembly: str) -> None
# GTF → Gene + Transcript + Exon + CDS nodes in Neo4j
# Uses: pysam.TabixFile for indexed GTF; gffutils for parsing
```

### Pangenome (HPRC)
Storage formats:
- **GFA/GBZ**: graph structure (segments = nodes, links = edges, paths = haplotypes)
- **VCF bubble decomposition**: variant sites in the graph → standard VRS variants
- **GAF**: read alignments to graph

```python
# src/cytos/genomics/pangenome.py  [NEW]
load_hprc_gfa(gfa_path: Path) -> None
# Segments → PangenomeSegment nodes; Links → CONNECTS edges
# Paths → PangenomeHaplotype nodes with TRAVERSES edges

map_linear_variant_to_pangenome(vrs_id: str) -> list[str]
# Returns pangenome node IDs containing this variant

extract_haplotype_path(sample_id: str, chromosome: str) -> list[str]
# Individual haplotype as ordered segment list
```

Tools required: `pysam>=0.22`, `gfapy` (GFA parsing), `vg` (CLI, for GBZ → GFA conversion)

---

## 9.5 Region Annotation Layer

### Annotation types

| Type | Format | Source | Conditionality |
|------|--------|--------|---------------|
| Gene bodies | GTF/GFF3 | GENCODE v46 | Unconditional |
| cCREs | BigBed/BED | ENCODE v3 SCREEN | Unconditional |
| Cell-type enhancers | BED/CSV | PsychENCODE brainSCOPE | Conditional (cell type) |
| Chromatin accessibility | BigWig | ATAC-seq (bulk/sc) | Conditional (cell type) |
| Histone marks | BigWig | ChIP-seq | Conditional (tissue) |
| TAD boundaries | BED | Hi-C derived | Conditional (cell line) |
| CTCF peaks | BED/BigBed | ChIP-seq | Conditional (cell type) |

### Conditional annotation model
```python
# RegionAnnotation node properties:
{
  "region_id": "CRE:chr22:19960000-19961200",
  "annotation_type": "enhancer",
  "so_term": "SO:0000165",
  "context": {"cell_type": "L2/3_IT", "tissue": "PFC"},    # conditional
  "evidence": {"assay": "ATAC-seq", "source": "PsychENCODE"},
  "score": 0.87,
  "is_conditional": True
}
```

### Signal tracks (BigWig mapping)
BigWig tracks are NOT stored as nodes — they are mapped as TileDB arrays and queried on-demand:
```python
# src/cytos/genomics/tracks.py  [NEW]
ingest_bigwig(bw_path: Path, track_id: str, assembly: str) -> None
# Stores in TileDB: dimensions (chrom, position), attribute (score)
# No Python-specific formats

query_signal(region: GenomicInterval, track_id: str) -> pl.DataFrame
# Slice TileDB array by genomic coordinates → Polars DataFrame
# pyBigWig used only for initial reading; output to TileDB

list_tracks(context: dict | None = None) -> list[TrackMetadata]
```

---

## 9.6 Interaction Types

### eQTL (variant → gene expression)
Sources: GTEx v10, PsychENCODE brainSCOPE scQTL, eQTL Catalogue
```python
# src/cytos/genomics/eqtl.py  [NEW]
load_gtex_eqtl(tissue: str, sumstats_path: Path) -> None
load_psychencode_scqtl(h5ad_path: Path, cell_type: str) -> None
# Creates: (Variant)-[:IS_EQTL_FOR {pip, beta, se, tissue, cell_type}]->(Gene)
# Format: susie PIP scores + beta/SE per variant-gene pair
```

### TF → CRE → Target Gene (PsychENCODE GRN)
```python
load_psychencode_grn(csv_path: Path, cell_type: str) -> None
# Creates: (TF:Gene)-[:BINDS_TO]->(CRE:RegulatoryRegion)
#          (CRE)-[:REGULATES {cell_type}]->(TG:Gene)
# Source: PsychENCODE TF-CRE-target CSV files
```

### Region-region interactions (Hi-C / HiChIP)
Format: BEDPE (two genomic intervals + score)
```python
load_region_interactions(bedpe_path: Path, assay: str, cell_type: str) -> None
# Creates: (RegionA)-[:INTERACTS_WITH {score, assay, cell_type}]->(RegionB)
```

### Linkage Disequilibrium matrices — terminology and storage

Two distinct mathematical objects; do NOT conflate:

| Object | What it is | Format | Storage |
|--------|-----------|--------|---------|
| **LD correlation matrix** R | Dense covariance-like matrix; R_ij = correlation between SNPs i and j; typically dense within a block | Various: PLINK `.ld`, Hail BlockMatrix, `.bcor` (PLINK2), compressed HDF5 | TileDB dense array per LD block per ancestry; or leave as Parquet/HDF5 for reference |
| **LD precision matrix** Ω = R⁻¹ | **Sparse** inverse of R; LDGM represents this as a sparse graph (edge = non-zero precision entry); NOT the same as r² | graphLD `.edgelist` + `.snplist`; we store in TileDB sparse | TileDB sparse array, indexed by block + ancestry |

**LDGM is the sparse precision matrix** (R⁻¹), NOT the LD correlation matrix (R). The block-diagonal structure of R means Ω has sparse off-block zeros but within-block structure that graphLD exploits for efficient computation.

**In Neo4j** — LDGM precision edges:
```
(Variant)-[:IN_PRECISION_LD {precision_ij, block_id, ancestry}]->(Variant)
# Only edges where |Ω_ij| > threshold stored in graph
# precision_ij = element of the precision matrix (NOT r²)
```

**Pan-UKBB LD matrices** (from `s3://pan-ukb-us-east-1/ld_release/`) are dense covariance matrices for fine-mapping — stored separately as TileDB dense arrays, NOT LDGM.

### Variant → Disease (GWAS + rare variant)
```python
load_gwas_associations(sumstats: pl.DataFrame, study_id: str) -> None
# p < 5e-8 → (Variant)-[:ASSOCIATED_WITH {p, beta, se, study}]->(Disease)

load_rare_variant_results(results_path: Path) -> None
# gene-collapsing or burden test → (Gene)-[:IMPLICATED_IN {test, p, OR}]->(Disease)
```

### Open Targets Platform edges (already partially done)
- `(Gene)-[:IMPLICATED_IN]->(Disease)` with evidence scores
- Re-use existing Open Targets ingestion, map to new GenomeKG node types

---

## 9.7 Storage Architecture

```
Neo4j (semantic/graph layer):
  SO hierarchy, gene/transcript/exon/CRE nodes
  Variant nodes (VRS IDs, SO terms)
  All relationship types with properties
  Phenopacket individuals, diseases, phenotypes

SurrealDB (observation layer):
  Per-sample genotype records (from TileDB-VCF queries)
  GWAS study metadata
  eQTL study metadata

TileDB (bulk numerical layer):
  tiledb/vcf/Olivia/{snp,cnv,sv}/    Personal VCF partitioned by variant type
  tiledb/vcf/Shahin/snp/             HC VCF
  tiledb/vcf/PEC/snp/                388-sample cohort
  tiledb/ldgm/{ancestry}/            LDGM SPARSE precision matrices (R⁻¹ sparse)
  tiledb/ld_dense/{ancestry}/        Dense LD covariance matrices (R) for fine-mapping
  tiledb/tracks/{track_id}/          BigWig signal tracks
  tiledb/eqtl/                       eQTL summary stats (all tissues)
  tiledb/haplotypes/{sample}/        Phased haplotype arrays (position → allele, per copy)

DuckDB (region/interval index):
  ldgm/index.duckdb           LD block boundaries by ancestry + SNP membership
  regions/index.duckdb        Genomic region BED intervals (fast overlap queries)
```

---

## 9.8 Python Module Layout

```
src/cytos/genomics/
├── __init__.py
├── reference.py        # Assembly metadata, chromosome nodes, GENCODE GTF loader
├── pangenome.py        # GFA/GBZ loading, haplotype paths, HPRC integration
├── vcf.py              # Multi-type VCF loader, CRAM support, variant ingestion
├── vrs.py              # VRS 2.0 type dispatch, ID computation, normalization
├── cat_vrs.py          # Cat-VRS categorical variants, credible sets
├── va.py               # VA-Spec annotations: pathogenicity, consequence, frequency
├── phenopacket.py      # Phenopackets v2 + Pedigree → KG nodes
├── so.py               # SO OBO ingestion, subsumption queries
├── regions.py          # GenomicRegion CRUD, BED/GFF3/BigBed loaders
├── tracks.py           # BigWig/BigBed → TileDB ingestion + query
├── annotations.py      # Conditional annotation model, ENCODE cCRE, GENCODE
├── eqtl.py             # GTEx, PsychENCODE scQTL, eQTL Catalogue loaders
├── grn.py              # TF-CRE-TG GRN loading (PsychENCODE CSV format)
├── interactions.py     # Hi-C BEDPE, region-region, variant-variant
├── gwas.py             # GWAS association → KG edges (threshold + credible sets)
├── munge.py            # EXISTS ✅
├── sources.py          # EXISTS ✅
├── ingest.py           # EXISTS ✅
├── io.py               # EXISTS — refactor: move VRS logic to vrs.py
├── liftover.py         # EXISTS ✅
├── annotate.py         # EXISTS ✅
├── regulatory.py       # EXISTS ✅
├── join.py             # EXISTS ✅
├── prs.py              # EXISTS ✅
├── haplotype.py        # Phased haplotype loading, storage, KG bridge  [NEW]
└── graphld/            # Track 3 submodule
```

---

## 9.9 Standards Evaluation Summary

| Layer | Chosen standard | Alternatives evaluated | Rationale |
|-------|----------------|----------------------|-----------|
| Variant identity | VRS 2.0 (GA4GH) | HGVS, dbSNP rsID | VRS is globally unique, assembly-agnostic, computable |
| Variant typing | SO hierarchy | VEP consequence terms | SO is the OBO standard; VEP terms map to SO |
| Variant categories | Cat-VRS | Custom classes | GA4GH standard, interoperable with VA-Spec |
| Variant annotation | VA-Spec | ClinVar XML, VEP JSON | Provenance-aware, GA4GH interoperable |
| Clinical phenotype | Phenopackets v2 | OMOP CDM, HL7 FHIR | GA4GH, Monarch KG compatible |
| Family structure | GA4GH Pedigree | PED/FAM files | GA4GH computable pedigree |
| Linear variant storage | TileDB-VCF | BCF+tabix, Hail, BGEN | Cloud-native, language-agnostic, incremental |
| Phased haplotype storage | TileDB dense per sample | VCF GT phase, HAP/LEGEND, BGEN | TileDB sliceable by position; VCF phased GT as source |
| LDGM precision matrix (R⁻¹) | TileDB sparse | HDF5, NPZ | Sparse inverse of LD covariance; language-agnostic |
| Dense LD covariance matrix (R) | TileDB dense per block | PLINK .ld, Hail BlockMatrix, .bcor | Dense R needed for fine-mapping; Pan-UKBB ld_release |
| Signal tracks | TileDB array | BigWig (read-only) | BigWig read via pyBigWig; TileDB for storage |
| Pangenome graph | GBZ + GFA | rGFA, HAL | GBZ is HPRC production format; GFA is text/portable |
| Region intervals | BED + DuckDB index | SQLite, tabix | DuckDB for fast overlap queries without a server |
| Interactions | BEDPE (Hi-C), TSV (eQTL) | ENCODE JSON, custom | Standard interchange formats |
| Gene annotation | GTF (GENCODE) + GFF3 | BED12, refFlat | GTF is canonical for GENCODE; GFF3 for SO features |
| Region semantics | SO terms + ENCODE cCRE classes | Custom | SO is the OBO standard |
| Semantic layer | Neo4j (Biolink-compatible) | RDF/SPARQL, TigerGraph | Property graph is more practical; Biolink maps to RDF |

---

## 9.10 New Dependencies

```toml
[project.optional-dependencies]
genomics = [
    "cyvcf2>=0.31",          # VCF parsing
    "pysam>=0.22",           # CRAM, BAM, tabix
    "gffutils>=0.12",        # GTF/GFF3 parsing
    "pyBigWig>=0.3",         # BigWig reading
    "gfapy>=1.2",            # GFA pangenome parsing
    "pronto>=2.5",           # OBO ontology parsing (SO)
    "tiledb>=0.25",          # Core TileDB
    "tiledbvcf>=0.30",       # TileDB-VCF
]
ga4gh = [
    "ga4gh.vrs[extras]>=2.0",     # VRS 2.0 + normalization + VCF annotator
    "cat-vrs-python>=1.0",         # Cat-VRS
    "va-spec-python>=1.0",         # VA-Spec
    "phenopackets>=2.0",           # Phenopackets + Pedigree
    "phenopacket-tools>=2.0",      # Validation + conversion
]
pangenome = [
    "gfapy>=1.2",
    # vg: CLI tool, not a Python package — managed via conda/apt
]
```

System packages: `libhts-dev` (htslib for CRAM), `libsuitesparse-dev` (for graphLD)

---

## 9.11 Execution Sequence within Track 9

```
Phase A (foundation):
  9.1 SO OBO ingestion → Neo4j
  9.3 Reference genome: GRCh38 assembly + chromosome nodes
  9.3 GENCODE GTF → Gene/Transcript/Exon nodes

Phase B (variants):
  9.2 VRS 2.0 + Cat-VRS + VA-Spec modules
  9.4 Personal VCF ingestion (Olivia + Shahin) with VRS IDs
  9.4 TBX1 SV as VA-Spec annotation test case
  9.4 PEC cohort VCF → TileDB-VCF

Phase C (regions + signals):
  9.5 ENCODE cCRE loading → RegulatoryRegion nodes
  9.5 GENCODE regulatory features → SO-typed nodes
  9.5 BigWig track ingestion → TileDB
  9.5 PsychENCODE cell-type enhancers (conditional annotations)

Phase D (interactions):
  9.6 GTEx eQTL → variant-gene edges
  9.6 PsychENCODE scQTL (brainSCOPE)
  9.6 PsychENCODE TF-CRE-TG GRN
  9.6 GWAS credible sets → Cat-VRS + disease edges (PGC)

Phase E (pangenome + clinical):
  9.4 HPRC pangenome GFA/GBZ loading
  9.2 Phenopacket ingestion (Shahin + Olivia as test individuals)
  9.2 Pedigree loading

Phase F (LDGM integration):
  LDGM edges into Neo4j (r² > 0.1 threshold)
  LDGM-GWAS alignment for all PGC traits
```

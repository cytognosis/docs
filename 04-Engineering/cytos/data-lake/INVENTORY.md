# Data Lake Inventory

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: engineers
> **Tags**: `engineering`
> **Variants**: Technical (this doc) - Readable (INVENTORY.md in Obsidian vault: 04-Engineering/cytos/data-lake/) - Agent (n/a)

> Location: `https://github.com/cytognosis/datasets` (~1.5TB total)
> Last audited: 2026-05-22

---

## Canonical Directory Structure

```
~/datasets/
├── 01-ontologies/          ~75GB    OWL/OBO files + registry.yaml
│   ├── owl/                         Flat deduplicated OWL files (37+ ontologies)
│   ├── mappings/                    SSSOM mapping files
│   ├── archive/                     Legacy directory structure (pre-cleanup)
│   └── registry.yaml               Single source of truth for all semantic resources
│
├── 02-vocabularies/        ~76GB    UMLS 2026AA, SNOMED CT INT+US, MeSH
│
├── 03-knowledge-graphs/    ~440GB   Monarch, PrimeKG, PlaNet, Open Targets, PKG2.0
│
├── 04-identifiers/         ~178GB   Ensembl 115, UniChem, OLS4 SSSOM
│   └── ontologies/                  SO, GO, HP, MP, etc. (OBO format)
│       └── so.obo                  ← Sequence Ontology (used by cytos)
│   └── seqrepo/                    ← NOT YET INSTALLED (~50GB needed for VRS)
│
├── 05-annotations/         ~12GB    CellxGene, HRA CCF, topic areas
│
├── 06-genotype/            ~103GB   ALL genotype/WGS data
│   ├── personal/
│   │   ├── Shahin/
│   │   │   ├── NG1CNUL31H.mm2.sortdup.bqsr.hc.vcf.gz     ← HC variant calls
│   │   │   ├── NG1CNUL31H.mm2.sortdup.bqsr.hc.vcf.gz.tbi
│   │   │   ├── NG1CNUL31H.mm2.sortdup.bqsr.cram           ← Full read data
│   │   │   ├── NG1CNUL31H.mm2.sortdup.bqsr.cram.crai
│   │   │   ├── genotypes_ext.tsv                          ← Extended variant table
│   │   │   └── insertion_TBX1.fa                          ← TBX1 SV sequence
│   │   └── Olivia/
│   │       ├── *snp-indel.genome.vcf.gz                   ← SNP+INDEL
│   │       ├── *cnv.vcf.gz                                ← Copy number
│   │       └── *sv.vcf.gz                                 ← Structural variants
│   ├── cohort/
│   │   └── PEC/
│   │       └── brainSCOPE_PEC_sample_genotypes_no_rna.vcf.gz  ← 218 WGS samples
│   ├── gwas/
│   │   └── pgc/             14 PGC psychiatric GWAS files (ADHD, ALCH, AN, ...)
│   ├── ldgm/
│   │   ├── index.duckdb     ← DuckDB block index (1,360 entries)
│   │   ├── ancestry/EUR/    ← Raw edgelist + snplist files (graphLD native)
│   │   └── tiledb/EUR/      ← TileDB sparse Ω arrays (one per block)
│   └── reference/
│       └── gencode.v47.annotation.gtf.gz    ← GENCODE v47 gene annotation
│
├── 07-single-cell/                  TileDB-SOMA (PEC RNA-seq pending)
│   └── PEC/
│       ├── CMC/
│       ├── SZBDMulti-Seq/
│       ├── DevBrain-snRNAseq/
│       └── UCLA-ASD/
│
├── 08-neuroimaging/        ~319GB   BIDS/NWB datasets
│   └── PEC/
│       └── synapse/genotype/WGS-Derived-ImputedGenotypes/   ← PEC RNA imputed VCFs
│
├── 09-literature/                   BibTeX + PDF cache
├── 10-embeddings/          ~34GB    Pre-computed embeddings
├── 11-benchmarks/          ~23GB    Benchmark datasets
├── 12-network/             ~200GB   Biological networks
├── 13-cell-lines/                   Cell line data
├── 14-cohort-metadata/              Sample manifests + IRB + phenotypes
│   └── PEC/
│       └── SYNAPSE_METADATA_MANIFEST.tsv    ← PEC sample manifest
└── 15-databases/                    Database storage
    └── surrealdb/
        └── cytos.db                ← SurrealDB persistent store
```

---

## TileDB-VCF Stores

Location: `https://github.com/cytognosis/cytos/tree/main/tiledb/vcf`
(NOT in git — local disk only)

| Store | Samples | Source | Notes |
|-------|---------|--------|-------|
| `Shahin/snp/` | 1 | HC VCF | 47 attrs including GT, DP, GQ, AD |
| `Olivia/snp/` | 1 | SNP+INDEL VCF | |
| `Olivia/cnv/` | 1 | CNV VCF | |
| `Olivia/sv/` | 1 | SV VCF | |
| `PEC/snp/` | 218 | brainSCOPE WGS | Full cohort |
| `PEC_RNA/snp/` | 226 | RNA-derived imputed | From 08-neuroimaging/PEC |

**Total:** 447 sample-store combinations

---

## GWAS Data in Repo

Location: `https://github.com/cytognosis/cytos/tree/main/data/gwas`

### GWAS Catalog (harmonized, downloaded)
```
gwas_catalog/
├── SCZ_GCST90038608.h.tsv.gz    9.7M variants (SCZ, PMID 35396580)
├── BIP_GCST003724.h.tsv.gz      9.5M variants (BIP, PMID 21926972)
└── MDD_GCST006085.h.tsv.gz     20.0M variants (MDD, PMID 29892016)
```

### PGC (minimal format, downloaded)
```
pgc/
├── ADHD.tsv.gz       ├── AN.tsv.gz         ├── ASD.tsv.gz
├── ALCH.tsv.gz       ├── ANX.tsv.gz        ├── BIP.tsv.gz
├── CANNABIS.tsv.gz   ├── INSOMNIA.tsv.gz   └── [more]
```

---

## Known Data Issues

1. **PEC WGS count:** Expected 388 samples (paper), ingested 218. Remaining ~170 may be
   from a different batch or protected-access tier. RNA-derived VCFs give 226 samples.
   Not a data processing error — the source VCF has 218 samples.

2. **seqrepo not installed:** VRS ID computation requires seqrepo (~50GB).
   Must install before Variant nodes can be created.

3. **PEC RNA location:** PEC RNA-derived VCFs are at `08-neuroimaging/PEC/` (not `07-single-cell/`).
   This is a pre-existing mis-organization; symlinks exist at both locations.

4. **DVC tracked files:** Some data is tracked by DVC with remote at GCS.
   `dvc status` shows `topic_areas` and `monarch_merge` stages have changed deps.
   These are pre-existing (not caused by recent genomics work).

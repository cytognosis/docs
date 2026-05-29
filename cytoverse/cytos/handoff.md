# Cytos Platform — Complete Agent Handoff

> **Written:** 2026-05-22 | **Conversation IDs:** b591c0f4 (GenomeKG), cd6537fc (GWAS/PGC), f78b85f5 (Cytoskeleton/FAIR)
>
> This document is the single entry point for a new agent picking up the Cytos project.
> Read it top to bottom before touching any code.

---

## 1. What Is Cytos?

Cytos (`/home/mohammadi/repos/cytognosis/cytos`) is the **master Cytognosis Python package** — the
data engineering, knowledge graph, and genomic infrastructure layer for the Cytognosis Foundation
platform ("GPS for Health"). It is **not** a user-facing application. It is the substrate that
produces data products consumed by:
- **Cytoverse** (The Map — AI health coordinate system)
- **Cytoscope** (The Sensor — continuous biosensing)
- **Cytonome** (The Navigator — on-device causal AI)

**Core identity:** `cytos` is a data-only Knowledge Graph construction and genomic ingestion system.
Machine learning models are external consumers. Modeling stubs (features/, models/, train/, evaluate/)
exist in src/ but are explicitly deferred to v2.x.

**Package coordinates:**
```
name = "cytos"
version = "2026.5.0"
license = "Apache-2.0"
python = ">=3.13"
```

**Environment:** managed via `pixi`/`uv` from `cytoskeleton` environment hierarchy.
Active conda env: `cytognosis`.

---

## 2. Repository Layout

```
cytos/
├── src/cytos/              ← All Python code (src layout)
│   ├── genomics/           ← PRIMARY FOCUS — 23 modules + graphld/ subdir
│   ├── db/                 ← neo4j/ + surrealdb/ clients
│   ├── schema/             ← LinkML → multi-format pipeline
│   ├── kg/                 ← Knowledge graph builder (DuckDB-based)
│   ├── scholarly/          ← Academic paper/author intelligence (30 files)
│   ├── ontology/           ← Ontology registry + fetcher
│   ├── harmonize/          ← Entity resolver, SSSOM
│   ├── ingest/ sources/ pipelines/ publish/ services/ utils/ validate/
│   └── [stubs] features/ models/ train/ evaluate/ rag/
│
├── schemas/domains/        ← 36 LinkML YAML schemas (source of truth)
├── data/                   ← DVC-tracked data (gwas/, kg/, surreal/)
├── tests/                  ← 143 collected; genomics suite is primary
│   └── genomics/           ← test_genomics_pipeline.py + test_so_hierarchy.py
├── scripts/                ← Ingestion scripts (ingest_ldgm, ingest_gwas_neo4j, etc.)
├── third_party/graphld/    ← graphLD package (installed editable)
├── tiledb/                 ← TileDB-VCF arrays (NOT in git; on local disk)
├── design/                 ← Historical design docs (now mirrored to docs/historical/)
└── docs/                   ← THIS directory — canonical documentation
```

---

## 3. What Has Been Built (Complete)

### Phase 0 — Knowledge Graph Foundation (Pre-session)
Large-scale biomedical KG built from:
- UMLS 2026AA (8.7M nodes, 43.3M edges)
- SNOMED CT RF2 (INT+US)
- 37 OBO/OWL ontologies via Pronto
- UniProt 868K proteins
- Monarch Initiative (1.38M nodes, 15.4M edges)
- PrimeKG, Open Targets 25.03, PKG2.0, PlaNet, UniChem, Ensembl
- HRA CCF (9,493 nodes + spatial placements)
- **Neo4j deployment:** 10.7M nodes × 118.5M edges (pre-GenomeKG)
- **DVC pipeline:** 10 stages in `dvc.yaml`
- **Dagster orchestration:** 5 assets, 3 jobs

### Phase 1 — Scholarly Intelligence (Pre-session)
`src/cytos/scholarly/` — 30 modules:
- Multi-backend PDF parser (Docling + Marker + Surya + PyMuPDF)
- scispaCy + UMLS NER, author identity/profiling
- OpenAlex, Semantic Scholar, ORCID, Zotero integration
- Citation graph, paper profiling, intelligence layer

### Phase 2 — GenomeKG Infrastructure (Sessions 1–3, May 2026)
**This is the main recent work.** See `docs/genomekg/GENOMEKG.md` for full detail.

#### Data Lake Reorganization ✅
- PEC data split: `06-genotype/cohort/PEC/` + `07-single-cell/PEC/` + `14-cohort-metadata/PEC/`
- Canonical 13-directory taxonomy established
- DVC validated clean after move

#### 23 New Genomics Modules ✅
All in `src/cytos/genomics/`:

| Module | Purpose | Status |
|--------|---------|--------|
| `vcf.py` | TileDB-VCF wrapper + CRAM functions | ✅ tested |
| `vrs.py` | VRS 2.0 type dispatch + ID computation | ✅ (seqrepo-blocked for SV) |
| `reference.py` | GRCh38 assembly + GENCODE GTF loader | ✅ tested |
| `so.py` | SO OBO ingestion via pronto + sanitizer | ✅ 18 tests pass |
| `haplotype.py` | Phased haplotype storage + KG bridge | ✅ |
| `regions.py` | GenomicRegion CRUD, BED/GFF3 loaders | ✅ smoke tested |
| `tracks.py` | BigWig → TileDB ingestion + query | ✅ |
| `eqtl.py` | GTEx + PsychENCODE eQTL loaders | ✅ smoke tested |
| `gwas.py` | GWAS-SSF + harmonized + PGC format loader | ✅ tested |
| `pangenome.py` | GFA 1.0/2.0 loader, haplotype paths | ✅ smoke tested |
| `phenopacket.py` | Phenopackets v2 + PED → KG bridge | ✅ smoke tested |
| `graphld/` | graphLD submodule (5 files) | ✅ see below |

#### graphLD Submodule ✅
`src/cytos/genomics/graphld/`:
- `ldgm.py` — LDGM TileDB sparse ingestion + DuckDB index
- `dense.py` — Pan-UKBB dense LD covariance (Hail bridge)
- `analysis.py` — GWAS-LDGM alignment (`align_ldgm_to_sumstats`)
- `interface.py` — Native graphLD library bridge (`load_block_precision`, `align_block_sumstats`, `run_graphreml`, `compute_blup_scores`, `list_blocks`, `load_chromosome_blocks`)

**Key data fact:** 1,360 UKBB LDGM blocks ingested (all 22 autosomes, EUR ancestry).
DuckDB index at `/home/mohammadi/datasets/06-genotype/ldgm/index.duckdb`.
graphLD package installed editable from `third_party/graphld/`.

#### TileDB-VCF Stores ✅
All at `tiledb/vcf/`:
- `Shahin/snp/` — 1 sample (NG1CNUL31H.mm2.sortdup.bqsr.hc.vcf.gz)
- `Olivia/snp/`, `Olivia/cnv/`, `Olivia/sv/` — 1 sample × 3 variant types
- `PEC/snp/` — 218 WGS samples (brainSCOPE cohort)
- `PEC_RNA/snp/` — 226 RNA-derived imputed genotype samples

#### Neo4j GenomeKG ✅
Running at `bolt://localhost:7687` (auth: `neo4j`/`cytognosis2026`):
- 233,878 Gene nodes (GENCODE v47, properties: gene_id, gene_name, chrom, start_bp, end_bp)
- 25 Chromosome nodes (GRCh38)
- 3 Trait nodes (SCZ EFO_0000692, BIP EFO_0000289, MDD EFO_0001663)
- 19,621 GWASHit nodes (p < 5×10⁻⁸, from 3 GWAS Catalog studies)
- 78,687 LOCATED_ON edges (Gene → Chromosome)
- 795,297 NEAR_GENE edges (GWASHit → Gene ±500kb)
- 19,868 ASSOCIATED_WITH edges (GWASHit → Trait)
- **0 Variant nodes** (seqrepo not installed — see blockers)

#### Schema System ✅ (partial)
- 36 domain LinkML YAMLs in `schemas/domains/`
- `schema/export.py`: `export_schema()`, `export_all()`, `push_to_cytoskeleton()`
- Pydantic v2 models for genomics domain in `schema/generated/genomics.py`
- Full `SchemaGenerator` class **not yet implemented**

#### SO OBO ✅
- `so.obo` at `/home/mohammadi/datasets/04-identifiers/ontologies/so.obo`
- Upstream parse bugs fixed (backslash xrefs + PMID spacing) via regex sanitizer in `so.py`
- 2,615 terms, 2,510 is_a edges
- 18-test hierarchy suite: all pass

#### SurrealDB ✅ (partial)
- Docker container `cytos-surrealdb` running at `ws://localhost:8000`
- Client at `src/cytos/db/surrealdb/` — **async context manager bug** (see blockers)
- No genomics schema tables defined yet

#### Test Suite
- 143 tests collected total across all suites
- Genomics: 56 pass, 4 skip (all legitimate infra-conditional skips)
- SO hierarchy: 18/18 pass
- Older suites (scholarly, KG, pipeline): not re-validated in recent sessions

#### Ingestion Scripts
All in `scripts/`:
- `ingest_ldgm.py` — Bulk LDGM 1360-block ingestion
- `ingest_gwas_neo4j.py` — GWAS Catalog (SCZ, BIP, MDD) → Neo4j
- `ingest_pec_vcf.py` — PEC cohort → TileDB-VCF
- `ingest_vcf.py` — Personal WGS → TileDB-VCF

---

## 4. What Is NOT Done (Prioritized)

### Priority 1 — PGC GWAS Ingestion (data present, code needed)
14 PGC psychiatric GWAS files at `data/gwas/pgc/`:
`ADHD, ALCH, AN, ANX, ASD, BIP, CANNABIS, INSOMNIA, MDD, OCD, PTSD, SCZ, TS, TOURETTE`

**Tasks:**
- Extend `ingest_gwas_neo4j.py` for PGC format (uses PGC minimal format: CHR/BP/A1/A2/OR/SE/P)
- Add EFO/MONDO metadata for all 14 traits
- Run ingestion — expect 100–5,000 hits per trait at p<5e-8

### Priority 2 — SurrealDB Schema Fix
- **Bug:** `SurrealClientManager` does not implement async context manager protocol
  - Fix: add `__aenter__`/`__aexit__` to `src/cytos/db/surrealdb/client.py`
- Define genomics tables (Variant, SNP, GWASHit, Trait) via LinkML→SurrealQL transpiler
- `schema/bridges/linkml_to_surreal.py` needs implementation

### Priority 3 — Variant Nodes + VRS
- **Blocker:** seqrepo data not installed (~50GB)
  - Install: `seqrepo pull -i 2021-01-29`
- After seqrepo: implement VRS 2.0 Allele for SNPs → load into Neo4j as Variant nodes
- TBX1 SV → VRS Adjacency object (primary clinical test case)
- Link GWASHit nodes to Variant nodes via rsid matching

### Priority 4 — SchemaGenerator Class
`src/cytos/schema/generator.py` (planned, not built):
```python
class SchemaGenerator:
    def generate_jsonld(domain) → Path
    def generate_pydantic(domain) → Path
    def generate_jsonschema(domain) → Path
    def generate_shacl(domain) → Path
    def generate_all(domains=None) → dict[str, Path]
```
CLI: `cytos schema generate --domains gene,variant --formats jsonld,pydantic`

### Priority 5 — CLI, Makefile, docker-compose
- `Makefile`: `make db-start`, `make db-stop`, `make graphld-download`, `make schema-generate`, `make test`
- `cytos graphld` CLI: `heritability`, `clump`, `blup`, `simulate`
- `docker-compose.yml`: Neo4j + SurrealDB + OLS4 unified
- `dvc.yaml`: add stages for gwas_ingest, vcf_ingest, graphld_validate
- **git push to origin** — currently 19 commits ahead of remote

### Priority 6 — Multi-ancestry LDGM
Currently only EUR (1,360 blocks). Need EAS/AFR/AMR/CSA.
- Download: `cd third_party/graphld && make download_all` (adds ~15GB)
- Ingest via same `scripts/ingest_ldgm.py` (supports any ancestry)

### Priority 7 — Tests and CI/CD
- Run full 143-test suite and fix failures (only genomics subset validated recently)
- Add `test_graphld_pipeline.py` — end-to-end LDGM → graphREML validation
- Add `test_vcf_personal.py` — TBX1 SV + CRAM validation
- Add `test_db_both.py` — same query on Neo4j + SurrealDB
- GitHub Actions CI: ruff + mypy + pytest with infra-conditional skips

---

## 5. Settled Design Decisions

| Decision | Verdict | Rationale |
|----------|---------|-----------|
| Storage format for precision matrices | TileDB sparse arrays | **No NPZ ever** — Python-specific, not language-agnostic |
| GWAS p-value threshold | 5×10⁻⁸ (GWS) | Standard genome-wide significance |
| Gene-hit proximity | ±500kb NEAR_GENE edges | Standard cis-regulatory window |
| Schema source of truth | LinkML YAML in `schemas/domains/` | All other formats generated from this |
| SurrealDB role | Parallel store for sensor/clinical; Neo4j owns population genomics | Based on benchmark results |
| Variant nodes | Neo4j nodes with rsid + VRS ID | Requires seqrepo |
| LDGM mathematical note | Ω = R⁻¹ (precision = inverse LD), NOT the LD matrix | Critical: LDGM is sparse because Ω is sparse, not R |
| Cytos scope | Data-only KG construction layer | ML models are external consumers |
| Ancestry encoding | HANCESTRO ontology CURIEs | EUR=HANCESTRO:0005, EAS=HANCESTRO:0009, etc. |

---

## 6. Open Design Questions (Unresolved)

1. **SurrealDB genomics scope** — Mirror Neo4j genomics graph, or focus SurrealDB only on clinical/sensor/personal data?
2. **Multi-ancestry LDGM priority** — Download EAS/AFR/AMR now or after EUR validated?
3. **Gene node enrichment** — Add HGNC ID, Entrez ID, strand from GENCODE now?
4. **PGC hit threshold** — Store suggestive hits (p<1e-5) alongside GWS hits (p<5e-8)?
5. **Schema migration** — Keep schemas in `cytos/schemas/` or migrate to `cytoskeleton` (as planned in decision_log.md)?

---

## 7. Environment Setup

```bash
# Activate conda environment
conda activate cytognosis

# Verify graphLD is installed
python3 -c "from graphld import PrecisionOperator; print('OK')"

# Verify TileDB-VCF
python3 -c "import tiledbvcf; print(tiledbvcf.version())"

# Check Neo4j connection
NEO4J_PASSWORD=cytognosis2026 python3 -c "
from cytos.db.neo4j.client import get_driver
d = get_driver()
with d.session() as s:
    print(s.run('RETURN 1').single()[0])
"

# Check SurrealDB container
docker ps --filter name=cytos-surrealdb

# Run genomics test suite
cd /home/mohammadi/repos/cytognosis/cytos
NEO4J_PASSWORD=cytognosis2026 python3 -m pytest tests/genomics/ -q
```

**Key env vars:**
- `NEO4J_URI=bolt://localhost:7687`
- `NEO4J_USER=neo4j`
- `NEO4J_PASSWORD=cytognosis2026`
- `SURREAL_URL=ws://localhost:8000`

---

## 8. Key File Paths

| Asset | Path |
|-------|------|
| LDGM DuckDB index | `/home/mohammadi/datasets/06-genotype/ldgm/index.duckdb` |
| SO OBO ontology | `/home/mohammadi/datasets/04-identifiers/ontologies/so.obo` |
| Shahin WGS VCF | `/home/mohammadi/datasets/06-genotype/personal/Shahin/NG1CNUL31H.mm2.sortdup.bqsr.hc.vcf.gz` |
| Shahin CRAM | `/home/mohammadi/datasets/06-genotype/personal/Shahin/NG1CNUL31H.mm2.sortdup.bqsr.cram` |
| Olivia SNP VCF | `/home/mohammadi/datasets/06-genotype/personal/Olivia/` (3 VCF types) |
| PEC WGS VCF | `/home/mohammadi/datasets/06-genotype/cohort/PEC/brainSCOPE_PEC_sample_genotypes_no_rna.vcf.gz` |
| PEC RNA VCF | `/home/mohammadi/datasets/08-neuroimaging/PEC/synapse/genotype/WGS-Derived-ImputedGenotypes/` |
| PGC GWAS files | `/home/mohammadi/repos/cytognosis/cytos/data/gwas/pgc/` (14 files) |
| GWAS Catalog files | `/home/mohammadi/repos/cytognosis/cytos/data/gwas/gwas_catalog/` (SCZ, BIP, MDD) |
| graphLD third-party | `/home/mohammadi/repos/cytognosis/cytos/third_party/graphld/` |
| GENCODE v47 GTF | `/home/mohammadi/datasets/06-genotype/reference/gencode.v47.annotation.gtf.gz` |

---

## 9. Git State

```
HEAD: 8cc070b9 (main)
Remote: 46c0acd1 (origin/main) — 19 commits behind
Uncommitted changes: design/README.md modified; many deleted stubs (D flags)
```

**Commits since origin:**
```
8cc070b  fix(scripts/gwas): remove unused imports
3cc8c3c  feat(genomics): graphLD interface + GWAS Neo4j + SO tests
f259f0a  fix(genomics/so): robust SO OBO sanitizer
e209551  test: SurrealDB + LDGM alignment integration tests
8cebc7a  fix(genomics/ldgm+analysis): production-ready alignment
3465a73  feat(genomics/ldgm): CSV snplist parsing + bulk ingest script
3732b2d  feat(schema/export): push_to_cytoskeleton pipeline
2a22405  feat(genomics/gwas): multi-format loader
3fa8ede  test(genomics/neo4j): TestNeo4jGraph integration tests
ba481d0  feat(db/neo4j+ingest): Neo4j client + GRCh38 graph
87aa5a0  fix(tests/vrs): skip VRS seqrepo test when unavailable
8468fbe  feat(schemas/genomics): Pydantic v2 + core.yaml fix
7ad0313  chore: genomics domain import in master cytos.yaml
8472b40  feat(schemas): GenomeKG LinkML schema
05f34d9  feat(genomics/tests): comprehensive test suite + PEC ingestion
3fbdfeb  feat(genomics/vcf): TileDB-VCF ingestion pipeline
4b98f2e  feat(genomics): remaining Phase 2 modules
cadd634  feat(genomics): GenomeKG foundation modules
6b85a5b  feat(publish): asset pipeline for CSO ontology
```

---

## 10. Related Repositories

| Repo | Path | Relevance |
|------|------|-----------|
| `cytoskeleton` | `~/repos/cytognosis/cytoskeleton` | Environment hierarchy; `schemas/` migration target |
| `cyto-skills` | `~/repos/cytognosis/cytoskills` | Agent skill system; schema taxonomy push target |
| `agents` | `~/repos/cytognosis/agents` | Skill definitions + MEMORY.md |
| `graphld` | `third_party/graphld/` | LDGM native library (editable install) |

---

## 11. Conversation History References

| Session ID | Topic | Key outputs |
|-----------|-------|------------|
| `b591c0f4` | GenomeKG infrastructure (this session) | All genomics modules, LDGM, GWAS Neo4j, SO tests |
| `cd6537fc` | GWAS/PGC ingestion + scholarly pipeline | GWAS-SSF loaders, BioCypher schema config |
| `f78b85f5` | Cytoskeleton FAIR infrastructure | RO-Crate builder, SWHID, asset management |
| `3a11be50` | Infrastructure / CI/CD | OIDC migration, GCS bucket, HIPAA compliance |

---

## 12. Standards and Protocols Used

| Standard | Purpose | Implementation |
|----------|---------|----------------|
| **VRS 2.0** (GA4GH) | Variant representation | `src/cytos/genomics/vrs.py` |
| **GWAS-SSF 1.0** | GWAS summary statistics | `src/cytos/genomics/gwas.py` |
| **Sequence Ontology** | Variant type classification | `src/cytos/genomics/so.py` |
| **HANCESTRO** | Population ancestry encoding | LDGM DuckDB schema `hancestro` column |
| **LinkML** | Schema source of truth | `schemas/domains/*.yaml` |
| **TileDB** | Array storage (VCF + LDGM) | `tiledb/vcf/` + `datasets/.../ldgm/tiledb/` |
| **DuckDB** | LDGM block index + KGBuilder | `index.duckdb` + `kg/` pipeline |
| **graphLD/LDGM** | Precision LD matrices | `third_party/graphld/` + `graphld/` submodule |
| **EFO** | GWAS trait ontology | Trait node `efo_id` property |
| **MONDO** | Disease ontology | Trait node `mondo_id` property |
| **KGX TSV** | Knowledge graph exchange format | `data/kg/*.tsv` |
| **RO-Crate** | Provenance metadata | `src/cytos/publish/rocrate.py` |
| **GWAS Catalog harmonized** | Harmonized GWAS format | Auto-detected by `load_gwas_ssf()` |

---

*This document was generated during session b591c0f4 (2026-05-22) as part of the clean-state checkpoint before Antigravity update. All design decisions, completed work, and remaining tasks are accurate as of git HEAD `8cc070b9`.*

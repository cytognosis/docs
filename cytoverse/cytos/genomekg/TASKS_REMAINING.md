# GenomeKG — Remaining Tasks

> **Priority-ordered checklist for the next agent session.**
> All items are specific, actionable, and include exact file/command references.

---

## Status Legend
- `[ ]` Not started
- `[/]` In progress / partially done
- `[x]` Complete
- `[~]` Blocked (dependency noted)

---

## P1 — PGC GWAS Ingestion *(data present, just needs code)*

**PGC files at:** `data/gwas/pgc/`
Current files: `ADHD.tsv.gz`, `ALCH.tsv.gz`, `AN.tsv.gz`, `ANX.tsv.gz`, `ASD.tsv.gz`,
`BIP.tsv.gz`, `CANNABIS.tsv.gz`, `INSOMNIA.tsv.gz` + more (run `ls data/gwas/pgc/`)

PGC minimal format columns: `CHR | BP | SNP | A1 | A2 | OR | SE | P`
(Different from GWAS-SSF — needs a PGC-specific loader branch in `gwas.py`)

- [ ] **P1.1** Add PGC trait metadata to `EXTENDED_MANIFEST` in `scripts/ingest_gwas_neo4j.py`
  - EFO IDs: ADHD=EFO_0003756, ASD=EFO_0003756, OCD=EFO_0004683, PTSD=EFO_0001358, etc.
- [ ] **P1.2** Add PGC-format detection to `load_gwas_ssf()` in `gwas.py`
  - Detect: has `OR` column (not `beta`), compute `beta = log(OR)`
- [ ] **P1.3** Run `python3 scripts/ingest_gwas_neo4j.py` (or extend manifest)
- [ ] **P1.4** Verify: `MATCH (t:Trait) RETURN count(t)` → should be ≥14

---

## P2 — SurrealDB Schema Fix

- [ ] **P2.1** Fix async context manager in `src/cytos/db/surrealdb/client.py`
  ```python
  # Add to SurrealClientManager:
  async def __aenter__(self): ...
  async def __aexit__(self, *args): ...
  ```
- [ ] **P2.2** Implement `src/cytos/schema/bridges/linkml_to_surreal.py`
  - Input: LinkML YAML → Output: SurrealQL `DEFINE TABLE` DDL
- [ ] **P2.3** Define genomics tables in SurrealDB: Variant, SNP, GWASHit, Trait
- [ ] **P2.4** Test: `pytest tests/genomics/test_genomics_pipeline.py::TestSurrealDB`

---

## P3 — Variant Nodes + VRS *(blocked on seqrepo install)*

- [~] **P3.1** Install seqrepo: `seqrepo pull -i 2021-01-29` (~50GB, ~1 hour)
  - Data path: `/home/mohammadi/datasets/04-identifiers/seqrepo/`
  - Set `SEQREPO_ROOT` env var after install
- [~] **P3.2** After seqrepo: load SNP Variant nodes from TileDB-VCF into Neo4j
  - Properties: `rsid`, `chrom`, `pos`, `ref`, `alt`, `vrs_id`, `so_term`
  - Source: Shahin + PEC WGS TileDB stores
- [~] **P3.3** Create `(Variant)-[:ASSOCIATED_WITH]->(Trait)` from rsid matching GWASHit
- [~] **P3.4** TBX1 SV → VRS Adjacency object (use `vrs.py:infer_vrs_type()`)
- [ ] **P3.5** Un-skip seqrepo test in `tests/genomics/test_genomics_pipeline.py`

---

## P4 — SchemaGenerator Class

**File to create:** `src/cytos/schema/generator.py`

```python
class SchemaGenerator:
    """Generate multiple output formats from a LinkML domain schema."""

    def generate_jsonld(self, domain: str) -> Path: ...
    def generate_pydantic(self, domain: str) -> Path: ...
    def generate_jsonschema(self, domain: str) -> Path: ...
    def generate_shacl(self, domain: str) -> Path: ...
    def generate_all(self, domains: list[str] | None = None) -> dict[str, Path]: ...
```

- [ ] **P4.1** Implement `SchemaGenerator` using `linkml.generators.*` CLI wrappers
- [ ] **P4.2** Add `cytos schema generate` CLI subcommand in `src/cytos/__main__.py`
- [ ] **P4.3** Add `cytos schema pull` — refresh upstream schemas from biolink/GA4GH
- [ ] **P4.4** Add `cytos schema push ols4` — push generated OWL to local OLS4
- [ ] **P4.5** Add `cytos schema push cyto-skills` — entity type taxonomy as skill enums
- [ ] **P4.6** Version a release bundle: `schemas/releases/v2026.5/`

---

## P5 — CLI, Makefile, docker-compose

- [ ] **P5.1** Create `Makefile` with targets:
  ```makefile
  db-start:    docker-compose up -d neo4j surrealdb
  db-stop:     docker-compose down
  test:        pytest tests/genomics/ -q
  schema-gen:  cytos schema generate --all
  graphld-dl:  cd third_party/graphld && make download_all
  push:        git push origin main
  ```
- [ ] **P5.2** Create `docker-compose.yml`:
  - neo4j:2026.04.0 (port 7687/7474, auth neo4j/cytognosis2026)
  - surrealdb:latest (port 8000, surrealkv backend)
  - ebispot/ols4:latest (port 8080, optional)
- [ ] **P5.3** Add `cytos graphld` CLI subcommand:
  - `heritability <sumstats>` — run graphREML
  - `clump <sumstats>` — LD-based clumping
  - `blup <sumstats>` — polygenic scores
  - `download-data [--populations EUR,EAS]`
- [ ] **P5.4** Add DVC pipeline stages to `dvc.yaml`:
  - `gwas_ingest`: `scripts/ingest_gwas_neo4j.py` → triggers on GWAS file changes
  - `vcf_ingest`: `scripts/ingest_vcf.py` → triggers on VCF changes
  - `graphld_validate`: validation stage
- [ ] **P5.5** **Push 19 pending commits to origin:** `git push origin main`

---

## P6 — Multi-ancestry LDGM

Current state: EUR only (1,360 blocks, UKBB)

- [ ] **P6.1** Download EAS ancestry: `cd third_party/graphld && make download_eas`
- [ ] **P6.2** Download AFR ancestry: `make download_afr`
- [ ] **P6.3** Run `scripts/ingest_ldgm.py --ancestry EAS` for each new ancestry
- [ ] **P6.4** Verify: DuckDB shows 4+ ancestries in `ld_blocks` table

---

## P7 — Tests and CI/CD

- [ ] **P7.1** Run full 143-test suite: `pytest tests/ -q --tb=short`
  - Fix any failures in non-genomics suites
- [ ] **P7.2** Create `tests/genomics/test_graphld_pipeline.py`:
  - Load chr1 blocks → align SCZ GWAS → run graphREML → verify h² estimate
- [ ] **P7.3** Create `tests/genomics/test_vcf_personal.py`:
  - Query TBX1 region (chr22:19,700,000-20,000,000) in Shahin TileDB store
  - Verify CRAM read access
- [ ] **P7.4** Create `tests/test_db_both.py`:
  - Same gene lookup on Neo4j and SurrealDB → compare results
- [ ] **P7.5** Create `.github/workflows/ci.yml`:
  ```yaml
  on: [push, pull_request]
  jobs:
    test:
      steps:
        - ruff check src/
        - mypy src/ --ignore-missing-imports
        - pytest tests/ -q --ignore=tests/genomics  # infra-free subset
  ```

---

## Dependency Graph

```
P1 (PGC GWAS) ──────────────────────────────► P7 (full test run)
P2 (SurrealDB fix) ──────────────────────────► P7
P3 (seqrepo → Variant nodes) ───────────────► P7
P4 (SchemaGenerator) ────────────────────────► P5 (CLI)
P5 (CLI + Makefile + push) ──────────────────► P7 (CI)
P6 (multi-ancestry LDGM) ───────────────────► P7 (graphld test)
```

**Parallelizable immediately:** P1 + P2 + P3.1(seqrepo download) + P4

---

## Quick Verification Commands

After each task, use these to verify:

```bash
# P1 verify: PGC traits in Neo4j
NEO4J_PASSWORD=cytognosis2026 python3 -c "
from cytos.db.neo4j.client import get_driver
with get_driver().session() as s:
    print(s.run('MATCH (t:Trait) RETURN t.name, t.efo_id').data())"

# P2 verify: SurrealDB context manager
python3 -c "
import asyncio
from cytos.db.surrealdb.client import SurrealClientManager
async def t():
    async with SurrealClientManager() as db:
        print(await db.query('INFO FOR DB'))
asyncio.run(t())"

# P3 verify: Variant nodes
NEO4J_PASSWORD=cytognosis2026 python3 -c "
from cytos.db.neo4j.client import get_driver
with get_driver().session() as s:
    print(s.run('MATCH (v:Variant) RETURN count(v)').single()[0])"

# P5 verify: git push
cd /home/mohammadi/repos/cytognosis/cytos && git log origin/main..HEAD --oneline | wc -l
```

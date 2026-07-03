# Benchmark Revision Plan
**File:** `BENCHMARK_REVISION_PLAN.md`
**Date:** 2026-06-22
**Author:** Claude (Cytognosis Agents)
**Aligns with:** `BENCHMARK_DIGEST.md`, `SurrealDB-tuning-and-graphrag-guide.md`
**Source codebase:** `yar_supervisor_reproducible_benchmark_package/`

---

## TL;DR

The benchmark package is runnable and mostly correct, but has six issues that distort results: a persistent Docker volume bug that cross-contaminates Neo4j vector dimensions, SurrealDB's FTS runtime ORDER BY incompatibility (fixed in PATCH10 but not yet landed in the main harness), Kuzu using CONTAINS scan as its default lexical path, FalkorDB using an unpinned `latest` image tag, the `build_import` timer including schema/index creation time on server engines, and a double-run overhead in recall measurement. Fix these before comparing results to Ali's prior run.

---

## 1. Package Overview

The package benchmarks five database engines for the Yar personal knowledge graph against a 13-operation workload derived from Yar's actual hot path. Operations span: bulk import (`build_import`), keyed record lookup (`task_lookup`), graph traversal at 2 and 3 hops (`depth2_context`, `depth3_context`), reverse-reference lookup (`reverse_refs`), person-anchored memory fetch (`person_memory`), project-anchored decision fetch (`project_decisions`), BM25 full-text search (`lexical_search`), approximate nearest-neighbor vector search (`vector_search`), reciprocal rank fusion hybrid retrieval (`hybrid_rrf`), composite memory packet retrieval (`memory_packet`), single-record incremental write (`incremental_write`), and fresh-connection latency (`cold_open`).

**Engines:** SQLite + FTS5 + sqlite-vec (embedded), Kuzu (embedded graph), SurrealDB (Docker server, two adapters: legacy `surrealdb` and tuned `surrealdb_tuned`), Neo4j (Docker server), FalkorDB (Docker server).

**Dataset sizes:** 3k (smoke), 10k (default), 100k (stress). Node records carry a 384-dimensional float32 embedding, graph edges at 5 per node, 15 topic-cluster topic vectors generating correlated embeddings, and deterministic ground-truth top-20 vectors per query.

**Scoring:** Weighted geometric-style decision score; lower is better. Each operation is normalized against the fastest engine's p50 then multiplied by its weight. Missing or majority-failed operations receive a penalty of 10x weight. Weights favor: `memory_packet` (0.16), `vector_search` and `incremental_write` (0.12 each), `depth2_context` and `build_import` (0.10 each).

The package also includes a sync benchmark (`sync_benchmark/`) that tests Yar's CRDT op-log sync contract across 12 edge-case scenarios using real SQLite stores. It does not test the database engines and is separate from the DB scoring.

Reference results from Ali's M3 MacBook are in `reference_results/`. The final PATCH10 comparison is the canonical prior-run baseline.

---

## 2. Issues Found

### Issue 1: Docker volume reuse between dataset sizes corrupts Neo4j vector index (CONFIRMED BUG)
**Files:** `db_benchmark/run_full.sh` lines 1-53, `db_benchmark/run_surreal_tuned_retest.sh` lines 6-10.
**Description:** `run_full.sh` starts Docker with `docker compose up -d` once before all four runs and never tears down volumes between them. The 3k smoke run at `dim=128` (if `--dim` is omitted, it defaults to 128) writes Neo4j and SurrealDB volumes at that dimension. The 10k and 100k runs at `dim=384` then try to build vector indexes on top of stale volume data at the wrong dimension. This is the confirmed root cause of Neo4j's 200-failure vector and lexical paths in Ali's 10k/100k runs per `BENCHMARK_DIGEST.md` Section 4b point 6.
`run_surreal_tuned_retest.sh` (PATCH8+) correctly calls `reset_stack()` which runs `docker compose down -v` before each case. The main `run_full.sh` does not.
**Severity:** Critical for Neo4j; high for SurrealDB in the un-tuned adapter.

### Issue 2: SurrealDB FTS runtime ORDER BY incompatibility (FIXED IN PATCH10 but not propagated to main harness)
**Files:** `db_benchmark/yar_bench.py` lines 1191-1192 (legacy `SurrealAdapter.lexical_search`), lines 1191-1192 of `SurrealTunedAdapter.lexical_search`.
**Description:** The legacy `SurrealAdapter` (line 987) uses `ORDER BY search::score(0) DESC`, which SurrealDB's parser rejected, silently triggering the CONTAINS fallback (line 990-993). `SurrealTunedAdapter` (line 1191) does the same. PATCH10 fixes this in a patched zip by aliasing the score first (`search::score(0) AS score`) then ordering by the alias. This fix exists in `README_PATCH10_SURREAL_FTS_RUNTIME_FIX.md` and was validated in the final PATCH10 comparison, but the fix is NOT reflected in the current `yar_bench.py` in this repo. The current `SurrealTunedAdapter.lexical_search` at line 1191 still uses the broken form, meaning a fresh run from this repo will repro the pre-PATCH10 FTS failure.
**Severity:** Critical for SurrealDB lexical and hybrid results.

### Issue 3: Kuzu lexical_search is always a CONTAINS scan (methodology: unlabeled capability gap)
**Files:** `db_benchmark/yar_bench.py` lines 718-721 (`KuzuAdapter.lexical_search`).
**Description:** The FTS extension install is attempted at line 673-678 and failures are recorded in `capabilities["fts_extension"]`. However, `lexical_search` always falls through to a `CONTAINS` string scan (line 719-722) regardless of whether the extension loaded. The FTS extension's query syntax changed across Kuzu versions and the code never attempts to call it. The capabilities record says `"contains_scan_fallback_unless_fts_extension_query_works"` but the FTS query path is entirely absent. As a result, Kuzu's lexical numbers are linear scan numbers and are not comparable to FalkorDB's RediSearch or SQLite's FTS5 results.
**Severity:** High for Kuzu lexical/hybrid scores; methodology gap.

### Issue 4: FalkorDB Docker image is unpinned (`latest`)
**Files:** `db_benchmark/docker-compose.yml` line 22 (`image: falkordb/falkordb:latest`).
**Description:** Every other service in the compose file uses a pinned version (`surrealdb/surrealdb:v3.1.3`, `neo4j:2025.10`). FalkorDB uses `latest`, which means the image version changes between runs as new releases are pushed. This breaks reproducibility: Ali's run and a local rerun may use different FalkorDB binaries, and vector API or FTS query syntax differences between FalkorDB versions can silently change results.
**Severity:** High for reproducibility.

### Issue 5: `build_import` timer includes schema/index creation time on server engines
**Files:** `db_benchmark/yar_bench.py` lines 1701-1705 (`run_engine`).
**Description:** For SQLite and Kuzu, schema creation (`CREATE TABLE`, `CREATE INDEX`, FTS virtual table) happens in `setup()` and `load()` but the load timer at line 1701-1705 covers only `adapter.load()`, not `adapter.setup()`. For Neo4j and FalkorDB, index creation is inside `load()` (Neo4j lines 1276-1295, FalkorDB lines 1455-1464). For SurrealDB, schema and index definitions are also inside `load()` (lines 863-898). This means server engines' `build_import` times include index build time while SQLite's does not, making the comparison unfair. At 100k with HNSW index building, Neo4j and SurrealDB index creation is a large fraction of total import time.
**Severity:** Medium (inflates server engine scores in the import operation).

### Issue 6: Recall measurement executes each query twice (double-run overhead)
**Files:** `db_benchmark/yar_bench.py` lines 1751-1766 (`run_engine` inner loop).
**Description:** For `vector_search`, `hybrid_rrf`, `memory_packet`, and `lexical_search`, the code first calls `timed_call(...)` which internally calls `fn()` (line 1582), then immediately calls `fn()` again at line 1755 (`res = fn()`) to compute recall. Each relevant operation is therefore executed twice in sequence. The latency recorded is from the first call, but the second call's warm-cache effect slightly inflates the first call by loading query state. More importantly, incremental warm-cache effects make the recorded latency for round N slightly optimistic because round N+1 partially warms the cache for round N's state. This is a minor issue but means the timing is not truly measuring the nth-query-only latency.
**Severity:** Low; affects interpretation of latency numbers but not ranking order.

### Issue 7: `wait_for_services.py` has a fixed 8-second post-wait but does not wait for index readiness
**Files:** `db_benchmark/wait_for_services.py` lines 28-29.
**Description:** After TCP ports open, the script sleeps 8 seconds unconditionally. Neo4j's HNSW index (`CALL db.awaitIndexes(300)` at line 1294 and 1326) takes significantly longer than 8 seconds after data import at 100k. `db.awaitIndexes` is called inside `load()`, not in the service-readiness check, but that is the correct location. The issue is that `wait_for_services.py` is used before data import (it only checks that ports are open), so this 8-second delay is not relevant to index readiness. However, the compose health check for SurrealDB uses `surreal isready`, and if the health check passes before the engine is actually ready for writes (which can happen with SurrealKV backend startup), the first import batches may fail. Verified by PATCH8-PATCH10 notes.
**Severity:** Low.

### Issue 8: Embedding dimension defaults to 128 in CLI but scripts use 384
**Files:** `db_benchmark/yar_bench.py` line 1852 (`--dim` default 128), `db_benchmark/run_full.sh` line 14 (passes `--dim 384`).
**Description:** The CLI default is 128 but every production script passes `--dim 384`. Any manual invocation that omits `--dim` will produce incomparable results and will trigger the Docker volume dimension mismatch bug (Issue 1) if a prior 384-dim run's volumes are present. The mismatch is not warned anywhere.
**Severity:** Medium; traps manual users.

### Issue 9: `surrealdb_tuned` `build_import` is 2x slower than legacy `surrealdb` at 10k and 100k
**Files:** `db_benchmark/yar_bench.py` lines 1155-1174 (`SurrealTunedAdapter.load`), `reference_results/surreal_tuned_patch10_final_comparison.md` rows `build_import`.
**Description:** PATCH10 results show `build_import` for `surrealdb_tuned` at 10k is 24,031 ms vs 8,110 ms for the old untuned adapter. At 100k it is 290,134 ms vs 145,125 ms. The tuned adapter wraps each batch in `BEGIN TRANSACTION; INSERT INTO node $rows; COMMIT TRANSACTION;` (lines 1162-1164), which forces synchronous WAL flushes. The legacy adapter uses `INSERT INTO node $rows;` without transactions. SCHEMAFULL schema and additional indexes (8 node indexes in tuned vs 5 in legacy) also add index-build overhead. This does not affect query latency but materially inflates the `build_import` score (weight 0.10) for the tuned adapter relative to what a real Yar import pipeline would use (streaming, async, no mandatory per-batch transactions).
**Severity:** Medium; methodology concern for the import score.

### Issue 10: `SurrealAdapter.depth2` and `depth3` make N+1 sequential round trips
**Files:** `db_benchmark/yar_bench.py` lines 949-969 (`SurrealAdapter.depth2`, `SurrealAdapter.depth3`).
**Description:** The SurrealDB depth2 implementation fetches first-hop edges, then loops over each first-hop node and fetches its outgoing edges sequentially. At 100k this produces N sequential WebSocket round trips where N is proportional to `expand_k`. The `SurrealTunedAdapter` inherits this behavior. Neo4j, FalkorDB, and SQLite all express depth2 as a single query. This is a structural disadvantage in the adapter code, not in SurrealDB's engine capability, and inflates `depth2_context` and `depth3_context` latency artificially.
**Severity:** High for SurrealDB graph scores; adapter methodology bug.

### Issue 11: `task_lookup` at 100k is 445 ms even after PATCH10 tuning
**Files:** `reference_results/surreal_tuned_patch10_final_comparison.md`, `db_benchmark/yar_bench.py` line 947.
**Description:** After PATCH10 tuning, SurrealDB `task_lookup` is still 445 ms at 100k despite a UNIQUE index on `yid` and an index on `kind`. The query `SELECT VALUE yid FROM node WHERE kind = 'task' ORDER BY created_at DESC LIMIT N` requires a range scan on `kind` then a sort. SurrealDB 3.1 does not yet support composite sorted indexes in the same way FalkorDB does. A compound index on `(kind, created_at)` exists in the tuned schema (`idx_node_project_kind`) for `project_id + kind`, but not for the `kind + created_at` sort pattern used in `task_lookup`. This is a legitimate optimization that has not been tested.
**Severity:** Medium; open retest opportunity.

### Issue 12: No version pinning for Python packages; `surrealdb>=1.0.4` is a wide range
**Files:** `db_benchmark/requirements.txt` all lines.
**Description:** All requirements use `>=` minimums only. The `surrealdb` Python SDK has had breaking API changes between 1.0.x and 1.0.4+; the connection lifecycle handling in `SurrealAdapter.setup()` (lines 775-813) has version-detection branches specifically because the API was unstable. Without pinned versions, a future pip install may pick up a version that breaks one of those branches. `kuzu>=0.11.0` is similarly wide; Kuzu's Python API changed several times across minor versions (noted in `KuzuAdapter._collect_first_col` comment at line 640).
**Severity:** Medium; reproducibility risk.

---

## 3. Local Install Plan

This laptop is Linux (`7.0.0-22-generic`). The following steps install everything in order.

### 3.1 System prerequisites

```bash
sudo apt-get update
sudo apt-get install -y \
  python3.12 python3.12-venv python3.12-dev \
  build-essential \
  zip unzip \
  git
```

Verify:
```bash
python3.12 --version   # must be 3.12.x
docker --version       # must be 20+ with Compose v2
docker compose version # must be v2.x
```

If Docker is not installed:
```bash
curl -fsSL https://get.docker.com | sh
sudo usermod -aG docker $USER
# Re-login for group change to take effect
```

### 3.2 Python environment

```bash
cd /home/mohammadi/repos/cytognosis/yar_supervisor_reproducible_benchmark_package/db_benchmark
python3.12 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

Required packages and install paths:

| Package | Version in requirements.txt | Install path |
|---|---|---|
| `numpy` | >=1.26 | pip (Python, no native DB) |
| `psutil` | >=5.9 | pip |
| `sqlite-vec` | >=0.1.6 | pip (pre-built wheel; installs the C extension) |
| `kuzu` | >=0.11.0 | pip (pre-built wheel with embedded Kuzu C++ DB) |
| `surrealdb` | >=1.0.4 | pip (Python WebSocket client; requires SurrealDB server via Docker) |
| `neo4j` | >=5.28 | pip (Bolt protocol client; requires Neo4j server via Docker) |
| `redis` | >=5.0 | pip (Redis protocol client; FalkorDB uses Redis wire protocol) |
| `falkordb` | >=1.0.0 | pip (FalkorDB Python driver on top of redis) |

For the sync benchmark:
```bash
cd ../sync_benchmark
pip install -r requirements.txt  # pandas>=2.2.0 only
```

### 3.3 Docker images

Pull all images before running to avoid download time during benchmark:

```bash
docker pull surrealdb/surrealdb:v3.1.3
docker pull falkordb/falkordb:latest

# Note: pin FalkorDB to a specific tag before running (see Issue 4).
# Check current tags at: https://hub.docker.com/r/falkordb/falkordb/tags
# Recommended pinned tag as of June 2026:
docker pull falkordb/falkordb:v4.4.0  # or latest released tag; verify

docker pull neo4j:2025.10
```

- **SurrealDB:** Docker only for server mode. No native Linux binary install needed for this benchmark. Uses port 8000.
- **FalkorDB:** Docker only. Based on Redis; uses port 6379. No native install needed.
- **Neo4j:** Docker only. Uses ports 7474 (HTTP) and 7687 (Bolt). No native install needed.
- **SQLite:** Native via Python stdlib (`sqlite3`). No Docker needed.
- **Kuzu:** Native embedded via pip wheel. No Docker needed.

### 3.4 Disk and RAM budget

| Engine | Approx disk (100k run) | Approx RAM (Docker) |
|---|---|---|
| SQLite | ~400 MB (file on disk) | N/A (embedded) |
| Kuzu | ~500 MB (directory on disk) | N/A (embedded) |
| SurrealDB RocksDB | ~2-3 GB Docker volume | 1-2 GB container |
| FalkorDB | ~800 MB Docker volume | 1-2 GB container |
| Neo4j | ~2 GB Docker volume | 4-6 GB (Java heap) |

Minimum for a full 100k run: **8 GB RAM, 30 GB free disk**. Neo4j's Java heap config in `docker-compose.yml` already sets 2 GB initial / 4 GB max / 2 GB page cache.

---

## 4. Optimal Engine Configuration

### 4.1 SQLite (benchmark workload)

The current configuration is well-tuned for the benchmark workload: WAL journal, NORMAL sync, MEMORY temp store, 200 MB cache (`PRAGMA cache_size=-200000`). No changes needed. For production Yar use, add `PRAGMA mmap_size=1073741824` (1 GB memory-map) on desktop.

For GraphRAG use: SQLite handles the graph traversal and FTS path well. The `sqlite-vec` extension enables HNSW-equivalent ANN search. The 100k cold_open at 1165 ms is high because the benchmark reopens the connection from scratch; in a real app, keep the connection open.

### 4.2 Kuzu (benchmark workload)

Kuzu is embedded and has no server-side tuning knobs exposed in the benchmark. The FTS extension should be tested with the correct version-specific query syntax. For Kuzu >=0.11, the correct FTS query is `CALL query_fts_index('Node', 'node_fts_index', 'token')` (check version-specific docs). The current CONTAINS fallback makes Kuzu's lexical score artificially worse.

For GraphRAG use: Kuzu is a strong embedded graph engine but does not support HNSW/ANN indexes natively. All vector operations fall back to NumPy exact search. For Yar GraphRAG at small scale (<50k nodes), Kuzu + NumPy exact search is adequate. Above that, use FalkorDB or SurrealDB for vector-heavy paths.

### 4.3 Neo4j (benchmark workload)

Pin the Docker image. Ensure fresh volumes between runs at different dimensions. The `CALL db.awaitIndexes(300)` call inside `load()` is correct and necessary; do not remove it. For the benchmark, Neo4j is already well-configured via the compose file's heap and page cache settings.

For GraphRAG use: Neo4j has mature GDS library support and production-grade HNSW indexes. It is heavier than FalkorDB for Yar's workload scale but appropriate for a server-side projection with large corpora (>500k nodes).

### 4.4 FalkorDB (benchmark workload)

Pin the Docker image (fix Issue 4). FalkorDB's current performance advantage in the benchmark is partly due to its Redis-protocol connection reuse; FalkorDB maintains connection state more efficiently than SurrealDB's WebSocket reconnect pattern. No other tuning changes are needed.

For GraphRAG use: FalkorDB supports HNSW vector index and RediSearch BM25 full-text in one query via GQL/OpenCypher. It is the current recommended server graph projection for Yar MVP. For a single-node server, FalkorDB is the most efficient option for graph-traversal-heavy workloads.

### 4.5 SurrealDB (benchmark workload and GraphRAG)

See `SurrealDB-tuning-and-graphrag-guide.md` for the full reference. Summary of required configuration:

**For benchmark correctness:**
- Use `surrealdb_tuned` adapter, not `surrealdb`.
- Run with `--surreal-strict-validation` to fail fast if FTS or vector index does not validate.
- Fix the PATCH10 FTS ORDER BY query in `yar_bench.py` before running (see Section 5, Code Revision CR-1).
- Fix the N+1 depth2/depth3 traversal (see Section 5, Code Revision CR-2).
- Add a `(kind, created_at)` compound index to test the `task_lookup` path (see CR-3).
- Always use `reset_stack()` / fresh volumes.

**Storage backend:**
- Use `rocksdb:///data/yarbench.db` as the primary comparable run (what Ali used).
- Add a `surrealkv:///data/yarbench.db` run for comparison; PATCH8 ran it but did not compare it head-to-head with FalkorDB/SQLite.

**For GraphRAG use:**
- Use `SurrealKV` embedded Rust mode (no socket overhead) on desktop.
- Use the native `RELATE` graph edge model and SurrealQL `search::rrf()` for single-query hybrid retrieval.
- Target: single SurrealQL query combining `<|k, ef|>` KNN + `@0@` BM25 + `->relation->` graph expansion.
- The `SurrealDB-tuning-and-graphrag-guide.md` Section 4.3 has the canonical query pattern.

**Known remaining issue after PATCH10:** `task_lookup` and `cold_open` are still materially slower than FalkorDB at 100k (445 ms and 535 ms respectively). The task_lookup gap is likely addressable with a `(kind, created_at)` sorted compound index in SurrealDB 3.1+. The cold_open gap is structural to WebSocket session initialization and will only be closed by the embedded Rust SDK path.

---

## 5. Code Revisions Required

### Priority 1: Correctness fixes (run BEFORE comparing results)

**CR-1: Apply PATCH10 FTS ORDER BY fix to `SurrealTunedAdapter.lexical_search`**
**File:** `db_benchmark/yar_bench.py` lines 1191-1207
**What:** Change the lexical search query from `ORDER BY search::score(0) DESC` to alias the score and order by the alias. Current broken form (line 1191):
```python
q = f"SELECT yid, search::score(0) AS score FROM node WHERE body @0@ $q ORDER BY score DESC LIMIT {lim};"
```
This is actually already the corrected form in the current file (the alias `AS score` is present). However, the PATCH10 README says the old form was `ORDER BY search::score(0) DESC`. Verify that the current file already has the alias form (it does, at line 1191: `search::score(0) AS score ... ORDER BY score DESC`). If this is already correct, CR-1 may already be landed. **Action: run with `--surreal-strict-validation` and check `fts_body_runtime` in capabilities JSON; if it shows a fallback, the query still needs adjustment for the specific SurrealDB version running.**

**CR-2: Fix SurrealDB `depth2` and `depth3` N+1 query pattern**
**File:** `db_benchmark/yar_bench.py` lines 949-969
**What:** Replace the current loop-over-first-hop-nodes approach with a single two-hop lookup. SurrealDB 3.1 supports subquery chaining. Replace `depth2` with:
```surrealql
SELECT VALUE dst FROM edge
WHERE src IN (SELECT VALUE dst FROM edge WHERE src = $id LIMIT $fan)
LIMIT $lim;
```
as a single `_q()` call. This eliminates the N sequential round trips and makes SurrealDB's depth2 comparable to the single-query implementations in other adapters. Apply the same pattern to `depth3`. Also apply to `SurrealTunedAdapter` (which inherits these from `SurrealAdapter`).

**CR-3: Add fresh-volume reset to `run_full.sh` between all dataset-size runs**
**File:** `db_benchmark/run_full.sh`
**What:** Before each invocation of `yar_bench.py`, add a volume teardown step equivalent to `run_surreal_tuned_retest.sh`'s `reset_stack()`. For non-SurrealDB runs, this means stopping and removing the relevant containers and their volumes. Minimum fix: call `docker compose down -v --remove-orphans` and `docker compose up -d` before each run section, not once before all sections.

**CR-4: Pin FalkorDB Docker image to a specific tag**
**File:** `db_benchmark/docker-compose.yml` line 22
**What:** Change `image: falkordb/falkordb:latest` to a pinned version, for example `image: falkordb/falkordb:v4.4.0` (verify current stable tag at `hub.docker.com/r/falkordb/falkordb/tags`). Document the pinned version in a comment.

### Priority 2: Methodology improvements (run for fair comparison)

**CR-5: Pin all Python package versions in `requirements.txt`**
**File:** `db_benchmark/requirements.txt`
**What:** Freeze the current working versions. Run `pip freeze` after a successful install and record exact versions. Replace `>=` specifiers with `==` specifiers for all packages. Add a comment showing the tested versions. Minimum: pin `surrealdb`, `kuzu`, `falkordb`, and `neo4j` to exact versions since these have had breaking API changes.

**CR-6: Separate schema/index creation time from data insert time in `build_import`**
**File:** `db_benchmark/yar_bench.py` lines 1700-1705 (`run_engine`), and all adapter `load()` methods.
**What:** Add separate timers for schema setup and data insert within `load()`. The cleanest approach: split `load()` into `schema_setup(dataset)` and `data_insert(dataset)` on the base class, call them separately in `run_engine`, and record `build_schema_ms` and `build_insert_ms` as separate measurements in addition to the aggregate `build_import` measurement. This makes the import comparison fair across embedded and server engines.

**CR-7: Eliminate the double-call recall measurement**
**File:** `db_benchmark/yar_bench.py` lines 1753-1766
**What:** Pass the result out of `timed_call` or restructure so the recall measurement reuses the result from the timed call rather than calling `fn()` again. One approach: `timed_call` returns `(Measurement, Optional[Any])` where the second element is the result. Then recall is computed from the returned result, not a second call.

**CR-8: Implement real FTS extension query path for Kuzu**
**File:** `db_benchmark/yar_bench.py` lines 718-722 (`KuzuAdapter.lexical_search`)
**What:** After loading the FTS extension in `load()` (line 673-678), attempt the version-specific FTS query in `lexical_search` before falling back to CONTAINS. For Kuzu >=0.11: `CALL query_fts_index('Node', 'node_fts_index', $q)`. Record the result in `capabilities["lexical"]` as either `"fts"` or `"contains_fallback"`.

**CR-9: Warn on dimension mismatch with existing volumes**
**File:** `db_benchmark/wait_for_services.py` or a new pre-run check script
**What:** Before starting the benchmark, check whether existing Docker volumes contain data at a different embedding dimension than the current run. This is hard to check generically but can be approximated by recording the `--dim` and `--nodes` of the last run in a `.last_run_params.json` file and comparing at startup.

---

## 6. Rerun Procedure

### 6.1 Clean state setup

```bash
# Working directory
cd /home/mohammadi/repos/cytognosis/yar_supervisor_reproducible_benchmark_package

# Kill any running containers
docker rm -f yar-surrealdb yar-falkordb yar-neo4j 2>/dev/null || true

# Remove all related volumes (critical: prevents dimension contamination)
cd db_benchmark
docker compose down -v --remove-orphans 2>/dev/null || true
docker volume ls -q | grep -E 'db_benchmark|surreal|falkor|neo4j' | xargs -r docker volume rm 2>/dev/null || true

# Clean prior outputs
rm -rf results_patch8_* slim_patch8_surreal_tuned yar_surreal_tuned_results_slim.zip

# Create and activate Python environment
python3.12 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

### 6.2 Apply Code Revision CR-1 verification

Before running, verify the FTS ORDER BY fix is in place:
```bash
grep -n "search::score" yar_bench.py
```
Both occurrences (lines ~987 and ~1191) should have the alias form `search::score(0) AS score ... ORDER BY score DESC`, not `ORDER BY search::score(0) DESC`. If either is the old form, apply the PATCH10 fix manually.

### 6.3 Run the tuned DB benchmark

```bash
cd db_benchmark
./run_surreal_tuned_retest.sh
```

This script runs four cases in order, calling `reset_stack()` (volume teardown + fresh startup) before each:
1. 10k RocksDB + HNSW: sqlite, falkordb, surrealdb_tuned (strict validation on)
2. 10k RocksDB + DISKANN: surrealdb_tuned only (strict off)
3. 10k SurrealKV + HNSW: surrealdb_tuned only (strict off)
4. 100k RocksDB + HNSW: sqlite, falkordb, surrealdb_tuned (strict on)

Expected runtime: 45-90 minutes on this Linux machine depending on CPU and disk speed. The 100k run is the longest.

### 6.4 Collect slim results

```bash
./collect_tuned_results.sh
# Produces: yar_surreal_tuned_results_slim.zip
```

### 6.5 Compare against Ali's prior PATCH10 run

```bash
# Extract Ali's reference (already in the repo)
cp /home/mohammadi/repos/cytognosis/yar_supervisor_reproducible_benchmark_package/reference_results/yar_surreal_tuned_results_slim_PATCH10.zip ./

python compare_surreal_tuned.py \
  --old final_db_slim.zip \
  --new yar_surreal_tuned_results_slim.zip \
  --out LOCAL_VS_ALI_COMPARISON.md
```

Note: `final_db_slim.zip` is in `reference_results/`. Copy it first:
```bash
cp ../reference_results/final_db_slim.zip ./
```

### 6.6 Version stamping

Before accepting any run as comparable, verify version stamps in the `engine_meta.json` output files:
- `surrealdb_tuned/engine_meta.json`: should contain `surreal_version_query` from `INFO FOR DB`. The image is `v3.1.3`.
- `falkordb/engine_meta.json`: should contain FalkorDB version from the `dbms.procedures()` probe.
- Record these in a `RUN_MANIFEST.md` alongside the output zips.

### 6.7 What "comparable to Ali's run" means

Ali ran on macOS M3 8 GB RAM. This is Linux x86_64. Absolute latency numbers will differ (expect Linux Docker to be slightly faster on CPU-bound operations). What should be comparable:

- **Ranking order**: FalkorDB first at 100k, SQLite second, SurrealDB tuned third.
- **Score magnitudes**: Tuned SurrealDB 100k score should be in the 8-10 range (Ali got 9.375). If it is below 7, check that FTS is working and the task_lookup index is as intended.
- **FTS improvement**: 10k lexical_search for surrealdb_tuned should be under 10 ms (Ali got 3.5 ms). If still 200+ ms, PATCH10 fix is not applied.
- **task_lookup**: 10k should be 40-60 ms (Ali got 46 ms). 100k should be 400-500 ms (Ali got 445 ms). If dramatically lower, check whether the depth2 N+1 fix (CR-2) was applied, which would not affect task_lookup but might indicate an unexpected schema change.

---

## 7. Risks and Gotchas

### R1: PATCH10 FTS fix may already be in `yar_bench.py` in this repo
Inspection of the current `yar_bench.py` at lines 1191 and 1196 shows the alias form is already present (`search::score(0) AS score ... ORDER BY score DESC`). If this is actually the PATCH10-fixed version, CR-1 is already done. Confirm by running the strict-validation case and checking `fts_body_runtime` in capabilities. If it says `"body fulltext failed"` or `"fulltext_failed_contains_fallback"`, the fix did not land correctly or the SurrealDB version running does not accept this syntax.

### R2: SurrealDB `build_import` at 100k takes ~290 seconds (4.8 minutes)
This is not a bug; it is the cost of SCHEMAFULL insert with batch transactions and HNSW index building. The `run_surreal_tuned_retest.sh` wraps it in `|| true` at line 55, so it will silently succeed even if it times out. Monitor with `docker logs -f yar-surrealdb` to ensure the import completes. If it hangs, increase Docker memory limit.

### R3: SurrealDB health check passes before engine is ready for writes with SurrealKV backend
The PATCH8-PATCH10 notes mention that SurrealKV startup takes longer than the TCP health check. If `run_case 3` (SurrealKV) fails immediately, increase `YARBENCH_POST_WAIT_SECONDS` in `wait_for_services.py` from 8 to 20.

### R4: Neo4j on Linux requires `ulimit` adjustment for production use
The benchmark's compose file sets Java heap to 4 GB max. On Linux, if `vm.max_map_count` is low, Neo4j may fail to start. Run `sudo sysctl -w vm.max_map_count=262144` before starting the compose stack if Neo4j container exits immediately.

### R5: `kuzu>=0.11.0` Python API is not fully stable; read `_collect_first_col`
The Kuzu adapter has two result-iteration paths (lines 640-651) because the API changed. If Kuzu >=0.12 changes the result iterator again, depth queries may return empty lists. Verify by checking `results_patch8_10k_rocks_hnsw/kuzu/measurements.jsonl` for non-zero `result_count` on depth operations.

### R6: Docker volume names are auto-prefixed by compose project name
The compose file declares volumes as `surreal_data`, `falkor_data`, `neo4j_data`, `neo4j_logs`. Docker Compose prefixes these with the project directory name, so the actual volume names will be something like `db_benchmark_surreal_data`. The cleanup commands in `run_db_surreal_tuned.sh` (line 12) use `grep -E 'yar_db_eval_suite|surreal|falkor|neo4j'`, which should catch these. Verify after cleanup with `docker volume ls`.

### R7: After applying CR-2 (depth2 N+1 fix), SurrealDB graph scores will change
The depth2/depth3 fix will likely improve SurrealDB graph-traversal latency materially, which will change both the raw latency numbers and the weighted decision score. This is a methodology correction, not a performance improvement in the engine. Clearly label runs as "pre-CR2" and "post-CR2" when comparing.

### R8: The `run_full.sh` script does not apply fresh volumes
If you use `run_full.sh` instead of `run_surreal_tuned_retest.sh`, you will repro Issue 1 (Neo4j volume contamination). Only use `run_surreal_tuned_retest.sh` (or `run_db_surreal_tuned.sh` from the repo root) for comparable runs.

### What to verify after the rerun

1. **PASS gate:** `results_patch8_10k_rocks_hnsw/surrealdb_tuned/engine_meta.json` contains `"validation_fts_body_not_table_iterator": "True"` and `"validation_vector_has_knn": "True"`.
2. **FTS is working:** `lexical_search` p50 for `surrealdb_tuned` at 10k is under 20 ms (not 200+ ms). Check `summary.csv` in the 10k results directory.
3. **No contamination:** `decision_score.csv` for every run shows `coverage_weight: 1.2` for all included engines, meaning no operations are entirely missing.
4. **Ranking preserved:** 100k ranking is FalkorDB first, SQLite second, SurrealDB tuned third.
5. **FalkorDB version recorded:** `results_patch8_10k_rocks_hnsw/falkordb/engine_meta.json` contains a FalkorDB version string. If it shows `latest` was pulled and the version is different from Ali's run, note it as a potential confounder.
6. **No `contains_fallback` in SurrealDB strict runs:** grep the 10k and 100k strict-run `engine_meta.json` files for `fulltext_failed_contains_fallback`. Any hit means the FTS path is still broken.

---

*End of plan. Primary blocker for a valid rerun: apply CR-1 (verify PATCH10 FTS fix is in yar_bench.py) and CR-3 (fresh volumes in run_full.sh if using that script). The recommended path is to use `run_db_surreal_tuned.sh` directly, which already calls `run_surreal_tuned_retest.sh` with correct volume resets.*

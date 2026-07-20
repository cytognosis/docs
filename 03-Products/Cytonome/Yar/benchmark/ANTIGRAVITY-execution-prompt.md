---
status: authoritative
date: 2026-06-22
author: "@shahin"
audience: antigravity-coding-agent
tags: [yar, storage, benchmark, surrealdb, falkordb, sqlite, neo4j, graphrag, cytomem, runbook]
---

# Antigravity Execution Prompt: Yar Database and GraphRAG Benchmark

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: engineers, stakeholders
> **Tags**: `yar`, `benchmark`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)

**Estimated reading time: 12 minutes.**
**If you only read one section:** read Section 3 (Guardrails) before touching any files, and Section 4 (SurrealDB Optimizations) before writing any code.

---

## 0. Objective and Premise

**Goal:** Make SurrealDB perform as well as it can, produce a valid comparable rerun of the Yar storage benchmark (PATCH11), add standard GraphRAG-tool benchmarks on the desktop, and assess and optimize the cytomem memory service (which uses Neo4j).

**Why this matters:** SurrealDB placed last (score 9.38 at 100k in the PATCH10 run) due to confirmed configuration and methodology artifacts. Three root causes are proven by the benchmark's own data. The engine itself scored 1.20 (perfect) on the DISKANN-only isolated probe. SurrealDB is the primary candidate for Yar's GraphRAG projection path, and it cannot be promoted to that role until the artifacts are corrected and the async SDK port is done.

**Expected outcome:** After all optimizations, SurrealDB's weighted score at 100k should move from approximately 9.38 into the 3 to 5 range, making it competitive with FalkorDB (current score 4.26) and SQLite (current score 5.49) on server-side graph plus vector workloads.

**PATCH10 baseline (100k RocksDB + HNSW):**

| Engine | Weighted Score |
|---|---|
| FalkorDB | 4.26 |
| SQLite | 5.49 |
| SurrealDB tuned | 9.38 |

All work in this runbook is additive: it does not change the architecture decision (SQLite = phone/laptop MVP, FalkorDB = current server graph projection). It determines whether SurrealDB graduates from "retest candidate" to "validated GraphRAG projection."

**Scope is also cytomem.** The cytomem service (at `https://github.com/cytognosis/cytomem`) uses Neo4j. It has a known O(n) CONTAINS scan on keyword search. This runbook fixes that, activates the existing Graphiti recall path, and benchmarks recall quality before and after.

---

## 1. Reference Documents

Read all of these before writing any code. They contain exact file paths, line numbers, SurrealQL snippets, and before/after code. Do not guess; use these.

| Document | Path | Purpose |
|---|---|---|
| Benchmark evaluation and results | `https://github.com/cytognosis/docs/blob/main/03-Products/Cytonome/Yar/benchmark/BENCHMARK-evaluation-and-results.md` | Authoritative results, issue list (12 package-level issues), SurrealDB artifact verdict, Section 8 validity requirements |
| Benchmark prompts catalog | `https://github.com/cytognosis/docs/blob/main/03-Products/Cytonome/Yar/benchmark/BENCHMARK-prompts-catalog.md` | Status of each prior patch (A1-A5), which are canonical vs superseded; Section 4 lists N1-N3 prompts needed for this phase |
| cytomem GraphRAG integration and optimization | `https://github.com/cytognosis/docs/blob/main/03-Products/Cytonome/Yar/benchmark/CYTOMEM-graphrag-integration-and-optimization.md` | cytomem architecture (Section 1), fit assessment (Section 2), GraphRAG framework comparison (Section 3), concrete optimizations (Section 4), desktop benchmark plan (Section 5) |
| Benchmark revision plan | `https://github.com/cytognosis/docs/blob/main/03-Products/Cytonome/Yar/consolidation_2026-06-21/_storage/BENCHMARK_REVISION_PLAN.md` | All 12 package-level issues with exact file paths and line numbers, local install plan (Section 3), optimal engine configuration (Section 4), 9 code revisions CR-1 through CR-9 (Section 5), rerun procedure (Section 6), risks R1-R8 |
| SurrealDB code audit | `https://github.com/cytognosis/docs/blob/main/03-Products/Cytonome/Yar/consolidation_2026-06-21/_storage/SURREALDB_CODE_AUDIT.md` | 8 code-level issues ranked by impact, exact before/after code for each fix, Summary Table |
| SurrealDB tuning and GraphRAG guide | `https://github.com/cytognosis/docs/blob/main/03-Products/Cytonome/Yar/spec/SurrealDB-tuning-and-graphrag-guide.md` | Troubleshooting table T1-T12, SCHEMAFULL schema, FTS analyzer and index syntax, KNN operator forms, persistent WebSocket pattern, GraphRAG query patterns (Section 4), verification checklist (Section 6) |
| SurrealDB advanced optimization and versions | `https://github.com/cytognosis/docs/blob/main/03-Products/Cytonome/Yar/spec/SurrealDB-advanced-optimization-and-versions.md` | Latest versions and relevant changes (Section 1), advanced optimization configs (Section 2), maximum-performance checklist (Section 4), docker-compose.yml and run script changes (Section 5) |
| Storage benchmark tracker | `https://github.com/cytognosis/docs/blob/main/03-Products/Cytonome/Yar/spec/STORAGE_BENCHMARK_TRACKER.md` | Living master status table (Section 1), open decisions O-1 through O-8 (Section 3) |
| Benchmark package top-level README | `https://github.com/cytognosis/yar_supervisor_reproducible_benchmark_package/README.md` | Run commands, architecture decision summary, reference output list |
| PATCH10 README | `https://github.com/cytognosis/yar_supervisor_reproducible_benchmark_package/db_benchmark/README_PATCH10_SURREAL_FTS_RUNTIME_FIX.md` | Canonical prior patch; PATCH11 is built on top of it |
| cytomem repo | `https://github.com/cytognosis/cytomem` | Source of truth for cytomem code; key files: `src/cytomem/graph/queries.py`, `src/cytomem/graph/client.py`, `src/cytomem/mcp/server.py` |

---

## 2. Key Facts (No Session Context Available)

These facts are stated inline because this agent does not have session context.

**Repo paths:**
- Benchmark package: `https://github.com/cytognosis/yar_supervisor_reproducible_benchmark_package`
- Benchmark code: `.../yar_supervisor_reproducible_benchmark_package/db_benchmark/`
- cytomem: `https://github.com/cytognosis/cytomem`
- Docs: `https://github.com/cytognosis/docs`

**PATCH10 baseline scores (100k RocksDB + HNSW):** FalkorDB 4.26, SQLite 5.49, SurrealDB tuned 9.38.

**SurrealDB version history:** The package pins `surrealdb/surrealdb:v3.1.3`. The current latest stable as of 2026-06-22 is v3.1.5 (security fix, drop-in from 3.1.3, no schema changes needed). v3.1.4 fixed a `type::field('id')` equality that was doing full table scans instead of point lookups, which is directly relevant to `task_lookup`. Pin to v3.1.5 for the PATCH11 run.

**Python SDK:** The package pins `surrealdb>=1.0.4`. SDK 2.0.0 renames the async class from `AsyncSurrealDB` to `AsyncSurreal`. Verify the exact class name against the installed SDK before writing code (see Section 4, Item 1).

**cytomem graph:** Neo4j Community Edition at `bolt://localhost:7687`. Approximately 7,322 Artifact nodes. The keyword search at `src/cytomem/graph/queries.py` uses `CONTAINS` (O(n) scan, no index). The Graphiti integration in `src/cytomem/graph/client.py` is initialized but not used in the MCP recall path.

**FalkorDB pin:** The docker-compose.yml currently uses `falkordb/falkordb:latest`. Pin to `v4.4.0` or the current latest stable tag before running (check `hub.docker.com/r/falkordb/falkordb/tags`).

---

## 3. Guardrails

Follow these strictly. They prevent data loss and preserve comparability with PATCH10.

1. **Work on a new git branch.** Before making any file changes, create a branch named `yar-bench-patch11` from the current HEAD of the benchmark package repo. Do not commit directly to main.

2. **Do not break the existing working tree.** All code changes are additive or drop-in replacements. Do not delete any existing result files or reference outputs.

3. **Pin all versions.** After applying each fix, update `requirements.txt` to use `==` specifiers for every package. Run `pip freeze` after a successful install and record the exact versions. Minimum pins: `surrealdb`, `kuzu`, `falkordb`, `neo4j`, `redis`, `sqlite-vec`.

4. **Fresh Docker volumes per dataset size.** Never skip the `docker compose down -v --remove-orphans` step between runs. Verify volume deletion explicitly before each run case. This is Issue 1 in the benchmark evaluation doc: stale volumes from the 3k run at dim=128 corrupted Neo4j and SurrealDB at 10k and 100k.

5. **Stamp engine versions in results.** Every run must produce an `engine_meta.json` that includes the SurrealDB version (from `SELECT * FROM sys::version()`), the FalkorDB version, and the Neo4j version. Record these in a `RUN_MANIFEST.md` alongside output zips with: hardware, Python version, Docker version, image tags, date, and applied code revisions.

6. **Fail strict if FTS falls back to a scan.** Run all SurrealDB cases with `--surreal-strict-validation`. Reject any run where `engine_meta.json` contains `fulltext_failed_contains_fallback` or where `lexical_search` p50 at 10k exceeds 20 ms. Both indicate the PATCH10 FTS fix did not land.

7. **Always pass `--dim 384` explicitly.** Never rely on the default (it is 128 in the CLI). Omitting it produces incomparable results and triggers the volume dimension mismatch bug.

8. **Label runs clearly.** Mark pre-CR2 and post-CR2 runs separately when comparing, because the N+1 fix (Section 4, Item 6) changes SurrealDB graph-traversal latency materially.

---

## 4. Install and Configure

### 4.1 System Prerequisites

```bash
sudo apt-get update
sudo apt-get install -y \
  python3.12 python3.12-venv python3.12-dev \
  build-essential zip unzip git

python3.12 --version   # must be 3.12.x
docker --version       # must be 20+ with Compose v2
docker compose version # must be v2.x
```

If Docker is not installed:
```bash
curl -fsSL https://get.docker.com | sh
sudo usermod -aG docker $USER
# re-login for group change to take effect
```

Increase Neo4j map count (required on Linux):
```bash
sudo sysctl -w vm.max_map_count=262144
```

### 4.2 Python Environment (Benchmark)

```bash
cd ~/repos/cytognosis/yar_supervisor_reproducible_benchmark_package/db_benchmark
python3.12 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

After all code changes are applied (Section 4.4), freeze the requirements:
```bash
pip freeze > requirements_pinned.txt
# Review and replace requirements.txt with pinned versions
```

### 4.3 Docker Images (Benchmark Engines)

Pull all images before running to avoid download time during timed benchmark:

```bash
# SurrealDB: pin to v3.1.5 (upgrade from v3.1.3 in the package)
# v3.1.4 fixed id-equality table scans; v3.1.5 is security patch + cold-start race fix
docker pull surrealdb/surrealdb:v3.1.5

# FalkorDB: pin to a specific tag (the package uses 'latest'; see Section 3 Guardrail 3)
# Check current stable tag at hub.docker.com/r/falkordb/falkordb/tags
docker pull falkordb/falkordb:v4.4.0  # or current stable; verify the tag

# Neo4j: already pinned in the package
docker pull neo4j:2025.10
```

Update `docker-compose.yml`:
- Line 3: change `surrealdb/surrealdb:v3.1.3` to `surrealdb/surrealdb:v3.1.5`
- Line 22: change `falkordb/falkordb:latest` to `falkordb/falkordb:v4.4.0` (or current stable tag)

Also update the default storage backend in docker-compose.yml (line 7):
```yaml
# Change from:
command: >
  start --bind 0.0.0.0:8000 --user root --pass root ${SURREAL_STORE:-rocksdb:///data/yarbench.db}
# Change to:
command: >
  start --bind 0.0.0.0:8000 --user root --pass root
  --index-compaction-interval 5s
  --slow-log-threshold 100
  ${SURREAL_STORE:-surrealkv:///data/yarbench.db}
```

### 4.4 GraphRAG Tool Installs (Additional Desktop Benchmarks)

These are for Section 7 only. Install into the same `.venv` after the benchmark environment is established:

```bash
# neo4j-graphrag-python: HybridRetriever (vector + BM25) over existing cytomem Neo4j
pip install neo4j-graphrag

# graphiti-core: already a cytomem dependency; install to venv for benchmarking
pip install graphiti-core

# LightRAG with Ollama backend (local LLM, no API key required)
pip install lightrag-hku
# Pull the Ollama model separately (requires Ollama installed on the host):
# ollama pull llama3.1
# Note: verify the model name against current Ollama model registry
# (this runbook uses llama3.1 as documented in the cytomem GraphRAG doc, Section 5.3)
```

### 4.5 cytomem Python Environment

```bash
cd ~/repos/cytognosis/cytomem
# cytomem uses uv; check pyproject.toml for the exact install command
cat pyproject.toml
uv sync  # or: pip install -e ".[dev]" if uv is not available
```

---

## 5. Apply the SurrealDB Optimizations

Apply these in priority order. Highest impact first. All code references are in the benchmark code audit at:
`https://github.com/cytognosis/docs/blob/main/03-Products/Cytonome/Yar/consolidation_2026-06-21/_storage/SURREALDB_CODE_AUDIT.md`

### Item 1 (CRITICAL): Switch to the Async SDK

**File:** `db_benchmark/yar_bench.py`, lines 766-814 (`SurrealAdapter.setup`) and every `_q()` call.

**Why:** The `surrealdb>=1.0.4` SDK uses a synchronous blocking WebSocket client. Every query incurs a full blocking socket round-trip. This is the confirmed root cause of `task_lookup` at 46-446 ms vs FalkorDB's 0.6-3.3 ms.

**IMPORTANT: Verify the class name before coding.** The audit notes that SDK 2.0.0 renames `AsyncSurrealDB` to `AsyncSurreal`. The advanced guide (Section 2.3) states the correct class is `AsyncSurreal` in SDK 2.0.0+. Before writing any code, run:

```python
import surrealdb; help(surrealdb)
# or:
python -c "import surrealdb; print(dir(surrealdb))"
```

Identify the actual async class in the installed SDK. Use whatever the installed SDK exposes; do not hardcode a class name from docs without verifying.

**Minimum viable async port (sync harness wrapper):**

```python
import asyncio
from surrealdb import AsyncSurreal  # verify class name first

class SurrealAdapter:
    def __init__(self, url: str):
        self._loop = asyncio.new_event_loop()
        self.db = self._loop.run_until_complete(self._async_setup(url))

    async def _async_setup(self, url: str):
        db = AsyncSurreal(url)  # use verified class name
        await db.connect()
        await db.sign_in({"user": "root", "pass": "secret"})
        await db.use("yar", "personal")
        return db

    def _q(self, query: str, params: dict | None = None):
        return self._loop.run_until_complete(self.db.query(query, params or {}))
```

Apply this pattern to both `SurrealAdapter` (lines 766-814) and `SurrealTunedAdapter`. Do NOT create a new `AsyncSurreal()` per query; that re-triggers the WebSocket handshake (40-400 ms per call).

After porting, verify with a single smoke run at 3k:
```bash
python yar_bench.py --engines surrealdb_tuned --nodes 3000 --dim 384 --surreal-strict-validation
```

The `task_lookup` p50 should drop from ~46 ms into the 1-5 ms range.

### Item 2 (HIGH): Fix Transaction Wrapping in build_import

**File:** `db_benchmark/yar_bench.py`, lines 1161-1174 (`SurrealTunedAdapter.load`).

**Why:** PATCH9 added `BEGIN TRANSACTION; INSERT INTO node $rows; COMMIT TRANSACTION;` as a single query string. The server parses and executes three statements per batch, tripling the per-batch cost. This caused a 3x regression in `build_import` (8k ms to 24k ms at 10k).

**Fix:** Issue the three statements as separate `_q()` calls:

Before:
```python
try:
    self._q("BEGIN TRANSACTION; INSERT INTO node $rows; COMMIT TRANSACTION;", {"rows": rows})
except Exception:
    self._q("INSERT INTO node $rows;", {"rows": rows})
```

After:
```python
try:
    self._q("BEGIN TRANSACTION;")
    self._q("INSERT INTO node $rows;", {"rows": rows})
    self._q("COMMIT TRANSACTION;")
except Exception:
    try:
        self._q("CANCEL TRANSACTION;")
    except Exception:
        pass
    self._q("INSERT INTO node $rows;", {"rows": rows})
```

Apply the same pattern to the edge insertion loop at lines 1167-1174.

### Item 3 (HIGH): Add Comparable SurrealKV Runs

**Files:** `db_benchmark/docker-compose.yml` line 7 (already updated in Section 4.3), `db_benchmark/run_surreal_tuned_retest.sh` lines 48-51.

**Why:** The only SurrealKV run in PATCH10 was a single-engine probe (no SQLite or FalkorDB alongside it), so the score of 1.20 is not comparable. We need apples-to-apples SurrealKV vs SQLite vs FalkorDB runs at 10k and 100k.

Update `run_surreal_tuned_retest.sh` to add these cases:
```bash
# 5) SurrealKV at 10k, all three engines for a comparable score
reset_stack "surrealkv:///data/yarbench.db"
run_case results_patch11_10k_surrealkv_hnsw "sqlite,falkordb,surrealdb_tuned" 10000 200 50 hnsw 1 || true

# 6) SurrealKV at 100k, all three engines
reset_stack "surrealkv:///data/yarbench.db"
run_case results_patch11_100k_surrealkv_hnsw "sqlite,falkordb,surrealdb_tuned" 100000 300 100 hnsw 1 || true
```

### Item 4 (MEDIUM): Verify FTS ORDER BY Alias Form

**File:** `db_benchmark/yar_bench.py`, lines 1191-1207.

Before any run, verify PATCH10 FTS fix is in place:
```bash
grep -n "search::score" yar_bench.py
```

Both occurrences should have the alias form:
```surrealql
SELECT yid, search::score(0) AS score FROM node WHERE body @0@ $q ORDER BY score DESC LIMIT $limit;
```

If either shows `ORDER BY search::score(0) DESC` (the old broken form), apply the PATCH10 fix manually. Then verify the index with:
```surrealql
INFO FOR TABLE node;
EXPLAIN FULL SELECT yid FROM node WHERE body @0@ "test";
-- Expected: operation = "Matches" or "Union", not "Table Iterator"
```

### Item 5 (MEDIUM): Move HNSW Index Definition to After Data Import

**File:** `db_benchmark/yar_bench.py`, lines 1140-1153 (`SurrealTunedAdapter.load`).

**Why:** Defining HNSW before inserting data forces SurrealDB to update the graph incrementally per row. Defining it after data import allows a single-pass build via `REBUILD INDEX`, which is faster and produces better graph structure.

Move the vector index creation block from before the insertion loop (lines 1140-1153) to after the edge insertion loop (after line 1174), then add:
```surrealql
REBUILD INDEX idx_node_vec ON TABLE node;
```

As a Python `_q()` call immediately after the index definition:
```python
try:
    self._q("REBUILD INDEX idx_node_vec ON TABLE node;")
    self.capabilities["vector_index_rebuild"] = "ok"
except Exception as e:
    self.capabilities["vector_index_rebuild"] = f"failed: {e}"
```

### Item 6 (HIGH): Fix N+1 Graph Traversal in depth2 and depth3

**File:** `db_benchmark/yar_bench.py`, lines 949-969 (`SurrealAdapter.depth2`, `SurrealAdapter.depth3`).

**Why:** SurrealDB fetches first-hop edges then loops over each first-hop node and fetches its outgoing edges sequentially. Neo4j, FalkorDB, and SQLite all express this as a single query. This inflates `depth2_context` and `depth3_context` latency.

Replace the N+1 loop with a single two-hop SurrealQL query:
```surrealql
SELECT VALUE dst FROM edge
WHERE src IN (SELECT VALUE dst FROM edge WHERE src = $id LIMIT $fan)
LIMIT $lim;
```

Issue this as a single `_q()` call. Apply the same pattern to `depth3` and to `SurrealTunedAdapter` (which inherits these methods). Label runs as "pre-CR2" vs "post-CR2" in your output files when comparing, because this change materially shifts graph-traversal scores.

### Item 7 (MEDIUM): Add Embedding Dimension Assertion

**File:** `db_benchmark/yar_bench.py`, line 1108.

Change:
```python
"DEFINE FIELD embedding ON TABLE node TYPE array<float>",
```

To:
```python
f"DEFINE FIELD embedding ON TABLE node TYPE array<float> ASSERT array::len($value) = {dataset.dim}",
```

This catches dimension mismatches at write time rather than at index creation time.

### Item 8 (LOW): Fix Volume Deletion and Add Version Stamp

**Volume deletion (run_surreal_tuned_retest.sh, line 8):** Remove `|| true` from `docker compose down -v --remove-orphans`. Add explicit volume verification:
```bash
reset_stack() {
  local store="$1"
  docker compose down -v --remove-orphans  # no || true
  if docker volume ls -q | grep -q surreal_data; then
    docker volume rm "$(basename $(pwd))_surreal_data" 2>/dev/null || echo "WARNING: volume rm failed"
  fi
  SURREAL_STORE="$store" docker compose up -d surrealdb falkordb
  python wait_for_services.py
}
```

**Version stamp (yar_bench.py, lines 933-938):** Try `SELECT * FROM sys::version()` first (confirmed available in SurrealDB 3.1.3+), fall back to `INFO FOR DB`:
```python
try:
    ver = self._q("SELECT * FROM sys::version();")
    return {"surreal_version": str(ver)[:200], "surreal_info_db": str(self._q("INFO FOR DB;"))[:500]}
except Exception:
    return {"surreal_info_db": str(self._q("INFO FOR DB;"))[:500]}
```

---

## 6. Run the Benchmark (PATCH11)

### 6.1 Clean State

```bash
cd ~/repos/cytognosis/yar_supervisor_reproducible_benchmark_package

# Kill any running containers
docker rm -f yar-surrealdb yar-falkordb yar-neo4j 2>/dev/null || true

# Remove all related volumes (critical: prevents dimension contamination)
cd db_benchmark
docker compose down -v --remove-orphans 2>/dev/null || true
docker volume ls -q | grep -E 'db_benchmark|surreal|falkor|neo4j' | xargs -r docker volume rm 2>/dev/null || true

# Activate the environment
source .venv/bin/activate
```

### 6.2 Pre-Run Validation Checks

Before the full run, verify each of these:
```bash
# 1. Verify FTS alias form is in place
grep -n "search::score" yar_bench.py
# Both occurrences must show: search::score(0) AS score ... ORDER BY score DESC

# 2. Verify dim defaults and confirm --dim 384 is passed in the run scripts
grep -n "\-\-dim" run_surreal_tuned_retest.sh

# 3. Verify SurrealDB image is v3.1.5 in docker-compose.yml
grep "surrealdb/surrealdb" docker-compose.yml

# 4. Verify FalkorDB image is pinned (not 'latest')
grep "falkordb/falkordb" docker-compose.yml

# 5. Verify requirements are pinned to == specifiers
grep ">=" requirements.txt
# Should be empty or zero matches after pinning
```

### 6.3 Run the Tuned DB Benchmark

Use `run_surreal_tuned_retest.sh`, NOT `run_full.sh`. The full script has the volume contamination bug.

```bash
./run_surreal_tuned_retest.sh
```

This runs (in order), calling `reset_stack()` with fresh volumes before each case:
1. 10k RocksDB + HNSW: sqlite, falkordb, surrealdb_tuned (strict validation on)
2. 10k RocksDB + DISKANN: surrealdb_tuned only
3. 10k SurrealKV + HNSW: surrealdb_tuned only (pre-existing single-engine probe)
4. 100k RocksDB + HNSW: sqlite, falkordb, surrealdb_tuned (strict on)
5. 10k SurrealKV + HNSW comparable: sqlite, falkordb, surrealdb_tuned (new in PATCH11)
6. 100k SurrealKV + HNSW comparable: sqlite, falkordb, surrealdb_tuned (new in PATCH11)

Expected total runtime: 90-150 minutes on Linux x86_64 (longer than Ali's M3 MacBook run).

Monitor the 100k SurrealDB import (expected ~290 seconds):
```bash
docker logs -f yar-surrealdb
```

### 6.4 Collect Results

```bash
./collect_tuned_results.sh
# Produces: yar_surreal_tuned_results_slim.zip
```

### 6.5 Compare Against PATCH10 Baseline

```bash
# Copy the PATCH10 reference
cp ../reference_results/final_db_slim.zip ./

python compare_surreal_tuned.py \
  --old final_db_slim.zip \
  --new yar_surreal_tuned_results_slim.zip \
  --out PATCH11_VS_PATCH10_COMPARISON.md
```

### 6.6 Validity Gates

A run is valid for architecture comparison only if ALL of the following hold. Check each before reporting results:

1. `surrealdb_tuned/engine_meta.json` contains `"validation_fts_body_not_table_iterator": "True"` and `"validation_vector_has_knn": "True"`.
2. `lexical_search` p50 for `surrealdb_tuned` at 10k is under 20 ms. If 200+ ms, PATCH10 FTS fix has not landed.
3. No `fulltext_failed_contains_fallback` in any strict-run `engine_meta.json`.
4. `task_lookup` p50 for `surrealdb_tuned` at 10k is under 10 ms (target after async port; if still 46 ms, the async SDK port did not take effect).
5. Every run case's `engine_meta.json` records SurrealDB version, FalkorDB version, and date.
6. `RUN_MANIFEST.md` exists alongside output zips recording: hardware, Python version, Docker version, image tags, and applied code revisions.

---

## 7. Iterate (PATCH11 Tuning Loop)

If any validity gate fails, use this loop:

1. Check `engine_meta.json` for the specific failure:
   - `fts_body_runtime: "body fulltext failed"` or `"fulltext_failed_contains_fallback"`: FTS query still broken; re-check the ORDER BY alias form and the index definition.
   - `task_lookup` p50 still ~46 ms: async SDK port did not work; confirm the class name and that no new `AsyncSurreal()` is created per query.
   - `build_import` still 24k ms at 10k: transaction wrapping still wrong; check the three-call pattern landed correctly.

2. For each fix applied, run `EXPLAIN FULL` and `INFO FOR TABLE` before the full benchmark:
   ```surrealql
   -- Confirm FTS index is used
   EXPLAIN FULL SELECT yid FROM node WHERE body @0@ "test";
   -- Expected: operation = "Matches" or "Union", not "Table Iterator"

   -- Confirm HNSW index is used
   EXPLAIN FULL SELECT yid, vector::distance::knn() AS dist FROM node WHERE embedding <|5, 100|> $vec;
   -- Expected: operation = "KnnScan", index = "idx_node_vec"

   -- Confirm table schema
   INFO FOR TABLE node;
   -- Expected: FTS index and HNSW index both listed
   ```

3. Increment the patch level (PATCH12 etc.) in output directory names. Record every patch in `RUN_MANIFEST.md`.

**Success criteria for this phase:**
- No FTS fallback in any strict run.
- Persistent async connection confirmed (task_lookup < 10 ms at 10k).
- SurrealDB weighted score at 100k RocksDB + HNSW in the 3 to 5 range.
- At least one valid comparable SurrealKV run at both 10k and 100k.

---

## 8. GraphRAG Additional Desktop Benchmarks

This section implements the plan in `CYTOMEM-graphrag-integration-and-optimization.md` Section 5.

### 8.1 Query Set Construction

Construct a fixed set of 50 queries representative of cytomem agent use. The four classes are defined in the cytomem doc Section 5.2:

- **Class A (15 queries): artifact lookup** -- e.g., "Find the IGoR solution summary", "What is the latest version of the Yar feature spec".
- **Class B (15 queries): semantic recall** -- e.g., "Show me research docs about BDNF", "Find planning documents for the NSF grant".
- **Class C (10 queries): cross-repo relationship** -- e.g., "What artifacts in the docs repo relate to cytomem?", "Which tasks are linked to the IGoR track?".
- **Class D (10 queries): temporal / recency** -- e.g., "What changed in the Grants repo in the last 7 days?", "Show the history of the IGoR solution summary".

Save the query set as `benchmark/graphrag_query_set.json` with this structure:
```json
{
  "queries": [
    {"id": "A-01", "class": "A", "text": "...", "ground_truth_ids": ["cytognosis://..."]},
    ...
  ]
}
```

Ground truth for the live 7K-node graph requires manual labeling. For automated testing in this benchmark, use the top-5 results from `SEMANTIC_SEARCH` as a pseudo-ground-truth baseline (labeled as "current best"). Label at least 10 queries per class manually if possible.

### 8.2 Metrics

For each tool, measure and record:
- **Hits@5**: fraction of queries where at least one correct result is in top 5.
- **MRR**: mean reciprocal rank of first correct result.
- **P50 and P95 latency**: wall-clock from query string to result list, measured from the MCP tool call layer.

Store results in `benchmark/graphrag_results.json` and a summary table in `benchmark/GRAPHRAG_BENCHMARK_RESULTS.md`.

### 8.3 Tools to Benchmark

Implement a thin adapter for each tool that wraps its retrieval call and returns a ranked list of artifact IDs. Wire each adapter into a shared harness in `benchmark/graphrag_harness.py`:

**Baseline 1: cytomem current keyword (ARTIFACT_SEARCH)**
- Query: `WHERE a.title CONTAINS $q OR a.path CONTAINS $q OR a.repo CONTAINS $q`
- This is the O(n) scan baseline. Measure it before adding the full-text index.

**Baseline 2: cytomem current semantic (SEMANTIC_SEARCH)**
- Query: `CALL db.index.vector.queryNodes('artifact_embedding', $k, $embedding)`
- Already uses the HNSW index. This is the vector-only baseline.

**Tool 3: neo4j-graphrag HybridRetriever**
- Install: `pip install neo4j-graphrag`
- Uses both the vector index and the new full-text index (see Section 9.1 for the full-text index creation).
- Docs: [neo4j-graphrag-python documentation](https://neo4j.com/docs/neo4j-graphrag-python/current/)
- Use `HybridRetriever(driver, index_name="artifact_embedding", fulltext_index_name="artifact_fulltext")`.
- This requires the full-text index to exist first (Section 9.1).

**Tool 4: Graphiti search() (already in codebase)**
- `graphiti-core` is already in `cytomem/pyproject.toml` as a dependency.
- The `get_graphiti()` method in `src/cytomem/graph/client.py` initializes Graphiti but the MCP recall path does not call `graphiti.search()`.
- Benchmark: call `graphiti.search(query, num_results=5)` and compare recall vs the ARTIFACT_SEARCH baseline.
- Note: Graphiti uses Gemini API for LLM calls. Verify Gemini credentials are available before benchmarking Tool 4; if not, record as "credentials not available" and skip.

**Tool 5: LightRAG**
- Install: `pip install lightrag-hku`
- Requires a running Ollama instance with `llama3.1` (or substitute the current best local model from `ollama list`).
- Index build: run LightRAG over a 1,000-artifact subset of the cytomem graph (not the full 7k; index build is ~3 minutes per 1k docs with a local LLM).
- Reference: cytomem GraphRAG doc Section 5.3 (Tools to Benchmark).

### 8.4 Reporting

Wire results into the existing harness via a thin adapter as described in the cytomem doc Section 5.5. Produce:
1. `benchmark/GRAPHRAG_BENCHMARK_RESULTS.md` with the Hits@5, MRR, P50, P95 table for all tools.
2. An updated `STORAGE_BENCHMARK_TRACKER.md` note on the GraphRAG results.

---

## 9. cytomem Assessment and Optimization

Read these files before making any changes:
- `https://github.com/cytognosis/cytomem/blob/main/src/cytomem/graph/queries.py`
- `https://github.com/cytognosis/cytomem/blob/main/src/cytomem/graph/client.py`
- `https://github.com/cytognosis/cytomem/blob/main/src/cytomem/mcp/tools.py`
- `https://github.com/cytognosis/cytomem/blob/main/pyproject.toml`

### 9.1 Fix 1: Add Full-Text Index (Priority 1)

The current `ARTIFACT_SEARCH` query uses `CONTAINS` (O(n) linear scan, no index). Add a Lucene-backed full-text index.

Run this Cypher once against the live Neo4j at `bolt://localhost:7687`:
```cypher
CREATE FULLTEXT INDEX artifact_fulltext IF NOT EXISTS
FOR (a:Artifact)
ON EACH [a.title, a.path, a.repo, a.artifact_type]
OPTIONS { indexConfig: { `fulltext.analyzer`: 'standard-no-stop-words' } }
```

Then update `src/cytomem/graph/queries.py`: replace `ARTIFACT_SEARCH` with:
```cypher
CALL db.index.fulltext.queryNodes('artifact_fulltext', $q)
YIELD node AS a, score
RETURN a.repo AS repo, a.path AS path,
       a.title AS title, a.artifact_type AS type,
       a.modified_at AS modified_at
ORDER BY score DESC
LIMIT $limit
```

Also update any callers in `src/cytomem/mcp/tools.py` and `src/cytomem/cli.py` that pass the query variable to ARTIFACT_SEARCH: confirm the parameter name matches (`$q` or `$query`; the current query uses `$q`).

Measure before-and-after latency for a representative query at 7k nodes. Record the results in `cytomem/benchmark/CYTOMEM_OPTIMIZATION_REPORT.md`.

### 9.2 Fix 2: Activate Graphiti Recall Path

The `get_graphiti()` method in `src/cytomem/graph/client.py` initializes Graphiti but the `cytomem_recall` MCP tool in `src/cytomem/mcp/tools.py` does not use it. The Graphiti `search()` call adds BM25 + semantic + graph traversal + temporal recency weighting in a single call.

Add a `semantic_graphiti=False` parameter to the MCP `cytomem_recall` tool. When set to True, route the recall through `graphiti.search(query, num_results=k)` instead of the direct Cypher paths. This enables benchmarking the Graphiti path without changing the default behavior.

Implementation steps:
1. In `src/cytomem/mcp/tools.py`, in the `cytomem_recall` tool, check for the new parameter.
2. If `semantic_graphiti=True`, call `get_client().get_graphiti()` and call `graphiti.search(query, num_results=limit)`.
3. Return results in the same schema as the existing recall paths.
4. If Graphiti is not initialized (returns None), fall back to `SEMANTIC_SEARCH`.

Note: Graphiti requires Gemini credentials (or a compatible LLM client). The `GeminiLLMClient` in `src/cytomem/graph/gemini_llm.py` uses Application Default Credentials. If ADC is not configured, Graphiti will fall back to the `dummy_llm.py` stub. Record whether Graphiti was fully initialized in the benchmark results.

### 9.3 Benchmark Recall Paths Before and After

Run the 50-query set from Section 8.1 against:
1. cytomem keyword (CONTAINS, before fix).
2. cytomem keyword (full-text index, after fix 9.1).
3. cytomem semantic (SEMANTIC_SEARCH, unchanged).
4. cytomem Graphiti (after fix 9.2, if Gemini credentials available).

Record Hits@5, MRR, P50, and P95 for each. Append results to `cytomem/benchmark/CYTOMEM_OPTIMIZATION_REPORT.md`.

### 9.4 Keep-Neo4j Recommendation Assessment

After the benchmarks in Sections 8 and 9, assess whether the keep-Neo4j recommendation (from the cytomem GraphRAG doc Section 4.1) is supported by the evidence. The recommendation should be confirmed if:
- The full-text index reduces keyword-search latency to under 5 ms (from ~sub-100ms CONTAINS scan).
- HybridRetriever Hits@5 is comparable to or better than the SEMANTIC_SEARCH baseline.
- There is no evidence of latency degradation that would justify migrating to FalkorDB.

Record the assessment in `cytomem/benchmark/CYTOMEM_OPTIMIZATION_REPORT.md` as a one-paragraph "Keep Neo4j / Reconsider Migration" verdict with evidence.

---

## 10. Deliverables

The agent must produce all of the following before reporting success:

### Benchmark deliverables

1. **PATCH11 results zip:** `yar_surreal_tuned_results_slim.zip` (or equivalent for the latest patch number).
2. **Comparison table:** `PATCH11_VS_PATCH10_COMPARISON.md` (or equivalent) showing SurrealDB weighted scores vs PATCH10 baseline. Format:

   | Engine | PATCH10 Score (100k) | PATCH11 Score (100k) | Delta |
   |---|---|---|---|
   | FalkorDB | 4.26 | [measured] | [delta] |
   | SQLite | 5.49 | [measured] | [delta] |
   | SurrealDB tuned (RocksDB) | 9.38 | [measured] | [delta] |
   | SurrealDB tuned (SurrealKV) | N/A (not comparable in PATCH10) | [measured] | N/A |

3. **RUN_MANIFEST.md** alongside the results, documenting hardware, versions, and all applied code revisions.
4. **Updated `STORAGE_BENCHMARK_TRACKER.md`** (Section 1 master status table and Section 3 open decisions): update O-3 (SurrealDB benchmark retest) and add a new O-9 entry for the SurrealKV comparable run result.

### cytomem deliverables

5. **cytomem optimization branch:** a git branch in the cytomem repo named `cytomem-graphrag-opt-2026-06` with the full-text index creation script and the `ARTIFACT_SEARCH` query update.
6. **cytomem optimization report:** `cytomem/benchmark/CYTOMEM_OPTIMIZATION_REPORT.md` with:
   - Before-and-after latency for keyword search (CONTAINS scan vs full-text index).
   - Recall quality table (Hits@5, MRR) for all four paths (keyword-old, keyword-new, semantic, Graphiti).
   - Keep-Neo4j verdict paragraph with evidence.

### Final summary

7. **Summary statement** (inline in your response, not a file) covering:
   - Whether SurrealDB reached the 3 to 5 range.
   - If not, what specific issue remains blocking it.
   - Whether the cytomem full-text index fix was applied successfully.
   - Whether the Graphiti path was activated and what recall improvement it showed.

---

## 11. Abort Conditions

Stop and report without completing the run if any of the following occurs:

- The async SDK port causes the entire benchmark suite to fail (not just SurrealDB): undo the async port and revert to sync, note the failure, and continue with the remaining items.
- Docker volume cleanup fails after three retries: do not proceed with a contaminated run; report the Docker state.
- SurrealDB consistently hangs at build_import for more than 10 minutes at 100k: note the hang, capture `docker logs yar-surrealdb`, and report. Do not kill and retry more than twice.
- The cytomem Neo4j is not running at `bolt://localhost:7687`: note this, skip Section 9, and proceed with Sections 7 and 8.

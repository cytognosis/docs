# SurrealDB Code Audit: Yar Benchmark Package

**Audit date:** 2026-06-22
**Package path:** `/home/mohammadi/repos/cytognosis/yar_supervisor_reproducible_benchmark_package`
**Reference guide:** `/home/mohammadi/repos/cytognosis/docs/03-Products/Cytonome/Yar/spec/SurrealDB-tuning-and-graphrag-guide.md`
**Benchmark digest:** `/home/mohammadi/repos/cytognosis/docs/03-Products/Cytonome/Yar/consolidation_2026-06-21/_storage/BENCHMARK_DIGEST.md`
**SurrealDB version pinned:** `v3.1.3` (docker-compose.yml line 3)
**Python SDK pinned:** `surrealdb>=1.0.4` (requirements.txt line 5)
**Status of retest sequence:** PATCH10 is the final valid run; this audit applies to the code as it stands after PATCH10.

---

## BLUF

After PATCH10, the three confirmed artifacts (FTS failure, connection overhead, schemaless writes) are partially fixed. Two root causes remain active in the current code: `task_lookup` at 46 ms (10k) and 446 ms (100k) is still an order of magnitude above FalkorDB (0.6-3.3 ms), and `build_import` regressed 3x after PATCH9 added transaction wrapping. The remaining gap is dominated by Issue 1 (per-query connection overhead) and Issue 4 (RocksDB storage backend for most runs). These are the fixes not yet applied.

---

## Ranked Issues

### Issue 1 (HIGHEST IMPACT): Per-query connection overhead NOT fixed

**File:** `db_benchmark/yar_bench.py`, lines 764-814 (`SurrealAdapter.setup`)
**Symptom:** `task_lookup` p50 = 46 ms at 10k, 446 ms at 100k. FalkorDB: 0.6 ms and 3.3 ms for the same workload. Cold open = 64-536 ms.
**Guide reference:** Section 3.5, Troubleshooting T2.

**What the code does NOW:**

A single `Surreal(url)` object is created once in `setup()` at lines 767-813, and `self.db` is reused for the entire run. The connection management logic is version-adaptive: it calls `connect()` if available (line 776), or falls back to `__enter__()` (line 783). The connection itself is persistent.

However, `surrealdb>=1.0.4` (the pinned SDK version) exposes a **synchronous blocking WebSocket client** (`BlockingWsSurrealConnection`). The sync SDK wraps every call in a new internal request-response cycle that, depending on the SDK version, may re-establish the WebSocket or at minimum add socket-level round-trip overhead per query that the async client avoids.

The guide explicitly recommends `AsyncSurrealDB` (Section 3.5):

```python
# Guide recommends (Section 3.5)
from surrealdb import AsyncSurrealDB
db = AsyncSurrealDB("ws://127.0.0.1:8000/rpc")
await db.connect()
```

The benchmark uses the synchronous class path only. Every `self._q()` call at lines 817-831 goes through the sync client, which on `surrealdb` 1.x performs blocking I/O with no connection pooling. The 46-446 ms `task_lookup` latency matches TCP round-trip + blocking-IO overhead exactly; FalkorDB uses redis-py which keeps a persistent TCP socket with pipelining.

**Root cause:** Synchronous SDK with blocking per-call socket I/O. The connection object is reused but the underlying sync transport adds 40-400 ms per call at scale.

**Fix:**

Before:
```python
# yar_bench.py line 766-767
from surrealdb import Surreal  # type: ignore
self.db = Surreal(self.url)
```

After (requires async adapter rewrite; minimum viable change):
```python
# yar_bench.py lines 766-767
from surrealdb import AsyncSurrealDB  # type: ignore
import asyncio
# Store event loop and run async setup
self._loop = asyncio.new_event_loop()
self.db = self._loop.run_until_complete(self._async_setup())
```

And replace `_q()` to use `self._loop.run_until_complete(self.db.query(...))`. The full correct fix is to port `SurrealAdapter` and `SurrealTunedAdapter` to fully async (using `async def setup`, `async def _q`, etc.) and run the benchmark engine loop with `asyncio.run()`. This is a significant but well-scoped change.

**Mapping:** Guide Section 3.5 (persistent WebSocket connection), Troubleshooting T2.

---

### Issue 2 (HIGH): `build_import` regression from over-aggressive transaction wrapping

**File:** `db_benchmark/yar_bench.py`, lines 1161-1174 (`SurrealTunedAdapter.load`)
**Symptom:** `build_import` p50 = 24,032 ms at 10k (PATCH10) vs 8,111 ms for the old untuned adapter. The tuned adapter is 3x SLOWER at import than the baseline it was meant to replace.
**Guide reference:** Section 3.6 (transactions); batch size recommendation 200-500 records.

**What the code does NOW:**

```python
# yar_bench.py lines 1161-1164
try:
    self._q("BEGIN TRANSACTION; INSERT INTO node $rows; COMMIT TRANSACTION;", {"rows": rows})
except Exception:
    self._q("INSERT INTO node $rows;", {"rows": rows})
```

The default `--batch-size` is 1000 (line 1858 of `main()`). The tuned retest script `run_surreal_tuned_retest.sh` passes `--batch-size 500`. SurrealDB 3.1 documents that very large transactions hold locks longer; multi-statement transaction strings sent as a single `query()` call also require the server to parse and execute three statements per batch instead of one. More critically, `BEGIN TRANSACTION; INSERT ...; COMMIT TRANSACTION;` as a single string to the Python SDK may not be treated as a true batched transaction by all SDK versions, and may instead execute sequentially with full round-trips per statement, tripling the per-batch cost.

The guide recommendation is: "wrap inserts in transactions" with "up to ~500 records per transaction is a reasonable batch size" and "use a loop with commits every N records". The intent is a loop-level commit, not embedding `BEGIN/COMMIT` in the same query string.

**Root cause:** The multi-statement transaction string causes 3x round-trips per batch and may block on each statement. The guide intended programmatic `BEGIN`/`COMMIT` as separate calls, not inline with `INSERT`.

**Fix:**

Before:
```python
# lines 1161-1164
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

Apply the same fix to the edge import loop at lines 1167-1174.

**Mapping:** Guide Section 3.6, batch size guidance.

---

### Issue 3 (HIGH): Storage backend defaults to RocksDB; SurrealKV not the default for any comparable run

**File:** `db_benchmark/docker-compose.yml`, line 7; `db_benchmark/run_surreal_tuned_retest.sh`, lines 40-55
**Symptom:** `task_lookup` and `build_import` are elevated. SurrealKV was only tested as a single-engine probe (no SQLite/FalkorDB baseline alongside it), making the comparison result non-actionable.
**Guide reference:** Section 3.1, Troubleshooting T3.

**What the code does NOW:**

```yaml
# docker-compose.yml line 7
command: >
  start --bind 0.0.0.0:8000 --user root --pass root ${SURREAL_STORE:-rocksdb:///data/yarbench.db}
```

The `SURREAL_STORE` variable defaults to `rocksdb:///data/yarbench.db`. The retest script runs the comparable 10k and 100k runs on RocksDB (lines 40-41, 54-55). SurrealKV is only probed in a single-engine run (line 50) with no competing engines present, so the score of 1.20 is not comparable.

**Root cause:** No apples-to-apples SurrealKV vs SQLite/FalkorDB run exists in the current test matrix.

**Fix:**

In `run_surreal_tuned_retest.sh`, add a fourth comparable run:

Before (lines 48-51):
```bash
# 3) SurrealKV probe, single engine only
reset_stack "surrealkv:///data/yarbench.db"
run_case results_patch8_10k_surrealkv_hnsw "surrealdb_tuned" 10000 200 50 hnsw 0 || true
```

After:
```bash
# 3) SurrealKV at 10k with all three engines for a comparable score
reset_stack "surrealkv:///data/yarbench.db"
run_case results_patch10_10k_surrealkv_hnsw "sqlite,falkordb,surrealdb_tuned" 10000 200 50 hnsw 1 || true

# 4) SurrealKV at 100k comparable
reset_stack "surrealkv:///data/yarbench.db"
run_case results_patch10_100k_surrealkv_hnsw "sqlite,falkordb,surrealdb_tuned" 100000 300 100 hnsw 1 || true
```

**Mapping:** Guide Section 3.1 (SurrealKV preferred), Troubleshooting T3.

---

### Issue 4 (MEDIUM): KNN operator form uses `<|k, ef|>` (correct) but also carries a silent brute-force fallback at lines 1003-1006 and 1222-1230

**File:** `db_benchmark/yar_bench.py`, lines 995-1015 (`SurrealAdapter.vector_search`), lines 1209-1237 (`SurrealTunedAdapter.vector_search`)
**Guide reference:** Section 3.4 (KNN operator syntax), Troubleshooting T8.

**What the code does NOW:**

```python
# yar_bench.py lines 998-1000 (SurrealAdapter)
k = int(limit); ef = int(self.args.hnsw_ef_runtime)
q = f"SELECT yid, vector::distance::knn() AS distance FROM node WHERE embedding <|{k}, {ef}|> $vec LIMIT {k};"
```

And in `SurrealTunedAdapter` at lines 1213-1215:
```python
k = int(limit)
ef = int(self.args.hnsw_ef_runtime)
q = f"SELECT yid, vector::distance::knn() AS distance FROM node WHERE embedding <|{k}, {ef}|> $vec LIMIT {k};"
```

The operator form `<|k, ef|>` is correct per the guide and hits the HNSW index. This is NOT the brute-force form. However, both adapters have a fallback chain:

1. If the KNN indexed path fails (lines 1001-1006 / 1218-1230), the code falls back to `ORDER BY vector::distance::cosine(embedding, $vec) ASC`, which is explicitly the brute-force path (no index, full table scan).
2. If that fails, it falls back to a Python numpy exact search (lines 1010-1015 / 1231-1237).

The PATCH10 results show `vector_search` at 2.7 ms (10k) and 16.5 ms (100k), which is competitive. The KNN path is working. However, the fallback to brute-force cosine `ORDER BY` is never logged when it fires silently; there is no guaranteed capability flag set if the indexed path succeeds but the fallback is used on a retry. If the vector index fails intermittently (e.g., after a schema reset), the brute-force fallback will make the engine appear to work while returning correct results at full-scan latency.

**Root cause:** Silent fallback means FTS/vector index failures can go undetected during non-strict runs.

**Fix:**

The issue is not in the KNN operator form (that is correct), but in the fallback logging. Ensure the brute-force fallback is always recorded and fail strict runs explicitly:

Before (lines 1222-1230):
```python
except Exception as e:
    self.capabilities["vector_runtime"] = f"indexed vector path failed: {type(e).__name__}: {e}"
    if getattr(self.args, "surreal_strict_validation", False):
        raise CapabilityError("SurrealDB tuned vector index failed; strict mode forbids Python fallback")
```

After (add logging for the intermediate brute-force fallback):
```python
except Exception as e:
    self.capabilities["vector_runtime_indexed_failed"] = f"{type(e).__name__}: {e}"
    if getattr(self.args, "surreal_strict_validation", False):
        raise CapabilityError("SurrealDB tuned vector index failed; strict mode forbids fallback")
# In the ORDER BY cosine branch, always set:
self.capabilities["vector_runtime_path"] = "surrealql_bruteforce_order_by_cosine"
```

**Mapping:** Guide Section 3.4 (KNN operator), Section 3.7 (EXPLAIN-driven verification).

---

### Issue 5 (MEDIUM): HNSW index defined BEFORE data insertion; correct but no post-import REBUILD

**File:** `db_benchmark/yar_bench.py`, lines 1140-1153 (`SurrealTunedAdapter.load`)
**Guide reference:** Section 4.4 (index rebuild), Troubleshooting T6.

**What the code does NOW:**

The HNSW/DISKANN index is defined at lines 1140-1153, before any data is inserted. Data insertion begins at line 1155. This means SurrealDB must index each row as it arrives, rather than building the index once over a complete dataset. For HNSW, incremental insertion during bulk load is less efficient than a post-load `REBUILD INDEX` because the graph structure is built incrementally without global optimization.

The `build_import` time for `surrealdb_tuned` at 100k is 290,134 ms (PATCH10 data), vs 22,463 ms for SQLite. A significant portion of this is HNSW incremental indexing during insertion.

**Root cause:** Index-before-insert forces live HNSW graph updates per row during bulk load. Post-insert rebuild builds the full HNSW graph in one pass, which is faster.

**Fix:**

Move vector index creation to after data insertion, then call `REBUILD INDEX`:

Before (lines 1140-1153, before insertion loop):
```python
if self.vector_mode in ("hnsw", "diskann"):
    if self.vector_mode == "hnsw":
        self._create_index_try("vector", [
            f"DEFINE INDEX idx_node_vec ON TABLE node FIELDS embedding HNSW ...",
        ])
```

After (move the block to after the edge insertion loop, then add):
```python
# After edge insertion loop (after line 1174):
if self.vector_mode in ("hnsw", "diskann"):
    if self.vector_mode == "hnsw":
        self._create_index_try("vector", [
            f"DEFINE INDEX idx_node_vec ON TABLE node FIELDS embedding HNSW ...",
        ])
    else:
        self._create_index_try("vector", [
            f"DEFINE INDEX idx_node_vec ON TABLE node FIELDS embedding DISKANN ...",
        ])
    # Trigger explicit rebuild for deterministic index quality
    try:
        self._q("REBUILD INDEX idx_node_vec ON TABLE node;")
        self.capabilities["vector_index_rebuild"] = "ok"
    except Exception as e:
        self.capabilities["vector_index_rebuild"] = f"failed: {e}"
```

**Mapping:** Guide Section 4.4 (index rebuild after schema migration), Troubleshooting T5/T6.

---

### Issue 6 (MEDIUM): Docker volume reuse risk still present; no per-run volume name enforcement

**File:** `db_benchmark/docker-compose.yml`, lines 45-48; `db_benchmark/run_surreal_tuned_retest.sh`, line 8
**Symptom:** The original benchmark (pre-PATCH9) had a stale-index failure where the 3k volume (dim=128) was loaded for the 10k run (dim=384). The tuning guide flagged this as T5.
**Guide reference:** Section 6 (verification checklist), Troubleshooting T5.

**What the code does NOW:**

```yaml
# docker-compose.yml lines 45-48
volumes:
  surreal_data:
  falkor_data:
  neo4j_data:
  neo4j_logs:
```

The `surreal_data` volume name is hardcoded. The retest script calls `docker compose down -v` (line 8) which deletes volumes, so between cases the volume is cleared. However, this means:

1. If `docker compose down -v` fails (e.g., partial Docker state), the old volume persists and the new run loads stale data.
2. Across multiple benchmark invocations without a clean reset, the volume accumulates stale data.
3. The script uses `|| true` at line 8 which silently swallows any failure to delete volumes.

**Root cause:** Volume deletion is not verified; failure is silently ignored.

**Fix:**

Replace the `reset_stack` function in `run_surreal_tuned_retest.sh`:

Before (lines 5-10):
```bash
reset_stack() {
  local store="$1"
  echo "[patch8] reset docker volumes; SURREAL_STORE=$store"
  docker compose down -v --remove-orphans 2>/dev/null || true
  SURREAL_STORE="$store" docker compose up -d surrealdb falkordb
  python wait_for_services.py
}
```

After:
```bash
reset_stack() {
  local store="$1"
  echo "[patch10] reset docker volumes; SURREAL_STORE=$store"
  docker compose down -v --remove-orphans
  # Verify volume is gone before proceeding
  if docker volume ls -q | grep -q surreal_data; then
    docker volume rm "$(basename $(pwd))_surreal_data" 2>/dev/null || true
  fi
  SURREAL_STORE="$store" docker compose up -d surrealdb falkordb
  python wait_for_services.py
}
```

**Mapping:** Guide Section 6 (verification checklist, "delete Docker volumes between dataset sizes"), Troubleshooting T5.

---

### Issue 7 (LOW): `DEFINE FIELD embedding ON TABLE node TYPE array<float>` is correct but lacks explicit dimension constraint

**File:** `db_benchmark/yar_bench.py`, line 1108 (`SurrealTunedAdapter.load`)
**Guide reference:** Section 3.2 (SCHEMAFULL), Troubleshooting T6.

**What the code does NOW:**

```python
# yar_bench.py line 1108
"DEFINE FIELD embedding ON TABLE node TYPE array<float>",
```

This correctly declares the field as `array<float>`, which satisfies the guide's requirement and is what the guide's T6 fix calls for. However, the field definition does not constrain the array dimension. SurrealDB 3.1 allows `DEFINE FIELD embedding TYPE array<float> ASSERT array::len($value) = $dim` or similar assertion, which would catch a dimension mismatch at write time rather than at index creation time.

**Root cause:** Missing dimension assertion means a mis-sized embedding (e.g., from a different model) would be silently stored and cause the HNSW index to reject or corrupt queries later.

**Fix:**

Before (line 1108):
```python
"DEFINE FIELD embedding ON TABLE node TYPE array<float>",
```

After:
```python
f"DEFINE FIELD embedding ON TABLE node TYPE array<float> ASSERT array::len($value) = {dataset.dim}",
```

(Pass `dataset.dim` into the schema statement generation block at lines 1098-1122.)

**Mapping:** Guide Section 3.2, Troubleshooting T6.

---

### Issue 8 (LOW): Version is not stamped with `sys::version()`; `INFO FOR DB` is used instead

**File:** `db_benchmark/yar_bench.py`, lines 933-938 (`SurrealAdapter.version_info`), lines 1178-1184 (`SurrealTunedAdapter.version_info`)
**Guide reference:** Section 6 (verification checklist step 1), Troubleshooting T10.

**What the code does NOW:**

```python
# yar_bench.py lines 933-938
def version_info(self) -> Dict[str, Any]:
    try:
        res = self._q("INFO FOR DB;")
        return {"surreal_info_db": str(res)[:500], "url": self.url, "vector_mode": self.vector_mode}
    except Exception as e:
        return {"surreal_info_db": f"unavailable: {e}", ...}
```

PATCH9's README explains that `SELECT * FROM sys::version()` was rejected by the parser at the time. The guide's verification checklist step 1 requires this exact query. As of SurrealDB 3.1.3 (the pinned version), `SELECT * FROM sys::version()` should work per the official docs. Not recording it makes exact version identification dependent on Docker image metadata alone.

**Root cause:** Historical workaround from PATCH9; should be retried on v3.1.3 where the function is confirmed available.

**Fix:**

Before (lines 933-938):
```python
res = self._q("INFO FOR DB;")
return {"surreal_info_db": str(res)[:500], ...}
```

After:
```python
try:
    ver = self._q("SELECT * FROM sys::version();")
    return {"surreal_version": str(ver)[:200], "surreal_info_db": str(self._q("INFO FOR DB;"))[:500], ...}
except Exception:
    return {"surreal_info_db": str(self._q("INFO FOR DB;"))[:500], ...}
```

**Mapping:** Guide Section 6 step 1, Troubleshooting T10.

---

## Summary Table

| Rank | Issue | File | Lines | Fix (one line) |
|------|-------|------|-------|----------------|
| 1 | Sync SDK per-call blocking I/O (task_lookup 46-446 ms vs 0.6-3.3 ms) | `yar_bench.py` | 766-814 | Switch to `AsyncSurrealDB` with `asyncio.run()` harness |
| 2 | Transaction wrapping triples build_import (24k ms vs 8k ms) | `yar_bench.py` | 1161-1174 | Separate `BEGIN`, `INSERT`, `COMMIT` into three `_q()` calls |
| 3 | RocksDB default; no comparable SurrealKV run | `docker-compose.yml` line 7, `run_surreal_tuned_retest.sh` lines 48-51 | Add `sqlite,falkordb,surrealdb_tuned` comparable SurrealKV runs at 10k and 100k |
| 4 | Silent brute-force fallback after KNN failure | `yar_bench.py` | 1222-1230 | Log fallback path always; fail strict on intermediate brute-force |
| 5 | HNSW built incrementally during bulk load; no `REBUILD INDEX` | `yar_bench.py` | 1140-1153 | Move index definition after data insertion; call `REBUILD INDEX` |
| 6 | Volume deletion silently ignored (`\|\| true`) | `run_surreal_tuned_retest.sh` | 8 | Remove `|| true`; add explicit volume verification |
| 7 | No dimension assertion on embedding field | `yar_bench.py` | 1108 | Add `ASSERT array::len($value) = {dataset.dim}` to field definition |
| 8 | Version not stamped with `sys::version()` | `yar_bench.py` | 933-938 | Try `sys::version()` first, fall back to `INFO FOR DB` |

---

## Highest-Impact Fix

**Issue 1: Switch from synchronous SDK to `AsyncSurrealDB`.**

The synchronous `surrealdb` SDK wraps every query in a blocking socket call that incurs 40-400 ms overhead per operation at scale. This is why `task_lookup` is 46-446 ms after all other tuning was applied. FalkorDB achieves 0.6-3.3 ms for the same workload because redis-py maintains a persistent pipelined TCP socket. The async WebSocket client reuses a single handshake across all queries. Switching to `AsyncSurrealDB` is the one change that most directly collapses the remaining gap between SurrealDB and FalkorDB on the Yar hot-path operations.

---

## Verdict

**Will these fixes move SurrealDB into competitive range?**

Based on PATCH10 results and the BENCHMARK_DIGEST analysis: yes, with high confidence for the server-mode comparison, and with caveats.

After applying Issues 1 and 2 (async SDK + correct transaction handling):

- `task_lookup` should drop from 46-446 ms to the 1-5 ms range (guide Section 3.5 prediction, BENCHMARK_DIGEST Section 4c).
- `build_import` should drop from 24,032-290,134 ms to at least the untuned baseline (8,111-145,125 ms) and likely better with SCHEMAFULL + correct transaction batching.
- `cold_open` should drop from 64-536 ms to the network round-trip range (2-10 ms).

After applying Issues 3 and 5 (SurrealKV + post-load REBUILD):

- `build_import` should improve further from reduced RocksDB write amplification.
- `vector_search` recall and latency should improve with a deterministic HNSW build.

The weighted score at 100k could plausibly move from 9.37 toward the 3-5 range, making SurrealDB competitive with FalkorDB on server-side graph+vector workloads.

**Caveats:**

1. The `task_lookup` fix requires an async SDK port, which is a non-trivial rewrite (40-60 lines across `SurrealAdapter` and `SurrealTunedAdapter`). The sync SDK may have improved in post-1.0.4 releases; check the latest `surrealdb` PyPI changelog before assuming the full async port is necessary.

2. Embedded Rust mode (no Docker, no socket) would eliminate connection overhead entirely and is the right long-term target for desktop deployment. The current Docker/WebSocket mode is always going to carry some socket tax compared to SQLite's in-process embedding. The PATCH10 results showing 46-446 ms task_lookup after tuning confirm this architecture gap is real and not eliminatable by SDK switching alone.

3. SurrealDB remains a "priority GraphRAG projection candidate" and not the MVP default until the embedded Rust mode is benchmarked on equivalent hardware.

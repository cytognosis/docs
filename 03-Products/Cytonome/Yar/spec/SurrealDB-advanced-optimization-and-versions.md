---
status: Draft
date: 2026-06-22
author: "@shahin"
audience: engineers
tags: [surrealdb, performance, versions, optimization, graphrag]
---

# SurrealDB Advanced Optimization and Version Guide

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: engineers, stakeholders
> **Tags**: `yar`, `spec`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)

**BLUF.** The benchmark was pinned to 3.1.3; the current latest is 3.1.5 (security fix, June 19 2026). Pin production to 3.1.5. The single highest-impact change remaining in the rerun is switching from the synchronous SDK to `AsyncSurreal`, which collapses task_lookup from 46-446 ms to the 1-5 ms range. This guide is a companion to [SurrealDB-tuning-and-graphrag-guide.md](./SurrealDB-tuning-and-graphrag-guide.md); read that first, then use this for advanced configs, resolved unknowns, and the ordered rerun checklist.

---

## 1. Latest Versions and Relevant Changes

The benchmark was pinned to **v3.1.3**. The current latest stable is **v3.1.5** (June 19, 2026). Source: [SurrealDB releases page](https://surrealdb.com/releases).

### Release table: performance-relevant changes

| Version | Date | Performance-Relevant Change |
|---------|------|-----------------------------|
| **3.1.5** | Jun 19, 2026 | Security-focused patch (graph traversal bug fix, permissions). Drop-in from any 3.1.x. No on-disk layout change. **Recommended pin for rerun and production.** Source: [surrealdb.com/releases](https://surrealdb.com/releases) |
| 3.1.4 | Jun 10, 2026 | Fixed `type::field('id')` equality not using record-id point lookup (was doing a full table scan instead). Permissions fix on file buckets. Source: [surrealdb.com/releases/3.1](https://surrealdb.com/releases/3.1) |
| 3.1.3 | Jun 3, 2026 | Fixed cold-start "Session not found" race in engine router (relevant to benchmark cold_open). Clearer kNN query plans in EXPLAIN (`predicate` attribute on KnnScan). Fixed graph traversal with inline filter returning no results. In-flight queries cancelled when WebSocket closes. Source: [surrealdb.com/releases/3.1](https://surrealdb.com/releases/3.1) |
| 3.1.0 | May 26, 2026 | **DiskANN GA** alongside HNSW; both gain F16/U8/I8 types and COSINE_NORMALIZED/INNER_PRODUCT metrics. **HNSW vector search up to 8x faster** (warm-lookup path rewritten with process-local caches). Predicate prefilter on every KV scan (pushes WHERE predicates to raw bytes before decode). Single-scan `->edge->vertex` graph traversals (vertex adjacency keys embed target, one range scan vs two). Per-row clone elimination on projection hot path. RocksDB upgraded to 11.0.0 with prefix bloom filters and blob-file separation. SurrealKV updated to 0.21.2. `DEFINE INDEX` on ANN now drains pending vectors before returning (immediately usable). Durable distributed index build coordination. Source: [surrealdb.com/blog/surrealdb-3-1-stability-diskann-and-a-new-release-process](https://surrealdb.com/blog/surrealdb-3-1-stability-diskann-and-a-new-release-process) |
| 3.0.x | Feb-Mar 2026 | New streaming execution engine. HNSW concurrent writes on vector indexes. Streaming results as produced. Strict mode moved to `DEFINE DATABASE STRICT`. Source: [surrealdb.com/releases/3.0](https://surrealdb.com/releases/3.0) |
| 2.5.0 | Jan 22, 2026 | **`DEFER` keyword added (Experimental)** for background index building. WebSocket limits made configurable. Source: [surrealdb.com/releases](https://surrealdb.com/releases) |
| 2.4.0 | Nov 24, 2025 | 32-bit floats now default for HNSW (halves memory vs F64 at negligible accuracy loss). Source: [surrealdb.com/releases](https://surrealdb.com/releases) |

### Version recommendation

**Benchmark rerun:** pin to `surrealdb/surrealdb:v3.1.5` in docker-compose.yml. This is the latest stable, includes the cold-start race fix from 3.1.3 (relevant to cold_open numbers), the point-lookup fix from 3.1.4 (relevant to task_lookup), and the HNSW 8x warm-path speedup from 3.1.0. Drop-in from 3.1.3, no schema changes needed.

**Production:** same pin; upgrade monthly per [SurrealDB's new monthly release schedule](https://surrealdb.com/blog/introducing-our-new-monthly-release-schedule).

---

## 2. Advanced Optimization Configs

### 2.1 Server and Capabilities

The complete production-oriented startup command for a Yar server node:

```bash
surreal start \
  --user root --pass "$SURREALDB_PASS" \
  --bind 127.0.0.1:8000 \
  --log info \
  --index-compaction-interval 5s \
  --query-timeout 30s \
  --transaction-timeout 60s \
  --slow-log-threshold 100 \
  --allow-scripting \
  --allow-funcs "array, string, search, vector, math, type, time, encoding" \
  --deny-net \
  "surrealkv://data/yar.db?sync=every"
```

**Key flags not in the base guide:**

| Flag | Env Var | Effect |
|------|---------|--------|
| `--index-compaction-interval 5s` | `SURREAL_INDEX_COMPACTION_INTERVAL` | Controls how often background index compaction runs (default 5s). Lower if index reads degrade after heavy writes. |
| `--query-timeout 30s` | `SURREAL_QUERY_TIMEOUT` | Kills runaway queries. Set to match your SLA. |
| `--slow-log-threshold 100` | `SURREAL_SLOW_QUERY_LOG_THRESHOLD` | Logs any query over 100 ms. Essential for identifying new regressions in production. |
| `SURREAL_MEMORY_THRESHOLD` | (env only, no CLI flag) | Memory pressure cap; when reached, server starts rejecting new requests and cancelling transactions to reduce heap. Set to e.g. `2GiB` for a constrained desktop. See section 6 for verification. |
| `SURREAL_ROCKSDB_PERIODIC_COMPACTION_SECONDS` | (env) | Default 3600. Controls version overhang and tombstone accumulation. Raise if write-heavy and compaction causes latency spikes. |
| `SURREAL_ROCKSDB_SCAN_VERIFY_CHECKSUMS` | (env) | Default `true`. Set to `false` on trusted storage to skip CRC32C on scan reads for higher cold-scan throughput. |
| `SURREAL_SCAN_BATCH_SIZE` | (env) | Default 1000. Reduce if large scans are starving the scheduler. |

**Strict mode in 3.x.** In 3.0+, `--strict` no longer exists as a CLI flag. Set strict mode at the database level:

```surrealql
DEFINE DATABASE yar STRICT;
```

This prevents automatic table creation and forces all schema to be declared before use, eliminating accidental schemaless writes. Source: [surreal start docs](https://surrealdb.com/docs/reference/cli/surrealdb-cli/commands/start).

### 2.2 Storage Backend Selection and Tuning

**Decision table:**

| Backend | When to Use | Key Characteristic |
|---------|-------------|-------------------|
| `surrealkv://path?sync=every` | Desktop (embedded Rust) and server Yar node | MVCC store, lower write amplification than RocksDB, native to SurrealDB. Default sync=every = most durable. |
| `surrealkv://path?sync=never` | Benchmark rerun only (no durability needed) | Maximize throughput; leaves flushing to OS. |
| `surrealkv://path?sync=5s` | Mobile on-device server with battery concern | Periodic sync, trades slight durability for battery. |
| `rocksdb://path?sync=every` | Production multi-node, format stability required | Proven format; SurrealKV format may change across SurrealDB minor versions. |
| `memory` | CI, testing, single benchmark run | No persistence; fastest possible. |

**SurrealKV tuning note (3.x).** In 3.x, the datastore URL accepts query parameters:

```bash
# SurrealKV with durability tuning
surrealkv://data/yar.db?sync=every

# SurrealKV with periodic flush (lower write overhead)
surrealkv://data/yar.db?sync=5s

# RocksDB with no sync (benchmark mode)
rocksdb://data/yar.db?sync=never
```

Source: [surreal start datastore configuration](https://surrealdb.com/docs/reference/cli/surrealdb-cli/commands/start#datastore-configuration).

**RocksDB compaction:** Run `ALTER SYSTEM COMPACT` periodically (or `ALTER TABLE memo COMPACT`) to push data to L6 with Zstd compression. This is especially important after large bulk imports.

```surrealql
-- Manual compaction (production maintenance window)
ALTER SYSTEM COMPACT;
```

### 2.3 Connection and Async Client

**Critical update from the code audit.** The Python SDK version pinned in the benchmark (`surrealdb>=1.0.4`) uses a synchronous blocking client. The SDK has since released version 2.0.0 with `AsyncSurreal` as the preferred async class. The class name changed from `AsyncSurrealDB` (referenced in the base guide) to `AsyncSurreal` in SDK 2.0.0. Source: [surrealdb PyPI](https://pypi.org/project/surrealdb/), [SurrealDB Python SDK docs](https://surrealdb.com/docs/sdk/python).

**Correct async client pattern for SDK 2.0.0:**

```python
from surrealdb import AsyncSurreal  # SDK 2.0.0+; class renamed from AsyncSurrealDB

# Connect once at benchmark/app startup; reuse for all queries
async def setup_db() -> AsyncSurreal:
    db = AsyncSurreal("ws://localhost:8000/rpc")
    await db.connect()
    await db.sign_in({"user": "root", "pass": "secret"})
    await db.use("yar", "personal")
    return db

# Run benchmark with a single event loop
import asyncio

async def main():
    db = await setup_db()
    # All queries reuse the same WebSocket session
    result = await db.query("SELECT * FROM memo WHERE id = $id", {"id": "memo:abc"})
    # ...

asyncio.run(main())
```

If you must wrap async in a sync harness (e.g., because the benchmark framework is synchronous):

```python
import asyncio
from surrealdb import AsyncSurreal

class SurrealAdapter:
    def __init__(self, url: str):
        self._loop = asyncio.new_event_loop()
        self.db: AsyncSurreal = self._loop.run_until_complete(self._async_setup(url))

    async def _async_setup(self, url: str) -> AsyncSurreal:
        db = AsyncSurreal(url)
        await db.connect()
        await db.sign_in({"user": "root", "pass": "secret"})
        await db.use("yar", "personal")
        return db

    def _q(self, query: str, params: dict | None = None):
        return self._loop.run_until_complete(self.db.query(query, params or {}))
```

**Do not** create a new `AsyncSurreal()` per query. Every instantiation triggers a new WebSocket handshake (40-400 ms overhead per call). Source: [Code Audit Issue 1](../research/SURREALDB_CODE_AUDIT.md).

### 2.4 Query and Index Tuning

**Index hints and forced plans.** SurrealDB 3.x does not expose explicit index hints in SurrealQL syntax. The query planner selects the index automatically. To force index use, verify with `EXPLAIN FULL` and ensure the field type and index definition exactly match the query predicate:

```surrealql
-- Check which plan the planner chose
EXPLAIN FULL
  SELECT id FROM memo WHERE content @0@ "anxiety";

-- Expected output includes operation: "Matches" or "Union" (index path)
-- If you see "Table Iterator", the FTS index is missing or misconfigured
```

**Graph traversal without N+1.** In 3.1.0+, single-hop `->edge->vertex` traversals use a one-scan path. Multi-hop traversals still benefit from writing the full path inline:

```surrealql
-- Efficient: one statement, one traversal (3.1.0+ one-scan path for first hop)
SELECT
  ->mentions->concept->related_to->concept AS related_concepts
FROM memo:abc;

-- Avoid: N+1 pattern (fetch memos then loop in application code)
-- SELECT id FROM memo; -- then for each id: SELECT ->mentions->concept FROM memo:X
```

**LIMIT push-down.** Always add `LIMIT` before `ORDER BY` when you only need top-k results. In 3.1.0+, the planner can push LIMIT into a bounded KV scan:

```surrealql
-- Planner can push LIMIT into the index scan (3.1.0+)
SELECT id, content FROM memo
WHERE content @0@ "focus"
ORDER BY search::score(0) DESC
LIMIT 10;
```

**Projections.** Select only needed fields. Avoid `SELECT *` in inner subqueries:

```surrealql
-- Good: project only needed fields
SELECT id, content, vector::distance::knn() AS dist
FROM memo
WHERE embedding <|10, 100|> $qvec;

-- Avoid in hot paths:
SELECT * FROM memo WHERE embedding <|10, 100|> $qvec;
```

### 2.5 Concurrency and PARALLEL

The `PARALLEL` keyword in SurrealQL is available but not well-documented for when it fires:

```surrealql
-- PARALLEL applies to multi-table SELECT or subquery fanout
-- It does NOT parallelize a single-table scan
SELECT * FROM memo, concept PARALLEL;

-- For Yar's single-table hot path queries, PARALLEL has no effect
-- It is most useful in analytics queries over many tables
```

**Server-level concurrency.** SurrealDB 3.x uses a Tokio async runtime with automatic thread management. There are no exposed thread count flags in the `surreal start` CLI as of 3.1.5. Tokio defaults to one thread per CPU core. For Docker deployments, set CPU limits explicitly:

```yaml
# docker-compose.yml
services:
  surrealdb:
    cpus: '4.0'       # give SurrealDB 4 cores
    mem_limit: '4g'   # hard OOM limit via Docker
```

### 2.6 Transaction and Batch Tuning

**Correct transaction pattern (addresses Code Audit Issue 2).** Do NOT embed `BEGIN TRANSACTION; ...; COMMIT TRANSACTION;` as a single query string. Issue each as a separate SDK call:

```python
# Correct: three separate _q() calls
self._q("BEGIN TRANSACTION;")
try:
    self._q("INSERT INTO node $rows;", {"rows": rows})
    self._q("COMMIT TRANSACTION;")
except Exception as e:
    try:
        self._q("CANCEL TRANSACTION;")
    except Exception:
        pass
    # Fallback to non-transactional insert
    self._q("INSERT INTO node $rows;", {"rows": rows})
```

**Batch size guidance by dataset:**

| Dataset Size | Recommended Batch Size | Notes |
|-------------|----------------------|-------|
| < 1k records | 50-100 | Minimal overhead; small transactions |
| 1k-10k | 200-300 | Balance lock duration vs round-trips |
| 10k-100k | 300-500 | Guide recommendation (Section 3.6 in base guide) |
| > 100k | 200-400 | Larger transactions hold locks longer; test empirically |

**Bulk insert without transaction (faster for append-only import):**

```surrealql
-- INSERT accepts an array; send as one payload, no explicit transaction needed
-- Internally atomic per INSERT statement
INSERT INTO memo $rows;
```

### 2.7 Vector Index Parameter Tuning by Dataset Size

HNSW parameters (M, EFC) trade memory and build time for recall quality. DISKANN parameter (DEGREE, L_BUILD) trades disk IO for build time and recall.

**HNSW:**

| Dataset | M | EFC | TYPE | Notes |
|---------|---|-----|------|-------|
| < 5k records (mobile) | 8-12 | 80-100 | F32 | Low memory; acceptable recall for personal-scale data |
| 5k-50k (desktop) | 16 | 150-200 | F32 | Guide default; good recall/memory balance |
| > 50k (desktop/server) | 20-32 | 200-400 | F32 | Higher recall; build time increases; consider DISKANN instead |

**DISKANN** (3.1.0+ GA, 64-bit only):

| Dataset | DEGREE | L_BUILD | TYPE | Notes |
|---------|--------|---------|------|-------|
| 10k-100k | 16 | 64 | F32 | Guide syntax `DISKANN DIMENSION 384 DIST COSINE TYPE F32 DEGREE 16 L_BUILD 64` |
| > 100k | 32 | 128 | F32 | Higher recall; disk-resident so less memory pressure than HNSW at scale |
| Memory-constrained | 16 | 64 | F16 | F16 halves disk footprint; negligible recall loss for semantic search |

**Full syntax for benchmark rerun:**

```surrealql
-- HNSW for 10k dataset (matches benchmark)
DEFINE INDEX idx_node_vec ON TABLE node
  FIELDS embedding
  HNSW DIMENSION 384
  DIST COSINE
  TYPE F32
  M 16
  EFC 200;

-- DISKANN for 10k dataset (matches benchmark DISKANN probe)
DEFINE INDEX idx_node_vec ON TABLE node
  FIELDS embedding
  DISKANN DIMENSION 384
  DIST COSINE
  TYPE F32
  DEGREE 16
  L_BUILD 64;
```

Source: [SurrealDB vector indexes docs](https://surrealdb.com/docs/learn/data-models/vector-search/vector-indexes), [DEFINE INDEX docs](https://surrealdb.com/docs/reference/query-language/statements/define/indexes).

### 2.8 Embedded Rust Mode vs Server Mode

**Performance comparison:**

| Mode | Latency | Overhead | When to Use |
|------|---------|----------|-------------|
| Embedded Rust (`SurrealKv` in-process) | Sub-millisecond for simple lookups; no socket | Zero network, no Docker, no serialization | Desktop native app (macOS/Linux/Windows) |
| Server mode (Docker/WebSocket) | 2-10 ms minimum per query even with async client (TCP + WebSocket) | Socket round-trip, serialization overhead | Development, multi-user server, benchmarks |

**Desktop Rust embedding:**

```rust
use surrealdb::engine::local::SurrealKv;
use surrealdb::Surreal;

// No socket, no Docker, no serialization overhead
let db: Surreal<surrealdb::engine::local::Db> =
    Surreal::new::<SurrealKv>("./yar_data/db").await?;
db.use_ns("yar").use_db("personal").await?;
```

**Implication for benchmarks.** The current benchmark runs SurrealDB in Docker/WebSocket mode, which is always going to carry socket overhead compared to SQLite's in-process embedding. The benchmark's task_lookup comparison (SurrealDB 46 ms vs SQLite sub-1 ms) conflates architecture with engine quality. The true comparison is:

- SurrealDB embedded Rust vs SQLite embedded: more comparable
- SurrealDB server vs FalkorDB server: the correct server-to-server comparison

Source: [SurrealDB embedding in Rust docs](https://surrealdb.com/docs/surrealdb/embedding/rust).

---

## 3. GraphRAG Maximum-Performance Configuration

This section gives the end-to-end recommended setup for graph traversal, vector KNN, and BM25 full-text combined, targeting Yar's personal knowledge graph workload.

### 3.1 Schema Setup (Run Once)

```surrealql
-- Database with strict mode (3.x syntax)
DEFINE DATABASE yar STRICT;

-- Analyzer (defined at DB level, shared across tables)
DEFINE ANALYZER yar_analyzer
  TOKENIZERS class, blank, punct
  FILTERS lowercase, ascii, snowball(english);

-- Memo (core node)
DEFINE TABLE memo SCHEMAFULL;
DEFINE FIELD id           ON TABLE memo TYPE record;
DEFINE FIELD content      ON TABLE memo TYPE string;
DEFINE FIELD embedding    ON TABLE memo TYPE array<float>
  ASSERT array::len($value) = 384;   -- dimension guard (3.x syntax)
DEFINE FIELD source       ON TABLE memo TYPE string;
DEFINE FIELD created_at   ON TABLE memo TYPE datetime;
DEFINE FIELD updated_at   ON TABLE memo TYPE datetime;

-- Concept (named entity node)
DEFINE TABLE concept SCHEMAFULL;
DEFINE FIELD id           ON TABLE concept TYPE record;
DEFINE FIELD name         ON TABLE concept TYPE string;
DEFINE FIELD embedding    ON TABLE concept TYPE array<float>
  ASSERT array::len($value) = 384;

-- Edge: memo -> concept
DEFINE TABLE mentions SCHEMAFULL TYPE RELATION IN memo OUT concept;
DEFINE FIELD weight       ON TABLE mentions TYPE float;

-- Edge: concept -> concept
DEFINE TABLE related_to SCHEMAFULL TYPE RELATION IN concept OUT concept;
DEFINE FIELD rel_type     ON TABLE related_to TYPE string;
```

### 3.2 Index Setup (After Data Import, Not Before)

**Key insight from Code Audit Issue 5.** Define vector indexes AFTER bulk data import. If you define HNSW before inserting data, SurrealDB updates the graph incrementally per row during import. Defining it after allows a single-pass build with `REBUILD INDEX`, which produces better graph structure and faster build time.

```surrealql
-- Step 1: import all data (no vector index yet)

-- Step 2: define all indexes after import completes
DEFINE INDEX idx_memo_content ON TABLE memo
  FIELDS content
  FULLTEXT ANALYZER yar_analyzer
  BM25(1.2, 0.75)
  HIGHLIGHTS;

DEFINE INDEX idx_memo_vec ON TABLE memo
  FIELDS embedding
  HNSW DIMENSION 384
  DIST COSINE
  TYPE F32
  M 16
  EFC 200;

DEFINE INDEX idx_concept_vec ON TABLE concept
  FIELDS embedding
  HNSW DIMENSION 384
  DIST COSINE
  TYPE F32
  M 12
  EFC 150;

-- Step 3: trigger explicit rebuild for deterministic index quality
REBUILD INDEX idx_memo_vec ON TABLE memo;
REBUILD INDEX idx_concept_vec ON TABLE concept;

-- Step 4: verify (always before first query)
INFO FOR TABLE memo;
```

### 3.3 Maximum-Performance Hybrid Query

The recommended end-to-end GraphRAG query for Yar, combining all three retrieval modes in one SurrealQL statement:

```surrealql
-- Inputs
LET $qvec = [...];       -- 384-dim query embedding
LET $qtext = "focus anxiety sleep";   -- query text

-- Step 1: vector similarity (top 20 candidates)
-- Use <|k, ef|> form to hit the HNSW index; NEVER use <|k, COSINE|>
LET $vs = (
  SELECT id
  FROM memo
  WHERE embedding <|20, 150|> $qvec
);

-- Step 2: BM25 full-text (top 20 candidates)
LET $ft = (
  SELECT id, search::score(0) AS score
  FROM memo
  WHERE content @0@ $qtext
  ORDER BY search::score(0) DESC
  LIMIT 20
);

-- Step 3: graph expansion from top vector hits
-- 3.1.0+ uses a single range scan for first-hop traversal
LET $top_concepts = (
  SELECT ->mentions->concept.id AS cid
  FROM $vs[*]
  LIMIT 10
);
LET $graph = (
  SELECT <-mentions<-memo.id AS id
  FROM $top_concepts[*].cid
  LIMIT 15
);

-- Step 4: fuse with Reciprocal Rank Fusion (k=60 smoothing constant)
search::rrf([$vs, $ft, $graph], 10, 60);
```

**Verification before using this query:**

```surrealql
-- Confirm HNSW index is being used (not brute force)
EXPLAIN FULL
  SELECT id, vector::distance::knn() AS dist
  FROM memo
  WHERE embedding <|5, 100|> [0.1, 0.2]; -- abbreviated

-- Expected: operation = "KnnScan", index = "idx_memo_vec"
-- If you see "TableScan": the HNSW index is missing or the field type is wrong

-- Confirm FTS index is being used (not CONTAINS fallback)
EXPLAIN FULL
  SELECT id FROM memo WHERE content @0@ "focus";

-- Expected: operation = "Matches" or "Union"
-- If you see "TableScan": the FTS index was not created or uses wrong analyzer name
```

---

## 4. The Maximum-Performance Checklist

Ordered by impact, highest first. Items marked [AUDIT] are fixes from the code audit that were not yet applied in PATCH10.

**Before the benchmark rerun:**

1. **[AUDIT, CRITICAL] Switch to `AsyncSurreal` (SDK 2.0.0).** Replace `from surrealdb import Surreal` with `from surrealdb import AsyncSurreal`. Rewrite `SurrealAdapter` and `SurrealTunedAdapter` to use `asyncio.run()` or a single persistent event loop. Expected drop: task_lookup 46-446 ms → 1-5 ms. This is the single largest latency reduction available. Source: [Code Audit Issue 1](../research/SURREALDB_CODE_AUDIT.md).

2. **[AUDIT, HIGH] Fix transaction wrapping in `build_import`.** Separate `BEGIN TRANSACTION`, `INSERT INTO node $rows`, and `COMMIT TRANSACTION` into three `_q()` calls (not one multi-statement string). Expected: build_import drops from 24k ms back toward the 8k ms untuned baseline and likely better. Source: [Code Audit Issue 2](../research/SURREALDB_CODE_AUDIT.md).

3. **[AUDIT, HIGH] Add SurrealKV comparable runs.** Change `docker-compose.yml` default from `rocksdb://` to `surrealkv://` (with `sync=every` for fair comparison) and run the full 10k and 100k benchmark against all three engines. The DISKANN-only SurrealKV probe scored 1.20 but is not comparable because it ran without SQLite and FalkorDB. Source: [Code Audit Issue 3](../research/SURREALDB_CODE_AUDIT.md).

4. **[VERSION] Pin to `surrealdb/surrealdb:v3.1.5`.** Replaces the benchmark's 3.1.3 pin. Includes cold-start race fix, record-id point-lookup fix, and all 3.1.0 HNSW performance gains. Source: [surrealdb.com/releases](https://surrealdb.com/releases).

5. **[SCHEMA] Move vector index definition to after data import.** Define HNSW/DISKANN after all rows are inserted, then call `REBUILD INDEX`. Eliminates incremental per-row HNSW graph updates during bulk load. Expected: build_import improvement at 100k. Source: [Code Audit Issue 5](../research/SURREALDB_CODE_AUDIT.md).

6. **[SCHEMA] Add `SCHEMAFULL` and `DEFINE DATABASE STRICT`.** Eliminates per-write type inference overhead. Already in PATCH10 but confirm via `INFO FOR TABLE` output.

7. **[SCHEMA] Add embedding dimension assertion.** Add `ASSERT array::len($value) = {dim}` to the embedding field definition. Prevents silent dimension mismatch that corrupts HNSW at the next dataset size. Source: [Code Audit Issue 7](../research/SURREALDB_CODE_AUDIT.md).

8. **[QUERY] Confirm KNN operator form uses `<|k, ef|>` not `<|k, COSINE|>`.** The `<|k, COSINE|>` form bypasses the HNSW index entirely and runs brute force. The current code uses `<|k, ef|>` correctly but has a silent brute-force fallback on failure. Add explicit logging for the fallback path. Source: [Code Audit Issue 4](../research/SURREALDB_CODE_AUDIT.md).

9. **[INFRA] Remove `|| true` from volume reset.** Silently swallowed volume deletion failures cause stale index data across runs. Verify volume deletion explicitly. Source: [Code Audit Issue 6](../research/SURREALDB_CODE_AUDIT.md).

10. **[VERIFY] Stamp version with `SELECT * FROM sys::version()`** at the start of every run. The current code uses `INFO FOR DB` as a workaround from an earlier patch; the `sys::version()` function is confirmed available in 3.1.3+. Source: [Code Audit Issue 8](../research/SURREALDB_CODE_AUDIT.md).

11. **[VERIFY] Run `INFO FOR TABLE memo` before first query** and confirm: HNSW/DISKANN index listed, FTS index listed, field types correct. Reject any run where an expected index is missing.

12. **[TUNING, PRODUCTION ONLY] Set `DEFINE DATABASE yar STRICT`** to catch accidental schemaless writes at the query level, not just at insert time.

13. **[TUNING, PRODUCTION ONLY] Set `SURREAL_MEMORY_THRESHOLD`** environment variable for memory pressure management on constrained deployments. No CLI flag exists; must be an env var.

14. **[PRODUCTION ONLY] Run `ALTER SYSTEM COMPACT`** after large bulk imports to push data to L6 with Zstd and eliminate tombstone overhead.

---

## 5. Benchmark Rerun Configuration

The following changes to the benchmark package are required for a valid rerun. This cross-references the code audit directly.

### docker-compose.yml changes

```yaml
# Current (line 7 of docker-compose.yml):
command: >
  start --bind 0.0.0.0:8000 --user root --pass root ${SURREAL_STORE:-rocksdb:///data/yarbench.db}

# Change to:
command: >
  start --bind 0.0.0.0:8000 --user root --pass root
  --index-compaction-interval 5s
  --slow-log-threshold 100
  ${SURREAL_STORE:-surrealkv:///data/yarbench.db}

# Change image tag (line 3 or image: line):
# From: surrealdb/surrealdb:v3.1.3
# To:   surrealdb/surrealdb:v3.1.5
```

### run_surreal_tuned_retest.sh changes

```bash
# Replace the reset_stack function to remove || true on volume deletion:
reset_stack() {
  local store="$1"
  docker compose down -v --remove-orphans  # no || true
  if docker volume ls -q | grep -q surreal_data; then
    docker volume rm "$(basename $(pwd))_surreal_data" 2>/dev/null || true
  fi
  SURREAL_STORE="$store" docker compose up -d surrealdb falkordb
  python wait_for_services.py
}

# Add comparable SurrealKV runs at 10k and 100k (alongside SQLite and FalkorDB):
reset_stack "surrealkv:///data/yarbench.db"
run_case results_rerun_10k_surrealkv "sqlite,falkordb,surrealdb_tuned" 10000 200 50 hnsw 1 || true

reset_stack "surrealkv:///data/yarbench.db"
run_case results_rerun_100k_surrealkv "sqlite,falkordb,surrealdb_tuned" 100000 300 100 hnsw 1 || true
```

### yar_bench.py changes (summary)

| Issue | File | Lines | Required Change |
|-------|------|-------|----------------|
| Sync SDK | yar_bench.py | 766-814 | Replace `from surrealdb import Surreal` with `AsyncSurreal`; port adapter to asyncio |
| Transaction wrapping | yar_bench.py | 1161-1174 | Separate BEGIN, INSERT, COMMIT into three `_q()` calls |
| Index timing | yar_bench.py | 1140-1153 | Move HNSW/DISKANN index definition to after data insertion; call `REBUILD INDEX` |
| Fallback logging | yar_bench.py | 1222-1230 | Log brute-force fallback path explicitly |
| Dimension assert | yar_bench.py | 1108 | Add `ASSERT array::len($value) = {dataset.dim}` |
| Version stamp | yar_bench.py | 933-938 | Try `SELECT * FROM sys::version()` first; fall back to `INFO FOR DB` |

Full code for each fix is in [SURREALDB_CODE_AUDIT.md](../research/SURREALDB_CODE_AUDIT.md).

---

## 6. Resolved Unverified Items

The base guide flagged three items as unverified. All three are now resolved.

### Memory-limit flag name

**Resolved.** The `--memory-limit` CLI flag does **not exist** in `surreal start` as of 3.1.5. The current `surreal start --help` output lists no memory-specific flag. Memory pressure management is via the environment variable `SURREAL_MEMORY_THRESHOLD`. When set, the server begins rejecting new HTTP and WebSocket RPC requests and can cancel running transactions when heap usage exceeds the threshold. Set as an env var, not a CLI flag:

```bash
SURREAL_MEMORY_THRESHOLD=2GiB surreal start surrealkv://data/yar.db
```

Docker equivalent:

```yaml
environment:
  - SURREAL_MEMORY_THRESHOLD=2GiB
```

Source: [SurrealDB start command docs](https://surrealdb.com/docs/reference/cli/surrealdb-cli/commands/start), [GitHub PR #5221](https://github.com/surrealdb/surrealdb/pull/5221).

### DEFER keyword status

**Resolved.** `DEFER` was introduced as **Experimental in SurrealDB 2.5.0** (January 22, 2026), not 3.1 as implied by the base guide's description of "3.1 adds a `DEFER` keyword (experimental)". It carries through 3.0 and 3.1 and remains experimental as of 3.1.5. The base guide's warning ("do not use in production yet") stands.

How to use it when you accept the experimental status:

```surrealql
-- Requires SURREAL_CAPS_ALLOW_EXPERIMENTAL=defer (unverified exact tag; check docs)
-- Or: --allow-experimental defer

DEFINE INDEX idx_memo_vec ON TABLE memo
  FIELDS embedding
  HNSW DIMENSION 384
  DIST COSINE
  TYPE F32
  M 16
  EFC 200
  DEFER;   -- builds in background; does not block DEFINE INDEX return
```

**Do not use `DEFER` in the benchmark rerun.** It would make the index unavailable immediately after `DEFINE INDEX` returns, producing incorrect query results until the background build completes. Instead use the post-import `REBUILD INDEX` pattern from Section 3.2.

Source: [SurrealDB 2.5 release notes](https://surrealdb.com/releases), [SurrealDB DEFINE INDEX docs](https://surrealdb.com/docs/reference/query-language/statements/define/indexes).

### SurrealKV production stability

**Resolved.** SurrealKV is in active use in SurrealDB 3.x production deployments. It was updated to 0.21.2 in SurrealDB 3.1.0 (with memtable size increase for large transactions) and to 0.22.0 in 3.1.3. SurrealDB 3.0's GA announcement describes it as production-ready in conjunction with the 3.x line. Source: [SurrealDB 3.0 GA announcement](https://surrealdb.com/blog/introducing-surrealdb-3-0--the-future-of-ai-agent-memory), [SurrealKV releases](https://github.com/surrealdb/surrealkv/releases).

**Remaining caveat:** the file format may change between SurrealDB minor versions (0.21 to 0.22 is an example). Before upgrading SurrealDB, verify the SurrealKV version in the release notes and export/reimport if a format change is noted. For production deployments where format stability is critical, use `rocksdb://` until SurrealKV publishes a stable format guarantee (not yet as of 3.1.5). For Yar development and the benchmark rerun, SurrealKV is safe and preferred.

---

## 7. Sources

- [SurrealDB releases page (all versions, latest 3.1.5)](https://surrealdb.com/releases)
- [SurrealDB 3.1 release notes (3.1.0-3.1.4, full changelog)](https://surrealdb.com/releases/3.1)
- [SurrealDB 3.1 blog post (DiskANN GA, HNSW 8x speedup, predicate prefilter)](https://surrealdb.com/blog/surrealdb-3-1-stability-diskann-and-a-new-release-process)
- [SurrealDB 3.0 blog post (GA, streaming executor)](https://surrealdb.com/blog/introducing-surrealdb-3-0--the-future-of-ai-agent-memory)
- [surreal start command docs (all CLI flags, no --memory-limit flag)](https://surrealdb.com/docs/reference/cli/surrealdb-cli/commands/start)
- [SurrealDB environment variables](https://surrealdb.com/docs/surrealdb/cli/env)
- [SURREAL_MEMORY_THRESHOLD PR #5221](https://github.com/surrealdb/surrealdb/pull/5221)
- [DEFINE INDEX docs (HNSW, DISKANN, FTS, DEFER syntax)](https://surrealdb.com/docs/reference/query-language/statements/define/indexes)
- [SurrealDB vector indexes docs (parameters, KNN operator)](https://surrealdb.com/docs/learn/data-models/vector-search/vector-indexes)
- [SurrealDB Python SDK docs (AsyncSurreal, SDK 2.0.0)](https://surrealdb.com/docs/sdk/python)
- [surrealdb PyPI (SDK version history)](https://pypi.org/project/surrealdb/)
- [SurrealDB embedding in Rust docs](https://surrealdb.com/docs/surrealdb/embedding/rust)
- [SurrealKV GitHub (version history, releases)](https://github.com/surrealdb/surrealkv)
- [SurrealDB monthly release schedule announcement](https://surrealdb.com/blog/introducing-our-new-monthly-release-schedule)
- [SurrealDB 3.x benchmarks](https://surrealdb.com/benchmarks)
- [SurrealDB GraphRAG blog post](https://surrealdb.com/blog/graph-rag-does-not-need-a-graph-database-it-needs-a-database-that-does-everything)
- [SURREALDB_CODE_AUDIT.md (benchmark code issues 1-8)](../research/SURREALDB_CODE_AUDIT.md)
- [BENCHMARK_DIGEST.md (original benchmark results and root-cause analysis)](../_archive/consolidation_2026-06-21/_storage/BENCHMARK_DIGEST.md)
- [SurrealDB-tuning-and-graphrag-guide.md (base guide this document extends)](./SurrealDB-tuning-and-graphrag-guide.md)

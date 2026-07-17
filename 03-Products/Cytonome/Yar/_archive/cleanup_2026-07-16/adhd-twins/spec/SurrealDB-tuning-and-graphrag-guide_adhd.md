> **Status**: Draft
> **Date**: 2026-06-22
> **Author**: Cytognosis Foundation
> **Audience**: engineers
> **Tags**: `yar`, `surrealdb`, `performance`, `graphrag`, `tuning`, `flutter`, `adhd-friendly`

Technical source: ../SurrealDB-tuning-and-graphrag-guide.md

# ⚡ SurrealDB Tuning, Troubleshooting, and GraphRAG Guide for Yar

> [!NOTE]
> **TL;DR**: SurrealDB 3.1's last-place benchmark finish was caused by three fixable configuration artifacts: FTS index failure, per-call connection overhead, and the wrong storage backend. Fix those three issues first. This guide shows you exactly how.
> **Full source**: [SurrealDB-tuning-and-graphrag-guide.md](../SurrealDB-tuning-and-graphrag-guide.md)

**Reading time**: ~8 minutes.

**If you only read one thing**: the Troubleshooting Table (Section 2). The three highest-priority fixes (T1, T2, T3) will likely drop the 100k weighted score from 8.68 to the 2-4 range.

> [!TIP]
> **SurrealDB 3.1 ships DISKANN as a GA second vector index.** This is a major improvement for larger-than-memory workloads on desktop. The benchmark ran on what appears to have been an older or misconfigured setup.

---

## 🔍 Overview

This guide covers four concerns:

1. **Troubleshooting** the benchmark failures and common pitfalls
2. **Configuration and optimization** with concrete SurrealQL and startup command examples
3. **GraphRAG** data model and query patterns combining vector KNN, BM25 full-text, and graph traversal
4. **Phone vs desktop config profiles** for the Flutter app

**Target version**: SurrealDB 3.1.x. The Flutter Dart SDK (`surrealdb` v1.1.2) connects via WebSocket only; it does not embed SurrealDB in-process. See Section 5 for mobile architecture.

---

## ⚡ Quick Start: Three Highest-Impact Fixes

1. **Fix FTS index** (T1): define the `ANALYZER` and `FULLTEXT ANALYZER` index before running any lexical query; verify with `INFO FOR TABLE`.
2. **Use a persistent WebSocket** (T2): call `connect()` once at startup and reuse it. This single fix likely collapses `task_lookup` latency from 400ms to under 5ms.
3. **Use SurrealKV backend** (T3): set `surrealkv:///data/yar.db` in the Docker startup command instead of the default RocksDB.

> [!TIP]
> **T2 (persistent WebSocket) is the single highest-impact fix.** Opening a new connection per query adds 40-400ms overhead. This one change can transform the benchmark result.

---

## 📖 2. Troubleshooting Table

| # | Symptom | Likely Cause | Fix |
|---|---|---|---|
| **T1** | Lexical search 200-450ms; benchmark marks `CONTAINS` fallback | FTS index never created or failed silently | Define `ANALYZER` + `FULLTEXT ANALYZER` index; verify with `INFO FOR TABLE`; see Section 3.3 |
| **T2** | `task_lookup` 50-400ms even for small datasets | Per-call HTTP or WebSocket reconnect | Use async WebSocket client with single `connect()` at startup; see Section 3.5 |
| **T3** | `build_import` and `task_lookup` slow; Docker shows default backend | Default Docker uses RocksDB | Set `surrealkv://data` as storage path; see Section 3.1 |
| **T4** | Writes slower than expected | Schemaless mode performs type inference on every write | Add `SCHEMAFULL` to every `DEFINE TABLE`; see Section 3.2 |
| **T5** | Vector index returns wrong results at 10k/100k | Stale Docker volume from prior run (dimension mismatch) | Run `docker volume rm <vol>` before each dataset size |
| **T6** | `DEFINE INDEX ... HNSW DIMENSION 384` fails | Field type not declared as `array<float>` | Declare `DEFINE FIELD embedding ON TABLE memo TYPE array<float>` first |
| **T7** | `EXPLAIN` shows `Full Table Scan` for record lookup | Non-id field has no index | Add `DEFINE INDEX idx_slug ON TABLE memo FIELDS slug` |
| **T8** | Hybrid RRF query 455ms p50 | FTS doing linear scan (T1) + possible brute-force vector | Fix T1 first; confirm HNSW/DISKANN index exists; use `<|k|>` not `<|k, COSINE|>` |
| **T9** | Cold open 50ms unacceptable for embedded | Docker network socket initialization | For desktop: use embedded Rust mode; for mobile: keep single persistent WebSocket open |
| **T10** | Version not recorded in benchmark | Version not stamped | Always run `SELECT * FROM sys::version()` at benchmark start |
| **T11** | `SEARCH ANALYZER` syntax error on 3.x | Breaking syntax change from pre-3.0 | Use `FULLTEXT ANALYZER` not `SEARCH ANALYZER` |
| **T12** | Queries fail in strict mode | Capabilities not explicitly granted | Add `--allow-scripting`, `--allow-net` to `surreal start` |

---

## 📖 3. Configuration and Optimization

### 3.1 Backend and Startup

> [!TIP]
> **Use SurrealKV for Yar development.** Lower write amplification than RocksDB. Use RocksDB only if you need a format stability guarantee in production today.

**Server mode (Docker):**
```bash
# SurrealKV backend (preferred)
docker run --rm -p 8000:8000 \
  -v yar_data:/data \
  surrealdb/surrealdb:3.1 \
  start --user root --pass secret \
  surrealkv:///data/yar.db

# In-memory (testing and CI only)
docker run --rm -p 8000:8000 \
  surrealdb/surrealdb:3.1 \
  start --user root --pass secret memory
```

**Embedded mode (Rust SDK, for desktop native app):**
```rust
use surrealdb::engine::local::SurrealKv;
use surrealdb::Surreal;

let db = Surreal::new::<SurrealKv>("./yar_data/db").await?;
db.use_ns("yar").use_db("personal").await?;
```

> [!NOTE]
> **What is SurrealKV vs RocksDB?** (101)
> SurrealDB's default Docker image uses RocksDB (higher write amplification). SurrealKV is SurrealDB's newer embedded MVCC backend with better performance for its access patterns. SurrealKV is marked beta/actively evolving as of 3.1; file format may change between minor versions.

### 3.2 Schemafull Tables

Always use `SCHEMAFULL`. Eliminates per-write type inference overhead.

```surrealql
DEFINE TABLE memo SCHEMAFULL;
DEFINE FIELD content   ON TABLE memo TYPE string;
DEFINE FIELD embedding ON TABLE memo TYPE array<float>;
DEFINE FIELD created_at ON TABLE memo TYPE datetime;
DEFINE FIELD source    ON TABLE memo TYPE string;

DEFINE TABLE concept SCHEMAFULL;
DEFINE FIELD name      ON TABLE concept TYPE string;
DEFINE FIELD embedding ON TABLE concept TYPE array<float>;

-- Edge table for graph relations
DEFINE TABLE mentions SCHEMAFULL TYPE RELATION IN memo OUT concept;
DEFINE FIELD weight    ON TABLE mentions TYPE float;
```

### 3.3 Full-Text Index (FTS)

> [!TIP]
> **Syntax changed at SurrealDB 3.0.** Use `FULLTEXT ANALYZER`, not `SEARCH ANALYZER`.

```surrealql
-- Define the analyzer (global, not per-table)
DEFINE ANALYZER yar_analyzer
  TOKENIZERS class, blank, punct
  FILTERS lowercase, ascii, snowball(english);

-- Define the FTS index with BM25
DEFINE INDEX idx_memo_content ON TABLE memo
  FIELDS content
  FULLTEXT ANALYZER yar_analyzer
  BM25(1.2, 0.75)
  HIGHLIGHTS;

-- Verify the index was created (critical step)
INFO FOR TABLE memo;
```

> [!NOTE]
> **What is BM25?** (101)
> Best Match 25. A full-text search ranking algorithm that scores documents by term frequency and inverse document frequency. BM25(1.2, 0.75) are the standard defaults.

### 3.4 Vector Indexes (HNSW and DISKANN)

> [!TIP]
> **Use HNSW for phone and typical desktop.** Use DISKANN for large-than-memory desktop corpora (GA in SurrealDB 3.1).

```surrealql
-- HNSW (in-memory, fast warm-cache lookups)
DEFINE INDEX idx_memo_vec ON TABLE memo
  FIELDS embedding
  HNSW DIMENSION 384
  DIST COSINE
  TYPE F32
  M 16
  EFC 200;

-- DISKANN (disk-resident, better for large corpora)
DEFINE INDEX idx_memo_vec_disk ON TABLE memo
  FIELDS embedding
  DISKANN DIMENSION 384
  DIST COSINE
  TYPE F32;
```

**KNN query syntax:**
```surrealql
-- ALWAYS use <|k|> or <|k, ef|> to hit the index
-- <|k, COSINE|> bypasses the index and runs brute force
LET $qvec = [...];
SELECT id, content, vector::distance::knn() AS dist
FROM memo
WHERE embedding <|10, 100|> $qvec
ORDER BY dist ASC;
```

> [!NOTE]
> **What is HNSW?** (101)
> Hierarchical Navigable Small World. An in-memory approximate nearest-neighbor vector index. Fast warm-cache lookups; requires the full index to fit in RAM.

### 3.5 Persistent WebSocket Connection

> [!TIP]
> **This is the single highest-impact fix.** New connection per query = 40-400ms overhead per call.

**Python SDK (benchmark retest):**
```python
from surrealdb import AsyncSurrealDB

db = AsyncSurrealDB("ws://localhost:8000/rpc")
await db.connect()
await db.sign_in({"user": "root", "pass": "secret"})
await db.use("yar", "personal")
# All subsequent queries reuse the same WebSocket session
```

**Dart/Flutter SDK:**
```dart
final db = SurrealDB('ws://localhost:8000/rpc');

Future<void> initDb() async {
  db.connect();
  await db.wait();
  await db.use('yar', 'personal');
}
// Call initDb() once at app startup; never create a new SurrealDB() per query
```

<details>
<summary>🔬 Deep Dive: Batched Inserts and EXPLAIN Tuning</summary>

**Batched inserts** (reduces write-ahead log flushes):
```surrealql
BEGIN TRANSACTION;
CREATE memo:a1 SET content = "...", embedding = [...], created_at = time::now();
CREATE memo:a2 SET content = "...", embedding = [...], created_at = time::now();
-- ~500 records per transaction is a reasonable batch size
COMMIT TRANSACTION;
```

**EXPLAIN-driven query tuning** (always confirm index usage before measuring):
```surrealql
EXPLAIN FULL
SELECT id, vector::distance::knn() AS dist
FROM memo
WHERE embedding <|10|> $qvec;
-- Look for: "operation": "Knn", "index": "idx_memo_vec"
-- If you see "Table Iterator" instead, add or fix the relevant index
```

</details>

---

## 📖 4. GraphRAG on SurrealDB

> [!NOTE]
> **What is GraphRAG?** (101)
> Graph-enhanced Retrieval-Augmented Generation. Combines vector similarity search, BM25 full-text search, and graph traversal to retrieve richer, more contextual results for an LLM. SurrealDB can run all three in a single query with no extra network hops.

### Architecture: SurrealDB as a Derived Index

**The CRDT op-log is the source of truth.** SurrealDB is a derived, queryable index rebuilt from the op-log. This means:

- Every record can be deleted and reconstructed from the op-log.
- Indexes (HNSW, DISKANN, FTS) can be dropped and rebuilt with `REBUILD INDEX`.
- Schema migrations are safe: drop, migrate, rebuild.
- Phone holds the op-log and its smaller derived index; desktop syncs the op-log and maintains a larger index independently.

### GraphRAG Hybrid Query (All Three Combined)

```surrealql
-- Step 1: vector search (top 20)
LET $qvec = [...];
LET $vs = (SELECT id FROM memo WHERE embedding <|20, 100|> $qvec);

-- Step 2: BM25 full-text search (top 20)
LET $ft = (
  SELECT id, search::score(0) AS score FROM memo
  WHERE content @0@ "focus morning"
  ORDER BY score DESC LIMIT 20
);

-- Step 3: graph expansion (memos connected to top concepts)
LET $concepts = (SELECT ->mentions->concept AS cs FROM $vs LIMIT 5);
LET $graph = (
  SELECT <-mentions<-memo.id AS id FROM $concepts[*].cs
  WHERE <-mentions<-memo.id NOT IN $vs[*].id
  LIMIT 10
);

-- Step 4: fuse all three with RRF (k=60)
search::rrf([$vs, $ft, $graph], 10, 60);
```

> [!NOTE]
> **What is RRF?** (101)
> Reciprocal Rank Fusion. A rank aggregation method that merges multiple ranked lists without needing score normalization. `search::rrf()` is built into SurrealQL.

<details>
<summary>🔬 Deep Dive: Individual Query Patterns and Graph Traversal</summary>

**Vector KNN only:**
```surrealql
LET $qvec = [...];
SELECT id, content, vector::distance::knn() AS dist
FROM memo WHERE embedding <|10, 100|> $qvec
ORDER BY dist ASC;
```

**BM25 full-text only:**
```surrealql
SELECT id, content, search::score(0) AS score
FROM memo WHERE content @0@ "morning routine focus"
ORDER BY score DESC LIMIT 10;
```

**Graph traversal (2-hop: memo -> concept -> related concept -> memo):**
```surrealql
SELECT
  <-mentions<-memo.id AS memo_id,
  <-mentions<-memo.content AS memo_content
FROM concept:focus
  ->related_to->concept
  <-mentions<-memo;
```

**Graph edge creation with RELATE:**
```surrealql
RELATE memo:a1 -> mentions -> concept:focus SET weight = 0.92;
RELATE concept:focus -> related_to -> concept:attention SET type = "associated";
```

</details>

---

## 📖 5. Phone vs Desktop Config Profiles

> [!IMPORTANT]
> **Critical for Flutter**: The `surrealdb` Dart package (v1.1.2) is a WebSocket client only. It does not embed SurrealDB in-process on iOS or Android. True in-process embedding via `flutter_rust_bridge` requires writing a Rust FFI shim and compiling for multiple mobile targets; no official embedding SDK exists as of 2026-06-21.

**Recommended mobile architecture**: run SurrealDB as a local background service on-device. The Flutter app connects to it via localhost WebSocket (`ws://127.0.0.1:PORT/rpc`). Full SurrealQL and index stack available without a custom FFI layer.

| Configuration | Phone (iOS/Android) | Desktop (macOS/Linux/Windows) |
|---|---|---|
| **Backend** | SurrealKV (via embedded server binary) | SurrealKV (embedded Rust) or DISKANN-backed |
| **Mode** | Local server binary on-device (localhost WebSocket) | Embedded Rust SDK (no socket, lowest latency) |
| **Vector index** | HNSW, F32, DIMENSION 384, M 12, EFC 100 (lower memory) | HNSW up to ~50k memos; DISKANN for larger corpora |
| **Transaction batch** | 50-100 records | 200-500 records |
| **Connection** | Single persistent WebSocket; never reconnect per query | In-process Rust SDK; no socket |

> [!TIP]
> **Share one SurrealQL schema file across both platforms.** The `DEFINE TABLE`, `DEFINE FIELD`, `DEFINE ANALYZER`, and `DEFINE INDEX` statements are identical except for HNSW M and EFC values. Use a schema templating step to swap those values by platform at init time.

---

## ✅ 6. Verification Checklist

Run this after every schema setup or retest before a benchmark.

```surrealql
-- 1. Confirm SurrealDB version
SELECT * FROM sys::version();

-- 2. Confirm indexes exist on memo table
INFO FOR TABLE memo;
-- Expected: both idx_memo_content (FTS) and idx_memo_vec (HNSW/DISKANN) present

-- 3. Confirm vector index is used (not brute force)
EXPLAIN FULL SELECT id, vector::distance::knn() AS dist
FROM memo WHERE embedding <|5|> [0.1, 0.2, ...];
-- Expected: operation = "Knn", index = "idx_memo_vec"

-- 4. Confirm FTS index is used (not CONTAINS scan)
EXPLAIN FULL SELECT id FROM memo WHERE content @0@ "focus";
-- Expected: operation = "Union" or "Matches", NOT "Table Iterator"

-- 5. Confirm record count after bulk import
SELECT count() FROM memo GROUP ALL;
```

**Before any benchmark run**: delete Docker volumes between dataset sizes (`docker volume rm yar_data`), record version output, and confirm `INFO FOR TABLE` shows all indexes before accepting the results.

---

## ➡️ What's Next?

- **Run the benchmark retest**: follow the checklist above before reporting any SurrealDB result.
- **See the tracker**: [STORAGE_BENCHMARK_TRACKER.md](../STORAGE_BENCHMARK_TRACKER.md) for the open decision list and expected retest outcome.
- **See the storage engine spec**: [SPEC-storage-engine.md](../SPEC-storage-engine.md) for architecture patterns and full rationale.

---

<details>
<summary>📚 Glossary</summary>

| Term | Definition |
|------|-----------|
| **BM25** | Best Match 25; full-text search ranking algorithm used in SurrealDB's FTS index |
| **CRDT op-log** | Conflict-free Replicated Data Type operation log; source of truth for Yar's local-first sync |
| **DISKANN** | Disk-resident approximate nearest-neighbor vector index; GA in SurrealDB 3.1 |
| **FTS** | Full-Text Search; lexical keyword search using an inverted index |
| **GraphRAG** | Graph-enhanced Retrieval-Augmented Generation; combines vector, BM25, and graph traversal |
| **HNSW** | Hierarchical Navigable Small World; in-memory approximate nearest-neighbor vector index |
| **KNN** | K-Nearest Neighbors; the query operation that finds the top-k most similar vectors |
| **RRF** | Reciprocal Rank Fusion; rank aggregation method for merging multiple ranked result lists |
| **RocksDB** | Default SurrealDB storage backend; higher write amplification for SurrealDB's access patterns |
| **SurrealKV** | SurrealDB's newer embedded MVCC storage backend with better performance |
| **SurrealQL** | SurrealDB's SQL-like query language; supports graph, vector, and relational queries in one statement |

</details>

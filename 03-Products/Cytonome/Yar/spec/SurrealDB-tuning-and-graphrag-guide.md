---
status: Draft
date: 2026-06-21
author: "@shahin"
audience: engineers
tags: [surrealdb, performance, graphrag, storage, tuning, flutter, mobile]
version_at_time_of_writing: "3.1.0"
---

# SurrealDB Tuning, Troubleshooting, and GraphRAG Guide for Yar

> **Reading options:** An ADHD-friendly progressive-disclosure rendering is generated from this file. The hand-maintained ADHD twin (`spec/adhd/SurrealDB-tuning-and-graphrag-guide_adhd.md`) was retired 2026-07-16; see `_archive/cleanup_2026-07-16/adhd-twins/`.

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: engineers, stakeholders
> **Tags**: `yar`, `spec`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)

**TL;DR.** SurrealDB 3.1 (May 2026) now includes DISKANN as a GA second vector index alongside HNSW, a major stability pass, and improved in-memory performance. The benchmark last-place finish for SurrealDB was caused by three configuration artifacts (FTS index failure, per-call connection overhead, and unchecked storage backend), none of which reflect the engine's ceiling. Fix those three issues first before any architecture decision.

---

## 1. Purpose and Scope

This guide covers four concerns in one place:

1. **Troubleshooting** the specific failures identified in the Yar benchmark (see `BENCHMARK_DIGEST.md`), plus common pitfalls.
2. **Configuration and optimization** with concrete SurrealQL and startup command examples for both embedded desktop and server modes.
3. **GraphRAG** data model and query patterns that combine vector KNN, BM25 full-text, and graph traversal in a single SurrealQL query, mapped to Yar's personal knowledge graph.
4. **Phone vs desktop profiles** for the Flutter app, covering the mobile embedding constraint and the recommended architecture.

**Scope boundaries.** This guide targets SurrealDB 3.1.x. Claims about version-specific behavior are cited. The Flutter Dart SDK (`surrealdb` v1.1.2, March 2026) connects via WebSocket only; it does not embed SurrealDB in-process. The Rust SDK does support in-process embedding. See Section 5 for the implications for the Flutter app.

---

## 2. Troubleshooting Table

All symptoms below were either directly observed in the Yar benchmark or are well-documented community issues. Each fix is concrete and testable.

| # | Symptom | Likely Cause | Fix |
|---|---------|-------------|-----|
| T1 | Lexical search returns in 200-450 ms; benchmark marks it as `CONTAINS` fallback | FTS index was never created or failed silently at runtime; the query fell back to a linear scan | Define `ANALYZER` and `FULLTEXT ANALYZER` index before running any lexical query; verify with `INFO FOR TABLE`; see Section 3.3 |
| T2 | `task_lookup` latency is 50-400 ms even for small datasets; co-located FalkorDB achieves sub-1 ms for the same workload | Per-call HTTP or WebSocket reconnect; a new socket handshake is opened per query instead of reusing a persistent connection | Use the async WebSocket client with a single `connect()` at startup; reuse across all queries; see Section 3.5 |
| T3 | `build_import` and `task_lookup` are slow; Docker startup shows default backend | Default Docker image uses RocksDB without SurrealKV; RocksDB write amplification is higher for SurrealDB's access patterns | Set `surrealkv://data` as the storage path in Docker or the Rust SDK; see Section 3.1 |
| T4 | Write operations are slower than expected under schemaless mode | SurrealDB in schemaless mode performs type inference on every write | Add `SCHEMAFULL` to every `DEFINE TABLE` statement; see Section 3.2 |
| T5 | Vector index at 10k or 100k returns wrong results or fails entirely; benchmark shows "fell back to Python exact search" | Docker volume from a prior run (e.g., 3k with dimension 128) was not deleted before the 10k run (dimension 384); SurrealDB loaded the stale index | Run `docker volume rm <vol>` or use a fresh named volume per dataset size; always verify with `INFO FOR TABLE` after data import |
| T6 | `DEFINE INDEX ... HNSW DIMENSION 384` fails or is silently ignored | Field type was not declared as `array<float>` or dimension was mismatched between index definition and stored vectors | Declare `DEFINE FIELD embedding ON TABLE memo TYPE array<float>` before defining the index; confirm dimension matches your embedding model |
| T7 | `EXPLAIN` shows `Full Table Scan` for a record ID lookup | The default `id` field has an implicit index, but a lookup on a non-id field (e.g., `WHERE slug = "x"`) has no index | Add `DEFINE INDEX idx_slug ON TABLE memo FIELDS slug` for any field used in WHERE clauses |
| T8 | Hybrid RRF query returns 455 ms p50 | FTS is doing a linear scan (T1) AND vector search may be using brute force instead of an index | Fix T1 first; then confirm HNSW or DISKANN index exists and the `<|k|>` KNN operator (not `<|k, COSINE|>`) is used so the index path fires |
| T9 | Cold open is 50 ms; acceptable for server but unacceptable for embedded | Docker network socket initialization; TCP handshake overhead per session | For desktop, use embedded Rust mode (no socket); for mobile (Flutter), keep a single persistent WebSocket open for the app lifetime |
| T10 | `SELECT * FROM sys::version()` not recorded in benchmark output | Version not stamped; reproducibility impossible | Always run `SELECT * FROM sys::version()` at the start of any benchmark run and record it in output |
| T11 | `SEARCH ANALYZER` syntax error on SurrealDB 3.x | Breaking syntax change: pre-3.0 used `SEARCH ANALYZER`; 3.0+ uses `FULLTEXT ANALYZER` | Use `FULLTEXT ANALYZER <analyzer_name>` in `DEFINE INDEX`; see Section 3.3 |
| T12 | `--allow-all` capability flag causes queries to fail in strict mode | Capabilities not explicitly granted; scripting or network functions blocked by default | Add `--allow-scripting`, `--allow-net`, or `--allow-all` to the `surreal start` command as needed; see Section 3.7 |

---

## 3. Configuration and Optimization

### 3.1 Backend Selection and Startup

**Server mode (Docker, recommended for development and server-side desktop):**

```bash
# SurrealKV backend (preferred for single-node; lower write amplification than RocksDB)
docker run --rm -p 8000:8000 \
  -v yar_data:/data \
  surrealdb/surrealdb:3.1 \
  start \
  --user root --pass secret \
  surrealkv:///data/yar.db

# RocksDB (stable default; use if SurrealKV shows data format issues)
docker run --rm -p 8000:8000 \
  -v yar_data:/data \
  surrealdb/surrealdb:3.1 \
  start \
  --user root --pass secret \
  rocksdb:///data/yar.db

# In-memory (testing and CI only; data lost on restart)
docker run --rm -p 8000:8000 \
  surrealdb/surrealdb:3.1 \
  start --user root --pass secret memory
```

**Embedded mode (Rust SDK, for desktop native app):**

```rust
use surrealdb::engine::local::SurrealKv;
use surrealdb::Surreal;

// SurrealKV embedded -- no separate process, no socket overhead
let db = Surreal::new::<SurrealKv>("./yar_data/db").await?;
db.use_ns("yar").use_db("personal").await?;
```

Source: [SurrealDB Embedding in Rust docs](https://surrealdb.com/docs/surrealdb/embedding/rust); [SurrealKV storage engine blog](https://ori-cohen.medium.com/surrealkv-diving-deep-with-the-new-storage-engine-in-surrealdb-2-0-5c8d276aaaf6).

**Important:** SurrealKV is documented as beta/actively evolving as of 3.1. The file format may change between minor versions. Use RocksDB if you need a format stability guarantee for a production deployment today. Use SurrealKV for Yar desktop development and retest on each SurrealDB upgrade. Source: [SurrealDB storage engines docs](https://surrealdb.com/docs/build/embedding/storage-engines).

### 3.2 Schemafull Table Definitions

Always use `SCHEMAFULL`. Schemaless is SurrealDB's default but performs type inference on every write.

```surrealql
-- Core memo/chunk node in Yar's knowledge graph
DEFINE TABLE memo SCHEMAFULL;
DEFINE FIELD id           ON TABLE memo TYPE record;
DEFINE FIELD content      ON TABLE memo TYPE string;
DEFINE FIELD embedding    ON TABLE memo TYPE array<float>;
DEFINE FIELD created_at   ON TABLE memo TYPE datetime;
DEFINE FIELD updated_at   ON TABLE memo TYPE datetime;
DEFINE FIELD source       ON TABLE memo TYPE string;

-- Concept node
DEFINE TABLE concept SCHEMAFULL;
DEFINE FIELD id           ON TABLE concept TYPE record;
DEFINE FIELD name         ON TABLE concept TYPE string;
DEFINE FIELD embedding    ON TABLE concept TYPE array<float>;

-- Edge table for graph relations
DEFINE TABLE mentions SCHEMAFULL TYPE RELATION IN memo OUT concept;
DEFINE FIELD weight       ON TABLE mentions TYPE float;
DEFINE FIELD created_at   ON TABLE mentions TYPE datetime;
```

### 3.3 Full-Text Analyzer and Index

**Syntax changed at 3.0.** Use `FULLTEXT ANALYZER`, not `SEARCH ANALYZER`. Source: [SurrealDB full-text search docs](https://surrealdb.com/docs/surrealdb/models/full-text-search).

```surrealql
-- Define the analyzer (global, not per-table)
DEFINE ANALYZER yar_analyzer
  TOKENIZERS class, blank, punct
  FILTERS lowercase, ascii, snowball(english);

-- Define the full-text index with BM25
-- BM25(1.2, 0.75) are the standard defaults; tune if needed
DEFINE INDEX idx_memo_content ON TABLE memo
  FIELDS content
  FULLTEXT ANALYZER yar_analyzer
  BM25(1.2, 0.75)
  HIGHLIGHTS;

-- Verify the index was created
INFO FOR TABLE memo;

-- Example FTS query using @N@ match operator with scored results
SELECT
  id,
  content,
  search::score(0)   AS bm25_score,
  search::highlight("<b>", "</b>", 0) AS highlighted
FROM memo
WHERE content @0@ "anxiety sleep"
ORDER BY bm25_score DESC
LIMIT 20;
```

The `@0@` operator number links the WHERE clause to `search::score(0)`. Multiple fields can be searched simultaneously using different numbers (e.g., `@1@` for a second field). Source: [DEFINE INDEX statement docs](https://surrealdb.com/docs/surrealql/statements/define/indexes).

### 3.4 Vector Indexes

**HNSW** (in-memory, fast warm-cache lookups, suits phone and desktop for typical Yar dataset sizes):

```surrealql
-- For 384-dim embeddings (e.g., all-MiniLM-L6-v2, nomic-embed-text)
-- TYPE F32 halves memory vs F64 with negligible accuracy loss for semantic search
DEFINE INDEX idx_memo_vec ON TABLE memo
  FIELDS embedding
  HNSW DIMENSION 384
  DIST COSINE
  TYPE F32
  M 16
  EFC 200;

-- For concept embeddings (same model, same dimension)
DEFINE INDEX idx_concept_vec ON TABLE concept
  FIELDS embedding
  HNSW DIMENSION 384
  DIST COSINE
  TYPE F32
  M 12
  EFC 150;
```

**DISKANN** (GA in SurrealDB 3.1, disk-resident, better for larger-than-memory workloads on desktop):

```surrealql
-- DISKANN accepts F32, F16, I8, U8 only (not F64 or I64)
DEFINE INDEX idx_memo_vec_disk ON TABLE memo
  FIELDS embedding
  DISKANN DIMENSION 384
  DIST COSINE
  TYPE F32;
```

Source: [SurrealDB 3.1 release post](https://surrealdb.com/blog/surrealdb-3-1-stability-diskann-and-a-new-release-process); [vector indexes docs](https://surrealdb.com/docs/learn/data-models/vector-search/vector-indexes).

**KNN query operator syntax:**

```surrealql
-- <|k|>         uses the distance function defined in the index (COSINE here)
-- <|k, effort|> second param is HNSW ef (search effort); higher = more accurate, slower
-- <|k, COSINE|> explicit distance metric bypasses the index (brute force)

LET $qvec = [...]; -- your 384-dim query embedding

SELECT
  id,
  content,
  vector::distance::knn() AS dist
FROM memo
WHERE embedding <|10, 100|> $qvec  -- top 10, ef=100
ORDER BY dist ASC;
```

Using `<|k, COSINE|>` instead of `<|k|>` bypasses the HNSW index entirely and runs brute force. Always use `<|k|>` or `<|k, ef|>` to hit the index. Verify with `EXPLAIN FULL`.

### 3.5 Persistent WebSocket Connection

This is the single highest-impact fix for the benchmark task_lookup latency. Opening a new connection per query adds 40-400 ms overhead.

**Python SDK (for benchmark retest):**

```python
from surrealdb import AsyncSurrealDB

# Connect once at app startup; reuse for all queries
db = AsyncSurrealDB("ws://localhost:8000/rpc")
await db.connect()
await db.sign_in({"user": "root", "pass": "secret"})
await db.use("yar", "personal")

# All subsequent queries reuse the same WebSocket session
result = await db.query("SELECT * FROM memo WHERE id = $id", {"id": "memo:abc"})
```

**Dart/Flutter SDK (surrealdb v1.1.2):**

```dart
import 'package:surrealdb/surrealdb.dart';

// In your app's state/service layer -- one instance for the entire app
final db = SurrealDB('ws://localhost:8000/rpc');

Future<void> initDb() async {
  db.connect();
  await db.wait();
  await db.use('yar', 'personal');
}

// Call initDb() once at app startup; never create a new SurrealDB() per query
```

Source: [surrealdb Dart package](https://pub.dev/packages/surrealdb).

### 3.6 Transactions and Batched Inserts

For bulk imports (embedding store operations, CRDT op-log replay), wrap inserts in transactions. This reduces write-ahead log flushes.

```surrealql
BEGIN TRANSACTION;

CREATE memo:a1 SET
  content = "...",
  embedding = [...],
  created_at = time::now();

CREATE memo:a2 SET
  content = "...",
  embedding = [...],
  created_at = time::now();

-- Up to ~500 records per transaction is a reasonable batch size.
-- Beyond that, test empirically; very large transactions hold locks longer.

COMMIT TRANSACTION;
```

For Python bulk inserts, use a loop with commits every N records rather than one giant transaction.

### 3.7 EXPLAIN-Driven Query Tuning

Always confirm index usage before measuring latency.

```surrealql
-- EXPLAIN shows the query plan without executing
EXPLAIN SELECT id FROM memo WHERE content @0@ "focus";

-- EXPLAIN FULL shows per-iterator timing
EXPLAIN FULL
SELECT id, vector::distance::knn() AS dist
FROM memo
WHERE embedding <|10|> $qvec;
```

A result showing `"operation": "Knn"` and `"index": "idx_memo_vec"` confirms the HNSW index was used. A result showing `"operation": "Table Iterator"` means a full scan ran; add or fix the relevant index.

### 3.8 Capabilities and Resource Flags

For a server deployment that runs LLM-adjacent functions:

```bash
surreal start \
  --user root --pass $SURREALDB_PASS \
  --allow-scripting \
  --allow-net \
  --bind 127.0.0.1:8000 \
  surrealkv:///data/yar.db
```

Avoid `--allow-all` in production. Explicitly grant only what Yar uses.

---

## 4. GraphRAG on SurrealDB

### 4.1 Philosophy: Index as a Derived View

Yar's **CRDT op-log is the source of truth**. The SurrealDB store is a derived, queryable index rebuilt from the op-log. This means:

- Every record in SurrealDB can be deleted and reconstructed from the op-log at any time.
- SurrealDB indexes (HNSW, DISKANN, FTS) can be dropped and rebuilt with `REBUILD INDEX`.
- Schema migrations are safe: drop the index, migrate records, rebuild the index.
- This decoupling is what makes the mobile architecture viable: the phone holds the op-log and the derived index; the desktop can sync the op-log and independently maintain its own larger index.

### 4.2 Data Model

```
memo (node)
  id: record
  content: string        -- raw text
  embedding: array<f32>  -- semantic embedding (384-dim)
  source: string         -- app context where memo was captured
  created_at: datetime

concept (node)
  id: record
  name: string
  embedding: array<f32>  -- concept-level embedding

mentions (edge)          -- RELATE memo -> concept
  in: record<memo>
  out: record<concept>
  weight: float          -- salience score from NER/extraction

related_to (edge)        -- concept-to-concept
  in: record<concept>
  out: record<concept>
  type: string           -- "causal", "hierarchical", "associated"
```

Graph edges are created with `RELATE`:

```surrealql
RELATE memo:a1 -> mentions -> concept:focus SET weight = 0.92;
RELATE concept:focus -> related_to -> concept:attention SET type = "associated";
```

### 4.3 Query Patterns

**Vector KNN (semantic similarity):**

```surrealql
LET $qvec = [...]; -- query embedding

SELECT id, content, vector::distance::knn() AS dist
FROM memo
WHERE embedding <|10, 100|> $qvec
ORDER BY dist ASC;
```

**BM25 Full-Text:**

```surrealql
SELECT id, content, search::score(0) AS score
FROM memo
WHERE content @0@ "morning routine focus"
ORDER BY score DESC
LIMIT 10;
```

**Graph Traversal (2-hop: memo -> concept -> related concept -> memo):**

```surrealql
-- Starting from a concept, find memos two hops away via related concepts
SELECT
  <-mentions<-memo.id AS memo_id,
  <-mentions<-memo.content AS memo_content
FROM concept:focus
  ->related_to->concept
  <-mentions<-memo;
```

**Hybrid Retrieval (vector + BM25 + graph, fused with RRF):**

```surrealql
-- Step 1: vector search
LET $qvec = [...];
LET $vs = (
  SELECT id FROM memo
  WHERE embedding <|20, 100|> $qvec
);

-- Step 2: BM25 full-text search
LET $ft = (
  SELECT id, search::score(0) AS score FROM memo
  WHERE content @0@ "focus morning"
  ORDER BY score DESC
  LIMIT 20
);

-- Step 3: graph expansion (find memos connected to top concepts)
LET $concepts = (
  SELECT ->mentions->concept AS cs FROM $vs LIMIT 5
);
LET $graph = (
  SELECT
    <-mentions<-memo.id AS id
  FROM $concepts[*].cs
  WHERE <-mentions<-memo.id NOT IN $vs[*].id
  LIMIT 10
);

-- Step 4: fuse all three candidate sets with RRF (k=60)
search::rrf([$vs, $ft, $graph], 10, 60);
```

The `search::rrf()` function is built into SurrealQL. It takes an array of ranked lists, a top-k count, and a smoothing constant k. This single query runs entirely within SurrealDB, with no network hops between retrieval steps. Source: [SurrealDB vector search docs](https://surrealdb.com/docs/surrealdb/models/vector#hybrid-search-functions).

### 4.4 Index Rebuild After Schema Migration

```surrealql
-- Drop and rebuild a single index (e.g., after dimension change)
REMOVE INDEX idx_memo_vec ON TABLE memo;
DEFINE INDEX idx_memo_vec ON TABLE memo
  FIELDS embedding
  HNSW DIMENSION 384 DIST COSINE TYPE F32 M 16 EFC 200;
REBUILD INDEX idx_memo_vec ON TABLE memo;

-- Check progress
INFO FOR TABLE memo;
```

SurrealDB 3.1 adds a `DEFER` keyword for background index building (experimental as of 3.1). Do not use it in production yet.

---

## 5. Phone vs Desktop Config Profiles

### 5.1 Mobile Embedding Constraint (Critical for Flutter)

The `surrealdb` Dart package (v1.1.2, March 2026) is a **WebSocket client only**. It does not embed SurrealDB in-process on iOS or Android. Source: [pub.dev/packages/surrealdb](https://pub.dev/packages/surrealdb).

True in-process embedding on mobile is possible via `flutter_rust_bridge` with the SurrealDB Rust crate, but this requires:

- Writing a Rust FFI shim.
- Compiling for `aarch64-apple-ios`, `armv7-linux-androideabi`, and `aarch64-linux-android`.
- Shipping a significantly larger binary.
- Managing async Rust lifetimes across the Dart/Rust boundary.

This is not trivial and no official SurrealDB Flutter embedding SDK exists as of 2026-06-21. The discussion thread requesting it dates from the SurrealDB org (unverified current status; confirm against [github.com/orgs/surrealdb/discussions/109](https://github.com/orgs/surrealdb/discussions/109)).

**Recommended architecture for Yar mobile:**

Run SurrealDB as a local background service on-device (similar to how SQLite apps bundle a native binary). The Dart Flutter app connects to it via localhost WebSocket (`ws://127.0.0.1:PORT/rpc`). This keeps the full SurrealQL and index stack available without a custom FFI layer, at the cost of a slightly longer first-launch startup.

### 5.2 Comparison Table

| Configuration | Phone (iOS/Android) | Desktop (macOS/Linux/Windows) |
|---|---|---|
| **Backend** | SurrealKV (via embedded server binary) or in-memory for light use | SurrealKV (embedded Rust) or DISKANN-backed for large corpora |
| **Mode** | Local server binary on-device (localhost WebSocket) OR flutter_rust_bridge FFI (advanced) | Embedded Rust SDK (no socket, lowest latency) |
| **Vector index** | HNSW, F32, DIMENSION 384, M 12, EFC 100 (lower memory) | HNSW for up to ~50k memos; DISKANN for larger corpora; F32 throughout |
| **Full-text index** | BM25(1.2, 0.75), snowball(english), same analyzer as desktop | BM25(1.2, 0.75), snowball(english) |
| **Cache and memory** | Limit to 256-512 MB; use `--memory-limit` flag if available (unverified, confirm against current docs) | No hard limit; let OS manage; 1-4 GB typical |
| **Connection** | Single persistent WebSocket from Flutter app to local server; never reconnect per query | In-process Rust SDK; no socket |
| **Schema** | Identical `SCHEMAFULL` schema as desktop | Identical schema |
| **Index parameters** | Lower M and EFC to reduce memory: `M 12, EFC 100` | Higher M and EFC for better recall: `M 16, EFC 200` |
| **Transaction batch size** | 50-100 records per transaction | 200-500 records per transaction |

### 5.3 Recommendation

Share one SurrealQL schema file deployed to both environments. The `DEFINE TABLE`, `DEFINE FIELD`, `DEFINE ANALYZER`, and `DEFINE INDEX` statements are identical except for HNSW parameter values. Use a schema templating step (or conditional SurrealQL variables) to swap `M` and `EFC` values by platform at init time. This approach ensures the query layer, GraphRAG patterns, and hybrid retrieval queries are identical across phone and desktop without any branching logic in the application code.

---

## 6. Verification Checklist

Run this after every schema setup or retest before a benchmark.

```surrealql
-- 1. Confirm SurrealDB version
SELECT * FROM sys::version();
-- Expected: { version: "3.1.0", ... } or later

-- 2. Confirm indexes exist on memo table
INFO FOR TABLE memo;
-- Expected output includes:
--   indexes: {
--     idx_memo_content: "DEFINE INDEX idx_memo_content ON memo FIELDS content FULLTEXT ANALYZER yar_analyzer BM25(1.2, 0.75) HIGHLIGHTS",
--     idx_memo_vec:     "DEFINE INDEX idx_memo_vec ON memo FIELDS embedding HNSW DIMENSION 384 DIST COSINE TYPE F32 M 16 EFC 200"
--   }

-- 3. Confirm vector index is being used (not brute force)
EXPLAIN FULL
SELECT id, vector::distance::knn() AS dist
FROM memo
WHERE embedding <|5|> [0.1, 0.2, ...]; -- abbreviated example
-- Expected: operation = "Knn", index = "idx_memo_vec"

-- 4. Confirm FTS index is being used (not CONTAINS scan)
EXPLAIN FULL
SELECT id FROM memo WHERE content @0@ "focus";
-- Expected: operation = "Union" or "Matches", not "Table Iterator"

-- 5. Confirm namespace and database context
INFO FOR DB;

-- 6. Confirm record count after bulk import (sanity check)
SELECT count() FROM memo GROUP ALL;
```

**Before any benchmark run:** delete Docker volumes between dataset sizes (`docker volume rm yar_data`), record the version output, and run `INFO FOR TABLE memo` to confirm all indexes are present. Do not accept a run where `INFO FOR TABLE` is missing an expected index.

---

## 7. Sources

- [SurrealDB 3.1 release post (DISKANN GA, stability)](https://surrealdb.com/blog/surrealdb-3-1-stability-diskann-and-a-new-release-process)
- [SurrealDB official releases page](https://surrealdb.com/releases)
- [SurrealDB vector search model docs (HNSW parameters, KNN syntax, hybrid search::rrf)](https://surrealdb.com/docs/surrealdb/models/vector)
- [DEFINE INDEX statement docs (HNSW, DISKANN, FTS syntax)](https://surrealdb.com/docs/surrealql/statements/define/indexes)
- [SurrealDB full-text search docs (DEFINE ANALYZER, BM25, search::score)](https://surrealdb.com/docs/surrealdb/models/full-text-search)
- [SurrealDB embedding in Rust docs](https://surrealdb.com/docs/surrealdb/embedding/rust)
- [SurrealKV GitHub repo and description](https://github.com/surrealdb/surrealkv)
- [SurrealKV deep-dive article (SurrealDB 2.0 context; architecture is unchanged in 3.x)](https://ori-cohen.medium.com/surrealkv-diving-deep-with-the-new-storage-engine-in-surrealdb-2-0-5c8d276aaaf6)
- [SurrealDB storage engines docs (SurrealKV beta status)](https://surrealdb.com/docs/build/embedding/storage-engines)
- [surrealdb Dart package (v1.1.2, March 2026)](https://pub.dev/packages/surrealdb)
- [SurrealDB Flutter discussion thread](https://github.com/orgs/surrealdb/discussions/109)
- [SurrealDB GraphRAG blog post](https://surrealdb.com/blog/graph-rag-does-not-need-a-graph-database-it-needs-a-database-that-does-everything)
- [Knowledge Graph RAG query patterns post](https://surrealdb.com/blog/knowledge-graph-rag-two-query-patterns-for-smarter-ai-agents)
- [Hybrid search inside SurrealDB (RRF example)](https://medium.com/@atwmarshall/hybrid-search-inside-surrealdb-one-query-vector-keyword-rrf-4ea41ba7a793)
- [SurrealDB deployment and storage layer fundamentals](https://surrealdb.com/learn/fundamentals/performance/deployment-storage)

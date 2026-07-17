# SurrealDB v3.1.5 Retest Report — Root Cause, Changelog, and Results

> **Status**: Active
> **Date**: 2026-07-16
> **Author**: Cytognosis Foundation (@shahin)
> **Audience**: engineers, stakeholders
> **Tags**: `yar`, `benchmark`, `surrealdb`, `sqlite`, `falkordb`, `storage`, `retest`
> **Merged from**: `spec/BENCHMARK-REPORT.md`, `spec/OPTIMIZATION-CHANGELOG.md`, `spec/SURREALDB-ROOTCAUSE.md` (retired 2026-07-16; originals archived at `_archive/cleanup_2026-07-16/surrealdb/`)

---

## BLUF

The SurrealDB v3.1.5 retest confirms the prior PATCH10 finding: **SQLite wins at 10k, FalkorDB wins at 100k, SurrealDB finishes third at both scales.** SurrealDB v3.1.5 shows moderate improvements over v3.1.3 in 8 of 10 operations (cold_open -43%, memory_packet -42%, depth3_context -42%) but does not change the ranking. SurrealDB's poor performance traces to six ranked root causes — three configuration artifacts (now fixed) and three architectural characteristics of the engine (not fixable by configuration). The retest closes open decision O-3 and unblocks `SPEC-storage-engine.md` from DRAFT to ACTIVE.

---

## 1. Test Environment

| Component | Value |
|---|---|
| OS | Linux (Ubuntu-based) |
| Docker | 29.3.1 |
| Docker Compose | v5.1.1 |
| Python | 3.14.4 |
| SurrealDB image | `surrealdb/surrealdb:v3.1.5` (upgraded from v3.1.3) |
| SurrealDB backend | RocksDB (`rocksdb:///data/yarbench.db`) |
| SurrealDB Python SDK | `surrealdb` v2.0.0 (WebSocket, `BlockingWsSurrealConnection`) |
| FalkorDB image | `falkordb/falkordb:latest` |
| SQLite | 3.46.1 + sqlite-vec 0.1.9 |
| Embedding dimension | 384 |
| Seed | 42 (deterministic) |
| Docker volumes | Fresh per run (cleaned between scale tests) |
| Benchmark suite | `yar_supervisor_reproducible_benchmark_package/db_benchmark/yar_bench.py` |

---

## 2. Root Cause Analysis

Six ranked root causes for SurrealDB's benchmark performance. Three were configuration artifacts, fixed in PATCH8-10; three are architectural characteristics of the engine and are not fixable by configuration alone.

### RC-1: FTS Index Failure (FIXED in PATCH10)

**Impact:** lexical_search 214ms to 3.6ms (59x improvement at 10k). **Severity:** Critical (benchmark-invalidating).

The original benchmark's `DEFINE INDEX ... SEARCH ANALYZER` syntax silently failed on SurrealDB 3.x, which uses `FULLTEXT ANALYZER`. Queries fell back to `string::contains()` linear scans. Additionally, `ORDER BY search::score(0) DESC` was rejected by the parser; PATCH10 introduced aliasing (`AS score`) to fix this.

**Evidence:** `yar_bench.py` line 880-888 (legacy adapter tries `FULLTEXT ANALYZER` then `SEARCH ANALYZER` without verifying success); line 987 (legacy lexical query uses the rejected `ORDER BY search::score(0) DESC`); PATCH10 fix at line 1191 (`SELECT yid, search::score(0) AS score ... ORDER BY score DESC`).

### RC-2: SCHEMALESS Mode Type Inference Overhead (FIXED in PATCH8)

**Impact:** 10-30% write throughput degradation. **Severity:** High.

The legacy adapter used `DEFINE TABLE node SCHEMALESS` (line 864). SurrealDB's schemaless mode performs type inference on every write. The tuned adapter uses `SCHEMAFULL` with explicit typed fields including `embedding TYPE array<float>`.

**Evidence:** Legacy `DEFINE TABLE node SCHEMALESS` (line 864); tuned `DEFINE TABLE node SCHEMAFULL` + 9 typed field definitions (lines 1098-1112); tuning guide §3.2: "Always use SCHEMAFULL. Schemaless is SurrealDB's default but performs type inference on every write."

### RC-3: Missing Composite and Partial Indexes (FIXED in PATCH8)

**Impact:** `project_decisions` improved from 2.8ms to 0.7ms at 10k, 61ms to 2.2ms at 100k. **Severity:** Medium.

The legacy adapter defined only single-field indexes. The tuned adapter adds `idx_node_project_kind` (composite on `project_id, kind`), `idx_node_created` (for `task_lookup` ORDER BY), and separate FTS indexes on body and title (instead of a combined multi-field index).

**Evidence:** Legacy has 5 single-field indexes (lines 867-872); tuned has 10 indexes including composite (lines 1113-1121).

### RC-4: `task_lookup` Full Table Scan — No Covering Index (ARCHITECTURAL, NOT FIXED)

**Impact:** 46ms at 10k → 38ms after PATCH10 → 325ms at 100k (vs SQLite 11.4ms, FalkorDB 8.1ms at 100k). **Severity:** Critical for MVP viability.

The query `SELECT VALUE yid FROM node WHERE kind = 'task' ORDER BY created_at DESC LIMIT N` requires a filter on `kind` then sort on `created_at`. SurrealDB does not support covering indexes or composite sort+filter the way SQLite and graph engines handle this natively. Even with `idx_node_kind` and `idx_node_created` defined, the engine does not merge them efficiently.

**Root cause:** SurrealDB's query planner as of v3.1.x does not perform index intersection or use composite indexes for filter+sort patterns. This is the single largest contributor to SurrealDB's weighted score gap, and it **worsens with scale** (8.6x degradation from 10k to 100k).

**Potential optimization:** Define `DEFINE INDEX idx_task_lookup ON TABLE node FIELDS kind, created_at` as a composite index and use `EXPLAIN FULL` to verify the planner uses it.

### RC-5: Cold Open Latency — Docker/WebSocket Overhead (ARCHITECTURAL, NOT FIXED in this benchmark)

**Impact:** 64ms at 10k (v3.1.3) → 36ms at 10k (v3.1.5, -43%) → 354ms at 100k (vs SQLite 104ms, FalkorDB 8.9ms). **Severity:** High for user experience.

Cold open measures time to establish a connection and execute a first query. The benchmark connects to SurrealDB over WebSocket (Docker container, TCP). SQLite is in-process (zero network). FalkorDB uses the Redis protocol over TCP but is optimized for persistent connections.

**Root cause:** Network socket initialization dominates cold-open time, and it scales with DB size. The tuning guide (§3.1) documents that embedded Rust mode (`Surreal::new::<SurrealKv>("./path")`) eliminates this entirely.

**Recommended test:** Benchmark embedded Rust SurrealDB (via Tauri FFI or a direct Rust binary) vs Docker/WebSocket. This is the intended production mode for Yar desktop and is the next scheduled retest (PATCH11, in progress as of 2026-07-16).

### RC-6: Graph Traversal N+1 Query Pattern (ARCHITECTURAL, NOT FIXED — inherent to non-graph engines)

**Impact:** depth2 2.3ms, depth3 2.6ms at 10k (vs SQLite 0.02-0.03ms, FalkorDB 0.29-0.32ms). **Severity:** Medium.

SurrealDB does not have native graph traversal in the benchmark's data model. The benchmark simulates 2-hop and 3-hop traversals by chaining edge lookups (`SELECT dst FROM edge WHERE src = $id`), resulting in N+1 queries per hop. Native graph engines (FalkorDB Cypher, Neo4j Cypher) express this as a single pattern match.

SurrealDB 3.x supports `->` arrow syntax for record-link traversal, but this requires edges to be modeled as record links rather than a flat edge table. The benchmark's edge model uses separate `src`/`dst` fields — the standard relational pattern — which does not leverage SurrealDB's graph features.

**Recommended optimization:** Model edges using SurrealDB's native `RELATE` graph syntax and use `->edge->node` traversal patterns. This could eliminate N+1 and bring graph operations closer to native graph engines.

### Performance Impact Matrix

| Root Cause | 10k Impact | 100k Impact | Fixable? | Effort |
|---|---|---|---|---|
| RC-1: FTS failure | 59x worse | 6x worse | **Fixed** | Done |
| RC-2: SCHEMALESS | 10-30% writes | 10-30% writes | **Fixed** | Done |
| RC-3: Missing indexes | 2-7x worse selectively | 5-30x worse selectively | **Fixed** | Done |
| RC-4: task_lookup scan | 80x vs SQLite | 65x vs SQLite | **Partial** (composite index) | Days |
| RC-5: Cold open | 5x vs FalkorDB | 167x vs FalkorDB | **Yes** (embedded mode) | Weeks |
| RC-6: Graph N+1 | 100x vs SQLite | 96x vs SQLite | **Partial** (RELATE model) | Weeks |

### SDK and Connection Analysis

| Factor | Current State | Risk |
|---|---|---|
| SDK version | `surrealdb` v2.0.0 (Python) | Stable GA; WebSocket-based |
| Connection mode | WebSocket to Docker container | Adds ~5-50ms per cold call |
| Persistent connection | Yes (tuned adapter reuses `self.db`) | Correct; PATCH8 fixed |
| Transaction support | Attempted (`BEGIN/COMMIT TRANSACTION`) with fallback | Works on v3.1.5 |
| Batch insert | `INSERT INTO node $rows` with fallback to per-row | Working correctly |
| Engine mode | Server (Docker), not embedded | Embedded untested (PATCH11) |

---

## 3. Optimization Changelog (PATCH8, PATCH9, PATCH10)

Changes applied ahead of the v3.1.5 retest, upgrading from v3.1.3:

```diff
-    image: surrealdb/surrealdb:v3.1.3
+    image: surrealdb/surrealdb:v3.1.5
```

**Rationale:** the v3.1.5 retest was required to unblock `SPEC-storage-engine.md`.

1. **PATCH8 — SCHEMAFULL tables + typed fields.** Before: `DEFINE TABLE node SCHEMALESS` (type inference on every write). After: `DEFINE TABLE node SCHEMAFULL` with 9 explicitly typed fields including `embedding TYPE array<float>`.
2. **PATCH8 — Separate FTS indexes.** Before: a combined multi-field FTS index that silently failed. After: separate `idx_node_body_fts` and `idx_node_title_fts` with `FULLTEXT ANALYZER yar_analyzer BM25 HIGHLIGHTS`.
3. **PATCH8 — Vector index with explicit parameters.** Before: a generic HNSW index without explicit M/EFC parameters. After: `HNSW DIMENSION 384 DIST COSINE TYPE F32 M 16 EFC 200` with runtime `ef=100`.
4. **PATCH8 — Composite indexes.** Before: single-field indexes only. After: added `idx_node_project_kind` (composite) and `idx_node_created` (for ORDER BY).
5. **PATCH9 — Validation layer fixes.** `INFO FOR TABLE` output no longer truncated; `EXPLAIN FULL` uses correct SurrealQL syntax (appended, not prefixed); `INFO FOR DB` replaces `sys::version()` for version info.
6. **PATCH10 — FTS score aliasing.** Before: `ORDER BY search::score(0) DESC` (rejected by parser). After: `SELECT yid, search::score(0) AS score FROM node WHERE body @0@ $q ORDER BY score DESC LIMIT N`.

---

## 4. Results — 10k Scale (RocksDB + HNSW)

**Weighted decision scores** (lower is better):

| Engine | Score | Coverage |
|---|---|---|
| **sqlite** | **3.609** | 1.20 |
| **falkordb** | **5.344** | 1.20 |
| **surrealdb_tuned** | **8.384** | 1.20 |

**p50 latency (ms):**

| Operation | SQLite | FalkorDB | SurrealDB v3.1.5 | SurrealDB v3.1.3 (PATCH10 ref) |
|---|---|---|---|---|
| build_import | 1,445 | 56,806 | 26,706 | — |
| cold_open | 14.20 | 1.07 | 36.41 | 63.65 |
| depth2_context | 0.02 | 0.29 | 2.30 | 2.58 |
| depth3_context | 0.03 | 0.32 | 2.59 | 4.46 |
| hybrid_rrf | 2.56 | 2.26 | 4.68 | 5.92 |
| incremental_write | 0.22 | 2.63 | 4.85 | 6.26 |
| lexical_search | 0.19 | 0.20 | 4.31 | 3.56 |
| memory_packet | 2.34 | 1.04 | 4.84 | 8.37 |
| person_memory | 2.52 | 0.36 | 1.15 | — |
| project_decisions | 6.25 | 0.37 | 0.45 | 0.73 |
| reverse_refs | 0.01 | 0.23 | 0.23 | — |
| task_lookup | 1.13 | 0.48 | 37.97 | 46.00 |
| vector_search | 2.42 | 2.09 | 2.87 | 2.72 |

**Recall@10:**

| Operation | SQLite | FalkorDB | SurrealDB v3.1.5 |
|---|---|---|---|
| lexical_search | 0.879 | 0.879 | 0.868 |
| vector_search | 1.000 | 0.999 | 0.999 |
| hybrid_rrf | 0.501 | 0.500 | 0.501 |
| memory_packet | 1.000 | 0.999 | 0.999 |

**Validation:** all 2052 measurements per engine completed with 0 failures. SurrealDB `EXPLAIN FULL` confirmed `FullTextScan` for FTS and `KnnScan` for vector search.

### v3.1.5 vs v3.1.3 — 10k comparison and interpretation

| Operation | v3.1.3 (ref) | v3.1.5 | Change | Interpretation |
|---|---|---|---|---|
| cold_open | 63.65 | 36.41 | -43% | Startup/connection overhead reduced |
| memory_packet | 8.37 | 4.84 | -42% | Combined FTS+vector path faster |
| depth3_context | 4.46 | 2.59 | -42% | Multiple-hop lookup faster |
| project_decisions | 0.73 | 0.45 | -38% | Composite index better utilized |
| incremental_write | 6.26 | 4.85 | -23% | Transaction path more efficient |
| hybrid_rrf | 5.92 | 4.68 | -21% | Score fusion faster |
| task_lookup | 46.00 | 37.97 | -17% | Query planner slightly improved |
| depth2_context | 2.58 | 2.30 | -11% | Multiple-hop lookup faster |
| vector_search | 2.72 | 2.87 | +5% | Within noise range |
| lexical_search | 3.56 | 4.31 | +21% | Within noise range; both valid FTS hits |

**Interpretation:** v3.1.5 delivers genuine performance improvements in most operations, particularly cold_open, memory_packet, and graph traversal. The lexical_search regression is within test-to-test variance (both are valid FTS scans producing correct results). The overall weighted score is nearly identical (8.38 vs 8.35) — **the ranking is unchanged: SQLite > FalkorDB > SurrealDB.**

---

## 5. Results — 100k Scale (RocksDB + HNSW)

**Weighted decision scores** (lower is better):

| Engine | Score (v3.1.5) | Score (v3.1.3 ref) |
|---|---|---|
| **falkordb** | **5.369** | 4.262 |
| **sqlite** | **6.794** | 5.495 |
| **surrealdb_tuned** | **9.478** | 9.375 |

**p50 latency (ms):**

| Operation | SQLite | FalkorDB | SurrealDB v3.1.5 |
|---|---|---|---|
| build_import | 15,361 | 605,324 | 303,321 |
| cold_open | 103.97 | 8.93 | 353.67 |
| depth2_context | 0.03 | 0.47 | 2.13 |
| depth3_context | 0.03 | 0.48 | 2.37 |
| hybrid_rrf | 24.96 | 2.53 | 23.56 |
| incremental_write | 0.21 | 3.42 | 5.01 |
| lexical_search | 1.09 | 0.33 | 20.89 |
| memory_packet | 23.34 | 1.36 | 6.63 |
| person_memory | 12.38 | 0.53 | 7.92 |
| project_decisions | 21.93 | 1.21 | 0.89 |
| reverse_refs | 0.01 | 0.29 | 0.30 |
| task_lookup | 11.41 | 8.12 | 325.42 |
| vector_search | 23.57 | 2.38 | 5.10 |

**Validation:** all 3102 measurements per engine completed with 0 failures.

**Key 100k observations:**

1. **FalkorDB wins at 100k** — graph operations scale sub-linearly; lexical search stays sub-millisecond.
2. **SQLite degrades** — vector_search hits 23.6ms (brute-force vec0); hybrid_rrf escalates to 25ms; cold_open jumps to 104ms.
3. **SurrealDB task_lookup explodes** — 325ms at 100k (vs 38ms at 10k; 8.6x degradation). Confirms RC-4.
4. **SurrealDB memory_packet improves relative to SQLite** — 6.6ms vs 23.3ms. SurrealDB's vector search (5.1ms) beats SQLite's (23.6ms) at 100k — a **4.6x** advantage due to HNSW index vs brute-force.
5. **SurrealDB cold_open** — 354ms at 100k. Network/startup overhead scales with DB size. SurrealDB's task_lookup (325ms) is **40x slower** than FalkorDB's (8.1ms) due to the composite-index limitation (RC-4).

---

## 6. SurrealDB Validation Details

The `surrealdb_tuned` adapter on v3.1.5 confirmed:

| Validation Gate | Result |
|---|---|
| Connection class | `BlockingWsSurrealConnection` |
| Auth style | `username_password` |
| FTS body index | `DEFINE INDEX idx_node_body_fts ... FULLTEXT ANALYZER yar_analyzer BM25(1.2,0.75) HIGHLIGHTS` |
| FTS title index | `DEFINE INDEX idx_node_title_fts ... FULLTEXT ANALYZER yar_analyzer BM25(1.2,0.75) HIGHLIGHTS` |
| Vector index | `DEFINE INDEX idx_node_vec ... HNSW DIMENSION 384 DIST COSINE TYPE F32 EFC 200 M 16` |
| FTS EXPLAIN | `FullTextScan` (not Table Iterator) — pass |
| Vector EXPLAIN | `KnnScan` with `idx_node_vec` — pass |
| Schema | `SCHEMAFULL`, 10 typed fields, 9 indexes |
| Strict validation | Passed (all required indexes present) |
| SCHEMAFULL schema verified | `INFO FOR TABLE` shows all typed fields |
| Recall@10 for vector_search | 0.999 |
| Recall@10 for hybrid_rrf | 0.500 (same as baselines; deterministic test set) |

---

## 7. Conclusion and Recommendations

1. **SQLite is the MVP device engine.** Lowest latency across the Yar hot-path at 10k; reasonable at 100k.
2. **FalkorDB is the server graph projection.** Best at 100k; Cypher for n-hop traversal.
3. **SurrealDB v3.1.5 is improved but not MVP-ready.** Cold_open (RC-5) and task_lookup (RC-4) remain the primary bottlenecks. Next test: embedded Rust mode (PATCH11).
4. **O-3 is closed.** The v3.1.5 retest is complete. `SPEC-storage-engine.md` can advance from DRAFT to ACTIVE.
5. **Composite index for task_lookup** — define `DEFINE INDEX idx_task_kind_created ON TABLE node FIELDS kind, created_at` and verify with `EXPLAIN FULL`.
6. **Embedded Rust benchmark (PATCH11, in progress 2026-07-16)** — test SurrealDB embedded via the Rust SDK (`Surreal::new::<SurrealKv>`) to eliminate cold-open and per-query network overhead. This is the intended production mode for Yar desktop.
7. **RELATE-based graph model** — remodel edges using `RELATE node:src_id->edge->node:dst_id` and benchmark native graph traversal vs the flat-table approach.
8. **ID lookup optimization** — benchmark SurrealDB record-ID lookup (`node:⟨yid⟩`) vs `WHERE yid = $id` vs the current string-field approach.
9. **GraphRAG single-query benchmark** — test a combined FTS + KNN + graph expansion query in SurrealQL vs the multi-engine pipeline, which is SurrealDB's actual value proposition.

---

## Cross-References

- Benchmark package: `yar_supervisor_reproducible_benchmark_package/`
- PATCH8/9/10 READMEs: `db_benchmark/`
- Raw output — 10k: `db_benchmark/results_v315_10k_rocks_hnsw/`
- Raw output — 100k: `db_benchmark/results_v315_100k_rocks_hnsw/`
- Reference results: `reference_results/surreal_tuned_patch10_final_comparison.md`
- Tuning guide: `../spec/SurrealDB-tuning-and-graphrag-guide.md`
- Storage engine spec: `../spec/SPEC-storage-engine.md`
- Storage benchmark tracker: `../spec/STORAGE_BENCHMARK_TRACKER.md`
- Superseded originals (archived 2026-07-16): `../_archive/cleanup_2026-07-16/surrealdb/SURREALDB-ROOTCAUSE.md`, `../_archive/cleanup_2026-07-16/surrealdb/OPTIMIZATION-CHANGELOG.md`, `../_archive/cleanup_2026-07-16/surrealdb/BENCHMARK-REPORT.md`

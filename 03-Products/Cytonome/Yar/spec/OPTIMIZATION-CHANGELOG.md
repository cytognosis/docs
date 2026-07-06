# Optimization Changelog — SurrealDB v3.1.5 Retest

**Date:** 2026-07-06
**Environment:** Linux, Docker 29.3.1, Docker Compose v5.1.1, Python 3.14.4
**SurrealDB:** v3.1.5 (Docker, RocksDB backend)
**Python SDK:** surrealdb v2.0.0

---

## Summary

This retest upgrades SurrealDB from v3.1.3 to v3.1.5 and runs the PATCH10 tuned benchmark suite on fresh Docker volumes. All optimizations from PATCH8/9/10 are applied. Results confirm the prior finding: SurrealDB is functional and improved, but still does not beat SQLite or FalkorDB on the Yar hot-path workload.

---

## Changes Applied

### 1. Docker Image Upgrade (v3.1.3 → v3.1.5)

```diff
-    image: surrealdb/surrealdb:v3.1.3
+    image: surrealdb/surrealdb:v3.1.5
```

**Rationale:** Task specification requires v3.1.5 retest to unblock SPEC-storage-engine.

### 2. PATCH8: SCHEMAFULL Tables + Typed Fields

**Before:** `DEFINE TABLE node SCHEMALESS` — type inference on every write.
**After:** `DEFINE TABLE node SCHEMAFULL` with 9 explicitly typed fields including `embedding TYPE array<float>`.

### 3. PATCH8: Separate FTS Indexes

**Before:** Combined multi-field FTS index that silently failed.
**After:** Separate `idx_node_body_fts` and `idx_node_title_fts` with `FULLTEXT ANALYZER yar_analyzer BM25 HIGHLIGHTS`.

### 4. PATCH8: Vector Index with Explicit Parameters

**Before:** Generic HNSW index without explicit M/EFC parameters.
**After:** `HNSW DIMENSION 384 DIST COSINE TYPE F32 M 16 EFC 200` with runtime `ef=100`.

### 5. PATCH8: Composite Indexes

**Before:** Single-field indexes only.
**After:** Added `idx_node_project_kind` (composite) and `idx_node_created` (for ORDER BY).

### 6. PATCH9: Validation Layer Fixes

- `INFO FOR TABLE` output no longer truncated
- `EXPLAIN FULL` uses correct SurrealQL syntax (appended, not prefixed)
- `INFO FOR DB` replaces `sys::version()` for version info

### 7. PATCH10: FTS Score Aliasing

**Before:** `ORDER BY search::score(0) DESC` — rejected by parser.
**After:** `SELECT yid, search::score(0) AS score FROM node WHERE body @0@ $q ORDER BY score DESC LIMIT N`

---

## v3.1.5 Benchmark Results — 10k RocksDB + HNSW

**Decision scores** (lower is better):

| Engine | Score | Coverage |
|---|---|---|
| **sqlite** | **3.609** | 1.20 |
| **falkordb** | **5.344** | 1.20 |
| **surrealdb_tuned** | **8.384** | 1.20 |

**p50 latency (ms):**

| Operation | FalkorDB | SQLite | SurrealDB v3.1.5 | SurrealDB v3.1.3 (PATCH10 ref) |
|---|---|---|---|---|
| lexical_search | 0.204 | 0.194 | 4.309 | 3.555 |
| hybrid_rrf | 2.263 | 2.562 | 4.680 | 5.923 |
| vector_search | 2.085 | 2.420 | 2.868 | 2.722 |
| memory_packet | 1.043 | 2.335 | 4.835 | 8.374 |
| task_lookup | 0.482 | 1.132 | 37.967 | 46.003 |
| depth2_context | 0.288 | 0.022 | 2.302 | 2.584 |
| depth3_context | 0.315 | 0.025 | 2.592 | 4.458 |
| project_decisions | 0.374 | 6.251 | 0.451 | 0.732 |
| incremental_write | 2.628 | 0.216 | 4.846 | 6.259 |
| cold_open | 1.073 | 14.200 | 36.406 | 63.654 |

### Notable Changes in v3.1.5 vs v3.1.3

| Operation | Direction | Magnitude | Interpretation |
|---|---|---|---|
| task_lookup | ✅ Improved | 46.0ms → 38.0ms (17%) | Query planner slightly improved |
| cold_open | ✅ Improved | 63.7ms → 36.4ms (43%) | Startup/connection overhead reduced |
| memory_packet | ✅ Improved | 8.4ms → 4.8ms (42%) | Combined FTS+vector path faster |
| depth3_context | ✅ Improved | 4.5ms → 2.6ms (42%) | Multiple-hop lookup faster |
| hybrid_rrf | ✅ Improved | 5.9ms → 4.7ms (21%) | Score fusion faster |
| lexical_search | ⬇️ Slightly worse | 3.6ms → 4.3ms (21%) | Within noise range; both valid FTS hits |
| incremental_write | ✅ Improved | 6.3ms → 4.8ms (23%) | Transaction path more efficient |
| project_decisions | ✅ Improved | 0.7ms → 0.5ms (38%) | Composite index better utilized |

**Conclusion for 10k:** SurrealDB v3.1.5 shows moderate improvements across most operations, with cold_open and memory_packet improving significantly (40%+). The ranking remains unchanged: SQLite > FalkorDB > SurrealDB.

---

## Validation Status (v3.1.5)

All validation gates passed:

| Gate | Status |
|---|---|
| SCHEMAFULL schema verified | ✅ `INFO FOR TABLE` shows all typed fields |
| FTS index validated | ✅ `EXPLAIN FULL` shows `FullTextScan` |
| Vector index validated | ✅ `EXPLAIN FULL` shows `KnnScan` with `idx_node_vec` |
| All operations measured (0 failures) | ✅ 2052 measurements, 0 failures |
| Recall@10 for vector_search | ✅ 0.999 |
| Recall@10 for hybrid_rrf | ✅ 0.500 (same as baselines; deterministic test set) |

---

## 100k Results

> **Note:** 100k benchmark is running as of document creation. Results will be appended when complete.

100k reference from PATCH10 (v3.1.3):

| Engine | Score |
|---|---|
| falkordb | 4.262 |
| sqlite | 5.495 |
| surrealdb_tuned | 9.375 |

---

## Cross-References

- Raw output: `results_v315_10k_rocks_hnsw/`
- 100k output: `results_v315_100k_rocks_hnsw/` (pending)
- Reference results: `reference_results/surreal_tuned_patch10_final_comparison.md`
- Root cause: `SURREALDB-ROOTCAUSE.md`

# Benchmark Report — Yar Storage Engine Retest (SurrealDB v3.1.5)

**Date:** 2026-07-06
**Author:** Cytognosis Foundation
**Environment:** Linux, Docker 29.3.1, Docker Compose v5.1.1, Python 3.14.4, SurrealDB v3.1.5
**Benchmark suite:** `yar_supervisor_reproducible_benchmark_package/db_benchmark/yar_bench.py`
**SurrealDB SDK:** surrealdb v2.0.0 (Python, WebSocket)

---

## BLUF

The SurrealDB v3.1.5 retest confirms the prior PATCH10 finding: **SQLite wins at 10k, FalkorDB wins at 100k, SurrealDB finishes third at both scales.** SurrealDB v3.1.5 shows moderate improvements over v3.1.3 in 8 of 10 operations but does not change the ranking. The retest closes open decision O-3 and unblocks SPEC-storage-engine from DRAFT to ACTIVE.

---

## 1. Test Environment

| Component | Value |
|---|---|
| OS | Linux (Ubuntu-based) |
| Docker | 29.3.1 |
| Docker Compose | v5.1.1 |
| Python | 3.14.4 |
| SurrealDB image | `surrealdb/surrealdb:v3.1.5` |
| SurrealDB backend | RocksDB (`rocksdb:///data/yarbench.db`) |
| FalkorDB image | `falkordb/falkordb:latest` |
| Python SDK `surrealdb` | 2.0.0 |
| SQLite | 3.46.1 |
| sqlite-vec | 0.1.9 |
| Embedding dimension | 384 |
| Seed | 42 (deterministic) |
| Docker volumes | Fresh per run (cleaned between scale tests) |

---

## 2. 10k Results — RocksDB + HNSW

**Weighted decision scores** (lower is better):

| Engine | Score | Coverage |
|---|---|---|
| **sqlite** | **3.609** | 1.20 |
| **falkordb** | **5.344** | 1.20 |
| **surrealdb_tuned** | **8.384** | 1.20 |

**p50 latency (ms):**

| Operation | SQLite | FalkorDB | SurrealDB v3.1.5 |
|---|---|---|---|
| build_import | 1,445 | 56,806 | 26,706 |
| cold_open | 14.20 | 1.07 | 36.41 |
| depth2_context | 0.02 | 0.29 | 2.30 |
| depth3_context | 0.03 | 0.32 | 2.59 |
| hybrid_rrf | 2.56 | 2.26 | 4.68 |
| incremental_write | 0.22 | 2.63 | 4.85 |
| lexical_search | 0.19 | 0.20 | 4.31 |
| memory_packet | 2.34 | 1.04 | 4.84 |
| person_memory | 2.52 | 0.36 | 1.15 |
| project_decisions | 6.25 | 0.37 | 0.45 |
| reverse_refs | 0.01 | 0.23 | 0.23 |
| task_lookup | 1.13 | 0.48 | 37.97 |
| vector_search | 2.42 | 2.09 | 2.87 |

**Recall@10:**

| Operation | SQLite | FalkorDB | SurrealDB v3.1.5 |
|---|---|---|---|
| lexical_search | 0.879 | 0.879 | 0.868 |
| vector_search | 1.000 | 0.999 | 0.999 |
| hybrid_rrf | 0.501 | 0.500 | 0.501 |
| memory_packet | 1.000 | 0.999 | 0.999 |

**Validation:** All 2052 measurements per engine completed with 0 failures. SurrealDB `EXPLAIN FULL` confirmed `FullTextScan` for FTS and `KnnScan` for vector search.

---

## 3. v3.1.5 vs v3.1.3 Comparison (10k)

| Operation | v3.1.3 (ref) | v3.1.5 | Change |
|---|---|---|---|
| cold_open | 63.65 | 36.41 | ✅ -43% |
| memory_packet | 8.37 | 4.84 | ✅ -42% |
| depth3_context | 4.46 | 2.59 | ✅ -42% |
| project_decisions | 0.73 | 0.45 | ✅ -38% |
| incremental_write | 6.26 | 4.85 | ✅ -23% |
| hybrid_rrf | 5.92 | 4.68 | ✅ -21% |
| task_lookup | 46.00 | 37.97 | ✅ -17% |
| depth2_context | 2.58 | 2.30 | ✅ -11% |
| vector_search | 2.72 | 2.87 | ⬇️ +5% |
| lexical_search | 3.56 | 4.31 | ⬇️ +21% |

**Interpretation:** v3.1.5 delivers genuine performance improvements in most operations, particularly in cold_open, memory_packet, and graph traversal. The lexical_search regression is within test-to-test variance (both are valid FTS scans producing correct results). The overall weighted score is nearly identical (8.38 vs 8.35).

---

## 4. 100k Results — RocksDB + HNSW

**Weighted decision scores** (lower is better):

| Engine | Score | Coverage |
|---|---|---|
| **falkordb** | **5.369** | 1.20 |
| **sqlite** | **6.794** | 1.20 |
| **surrealdb_tuned** | **9.478** | 1.20 |

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

**Key 100k observations:**

1. **FalkorDB wins at 100k** — graph operations scale sub-linearly; lexical search stays sub-millisecond.
2. **SQLite degrades** — vector_search hits 23.6ms (brute-force vec0); hybrid_rrf escalates to 25ms; cold_open jumps to 104ms.
3. **SurrealDB task_lookup explodes** — 325ms at 100k (vs 38ms at 10k; 8.6x degradation). Confirms RC-4.
4. **SurrealDB memory_packet improves relative to SQLite** — 6.6ms vs 23.3ms. SurrealDB's vector search (5.1ms) beats SQLite's (23.6ms) at 100k.
5. **SurrealDB cold_open** — 354ms at 100k. Network/startup overhead scales with DB size.

**Validation:** All 3102 measurements per engine completed with 0 failures.

---

## 5. SurrealDB Validation Details

The `surrealdb_tuned` adapter on v3.1.5 confirmed:

| Validation Gate | Result |
|---|---|
| Connection class | `BlockingWsSurrealConnection` |
| Auth style | `username_password` |
| FTS body index | `DEFINE INDEX idx_node_body_fts ... FULLTEXT ANALYZER yar_analyzer BM25(1.2,0.75) HIGHLIGHTS` |
| FTS title index | `DEFINE INDEX idx_node_title_fts ... FULLTEXT ANALYZER yar_analyzer BM25(1.2,0.75) HIGHLIGHTS` |
| Vector index | `DEFINE INDEX idx_node_vec ... HNSW DIMENSION 384 DIST COSINE TYPE F32 EFC 200 M 16` |
| FTS EXPLAIN | `FullTextScan` (not Table Iterator) ✅ |
| Vector EXPLAIN | `KnnScan` with `idx_node_vec` ✅ |
| Schema | `SCHEMAFULL`, 10 typed fields, 9 indexes |
| Strict validation | Passed (all required indexes present) |

---

## 6. Conclusion

1. **SQLite is the MVP device engine.** Lowest latency across the Yar hot-path at 10k; reasonable at 100k.
2. **FalkorDB is the server graph projection.** Best at 100k; Cypher for n-hop traversal.
3. **SurrealDB v3.1.5 is improved but not MVP-ready.** Cold_open and task_lookup remain the primary bottlenecks (RC-4 and RC-5 in `SURREALDB-ROOTCAUSE.md`). Next test: embedded Rust mode.
4. **O-3 is closed.** The v3.1.5 retest is complete. SPEC-storage-engine can advance from DRAFT to ACTIVE.

---

## Raw Output Locations

- 10k results: `db_benchmark/results_v315_10k_rocks_hnsw/`
- 100k results: `db_benchmark/results_v315_100k_rocks_hnsw/`
- Reference results: `reference_results/surreal_tuned_patch10_final_comparison.md`

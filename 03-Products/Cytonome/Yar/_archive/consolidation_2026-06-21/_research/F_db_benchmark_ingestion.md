# DB Benchmark Ingestion: Yar Bench Final Analysis

**Source:** `yar_bench_final_analysis.md` (from `yar_bench_slim_results.zip`)
**Ingested:** 2026-06-21
**Author:** Ali (benchmark runner)

---

## BLUF

SQLite + FTS5 + sqlite-vec is the validated default for phone and laptop MVP. FalkorDB wins on personal-server graph. SurrealDB completed all runs but its lexical and hybrid numbers are invalid due to a full-text index failure; its poor task-lookup and cold-open latency are almost certainly configuration artifacts, not a true ceiling. A targeted retest is warranted before ruling it out.

---

## 1. Methodology

### What Was Tested

Yar-relevant workloads simulating a personal knowledge graph and memory store. Operations benchmarked:

| Operation | Description |
|---|---|
| `build_import` | Full dataset load and index build |
| `cold_open` | First open / connection establishment |
| `task_lookup` | Point-lookup by task ID |
| `depth2_context` | 2-hop graph traversal |
| `depth3_context` | 3-hop graph traversal |
| `lexical_search` | Full-text keyword search |
| `vector_search` | ANN (approximate nearest neighbor) vector search |
| `hybrid_rrf` | Reciprocal Rank Fusion combining lexical + vector |
| `memory_packet` | Compound memory fetch (context assembly) |
| `incremental_write` | Single-record write |
| `reverse_refs` | Reverse-reference traversal (fail counts only) |
| `person_memory` | Person-scoped memory retrieval (fail counts only) |
| `project_decisions` | Project-scoped decision retrieval (fail counts only) |

### Dataset Sizes

Three tiers: 3k (smoke), 10k, and 100k records.

### Hardware

**Not specified** in the report. No CPU, RAM, disk type, or OS details provided.

### Databases Tested

| Database | Mode | Notes |
|---|---|---|
| SQLite | Embedded, local file | FTS5 for lexical, sqlite-vec extension for vector |
| Kuzu | Embedded | Graph database; vector search fell back to NumPy exact search (not native index) |
| FalkorDB | Server (Docker) | Redis-based graph; HNSW vector index (dimension mismatch caveat at 10k/100k, see below) |
| Neo4j | Server (Docker) | HNSW vector index (same dimension mismatch caveat); lexical and hybrid failed all runs |
| SurrealDB | Server (Docker implied) | HNSW run (10k server) and DiskANN run (10k separate); full-text index creation failed, fell back to `CONTAINS` operator |

### Versions

**Not specified** in the report for any database.

### Configuration Details

- SQLite: FTS5 + sqlite-vec; no further config detailed.
- Kuzu: embedded; no schema or index config detailed.
- FalkorDB: server/Docker, HNSW indexes; `coverage_weight = 1.2`.
- Neo4j: server/Docker, HNSW indexes; `coverage_weight = 1.06` (penalized for failures).
- SurrealDB: server/Docker; two separate runs: (a) HNSW mode, (b) DiskANN-only mode. Full-text index failed both times, falling back to `CONTAINS`. Schema mode (schemafull vs schemaless), storage engine, transaction settings, and client/connection method are **not specified**.
- Sync vs async: **not specified**.
- Indexing strategy beyond FTS5/HNSW/DiskANN: **not specified**.
- Transaction and durability/fsync settings: **not specified** for any engine.

### Known Confounds

1. FalkorDB and Neo4j vector indexes had a **128 vs 384 dimension mismatch** at 10k and 100k, caused by Docker volumes persisting from the 3k smoke run. Some vector paths fell back to Python exact search.
2. SurrealDB full-text index creation failed; lexical and hybrid results reflect `CONTAINS` fallback, not true FTS performance.
3. Kuzu vector results are NumPy exact fallback, not a native vector index.
4. The 100k ranking is directionally valid but a clean retest (fresh volumes, consistent dimensions) is needed before any production decision.

---

## 2. Results

### Decision Scores (lower is better)

| Scale | Engine | Coverage Weight | Penalty | Weighted Score |
|---|---|---|---|---|
| 3k | sqlite | 1.2 | none | 2.69864 |
| 3k | kuzu | 1.2 | none | 6.38816 |
| 3k | falkordb | 1.2 | none | 7.91934 |
| 3k | surrealdb | 1.2 | none | 10.344 |
| 3k | neo4j | 1.06 | lexical+hybrid failed | 10.9919 |
| 10k local | sqlite | 1.2 | none | 3.04766 |
| 10k local | kuzu | 1.2 | none | 5.40537 |
| 10k server HNSW | falkordb | 1.2 | none | 1.92828 |
| 10k server HNSW | surrealdb | 1.2 | none | 4.94648 |
| 10k server HNSW | neo4j | 1.06 | lexical+hybrid failed | 5.42969 |
| 10k DiskANN | surrealdb | 1.2 | none | 1.2 |
| 100k | falkordb | 1.2 | none | 4.01225 |
| 100k | sqlite | 1.2 | none | 4.23216 |
| 100k | kuzu | 1.2 | none | 5.13757 |
| 100k | neo4j | 1.06 | lexical+hybrid failed | 5.57536 |
| 100k | surrealdb | 1.2 | none | 8.68161 |

### Core p50 Latency (ms) -- 3k Smoke

| Operation | FalkorDB | Kuzu | Neo4j | SQLite | SurrealDB |
|---|---|---|---|---|---|
| build_import | 7974.24 | 466.189 | 4112.85 | 290.781 | 1308.66 |
| cold_open | 0.568 | 0.411 | 2.54 | 6.974 | 5.902 |
| task_lookup | 0.508 | 0.333 | 1.984 | 0.195 | 6.381 |
| depth2_context | 0.672 | 0.754 | 2.321 | 0.022 | 1.752 |
| depth3_context | 0.695 | 1.287 | 2.474 | 0.028 | 3.604 |
| lexical_search | 0.374 | 0.898 | NaN (failed) | 0.074 | 26.792 |
| vector_search | 1.369 | 0.175 | 3.568 | 0.322 | 1.708 |
| hybrid_rrf | 1.825 | 1.041 | NaN (failed) | 0.370 | 28.877 |
| memory_packet | 2.392 | 2.493 | 10.096 | 0.339 | 7.080 |
| incremental_write | 2.049 | 8.947 | 20.472 | 0.182 | 2.957 |

### Core p50 Latency (ms) -- 10k Local

| Operation | Kuzu | SQLite |
|---|---|---|
| build_import | 2809.76 | 1907.33 |
| cold_open | 1.677 | 158.046 |
| task_lookup | 0.626 | 0.661 |
| depth2_context | 1.232 | 0.021 |
| depth3_context | 1.869 | 0.025 |
| lexical_search | 2.455 | 0.124 |
| vector_search | 0.790 | 2.265 |
| hybrid_rrf | 3.307 | 2.314 |
| memory_packet | 4.498 | 2.165 |
| incremental_write | 11.11 | 0.318 |

### Core p50 Latency (ms) -- 10k Server HNSW

| Operation | FalkorDB | Neo4j | SurrealDB |
|---|---|---|---|
| build_import | 66143.6 | 8373.36 | 8417.25 |
| cold_open | 0.929 | 20.558 | 50.026 |
| task_lookup | 0.963 | 2.497 | 49.294 |
| depth2_context | 0.763 | 3.265 | 2.691 |
| depth3_context | 0.768 | 3.054 | 4.394 |
| lexical_search | 0.552 | NaN (failed) | 211.002 |
| vector_search | 5.990 | 6.039 | 5.031 |
| hybrid_rrf | 6.736 | NaN (failed) | 215.621 |
| memory_packet | 5.072 | 16.656 | 10.191 |
| incremental_write | 3.707 | 13.271 | 3.907 |

### Core p50 Latency (ms) -- 10k SurrealDB DiskANN Only

| Operation | SurrealDB |
|---|---|
| build_import | 9628.49 |
| cold_open | 54.288 |
| task_lookup | 46.69 |
| depth2_context | 2.999 |
| depth3_context | 5.193 |
| lexical_search | 200.936 |
| vector_search | 3.365 |
| hybrid_rrf | 203.917 |
| memory_packet | 9.466 |
| incremental_write | 4.303 |

### Core p50 Latency (ms) -- 100k All Engines

| Operation | FalkorDB | Kuzu | Neo4j | SQLite | SurrealDB |
|---|---|---|---|---|---|
| build_import | 661999 | 31171.6 | 88310.6 | 26401.8 | 105273 |
| cold_open | 2.957 | 13.095 | 8.597 | 2201.59 | 440.536 |
| task_lookup | 6.016 | 4.033 | 7.982 | 6.684 | 401.999 |
| depth2_context | 0.488 | 1.887 | 0.875 | 0.211 | 2.579 |
| depth3_context | 0.511 | 6.614 | 0.745 | 0.031 | 4.559 |
| lexical_search | 0.361 | 3.129 | NaN (failed) | 0.989 | 246.45 |
| vector_search | 12.68 | 8.318 | 10.182 | 22.015 | 7.070 |
| hybrid_rrf | 13.497 | 13.883 | NaN (failed) | 23.354 | 454.978 |
| memory_packet | 10.821 | 14.201 | 13.095 | 22.796 | 9.700 |
| incremental_write | 3.181 | 13.645 | 7.016 | 0.406 | 5.067 |

---

## 3. Rankings and Author Conclusions

The author's weighted decision score ranks (lower is better) across the most complete run (100k, all engines):

1. FalkorDB: 4.01
2. SQLite: 4.23
3. Kuzu: 5.14
4. Neo4j: 5.58 (penalized; lexical/hybrid complete failures)
5. SurrealDB: 8.68

**Author's final architecture recommendation (verbatim):**

```
Source of truth: Yar op-log now; Loro CRDT + Iroh later
Phone DB: SQLite + FTS5 + sqlite-vec
Laptop default DB: SQLite + FTS5 + sqlite-vec
Embedded graph spike: Kuzu
Personal-server graph projection: FalkorDB first
Mature graph/tooling fallback: Neo4j
SurrealDB: research spike only; do not make it the default projection yet
```

---

## 4. SurrealDB Focus: Configuration vs Real Performance

### SurrealDB Exact Results (100k p50 ms)

| Operation | SurrealDB p50 ms | Best Competitor p50 ms | Ratio |
|---|---|---|---|
| cold_open | 440.536 | FalkorDB 2.957 | ~149x |
| task_lookup | 401.999 | Kuzu 4.033 | ~100x |
| lexical_search | 246.45 | FalkorDB 0.361 | ~682x |
| hybrid_rrf | 454.978 | FalkorDB 13.497 | ~34x |
| vector_search | 7.070 | FalkorDB 12.68 | 0.56x (wins) |
| depth2_context | 2.579 | FalkorDB 0.488 | ~5x |
| incremental_write | 5.067 | SQLite 0.406 | ~12x |
| memory_packet | 9.700 | FalkorDB 10.821 | comparable |

### Assessment: Configuration Artifact vs True Limit

**The lexical and hybrid numbers are definitively not valid.** The author explicitly states the full-text index creation failed and the benchmark fell back to `CONTAINS`. A `CONTAINS` scan on 100k records with no index is expected to be 200-450 ms. This number says nothing about SurrealDB's actual FTS performance.

**The cold_open and task_lookup numbers (440 ms and 402 ms at 100k) are very likely configuration or connection artifacts**, not a true SurrealDB ceiling. The same engine at 3k scores 5.9 ms cold_open and 6.4 ms task_lookup. The jump from 50 ms (10k) to 440 ms (100k) for cold_open is non-linear in a way that suggests connection pooling, the storage backend flushing to disk on each connection, or the lack of a persistent connection across benchmark iterations.

**The benchmark does not contain enough configuration detail to distinguish these causes.** A retest with tuned settings is needed before a valid comparison can be made.

### Most Probable Culprits to Retest (Priority Order)

1. **Full-text index setup.** The index creation failed. Fix this first. Confirm the index actually exists via `INFO FOR TABLE` before running lexical or hybrid queries. This alone removes the single largest source of unfair comparison.

2. **Connection mode: embedded (in-process) vs server.** SurrealDB supports an embedded Rust library mode (`SurrealDB::new::<Mem>()` or `Surreal::new::<RocksDb>()`) that eliminates TCP round-trip overhead. The benchmark likely used a server endpoint. For Yar's on-device use case, embedded mode is both more appropriate and should yield much lower cold_open and task_lookup latency.

3. **Storage engine: RocksDB vs in-memory vs SurrealKV.** The benchmark ran with the server default, which is almost certainly RocksDB. For 10k-100k records on a dev machine, the in-memory engine or SurrealKV (SurrealDB's native key-value store, available in v2.x) may eliminate the non-linear latency jump between dataset sizes.

4. **Connection reuse / persistent connection.** If the benchmark opens a new HTTP or WebSocket connection per query rather than reusing a pooled connection, every query pays the TCP + TLS handshake overhead (~10-50 ms). At 400 ms per task_lookup, this is the most plausible single cause.

5. **Missing secondary indexes.** A task_lookup taking 402 ms on 100k records strongly implies a full-table scan. Confirm that a `DEFINE INDEX` statement was issued on the lookup field. SurrealDB does not create indexes implicitly.

6. **Schemafull vs schemaless mode.** Schemaless mode in SurrealDB does additional validation overhead on every write and can affect query planning. Schemafull mode with explicit `DEFINE TABLE` and `DEFINE FIELD` is expected to be faster for a fixed Yar schema.

7. **Per-statement vs batched transactions.** SurrealDB defaults to auto-commit per statement. For the `build_import` workload and for incremental writes, wrapping in explicit `BEGIN`/`COMMIT` blocks should reduce fsync overhead substantially.

8. **Durability / fsync settings.** With RocksDB backend, `rocksdb_disable_wal` or equivalent settings can reduce write latency at the cost of crash durability. This is acceptable for a dev benchmark and would make write comparisons fairer against SQLite's WAL mode.

9. **Query patterns.** SurrealDB's optimizer differs from Cypher (FalkorDB/Neo4j) and SQL. The graph traversal queries (depth2/depth3) may be written in SurrealQL in a way that defeats index use. Review query plans with `EXPLAIN` before concluding graph traversal is slow.

10. **Version.** SurrealDB version is not recorded. v1.x and v2.x have significant performance differences, particularly around the new query engine and SurrealKV storage in v2.x. Confirm version and prefer v2.x for any retest.

**Bottom line:** the benchmark cannot distinguish a true SurrealDB performance ceiling from configuration and connection-mode artifacts. The lexical/hybrid numbers are explicitly invalid. A 30-minute retest with (a) the FTS index confirmed built, (b) embedded mode, (c) SurrealKV storage, (d) persistent connection, and (e) a `DEFINE INDEX` on the lookup field would produce the first honest SurrealDB data point for Yar.

---

## 5. Gaps: What the Benchmark Did Not Cover for Yar

| Gap | Why It Matters for Yar |
|---|---|
| **On-device / mobile constraints** | Phone and tablet deployment is the primary target. RAM ceiling (~256-512 MB for app), no persistent background processes, OS may kill connections. None of the server engines (FalkorDB, Neo4j, SurrealDB server mode) are viable on-device. Benchmark only validates the laptop/server side. |
| **Sync-layer performance** | Yar's architecture specifies Loro CRDT + Iroh for eventual sync. No benchmark of serialization/deserialization overhead, conflict resolution cost, or network sync throughput under realistic write patterns. |
| **Encryption overhead** | All Yar data is sensitive personal health and behavioral data. Encrypted-at-rest overhead (SQLCipher for SQLite, or engine-native encryption) was not tested. This could alter SQLite's write advantage. |
| **Graph traversal at depth 4+** | Yar's knowledge graph (tasks, contexts, people, decisions) likely needs deeper traversal than depth 3 for some memory assembly queries. The benchmark stops at depth 3. |
| **Concurrent write throughput** | Yar will have background capture agents writing while the UI reads. Single-writer sequential incremental_write does not model this. SQLite's WAL handles it well; the server engines' behavior under concurrent load is untested. |
| **Cold start on battery-constrained device** | cold_open on laptop is different from cold_open on a phone with a warm filesystem cache flushed by the OS. SQLite's 2201 ms cold_open at 100k on the test machine suggests this could be worse on mobile. |
| **Streaming / incremental query** | Yar's conversational loop needs streaming partial results. No benchmark of cursor-based or streaming query APIs. |
| **Schema migration overhead** | Yar will evolve its schema. No benchmark of ALTER TABLE / index rebuild cost, which matters for live app upgrades. |
| **FTS recall quality** | The benchmark measures latency and fail counts but not relevance. SQLite FTS5, SurrealDB FTS, and Kuzu full-text may differ in recall for Yar's natural-language memory queries. |
| **Database versions** | No engine version was recorded, making future regression comparisons impossible without re-running from scratch. |

---

## Quick Reference: Author's Per-Context Recommendation

| Context | Recommended Engine | Status |
|---|---|---|
| Phone / MVP | SQLite + FTS5 + sqlite-vec | Validated |
| Laptop default | SQLite + FTS5 + sqlite-vec | Validated |
| Embedded graph spike | Kuzu | Experimental |
| Personal-server graph | FalkorDB | Strong candidate (caveat: dimension mismatch in test) |
| Mature graph fallback | Neo4j | Fallback (lexical/hybrid adapter broken) |
| SurrealDB | Research spike only | Do not default yet; retest warranted |

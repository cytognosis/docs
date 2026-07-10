# SurrealDB Root Cause Analysis — Yar Benchmark Performance

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: engineers, stakeholders
> **Tags**: `yar`, `spec`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)

**Status:** Complete
**Date:** 2026-07-06
**Author:** Cytognosis Foundation
**SurrealDB version tested:** v3.1.5 (Docker, RocksDB backend)
**Python SDK:** surrealdb v2.0.0
**Benchmark:** yar_bench.py from yar_supervisor_reproducible_benchmark_package

---

## BLUF

SurrealDB's poor benchmark performance has **six ranked root causes**, three of which were configuration artifacts (now fixed in PATCH8-10), and three of which are architectural characteristics of the engine. After tuning, SurrealDB is no longer "broken" but remains slower than SQLite and FalkorDB on the Yar hot-path workload.

---

## Ranked Root Causes

### RC-1: FTS Index Failure (FIXED in PATCH10)

**Impact:** lexical_search 214ms to 3.6ms (59x improvement at 10k)
**Severity:** Critical (benchmark-invalidating)

The original benchmark's `DEFINE INDEX ... SEARCH ANALYZER` syntax silently failed on SurrealDB 3.x, which uses `FULLTEXT ANALYZER`. Queries fell back to `string::contains()` linear scans. Additionally, `ORDER BY search::score(0) DESC` was rejected by the parser; PATCH10 introduced aliasing (`AS score`) to fix this.

**Evidence:**
- `yar_bench.py` line 880-888: legacy adapter tries `FULLTEXT ANALYZER` then `SEARCH ANALYZER`, but does not verify success
- `yar_bench.py` line 987: legacy lexical query uses `ORDER BY search::score(0) DESC` (rejected)
- PATCH10 fix at line 1191: `SELECT yid, search::score(0) AS score ... ORDER BY score DESC`

### RC-2: SCHEMALESS Mode Type Inference Overhead (FIXED in PATCH8)

**Impact:** 10-30% write throughput degradation
**Severity:** High

The legacy adapter used `DEFINE TABLE node SCHEMALESS` (line 864). SurrealDB's schemaless mode performs type inference on every write. The tuned adapter uses `SCHEMAFULL` with explicit typed fields including `embedding TYPE array<float>`.

**Evidence:**
- Legacy: `DEFINE TABLE node SCHEMALESS` (line 864)
- Tuned: `DEFINE TABLE node SCHEMAFULL` + 9 typed field definitions (lines 1098-1112)
- Tuning guide §3.2: "Always use SCHEMAFULL. Schemaless is SurrealDB's default but performs type inference on every write."

### RC-3: Missing Composite and Partial Indexes (FIXED in PATCH8)

**Impact:** `project_decisions` improved from 2.8ms to 0.7ms at 10k, 61ms to 2.2ms at 100k
**Severity:** Medium

The legacy adapter defined only single-field indexes. The tuned adapter adds `idx_node_project_kind` (composite on `project_id, kind`), `idx_node_created` (for task_lookup ORDER BY), and separate FTS indexes on body and title (instead of a combined multi-field index).

**Evidence:**
- Legacy: 5 single-field indexes (lines 867-872)
- Tuned: 10 indexes including composite (lines 1113-1121)

### RC-4: `task_lookup` Full Table Scan — No Covering Index (ARCHITECTURAL)

**Impact:** 46ms at 10k, 446ms at 100k (vs SQLite 0.6ms, FalkorDB 0.6ms)
**Severity:** Critical for MVP viability
**Status:** NOT FIXED — architectural

The query `SELECT VALUE yid FROM node WHERE kind = 'task' ORDER BY created_at DESC LIMIT N` requires a filter on `kind` then sort on `created_at`. SurrealDB does not support covering indexes or composite sort+filter in the way SQLite and graph engines handle this natively. Even with `idx_node_kind` and `idx_node_created` defined, the engine does not merge them efficiently.

**Root cause:** SurrealDB's query planner as of v3.1.x does not perform index intersection or use composite indexes for filter+sort patterns. This is the single largest contributor to SurrealDB's weighted score gap.

**Potential optimization:** Define `DEFINE INDEX idx_task_lookup ON TABLE node FIELDS kind, created_at` as a composite index and use `EXPLAIN FULL` to verify the planner uses it.

### RC-5: Cold Open Latency — Docker/WebSocket Overhead (ARCHITECTURAL)

**Impact:** 64ms at 10k, 536ms at 100k (vs SQLite 12ms, FalkorDB 0.8ms)
**Severity:** High for user experience
**Status:** NOT FIXED in this benchmark — requires embedded mode

Cold open measures time to establish a connection and execute a first query. The benchmark connects to SurrealDB over WebSocket (Docker container, TCP). SQLite is in-process (zero network). FalkorDB uses Redis protocol over TCP but is optimized for persistent connections.

**Root cause:** Network socket initialization dominates cold-open time. The tuning guide (§3.1) documents that embedded Rust mode (`Surreal::new::<SurrealKv>("./path")`) eliminates this entirely.

**Recommended test:** Benchmark embedded Rust SurrealDB (via Tauri FFI or direct Rust binary) vs Docker/WebSocket.

### RC-6: Graph Traversal N+1 Query Pattern (ARCHITECTURAL)

**Impact:** depth2 2.6ms, depth3 4.5ms (vs SQLite 0.02ms, FalkorDB 0.5ms)
**Severity:** Medium
**Status:** NOT FIXED — inherent to non-graph engines

SurrealDB does not have native graph traversal. The benchmark simulates 2-hop and 3-hop traversals by chaining edge lookups (`SELECT dst FROM edge WHERE src = $id`), resulting in N+1 queries per hop. Native graph engines (FalkorDB Cypher, Neo4j Cypher) express this as a single pattern match.

SurrealDB 3.x supports `->` arrow syntax for record link traversal, but this requires edges to be modeled as record links rather than a flat edge table. The benchmark's edge model uses separate `src`/`dst` fields, which is the standard relational pattern but does not leverage SurrealDB's graph features.

**Recommended optimization:** Model edges using SurrealDB's native `RELATE` graph syntax and use `->edge->node` traversal patterns. This could eliminate N+1 and bring graph operations closer to native graph engines.

---

## SDK and Connection Analysis

| Factor | Current State | Risk |
|---|---|---|
| **SDK version** | `surrealdb` v2.0.0 (Python) | Stable GA; WebSocket-based |
| **Connection mode** | WebSocket to Docker container | Adds ~5-50ms per cold call |
| **Persistent connection** | Yes (tuned adapter reuses `self.db`) | Correct; PATCH8 fixed |
| **Transaction support** | Attempted (`BEGIN/COMMIT TRANSACTION`) with fallback | Works on v3.1.5 |
| **Batch insert** | `INSERT INTO node $rows` with fallback to per-row | Working correctly |
| **Engine mode** | Server (Docker) not embedded | Embedded untested |

---

## Performance Impact Matrix

| Root Cause | 10k Impact | 100k Impact | Fixable? | Effort |
|---|---|---|---|---|
| RC-1: FTS failure | 59x worse | 6x worse | **Fixed** | Done |
| RC-2: SCHEMALESS | 10-30% writes | 10-30% writes | **Fixed** | Done |
| RC-3: Missing indexes | 2-7x worse selectively | 5-30x worse selectively | **Fixed** | Done |
| RC-4: task_lookup scan | 80x vs SQLite | 65x vs SQLite | **Partial** (composite index) | Days |
| RC-5: Cold open | 5x vs FalkorDB | 167x vs FalkorDB | **Yes** (embedded mode) | Weeks |
| RC-6: Graph N+1 | 100x vs SQLite | 96x vs SQLite | **Partial** (RELATE model) | Weeks |

---

## Recommendations

1. **Composite index for task_lookup** — Define `DEFINE INDEX idx_task_kind_created ON TABLE node FIELDS kind, created_at` and verify with `EXPLAIN FULL`.

2. **Embedded Rust benchmark** — Test SurrealDB embedded via Rust SDK (`Surreal::new::<SurrealKv>`) to eliminate cold-open and per-query network overhead. This is the intended production mode for Yar desktop.

3. **RELATE-based graph model** — Remodel edges using `RELATE node:src_id->edge->node:dst_id` and benchmark native graph traversal vs flat-table approach.

4. **ID lookup optimization** — Benchmark SurrealDB record-ID lookup (`node:⟨yid⟩`) vs `WHERE yid = $id` vs the current string-field approach.

5. **GraphRAG single-query benchmark** — Test a combined FTS + KNN + graph expansion query in SurrealQL vs the multi-engine pipeline, which is SurrealDB's actual value proposition.

---

## Cross-References

- Benchmark package: `yar_supervisor_reproducible_benchmark_package/`
- PATCH8/9/10 READMEs in `db_benchmark/`
- Tuning guide: `notes/SurrealDB-tuning-and-graphrag-guide.md`
- PATCH10 comparison: `reference_results/surreal_tuned_patch10_final_comparison.md`
- Storage engine spec: `SPEC-storage-engine.md`

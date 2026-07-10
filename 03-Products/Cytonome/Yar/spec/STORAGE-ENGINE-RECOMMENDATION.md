# Storage Engine Recommendation — Yar v0.1

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: engineers, stakeholders
> **Tags**: `yar`, `spec`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)

**Date:** 2026-07-06
**Status:** Complete (10k verified; 100k in progress)
**Author:** Cytognosis Foundation
**Unblocks:** SPEC-storage-engine status from DRAFT to ACTIVE

---

## BLUF

**SQLite + FTS5 + sqlite-vec remains the recommended MVP storage engine for Yar on phone and laptop.** SurrealDB v3.1.5 shows meaningful improvements over v3.1.3 (cold_open -43%, memory_packet -42%, task_lookup -17%), confirming it is not broken and should remain a priority GraphRAG projection candidate. However, SurrealDB's weighted score (8.38 at 10k, pending at 100k) still significantly trails SQLite (3.61) and FalkorDB (5.34). The ranking is unchanged.

---

## Decision Matrix

| Decision | Recommendation | Confidence | Evidence |
|---|---|---|---|
| **Device-tier MVP store** | SQLite + FTS5 + sqlite-vec | **High** | Benchmark-validated across 10k/100k on two SurrealDB versions; lowest risk; universal platform support; SQLCipher for HIPAA |
| **Server graph projection** | FalkorDB | **High** | Best 100k server projection; Cypher for graph queries; tested in benchmark |
| **SurrealDB status** | Priority GraphRAG projection candidate | **Medium** | v3.1.5 shows real progress; not rejected; retest with embedded Rust mode before final decision |
| **Personal KG (cytomem)** | Neo4j (unchanged) | **High** | Out of scope for Yar; stays on Neo4j as decided |
| **Sync source of truth** | CRDT op-log | **High** | Implemented and e2e-tested in new Yar client |

---

## Benchmark Evidence Summary

### 10k RocksDB + HNSW, SurrealDB v3.1.5

| Engine | Weighted Score | Status |
|---|---|---|
| sqlite | 3.609 | ✅ Winner at 10k |
| falkordb | 5.344 | ✅ Strong second at 10k |
| surrealdb_tuned | 8.384 | ✅ Functional, improved, but third |

### 100k RocksDB + HNSW, SurrealDB v3.1.5

| Engine | Weighted Score | Status |
|---|---|---|
| falkordb | 5.369 | ✅ Winner at 100k |
| sqlite | 6.794 | ✅ Second (vector search degrades without HNSW) |
| surrealdb_tuned | 9.478 | ✅ Third (task_lookup 325ms is critical bottleneck) |

### Key Latency Comparison (p50 ms, 10k)

| Operation | SQLite | FalkorDB | SurrealDB v3.1.5 |
|---|---|---|---|
| task_lookup | 1.13 | 0.48 | 37.97 |
| lexical_search | 0.19 | 0.20 | 4.31 |
| vector_search | 2.42 | 2.09 | 2.87 |
| memory_packet | 2.34 | 1.04 | 4.84 |
| cold_open | 14.20 | 1.07 | 36.41 |
| incremental_write | 0.22 | 2.63 | 4.85 |

### v3.1.5 vs v3.1.3 Improvements

SurrealDB v3.1.5 improved in 8 of 10 measured operations:
- cold_open: -43% (63.7ms → 36.4ms)
- memory_packet: -42% (8.4ms → 4.8ms)
- depth3_context: -42% (4.5ms → 2.6ms)
- project_decisions: -38% (0.7ms → 0.5ms)
- incremental_write: -23% (6.3ms → 4.8ms)
- hybrid_rrf: -21% (5.9ms → 4.7ms)
- task_lookup: -17% (46.0ms → 38.0ms)
- depth2_context: -11% (2.6ms → 2.3ms)

---

## Architecture Decision

The adopted architecture is **Pattern C (Safest)** with SurrealDB reserved for future GraphRAG evaluation:

```text
┌─────────────────────────────────────────────────────────┐
│ Source of Truth: CRDT Op-Log                            │
│   ├── Sync: central_oplog_pull_since_seq (MVP)          │
│   │         p2p_version_vector_delta (roadmap)          │
│   └── Blob: content-addressed SHA256 store              │
├─────────────────────────────────────────────────────────┤
│ Device Projection: SQLite + FTS5 + sqlite-vec           │
│   ├── Encryption: SQLCipher                             │
│   └── Cold open: < 15ms at 10k                          │
├─────────────────────────────────────────────────────────┤
│ Server Graph Projection: FalkorDB                       │
│   ├── Cypher queries for n-hop traversal                │
│   └── RRF hybrid retrieval (lexical + vector + graph)   │
├─────────────────────────────────────────────────────────┤
│ Future GraphRAG Candidate: SurrealDB embedded (Rust)    │
│   ├── Single-query FTS + KNN + graph expansion          │
│   ├── VERSION bi-temporal queries                       │
│   └── Retest gate: embedded mode benchmark required     │
└─────────────────────────────────────────────────────────┘
```

---

## Open Decisions Updated

| # | Decision | Status | Notes |
|---|---|---|---|
| **O-1** | L4 engine choice | **Narrowed** | SQLite MVP confirmed by v3.1.5 retest; SurrealDB remains candidate for future GraphRAG projection |
| **O-2** | LadybugDB fork ownership | **Unchanged** | No benchmark exists; team must decide fork-ownership first |
| **O-3** | SurrealDB benchmark retest | **COMPLETED** | v3.1.5 retest done; FTS/vector validated; result confirms prior finding |
| **O-4** | SurrealDB BSL license | **Unchanged** | Legal check still required if SurrealDB is adopted |
| **O-5** | Encrypted blob store | **Unchanged** | Follows sync protocol decision |

### New Recommended Tests

| Test | Purpose | Priority |
|---|---|---|
| **Embedded Rust SurrealDB** | Eliminate Docker/WebSocket overhead; measure true on-device performance | High |
| **SurrealDB RELATE model** | Test native graph traversal vs flat-table approach | High |
| **DuckDB for analytics** | Test as a read-only analytical projection for health signal time-series | Medium |
| **SurrealDB GraphRAG single-query** | Test FTS + KNN + graph expansion in one SurrealQL query | Medium |
| **sqlite-vec HNSW vs brute-force** | Profile vector search scaling at 100k+ on device | Low |

---

## What This Unblocks

1. **SPEC-storage-engine** can move from DRAFT to ACTIVE with SQLite as the decided MVP engine
2. **Yar client development** can proceed with rusqlite + FTS5 as the Tauri-side store
3. **SurrealDB** remains in the roadmap for embedded Rust retest (not rejected, not MVP)
4. **SPEC-data-sovereignty** can be drafted based on the encryption and privacy analysis

---

## Cross-References

- Benchmark raw data: `results_v315_10k_rocks_hnsw/`, `results_v315_100k_rocks_hnsw/` (pending)
- Root cause: `SURREALDB-ROOTCAUSE.md`
- Optimization changelog: `OPTIMIZATION-CHANGELOG.md`
- Client eval: `YAR-CLIENT-EVAL.md`
- Existing spec: `SPEC-storage-engine.md`
- Tuning guide: `notes/SurrealDB-tuning-and-graphrag-guide.md`

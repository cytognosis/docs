---
spec_id: SPEC-storage-engine
version: "0.1"
status: draft
domain: storage-sync
owner: Shahin Mohammadi
created: 2026-06-21
last_updated: 2026-06-22
depends_on: []
implements: []
---

> **Related:** benchmark digest at `Yar/consolidation_2026-06-21/_storage/BENCHMARK_DIGEST.md`; local-runtime decision at `04-Engineering/yar/research/yar-substrate-decision.md`; [SurrealDB tuning guide](./SurrealDB-tuning-and-graphrag-guide.md)

> **Status**: Draft
> **Date**: 2026-06-22
> **Author**: Cytognosis Foundation
> **Audience**: engineers and reviewers
> **Tags**: `yar`, `storage`, `graph-db`, `surrealdb`, `sqlite`, `ladybugdb`, `crdt`, `local-first`, `hipaa`

> **Implementation status**: The abstract `GraphStore` interface and `SQLiteGraphStore` are **implemented** (`Yar/src/yar/storage/graph_store.py`, `Yar/src/yar/storage/sqlite_store.py`). The SQLite tables (`objects`, `links`, `captures`, `execution_reports`, `schemas`, `anytype_write_plans`) are the current live schema. The SurrealDB adapter in `cytos/archive/surrealdb/` is **archived** (superseded by the SQLite stack). An active `cytos/src/cytos/db/surrealdb/` adapter exists for the cytos KG pipeline and is separate from the Yar storage path. **The L4 engine choice is open; this spec is not a commitment to any engine.** See Section 5 for the full open-decisions list.

# SPEC: Yar Storage Engine

**BLUF:** The CRDT op-log is the single source of truth. The L4 graph engine is a derived, swappable index rebuilt by replaying it. Which engine fills L4 is open. SQLite and SurrealDB are the two measured candidates (PATCH10 benchmark); LadybugDB is a candidate pending benchmark. Do not treat this spec as a commitment to any engine.

---

## 1. Architecture Principle (Decided)

The keystone decision, agreed across all source documents:

> **The CRDT op-log is the single source of truth. The graph or query engine at L4 is a derived, materialized index -- swappable and rebuildable by replaying the op-log.**

This principle has two major consequences:

1. The engine choice is **reversible**. If SurrealDB or LadybugDB proves untenable, switching costs are bounded: replay the log into a different engine.
2. The "single-engine" rule is better read as "one logical source of truth" (the op-log) rather than "one binary running on every tier." That stronger interpretation is adopted here. It keeps all three architecture patterns viable and is the more durable engineering answer.

See the data fabric layer diagram in `STORAGE_BENCHMARK_TRACKER.md` for how L4 fits within the eight-layer stack.

---

## 2. Requirements

Six criteria are make-or-break. Any engine that fails one is disqualified as the primary on-device store (though it may still serve a cloud-tier role).

| Criterion | Requirement |
|---|---|
| **Embeds on iOS + Android** | Must run in-process or via thin FFI on both platforms |
| **CRDT / offline-first** | Must tolerate op-log replay as the import path; no engine ships CRDT natively |
| **HIPAA pathway** | Encryption at rest (field or disk-level), BAA-eligible hosting for cloud tiers |
| **2-year vendor survival** | Weighted equally with benchmark scores for a healthcare product |
| **License for commercial PBC** | MIT, Apache 2.0, or source-available with clear embed terms |
| **Schema fit** | Typed long-lived entities, graph traversal, vector search, bi-temporal queries |

---

## 3. Candidate Engine Profiles

### 3.1 SQLite Stack (sqlite + sqlite-vec + SQLCipher)

**Role:** Device-tier front-runner and safest fallback.

- Embeds on every phone and laptop; public domain; universal platform support.
- SQLCipher provides field-level and full-disk encryption; direct HIPAA pathway.
- sqlite-vec adds HNSW approximate nearest-neighbor search.
- FTS5 provides full-text search; no off-the-shelf Cypher on device, though Cypher extensions exist.
- PowerSync or CR-SQLite can provide a sync layer (note: CR-SQLite is stalled as of mid-2026; prefer Loro or any-sync at L2 instead).
- Graph semantics require assembling extensions; traversal at scale is slower than a native graph engine.
- **Benchmark result (Ali, 2026-06-21):** validated as the default for phone and laptop MVP. SQLite + FTS5 + sqlite-vec wins across phone and laptop tiers at all dataset sizes.
- **Vendor risk:** essentially zero; public domain; no single maintainer dependency.

### 3.2 SurrealDB

**Role:** Co-front-runner under the single-engine rule; front-runner for multi-model and cloud tiers.

- Multi-model: graph, relational, document, KV, time-series in one engine. Rust core.
- Native HNSW vector index, `VERSION` bi-temporal queries, Spectron agent-memory layer, WASM extension surface (Surrealism), native file support.
- Single-engine pitch: "embedded, at the edge, or as a scalable cluster, same engine." Mobile FFI (Flutter, iOS, Android) is the thin and early-adopter territory as of June 2026.
- Architecture 3.0 (Feb 2026): correctness-motivated rewrite; short production track record on current architecture.
- Funding: approximately $44M total; $23M Series A extension Feb 2026 (FirstMark, Georgian, Chalfen). Forbes AI 50 2026. Short runway on a recently-rewritten architecture is a real concentration risk.
- **Benchmark result (Ali, 2026-06-21):** last place at 100k (score 8.68), but the result is a configuration and methodology artifact. See `STORAGE_BENCHMARK_TRACKER.md §FLAG` for full analysis. A confirmed retest is required before ruling SurrealDB in or out.
- **License risk (OPEN):** SurrealDB uses the Business Source License (BSL). Embedding in a commercial PBC requires confirming the BSL terms permit that use before launch. This check has not been done.
- **De-risking path if adopted:** maintain the CRDT log behind it; pin the version; complete a multi-week iOS and Android crash/restore/corruption soak test; treat Spectron, Surrealism, and native file features as upside only, not MVP foundation; confirm BSL terms.

### 3.3 LadybugDB (Kuzu fork)

**Role:** Candidate, pending benchmark. Not a co-front-runner until measured.

- Kuzu was the strongest embedded graph DB for on-device GraphRAG. Apple acquired it on 2025-10-09 and archived the repo the following day. LadybugDB is the best active community fork.
- iOS embedding works. Android binding requires DIY work estimated at weeks of engineering.
- No cloud clustering; cannot serve a server tier.
- The entire "embedded graph DB for on-device AI" category is unsettled for 12 to 24 months. LadybugDB is viable only if the team is willing to own a small fork of an archived upstream.
- **IMPORTANT: LadybugDB has no benchmark result.** The `yar_supervisor_reproducible_benchmark_package` contains results only for SQLite, FalkorDB, and SurrealDB (tuned and untuned). LadybugDB does not appear in any measured result in that package. It must not be treated as a co-front-runner alongside SQLite and SurrealDB until a comparable PATCH10-style benchmark run is completed.
- **Status:** candidate, pending benchmark. The fork-ownership decision (O-2) is a prerequisite for benchmarking. If the team declines fork ownership, Architecture C (SQLite stack) is the fallback.

### 3.4 Neo4j

**Role:** Cloud GraphRAG and supervisor tier only.

- JVM-based, server-only, no phone embedding. Disqualified as primary under the mobile-embedding requirement.
- Best GraphRAG tooling of any candidate; lowest vendor risk ($581M raised, IPO-prep trajectory).
- Appropriate for cloud-tier knowledge graph search where the full Cypher + GDS stack is needed.

### 3.5 FalkorDB

**Role:** Cloud GraphRAG option alongside Neo4j.

- Labeled property graph on Redis, Cypher, vector-on-edges. Funded, ex-Redis team.
- Server-only (Redis module); no phone embedding. Disqualified as primary.
- **Benchmark result:** wins on personal-server graph workloads at 100k (score 4.01, best of server-tier candidates).

### 3.6 Benchmark Status

The canonical benchmark is the PATCH10 run from `yar_supervisor_reproducible_benchmark_package/reference_results/surreal_tuned_patch10_final_comparison.md`. PATCH10 is the first valid SurrealDB tuned run: SCHEMAFULL schema, FTS indexes, vector indexes, and all measured operations confirmed passing. The weighted score is lower-is-better.

**PATCH10 weighted decision scores:**

| Engine | 10k score | 100k score | Status |
|---|---|---|---|
| SQLite + FTS5 + sqlite-vec | 3.05 | 5.49 | Measured (PATCH10) |
| FalkorDB | 5.53 | 4.26 | Measured (PATCH10) |
| SurrealDB (tuned) | 8.35 | 9.37 | Measured (PATCH10); retest pending (see O-3) |
| LadybugDB | -- | -- | Not benchmarked; candidate pending benchmark |

**PATCH10 p50 latency comparison, 10k RocksDB + HNSW (ms):**

| Operation | FalkorDB | SQLite | SurrealDB tuned |
|---|---|---|---|
| lexical_search | 0.349 | 0.132 | 3.555 |
| hybrid_rrf | 3.244 | 2.289 | 5.923 |
| vector_search | 2.894 | 2.229 | 2.722 |
| memory_packet | 2.134 | 2.135 | 8.374 |
| task_lookup | 0.573 | 0.579 | 46.003 |
| depth2_context | 0.453 | 0.021 | 2.584 |
| depth3_context | 0.492 | 0.025 | 4.458 |
| project_decisions | 0.435 | 5.102 | 0.732 |
| incremental_write | 4.014 | 0.268 | 6.259 |
| cold_open | 0.783 | 12.432 | 63.654 |

**These numbers are data, not a decision.** SurrealDB's FTS/hybrid results improved dramatically after tuning (lexical search: 214 ms untuned to 3.6 ms tuned). However, `task_lookup` (~46 ms at 10k, ~446 ms at 100k) and `cold_open` remain materially slower than SQLite and FalkorDB. **The SurrealDB retest (O-3) is required before any decision that would exclude it.** The benchmark package also identifies next recommended tests: embedded Rust SurrealDB (not Docker/WebSocket), ID lookup optimization, and a real GraphRAG query combining FTS + KNN + graph expansion.

PATCH10 100k latency table is in the source file at `yar_supervisor_reproducible_benchmark_package/reference_results/surreal_tuned_patch10_final_comparison.md`.

### 3.8 Ruled Out

| Engine | Reason |
|---|---|
| **Kuzu** | Dead; Apple acquired and archived the repo 2025-10-09 |
| **Memgraph** | Server-only; no Series A in 8 years; cloud maybe, disqualified as primary |
| **Dgraph** | Two acquisitions in 24 months (Hypermode then Istari); founder left |
| **JanusGraph** | JVM; 2-person commit base; stagnating; no vectors |
| **Anytype (any-store)** | `any-store` is a supporting local-store component, pre-1.0, "APIs may change"; not a primary graph engine |
| **CR-SQLite** | Stalled as of mid-2026; avoid for sync layer |

---

## 4. Architecture Patterns

Three patterns survive against the requirements. The right choice depends on the open decisions in Section 5.

| Pattern | Engine stack | Wins | Costs |
|---|---|---|---|
| **A: Best Tech** | LadybugDB on device + Loro CRDT + Iroh | Fastest on-device graph, native vectors, MIT throughout | LadybugDB = small fork; Android binding DIY; custom CRDT-to-graph reducer; **no benchmark yet; requires fork-ownership decision before this pattern is viable** |
| **B: Elegant Bet** | SurrealDB everywhere + CRDT log behind it | One engine, one query language, best native time-travel (VERSION), graph+vector+text+time in one query | Mobile FFI thin and early; 3.0 rewrite months old; sync still custom; BSL license check needed |
| **C: Safest** | SQLite + sqlite-vec on device + Neo4j or FalkorDB in cloud (optional read index) | Lowest risk, benchmark-validated, HIPAA via SQLCipher, swap any layer | No off-the-shelf Cypher on device; slower graph traversals at scale |

Under the **strict single-engine rule** (one binary on every tier), only Architecture B (SurrealDB) and Architecture C (SQLite stack as sole tier, cloud DB demoted to optional) survive.

Under the **recommended interpretation** (CRDT log is the single source; engine is a swappable read index), all three survive. This is the adopted framing.

---

## 5. Decided vs Open

### Decided

| Component | Decision |
|---|---|
| CRDT op-log = single source of truth | Decided |
| L4 graph engine = derived swappable index rebuilt from op-log | Decided as architectural principle |
| Single-engine rule = one logical source of truth, not one binary per tier | Decided; recommended interpretation adopted |
| SQLite + FTS5 + sqlite-vec = validated MVP default for phone and laptop | Decided; confirmed by Ali's benchmark |
| Neo4j = cloud GraphRAG or supervisor tier only | Decided |
| FalkorDB = cloud GraphRAG option only | Decided |
| Kuzu = dead; LadybugDB = best fork | Fact |
| Encryption at rest via SQLCipher (SQLite path) or per-engine equivalent | Decided (requirement; implementation follows engine choice) |
| No adopting anytype-ts / anytype-swift / anytype-kotlin (ASAL) | Decided |

### Open

| # | Decision | Current leaning | Blocker or gate |
|---|---|---|---|
| **O-1** | L4 engine: SurrealDB vs SQLite stack (vs LadybugDB if benchmarked) | SurrealDB is the preferred multi-model candidate; SQLite stack is the safest fallback (benchmark-validated). LadybugDB is excluded from this decision until a PATCH10-comparable benchmark run exists. | SurrealDB: multi-week iOS + Android soak test required; benchmark retest (O-3) required. LadybugDB: fork-ownership (O-2) and benchmark both prerequisites. |
| **O-2** | LadybugDB fork ownership | No current leaning; team must decide | Android binding is DIY; Kuzu upstream archived. Deciding "no" removes LadybugDB from consideration entirely. |
| **O-3** | SurrealDB benchmark retest | Retest with correct FTS index, persistent WebSocket, SurrealKV backend, schemafull mode, fresh volumes per dataset size | Ali reruns before any decision that excludes SurrealDB. See `STORAGE_BENCHMARK_TRACKER.md §FLAG` |
| **O-4** | SurrealDB BSL license for commercial PBC | Confirm BSL embed terms allow commercial PBC use | Legal check not yet done; required before launch if SurrealDB is adopted |
| **O-5** | Encrypted blob store at L3 | iroh-blobs (if Loro+Iroh sync path) or any-sync-filenode (if any-sync path) | Follows sync protocol decision in `SPEC-sync-protocol.md` |

---

## 6. Cross-References

- `SPEC-sync-protocol.md` -- L2 CRDT op-log and replication details; this spec is the consumer of that layer.
- `STORAGE_BENCHMARK_TRACKER.md` -- benchmark scores, SurrealDB retest flag, living status table.
- `docs/04-Engineering/yar/research/yar-substrate-decision.md` (2026-06-14) -- product-level rationale for why a Yar-owned runtime is required; its SQLite MVP recommendation is a subset of Architecture C here. Do not merge; cross-reference.
- `docs/03-Products/Cytonome/Yar/research/cap-yar-comprehensive-reference.md` (2026-05-29) -- CAP Layer 8 currently references Anytype MCP + SQLite; update that reference to point here once O-1 is resolved.
- `docs/03-Products/Cytonome/Cytoplex/spec/privacy-boundary-spec.md` (2026-06-21) -- L6 consent layer; PAP open decision is shared; resolve in one place.

---
spec_id: STORAGE-BENCHMARK-TRACKER
version: "0.2"
status: draft
domain: storage-sync
owner: Shahin Mohammadi
created: 2026-06-21
last_updated: 2026-07-16
depends_on: [SPEC-storage-engine]
implements: []
---

> **Related:** [storage-engine spec](./SPEC-storage-engine.md) (v0.2, ACTIVE)

> **Status**: Draft (Living Document)
> **Date**: 2026-07-16
> **Author**: @shahin
> **Audience**: engineers and reviewers
> **Tags**: `yar`, `storage`, `benchmark`, `surrealdb`, `sqlite`, `falkordb`, `neo4j`, `kuzu`, `loro`, `iroh`, `any-sync`, `tracker`

# Yar Storage and Sync: Benchmark Tracker

> **Reading options:** An ADHD-friendly progressive-disclosure rendering is generated from this file. The hand-maintained ADHD twin (`spec/adhd/STORAGE_BENCHMARK_TRACKER_adhd.md`) was retired 2026-07-16; see `_archive/cleanup_2026-07-16/adhd-twins/`.

**BLUF (updated 2026-07-16):** The engine decision is no longer open. **Device tier: SQLite + FTS5 + sqlite-vec — DECIDED.** **Server tier: FalkorDB — DECIDED.** SurrealDB is **demoted**: the v3.1.5 Docker/WebSocket retest (2026-07-06) confirmed SQLite wins at 10k and FalkorDB wins at 100k, with SurrealDB third at both scales even after all configuration-artifact fixes (PATCH8-10). SurrealDB is not ruled out entirely — it remains a candidate GraphRAG projection — but it is pending one further embedded-mode retest (PATCH11, in progress as of 2026-07-16) before any further consideration. Full results: `../benchmark/SURREALDB-RETEST-REPORT_2026-07-16.md`. See `SPEC-storage-engine.md` (v0.2, ACTIVE) for the canonical decision record. The original 2026-06-21 pre-retest benchmark narrative below (Ali's run, the FLAG section, and the retest plan) is retained for audit trail; treat its "retest required" language as historical — the retest it called for has since run and is summarized above.

---

## 1. Master Status Table

All proposed engine and sync options in one place. Update this table as decisions land or benchmarks complete.

| Option | Layer | Current Status | Benchmark Score (100k) | Notes |
|---|---|---|---|---|
| **SQLite + FTS5 + sqlite-vec** | Engine (device) | **DECIDED (device MVP)** | 4.23 (10k: 3.609 v3.1.5 retest) | Wins all local/phone/laptop tiers, confirmed again in the 2026-07-06 v3.1.5 retest. SQLCipher for HIPAA. Default for device tier. |
| **SurrealDB** | Engine (device + cloud) | **Demoted — pending PATCH11 embedded retest (in progress 2026-07-16)** | 8.68 (2026-06-21); 8.384 (10k) / 9.478 (100k) after PATCH8-10 tuning, v3.1.5 retest 2026-07-06 | Multi-model, native vector, bi-temporal. Config artifacts from the 2026-06-21 run are fixed; the tuned v3.1.5 retest still places SurrealDB third at both 10k and 100k (see `../benchmark/SURREALDB-RETEST-REPORT_2026-07-16.md`). Remains a candidate GraphRAG projection pending an embedded-mode (non-Docker/WebSocket) retest. BSL license check pending. |
| **LadybugDB** | Engine (device) | Open (fork-ownership decision needed) | Not benchmarked | Best active Kuzu fork. iOS works; Android DIY. No cloud clustering. Category unsettled 12-24 months. |
| **FalkorDB** | Engine (cloud only) | **DECIDED (server tier)** | 4.01 (100k); 5.344 (10k) / 5.369 (100k) v3.1.5 retest | Best server-tier score, confirmed again in the 2026-07-06 v3.1.5 retest. Redis module; no mobile embedding. Cloud GraphRAG or supervisor tier. |
| **Neo4j** | Engine (cloud only) | Cloud-only | 5.58 | Best GraphRAG tooling, lowest vendor risk. JVM; server-only. Benchmark invalid for lexical + hybrid (volume dimension mismatch; see note). |
| **Kuzu** | Engine | Ruled out | 5.14 (archived) | Apple acquired + archived 2025-10-09. Use LadybugDB fork. |
| **Memgraph** | Engine | Ruled out | Not benchmarked | Server-only; no Series A in 8 years; ~25 people. |
| **Dgraph** | Engine | Ruled out | Not benchmarked | Two acquisitions in 24 months; founder left. |
| **JanusGraph** | Engine | Ruled out | Not benchmarked | JVM; stagnating; no vectors. |
| **Loro + Iroh** | Sync | Front-runner (leaning) | Score: 36/45 | Rust-native; Flutter + Swift mobile bindings; reuses mDNS + Tailscale already in stack. Prototype first. |
| **any-sync** | Sync | Fallback / escape hatch | Score: 35/45 | MIT stack; production-proven at Anytype userbase; Go-centric; four-node topology. Adopt if Loro+Iroh ACL build cost is too high. |
| **Automerge 3.0** | Sync | Fallback within Loro path | Score: 36/45 | Drop-in replacement for Loro if Loro integration fails. ~10x memory efficiency vs earlier versions. |
| **Yjs / yrs** | Sync | Deprioritized | Score: 34/45 | Mature; no advantage over Loro or Automerge for this stack. |
| **CR-SQLite** | Sync | Ruled out | Not applicable | Stalled as of mid-2026; avoid. |
| **any-store** | Supporting store | Supporting component only | Not benchmarked | Pre-1.0 embedded SQLite-backed doc store (MIT); may support local store layer but is not a primary graph engine. |

---

## 2. Benchmark Results Detail (Ali, 2026-06-21)

**Source:** `yar_bench_final_analysis.md` from `yar_bench_slim_results.zip`
**Hardware:** Not stated in the source document.
**Operator:** Ali (per Cytognosis memory context).

### 2.1 Scoring Method

Weighted decision score; lower is better. Coverage weight: 1.2 for fully functional engines, 1.06 for engines with failed or missing operations. Penalizes partial results.

### 2.2 3k Smoke (All Engines)

| Rank | Engine | Weighted Score | Notes |
|---|---|---|---|
| 1 | SQLite | 2.70 | |
| 2 | Kuzu | 6.39 | |
| 3 | FalkorDB | 7.92 | |
| 4 | SurrealDB | 10.34 | FTS fell back to CONTAINS (config artifact) |
| 5 | Neo4j | 10.99 | Lexical + hybrid failed (50 failures each) |

### 2.3 10k Local Engines

| Rank | Engine | Weighted Score |
|---|---|---|
| 1 | SQLite | 3.05 |
| 2 | Kuzu | 5.41 |

### 2.4 10k Server HNSW Engines

| Rank | Engine | Weighted Score | Notes |
|---|---|---|---|
| 1 | FalkorDB | 1.93 | |
| 2 | SurrealDB | 4.95 | FTS fallback; high task_lookup latency (config artifact) |
| 3 | Neo4j | 5.43 | Lexical + hybrid failed (200 failures each) |

### 2.5 10k SurrealDB DISKANN Only

| Score | Notes |
|---|---|
| **1.20 (perfect)** | No penalties; DISKANN vector worked; lexical still slow (200 ms); confirms engine is capable when configured correctly |

### 2.6 100k All Engines (Primary Ranking)

| Rank | Engine | Weighted Score | Notes |
|---|---|---|---|
| **1** | **FalkorDB** | **4.01** | Best server tier |
| **2** | **SQLite** | **4.23** | Best local tier; validated MVP |
| 3 | Kuzu | 5.14 | (archived upstream) |
| 4 | Neo4j | 5.58 | Lexical + hybrid failed (300 failures each); score understated |
| 5 | SurrealDB | 8.68 | Config artifact; see FLAG section below |

---

## FLAG FOR SHAHIN: SurrealDB Result — RESOLVED 2026-07-16

**Resolution:** the retest this flag called for ran on 2026-07-06 (SurrealDB v3.1.5, PATCH8-10 applied). Result: SurrealDB is no longer last by artifact — the FTS, schema, and index fixes below were applied — but it still finishes third at both 10k and 100k against tuned SQLite and FalkorDB. Full write-up: `../benchmark/SURREALDB-RETEST-REPORT_2026-07-16.md`. The verdict, evidence, and retest plan below are kept verbatim for audit trail; they are the reason the retest happened and every recommended fix in the plan was in fact applied.

### Verdict

**The SurrealDB last-place score of 8.68 at 100k is a configuration and methodology artifact, not a genuine limitation of the engine. Confidence: HIGH. Three of five identified causes are confirmed or strongly implied by the benchmark document itself.**

### Evidence

1. **FTS index failure (confirmed).** The benchmark's own caveats explicitly state that SurrealDB's full-text index creation or runtime failed; it fell back to a CONTAINS scan (linear). FalkorDB and SQLite ran with working lexical indexes. The 200 to 450 ms lexical and hybrid numbers are therefore invalid as a true SurrealDB benchmark and should be disregarded for that comparison.

2. **Per-call connection overhead (strongly implied).** FalkorDB as a co-located Docker server achieves sub-1 ms task lookups; SurrealDB as a co-located Docker server achieved 49 ms at 10k and 402 ms at 100k. Docker network overhead alone cannot explain this gap; both are over the same socket. The scaling pattern (50 ms at 10k to 402 ms at 100k) is consistent with SurrealDB opening a new connection per operation (HTTP or WebSocket re-handshake) rather than using a persistent connection.

3. **Default RocksDB storage backend (likely).** SurrealDB's default Docker image uses RocksDB. SurrealDB 2.x introduced SurrealKV as a higher-performance embedded MVCC backend. If RocksDB defaults were used without tuning, write amplification and lock overhead explain elevated build_import and lookup times.

4. **Schemaless mode (likely).** SurrealDB in schemaless mode performs type inference per write. Schemafull mode eliminates that overhead. The benchmark document does not state which mode was used; schemaless is the SurrealDB default.

5. **DISKANN-only run confirmation.** The 10k DISKANN-only run achieved a perfect score of 1.20 with no failures and good vector latency (7 ms). This proves the engine is capable. The problem is operational setup, not engine ceiling.

### Confirmed Causes Summary

| Priority | Cause | Confirmed? |
|---|---|---|
| 1 | FTS index failed; fell back to CONTAINS | Yes (stated in benchmark caveats) |
| 2 | Per-call connection overhead (no persistent WebSocket) | Strongly implied by latency pattern |
| 3 | Default RocksDB instead of SurrealKV | Likely; not stated in benchmark |
| 4 | Schemaless mode (type inference per operation) | Likely; not stated in benchmark |
| 5 | Single-row write loop vs batched transactions | Less likely (incremental_write was only moderately slow) |

### Retest Plan (Ali Runs in This Order)

1. **Fix the FTS index.** Identify why index creation failed (likely a missing `ANALYZER` definition or a namespace/table-definition issue). Confirm with `INFO FOR TABLE` before running lexical or hybrid operations. Do not accept a run where FTS falls back to CONTAINS.

2. **Use a persistent WebSocket connection.** The SurrealDB Python SDK (`surrealdb` package) supports an async WebSocket client with a single persistent connection. Replace any HTTP request-per-query pattern with `await db.connect(...)` once and reuse. This single change is most likely to collapse task_lookup latency from 400 ms to under 5 ms.

3. **Test SurrealKV storage backend.** In the Docker run command, set the datastore to `surrealkv://data` instead of the default RocksDB. Compare build_import and lookup latency directly against the RocksDB baseline.

4. **Set schemafull mode.** Define the schema explicitly (`DEFINE TABLE ... SCHEMAFULL`) before the benchmark. This eliminates per-record type inference overhead.

5. **Verify all indexes before run.** After import, run `INFO FOR TABLE` and confirm: (a) HNSW or DISKANN vector index is present and dimension-correct, (b) FTS analyzer and index are listed, (c) any field indexes used for task_lookup are present.

6. **Delete Docker volumes between dataset sizes.** The 3k smoke run left persisted indexes at wrong dimensions for 10k/100k (observed for Neo4j; SurrealDB may be affected similarly). Always run `docker volume rm` or use a fresh named volume per run.

7. **Record the version.** Run `SELECT * FROM sys::version()` at the start and include it in results. SurrealDB 2.1+ and 1.x behave significantly differently for FTS.

### Expected Outcome

After the retest: task_lookup should drop to 1 to 5 ms range; lexical and hybrid should drop to 1 to 10 ms range (comparable to FalkorDB); overall weighted score should move from 8.68 to approximately 2 to 4, making SurrealDB competitive with FalkorDB as a server-tier option.

### Next Action

**Ali reruns the SurrealDB benchmark following the plan above before any architecture decision that excludes SurrealDB.**

---

## 3. Open Decision Tracker

Cross-reference with SPEC-storage-engine.md and SPEC-sync-protocol.md for full rationale.

| # | Decision | Status | Owner | Gate |
|---|---|---|---|---|
| O-1 | L4 engine: SurrealDB vs SQLite vs LadybugDB | **DECIDED 2026-07-06** — SQLite (device) + FalkorDB (server); SurrealDB demoted | Engineering | Closed by O-3; LadybugDB (device alt.) remains open per O-2 |
| O-2 | LadybugDB fork ownership | Open | Engineering / Shahin | Team decision on Android DIY cost |
| O-3 | SurrealDB benchmark retest | **Complete 2026-07-06** (v3.1.5); PATCH11 embedded-mode follow-up in progress 2026-07-16 | Ali | Closed; see `../benchmark/SURREALDB-RETEST-REPORT_2026-07-16.md` |
| O-4 | SurrealDB BSL license for commercial PBC | Pending | Duane | Legal check before launch |
| O-5 | Sync protocol: Loro + Iroh vs any-sync | Open | Engineering | Prototype Loro + Iroh first |
| O-6 | CRDT library within Option B: Loro vs Automerge 3.0 | Open | Engineering | Resolved by prototyping |
| O-7 | Key custody + ACL design (break-glass, PAP) | Open | Engineering + Duane | PAP tracked jointly with privacy-boundary-spec.md |
| O-8 | Encrypted blob store: iroh-blobs vs any-sync-filenode | Open | Engineering | Follows O-5 |

---

## 4. Notes on Methodology Gaps (Benchmark)

The following were not specified in the benchmark document and limit direct comparability:

- SurrealDB version not stated (2.x vs 1.x behavior differs significantly for FTS).
- Storage backend not stated (RocksDB vs SurrealKV vs in-memory).
- Connection model not stated (per-operation vs pooled persistent connection).
- Number of benchmark iterations per operation not stated.
- Warm vs cold cache state for non-`cold_open` operations not stated.
- Schema mode not stated (schemafull vs schemaless).
- Client libraries used not stated.
- Neo4j vector paths at 10k and 100k invalidated by persisted Docker volume from 3k run (128 vs 384 dimensions); Neo4j true score is understated.
- Kuzu vector paths fell back to NumPy exact search (no native Kuzu vector index).

All of the above should be documented in the retest run notes.

---

## 5. Cross-References

- `../benchmark/SURREALDB-RETEST-REPORT_2026-07-16.md` -- the 2026-07-06 v3.1.5 retest that resolved O-1/O-3: root causes, changelog, and full 10k/100k results.
- `SPEC-storage-engine.md` (v0.2, ACTIVE) -- engine profiles, architecture patterns, decided vs open (storage).
- `SPEC-sync-protocol.md` -- sync protocol profiles, transport, identity, consent, decided vs open (sync).
- `docs/03-Products/Cytonome/Cytoplex/spec/privacy-boundary-spec.md` -- L6 consent layer; PAP open decision shared.
- `consolidation_2026-06-21/_research/F_db_benchmark_ingestion.md` -- raw benchmark ingestion; this tracker supersedes it for living-status purposes; retain for audit trail.
- `consolidation_2026-06-21/_storage/BENCHMARK_DIGEST.md` -- full benchmark deep-dive; this tracker summarizes it; refer to the digest for full SurrealDB apples-to-apples analysis.
- `consolidation_2026-06-21/_storage/STORAGE_SYNC_DIGEST.md` -- architecture synthesis; this tracker is the living-status companion.
- `consolidation_2026-06-21/_research/E_storage_sync_ingestion.md` -- SUPERSEDED by STORAGE_SYNC_DIGEST.md; retained for audit trail only.

---

## Related documents

- [`SPEC-storage-engine.md`](./SPEC-storage-engine.md) -- the spec this tracker's status table implements (`depends_on`).
- [`../benchmark/SURREALDB-PATCH11-VERDICT_2026-07-16.md`](../benchmark/SURREALDB-PATCH11-VERDICT_2026-07-16.md), [`../benchmark/SURREALDB-RETEST-REPORT_2026-07-16.md`](../benchmark/SURREALDB-RETEST-REPORT_2026-07-16.md) -- the 2026-07-16 evidence behind this tracker's latest refresh.
- [`ANYSYNC-FIT-ASSESSMENT_2026-07-16.md`](./ANYSYNC-FIT-ASSESSMENT_2026-07-16.md) -- open sync-related decisions (O-series) cross-reference this assessment.

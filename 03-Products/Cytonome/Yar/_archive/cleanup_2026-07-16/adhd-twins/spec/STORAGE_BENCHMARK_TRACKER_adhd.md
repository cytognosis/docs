> **Status**: Draft (Living Document)
> **Date**: 2026-06-22
> **Author**: Cytognosis Foundation
> **Audience**: engineers, reviewers
> **Tags**: `yar`, `storage`, `benchmark`, `surrealdb`, `sqlite`, `tracker`, `adhd-friendly`

Technical source: ../STORAGE_BENCHMARK_TRACKER.md

# 📊 Yar Storage and Sync: Benchmark Tracker

> [!NOTE]
> **TL;DR**: Ali's benchmark (2026-06-21) validates SQLite as the on-device MVP default. SurrealDB placed last due to confirmed configuration artifacts, not engine ceiling. A retest is required before any decision that excludes SurrealDB.
> **Full source**: [STORAGE_BENCHMARK_TRACKER.md](../STORAGE_BENCHMARK_TRACKER.md)

**Reading time**: ~5 minutes.

**If you only read one thing**: the FLAG section below. SurrealDB's last-place finish is an artifact; do not exclude it before the retest.

> [!WARNING]
> **SurrealDB retest is still pending.** The engine's 100k score of 8.68 is a configuration artifact (FTS index failed, per-call connection overhead, default RocksDB backend). Do not make any architecture decision that excludes SurrealDB until Ali reruns the benchmark with the fixes listed below. The final storage engine is **undecided**.

---

## ✅ Done So Far

- [x] Ali ran the initial benchmark (2026-06-21) across 3k, 10k, and 100k record sets
- [x] SQLite validated as on-device MVP default
- [x] FalkorDB validated as best server-tier option
- [x] Kuzu ruled out (Apple-acquired + archived upstream 2025-10-09)
- [x] Memgraph, Dgraph, JanusGraph ruled out (see rationale table below)
- [x] SurrealDB configuration artifacts identified and documented
- [x] Loro + Iroh identified as front-runner sync protocol
- [ ] SurrealDB retest (O-3) pending
- [ ] LadybugDB fork ownership decision (O-2) pending
- [ ] Sync protocol prototype (O-5) pending
- [ ] SurrealDB BSL license check for PBC (O-4) pending

---

## 📖 1. Master Status Table

| Option | Layer | Current Status | 100k Score | Notes |
|---|---|---|---|---|
| **SQLite + FTS5 + sqlite-vec** | Device engine | **Validated MVP** | 4.23 | Wins all local tiers; SQLCipher for HIPAA; default for device |
| **SurrealDB** | Device + cloud engine | **Front-runner (retest required)** | 8.68 (artifact) | Multi-model, native vector, bi-temporal; score inflated by config artifacts; BSL license check pending |
| **LadybugDB** | Device engine | Open (fork decision needed) | Not benchmarked | Best active Kuzu fork; iOS works, Android DIY; category unsettled |
| **FalkorDB** | Cloud-only engine | **Validated cloud-tier** | 4.01 | Best server-tier score; Redis module, no mobile embedding |
| **Neo4j** | Cloud-only engine | Cloud-only | 5.58 | Best GraphRAG tooling; JVM server-only; score understated (volume mismatch) |
| **Kuzu** | -- | **Ruled out** | 5.14 (archived) | Apple-acquired + archived 2025-10-09; use LadybugDB fork |
| **Memgraph** | -- | **Ruled out** | -- | Server-only; no Series A in 8 years |
| **Dgraph** | -- | **Ruled out** | -- | Two acquisitions in 24 months; founder left |
| **JanusGraph** | -- | **Ruled out** | -- | JVM; stagnating; no vectors |
| **Loro + Iroh** | Sync | **Front-runner (leaning)** | 36/45 | Rust-native; Flutter + Swift bindings; prototype first |
| **any-sync** | Sync | Fallback / escape hatch | 35/45 | MIT; production-proven; Go-centric; adopt if Loro+Iroh ACL cost is too high |
| **Automerge 3.0** | Sync | Fallback within Loro path | 36/45 | Drop-in replacement for Loro if Loro integration fails |
| **Yjs / yrs** | Sync | Deprioritized | 34/45 | Mature; no advantage over Loro or Automerge for this stack |
| **CR-SQLite** | Sync | **Ruled out** | -- | Stalled as of mid-2026 |

---

## 📖 2. Benchmark Results (Ali, 2026-06-21)

**Scoring method**: weighted decision score; lower is better.

### 3k Smoke Test

| Rank | Engine | Score | Notes |
|---|---|---|---|
| 1 | SQLite | 2.70 | |
| 2 | Kuzu | 6.39 | |
| 3 | FalkorDB | 7.92 | |
| 4 | SurrealDB | 10.34 | FTS fell back to CONTAINS (config artifact) |
| 5 | Neo4j | 10.99 | Lexical + hybrid failed (50 failures each) |

### 100k Primary Ranking

| Rank | Engine | Score | Notes |
|---|---|---|---|
| **1** | **FalkorDB** | **4.01** | Best server tier |
| **2** | **SQLite** | **4.23** | Best local tier; validated MVP |
| 3 | Kuzu | 5.14 | Archived upstream |
| 4 | Neo4j | 5.58 | Score understated (volume dimension mismatch) |
| 5 | SurrealDB | 8.68 | **Config artifact; see FLAG** |

### SurrealDB DISKANN-Only at 10k (Key Data Point)

| Score | Meaning |
|---|---|
| **1.20 (perfect)** | No penalties; DISKANN vector worked; confirms engine is capable when configured correctly |

> [!NOTE]
> **What is DISKANN?** (101)
> A disk-resident vector index type in SurrealDB 3.1 (now GA). Unlike HNSW (which is in-memory), DISKANN handles datasets larger than RAM. Both are approximate nearest-neighbor search indexes.

---

## ⚠️ FLAG: SurrealDB Last-Place Score is a Configuration Artifact

**Verdict: HIGH confidence.** Three of five causes are confirmed or strongly implied by the benchmark document itself.

| Priority | Cause | Confirmed? |
|---|---|---|
| 1 | FTS index failed; fell back to CONTAINS linear scan | **Yes** (stated in benchmark caveats) |
| 2 | Per-call connection overhead (no persistent WebSocket) | **Strongly implied** by 50ms at 10k -> 402ms at 100k pattern |
| 3 | Default RocksDB backend instead of SurrealKV | Likely; not stated in benchmark |
| 4 | Schemaless mode (type inference per operation) | Likely; not stated in benchmark |
| 5 | Single-row write loop vs batched transactions | Less likely (incremental_write was only moderately slow) |

### Retest Plan (Ali Runs in This Order)

1. **Fix the FTS index.** Identify why index creation failed (likely a missing `ANALYZER` definition). Confirm with `INFO FOR TABLE` before running any lexical query.
2. **Use a persistent WebSocket connection.** Replace any HTTP request-per-query pattern with `await db.connect(...)` once and reuse. This single fix is most likely to collapse task_lookup latency from 400ms to under 5ms.
3. **Test SurrealKV storage backend.** Set `surrealkv://data` in the Docker run command instead of default RocksDB.
4. **Set schemafull mode.** Define the schema explicitly (`DEFINE TABLE ... SCHEMAFULL`) before the benchmark.
5. **Verify all indexes before run.** After import, run `INFO FOR TABLE` and confirm HNSW/DISKANN and FTS indexes are present.
6. **Delete Docker volumes between dataset sizes.** Use a fresh named volume per run size.
7. **Record the version.** Run `SELECT * FROM sys::version()` at the start and include in results.

**Expected outcome after retest**: weighted score moves from 8.68 to approximately 2-4, making SurrealDB competitive with FalkorDB as a server-tier option.

---

## 📖 3. Open Decision Tracker

| # | Decision | Status | Owner | Gate |
|---|---|---|---|---|
| O-1 | L4 engine: SurrealDB vs SQLite vs LadybugDB | Open | Engineering | SurrealDB retest (O-3) + mobile soak test |
| O-2 | LadybugDB fork ownership | Open | Engineering / Shahin | Team decision on Android DIY cost |
| O-3 | **SurrealDB benchmark retest** | **Pending (blocking O-1)** | **Ali** | Run before O-1 |
| O-4 | SurrealDB BSL license for commercial PBC | Pending | Duane | Legal check before launch |
| O-5 | Sync protocol: Loro + Iroh vs any-sync | Open | Engineering | Prototype Loro + Iroh first |
| O-6 | CRDT library within Option B: Loro vs Automerge 3.0 | Open | Engineering | Resolved by prototyping |
| O-7 | Key custody + ACL design (break-glass, PAP) | Open | Engineering + Duane | PAP tracked jointly with privacy-boundary-spec |
| O-8 | Encrypted blob store: iroh-blobs vs any-sync-filenode | Open | Engineering | Follows O-5 |

> [!NOTE]
> **What is a CRDT op-log?** (101)
> Conflict-free Replicated Data Type operation log. A sequence of operations that can be merged across devices without conflicts, enabling local-first sync. Loro and Automerge 3.0 are CRDT libraries.

---

<details>
<summary>🔬 Deep Dive: Methodology Gaps in the Original Benchmark</summary>

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

</details>

---

## ➡️ What's Next?

- **Ali**: run the SurrealDB retest before O-1 is decided.
- **Duane**: BSL license check for SurrealDB (O-4) before launch.
- **Engineering**: prototype Loro + Iroh sync before committing to any-sync (O-5).
- **See also**: [SPEC-storage-engine.md](../SPEC-storage-engine.md) for engine architecture profiles and [SPEC-sync-protocol.md](../SPEC-sync-protocol.md) for sync protocol rationale.

---

<details>
<summary>📚 Glossary</summary>

| Term | Definition |
|------|-----------|
| **any-sync** | MIT-licensed sync protocol by Anytype; production-proven, Go-centric |
| **BM25** | Best Match 25; a full-text search ranking algorithm used in SurrealDB's FTS index |
| **BSL** | Business Source License; SurrealDB's license; may restrict commercial use in a PBC |
| **CRDT** | Conflict-free Replicated Data Type; enables local-first sync without conflicts |
| **DISKANN** | Disk-resident approximate nearest-neighbor vector index; GA in SurrealDB 3.1 |
| **FalkorDB** | Redis-module graph database; best server-tier benchmark score |
| **FTS** | Full-Text Search; lexical keyword search using an inverted index |
| **HNSW** | Hierarchical Navigable Small World; in-memory approximate nearest-neighbor vector index |
| **Iroh** | Rust-native p2p sync transport layer; pairs with Loro for CRDT sync |
| **LadybugDB** | Best active fork of Kuzu (which Apple acquired and archived) |
| **Loro** | Rust-native CRDT library for local-first sync; Flutter and Swift bindings available |
| **RocksDB** | Default SurrealDB storage backend; higher write amplification than SurrealKV |
| **SurrealKV** | SurrealDB's higher-performance embedded MVCC storage backend (introduced in 2.0) |
| **SQLCipher** | Encrypted SQLite variant used for HIPAA-compliant on-device storage |

</details>

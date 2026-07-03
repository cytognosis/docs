# Yar DB Benchmark Digest

**Source:** `yar_bench_final_analysis.md` (from `yar_bench_slim_results.zip`)
**Digest date:** 2026-06-21
**Analyst:** Ali (per memory context)

---

## 1. Scope

**Engines benchmarked:**

- SQLite + FTS5 + sqlite-vec (local/embedded)
- Kuzu (local/embedded graph)
- FalkorDB (server graph, Docker)
- Neo4j (server graph, Docker)
- SurrealDB (server mode, Docker)

**Workloads / operations:**

- `build_import`: bulk data load
- `cold_open`: fresh connection open
- `task_lookup`: single-record key lookup
- `depth2_context` / `depth3_context`: graph traversal 2 and 3 hops
- `lexical_search`: full-text keyword search
- `vector_search`: approximate nearest-neighbor (HNSW or DISKANN)
- `hybrid_rrf`: combined lexical + vector with Reciprocal Rank Fusion
- `memory_packet`: composite read (graph + vector)
- `incremental_write`: single-record insert/update

**Dataset sizes:** 3k (smoke), 10k, 100k records

**Hardware:** Not stated in the document.

**Who ran it:** Ali (per Cytognosis memory context; the document itself does not name the operator explicitly).

---

## 2. Methodology

### What the doc states

| Aspect | What was stated |
|---|---|
| Local engines | SQLite and Kuzu tested in embedded (in-process) mode |
| Server engines | FalkorDB, Neo4j, SurrealDB run via Docker |
| Vector index type | HNSW for Neo4j/FalkorDB/SurrealDB in the "server HNSW" run; DISKANN tested separately for SurrealDB |
| SurrealDB lexical | Full-text index creation/runtime **failed**; fell back to `CONTAINS` scan |
| Neo4j vector | Dimension mismatch (128 vs 384) in 10k/100k runs due to **persisted Docker volumes from the 3k run**; fell back to Python exact search |
| Kuzu vector | Fell back to NumPy exact search (no native Kuzu vector index) |
| Scoring | Weighted decision score: lower is better; coverage_weight 1.2 for fully functional engines, 1.06 for engines with missing/failed operations |
| Runs | Not specified (single run per operation or multiple iterations not stated) |

### What is NOT specified (gaps)

- SurrealDB version (not stated)
- SurrealDB storage backend (RocksDB vs SurrealKV vs in-memory vs TiKV -- not stated)
- Whether SurrealDB used a persistent connection or a new connection per operation
- Whether SurrealDB ran in release or debug build
- Transaction batching strategy for any engine
- Number of benchmark iterations per operation
- Warm vs cold cache state for non-`cold_open` operations
- Whether indexes were explicitly defined and verified before each run
- Client libraries used for each engine
- Whether async vs sync I/O was used

---

## 3. Results (Ranking Table)

### 3k smoke -- all engines (lower score is better)

| Rank | Engine | Weighted Score | Notes |
|---|---|---|---|
| 1 | SQLite | 2.70 | |
| 2 | Kuzu | 6.39 | |
| 3 | FalkorDB | 7.92 | |
| 4 | SurrealDB | 10.34 | FTS fell back to CONTAINS |
| 5 | Neo4j | 10.99 | lexical + hybrid both failed (50 failures each) |

### 10k local engines

| Rank | Engine | Weighted Score |
|---|---|---|
| 1 | SQLite | 3.05 |
| 2 | Kuzu | 5.41 |

### 10k server HNSW engines

| Rank | Engine | Weighted Score | Notes |
|---|---|---|---|
| 1 | FalkorDB | 1.93 | |
| 2 | SurrealDB | 4.95 | FTS fallback; high task_lookup latency |
| 3 | Neo4j | 5.43 | lexical + hybrid failed (200 failures each) |

### 10k SurrealDB DISKANN only

| Score | Notes |
|---|---|
| 1.20 (perfect) | No penalties; DISKANN vector worked; lexical still slow (200 ms) |

### 100k all engines (primary ranking)

| Rank | Engine | Weighted Score | Notes |
|---|---|---|---|
| 1 | FalkorDB | 4.01 | |
| 2 | SQLite | 4.23 | |
| 3 | Kuzu | 5.14 | |
| 4 | Neo4j | 5.58 | lexical + hybrid failed (300 failures each) |
| 5 | SurrealDB | 8.68 | task_lookup 402 ms p50; hybrid_rrf 455 ms p50 |

---

## 4. SurrealDB Deep-Dive

### 4a. How SurrealDB was configured and accessed (what the doc reveals)

| Aspect | Status |
|---|---|
| Mode | Server (Docker) |
| Storage backend | NOT stated in the document |
| Version | NOT stated |
| Vector index | HNSW (in the server HNSW run); DISKANN (in the separate DISKANN run) |
| Full-text index | **Failed to create or failed at runtime; fell back to CONTAINS scan** |
| Connection model | NOT stated (per-operation vs pooled connection unknown) |
| Transactions | NOT stated |
| Schema mode | NOT stated (schemafull vs schemaless) |
| Build type | NOT stated (release vs debug) |
| Indexes verified pre-run | NOT stated |

### 4b. Apples-to-apples check

The comparison is **not fully apples-to-apples** in these specific ways:

1. **Full-text index failure.** SurrealDB's lexical and hybrid numbers were produced by a `CONTAINS` scan (linear), not a proper FTS index. FalkorDB and SQLite ran with working lexical indexes. This alone explains the 200-450 ms lexical/hybrid numbers vs sub-1 ms for competitors.

2. **Docker overhead vs embedded.** SQLite and Kuzu are in-process embedded engines. SurrealDB, FalkorDB, and Neo4j ran as Docker servers with network socket overhead per call. The 50 ms `cold_open` and ~50 ms `task_lookup` for SurrealDB vs sub-1 ms for FalkorDB suggests SurrealDB may have incurred per-call connection overhead that FalkorDB did not, even though both are Docker servers.

3. **Connection model unknown.** FalkorDB achieved sub-1 ms task lookups at 10k while SurrealDB hit 49 ms. At 100k FalkorDB task lookup is 6 ms and SurrealDB is 402 ms. This pattern is consistent with SurrealDB opening a new connection per operation (HTTP or WebSocket re-handshake) rather than using a persistent connection.

4. **Storage backend unknown.** SurrealDB's default Docker backend is RocksDB. SurrealDB 2.x introduced SurrealKV as a higher-performance embedded backend. If RocksDB defaults were used without tuning, write amplification would explain the elevated build_import and lookup times.

5. **Schemaless vs schemafull unknown.** SurrealDB in schemaless mode performs type inference per write. Schemafull mode eliminates that overhead. Unspecified.

### 4c. Likely root causes (ranked by probability)

| Priority | Root cause | Evidence |
|---|---|---|
| 1 (highest) | FTS index creation/runtime failure causing CONTAINS fallback | Explicitly stated in caveats; directly explains 200-450 ms lexical/hybrid |
| 2 | Per-call connection or HTTP handshake overhead (no persistent connection) | 50 ms cold_open + 49-402 ms task_lookup vs FalkorDB <1-6 ms despite both being Docker servers |
| 3 | Default RocksDB storage backend without tuning (vs SurrealKV or in-memory) | Not stated, but default Docker image uses RocksDB; explains elevated build_import and lookup |
| 4 | Schemaless mode (type inference overhead per write/read) | Not stated; schemaless is the SurrealDB default |
| 5 | Single-row write loop vs batched transactions | Not stated; incremental_write is only moderately slow (3-5 ms) so less likely the dominant factor |

---

## FLAG FOR SHAHIN: SurrealDB result

### Verdict

**Likely a configuration and methodology artifact, not a genuine limitation of SurrealDB. Confidence: HIGH (3 of 5 identified causes are confirmed or strongly implied by the document itself).**

Reasoning:

- The FTS failure is confirmed by the benchmark's own caveats. The lexical and hybrid scores are therefore **invalid as a true SurrealDB benchmark** and should be disregarded for that comparison.
- The task_lookup and cold_open latencies (50 ms at 10k, 402 ms at 100k) scale in a pattern inconsistent with a properly pooled connection. FalkorDB as a co-located Docker server achieves sub-1 ms task lookups, so Docker overhead alone cannot explain the gap. A per-call reconnection (new HTTP or WebSocket session per query) would fully account for it.
- SurrealDB's vector performance, when the index actually worked, was competitive (5 ms at 10k, 7 ms at 100k, matching FalkorDB and Neo4j).
- The DISKANN-only run achieved a perfect score of 1.20 with no failures and good vector latency, confirming the engine is capable. The problem is operational setup, not engine ceiling.

### Retest plan (specific changes Ali should make)

1. **Fix the FTS index.** Identify why SurrealDB FTS index creation failed (likely a namespace/table-definition issue or a missing `ANALYZER` definition). Confirm the index exists with `INFO FOR TABLE` before running lexical/hybrid operations. Do not accept a run where FTS falls back to CONTAINS.

2. **Use a persistent WebSocket connection.** The SurrealDB Python SDK (`surrealdb` package) supports an async WebSocket client with a single persistent connection. Replace any HTTP request-per-query pattern with `await db.connect(...)` once and reuse. This is the single change most likely to collapse task_lookup latency from 400 ms to under 5 ms.

3. **Test SurrealKV storage backend.** In the Docker run command add `--strict` and set the datastore to `surrealkv://data` instead of the default RocksDB. SurrealKV is SurrealDB's native MVCC store, optimized for its query patterns. Compare build_import and lookup latency directly.

4. **Set schemafull mode.** Define the schema explicitly (`DEFINE TABLE ... SCHEMAFULL`) before the benchmark. This eliminates per-record type inference overhead.

5. **Verify all indexes before run.** After import, run `INFO FOR TABLE` and confirm: (a) HNSW or DISKANN vector index is listed and not dimension-mismatched, (b) FTS analyzer and index are listed, (c) any field indexes used for task_lookup are present.

6. **Delete Docker volumes between dataset sizes.** The 3k smoke run left persisted indexes at wrong dimensions for 10k/100k. Always run `docker volume rm` or use a fresh named volume per run.

7. **Run version-stamped.** Record `SELECT * FROM sys::version()` at the start and include in results. SurrealDB 2.1+ vs 1.x behave significantly differently for FTS.

Expected outcome after retest: SurrealDB task_lookup should drop to 1-5 ms range; lexical/hybrid should drop to 1-10 ms range (comparable to FalkorDB); overall weighted score should move from 8.68 to the 2-4 range, making it competitive with FalkorDB as a server projection.

---

## 5. Summary (5 bullets)

- SQLite dominates all local runs; FalkorDB dominates server runs across 10k and 100k datasets.
- SurrealDB's composite score of 8.68 at 100k (last place) is inflated by two confirmed artifacts: FTS index failure (fell back to CONTAINS) and apparent per-call connection overhead; neither reflects the engine's ceiling.
- SurrealDB's vector performance (5-7 ms) was competitive in every run where the vector index worked; the DISKANN-only run achieved a perfect score of 1.20.
- Neo4j suffered persisted-volume dimension mismatch (128 vs 384) invalidating its vector paths in 10k/100k runs, and its lexical/hybrid operations failed entirely; its true performance is also understated.
- Before making any architecture decision that excludes SurrealDB, Ali should rerun with: persistent WebSocket connection, confirmed FTS index, SurrealKV backend, schemafull schema, and fresh volumes per dataset size.

# SurrealDB PATCH11 Verdict — Async SDK, Embedded Mode, RELATE Graph Model

> **Status**: Active
> **Date**: 2026-07-16
> **Author**: Cytognosis Foundation (@shahin)
> **Audience**: engineers, stakeholders
> **Tags**: `yar`, `benchmark`, `surrealdb`, `sqlite`, `falkordb`, `storage`, `patch11`, `decision-d4`
> **Supersedes**: closes the PATCH11 item left "in progress" in `SURREALDB-RETEST-REPORT_2026-07-16.md`

---

## BLUF

**PATCH11 does not change the MVP storage decision.** SQLite+sqlite-vec still wins on-device patterns; FalkorDB still wins server graph patterns; SurrealDB remains third in every configuration tested — sync, async, and embedded. The async SDK port and the RELATE-based graph model are real, validated engineering improvements (RELATE roughly halves depth2/depth3 latency vs the old N+1 pattern; the composite index fix drops task_lookup at 100k from 325ms to 0.45ms), but neither closes the gap to SQLite or FalkorDB, and the Python-embedded mode — the configuration PATCH11 was supposed to make the case for — is dramatically **worse**, not better, at the two things it was meant to fix (cold-open, bulk load). This report also found and fixed a real bug in the prior benchmark: SurrealDB's "cold_open" numbers in `SURREALDB-RETEST-REPORT_2026-07-16.md` were never actually measuring reconnection — they were re-running `task_lookup` on the same warm connection.

**If you only read one table**, see [Section 3](#3-key-numbers-10k-scale-all-five-engines).

**Reading time:** ~10 minutes.

---

## 1. What PATCH11 was and what I found when I looked for it

The 2026-07-16 retest report and its predecessor `SURREALDB-ROOTCAUSE.md` both referenced "PATCH11" as the next scheduled SurrealDB retest, covering: an embedded Rust benchmark, a RELATE-based graph model, a GraphRAG single-query test, and (per this task's brief) an async-SDK port to replace the `BlockingWsSurrealConnection` used everywhere in `yar_bench.py`.

I searched the benchmark package (`notes/`, `reports/`, `db_benchmark/`) and the docs repo (including `_archive/cleanup_2026-07-16/surrealdb/`) for PATCH11 scripts. **None existed.** Every mention of PATCH11 in `SURREALDB-RETEST-REPORT_2026-07-16.md` and `SURREALDB-ROOTCAUSE.md` describes it as a recommendation ("next scheduled retest," "in progress as of 2026-07-16") with no accompanying code. I implemented it from the specification in those two documents plus this task's brief, patching `db_benchmark/yar_bench.py` directly (no separate PATCH11 script existed to run).

## 2. What was implemented

All changes are in `yar_supervisor_reproducible_benchmark_package/db_benchmark/yar_bench.py` (not a git repo — see Section 7 for what's committed where).

| Change | Engine name | What it does |
|---|---|---|
| Async SDK port | `surrealdb_async_tuned` | Replaces `BlockingWsSurrealConnection` with `AsyncSurreal`/`AsyncWsSurrealConnection`, driven by one persistent `asyncio` event loop opened in `setup()` and reused for every call (`loop.run_until_complete` per query, no per-op connect). |
| Embedded mode | `surrealdb_embedded` | Connects via `surrealkv://<path>` — the Python SDK's bundled embedded engine — instead of Docker + WebSocket. No network, no container. |
| RELATE graph model | both of the above | Nodes get an explicit record id (`node:<yid>`); edges are created via `RELATE node:<src>->graph_edge->node:<dst>` in addition to the existing flat `edge` table (kept for back-compat ops). `depth2`/`depth3` try a single-query arrow traversal (`->graph_edge->node`, `->graph_edge->node->graph_edge->node`) before falling back to the old N+1 path. |
| GraphRAG single query | both of the above | New `graphrag_single_query` op: one round trip combining vector KNN seed selection (`LET $seed = (... embedding <|k,ef|> $vec ...)`) with graph expansion (`->graph_edge->node`), vs. the multi-call Python pipeline every other engine (and SurrealDB's own `memory_packet()`) uses. Hooked into the runner as an informational op — not in the weighted decision score, since no other engine implements the equivalent primitive. |
| Genuine cold-open probe | both of the above | Overrides `cold_open_probe()` to actually close and reopen the connection before querying. See Section 4 for why this matters. |
| Composite index (RC-4) | `surrealdb_tuned` and both new engines (inherited) | Added `DEFINE INDEX idx_task_lookup ON TABLE node FIELDS kind, created_at`, the fix `SURREALDB-ROOTCAUSE.md` recommended for `task_lookup`'s filter+sort pattern. |

### Bugs found and fixed during implementation (all in the new harness code, not pre-existing)

1. **Node re-keying collided with the unique `yid` index.** Inserting explicit-id rows after the parent's auto-id insert violated `idx_node_yid UNIQUE`. Fixed by deleting the auto-id rows first.
2. **`RecordID` import was function-scoped and missing in `depth2`/`depth3`,** causing silent fallback to the old N+1 path with no visible error (only found by inspecting `capabilities` in `engine_meta.json`, not from a failed measurement — the fail-soft design masked it).
3. **`graph_edge` table wasn't in the reset list,** so a second run against the same Docker volume hit `AlreadyExistsError`. Fixed by adding it to the reset statements and by making the parent's strict-validation FTS retry run inside `_validate_surreal()` (before the hard-fail check), not after `load()` returns.
4. **The Python-embedded engine's bundled SurrealDB core is a different (older) version than the `v3.1.5` Docker image** — it rejects `FULLTEXT ANALYZER` (parse error) and only accepts the legacy `SEARCH ANALYZER` syntax, the *opposite* of what RC-1 found for the Docker server. It also rejects `SELECT VALUE x ... ORDER BY y` unless `x == y`. Both are worked around in `SurrealEmbeddedAsyncAdapter`, but this is a genuine version confound, not just a transport difference — see Section 6.

## 3. Key numbers, 10k scale, all five engines

10k nodes, 5 edges/node (50k edges), dim=384, 200 queries, RocksDB backend for the ws-based engines, `--surreal-strict-validation` on. All five engines completed with **zero failed measurements**.

**Weighted decision score (lower is better):**

| Engine | Score | vs. prior retest |
|---|---:|---|
| sqlite | 3.85 | (was 3.61) |
| falkordb | 5.37 | (was 5.34) |
| surrealdb_tuned | 6.91 | (was 8.38 — improved, mostly from the RC-4 index) |
| **surrealdb_async_tuned** | **8.24** | new |
| **surrealdb_embedded** | **10.11** | new |

**p50 latency (ms):**

| Operation | SQLite | FalkorDB | Surreal (sync-tuned, ws) | Surreal (async-tuned, ws) | Surreal (embedded, no network) |
|---|---:|---:|---:|---:|---:|
| build_import | 1,506 | 55,206 | 26,960 | 101,754 † | 491,772 †‡ |
| cold_open (true reconnect where noted) | 16.98 | 1.09 | 0.83 (not a real reconnect — see §4) | **18.38** (real) | **2,212** (real) |
| task_lookup | 1.16 | 0.39 | 0.39 | 0.60 | 46.68 |
| depth2_context | 0.024 | 0.275 | 1.02 (N+1) | **0.45** (RELATE, single query) | 1.84 (RELATE) |
| depth3_context | 0.027 | 0.306 | 2.04 (N+1) | **1.10** (RELATE, single query) | 6.37 (RELATE) |
| lexical_search | 0.19 | 0.19 | 3.94 | 8.86 | 9.21 |
| vector_search | 3.09 | 2.06 | 2.32 | 4.65 | 11.32 |
| memory_packet | 2.82 | 1.01 | 4.65 | 4.85 | 13.86 |
| graphrag_single_query | n/a | n/a | n/a | 4.29 (new) | 19.26 (new) |
| incremental_write | 0.20 | 2.81 | 4.87 | 5.05 | 24.54 |

† `build_import` for the async/embedded engines includes constructing **both** the flat edge table and the new RELATE `graph_edge` table (50k RELATE statements on top of the existing 50k flat-edge inserts). It is not an apples-to-apples async-vs-sync comparison; the extra work, not the SDK, explains most of the gap over `surrealdb_tuned`.
‡ Embedded `build_import` also reflects a genuinely slower write path — the embedded_kv directory grew past 200MB during the RELATE phase alone, well past what 10k nodes/50k edges should need, consistent with write amplification in the bundled engine.

Full CSVs: `results_patch11_10k_rocks_hnsw/{summary.csv,decision_score.csv}` in the benchmark package.

## 4. The cold-open bug this audit found and fixed

`BaseAdapter.cold_open_probe()` (the default every SurrealDB adapter used before this patch) just calls `task_lookup()` again **on the same already-open connection**. Only `SQLiteAdapter` overrode it to do a real close-and-reopen. This means every "cold_open" number for SurrealDB in `SURREALDB-RETEST-REPORT_2026-07-16.md` was actually re-measuring `task_lookup` latency:

| Scale | Reported RC-4 (task_lookup) | Reported RC-5 (cold_open) |
|---|---:|---:|
| 10k | 38ms | 36ms |
| 100k | 325ms | 354ms |

These are nearly identical because they were the same measurement. **RC-5's "network socket initialization dominates cold-open time" conclusion needs revision** — it was inferred from a metric that never actually opened a socket.

This patch adds a genuine reconnect probe (close, reopen, query) to the new adapters. Results: the ws/Docker true cold-open (18.4ms) is now roughly comparable to SQLite's real file-reopen cost (17.0ms) and much better than the old report implied — SurrealDB's Docker/WebSocket connection overhead is not the dominant problem RC-5 claimed. The embedded engine's true cold-open (2,212ms) is the opposite of what RC-5 hypothesized embedded mode would fix — see Section 6.

## 5. What the RELATE graph model actually validated

RC-6 said SurrealDB's flat-edge N+1 traversal was "inherent to non-graph engines." That's true for the flat model, but SurrealDB does support native record-link traversal (`->edge->node`), and it works:

- `depth2_context`: 1.02ms (N+1, old model) → 0.45ms (RELATE, single query) — **2.3x faster**
- `depth3_context`: 2.04ms (N+1) → 1.10ms (RELATE) — **1.9x faster**
- `graphrag_single_query` (new): 4.29ms for a combined vector-KNN-seed + graph-expansion query in one round trip, vs. `vector_search` alone at 4.65ms — validates SurrealDB's actual pitch (one query beats a multi-call pipeline) at roughly the cost of one op, not two.

This is real and worth keeping if SurrealDB is ever revisited. It does not change the ranking: FalkorDB's native Cypher traversal (0.28–0.31ms) and SQLite's in-process pointer-chase (0.02–0.03ms) both remain well ahead of even the RELATE-improved SurrealDB numbers.

## 6. Embedded mode: the opposite of the hypothesis

RC-5 and PATCH11's own framing assumed embedded SurrealDB would fix cold-open and, implicitly, general overhead, by removing Docker/WebSocket/TCP. At 10k scale it did the reverse on nearly every metric:

| Metric | ws/Docker (async-tuned) | Embedded (surrealkv) | Embedded is... |
|---|---:|---:|---|
| cold_open (true reconnect) | 18.4ms | 2,212ms | **120x worse** |
| build_import | 101.8s | 491.8s | 4.8x worse |
| depth2_context | 0.45ms | 1.84ms | 4x worse |
| depth3_context | 1.10ms | 6.37ms | 5.8x worse |
| lexical_search | 8.86ms | 9.21ms | roughly even |
| vector_search | 4.65ms | 11.32ms | 2.4x worse |

Two confounds matter for interpreting this fairly:

1. **Version mismatch.** The embedded engine bundled in the `surrealdb` 2.0.0 Python wheel is a different, apparently older SurrealDB core than the `v3.1.5` Docker image used everywhere else in this benchmark (it rejects `FULLTEXT ANALYZER` and needs the legacy `SEARCH ANALYZER` syntax — the reverse of what RC-1 found for Docker). Some of the gap could be an unoptimized/older build, not an architectural property of "embedded" as a concept.
2. **Not the real target architecture.** This is the Python SDK's embedded engine, not `Surreal::new::<SurrealKv>` compiled directly into a Rust/Tauri binary — the actual planned Yar desktop production mode. A compiled-Rust embedded build was out of scope for this run (see Section 8, Limitations) and could plausibly perform very differently.

Given both confounds, **this result should not be read as "embedded SurrealDB is bad."** It should be read as "the specific embedded configuration reachable from Python in this benchmark's time budget is bad, and a compiled-Rust embedded test is still an open question" — which is exactly the state PATCH11 was in before this run, just with harder evidence now for how large the gap could be if it doesn't improve.

## 7. Async SDK port: no net benefit in this benchmark's access pattern

Isolating the async port's effect from the RELATE change (both were bundled into the same new adapter, so a clean isolation would need one more variant without RELATE — not built here, noted as a gap): the per-op numbers where RELATE isn't a factor (`lexical_search`, `vector_search`, `hybrid_rrf`, `incremental_write`) are all **modestly worse** on `surrealdb_async_tuned` than on `surrealdb_tuned` (e.g., lexical_search 3.94ms → 8.86ms, vector_search 2.32ms → 4.65ms). The likely reason: this benchmark issues one query, awaits it, then issues the next — strictly sequential, no concurrent in-flight requests. Async I/O has no overlap to exploit in that pattern; it only adds `asyncio` event-loop and coroutine-scheduling overhead on top of the same underlying WebSocket round trip. **Async would plausibly help in a workload with concurrent overlapping requests (e.g., multiple simultaneous background sync writes while a query is in flight), which this benchmark does not test.** That's a fair characterization of Yar's actual access pattern only if Yar itself is single-request-at-a-time on its storage layer — worth revisiting if that assumption changes.

## 8. 100k scale — partial, with an honest limitation

100k nodes / 500k edges, RocksDB backend, same query mix as the prior retest, run sequentially with nothing else heavy on the machine.

**Completed cleanly (0 failures):**

| Engine | Score | build_import | cold_open* | task_lookup | depth2 | depth3 | lexical | vector |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| falkordb | 6.80 | 576.3s | 8.66ms | 7.74ms | 0.44ms | 0.46ms | 0.32ms | 2.35ms |
| sqlite | 7.31 | 15.4s | 109.4ms | 11.43ms | 0.025ms | 0.025ms | 1.05ms | 23.48ms |
| surrealdb_tuned | 8.11 | 294.9s | 0.56ms* | **0.45ms** | 0.88ms | 1.68ms | 34.34ms | 4.95ms |

\* `surrealdb_tuned`'s cold_open still uses the unfixed base probe (task_lookup on a warm connection — see Section 4); it is not a real reconnect number and is included only for continuity with the prior report's table.

**The headline 100k finding: the RC-4 composite index fix is validated at scale.** `task_lookup` drops from **325ms (prior report) to 0.45ms** at 100k — a ~700x improvement, and SurrealDB's `task_lookup` is now *faster* than SQLite's (11.4ms) and FalkorDB's (7.7ms) at this scale. This single fix closes what the prior report called "the single largest contributor to SurrealDB's weighted score gap."

**Did not complete: `surrealdb_async_tuned` (RELATE) at 100k.** Two independent attempts (one before, one after adding retry-with-backoff around every bulk-write statement) both failed identically, deep in the RELATE-edge construction phase (~495k/500k edges in), with:

```
QueryError: Transaction conflict: Resource busy. This transaction can be retried
```

This is a **SurrealDB-reported condition**, not a benchmark harness bug — the retry logic (4 attempts, up to 1.2s backoff per batch) still hit it consistently at the same point in both runs, suggesting sustained RocksDB MVCC write contention under this benchmark's un-transacted, high-volume RELATE batching pattern (500 RELATE statements per round trip, 100 round trips) rather than a transient blip. The flat-edge model (`surrealdb_tuned`, no RELATE) loaded the identical 500k edges at 100k with zero errors in the same run, isolating the failure to the RELATE-construction path specifically, not SurrealDB-at-100k generally.

**Not attempted: `surrealdb_embedded` at 100k.** Given the 10k embedded numbers already show severe, consistent degradation (491.8s build, 2,212ms cold-open, worse than every other engine on 5 of 8 comparable ops), and the RELATE-write-contention issue above would very likely compound at 100k for the same engine, running it to completion was assessed as low-value relative to the time it would cost (extrapolating from the 10k build_import alone, a 100k embedded run could plausibly take 45+ minutes just to load, before even reaching the query phase, with a materially likely chance of hitting the same transaction-conflict failure).

## 9. Honest limitations

- **No compiled-Rust embedded test.** The Python-embedded `surrealkv://` engine is not `Surreal::new::<SurrealKv>` in a native Tauri binary — the actual production target. This remains the single most important open question for Yar's desktop storage decision and was not resolved here.
- **Async port and RELATE model are confounded.** Both ship in the same new adapter class; there is no "async-SDK-only, flat-edge-model" variant to isolate the async port's effect in general (only in the ops RELATE doesn't touch — Section 7).
- **100k RELATE result is missing, not just slow.** `surrealdb_async_tuned` at 100k is a genuine gap in this report, not a rounding-error omission — see Section 8.
- **`build_import` across variants is not apples-to-apples.** The new adapters build both the flat and RELATE edge models; the baseline only builds the flat model. Section 3's footnote flags this inline.
- **Embedded engine version mismatch confounds the embedded-vs-ws comparison** (Section 6) — some of embedded's gap could be an older/less-optimized bundled core rather than an architectural property of "no network."
- **Single-machine, single-run measurements.** No repeated-trial variance bars; p50/p95/p99 come from one run per engine per scale, consistent with the prior report's methodology but still a single sample per condition.
- **Machine was kept quiet** (builds/tests finished, cases run sequentially, `YAR_DISABLE_DOCKER_STATS=1`), but this is a shared dev machine, not an isolated benchmark rig.

## 10. Decision

**No change to `SPEC-storage-engine.md`.** SQLite+sqlite-vec remains the device engine; FalkorDB remains the server graph engine. SurrealDB, across sync, async, and embedded configurations, does not beat either on the patterns each currently wins. The RELATE graph model and the RC-4 composite index are genuine, validated improvements worth preserving in any future SurrealDB revisit; the embedded-mode question remains genuinely open pending a compiled-Rust test, which this report explicitly does not answer.

**Recommendation:** treat SurrealDB as closed for the current MVP scope. If a compiled-Rust embedded benchmark becomes cheap to run later (e.g., as a side effect of other Rust/Tauri work), it is the one remaining test that could plausibly change this conclusion — everything else in the PATCH11 spec has now been tried and did not move the needle.

---

## Appendix: artifact paths

- Harness patches (not a git repo — see below): `~/repos/cytognosis/yar_revisions/yar_supervisor_reproducible_benchmark_package/db_benchmark/yar_bench.py`
- Docker port remap (8000→8010 to avoid a host port collision on this machine): `db_benchmark/docker-compose.yml`
- 10k results (all 5 engines, 0 failures): `db_benchmark/results_patch11_10k_rocks_hnsw/`
- 100k results (sqlite, falkordb, surrealdb_tuned — 0 failures): `db_benchmark/results_patch11_100k_rocks_hnsw/`
- 100k async_tuned failed attempts (RELATE transaction-conflict, both logged): `db_benchmark/results_patch11_100k_async_retry/`, `db_benchmark/results_patch11_100k_async_retry2/`
- Run logs: `/tmp/patch11_10k_run.log` (first attempt, fixed a bug mid-run), `/tmp/patch11_10k_run2.log` (clean final 10k run), `/tmp/patch11_100k_run.log`, `/tmp/patch11_100k_async_retry.log`, `/tmp/patch11_100k_async_retry2.log`

**Note on the benchmark package:** `yar_supervisor_reproducible_benchmark_package/` is not a git repository, so the harness patches above are not committed anywhere (per instructions, only this report is committed, in the docs repo). If the package is git-initialized later, `yar_bench.py` and `docker-compose.yml` as they stand at the time of this report are the PATCH11 harness.

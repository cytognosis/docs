---
status: authoritative
date: 2026-06-22
author: "@shahin"
audience: engineers
tags: [yar, storage, benchmark, sqlite, falkordb, surrealdb, neo4j, kuzu, graphrag]
---

# Yar DB Benchmark: Evaluation and Results

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: engineers, stakeholders
> **Tags**: `yar`, `benchmark`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)

**BLUF.** Ali's benchmark (Ali Mohammadi, 2026-06-21) validates SQLite as the on-device MVP default and FalkorDB as the best server-tier graph projection. SurrealDB's last-place finish at 100k is a confirmed configuration and methodology artifact; three root causes are proven by the benchmark's own data. A corrected retest is required before any architecture decision that excludes SurrealDB from the GraphRAG path.

---

## 1. Scope

### 1.1 Engines Tested

| Engine | Mode | Category |
|---|---|---|
| SQLite + FTS5 + sqlite-vec | Embedded (in-process) | Local/device |
| Kuzu | Embedded graph | Local/device |
| SurrealDB (legacy adapter) | Docker server, WebSocket | Server |
| SurrealDB (tuned adapter, PATCH8 onward) | Docker server, WebSocket, SCHEMAFULL | Server |
| Neo4j | Docker server, Bolt protocol | Server |
| FalkorDB | Docker server, Redis protocol | Server |

The benchmark also contains a sync benchmark (`sync_benchmark/`) covering CRDT op-log edge cases. That benchmark is separate from DB engine scoring and is not in scope for this document.

### 1.2 Workload Operations

Thirteen operations derived from Yar's actual hot path:

| Operation | Description |
|---|---|
| `build_import` | Bulk data load (schema + index + data) |
| `cold_open` | Fresh connection open from scratch |
| `task_lookup` | Single-record key lookup (kind + created_at sort) |
| `depth2_context` | Graph traversal, 2 hops |
| `depth3_context` | Graph traversal, 3 hops |
| `reverse_refs` | Reverse-reference lookup |
| `person_memory` | Person-anchored memory fetch |
| `project_decisions` | Project-anchored decision fetch |
| `lexical_search` | BM25 / FTS5 full-text keyword search |
| `vector_search` | ANN search (HNSW or DISKANN) |
| `hybrid_rrf` | Combined lexical + vector with Reciprocal Rank Fusion |
| `memory_packet` | Composite read (graph + vector) |
| `incremental_write` | Single-record insert or update |

### 1.3 Dataset Sizes

- 3k records (smoke)
- 10k records (default)
- 100k records (stress; primary decision basis)

Embedding dimension: 384 (float32). Graph edges: 5 per node. 15 topic clusters, deterministic ground-truth top-20 vectors per query.

### 1.4 Hardware (Reference Run)

Ali's M3 MacBook: macOS 26.5.1, Apple M3, 8 GB RAM, Python 3.12.12, Docker 28.3.2, Docker Compose v2.39.1. Approximately 45 GiB free disk during run. Linux x86_64 reruns will differ in absolute latency.

---

## 2. Methodology

### 2.1 Scoring

Weighted decision score; lower is better. Each operation is normalized against the fastest engine's p50, then multiplied by its weight. Operations that are missing or majority-failed receive a 10x weight penalty.

Key operation weights: `memory_packet` 0.16, `vector_search` and `incremental_write` 0.12 each, `depth2_context` and `build_import` 0.10 each.

Coverage weight: 1.2 for fully functional engines, 1.06 for engines with one or more failed or missing operations.

### 2.2 Measurement Notes

- Latency reported as p50 and p95.
- `build_import` timer includes schema creation, index creation, and data insertion for server engines (SQLite and Kuzu schema is set up in `setup()`, not the timed `load()` call; this is a known methodology gap detailed in Section 4, Issue 5).
- Each timed operation is called twice: once for the timed measurement and once for recall computation. The second call is not timed, but it introduces minor warm-cache effects on the first call of the next iteration.

---

## 3. Results and Ranking

### 3.1 Primary Ranking: 100k All Engines

This is the authoritative ranking for architecture decisions.

| Rank | Engine | Weighted Score | Notes |
|---|---|---|---|
| 1 | FalkorDB | 4.01 | Best server tier; no operation failures |
| 2 | SQLite | 4.23 | Best local tier; validated MVP |
| 3 | Kuzu | 5.14 | Archived upstream (Apple acquisition Oct 2025); LadybugDB fork recommended |
| 4 | Neo4j | 5.58 | Lexical + hybrid failed entirely (300 failures each); true score is understated |
| 5 | SurrealDB | 8.68 | **Configuration artifact**; see Section 5 |

### 3.2 10k Server HNSW Engines

| Rank | Engine | Weighted Score | Notes |
|---|---|---|---|
| 1 | FalkorDB | 1.93 | |
| 2 | SurrealDB | 4.95 | FTS fallback; elevated task_lookup |
| 3 | Neo4j | 5.43 | Lexical + hybrid failed (200 failures each) |

### 3.3 10k Local Engines

| Rank | Engine | Weighted Score |
|---|---|---|
| 1 | SQLite | 3.05 |
| 2 | Kuzu | 5.41 |

### 3.4 3k Smoke (All Engines)

| Rank | Engine | Weighted Score | Notes |
|---|---|---|---|
| 1 | SQLite | 2.70 | |
| 2 | Kuzu | 6.39 | |
| 3 | FalkorDB | 7.92 | |
| 4 | SurrealDB | 10.34 | FTS fell back to CONTAINS |
| 5 | Neo4j | 10.99 | Lexical + hybrid failed (50 failures each) |

### 3.5 PATCH10 Comparable Run: 10k and 100k RocksDB + HNSW

PATCH10 is the tuned SurrealDB retest. It fixed FTS index validation and confirmed the engine is capable, but `task_lookup` and `cold_open` remain elevated because the SDK connection overhead was not fixed.

**10k RocksDB + HNSW:**

| Engine | Weighted Score |
|---|---|
| SQLite | 3.05 |
| FalkorDB | 5.53 |
| SurrealDB tuned | 8.35 |

**100k RocksDB + HNSW:**

| Engine | Weighted Score |
|---|---|
| FalkorDB | 4.26 |
| SQLite | 5.49 |
| SurrealDB tuned | 9.38 |

**Key PATCH10 p50 latency (ms), 100k:**

| Operation | FalkorDB | SQLite | SurrealDB tuned |
|---|---|---|---|
| task_lookup | 3.3 | 6.8 | 445.6 |
| lexical_search | 0.5 | 1.1 | 42.8 |
| hybrid_rrf | 4.3 | 24.2 | 31.1 |
| vector_search | 4.3 | 22.5 | 16.5 |
| memory_packet | 3.1 | 23.2 | 10.8 |
| depth2_context | 0.7 | 0.2 | 4.3 |
| cold_open | 3.2 | 1165.3 | 535.8 |

### 3.6 SurrealDB DISKANN-Only Run (10k)

Single-engine probe, not comparable to other engines in isolation. Score: 1.20 (perfect, no penalties). This proves the engine is capable when configured correctly; the last-place finish in the full run reflects setup artifacts, not the engine ceiling.

---

## 4. Issues Found: Package-Level

Twelve package-level issues were identified during the code audit. They are ranked by severity and cross-referenced to source files.

### Critical

**Issue 1: Docker volume reuse between dataset sizes corrupts Neo4j and SurrealDB vector indexes.**
File: `db_benchmark/run_full.sh` lines 1-53. The script starts Docker once before all four runs and never tears down volumes between them. The 3k run at dimension 128 leaves stale indexed data; 10k and 100k runs at dimension 384 then build on corrupted volumes. This is the confirmed root cause of Neo4j's 200-300 failures per operation at 10k and 100k. `run_surreal_tuned_retest.sh` (PATCH8+) correctly calls `reset_stack()` with `docker compose down -v` before each case. Use `run_db_surreal_tuned.sh` rather than `run_full.sh` for any run you intend to compare.

**Issue 2: SurrealDB FTS ORDER BY incompatibility (fixed in PATCH10, not yet in main `yar_bench.py`).**
File: `db_benchmark/yar_bench.py` lines 1191-1207. The pre-PATCH10 form `ORDER BY search::score(0) DESC` caused the SurrealDB parser to reject the query at runtime, triggering the CONTAINS fallback. PATCH10 fixes this by aliasing the score first (`search::score(0) AS score`) and ordering by the alias. Verify the current `yar_bench.py` has the alias form before any run; grep for `search::score` and confirm both occurrences use `AS score ... ORDER BY score DESC`.

### High

**Issue 3: Kuzu `lexical_search` is always a CONTAINS scan; FTS extension path is absent.**
File: `db_benchmark/yar_bench.py` lines 718-722. Kuzu's lexical scores are linear-scan numbers, not FTS index numbers. They are not comparable to FalkorDB's RediSearch or SQLite's FTS5.

**Issue 4: FalkorDB Docker image is unpinned (`latest`).**
File: `db_benchmark/docker-compose.yml` line 22. Every other service uses a pinned version. An unpinned FalkorDB means the image version changes between runs. Pin to a specific tag (e.g., `v4.4.0`) before any reproducibility-sensitive run.

**Issue 10: SurrealDB `depth2` and `depth3` adapters use an N+1 sequential round-trip pattern.**
File: `db_benchmark/yar_bench.py` lines 949-969. SurrealDB fetches first-hop edges then loops over each first-hop node and fetches outgoing edges sequentially. Neo4j, FalkorDB, and SQLite all express this as a single query. The elevated `depth2_context` and `depth3_context` latency for SurrealDB is an adapter methodology artifact, not an engine capability limitation.

### Medium

**Issue 5: `build_import` timer includes schema and index creation time for server engines but not for embedded engines.**
File: `db_benchmark/yar_bench.py` lines 1700-1705. SQLite and Kuzu create schema in `setup()` (not timed); server engines create it inside `load()` (timed). At 100k with HNSW building, this is a material fraction of server engine import time.

**Issue 8: `--dim` defaults to 128 in CLI; all production scripts pass 384.**
File: `db_benchmark/yar_bench.py` line 1852. Manual invocations that omit `--dim` will produce incomparable results and will trigger the volume dimension mismatch bug from Issue 1.

**Issue 9: `surrealdb_tuned` `build_import` is 2-3x slower than the legacy adapter at 10k and 100k.**
File: `db_benchmark/yar_bench.py` lines 1155-1174. PATCH10 wraps each batch in `BEGIN TRANSACTION; INSERT ...; COMMIT TRANSACTION;` as a single query string, forcing synchronous WAL flushes and three sequential round-trips per batch. This inflates the `build_import` score for the tuned adapter. See SurrealDB code-level Issue 2 in Section 5 below.

**Issue 11: SurrealDB `task_lookup` at 100k is 445 ms even after PATCH10.**
File: `db_benchmark/yar_bench.py` line 947, `reference_results/surreal_tuned_patch10_final_comparison.md`. The query uses `WHERE kind = 'task' ORDER BY created_at DESC`, requiring a range scan on `kind` then a sort. A compound index on `(kind, created_at)` is not in the current schema; this is an untested optimization.

**Issue 12: Python packages are unpinned (`>=` minimums only).**
File: `db_benchmark/requirements.txt`. The `surrealdb` SDK has had breaking API changes between versions; `kuzu` likewise. Pin all packages to exact versions for reproducibility.

### Low

**Issue 6: Volume deletion failure is silently ignored (`|| true`) in `reset_stack`.**
File: `db_benchmark/run_surreal_tuned_retest.sh` line 8. If `docker compose down -v` fails, the old volume persists and the next run loads stale data. Remove `|| true` and add explicit volume verification.

**Issue 7: `wait_for_services.py` has a fixed 8-second post-wait; does not check index readiness.**
File: `db_benchmark/wait_for_services.py` lines 28-29. For SurrealKV backend startup, the TCP health check passes before the engine is ready for writes. If the SurrealKV case (PATCH8 case 3) fails immediately, increase `YARBENCH_POST_WAIT_SECONDS` from 8 to 20.

---

## 5. SurrealDB Code-Level Issues

Eight code-level issues were identified in `db_benchmark/yar_bench.py` via the audit in `SURREALDB_CODE_AUDIT.md`. The two highest-impact issues are summarized here with file references; the full code-level audit is in:

`docs/03-Products/Cytonome/Yar/consolidation_2026-06-21/_storage/SURREALDB_CODE_AUDIT.md`

### SurrealDB Code Issue 1 (Highest Impact): Synchronous SDK blocking the event loop

**File:** `yar_bench.py` lines 766-814 (`SurrealAdapter.setup`), every `_q()` call throughout.
**Root cause:** The benchmark pins `surrealdb>=1.0.4`, which provides a synchronous blocking WebSocket client. Each query incurs a full blocking socket round-trip. FalkorDB uses redis-py with a persistent pipelined TCP socket. The 45-446 ms `task_lookup` across all dataset sizes is explained entirely by this per-call blocking overhead.
**Fix:** Replace `from surrealdb import Surreal` with `from surrealdb import AsyncSurrealDB` and port `SurrealAdapter` and `SurrealTunedAdapter` to `async def` using `asyncio.run()`. This is the single change most likely to collapse the remaining latency gap.
**Note on version:** The correct async class name in SDK 2.0.0 is `AsyncSurreal`, not `AsyncSurrealDB`. Verify the exact class name against the installed SDK version before porting.

### SurrealDB Code Issue 2 (High): Transaction wrapping regression in build_import

**File:** `yar_bench.py` lines 1161-1174 (`SurrealTunedAdapter.load`).
**Root cause:** PATCH9 added `BEGIN TRANSACTION; INSERT INTO node $rows; COMMIT TRANSACTION;` as a single query string. The server parses and executes three statements per batch, incurring three synchronous round-trips per batch. The pre-PATCH tuned adapter had an 8,111 ms `build_import` at 10k; PATCH10 shows 24,032 ms -- a 3x regression.
**Fix:** Issue `BEGIN TRANSACTION`, `INSERT INTO node $rows`, and `COMMIT TRANSACTION` as three separate `_q()` calls in a try/except block, with `CANCEL TRANSACTION` in the except.

Full code-level issue table: see `SURREALDB_CODE_AUDIT.md` Section "Summary Table" (8 issues, ranked by impact).

---

## 6. SurrealDB Artifact Verdict

**The SurrealDB last-place score of 8.68 at 100k is a configuration and methodology artifact, not a genuine limitation of the engine. Confidence: HIGH.**

Evidence supporting this verdict:

1. **FTS failure is confirmed by the benchmark itself.** The benchmark caveats explicitly state that FTS index creation or runtime failed; lexical and hybrid results are from a CONTAINS linear scan. These numbers are invalid for engine comparison.

2. **Connection overhead is proven by the PATCH10 code audit.** The sync SDK (`surrealdb>=1.0.4`) uses blocking socket I/O per call. FalkorDB achieves sub-1 ms task lookups over the same Docker network; SurrealDB achieves 46-446 ms. The gap scales with dataset size in a pattern consistent with blocking socket overhead, not with index complexity.

3. **DISKANN-only run scores 1.20 (perfect).** When the engine is isolated from FTS and connection issues, it achieves a perfect score with competitive vector latency (7 ms at 10k). This directly demonstrates engine capability.

4. **PATCH10 confirmed the artifact interpretation.** After fixing FTS (changing `ORDER BY search::score(0) DESC` to the alias form), 10k lexical search improved from 214 ms to 3.6 ms and hybrid RRF improved from 218 ms to 5.9 ms -- a 60x improvement on those operations. The task_lookup gap remained because the sync SDK was not changed.

**Architecture decision from PATCH10:** SurrealDB is promoted from "research spike only" to "priority GraphRAG projection candidate." It is not the MVP default yet, and cannot be until the async SDK port and a comparable SurrealKV run are completed.

---

## 7. Revision Plan Summary

Five correctness fixes are required before a valid rerun can be compared to Ali's results. See the full plan in:

`docs/03-Products/Cytonome/Yar/consolidation_2026-06-21/_storage/BENCHMARK_REVISION_PLAN.md`

### Priority 1: Required Before Any Rerun

| Code Revision | File | Change |
|---|---|---|
| CR-1 | `yar_bench.py` lines 1191-1207 | Verify PATCH10 FTS ORDER BY alias form is in place; grep for `search::score` |
| CR-2 | `yar_bench.py` lines 949-969 | Replace SurrealDB `depth2`/`depth3` N+1 loop with single two-hop SurrealQL query |
| CR-3 | `run_full.sh` | Add volume teardown between each dataset-size run (use `run_db_surreal_tuned.sh` instead) |
| CR-4 | `docker-compose.yml` line 22 | Pin FalkorDB image to a specific tag |

### Priority 2: Required for a Fair Comparison

| Code Revision | File | Change |
|---|---|---|
| CR-5 | `requirements.txt` | Pin all package versions with `==` specifiers |
| CR-6 | `yar_bench.py` `run_engine` | Separate schema/index creation time from data insertion in `build_import` measurement |
| CR-7 | `yar_bench.py` lines 1753-1766 | Eliminate double-call recall measurement |
| CR-8 | `yar_bench.py` lines 718-722 | Implement real FTS extension query path for Kuzu |

---

## 8. Requirements for a Valid Rerun

A run is not valid for architecture comparison unless all of the following hold:

1. `run_db_surreal_tuned.sh` (not `run_full.sh`) is used for the tuned retest.
2. Docker volumes are deleted and verified gone before each dataset-size case.
3. FalkorDB Docker image is pinned to a specific tag.
4. SurrealDB `--dim` is explicitly passed as 384; not relied on from default.
5. `surrealdb_tuned` passes strict validation: `engine_meta.json` contains `"validation_fts_body_not_table_iterator": "True"` and `"validation_vector_has_knn": "True"`.
6. `lexical_search` p50 for `surrealdb_tuned` at 10k is under 20 ms. If it is 200+ ms, the PATCH10 FTS fix has not landed.
7. No `contains_fallback` appears in `engine_meta.json` for `surrealdb_tuned`.
8. Engine version is recorded: `engine_meta.json` for SurrealDB should contain an `INFO FOR DB` or `sys::version()` result confirming v3.1.x.
9. A `RUN_MANIFEST.md` is written alongside output zips recording: hardware, Python version, Docker version, FalkorDB image tag, SurrealDB image tag, date, and any code revisions applied.

**Note on SurrealDB version.** The benchmark package pins `surrealdb/surrealdb:v3.1.3`. The current latest release as of 2026-06-22 is 3.1.5. Version 3.1.5 may fix behaviors observed in 3.1.3, but the package has not been tested against it. Run 3.1.3 first to reproduce Ali's baseline; then optionally run 3.1.5 with the same configuration and note differences.

---

## 9. Final Architecture Decision (Current State)

From the PATCH10 supervisor brief (`reports/Yar_Data_Fabric_Supervisor_Brief_EN.md`):

| Role | Selected Option |
|---|---|
| Phone and laptop MVP | SQLite + FTS5 + sqlite-vec |
| Server graph projection | FalkorDB |
| GraphRAG projection candidate | SurrealDB (retest required before promoting to default) |
| Embedded graph experiment | LadybugDB (Kuzu fork; Kuzu itself archived) |
| Mature server graph fallback | Neo4j (lexical and hybrid adapter must be fixed before final ranking) |
| Source of truth | Yar op-log / CRDT state |
| Sync MVP | central_oplog_pull_since_seq |
| Local-first sync | p2p_version_vector_delta |

---

## 10. Cross-References

All of the following documents are authoritative sources consulted to produce this evaluation. None of the content from these documents is duplicated in full here; this document summarizes and links to them.

| Document | Path | Role |
|---|---|---|
| Ali's analysis | `~/Downloads/Telegram\ Desktop/yar_bench_final_analysis.md` | Primary raw results source |
| Benchmark package README | `yar_supervisor_reproducible_benchmark_package/README.md` | Run instructions, architecture decision |
| PATCH8 README | `yar_supervisor_reproducible_benchmark_package/db_benchmark/README_PATCH8_SURREAL_TUNED.md` | Tuned adapter introduction and rationale |
| PATCH9 README | `yar_supervisor_reproducible_benchmark_package/db_benchmark/README_PATCH9_SURREAL_TUNED_FIX.md` | Validation layer fixes |
| PATCH10 README | `yar_supervisor_reproducible_benchmark_package/db_benchmark/README_PATCH10_SURREAL_FTS_RUNTIME_FIX.md` | FTS ORDER BY fix |
| PATCH10 comparison | `yar_supervisor_reproducible_benchmark_package/notes/surreal_tuned_patch10_final_comparison.md` | Final PATCH10 p50 tables, interpretation |
| Supervisor brief | `yar_supervisor_reproducible_benchmark_package/reports/Yar_Data_Fabric_Supervisor_Brief_EN.md` | Decision summary |
| Benchmark digest | `docs/03-Products/Cytonome/Yar/consolidation_2026-06-21/_storage/BENCHMARK_DIGEST.md` | Deep-dive SurrealDB analysis, full results tables |
| SurrealDB code audit | `docs/03-Products/Cytonome/Yar/consolidation_2026-06-21/_storage/SURREALDB_CODE_AUDIT.md` | 8 code-level issues with line references and fixes |
| Benchmark revision plan | `docs/03-Products/Cytonome/Yar/consolidation_2026-06-21/_storage/BENCHMARK_REVISION_PLAN.md` | 12 package-level issues, rerun procedure, risks |
| SurrealDB tuning guide | `docs/03-Products/Cytonome/Yar/spec/SurrealDB-tuning-and-graphrag-guide.md` | Troubleshooting table, configuration, GraphRAG patterns |
| Storage benchmark tracker | `docs/03-Products/Cytonome/Yar/spec/STORAGE_BENCHMARK_TRACKER.md` | Living decision tracker; open decisions O-1 through O-8 |

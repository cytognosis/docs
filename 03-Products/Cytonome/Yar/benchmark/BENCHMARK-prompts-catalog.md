---
status: authoritative
date: 2026-06-22
author: "@shahin"
audience: engineers
tags: [yar, storage, benchmark, prompts, ai, catalog, surrealdb]
---

# Yar DB Benchmark: Prompts Catalog

**BLUF.** The benchmark package contains no embedded LLM prompts in code. All LLM-driven work was done through conversational sessions (Claude); the artifacts produced by those sessions are the benchmark analysis docs and code audit docs. Three categories of prompts are identified below: conversational prompts Shahin gave to produce the analysis docs, run instructions Ali received, and prompts needed for the next phase. The prompt history is partially reconstructed from context; original session transcripts are not preserved.

---

## 1. Prompts Found in the Package

A full-text search for LLM-related patterns across all `.py`, `.sh`, `.md`, and `.txt` files in `yar_supervisor_reproducible_benchmark_package/` found zero embedded LLM prompts.

**No LLM prompt strings, chat-completion calls, Claude/OpenAI API calls, or prompt templates exist inside the benchmark code package.** The benchmark is a pure Python + Docker + shell harness; it measures database engines and does not call any language model.

---

## 2. Run and Patch Prompts: Instructions Ali Used

These are the prompts Ali (the operator) received to run each benchmark patch. They are reconstructed from the PATCH README files in the package. All are located in `yar_supervisor_reproducible_benchmark_package/db_benchmark/`.

### Prompt A1: Initial Benchmark Run (pre-PATCH8)

**Location:** Reconstructed; original message not preserved.
**Purpose:** Ali ran the initial untuned benchmark using `run_full.sh` and returned `yar_bench_slim_results.zip`.
**Status:** Do not reuse. This run had the volume contamination bug (Issue 1 in BENCHMARK-evaluation-and-results.md) and the untuned SurrealDB adapter.

---

### Prompt A2: PATCH8 Tuned Retest

**Location:** `yar_supervisor_reproducible_benchmark_package/db_benchmark/README_PATCH8_SURREAL_TUNED.md`

Full text of the run instructions:

```
cd ~/Downloads
unzip -o yar_db_eval_suite_PATCH8_SURREAL_TUNED.zip
cd yar_db_eval_suite_PATCH8_SURREAL_TUNED
python3.12 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
./run_surreal_tuned_retest.sh
./collect_tuned_results.sh
```

Return: `yar_surreal_tuned_results_slim.zip` and `SURREAL_TUNED_COMPARISON.md`.

**Purpose:** Run the new `surrealdb_tuned` adapter with SCHEMAFULL, validated FTS/vector indexes, fresh volumes, and persistent connection.
**Status:** Superseded by PATCH9 (the PATCH8 run failed because the validation layer had SurrealQL version issues). Do not use PATCH8 as a baseline.

---

### Prompt A3: PATCH9 Validation Fix

**Location:** `yar_supervisor_reproducible_benchmark_package/db_benchmark/README_PATCH9_SURREAL_TUNED_FIX.md`

Full text of run instructions:

```
cd ~/Downloads
unzip -o yar_db_eval_suite_PATCH9_SURREAL_TUNED_FIX.zip
cd yar_db_eval_suite_PATCH9_SURREAL_TUNED_FIX
python3.12 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
./run_surreal_tuned_retest.sh
./collect_tuned_results.sh
```

Return: `yar_surreal_tuned_results_slim.zip`.

**Purpose:** Fix three SurrealQL version issues that caused PATCH8 validation to fail: `INFO FOR TABLE` truncation, `EXPLAIN FULL` prefix syntax, and `sys::version()` rejection.
**Status:** Superseded by PATCH10. The PATCH9 run still had the FTS ORDER BY runtime failure; use PATCH10 as the baseline.

---

### Prompt A4: PATCH10 FTS Runtime Fix

**Location:** `yar_supervisor_reproducible_benchmark_package/db_benchmark/README_PATCH10_SURREAL_FTS_RUNTIME_FIX.md`

Full text of run instructions:

```
cd ~/Downloads
unzip -o yar_db_eval_suite_PATCH10_SURREAL_FTS_RUNTIME_FIX.zip
cd yar_db_eval_suite_PATCH10_SURREAL_FTS_RUNTIME_FIX
docker rm -f yar-surrealdb yar-falkordb yar-neo4j 2>/dev/null || true
docker compose down -v --remove-orphans 2>/dev/null || true
docker volume ls -q | grep -E 'yar_db_eval_suite|surreal|falkor|neo4j' | xargs -r docker volume rm 2>/dev/null || true
python3.12 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
./run_surreal_tuned_retest.sh
./collect_tuned_results.sh
ls -lh yar_surreal_tuned_results_slim.zip
unzip -l yar_surreal_tuned_results_slim.zip | head -80
```

Return: `yar_surreal_tuned_results_slim.zip`.

**Purpose:** Fix the runtime FTS query -- change `ORDER BY search::score(0) DESC` to the aliased form `search::score(0) AS score ... ORDER BY score DESC`. This was the final patch that produced valid FTS results.
**Status:** CANONICAL. PATCH10 is the baseline for all future comparisons. The `reference_results/yar_surreal_tuned_results_slim_PATCH10.zip` in the package contains Ali's PATCH10 results.

---

### Prompt A5: Full Reproduction Run

**Location:** `yar_supervisor_reproducible_benchmark_package/README.md` (Section "Full reproduction run")

```
chmod +x *.sh db_benchmark/*.sh sync_benchmark/*.sh
./run_full_reproduction.sh
```

**Purpose:** Full end-to-end reproduction including both DB and sync benchmarks. Intended for a supervisor who wants to reproduce all results.
**Status:** Do not use for SurrealDB-focused reruns; use `run_db_surreal_tuned.sh` instead to avoid the `run_full.sh` volume contamination bug.

---

## 3. Analysis Prompts: Claude Sessions Producing the Docs

These are the conversational prompts used with Claude to produce the analysis documents from the benchmark results. Session transcripts are not preserved; prompts are reconstructed from document content, dates, and context.

### Prompt B1: Benchmark Digest

**Origin:** Claude session, 2026-06-21.
**Purpose:** Analyze `yar_bench_final_analysis.md` (Ali's results) and produce a formal digest covering scope, methodology, results tables, SurrealDB deep-dive, and a retest plan.
**Output:** `docs/03-Products/Cytonome/Yar/consolidation_2026-06-21/_storage/BENCHMARK_DIGEST.md`
**Status:** Reuse with updates. The digest is still authoritative for the raw results. Update Section 4 (SurrealDB deep-dive) after the next retest by appending a "post-retest addendum" rather than overwriting.

Reconstructed prompt intent:
> "Read `yar_bench_final_analysis.md`. Produce a formal benchmark digest covering: scope, methodology, results ranking tables at all dataset sizes, and a deep SurrealDB analysis explaining why its last-place score is a configuration artifact. Include a specific retest plan for Ali."

---

### Prompt B2: SurrealDB Code Audit

**Origin:** Claude session, 2026-06-22.
**Purpose:** Audit `yar_bench.py` against the SurrealDB tuning guide and identify code-level issues causing benchmark artifacts.
**Output:** `docs/03-Products/Cytonome/Yar/consolidation_2026-06-21/_storage/SURREALDB_CODE_AUDIT.md`
**Status:** Reuse and update after each code revision applied. After the async SDK port (Issue 1 fix), update the audit to reflect the new code state; label the prior audit state "pre-async-port."

Reconstructed prompt intent:
> "Audit `yar_bench.py` in the benchmark package. For each SurrealDB adapter, compare the code to the tuning guide. Find and rank issues causing the benchmark performance gap. For each issue: state the file and lines, root cause, specific fix with before/after code."

---

### Prompt B3: Benchmark Revision Plan

**Origin:** Claude session, 2026-06-22.
**Purpose:** Produce a comprehensive code revision plan covering all package-level issues, optimal engine configuration, and a step-by-step rerun procedure for Linux.
**Output:** `docs/03-Products/Cytonome/Yar/consolidation_2026-06-21/_storage/BENCHMARK_REVISION_PLAN.md`
**Status:** Reuse as a checklist. Mark each code revision (CR-1 through CR-9) as done when applied. The rerun procedure in Section 6 is the canonical step-by-step reference for the next Ali run.

Reconstructed prompt intent:
> "Produce a formal revision plan for the benchmark package. Cover: all package-level issues found, optimal configuration for each engine, priority code revisions with specific file/line references, and a complete step-by-step rerun procedure for Linux x86_64. Include risks and what 'comparable to Ali's run' means."

---

### Prompt B4: SurrealDB Tuning and GraphRAG Guide

**Origin:** Claude session, 2026-06-21.
**Purpose:** Consolidate SurrealDB troubleshooting, configuration, and GraphRAG query patterns into a single engineer-facing reference.
**Output:** `docs/03-Products/Cytonome/Yar/spec/SurrealDB-tuning-and-graphrag-guide.md`
**Status:** Authoritative reference. Update when SurrealDB version advances; the guide notes version-specific behavior for 3.1.x. The troubleshooting table (T1-T12) and GraphRAG query patterns (Section 4) are the most frequently referenced sections.

Reconstructed prompt intent:
> "Write a SurrealDB 3.1 tuning, troubleshooting, and GraphRAG guide for the Yar project. Cover: troubleshooting table for all benchmark failures, configuration for server and embedded modes, SCHEMAFULL schema, FTS and vector index setup, the single-query GraphRAG pattern combining KNN + BM25 + graph traversal, and phone vs desktop profiles for Flutter."

---

## 4. Prompts Needed for the Next Phase

These prompts do not yet exist and should be written before the next retest or architecture decision.

### Needed Prompt N1: Async SDK Port Review

**Purpose:** Review the proposed async SDK port of `SurrealAdapter` and `SurrealTunedAdapter` before Ali runs it. Verify: correct use of `AsyncSurreal` (SDK 2.0.0 class name), event loop management, error handling for connection drops, and that all `_q()` call sites are correctly ported.
**Who writes it:** Shahin or engineering lead, addressed to the code-reviewer agent.
**When:** Before submitting the async port to Ali.

---

### Needed Prompt N2: PATCH11 Run Instructions

**Purpose:** Give Ali a clean, self-contained run prompt for the next benchmark patch. It should include: the volume cleanup sequence, the updated `run_surreal_tuned_retest.sh` with a SurrealKV comparable run, the Python requirements pinned to exact versions, and the expected validation gates (Section 8 of BENCHMARK-evaluation-and-results.md).
**Who writes it:** Shahin after code revisions CR-1 through CR-4 are applied.
**When:** After the async SDK port (N1) is reviewed and CR-4 (FalkorDB pin) is applied.
**Template base:** Prompt A4 (PATCH10) is the closest prior prompt; replace the unzip step with the repo path and add the SurrealKV comparable run instruction.

---

### Needed Prompt N3: GraphRAG Single-Query Benchmark

**Purpose:** Once the async SDK port is done and SurrealDB passes the basic benchmarks, design a GraphRAG-specific benchmark. The benchmark should measure a single SurrealQL query combining `<|k, ef|>` KNN + `@0@` BM25 + `->relation->` graph expansion, compared to a multi-step pipeline using FalkorDB for graph and SQLite-vec for vectors.
**Who writes it:** Shahin or the engineering lead.
**When:** After the main retest (N2) confirms SurrealDB is competitive.
**Reference:** `SurrealDB-tuning-and-graphrag-guide.md` Section 4.3 contains the canonical single-query pattern to test.

---

## 5. Summary Table

| Prompt | Location | Purpose | Status |
|---|---|---|---|
| A1: Initial run | Not preserved | Original untuned benchmark | Do not reuse |
| A2: PATCH8 run | `README_PATCH8_SURREAL_TUNED.md` | Tuned adapter introduction | Superseded |
| A3: PATCH9 run | `README_PATCH9_SURREAL_TUNED_FIX.md` | Validation layer fix | Superseded |
| A4: PATCH10 run | `README_PATCH10_SURREAL_FTS_RUNTIME_FIX.md` | FTS fix, canonical baseline | Reuse as template for PATCH11 |
| A5: Full reproduction | `README.md` | End-to-end reproduction | Use only for sync benchmark |
| B1: Benchmark digest | Reconstructed; output in `_storage/BENCHMARK_DIGEST.md` | Raw results analysis | Reuse; append addendum after retest |
| B2: Code audit | Reconstructed; output in `_storage/SURREALDB_CODE_AUDIT.md` | SurrealDB code issues | Reuse; update after each CR applied |
| B3: Revision plan | Reconstructed; output in `_storage/BENCHMARK_REVISION_PLAN.md` | Package-level issues, rerun procedure | Use as checklist |
| B4: Tuning guide | Reconstructed; output in `spec/SurrealDB-tuning-and-graphrag-guide.md` | Configuration and GraphRAG reference | Authoritative; update on version upgrade |
| N1: Async SDK review | Not yet written | Review async port before Ali runs | Needed before CR-1 port |
| N2: PATCH11 run instructions | Not yet written | Next Ali run prompt | Needed after CR-1 to CR-4 applied |
| N3: GraphRAG benchmark | Not yet written | SurrealQL single-query vs pipeline | Needed after N2 confirms competitiveness |

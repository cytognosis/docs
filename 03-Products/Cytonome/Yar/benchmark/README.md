---
status: authoritative
date: 2026-06-22
author: "@shahin"
audience: engineers
tags: [yar, storage, benchmark, index]
---

# Yar Storage and GraphRAG Benchmark: Document Index

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: engineers, stakeholders
> **Tags**: `yar`, `benchmark`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)

This is the one-page index for all formal benchmark documents in this folder and in adjacent paths. One-line purpose per document. Start here.

---

## Documents in This Folder

| Document | Path | Purpose |
|---|---|---|
| Benchmark Evaluation and Results | [`BENCHMARK-evaluation-and-results.md`](./BENCHMARK-evaluation-and-results.md) | Authoritative benchmark results, 12 package-level issues, SurrealDB artifact verdict, Section 8 validity requirements for any rerun |
| Benchmark Prompts Catalog | [`BENCHMARK-prompts-catalog.md`](./BENCHMARK-prompts-catalog.md) | History of PATCH run instructions (A1-A5), analysis prompts (B1-B4), and needed next-phase prompts (N1-N3) |
| cytomem GraphRAG Integration and Optimization | [`CYTOMEM-graphrag-integration-and-optimization.md`](./CYTOMEM-graphrag-integration-and-optimization.md) | cytomem Neo4j architecture, engine fit assessment, GraphRAG framework comparison, concrete optimization steps, and desktop benchmark plan |
| Antigravity Execution Prompt | [`ANTIGRAVITY-execution-prompt.md`](./ANTIGRAVITY-execution-prompt.md) | Self-contained runbook for the Antigravity coding agent: apply SurrealDB optimizations, run PATCH11, add GraphRAG benchmarks, and optimize cytomem |
| Benchmark Master Plan | [`BENCHMARK_MASTER_PLAN.md`](./BENCHMARK_MASTER_PLAN.md) | Original master plan for the benchmark program |
| Master Drive Plan | [`MASTER_DRIVE_PLAN.md`](./MASTER_DRIVE_PLAN.md) | Historical drive plan for the feature-research and benchmark consolidation program (program complete 2026-06-21) |

---

## SurrealDB Guides (spec/)

| Document | Path | Purpose |
|---|---|---|
| SurrealDB Tuning and GraphRAG Guide | `../spec/SurrealDB-tuning-and-graphrag-guide.md` | Troubleshooting table T1-T12, SCHEMAFULL schema, FTS/HNSW index syntax, persistent WebSocket pattern, GraphRAG query patterns, verification checklist |
| SurrealDB Advanced Optimization and Versions | `../spec/SurrealDB-advanced-optimization-and-versions.md` | Latest version changelog (3.1.0-3.1.5), maximum-performance checklist ordered by impact, docker-compose and run script changes for PATCH11 |
| Storage Benchmark Tracker | `../spec/STORAGE_BENCHMARK_TRACKER.md` | Living master status table for all engines and sync options; open decisions O-1 through O-8 |

---

## Code Audit and Revision Plan

> **Path correction (2026-07-17):** both documents below used to be cited at `../consolidation_2026-06-21/_storage/`. That directory was archived on 2026-06-21/2026-07-16; `SURREALDB_CODE_AUDIT.md` was separately promoted to `research/` and never lived only in the archive. Links below point at the real current locations.

| Document | Path | Purpose |
|---|---|---|
| SurrealDB Code Audit | [`../research/SURREALDB_CODE_AUDIT.md`](../research/SURREALDB_CODE_AUDIT.md) | 8 code-level issues ranked by impact, exact before/after code snippets for each fix, Summary Table |
| Benchmark Revision Plan (archived) | git history (the on-disk `_archive/` was retired) | All 12 package-level issues with file/line references, local install plan, code revisions CR-1 through CR-9, step-by-step rerun procedure, risks R1-R8. Historical; superseded by `SURREALDB-RETEST-REPORT_2026-07-16.md` and `SURREALDB-PATCH11-VERDICT_2026-07-16.md` below |

---

## Session Updates (2026-07-16)

| Document | Path | Purpose |
|---|---|---|
| SurrealDB PATCH11 Verdict | [`SURREALDB-PATCH11-VERDICT_2026-07-16.md`](./SURREALDB-PATCH11-VERDICT_2026-07-16.md) | Closes the PATCH11 async-SDK / embedded-mode / RELATE graph-model test; decision D4 |
| SurrealDB v3.1.5 Retest Report | [`SURREALDB-RETEST-REPORT_2026-07-16.md`](./SURREALDB-RETEST-REPORT_2026-07-16.md) | Root cause, changelog, and results; merges the retired `BENCHMARK-REPORT.md`, `OPTIMIZATION-CHANGELOG.md`, `SURREALDB-ROOTCAUSE.md` (now in `_archive/cleanup_2026-07-16/surrealdb/`) |

---

## Benchmark Package (external, outside this docs repo)

> **External anchor:** `https://github.com/cytognosis/yar_revisions/yar_supervisor_reproducible_benchmark_package/` (verified present 2026-07-17; this replaces the old, never-resolved `<repo-root>/yar_supervisor_reproducible_benchmark_package/` placeholder path below).

| Document | Path | Purpose |
|---|---|---|
| Package README | `https://github.com/cytognosis/yar_revisions/yar_supervisor_reproducible_benchmark_package/README.md` | Run commands, architecture decision summary, reference output list; start here to reproduce a run |
| PATCH10 README | `.../db_benchmark/README_PATCH10_SURREAL_FTS_RUNTIME_FIX.md` | Canonical prior patch; PATCH11 builds on it; contains the FTS ORDER BY alias fix |
| PATCH10 Final Comparison | `.../reference_results/surreal_tuned_patch10_final_comparison.md` | Authoritative PATCH10 p50 latency tables and interpretation; the comparison baseline for all future runs |

---

## Reading Order

For a new engineer approaching this work for the first time:

1. `BENCHMARK-evaluation-and-results.md` -- understand what was measured and what the artifacts are.
2. `../spec/STORAGE_BENCHMARK_TRACKER.md` -- see the current engine status and open decisions.
3. `SURREALDB-RETEST-REPORT_2026-07-16.md` then `SURREALDB-PATCH11-VERDICT_2026-07-16.md` -- the current-state results (supersede the old code-audit-only path).
4. `../research/SURREALDB_CODE_AUDIT.md` -- understand the specific code fixes needed.
5. `../spec/SurrealDB-tuning-and-graphrag-guide.md` -- get the SurrealQL syntax and configuration patterns.
6. `ANTIGRAVITY-execution-prompt.md` -- the full execution runbook (or pass directly to the Antigravity agent).

---

[Up: Yar master index](../README.md)

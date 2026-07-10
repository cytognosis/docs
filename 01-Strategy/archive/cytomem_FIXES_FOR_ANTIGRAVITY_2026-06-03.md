# CytoMem: Fixes / Tests / Additions (hand-off to Antigravity)

**Date:** 2026-06-03 · From: Shahin's Claude Cowork strategy session · **Goal:** make cytomem the true universal, cross-agent memory (repos **and** all doc systems, with native MCP recall) so the org-wide consolidation program can build on it instead of around it. Items are prioritized with acceptance criteria.

## Baseline verified working (2026-06-03)

- Neo4j live (`bolt://localhost:7687`); `cytomem health` ✅; **7,322 artifacts**.
- Rich CLI: `health, stats, search (+ --semantic), duplicates, branch-report, init, ingest (--repos/--agents/--dry-run), task (add/list/update), backlog (add/list/promote), link (add/list/auto), obsidian-sync`.
- 19 repos registered in `configs/repos.yaml`; **15 on `main`, 0 feature branches** (branch hygiene good; Stage B effectively done).
- Task/backlog/link graph model present (4 tasks, 3 backlog ideas).

## P0 — Build the doc-source ingestion CAPABILITY + connect the MCP (Antigravity builds the machine; Claude runs the ingestion)

**Division of labor (per Shahin):** Antigravity builds and verifies the *machinery*; **Claude/Cowork runs the actual content ingestion and the curated audit** (the judgment-heavy parts: track-tagging, dedup decisions, canonical-vs-obsolete) in the fresh Cowork project, once the capability + MCP exist. cytomem today indexes code repos + `agent-antigravity` only.

**Antigravity builds:**

1. **Non-repo doc-source ingestion capability.** A git-agnostic, **type-filtered** folder scanner (ingest `.md/.txt/.ipynb`/code/schemas; **exclude** binaries, images, `node_modules`, `.git`, `.venv`, lockfiles, caches, large data blobs), a `configs/doc_sources.yaml` registry (path, track, status, include/exclude globs), and a documented CLI (e.g., `cytomem ingest --doc-source <path>` and/or registry-driven). **Verify end-to-end on the Obsidian vault** (`cytomem obsidian-sync` → artifacts land, section→track tagged). **Acceptance:** Claude can point the tool at any folder and get type-filtered, track-tagged artifacts in the graph; Obsidian notes searchable.
2. **Connect the MCP** to Claude Cowork + Antigravity (`cytomem_recall`, `cytomem_stats`, `cytomem_timeline`, `cytomem_duplicates`; ideally `search --semantic` and task/backlog/link reads). **Acceptance:** a Cowork session calls `cytomem_recall` natively (no Bash).

**Claude/Cowork runs (NOT Antigravity), once the above exist:**

- Ingest the **7 active Cowork projects** (`~/Claude/Projects/*`: Grants and Applications, Science and Platform, Strategic Planning, Infrastructure and Tooling, Toolings, Refactor, X-Labs), track-tagged and type-filtered (flag `Refactor`/`Toolings` as possibly scratch).
- The **stage-1 curated audit** of `~/Documents/_archive` (**~111K files**: Design, RDoC, Strategy, Tools and Standards, application_templates, backup, old_Obsidian Vault, unsorted) + `~/Documents/Personal_drafts` (~1,150) + all `_archive`/`_history`/scratch subfolders: a master triage list (ingest / reorg / archive / delete) using cytomem `duplicates`/`search` as the **dedup oracle**, then selective ingest + cleanup. Register these `status: audit-pending` now (tracked, not scanned).

## P0 — Connect the MCP so agents get native recall

`cytomem-mcp` (tools: `cytomem_recall`, `cytomem_stats`, `cytomem_duplicates`, `cytomem_timeline`) is **not connected to Claude Cowork** (only CLI-over-Bash works today). **Action:** document and provide the MCP connection config so it can be registered as a connector in **(a) Claude Cowork** and **(b) Antigravity**; expose recall/stats/timeline/duplicates plus ideally `search --semantic` and task/backlog/link reads. **Acceptance:** a Cowork session calls `cytomem_recall` natively (no Bash).

## P1 — Verify semantic search

`--semantic`, `_semantic_search`, and a fastembed `local_embedder` exist. **Action:** confirm embeddings are built during ingest and that `cytomem search --semantic <q>` returns vector matches a keyword search misses; if embeddings are not populated, add an embed step to ingest. **Acceptance:** a semantic query surfaces relevant artifacts that keyword search does not.

## P1 — Registry consistency + cleanup

- `agent-antigravity` is ingested (509 artifacts) but **not in `repos.yaml`** → register it or document its source.
- branch-report git-errors on `scratch, archive, cytodocs, neuro-pheno` → mark non-git/empty/absorbed so ingest and branch-report do not error (`neuro-pheno` = empty; `cytodocs` = absorbed into cytomem).
- **Acceptance:** `branch-report` has zero ⚠️; the registry matches the ingested set.

## P1 — Cross-source dedup + canonical home

Once Obsidian + X-Labs + docs-repo are ingested, the same doc may appear in several sources. **Action:** verify `cytomem duplicates` groups cross-source copies (content-hash) and add a **canonical-home** flag with precedence (docs-repo = engineering; X-Labs = strategy/funding; Obsidian = ADHD-variant mirror). **Acceptance:** duplicates report groups cross-source copies; canonical flag queryable.

## P2 — Task/Backlog/Link usable for the program

The consolidation runs per-track subagents with goals/deliverables/verification. **Action:** confirm the task/backlog/link schema supports a task per track with **deliverable** and **verification** fields, linked to artifacts; document with an example. **Acceptance:** can create "Consolidate <track>" with deliverable + acceptance criteria linked to its artifacts.

## P2 — Tests + reliability

Only `tests/test_core.py` exists. **Action:** add smoke tests per ingestion source type (repo, obsidian, doc-source), search (keyword + semantic), and dedup; minimal CI. **Acceptance:** `pytest` covers ingest + search + dedup.

## Notes for Antigravity

- Ingestion is idempotent (content-hash), so re-running is safe; do not risk data loss.
- Canonical taxonomy = `tracks.yaml` pillars (cytoverse/cytonome/cytoscope/toolchain/operational/research). The **strategy overlays (funding/people/personal) are cross-cutting tags, not repos** — consider adding them as artifact labels.
- Unblocks: once P0 (doc-source ingestion) + the MCP land, the Cowork consolidation program (in a fresh project) can anchor on cytomem and build the per-track docs + master view directly from the graph.

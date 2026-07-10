# Stage 1 — Archive Audit & Triage

**Date:** 2026-06-03 · Metadata-only inventory of the archives and in-project scratch folders, scoped per the agreed Stage 1 plan. Manifests live in the session scratch dir (`stage1/*.tsv`). **No files moved, ingested, or deleted yet.** This is the triage list for your sign-off.

## BLUF

The 21 GB / 112K-file `_archive` is **mostly code and dependencies** (pyi, js, dll, venvs), not documents. Filtering to real document content and to the last 18 months leaves **2,677 doc files** in clean clusters, plus **835 doc files in `Personal_drafts`**. Recommendation: **ingest only the Strategy + templates + RDoC clusters (~398 files) after a dedup check; archive-in-place the backups and old Claude exports; handle `Personal_drafts` in a separate sensitivity-screened pass.**

## Done (2026-06-03)

- ✅ **Ingested** `Personal_drafts` (843 files; `prompts/` excluded per your instruction) → graph
- ✅ **Ingested** `_archive/Strategy` (232), `_archive/application_templates` (147), `_archive/RDoC` (3)
- ✅ Confirmed `docs` repo (456 docs on disk vs 494 indexed) and the vault (160 md vs 170 indexed) are **already fully covered** — no gap
- ✅ Registered the four new sources in `cytomem/configs/doc_sources.yaml`
- ✅ Graph grew **8,029 → 9,255 artifacts** (+1,226), **21 → 25 sources**; dedup (content-hash) confirmed working

## Stage 1 CLOSED (2026-06-03)

- ✅ `_archive/unsorted` ingested (128 docs; `images/` excluded; duplicate Cowork copies auto-dedup)
- ✅ `_archive/old_Obsidian Vault` ingested (623 docs; larger than live vault, held un-migrated strategy/architecture content; overlap auto-flagged by content-hash)
- ✅ `Claude` exports (671) + `backup` (603): **archive-in-place, no ingest** (low canonical value)
- ✅ Files older than 18 months (2,764): out of scope, left archived

**Final graph state:** 10,006 artifacts · 27 sources · 20 content-hash dedup clusters (canonical auto-selected, `docs` repo preferred). Six new doc sources registered in `cytomem/configs/doc_sources.yaml`: personal-drafts, archive-strategy, archive-application-templates, archive-rdoc, archive-old-obsidian, archive-unsorted.

**Nothing was deleted.** All archive folders remain in place; cytomem indexes them and flags duplicates against canonical homes.

## What the sweep found

| Source | Raw | After excluding code deps | Recent (≥ 2024-12-03) |
|---|---|---|---|
| `~/Documents/_archive` | 112,316 files / 21 GB | 5,441 doc files | **2,677** |
| `~/Documents/Personal_drafts` | 1,150 files | 835 doc files | (not yet split) |
| In-project scratch/archive dirs | 55 dirs | ~12 genuine (rest are `third_party`/build) | n/a |

## `_archive` recent doc clusters (2,677 files) — proposed triage

| Cluster | Files | Action | Why |
|---|---|---|---|
| **Strategy** | 237 | **Ingest after dedup** | Strategy corpus, high canonical value |
| **application_templates** | 148 | **Ingest after dedup** | Grant/proposal templates (IGoR, NSF, NIH) |
| **RDoC** | 13 | **Ingest** | Research-domain criteria, small and relevant |
| Tools and Standards / Design | 2 | Ingest | Trivial, likely canonical |
| **old_Obsidian Vault** | 686 | **Dedup, then skip the matches** | Superseded by the live vault (already indexed); ingest only notes with no canonical match |
| **Claude** | 671 | Archive-in-place | Old Claude session exports; low canonical value |
| **backup** | 603 | Archive-in-place | Backups of content already canonical elsewhere |
| **unsorted** | 317 | **Sample + triage** | Genuinely unknown; needs a content sample before deciding |

**Older than 18 months (2,764 doc files):** out of scope per the agreed sampling; left archived. We sample only if a gap shows up later.

## In-project scratch/archive dirs worth a look

These sit inside already-ingested repos, so most content is likely already indexed. Genuine (non-`third_party`, non-build) candidates:

- `~/Claude/Projects/X-Labs/_archive`
- `~/Claude/Projects/Science and Platform/schema-survey-2026-05/{old, .../archive}`
- `~/Claude/Projects/Infrastructure and Tooling/sensing/old`
- `~/repos/cytognosis/{scratch, archive, cytos/archive, cytoskeleton/scratch, cytocast/scratch, branding/archive}`
- `~/Documents/ObsidianVault/{_history, _archive}`

The large `~/repos/cytognosis/archive/old/**` tree is deep legacy (old neo4j/zotero/anytype checkouts); treat as archive-in-place.

## Decision flagged (recommendation in bold)

`Personal_drafts` (835 doc files) likely holds **personal, legal, and financial material**. **Recommendation: handle it in a separate, sensitivity-screened pass rather than folding it into the general ingest** — so nothing private lands in the shared knowledge graph by default.

## Next actions (no outreach needed)

1. Run `cytomem_duplicates` + semantic `cytomem_recall` on the **Strategy** and **application_templates** clusters to confirm what is net-new.
2. Sample ~15 files from **unsorted** to classify it.
3. Ingest the confirmed net-new Strategy/templates/RDoC files with track tags.
4. Produce the final ingest/reorg/archive/delete manifest for your approval before any deletion.

# Cytos pillar — agent brief

> **Variants**: Agent seed (this doc) - Technical (cytos-pillar.md) - Readable (cytos-pillar.md in Obsidian vault: 04-Engineering/cytos/)

> **Status:** Active · **Date:** 2026-07-01 · **Audience:** Fresh agent, zero context · Self-contained.

**Goal:** Maintain and extend the Cytos engineering platform (the Cytoverse "Map"): LinkML schemas, DVC-managed data, the knowledge graph, generated typed artifacts, and the sensing schema.

**Scope (yours):** `~/repos/cytognosis/cytos` code and schemas; docs layers `04-Engineering/cytos` and `03-Products/Cytoverse`. **Not yours:** the science-foundation narrative (Neuroverse, `05-Research/neuroverse`); cytomem (terminal wave only).

## Decided / done (do not redo)

- Generated trees (`artifacts/`, `dist/`, `data/` blobs, caches) are correctly gitignored; the repo is compliant. Verified 2026-07-01.
- Schema artifacts regenerate with `nox -s schema_generate` (`uv run cytos schema generate all`). Do not commit outputs.
- `src/cytos/schema/generated/genomics.py` is a tracked, labeled hand-crafted exception. Keep it.
- Duplicate/superseded docs archived to `04-Engineering/cytos/_archive/` with forward links: `architecture-overview.md`, `architecture-overview-v2.md`, `module-map-v2.md`, `scholarly-kg.yaml` (v0.3.0).
- Canonical entry docs added: layer `README.md` and this three-variant pillar doc.

## Open questions (recommendations in the resume kit)

1. In-repo `cytos/docs/` (170M) overlaps this docs layer. Recommend thinning to a pointer; deferred to Wave 2. (OPEN_QUESTIONS Q6)
2. Four docs touch the neuros boundary (`brain-atlas.md`, `sensing-schema/data-formats.md`, `sensing-schema/sensor-taxonomy.md`, `schemas-ontologies/biotools-schema-edam-research.md`). Kept here this wave; reconcile with Neuroverse in Wave 2. (Q7)
3. `03-Products/Cytoverse` is claimed by both Cytos and Neuroverse. Cytos owns product/platform framing. (CONFLICTS C1)

## Pending work (prioritized)

1. **Three-variant treatment for the remaining substantive docs** (this wave produced the pillar entry doc only). Ranked: `architecture.md`, `platform-design.md`, `unified-sensor-report.md`, `cytos-neuros-separation.md`, `data-lifecycle-architecture.md`, `semantic-alignment.md`, `experiment-orchestration-research.md`, `genomic-atlas.md`, `platform-tutorial.md`, `scholarly-kg-v0.4.0.yaml`, `vfs-containers-databases-analysis.md`, `tool-roles-explained.md`. Mirror each readable variant to Obsidian.
2. Resolve Q6/Q7/C1 in Wave 2.
3. `cytoexplorer` repo doc structure (future wave).

## Source-of-truth files

- Layer index: `04-Engineering/cytos/README.md`
- This pillar doc: `04-Engineering/cytos/cytos-pillar.{technical,readable,agent}.md`
- Resume kit: `~/Claude/Projects/Cytos/00-CONSOLIDATION/{STATE,OPEN_QUESTIONS,NEXT_STEPS,DATA-MANIFEST,CONFLICTS,CLASSIFICATION.tsv,INDEX}.md`
- Rules: `~/Claude/Projects/Refactor/00-CONSOLIDATION/SHARED-BLUEPRINT.md`

## Success criteria

- Schemas remain the only source of truth; artifacts stay generated and uncommitted.
- Every substantive doc has three variants; no dangling links; badges accurate.
- A fresh agent can orient in 5/10/15 minutes from `00-CONSOLIDATION/INDEX.md`.

## Exact start commands

```bash
cd ~/repos/cytognosis/_worktrees/docs-cytos && git branch --show-current   # reorg/cytos-2026-07-01 (docs work, isolated)
cd ~/repos/cytognosis/cytos && git branch --show-current                    # reorg/cytos-2026-07-01 (code work)
cd ~/repos/cytognosis/cytos && nox -s schema_generate                       # regenerate artifacts (do not commit)
```
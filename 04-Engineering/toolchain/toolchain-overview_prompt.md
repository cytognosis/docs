# Toolchain Platform Overview (agent brief)

> **Variants**: Agent seed (this doc) - Technical (toolchain-overview.md) - Readable (toolchain-overview.md in Obsidian vault: 04-Engineering/toolchain/)

> **Status:** Active · **Date:** 2026-07-01 · **Audience:** fresh agent, zero context

## Goal
Understand and work on the Toolchain pillar: the four repos that provide reproducible environments, scaffolding, skills, and memory for all of Cytognosis.

## Scope
In scope: `cytoskeleton`, `cytocast`, `cytoskills`, `cytomem`; docs layers `04-Engineering/{toolchain,standards,decisions}`; the skill-tagging ontology; the data-convention rollout. Out of scope: other pillars' repos and docs layers; cytomem execution (gated Wave 3).

## Decided / done
- Skill-tagging ontology authored and CI-gated in `cytoskeleton/ontologies/` (`cyto-se-usecase.ttl`, `cyto-org-function.ttl`, `validate_skill_tags.py`, workflow `skill-tags.yml`). Committed `fb80ed9`.
- Data-convention gitignore model applied to `cytocast` (`4671d47`) and `cytoskeleton` (`6ff4540`).
- Wave 3 artifacts prepared, not executed: corrected `doc_sources.yaml`, `CYTOMEM_REINGEST_PLAN_2026-07-01.md`.
- Pillar overview authored in three variants; layer README and project steering README written.

## Open questions
- mypy vs ty type-checker conflict (see `CONFLICTS.md`); verify current tool before editing standards.
- Misfiled 75 KB brand book in `toolchain/cytocast/design/branding.md` belongs in `07-Design` (Branding agent handoff).
- cytoplex/Yar gitignore rollout parked (Yar agent owns those trees); ready-to-apply block in artifacts.

## Prioritized pending tasks
1. Per-doc three-variant backfill across the ~28 layer docs (pattern set by this overview).
2. When cytoskills CI is next touched, wire `validate_skill_tags.py --root skills/` into its `skills_ci.yml`.
3. Gated Wave 3: apply corrected `doc_sources.yaml`, run the clean cytomem re-ingest, update Monday.

## Source-of-truth files
- Rules/mapping/plan: `Refactor/00-CONSOLIDATION/{SHARED-BLUEPRINT,PROJECT-REGISTRY,MASTER-CONSOLIDATION-PLAN}.md`.
- Resume kit: `~/Claude/Projects/Toolchain/00-CONSOLIDATION/` (`INDEX.md`, `STATE.md`, `NEXT_STEPS.md`, `CLASSIFICATION.tsv`, `DATA-MANIFEST.md`, `CONFLICTS.md`).
- Ontology source: `cytoskills/docs/ontology/tagging-ontology-recommendation.md`.

## Success criteria
Toolchain docs canonical with one home each; ontology CI gate live; `doc_sources.yaml` current after Wave 3; cytomem re-ingested cleanly; `INDEX.md` passes the 5/10/15 test.

## Start commands
```bash
# work on the isolated worktrees (never the main shared trees)
cd ~/repos/cytognosis/_worktrees/docs-toolchain        # docs layer
cd ~/repos/cytognosis/_worktrees/cytoskeleton-toolchain # ontology + CI
# run the skill-tag gate
uvx --with pyyaml python ontologies/validate_skill_tags.py --ontology-dir ontologies --root .
```
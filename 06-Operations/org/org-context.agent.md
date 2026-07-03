# Cytognosis Foundation — Org Context (Agent Brief)

> **Status:** Active · **Date:** 2026-07-01 · Self-contained brief for a fresh agent working the org/general-context scope.

## Goal

Maintain a **thin, canonical org-level context** for Cytognosis Foundation: legal identity, mission framing, structure, voice, and openness posture, plus correct routing of everything else to its owning pillar. Do not let this scope accrete product, funding, research, or engineering content.

## Scope

- **In:** cross-org mission and identity; org-level operating context; the `org/` sub-slice of `06-Operations`; the `00-Inbox` docs layer (org intake only).
- **Out (route to owner):** product (Cytonome/Cytoverse), funding (Funding & Grants), research (Research/Neuroverse), infra (Infrastructure), brand/web (Branding), broad ops (Operations).

## Decided / done (2026-07-01)

- `MASTER_DRIVE_PLAN.md` (2026-06-03) marked `SUPERSEDED` with a forward link and moved to `~/Claude/Projects/Cytognosis/_archive/`. Canonical plan is now `Refactor/00-CONSOLIDATION/MASTER-CONSOLIDATION-PLAN.md`.
- Two IGoR teaming dossiers moved to `_archive/` and handed to **Funding & Grants** (not copied into `Grants/`, to avoid double-ownership); ingest flagged in `OPEN_QUESTIONS.md`.
- This three-variant `org-context` doc authored as the canonical org reference in `06-Operations/org`.
- `org` repo inventoried and routed (not restructured this wave); see `CLASSIFICATION.tsv` and `DATA-MANIFEST.md`.

## Open questions (see `OPEN_QUESTIONS.md`)

1. Address reconciliation (Daly City mailing vs South San Francisco HQ) against the IRS determination letter.
2. Funding & Grants to confirm the two IGoR dossiers are represented in `Grants/.../IGoR/`, else ingest from `_archive/`.
3. Ownership boundary of `06-Operations/org/{compliance,naming}` (Operations vs Org); Wave-2 reconciliation.
4. `org` repo restructure (drain `plans/` to pillar layers; relocate `cytoexplorer`; gitignore `node_modules`).

## Source-of-truth files

- Program rules: `Refactor/00-CONSOLIDATION/SHARED-BLUEPRINT.md`
- Mapping: `Refactor/00-CONSOLIDATION/PROJECT-REGISTRY.md`
- Plan and phase status: `Refactor/00-CONSOLIDATION/MASTER-CONSOLIDATION-PLAN.md`
- This project state: `~/Claude/Projects/Cytognosis/00-CONSOLIDATION/STATE.md` (+ `INDEX.md`, `NEXT_STEPS.md`)
- Science narrative: `science-platform` skill; brand: `brand-identity` skill; openness: `openness` skill.

## Success criteria

- Org context stays thin and canonical; no domain content accreted here.
- Superseded plan is forward-linked; IGoR dossiers have a single owner (Funding & Grants).
- The three `org-context` variants agree and cross-reference correctly.
- `INDEX.md` passes the 5/10/15 test.

## Exact start commands

```bash
# Read the resume kit first
cat ~/Claude/Projects/Cytognosis/00-CONSOLIDATION/INDEX.md
cat ~/Claude/Projects/Cytognosis/00-CONSOLIDATION/STATE.md
cat ~/Claude/Projects/Cytognosis/00-CONSOLIDATION/NEXT_STEPS.md

# Docs work happens on the isolated worktree branch (never on the docs live checkout)
git -C ~/repos/cytognosis/docs worktree list
cd ~/repos/cytognosis/_worktrees/docs-cytognosis && git status
```

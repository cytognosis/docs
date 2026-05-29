# 06 — Cytos Transition

**Phase 6 of master plan**. Depends on Phase 1 (cytoskeleton with schemas/), Phase 3 (cytocast v2), Phase 5 (cytognosis-data skill).

## What this subplan does

Least-destructive transition of cytos to consume the refactored stack:

- Add cytoskeleton submodule at pinned tag.
- Migrate `cytos/schemas/` → consume from cytoskeleton submodule (symlink or wrapper import).
- Consolidate cytos design docs: 11 files in `cytos/design/` + 9 files in `/Infra and design/cytos_drafts/v1/+v2/` → single canonical `cytos/docs/design/`.
- Add `.cytognosis-config.yaml` post-hoc (cytocast "adopt" pattern).
- Update DVC config to use new tier-aware remotes (per cytognosis-data skill).
- Inherit `_shared/` workflows from cytocast.
- Mark V1-style modeling modules (features/models/train/evaluate/kg_embed/infer) as `_stub.py` clearly to indicate their status.
- Keep all hand-authored code; no destructive rewrite.

## Prerequisites

- Phase 1, 3, 5 complete.
- cytoskeleton v2.0.0-rc1 tag exists.
- cytognosis-data skill content authored.

## Outputs

After this subplan:
- Branch `refactor/v2-cytoskeleton-integration` in `/refactor/cytos/`.
- `external/cytoskeleton/` submodule at pinned tag.
- `cytos/schemas/` removed (or symlinked to submodule).
- Single `cytos/docs/design/` (11 + 9 → ~15 consolidated files).
- `.cytognosis-config.yaml` + `.copier-answers.yml` post-hoc.
- Updated `dvc.yaml` references tier-aware remotes.

## Files

| File | Purpose |
|---|---|
| `01_plan_prose.md` | Reasoning |
| `02_checklist.md` | Atomic steps |
| `03_scripts/` | Migration scripts |
| `04_verification.md` | Acceptance |
| `05_open_questions.md` | Decisions |

## Estimated effort

2-3 days. Design consolidation is the largest task.

## Risk assessment

- **Medium risk on schema migration**: cytos has 43 schemas actively used; symlinks or wrappers must work transparently.
- **Medium risk on design consolidation**: 20 docs to reconcile; manual review required.
- **Low risk on DVC update**: changing remote URLs is reversible.
- **Low risk on modeling-stub marking**: rename-only refactor.

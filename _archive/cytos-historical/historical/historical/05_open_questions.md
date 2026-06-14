# 06 — Cytos Transition — Open Questions

## Blocking

### Q1. Schema migration mode: symlink vs Python wrapper vs copy

Recommendation: symlink (Option A in plan §3). 

**Alternative**: copy schemas into cytos/ at build time (Phase 6 step 4 script), so cytos remains independently buildable without the submodule.

**Tradeoff**: symlink keeps single source of truth; copy makes cytos portable. For Cytognosis-internal use, single source of truth wins.

**Action**: confirm symlink.

### Q2. cytos modeling arc retention

Recommendation (master plan D8, B5): KEEP all modeling modules; mark as stub status.

**Alternative**: carve into `cytos-models` subpackage now.

**Action**: confirm keep-in-place.

## Modifying

### Q3. Should historical/v1-full-package-design.md and v2-data-only-package-design.md stay in cytos/docs/design/historical/ or move to a separate archive repo?

Recommendation: keep in cytos repo (small files; useful as reference). Document their historical status in the file headers.

### Q4. DVC remote: how to handle existing tracked data?

Cytos has `processed.dvc` markers from previous runs. After remote change:
- Existing .dvc files point to old remote
- `dvc pull` after the change will fail unless remote is reconfigured

**Action**: include a one-time `dvc remote rename` + re-upload step in the checklist.

## Resolved

- Design docs consolidate to cytos/docs/design/ (not Plans/).
- cytoskeleton submodule at v2.0.0-rc1 (Phase 1 tag).
- Cytocast adoption via copier --skip-if-exists pattern.
- _shared/ workflows inherited from cytocast.

# 06 — Cytos Transition — Plan & Reasoning

## 1. Current state

Cytos (main branch) is a mature, production-ready substrate:

- **30+ src/cytos/ modules**: cli, sources, ingest, schema, ontology, harmonize, kg (KGBuilder DuckDB 860 LOC), validate, features (stubs), models (stubs), train (stubs), evaluate (stubs), scholarly, genomics, services, pipelines, publish, rag, utils.
- **43 LinkML schemas** in `cytos/schemas/` (30 domains + enums + cytos.yaml + core.yaml).
- **9 DVC stages** in `dvc.yaml` actively used.
- **11 design docs** in `cytos/design/` (May 12 2026, v3.0.0, agent-generated via Antigravity).
- **NOT generated from cytocast** (greenfield wrt cytocast; pyproject.toml references cytoskeleton-managed env via comment but no actual integration).
- **Python 3.13+, Hatchling, optional deps groups for biothings, ga4gh, scvi, imaging, genomics, connectomics, ehr, biblio, causal, mofa, llm, nlp, kg_neo4j, kg_kuzu, kg_tiledb, kedro_*, ray, rocrate_extra.**

Plus 9 draft docs in `/Infra and design/cytos_drafts/v1/+v2/` (v1 = full modeling, v2 = data-only).

## 2. Design consolidation (the hardest part)

We have 3 sources of cytos design truth:

| Source | # docs | Recency | Authoritative? |
|---|---|---|---|
| `/Infra and design/cytos_drafts/v1/` | 5 | Early | Was v1 design |
| `/Infra and design/cytos_drafts/v2/` | 4 | Mid | v2 refinement (data-only direction) |
| `/repos/cytognosis/cytos/design/` | 11 | Most recent (May 12, 2026) | Agent-generated (Antigravity); reflects current dir structure |

### Resolution strategy

Treat cytos/design/ (11 docs) as the **canonical present state**. Treat cytos_drafts/ as historical references. Consolidation:

1. Copy cytos/design/* into refactor branch's `cytos/docs/design/`.
2. For each cytos_drafts doc, decide: redundant (deletable), supplementary (keep as appendix), or contradictory (resolve in cytos/docs/design/ canonical version).
3. Reconcile differences explicitly in cytos/docs/design/decision_log.md.

### Key reconciliations

| Topic | v1 says | v2 says | cytos/design/ says | Decision |
|---|---|---|---|---|
| Modeling arc (features, models, train, eval, kg_embed, infer) | first-class | removed | exists as stubs | KEEP (per D8 in master plan) — mark as stub clearly; cytos is the foundation kernel, modeling belongs |
| Pipeline stages | 14 (data+model) | 9 (data only) | follows v1 (with stubs) | KEEP 14 stages; modeling stages marked stub |
| Schemas | in cytos/ | in cytos/ | in cytos/ | MOVE to cytoskeleton (Phase 1 already mirrored; this phase removes cytos copy) |
| Configs | configs/{sources,training,cohorts,quality,mappings,prefixes} | configs/{sources,quality,mappings,prefixes} (no training/cohorts) | as v1 | KEEP all (v1 superset) |
| Foundation model architecture (v1's 04_foundation_model_architecture.md) | full | n/a | not in cytos/design/ | KEEP v1's doc as historical reference in `docs/design/historical/` |

### Consolidation output

Single canonical `cytos/docs/design/` with ~15 files:
- README.md (the index, rewritten)
- ARCHITECTURE.md (current)
- SCHEMAS.md (current; updated to reference cytoskeleton submodule)
- PIPELINE.md (current EXECUTION_PLAN renamed for clarity)
- AUTOMATION.md (current)
- REQUIREMENTS.md (current)
- PROVENANCE.md (current)
- HRA_INTEGRATION.md (current)
- OBSERVATIONAL_INGESTION.md (current)
- ROADMAP.md (current; updated for v2.0 timeline)
- TASKS.md (current; cleared, repopulated post-refactor)
- decision_log.md (NEW; consolidates v1/v2/current reconciliations)
- historical/v1-full-package-design.md (from cytos_drafts/v1/01)
- historical/v1-foundation-model-architecture.md (from cytos_drafts/v1/04)
- historical/v2-data-only-package-design.md (from cytos_drafts/v2/01)
- adrs/ (current; preserved)
- rfcs/ (current; preserved)
- modules/ (current; preserved)
- evaluations/ (current; preserved)
- templates/ (current; preserved)

## 3. Schemas migration (cytos → cytoskeleton)

In Phase 1, cytoskeleton/schemas/ already received a COPY of cytos/schemas/. This phase makes that copy authoritative and removes cytos's local copy.

### Approach: symlink + Python wrapper

Option A (symlink only):
```bash
cd cytos
rm -rf schemas
ln -s external/cytoskeleton/schemas schemas
```

Option B (Python wrapper):
```python
# cytos/cytos/schemas.py
"""Forwards to the cytoskeleton-hosted schemas via submodule."""
from pathlib import Path
SCHEMAS_DIR = Path(__file__).parent.parent / "external" / "cytoskeleton" / "schemas"
```

**Recommendation**: Option A (symlink) + add a top-level `cytos/schemas/README.md` (file inside the symlinked dir) documenting the indirection. Tooling (LinkML SchemaView, codegen scripts) operates on paths and accepts symlinks transparently.

Risk: on Windows, symlinks may not work. Mitigation: cytos is primarily a Linux/macOS project; document Windows workaround (clone + post-create script that copies instead of symlinks).

## 4. Modeling stubs marking

V1-style modules exist as stubs in cytos/src/cytos/{features,models,train,evaluate,infer}/. Per D8, we KEEP these but make their status explicit.

Renaming pattern: each `__init__.py` adds:
```python
"""STATUS: stub. Implementation deferred to cytos v2.x (post Yar refactor).

See docs/design/historical/v1-foundation-model-architecture.md for full design.
"""
```

Optionally: rename individual files to `*_stub.py` if they really are stubs (e.g., `cytos/models/encoders/__init__.py` has stub class definitions). Use grep + AST analysis to identify.

For now, just add module-level docstrings. Renaming individual files is a future refactor (low priority).

## 5. Cytocast adoption (post-hoc)

Cytos was not originally generated from cytocast. We "adopt" it:

1. Generate the `.cytognosis-config.yaml` matching cytos's current setup.
2. Run `copier copy --vcs-ref=v2.0.0-rc1 --skip-if-exists` to register cytos with the template (creates `.copier-answers.yml` without overwriting).
3. Subsequent `copier update` calls will apply template changes (e.g., updated workflows, hook updates) while preserving cytos's hand-authored content.

`.cytognosis-config.yaml` for cytos:

```yaml
cytocast_version: 2.0.0-rc1
profile: cytos
project_name: cytos

cytoskeleton:
  ref: v2.0.0-rc1
  env: cytognosis
  components_extra: []

skills:
  defaults:
    - cytognosis-org
    - cytognosis-orchestrator
    - cytognosis-dev
    - python-pro
    - bioinformatics
    - documents/markdown-conversion
    - documents/diagramming
    - science/healthcare-ai
    - science/visualization
  optional:
    - science/fhir-developer-skill
    - ai-ml/deep-learning
    - ai-ml/data-io

schemas:
  ref: v2.0.0-rc1
  consume:
    - core/cytos.yaml
    - core/core.yaml
    # All domains consumed via wildcard
    - domains/*

templates:
  - package-python  # cytos is a Python package
```

## 6. DVC update to tier-aware remotes

Cytos currently has `dvc.yaml` with 9 stages. Update its DVC remote config to point at the tier-aware bucket (per cytognosis-data skill).

Tier classification for cytos data:
- **Raw sources** (UMLS, SNOMED, etc.): mixed Tier 2/3 depending on license; SNOMED is controlled (license required), UMLS is API-key controlled, BioLink/Monarch are public Tier 3.
- **Interim, normalized, harmonized**: Tier 2 (derivatives of mixed-tier sources).
- **KG snapshots**: Tier 2 (controlled by license terms of input sources).

Default DVC remote: `gs://cytognosis-data/dvc/cytos/`.

Tier 1 (PHI) is NOT applicable to cytos (cytos handles public + controlled-access biomedical data, not patient-identifiable).

## 7. Inherit _shared/ workflows

After Phase 3 has cytocast `_shared/.github/workflows/` published, cytos's local workflows can switch to calling them:

```yaml
# .github/workflows/ci.yml
name: CI
on: [push, pull_request]
jobs:
  call:
    uses: cytognosis/cytocast/.github/workflows/_shared_ci.yml@v2.0.0-rc1
    with:
      python_versions: '["3.13", "3.14"]'
```

This makes cytos auto-update its CI when cytocast publishes a new `_shared/` version.

## 8. What we are NOT doing

- **NOT rewriting any business logic** — KGBuilder, scholarly parsers, genomics ingestion all stay.
- **NOT changing the public CLI** — all 14 command groups preserved.
- **NOT regenerating from cytocast** — cytos's hand-authored code is the source of truth.
- **NOT publishing to PyPI** — Phase 10.
- **NOT changing modeling module names** — just adding stub-status docstrings.
- **NOT deleting cytos/schemas/ yet on the originals** — the refactor branch in /refactor/cytos/ does it; originals untouched.

## 9. Verification

See `04_verification.md`. Critical:
- Cytos still builds and tests pass.
- `cytos schema` CLI commands work against cytoskeleton-submodule schemas.
- All 9 DVC stages execute end-to-end on a test cohort.
- Design docs are reconciled (no contradictions in canonical files).

## 10. Handoff

After Phase 6:
- Cytos is the first major package to consume the refactored stack.
- Confidence to apply same pattern to Yar (Phase 7) and future neuro-* repos.
- Existing cytos users see no API change; build process slightly different (`uv sync` requires submodule init).

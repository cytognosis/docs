# 06 — Cytos Transition — Execution Checklist

Sandbox: `/home/mohammadi/repos/cytognosis/refactor/cytos/`

## 1. Setup

### 1.1 Branch
```bash
cd /home/mohammadi/repos/cytognosis/refactor/cytos
git fetch upstream
git checkout -b refactor/v2-cytoskeleton-integration upstream/main
```

### 1.2 Venv
```bash
uv venv .venv && source .venv/bin/activate
uv pip install -e ".[dev]"
uv pip freeze > scratch/refactor-requirements.txt
```

### 1.3 Verify prerequisites
```bash
test -d /home/mohammadi/repos/cytognosis/refactor/cytoskeleton/schemas && echo "schemas migrated"
test -d /home/mohammadi/repos/cytognosis/refactor/cytocast/_shared && echo "shared workflows present"
test -f /home/mohammadi/repos/cytognosis/refactor/cytoskeleton/skills/operational/cytognosis-data/SKILL.md && echo "data skill ready"
```

## 2. Consolidate design docs

### 2.1 Move cytos/design/ → cytos/docs/design/
```bash
mkdir -p docs/design/historical
git mv design docs/design  # rename
```

### 2.2 Copy v1 historical docs
```bash
SRC=/home/mohammadi/Documents/Cytognosis/Infra\ and\ design/cytos_drafts
cp "$SRC/v1/01_cytos_package_design.md" docs/design/historical/v1-full-package-design.md
cp "$SRC/v1/04_foundation_model_architecture.md" docs/design/historical/v1-foundation-model-architecture.md
cp "$SRC/v2/01_cytos_package_design.md" docs/design/historical/v2-data-only-package-design.md
```

### 2.3 Author decision_log.md
```bash
bash 03_scripts/seed_decision_log.sh
```

The script creates `docs/design/decision_log.md` documenting reconciliations between v1/v2/current (table in 01_plan_prose.md §2).

### 2.4 Rename EXECUTION_PLAN.md → PIPELINE.md
```bash
git mv docs/design/EXECUTION_PLAN.md docs/design/PIPELINE.md
```

### 2.5 Rewrite docs/design/README.md
```bash
bash 03_scripts/rewrite_design_readme.sh
```

Updates to: reference cytoskeleton submodule for schemas, point at decision_log for v1/v2 historical context, link to historical/ for foundation model architecture.

### 2.6 Commit
```bash
git add docs/design/
git commit -m "refactor(plan-phase-6-step-2): consolidate cytos design docs from /Infra/cytos_drafts + cytos/design into docs/design/"
```

## 3. Add cytoskeleton submodule

### 3.1 Add submodule pinned to v2.0.0-rc1
```bash
git submodule add https://github.com/cytognosis/cytoskeleton.git external/cytoskeleton
cd external/cytoskeleton
git checkout v2.0.0-rc1
cd ../..
git add .gitmodules external/cytoskeleton
```

### 3.2 Verify
```bash
ls external/cytoskeleton/schemas/domains/ | wc -l  # should be ≥ 30
ls external/cytoskeleton/skills/operational/  # should have cytognosis-data
```

### 3.3 Commit
```bash
git commit -m "feat(plan-phase-6-step-3): add cytoskeleton submodule pinned to v2.0.0-rc1"
```

## 4. Migrate schemas/ to symlink

### 4.1 Verify all cytoskeleton schemas match cytos's
```bash
python 03_scripts/compare_schemas.py
```

Compares cytos/schemas/ contents to external/cytoskeleton/schemas/ contents. Should be near-identical (allowing for minor differences in directory structure).

### 4.2 Remove cytos/schemas/ and create symlink
```bash
git rm -rf schemas/
ln -s external/cytoskeleton/schemas schemas
git add schemas
```

### 4.3 Verify CLI works with symlinked schemas
```bash
cytos schema --help
cytos schema generate  # should produce codegen
cytos validate linkml  # validates schemas via SchemaView
```

### 4.4 Verify imports still work
```bash
python -c "
from pathlib import Path
import yaml
# Old paths still resolve via symlink
schemas = list(Path('schemas/domains').glob('*.yaml'))
print(f'{len(schemas)} schemas accessible')
"
```

### 4.5 Run tests
```bash
nox -s test
```

### 4.6 Commit
```bash
git add -A
git commit -m "refactor(plan-phase-6-step-4): migrate cytos/schemas/ to symlink → external/cytoskeleton/schemas/"
```

## 5. Mark modeling modules as stubs

### 5.1 Add stub-status docstrings
```bash
python 03_scripts/mark_stub_modules.py
```

The script adds module-level docstring to `__init__.py` of stub-status modules:
- src/cytos/features/__init__.py
- src/cytos/models/__init__.py
- src/cytos/train/__init__.py
- src/cytos/evaluate/__init__.py
- src/cytos/infer/__init__.py
- src/cytos/kg_embed/__init__.py (or wherever it lives)

### 5.2 Add design/STATUS.md
```bash
cat > docs/design/STATUS.md << 'EOF'
# Module status

## Production-ready (actively used)
- `cli`, `sources`, `ingest`, `schema`, `harmonize`, `kg`, `validate`, `publish`, `services`, `scholarly`, `genomics`, `utils`

## Stub (designed; awaiting implementation)
- `features`, `models`, `train`, `evaluate`, `infer`, `kg_embed`, `rag`

Stubs are kept because cytos is the foundation kernel; modeling belongs here architecturally. Full implementation is deferred to cytos v2.x (post Yar refactor).

See `historical/v1-foundation-model-architecture.md` for the original design intent of modeling modules.
EOF
git add docs/design/STATUS.md
```

### 5.3 Commit
```bash
git add -A
git commit -m "docs(plan-phase-6-step-5): mark modeling modules as stub status with clear documentation"
```

## 6. Add .cytognosis-config.yaml (post-hoc cytocast adoption)

### 6.1 Generate .cytognosis-config.yaml from current state
```bash
cp 03_scripts/cytognosis-config.yaml.cytos .cytognosis-config.yaml
```

### 6.2 Register with cytocast via copier copy --skip-if-exists
```bash
# Run copier in mode that adopts existing project without overwriting
uvx --from /home/mohammadi/repos/cytognosis/refactor/cytocast copier copy \
  /home/mohammadi/repos/cytognosis/refactor/cytocast . \
  --data profile=cytos --data project_name=cytos \
  --vcs-ref v2.0.0-rc1 \
  --skip-if-exists --quiet
```

This writes:
- `.copier-answers.yml` (Copier's answer file)
- Selected `_shared/` workflow files (if they don't conflict with existing)

### 6.3 Add cytocast's _shared workflow references
```bash
bash 03_scripts/update_workflows_to_shared.sh
```

Updates `.github/workflows/*.yml` to reference cytocast's `_shared_*.yml` reusable workflows.

### 6.4 Verify
```bash
test -f .cytognosis-config.yaml && echo OK
test -f .copier-answers.yml && echo OK
nox -s lint typecheck test
```

### 6.5 Commit
```bash
git add .cytognosis-config.yaml .copier-answers.yml .github/
git commit -m "feat(plan-phase-6-step-6): adopt cytocast template post-hoc (add cytognosis-config + copier-answers + shared workflows)"
```

## 7. Update DVC remotes to tier-aware

### 7.1 Update .dvc/config
```bash
python 03_scripts/update_dvc_remotes.py --tier 2
```

The script:
- Reads current `.dvc/config`
- Updates `default` remote to `gs://cytognosis-data/dvc/cytos/`
- Adds tier-specific remotes:
  - `controlled` → `gs://cytognosis-data/dvc/cytos/controlled/`
  - `public` → `gs://cytognosis-public/dvc/cytos/`

### 7.2 Verify DVC operations
```bash
dvc remote list
# Should show: default (Tier 2), controlled (Tier 2), public (Tier 3)
dvc status
```

### 7.3 Commit
```bash
git add .dvc/config
git commit -m "refactor(plan-phase-6-step-7): update DVC remotes to tier-aware bucket structure"
```

## 8. Final validation

### 8.1 Full nox
```bash
nox -s lint typecheck test
```

### 8.2 End-to-end pipeline smoke
```bash
dvc dag  # shows DAG
# Note: full dvc repro requires data; skip in plan, document for manual verification
```

### 8.3 Schema codegen
```bash
cytos schema codegen --target=pydantic
# Should produce outputs in artifacts/pydantic/
```

### 8.4 Verify originals untouched
```bash
cd /home/mohammadi/repos/cytognosis/cytos && git status
```

### 8.5 Tag
```bash
cd /home/mohammadi/repos/cytognosis/refactor/cytos
git tag v$(grep version pyproject.toml | head -1 | cut -d'"' -f2)-refactor-rc1 -m "Phase 6: cytoskeleton integration"
```

### 8.6 Summary
```bash
bash 03_scripts/final_state_summary.sh > scratch/phase-6-summary.txt
```

## Halt criteria

- Tests fail after symlink change (likely schemas issue → revert symlink, troubleshoot)
- CLI commands fail (`cytos schema generate` etc.) — schemas indirection broken
- DVC config rejects updated remotes
- Design doc consolidation introduces contradictions (manual review)

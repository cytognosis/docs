# 06 — Cytos Transition — Verification

## V1 — Submodule + schemas

| Check | Expected | Command |
|---|---|---|
| external/cytoskeleton submodule pinned | v2.0.0-rc1 | `cd external/cytoskeleton && git describe --tags` |
| Symlink cytos/schemas → external/cytoskeleton/schemas | yes | `ls -la schemas \| grep "^l"` |
| Schema files accessible | ≥ 30 in domains/ | `ls schemas/domains/*.yaml \| wc -l` |
| LinkML SchemaView reads via symlink | success | `python -c "from linkml_runtime.utils.schemaview import SchemaView; sv = SchemaView('schemas/core/cytos.yaml'); print(len(list(sv.all_classes())))"` |

## V2 — Design docs consolidation

| Check | Expected | Command |
|---|---|---|
| design/ renamed to docs/design/ | yes | `test -d docs/design && test ! -d design` |
| Historical docs present | 3 | `ls docs/design/historical/*.md \| wc -l` ≥ 3 |
| decision_log.md present | yes | `test -f docs/design/decision_log.md` |
| EXECUTION_PLAN renamed to PIPELINE.md | yes | `test -f docs/design/PIPELINE.md && test ! -f docs/design/EXECUTION_PLAN.md` |
| design/README.md mentions cytoskeleton | yes | `grep -i cytoskeleton docs/design/README.md` |

## V3 — Stub status

| Check | Expected | Command |
|---|---|---|
| Modeling modules have STATUS docstring | yes (5+ modules) | `grep -l "STATUS: stub" src/cytos/{features,models,train,evaluate,infer}/__init__.py \| wc -l` ≥ 5 |
| docs/design/STATUS.md exists | yes | `test -f docs/design/STATUS.md` |

## V4 — Cytocast adoption

| Check | Expected | Command |
|---|---|---|
| .cytognosis-config.yaml at root | yes | `test -f .cytognosis-config.yaml` |
| .copier-answers.yml at root | yes | `test -f .copier-answers.yml` |
| Profile=cytos in config | yes | `grep "profile: cytos" .cytognosis-config.yaml` |
| .github/workflows reference _shared | yes | `grep -E "cytognosis/cytocast/.github/workflows/_shared" .github/workflows/*.yml` |

## V5 — DVC

| Check | Expected | Command |
|---|---|---|
| Default remote is cytognosis-data | yes | `dvc remote list \| grep "gs://cytognosis-data"` |
| dvc.yaml stages parse | success | `dvc dag` |

## V6 — Functionality preserved

| Check | Expected | Command |
|---|---|---|
| `cytos --help` works | success | `cytos --help` |
| `cytos schema --help` | success | `cytos schema --help` |
| `cytos schema codegen --target=pydantic --dry-run` | success | (above command) |
| nox -s lint passes | green | `nox -s lint` |
| nox -s typecheck passes | green | `nox -s typecheck` |
| nox -s test passes | green | `nox -s test` |

## V7 — Originals untouched

| Check | Expected | Command |
|---|---|---|
| /repos/cytognosis/cytos unchanged | clean | `cd /home/mohammadi/repos/cytognosis/cytos && git status` |
| /repos/cytognosis/cytoskeleton not refactored copy | yes | (it's a separate clone) |

## Halt criteria

- Schema operations fail after symlink (try copy fallback)
- Tests fail
- DVC config update breaks existing tracked data references
- Design docs have unresolved contradictions

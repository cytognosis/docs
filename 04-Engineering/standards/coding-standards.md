# Cytos Standards Reference

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: engineers
> **Tags**: `engineering`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)

> Canonical coding standards for all Cytognosis Python projects.
> Derived from the cytos repo, which serves as the reference implementation.

## Build System

| Standard | Value | Where Enforced |
|----------|-------|---------------|
| Build backend | `hatchling>=1.21` | `pyproject.toml` `[build-system]` |
| Package layout | `src/` layout (e.g., `src/cytos/`) | `pyproject.toml` `[tool.hatch.build]` |
| Python version | `>=3.13` | `pyproject.toml` `python_requires` |
| Version scheme | CalVer: `YYYY.M.PATCH` (e.g., `2026.5.0`) | `pyproject.toml` `version` |
| Package manager | `uv` | `uv sync`, `uv run`, `uv build` |
| Lock file | `uv.lock` (committed) | `.gitignore` excludes nothing |
| Task runner | `nox` with `uv` backend | `noxfile.py`, `nox.toml` |

## Linting (Ruff)

```toml
[tool.ruff]
target-version = "py313"
line-length = 88
src = ["src"]

[tool.ruff.lint]
select = ["E", "W", "F", "I", "UP", "B", "SIM", "RUF", "D", "ANN", "TCH"]
ignore = ["D100", "D104", "D105", "D107", "ANN101", "ANN102", "ANN401", "E501"]

[tool.ruff.lint.pydocstyle]
convention = "google"

[tool.ruff.lint.isort]
known-first-party = ["<package_name>"]
```

### Tiered Lint System

| Tier | Nox Session | Trigger | Behavior |
|------|------------|---------|----------|
| **Local** | `lint_local` | On save | `ruff check --fix` (auto-fix) |
| **Dev** | `lint_dev` | Pre-commit | `ruff check --fix` + `ruff format --check` |
| **CI** | `lint_ci` | PR/push | `ruff check` (no fix) + `ruff format --check` |
| **Release** | `lint_release` | Tag | `ruff check --select ALL` (strictest) |

## Type Checking (mypy)

```toml
[tool.mypy]
python_version = "3.13"
warn_return_any = true
warn_unused_configs = true
disallow_untyped_defs = true
packages = ["<package_name>"]
mypy_path = "src"
```

## Testing (pytest)

```toml
[tool.pytest.ini_options]
testpaths = ["tests"]
addopts = "-v --tb=short --strict-markers"
asyncio_mode = "auto"
markers = ["slow", "integration", "platform", "controlled"]
```

### Test Sessions

| Session | Scope | CI Gate |
|---------|-------|---------|
| `test_unit` | Unit tests only | ✅ Required |
| `test_integration` | Integration tests | ✅ Required |
| `test_platform` | Platform-specific | Optional |
| `test` | All tests | Manual |

### PR Verify Chain

```
lint_ci → typecheck → test_unit → test_integration
```

## Documentation (MkDocs)

```toml
# pyproject.toml [project.optional-dependencies]
docs = ["mkdocs-material>=9.5", "mkdocstrings[python]>=0.25"]
```

- Engine: mkdocs-material (dark mode, deep purple primary, pink accent)
- API docs: mkdocstrings with Python handler
- Deploy: `mkdocs gh-deploy --force` to GitHub Pages
- Nox sessions: `docs_build`, `docs_serve`, `docs_publish`

## Dependency Management

> [!CAUTION]
> **Never add dependencies to `pyproject.toml` directly.**
> Use: `cytoskeleton env build --env <environment_name>`

Dependencies are centralized in cytoskeleton. The workflow:
1. Add component to `cytoskeleton/components/<domain>/<component>.yaml`
2. Run `cytoskeleton env build --env <name>` to regenerate lockfiles
3. Run `uv sync` to install

## Schema System

- **Source of truth**: LinkML YAML in `schemas/`
- **Generated formats**: JSON-LD, Pydantic, JSON Schema, SHACL, OWL
- **Never hand-write** generated formats; always regenerate from LinkML
- Validation enums are DVC-tracked when large (>10KB)

## Git Conventions

| Convention | Value |
|-----------|-------|
| Commit style | Conventional commits (`feat:`, `fix:`, `docs:`, `refactor:`, `chore:`) |
| Branch format | `feat/{description}`, `fix/{description}` |
| PR workflow | Feature branch → squash merge to `main` |
| SSH safety | `GIT_SSH_COMMAND="ssh -o BatchMode=yes -o StrictHostKeyChecking=accept-new"` |

## Agent Configuration (`.agents/`)

Every project must have:
```
.agents/
├── config.yaml       # Project metadata, skill defaults, preferences
├── registry.yaml     # Skill catalog resolution
├── plugins/
│   ├── claude/instructions.md
│   └── gemini/instructions.md
└── skills/           # Symlinked skill stubs
```

Key config fields:
- `environment_strategy: cytoskeleton`
- `auto_format: true`, `auto_lint: true`
- `commit_style: conventional`
- Default skills: `cytognosis-project-dev, cytognosis-python-standards`

## Nox Session Catalog

Standard sessions every project should have:

| Category | Sessions |
|----------|----------|
| Quality | `format`, `lint_local`, `lint_dev`, `lint_ci`, `typecheck`, `security` |
| Tests | `test_unit`, `test_integration`, `test` |
| Docs | `docs_build`, `docs_serve` |
| CI | `pr_verify` (chains lint_ci + typecheck + test_unit + test_integration) |

Additional sessions are project-specific (data pipelines, model training, etc.).

## Checklist for New Projects

1. [ ] Use `cytocast` to scaffold from the appropriate profile
2. [ ] Verify `.agents/config.yaml` has correct environment_name
3. [ ] Run `cytoskeleton env build --env <name>` for dependencies
4. [ ] Verify ruff config matches this standard
5. [ ] Verify mypy config has `disallow_untyped_defs = true`
6. [ ] Add `pr_verify` nox session to CI
7. [ ] Set up MkDocs for user-facing documentation
8. [ ] Move spec/design docs to the `docs` repo

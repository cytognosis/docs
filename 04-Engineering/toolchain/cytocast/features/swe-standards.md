# Software Engineering Best Practices

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: engineers
> **Tags**: `engineering`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)

Cytocast codifies software engineering standards into every generated project, covering branching strategy, commit conventions, code review workflows, and progressive quality enforcement.

## Branching Strategy

```mermaid
gitgraph
    commit
    branch develop
    checkout develop
    commit
    branch feature/add-model
    checkout feature/add-model
    commit
    commit
    checkout develop
    merge feature/add-model
    checkout main
    merge develop tag:"v1.0.0"
```

### Branch Naming Conventions

| Prefix | Purpose | Example |
|:---|:---|:---|
| `feat/` | New feature | `feat/add-cell-classifier` |
| `fix/` | Bug fix | `fix/resolve-oom-error` |
| `docs/` | Documentation | `docs/update-api-reference` |
| `refactor/` | Code restructure | `refactor/split-data-module` |
| `chore/` | Maintenance | `chore/update-dependencies` |

## Commit Conventions

Cytocast projects follow [Conventional Commits](https://www.conventionalcommits.org/):

```bash
# Feature
git commit -m "feat: add biomarker detection pipeline"

# Bug fix
git commit -m "fix: resolve memory leak in data loader"

# Breaking change
git commit -m "feat!: redesign API for cell classification"

# With scope
git commit -m "feat(data): add streaming dataset support"
```

### Commit Types

| Type | Description | Changelog Section |
|:---|:---|:---|
| `feat` | New feature | Features |
| `fix` | Bug fix | Bug Fixes |
| `docs` | Documentation | Documentation |
| `refactor` | Code restructure | Code Refactoring |
| `test` | Test changes | Testing |
| `chore` | Maintenance | — |
| `perf` | Performance | Performance |
| `ci` | CI/CD changes | — |

## Code Review Workflow

### PR Quality Gates

Every pull request must pass:

1. **Contributed/Prod lint** (`nox -s lint_ci`): No auto-fixes allowed
2. **Test suite** (`nox -s test`): Full pytest matrix
3. **Peer review**: At least one approval

For releases, additional gates:

4. **Release lint** (`nox -s lint_release`): Strictest rules
5. **Type checking** (`nox -s type_ci`): Full type safety
6. **Full test matrix**: All supported Python versions

### Progressive Quality Enforcement

```
Developer laptop → Sandbox (permissive, auto-fix)
    ↓
Feature branch → Local Dev (imports + docstrings)
    ↓
Pull request → Contributed/Prod (strict, no auto-fix)
    ↓
Release tag → Release (strictest, naming + complexity)
```

## Pre-commit Integration

Pre-commit runs automatically on every `git commit`:

```yaml
# .pre-commit-config.yaml hooks (always present)
repos:
  - repo: local
    hooks:
      - id: formatting-check   # ruff format
      - id: linting-check      # ruff check --fix (Sandbox)
      - id: typing-check       # nox -s type_local (manual)
      - id: test-check          # nox -s test (manual)
```

### Running Manual Hooks

```bash
# Run type checking before committing
pre-commit run typing-check

# Run tests before committing
pre-commit run test-check

# Run all hooks including manual
pre-commit run --all-files --hook-stage manual
```

## Project Initialization

```bash
# One-command project setup
nox -s init_project

# This runs:
# 1. git init (if needed)
# 2. uv sync --all-extras
# 3. pre-commit install
```

## Security Practices

### Trusted Publishing (PyPI)

Release workflows use GitHub's trusted publishing (OIDC), avoiding stored API tokens:

```yaml
permissions:
  id-token: write

steps:
  - uses: pypa/gh-action-pypi-publish@release/v1
```

### Security Scanning

```bash
# Run bandit rules via Ruff
nox -s security

# Checks for:
# - Hardcoded passwords (S105)
# - SQL injection (S608)
# - Unsafe deserialization (S301)
# - Shell injection (S602)
```

## AI Agent Integration

Generated projects include AI agent configurations under `.agents/`:

```
.agents/
├── config.yaml              # Agent routing configuration
├── README.md                 # Agent usage guide
├── skills/                   # Reusable AI skills
│   ├── python-dev/
│   ├── testing/
│   └── healthcare-ai/
├── workflows/                # Automated workflows
│   ├── new-feature.md
│   └── environment-resolve.md
├── commands/                 # CLI-like agent commands
│   ├── setup.md
│   ├── test.md
│   └── lint.md
└── plugins/                  # IDE-specific configs
    ├── claude/
    ├── gemini/
    ├── cursor/
    └── windsurf/
```

[← Back to the Comparative Study](comparative_study.md)

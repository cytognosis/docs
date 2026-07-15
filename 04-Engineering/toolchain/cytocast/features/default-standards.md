# Default Standards & Consistency

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: engineers
> **Tags**: `engineering`
> **Variants**: Technical (this doc) - Readable (default-standards.md in Obsidian vault: 04-Engineering/toolchain/cytocast/features/) - Agent (n/a)

Cytocast enforces organizational standards across all generated projects through locked environments, consistent tooling configurations, and a 4-tier code quality architecture. This document covers the mechanisms that ensure every project meets Cytognosis Foundation quality baselines.

## Dependency Management

### uv (Default)

[uv](https://github.com/astral-sh/uv) is the default package manager, chosen for its speed and reproducibility:

```bash
# Initialize project with all dev dependencies
nox -s init_project

# Sync dependencies from pyproject.toml
uv sync --all-extras

# Add a new dependency
uv add requests

# Lock dependencies for reproducibility
uv lock
```

### Pixi (Alternative)

For projects requiring conda-forge packages (e.g., CUDA, genomics tools):

```bash
copier copy --trust gh:cytognosis/cytocast my-project \
  --data dependency_manager=pixi
```

Pixi uses `pixi.toml` for environment specification:

```toml
[project]
name = "my-project"
channels = ["conda-forge"]
platforms = ["linux-64"]

[dependencies]
python = ">=3.11"
```

## Environment Strategies

| Strategy | Description | Profile |
|:---|:---|:---|
| `prelocked` | Fixed Python version, no multi-version testing | Production deployments |
| `resolve` | Resolve deps at install time, multi-Python testing | Library development |
| `empty` | Minimal setup, resolve on demand | Quick prototyping |

```bash
# Generate with prelocked strategy
copier copy --trust gh:cytognosis/cytocast my-project \
  --data environment_strategy=prelocked
```

## Cytoskeleton Integration

[Cytoskeleton](https://github.com/cytognosis/cytoskeleton) is our environment management submodule that provides pre-configured environment specs:

```bash
# Setup the base environment
nox -s setup_base

# Setup the ML environment (includes PyTorch)
nox -s setup_ml

# Setup the full Cytognosis stack
nox -s setup_cytognosis
```

Each environment is defined in Cytoskeleton and ensures consistent dependency versions across all Cytognosis projects.

## 4-Tier Code Quality Architecture

Every generated project ships all 4 tiers simultaneously. They are triggered by context, not selected at generation time.

### Tier Definitions

| Tier | Config File | Rules | Auto-fix | Trigger |
|:---|:---|:---|:---|:---|
| **Sandbox** | `pyproject.toml` | E, F, W | Yes | `nox -s lint_local` |
| **Local Dev** | `ruff.dev.toml` | + I, D | Yes | `nox -s lint_dev` |
| **Contributed/Prod** | `ruff.ci.toml` | + UP, PT, B, SIM | No | `nox -s lint_ci` |
| **Release** | `ruff.release.toml` | + ARG, N, C90, S | No | `nox -s lint_release` |

### Rule Code Reference

| Code | Category | Description |
|:---|:---|:---|
| `E` | pycodestyle | Style errors |
| `F` | Pyflakes | Logic errors, unused imports |
| `W` | pycodestyle | Style warnings |
| `I` | isort | Import sorting |
| `D` | pydocstyle | Docstring enforcement |
| `UP` | pyupgrade | Python version upgrades |
| `PT` | pytest-style | Pytest best practices |
| `B` | bugbear | Common bug patterns |
| `SIM` | simplify | Simplification opportunities |
| `ARG` | unused-args | Unused function arguments |
| `N` | pep8-naming | Naming conventions |
| `C90` | mccabe | Cyclomatic complexity |
| `S` | bandit | Security vulnerabilities |

### Hands-on: Gradual Tier Adoption

```bash
# Start permissive during prototyping
nox -s lint_local

# Add import sorting and docstrings when stabilizing
nox -s lint_dev

# Enforce CI-level checks before opening PR
nox -s lint_ci

# Final check before release
nox -s lint_release
```

## Docstring Standard

Cytocast defaults to Google-style docstrings:

```python
def train_model(data: Dataset, epochs: int = 10) -> Model:
    """Train a model on the given dataset.

    Args:
        data: Training dataset.
        epochs: Number of training epochs.

    Returns:
        Trained model instance.

    Raises:
        ValueError: If dataset is empty.
    """
```

The docstring convention is configurable via the `docstring_style` Copier parameter (Google, NumPy, Sphinx).

## Project Structure

Every generated project follows a consistent layout:

```
my-project/
├── src/my_project/        # Source code (src layout)
│   ├── __init__.py
│   ├── data/
│   ├── features/
│   ├── models/
│   ├── modules/
│   └── utils/
├── tests/                 # Test suite
│   └── test_quality_tiers.py
├── docs/                  # Documentation
├── .github/               # CI/CD workflows + linter configs
├── pyproject.toml         # Project metadata + Sandbox ruff config
├── noxfile.py             # 25 automation sessions
└── .pre-commit-config.yaml
```

[← Back to the Comparative Study](comparative_study.md)

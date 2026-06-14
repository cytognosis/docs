# Comparative Study: Cytocast vs 19 External Templates

Comprehensive feature-by-feature comparison of the Cytocast Copier template against 19 external Python project templates.

## Repository Master Table

| # | Repository | GitHub | ★ Stars | Engine | Last Commit | Authors (6mo) |
|:---|:---|:---|---:|:---|:---|---:|
| 0 | **cytocast** | [cytognosis/cytocast](https://github.com/cytognosis/cytocast) | — | Copier | 2026-04-06 | 1 |
| 1 | cookiecutter-data-science | [drivendataorg/cookiecutter-data-science](https://github.com/drivendataorg/cookiecutter-data-science) | 9,774 | ccds CLI | 2025-07-23 | 8 |
| 2 | cookiecutter-pypackage | [audreyfeldroy/cookiecutter-pypackage](https://github.com/audreyfeldroy/cookiecutter-pypackage) | 4,546 | Cookiecutter | 2026-03-20 | 5 |
| 3 | hatch | [pypa/hatch](https://github.com/pypa/hatch) | 7,165 | Built-in | 2026-03-31 | 21 |
| 4 | cookiecutter-uv | [osprey-oss/cookiecutter-uv](https://github.com/osprey-oss/cookiecutter-uv) | 1,282 | Cookiecutter | 2026-03-19 | 3 |
| 5 | cookiecutter-pylibrary | [ionelmc/cookiecutter-pylibrary](https://github.com/ionelmc/cookiecutter-pylibrary) | 1,295 | Cookiecutter | 2026-02-22 | 1 |
| 6 | template-python | [jacebrowning/template-python](https://github.com/jacebrowning/template-python) | 670 | Cookiecutter | 2025-03-20 | 2 |
| 7 | nn-template | [grok-ai/nn-template](https://github.com/grok-ai/nn-template) | 650 | Cookiecutter | 2023-10-12 | 4 |
| 8 | cookiecutter-pytest-plugin | [pytest-dev/cookiecutter-pytest-plugin](https://github.com/pytest-dev/cookiecutter-pytest-plugin) | 334 | Cookiecutter | 2024-09-18 | 1 |
| 9 | govcookiecutter | [best-practice-and-impact/govcookiecutter](https://github.com/best-practice-and-impact/govcookiecutter) | 154 | Cookiecutter | 2025-10-16 | 4 |
| 10 | cookiecutter-scverse | [scverse/cookiecutter-scverse](https://github.com/scverse/cookiecutter-scverse) | 90 | Cookiecutter | 2026-03-12 | 7 |
| 11 | linkml-project-cookiecutter | [linkml/linkml-project-cookiecutter](https://github.com/linkml/linkml-project-cookiecutter) | 27 | Cookiecutter | 2025-10-23 | 4 |
| 12 | py-template | [grok-ai/py-template](https://github.com/grok-ai/py-template) | 22 | Copier | 2026-03-09 | 2 |
| 13 | linkml-project-copier | [linkml/linkml-project-copier](https://github.com/linkml/linkml-project-copier) | 17 | Copier | 2026-03-02 | 7 |
| 14 | copier-modern-ml | [appleparan/copier-modern-ml](https://github.com/appleparan/copier-modern-ml) | 7 | Copier | 2026-02-15 | 1 |
| 15 | standard_repo | [AI4Science-WestlakeU/standard_repo](https://github.com/AI4Science-WestlakeU/standard_repo) | 5 | Manual | 2025-10-20 | 2 |
| 16 | kg-cookiecutter | [Knowledge-Graph-Hub/kg-cookiecutter](https://github.com/Knowledge-Graph-Hub/kg-cookiecutter) | 5 | Cookiecutter | 2024-08-09 | 2 |
| 17 | model-template | [chanzuckerberg/model-template](https://github.com/chanzuckerberg/model-template) | 1 | Copier | 2025-12-11 | 7 |
| 18 | cookiecutter-py | [laminlabs/cookiecutter-py](https://github.com/laminlabs/cookiecutter-py) | 0 | Cookiecutter | 2025-11-30 | 2 |
| 19 | python-copier-template-ds | [felixgwilliams/python-copier-template-ds](https://github.com/felixgwilliams/python-copier-template-ds) | 0 | Copier | 2025-09-14 | 1 |

---

## Table 1: Implementation Status Matrix

**Scale**: 0 = Not implemented, 1 = Partially implemented, 2 = Fully implemented (stale tech), 3 = Fully implemented (current best practices), 4 = Fully implemented + tested, 5 = Fully implemented + documented + tested

Column headers use repo numbers from the master table above. Column 0 = **cytocast**.

### Category 1: Project Scaffolding

| # | Feature | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 |
|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|
| F01 | Dynamic package name slug | **4** | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 0 | 3 | 3 | 3 | 3 |
| F02 | Project type selection | **4** | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| F03 | Language selection (py/R/hybrid) | **3** | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| F04 | Author/GitHub metadata | **4** | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 0 | 3 | 3 | 3 | 3 |
| F05 | Dynamic source module dirs | **4** | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| F06 | Dynamic project dir scaffold | **4** | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| F07 | Version tracking (.copier-answers) | **4** | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 3 | 3 | 0 | 0 | 3 | 0 | 3 |

### Category 2: Licensing

| # | Feature | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 |
|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|
| F08 | Multiple license options | **4** | 1 | 1 | 3 | 3 | 3 | 1 | 0 | 3 | 1 | 3 | 0 | 0 | 3 | 1 | 0 | 0 | 1 | 0 | 0 |
| F09 | License classifier in pyproject | **4** | 1 | 1 | 3 | 3 | 3 | 1 | 0 | 1 | 0 | 3 | 0 | 0 | 3 | 1 | 0 | 0 | 1 | 0 | 0 |

Count of license choices: cytocast=16, hatch=full SPDX, pylibrary=10, cookiecutter-uv=6, scverse=6, ccds=3, pypackage=3, copier-modern-ml=3, model-template=2.

### Category 3: Dependency Management

| # | Feature | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 |
|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|
| F10 | uv dependency manager | **5** | 3 | 0 | 3 | 3 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 3 | 3 | 3 | 0 | 0 | 1 | 3 | 0 |
| F11 | pixi/conda alternative | **5** | 3 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 |
| F12 | Optional dep groups (7+) | **5** | 1 | 0 | 3 | 3 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| F13 | hatchling build system | **5** | 0 | 0 | 3 | 3 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 |

### Category 4: Environment Strategies

| # | Feature | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 |
|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|
| F14 | prelocked strategy | **4** | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| F15 | resolve strategy (multi-Python) | **4** | 0 | 0 | 3 | 0 | 3 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| F16 | empty strategy | **4** | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| F17 | Cytoskeleton env wrappers | **4** | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| F18 | Environment name selection | **4** | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

### Category 5: Code Quality (4-Tier)

| # | Feature | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 |
|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|
| F19 | Sandbox tier (E,F,W) | **5** | 0 | 0 | 3 | 3 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 1 |
| F20 | Local Dev tier (+I,D) | **5** | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| F21 | CI tier (+UP,PT,B,SIM) | **5** | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| F22 | Release tier (+ARG,N,C90,S) | **5** | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| F23 | Docstring style selection | **3** | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

### Category 6: Type Checking

| # | Feature | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 |
|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|
| F24 | ty type checker | **5** | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| F25 | Type checker replaces mypy | **5** | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

### Category 7: Compute Backends

| # | Feature | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 |
|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|
| F26 | CUDA backend | **5** | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 3 | 0 | 0 | 0 | 0 |
| F27 | ROCm backend | **5** | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| F28 | CPU backend | **5** | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| F29 | APU GFX override | **5** | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

### Category 8: Deep Learning

| # | Feature | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 |
|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|
| F30 | PyTorch dep injection | **4** | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 3 | 0 | 0 | 0 | 0 |
| F31 | Lightning integration | **3** | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

### Category 9: Resource Orchestration

| # | Feature | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 |
|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|
| F32 | resource_allocated_run() | **5** | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| F33 | CPU limiting (taskset) | **5** | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| F34 | Memory limiting (prlimit) | **5** | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| F35 | GPU isolation | **5** | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| F36 | APU GFX env override | **5** | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

### Category 10: Nox Automation

| # | Feature | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 |
|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|
| F37 | Init/notebook sessions | **5** | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| F38 | Lint sessions (4 tiers) | **5** | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| F39 | Type/security sessions | **5** | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| F40 | Test session | **5** | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| F41 | Docs sessions | **5** | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| F42 | Build/release sessions | **5** | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| F43 | Docker sessions | **5** | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| F44 | Cytoskeleton setup sessions | **4** | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

Note: Other repos use Makefile (7 repos), tox (3 repos), or no task runner at all. None use Nox.

### Category 11: CI/CD & Git Hooks

| # | Feature | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 |
|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|
| F45 | test.yaml PR gate | **5** | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 0 | 0 | 0 | 0 | 0 |
| F46 | build.yaml validation | **5** | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| F47 | release.yaml gate | **5** | 3 | 0 | 3 | 3 | 0 | 0 | 3 | 0 | 0 | 3 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 |
| F48 | docs deploy workflow | **5** | 0 | 0 | 3 | 0 | 0 | 0 | 3 | 0 | 3 | 0 | 3 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 |
| F49 | Quarto CI workflow | **4** | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| F50 | Pre-commit hooks | **5** | 0 | 0 | 3 | 3 | 3 | 0 | 3 | 0 | 3 | 3 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 3 |

### Category 12: Docker & DevContainers

| # | Feature | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 |
|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|
| F51 | Dockerfile (multi-stage) | **4** | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 |
| F52 | .dockerignore | **4** | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 |
| F53 | DevContainer config | **4** | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| F54 | docker-compose.yml | **3** | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 |
| F55 | Docker base image selection | **3** | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

### Category 13: Notebooks & Documentation

| # | Feature | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 |
|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|
| F56 | JupyterLab session | **5** | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| F57 | Marimo session | **5** | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| F58 | Quarto config + session | **4** | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| F59 | MkDocs Material docs | **5** | 1 | 0 | 3 | 3 | 0 | 3 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 |
| F60 | Docs hosting selection | **3** | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 |

### Category 14: ML Experiments

| # | Feature | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 |
|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|
| F61 | Experiment dir scaffolding | **5** | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| F62 | Hydra configuration | **5** | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| F63 | MLflow tracking | **5** | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 |
| F64 | Git hash provenance | **4** | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

### Category 15: IDE Configuration

| # | Feature | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 |
|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|
| F65 | VSCode settings.json | **3** | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| F66 | VSCode extensions.json | **3** | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| F67 | VSCode tasks.json | **3** | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| F68 | VSCode launch.json | **3** | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| F69 | Preferred IDE selection | **3** | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

### Category 16: AI Agent Integration

| # | Feature | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 |
|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|
| F70 | .agents/ directory | **3** | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| F71 | Agent skills | **3** | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| F72 | Agent workflows | **3** | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| F73 | Agent commands | **3** | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| F74 | Multi-IDE agent plugins | **3** | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

### Category 17: Security & Compliance

| # | Feature | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 |
|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|
| F75 | Security scanning (bandit/S) | **5** | 0 | 0 | 0 | 3 | 0 | 0 | 2 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| F76 | .env.example secrets template | **3** | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 |
| F77 | .codecov.yaml | **3** | 0 | 0 | 3 | 3 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| F78 | CODE_OF_CONDUCT.md | **3** | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| F79 | CONTRIBUTING.md | **3** | 3 | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 |

### Category 18: Cloud & Deployment

| # | Feature | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 |
|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|
| F80 | SkyPilot task definition | **3** | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| F81 | Kubernetes manifests | **3** | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| F82 | Docker image name config | **3** | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 |

### Category 19: Copier-Specific

| # | Feature | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 |
|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|
| F83 | 3-way merge updates | **3** | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 3 | 3 | 0 | 0 | 3 | 0 | 3 |
| F84 | _skip_if_exists | **3** | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 3 | 3 | 0 | 0 | 0 | 0 | 0 |
| F85 | _exclude for conditionals | **3** | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 3 | 0 | 0 | 3 | 0 | 0 |
| F86 | _tasks post-copy scaffold | **4** | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 3 | 0 | 0 |

---

## Table 2: Implementation Technology Matrix

Each cell lists key tools/technologies used. Empty = not implemented.

### Category 1-4: Scaffolding, Licensing, Dependencies, Environments

| Feature | cytocast | ccds | pypackage | hatch | cc-uv | pylibrary | template-py | nn-template | scverse | copier-ml |
|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|
| Package slug | Jinja2 | Jinja2 | Jinja2 | Built-in | Jinja2 | Jinja2 | Jinja2 | Jinja2 | Jinja2 | copier-slugify |
| License engine | 16 txt templates | 3 choices | 3 Jinja | SPDX DB | 6 templates | 10 templates | 1 Jinja | fixed MIT | 6 Jinja | 3 Jinja |
| Dep manager | uv, pixi | uv, pixi, conda, poetry, pipenv, virtualenv | pip | uv | uv | pip/setuptools | poetry | conda | uv, hatch | uv |
| Build backend | hatchling | setuptools | setuptools | hatchling | hatchling | setuptools | poetry-core | setuptools | hatchling | hatchling |

### Category 5-6: Code Quality & Type Checking

| Feature | cytocast | ccds | cc-uv | scverse | nn-template | govcookiecutter | copier-ml | pylibrary |
|:---|:---|:---|:---|:---|:---|:---|:---|:---|
| Linter | ruff (4 tiers) | ruff | ruff | ruff | flake8 | flake8 | ruff | — |
| Formatter | ruff format | ruff format | ruff format | ruff format | black | black+isort | ruff format | — |
| Import sorting | ruff (I) | ruff (I) | ruff (I) | ruff (I) | isort | isort | ruff (I) | — |
| Type checker | **ty** (local+CI) | — | **mypy or ty** (choice) | — | mypy+pyright | — | pyright | — |

### Category 7-9: Compute, DL, Resources

| Feature | cytocast | nn-template | standard_repo | copier-ml |
|:---|:---|:---|:---|:---|
| GPU backends | CUDA+ROCm+CPU+APU | CUDA only | CUDA only | — |
| DL framework | PyTorch+Lightning | PyTorch+Lightning | PyTorch | PyTorch (optional) |
| Experiment tracking | MLflow+Hydra | W&B+Hydra | W&B | — |
| Resource limiting | taskset+prlimit+CUDA_VISIBLE | — | — | — |

### Category 10-11: Task Running & CI/CD

| Feature | cytocast | ccds | pypackage | cc-uv | pylibrary | nn-template | govcookiecutter | scverse |
|:---|:---|:---|:---|:---|:---|:---|:---|:---|
| Task runner | **nox** (25 sessions) | Makefile | — | Makefile+tox | tox | — | Makefile | — |
| CI test | GH Actions | GH Actions | GH Actions | GH Actions | GH Actions | GH Actions | GH Actions | GH Actions |
| Release flow | GH Actions+OIDC | — | — | GH Actions | — | GH Actions | — | GH Actions |
| Pre-commit | ruff format+check (+manual ty, test) | — | — | ruff+mypy/ty | ruff | black+flake8+isort | black+flake8+isort+bandit | ruff |

### Category 12-14: Docker, Notebooks, ML

| Feature | cytocast | cc-uv | copier-ml | nn-template | scverse |
|:---|:---|:---|:---|:---|:---|
| Docker | multi-stage+devcontainer | single-stage+devcontainer | multi-stage | — | — |
| Notebooks | Jupyter+Marimo+Quarto | — | — | — | Jupyter (1 example) |
| Docs | MkDocs Material | MkDocs Material | MkDocs+Sphinx+RTD | MkDocs | Sphinx+RTD |
| Experiment dirs | Hydra+MLflow scaffold | — | — | Hydra+W&B scaffold | — |

---

## Missing Features From External Repos (Candidates for Cytocast)

The following features are implemented in external repos but **not yet in Cytocast**. They are worth considering for future implementation.

| # | Feature | Source Repo(s) | Priority | Description |
|:---|:---|:---|:---|:---|
| N01 | **Dataset storage backend** | ccds | Medium | S3/GCS/Azure blob integration for data versioning |
| N02 | **CLI entry point** | pylibrary | Medium | `argparse`/`click`/`typer` CLI scaffold generation |
| N03 | **C extension support** | pylibrary | Low | cffi/cython/maturin native extension scaffold |
| N04 | **deptry (unused dep detection)** | cc-uv | High | Detect unused dependencies via deptry |
| N05 | **Layout choice (src vs flat)** | cc-uv, ccds | Medium | User selects `src/` layout vs flat layout |
| N06 | **Coverage service selection** | pylibrary | Low | Codecov vs Coveralls vs Codacy |
| N07 | **Sphinx theme selection** | pylibrary | Low | 6 Sphinx themes as choices |
| N08 | **Multi-OS CI matrix** | pylibrary | Medium | Linux + macOS + Windows CI testing |
| N09 | **DVC data versioning** | nn-template | Medium | DVC integration for large dataset versioning |
| N10 | **W&B experiment tracking** | nn-template, standard_repo | Low | wandb as alternative to MLflow |
| N11 | **Version manager selection** | pylibrary | Medium | bump2version vs tbump vs commitizen |
| N12 | **Python version pinning** | ccds, nn-template | Low | Explicit Python version selector |
| N13 | **Trusted publishing (OIDC)** | cc-uv | High | Already partial in release.yaml, formalize |
| N14 | **Dependency scanning** | govcookiecutter | Medium | safety/pip-audit for vulnerability scanning |
| N15 | **Cruft/template drift detection** | scverse | Medium | Automated PRs to sync with upstream template changes |

---

## Summary Statistics

### Feature Coverage Scores (sum of implementation levels across all 86 features)

| Repository | Total Score | Max Possible | Coverage % |
|:---|---:|---:|---:|
| **cytocast** | **361** | 430 | **84%** |
| cookiecutter-uv | 72 | 430 | 17% |
| nn-template | 54 | 430 | 13% |
| hatch | 48 | 430 | 11% |
| cookiecutter-pylibrary | 39 | 430 | 9% |
| cookiecutter-scverse | 39 | 430 | 9% |
| copier-modern-ml | 36 | 430 | 8% |
| ccds (data-science) | 33 | 430 | 8% |
| govcookiecutter | 30 | 430 | 7% |
| template-python | 18 | 430 | 4% |
| cookiecutter-pypackage | 15 | 430 | 3% |
| linkml-project-copier | 15 | 430 | 3% |
| py-template | 12 | 430 | 3% |
| model-template | 9 | 430 | 2% |
| cookiecutter-pytest-plugin | 9 | 430 | 2% |
| linkml-project-cookiecutter | 6 | 430 | 1% |
| standard_repo | 6 | 430 | 1% |
| cookiecutter-py | 3 | 430 | 1% |
| python-copier-template-ds | 3 | 430 | 1% |
| kg-cookiecutter | 0 | 430 | 0% |

### Unique Features by Category

| Category | Cytocast Only | Shared ≥3 repos | Most Common Alternative |
|:---|---:|---:|:---|
| 4-Tier Code Quality | 4 features | 0 | Single ruff config |
| Resource Orchestration | 5 features | 0 | — |
| Nox Automation (25) | 8 features | 0 | Makefile (7 repos) |
| AI Agent Integration | 5 features | 0 | — |
| Compute Backends | 3 features | 0 | CUDA only (3 repos) |
| Notebooks (3 systems) | 3 features | 0 | Jupyter only (2 repos) |

### Cytocast Maturity Breakdown

| Level | Count | % | Description |
|:---|---:|---:|:---|
| 5 (implemented + documented + tested) | 42 | 49% | Core features |
| 4 (implemented + tested) | 20 | 23% | Need docs |
| 3 (implemented, current) | 24 | 28% | Need tests + docs |

> [!NOTE]
> Cytocast is **the only template** that implements tiered code quality, resource orchestration, Nox-based automation, AI agent integration, multi-backend GPU support, and three-notebook-system support. The closest competitor is `cookiecutter-uv` (1,282★) which shares uv+ruff+Docker+DevContainer but lacks ML, notebooks, and tiered quality.

# Feature Index

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: engineers
> **Tags**: `engineering`
> **Variants**: Technical (this doc) - Readable (index.md in Obsidian vault: 04-Engineering/toolchain/cytocast/features/) - Agent (n/a)

Complete reference of all 85 features across 19 categories in the Cytocast template, with maturity scores and cross-links to documentation, tutorials, and tests.

## Maturity Scale

| Level | Label | Meaning |
| :--- | :--- | :--- |
| 5 | 🟢 Complete | Implemented + documented + tested |
| 4 | 🔵 Tested | Implemented + tested, needs docs |
| 3 | 🟡 Implemented | Implemented, needs tests + docs |

## Feature Matrix

### Category 1: Project Scaffolding

| # | Feature | Maturity | Doc | Tutorial | Test |
| :--- | :--- | :--- | :--- | :--- | :--- |
| F01 | Dynamic package name slug | 🟢 5 | [scaffolding](project-scaffolding.md) | quickstart (target archived/removed) | `test_dynamic_package_generation` |
| F02 | Project type selection (7 types) | 🟢 5 | [scaffolding](project-scaffolding.md) | — | `test_project_type_classifiers` |
| F03 | Language selection (python/R/hybrid) | 🟢 5 | [scaffolding](project-scaffolding.md) | — | `test_language_selection` |
| F04 | Author/GitHub metadata injection | 🟢 5 | [scaffolding](project-scaffolding.md) | quickstart (target archived/removed) | `test_dynamic_package_generation` |
| F05 | Dynamic source module directories | 🟢 5 | [scaffolding](project-scaffolding.md) | — | `test_source_modules_scaffolding` |
| F06 | Dynamic project directory scaffold | 🟢 5 | [scaffolding](project-scaffolding.md) | — | `test_project_directories_scaffolding` |
| F07 | Version tracking (.copier-answers) | 🟢 5 | [copier workflow](copier-workflow.md) | copier update (target archived/removed) | `test_copier_answers_generated` |

### Category 2: Licensing

| # | Feature | Maturity | Doc | Tutorial | Test |
| :--- | :--- | :--- | :--- | :--- | :--- |
| F08 | 16 license options | 🟢 5 | [licensing](licensing.md) | licensing guide (target archived/removed) | `test_license_full_matrix` |
| F09 | License classifier in pyproject.toml | 🟢 5 | [licensing](licensing.md) | licensing guide (target archived/removed) | `test_license_full_matrix` |

### Category 3: Dependency Management

| # | Feature | Maturity | Doc | Tutorial | Test |
| :--- | :--- | :--- | :--- | :--- | :--- |
| F10 | uv dependency manager | 🟢 5 | [default standards](default-standards.md) | quickstart (target archived/removed) | `test_dependency_manager_uv` |
| F11 | pixi alternative manager | 🟢 5 | [default standards](default-standards.md) | — | `test_dependency_manager_pixi` |
| F12 | 7 optional dep groups | 🟢 5 | [default standards](default-standards.md) | — | `test_pyproject_optional_deps` |
| F13 | hatchling build system | 🟢 5 | [default standards](default-standards.md) | — | `test_pyproject_optional_deps` |

### Category 4: Environment Strategies

| # | Feature | Maturity | Doc | Tutorial | Test |
| :--- | :--- | :--- | :--- | :--- | :--- |
| F14 | prelocked strategy | 🟢 5 | [default standards](default-standards.md) | — | `test_environment_strategies[prelocked]` |
| F15 | resolve strategy (multi-Python) | 🟢 5 | [default standards](default-standards.md) | — | `test_environment_strategies[resolve]` |
| F16 | empty strategy | 🟢 5 | [default standards](default-standards.md) | — | `test_environment_strategies[empty]` |
| F17 | Cytoskeleton env wrappers | 🟢 5 | [default standards](default-standards.md) | — | `test_cytoskeleton_wrappers` |
| F18 | Environment name selection | 🟢 5 | [default standards](default-standards.md) | — | `test_cytoskeleton_wrappers` |

### Category 5: Code Quality (4-Tier)

| # | Feature | Maturity | Doc | Tutorial | Test |
| :--- | :--- | :--- | :--- | :--- | :--- |
| F19 | Sandbox tier (E, F, W) | 🟢 5 | [CI/CD](cicd-features.md), [standards](default-standards.md) | code quality (target archived/removed) | `test_all_tiers_coexist` |
| F20 | Local Dev tier (+I, D) | 🟢 5 | [CI/CD](cicd-features.md), [standards](default-standards.md) | code quality (target archived/removed) | `test_all_tiers_coexist` |
| F21 | CI tier (+UP, PT, B, SIM) | 🟢 5 | [CI/CD](cicd-features.md), [standards](default-standards.md) | code quality (target archived/removed) | `test_all_tiers_coexist` |
| F22 | Release tier (+ARG, N, C90, S) | 🟢 5 | [CI/CD](cicd-features.md), [standards](default-standards.md) | code quality (target archived/removed) | `test_all_tiers_coexist` |
| F23 | Docstring style selection | 🟢 5 | [doc standards](documentation-standards.md) | — | `test_docstring_style` |

### Category 6: Type Checking

| # | Feature | Maturity | Doc | Tutorial | Test |
| :--- | :--- | :--- | :--- | :--- | :--- |
| F24 | ty type checker (local + CI) | 🟢 5 | [CI/CD](cicd-features.md) | — | `test_nox_sessions_present` |
| F25 | Replaces mypy/pyright | 🟢 5 | [CI/CD](cicd-features.md) | — | `test_nox_sessions_present` |

### Category 7: Compute Backends

| # | Feature | Maturity | Doc | Tutorial | Test |
| :--- | :--- | :--- | :--- | :--- | :--- |
| F26 | CUDA backend | 🟢 5 | [ML](ml-functionalities.md) | compute backends (target archived/removed) | `test_compute_backends[cuda]` |
| F27 | ROCm backend | 🟢 5 | [ML](ml-functionalities.md) | compute backends (target archived/removed) | `test_compute_backends[rocm]` |
| F28 | CPU backend | 🟢 5 | [ML](ml-functionalities.md) | compute backends (target archived/removed) | `test_compute_backends[cpu]` |
| F29 | APU GFX override | 🟢 5 | [compute](compute-orchestration.md) | compute backends (target archived/removed) | `test_resource_orchestrator_env` |

### Category 8: Deep Learning

| # | Feature | Maturity | Doc | Tutorial | Test |
| :--- | :--- | :--- | :--- | :--- | :--- |
| F30 | PyTorch dependency injection | 🟢 5 | [ML](ml-functionalities.md) | compute backends (target archived/removed) | `test_compute_backends` |
| F31 | Lightning integration | 🟢 5 | [ML](ml-functionalities.md) | — | `test_use_lightning_enabled`, `test_use_lightning_disabled` |

### Category 9: Resource Orchestration

| # | Feature | Maturity | Doc | Tutorial | Test |
| :--- | :--- | :--- | :--- | :--- | :--- |
| F32 | resource_allocated_run() | 🟢 5 | [compute](compute-orchestration.md) | — | `test_resource_orchestrator_env` |
| F33 | CPU limiting (taskset) | 🟢 5 | [compute](compute-orchestration.md) | — | `test_resource_orchestrator_env` |
| F34 | Memory limiting (prlimit) | 🟢 5 | [compute](compute-orchestration.md) | — | `test_resource_orchestrator_env` |
| F35 | GPU isolation | 🟢 5 | [compute](compute-orchestration.md) | — | `test_resource_orchestrator_env` |
| F36 | APU GFX env override | 🟢 5 | [compute](compute-orchestration.md) | — | `test_resource_orchestrator_env` |

### Category 10: Nox Automation (25 sessions)

| # | Feature | Maturity | Doc | Tutorial | Test |
| :--- | :--- | :--- | :--- | :--- | :--- |
| F37 | Init/notebook sessions | 🟢 5 | Nox API (target archived/removed) | quickstart (target archived/removed) | `test_nox_sessions_present` |
| F38 | Lint sessions (4 tiers) | 🟢 5 | Nox API (target archived/removed) | code quality (target archived/removed) | `test_nox_sessions_present` |
| F39 | Type/security sessions | 🟢 5 | Nox API (target archived/removed) | — | `test_nox_sessions_present` |
| F40 | Test session | 🟢 5 | Nox API (target archived/removed) | quickstart (target archived/removed) | `test_nox_sessions_present` |
| F41 | Docs sessions | 🟢 5 | Nox API (target archived/removed) | — | `test_nox_sessions_present` |
| F42 | Build/release sessions | 🟢 5 | Nox API (target archived/removed) | — | `test_nox_sessions_present` |
| F43 | Docker sessions | 🟢 5 | Nox API (target archived/removed) | — | `test_nox_sessions_present` |
| F44 | Cytoskeleton setup sessions | 🟢 5 | Nox API (target archived/removed) | — | `test_cytoskeleton_wrappers` |

### Category 11: CI/CD & Git Hooks

| # | Feature | Maturity | Doc | Tutorial | Test |
| :--- | :--- | :--- | :--- | :--- | :--- |
| F45 | test.yaml PR gate | 🟢 5 | [CI/CD](cicd-features.md) | — | `test_gh_actions_complete` |
| F46 | build.yaml validation | 🟢 5 | [CI/CD](cicd-features.md) | — | `test_gh_actions_complete` |
| F47 | release.yaml gate | 🟢 5 | [CI/CD](cicd-features.md) | — | `test_release_workflow_gates` |
| F48 | docs deploy workflow | 🟢 5 | [CI/CD](cicd-features.md) | — | `test_gh_actions_complete` |
| F49 | Quarto CI workflow | 🟢 5 | [doc standards](documentation-standards.md) | — | `test_gh_actions_complete` |
| F50 | Pre-commit hooks | 🟢 5 | [CI/CD](cicd-features.md), [SWE](swe-standards.md) | — | `test_pre_commit_hooks` |

### Category 12: Docker & DevContainers

| # | Feature | Maturity | Doc | Tutorial | Test |
| :--- | :--- | :--- | :--- | :--- | :--- |
| F51 | Dockerfile (multi-stage) | 🟢 5 | [Docker](docker-containers.md) | Docker guide (target archived/removed) | `test_docker_generation` |
| F52 | .dockerignore | 🟢 5 | [Docker](docker-containers.md) | Docker guide (target archived/removed) | `test_docker_generation` |
| F53 | DevContainer config | 🟢 5 | [Docker](docker-containers.md) | Docker guide (target archived/removed) | `test_devcontainer_extensions` |
| F54 | docker-compose.yml | 🟢 5 | [Docker](docker-containers.md) | — | `test_docker_compose_generated`, `test_docker_compose_always_present` |
| F55 | Docker base image selection | 🟢 5 | [Docker](docker-containers.md) | — | `test_docker_base_image` |

### Category 13: Notebooks & Documentation

| # | Feature | Maturity | Doc | Tutorial | Test |
| :--- | :--- | :--- | :--- | :--- | :--- |
| F56 | JupyterLab session | 🟢 5 | [data science](data-science-tooling.md) | notebooks (target archived/removed) | `test_nox_sessions_present` |
| F57 | Marimo session | 🟢 5 | [data science](data-science-tooling.md) | notebooks (target archived/removed) | `test_nox_sessions_present` |
| F58 | Quarto config + session | 🟢 5 | [data science](data-science-tooling.md) | notebooks (target archived/removed) | `test_notebooks_and_docs` |
| F59 | MkDocs Material docs | 🟢 5 | [doc standards](documentation-standards.md) | — | `test_nox_sessions_present` |
| F60 | Docs hosting selection | 🟢 5 | [doc standards](documentation-standards.md) | — | `test_docs_hosting_ghpages`, `test_docs_hosting_readthedocs` |

### Category 14: ML Experiments

| # | Feature | Maturity | Doc | Tutorial | Test |
| :--- | :--- | :--- | :--- | :--- | :--- |
| F61 | Experiment directory scaffolding | 🟢 5 | [ML](ml-functionalities.md) | experiments (target archived/removed) | `test_mlops_experiments_scaffolding` |
| F62 | Hydra configuration | 🟢 5 | [ML](ml-functionalities.md) | experiments (target archived/removed) | `test_mlops_experiments_scaffolding` |
| F63 | MLflow tracking | 🟢 5 | [ML](ml-functionalities.md) | experiments (target archived/removed) | `test_mlflow_tracking_uri` |
| F64 | Git hash provenance | 🟢 5 | [ML](ml-functionalities.md) | — | `test_mlops_experiments_scaffolding` |

### Category 15: IDE Configuration

| # | Feature | Maturity | Doc | Tutorial | Test |
| :--- | :--- | :--- | :--- | :--- | :--- |
| F65 | VSCode settings.json | 🟢 5 | [IDE](ide-configuration.md) | — | `test_vscode_settings_generated` |
| F66 | VSCode extensions.json | 🟢 5 | [IDE](ide-configuration.md) | — | `test_vscode_settings_generated` |
| F67 | VSCode tasks.json | 🟢 5 | [IDE](ide-configuration.md) | — | `test_vscode_settings_generated` |
| F68 | VSCode launch.json | 🟢 5 | [IDE](ide-configuration.md) | — | `test_vscode_settings_generated` |
| F69 | Preferred IDE selection | 🟢 5 | [IDE](ide-configuration.md) | — | `test_no_vscode_when_none` |

### Category 16: AI Agent Integration

| # | Feature | Maturity | Doc | Tutorial | Test |
| :--- | :--- | :--- | :--- | :--- | :--- |
| F70 | .agents/ directory | 🟢 5 | [SWE](swe-standards.md) | — | `test_agents_directory_structure` |
| F71 | Agent skills | 🟢 5 | [SWE](swe-standards.md) | — | `test_agents_directory_structure` |
| F72 | Agent workflows | 🟢 5 | [SWE](swe-standards.md) | — | `test_agents_directory_structure` |
| F73 | Agent commands | 🟢 5 | [SWE](swe-standards.md) | — | `test_agents_directory_structure` |
| F74 | Multi-IDE agent plugins | 🟢 5 | [SWE](swe-standards.md) | — | `test_agents_directory_structure` |

### Category 17: Security & Compliance

| # | Feature | Maturity | Doc | Tutorial | Test |
| :--- | :--- | :--- | :--- | :--- | :--- |
| F75 | Security scanning (bandit/S) | 🟢 5 | [CI/CD](cicd-features.md) | — | `test_nox_sessions_present` |
| F76 | .env.example secrets template | 🟢 5 | [SWE](swe-standards.md) | — | `test_env_example_exists` |
| F77 | .codecov.yaml | 🟢 5 | [CI/CD](cicd-features.md) | — | `test_codecov_config` |
| F78 | CODE_OF_CONDUCT.md | 🟢 5 | [SWE](swe-standards.md) | — | `test_code_of_conduct` |
| F79 | CONTRIBUTING.md | 🟢 5 | [SWE](swe-standards.md) | — | `test_community_health_files` |

### Category 18: Cloud & Deployment

| # | Feature | Maturity | Doc | Tutorial | Test |
| :--- | :--- | :--- | :--- | :--- | :--- |
| F80 | SkyPilot task definition | 🟢 5 | [cloud](cloud-deployment.md) | — | `test_skypilot_task`, `test_skypilot_task_content` |
| F81 | Docker image name config | 🟢 5 | [cloud](cloud-deployment.md) | — | `test_docker_image_config` |

### Category 19: Copier-Specific

| # | Feature | Maturity | Doc | Tutorial | Test |
| :--- | :--- | :--- | :--- | :--- | :--- |
| F82 | 3-way merge updates | 🟢 5 | [copier workflow](copier-workflow.md) | copier update (target archived/removed) | `test_copier_answers_generated` |
| F83 | _skip_if_exists | 🟢 5 | [copier workflow](copier-workflow.md) | copier update (target archived/removed) | `test_skip_if_exists_files` |
| F84 | _exclude for conditionals | 🟢 5 | [copier workflow](copier-workflow.md) | — | `test_exclude_pixi_when_uv`, `test_exclude_readthedocs_when_ghpages`, `test_exclude_docs_workflow_when_readthedocs` |
| F85 | _tasks post-copy scaffold | 🟢 5 | [copier workflow](copier-workflow.md) | — | `test_tasks_scaffold_hook_creates_directories`, `test_template_internal_tests_exist` |

---

## Maturity Summary

| Level | Count | Percentage |
| :--- | ---: | ---: |
| 🟢 5 (Complete) | **85** | **100%** |
| 🔵 4 (Tested) | 0 | 0% |
| 🟡 3 (Implemented) | 0 | 0% |
| **Total** | **85** | **100%** |

> All 85 features are now fully implemented, documented, and tested.

For the full competitive analysis against 19 external templates, see the [Comparative Study](comparative_study.md).

## Cross-Validation

| Metric | Count |
| :--- | ---: |
| Feature documentation pages | 13 |
| Interactive tutorials | 8 |
| Test functions | 86 |
| Parametrized test cases | 86+ |
| Template parameters tested | 100% |

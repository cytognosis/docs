# Data Science Tooling & Notebooks

Cytocast provides a unified approach to interactive computing, supporting three notebook ecosystems (Jupyter, Marimo, Quarto) through dedicated Nox sessions. Each session automatically loads the project's optimized environment so developers can start working immediately.

## Supported Notebook Environments

| Environment | Session | Profile | Format |
|:---|:---|:---|:---|
| **JupyterLab** | `nox -s jupyter_lab` | General-purpose interactive computing | `.ipynb` |
| **Marimo** | `nox -s marimo_edit` | Reactive, reproducible notebooks | `.py` (marimo) |
| **Quarto** | `nox -s quarto_preview` | Publication-quality documents | `.qmd` |

## Launching Notebook Environments

### JupyterLab

```bash
# Launch JupyterLab with the project's virtual environment
nox -s jupyter_lab

# Pass additional arguments (e.g., custom port)
nox -s jupyter_lab -- --port=8889 --no-browser
```

JupyterLab is installed on-demand via `uv run --with jupyterlab`, so it does not pollute the project's core dependency tree.

### Marimo

```bash
# Launch Marimo editor for reactive notebooks
nox -s marimo_edit

# Edit a specific notebook
nox -s marimo_edit -- notebooks/analysis.py
```

Marimo notebooks are pure Python files, making them naturally version-controllable with Git. Unlike `.ipynb` files, they produce clean diffs and support standard code review workflows.

### Quarto

```bash
# Preview Quarto documentation with live reload
nox -s quarto_preview

# Build Quarto to static HTML
nox -s quarto_build
```

Quarto supports `.qmd` files that combine Markdown with executable code blocks (Python, R, Julia). Generated projects include a `_quarto.yml` configuration file for consistent rendering.

## Resource Management

All notebook sessions use the `resource_allocated_run()` wrapper, respecting resource limits:

```bash
# Launch JupyterLab with GPU isolation
CYTO_LIMIT_GPUS=1 nox -s jupyter_lab

# Limit CPU cores for heavy computations
CYTO_LIMIT_CPUS=4 nox -s marimo_edit
```

## DevContainer Integration

When Docker is enabled, the DevContainer configuration includes:
- **Quarto CLI** installed via DevContainer features
- **quarto.quarto** VS Code extension for inline rendering
- All notebook extensions pre-configured

```json
{
  "features": {
    "ghcr.io/rocker-org/devcontainer-features/quarto-cli:1": {}
  },
  "customizations": {
    "vscode": {
      "extensions": ["quarto.quarto"]
    }
  }
}
```

## CI/CD Integration

The `quarto.yaml` GitHub Actions workflow automatically renders Quarto notebooks on pull requests:

```yaml
# Triggered on PRs that modify .qmd files
on:
  pull_request:
    paths: ['**/*.qmd', '_quarto.yml']

steps:
  - name: Render Quarto notebooks
    run: quarto render docs/
```

## Notebook Directory Structure

Generated projects include a `docs/notebooks/` directory with example files:

```
docs/
├── notebooks/
│   ├── example.ipynb      # Jupyter notebook example
│   ├── tutorial.py        # Marimo notebook example
│   └── tutorial.qmd       # Quarto notebook example
```

## Why Three Notebook Systems?

| Feature | Jupyter | Marimo | Quarto |
|:---|:---|:---|:---|
| **Git-friendliness** | Poor (JSON) | Excellent (Python) | Good (Markdown) |
| **Reactivity** | Manual re-run | Automatic | Manual |
| **Publication quality** | Low | Medium | High |
| **Ecosystem** | Largest | Growing | Strong |
| **Best for** | Exploration | Reproducible analysis | Reports & papers |

[← Back to the Comparative Study](comparative_study.md)

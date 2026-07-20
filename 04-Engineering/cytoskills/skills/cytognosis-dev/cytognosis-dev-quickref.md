> **Status**: Active
> **Date**: 2026-06-14
> **Author**: Cytognosis Foundation
> **Audience**: engineers
> **Tags**: `quick-reference`, `cytognosis-dev`

# cytognosis-dev — Quick Reference

> **One line**: Load this skill for all Cytognosis software development: project scaffolding (Cytocast), environment management (Cytoskeleton), coding standards, steering docs, and spec-driven development.
> **Full doc**: [cytognosis-dev.md](cytognosis-dev.md)

---

## Key Concepts

| Term | Definition |
|------|-----------|
| **Cytocast** | Copier-based template engine that scaffolds Cytognosis projects. `copier copy` creates; `copier update` applies template upgrades. |
| **Cytoskeleton** | Component-based environment manager. Resolves dependencies, generates lockfiles, builds `.venv`. |
| **cyto-skills** | JavaScript/Node.js skill runtime (renamed from cytoagent). Repo: `https://github.com/cytognosis/cytoskills`. |
| **Steering docs** | AI-agent context files in `.agents/steering/` (product.md, tech.md, structure.md, etc.). |
| **Spec-driven dev** | Three-file workflow: `requirements.md` → `design.md` → `tasks.md` in `.agents/specs/{feature}/`. |
| **EARS notation** | Formal requirements syntax: WHEN/WHILE/IF/THE SYSTEM SHALL patterns. |
| **cytoagent profile** | Deprecated; use `cytos` profile instead. |

---

## Commands

| Command | What It Does |
|---------|-------------|
| `uvx copier copy <template> <dest> --vcs-ref <tag> --data profile=<p>` | Scaffold a new project |
| `uvx copier update --vcs-ref <tag>` | Update project to latest template version |
| `nox -s init_project` | Initialize scaffolded project |
| `cytocast apply-branch-config` | Apply per-branch configuration after checkout |
| `cytoskeleton env build --env-config <yaml> --backend uv` | Resolve and install environment |
| `cytoskeleton deps doctor --env <name> --fix-suggestions` | Diagnose dependency conflicts |
| `cytoskeleton lock generate` | Regenerate all lockfiles |
| `nox -s sync_profile_contracts` | Refresh vendored contracts after upstream changes |
| `mise install && uv sync --workspace && pnpm install -r` | Bootstrap multi-app monorepo (Yar-style) |

---

## Cytocast Profiles

| Profile | Use for |
|---------|---------|
| `library` | Generic Python library |
| `tool` | Nox-driven tooling repo |
| `ml` | Machine learning research |
| `data-science` | Data analysis |
| `full-stack` | Python backend + frontend |
| `bio-modeling` | Foundation-model bio work |
| `ai-llm` | LLM-centric project |
| `r-analysis` | R-only analysis |
| `cytos` | Cytognosis foundation kernel |
| `interface-template` | Downstream product app (pair with `--data template=app-<name>`) |
| `yar-backend` / `yar-mobile` / `yar-desktop` / `yar-extension` | Yar sub-apps |

---

## Standards Toolchain

| Tool | Purpose | Replaces |
|------|---------|---------|
| `uv` | Python package + env management | pip, conda, poetry |
| `pnpm` | Node.js package management | npm, yarn |
| `Ruff` | Python linting + formatting | black, isort, flake8 |
| `ty` (Astral) | Python type checking | mypy, Pyright |
| `Biome` | TypeScript linting + formatting | ESLint + Prettier |
| `pytest` | Python testing | unittest |
| `nox` | Task runner / session manager | Makefile, tox |

---

## Common Patterns

```bash
# Scaffold a new library project
uvx copier copy https://github.com/cytognosis/cytocast ~/repos/cytognosis/my-lib \
    --vcs-ref v2.0.0 --data profile=library
cd ~/repos/cytognosis/my-lib && nox -s init_project

# Scaffold a new phone app
uvx copier copy https://github.com/cytognosis/cytocast ~/repos/cytognosis/my-app \
    --vcs-ref v2.0.0 --data profile=interface-template --data template=app-phone

# Resolve environment after scaffold
cytoskeleton env build --env-config envs/cytognosis.yaml --backend uv

# Initialize steering docs for a new product
mkdir -p .agents/steering
# Copy product.md, tech.md, structure.md from references/steering-templates.md

# Start spec-driven development for a feature
mkdir -p .agents/specs/my-feature
# Create requirements.md → design.md → tasks.md
```

---

## Options / Parameters

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `--vcs-ref` | `str` | — | Cytocast template release tag to use (required; never use HEAD) |
| `--data profile=<name>` | `str` | — | Cytocast profile (library, ml, interface-template, etc.) |
| `--data template=<name>` | `str` | — | Template variant for `interface-template` profile |
| `--backend uv` | `str` | `uv` | Cytoskeleton environment backend |
| `--fix-suggestions` | `bool` | `false` | Ask cytoskeleton deps doctor for suggested fixes |

---

## Error Quick-Fix

| Error / Symptom | Fix |
|-----------------|-----|
| `uv sync` fails after scaffold | Check `cytoskeleton.ref` — it must pin to a release tag, not HEAD |
| Copier update breaks vendored contracts | Run `nox -s sync_profile_contracts` to refresh |
| Steering doc not picked up by agent | Confirm docs are in `.agents/steering/`, not `.cytognosis/steering/` (does not exist) |
| `cytoagent` profile not found | Profile is deprecated; use `cytos` |
| Import errors in src layout | Package must be under `src/<package>/`; never flat layout |

---

## See Also

- [Full documentation](cytognosis-dev.md) — comprehensive reference + explanation
- [cytognosis-doc](../cytognosis-doc/cytognosis-doc.md) — documentation standards (ADRs, specs, RFCs)
- [cytognosis-template-master](../cytognosis-template-master/cytognosis-template-master.md) — interface app templates
- [cytognosis-orchestrator](../cytognosis-orchestrator/cytognosis-orchestrator.md) — routing between skills

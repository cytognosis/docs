> **Status**: Active
> **Date**: 2026-06-14
> **Author**: Cytognosis Foundation
> **Audience**: engineers
> **Tags**: `development`, `cytognosis-dev`, `cytocast`, `cytoskeleton`

# cytognosis-dev — Development Lifecycle Skill

> **Reading time**: ~8 minutes
> **If you only read one thing**: Use Cytocast (`copier copy`) to scaffold every project. Never build a directory tree manually. Never use pip, conda, mypy, or ESLint.

---

## What It Is and Why

`cytognosis-dev` covers the entire Cytognosis software development lifecycle: project scaffolding with Cytocast, environment management with Cytoskeleton, coding standards, steering documents, spec-driven development, and daily workflow.

**When to load this skill**:

- Creating or updating a Cytognosis project
- Setting up or managing environments (Python, Node.js, Dart, Rust)
- Working inside an existing generated project (nox sessions, CI/CD)
- Authoring a skill in cyto-skills (TS/Node.js)
- Setting up or updating steering documents
- Using spec-driven development (requirements.md, design.md, tasks.md)
- Configuring coding standards (Ruff, ty, pytest, nox)

**When NOT to use this skill**:

- Interface app templates (phone, web, desktop, extension): use `cytognosis-template-master`
- Brand application: use `cytognosis-design-system-master`
- Technical documentation: use `cytognosis-doc`
- Cytoplex or the Cytognosis Authority Protocol: use the `docs` repo

> Key naming facts (as of 2026-05-29):
> - **cyto-skills** = rename of **cytoagent** (Python to JavaScript/Node.js). Repo: `~/repos/cytognosis/cytoskills`.
> - **Cytoplex** (formerly CAP) = component of Cytonome, NOT part of cyto-skills.
> - Spec/design docs live in the central `docs` repo; user-facing docs stay in source repos.

---

## System Architecture

```
Developer
  → copier copy (Cytocast: template engine + dev skills + _shared/ CI)
      → Generated Project
          → .cytognosis-config.yaml + cytoskeleton.ref
              → Cytoskeleton (envs + schemas + templates + skills)
                  → lockfile + .venv
          → external/cyto-skills (peer submodule)
          → external/cytoplex (peer submodule, independent)
```

| Repo | Purpose | Local Path |
|------|---------|------------|
| `cytocast` | Copier template engine + dev skills + shared CI | `~/repos/cytognosis/cytocast` |
| `cytoskeleton` | Component-based env manager + interface templates + schemas | `~/repos/cytognosis/cytoskeleton` |
| `branding` | Design system + brand-phase skills | `~/repos/cytognosis/org/branding` |
| `cyto-skills` (was `cytoagent`) | JS/Node.js skill runtime | `~/repos/cytognosis/cytoskills` |
| `cytos` | Foundation kernel | `~/repos/cytognosis/cytos` |
| `Yar` | Personal KG system; multi-app monorepo | `~/repos/cytognosis/Yar` |
| `Cytoplex` (was `CAP`) | Cytognosis Authority Protocol; component of Cytonome | `~/repos/cytognosis/CAP` |
| `docs` | Central spec/design documentation | `~/repos/cytognosis/docs` |

---

## Decision Tree

```
Create a new Cytognosis project?
├─ Interface app (phone/web/desktop/extension)?
│  └─ Use cytocast workflow + LOAD cytognosis-template-master in a SEPARATE response
├─ Yar-style multi-app monorepo?
│  └─ READ references/multi-app-monorepo.md
├─ Library, tool, scientific package?
│  └─ READ references/cytocast-workflow.md
└─ Agent skill in cyto-skills?
   └─ READ references/cyto-skills-authoring.md

Resolve, lock, or debug an environment?
└─ READ references/cytoskeleton-reference.md

Work inside an existing generated project?
└─ READ references/project-dev-guide.md

Update a project to the latest template?
└─ READ references/cytocast-workflow.md (§ Updating Projects)

Need coding standards (Ruff, ty, pytest, nox)?
└─ READ references/standards/code-standards.md

Need environment or dependency management standards?
└─ READ references/standards/environment-standards.md

Need git workflow, branch strategy, naming conventions?
└─ READ references/standards/version-control-standards.md

Need agentic/skill authoring or steering doc norms?
└─ READ references/standards/agentic-standards.md

Set up or manage steering docs?
└─ READ references/steering-management.md
```

---

## Quick Commands

```bash
# Generate a new project
uvx copier copy https://github.com/cytognosis/cytocast my-project \
                --vcs-ref v2.0.0 --data profile=library

# Generate an interface app
uvx copier copy https://github.com/cytognosis/cytocast my-app \
                --vcs-ref v2.0.0 --data profile=interface-template \
                --data template=app-phone

# Update to latest template
cd my-project && uvx copier update --vcs-ref v2.1.0

# Initialize generated project
nox -s init_project

# Apply per-branch config (post-checkout)
cytocast apply-branch-config

# Resolve + install environment
cytoskeleton env build --env-config envs/cytognosis.yaml --backend uv

# Diagnose dependency conflict
cytoskeleton deps doctor --env cytognosis --fix-suggestions

# Regenerate all lockfiles
cytoskeleton lock generate

# Multi-app monorepo (Yar-style)
mise install && uv sync --workspace && pnpm install -r
cd apps/mobile && melos bootstrap && prek install
```

---

## Cytocast Profiles

| Profile | Use for | Cytoskeleton env |
|---------|---------|-----------------|
| `library` | Generic Python library | base |
| `tool` | Nox-driven tooling repo | base |
| `ml` | Machine learning research | ml |
| `data-science` | Data analysis | datascience |
| `full-stack` | Python backend + frontend | full-stack |
| `bio-modeling` | Foundation-model bio work | bio-ml |
| `ai-llm` | LLM-centric project | llm |
| `r-analysis` | R-only analysis | r-base |
| `cytos` | Cytognosis foundation kernel | cytognosis |
| `neuros` / `neuro-scale` | Neuro-scale work | bio-ml |
| `interface-template` | Downstream product app | app-{phone,web,desktop,extension} |
| `yar-backend` | Yar FastAPI backend | agentic |
| `yar-mobile` | Yar mobile (Flutter) | app-phone |
| `yar-desktop` | Yar desktop (Tauri) | app-desktop |
| `yar-extension` | Yar extension (MV3) | app-extension |

Note: `cytoagent` profile is deprecated; use `cytos`.

---

## Steering Documents

Every Cytognosis product has a `.agents/steering/` directory with AI-agent context files.

Steering document types:

| File | Purpose |
|------|---------|
| `product.md` | Product vision, goals, audience, success criteria |
| `tech.md` | Technology choices, architecture decisions |
| `structure.md` | Repo layout, module boundaries |
| `requirements.md` | Formal EARS-notation requirements |
| `design.md` | Feature-level design decisions |
| `tasks.md` | Current sprint tasks |

Key rules:

- Steering docs live in `.agents/steering/`, not `.cytognosis/`.
- `.agents/` is the single home for all agent context.
- Simple projects (libraries, tools): `.agents/config.yaml` alone is sufficient.
- Products (Yar, cytos, Cytoplex): add steering docs.

References: `references/steering-management.md`, `references/steering-init-guide.md`, `references/steering-templates.md`

---

## Spec-Driven Development

For non-trivial features, use the three-file spec workflow:

```
User Story → requirements.md → design.md → tasks.md
```

Files live in `.agents/specs/{feature}/`.

### EARS Notation Patterns

| Pattern | Syntax |
|---------|--------|
| Event-Driven | `WHEN [trigger], THE SYSTEM SHALL [response]` |
| State-Driven | `WHILE [state], THE SYSTEM SHALL [behavior]` |
| Unwanted Behavior | `IF [error], THEN THE SYSTEM SHALL [recovery]` |
| Ubiquitous | `THE SYSTEM SHALL [behavior]` |
| Optional | `WHERE [feature enabled], THE SYSTEM SHALL [behavior]` |

Example spec directory layout:

```
.agents/specs/
├── voice-capture/
│   ├── requirements.md
│   ├── design.md
│   └── tasks.md
└── bugfixes/neo4j-timeout/
    ├── bugfix.md
    ├── design.md
    └── tasks.md
```

---

## Contract Boundaries

| Boundary | Rule |
|----------|------|
| Cytocast → Cytoskeleton | `cytoskeleton.ref` pins to a release tag, NOT HEAD. Wrong ref causes `uv sync` to fail. |
| Cytocast → Branding | Brand tokens via `cytognosis-branding` PyPI or submodule fallback. |
| Cyto-skills ↔ Cytoplex | Peer dependencies; never merge them. |
| Vendored contracts | Refresh via `nox -s sync_profile_contracts` after upstream changes. |

---

## Hard Rules (NEVER)

- NEVER manually build a project directory tree. Use Cytocast (`copier copy`).
- NEVER use `pip`, `conda`, or `poetry`. Use `uv`.
- NEVER use `npm` or `yarn` for TS work. Use `pnpm`.
- NEVER use `mypy` or `Pyright`. Use Astral `ty`.
- NEVER use `black`, `isort`, or `flake8`. Ruff absorbs all.
- NEVER use `ESLint + Prettier` for new TS work. Use Biome.
- NEVER use flat layout. Always `src/<package>/` (Python).
- NEVER use `setup.py` / `setup.cfg`. Use `pyproject.toml`.
- NEVER use `cookiecutter` / `cruft` (legacy). Cytocast is the engine.
- NEVER add deps directly to `pyproject.toml`. Use cytoskeleton env build.
- NEVER hardcode wheel URLs. Use `[[tool.uv.index]]` with `explicit = true`.
- NEVER edit vendored contracts by hand. Use `nox -s sync_profile_contracts`.
- NEVER put Cytoplex code inside cyto-skills. They are independent peer submodules.
- NEVER add cyto-skills as a build-time dep to cytocast (removed in v2).
- NEVER reference `.cytognosis/steering/` — it does not exist. Steering lives in `.agents/steering/`.

---

## Examples

### Example 1: Scaffold a new ML research project

```bash
uvx copier copy https://github.com/cytognosis/cytocast ~/repos/cytognosis/my-ml-project \
    --vcs-ref v2.0.0 --data profile=ml

cd ~/repos/cytognosis/my-ml-project
nox -s init_project
cytoskeleton env build --env-config envs/cytognosis.yaml --backend uv
```

Result: fully scaffolded project with `src/` layout, Ruff config, ty, pytest, nox sessions, lockfile, and `.agents/config.yaml`.

### Example 2: Set up steering docs for an existing product

1. Create `.agents/steering/` directory.
2. Copy templates from `references/steering-templates.md`: `product.md`, `tech.md`, `structure.md`.
3. Populate each with the current project state.
4. Commit alongside a new ADR documenting the steering setup decision.

---

## Reference Index

| Reference | When to Read |
|-----------|-------------|
| `references/standards/code-standards.md` | Ruff config, ty, pytest, nox sessions, code conventions |
| `references/standards/environment-standards.md` | uv, cytoskeleton, env strategies, lockfiles, compute backends |
| `references/standards/version-control-standards.md` | Git workflow, branch strategy, commit style, tag format |
| `references/standards/agentic-standards.md` | Skills authoring norms, .agents/ config, steering docs, spec-driven dev |
| `references/cytocast-workflow.md` | Creating/updating projects, profiles, copier workflow, hooks, CI/CD |
| `references/cytoskeleton-reference.md` | Environment resolution, CLI, components, ROCm, diagnostics |
| `references/project-dev-guide.md` | Nox sessions, code quality tiers, CI/CD, testing |
| `references/multi-app-monorepo.md` | UV workspaces + Melos + pnpm + cargo + mise + prek (Yar-style) |
| `references/cyto-skills-authoring.md` | Authoring a skill in cyto-skills (TS/Node.js) |
| `references/steering-management.md` | Steering doc decision tree, hooks, conflict resolution, YAML spec |
| `references/steering-init-guide.md` | Step-by-step steering initialization |
| `references/steering-templates.md` | Ready-to-copy templates for all 9 steering doc types |

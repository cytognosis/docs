# Toolchain engineering layer

> **Status:** Active · **Date:** 2026-07-01 · **Owner:** Toolchain pillar · **Canonical for:** cross-cutting toolchain engineering docs

**If you only read one thing:** This layer is the canonical home for cross-cutting documentation of the four Toolchain repos (cytoskeleton, cytocast, cytoskills, cytomem). Repo-internal user guides stay in each repo's own `docs/` (they power that repo's MkDocs site); the authoritative, cross-cutting, and decision-level docs live here.

## Contents

| Path | What |
|---|---|
| `toolchain-overview.{technical,readable,agent}.md` | The pillar overview, three variants (blueprint Section 4) |
| `cytoskeleton/` | Architecture, platform design, dependency and asset-registry strategy |
| `cytocast/` | Scaffolder feature reference (85 features), comparative study |
| `cytoskills/` | Skill-platform architecture, CLI, module specs, branding-skill spec |
| `../standards/` | `coding-standards.md`, `documentation-standards.md` |
| `../decisions/` | ADRs (e.g. `ADR-002-container-runtime-standard.md`) |

## Canonical vs repo-local (avoid re-duplication)
Each repo documents itself in its own `docs/` for its MkDocs site. That is expected and is not a duplicate to remove. This layer holds the versions that are authoritative across the pillar. When they overlap, this layer wins for cross-cutting content; the repo copy wins for repo-internal implementation detail. See `00-CONSOLIDATION/CLASSIFICATION.tsv` in the Toolchain project for the per-file disposition.

## Related, owned elsewhere
- **Skill-tagging ontology and CI gate:** `cytoskeleton/ontologies/` (`cyto-se-usecase.ttl`, `cyto-org-function.ttl`, `validate_skill_tags.py`) and `cytoskeleton/.github/workflows/skill-tags.yml`. Operationalizes SHARED-BLUEPRINT Section 10.
- **Brand book:** `cytocast/design/branding.md` here is misfiled (belongs in `07-Design`, owned by the Branding agent). Tracked as a handoff in the Toolchain `CONFLICTS.md`; not moved unilaterally.

## Open conflicts (see Toolchain `CONFLICTS.md`)
- **mypy vs ty:** `../standards/coding-standards.md` specifies mypy; `cytocast/features/cicd-features.md` says ty replaced it. Verify the current tool, then make standards canonical.

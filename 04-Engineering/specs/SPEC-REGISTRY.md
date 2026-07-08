# Spec Registry (Central Index of All Specs)

> **Status**: Active
> **Date**: 2026-07-08
> **Author**: Claude (Cowork) for @shahin
> **Audience**: engineers, agents
> **Tags**: `specs`, `registry`, `spec-driven`, `central-index`

**Reading time**: 3 minutes. This is the single central place to find every spec across every Cytognosis repo. Feature specs physically live with their code (docs-as-code, required by Spec Kit and the repo constitutions); this registry links to all of them and hosts the location policy so nothing is lost.

## Location policy (where each spec type lives)

| Spec type | Physical location | Why |
|-----------|-------------------|-----|
| **Feature spec** | Owning repo: `specs/NNN-slug/` (Spec Kit layout) | Travels with the code it governs; reviewed in the same PR; append-only after shipping (constitution Article X) |
| **Cross-repo / platform / architecture spec** | Central: `docs/04-Engineering/architecture/` | Spans repos, so it has no single code home |
| **Decision record (ADR)** | Central: `docs/04-Engineering/decisions/` | Org memory, superseded not edited |
| **This registry (index of all specs)** | Central: `docs/04-Engineering/specs/SPEC-REGISTRY.md` | One place to discover everything |

The weekly Cowork drift audit refreshes the table below and flags specs stale versus their code.

## Standard format (every spec, everywhere)

Enforced by each repo's constitution and the Cytognosis preset:

1. **Metadata header**: Status, Date, Author, Audience, Tags.
2. **Requirements in EARS** with stable `REQ-NNN` identifiers.
3. **Checks section**: executable acceptance criteria, each traceable to a `REQ-NNN`, run by an independent verifier.
4. **Lifecycle status**: Draft → Approved → Implementing → Live → Superseded.
5. **Changes as deltas** (ADDED / MODIFIED / REMOVED / RENAMED), merged after shipping, never silent edits.

## Registry (all specs, all repos)

| Repo | Spec | Status | Link |
|------|------|--------|------|
| cytomem | 001 Per-repo scoped task boards | Draft (pilot) | `cytomem/specs/001-per-repo-scoped/spec.md` |

*(New specs append here automatically via the drift audit; cross-repo specs also list their `docs/04-Engineering/architecture/` path.)*

## How agents and Cowork use this

- **Cowork** writes new feature specs into the owning repo, then adds a registry row here.
- **Claude Code** reads the owning repo's spec plus its constitution before implementing.
- **Anyone** browses this one file to find any spec across the org.

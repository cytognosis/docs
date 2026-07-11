# Spec Registry (cross-repo index)

> **Status**: Active
> **Date**: 2026-07-11
> **Author**: @shahin
> **Audience**: engineers, agents
> **Tags**: `engineering`, `specs`, `registry`
> **Variants**: Technical (this doc) - Readable (`simple/SPEC-REGISTRY.md`)

> [!NOTE]
> **TL;DR**: One row per spec across all repos. Specs live in-repo at `specs/NNN-slug/spec.md`; changes ride `changes/` deltas; statuses: Draft -> Approved -> Implementing -> Live -> Superseded. The mission hub board mirrors this table; cytomem ingests it (cytomem spec 004).

| Repo | Spec | Title | Status | Board issue | Depends on |
|---|---|---|---|---|---|
| cytomem | 001-per-repo-scoped | Per-repo scoped memory | Live | - | - |
| website | 001-gen1-reconciliation | Gen-1 feature reconciliation onto Payload | Approved | pending sign-in | branding 003 (partial) |
| website | 002-template-adoption | Website Template adoption + token enforcement | Approved | pending sign-in | branding 003 |
| branding | 001-recover-brand-assets | Recover pre-CytoStyle assets into CytoStyle | Approved | pending sign-in | - |
| branding | 002-claude-design-sync-ci | Restore Claude Design sync + drift CI | Approved | pending sign-in | 001 |
| branding | 003-website-template-package | Website Template package build + publish | Approved | pending sign-in | 001, 002 |
| cytomem | 002-mission-hub-bridge | cytomem <-> mission hub task sync | Draft | pending sign-in | hub MCP (live) |
| cytomem | 003-cca-memory-upgrade | Notes, hindsight, compaction (CCA fold-in) | Draft | pending sign-in | - |
| cytomem | 004-spec-ingestion | Specs as first-class memory | Draft | pending sign-in | 002, 003 |

## Conventions

- **Location**: feature specs in-repo `specs/NNN-slug/`; cross-repo or architecture specs in `04-Engineering/architecture/`.
- **Requirements**: EARS syntax; every spec ends with executable **Checks**; a verifier session (never the implementer) runs Checks and writes `verification.md` before Live.
- **Evolution**: never silently edit a Live spec; add `changes/NNN-date-slug.md` deltas (ADDED/MODIFIED/REMOVED/RENAMED), archive on supersession.
- **Board mirror**: each spec gets one hub issue carrying only pointers (spec ID, repo, path, status); content stays in git (pointer discipline, ADR D-2/REQ-002-03).
- **Enforcement**: spec-guard (pre-commit + CI + PreToolUse hook) blocks `src/` changes without a governing spec; escape hatches `SPEC_GUARD_SKIP=1`, `[trivial]` tag.

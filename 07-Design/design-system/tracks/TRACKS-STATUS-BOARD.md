# Tracks Status Board

> **Status**: Active
> **Date**: 2026-07-11
> **Author**: @shahin
> **Audience**: designers, engineers
> **Tags**: `design`, `design-system`, `tracks`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)

**Purpose:** the single shared file both track sessions read at start and update at end. Keeps Branding (Track A) and Website (Track B) consistent without sharing context. Update the date and the three live fields whenever you touch either track.

**Last updated:** 2026-07-10 (setup).

## Live sync fields

| Field | Value |
|---|---|
| Design System (upstream) | v11.2.1, PUBLISHED + team Default, `https://claude.ai/design/p/11d44c2c-5d95-416f-9395-f12091cba8ee` |
| Current Website Template version | none yet (Track A Phase 3 produces `website-template@0.1.0`) |
| Website pinned Template version | none yet |
| Open cross-track blockers | none |
| Ali gate (branding-repo recovery) | OPEN, blocks Track A Phase 0 and the `branding/design-system/` write only |

## Track A (Branding) status

- Plan: `TRACK-A_BRANDING-REPO_PLAN.md`. Home after relocation: Branding project.
- Done: Design System published v11.2.1; logo + icon family generated (light/dark pairs, product glyphs, `logos.card.html`, 64 icons / 10 families, verified clean).
- Next: run the artifact pack (`prompt_google_and_artifact_templates.md`, still queued: Google Docs/letterhead/Slides templates, meeting + social backgrounds, VS Code theme family); then Phase 1 graft into the recovered repo, wire sync, publish the Website Template.
- Flags from the logo run: `references/06_iconography.md` was reconciled from an aspirational set to the real 64-icon set; the horizontal wordmark keeps a tight right margin (say if you want more breathing room, it is a deliberate geometry change).

## Track B (Website) status

- Plan: `TRACK-B_WEBSITE_PLAN.md` (+ `simple/`). Home after relocation: Website project.
- Known now: stack is Vite 6 + React 19 + Node 22 + Payload CMS 3 + Postgres (the FastAPI backend in-repo is dead code); CI/CD is currently BROKEN (workflows build Docker `--target site`/`cms` stages the Dockerfile does not define; neither uses cytohost); a July 6 patch swapped Space Grotesk for Inter and must be reverted.
- Next: pin the Website Template when Track A publishes it; feature-gap reconstruction; DB/resource pressure-test; CI/CD repair on cytohost; Yar-section revision; IA revision. Animations deferred to their own sessions.

## Protocol

1. Read this board at session start.
2. Template releases are the only hard handoff: Track A announces `website-template@x.y.z` + changelog here; Track B pins it and reports integration status here.
3. Cross-track needs get a one-line request under "Open cross-track blockers".
4. Both sessions read the published Design System via the Chrome bridge (`CLAUDE_DESIGN_BRIDGE.md`); neither invents token values.

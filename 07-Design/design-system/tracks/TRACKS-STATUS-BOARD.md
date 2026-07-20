# Tracks Status Board

> **Status**: Active
> **Date**: 2026-07-11
> **Author**: @shahin
> **Audience**: designers, engineers
> **Tags**: `design`, `design-system`, `tracks`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)

**Purpose:** the single shared file both track sessions read at start and update at end. Keeps Branding (Track A) and Website (Track B) consistent without sharing context. Update the date and the three live fields whenever you touch either track.

**Last updated:** 2026-07-11 (Track B Phase 0 executed).

## Live sync fields

| Field | Value |
|---|---|
| Design System (upstream) | v11.2.1, PUBLISHED + team Default, `https://claude.ai/design/p/11d44c2c-5d95-416f-9395-f12091cba8ee` |
| Current Website Template version | none yet (Track A Phase 3 produces `website-template@0.1.0`) |
| Website pinned Template version | none yet — **fetch/pin mechanism now BUILT and waiting** in the website repo (`TEMPLATE_VERSION.lock` status=pending, `scripts/fetch-template.mjs` verified no-op, wired as a `pnpm build` prestep). Track B flips the lock to status=published the instant Track A ships a release. |
| Open cross-track blockers | **Track A -> Track B:** publish `website-template@x.y.z` (checksummed tokens.css + fonts + component classes) so Track B can pin it. Only Track B Phase 1 (Template adoption) is blocked on this; everything else in Phase 0 is done. |
| Ali gate (branding-repo recovery) | OPEN, blocks Track A Phase 0 and the `branding/design-system/` write only |

## Track A (Branding) status

- Plan: `TRACK-A_BRANDING-REPO_PLAN.md`. Home after relocation: Branding project.
- Done: Design System published v11.2.1; logo + icon family generated (light/dark pairs, product glyphs, `logos.card.html`, 64 icons / 10 families, verified clean).
- Next: run the artifact pack (`prompt_google_and_artifact_templates.md`, still queued: Google Docs/letterhead/Slides templates, meeting + social backgrounds, VS Code theme family); then Phase 1 graft into the recovered repo, wire sync, publish the Website Template.
- Flags from the logo run: `references/06_iconography.md` was reconciled from an aspirational set to the real 64-icon set; the horizontal wordmark keeps a tight right margin (say if you want more breathing room, it is a deliberate geometry change).

## Track B (Website) status

- Plan: `TRACK-B_WEBSITE_PLAN.md` (+ `simple/`). Home after relocation: Website project.
- **Phase 0 DONE (2026-07-11)**, on branch `claude/busy-mirzakhani-88b0e9` in `https://github.com/cytognosis/website` (pre-change tag `pre-track-b-consolidation-2026-07-11`):
  - **CI/CD repaired + verified.** Restored the Node multi-stage Dockerfile (`deps`/`site-build`/`cms-build`/`cms`/`site`) from last-good `d91dc90`; `docker build --target site` and `--target cms` both build locally (exit 0). Both workflows moved to the self-hosted **cytohost** runner (`[self-hosted, Linux, X64, cytohost]`); added the missing `cytognosis-cms` deploy job. Site healthcheck now hits `/api/health`.
  - **Dead FastAPI backend removed** (`main.py`, `backend/auth.py`, stale `DEPLOY.md`); permanently closes the `/auth/dev_login` gate. Node + Payload is the one backend.
  - **Space Grotesk heading regression reverted** (`--f-display` back to Space Grotesk 500); adopted live-site deltas (96/48px section rhythm; `#23232B` ink and uppercase-mono eyebrows were already correct).
  - **Repo hygiene:** untracked `dist/` (82) + `cms/.next/` (632) build artifacts and gitignored them; deleted stray root `package-lock.json`.
  - **Template pin mechanism built** (`TEMPLATE_VERSION.lock` + `scripts/fetch-template.mjs`), a verified no-op until Track A publishes.
  - **Feature recovery:** git archaeology report at `docs/FEATURE-RECOVERY-REPORT.md`; dropped Generation-1 features staged for reconciliation on branch `feat/website-feature-recovery` (see `RECOVERY-STAGING.md`). Restore ref is `c5a9a17^` (`2ad85a6`). Corrections: Contact FAQ was NOT lost; CSV export half-survives. Open conflict for adjudication: `team` collection vs static team pages.
- Next: **Phase 1 = pin the Website Template once Track A publishes it** (mechanism ready). Then DB/resource pressure-test; Yar-section revision; IA revision; feature reimplementation from the recovery branch (RSS/CSV/delete first, then CV pipeline as Node). Animations deferred to their own sessions.

## Protocol

1. Read this board at session start.
2. Template releases are the only hard handoff: Track A announces `website-template@x.y.z` + changelog here; Track B pins it and reports integration status here.
3. Cross-track needs get a one-line request under "Open cross-track blockers".
4. Both sessions read the published Design System via the Chrome bridge (`CLAUDE_DESIGN_BRIDGE.md`); neither invents token values.

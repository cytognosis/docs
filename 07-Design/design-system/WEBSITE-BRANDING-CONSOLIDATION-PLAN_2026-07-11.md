# Website + Branding Consolidation Plan (autonomous, 2026-07-11)

> **Status**: Active
> **Date**: 2026-07-11
> **Author**: @shahin
> **Audience**: designers, engineers
> **Tags**: `design`, `design-system`, `website`, `branding`, `consolidation`
> **Variants**: Technical (this doc) - Readable (`simple/WEBSITE-BRANDING-CONSOLIDATION-PLAN_2026-07-11.md`) - Agent (n/a)

> [!NOTE]
> **TL;DR**: Ali rebuilt both repos on top of older versions and dropped real features. This plan recovers the old features from git, reconciles them with his modern rebuilds, enforces the v11.2.1 design system, and restores Claude Design integration. Done autonomously from git + prior context; no Ali brief.

## 1. Scope and sources (read all before finalizing execution)
- **Repos:** `https://github.com/cytognosis/website`, `https://github.com/cytognosis/branding`.
- **Old versions (git):** branding pre-CytoStyle = `c4a4f29` and ancestors (Design System v10, logos, Dusk theme, Claude Design sync pipeline `22a42ac`); website pre-rebuild = "Generation-1" (pre `3a2caae`).
- **Ali rewrites:** branding `9bf41cb` "Replace branding repo with CytoStyle package"; website `3a2caae` calm/neurodiverse redesign + `97b8d46` consolidation rebuild.
- **Already executed (website, Track B session, 2026-07-11):** CI restored (`94658ee`), Space Grotesk regression reverted (`5925292`), node_modules untracked (`5682519`), checksum-pinned Template fetch (`15088e6`), `docs/FEATURE-RECOVERY-REPORT.md` (`900fc14`), Gen-1 features staged (`2468532`: FastAPI backend + candidates/events pages).
- **Context to fold in:** design chat outputs (`07-Design/design-system/`), Antigravity update (`04-Engineering/toolchain/antigravity-update-20260622`), prior Claude sessions (Branding-project-consolidation, Spec-driven-development-strategy), the published Claude Design v11.2.1, and the Website Template (Track A).

## 2. Branding: old vs CytoStyle (868 files changed; 55k deletions)
- **CytoStyle added (keep):** Storybook + React/TS component library, Figma-first audits, implementation roadmap, Dockerfile, IranYekan (fa) fonts.
- **CytoStyle dropped (recover + reconcile):**
  - Claude Design **sync/drift CI**: `.github/workflows/claude-design-drift.yml`, `publish-branding.yml`, and the bidirectional Claude Design <-> branding <-> cytoskeleton pipeline (`22a42ac`). **This is the Claude Design integration; restore it.**
  - `.sandbox/brand-variants/*` (14 explorations), Atkinson Hyperlegible **accessibility fonts**, governance docs (ATTRIBUTION/CHANGELOG/CONTRIBUTING/DESIGN/SECURITY/TRADEMARK), Design System v10 + logos + Cytognosis **Dusk** VS Code theme.
- **Target:** keep CytoStyle's component architecture; restore the dropped sync CI, accessibility fonts, brand variants, governance, logos/Dusk; enforce **v11.2.1** tokens; align to the Website Template.

## 3. Website: old vs rebuild
- **Rebuild (keep):** Vite frontend, calm/neurodiverse redesign, Payload CMS, /science, forms, blog, hardening.
- **Dropped Gen-1 (staged for reconciliation):** FastAPI backend (forms, CV parser, blog, email), candidates + events pages.
- **Target:** reconcile the staged Gen-1 features into the current stack (decide FastAPI-vs-Payload for forms/CV/blog; recommend Payload + port Gen-1 logic), keep the neurodiverse redesign, enforce v11.2.1 via the pinned Website Template, and remove the re-committed `.venv` (build junk; gitignore it).

## 4. Design-system enforcement + Claude Design integration
- Single upstream = **published Claude Design v11.2.1**. Branding mirrors it (design-system/), website consumes the checksum-pinned Website Template. Never hand-edit tokens.
- **Restore the Claude Design drift/publish CI** in branding (the sync pipeline CytoStyle removed). The `CLAUDE_DESIGN_BRIDGE.md` (in `07-Design/design-system/tracks/`) documents the read/export path; the integration research (item 1) will standardize the local Cowork/Code/Design wiring.

## 5. Execution via Claude Code (unified; supersedes the two earlier premature launches)
- One coordinated effort with two repos, synced via the Website Template + the status board (`07-Design/design-system/tracks/TRACKS-STATUS-BOARD.md`):
  - **Branding:** recover dropped features from `c4a4f29`; reconcile into CytoStyle; enforce v11.2.1; restore the Claude Design sync CI; publish `website-template@x.y.z`.
  - **Website:** finish reconciling the staged Gen-1 features; enforce the pinned Template; remove `.venv`; keep CI green via cytohost.
- Backups: repo bundles in `_safety-archives`; work on branches; commits as Shahin Mohammadi <mohammadi@cytognosis.org>; reconcile-not-overwrite.

## 6. Open decisions (stated, not blocking)
- Forms/CV/blog backend: FastAPI (Gen-1) vs Payload (current). Recommend Payload + port Gen-1 logic.
- Fonts: keep BOTH IranYekan (Persian) and Atkinson Hyperlegible (accessibility).

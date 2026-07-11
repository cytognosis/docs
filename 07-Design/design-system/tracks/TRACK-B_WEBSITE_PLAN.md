# TRACK B: Website Consolidation and Rebuild Plan

> **Status**: Active
> **Date**: 2026-07-11
> **Author**: @shahin
> **Audience**: designers, engineers
> **Tags**: `design`, `design-system`, `tracks`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)

**Status:** Draft, for review. **Date:** 2026-07-10. **Owner:** Shahin Mohammadi (Founder and CEO). **Reading time:** about 20 minutes; each section stands alone.

**If you only read one thing:** the website repo is not one coherent site right now. It is three unfinished migrations stacked on top of each other (Python backend to Node and Payload, a git submodule to hand-copied token files, and the old marketing site to Ali's calm redesign), and two of those layers currently break the build. `main.py` imports Python modules that no longer exist on disk, and the CI and deploy workflows build a Docker stage name the current `Dockerfile` does not define. Fix the break and adopt a pinned Website Template before touching Yar content, navigation, or animation.

## BLUF

- The live site mixes Ali's current Vite, React, Node, and Payload CMS build with orphaned Python and FastAPI code, and three copies of design tokens that disagree with each other and with the finalized Design System v11.2.1.
- CI/CD is silently broken (a Docker build-target mismatch) and does not use the `cytohost` self-hosted runner at all; this blocks everything else and should be fixed first.
- Recommended sequence: Phase 0 stops the bleeding (fix the build, pick one backend), Phase 1 adopts the pinned Website Template from Track A, Phase 2 pressure-tests every resource, Phase 3 revises Yar and the navigation, Phase 4 scopes animation for a later session.

---

## Section 1: Current State

### 1.1 What "the website" actually is right now

The repo at `~/repos/cytognosis/website` is not a single design in progress. It holds the residue of at least three separate rebuilds that each got partly merged into `main`:

| Layer | What it is | Evidence |
|---|---|---|
| **Ali's current build** | Vite 6 + React 19 landing page (15 sections), Node 22 server (`server.js`), Payload CMS 3 headless backend, Yar/Neuroverse/Research pages | `README.md`, `package.json`, `git log` merges `8abf994` and `d2ec0b2` |
| **Orphaned Python backend** | `main.py` (FastAPI), `backend/auth.py` only; every other module it imports (`database.py`, `models.py`, `admin.py`, `routes/forms.py`, `routes/blog.py`, `cv_parser.py`, `email_service.py`) is missing from disk and from git | `git ls-files backend/` returns one file; `find backend -type f` shows only compiled `.pyc` ghosts of the missing modules |
| **Old marketing site (pre-redesign)** | Glassmorphism dark theme, Vision/Mission/Values cards, a Roadmap with revenue projections, the "Helix Framework" quote, Cal.com events page, FastAPI + Jinja2 blog with comments and RSS | `_drive/inventory-current-site.md`, dated 2026-06-09, describing the site before Ali's redesign |

None of this is a guess. Run `git -C ~/repos/cytognosis/website log --oneline -30` and you see it directly: `feat/vite-frontend-serving` (the calm/ND Python-serving rebuild) and `feat/branding-consolidation-2026-07` (Ali's Yar/branding work) were both merged into `main` within the last four days, on top of each other, without a reconciliation pass. The working tree today is the union of both, including the parts that do not work together.

**The single most important fact in this plan:** the FastAPI backend that `main.py` and the `Dockerfile`'s Python stage still reference cannot start. Its imports point at five modules that do not exist. `README.md`, the current and authoritative doc, does not mention Python or FastAPI anywhere in its stated stack. This means the Python path is dead code that nobody finished deleting, not a live parallel backend. Decide this in Phase 0 (Section 8).

### 1.2 The stack, as it actually runs today

| Layer | Technology | Notes |
|---|---|---|
| Frontend build | Vite 6, React 19 | Root-level `src/` and `index.html`; NOT the `frontend/` subdirectory (see 1.3) |
| Site server | Node 22, plain `http` module (`server.js`) | Serves `dist/`, proxies to Payload, handles Google SSO admin login, has its own JSON data file fallback (`admin-data.json`) |
| Headless CMS | Payload CMS 3, Next.js 16 (`cms/`) | Collections: `users`, `media`, `posts`, `page-content`, `form-submissions` |
| Database | Postgres 16 (local, Docker Compose) / Cloud SQL Postgres 15 `cytognosis-db-prod` (prod) | Payload writes to a dedicated `payload` schema |
| PHI stories path | Node 20 + Express, separate Cloud Run service `stories-api` | Firestore, not Postgres; unrelated to the two paths above |
| Package manager | pnpm 11.5.0 (pinned) | A stray `package-lock.json` also exists at root; see Section 4 |
| Motion | GSAP + ScrollTrigger, Lenis, Motion (Framer Motion) | Desktop-only, reduced-motion aware |
| Legacy, non-functional | Python 3.13, FastAPI, SQLModel | `main.py` present; supporting modules deleted; no `requirements.txt` on disk despite the `Dockerfile` copying it |

### 1.3 Duplicate and stale directories (a structural finding, not a style note)

The repo currently carries the same content in **three or four places** at once:

| Duplicate | Locations | Status |
|---|---|---|
| Static inner pages (team, blog, contact, etc.) | `team.html` / `public/team.html` / `dist/team.html` (and same for `careers`, `contact`, `blog`, `privacy`, `terms`, `donate`, `partner`, `research`, `neuroverse`, `stories`, `yar`) | Intentional per `SITE_SOURCE_OF_TRUTH.md`: `public/*.html` is the authored copy, root-level files are "mirrored... for local preview compatibility," `dist/` is the build output. Three copies to keep in sync by hand is still a real maintenance risk. |
| Frontend app root | `frontend/` (its own `package.json`, `vite.config.js`, `src/`) vs. root-level `src/` + `vite.config.js` + `package.json` (`cytognosis-landing`) | `frontend/` is the OLD Option-A serving model described in `WEBSITE_DESIGN_HANDBOOK.md` (2026-06-09). The active build is root-level (confirmed: root `package.json`'s `build` script runs `vite build` from the repo root, and `main.py`, the only place that still references `frontend/`, is itself dead code). `frontend/` was still touched on 2026-07-06 (likely during the merge) but is not part of the live build path. |
| Design tokens | `modules/branding` (embedded, now CytoStyle), `00-CONSOLIDATION/DESIGN-TOKENS-CANONICAL.{css,json}`, `landing/styles.css` + `public/landing/styles.css` | Three sources that have already drifted from each other and from the finalized Design System. Full detail in Section 2. |
| Deploy documentation | `DEPLOY.md` (stale, describes the Python/FastAPI "Option A" flow and branch `feat/vite-frontend-serving`), `DEPLOYMENT.md` (current, matches `deploy.yml` and `compose.yaml` exactly), `README.md` (current) | Keep `DEPLOYMENT.md` and `README.md`. Retire or clearly mark `DEPLOY.md` as superseded so nobody follows its stale gcloud commands. |

**Recommendation:** none of this is safe to leave as-is while building new features on top. Section 6 and Section 8 give the concrete cleanup sequence.

### 1.4 Old-site vs. current-site feature gap

Built from `_drive/inventory-current-site.md` (the pre-redesign site, inventoried 2026-06-09) against what is actually present in the repo today.

| Feature (old site) | Status in current site | Severity |
|---|---|---|
| Cal.com events page (`events.html`) | **Gone.** No `events.html` anywhere in `public/`, root, or `dist/`. | Medium; confirm whether Cal.com booking is wanted anywhere, or formally retire it. |
| Team member self-service profile editing (`PATCH /api/team/{id}`, authenticated) | **Gone.** Payload's collection list (`users`, `media`, `posts`, `page-content`, `form-submissions`) has no `team` collection. Team bios are most likely static now. | Medium; a real capability loss if any team member relied on self-editing their bio. |
| Blog comments + RSS feed (`/blog/feed.xml`) | **Likely gone.** Payload's `posts` collection has no comment-related fields and no RSS route was found. | Low to medium; confirm before calling the blog migration complete. |
| Candidate / volunteer CV parsing (PyMuPDF + Gemini AI, structured extraction) | **Needs verification.** Not visible in `server.js` (read through line 150; the rest was not audited) or in Payload's `form-submissions` schema, which stores raw JSON with no parser hook. | Medium; if wanted, it needs a new Node-side implementation, since the old Python `CVParsingEngine` is part of the deleted `backend/cv_parser.py`. |
| Admin submissions table with CSV export and delete | **Replaced, arguably improved.** Payload's `form-submissions` collection is access-gated (`signedIn` only) and explicitly documented in its own schema as PHI-sensitive. | Gain, not a gap. Confirm CSV export still exists if anyone depends on it operationally. |
| Roadmap section with phase-by-phase metrics (500K users, $380M revenue, 25M users by Phase 3, etc.) | Gone from the live nav (no `roadmap` page found). | **Do not resurrect as-is.** Specific dollar and user-count projections read as "hard future commitments framed as dated promises," which `_drive/DO-NOT-PUBLISH.md` explicitly rules out. If a roadmap page returns, keep it directional, not numeric. |
| "Helix Framework" strategy quote and "Helix Model" as a labeled system (`Helix_model_logo.png` asset) | Not present in the current nav; the asset file may still exist on disk. | **Do not resurrect.** Per this project's own established canon, there is no Helix product; Helix is an internal org-structure and bifurcation framework, not one of the three named systems (Cytoverse, Cytoscope, Cytonome). Any old asset or copy calling Helix a product needs to be deleted, not migrated. |
| Full FAQ accordion on Contact | Not confirmed either way; `contact.html`'s current content was not read in full during this pass. | Low; verify during Section 6 IA work. |
| Online donation processor (Every.org or similar) | Neither the old nor the new site has one; both use `mailto:` or a placeholder. | Still open; `WEBSITE_DESIGN_HANDBOOK.md` already recommends Every.org (free for 501(c)(3)s). Carry that recommendation forward. |
| Slack community invite link | Never existed in either version. | Still open; default to GitHub Discussions per the existing `LAUNCH-GATES.md` decision (Section 2) unless a Slack workspace URL is supplied. |

**What the new site added, that the old site never had** (for balance, not a gap): Yar (intro, early access, feature catalog, admin dashboard, Google OAuth login), Neuroverse and Research pages, a calm/neurodiverse motion and typography system with a Reading-mode and Reduce-motion toggle, self-hosted variable fonts, and a build-time Yar data generation pipeline (`scripts/generate-yar-data.mjs`). These are real gains and should not be disturbed by the cleanup work in this plan.

---

## Section 2: Design System to Website Template to Website Repo

### 2.1 What exists today (and why it is the wrong shape)

Three things currently claim to be "the design tokens," and none of them is a proper Template consumption:

| Source | What it actually is | Problem |
|---|---|---|
| `modules/branding` | An embedded copy of the branding repo. `.gitmodules` is empty or missing, yet `git status` still reports it as a dirty gitlink ("modified content"), so the submodule wiring itself is broken. As of the last consolidation pass, this repo's content is CytoStyle: a React/MUI TypeScript component library plus IDE themes (Geany, Starship, VS Code), not CSS tokens. | Not consumable by a Vite + vanilla-CSS site without pulling in an entire unrelated MUI/React component system. Also technically broken as a submodule. |
| `00-CONSOLIDATION/DESIGN-TOKENS-CANONICAL.{css,json}` | A hand-built snapshot created in-repo on 2026-07-06 by an Antigravity consolidation pass, reconciled against spec **v10.1.0**. | Already stale: v10.1.0 has since been superseded by the finalized **v11.2.1**. It also contains an incorrect patch (see 2.3). |
| `landing/styles.css` + `public/landing/styles.css` | The actual CSS the live site renders from, hand-authored, mirrored in two places that must be kept in sync manually (a risk the project's own handbook already flags). | This is the true source of truth today, but it was never generated FROM a published Template; it is where drift originates. |

### 2.2 The target flow

```
Design System v11.2.1 (Claude Design, team Default)
        |
        v
Track A publishes a versioned "Website Template" package
  (framework-agnostic: tokens.css, self-hosted font files + @font-face,
   shared component CSS classes for buttons/cards/nav)
        |
        v
Website repo pins an exact version and fetches it at build/install time
        |
        v
public/landing/tokens.generated.css  (produced from the pinned package, never hand-edited)
landing/styles.css                    (hand-authored layout, motion, page rules;
                                        imports/extends the generated tokens, does not redeclare them)
```

The website repo should never again hand-copy hex values or redeclare `:root` tokens locally. It should **consume** a package it does not author.

### 2.3 A concrete contradiction to resolve first

The 2026-07-06 consolidation pass patched `landing/styles.css` to replace Space Grotesk with Inter for the display font, reasoning that spec v10.1.0 called for "Inter only." That reasoning is now **superseded**. The finalized v11.2.1 (this track's own starting context) explicitly names **Space Grotesk as the display font**, and the live site's actual hero treatment (Space Grotesk weight 500 at 64px) matches that. **Recommendation: revert the Jul 6 Inter patch.** Space Grotesk stays. This is not a new decision; it is un-reverting a change that was correct in June, patched incorrectly in July against a stale spec, and is correct again now that v11.2.1 is final.

The rest of that consolidation pass's drift table has, in fact, already resolved itself correctly: warm beige `#F4F2EF` (not the cooler "Ghost Day" `#F8F8FC`) and the azure-violet-indigo gradient at 135 degrees are both exactly what v11.2.1 specifies and what the live site already does. No further action needed there beyond formally retiring the documents that still call them "drift."

### 2.4 Fetch and pin mechanism (recommendation)

Kill both the git-submodule pattern (already broken, and this is its second failure mode after Ali's total CytoStyle replacement) and the ad hoc canonical-file pattern (already stale twice in five weeks). Replace with:

1. **Track A tags a release** on the branding repo: `website-template-v1.0.0`, with a build step that outputs a small, framework-agnostic bundle (tokens CSS, font files, a handful of shared component classes) as a zip release asset.
2. **The website repo adds `scripts/fetch-template.mjs`**, run as a `pnpm build` prestep and in CI, that downloads the pinned release asset into `vendor/website-template/` and verifies it against a checksum committed in a `TEMPLATE_VERSION.lock` file. A version bump is then a one-line, reviewable diff in a pull request, not a silent drift.
3. **`public/landing/tokens.generated.css`** is generated from that vendored bundle at build time and is never hand-edited; `landing/styles.css` imports it.
4. If a private npm-compatible registry ever gets built for other reasons (the org already runs a Python-package equivalent at `us-central1-python.pkg.dev/cytognosis-infrastructure/cytognosis-python/simple/`), migrate to a real pinned npm dependency (`@cytognosis/website-template`) instead of the release-asset fetch. Do not build that registry just for this; the release-asset approach works today with zero new infrastructure.

### 2.5 Interlock dependency (flag now, not later)

Per this project's own record, Track A's branding repo is mid-recovery: Ali replaced the entire CSS/token system with CytoStyle, and restoring a clean, publishable set of web tokens is gated on a conversation with Ali that has not happened yet. **This means Track B's Phase 1 (Section 8) cannot start until that conversation happens.** Track B can and should proceed with Phase 0 (Section 8) in the meantime, but should freeze further hand-edits to `00-CONSOLIDATION/*` so a third drift event does not get created while waiting.

---

## Section 3: Resources and Databases Pressure Test

### 3.1 Full inventory

| # | Resource | Kind | Project | PHI? |
|---|---|---|---|---|
| 1 | `cytognosis-website-v2` | Cloud Run service ("site" Docker target) | `cytognosis-phi-prod` | No |
| 2 | `cytognosis-cms` | Cloud Run service (Payload, "cms" Docker target) | `cytognosis-phi-prod` | Partial (form submissions) |
| 3 | `stories-api` | Cloud Run service, Node/Express | `cytognosis-phi-prod` | **Yes** |
| 4 | `cytognosis-db-prod` | Cloud SQL Postgres 15 (`db-custom-1-3840`), database `cytognosis_website`, user `cytognosis_app` | `cytognosis-phi-prod` | Partial |
| 5 | Firestore (`stories` + `audit_logs` collections) | NoSQL, native mode, `nam5` | `cytognosis-phi-prod` | **Yes** |
| 6 | GCS PHI buckets: `-active`, `-archive`, `-vault`, `-prod-data`, `-core` | Storage, tiered, CMEK | `cytognosis-phi-prod` | **Yes** |
| 7 | GCS shared buckets: `-audit-7yr` (locked), `-data-hub`, `-public-data`, `-internal` | Storage | `cytognosis-infrastructure` | Mixed |
| 8 | KMS keyring `cytognosis-phi-keys` (`storage-key`, `bigquery-key`) | Encryption, 90-day rotation | `cytognosis-phi-prod` | N/A |
| 9 | BigQuery: `genomics_variants`, `clinical_data`, `pipeline_metadata`, `audit_logs` | Analytics | `cytognosis-data` (**project existence itself unconfirmed** in the source infra map) | Regulated |
| 10 | Secret Manager (7 secrets: session key, DB URL, OAuth client ID/secret, Payload API key, Payload bootstrap password) | Secrets | `cytognosis-phi-prod` | No |
| 11 | Artifact Registries (Docker x2, Python package index x1) | CI/CD | `cytognosis-phi-prod` / `cytognosis-infrastructure` | No |
| 12 | Local dev Postgres (Docker Compose, default password `localdev2026`) | Dev only | N/A | No |
| 13 | `backend/cytognosis.db`, `backend/database.db` | SQLite, both 0 bytes | Orphaned | No |
| 14 | Legacy GCS static bucket `gs://www.cytognosis.com` + Cloud CDN URL map `https-um-cytognosis` | Storage + CDN | Unknown | No |
| 15 | Google OAuth client (visible client ID) | Auth | Google Cloud | No |
| 16 | `cytohost` VM (`136.111.39.188`), serving `cal.`, `code.`, `hub.` subdomains | Self-hosted infra | `cytognosis-infrastructure` (DNS) | No |

### 3.2 Per-resource checklist

Run all six checks below for every numbered resource above. This plan defines the checklist; Phase 2 (Section 8) executes it.

| Check | What it means |
|---|---|
| **Exists** | Confirm the resource is actually provisioned, not just documented. (Item 9's project existence is explicitly unconfirmed today; item 14's decommission status is unconfirmed.) |
| **Reachable** | Health-check or connect from a location that matches production network rules. |
| **Migrations** | Schema/migration state is current and was applied to the real environment, not just local dev. |
| **Backups** | A backup or retention policy exists and has been tested at least once (not just configured). |
| **Secrets** | The resource's credentials live in Secret Manager, not in `.env`, code, or a default fallback. |
| **Load** | A basic sense of expected traffic/volume exists so a launch does not surprise it. |

### 3.3 Specific findings worth flagging now (not waiting for Phase 2)

- **Two Google OAuth integration paths exist simultaneously**: `server.js`'s admin login flow (redirect URI `https://cytognosis.org/admin/oauth/callback`, per `DEPLOYMENT.md`) and Payload's own `googleAuthStrategy` with its own `/auth/google/start` and `/auth/google/callback` endpoints (`payload.config.ts`). Confirm both redirect URIs are registered on the actual Google Cloud OAuth client, and that nobody has confused which flow serves which login screen.
- **`/auth/dev_login`** (the long-flagged unguarded admin-session endpoint) lives in `backend/auth.py`, which is part of the currently non-functional Python path. Its risk is moot only because that app cannot start today. If anyone "fixes" the missing Python imports without first deleting `dev_login`, the hole reopens. The single-backend decision in Phase 0 (Section 8) should close this permanently by retiring the Python path outright, rather than patching it.
- **`dist/` (build output) is committed to git**, 82 tracked files, and is not gitignored. Every fresh `pnpm build` produces new content-hashed filenames that show up as untracked changes. This is why `git status` currently shows five untracked `dist/*` files. Build artifacts should not be committed at all; the Docker build produces `dist/` fresh every time.
- **The repo just recovered from committing `node_modules/`** (43,595 files, over 124 MB), which blocked `git push` against GitHub's 100 MB file-size limit. Fixed 2026-07-08 by Shahin directly. Confirm the next push after that fix actually succeeded and triggered a deploy; do not assume it did.
- **Mixed package manager lockfiles**: both `package-lock.json` and `pnpm-lock.yaml` exist at root, same timestamp. `ci.yml` uses pnpm exclusively via `corepack`. Delete `package-lock.json` to remove the risk of someone running plain `npm install` and drifting the lockfile.
- **The legacy GCS static bucket and CDN URL map** (`gs://www.cytognosis.com`, `https-um-cytognosis`) were flagged as "dead" in the old inventory but never confirmed torn down. Verify and decommission, or confirm it is already gone, so it stops being a stale-content or cost risk.

---

## Section 4: CI/CD Verification

### 4.1 What exists

Two workflows, both recently touched (`ci.yml` and `deploy.yml`, both edited 2026-07-06):

| Workflow | Trigger | Job | What it does |
|---|---|---|---|
| `.github/workflows/ci.yml` | Pull request into `main` | `build` | Installs with pnpm, runs `pnpm build`, then runs `docker build --target site` and `docker build --target cms` as build tests |
| `.github/workflows/deploy.yml` | Push to `main` | `deploy` | Authenticates via Workload Identity Federation, builds `--target site`, pushes to Artifact Registry, deploys to Cloud Run (`cytognosis-website-v2`), routes traffic, runs a health check with retries |

### 4.2 The break

Both workflows build Docker images using `--target site` (and `ci.yml` also uses `--target cms`). **The current `Dockerfile` has no stage named `site` and no stage named `cms`.** It defines exactly one named stage (`AS frontend`, the Node build stage) followed by an unnamed final Python/FastAPI stage (`FROM python:3.13-slim`, ending in `CMD ["uvicorn", "main:app", ...]`). A `docker build --target site` against this file fails outright with "failed to reach build target."

This means, as currently committed, **both CI and the production deploy path are broken.** Either:
- the last successful production deploy predates this Dockerfile, and `cytognosis.org` is currently serving a stale revision, or
- nobody has pushed to `main` since this mismatch was introduced, so the break has not yet been exercised.

Both explanations point to the same fix: **rewrite the `Dockerfile` with explicit `site` and `cms` named stages** that match what `compose.yaml`, `ci.yml`, and `deploy.yml` all already assume (a Node-based `site` server plus a separate Next.js/Payload `cms` server), replacing the current Python-oriented single-stage design entirely. This is the same decision as the single-backend call in Section 1 and Section 8; it is one fix, not two.

### 4.3 Other CI/CD gaps

| Gap | Detail | Recommendation |
|---|---|---|
| **No automated deploy for the `cms` Cloud Run service** | `DEPLOYMENT.md` documents `cytognosis-cms` as a deployed service, but `deploy.yml` only builds and deploys the `site` target. The CMS service's deployment path is not visible in any workflow. | Add a second job (or a matrix) to `deploy.yml` that builds and deploys the `cms` target to its own Cloud Run service, so a `cms/` code change actually ships. |
| **`cytohost` is not used anywhere** | Both workflows run on `runs-on: ubuntu-latest` (GitHub-hosted). `cytohost` (the self-hosted VM at `136.111.39.188`, already carrying `cal.`, `code.`, and `hub.` subdomains, and registered as a runner per this org's own infra consolidation record) is not referenced in either workflow. | Confirm the exact runner label registered for `cytohost` (not found in any repo checked during this pass; likely only visible in the GitHub org's runner settings or the standalone `~/repos/cytognosis/infrastructure` repo), then switch at least `deploy.yml`, and ideally `ci.yml`, to `runs-on: [self-hosted, cytohost]` or the equivalent label. Verify the runner is online before cutting over, not after. |
| **No rollback runbook** | `DEPLOY.md` (stale) shows a staged, no-traffic-then-shift pattern for the old single-service model. Nothing current documents rollback for either `site` or `cms`. | Write a one-page rollback runbook: `gcloud run services update-traffic <service> --to-revisions=<PREVIOUS_REVISION>=100 --region=us-central1 --project=cytognosis-phi-prod`, for both services, plus how to find the previous good revision. |
| **`dist/` committed to git** (see 3.3) | Creates noisy diffs and risks a stale committed `dist/` shipping instead of the CI-built one, depending on `.dockerignore` behavior. | Gitignore `dist/`, rely on the Docker build stage to produce it fresh every time. |

### 4.4 Verification checklist for Phase 2

- [ ] Confirm the exact `cytohost` runner label and that the runner is currently online.
- [ ] Rewrite `Dockerfile` with named `site` and `cms` stages; confirm `docker build --target site` and `--target cms` both succeed locally before touching CI.
- [ ] Add the missing `cms` deploy job.
- [ ] Switch both workflows to the `cytohost` runner (or document explicitly why not, if there is a good reason to keep `ci.yml` on GitHub-hosted runners for PR speed).
- [ ] Write and test the rollback runbook against a real previous revision.
- [ ] Confirm the latest push after the `node_modules` fix (2026-07-08) actually deployed; check the live site's served revision against `git rev-parse HEAD`.
- [ ] Gitignore `dist/`; remove the 82 currently-tracked files from git in a dedicated commit.

---

## Section 5: Yar Sections Revision Scope

### 5.1 What exists

- **Canonical catalog**: `docs/YAR_FEATURE_CATALOG.md` (dated 2026-06-26, explicitly "canonical front door for all Yar features"). 62 features (F01 to F62) across 6 neurodivergent functional domains (attention/executive function, emotion regulation/mood, social/communication, sensory/processing, cognition/thought organization, self-monitoring/insight), plus 5 infrastructure features and 2 gating modules (privacy boundary, crisis detection). Organized into Wave 0 through Wave 3 by an Impact Priority Score.
- **Live pages**: `yar/early-access.html`, `yar/features.html` (each present in three copies: root, `public/`, `dist/`, same pattern as Section 1.3), an admin dashboard, and Google OAuth login for the Yar admin panel.
- **Data pipeline**: `scripts/generate-yar-data.mjs` produces `yar-data.js` / `yar-data.json` at build time (`pnpm build` runs it before `vite build`).
- **A dedicated stylesheet**: `landing/yar.css` (added via a specific fix commit, "add yar.css to public/landing/ so it deploys to dist/"), separate from the site's main `styles.css`.

### 5.2 Revision scope (content and alignment, per the task's own framing)

| Item | What to check | Why |
|---|---|---|
| **Feature accuracy** | Does `yar/features.html`'s displayed content match the current canonical Wave 1 set (25 features, founder-elevated in v1.1) from `docs/YAR_FEATURE_CATALOG.md`, or an earlier, stale cut? | The catalog itself says it "supersedes the 05-31 feature master and all pre-v4 comparisons"; the live page needs to match the current version, not a snapshot from before that supersession. |
| **Single source of truth** | Confirm `scripts/generate-yar-data.mjs` reads from (or is kept in lockstep with) `docs/YAR_FEATURE_CATALOG.md`, not a separately hand-maintained copy of the feature list. | Two hand-maintained copies of the same 62-feature list is exactly the kind of drift this whole track exists to prevent. |
| **Token alignment** | Does `landing/yar.css` use the same tokens as `landing/styles.css` (once that pulls from the Website Template per Section 2), or has it drifted its own colors/spacing? | A dedicated stylesheet is fine; a dedicated set of hardcoded hex values is not. |
| **Nav placement** | Yar is already a top-level nav item on the live site (confirmed by direct inspection), consistent with its status as the flagship product. Keep it there; see Section 6 for the full nav proposal. | Matches the org's own priority: Yar is "by neurodivergent people, for neurodivergent people," a mission-congruence signal, not a secondary feature. |
| **Open catalog items** | The catalog itself lists five open integration deltas (benchmark numbers into a spec, a module reference fix, retiring a dated snapshot folder, confirming ADHD-Obsidian variant coverage, retiring a stale 05-31 master). These are docs-repo housekeeping, not website work, but the website's copy should not contradict whichever version wins. | Keeps the website's Yar copy from citing a spec detail that the docs-repo itself is about to retire. |

This section is scope, not execution. Section 8 places it in Phase 3.

---

## Section 6: Website Organizational-Structure Revision

### 6.1 Three navigation structures currently disagree

| Source | Nav |
|---|---|
| Old site (`_drive/inventory-current-site.md`) | About (dropdown: Our Story, Technology, Roadmap, Strategy), Team, Careers (dropdown), Blog, Contact, Get Involved (dropdown: Community, Partner, Stories), Log In |
| June 9 handbook proposal (`WEBSITE_DESIGN_HANDBOOK.md`) | Home, Science, Blog, Team, Get Involved (dropdown), Contact |
| **Live site today** (direct inspection) | Home, Yar, Neuroverse, Research, Blog, About, Contact, Early Access |

None of these three is wrong exactly; they are three successive, uncoordinated decisions. The live nav is the one that matters because it is what visitors see, and it already correctly elevates Yar and Neuroverse to top-level status.

### 6.2 Recommended nav (one proposal, not options)

**Home, Platform, Neuroverse, Yar, Research, Blog, About, Get Involved (dropdown), Contact**, plus a persistent **Early Access** button styled as a call to action, not a nav link.

Rationale:
- **Platform** replaces the old "Science"/"Technology" idea and folds in Cytoverse, Cytoscope, and Cytonome as one destination, matching the three-system framing already established for this org.
- **Neuroverse, Yar, and Research** each stay top-level because they are the three things visitors are most likely to arrive looking for directly (the public flagship program, the flagship ND product, and the evidence base). Flattening them into dropdowns would bury the org's actual current focus.
- **Get Involved** absorbs Partner, Share Your Story, Careers, Volunteer, Community, and Donate into one dropdown. Six separate top-level items would violate the neurodiverse design principle already established for this project (minimize top-level choices, one clear task per page); one grouped entry with six clear sub-destinations keeps the choice architecture calm without losing any of the six paths.
- **About** carries Team, the origin story, and org background as one page with anchors, matching what the old site did well and what the live Team page already contains.

### 6.3 Page taxonomy and file-structure cleanup

| Action | Detail |
|---|---|
| Pick one authored location for static HTML | `public/*.html`, per `SITE_SOURCE_OF_TRUTH.md`'s own stated intent. Stop treating root-level mirrors as anything but a local preview convenience, and confirm the mirror step is automated (not manually copy-pasted) if it needs to continue at all. |
| Retire `frontend/` | Confirm nothing in the live build path references it (Section 1.3), then delete it. Its only remaining reference is inside the dead Python path. |
| Retire `00-CONSOLIDATION/*` | Superseded by the Website Template pipeline (Section 2) once that lands. Keep the markdown reports as historical record if useful, but stop treating the CSS/JSON files there as a source of truth. |
| Pick one backend | Node (`server.js`) + Payload, per `README.md`. Archive `main.py`, the Python `Dockerfile` stage, and any remaining `backend/*.py` rather than leaving it half-deleted. This single decision also permanently closes the long-standing `/auth/dev_login` security gate (Section 3.3). |
| Consolidate deploy docs | Keep `DEPLOYMENT.md` and `README.md`. Mark `DEPLOY.md` as superseded or delete it; its Python-era commands would actively mislead anyone who runs them today. |
| Remove dead local files | `backend/cytognosis.db`, `backend/database.db` (both 0 bytes), `package-lock.json` (Section 3.3). |

---

## Section 7: Animated Visualizations (Scope Only)

Per this track's brief, actual design and build work happens in dedicated later sessions. This section only scopes candidates and the constraints they must obey.

### 7.1 Candidate visualizations

| Candidate | Where it would live | Basis |
|---|---|---|
| Disease-as-trajectory chart | `TrajectorySection` on the landing page (already exists as a GSAP-scrubbed SVG; already reduced in scope during Phase 7a of the calm-motion work) | Existing content, already partially built |
| Cytoverse coordinate-map animation | Platform section or a dedicated `/platform` page | Visualizes the "GPS for health" metaphor directly: points moving through a coordinate space rather than a static diagram |
| Signal-layers stack | `SignalLayersSection` (already exists) | The five-layer stack (molecular, brain circuits, physiology, behavior, clinical) is a natural candidate for a calmer, non-scrubbed reveal |
| Yar feature-wave map | A future Yar page | 62 features across waves 0 to 3 is naturally a roadmap-style animated view, distinct from a static table |
| Cytoscope sensor/UBAP animation | Platform or Cytoscope-specific page | Visualizes the active-reset sensor architecture and the open UBAP standard |

### 7.2 Constraints that apply to all future animation work (non-negotiable, already established)

- Must respect the combined reduce-motion signal (OS preference OR the in-page toggle), per `design-system-decision-v2.md` Section 4.
- No scroll-jacking. Opacity and scale entrances only; no large parallax or scrub-driven motion, which the org's own neurodiverse design research already identified as the single biggest risk factor.
- No infinite looping peripheral motion (WCAG 2.2.2).
- Motion durations must come from the Website Template's motion tokens (Section 2) once that pipeline exists, not hardcoded GSAP values as `ScrollScenes.jsx` currently does.

This plan does not design these animations. It flags them so the dedicated future sessions have a starting list and do not have to rediscover the constraints.

---

## Section 8: Phased Execution, Track A Interlock, and Open Questions

### 8.1 Phases

| Phase | Focus | Depends on |
|---|---|---|
| **Phase 0: Stop the bleeding** | Rewrite `Dockerfile` with named `site`/`cms` stages; decide and commit to Node + Payload as the one backend; archive the Python path; gitignore `dist/`; delete `package-lock.json`; confirm the current production deploy is actually healthy | Nothing; can start immediately |
| **Phase 1: Template pipeline** | Track A publishes the Website Template; website repo adopts the pinned fetch mechanism (Section 2); retire `00-CONSOLIDATION/*` and the broken `modules/branding` submodule reference; revert the Space Grotesk to Inter patch | **Blocked on the Ali conversation** about branding-repo recovery (Section 2.5) |
| **Phase 2: Pressure test + CI/CD hardening** | Execute the Section 3 checklist against all 16 resources; wire `cytohost` into CI/CD; add the missing `cms` deploy job; write and test the rollback runbook; verify OAuth redirect URIs and the legacy GCS bucket's decommission status | Phase 0 |
| **Phase 3: IA and Yar revision** | Implement the Section 6 nav; execute the Section 5 Yar content and alignment checks | Phase 1 (tokens must be stable before touching page content that depends on them) |
| **Phase 4: Animation sessions** | Execute the Section 7 candidates, in dedicated later sessions | Phase 1 (motion tokens must exist in the Template first) |

### 8.2 Interlock with Track A

The Website Template is the shared contract between the two tracks. Track A owns its content and versioning; Track B owns consuming it correctly and never re-authoring it locally. Track B's Phase 1 is explicitly blocked until Track A's branding-repo recovery (gated on the pending Ali conversation) produces a publishable, framework-agnostic template rather than the current CytoStyle React/MUI package. Flag this dependency to Shahin directly: **the Ali conversation is now also a Track B blocker, not only a Track A one.**

### 8.3 Recommendations on the open questions (stated as decisions, not a menu)

| Question | Recommendation | Rationale |
|---|---|---|
| Which backend survives? | **Node (`server.js`) + Payload CMS.** Archive the Python/FastAPI path entirely. | Matches `README.md`, the current and only doc that describes the stack without contradiction; the Python path is already half-deleted and cannot start. |
| How does the website fetch the Template? | **Pinned GitHub Release asset + a fetch script**, checksum-verified, version-locked in a committed file. | No new registry infrastructure needed; works today; a version bump becomes a reviewable one-line diff. |
| Space Grotesk or Inter for display? | **Space Grotesk.** Revert the July 6 patch. | Matches the finalized v11.2.1 spec and the live site's actual current rendering; the patch was made against a since-superseded v10.1.0. |
| Nav structure | The eight-item structure in Section 6.2. | Balances flagship-surface visibility (Yar, Neuroverse, Research) against the org's own calm/low-choice design principle. |
| Donation processor and community channel | **Every.org embed** and **GitHub Discussions** (switch to Slack only if a workspace URL is actually supplied). | Already the standing default recorded in this project's own prior decisions; nothing has changed to revisit it. |

---

**File written:** `Science and Platform/design-system-merge-2026-07/05_tracks/TRACK-B_WEBSITE_PLAN.md`
**Simple companion:** `05_tracks/simple/TRACK-B-WEBSITE-simple.md`

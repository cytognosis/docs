> **Status**: Active
> **Date**: 2026-06-14
> **Author**: Cytognosis Foundation
> **Audience**: engineers, front-end developers
> **Tags**: `templates`, `cytognosis-template-master`, `interface`, `scaffolding`

# cytognosis-template-master — Interface Template Skill

> **Reading time**: ~7 minutes
> **If you only read one thing**: Load this skill before writing any code for a Cytognosis product surface (website, phone app, web dashboard, desktop app, browser extension). Read the SKILL.md, then `references/general.md`, then the per-template delta file.

---

## What It Is and Why

`cytognosis-template-master` is the master entry skill for the five Cytognosis interface templates. Each template provides a scaffold for a specific product surface: public website, patient phone app, logged-in web dashboard, desktop supervisor app, or browser extension. The skill routes to per-template delta files while carrying cross-template essentials at the surface.

**When to load this skill**:

- Scaffolding any new Cytognosis product surface
- Revising or porting changes across templates
- Building or wiring the seven shared packages
- Any task mentioning: Astro, Flutter, React 19/Vite, Tauri, Manifest V3, LiteRT-LM, voice loop, supervisor sidecar, cytognosis.org
- Choosing a template for a new product

**When NOT to load this skill**:

- Visual tokens, brand voice, microcopy: load `cytognosis-design-system-master`
- Development tooling (nox, cytocast, uv): load `cytognosis-dev`
- Do not load this skill and `cytognosis-design-system-master` in the same response

---

## The Five Templates

| Template | Framework | Default Profile | Primary Use |
|----------|-----------|----------------|-------------|
| `app-website` | Astro + FastAPI backend | Foundation (public) / Research (admin) | Public cytognosis.org site: about, team, stories, blog, forms, admin |
| `app-phone` | Flutter | Clinical | Interviewer agent (voice-first); asset/knowledge-hub mobile client |
| `app-web` | React 19 + Vite + Tailwind + shadcn | Foundation (logged-out) / Research (logged-in) | Logged-in dashboards, asset hub, internal product surfaces |
| `app-desktop` | Tauri v2 wrapping app-web | Research | Internal hub, supervisor-agent sidecar host, local-first editor |
| `app-extension` | Manifest V3 + side panel | Clinical (patient) / Lab (internal) | Patient asset companion; internal clipping / annotation power tool |

**Key distinction**: `app-website` is the **public marketing + content site**; `app-web` is the **logged-in SPA** for product surfaces. They share the design system but not the runtime.

All templates live under `cytoskeleton/templates/app-<name>/`. They consume shared packages from `cytoskeleton/templates/shared/` and brand tokens from `branding/design-system/`.

---

## Reading Order (For Any Template Task)

1. Read this SKILL.md (confirm which template applies; load cross-template rules)
2. Read `references/general.md` (cross-template rules, the shared 70%)
3. Read `references/<template-name>.md` (template-specific delta, the unique 30%)

If a delta and the general reference conflict, **the delta wins** for that template.

---

## The Seven Shared Packages

Every template wires the same seven packages:

```
templates/shared/
├── design-system-package/      Consumes brand-repo tokens; exports framework-native primitives
├── api-client-package/         Generated from cytos OpenAPI; typed endpoints + streaming
├── fabric-client-package/      Wraps cytoagent's TS + Dart SDK; useAgent / useEvent / useCrdtDocument / useCrisisRail
├── voice-client-package/       VAD + barge-in; emits schema-enforced feature events; never sends raw audio
├── auth-shell-package/         Pluggable auth provider; per-platform token storage
├── telemetry-package/          Schema-enforced events; redaction defaults; opt-in by default
└── agent-presentation-package/ Shared visual language for agent presence (avatar, state, turn-taking)
```

Do not re-implement these in template body code. If you find yourself writing a `useAgent` hook, surface to revise `fabric-client-package` instead.

---

## Cross-Template Mandatory Baselines

Every template, on first scaffold:

1. **Seven starter screens**: welcome / home / settings / consent-prompt / crisis-safety / empty-state / error-state
2. **`microcopy.json`**: keyed for every visible string; no string literals scattered in components
3. **Accessibility**: focus management on route changes, keyboard nav, reduced-motion variants, screen-reader support, target sizes (44pt phone, 24px web, 32px patient-facing), color independence
4. **Telemetry wired**: schema-enforced events; default redaction; opt-in for non-essential events; debug overlay (dev flag)
5. **Voice surface** (phone, web, desktop): on-device feature extraction; raw audio never crosses device boundary; barge-in supported
6. **Agent presence widget**: rendered via `agent-presentation-package`
7. **Quality gates pass**: biome, dart analyze, clippy, ruff (Python hooks), commitlint, actionlint
8. **Docs**: README, architecture, accessibility, privacy, voice (if applicable), deployment
9. **`.agents/skills/manifest.yaml`**: declaring dev-skill dependencies
10. **Brand voice**: every visible string follows voice rules from `branding/design-system/WRITING.md`

---

## Quality Gates

| Gate | Tool | Threshold |
|------|------|-----------|
| Lint | biome / dart analyze / clippy | Zero warnings |
| Type | tsc strict / mypy / dart analyzer | Zero errors |
| Coverage | per-template runner | 80% line minimum |
| Accessibility | axe-core / Flutter a11y scanner | Zero critical or serious |
| Build determinism | reproducible build flag | Identical artifact on re-build |

---

## Privacy Posture (Non-Negotiable)

1. **No raw audio leaves the device.** The `voice-client-package` enforces this; do not bypass.
2. **No PII in telemetry.** The `telemetry-package` redaction defaults enforce this.
3. **Consent before escalation.** Any action escalating to a cloud tier requires a positive consent grant in the CRDT ledger.
4. **Local-first state.** Iroh CRDT documents are the default for state that should survive offline.
5. **Auditable.** The debug overlay (dev-only) shows what is sent.

---

## Brand Voice in Microcopy

All visible strings adhere to these rules:

- No em dashes
- No "user"; use "patient", "clinician", "researcher", or "you"
- No hype words
- Title Case headings, sentence case for UI labels
- Active present tense
- Per-profile dials: Clinical = warmest / shortest; Foundation = warm / short; Research = least warm / longest; Lab = least warm / short

---

## Cytocast Generation Flow

```bash
# Scaffold a new product from a template
uvx copier copy https://github.com/cytognosis-foundation/cytocast \
                ~/repos/cytognosis/<new-product> \
                --data profile=interface-template \
                --data template=app-<name> \
                --data product_name=<product-name> \
                --data brand_profile=cytognosis-primary

# Initial commit
cd ~/repos/cytognosis/<new-product>
git init && git add . && git commit -m "chore: initial scaffold from cytocast"

# Resolve env (examples)
uv sync         # Python
flutter pub get # phone
cargo build     # desktop
pnpm install    # web / extension

# Run starter screens
flutter run     # phone
npm run dev     # web
tauri dev       # desktop
# extension: load unpacked at chrome://extensions after npm run dev:extension
```

---

## Profile Defaults per Template

| Template | Profile Default |
|----------|----------------|
| app-website (public pages) | Foundation |
| app-website (stories pages) | Clinical |
| app-website (admin) | Research |
| app-phone | Clinical |
| app-web (logged-in) | Research |
| app-desktop | Research |
| app-extension (patient mode) | Clinical |
| app-extension (internal mode) | Research or Lab |

These are defaults, not enforced. The cytocast scaffold prompt asks for the profile choice.

---

## Per-Template Delta Routing

| Load `references/website.md` when | Load `references/phone.md` when |
|-----------------------------------|--------------------------------|
| cytognosis.org, Astro, MDX, Pagefind | Flutter, Dart, LiteRT-LM, HuBERT, VAD |
| Blog, stories, team page, SEO, JSON-LD | Crisis detector, interviewer agent |
| FastAPI + Jinja, form submission, OAuth admin | iOS, Android, App Store, Play Store |

| Load `references/web.md` when | Load `references/desktop.md` when |
|-------------------------------|----------------------------------|
| React, Vite, Tailwind, shadcn, TanStack | Tauri v2, Rust, Cargo.toml |
| Logged-in SPA, dashboard, PWA | System tray, native menu, sidecar |
| TypeScript, biome, tsconfig | Supervisor agent |

| Load `references/extension.md` when |
|------------------------------------|
| Browser extension, Manifest V3, side panel |
| Content script, Chrome Web Store |
| Patient mode or internal mode build flag |

---

## Hard NEVER List

- Never bypass `voice-client-package` to send raw audio
- Never write telemetry events without a registered schema
- Never inline a hex color literal; consume design-system tokens
- Never reintroduce a component contract change locally; surface to the design system
- Never write new agent skills inside a template; skills live in the four-phase model
- Never request broad permissions (extensions: never `<all_urls>`; desktop: scoped filesystem only)
- Never include analytics or ad SDKs
- Never ship with em dashes in any string

---

## Sibling Skills

| Task | Skill |
|------|-------|
| Visual / voice tokens, brand rules, microcopy patterns | `cytognosis-design-system-master` |
| Cytocast / cytoskeleton config / nox / pyproject details | `cytognosis-dev` |
| Where files live, GCP / Workspace ops | `cytognosis-org` |
| Grants, narrative, scientific writing | `cytognosis-writer` |
| Unsure which skill | `cytognosis-orchestrator` |

---

## Example: Scaffold a New Phone App

Task: "Create a new patient interviewer app."

```bash
uvx copier copy https://github.com/cytognosis-foundation/cytocast \
    ~/repos/cytognosis/interviewer-app \
    --data profile=interface-template \
    --data template=app-phone \
    --data product_name=InterviewerApp \
    --data brand_profile=cytognosis-primary

cd ~/repos/cytognosis/interviewer-app
git init && git add . && git commit -m "chore: initial scaffold from cytocast"
flutter pub get
flutter run
```

Then:

1. Load `references/general.md` for shared package wiring
2. Load `references/phone.md` for Flutter-specific delta (LiteRT-LM, HuBERT, voice loop)
3. In a separate response, load `cytognosis-design-system-master` for Clinical profile tokens and voice rules

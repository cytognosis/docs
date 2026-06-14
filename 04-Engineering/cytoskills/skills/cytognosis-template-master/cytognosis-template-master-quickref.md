> **Status**: Active
> **Date**: 2026-06-14
> **Author**: Cytognosis Foundation
> **Audience**: engineers, front-end developers
> **Tags**: `quick-reference`, `cytognosis-template-master`

# cytognosis-template-master — Quick Reference

> **One line**: Load this skill before writing any code for a Cytognosis product surface (website, phone app, web dashboard, desktop app, browser extension); it provides the scaffold, shared packages, and quality gates for all five interface templates.
> **Full doc**: [cytognosis-template-master.md](cytognosis-template-master.md)

---

## Key Concepts

| Term | Definition |
|------|-----------|
| **app-website** | Public cytognosis.org site (Astro + FastAPI; content-first, SEO-critical). NOT the same as app-web. |
| **app-web** | Logged-in SPA for product surfaces (React 19 + Vite + shadcn; auth-gated, interactive). |
| **app-phone** | Flutter patient app (voice-first interviewer agent; Clinical profile). |
| **app-desktop** | Tauri v2 wrapping app-web (Research profile; supervisor sidecar). |
| **app-extension** | Manifest V3 browser extension (patient mode = Clinical; internal mode = Research/Lab). |
| **Seven shared packages** | design-system, api-client, fabric-client, voice-client, auth-shell, telemetry, agent-presentation. Consumed by all templates. |
| **Delta file** | Per-template rules in `references/<template-name>.md` that override `references/general.md` for that template. |

---

## Template → Framework → Profile

| Template | Framework | Default Profile |
|----------|-----------|----------------|
| `app-website` | Astro + FastAPI | Foundation (public) / Research (admin) |
| `app-phone` | Flutter | Clinical |
| `app-web` | React 19 + Vite + Tailwind + shadcn | Research (logged-in) |
| `app-desktop` | Tauri v2 | Research |
| `app-extension` | Manifest V3 | Clinical (patient) / Lab (internal) |

---

## Commands

```bash
# Scaffold any product surface
uvx copier copy https://github.com/cytognosis-foundation/cytocast \
    ~/repos/cytognosis/<new-product> \
    --data profile=interface-template \
    --data template=app-<name> \
    --data product_name=<ProductName> \
    --data brand_profile=cytognosis-primary

# Initial commit
cd ~/repos/cytognosis/<new-product>
git init && git add . && git commit -m "chore: initial scaffold from cytocast"
```

---

## Env Init (by template)

| Template | Command |
|----------|---------|
| `app-phone` | `flutter pub get && flutter run` |
| `app-web` | `pnpm install && npm run dev` |
| `app-desktop` | `cargo build && tauri dev` |
| `app-extension` | `pnpm install && npm run dev:extension` (load unpacked at `chrome://extensions`) |
| `app-website` | `uv sync && nox -s init_project` |

---

## Delta File Routing

| Trigger | Load |
|---------|------|
| cytognosis.org, Astro, MDX, Pagefind, blog, SEO, JSON-LD | `references/website.md` |
| Flutter, Dart, LiteRT-LM, HuBERT, VAD, iOS, Android | `references/phone.md` |
| React, Vite, Tailwind, shadcn, logged-in SPA, dashboard | `references/web.md` |
| Tauri, Rust, system tray, sidecar, macOS/Windows/Linux | `references/desktop.md` |
| Manifest V3, side panel, content script, Chrome Web Store | `references/extension.md` |

---

## Quality Gates

| Gate | Tool | Threshold |
|------|------|-----------|
| Lint | biome / dart analyze / clippy | Zero warnings |
| Type | tsc strict / mypy / dart analyzer | Zero errors |
| Coverage | per-template runner | 80% minimum |
| Accessibility | axe-core / Flutter a11y scanner | Zero critical/serious |
| Build | reproducible build flag | Identical artifact on re-build |

---

## Cross-Template Baselines (All Templates)

1. Seven starter screens (welcome, home, settings, consent-prompt, crisis-safety, empty-state, error-state)
2. `microcopy.json` for every visible string
3. Accessibility: focus management, keyboard nav, reduced-motion, screen-reader, correct target sizes
4. Telemetry: schema-enforced events, default redaction, opt-in, debug overlay
5. Voice surface (phone/web/desktop): on-device only, no raw audio off-device
6. Agent presence widget via `agent-presentation-package`
7. All quality gates pass (biome, lint, type, coverage, a11y)
8. Docs: README, architecture, accessibility, privacy, voice, deployment
9. `.agents/skills/manifest.yaml` declaring dev-skill dependencies

---

## NEVER

- Bypass `voice-client-package` (raw audio never leaves device)
- Inline hex colors (consume design-system tokens)
- `<all_urls>` permissions in extensions
- Analytics or ad SDKs
- Em dashes in any string
- New agent skills inside a template body

---

## Error Quick-Fix

| Error / Symptom | Fix |
|-----------------|-----|
| Loaded both this skill and `cytognosis-design-system-master` in one response | Split: template task in one response, design tokens in the next |
| Raw audio leaving device | Audit `voice-client-package` usage; never bypass it |
| Extension requesting `<all_urls>` | Narrow to required origins only |
| Profile choice unclear | Follow decision tree: patient-facing → Clinical; logged-in product → Research; public/press → Foundation; devs → Lab |

---

## See Also

- [Full documentation](cytognosis-template-master.md) — comprehensive reference + explanation
- [cytognosis-design-system-master](../cytognosis-design-system-master/cytognosis-design-system-master.md) — visual tokens and voice rules (load in separate response)
- [cytognosis-dev](../cytognosis-dev/cytognosis-dev.md) — cytocast/cytoskeleton/nox details
- [cytognosis-orchestrator](../cytognosis-orchestrator/cytognosis-orchestrator.md) — routing between skills

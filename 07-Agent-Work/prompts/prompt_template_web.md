# Claude Design Prompt: Create the `app-web` Template

> Paste this prompt into Claude Design when you want it to produce the **initial scaffold** of the Cytognosis logged-in web template (`cytoskeleton/templates/app-web/`). This template is the basis for Cytognosis dashboards, the asset hub, and the Cytoverse workbench. It is NOT the public website (use `prompt_template_website.md` for that).
> Cytognosis context: full spec in `cytognosis-branding/references/web.md`.

> **Revised from**: `Documents/Cytognosis/Infra and design/03_claude_design_prompts/prompt_template_web.md`
> **Changes**: replaced `cytognosis-template-master` with `cytognosis-branding`, added profile switcher component requirement (data-profile attribute toggling), added density control component, added motion preference toggle, removed em dashes.

---

## Brief

Produce the initial scaffold for the Cytognosis logged-in web template. The template is the base for product surfaces that run in a browser **after sign-in**: patient longitudinal dashboards, clinician review surfaces, researcher analysis tools, asset-hub web client. It is also the substrate that the desktop template (`app-desktop`) wraps via Tauri v2; anything built here is reused there.

Distinguish from the **public website** (`app-website`): that template is content-first, server-rendered (Astro), SEO-critical. This template is dashboard-first, client-rich, auth-gated. They share the Design System and the brand voice but not the runtime.

## 1. Stack (mandatory choices)

- **Framework**: React 19, function components only.
- **Bundler**: Vite, latest stable.
- **Language**: TypeScript 5.x strict (`strict`, `exactOptionalPropertyTypes`, `noUncheckedIndexedAccess`).
- **Styling**: Tailwind CSS configured from Design System tokens preset.
- **Component library**: shadcn/ui base, vendored to `src/components/ui/`, customized to Cytognosis tokens.
- **Routing**: React Router v7 (pick this for the first revision; TanStack Router as an alternative if specifically requested).
- **Data fetching**: TanStack Query for server state; Zustand for UI state (minimal).
- **Forms**: React Hook Form + Zod.
- **Charts**: Recharts (consumes Design System tokens).
- **Auth UI**: from `auth-shell-package`; the auth provider is downstream-configurable.

## 2. Mandatory artifacts in the scaffold

### 2.1 Routing scaffold (code-split, typed, brand-aligned loading skeletons)

```
/                            welcome / sign-in
/home                        post-sign-in landing
/settings                    account, privacy, consent
/settings/privacy
/settings/consent
/settings/display            density, motion, font, profile preferences (NEW)
/crisis                      in-app crisis-safety surface (deep-linkable)
/voice                       voice surface (Web Speech + WASM-VAD)
```

Wrap each route with `React.lazy` + `<Suspense fallback={<BrandSkeleton />} />`.

### 2.2 Profile switcher component (NEW)

The app-web template requires a profile switcher that toggles the `data-profile` attribute on `<main>`:

- Available profiles: Foundation, Clinical, Research, Lab, Companion, Crisis.
- Default profile per route: Foundation for welcome, Research for logged-in, Crisis for `/crisis`.
- Admin/power users can override the profile for testing and preference.
- The switcher lives in Settings > Display and as a compact selector in the app shell header (admin only).
- Implementation: `useProfile()` hook that reads/writes `data-profile` on the root element and persists the choice in `localStorage`.
- CSS overlay tokens from `profiles.css` activate based on the `data-profile` attribute.

### 2.3 Density control component (NEW)

A density toggle that adjusts spacing, font size, and information density:

| Mode | Line height | Paragraph gap | Font size | Max width | Use case |
|---|---|---|---|---|---|
| Compact | 1.3 | 0.5em | 14px | 90ch | Power users, Lab/Research |
| Comfortable | 1.5 | 1em | 16px | 75ch | Default for Research |
| Spacious | 1.7 | 1.5em | 18px | 65ch | Companion/Clinical, ND users |

- Lives in Settings > Display and as a compact control in the app shell.
- Applies via CSS custom properties on the root element.
- Persists in `localStorage`.
- Companion profile defaults to Spacious; Research defaults to Comfortable; Lab defaults to Compact.

### 2.4 Motion preference toggle (NEW)

A motion preference control that governs animation behavior:

| Setting | Behavior |
|---|---|
| System default | Follows `prefers-reduced-motion` media query |
| Full motion | All animations enabled regardless of system preference |
| Reduced motion | Minimal transitions only (opacity, color); no position or scale animations |
| No motion | Zero animations; instant state changes |

- Lives in Settings > Display.
- Applies via a `data-motion` attribute on the root element.
- CSS uses `[data-motion="none"] *` selectors to override all `transition` and `animation` properties.
- Companion profile defaults to "Reduced motion"; Crisis profile forces "No motion".
- Persists in `localStorage`.

### 2.5 Voice surface (browser-native, privacy-preserving)

- Web Speech API + WASM-VAD fallback.
- The browser does NOT run an edge LLM; the supervisor lives on the desktop tier or on a local cytoplasma peer.
- Features extracted in-browser where possible; relayed via fabric as schema-enforced events.
- Raw audio never leaves the device.
- The voice affordance uses the Design System's calm-pulse listening visual.
- Graceful degradation: report which tier the agent is talking to.

### 2.6 Theme switcher

Light / dark / auto. Tokens support both modes. The switcher lives in Settings; default is `auto` (follow system).

### 2.7 Sign-in flow

Via `auth-shell-package`. Welcome screen to provider redirect or in-page form, then token (HTTP-only cookie default), then refresh transparent, then signed-out routing surfaces welcome.

### 2.8 PWA manifest

Minimal PWA: icon set re-exported from Design System; service worker for offline shell; install prompt. **Mobile-install primarily** (desktop users get the dedicated `app-desktop` template, so do not aggressively offer install on desktop).

### 2.9 Print stylesheet

Small print stylesheet: no nav, single-column, design-system typography. Cytognosis users print reports.

### 2.10 Agent presence widget placement

Persistent location: top-right of the app shell. `Cmd/Ctrl + /` expands into a voice/chat side panel.

### 2.11 Seven shared packages wired

Every starter screen demonstrates at least one of the seven shared packages from `cytoskeleton/templates/shared/`:

- `design-system-package` (Tailwind preset + token bindings)
- `api-client-package` (typed endpoint calls; mock layer for fixtures mode)
- `fabric-client-package` (useAgent, useEvent, useCrdtDocument, useCrisisRail hooks)
- `voice-client-package` (VAD, barge-in, feature events)
- `auth-shell-package` (login flow + HTTP-only cookies)
- `telemetry-package` (schema-enforced events + redaction defaults)
- `agent-presentation-package` (avatar, state indicators, turn-taking visuals)

## 3. File layout

```
app-web/
├── package.json
├── tsconfig.json
├── vite.config.ts
├── tailwind.config.ts          extends design-system preset
├── biome.json
├── index.html
├── public/
│   ├── manifest.webmanifest
│   ├── icons/                  re-exported from design-system
│   └── service-worker.js       generated by Vite plugin
├── src/
│   ├── main.tsx                React 19 root
│   ├── App.tsx
│   ├── theme/
│   │   ├── tokens.css          consumed Tailwind layer
│   │   └── theme-provider.tsx
│   ├── routing/
│   │   └── routes.tsx
│   ├── shared/                 consumes the seven shared packages
│   ├── screens/                seven starter screens (see §2.1; plus empty + error)
│   ├── components/
│   │   ├── ui/                 shadcn-derived, Cytognosis-tokenized
│   │   ├── ProfileSwitcher.tsx (NEW: data-profile toggling)
│   │   ├── DensityControl.tsx  (NEW: compact/comfortable/spacious)
│   │   ├── MotionToggle.tsx    (NEW: motion preference control)
│   │   └── (template-local components)
│   ├── hooks/                  custom hooks (useXxx naming)
│   │   ├── useProfile.ts      (NEW: profile state management)
│   │   ├── useDensity.ts      (NEW: density preference management)
│   │   ├── useMotion.ts       (NEW: motion preference management)
│   │   └── ...
│   ├── services/
│   │   ├── voice-service.ts
│   │   └── paralinguistic-service.ts
│   ├── state/                  Zustand stores (minimal)
│   ├── lib/                    small utilities; named by purpose, not "utils"
│   ├── queries/
│   │   └── keys.ts             TanStack Query key factory
│   └── microcopy.json
├── tests/
│   ├── unit/
│   ├── integration/
│   └── accessibility/          axe-core on every screen
├── e2e/                        Playwright: sign-in → home → voice
├── docs/
│   ├── README.md
│   ├── architecture.md
│   ├── accessibility.md
│   ├── privacy.md
│   ├── voice.md
│   ├── profiles.md             (NEW: documents profile switching, density, motion)
│   └── deployment.md
└── .agents/skills/manifest.yaml  dev-skill dependencies
```

## 4. Brand alignment

- Profile defaults: Foundation for the welcome / signed-out routes; Research for logged-in routes (`data-profile="research"` on `<main>`).
- Consume Design System tokens via Tailwind preset; never inline `#hex` colors.
- Logo wordmark in the app shell header; logo mark in the favicon.
- Voice rules in every visible string; microcopy in `microcopy.json`.
- Profile switcher, density control, and motion toggle use Design System tokens for their own UI.

## 5. Quality gates

- Initial JS bundle (welcome screen): < 200 KB gzip.
- Home screen JS bundle: < 350 KB gzip.
- Lighthouse Performance, Accessibility, Best Practices, SEO: 95+ on every screen.
- TTI: < 2 s on mid-tier laptop + 4G simulation.
- FCP: < 1 s on the same.
- Test coverage: 80% line minimum; `components/ui/` 90%.
- Playwright e2e covers sign-in, home, voice, profile-switch, density-toggle in < 30 s test runtime.

## 6. Hard rules

- Function components with explicit prop types via `interface` or `type`.
- Named exports for components and hooks (no default exports except `App.tsx`).
- Hooks named `useXxx` and live in `hooks/`.
- Avoid `useEffect` for derived state; prefer `useMemo`.
- Suspense at route boundaries, not in leaf components.
- No `any`. Use `unknown` and narrow.
- TanStack Query keys typed via the `keys.ts` factory.
- Profile switcher, density control, and motion toggle are accessible (keyboard navigable, screen-reader announced).

## 7. What to NOT produce

- No CSS-in-JS (no styled-components, no Emotion). Tailwind + tokens.
- No global state library beyond Zustand. Most state is server-state via TanStack Query.
- No `<style>` tags. Tailwind utilities + tokens.
- No analytics or ad SDKs.
- No shadcn import from a CDN. Vendor to `components/ui/`.
- No coupling to a specific auth provider in `screens/welcome/`. Use `auth-shell-package`.
- No marketing content. Marketing lives in `app-website`.
- No SEO meta tags as a primary concern (this template is auth-gated; SEO does not apply to logged-in routes).

## 8. Definition of done

1. `npm install && npm run dev` brings up the Vite dev server.
2. Sign-in screen renders. Authentication flow round-trips against a mock auth provider.
3. Home screen renders the agent presence widget and a sample data card.
4. Voice surface establishes a session with a local cytoplasma peer (mock OK for first revision).
5. Lighthouse 95+ on the home screen.
6. PWA installable from Chrome / Edge / Safari / Firefox.
7. Theme switcher works in all three modes.
8. Profile switcher toggles `data-profile` attribute and CSS overlays apply correctly.
9. Density control switches between compact, comfortable, and spacious modes.
10. Motion toggle controls animation behavior across all four settings.
11. Playwright e2e suite passes.
12. `docs/README.md` walks a new developer from clone to running the starter screens in under 10 minutes.
13. No em dashes anywhere.

## 9. Deliverables to ship back

1. The complete `app-web/` tree.
2. A mock-data layer in `src/shared/mocks/` so the template is runnable without a backend.
3. The first PR-ready commit message in Conventional Commits format.

## 10. Open questions to surface back to Cytognosis

1. Router: React Router v7 (scaffold default) vs TanStack Router. Confirm.
2. Public-marketing variant: out of scope for this template (lives in `app-website`). Confirm.
3. PWA scope: mobile-install only (recommendation) or also desktop install?
4. Default chart library: Recharts (scaffold default) vs ECharts vs Visx.
5. Web Speech vs custom WASM VAD: which is the primary voice path? Recommendation: Web Speech with WASM VAD fallback.
6. Auth provider default: Clerk vs Supabase vs self-hosted Keycloak/Authentik. Recommendation: self-hosted.
7. Should the profile switcher be visible to all users or admin-only? Recommendation: admin-only in production; all users in development.
8. Should density and motion preferences sync across devices via fabric, or stay local per browser? Recommendation: sync via fabric for logged-in users.

# Claude Design Brief: Web Template (Delta)

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: engineers
> **Tags**: `engineering`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)

> Read `templates_general_brief.md` first. This file only carries what is unique to the web template.
> Output destination: `cytoskeleton/templates/app-web/`.

## 1. What this template is for

The web template is the base for Cytognosis products that run primarily in a browser at a URL the user visits. Planned products derived from this template:

- Patient-facing longitudinal dashboards (after sign-in).
- Clinician-facing review surfaces.
- Researcher-facing analysis tools.
- The asset / knowledge-hub web client.
- The Cytognosis.org logged-in area (eventually).

The web template is also the substrate that the desktop template wraps via Tauri v2. Anything you build for web is reused on desktop with native bridges added.

## 2. Framework and platform

- **Framework**: React 19 (latest stable) using function components and hooks. No class components.
- **Bundler**: Vite (latest stable).
- **Language**: TypeScript 5.x, strict mode (`strict: true`, `exactOptionalPropertyTypes: true`, `noUncheckedIndexedAccess: true`).
- **Styling**: Tailwind CSS configured from the design-system tokens (the design-system-package emits a Tailwind preset).
- **Component library**: shadcn/ui as the base, customized to consume Cytognosis tokens. Components live in `src/components/ui/` and are owned by this template (per shadcn convention).
- **Routing**: React Router v7 (or TanStack Router; pick one in the first revision and document the choice).
- **Data fetching**: TanStack Query for server state; React state or Zustand for UI state.
- **Forms**: React Hook Form + Zod.
- **Charts**: Recharts (consumes design-system tokens for axes, gridlines, palette).
- **Auth UI**: from `auth-shell-package` (the auth provider itself is downstream-configurable).

## 3. Mandatory artifacts (web-specific)

In addition to the cross-template mandatory artifacts.

### 3.1 Routing scaffold

**Mandatory.** A clear, typed routing setup with code-split routes:

- `/` (welcome / sign-in)
- `/home` (post-sign-in)
- `/settings`
- `/settings/privacy`
- `/settings/consent`
- `/crisis` (safety surface, reachable via deep-link and from the persistent crisis affordance)
- `/voice` (the voice surface; Web-Speech-backed)

Each route is code-split via `React.lazy` and wrapped in a `<Suspense>` with a brand-aligned loading skeleton.

### 3.2 Voice surface (browser-native)

**Mandatory.** A working voice interaction using the Web Speech API plus the fabric:

- VAD via the Web Speech API or a small WASM-based VAD.
- The browser does not run an edge LLM; the supervisor lives on the laptop tier (the desktop template hosts it as a Tauri sidecar) or the user runs the voice session in the desktop app for full local capability. The web template gracefully reports the tier it is talking to.
- Same privacy rule: no raw audio leaves the device. Features extracted in-browser (where possible) or relayed to a local cytoplasma peer via the fabric.
- The voice affordance uses the same Design System pattern as the phone template (the calm pulse, the speaking waveform).

### 3.3 Server-rendered fallback (optional but recommended)

If a public-marketing variant of the web template is in scope (e.g., the Cytognosis.org logged-out area), use Next.js instead of Vite for that variant; the logged-in area can remain Vite-driven. Decide per downstream product. The template ships Vite by default.

### 3.4 Theme switcher

**Mandatory.** Light / dark / auto. Tokens already support both modes; the template exposes the control in settings. The default is `auto` (system).

### 3.5 Sign-in flow

**Mandatory.** Uses `auth-shell-package`. The flow:

- Welcome screen with a single primary action.
- Auth provider redirect or in-page form (depends on configured provider).
- Token in HTTP-only cookie (default) or in-memory (per provider).
- Refresh transparent to the user.
- Signed-out routing surfaces the welcome.

### 3.6 PWA manifest

**Mandatory.** The template ships a minimal PWA manifest (icon set re-exported from design-system iconography; service worker for offline shell; install prompt). The web template can be installed as a desktop or mobile PWA.

### 3.7 Print stylesheet

**Mandatory.** A small print stylesheet so any data-rendering screen prints legibly (no nav, single-column, design-system typography). Cytognosis users may need to print reports.

### 3.8 Embeddings of the agent presence widget

**Mandatory.** The agent-presence widget from `agent-presentation-package` sits in a persistent location (top-right of the app shell by default). It is reachable via `Cmd/Ctrl + /` to expand into a voice / chat side panel.

## 4. Optional artifacts (web-specific)

- **Storybook** (recommended) for the shared `Components/ui/` directory.
- **MSW** (Mock Service Worker) integration for fixtures mode.
- **Vitest UI** for an interactive test runner during development.
- **Bundle visualizer** (rollup-plugin-visualizer) running in CI to track bundle composition.

## 5. Folder layout (web-specific)

```
app-web/
├── package.json
├── tsconfig.json
├── vite.config.ts
├── tailwind.config.ts                 (extends design-system preset)
├── biome.json
├── index.html
├── public/
│   ├── manifest.webmanifest
│   ├── icons/                         (re-exported from design-system)
│   └── service-worker.js              (generated)
├── src/
│   ├── main.tsx                       (React 19 root)
│   ├── App.tsx
│   ├── theme/
│   │   ├── tokens.css                 (consumed Tailwind layer)
│   │   └── theme-provider.tsx
│   ├── routing/
│   │   └── routes.tsx
│   ├── shared/                        (consumes the seven shared packages)
│   ├── screens/
│   │   ├── welcome/
│   │   ├── home/
│   │   ├── settings/
│   │   ├── consent-prompt/
│   │   ├── crisis-safety/
│   │   ├── voice/
│   │   ├── empty-state/
│   │   └── error-state/
│   ├── components/
│   │   ├── ui/                        (shadcn-derived, Cytognosis-tokenized)
│   │   └── (template-local components)
│   ├── hooks/
│   ├── services/
│   │   ├── voice-service.ts
│   │   └── paralinguistic-service.ts
│   ├── state/                         (Zustand stores; minimal)
│   ├── lib/                           (small utilities; named by purpose, not "utils")
│   └── microcopy.json
├── tests/
│   ├── unit/
│   ├── integration/
│   └── accessibility/
├── e2e/                               (Playwright)
└── docs/
```

## 6. Code style (web-specific)

- Function components with explicit prop types via `interface` or `type` aliases.
- Named exports for components and hooks (no default exports except the root `App.tsx`).
- Hooks named `useXxx` and live in `hooks/`.
- Avoid `useEffect` for derived state; prefer `useMemo` or computed values.
- Avoid suspense boundaries inside leaf components; suspense lives at route boundaries and at deliberate streaming boundaries.
- No `any`. Use `unknown` and narrow.
- TanStack Query keys are typed via a small key-factory module (`src/queries/keys.ts`).

## 7. Quality gates (web-specific)

- **Initial JS bundle**: under 200 KB gzip for the welcome screen; under 350 KB gzip for the home screen.
- **Lighthouse score**: 95+ on Performance, Accessibility, Best Practices, SEO. Run in CI on a representative home screen.
- **Time to Interactive**: under 2 s on a mid-tier laptop on 4G simulation.
- **First Contentful Paint**: under 1 s on the same.
- **Coverage**: 80% line coverage; the `Components/ui/` directory at 90%.

## 8. Definition of done (web-specific)

In addition to the cross-template definition of done:

1. Lighthouse 95+ on the home screen.
2. PWA installable from Chrome / Edge / Safari / Firefox.
3. Theme switcher works in all three modes; tokens render correctly in both light and dark.
4. The voice surface establishes a session with a local cytoplasma peer in the integration test.
5. Playwright e2e suite covers sign-in to home to voice in under 30 seconds of test run time.

## 9. What to NOT produce (web-specific)

- Do not use any CSS-in-JS library (styled-components, Emotion). Tailwind + tokens are the styling layer.
- Do not introduce a global state library beyond Zustand. Most state is server-state via TanStack Query.
- Do not write framework-specific CSS in `<style>` tags. Tailwind utility classes + the tokens-driven preset.
- Do not include analytics or ad SDKs.
- Do not import shadcn components from a CDN; the shadcn convention is to vendor them into `Components/ui/` so they can be customized.
- Do not couple to a specific auth provider in `screens/welcome/`. The provider is plug-in via `auth-shell-package`.

## 10. Open questions for the Cytognosis team

1. Router choice: React Router v7 vs TanStack Router. Decide in the first revision.
2. Public-marketing variant: ship the Vite template only, or also ship a Next.js variant for the logged-out marketing area? Recommendation: ship Vite-only first; add Next.js later if Cytognosis.org consolidates.
3. PWA scope: install for mobile only (where it matters), or for desktop too (where it duplicates the Tauri desktop app)? Recommendation: mobile-install only; desktop users get the desktop template.
4. Default chart library: Recharts is in the brief; ECharts or Visx as alternatives if more complex visualizations are needed. Decide per downstream product.
5. Web Speech vs a custom WASM VAD: Web Speech is patchy; the WASM VAD is heavier. Decide before the first voice integration.

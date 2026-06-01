# Claude Design Prompt: Create the `app-extension` Template

> Paste this prompt into Claude Design when you want it to produce the **initial scaffold** of the Cytognosis browser-extension template (`cytoskeleton/templates/app-extension/`). The template is the basis for the patient companion extension and the internal knowledge-hub clipping tool.
> Cytognosis context: full spec in `cytognosis-branding/references/extension.md`.

> **Revised from**: `Documents/Cytognosis/Infra and design/03_claude_design_prompts/prompt_template_extension.md`
> **Changes**: replaced `cytognosis-template-master` with `cytognosis-branding`, added Companion profile as default for patient mode, added Crisis overlay for health alerts in content scripts, removed em dashes.

---

## Brief

Produce the initial scaffold for the Cytognosis browser extension template. Browser extensions for Chrome and Edge first (Firefox MV3 later). The headline UI surface is the side panel; secondary surfaces are an action popup, content scripts, and an options page. Two build modes from one codebase:

- **Patient mode**: lightweight companion for patients to browse approved content (educational materials, prescribed reading) with optional voice agent. Uses the **Companion profile** by default for ND-friendly daily use.
- **Internal mode**: power tool for the Cytognosis team (annotation, clip-to-graph, citation capture, asset-hub feeder).

## 1. Stack (mandatory choices)

- **Manifest**: Manifest V3.
- **Primary UI**: side panel (`chrome.sidePanel` API).
- **Secondary UI**: action popup, content scripts, options page.
- **Frontend**: React 19 + Vite (same stack as `app-web`, scaled down for extension constraints).
- **Language**: TypeScript 5.x strict.
- **Browser targets**: Chrome + Edge first; Firefox MV3 later (still maturing).
- **Bundler**: Vite with `@crxjs/vite-plugin` (or equivalent MV3-aware plugin).

## 2. Build modes (mandatory)

Single env var picks mode at build time, stamped into manifest + `mode.ts` constant:

- `MODE=patient`: lightweight, content-scoped to approved domains only, voice off by default, no in-page mutation, conservative defaults. **Companion profile active by default.**
- `MODE=internal`: full toolkit, voice on (with consent), in-page mutations allowed (annotation overlays), broad content-script scope (per-site permissions still apply).

Cytocast asks at scaffold which mode the product is built for.

## 3. Mandatory artifacts in the scaffold

### 3.1 Manifest V3

`manifest.template.json` filled per mode at build:

- Minimum-necessary permissions per mode.
- Side panel registered as the default UI.
- Action popup registered (small; quick toggles).
- Content scripts only on domains configured for the build mode.
- No `<all_urls>` in either mode. Host-permissions list explicit.
- CSP: no remote code, no `eval`, no `unsafe-inline`.

### 3.2 Side panel (headline UI)

Renders:

- Agent presence widget (`agent-presentation-package`).
- Chat / voice conversation surface.
- Contextual panel reflecting current tab's content (when permitted).

Behaviors:

- Persists across tab switches (per-window).
- Voice-enabled in internal mode (via `voice-client-package`); voice off by default in patient mode.
- Consent-gated cloud escalation.
- Survives extension reloads without losing conversation context (CRDT-backed via `fabric-client-package`).
- **Patient mode uses Companion profile**: Lexend font, generous spacing, muted 300-shade pastels, reduce-motion default.

### 3.3 Action popup

Small popup (< 600px tall) accessible from the browser toolbar:

- Primary action ("Capture this page" in internal mode; "Talk to Cytognosis" in patient mode).
- Toggle for the side panel.
- Privacy / pause-listening toggle prominent at the top.
- Status row showing agent connection state.

### 3.4 Content scripts (mode-scoped)

- **Patient mode**: read-only. Detect approved-content URLs, surface an "Ask Cytognosis" affordance, decorate citations.
- **Internal mode**: read-and-write. Annotation overlays, clip-to-graph, citation extraction, in-page agent commentary.

Privacy:

- Never log raw page content. Extract structured features (citations, headings, asset URLs) and emit schema-enforced events.
- Annotation overlays use Cytognosis tokens. No third-party annotation toolkits.

### 3.5 Crisis overlay for health alerts (NEW)

Content scripts in patient mode can trigger a Crisis overlay when health-alert content is detected on approved domains:

- The overlay uses the **Crisis profile**: high contrast, 56px touch targets, no animations, single-action focus.
- Activation: when the content script detects health-alert structured data or when the agent pushes a `CrisisDetected` event.
- The overlay renders as a full-viewport semi-transparent layer with a centered action card.
- The card contains: the alert message, one primary action button, and a "Dismiss" secondary action.
- The overlay does not block the underlying page permanently; the user can dismiss it.
- Crisis overlay uses `crisis-banner` and `consent-prompt` contracts from the Design System.

### 3.6 Background service worker (MV3-aware)

Handles:

- Side panel and popup messaging.
- `fabric-client` connection (NATS over wss; extensions cannot bind LAN sockets).
- Persistent listeners for tab events, scheduled tasks, omnibox commands.
- Telemetry batching with privacy defaults.
- Crisis event routing from fabric to content scripts.

Code uses `addEventListener` patterns; no long-lived globals (MV3 service workers can be killed and restarted).

### 3.7 Options page (mode-aware)

- Per-site permissions review (which domains the extension currently has content-script access to).
- Voice settings (on/off, microphone permission status).
- Consent management (linked to the fabric consent ledger).
- Privacy / data review (what was captured locally; one-tap export and delete).
- **Display preferences** (patient mode): font toggle (Inter/Lexend/Atkinson Hyperlegible), density control, motion preference.

### 3.8 Storage

- `chrome.storage.local`: non-sensitive UI state.
- `chrome.storage.session`: ephemeral tokens (cleared on browser restart).
- Fabric (Iroh CRDT via the service worker): content syncing across devices with explicit consent.
- Never store secrets in `chrome.storage.local`. Sign-in tokens go in the fabric's encrypted secret slot.

### 3.9 Per-site permission UX

When a content script wants a new domain, surface a consent prompt explaining why + what data leaves the page. Patient mode never auto-grants. Internal mode prompts once per domain.

## 4. File layout

```
app-extension/
├── package.json
├── tsconfig.json
├── vite.config.ts
├── manifest.template.json      filled at build per mode
├── public/
│   └── icons/                  re-exported from design-system
├── src/
│   ├── side-panel/
│   │   ├── index.tsx
│   │   ├── App.tsx
│   │   └── (screens, hooks, components)
│   ├── popup/
│   │   ├── index.tsx
│   │   └── App.tsx
│   ├── options/
│   │   └── App.tsx
│   ├── content-scripts/
│   │   ├── patient/
│   │   │   ├── main.ts
│   │   │   └── crisis-overlay.ts   (NEW: Crisis profile overlay for health alerts)
│   │   └── internal/
│   ├── background/
│   │   ├── service-worker.ts
│   │   ├── messaging.ts
│   │   ├── fabric.ts           NATS-over-wss client
│   │   ├── crisis-router.ts    (NEW: routes CrisisDetected events to content scripts)
│   │   └── tasks/              scheduled-task handlers
│   ├── shared/                 consumes the seven shared packages
│   ├── mode.ts                 build-mode constant
│   ├── theme/                  consumes design-system tokens; profile-aware
│   └── microcopy.json
├── tests/
│   ├── unit/
│   └── e2e/                    Playwright + extension test harness
└── docs/
    ├── README.md
    ├── architecture.md
    ├── modes.md                patient vs internal modes documented
    ├── privacy.md
    ├── crisis-overlay.md       (NEW: documents Crisis overlay behavior)
    └── accessibility.md
```

## 5. Brand alignment

- Profile default: **Companion** for patient mode; Lab or Research for internal mode (`data-profile` attribute set per build mode).
- Consume Design System tokens; never inline `#hex` colors.
- Logo mark as the extension icon at multiple resolutions.
- Voice rules apply to all visible strings.
- Patient mode uses Companion profile typography (Lexend body), spacing (1.7 line-height), and motion defaults (reduced).
- Crisis overlay uses Crisis profile tokens when active.

## 6. Quality gates

- Unzipped extension size (per browser): < 5 MB.
- Side panel cold start: < 500 ms on a 2020-class laptop.
- Service worker startup: < 200 ms.
- Lighthouse Accessibility on the options page: 95+.
- Manifest validation: Chrome Web Store dev console reports no errors.
- CSP: no `unsafe-inline`, no `unsafe-eval`.
- Coverage: 80% line minimum.
- Crisis overlay render: < 500 ms from event to visible overlay.

## 7. Hard rules

- Service worker code uses `addEventListener` patterns; no long-lived globals.
- Async messages between contexts (popup, side panel, content script, service worker) use a typed message router with versioned schemas.
- `chrome.*` types from `@types/chrome`. No `any`.
- Content scripts bundled as IIFEs (MV3 limitation).
- Side panel and popup are separate bundles to keep cold start small.
- Crisis overlay CSS is self-contained; no leakage into the host page's styles.

## 8. What to NOT produce

- No Manifest V2. V3 only.
- No `<all_urls>` host permissions in either mode.
- No remote-code-execution mechanisms (no `eval`, no remote `<script>`, no remote-loaded WASM that has not passed CSP).
- No analytics or ad SDKs.
- No page mutation in patient mode beyond the "Ask Cytognosis" affordance and the Crisis overlay.
- No secrets in `chrome.storage.local`.
- No blocking of the user's page interaction while content scripts process.

## 9. Definition of done

1. The extension loads in Chrome and Edge in both modes (patient and internal).
2. The side panel renders the agent presence widget and a working voice (internal mode) or chat (patient mode) exchange against a local cytoplasma peer.
3. The popup, options page, and at least one content script demonstrate the mode-appropriate behavior.
4. The per-site permission UX surfaces the consent prompt on a new domain.
5. The CSP and host-permissions list pass the Chrome Web Store linter.
6. Accessibility scanner reports zero critical or serious issues on the options page.
7. Patient mode uses Companion profile (Lexend font, generous spacing, muted palette).
8. Crisis overlay renders correctly on approved domains when a health alert triggers.
9. `docs/README.md` walks a new developer from clone to loading the extension unpacked in Chrome in under 10 minutes.
10. No em dashes anywhere.

## 10. Deliverables to ship back

1. The complete `app-extension/` tree.
2. Two zipped extension bundles (`patient.zip`, `internal.zip`) demonstrating both build modes.
3. A `docs/modes.md` documenting the per-mode differences for non-developer reviewers.
4. The first PR-ready commit message in Conventional Commits format.

## 11. Open questions to surface back to Cytognosis

1. Approved-content domain list (patient mode): who curates, where does it live? Recommendation: `branding/policy/approved-domains.yaml`, synced into the manifest at build.
2. Firefox MV3 support: in or out for first revision? Recommendation: out; revisit when Firefox MV3 stabilizes.
3. Side panel default-open behavior: action-click only (recommendation) or auto-open on approved domain (patient mode)?
4. Devtools panel for fabric debugging: in or out? Recommendation: in (it has helped debug).
5. Omnibox keyword: `cy` (short) or `cytognosis` (long)? Recommendation: reserve `cytognosis` as the safe long form; `cy` if it does not conflict with anything else the user has installed.
6. Annotation rendering: text-overlay only (default) or also visual highlights with marker shapes?
7. Should the Crisis overlay be dismissable by the user, or should it persist until the user takes the primary action? Recommendation: always dismissable, but log the dismissal for safety review.

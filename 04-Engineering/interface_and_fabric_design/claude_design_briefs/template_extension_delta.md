# Claude Design Brief: Browser Extension Template (Delta)

> Read `templates_general_brief.md` first. This file only carries what is unique to the extension template.
> Output destination: `cytoskeleton/templates/app-extension/`.

## 1. What this template is for

The browser extension template is the base for Cytognosis products that live as a browser companion: a side panel for in-browser interaction with the Cytognosis agent, content scripts for in-page actions (annotation, asset capture, citation grabbing), and an action popup for quick controls.

Planned products derived from this template, distinguished by build mode:

- **Patient mode**: a lightweight companion for patients to browse approved content (educational materials, prescribed reading) and interact with the agent inline.
- **Internal mode**: a power tool for the Cytognosis team to annotate, clip-to-graph, capture citations, and feed the asset hub.

Both modes ship from the same template; the build flag picks the bundle.

## 2. Framework and platform

- **Manifest**: Manifest V3.
- **Primary UI surface**: side panel (`chrome.sidePanel` API).
- **Secondary UI surfaces**: action popup, content scripts, options page.
- **Frontend**: React 19 + Vite (same stack as the web template, scaled down for extension constraints). TypeScript strict.
- **Browser targets**: Chrome and Edge first; Firefox as a build target later (MV3 in Firefox is still maturing).
- **Bundler**: Vite with `@crxjs/vite-plugin` (or equivalent MV3-aware plugin).
- **Packaging**: zipped extension per browser, signed where applicable.

## 3. Build modes

**Mandatory.** The template supports two build modes via a single environment variable:

- `MODE=patient`: lightweight, content-scoped to approved domains, voice off by default, no in-page mutation, conservative defaults.
- `MODE=internal`: full toolkit, voice on by default (with consent), in-page mutations allowed (annotation overlays), broad content-script scope (still respecting per-site permissions).

Build mode is set at the cytocast scaffold step and stamped into the manifest plus a `mode.ts` constant.

## 4. Mandatory artifacts (extension-specific)

In addition to the cross-template mandatory artifacts.

### 4.1 Manifest V3

**Mandatory.** A working `manifest.json` that:

- Declares minimum-necessary permissions (per mode).
- Registers the side panel as the default UI.
- Registers the action popup (small; for quick toggles).
- Registers content scripts only on the domains configured for the build (per mode).
- Declares the host-permissions list explicitly; no `<all_urls>` in either mode.
- Lists CSP rules that match Cytognosis posture (no remote code; no `eval`).

### 4.2 Side panel

**Mandatory.** The headline UI surface. Renders the agent presence widget, a chat/voice conversation surface, and a contextual panel that reflects the current tab's content (when permitted).

Required behaviors:

- Persists across tab switches (sidepanel is per-window).
- Voice-enabled in internal mode (uses `voice-client-package`); voice off by default in patient mode (opt-in).
- Consent-gated escalation to a cloud peer (same rules as the other templates).
- Survives extension reloads without losing conversation context (CRDT-backed).

### 4.3 Action popup

**Mandatory.** A small popup (under 600px height) accessible from the toolbar. Provides:

- A primary action ("Capture this page" in internal mode; "Talk to Cytognosis" in patient mode).
- A toggle for the side panel.
- A privacy / pause-listening toggle prominent at the top.
- A status row showing the agent connection state.

### 4.4 Content scripts

**Mandatory.** Content scripts are scoped by mode:

- **Patient mode** content scripts: read-only. Detect approved-content URLs, surface a "Ask Cytognosis" affordance, decorate citations.
- **Internal mode** content scripts: read-and-write. Annotation overlays, clip-to-graph captures, citation extraction, in-page agent commentary.

Required behaviors:

- Content scripts never log raw page content; they extract structured features (citations, headings, asset URLs) and emit schema-enforced events.
- Annotation overlays use Cytognosis tokens (color, typography, motion); they do not import third-party annotation toolkits.

### 4.5 Background service worker

**Mandatory.** A long-lived service worker handles:

- Side panel and popup messaging.
- The fabric-client connection (NATS over wss, since extensions cannot bind LAN sockets).
- Persistent listeners for tab events, scheduled tasks, omnibox commands.
- Telemetry batching (with privacy defaults).

### 4.6 Options page

**Mandatory.** A small options page that exposes:

- Mode-aware settings.
- Per-site permissions review (which domains the extension currently has content-script access to).
- Voice settings (on/off, microphone permission status).
- Consent management (linked to the fabric consent ledger).
- Privacy / data review (what the extension has captured locally; one-tap export and delete).

### 4.7 Storage

**Mandatory.** Use:

- `chrome.storage.local` for non-sensitive UI state.
- `chrome.storage.session` for ephemeral tokens (cleared on browser restart).
- The fabric (Iroh CRDT via the service worker) for content that should sync across the user's devices, with explicit consent.

Never store secrets in `chrome.storage.local`. Sign-in tokens go in the fabric's encrypted secret slot.

### 4.8 Per-site permission UX

**Mandatory.** When a content script wants to operate on a new domain, the extension surfaces a consent prompt explaining why and what data leaves the page. The patient mode never auto-grants; the internal mode prompts once per domain.

## 5. Optional artifacts (extension-specific)

- **Omnibox integration** (`chrome.omnibox`): type `cy ` in the address bar to start a Cytognosis voice command. Recommended for internal mode.
- **Context menu** entries (`chrome.contextMenus`): right-click selection to "Send to Cytognosis hub" (internal mode). Recommended.
- **Devtools panel**: a small Cytognosis devtools panel for inspecting fabric traffic during development. Optional but useful.
- **Cross-browser variant**: Firefox MV3 build. Add when Firefox MV3 stabilizes; defer for first revision.

## 6. Folder layout (extension-specific)

```
app-extension/
├── package.json
├── tsconfig.json
├── vite.config.ts
├── manifest.template.json             (filled at build time per mode)
├── public/
│   └── icons/                         (re-exported from design-system)
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
│   │   ├── patient/                   (patient-mode scripts)
│   │   └── internal/                  (internal-mode scripts)
│   ├── background/
│   │   ├── service-worker.ts
│   │   ├── messaging.ts
│   │   ├── fabric.ts                  (NATS-over-wss client)
│   │   └── tasks/                     (scheduled-task handlers)
│   ├── shared/                        (consumes the seven shared packages)
│   ├── mode.ts                        (build-mode constant)
│   ├── theme/                         (consumes design-system tokens)
│   └── microcopy.json
├── tests/
│   ├── unit/
│   └── e2e/                           (Playwright + extension test harness)
└── docs/
```

## 7. Code style (extension-specific)

- Service worker code uses `addEventListener` patterns; do not assume long-lived globals (MV3 service workers can be killed and restarted).
- All async messages between contexts (popup, side panel, content script, service worker) use a typed message router with versioned schemas.
- Use `chrome.*` namespace types from `@types/chrome`; no `any`.
- Content scripts are bundled as IIFEs; never as ESM (MV3 limitation).
- Side panel and popup React entries are separate bundles to keep cold-start small.

## 8. Quality gates (extension-specific)

- **Unzipped extension size**: under 5 MB per browser bundle.
- **Side panel cold start**: under 500 ms to first frame on a 2020-class laptop.
- **Service worker startup**: under 200 ms.
- **Lighthouse Accessibility on options page**: 95+.
- **Manifest validation**: Chrome's `chrome.runtime.validateManifest` passes; submit to Chrome Web Store dev console without errors.
- **CSP**: no `unsafe-inline`, no `unsafe-eval`.

## 9. Definition of done (extension-specific)

In addition to the cross-template definition of done:

1. The extension loads in Chrome and Edge in both modes.
2. The side panel renders the agent presence widget and a working voice (or chat in patient mode) exchange against a local cytoplasma peer.
3. The popup, options page, and at least one content script demonstrate the mode-appropriate behavior.
4. The per-site permission UX surfaces the consent prompt on a new domain.
5. The CSP and host-permissions list pass the Chrome Web Store linter.

## 10. What to NOT produce (extension-specific)

- Do not use Manifest V2; V3 only.
- Do not request `<all_urls>` host permissions in either mode.
- Do not include any remote-code-execution mechanisms (no `eval`, no remote script tags, no remote-loaded WASM that hasn't passed CSP).
- Do not bundle analytics or ad SDKs.
- Do not mutate pages in patient mode beyond surfacing the "Ask Cytognosis" affordance.
- Do not store secrets in `chrome.storage.local`.
- Do not block the user from interacting with the page while a content script processes it.

## 11. Open questions for the Cytognosis team

1. The approved-content domain list for patient mode: who curates it, where does it live? Recommendation: list in `branding/policy/approved-domains.yaml`, synced into the manifest at build time.
2. Firefox MV3 support: in or out for first revision? Recommendation: out; revisit when Firefox MV3 stabilizes.
3. Side panel default-open behavior: open on action click only, or open on first navigation to an approved domain (patient mode)? Recommendation: open on action click only; auto-opening feels intrusive.
4. Devtools panel: in or out? Recommendation: in (it has helped debug fabric traffic).
5. Omnibox keyword: `cy` is short but may conflict. Reserve `cytognosis` as the safe long form and `cy` as the short form.

# Claude Design Brief: Cytognosis Interface Templates (General)

> Read this brief end-to-end before producing or revising ANY of the four Cytognosis interface templates (phone, web, desktop, browser extension). Then read the matching delta (`template_<name>_delta.md`).
> The four templates live in `cytoskeleton/templates/app-<name>/`. Each is consumed via `copier copy cytoskeleton/templates/<name> <downstream-app>`.

## 1. Context

The four templates are the starting point for every Cytognosis user-facing application. Cytognosis ships products that range from a phone-based interviewer agent for patients, to a clinician-facing dashboard, to an internal asset-curation tool, to a browser extension for in-page capture. The templates ensure that any new product starts brand-aligned, accessible, and observably privacy-preserving, with the shared packages already wired so the team is not reinventing common surfaces.

Read `design_system_brief.md` first. The Design System is upstream: everything visual in the templates references the Design System's tokens, components, and microcopy patterns. Templates do not introduce new tokens or new components; they implement the contracts the Design System defines.

## 2. Mandatory artifacts (shared across all four templates)

Each template MUST include every artifact in this section. The matching delta then adds template-specific mandatory artifacts.

### 2.1 The seven shared packages

**Mandatory.** Each template depends on the same seven shared packages, sourced from `cytoskeleton/templates/shared/`. Their contracts (props, surface, behavior) are identical across templates; their implementations are framework-specific.

```
shared/
├── design-system-package/    consumes branding tokens; exports framework-native primitives
├── api-client-package/       generated from cytos.schema OpenAPI; typed endpoint calls + streaming
├── fabric-client-package/    wraps cytoagent's client SDK; exposes useAgent / useEvent / useCrdtDocument / useCrisisRail hooks
├── voice-client-package/     VAD + barge-in + push-to-talk; emits schema-enforced feature events; never sends raw audio
├── auth-shell-package/       login flow + token storage abstraction + signed-out routing
├── telemetry-package/        schema-enforced event telemetry; redaction defaults; opt-in
└── agent-presentation-package/  shared visual language for representing agents (avatars, state indicators, turn-taking visuals)
```

Each template imports these by name. The template's job is to make them work, not to re-implement them.

### 2.2 Starter screens

**Mandatory.** Every template ships a small set of starter screens so downstream products do not begin from a blank slate. The screens are brand-aligned and demonstrate the shared packages in use.

Required screens for every template:

- **Welcome / sign-in** (uses `auth-shell-package`).
- **Home** (post-sign-in landing; shows the agent presence widget from `agent-presentation-package` and a sample data card).
- **Settings** (account, privacy controls, consent management consuming the consent ledger from `fabric-client-package`).
- **Consent prompt** (a reusable flow for granting / revoking a consent class; consumed by other screens via deep-link).
- **Crisis safety surface** (the in-app resources surface invoked by the crisis rail; uses the `crisis-banner` and `consent-prompt` contracts).
- **Empty state** (a single representative empty state; downstream products override per surface but the example must exist).
- **Error state** (a single representative error; same pattern).

Delta files may add screens specific to that template (e.g., the phone template adds the voice-loop screen).

### 2.3 Accessibility implementation

**Mandatory.** Every template ships a working implementation of the accessibility-budget rules from `design-system/accessibility-budget.md`. This is not optional; the budget exists because Cytognosis serves patients, and accessibility is a clinical concern, not a feature.

Required implementation hooks:

- Focus management on route changes (move focus to the main heading; announce via live region).
- Keyboard navigation (tab order matches reading order; visible focus styles).
- Reduced-motion variants for every animation; honor `prefers-reduced-motion`.
- Screen reader support (semantic markup; aria-* where necessary; live regions for agent messages).
- Touch / pointer target sizes meeting the budget (44pt phone, 24px web standard, 32px patient-facing).
- Color independence: state never communicated by color alone; pair color with icon or text.
- Time independence: no forced timeouts on patient-facing flows.

Each template ships an `accessibility.md` documenting how each rule is implemented in that framework.

### 2.4 Brand voice in all microcopy

**Mandatory.** Every string in every template adheres to the voice and tone rules from `design-system/voice-and-tone/`. No "user"; use "patient", "clinician", "researcher", or "you". No em dashes. No infantilizing language. Crisis copy uses the crisis-rails patterns verbatim where applicable.

The template must include a `microcopy.json` (or framework-equivalent localizable resource) where every string is keyed and easy to swap. No string literals scattered in components.

### 2.5 Telemetry with privacy defaults

**Mandatory.** Every template wires `telemetry-package` so that:

- No event is sent without a registered schema.
- Every event field carries a redaction class (`none`, `pii`, `clinical`, `secret`).
- Default redaction applies on send and verifies on receive.
- Telemetry is opt-in. The default for any non-essential event is OFF. The opt-out control is one tap reachable from the home or settings surface.
- A debug overlay (gated behind a developer flag) shows exactly what is being sent.

### 2.6 Voice surface (where applicable)

**Mandatory** for the phone, web, and desktop templates. **Optional** for the extension template (voice is not the primary modality there).

When voice is included:

- `voice-client-package` is wired with a default empathic-listening visual (consumes the voice-affordance contract).
- The voice loop never sends raw audio off-device; only schema-enforced feature events traverse the fabric.
- Turn-taking respects barge-in: the agent can be interrupted; the user can interrupt without penalty.
- A clearly accessible "pause listening" affordance is reachable from the voice surface.

### 2.7 Agent presence

**Mandatory.** Every template renders the agent's connection state, capabilities, and turn-taking state via `agent-presentation-package`. This is the same widget across all four templates so a patient encountering Cytognosis on phone and on web sees the same conventions.

Required states the widget represents:

- Connecting / Connected / Disconnected
- Listening / Thinking / Speaking / Quiet
- Tool-use disclosure (when the agent is using a tool, the widget shows which)
- Escalation (when the agent has delegated; shows tier handoff)
- Crisis (visually distinct, accessible to colorblind users)

### 2.8 Build, lint, type-check, test

**Mandatory.** Every template inherits the seven shared workflow files from `cytocast/templates/_shared/.github/workflows/`. The template's job is to ensure those workflows pass on first scaffold.

Specifically:

- Lint passes (biome for TS, dart analyze for Flutter, ruff for any Python tooling).
- Type-check passes (tsc strict for TS; mypy for Python; Flutter analyzer).
- Tests pass; the template ships at least one unit test, one integration test, and one accessibility test (axe-core where applicable; Flutter accessibility scanner on phone).
- Build produces an artifact (a buildable bundle / APK / IPA / Tauri binary / extension zip, depending on template).
- Bundle-size budget enforced (per delta).

### 2.9 Documentation

**Mandatory.** Each template ships:

```
docs/
├── README.md                  ("you have just scaffolded this template; here is how to run it")
├── architecture.md            (the template's structure; where each shared package lives in the codebase)
├── accessibility.md           (how the template implements the budget)
├── privacy.md                 (what data the template handles and where it goes)
├── voice.md                   (only if voice is included)
└── deployment.md              (how to ship a downstream product built from this template)
```

### 2.10 Skill bundle

**Mandatory.** Each template ships a `.agents/skills/` directory bootstrapped by cytocast at scaffold time. This is consumed by coding agents (Antigravity, Claude Code, others) working on the downstream product.

The template's job: ensure the directory exists and references the cytocast-provided dev skills relevant to that template's stack. The template does not author new skills; it just declares which it depends on (in `.agents/skills/manifest.yaml`).

## 3. Optional artifacts (shared)

Include when they add real value, omit if they would dilute.

- **Onboarding tour** (a first-run guided tour). Useful for patient-facing products; pointless for internal tools. Decide per delta.
- **Theme switcher** (light / dark / auto). Always supported by the Design System tokens; the template may expose a UI control. Recommended for web and desktop; less critical for phone (which can follow system); not applicable for extension side panel (inherits browser).
- **Offline mode** (cached read-only state when the network is down). High value for phone; moderate for web; low for desktop (which uses Iroh CRDT regardless); low for extension.
- **Demo / fixtures mode** (a "demo data" build flag so non-engineers can run the template without backend access). Highly recommended; speeds review and grant demos.
- **Storybook** (or equivalent component explorer). Recommended for web and extension; per-platform tooling for phone (`widgetbook`) and desktop.
- **i18n scaffolding** (English-only at scaffold time; ICU-format message extraction wired so additional locales can be added without code changes). Recommended.

## 4. Folder layout (shape that every template follows)

```
app-<name>/
├── README.md
├── docs/                                  (mandatory; see §2.9)
├── microcopy.json                         (mandatory; all UI strings)
├── .agents/                               (mandatory; skills manifest)
│   └── skills/manifest.yaml
├── .github/workflows/                     (mandatory; inherited from cytocast _shared)
├── src/                                   (framework-specific layout per delta)
│   ├── shared/                            (consumes the seven shared packages)
│   ├── screens/                           (starter screens + template-specific)
│   ├── theme/                             (consumes design-system tokens)
│   └── ...
├── tests/                                 (mandatory baseline)
│   ├── unit/
│   ├── integration/
│   └── accessibility/
├── fixtures/                              (optional; demo data)
├── public/ or assets/                     (per framework convention)
└── pubspec.yaml | package.json | Cargo.toml  (framework-specific)
```

## 5. Naming and styling conventions

### 5.1 File names

- Source files: framework-idiomatic (`PascalCase.tsx` for React, `kebab-case.dart` for Flutter, `kebab-case.rs` for Rust).
- Documentation: kebab-case `.md`.
- Configuration: lowercase (`.eslintrc`, `biome.json`, `tsconfig.json`, `analysis_options.yaml`).
- Microcopy keys: dot-namespaced lowercase (`screen.home.welcome.heading`).

### 5.2 Component implementations

- Components import semantic tokens, never physical tokens directly.
- Components implement the Design System contracts; do not deviate from the contract's prop names or states.
- Components have no internal styling other than via tokens; no inline `#hexvalue` colors anywhere.
- Components export both a typed component and its prop types (so downstream consumers can extend cleanly).

### 5.3 Microcopy and strings

- Every visible string lives in `microcopy.json` (or framework-equivalent).
- Every string carries a key, a value, an optional plural form, an optional context.
- Strings reference the brand-voice rules; the brand-review skill from branding is the source of truth for review.

### 5.4 Code style

- TypeScript: biome formatter (2-space indent), strict TS (`noImplicitAny`, `strict`, `exactOptionalPropertyTypes`).
- Dart: `dart format` (2-space), strict analyzer (`always_specify_types`, `prefer_const_constructors`, custom Cytognosis lints).
- Rust: `rustfmt` defaults + `clippy --deny warnings`.
- No semicolons in TS/JS where the formatter omits them; do not fight the formatter.
- Imports ordered: standard, third-party, internal, relative. Enforced by the formatter.

### 5.5 Folder hygiene

- A folder containing components is `Components/` (PascalCase) on the web/desktop/extension templates; `widgets/` (lowercase) on Flutter.
- A folder containing screens is `screens/` (lowercase) across all templates.
- A folder containing hooks (React) or controllers (Flutter Riverpod or Bloc) is named after the convention of the framework.
- No `utils/` or `helpers/` dumping grounds; if a module is large enough to warrant a folder, give it a name describing what it does.

## 6. Privacy posture (cross-template)

Every template, on the first scaffold, must satisfy:

1. **No raw audio leaves the device.** The voice-client package enforces this; the template must not bypass it.
2. **No PII in telemetry.** The telemetry package's redaction defaults enforce this; the template must not declare an event with a `pii`-tagged field unredacted.
3. **Consent before escalation.** Any action that escalates to a cloud tier requires a positive consent grant in the ledger; the consent-prompt screen handles the grant flow.
4. **Local-first state.** Iroh CRDT documents are the default for any state that needs to survive offline.
5. **Auditable.** The debug overlay (developer-only) lets a reviewer see what is sent, when, and to whom.

## 7. Quality gates (cross-template)

Every template must pass on first scaffold:

| Gate | Tool | Threshold |
|---|---|---|
| Lint | biome / dart analyze / clippy | zero warnings |
| Type-check | tsc / mypy / dart | strict mode, zero errors |
| Test coverage | jest / dart test / cargo test | 80% line coverage minimum |
| Accessibility | axe-core / Flutter a11y scanner | zero critical or serious issues |
| Bundle size | per delta | per delta |
| Build determinism | reproducible build flag | identical artifact on re-build |

Templates that do not pass on first scaffold are not ready to ship.

## 8. Definition of done for a template revision

Before declaring a revision of any one of the four templates complete:

1. All shared mandatory artifacts in §2 are present and exercised.
2. All delta-mandatory artifacts (in the matching delta file) are present and exercised.
3. CI is green on a fresh clone with the cytocast scaffolding step.
4. The starter screens render correctly and demonstrate the seven shared packages.
5. The accessibility budget is met and documented.
6. No em dashes anywhere in any output.
7. The template's `docs/README.md` walks a new developer from clone to running the starter screens in under 10 minutes.

## 9. What to NOT produce

- Do not write new tokens or new component contracts; those live in the Design System. If a missing token is blocking, surface to the Cytognosis team rather than improvising.
- Do not write new shared packages. The seven listed are the surface; if a new one is genuinely needed, surface for review.
- Do not write product-specific screens. Templates ship the starter set; product-specific screens are downstream.
- Do not vendor copies of the design-system files; consume them from `branding` (via `design-system-package`).
- Do not introduce new agent skills. Skills live in the four sources defined by the four-phase skill model (branding, cytoskeleton, cytocast, cytoagent), not in template repos.

## 10. Open questions for the Cytognosis team

When you hit any of these, pause and ask:

1. The auth provider default is unset; Clerk vs Supabase vs self-hosted (Keycloak / Authentik). Pick before wiring `auth-shell-package`.
2. The default empathic-listening visual: a particle-flow pattern, a calm pulse, or a waveform-derived shape? Decide globally so all templates use the same.
3. The crisis-banner placement convention: top-of-screen sticky vs bottom-fixed vs modal-blocking. Decide globally.
4. The onboarding tour: in or out? Defaults differ per template; align with the patient-vs-clinician posture.
5. Demo/fixtures mode: should it be wired by default and gated by a build flag, or off by default and opt-in?

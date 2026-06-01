# Claude Design Prompt: Create the `app-phone` Template

> Paste this prompt into Claude Design when you want it to produce the **initial scaffold** of the Cytognosis phone template (`cytoskeleton/templates/app-phone/`). This template is the basis for the patient interviewer agent and any future Cytognosis mobile product, including the Yar companion app.
> Cytognosis context: full spec in `cytognosis-branding/references/phone.md`.

> **Revised from**: `Documents/Cytognosis/Infra and design/03_claude_design_prompts/prompt_template_phone.md`
> **Changes**: replaced `cytognosis-template-master` with `cytognosis-branding`, added Companion profile as default for Yar mobile surfaces, added Crisis profile for health alert dialogs, added Lexend and Atkinson Hyperlegible font support, removed em dashes.

---

## Brief

Produce the initial scaffold for the Cytognosis phone template. The template is the base for voice-first, patient-facing mobile products on iOS and Android, with the empathic interviewer agent as the headline product and the Yar companion app as the daily-use ND surface. It must build on first clone, pass the cross-template quality gates, host the LiteRT-LM edge model lazily, run the on-device paralinguistic pipeline, and ship the crisis-rail safety surface.

The phone is the highest-stakes surface in the Cytognosis platform. Calm, accessible, patient-respectful at every interaction.

## 1. Stack (mandatory choices)

- **Framework**: Flutter, latest stable.
- **Language**: Dart 3.x.
- **State management**: Riverpod (preferred).
- **Animation**: Rive for agent-state characters; built-in `AnimationController` for transitions.
- **Routing**: `go_router`.
- **Local storage**: `hive` (key-value), `drift` (relational), `iroh-flutter` (CRDT sync via cytoplasma fabric).
- **Edge model runtime**: LiteRT-LM with Gemma 4 E2B (lazy-loaded, behind a `LocalModelService` abstraction).

## 2. Profile assignments

The phone template supports three profiles, selected by surface context:

| Surface | Default profile | Rationale |
|---|---|---|
| Interviewer agent (clinical) | Clinical | Patient-facing clinical context |
| Yar companion (daily use) | Companion | ND-first daily use; Lexend font, generous spacing, reduce-motion default |
| Health alert dialogs | Crisis | Emergency/safety surfaces; high contrast, large type, single-action focus |

Profile switching uses the `[data-profile]` mechanism. The app reads the current context and applies the appropriate profile overlay.

## 3. Mandatory artifacts in the scaffold

### 3.1 Seven starter screens

```
lib/screens/
├── welcome/                    onboarding entry; consent grants; voice-permission walkthrough
├── onboarding/                 < 90 s sequence: intro, consent, voice demo, crisis-affordance reveal
├── home/                       agent presence widget + quick voice loop entry
├── voice_loop/                 the headline screen (listen/speak/repair states)
├── settings/                   privacy, consent management, data-usage panel, voice settings
├── consent_prompt/             grant or revoke individual consent classes
├── crisis_safety/              the patient-facing safety surface (Crisis profile)
├── empty_state/                representative empty state
└── error_state/                representative error state
```

### 3.2 Services

```
lib/services/
├── local_model_service.dart    LiteRT-LM wrapper; lazy load; memory-pressure handling; battery awareness
├── voice_service.dart          VAD + barge-in + push-to-talk fallback
├── paralinguistic_service.dart on-device HuBERT + openSMILE feature extraction; emits schema-enforced events
├── crisis_detector_service.dart  rules-table-driven, on-device, priority-channel events
└── profile_service.dart        manages active profile (Clinical/Companion/Crisis) based on surface context
```

### 3.3 Edge model wiring

- LiteRT-LM is the runtime; Gemma 4 E2B is the default model. Both pinned versions.
- Model loads on first voice interaction with a progress affordance, not at app cold start.
- Memory pressure (iOS / Android warnings) unloads gracefully; reload on next demand.
- Below 15% battery, the service degrades to laptop-tier routing (via `fabric-client-package`) instead of running edge inference.

### 3.4 Paralinguistic pipeline

- VAD running on-device.
- HuBERT + openSMILE feature extraction streaming.
- Target end-to-end latency < 250 ms (utterance offset to feature event emitted to fabric).
- Events conform to `cytos.schema.events.voice_features` (LinkML).
- Privacy gate (from `fabric-client-package`) validates every send. Raw audio never leaves the device.

### 3.5 Voice loop UI

- Primary listening affordance: large, central, accessible.
- Visual states: listening (the calm pulse pattern from the design system), thinking (subtle motion + thinking indicator), speaking (waveform from amplitude).
- Barge-in: tapping while the agent speaks interrupts cleanly.
- Push-to-talk fallback in Settings.
- "Pause listening" affordance reachable from the voice loop without entering Settings.
- Empathic-backchannel widget: low-intrusion acknowledgment cues during user speech (visual or subtle haptic; never audio).

### 3.6 Crisis-detection rails

- Rules-based detector wired to the voice pipeline (paralinguistic features + intent classifications).
- Rules table is data, loaded from a schema-validated YAML at scaffold time so it can be updated without code change.
- Emits `CrisisDetected` events on a priority channel (exempt from standard reliability budgets).
- The crisis-safety surface is reachable manually at any time via a persistent affordance, not only on positive detection.
- Surface uses the `crisis-banner` and `consent-prompt` contracts from the Design System.
- **Crisis profile activates automatically** when the crisis-safety surface renders: high contrast, 56px touch targets, no animations, single-action focus.

### 3.7 Consent management

- Plain-language descriptions for each consent class. Microcopy from `branding/design-system/voice-and-tone/microcopy-patterns/consent.md`.
- Revoke in one tap from settings.
- Default state for non-essential consent classes: OFF.
- Cloud-tier escalation requires positive `share_with_cloud_specialist` grant.

### 3.8 Onboarding (< 90 s target)

1. Cytognosis in three sentences (brand-voice aligned).
2. Voice-permission grant walkthrough.
3. Initial consent grants (everything optional defaulted OFF).
4. Voice loop demo with low-stakes prompt ("How are you feeling today?").
5. Crisis-safety affordance reveal.
6. **Profile selection**: if the app detects Yar companion mode, onboarding defaults to Companion profile with Lexend font and generous spacing.

### 3.9 Accessibility implementation

In addition to the cross-template baseline:

- Dynamic Type (iOS) support: typography scales by user system setting.
- Bold Text and Reduce Transparency (iOS) support.
- TalkBack (Android) and VoiceOver (iOS) tested on every screen.
- 44pt minimum touch target verified by Flutter accessibility scanner (48pt for Companion profile, 56pt for Crisis profile).
- One-handed reachability: primary actions in the lower two-thirds of the screen.

### 3.10 Font support

The phone template supports multiple font families, selectable per profile and via user preference:

| Font | Role | Available in |
|---|---|---|
| Inter | Default body and headings | Clinical, Foundation |
| Lexend | Body text for reading fluency | Companion (default) |
| Atkinson Hyperlegible | Code, data displays, high-distinguishability text | Companion (code/data), Crisis (alternate) |
| OpenDyslexic | User-selectable alternate | All profiles via Settings toggle |

Font toggle lives in Settings and persists across sessions. Companion profile defaults to Lexend; all other profiles default to Inter.

### 3.11 Battery and data discipline

- Background-task budget: no background work beyond crisis-rail listening when explicitly opt-in.
- Cellular-data switch: patient can require Wi-Fi for all fabric traffic.
- Data-usage panel in Settings showing approximate bytes by category.

### 3.12 Theme + tokens

- Material 3 base with Cytognosis brand overlay.
- Design tokens consumed via `design-system-package`'s Dart binding (`Tokens.cgViolet600`, etc.).
- Light + dark modes both supported; default to system.
- Clinical profile: AAA contrast where feasible.
- Companion profile: muted 300-shade pastels, cognitive-signal colors, reduce-motion default.
- Crisis profile: maximum contrast, no decorative elements, 56px touch targets.

## 4. File layout

```
app-phone/
├── pubspec.yaml
├── analysis_options.yaml
├── lib/
│   ├── main.dart
│   ├── app.dart
│   ├── theme/                  consumes design-system tokens; Material 3 + brand overlay; per-profile themes
│   ├── routing/                go_router config
│   ├── shared/                 consumes the seven shared packages
│   ├── screens/                per §3.1
│   ├── widgets/                template-local reusable widgets
│   ├── services/               per §3.2
│   └── state/                  Riverpod providers
├── assets/
│   ├── animations/             Rive files for agent states (placeholders OK)
│   ├── icons/                  re-exported from Design System (line variant at 24pt @1x/2x/3x)
│   ├── fonts/                  self-hosted Cytognosis fonts (Inter, Lexend, Atkinson Hyperlegible, OpenDyslexic)
│   └── rules/                  crisis-detector rules table (YAML)
├── ios/                        Flutter iOS scaffold
├── android/                    Flutter Android scaffold
├── test/                       unit + widget tests
├── integration_test/           full voice-loop happy path
├── docs/
│   ├── README.md
│   ├── architecture.md
│   ├── accessibility.md
│   ├── privacy.md
│   ├── voice.md
│   ├── profiles.md             documents Clinical/Companion/Crisis profile switching
│   └── deployment.md
├── microcopy.json              every UI string keyed
└── .agents/skills/manifest.yaml  dev-skill dependencies
```

## 5. Brand alignment

- Material 3 base + Cytognosis brand overlay.
- Clinical profile by default for interviewer agent surfaces; Companion profile for Yar daily-use surfaces; Crisis profile for health alert surfaces.
- Consume design tokens via the `design-system-package` Dart binding; never inline a `Color(0x...)` literal.
- Cytognosis voice rules in every visible string. Microcopy in `microcopy.json`.
- Logo mark in the splash screen + app icon; not in the body of any screen.
- Body text minimum 17pt (Clinical profile), 16pt with Lexend (Companion profile), 18pt (Crisis profile).

## 6. Quality gates

- APK / IPA bundle: target < 40 MB, hard fail > 60 MB.
- Cold start: < 1.5 s to first meaningful frame on Pixel 6a class.
- First-voice-interaction latency: < 250 ms press to listening state visible.
- Crisis-rail latency: < 1 s feature event to crisis-safety surface visible.
- Memory ceiling: < 250 MB resident with edge model loaded.
- Flutter accessibility scanner: zero critical or serious issues.
- Coverage: 80% line minimum (Riverpod providers, services, state machines).
- Integration test: a synthetic voice exchange completes happy path.
- Profile switching: < 100 ms to apply new profile overlay.

## 7. Hard rules

- Widgets are `StatelessWidget` unless local state is genuinely needed.
- Use `const` constructors aggressively (analyzer enforces).
- No `dynamic`. Use `Object?` and pattern-match.
- All side effects through service classes, not inside widgets.
- All async via `Future` or `Stream` explicitly. No callback-style.
- No platform-specific UI that breaks brand parity. Material 3 + Cytognosis overlay on both iOS and Android.
- Companion profile respects `prefers-reduced-motion` by default; animations opt-in only.
- Crisis profile renders zero animations under all conditions.

## 8. What to NOT produce

- No third-party analytics SDKs.
- No push notifications beyond what crisis rail explicitly needs.
- No direct cloud LLM calls; escalation via `fabric-client-package` only, consent-gated.
- No bottom tab bar by default; the headline screen is the voice loop.
- No second state-management library; pick Riverpod and document.
- No raw audio leaving the device under any circumstance.
- No bypass of the privacy gate in `fabric-client-package`.

## 9. Definition of done

1. `flutter run` brings up the app on iOS Simulator and Android Emulator.
2. Cold start under 1.5 s on a Pixel 6a class device profile.
3. The starter voice loop completes a synthetic happy path against a local cytoplasma peer in integration test.
4. The paralinguistic pipeline emits valid feature events that pass schema validation.
5. The crisis rail triggers the safety surface on a synthetic positive (test-only rules path).
6. Accessibility scanner reports zero critical or serious issues on every screen.
7. Onboarding completes in under 90 seconds for a representative user (measured manually for first revision).
8. `docs/README.md` walks a new developer from clone to first voice exchange in under 15 minutes.
9. Profile switching works across Clinical, Companion, and Crisis contexts.
10. Font toggle switches between Inter, Lexend, Atkinson Hyperlegible, and OpenDyslexic.
11. No em dashes anywhere.

## 10. Deliverables to ship back

1. The complete `app-phone/` tree.
2. The placeholder Rive animations (or clearly-flagged TODOs if commissioning is needed).
3. A `MIGRATION.md` for any salvaged content from current Cytognosis mobile work (if any).
4. The first PR-ready commit message in Conventional Commits format.

## 11. Open questions to surface back to Cytognosis

1. Initial Rive animations for agent states: commission custom or design in-house? The scaffold ships placeholders.
2. Crisis-detector rules table: who owns clinical sign-off? Scaffold ships a v1 placeholder.
3. Initial onboarding prompt: does "How are you feeling today?" need clinical review for the first revision?
4. Push notifications for crisis events: in or out for the first revision? Recommendation: out (in-app only).
5. Single app with build flag for interviewer-agent + asset-hub vs two apps? Scaffold supports both via cytocast profile choice.
6. The voice loop's empathic-backchannel cues: visual only (default) or visual + haptic?
7. Companion profile gamification: should streak and progress tokens appear in the first revision, or defer to v2?
8. OpenDyslexic font licensing: self-host or load from CDN? Recommendation: self-host (it is open source).

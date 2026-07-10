# Claude Design Brief: Phone Template (Delta)

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: engineers
> **Tags**: `engineering`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)

> Read `templates_general_brief.md` first. This file only carries what is unique to the phone template.
> Output destination: `cytoskeleton/templates/app-phone/`.

## 1. What this template is for

The phone template is the base for Cytognosis products that run primarily on a phone with a voice-first interaction model. The headline product is the empathic interviewer agent (the patient-facing voice agent that runs on a phone in Tier 1 of the multi-agent architecture). Other planned products derived from this template include the asset / knowledge-hub mobile client, the longitudinal-recorder companion, and the caregiver-facing variant. These may ship as one app with a profile switch or as separate apps; the template supports both via a build flag.

The phone is the highest-stakes surface in the platform. It is where the patient meets the system. The template should be calm, accessible, and patient-respectful at every interaction.

## 2. Framework and platform

- **Framework**: Flutter, latest stable channel (currently 3.x).
- **Language**: Dart 3.x.
- **State management**: Riverpod (preferred) or Bloc. The template should expose a clear convention; do not mix.
- **Animation**: Rive for character / agent-state animations; Flutter's built-in `AnimationController` for transitions.
- **Routing**: `go_router`.
- **Local storage**: `hive` for key-value; `drift` if relational; `iroh-flutter` binding for CRDT state shared with the fabric.

## 3. Mandatory artifacts (phone-specific)

In addition to the cross-template mandatory artifacts in `templates_general_brief.md`.

### 3.1 Edge model runtime

**Mandatory.** Wire `LiteRT-LM` so the template can host an edge model (Gemma 4 E2B is the planned default). The runtime sits behind a `LocalModelService` abstraction so the template can swap models without rewriting consumers.

Required:

- Lazy load: the model is not loaded on cold start; it loads on first voice interaction with a progress affordance.
- Memory pressure handling: the runtime unloads gracefully under iOS / Android memory warnings and reloads on next demand.
- Battery awareness: if the device is below 15% battery, the template degrades to laptop-tier first (via the fabric client) rather than running the edge model.

### 3.2 Paralinguistic feature pipeline

**Mandatory.** A streaming pipeline that extracts HuBERT and openSMILE features from microphone audio on-device, emits schema-enforced feature events to the fabric, and never transmits raw audio.

Required:

- Voice Activity Detection (VAD) on-device.
- Feature extraction pipeline with a documented frame rate and a documented latency budget (target: under 250 ms end-to-end from utterance offset to feature event sent).
- Schema-enforced events conforming to `cytos.schema.events.voice_features` (LinkML).
- Privacy gate from the `fabric-client-package` validates every send.

### 3.3 Voice loop

**Mandatory.** The user-facing voice loop, with:

- A primary listening affordance (large, central, accessible).
- Visual feedback in three states: listening (the calm pulse from the Design System), thinking (subtle motion plus a thinking indicator from agent-presentation-package), speaking (waveform-derived shape from the speech amplitude).
- Barge-in: tapping while the agent speaks interrupts the agent cleanly.
- Push-to-talk fallback for users who prefer it (in Settings).
- A clearly accessible "pause listening" affordance reachable without entering settings.
- An empathic-backchannel widget: while the user speaks, the agent emits low-intrusion acknowledgment cues (visual or subtle haptic; never audio that would interfere with the user's voice).

### 3.4 Crisis-detection rails (Tier 1)

**Mandatory.** The phone template ships the Tier 1 rules-based crisis detector wired to the voice pipeline. The detector consumes the paralinguistic features and the intent classification stream, applies a deterministic rules table, and emits `CrisisDetected` events to the fabric. The template renders a crisis-safety surface on positive detection.

Required:

- The detector runs on-device with no cloud dependency.
- The rules table is data, loaded at scaffold time from a schema-validated YAML (so the rule set can be updated without code change).
- Crisis events bypass the standard reliability budgets and are emitted on a priority channel.
- The crisis-safety surface is reachable manually at any time from a persistent affordance, not only triggered by detection.

### 3.5 Consent surface

**Mandatory.** A clear consent surface that lets the patient see, grant, and revoke each consent class. Consent decisions are written to the Iroh CRDT consent ledger via `fabric-client-package`.

Required:

- Plain-language descriptions for each consent class (the microcopy comes from `design-system/voice-and-tone/microcopy-patterns/consent.md`).
- Revoke is reachable in one tap from settings.
- Default state for any non-essential consent class is OFF.
- Cloud-tier escalations require an explicit positive grant for `share_with_cloud_specialist`.

### 3.6 Onboarding

**Mandatory.** A short onboarding sequence (target: under 90 seconds) that:

1. Introduces Cytognosis in three sentences (microcopy from the brand voice).
2. Walks the patient through the voice-permission grant.
3. Walks through the initial consent grants (with everything optional defaulted OFF).
4. Demonstrates the voice loop with a single low-stakes prompt ("How are you feeling today?").
5. Surfaces the crisis-safety affordance and shows where it lives.

### 3.7 Accessibility (phone-specific additions)

In addition to the cross-template accessibility baseline:

- Dynamic Type support (iOS): the template scales typography by the user's system setting.
- Bold Text and Reduce Transparency support (iOS).
- TalkBack (Android) and VoiceOver (iOS) tested for every screen.
- Minimum touch target 44pt (Apple HIG) verified by the accessibility scanner.
- One-handed reachability: primary actions sit in the lower two-thirds of the screen.

### 3.8 Battery and data discipline

**Mandatory.** The template includes:

- Background-task budget: the app does no work in background beyond what is required for crisis-rail listening when the patient has explicitly opted in.
- Cellular-data switch: the patient can require Wi-Fi for any fabric traffic (default ON for asset / knowledge-hub apps; default OFF for the interviewer agent because it should be reachable anywhere).
- Data-usage panel in settings showing approximate sent and received bytes per category.

## 4. Optional artifacts (phone-specific)

- **Apple Watch / Wear OS companion** (post-MVP; only if a real product needs it).
- **Lock-screen widget** showing agent state (post-MVP).
- **Live Activity** (iOS) showing an ongoing voice session.
- **Quick Settings tile** (Android) for one-tap voice loop.
- **Shortcuts integration** (iOS Shortcuts, Android App Actions).

## 5. Folder layout (phone-specific)

```
app-phone/
├── pubspec.yaml
├── analysis_options.yaml
├── lib/
│   ├── main.dart
│   ├── app.dart                       (top-level app)
│   ├── theme/                         (consumes design-system tokens; Material 3 + brand overlay)
│   ├── routing/                       (go_router config)
│   ├── shared/                        (consumes the seven shared packages)
│   ├── screens/
│   │   ├── welcome/
│   │   ├── onboarding/
│   │   ├── home/
│   │   ├── voice_loop/                (the headline screen)
│   │   ├── settings/
│   │   ├── consent_prompt/
│   │   ├── crisis_safety/
│   │   ├── empty_state/
│   │   └── error_state/
│   ├── widgets/                       (template-local widgets; reusable across screens)
│   ├── services/
│   │   ├── local_model_service.dart   (LiteRT-LM wrapper)
│   │   ├── voice_service.dart         (VAD + barge-in)
│   │   ├── paralinguistic_service.dart (HuBERT + openSMILE pipeline)
│   │   └── crisis_detector_service.dart
│   └── state/                         (Riverpod providers or Bloc cubits)
├── assets/
│   ├── animations/                    (Rive files for agent states)
│   ├── icons/                         (re-exported from design-system iconography)
│   └── fonts/
├── test/                              (unit + widget)
├── integration_test/
└── docs/                              (per cross-template requirements)
```

## 6. Code style (phone-specific additions)

- Widgets are `StatelessWidget` unless local state is genuinely needed.
- Use `const` constructors aggressively (analyzer enforces).
- No `dynamic`; prefer `Object?` and pattern-match.
- All side effects through service classes, not inside widgets.
- All async work uses `Future` or `Stream` explicitly; no callback-style.

## 7. Quality gates (phone-specific)

- **APK / IPA bundle size**: target under 40 MB; hard fail above 60 MB.
- **Cold start**: under 1.5 s to first meaningful frame on a mid-range Android device (Pixel 6a class). Profile in CI.
- **First-voice-interaction latency**: under 250 ms from press to listening state visible.
- **Crisis-rail latency**: under 1 s from feature event to crisis-safety surface visible.
- **Memory ceiling**: under 250 MB resident with edge model loaded.

## 8. Definition of done (phone-specific additions)

In addition to the cross-template definition of done:

1. The LiteRT-LM runtime loads Gemma 4 E2B and runs an end-to-end voice exchange in the integration test.
2. The paralinguistic pipeline emits feature events that pass schema validation.
3. The crisis rail triggers the safety surface on a synthetic positive in the integration test.
4. The accessibility scanner reports zero critical or serious issues on every screen.
5. The onboarding sequence completes in under 90 seconds for a representative user (measured manually for the first revision; automated later).

## 9. What to NOT produce (phone-specific)

- Do not embed any non-Cytognosis analytics SDKs. Telemetry is exclusive to `telemetry-package`.
- Do not introduce push-notification flows beyond what is necessary for the crisis rail (push for crisis only, per current scope).
- Do not write platform-specific UI in iOS or Android styles that breaks parity. Use Material 3 with the Cytognosis brand overlay across platforms.
- Do not include a tab bar or bottom navigation by default; the headline screen is the voice loop. Sub-products may add nav per their own design.
- Do not call cloud LLMs from this template directly. All escalation goes through `fabric-client-package` and is consent-gated.

## 10. Open questions for the Cytognosis team

1. The initial Rive animations for agent states: commission custom or design in-house? The template ships placeholders.
2. The crisis-detector rules table: who owns clinical sign-off on the rules? The template ships a v1 placeholder; production deployments require formal review.
3. The onboarding's initial prompt ("How are you feeling today?"): does this need clinical review for the first revision, or is the placeholder acceptable until a clinician sign-off?
4. Push notifications for crisis: in or out for the first revision? Recommendation: out (in-app only) until the consent UX is reviewed.
5. The phone template should serve both the interviewer agent and the asset-hub client. Are these the same app with a build flag, or two apps? The template supports both; the cytocast profile asks at scaffold.

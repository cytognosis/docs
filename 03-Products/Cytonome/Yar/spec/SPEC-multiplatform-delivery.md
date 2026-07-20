---
spec_id: SPEC-multiplatform-delivery
version: "1.0"
status: draft
domain: multiplatform-delivery
owner: Shahin Mohammadi
created: 2026-07-19
last_updated: 2026-07-19
depends_on:
  - SPEC-sync-protocol
  - SPEC-browser-extension
  - org interface_and_fabric_design (00_master_architecture.md, 01_refactor_brief.md)
coordinates_with:
  - SPEC-multi-agent
  - SPEC-transcriber-agent
  - SPEC-CSP
  - MODULE-crisis-detection
  - SPEC-personas-voice
  - YAR-CLIENT-EVAL
implements:
  - F41 (UI parity across phone, desktop, web dashboard; extension of F41, per FEATURE-VERIFICATION.md item 3a)
---

> **Status**: Draft v1
> **Date**: 2026-07-19
> **Author**: @shahin (agent-drafted, founder review pending)
> **Audience**: engineers and reviewers
> **Tags**: `yar`, `multiplatform`, `delivery`, `tauri`, `flutter`, `react`, `mv3`, `design-system-adoption`

**Reading time:** about 8 minutes.

**Note on the letters "CSP":** in this document, CSP means the **Cytonome Sensor Protocol** throughout (per `SPEC-CSP.md`). The browser manifest **Content Security Policy** directive, also abbreviated CSP, is discussed only in `SPEC-browser-extension.md` Section 8.3 and does not appear in this document.

**If you only read one thing:** Section 3 (phone framework recommendation) and Section 5 (the F41 parity statement). Together they settle the one open framework tension this spec faces and state exactly what "consistent" means across Yar's four surfaces.

---

## BLUF

Yar ships across four delivery surfaces (phone, desktop, web dashboard, browser extension) that map onto the org's four locked interface templates (`00_master_architecture.md` Section 4.2). This spec **adopts that design system wholesale** and adds only the deltas that exist because Yar is Yar. The one real tension: the org template names Flutter for phone, but Yar's shipped Wave 1 reference client is Tauri v2, which also targets iOS and Android; this spec recommends **Tauri v2 mobile**, with Flutter held as the org-template fallback.

---

## 1. Purpose and non-goals

**Purpose.** State, in one place, which org interface template each Yar delivery surface uses, resolve the phone-framework tension with a reasoned recommendation, and list the small number of Yar-specific UI deltas the org-wide design system does not already cover.

**Non-goals, what this spec does not own:**

| Area | Owner |
|---|---|
| Design tokens (color, type, motion, spacing) | `branding` repo, authored in Claude Design |
| Component library, the four interface template codebases themselves | `cytoskeleton/templates/app-*` |
| The four use-case profile CSS overlays (`[data-profile=...]`, Foundation / Clinical / Research / Lab) | `branding` + `cytoskeleton`, per `00_master_architecture.md` Section 11 |
| Per-agent conversational behavior (Transcriber, Proofreader, Mind-mapper, Interviewer, Supervisor) | `SPEC-multi-agent.md` and the per-worker specs |
| Sync wire protocol, CRDT op-log, conflict resolution | `SPEC-sync-protocol.md` |
| Extension-specific WADM capture and pairing mechanics | `SPEC-browser-extension.md` |

This spec is deliberately thin. It is an adoption and cross-reference document, not a design system.

---

## 2. Surface-to-template map

| Surface | Org template (`00_master_architecture.md` §4.2) | Status | Yar-specific deltas |
|---|---|---|---|
| **Phone** (`apps/mobile`) | `app-phone/`, org default is Flutter (BSD-3-Clause) | **Planned.** Framework choice open, see Section 3 | Voice-capture affordance, touch-first brainmap canvas, crisis screens, F23 read-aloud |
| **Desktop** (`apps/desktop`) | `app-desktop/`, Tauri v2 (MIT/Apache-2.0 dual) wrapping `app-web/` | **Shipped.** Wave 1 reference client per `YAR-CLIENT-EVAL.md` | Same deltas as web, plus native offline-first storage (op-log on local filesystem) |
| **Web dashboard** (`apps/web`) | `app-web/`, React 19 (MIT) + Vite (MIT) + Tailwind CSS (MIT) + shadcn/ui (MIT) | **Shipped**, Vite build clean per `YAR-CLIENT-EVAL.md` Section 9; used standalone and wrapped by desktop | Same deltas as desktop; "web" means the local dashboard build a person runs on their own machine, not a hosted multi-tenant site, consistent with Yar having no required server |
| **Browser extension** (`apps/extension`) | `app-extension/`, MV3 (platform API, not licensed software) plus side panel | **Drafted.** `SPEC-browser-extension.md`, capture and annotation only | Capture surface, not a full client (Section 5); paired localhost API handoff to desktop |

---

## 3. Phone framework recommendation

**The tension.** `00_master_architecture.md` Section 4.2 and Section 11 name Flutter as the org's locked phone template, authored in Claude Design. `YAR-CLIENT-EVAL.md` recommends adopting a Tauri v2 plus React plus Django codebase as the Yar Wave 1 reference implementation, and Tauri v2 targets iOS and Android from the same codebase already shipping Yar's desktop app.

**Recommendation: Tauri v2 mobile.** One codebase across desktop and phone means the op-log, the CRDT reducer, offline-first behavior, and every delta in Section 4 (voice capture, brainmap canvas, crisis screens) are written once, not reimplemented a second time in Dart for the Flutter template. Yar is a single-engineer-scale Wave 1 product; a second UI codebase is a real cost, not a convenience.

**Evidence check (July 2026).** Tauri v2 reached stable in late 2024 and is on the 2.11 line as of mid-2026 (2.11.5, July 1, 2026). Mobile support, iOS and Android from one codebase, WKWebView on iOS and Android System WebView on Android, is **functional for production but newer and less mature than desktop**; plugin coverage on mobile lags desktop, and some capabilities need platform-specific code. iOS App Store publishing is a supported path (bundle identifier, code signing, provisioning, App Store Connect upload).

**Fallback.** If Tauri mobile hits a hard blocker, a required native capability with no mobile plugin, or App Store review friction tied specifically to Tauri's WebView bridge, fall back to the org-template default, Flutter, for phone only, keeping Tauri for desktop and web. Treat this as a last resort: it forks the brainmap canvas and voice-capture UI into a second codebase.

**Founder decision flagged.** The org master architecture and the Yar client evaluation point in different directions on this one surface. Recommendation stated above; proceeding on Tauri v2 mobile unless told otherwise.

---

## 4. Yar-specific deltas

Everything below is additive to the org-wide design system; none of it redefines a token, component, or CSS profile.

### 4.1 Voice-capture UI

| Requirement | Detail |
|---|---|
| Always-reachable capture affordance | A capture control (button, shortcut, or gesture) is reachable from every screen on every surface, not buried in a menu; mirrors F01 (voice brain dump) and the extension's toolbar/context-menu capture action |
| Streaming partial transcripts | Per `SPEC-transcriber-agent.md` Section 9's own risk table, partial (unfinalized) text must be visually distinct from finalized text, for example dimmed or lower-contrast styling, so mid-utterance revision reads as normal behavior, not an error |
| Cross-surface consistency | The same partial-versus-final visual language applies on phone, desktop, and web; the extension's side panel (F66 ask and summarize) reuses it for its own streaming responses |

### 4.2 CSP (Cytonome Sensor Protocol) consent screens

Per `SPEC-CSP.md` Section 5.3, every adapter connection is a consent gate, not a background permission grant. Each surface that can host a sensor adapter (phone, desktop; web and extension are not sensor hosts) presents the same consent screen shape: what the adapter reads, which privacy tier applies (`on_device_only`, `boundary_derived`, `clinician_gated`), and a clear disconnect path. No surface may skip this screen or pre-check a consent box.

### 4.3 Crisis-resource screens

Per `MODULE-crisis-detection.md` Sections 2 and 6, the crisis-resource screen is identical in content and tone on every surface capable of receiving input (phone, desktop, web): warm, non-clinical, one-tap call or text to the verified hotline for the active market, no dismiss-and-forget pattern, and the same "supportive continuation" afterward. The browser extension does not need its own crisis screen; captured page content is not a conversational input surface (`SPEC-browser-extension.md` Section 7).

### 4.4 The brainmap spatial canvas (real per-platform complexity)

This is the one surface where per-platform difference is genuine, not cosmetic. The canvas (`SPEC-multi-agent.md` Section 9, the Mind-mapper's placement target) needs a different interaction model per input device:

| Surface | Primary interaction | Note |
|---|---|---|
| Desktop / web | Mouse or trackpad: click-drag nodes, scroll-zoom, keyboard shortcuts | Reference implementation exists (`YAR-CLIENT-EVAL.md` Section 1, "Thought map (spatial canvas)") |
| Phone | Touch: drag, pinch-zoom, long-press for node actions; simplified gesture set, no keyboard-shortcut parity expected | New work regardless of the Section 3 framework choice; Tauri mobile reuses the same canvas component with touch event handlers, Flutter would require a second implementation |
| Extension | None | The extension is a capture surface, not a canvas host (Section 5) |

### 4.5 ND accessibility requirements

| Requirement | Detail |
|---|---|
| Reduced motion | Every surface honors a reduced-motion setting; the org accessibility budget (`branding/design-system/accessibility-budget.md`) is the source of truth for the threshold, this spec only requires it be wired on all four surfaces consistently |
| Sensory-load settings | A single sensory-load preference (density, animation, color intensity) travels with the person's Yar data via the same sync mechanism as any other setting, not re-entered per surface |
| F23 read-aloud with highlighting | Available on phone, desktop, and web; not applicable to the extension, whose content is handed off to the app before any read-aloud playback happens |

### 4.6 Offline-first behavior on every surface

Every surface functions fully without a network connection, consistent with `SPEC-data-sovereignty.md`'s no-required-server principle and `YAR-CLIENT-EVAL.md` Section 3. Sync, when enabled, is opt-in and additive per `SPEC-sync-protocol.md`; no surface degrades its own local functionality while waiting for a sync round-trip. The extension is the partial exception: its offline queue (`SPEC-browser-extension.md` Section 4.1) buffers locally and flushes once the paired desktop app is reachable, but capture and annotation both work with the app closed.

---

## 5. Parity statement (F41 extension)

Per `FEATURE-VERIFICATION.md` item 3a, cross-surface UI parity is **not a new feature id**; it is an explicit extension of **F41** ("all-in-one ND support app, no app-switching"). This spec states that extension concretely:

- **Phone, desktop, and web dashboard present one consistent UI.** Same navigation structure, same brainmap canvas (input-adapted per Section 4.4), same voice-capture affordance, same crisis and consent screens. A person moving from laptop to phone should not have to relearn where anything lives.
- **The browser extension is a capture surface, not a full client.** It exposes highlight, capture, pairing, and a thin ask-and-summarize side panel (F66); it does not attempt to replicate the brainmap canvas, daily plan, or full settings surface. This boundary is deliberate (`SPEC-browser-extension.md` Section 3, the Memex parity checklist) and prevents scope creep toward a second full app.

---

## 6. Risks

| Risk | Mitigation |
|---|---|
| Tauri mobile hits a plugin or App Store blocker after work has started | Section 3's fallback to Flutter for phone only; monitor Tauri mobile plugin coverage before committing device-tier features that need a missing plugin |
| Brainmap canvas touch interaction diverges in feel from desktop, breaking the F41 parity statement | Section 4.4's per-surface interaction table is the explicit gate; test plan (Section 7) includes a cross-surface canvas parity check |
| ND accessibility settings drift across four codebases over time | Single sensory-load preference synced via `SPEC-sync-protocol.md`, not re-implemented per surface; accessibility budget lives in one place (`branding`), not forked |
| Crisis or consent screen copy diverges by surface, undermining the non-negotiable safety principles in `MODULE-crisis-detection.md` | Screens are content-identical by requirement (Sections 4.2, 4.3); any divergence is a defect, not a variant |
| Extension scope creep toward a full client | Section 5's parity statement and `SPEC-browser-extension.md` Section 3's parity checklist are the explicit gates |
| Org template propagation (`00_master_architecture.md` Section 8, `copier update`) silently overwrites a Yar-specific delta | Yar deltas live in files the org's `_skip_files` mechanism can exempt from automated template updates; flag any delta file that has diverged from the template default |

---

## 7. Test plan

| Test | What it verifies |
|---|---|
| Cross-surface smoke matrix | Phone, desktop, web dashboard each boot, capture a voice note, and place it on the brainmap without error |
| Voice-capture partial/final rendering | Partial transcript text is visually distinct from finalized text on every surface (Section 4.1) |
| Crisis screen content parity | The crisis-resource screen shows identical copy, hotline, and one-tap action across phone, desktop, and web |
| Consent screen content parity | The CSP adapter-connect consent screen shows identical privacy-tier language across phone and desktop |
| Brainmap canvas touch parity | A person can place, move, and link a node on phone using the touch gesture set with the same end state as the desktop mouse flow |
| Accessibility budget conformance | Reduced-motion and sensory-load settings apply consistently across all four surfaces; F23 read-aloud is present on phone, desktop, and web |
| Offline-first regression | Each surface completes its core loop (capture, place, review) with networking disabled |
| Extension parity boundary | The extension never renders the full brainmap canvas, daily plan, or settings surface; only capture, annotate, pair, and the F66 side panel |
| Template-update non-regression | Running `copier update` from a new `cytoskeleton` template release does not silently revert a Yar-specific delta (Section 6) |

---

## 8. Open questions with recommendations

| # | Question | Recommendation |
|---|---|---|
| **Q1** | Tauri v2 mobile vs. Flutter for phone | **Resolved in this revision: Tauri v2 mobile** (Section 3), for one-codebase reasons; revisit only if a hard plugin or App Store blocker appears |
| **Q2** | Does the web dashboard need a separately hosted, multi-tenant deployment target? | **No.** It is the same Vite build the desktop app wraps, run locally by the person, consistent with "no required server" |
| **Q3** | Should the browser extension ever grow into a full client? | **No.** Section 5 and `SPEC-browser-extension.md` Section 3 fix this boundary; revisit only if a concrete Wave 2 feature cannot function under the current scope |
| **Q4** | Who verifies accessibility-budget conformance across four codebases over time? | **Recommend** the org accessibility budget (`branding/design-system/accessibility-budget.md`) as the single source of truth, with a per-surface check in this spec's Section 7 test plan rather than a fifth, Yar-only accessibility document |
| **Q5** | iOS App Store review risk specific to Tauri's WebView bridge | **Monitor, do not pre-decide.** No confirmed rejection pattern exists as of this writing; revisit the Section 3 fallback only if a real rejection occurs |

---

## Cross-references

- `00_master_architecture.md`, `01_refactor_brief.md`: the org-wide locked interface templates this spec adopts.
- `YAR-CLIENT-EVAL.md`: the shipped Tauri/React/Django reference client, the basis for Section 3's recommendation.
- `SPEC-browser-extension.md`: the extension template consumer and the Memex parity checklist Section 5 relies on.
- `SPEC-multi-agent.md`, `SPEC-transcriber-agent.md`: the brainmap loop and voice-capture behavior behind Sections 4.1 and 4.4.
- `SPEC-CSP.md`: the sensor consent model behind Section 4.2.
- `MODULE-crisis-detection.md`: the safety principles behind Section 4.3.
- `SPEC-sync-protocol.md`, `SPEC-data-sovereignty.md`: offline-first and no-required-server principles behind Section 4.6.
- `FEATURE-VERIFICATION.md` item 3a, `SPECS-INVENTORY.md`: the F41-extension decision this spec formalizes.

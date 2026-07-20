---
spec_id: SPEC-browser-extension
version: "1.0"
status: draft
domain: capture-web-annotation
owner: Shahin Mohammadi
created: 2026-07-19
last_updated: 2026-07-19
depends_on:
  - SPEC-sync-protocol
  - SPEC-petkg-longmemory
  - SPEC-multiplatform-delivery (forthcoming)
coordinates_with:
  - SPEC-multi-agent
  - SPEC-data-sovereignty
implements:
  - F50 (web annotation layer)
  - F59 (capture from anywhere, codename Cytomark)
  - F66 (ask and summarize your captures)
  - F16 (open export)
---

> **Status**: Draft v1
> **Date**: 2026-07-19
> **Author**: @shahin (agent-drafted, founder review pending)
> **Audience**: engineers and reviewers
> **Tags**: `yar`, `browser-extension`, `wadm`, `annotation`, `capture`, `mv3`, `memex`, `hypothesis`, `cytomark`

**Reading time:** about 15 minutes.

**If you only read one thing:** Section 4 (Memex parity checklist) and Section 6.3 (the app-handoff recommendation). Together they fix what this extension does and how it talks to the rest of Yar; everything else follows from those two decisions.

**Note on the letters "CSP":** this spec uses **CSP** exactly once, in Section 8, to mean the browser's **Content Security Policy** manifest directive. Everywhere else in the Yar corpus, CSP means the Cytonome Sensor Protocol. The two never appear in the same sentence in this document; where ambiguity is possible, this spec spells the term out.

---

## BLUF

The Yar browser extension is a **local-first, account-free, fully free** capture and annotation surface built on the org's locked MV3 plus side-panel interface template, re-grounding the superseded WADM annotation work in the architecture that exists today. It captures whole pages and text highlights as **W3C Web Annotation Data Model (WADM)** objects (Body, Target, Motivation, Selector, Provenance), riding the same `OpEnvelope` op-log every other Yar write uses, and hands off to the Yar desktop app over a **paired localhost API**, never a persistent server. Capture happens only on explicit user action; there is no ambient browsing surveillance, and every AI-mediated summarize or ask call passes through the same CAP governance path as the rest of Yar.

---

## 1. Problem

A person doing research, following a rabbit hole, or trying to remember where they read something has no low-friction way to bring that moment into Yar. Today, capture from the web means copy-paste into a note, a browser bookmark that never gets read again, or a screenshot that loses all its text. `FEATURE-VERIFICATION.md` Section 1.1 already scored this gap precisely: **F59** (capture) and **F50** (annotate, WADM) are both named and full-coverage on paper, but the actual mechanism, a real browser extension with real selector anchoring, does not exist. `06_WADM_ANNOTATION_INTEGRATION.md` built a WADM-inspired preview and capture endpoint as of 2026-05-17, then was marked **superseded** on 2026-07-16 pointing at the product spec and the shipped Tauri client's architecture, neither of which lives in the extension itself. This spec re-grounds that prior work.

The stakes are specific to Yar's audience. A neurodivergent adult loses the thread of a research session the moment a tab closes; the tax of re-finding a half-remembered page or a highlighted sentence is exactly the kind of invisible cognitive load Yar exists to remove. Memex (WorldBrain, MIT license, [github.com/WorldBrain/Memex](https://github.com/WorldBrain/Memex)) and Hypothesis (hypothes.is, BSD-2-Clause client, [github.com/hypothesis/client](https://github.com/hypothesis/client)) both prove the pattern works at scale; neither is a Yar dependency, both are reference points this spec studies directly (Section 3).

**In scope:** capture (whole page, selection), highlight and annotate, offline queueing, handoff to the Yar desktop app, WADM data model and export, consent gates for capture and for AI-mediated summarize and ask.

**Out of scope:** mobile browser capture (native mobile capture is `SPEC-multiplatform-delivery`'s territory, forthcoming); PDF anchoring (documented future work, not this revision); the summarize and ask model itself (owned by `SPEC-petkg-longmemory` and `SPEC-multi-agent`, this spec only defines the extension-side call surface); meeting or video capture (unrelated feature, F69).

---

## 2. Prior art and research (July 2026)

Every claim below was checked directly, not carried over from the superseded 2026-05-17 document.

| System or standard | What it is | License | July 2026 status | Relevance to Yar |
|---|---|---|---|---|
| **Memex** (WorldBrain) | Browser extension: full-text search, annotation, and organization of saved web research | **MIT** | Actively maintained; repository updated within the last two months as of this research pass; funded through Steward Ownership, not VC, so it cannot be sold or gated behind a paid tier | Closest architectural and philosophical sibling: local-first, privacy-focused, account-free. Yar's F59 already carries the internal codename **Cytomark** in reference to this pattern |
| **Hypothesis** (`h` server, `client`) | Web and PDF annotation layer; the reference implementation most people mean when they say "WADM in production" | **BSD-2-Clause** (client and server) | Actively maintained on GitHub; the hosting entity (Annotation Unlimited, PBC, "Anno") raised a $14M seed round in 2022 and continues operating as a public benefit corporation as of 2026 | Reference for selector anchoring robustness (re-anchoring after page edits) and for the annotation JSON shape Yar's WADM export (Section 5) should stay compatible with |
| **W3C Web Annotation Data Model** | The `Annotation = Body + Target + Motivation + Selector + Provenance` standard | **Royalty-free W3C Recommendation** (not source code; a specification) | Reached Recommendation status February 23, 2017; the Working Group has since closed, and further evolution happens in the **W3C Open Annotation Community Group**. No breaking revision has shipped; the model is stable, not abandoned | The foundation of Section 5; Yar does not invent a new annotation schema |
| **MV3 `chrome.sidePanel` API** | Chrome and Chromium's side-panel extension surface | Platform API, not licensed software | Edge ships a compatible `chrome.sidePanel` implementation; Firefox has no equivalent API, it uses `sidebar_action` with a different manifest shape and lifecycle, requiring an adapter; Safari has **no third-party sidebar extension API at all** as of 2026, its app sandbox does not allow persistent third-party UI in the browser chrome | Directly determines Section 6's cross-browser fallback design |
| **Mozilla Readability** (`@mozilla/readability`) | Article-content extraction library (the engine behind Firefox Reader View) | **Apache-2.0** | Actively maintained on GitHub; current releases and open issue tracking as of 2026 | Fallback content extractor (Section 6.4) |
| **Defuddle** (kepano) | HTML-to-Markdown content extractor, built for the Obsidian Web Clipper | **MIT** | Actively released in 2026; positioned explicitly as a more forgiving, more metadata-rich alternative to Readability, with native Markdown output and schema.org metadata extraction | Primary content extractor (Section 6.4); its Markdown-first output matches Yar's own note format directly, no conversion step needed |

**What this confirms:** the annotation standard (WADM) and both reference implementations (Memex, Hypothesis) are mature, licensed cleanly, and stable. The open engineering work is entirely in **how Yar's own extension anchors selectors, queues offline, and hands off to the app**, not in re-deriving the annotation model or re-litigating whether WADM is the right standard.

Sources: [Memex GitHub](https://github.com/WorldBrain/Memex), [Hypothesis client GitHub](https://github.com/hypothesis/client), [Hypothesis `h` GitHub](https://github.com/hypothesis/h), [W3C Web Annotation Data Model](https://www.w3.org/TR/annotation-model/), [W3C Annotation Working Group](https://www.w3.org/annotation/), [chrome.sidePanel API reference](https://developer.chrome.com/docs/extensions/reference/api/sidePanel), [Firefox Manifest V3 migration guide](https://extensionworkshop.com/documentation/develop/manifest-v3-migration-guide/), [Mozilla Readability GitHub](https://github.com/mozilla/readability), [Defuddle GitHub](https://github.com/kepano/defuddle), [Defuddle vs Readability writeup](https://hoangyell.com/defuddle-explained/).

---

## 3. Memex parity checklist

Every Memex capability, mapped to a Yar feature id, a parity target, and the concrete Yar mechanism. This table is the gate against scope creep (Section 10, open question 1).

| Memex capability | Yar feature id | Parity target | Yar mechanism |
|---|---|---|---|
| Capture and save pages | **F59** capture from anywhere (Cytomark) | **Must-have, MVP** | Content script serializes the page (URL, canonical link, title, Defuddle-extracted Markdown) into a `web_capture` op (Section 6.2); queued offline, flushed on app handoff |
| Highlight and annotate | **F50** web annotation layer | **Must-have, MVP** | Content-script selection listener builds a WADM `Annotation` on explicit highlight action (Section 5); anchored via `TextQuoteSelector` plus `TextPositionSelector`, with a Text Fragment URL as a last-resort fallback |
| Organize into spaces | F52 (private local store, existing) plus F67 (PeT) | **Later** (Wave 1 to 2) | Captures land as PeT nodes and brainmap threads inside the app; the extension itself carries no folder or space UI, organization is the app's job, not the extension's |
| Full-text search of saved pages | F10 (saved smart searches, existing), FTS5 app-side | **Later** | The extension does not index locally beyond its small offline queue; search happens app-side over the synced op-log once handed off (Section 6) |
| Summarize | **F66** ask and summarize your captures | **Later** (Wave 2) | Side-panel "Summarize this capture" action calls the paired app's local API, which invokes the Proofreader and PeT recall pipeline; no model runs inside the extension |
| Ask, chat with your library | **F66** | **Later** (Wave 2) | Side-panel chat proxies to the app's local `pet.recall` call (`SPEC-petkg-longmemory` Section 5.1); the extension is a thin UI, never an inference surface |
| Mobile capture | F59 | **Out of scope** for this spec | Mobile capture is a native surface owned by `SPEC-multiplatform-delivery` (forthcoming), not a browser extension; most mobile browsers do not support extensions at all |
| Sync | F68 (cross-device sync, existing) | **Must-have, MVP** | Every capture and annotation is an `OpEnvelope` (Section 6.2); the extension never talks to a sync relay directly, only through the paired local app |
| Integrations (agents, MCP) | F28 (open data connections, MCP) | **Later** | The extension exposes no direct MCP surface; captured content becomes ordinary Yar objects, already reachable through F28's existing app-side MCP surface |

---

## 4. Architecture

### 4.1 Component layout

The extension follows `cytoskeleton/templates/app-extension/` (MV3 plus side panel, one of the four org-locked interface templates per `00_master_architecture.md` Section 4.2 and Section 4.7). Four components:

| Component | Responsibility | Persistence |
|---|---|---|
| **Content script** | Injected on demand (`activeTab`, user gesture only, never `<all_urls>` at install time); listens for a highlight action and a page-capture action; runs Defuddle or Readability extraction; builds the WADM selector | None; hands its result to the background worker immediately |
| **Background service worker** | Builds the `OpEnvelope`, writes it to the offline queue, attempts handoff to the paired app, retries with backoff | `chrome.storage.local` or IndexedDB, never in-memory only (Section 8, MV3 lifecycle risk) |
| **Side panel** | Capture and annotation UI, pairing flow, summarize and ask surface (F66), capture history for the current session | Reads from the offline queue and, once paired, from the app's local API |
| **Popup fallback** (Safari, and any browser without a working side panel) | Same core actions (capture, highlight, view queue) in a smaller surface | Same offline queue |

### 4.2 Selection and highlight anchoring

On an explicit highlight action, the content script builds three selector layers, most-specific first:

1. **`TextQuoteSelector`**: `exact` text plus `prefix` and `suffix` context, the primary anchor, most robust to minor DOM reflow (this is Hypothesis's own primary strategy).
2. **`TextPositionSelector`**: character offsets into the page's extracted text, a fast secondary check.
3. **Text Fragment fallback** (`#:~:text=`): a browser-native fragment directive, used only when the first two fail to re-locate the quote (for example after a substantial page edit), surfaced to the user as an "approximate location" annotation rather than a silent failure.

If none of the three anchors resolve on revisit, the annotation is marked **orphaned**, not deleted; the user sees the original quote and body text with a plain "could not relocate this on the page" notice, consistent with `SPEC-data-sovereignty` P5 (no dark patterns, no silent data loss).

### 4.3 Cross-browser reality

| Browser | Side-panel mechanism | Yar's approach |
|---|---|---|
| **Chrome, Edge** | `chrome.sidePanel` API, shared implementation | Primary target; one codebase |
| **Firefox** | `sidebar_action` manifest key, different shape and lifecycle | Thin adapter layer translates the same UI into Firefox's sidebar model |
| **Safari** | **No third-party sidebar extension API.** Apple's app sandbox treats Safari's chrome as OS-owned, not an extension surface | Popup plus toolbar-button fallback (Section 4.1); no persistent sidebar until Apple ships one, which is not currently planned per Apple's own developer documentation |

### 4.4 Content extraction

| Library | License | Role |
|---|---|---|
| **Defuddle** | **MIT** | Primary extractor; Markdown-first output matches Yar's own note format, richer metadata (schema.org, footnotes, code blocks) than Readability |
| **Mozilla Readability** | **Apache-2.0** | Fallback if Defuddle throws or returns empty content on a given page |

Capture never blocks on extraction failure: if both extractors fail, the raw page title, URL, and a manual "capture full page HTML" option are offered instead of silently dropping the capture.

---

## 5. WADM data model

The extension keeps the WADM shape exactly as `06_WADM_ANNOTATION_INTEGRATION.md` first specified: **Annotation = Body + Target + Motivation + Selector + Provenance**. This spec does not invent a new annotation schema; it anchors the existing one in real DOM selectors and a real op-log.

### 5.1 Controlled motivation vocabulary

Reused verbatim from the WADM standard's own vocabulary, not a Yar-only invention, so exports stay standards-compatible:

| Motivation | Used for |
|---|---|
| `bookmarking` | Whole-page capture with no specific selection (F59) |
| `highlighting` | A highlighted span with no accompanying note |
| `commenting` | A highlighted span with a user note attached |
| `questioning` | A flagged span the user wants to follow up on |
| `tagging` | A span tagged with a term or project reference |
| `linking` | A span explicitly linked to another Yar object |
| `summarizing` | An AI-generated or user-written summary attached to a capture (F66) |

### 5.2 Annotation object

```yaml
# WADM Annotation, as written to the op-log (Section 6.2)
type: Annotation
body:
  type: TextualBody
  value: "This connects to the phenotype-modeling thread from last week."
  format: "text/plain"
target:
  type: Webpage
  source: "https://example.com/article"
  selector:
    - type: TextQuoteSelector
      exact: "graph neural networks can model cell-cell interactions"
      prefix: "recent work shows that "
      suffix: ", which opens new directions"
    - type: TextPositionSelector
      start: 4820
      end: 4878
    - type: FragmentSelector
      value: "#:~:text=graph%20neural%20networks..."
      conformsTo: "https://wicg.github.io/scroll-to-text-fragment/"
motivation: commenting
creator:
  device_id: "device:laptop-01"
  actor_id: "user"
created: "2026-07-19T14:02:00Z"
source_capture_id: "capture:8f2e..."   # links to the web_capture op, if the page was also saved whole
```

### 5.3 Whole-page capture object

```yaml
type: WebCapture
url: "https://example.com/article"
canonical_url: "https://example.com/article?utm_source=..."   # utm-stripped
title: "Graph neural networks for cell-cell interaction modeling"
extracted_markdown: "# Graph neural networks...\n\n..."        # via Defuddle, MIT
extractor: "defuddle"                                          # or "readability" on fallback
captured_at: "2026-07-19T14:00:00Z"
favicon_ref: "blob:sha256-..."
```

### 5.4 Export as WADM JSON-LD (F16)

Every `Annotation` and `WebCapture` op exports as standard WADM JSON-LD, importable by any WADM-consuming tool, not only Yar:

```json
{
  "@context": "http://www.w3.org/ns/anno.jsonld",
  "type": "Annotation",
  "body": { "type": "TextualBody", "value": "...", "format": "text/plain" },
  "target": {
    "source": "https://example.com/article",
    "selector": [
      { "type": "TextQuoteSelector", "exact": "..." },
      { "type": "TextPositionSelector", "start": 4820, "end": 4878 }
    ]
  },
  "motivation": "commenting",
  "creator": "user",
  "created": "2026-07-19T14:02:00Z"
}
```

This satisfies `SPEC-data-sovereignty` P4 (export as a right) and F16 directly: a person's annotations are never locked into Yar's own format.

**Out of scope this revision:** PDF anchoring and DOM-range selectors for non-HTML documents, exactly as `06_WADM_ANNOTATION_INTEGRATION.md` already flagged as future work. PDF capture goes through the desktop app's own document viewer in a later spec, not this browser extension.

---

## 6. App handoff and sync

### 6.1 The coupling requirement

Every capture and annotation is an `OpEnvelope` per `SPEC-sync-protocol` Section 6.2. This spec proposes a one-line, coordinated addendum to that spec's `entity_type` enum: add `web_annotation` and `web_capture`, following the exact precedent `SPEC-petkg-longmemory` set when it added `pet_fact`. No other field in the envelope changes; `device_id`, `actor_id`, `lamport`, `hlc`, `signature`, and `space_id` all apply unchanged. The extension never writes a projection table directly; it only ever emits ops.

### 6.2 Op envelope, extension-specific fields

```yaml
OpEnvelope:
  entity_type: web_annotation   # or web_capture
  op_type: create               # update, delete for later edits or retraction
  object_id: "annotation:8f2e..." # or "capture:..."
  payload: { ... }               # the Annotation or WebCapture body, Section 5
  actor_id: "user"                # never an agent id; extension ops are always person-authored
  device_id: "device:laptop-01"
  space_id: "space:personal"      # single-tenant personal space, per SPEC-sync-protocol Section 8.2
```

### 6.3 The app-handoff decision

Three options were evaluated for how the extension reaches the rest of Yar. This is the concrete decision the task asked for, made once, with a stated rationale.

| Option | Description | Verdict |
|---|---|---|
| **A. Native messaging** | Browser-mediated stdin/stdout IPC to a registered native host | **Not chosen.** Clean security model in principle, but requires a separate native-messaging-host manifest registered per browser (Chrome, Firefox, Edge each need their own JSON manifest with allowed extension IDs, installed into different OS-specific locations on Windows, macOS, and Linux). That installer complexity works against a fully free, no-account, one-click-install product |
| **B. Localhost API on the paired desktop app** | The Tauri desktop app already exposes a local push, pull, ack, and heads API per `SPEC-sync-protocol` Section 6.3; the extension becomes one more client of an interface that already exists | **Chosen.** Reuses infrastructure instead of building a second bridge mechanism; one implementation works across all three target browsers; onboarding is a single pairing step, not a native-host install |
| **C. Extension self-syncs directly to a relay** | The extension embeds its own transport and talks to any-sync (or a future relay) without going through the desktop app at all | **Not chosen.** Duplicates the entire sync, ACL, and key-custody stack `SPEC-sync-protocol` already built for the app; breaks the device-first, single-trust-boundary model in `SPEC-data-sovereignty`; doubles the attack surface for no real gain, since the desktop app is already the trust boundary |

**Recommendation, adopted: Option B, a paired localhost API.** Concretely:

1. **Pairing.** On first install, the extension shows a short pairing code; the person enters it once in the Yar desktop app (or scans a QR code the app displays), mirroring the multi-device pairing pattern `SPEC-data-sovereignty` DS-2 already decided. The app issues a bearer token, stored in `chrome.storage.local`, never in a cookie.
2. **Transport hardening**, because localhost servers carry real, well-documented risk (DNS rebinding, other-origin probing of open ports):
   - The app's local API binds to `127.0.0.1` only, never `0.0.0.0`.
   - Every request must carry the pairing bearer token.
   - The app validates the `Origin` header equals the extension's own origin (`chrome-extension://<id>` or `moz-extension://<id>`) and rejects everything else.
   - The token can be rotated from the app's settings at any time, invalidating the extension's prior token immediately.
3. **Offline queue.** The extension's own `chrome.storage.local` queue (Section 4.1) buffers ops when the paired app is unreachable, closed, or not installed on the current machine. Ops flush in order on the next successful handoff; `op_id` uniqueness (already part of the `OpEnvelope` contract) makes replay idempotent, so a retried flush after a partial failure never double-writes.
4. **No account, ever.** Pairing is device-to-device (extension to the person's own desktop app), not extension-to-cloud-account. This is consistent with "fully free, no subscription" and with Yar never requiring a Yar-hosted account to function.

---

## 7. Consent and privacy

| Principle | Concrete behavior |
|---|---|
| **Capture only on explicit action** | The content script is injected only on a user gesture (`activeTab` permission, a keyboard shortcut, a context-menu "Add to Yar," or a toolbar click); it is never persistently active on every page, and it runs no page-monitoring, analytics, or passive-collection code |
| **No ambient browsing surveillance, ever** | Yar is not a surveillance product. The extension has no history-tracking, no passive tab-scanning, and no telemetry by default. If diagnostics are ever added, they are opt-in only, matching `SPEC-data-sovereignty`'s `share_diagnostics` default of **false** |
| **CAP governs AI processing** | Once a capture is handed off (Section 6), any summarize or ask call (F66) routes through the same CAP-governed pipeline as every other Yar agent call (`SPEC-multi-agent` Section 7). Raw captured page text is classified **Device-local**, exactly like a PeT fact or a raw transcript (`SPEC-petkg-longmemory` Section 9); it is never included in a `Directive` payload, `ExecutionReport`, or `CrossBoundarySignal` bound for an external recipient |
| **Pairing is a consent gate** | "Connect this browser to your Yar app" requires an explicit confirmation dialog explaining what will sync (captures, annotations) and what will not (browsing history, tabs not explicitly captured) |
| **Least-privilege manifest** | The extension requests `activeTab` and `storage`, not broad host permissions like `<all_urls>`, at install time. Broader host access, if ever needed for a specific feature, is requested at the point of use, not bundled into the initial install prompt |
| **Fully free** | No subscription, no paid tier gating capture, annotation, or export. Pairing with the desktop app is the only setup step, and the app itself is free |

---

## 8. Interfaces

### 8.1 Internal messaging

| Path | Mechanism | Purpose |
|---|---|---|
| Content script to background | `chrome.runtime.sendMessage` | Deliver a built `OpEnvelope` payload after a capture or highlight action |
| Background to side panel | `chrome.runtime.connect` (long-lived port) | Push queue state, pairing status, summarize and ask responses |
| Background to paired app | HTTPS over loopback (Section 6.3) | `POST /ext/v1/pair`, `POST /ext/v1/ops`, `GET /ext/v1/health`, `POST /ext/v1/recall` |

### 8.2 Local API surface (app-side, consumed by the extension)

| Endpoint | Method | Purpose | Auth |
|---|---|---|---|
| `/ext/v1/pair` | POST | Exchange a pairing code for a bearer token | Pairing code (one-time) |
| `/ext/v1/ops` | POST | Push a batch of `OpEnvelope`s | Bearer token, Origin check |
| `/ext/v1/health` | GET | Liveness check, used by the offline-queue retry loop | Bearer token |
| `/ext/v1/recall` | POST | Proxy to `pet.recall` for the side-panel ask and summarize surface (F66) | Bearer token |

### 8.3 Manifest CSP

The extension's `manifest.json` sets a strict **Content Security Policy** (CSP), the browser manifest directive, not to be confused with the org's Cytonome Sensor Protocol: `script-src 'self'; object-src 'none'`, no remote code execution, no inline scripts, consistent with MV3's own baseline requirement and with Cytognosis's org-wide security posture (`00_master_architecture.md` Section 7.6, pre-commit `detect-secrets` and license-check gates apply to this repo like every other generated package).

---

## 9. Risks

| Risk | Mitigation |
|---|---|
| **Selector drift**: a page's content changes after a highlight, breaking the anchor | Three-layer selector (Section 4.2); orphaned annotations are surfaced, never silently dropped |
| **Cross-browser side-panel fragmentation**, Safari has no sidebar extension API | Popup and toolbar-button fallback (Section 4.3); feature-detect and degrade, do not block Chrome and Firefox launch on Safari parity |
| **MV3 service-worker lifecycle**: the background worker can be killed and restarted by the browser at any time, losing in-memory state | The offline queue persists to `chrome.storage.local`, never held only in memory (Section 4.1) |
| **Localhost API attack surface**: DNS rebinding, a malicious page probing open loopback ports | Loopback-only bind, bearer token, Origin-header validation (Section 6.3) |
| **Extraction failure** on JavaScript-heavy or paywalled sites | Defuddle primary, Mozilla Readability fallback, manual full-page-HTML capture as a last resort; capture never blocks on extraction failure |
| **License drift** if a bundled library changes terms | Every library in this spec carries its license inline (Sections 2, 4.4); the org's `license-check` pre-commit gate (`00_master_architecture.md` Section 7.6) applies to this repo like every other generated package |
| **Scope creep toward full Memex or Hypothesis parity** | Section 3's parity checklist is the explicit gate; "later" and "out of scope" rows are not silently pulled forward |
| **Native-host installer complexity**, had Option A been chosen | Avoided entirely by choosing Option B (Section 6.3) |

---

## 10. Test plan

| Test | What it verifies |
|---|---|
| Selector anchoring regression | A highlight re-anchors correctly across a page reload and a minor DOM change; falls back to Text Fragment; marks orphaned only when all three layers fail |
| Offline queue integrity | Captures made while the paired app is closed queue locally and flush correctly once the app is reachable, with no duplicate ops (`op_id` idempotency) |
| Cross-browser side-panel parity | Chrome and Edge `sidePanel`, Firefox `sidebar_action` adapter, and the Safari popup fallback all expose the same capture and annotate actions |
| WADM export round-trip | An exported JSON-LD annotation re-imports correctly into a fresh Yar instance and validates against the standard WADM JSON-LD context |
| Pairing and token security | A request without a valid bearer token, or from a non-Yar `Origin`, is rejected by the local API; the loopback port is unreachable from any non-`127.0.0.1` bind |
| Consent gate audit | No network call and no content-script injection occurs without an explicit user gesture; verified by a scripted audit of every `chrome.*` permission use |
| CAP boundary test | A capture containing a crisis-adjacent or diagnosis-shaped sentence is stored device-locally as usual, but the same `CapLiteGuard` categories that gate conversation-time input (`SPEC-multi-agent` Section 7.4) also gate any summarize or ask call that would surface it |
| License compliance | The `license-check` CI gate covers every bundled JavaScript dependency (Defuddle MIT, Mozilla Readability Apache-2.0, and any future addition), consistent with the org-wide pre-commit standard |

---

## 11. Open questions with recommendations

Each item states a recommendation; none are left as a bare menu.

| # | Question | Recommendation |
|---|---|---|
| **Q1** | Native messaging vs. localhost API vs. self-sync (the app-handoff decision) | **Resolved in this revision: localhost API** (Section 6.3), for the installer-simplicity and infrastructure-reuse reasons stated there. Revisit only if browser vendors tighten loopback access further, for example if Chrome's Private Network Access restrictions eventually block extension-to-loopback requests outright |
| **Q2** | PDF annotation and anchoring | **Deferred**, matching the original 2026-05-17 WADM plan's own "still future work" line. PDF capture belongs to the desktop app's own document viewer in a later spec, not this browser extension |
| **Q3** | Should the extension carry its own local full-text index before handoff, for fully offline search? | **No, not for MVP.** Keep the extension thin; full-text search is app-side FTS5 over the synced op-log, mirroring PeT's own "one engine, not two" convergence philosophy (`SPEC-petkg-longmemory` Section 7) |
| **Q4** | Safari support timeline, given the sidebar-extension gap | **Ship the popup-based fallback now** (Section 4.3); revisit a native sidebar integration only if Apple publishes a public sidebar extension API, which is not currently planned per Apple's own developer documentation |
| **Q5** | Should whole-page capture mint a Yar-only WADM motivation term? | **No.** Reuse the existing WADM vocabulary term `bookmarking` (Section 5.1) rather than inventing a Yar-specific term, preserving standards fidelity for F16 export |
| **Q6** | Should `SPEC-sync-protocol`'s `entity_type` enum formally add `web_annotation` and `web_capture` now? | **Yes**, as a one-line coordinated addendum with that spec's owner, following the exact precedent `SPEC-petkg-longmemory` set for `pet_fact` (Section 6.1) |
| **Q7** | Content extraction library choice: Defuddle, Readability, or both? | **Defuddle primary, Readability fallback** (Section 4.4), mirroring the same dual-extractor approach the Obsidian Web Clipper already ships in production |
| **Q8** | Should the extension ever request broad host permissions (`<all_urls>`) for a future feature? | **Avoid if possible.** Request expanded host access only at the point of use for a specific, named feature, never bundled into the initial install prompt (Section 7); revisit only if a concrete Wave 2 feature cannot function under `activeTab` alone |

---

## 12. Cross-references

- `06_WADM_ANNOTATION_INTEGRATION.md`, superseded 2026-07-16, the WADM foundation this spec re-grounds: Annotation as Body, Target, Motivation, Selector, Provenance; the controlled motivation vocabulary (Section 5.1) and the 2026-05-17 implementation status are both carried forward here.
- `00_master_architecture.md`, `01_refactor_brief.md`, the org-wide locked interface templates; the MV3 plus side-panel extension template (`cytoskeleton/templates/app-extension/`) this spec builds on.
- `SPEC-sync-protocol.md`, the `OpEnvelope` contract every capture and annotation rides; Section 6.1 of this spec proposes the coordinated `entity_type` addendum.
- `SPEC-petkg-longmemory.md`, the `pet.recall` API the side-panel ask and summarize surface (F66) calls; the precedent for extending the op-log's entity types cleanly.
- `SPEC-multi-agent.md`, the CAP Directive envelope and `CapLiteGuard` categories that gate any AI-mediated processing of captured content (Section 7).
- `SPEC-data-sovereignty.md`, the device-first trust boundary, consent-gate pattern, and export-as-a-right principle (F16) this spec's Sections 5.4 and 7 satisfy directly.
- `SPECS-INVENTORY.md`, `FEATURE-VERIFICATION.md` Section 1.1, the Memex capability sub-mapping this spec's Section 3 formalizes into a concrete checklist.

---

<details>
<summary><strong>Glossary</strong></summary>

- **WADM (Web Annotation Data Model):** The W3C standard this spec anchors: Annotation as Body, Target, Motivation, Selector, Provenance. A specification, not a library.
- **Cytomark:** Internal codename for F59, capture from anywhere, named after the Memex-inspired capture pattern.
- **TextQuoteSelector, TextPositionSelector:** WADM selector types anchoring an annotation to exact text and character offsets, respectively.
- **Text Fragment:** A browser-native URL fragment (`#:~:text=`) used as a last-resort anchor when WADM selectors fail to re-locate a quote.
- **MV3:** Manifest V3, the current browser extension platform generation across Chrome, Edge, and Firefox.
- **Defuddle:** MIT-licensed HTML-to-Markdown content extractor, the primary extraction library (Section 4.4).
- **Paired localhost API:** The bearer-token-authenticated, loopback-only HTTP surface the Yar desktop app exposes for the extension to hand off ops (Section 6.3).
- **OpEnvelope:** The shared op-log envelope every Yar write, including web annotations and captures, rides (`SPEC-sync-protocol` Section 6.2).

</details>

# Cytonome Track — Navigator: On-Device + Causal AI, ND App, PBC / Dual Entity, YC

**Date:** 2026-06-03 · Stage 5, Track 4 (p2) · Consolidated from cytomem corpus, repos `cytoplex` + `Yar` + `docs/cytonome`, and X-Labs project files.
**Reading time:** ~12 min. **If you only read one thing:** see §3, Priority 1 — Yar needs real users before Demo Day; the MVP runs, the user pipeline does not yet. Ship the TestFlight beta first.

---

## BLUF

Cytonome is the Navigator pillar: on-device causal AI (Cytoplex), a privacy-first cognitive companion for neurodivergent adults (Yar), and the PBC commercialization arm through which Cytoscope soft-sensor revenue flows. Cytoplex v0.1 is production-candidate with 120+ conformance tests; Yar has a working MVP (243 passing tests, on-device Gemma 4); the YC Summer 2026 application positions Yar as a for-profit consumer app backed by Foundation science. The critical gap is zero production users: the engine runs, the user pipeline does not.

---

## 1. Component Map

| Component | What It Is | Repo / Location | Status |
|---|---|---|---|
| **Cytoplex** | Controller-Authority Protocol (CAP) — causal AI safety and governance layer for on-device agents | `cytoplex` | v0.1 production-candidate; v1 architecture spec complete, runtime partially scaffolded |
| **Yar** | Privacy-first cognitive companion app for ND adults: voice capture, communication coaching, sensor integration | `Yar`, `docs/cytonome/yar/` | Working MVP; TestFlight beta in prep |
| **Yar Mobile** | Flutter app: voice capture, gentle planning, persona animation | `Yar/apps/mobile/` | Hackathon MVP shipped |
| **Yar Browser Extension (Cytomark)** | MV3 Chrome/Firefox: contextual capture, annotation, social interpretation | planned | Not started |
| **Yar Desktop** | Tauri v2: system tray, vocal biomarker viz | planned | Not started |
| **USAP (Universal Sensor Adapter Protocol)** | MCP-for-sensors: pluggable physiological sensor streams, LinkML schema-backed | `docs/cytonome/yar/sensors/` + `cytos` schemas | v0.1 design spec; Cytos schemas present |
| **PBC subsidiary** | For-profit arm for regulated products and continuous-tracking datasets; not yet formed | Legal (M30 deliverable) | Not formed; pending Gate 1 / YC outcome |

---

## 2. Cytoplex (CAP) — Current State

### Architecture
Cytoplex is a deterministic runtime governance protocol. It intercepts every model call, validates proposed actions against typed schemas, hard-blocks diagnostic claims, treatment advice, and unconfirmed data writes, and produces cryptographically signed audit trails. The design is dual-tier (Local PEP at the edge, Central Control Plane in the cloud/backend) with three planes (Control, Execution, Observability).

### Repo evidence
- 7-spec documentation suite (`CAP_00` through `CAP_07`), fully written.
- `runtime/` module: `LocalPEP`, `EdgePEP`, `MobileLocalPEP`, `AttestedLocalPEP`, `SupervisorGateway`, `SessionRouter`, `WorkflowEngine`, `PrivacyPDP`, and more.
- Conformance runner: 33 v0.1 fixture checks pass; v1 scaffold conformance gates V1-C01 through V1-C15.
- Security hardening suite: detached-JWS, DSSE, tamper rejection, revoked-key refusal.
- Profiles: `CAPMed` (clinical domain), `CAPSWE` (software engineering), with inheritance system.
- LinkML schemas: `schemas/cap.yaml`, `schemas/core.yaml`, domain extensions.

### v0.1 vs v1 gap
The v0.1 production-candidate is real and used in Yar today. The v1 target adds a decomposed Central Control Plane, production SPIFFE SVID workload identity, external multi-organization interoperability, real platform attestation verifiers, and production KMS/HSM integration. None of those are blocking for Yar's consumer launch.

### Naming note
All internal code uses `cytoplex` as the package name. Strategy docs refer to CAP (Controller-Authority Protocol) as the protocol name. Never use "Substrate" for this layer.

---

## 3. Yar — Current State

### Identity
Yar (Your AI Representative) is a personalized cognitive companion built by neurodivergent minds, for everyone whose tools were not designed for how their brain works. It is not a therapist, not a productivity system, not a diagnostic tool. It is the companion that reduces the invisible tax of existing in systems not designed for ND cognition.

### Three capability tiers

| Tier | What It Does | Status |
|---|---|---|
| **1: Friction Reduction** | Voice/text brain-dump to structured typed objects (tasks, notes, ideas); browser-aware contextual capture; gentle planning | Working MVP, 243 passing tests |
| **2: Communication Coaching** | Bidirectional ND-NT translation; emotional aftercare after hard conversations; pattern surfacing | Next (batch priority) |
| **3: Relational Depth** | Longitudinal vocal biomarker tracking; persistent relational context; mood-context persona switching | Later; gated on user trust |

### Target populations

| Segment | Core need Yar addresses |
|---|---|
| ADHD adults | Thought loss before capture; executive dysfunction; shame spirals from failed systems |
| Autistic adults | Communication mismatch; social interpretation load; interface unpredictability |
| Twice-exceptional (2e) | Deep knowledge, no organization; semantic retrieval across domains |
| Late-diagnosed adults | Decades of half-working coping strategies; reflection without judgment |
| ND researchers and students | In-flow context capture; hyperfocus without loss |

### Product ecosystem

| Product | Interface | Status |
|---|---|---|
| Yar backend | FastAPI + CAP + Anytype adapter + model routing | MVP complete |
| Yar Mobile | Flutter (iOS/Android): voice capture, persona animation | Hackathon MVP |
| Yar Browser Extension (Cytomark) | MV3 Chrome/Firefox | Planned (highest-priority next interface) |
| Yar Desktop | Tauri v2: system tray, sidecar Yar + Ollama | Planned |
| Yar Web | Static shell: quick capture + search | Basic |

### Tech stack
Flutter (mobile), FastAPI (backend), on-device Gemma 4 via LiteRT and Ollama, SQLite local storage, optional Anytype sync for personal KG, Cytoplex safety protocol on every model call, LinkML-style YAML schemas for typed AI output, W3C Web Annotation standard for context anchoring.

### Design principles (non-negotiable)
No shame architecture: no streaks, no red overdue, no gamification that punishes. Identity-safe: communication coaching preserves user intent; never a masking engine. Frictionless: support where cognition happens (browser, voice). Privacy by architecture: on-device AI, local storage, not a policy promise.

### Multi-persona system (Phase 6)
Adaptive persona (Coach, Buddy, Guardian, Mom, Partner, Mentor) that auto-tunes via mood-context model: `(mood_state, time_of_day, activity_type, energy_level) → preferred_persona`. ElevenLabs per-persona voice. Context-aware persona switching without user configuration overhead.

### Sensor integration (Phase 7, USAP)
Universal Sensor Adapter Protocol: a pluggable, schema-backed MCP-for-sensors. Sensor classes include wearables (Oura, Apple Watch), smartphone sensors (AWARE), self-report instruments (PHQ-9, GAD-7), CGM (Dexcom), EEG (Muse), and Cytoscope biosensors when available. All observations align to SOSA/SSN, IEEE 1752.1, HL7 FHIR R5, and AWARE via Cytos LinkML schema crosswalks. The strategic sequence: win daily habit via Tier 1/2 utility, then layer soft sensors onto an already-retained app. This inverts the abandonment curve that kills health and wearable apps.

---

## 4. YC Application — State

### Strategic framing
The Summer 2026 YC application positions Yar as a for-profit consumer app (category: Consumer / AI app), with Cytognosis Foundation as the upstream nonprofit science platform. Deliberate pivot from prior two applications (Winter 2025, Spring 2026) that pitched the full platform as a nonprofit. Rationale: YC nonprofit track is narrow; Yar is shippable now; for-profit is where the odds favor this work.

### Company structure for YC
Yar's operating company does not yet exist. Will incorporate as a Delaware C-corp via YC's standard path if accepted. The Foundation holds all pre-Gate 1 IP; at PBC activation, the PBC receives a royalty-bearing perpetual non-exclusive license.

### Progress claimed in application
- Working MVP: Product Milestone 1 complete (end-to-end mobile voice loop: capture, on-device Gemma 4, Cytoplex-Lite safety gate, confirmed KG write).
- 243 passing automated tests; 93 on the safety layer; zero lint violations.
- No production users yet.
- TestFlight beta target: 4 to 6 weeks from application date.
- Demo Day target: 1,000+ retained users, communication translator shipped, first paid conversions, cofounder onboarded.

### Revenue model
Freemium subscription at $12/month; free tier: local capture and structure; paid tier: cross-device sync, communication translator, deeper KG integration, longitudinal insights. Later: B2B tier for neurodiversity employer support and university disability offices.

### Prior applications
Winter 2025 (platform as nonprofit, rejected), Spring 2026 (platform as nonprofit, rejected). The YC archive contains both: `archive-unsorted/Cytognosis/applications/YC/`.

---

## 5. PBC / Dual-Entity Pathway

### Structure
Cytognosis Foundation (501c3) is the permanent parent. The PBC (public benefit corporation) subsidiary activates at Gate 1, which is a board ratification event triggered by: sufficient Foundation asset base, PAC sign-off, Bylaws Article VI compliance, and counsel review (Duane Valz). The PBC holds the Foundation-controlled governance majority; VC investors hold preferred non-control positions.

### How the PBC connects to Cytonome
The PBC's commercial operations are: continuous individual tracking datasets (personalized navigation engine, cohort-trained), Cytoscope wearable hardware (v1+), and the Cytonome regulated product. Yar's consumer subscription revenue, once the operating company is incorporated and at scale, flows through the PBC arm rather than the Foundation. The Foundation's perpetual IP license to the PBC covers all pre-Gate 1 Foundation-funded work (Apache 2.0 for code, CC BY 4.0 for docs, OpenRAIL-M for responsible-AI models).

### How Cytoscope commercializes through Cytonome
Cytoscope (the biosensor / Psychoscope, NSF X-Labs track) produces hardware and soft sensors. Those sensors feed the USAP layer in Yar as pluggable sensor plugins. Revenue from Cytoscope hardware and the continuous-tracking data services it enables flows through the PBC commercial arm, not the Foundation. The Cytonome track is therefore the commercial gateway for Cytoscope outputs: Cytoscope builds the sensors, Cytonome/Yar provides the software layer users interact with, and the PBC monetizes the combined system.

### Consistency with openness policy
All pre-Gate 1 artifacts are Apache 2.0 / CC BY 4.0 / CC0 by default, fully open. Post-Gate 1, the bifurcation activates under the 36-month rule: the Foundation track stays open (Cytoverse map releases, disease-axis discoveries, cross-modal alignment models from public data); the PBC track holds defined proprietary components (continuous individual tracking datasets, personalized navigation engine, Cytoscope wearable v1+). The PBC pays a royalty stream back to the Foundation; aggregated, differentially-private insights flow from PBC to Foundation open track. The non-revocable perpetual license means the Foundation cannot lose control of the open mission regardless of PBC commercial decisions. The YC operating company structure (for Yar) is consistent with this: it is the PBC in consumer-product form, with the Foundation as IP licensor and governance majority holder.

---

## 6. Top-3 Priorities

| Priority | Action | Urgency | Owner |
|---|---|---|---|
| **P1: Yar user pipeline** | Ship TestFlight beta to ND design-partner community; instrument retention; target 50 to 100 real users before any investor conversation. | Now (no-outreach; communities already warm) | Shahin |
| **P2: YC application submission** | Review and finalize the Summer 2026 application before the batch deadline; record the 60-second demo video (product milestone 1 is complete; just needs video). | Within 2 weeks | Shahin |
| **P3: PBC / Yar operating-company formation** | If YC acceptance comes, incorporate Delaware C-corp immediately via YC's standard path; consult Duane Valz on IP-license terms between Foundation and new entity. | Gated on YC outcome; counsel loop needed | Shahin + Duane Valz |

---

## 7. Gaps

| Gap | Impact | Notes |
|---|---|---|
| Zero production users | Blocks all retention, conversion, and investor-readiness metrics | P1 above |
| Cofounder not found | YC specifically asks about this; ND + consumer/design/growth background needed | Active search; warm community available |
| Yar operating entity does not exist | Cannot receive YC SAFE without a C-corp | Gated on YC outcome |
| PBC charter (`SI-PBC-Charter`) not drafted | IP licensing terms undefined until M30 | Duane Valz review required pre-activation |
| Browser extension (Cytomark) not started | Likely most-used interface for ND researchers; deferred | Phase 3 roadmap |
| Cytoplex v1 runtime incomplete | v0.1 is adequate for consumer Yar; v1 completeness matters for regulated/clinical use | Low urgency for current launch |
| USAP physical sensor integration | Wearable data flowing into Yar (Oura, Apple Watch) not yet live | Phase 7; schema-ready but no adapters shipped |

---

## 8. Duplicate Documents Needing Canonical-Home Assignment

| Document cluster | Copies identified | Canonical home (recommended) | Others |
|---|---|---|---|
| YC applications | `Projects/X-Labs/02-applications/yc/Y Combinator Application (Summer 2026).md` (active); `archive-strategy/Applications/YC/Y Combinator Application (Spring 2026).md`; `archive-unsorted/Cytognosis/applications/YC/Apply to Y Combinator.md` + `.pdf` + `(1).pdf` | **`Projects/X-Labs/02-applications/yc/`** (active Summer 2026 draft) | Spring 2026 and older = historical archive; keep indexed, do not edit |
| Cytoplex implementation alignment | `cytoplex/docs/v1_baseline/11_implementation_alignment.md`; `docs/cytonome/yar/cytoplex/v1-baseline/11_implementation_alignment.md` | **`docs/cytonome/yar/cytoplex/v1-baseline/`** (the `cytoplex` repo copy has a `moved_to` stub pointing here) | `cytoplex` repo copy is a redirect stub only |
| Cytonome master reference | Referenced in product-implementation.md as `01_cytonome_master_reference.md` in an old Gemini-brain path; not found in current corpus | **`docs/cytonome/`** — needs locating or recreating | Possibly in agent-antigravity scratchpads; do not rely on those paths |
| CAP spec documents | Full `docs/CAP_00–07` suite in `cytoplex/docs/`; a copy of `11_implementation_alignment.md` exists in `docs/cytonome/yar/cytoplex/v1-baseline/` | **`cytoplex/docs/`** for CAP spec; **`docs/cytonome/yar/cytoplex/`** for cross-linked consolidations | |

---

## 9. Cross-Track Links

| Link | Detail |
|---|---|
| **Cytonome → Cytoscope** | USAP provides the sensor-ingestion layer; Cytoscope hardware ships as a USAP plugin; PBC monetizes the combined system (see §5) |
| **Cytonome → Toolchain** | Cytoplex schemas use LinkML (same as `cytoskeleton`); USAP sensor schemas live in `cytos/schemas/domains/sensor/`; IGoR ontology asks map to these schemas |
| **Cytonome → Funding** | YC = Yar consumer path; OneMind Accelerator (Yar PBC), Techstars AI Health (PBC phase), EA LTFF / Coefficient = Foundation bridge; IGoR is Cytoverse + Toolchain, not Cytonome |

---

## 10. Timeline Anchors

| Date | Event | Cytonome relevance |
|---|---|---|
| Now | TestFlight beta prep | P1 |
| ~4–6 weeks from application | TestFlight launch | First real users |
| YC batch (Summer 2026) | App Store launch; communication translator | If accepted |
| Month 3–12 post-batch | Grow to tens of thousands of users; B2B pilot | If accepted |
| Gate 1 (~M30 from present) | PBC activation; IP-license terms ratified | Foundation → PBC transition |
| Oct 1, 2026 | Runway cliff | Yar subscription revenue not yet material; bridge grants must cover |

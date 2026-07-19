# Canonical Edits Spec (approved decisions A-G)

> Authored 2026-07-18 after Shahin approved decisions A through G. This is the single source for the exact wording Phases 1 and 2 apply across the canonical pillar. Apply verbatim; do not paraphrase the identity block.

## 1. Canonical identity block (D-A: ND adults only; D-F: fully free)

Use this block wherever Yar is introduced (product spec, steering, README, CLAUDE.md). No em dashes; active voice.

> **Yar (Your AI Representative)** is a local-first, voice-aware, AI-native cognitive companion for neurodivergent adults, built by and for neurodivergent people. It is the consumer-facing expression of Cytognosis's Cytonome navigator layer. Yar accepts messy input (voice, text, web context), uses on-device AI to structure it into typed objects in a personal knowledge graph, and helps the user execute, manage time, and stay self-aware.
>
> **Who it is for:** neurodivergent adults (ADHD, autistic, AuDHD, and adjacent) for whom continuous tracking and multi-app context-switching fail. Yar is not built for clinicians or developers as target users.
>
> **Why it exists:** to get through a day, a neurodivergent adult stitches together seven or eight apps, and the context-switching between them is itself the executive-function problem each claims to solve. Yar replaces that stack with one companion that keeps data on-device, adapts to the user's brain, and is fully free.
>
> **Differentiator:** on-device AI, a hard safety boundary (CAP) that never diagnoses or treats, emotional-regulation depth that no competitor covers, and the branching-brainmap companion as the flagship.
>
> **What Yar is not:** not a therapist, not a diagnostic tool, not a medical device, not a surveillance product, and not a subscription.

**Personas to remove:** delete "Clinician" and "Developer" as target personas from `steering/yar-product.md`; keep only neurodivergent-adult personas. Keep `inclusion: always`.

**Business model wording (D-F):** replace every instance of "$12/mo", "freemium", or sync/translator paywall framing with "fully free, no subscription, indefinitely." The strategic asset is the userbase for when the sensor is ready.

## 2. Sensor protocol name (D-C)

- Canonical name: **CSP (Cytonome Sensor Protocol)**.
- **USAP** (Universal Sensor Adapter Protocol) and **UBAP** (Universal Biosensor Adapter Protocol) are deprecated aliases. On first mention in any doc that still uses them, add: "formerly USAP/UBAP, now standardized as CSP," then use CSP throughout.

## 3. Unique-features count (D-B)

Retire the "28 Cytognosis-unique features" claim everywhere. Replace with: **"20 features anchored to 8 named, defensible capability clusters, plus 21 additional features with no direct competitor equivalent."** Where a single number is needed externally, say "over 40 features with no direct competitor equivalent."

## 4. New features (D-E: add advocacy + personal compass now)

Add two features to the canonical taxonomy, bringing it to **64 features** (SCI 5, AEF 16; the other domains unchanged). Both are additive gap-closers with no competitor equivalent; neither is in the v4 comp-scoring matrix yet (note this where the matrix is cited).

| ID | Name | Domain / cluster | Status | Gated | Description |
|---|---|---|---|---|---|
| **F63** | Invisible-disability advocacy mode | SCI / Communication coaching | planned | yes | During depressive or anxious periods, Yar helps explain your situation, needs, and what to expect to partners or colleagues, on your terms, so you are not misunderstood when you cannot perform as usual. Closes the founder-narrative "advocates for you" gap. |
| **F64** | Personal compass (gentle goals) | AEF / Day planning & flexible plans | planned | no | Non-pressuring direction: gentle goals you steer by, never a performance bar. Reframes the Leantime "Goals" pattern into Yar's no-shame model. |

Defer (do not add now): rich-media-as-first-class-objects (CTO) and meeting-mode diarization (AEF/CTO). Keep them listed as known gaps.

## 5. Cluster layer (D adopts the 3-level hierarchy)

Adopt the 19-cluster middle layer from `research/features.json` and `research/FEATURE-HIERARCHY.md` as canonical. In `YAR_FEATURE_CATALOG.md` and `research/yar-unified-feature-comparison-v4.md`, add a short "Hierarchy" section that points to `features.json` as the machine-readable source and keeps the per-feature rows intact. Counts after this spec: **6 domains, 19 clusters, 64 features (15+1 AEF, 18 ERM, 4+1 SCI, 2 SPR, 16 CTO, 7 SMI)**.

## 6. Files to edit (Phase 1-2 application map)

| File | Edits |
|---|---|
| `yar-product-spec.md` | single frontmatter block; identity block (S1); CSP (S2); retire 28 (S3); free model (S1/D-F); add F63/F64 to pillar list; hierarchy pointer (S5) |
| `steering/yar-product.md` | rewrite to ND-only identity; drop Clinician/Developer; free model; keep inclusion: always |
| `YAR_FEATURE_CATALOG.md` | fix frontmatter date; add F63/F64; hierarchy section; CSP; count 62 to 64 |
| `research/yar-unified-feature-comparison-v4.md` | reconcile 28 to 20+21; note F63/F64 as post-matrix additions; CSP; cluster-layer note |
| `README.md`, `CLAUDE.md` (pillar) | identity block; counts; pointers |

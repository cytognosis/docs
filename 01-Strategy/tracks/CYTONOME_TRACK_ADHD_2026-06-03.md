# Cytonome Track — ADHD Summary

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: leadership
> **Tags**: `strategy`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)

**Date:** 2026-06-03 · Stage 5, Track 4 (p2)
**Reading time:** ~4 min.

---

## BLUF

Yar (cognitive companion for ND adults) has a working MVP with 243 tests passing and zero production users. Ship the TestFlight beta first — everything else (YC, PBC, investors) depends on having real users. Cytoplex (on-device AI safety layer) is production-ready at v0.1. The PBC / for-profit arm does not exist yet and activates only after YC outcome or Gate 1.

**If you only read one thing:** P1 is get 50 real users into TestFlight this week.

---

## Done

- [x] Cytoplex v0.1 production-candidate shipped (33 fixture conformance tests, 93 safety tests in Yar)
- [x] Yar MVP complete: voice capture, on-device Gemma 4, CAP safety gate, KG write (243 tests passing, zero lint)
- [x] Yar Flutter mobile app (hackathon MVP)
- [x] YC Summer 2026 application drafted (Yar as for-profit consumer app)
- [x] Universal Sensor Adapter Protocol (USAP) design spec written
- [x] LinkML sensor schemas in `cytos` (SOSA/SSN, FHIR, AWARE-aligned)
- [x] PBC structure and IP licensing terms documented (`23_open_science_and_ip.md`, `20_organization_helix.md`)

---

## Top-3 Priorities

| # | Action | How | Outreach needed? |
|---|---|---|---|
| **P1** | Launch TestFlight beta to ND design-partner community | Build + distribute; communities are warm | No outreach — existing community |
| **P2** | Finalize and submit YC Summer 2026 application | Record 60-sec demo video (MVP already works); submit | No — draft is ready |
| **P3** | If YC accepts: incorporate Yar C-corp and trigger IP-license discussion with Duane Valz | YC standard incorporation path | Yes — Duane Valz (counsel) |

---

## What Is What

| Name | What it does |
|---|---|
| **Cytoplex** | Safety layer: sits in front of every AI model call; blocks diagnosis, treatment advice, unconfirmed writes |
| **Yar** | The app: voice brain-dump, communication coach, sensor hub — for ADHD/autistic/ND adults |
| **CAP** | Controller-Authority Protocol: the spec Cytoplex implements |
| **USAP** | Universal Sensor Adapter Protocol: MCP-for-sensors, lets Oura/Apple Watch/Cytoscope all plug into Yar |
| **PBC** | The for-profit subsidiary Cytognosis Foundation will spin up at Gate 1 (or via YC); holds commercial IP |

---

## Yar Capability Tiers

| Tier | What | Status |
|---|---|---|
| 1: Capture | Voice/text to structured typed objects; gentle planning | Working today |
| 2: Translate | ND ↔ NT communication coaching; emotional aftercare | Next (YC batch priority) |
| 3: Companion | Longitudinal vocal biomarkers; mood-context persona | Later; gated on user trust |

---

## PBC Pathway (one paragraph)

The Foundation licenses all pre-Gate 1 IP (Apache 2.0 / CC BY 4.0) to the PBC on a royalty-bearing, perpetual, non-exclusive basis. The PBC holds the Foundation-controlled governance majority; VC investors get preferred non-control stakes. Cytoscope hard-sensors and continuous-tracking datasets belong to the PBC track post-Gate 1; Yar's consumer subscriptions flow through the PBC rather than the Foundation. The Foundation's open mission cannot be rescinded: the PBC license is non-revocable, and the Foundation retains rights to all Foundation-funded IP in the open track regardless of PBC commercial decisions. Gate 1 activates on board ratification, PAC sign-off, and Duane Valz counsel review — not before.

---

## Cytoscope Connects Here

Cytoscope (NSF X-Labs biosensor track) produces sensors. Those sensors plug into Yar via USAP as first-party plugins. Revenue from Cytoscope hardware and continuous-tracking services flows through the PBC commercial arm. Cytonome = the software layer; Cytoscope = the hardware layer; PBC = the commercial entity for both.

---

## Gaps

| Gap | What to do |
|---|---|
| Zero production users | Launch TestFlight (P1) |
| No cofounder | Active search; need ND + consumer/design/growth background |
| Yar entity not incorporated | Gated on YC or Gate 1 |
| PBC charter not drafted | Duane Valz; M30 deliverable |
| Browser extension (Cytomark) not built | Phase 3; likely most-used ND interface |
| USAP wearable adapters not shipped | Phase 7; schemas ready, runtime adapters not |

---

## Duplicate Docs Needing Canonical Home

| Cluster | Keep | Archive |
|---|---|---|
| YC applications | `Projects/X-Labs/02-applications/yc/Y Combinator Application (Summer 2026).md` | Spring 2026 + older in `archive-strategy` / `archive-unsorted` |
| Cytoplex implementation alignment | `docs/cytonome/yar/cytoplex/v1-baseline/11_implementation_alignment.md` | `cytoplex/docs/v1_baseline/11_implementation_alignment.md` (redirect stub) |
| Cytonome master reference | `docs/cytonome/` (needs locating or rebuilding; old path in agent-antigravity scratchpads is unreliable) | — |

---

## Key Dates

| Date | What |
|---|---|
| Now | TestFlight beta |
| ~4–6 weeks | TestFlight users |
| YC batch (Summer 2026) | App Store + communication translator |
| Gate 1 (~M30) | PBC activation |
| Oct 1, 2026 | Runway cliff — Yar revenue not yet material; bridge grants must cover |

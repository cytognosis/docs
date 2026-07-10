# Cytoscope Track — ADHD Variant

**Date:** 2026-06-03 · Stage 5, Track 5 (p2)
**Reading time:** ~4 min.

---

## BLUF

Psychoscope is the sensor. NSF X-Labs Phase 0 funds it (up to $1.5M; due **Jul 13**). One hard blocker: Shahin's dual US/Iran citizenship may bar him from Senior/Key Personnel designation. Resolve this in writing before submitting.

**If you only read one thing: contact NSF OCRSSP (researchsecurity@nsf.gov) today to request a written interpretation on the dual-citizenship question. Everything else is drafted and ready.**

---

## Done (check these off)

- [x] Phase 0 proposal drafted (8 pages): `07-nsf-xlabs/NSF_XLabs_Phase0_Draft_v1.md`
- [x] NSF X-Labs source materials processed
- [x] Transdiagnostic biotype atlas assembled (14 disorders, 3 scales)
- [x] Competitive technology landscape surveyed (EEG, OPM-MEG, fNIRS, Kernel, Openwater)
- [x] Topic 2 alignment table completed (5 challenge areas mapped)
- [x] Citizenship risk flagged in draft with recommended actions
- [x] UBAP sensor architecture defined; open standard committed

---

## Top-3 priorities

### 1 — Resolve citizenship, designate PI (before Jun 30) — NO OUTREACH NEEDED EXCEPT NSF/HERVE

| Action | Who | When |
|---|---|---|
| Email researchsecurity@nsf.gov for written dual-citizenship interpretation | Shahin | **Today** |
| Engage research-security counsel (CHIPS Act Sections 10636/10632) | Shahin | This week |
| Get Hervé's citizenship eligibility confirmed in writing | Shahin / Hervé | Jun 20 |
| Designate PI of record; general counsel review | Shahin + counsel | Jun 30 |

### 2 — Finalize and submit Phase 0 proposal (due Jul 13, 5:00 PM ET)

Proposal is substantively done. Remaining tasks, in "do now" order:

| Task | Outreach? | By |
|---|---|---|
| Update personnel section with confirmed PI of record | No (internal) | Jul 1 |
| Finalize COI PDF (separate doc, not in page count) | No | Jul 5 |
| Validate AUC benchmarks for coordinate model (SSRI and TMS response) | No (internal science) | Jul 10 |
| Draft LOC requests for Stanford Williams lab and MGH Martinos Center | Needs outreach | Jul 1 |
| Confirm Hervé team additional optical engineers as named personnel | Needs Hervé | Jul 1 |

### 3 — Build Psychoverse coordinate model (parallel, starts now)

The biotype atlas is done. Next: train the coordinate model, validate it against held-out treatment response cohorts, produce AUC benchmarks. This also feeds IGoR TA1 (same meso-scale layer). No blockers; start now.

---

## What Cytoscope is (the product)

**Psychoscope** = adaptive multi-chromophore optical headset for continuous mental-health monitoring.

Three sensing layers:

| Layer | What it does |
|---|---|
| Coarse (60 sec) | TD-fNIRS across cortex: triangulates mental-health coordinate on Psychoverse map |
| Adaptive zoom | Optode re-weighting to 9 anchor regions and 4 transdiagnostic edges (dlPFC-sgACC, amygdala-vmPFC, NAc-OFC, OFC-caudate) |
| Fine-grained | Marie-Nelly ultrasound-aided optical focusing: 2-3 cm depth, single-cell-class spectroscopic readout |

**Key differentiator vs. competitors (Kernel, Openwater, Muse):** Psychoscope is the only platform that combines multi-chromophore readout, biotype-adaptive targeting, edge (not just node) sensing, melanin equity as a first-class signal, and a continuous longitudinal training corpus.

---

## NSF X-Labs Phase 0 fit

| Topic 2 challenge area | How Psychoscope addresses it |
|---|---|
| Adaptive AI-based sensing | Coordinate-driven optode steering; skull-as-learnable-transform |
| AI-driven computational imaging | End-to-end-differentiable multi-chromophore reconstruction |
| MRI-free deep-tissue imaging | TD-fNIRS, DCS, Marie-Nelly depth-zoom; no MRI needed |
| Instruments engineered for AI training | Every device feeds a federated longitudinal corpus |
| Whole-brain activity at cellular resolution | Cellular-class spectroscopy in cortex (Phase 1); longitudinal per user |

---

## Citizenship eligibility: what to know

**The problem.** NSF X-Labs Sections 6.2-6.3 bar citizens of Iran from serving as Senior/Key Personnel. Shahin is a dual US/Iran citizen. The plain text covers citizens; it is unclear whether dual citizens are included. This is the one legal question that must be answered in writing before submission.

**The safe path.** Hervé Marie-Nelly serves as PI of record and Senior/Key Personnel (pending confirmation that his citizenship is not one of the four restricted countries). Shahin is listed as Founder/CEO and organizational lead, a genuine role but NOT designated Senior/Key Personnel.

**Do not submit with Shahin as Senior/Key Personnel without written NSF confirmation.**

---

## Cross-track links

| Link | What it means for Cytoscope |
|---|---|
| **Cytoverse / IGoR** | The Psychoverse coordinate sits on top of the micro-to-meso causal bridge. The meso-scale signals Cytoscope reads index the cellular states IGoR maps. |
| **Cytonome / Yar PBC** | Soft sensors (Level 1) and MH sensors (Level 2) ship via Yar app now. Psychoscope becomes a UBAP plug-in at Phase 1. PBC handles manufacturing scale at Phase 2. |
| **Toolchain / UBAP** | The open standard (Apache 2.0, SOSA/SSN grammar) ties all three sensor levels together and enables a plug-in ecosystem. |

---

## Funding timeline (sensor track)

| Date | Event | Status |
|---|---|---|
| **Today** | Email NSF OCRSSP for citizenship interpretation | Do now |
| Jun 20 | Hervé citizenship confirmed in writing | Outreach needed |
| Jun 30 | PI designated; counsel review complete | Internal |
| Jul 1 | LOC requests sent (Stanford, MGH) | Outreach needed |
| **Jul 13, 5:00 PM ET** | **NSF X-Labs Phase 0 offer due** | Submit |
| Q4 2026 | Phase 0 award decision | Up to $1.5M |
| 2027 | Phase 1 (if Phase 0 success) | Up to $50M/yr |
| Phase 2+ | PBC for manufacturing; protein-aggregate sensing stretch goal | Contingent |

---

## Gaps (by severity)

| Gap | Severity | Owner |
|---|---|---|
| NSF OCRSSP written interpretation | P0 blocker | Shahin (today) |
| Hervé citizenship confirmation | P0 blocker | Shahin / Hervé |
| PI of record designation | P0 blocker | Shahin + counsel |
| Clinical neuroscientist named | P1 (needed at Oral stage) | Shahin |
| MGH Martinos Center LOC | P1 | Shahin |
| Coordinate model AUC benchmarks | P1 (strengthens proposal) | Science team |
| Psychoscope repo created | P2 | Engineering |

---

## Duplicate docs needing canonical-home assignment (do not edit; flag for reconciliation)

| Path | Issue |
|---|---|
| `Strategic Planning/master_plan/13_sensor_ecosystem.md` | Likely verbatim duplicate of `X-Labs/01-strategy/master-plan-v2.0/13_sensor_ecosystem.md`; confirm and mark superseded |
| `Science and Platform/schema-survey-2026-05/old/sensors.md` | Superseded by the current `sensors.md` in same folder |
| `Infrastructure and Tooling/sensing/old/sensors.md` | Earlier sensors.md; superseded |

# Cytoscope Track — Sensor Strategy and NSF X-Labs

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: leadership
> **Tags**: `strategy`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)

**Date:** 2026-06-03 · Stage 5, Track 5 (p2) · Consolidated from cytomem corpus, NSF X-Labs materials, and X-Labs strategy docs.
**Reading time:** ~9 min. **If you only read one thing:** the NSF X-Labs Phase 0 proposal (Psychoscope) is the primary funding vehicle for the sensor track; the Jul 13 deadline is firm; the citizenship-eligibility question for Shahin as Senior/Key Personnel must be resolved with NSF counsel and Hervé before submission.

---

## BLUF

Cytoscope is the sensor pillar of the Cytognosis platform. Its first product is Psychoscope, an adaptive multi-chromophore optical spectroscopy headset for continuous mental-health monitoring, co-developed with Hervé Marie-Nelly. Phase 0 funding comes from NSF X-Labs (up to $1.5M; offer due Jul 13, 5:00 PM ET). The citizenship question — whether Shahin Mohammadi's dual US/Iran citizenship bars him from Senior/Key Personnel designation under NSF X-Labs Sections 6.2-6.3 — is an open legal question that must be resolved in writing before submission. The sensor reads meso-scale signals (functional connectivity, hemodynamics, CCO) that index the micro-scale cell-type states mapped by IGoR/Cytoverse; commercialization runs through the Cytonome/Yar PBC arm.

---

## Done (as of 2026-06-03)

- Phase 0 draft (8-page proposal) written: `07-nsf-xlabs/NSF_XLabs_Phase0_Draft_v1.md`
- NSF X-Labs source materials processed and consolidated: `07-nsf-xlabs/materials/`
- Transdiagnostic biotype atlas assembled across 14 disorders and three scales (molecular, connectomic, phenotypic)
- Technology landscape surveyed; competitive analysis of EEG, OPM-MEG, fNIRS, TD-fNIRS, Openwater TRUE, Kernel Flow2 complete
- Psychoscope Topic 2 alignment mapped (five challenge areas, one subsystem per area)
- Citizenship-eligibility risk identified and flagged in proposal draft with recommended actions
- Sensor schema standards survey complete (SOSA/SSN upper layer; BIDS, FHIR, Open mHealth profiles)
- Universal Biosensor Adapter Protocol (UBAP) architecture defined; open standard committed to perpetuity; Apache 2.0 reference implementation planned

---

## 1. Sensor strategy

### 1.1 Architecture: the three-level stack

Cytoscope is not a single device; it is a universal interface (UBAP) plus a specific hardware lineage. The sensor pillar spans three levels that represent an implementation progression:

| Level | Technology | Timeline | What it measures |
|---|---|---|---|
| **Soft sensors (Level 1)** | Passive sensing via Cytonome conversation, wearable physiology (Apple Watch, Oura, Whoop), clinical assessment scales (PHQ-9, GAD-7, HiTOP, MADRS), behavioral tracking | Available now; deployed in Yar/Cytonome app | Phenotypic outputs: mood, activity, sleep, symptoms, behavioral state |
| **MH sensors (Level 2)** | Consumer EEG (Muse, Emotiv), fNIRS wearable headsets, standardized neuropsych instruments, lab connectors (Quest, LabCorp) | Phase 1 integration ongoing | Intermediate endophenotypes: hemodynamics, cortical oscillations, molecular panels |
| **Wearable (Level 3)** | Psychoscope adaptive multi-chromophore optical headset; UBAP plug-in; eventually Caltech FRO or ARPA-H Delphi-class programmable sensor | Phase 0 proposal submitted Jul 2026; Phase 1 hardware by Month 24 | Multi-scale: HbO2, HbR, CCO, DCS, SWIR water/lipid; functional connectivity edges; biotype coordinate |

The UBAP contract governs all three levels. The data contract specifies measurement type, unit, uncertainty, sampling regime, biological meaning, provenance, and consent metadata. Vendors are free to protect processing IP; UBAP is a boundary specification, not a hardware or pipeline mandate.

### 1.2 Psychoscope: the Level 3 instrument

Psychoscope integrates three sensing layers not currently combined in any commercial system:

1. **Coarse whole-cortex mapping.** High-density time-domain fNIRS (TD-fNIRS) plus diffuse correlation spectroscopy (DCS) at 1-second resolution; measures HbO2, HbR, CCO (mitochondrial axis), and cerebral blood flow across the cortex. Runs for approximately 60 seconds to triangulate the user's coordinate on the Psychoverse map.

2. **Biotype-driven target selection.** The 60-second coarse scan places the user on the Psychoverse coordinate (the mental-health map built across 14 disorders and three RDoC-style scales). This coordinate drives optode re-weighting to the highest-yield anchor regions and, critically, to the transdiagnostic **edge** biomarkers: dlPFC-sgACC anticorrelation (depression, the SAINT target), amygdala-vmPFC threat edge (anxiety, PTSD), NAc-OFC reward edge (substance use disorders, ADHD, anorexia), and OFC-caudate CSTC loop (OCD, Tourette). Edges separate disorders and map onto interventions better than nodes alone.

3. **Fine-grained zoom.** Ultrasound-aided optical focusing (Marie-Nelly stealth program, 2024-2026) reaches 2-3 cm depth in vivo at single-cell-class spectroscopic resolution. Spatially offset Raman spectroscopy (SORS) provides a Phase 2 stretch capability for protein-aggregate sensing (Alzheimer's, Parkinson's).

A core engineering innovation is the skull-as-learnable-transform concept: the skull's hydroxyapatite microstructure is near-stationary (decorrelation time tens of seconds versus milliseconds for vascularized tissue) and therefore learnable. The foundation model estimates the skull's per-subject optical transfer function from a structural prior and in situ wavefront sensing, then inverts it computationally. This converts the classic optical obstacle into a per-subject calibration input and directly addresses NSF Topic 2's "Adaptive AI-based sensing algorithms" and "AI-driven computational imaging" challenge areas.

**Melanin equity** is built in as a first-class signal: a dedicated spectral calibration channel quantifies melanin per user rather than treating skin tone as noise (Kwasa et al., Nat Hum Behav 2023).

**Current TRL.** Through-skull adaptive optics in living humans: TRL 2-4. The Psychoscope architecture is designed to benefit from each incremental advance; Phase 1 validates the skull-model pipeline and demonstrates closed-loop correction gain on a phantom before in vivo translation.

### 1.3 The Psychoverse coordinate (biotype layer)

The biotype layer is what differentiates Psychoscope from all existing optical wearables. The current atlas covers 14 disorders (schizophrenia, bipolar, depression, PTSD, anxiety, autism, ADHD, OCD, Tourette, anorexia, and four substance use disorders), harmonized across three scales:

- **Molecular:** Gene Ontology terms; key recurring axes are BDNF/TrkB plasticity, excitatory-inhibitory balance, mitochondrial/oxidative stress, and inflammation.
- **Connectomic:** Allen Human Reference Atlas nodes and edges; anchored to the Grotzinger and Smoller five-factor genomic structure (Nature 2025) and the Williams 2024 six-biotype scaffold (negative affect, reward, cognitive control, salience, vigilance, sensory gating).
- **Phenotypic:** SNOMED CT and HPO; HiTOP and RDoC compatible at the latent-axis level.

This coordinate enables the sensor to know which regions to interrogate per user (for example, a user exhibiting anxiety triggers focus on the amygdala-vmPFC edge; a user with psychosis signatures triggers the OFC-caudate loop and the 40 Hz ASSR measurement). The Psychoverse coordinate is the link between Cytoscope and Cytoverse; it is the meso-scale output that the Cytoverse (Map) pillar grounds in cellular-scale biology.

---

## 2. Cross-track convergence: the cellular bridge

The sensor track converges with the science pillar at one point: the **cellular micro-to-meso bridge**.

- Cytoscope reads meso-scale signals (functional connectivity edges, hemodynamics, CCO, EEG oscillatory features).
- These meso-scale signals **index** the micro-scale cell-type states mapped by Cytoverse, IGoR, and HSF: cell-type composition drives thalamocortical circuit function; genetic instruments disentangle genetic from exposome contributions to connectomic variation.
- Specifically: the Cytoscope biotype coordinate should predict cell-type composition in targeted circuits, because the single-cell genomic-to-connectomic causal link (IGoR TA1) justifies that the molecular biotype axes (BDNF/TrkB, E/I balance, mitochondrial state) have cellular-level mechanistic substrates.

This cross-track link is the scientific differentiation of the full Cytognosis platform versus any single-modality effort. NSF X-Labs funding the sensor, and ARPA-H IGoR funding the multi-scale causal model, are complementary; the scopes are explicitly non-overlapping and the proposal draft acknowledges the IGoR/HSF layer as "planned, not yet awarded."

**Commercialization path:** soft sensors and MH sensor integrations deploy first through the Yar PBC (the Cytonome commercial arm). Psychoscope hardware, once manufactured, becomes a Cytognosis UBAP plug-in available through the Yar app. The nonprofit Foundation retains IP and mission control; a PBC incorporation at Phase 2 handles manufacturing scale per the Cytognosis Openness Policy.

---

## 3. NSF X-Labs Phase 0: fit and deadline

### 3.1 Opportunity summary

| Field | Detail |
|---|---|
| Program | NSF X-Labs Initiative, Topic 2: Scientific Instrumentation for Sensing and Imaging |
| Mechanism | OT (Other Transaction); 9-12 month Phase 0 |
| Phase 0 award | Up to $1.5M |
| Phase 1 scale | Up to $50M/yr (pending Phase 0 success) |
| Offer due | **Jul 13, 2026, 5:00 PM ET** — firm |
| Format | 8 single-sided pages, 12pt, single-spaced, 1" margins; separate COI PDF |
| Lead organization | Cytognosis Foundation (501(c)(3)) |
| Co-PI | Hervé Marie-Nelly (deep-tissue spectroscopy, stealth company, sub-awardee) |

### 3.2 Alignment with Topic 2

| Topic 2 challenge area | Psychoscope subsystem |
|---|---|
| Adaptive AI-based sensing algorithms | Coordinate-driven optode steering; skull transfer-function learning |
| AI-driven computational imaging | End-to-end-differentiable multi-chromophore tomogram reconstruction; skull-as-learnable-transform pipeline |
| MRI-free deep-tissue imaging | TD-fNIRS, DCS, and Marie-Nelly ultrasound-aided optical focusing; no MRI infrastructure required |
| Instruments engineered for AI training pipelines | Every fielded device contributes paired sensor/coordinate/outcome data to a federated training corpus |
| Whole-brain activity at cellular resolution across long timescales | Cellular-class spectroscopic resolution in cortex (Phase 1); longitudinal continuous monitoring per user |

### 3.3 Citizenship-eligibility question (OPEN, flagged)

NSF X-Labs Sections 6.2-6.3 bar citizens of the Islamic Republic of Iran from serving as Senior/Key Personnel on X-Labs awards. Shahin Mohammadi is a dual US/Iran citizen. The plain text of the restriction covers nationals and citizens; legal interpretations differ on whether it covers US/Iran dual citizens, but the most conservative reading includes them.

**The viable path:** an eligible individual serves as PI of record and Senior/Key Personnel (Hervé Marie-Nelly, subject to confirming his citizenship is not among the four restricted countries listed in Sections 6.2-6.3; his citizenship has not been verified and must not be assumed). Shahin participates as Founder/CEO and organizational lead, with his role fully described but NOT designated Senior/Key Personnel under the NSF X-Labs definition.

**Required actions before Jul 13:**

1. Request a written interpretation from NSF's Office of the Chief of Research Security Strategy and Policy (OCRSSP) at researchsecurity@nsf.gov on the dual-citizenship question.
2. Engage independent research-security counsel familiar with CHIPS Act Sections 10636/10632 and NSF implementing guidance.
3. Confirm Hervé Marie-Nelly's citizenship eligibility with him directly and in writing.
4. Have Foundation general counsel review the final submission before filing.
5. Revise the personnel section to reflect the confirmed PI of record once eligibility is established.

**Do not submit with Shahin Mohammadi designated Senior/Key Personnel before receiving written NSF confirmation of eligibility.**

### 3.4 Governance structure

**Phase 0.** Cytognosis Foundation leads; Marie-Nelly's company is sub-awardee. Two-person Executive Committee (Mohammadi, Marie-Nelly) makes decisions within 48 hours. The Foundation's 501(c)(3) structure provides full operational autonomy and IP ownership today.

**Phase 1.** A dedicated Psychoscope Steering Committee, independent of the Foundation Board, governs the program. All six Autonomy Factor Test conditions (OTASO Section 6.1.1) are met: decision-making in days, funding and research-direction control, IP ownership, hiring and contracting authority, and independent leadership board.

**Phase 2.** A PBC may be incorporated to handle commercial manufacturing, with Cytognosis retaining IP and mission control through an arms-length licensing agreement per the Openness Policy.

---

## 4. Top-3 priorities

### Priority 1 — Resolve the citizenship question and confirm PI of record (before Jun 30)

This is the only blocker for submission. The rest of the proposal (science, outcomes, governance) is drafted. Contact NSF OCRSSP and engage research-security counsel. Confirm Hervé's citizenship status in writing. Revise the personnel section. This must be done at least two weeks before Jul 13 to allow Foundation general counsel review.

### Priority 2 — Finalize and submit the Phase 0 proposal (due Jul 13)

The Phase 0 draft (`07-nsf-xlabs/NSF_XLabs_Phase0_Draft_v1.md`) is substantively complete. Remaining work: (a) confirm the PI of record from Priority 1; (b) finalize outcome benchmarks for the coordinate model (AUC targets vs. SSRI and TMS response cohorts); (c) confirm and name the Stanford-network clinical neuroscientist and the MGH Martinos Center TD-fNIRS collaborator (or note as to-be-confirmed at Oral Proposal stage); (d) complete the COI PDF (separate document, not in page count); (e) confirm Letters of Collaboration from Stanford Williams lab network and MGH Martinos Center.

### Priority 3 — Build the Psychoverse coordinate model infrastructure (parallel, not blocking)

The biotype atlas (14 disorders, three scales) is assembled. The next step is building the coordinate model: train the latent-axis representation, validate against SSRI and TMS response cohorts (held-out N >= 500 each), and produce AUC benchmarks for the proposal outcomes table. This work is also foundational for IGoR TA1 (meso-scale biotype layer) and HSF (the multi-scale foundation-model layer). It can begin now using existing cohorts in the research corpus.

---

## 5. Gaps and open questions

| Gap | Severity | Owner | By when |
|---|---|---|---|
| Citizenship / Senior Key Personnel eligibility (Shahin) | P0 blocker | Shahin + counsel | Jun 30 |
| Hervé citizenship confirmation in writing | P0 blocker | Shahin / Hervé | Jun 20 |
| PI of record designation | P0 blocker | Shahin / Hervé | Jun 30 |
| NSF OCRSSP written interpretation request | P0 blocker | Shahin | Immediate |
| Clinical neuroscientist (Stanford/TMS-fMRI biotype) named | P1 (needed at Oral) | Shahin | Jul 1 |
| MGH Martinos Center TD-fNIRS confirmation | P1 (LOC for Oral) | Shahin | Jul 1 |
| Coordinate model AUC benchmarks validated | P1 (strengthens proposal) | Science team | Jul 10 |
| Psychoscope repo created | P2 (no repo yet) | Engineering | Aug 2026 |
| Schmidt Futures and McGovern Foundation LOIs | P2 (Letters of Collaboration at Oral) | Shahin | Oral stage |

---

## 6. Duplicate docs and canonical-home reconciliation

The sensor strategy and NSF X-Labs content is split across multiple locations. None should be edited; cytomem indexes all. Canonical homes per the Stage 4 taxonomy:

| Path | Contents | Status | Canonical home |
|---|---|---|---|
| `~/Claude/Projects/X-Labs/07-nsf-xlabs/NSF_XLabs_Phase0_Draft_v1.md` | Full 8-page Psychoscope Phase 0 proposal draft | **Canonical active proposal** | `X-Labs/07-nsf-xlabs/` |
| `~/Claude/Projects/X-Labs/07-nsf-xlabs/NSF X-Labs.md` | NSF X-Labs project log and planning notes | Active planning log | `X-Labs/07-nsf-xlabs/` |
| `~/Claude/Projects/X-Labs/01-strategy/master-plan-v2.0/13_sensor_ecosystem.md` | UBAP architecture and sensor ecosystem strategy | **Canonical for UBAP/sensor-ecosystem strategy** | `X-Labs/01-strategy/master-plan-v2.0/` |
| `~/Claude/Projects/Strategic Planning/master_plan/13_sensor_ecosystem.md` | Earlier copy of sensor ecosystem strategy | Superseded by X-Labs copy; keep indexed, do not edit | Reconcile to X-Labs |
| `~/Claude/Projects/Science and Platform/schema-survey-2026-05/sensors.md` | SOSA/SSN and sensor schema survey (full version) | **Canonical for schema standards** | `Science and Platform/schema-survey-2026-05/` |
| `~/Claude/Projects/Science and Platform/schema-survey-2026-05/old/sensors.md` | Earlier draft of schema survey | Superseded; keep indexed | Archive |
| `~/Claude/Projects/Infrastructure and Tooling/sensing/old/sensors.md` | Even earlier sensors.md | Superseded; keep indexed | Archive |
| `cytos/data/staged/grants/nsf_xlabs/` (multiple files) | NSF X-Labs official documents and annotations | Reference material; not editable by Cytognosis | `cytos/data/staged/grants/nsf_xlabs/` |
| `docs/cytonome/yar/sensors/` (README-vault, sensor-architecture, unified-sensor-report, etc.) | Yar/Cytonome sensor implementation docs | **Canonical for Yar-level sensor integration** | `docs/cytonome/yar/sensors/` |

**Action:** confirm the `Strategic Planning/master_plan/13_sensor_ecosystem.md` copy is a verbatim duplicate of the X-Labs version. If so, mark it superseded in the cytomem index.

---

## 7. Funding timeline (sensor-track view)

| Date | Event | Action |
|---|---|---|
| Immediate | NSF OCRSSP written-interpretation request | Send email to researchsecurity@nsf.gov |
| Jun 20 | Hervé citizenship confirmation | Written confirmation from Hervé |
| Jun 30 | PI of record designated; counsel review scheduled | Internal decision and general counsel engagement |
| Jul 1 | Clinical neuroscientist and MGH Martinos confirmation | LOC drafted |
| Jul 10 | Coordinate model AUC benchmarks available | Science team output |
| **Jul 13, 5:00 PM ET** | **NSF X-Labs Phase 0 offer due** | **Submit** |
| 2026 Q4 | Phase 0 award decision | Award up to $1.5M |
| 2027 | Phase 1 (if Phase 0 success) | Up to $50M/yr |
| Phase 2+ | PBC incorporation for manufacturing scale | Contingent on Phase 1 award |

---

## Sources

- NSF X-Labs official: `cytos/data/staged/grants/nsf_xlabs/nsf-otaso-fy26-xlabsinitiative.md`
- NSF X-Labs Topic 2: `cytos/data/staged/grants/nsf_xlabs/nsf-topic2-fy26-xlabssensingandimaging.md`
- Phase 0 proposal draft: `~/Claude/Projects/X-Labs/07-nsf-xlabs/NSF_XLabs_Phase0_Draft_v1.md`
- NSF X-Labs planning log: `~/Claude/Projects/X-Labs/07-nsf-xlabs/NSF X-Labs.md`
- UBAP / sensor ecosystem architecture: `~/Claude/Projects/X-Labs/01-strategy/master-plan-v2.0/13_sensor_ecosystem.md`
- Sensor schema survey: `~/Claude/Projects/Science and Platform/schema-survey-2026-05/sensors.md`
- Funding and IGoR track (NSF detail at §3 Priority 3): `~/Claude/Projects/X-Labs/01-strategy/tracks/FUNDING_IGOR_TRACK_2026-06-03.md`
- Stage 4 taxonomy and canonical-home assignments: `~/Claude/Projects/X-Labs/01-strategy/STAGE4_META_STRATEGY_TAXONOMY_2026-06-03.md`
- NSF X-Labs Jul 13 deadline: [NSF X-Labs](https://www.nsf.gov/funding/initiatives/nsf-x-labs), [Granted AI analysis](https://grantedai.com/blog/nsf-x-labs-1-5-billion-quantum-instrumentation-ota-mechanism-july-13-deadline-strategy-2026)

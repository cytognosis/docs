# IGoR Cost Model — Cytognosis-led Integrated Team

**Prepared:** 2026-06-12. **Superseded by:** `COST_MODEL_DETAILED_2026-06-16.md`. **[FLAG 2026-06-17: re-derive — Anne reattribution / Cellanome model TBD]** This file predates the 2026-06-17 TA4 corrections (Anne Carpenter reattributed to computational / no bench; Cellanome operating model TBD; Tegtmeyer = academic experimental arm + Element AVITI24). Use `COST_MODEL_DETAILED_2026-06-16.md` as the source of truth for all per-organization, per-phase figures.

**Target:** ~$50.0M ARPA-H request over 5 years (60 months), within the rumored ~$150M / ~3-team program envelope. The solicitation states **no per-award ceiling**; ~$50M/team is right-sized for a 5-year, 4-TA, multi-lab closed-loop program and is consistent with $150M ÷ 3 teams.

**Phase durations (from Appendix A):** Phase I = 18 mo, Phase II = 18 mo, Phase III = 24 mo.

---

## 1. Top-line

| Line | Value |
|---|---|
| ARPA-H funds requested (all phases) | **$50.0M** |
| Performer resource sharing (in-kind) | ~$4.0M |
| Total project value | ~$54.0M |
| Phase I (18 mo) | $13.5M |
| Phase II (18 mo) | $15.0M |
| Phase III (24 mo) | $21.5M |

Average burn ~$10M/yr; smooth ramp ($0.78M → $0.83M → $0.90M per month) as experimentation scales and the second disease is added in Phase III.

---

## 2. Allocation by performer and phase (ARPA-H request)

| Performer | Role / TAs | 5-yr total | Phase I | Phase II | Phase III |
|---|---|---|---|---|---|
| IPAI / Purdue (**Prime**) | Coordination, PI, Project Mgmt, Software Architect, TA1/TA2 support | $7.0M | $1.9M | $2.1M | $3.0M |
| **Cytognosis** (sub) | TA1 **lead**, TA2 **co-lead** | $14.0M | $4.0M | $4.2M | $5.8M |
| Phylo (sub) | TA2 agentic-science partner | $4.0M | $1.1M | $1.2M | $1.7M |
| SIFT (sub) | TA3 **lead** (LabOP / protocol stack) | $5.0M | $1.5M | $1.5M | $2.0M |
| Carpenter Lab (sub) | **Superseded.** Carpenter is now computational (no bench). In COST_MODEL_DETAILED_2026-06-16, this line is split: Tegtmeyer wet-lab in-housed to Purdue (academic experimental arm); Broad sub = $2.0M computational-continuity only. **[FLAG 2026-06-17: re-derive — Anne reattribution / Cellanome model TBD]** | $5.0M (STALE) | — | — | — |
| Cellanome (sub) | TA4 lab #2 — live-cell + Perturb-seq | $8.0M | $2.0M | $2.4M | $3.6M |
| Illumina (sub) | TA4 lab #3 — sequencing + data | $4.0M | $0.9M | $1.2M | $1.9M |
| Cross-team / integration / reserve | DDD workshop, bake-offs, connect-a-thon, mgmt reserve | $3.0M | $0.8M | $0.9M | $1.3M |
| **Total** | | **$50.0M** | **$13.5M** | **$15.0M** | **$21.5M** |

Phase checks: I = 13.5, II = 15.0, III = 21.5; total 50.0. ✔

Notes:
- **Illumina** is partly a resource-sharing partner (Billion Cell Atlas data + sequencing credits); funded line is for dedicated execution + data engineering.
- **Tahoe** (chemical perturbation) is held as an **optional** TA4 add for chemical screens; not in the base $50M.
- **DataTecnica** is the **alternate** TA2 partner if Phylo is unavailable; same budget line.

---

## 3. Consolidated Basis of Estimate (Solution Summary BOE table)

| Category | Amount | Basis of estimate (data points) |
|---|---|---|
| Direct Labor (fully burdened) | $22.0M | ~14 funded FTE/yr blended across 7 orgs × 2026 loaded rates (below); rises with experimentation |
| Labor hours | ~147,000 hrs | $22.0M ÷ ~$150/hr blended (salary + fringe) |
| Subcontracts / Consultants | $1.0M | Clinical co-lead (Ruzicka) effort, biostatistics, ethics/IRB, standards consultants |
| Materials | $6.0M | iPSC lines + NGN2 differentiation, CRISPRi/a libraries + lentivirus, Perturb-seq kits, Cell Painting reagents, sequencing consumables |
| Equipment | $2.5M | Imaging + instrument access/amortization (incl. Cellanome R3200 time), lab + GPU hardware |
| Travel | $1.0M | DDD workshop (kickoff), TA3 bake-offs, Phase III connect-a-thon, biannual IV&V reviews, dissemination |
| Other Direct Costs (ODC) | $7.0M | GPU/cloud compute (TA1 training + TA2 agentic inference), sequencing-as-a-service, storage, software/API licenses, grad tuition |
| Indirect (F&A / overhead) | $9.0M | Cytognosis 15% de minimis MTDC (2 CFR 200.414(f)); Purdue ~57% on-campus F&A; commercial overhead reconciled |
| Profit / Fee | $1.5M | Commercial subs (Cellanome, Phylo, SIFT, Illumina) ~7–10% on cost base; none for nonprofit/academia |
| **Total (incl. all phases)** | **$50.0M** | |
| Resource Sharing (Performer, in-kind) | ~$4.0M | Illumina Billion Cell Atlas data + sequencing credits; Cellanome instrument access; cloud research credits |

Footnote for SS/C.3: commercial performers present fully-burdened rates inclusive of their own overhead in their individual cost workbooks; the consolidated Indirect line aggregates all performers' indirect for transparency. Rates are illustrative pre-award estimates; finalized at OT negotiation.

---

## 4. Rate and unit-cost anchors (data points)

**Fully-loaded annual labor (2026, blended salary + fringe + direct OH):**
- Senior ML/AI engineer (Bay Area): ~$260K
- ML research scientist: ~$240K
- Software architect (IGoR-required role): ~$250K
- Computational biologist: ~$210K
- Research scientist / postdoc (industry): ~$120–130K
- Technical project manager: ~$200K
- PI (partial effort): pro-rated from the $228K Rung-1 base (HHS Exec Level II cap)
- Academic postdoc (Purdue): ~$70K + F&A; PhD student: ~$50K stipend + tuition

**Compute:**
- H100 GPU-hour, blended cloud/spot: ~$2.50–3.00/GPU-hr
- TA1 foundation-model fine-tuning + causal-model training: ~$250–400K/yr
- TA2 agentic inference (frontier API + open-weight serving): ~$150–250K/yr

**Wet-lab assay unit costs:**
- iPSC → NGN2 neuron differentiation run: ~$3–15K/run
- Targeted Perturb-seq screen: ~$5–30K; genome-scale: ~$50–300K
- Optical pooled / Cell Painting screen: ~$50–500K by scale
- Multiplexed scRNA-seq: ~$200–700/sample
- CRISPR library + lentivirus prep: ~$10–50K

**Indirect:**
- Cytognosis: 15% de minimis on MTDC (2 CFR 200.414(f)); on an OT, ARPA-H may negotiate actuals
- Purdue on-campus F&A: ~55–60% MTDC
- Commercial subs: overhead embedded in loaded rate + fee ~7–10%
- MTDC base excludes subaward amounts above the first $50K each

**Program comparables (right-sizing):** ARPA-H/DARPA-class programs ~ $17M/team (PARADIGM) to ~$20–39M/performer (NITRO); a 5-yr, 4-TA, multi-lab closed-loop team at ~$50M is consistent with the rumored $150M / 3-team envelope.

---

## 5. Representative per-org breakdowns (for C.3 + C.4 workbook)

### Cytognosis (TA1 lead + TA2 co-lead) — ~$2.5–3.0M/yr steady state
| Role | FTE | Loaded $/yr |
|---|---|---|
| PI (Mohammadi), partial | 0.5 | ~$140K |
| Software architect (TA2/integration) | 1.0 | ~$250K |
| Senior ML/AI engineer (TA2) | 1.0 | ~$260K |
| ML research scientist (TA1/TA2) | 1.0 | ~$240K |
| Computational biologists (TA1) | 2.0 | ~$420K |
| Technical project manager | 1.0 | ~$200K |
| Research scientist / postdoc | 1.0 | ~$120K |
| **Personnel subtotal** | ~7.5 | **~$1.63M** |

Plus compute ~$400K/yr, ODC ~$200K/yr, indirect at 15% de minimis. 5-yr total ~$14.0M (Phase III heavier: 2nd disease + scaled inference).

### Cellanome (TA4 live-cell + Perturb-seq) — ~$1.6M/yr → scaling
Per-experiment anchors drive the ramp: optical pooled screens $50–500K each; targeted Perturb-seq $5–30K/screen; scRNA-seq ~$200–700/sample; iPSC differentiation $3–15K/run. Phase I intra-team validation (lighter) → Phase II cross-team + multicellular → Phase III marketplace scale. 5-yr ~$8.0M.

### IPAI / Purdue (Prime) — ~$1.2–1.5M/yr
PI (Grama) effort, project management, software-architect oversight, 1–2 researchers + students, TA1/TA2 methods support; Purdue F&A ~57%. 5-yr ~$7.0M.

---

## 6. Resource sharing (Criterion 4 leverage)
- **Illumina:** Billion Cell Atlas perturbation data access + sequencing credits (in-kind, ~$2–3M value).
- **Cellanome:** discounted instrument access / R3200 time (in-kind).
- **Cloud compute research credits** for TA1/TA2 (in-kind).
- **Broad/JUMP Cell Painting** reference data (open; leverages prior public investment).

Presented as ~$4.0M Performer in-kind share on top of the $50.0M ARPA-H request → ~$54.0M total project value. Cost-share is not required but is evaluated positively under Criterion 4.

---

## 7. OT / contracting notes (from Appendix C + E)
- **Instrument:** Other Transaction (OT); milestone-based payments via PMS (pms.psc.gov) + Defend the Spend, tied to accepted TDD milestones.
- **Appendix E (Draft OT Agreement):** must be submitted with redlines/comments; silence = acceptance as-is. Plan a counsel (Duane) redline pass before Aug 6.
- **IP / data rights:** open-source preferred (Apache-2.0 / MIT / BSD); software + data delivered to government; factorized-PRS method kept proprietary and marked on affected pages (extensible proprietary namespace is explicitly allowed by TA3).
- **IV&V:** do not budget for the IV&V partner, but budget effort to collaborate (containerization, docs, materials transfer, biannual reviews).

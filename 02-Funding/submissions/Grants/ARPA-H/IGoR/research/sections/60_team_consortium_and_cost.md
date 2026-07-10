## 60. Team, consortium, and cost model

**Current structure (decided 2026-06-03):** IPAI/Purdue = prime + PI; Cytognosis = funded sub-award (TA1 lead, TA2 co-lead); five additional sub-awardees for TA2, TA3, and TA4. This is a 7-performer structure. Total ARPA-H request: **$50,000,000** over 60 months (3 phases: 18 + 18 + 24 months). This supersedes the earlier $30M midpoint and Cytognosis-as-prime framing from the 2026-06-02 and 2026-06-05 solution summaries.

**Rationale for IPAI-prime:** "Funds still reach Cytognosis as a real sub-award (builds its record and resources the org), while Purdue's track record, infrastructure, and F&A environment carry the win." (Strategy Master 2026-06-03)

---

### Performer roles table

| Performer | Type | TA role | PI/key lead | Status |
|---|---|---|---|---|
| **IPAI/Purdue** | Academia (prime) | Coordination, PI, software architecture, TA1/TA2 support | Ananth Grama, PhD (Director, IPAI) | Warm; not yet formally committed |
| **Cytognosis Foundation** | Nonprofit 501(c)(3) | TA1 co-lead; TA2 co-lead | Shahin Mohammadi, PhD (Founder/CEO) | Confirmed |
| **Phylo** | For-profit | TA2 agentic-science co-lead | Kexin Huang, PhD (Founder; creator of Biomni) | Warm/in-discussion |
| **SIFT** | For-profit | TA3 lead (LabOP/protocol stack); shared cross-TA schema and representation co-led with Cytognosis (Mohammadi) | Daniel Bryce, PhD (lead); Robert Goldman, PhD (advisory); approx. 1 Staff-plus/Principal FTE, split ~70% Bryce/~30% Goldman | Confirmed |
| **Matt Tegtmeyer lab (Purdue)** | Academia | TA4.1 academic experimental arm (all wet-lab experiments; iPSC-neuron disease models; Element AVITI24 / Teton CytoProfiling) | Matthew Tegtmeyer, PhD (Purdue faculty) | Confirmed 2026-06-15 |
| **Anne Carpenter (IPAI/Purdue)** | Academia (IPAI/Purdue) | Computational morphology and imaging models (interpretable models, morphological profiling); TA4 analysis + TA1/TA2 bridge. **No wet-lab bench.** | Anne Carpenter, PhD (IPAI/Purdue) | Confirmed |
| **Cellanome** | For-profit | TA4.1 industry arm (live-cell + same-cell Perturb-seq) | Dwight Baker, SVP Product Development | Advancing; structure agreed, NDA sent |
| **Illumina** | For-profit | TA4.2 sequencing and bioinformatics | Key contact in discussion | Proposed |
| **McLean Hospital/HMS** | Academia | Clinical co-lead (translational grounding) | W. Brad Ruzicka, MD/PhD | Confirmed |

> [!NOTE]
> **2026-06-18 update:** TA4 restructured and confirmed. Matt Tegtmeyer's lab (Purdue) = TA4.1 academic experimental arm (all wet-lab experiments). Cellanome = TA4.1 industry arm (R3200 + Perturb-LINK). Anne Carpenter = computational morphology/imaging-model lead (IPAI/Purdue, confirmed, no bench); Carpenter Lab budget line covers personnel + compute, not wet-lab capex. SIFT confirmed: Daniel Bryce (lead), Robert Goldman (advisory), approx. 1 Staff-plus/Principal FTE, ~70/30 split; shared cross-TA schema co-led with Cytognosis/Mohammadi. Elham Jebalbarezi Sarbijan (IPAI/Purdue) fills the Software/Systems Architect seat (tentative). Patricia Purcell confirmed as PM. Transfyr declined 2026-06-18. SPOC declined 2026-06-18. Additionally, both Matt and Anne are on an IU-prime IGoR team (~5 lead PIs; likely Purdue subaward). This is effort/optics to resolve before Aug 6 but is not a blocker for the Jun 25 Solution Summary.

**Open mandatory roles status (as of 2026-06-18):**

- **Project Manager:** Patricia (Patty) Purcell, confirmed. ~1.0 FTE, ~$200K/yr fully loaded.
- **Software and Systems Architect:** Elham Jebalbarezi Sarbijan (IPAI/Purdue), tentative. Owns TA1-TA2 interface specs, cross-team interoperability, and open-source release. ~1.0 FTE, ~$250K/yr fully loaded. This is a named IGoR-required role, distinct from the PI and PM.

---

### Cost model: $50M, 3-phase allocation by performer

Source: COST_MODEL.md (2026-06-12); this is the authoritative current version.

| Performer | 5-yr total | Phase I (18 mo) | Phase II (18 mo) | Phase III (24 mo) |
|---|---|---|---|---|
| IPAI/Purdue (prime) | $7.0M | $1.9M | $2.1M | $3.0M |
| Cytognosis (sub) | $14.0M | $4.0M | $4.2M | $5.8M |
| Phylo (sub) | $4.0M | $1.1M | $1.2M | $1.7M |
| SIFT (sub) | $5.0M | $1.5M | $1.5M | $2.0M |
| Carpenter Lab (sub) | $5.0M | $1.3M | $1.5M | $2.2M |
| Cellanome (sub) | $8.0M | $2.0M | $2.4M | $3.6M |
| Illumina (sub) | $4.0M | $0.9M | $1.2M | $1.9M |
| Cross-team/integration/reserve | $3.0M | $0.8M | $0.9M | $1.3M |
| **Total** | **$50.0M** | **$13.5M** | **$15.0M** | **$21.5M** |

---

### Consolidated Basis of Estimate (BOE) categories

| Category | Amount | Basis |
|---|---|---|
| Direct labor (fully burdened) | $22.0M | ~14 funded FTE/yr blended across 7 organizations at 2026 loaded rates |
| Labor hours | ~147,000 hrs | $22.0M / ~$150/hr blended (salary + fringe) |
| Subcontracts/consultants | $1.0M | Clinical co-lead effort, biostatistics, ethics/IRB, standards consultants |
| Materials | $6.0M | iPSC/NGN2 differentiation, CRISPRi/a libraries, Perturb-seq kits, Cell Painting reagents, sequencing consumables |
| Equipment | $2.5M | Imaging/instrument access, lab and GPU hardware |
| Travel | $1.0M | DDD workshop (kickoff), TA3 bake-offs, connect-a-thon, biannual IV&V reviews, dissemination |
| Other direct costs (ODC) | $7.0M | GPU/cloud compute (TA1 training + TA2 agentic inference), sequencing-as-a-service, storage, software/API licenses, grad tuition |
| Indirect (F&A/overhead) | $9.0M | Cytognosis 15% de minimis MTDC; Purdue ~57% on-campus F&A; commercial subs' overhead reconciled |
| Profit/fee | $1.5M | Commercial subs ~7-10% on cost base; none for nonprofit/academia |
| **Total** | **$50.0M** | |
| Resource sharing (Performer, in-kind) | ~$4.0M | Illumina Billion Cell Atlas data + sequencing credits; Cellanome instrument access; cloud research credits |

---

### Cytognosis sub-award detail (~$2.5-3.0M/yr steady state; ~7.5 FTE)

| Role | FTE | Loaded $/yr |
|---|---|---|
| PI (Mohammadi), partial | 0.5 | ~$100K |
| Software architect (TA2/integration; IGoR-required) | 1.0 | ~$250K |
| Senior ML/AI engineer (TA2) | 1.0 | ~$260K |
| ML research scientist (TA1/TA2) | 1.0 | ~$240K |
| Computational biologists (TA1) | 2.0 | ~$420K |
| Technical project manager | 1.0 | ~$200K |
| Research scientist/postdoc | 1.0 | ~$120K |
| **Personnel subtotal** | ~7.5 | **~$1.59M** |

Plus compute ~$400K/yr, ODC ~$200K/yr, indirect at 15% de minimis MTDC. 5-yr total ~$14.0M (Phase III heavier due to second disease and scaled inference).

**Labor rate anchors (2026, Bay Area):**

- Senior ML/AI engineer: ~$260K; ML research scientist: ~$240K; software architect: ~$250K; computational biologist: ~$210K; research scientist/postdoc: ~$120-130K; technical PM: ~$200K
- H100 blended cloud/spot: ~$2.50-3.00/GPU-hr

**Indirect rates:**

- Cytognosis: 15% de minimis MTDC (2 CFR 200.414(f)); on an OT, ARPA-H negotiates the actual rate
- Purdue: ~57% on-campus F&A (negotiated)
- Commercial subs: overhead embedded in loaded rate + fee ~7-10%
- MTDC excludes first $50K of each subaward only

---

### Evolution from earlier versions

The 2026-06-02 cost model (IGoR_Cost_Breakdown_2026-06-02.md) and the 2026-06-05 SS used a 3-performer structure (Cytognosis prime ~$13.5M, Cellanome ~$10.5M, Purdue/IPAI ~$6.0M) at a planning midpoint of ~$30M. The FULLPROPOSAL_DRAFT and COST_MODEL_2026-06-12 expand to a 7-performer structure (adding Phylo, SIFT, and Illumina as named sub-awardees) and a $50M total request. The per-performer Cytognosis and Purdue/IPAI dollar amounts in the current model are consistent with the earlier planning shares; the increase reflects the full team scope. The prime/sub order also changed: the 2026-06-02 SS had Cytognosis as prime; the 2026-06-05 SS switched to IPAI-prime, which is the committed structure.


### Confirmed team decisions (2026-06-14)

- **Prime and PI:** confirmed **IPAI-Purdue as prime with Ananth Grama as PI**. The Cytognosis-prime alternative is retired as the base case; revisiting it would change only the cover page and the BOE order.
- **Project Manager:** **Patricia (Patty) Purcell** is added as PM (required role, distinct from the PI).
- **Software and Systems Architect (open role, actively recruiting).** Required by the ISO and distinct from the PI and PM. Target profile: senior or principal level, roughly 10 or more years building **interoperable, API-first, open-source systems**, with demonstrated **architectural authority over cross-organization implementation and integration** (including AI-accelerated development); expertise in **data and metadata schemas and standards** (for example LinkML, ontologies, FAIR), distributed and cloud systems, and ML/AI engineering platforms; ideally scientific or biomedical data interoperability. About $240K fully loaded is budgeted; state the annual level of effort.
- **TA3 and TA4 partners:** in **active parallel discussion; none finalized.** Candidate communications follow `partnerships/PARTNER_OUTREACH_STRATEGY.md` so we neither overstate commitments nor signal an empty roster.


### Roster with status (2026-06-14)

Confirmed members are untagged; tentative entries carry a short status. Full detail and engagement intel in `partnerships/TEAM_TRACKER.md`.

| Role | Member | Status |
|---|---|---|
| Prime and PI | IPAI/Purdue, Ananth Grama | confirmed |
| TA1 and TA2 co-leads | Cytognosis (Shahin Mohammadi, sub-awardee) and IPAI, Purdue | confirmed |
| Clinical and translational | W. Brad Ruzicka, McLean Hospital (Harvard Medical School affiliate) | confirmed |
| TA4.1 academic experimental arm | Matt Tegtmeyer lab, Purdue | confirmed (Purdue faculty; confirmed 2026-06-15) |
| Computational morphology and imaging models | Anne Carpenter (IPAI/Purdue; no wet bench) | confirmed |
| TA3 interoperable protocols | SIFT; Daniel Bryce (lead), Robert Goldman (advisory) | confirmed |
| Project Manager | Patricia Purcell | confirmed |
| Software and Systems Architect | Elham Jebalbarezi Sarbijan (IPAI/Purdue) | tentative |
| TA4.1 industry arm | Cellanome (live-cell imaging, same-cell scRNA-seq; advancing) | advancing |
| TA4.2 sequencing and bioinformatics | Illumina | proposed |
| TA2 add-on (optional) | Phylo (Kexin Huang) | in discussion |

> [!NOTE]
> Harvard's ToolUniverse is a tool we may use (MCP tool access), not a team or TA2 partner. Cytognosis and IPAI build TA2 jointly; Phylo and FutureHouse are optional add-ons, not blockers.


### Partner principles and flags (2026-06-14)

- **TA1 is in-house only:** Cytognosis, IPAI, and students. No external TA1 partners, to keep the mission-critical core focused.
- **DataTecnica (Faraz Faghri)** is an optional **TA2** add-on (CNS machine-learning, biobank-scale; neurodegeneration focus). Verify before including: Faraz's NIH employment status (federal employees are barred), OCI, and the salary cap (funded portion only).
- **Transfyr** declined 2026-06-18; removed from all rosters.
- **SPOC Biosciences** declined 2026-06-18; removed from all rosters.

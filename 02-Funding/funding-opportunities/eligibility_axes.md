# Eligibility Axes — Org-Form and Lead-Entity, All Priority + Active Opportunities

> **Status**: Active
> **Date**: 2026-07-16
> **Author**: Shahin Mohammadi
> **Tags**: `funding`

## BLUF

Cytognosis Foundation (US 501(c)(3), Delaware) is **lead-eligible today** for every active federal (ARPA-H, NSF, NIH), philanthropic (Wellcome Leap, Coefficient, Convergent Research), and EA-track opportunity, and for **ARIA (UK)**, which explicitly accepts non-UK lead applicants. The hard blockers are **Wellcome Trust Discovery** (needs a UK/Ireland/LMIC administering org), **Horizon Europe and ERC** (need an EU/Associated-country legal entity to lead or hold funding), and **Y Combinator** (for-profit only; needs the Yar PBC, not the 501(c)(3)). Two axes below: (a) org-form, (b) lead-entity location.

---

## Axis definitions

| Axis | Values |
|---|---|
| **(a) Org-form eligibility** | `nonprofit-eligible` (501(c)(3) can apply/lead) · `for-profit-only` (equity or company-form required) · `both` (either form works) |
| **(b) Lead-entity** | `US-lead-ok` (Cytognosis Foundation can be lead/prime today) · `requires-UK-or-EU-lead` (a UK or EU legal entity must lead or hold the funded portion) · `either` (no location restriction on the lead) |

---

## Part 1 — Active + priority opportunities (named individually)

Pulled from `opportunity_mapping.yaml` F04 (funding_source_type), F25/F26 (residency), F30 (required_partners_count), F20 (joint_program_partners), plus web-verified funder rules (see companion file `EU_UK_funders_2026-07-16.md` for citations).

| Opportunity | Funder | Pipeline status | (a) Org-form | (b) Lead-entity | Notes |
|---|---|---|---|---|---|
| ARPA-H Health Science Futures (HSF) ISO | ARPA-H | Under Consideration | both | US-lead-ok | US federal OT; SAM.gov registration required |
| ARPA-H Proactive Health Office (PHO) ISO | ARPA-H | Under Consideration | both | US-lead-ok | Same mechanics as HSF |
| NSF Tech Labs | NSF | Under Consideration | both | US-lead-ok | US federal OT |
| NSF Convergence Accelerator | NSF | Not Started (priority) | both | US-lead-ok | US federal grant |
| NSF-NIH Smart Health Program | NSF / NIH | Not Started (priority) | both | US-lead-ok | Joint program, still US-only |
| NIH Bridge2AI (Stage II) | NIH | Not Started (priority) | both | US-lead-ok | Academic affiliation typically expected (F37, verify for Cytognosis-as-institution) |
| NIH PRIMED-AI Program | NIH | Not Started (priority) | both | US-lead-ok | Same as above |
| Convergent Research — FRO | Convergent Research | Under Consideration | nonprofit-eligible | US-lead-ok | Proactive; FRO-style |
| Coefficient Giving — Global Health R&D | Coefficient Giving | Under Consideration | nonprofit-eligible | US-lead-ok | Direct-to-Shahin / org track per runway-comp memo |
| EA Funds — Long-term Future Fund | Effective Altruism | Under Consideration | both | US-lead-ok | Individuals or orgs |
| EA Funds — Infrastructure | Effective Altruism | Not Started (priority) | both | US-lead-ok | Same family as LTFF |
| Emergent Ventures | Mercatus Center | Not Started (priority) | both | US-lead-ok | Individuals or orgs |
| Wellcome Leap Programs | Wellcome Leap | Not Started (priority) | both | **either** | Verified: any legal entity, any jurisdiction; MARFA/CORFA contract at award, not application |
| Y Combinator (S26) | Y Combinator | Not Started (priority) | **for-profit-only** | US-lead-ok | Equity investment; needs Yar PBC entity, not the 501(c)(3) |
| Astera Institute Residency | Astera | Under Preparation | nonprofit-eligible | US-lead-ok | Residency requirement is **Emeryville, CA**, not a foreign-lead issue |
| Google.org AI for Science Impact Challenge | Google | Under Preparation | nonprofit-eligible | US-lead-ok | Corporate philanthropy, US 501(c)(3)-oriented |
| Genesis Mission | DoE | Under Preparation | both | US-lead-ok | US federal OT |
| **ARIA (UK) — Full Programmes** | ARIA (UK) | Priority (EU/UK track) | both | **either** — verify per-programme | Verified 2026-07: ARIA funds non-UK orgs incl. US companies; non-UK IP-commercialization triggers a small royalty |
| **ARIA (UK) — Opportunity Seeds** | ARIA (UK) | Priority (EU/UK track) | both | **either** | Same as above; rolling seed call includes "Scalable Neural Interfaces" space, relevant to Cytonome |
| **Wellcome Trust Discovery Programs** | Wellcome Trust | Priority (EU/UK track) | nonprofit-eligible | **requires-UK-or-EU-lead** | Hard block: administering org must be UK/Ireland/LMIC; tightens further from 29 Oct 2026 |
| **Horizon Europe — Cluster 1 Health** | European Commission | Priority (EU/UK track) | both | **requires-UK-or-EU-lead** | Needs ≥3 legal entities from ≥3 EU/Associated countries to be *funded beneficiaries*; a US entity can join unfunded as an Associated Partner only |

## Part 2 — Remainder of the 71, grouped by `funder_kind`

| `funder_kind` | Count | (a) Org-form (typical) | (b) Lead-entity (typical) | Verify flag |
|---|---:|---|---|---|
| `federal_grant` (remaining US) | 4 | both | US-lead-ok | — |
| `federal_OT` (remaining US) | 2 | both | US-lead-ok | — |
| `philanthropic_grant_proactive` (remaining) | 1 | nonprofit-eligible | US-lead-ok | — |
| `private_grant` (CZI, Schmidt, RWJF, Gates, DRK, AstraZeneca) | 9 | nonprofit-eligible (some allow both) | US-lead-ok | verify CZI for-profit arm |
| `intergovernmental_grant` (UNESCO/WHO) | 1 | nonprofit-eligible | either, program-dependent | verify |
| `ea_micro_grant` (remaining) | 1 | both | US-lead-ok | — |
| `private_fellowship` (Foresight, Spec.tech/Brains) | 2 | nonprofit-eligible | US-lead-ok | — |
| `accelerator` (Fast Forward, QB3, SkyDeck, J&J JLABS) | 4 | **verify per-program** | US-lead-ok | Fast Forward historically nonprofit-health-tech-friendly; SkyDeck/JLABS lean for-profit |
| `vc_investment` (IndieBio, Fifty Years, Lux, Next Sequence) | 4 | **for-profit-only** | US-lead-ok | Equity by definition; needs Yar PBC |
| `venture_builder` (Deep Science Ventures, Foresite Labs) | 2 | **for-profit-only** | US-lead-ok | Same as VC |
| `corporate_credit` (AWS Activate, Anthropic, NVIDIA, MathWorks, Azure, Google Cloud) | 7 | **verify** | US-lead-ok | Startup-oriented; usually incorporation-agnostic but confirm per program |
| `nonprofit_discount` (Adobe, AWS Nonprofit, Atlassian, Canva, Cisco, Dell, Claude, Google Workspace, DocuSign, HP, LinkedIn, GitHub, Zoom, Monday.com, Slack, Lenovo, Otter.ai, Microsoft, OpenAI, Notion, Mixpanel) | 21 | **nonprofit-eligible only** (TechSoup/registered-charity validation) | US-lead-ok | — |

**Total tagged: 71** (9 active-pipeline + 10 additional named priority/EU-UK + 52 grouped-by-kind = 71).

---

## Key takeaway for entity strategy

Only **two hard "requires-UK-or-EU-lead" blockers** exist in the current 71-opportunity set: **Wellcome Trust Discovery** and **Horizon Europe** (ERC would be a third if added; see `EU_UK_funders_2026-07-16.md`). Everything else in the EU/UK track — **ARIA** and **Wellcome Leap** — already accepts a US 501(c)(3) as lead. This scopes the Madhvi/UK-entity decision narrowly rather than broadly; see `runway-and-entity/Entity_Strategy_Madhvi_vs_UK_EU_Branch_2026-07-16.md`.

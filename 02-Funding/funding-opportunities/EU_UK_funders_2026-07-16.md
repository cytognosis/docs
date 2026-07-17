# EU / UK Funders — Verified Status, Eligibility, and Config-Stub Notes

> **Status**: Active
> **Date**: 2026-07-16
> **Author**: Shahin Mohammadi
> **Tags**: `funding`

## BLUF

Two funders in this set — **ARIA (UK)** and **Wellcome Leap** — accept Cytognosis Foundation (US 501(c)(3)) as lead applicant today, no UK/EU entity needed. Three — **Wellcome Trust, Horizon Europe, ERC** — legally require a UK, Irish, LMIC, or EU/Associated-country entity to lead or hold the funded portion; a US nonprofit can only join those as an unfunded partner. **UKRI** is rare-exception-only for overseas leads. **Novo Nordisk Foundation** is a poor mission/geography fit (Nordic-region PIs). The single most time-sensitive deadline across the set is **ARIA's rolling Opportunity Seed call, 31 July 2026** — it includes a "Scalable Neural Interfaces" opportunity space directly relevant to Cytonome.

---

## Summary table

| Funder | Next deadline (most important) | Org-form: nonprofit OK? | Lead-entity rule | Partner-count rule | Mission fit |
|---|---|---|---|---|---|
| **ARIA (UK)** | **31 Jul 2026** (rolling Opportunity Seeds, incl. Scalable Neural Interfaces); 27 Jul 2026 (Trust Everything Everywhere seed, lower fit) | Yes — universities, nonprofits, companies, individuals | **US-lead-ok**: non-UK applicants explicitly accepted; ARIA funded US companies directly in 2026 | None stated; single-team seeds, PD-orchestrated portfolios for full programmes | Good — AI-in-Science and neural-interface opportunity spaces align with Cytonome/Yar |
| **Wellcome Trust** (Discovery Awards) | Current round **22 Sept 2026**; after that the scheme goes always-open with no deadline; **eligibility narrows 29 Oct 2026** | Yes — universities, institutes, nonprofits, charities | **Requires UK/Ireland/LMIC-lead** (administering organisation); after 29 Oct 2026 restricted further to UK + LMIC in Africa/South Asia/SE Asia only | N/A (single-institution award; PI must commit ≥20% time, permanent contract) | Good scientifically (BDNF/plasticity, dimensional psychiatry) but organizationally blocked without a UK/eligible-LMIC host |
| **Wellcome Leap** | Program-specific; most recent open windows were single-week (e.g., 8–15 May 2026 for gut-sparing antibiotics); check wellcomeleap.org for next thrust opening | Yes — "any legal entity, any jurisdiction, academic/non-profit/for-profit/regulatory" | **Either / US-lead-ok** — no jurisdiction restriction to apply; MARFA (academic) or CORFA (commercial) contract executed only at award, not required to submit | None stated at application stage | Good — DARPA-style thrusts have matched Cytognosis focus areas (AI for Science, Healthcare, Proactive Health) before |
| **UKRI** | No single deadline; opportunity-specific (see ukri.org/opportunity) | Yes, in general — but as overseas lead, rare | **Requires-UK-lead** in practice: "UKRI only considers overseas organisations in rare cases, and there must be a pre-existing relationship with UKRI"; US orgs typically join as international co-investigator or self-funded project partner, not lead | Varies by opportunity; check per-call | Uncertain/low priority — no live UKRI call currently tracked in the 71-opportunity inventory |
| **Horizon Europe** (Cluster 1 Health, as one example pillar) | Recurring annual; 2026 Cluster 1 Health call closed 2026-04-16 per internal tracker — **next 2027 call date must be re-verified at call-opening** on the EU Funding & Tenders Portal | Yes — universities, nonprofits, companies, public bodies can all be beneficiaries | **Requires-EU-or-Associated-lead**: consortium of ≥3 independent legal entities from ≥3 different EU Member States or Associated Countries (UK is Associated since 2024). A US entity is **not** an Associated Country entity; it can join only as a self-funded Associated Partner, not as a funded Beneficiary or coordinator | **Minimum 3 legal entities from 3 different EU/Associated countries** (RIA/IA standard rule); CSA calls sometimes allow single-entity | Good scientifically; structurally the hardest of this set for a US-only nonprofit to lead |
| **ERC** (peer, not yet in 71-opp inventory) | Work Programme 2026 calls run on ERC's normal Starting/Consolidator/Advanced/Synergy cycle; check erc.europa.eu for exact 2026 dates | Yes — any legal entity type can host, but must be EU/Associated | **Requires-EU-or-Associated-lead**: "host institution must be located in an EU Member State or an Associated Country" for every grant type, incl. Synergy. PI nationality is unrestricted, but the *hosting entity* is not | N/A (single-PI or Synergy small-team grants, but always EU/Associated-hosted) | Low direct fit for Cytognosis-as-applicant (Cytognosis isn't EU-hosted); relevant only via a hosted collaborator like Madhvi at University of Manchester |
| **Novo Nordisk Foundation** (peer) | Program-specific (e.g., "New Exploratory Research and Discovery" 2026, "Project Grants in Natural/Technical Sciences" 2026); check novonordiskfonden.dk | Yes, for Nordic-based nonprofits/universities | **Requires-Nordic-lead**: primary calls (Emerging Investigator, Distinguished Innovator, most Project Grants) restrict the lead applicant to Denmark/Finland/Iceland/Norway/Sweden; non-Nordic orgs can be **co-applicants**, not leads | Varies; co-applicants outside Nordic region generally allowed | Low-moderate — biomedical mission overlap exists (metabolic/health science) but geography makes Cytognosis-as-lead structurally infeasible; only reachable via a Nordic co-lead |

---

## Config-stub notes (for `canonical/funders/*.yaml` and `opportunity_mapping.yaml`)

```yaml
# ARIA (UK) — update existing entries; F25/F26 confirmed false/null (correct, no residency requirement)
# Add: F31_strategic_connection note that ARIA funded 9 US tech companies + 3 US VC groups in 2026
# Add: F34_sub_programs — link Opportunity Seed spaces relevant to Cytonome: "Scalable Neural Interfaces"
# Next deadline correction needed: F08_deadline for aria-uk-opportunity-seeds should update to 2026-07-31
#   (rolling call); aria-uk-full-programmes F08 (2026-05-08) has passed — re-verify against open calls page.

funder_id: wellcome_trust
preset: preset_private_grant
funder_metadata:
  F25_residency_required: true       # correct existing "false" to true — admin-org location IS a hard gate
  F26_residency_location: "UK / Ireland / LMIC (Africa, South Asia, SE Asia after 2026-10-29)"
  F08_deadline: 2026-09-22            # current round; scheme goes always-open 2026-09-23
  F38_funding_score_rationale: "Blocked without UK/eligible-LMIC administering org; revisit only if Madhvi/Manchester or a UK entity can administer."

funder_id: wellcome_leap
funder_metadata:
  F25_residency_required: false       # confirmed correct
  F26_residency_location: null
  F38_funding_score_rationale: "No jurisdiction restriction; MARFA/CORFA executed at award only. Highest EU/UK-adjacent priority we can lead directly."

funder_id: horizon_europe_cluster1_health
funder_metadata:
  F30_required_partners_count: 3      # confirmed correct
  F25_residency_required: true        # add: lead/coordinator must be EU or Associated-country entity
  F26_residency_location: "EU Member State or Associated Country (UK included since 2024); US = self-funded Associated Partner only, not coordinator"

funder_id: ukri  # NEW — not yet in opportunity_mapping.yaml; add if a specific call is identified
funder_kind: federal_OT
funder_metadata:
  F25_residency_required: true
  F26_residency_location: "UK (overseas lead only by rare pre-existing-relationship exception)"

funder_id: erc  # NEW — peer funder, not in current 71; add only if a Manchester-hosted route is pursued
funder_kind: intergovernmental_grant
funder_metadata:
  F25_residency_required: true
  F26_residency_location: "EU Member State or Associated Country (host institution, not PI nationality)"

funder_id: novo_nordisk_foundation  # NEW — peer funder
funder_kind: private_grant
funder_metadata:
  F25_residency_required: true
  F26_residency_location: "Denmark, Finland, Iceland, Norway, Sweden (lead applicant); non-Nordic orgs co-apply only"
```

---

## Sources

- [ARIA — Funding opportunities (open calls, deadlines)](https://aria.org.uk/funding-opportunities)
- [ARIA — Funding FAQs](https://www.aria.org.uk/faqs-funding/)
- [Wellcome — Eligibility Information for Organisations](https://wellcome.org/research-funding/guidance/prepare-to-apply/eligibility-information-grant-applicants)
- [Wellcome Discovery Awards scheme page](https://wellcome.org/research-funding/schemes/wellcome-discovery-awards)
- [Wellcome — Scheme Application Deadlines and Key Dates](https://wellcome.org/research-funding/guidance/prepare-to-apply/scheme-application-deadlines)
- [Wellcome Leap — home](https://wellcomeleap.org/)
- [Wellcome Leap — CARE FAQ (eligibility language)](https://wellcomeleap.org/care-faq/)
- [UKRI — Apply to be an eligible organisation](https://www.ukri.org/apply-for-funding/before-you-apply/apply-to-be-an-eligible-organisation/)
- [UKRI — Get funding for international research](https://www.ukri.org/apply-for-funding/get-funding-for-international-research/)
- [EU — List of participating countries (Horizon/Euratom), v3.9, 10 Jul 2026](https://ec.europa.eu/info/funding-tenders/opportunities/docs/2021-2027/common/guidance/list-3rd-country-participation_horizon-euratom_en.pdf)
- [REA — Horizon Europe: Who should apply](https://rea.ec.europa.eu/horizon-europe-who-should-apply_en)
- [ERC — Grants for Non-European Researchers](https://erc.europa.eu/apply-grant/non-european-researchers)
- [ERC Starting Grant](https://erc.europa.eu/apply-grant/starting-grant)
- [Novo Nordisk Fonden — grants listing](https://novonordiskfonden.dk/en/grant/)
- [Novo Nordisk Fonden — New Exploratory Research and Discovery (NERD) Programme 2026](https://novonordiskfonden.dk/en/grant/new-exploratory-research-and-discovery-nerd-programme-2026/)

**Verify-before-use flag:** the Horizon Europe Cluster 1 Health *next* 2027 call date, the exact next Wellcome Leap thrust opening, and any live UKRI call should be re-checked at time of drafting — funder portals update call calendars continuously and this file reflects a 2026-07-16 snapshot.

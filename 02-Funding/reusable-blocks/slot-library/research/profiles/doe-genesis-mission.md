---
opportunity_name: Genesis Mission
funding_org: DoE
funding_category: Grants
funding_source: Government
url: https://genesismissionconsortium.org/
deadline: 2026-04-28
amount_typical_usd: 750000
focus_areas: [AI for Science]
research_tier: 1
researched: 2026-04-25
---

# DOE Genesis Mission

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: leadership, grant team
> **Tags**: `funding`, `opportunity-profile`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)

## Eligibility
Interdisciplinary teams from US institutions: universities, national labs, nonprofits, for-profit research orgs, hospitals, and certain government entities. DOE Office of Science (SC), CMEI, EM, NE, OE, HGEO co-lead. Some institutions limited-submission (only 1 application per institution as lead). Foreign collaboration via subaward subject to research-security review.

## Funding range
- **Phase I (small team)**: $500,000 – $750,000 over 9 months
- **Phase II (large team)**: larger awards (likely $5-25M over multi-year), preceded by LOI
- Total program: $293.76M anticipated total funding for FY26 across 21 topic areas

DOE standard F&A indirect rates apply (negotiated rates). Cost share not required for SC/CMEI grants; required for some EM/NE awards.

## Deadline pattern
- Phase I full applications: 2026-04-28
- Phase II Letters of Intent: 2026-04-28
- Phase II full applications: TBD post-LOI invitation

## Submission shape
Two phases:
1. **Phase I** (single-stage): full application via Grants.gov / PAMS
2. **Phase II**: LOI required → full application by invitation

DOE application format: SF-424 (R&R) + DOE-specific forms via Grants.gov / PAMS.

## Required artifacts
(Already partially canonical via `doe_genesis` funder file.)
- SF-424 (R&R) cover
- Project Abstract (1 page)
- Title page
- Project Narrative including:
  - §1 Significance (problem framing)
  - §2 Innovation / Approach
  - §3 Technical approach & milestones
  - §4 Team & management
  - §5 Go/no-go + outcomes
  - §6 Risk & mitigation
- Biosketches
- Facilities & Equipment
- Data Management Plan
- Bibliography
- Budget justification (per partner, per year)
- Current & Pending Support
- Letters of commitment / collaboration (consortium partners)
- AI methodology disclosure (Genesis-specific)
- Open-science / open-output plan
- Research-security disclosures (NSPM-33)

## Required topics / questions
Topic areas: advanced manufacturing, biotechnology, critical materials, nuclear fission, nuclear fusion, quantum information science, semiconductors and microelectronics, discovery science, energy.

Per topic, applications must address:
- AI/ML model or framework as central tool
- National Science & Technology Challenge alignment
- Interdisciplinary team formation
- Phase I → Phase II progression plan
- Quantitative milestones and go/no-go gates
- Open-output / publication plan (with research-security limitations)
- Biotechnology applicants: dual-use / biosecurity considerations
- Quantum applicants: quantum-advantage roadmap

## Schema gaps observed
None new — already a canonical funder file (`doe_genesis`). Profile reaffirms:
- §1-§6 narrative structure aligns with Heilmeier slots.
- Phase I/II structure covered by U07.2.
- DOE-specific NSPM-33 disclosures need A03 sub-slot ("research-security framework").
- Limited-submission (1 lead per institution) needs A03 sub-slot ("institutional limit").

## Notes
- Already a canonical funder (`doe_genesis`).
- Genesis Mission Consortium is the umbrella; DE-FOA-0003612 is the FY26 RFA.
- $293.76M total / 21 topic areas → average ~$14M per topic area across multiple awards.
- Biotechnology topic area is most relevant for Cytognosis.
- Phase I 9-month period is a feasibility/team-formation phase.

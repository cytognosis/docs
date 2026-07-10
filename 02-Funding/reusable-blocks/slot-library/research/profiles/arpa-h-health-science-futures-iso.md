---
opportunity_name: ARPA-H Health Science Futures (HSF) ISO
funding_org: ARPA-H
funding_category: Grants
funding_source: Government
url: https://sam.gov/opp/29c3ac2ea6754d1f897f9c71204c0eea/view
deadline: 2029-03-05
amount_typical_usd: unknown
focus_areas: [Healthcare]
research_tier: 1
researched: 2026-04-25
---

# ARPA-H Health Science Futures (HSF) ISO

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: leadership, grant team
> **Tags**: `funding`, `opportunity-profile`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)

## Eligibility
All responsible sources: academia, non-profits, for-profit entities, hospitals, community health centers, non-federal research centers, individuals, small businesses. US-based generally preferred but non-US allowed via teaming. Foreign participation subject to research-security review.

## Funding range
Awards via Other Transaction (OT) agreements. Typical project size $2M+ for high-impact efforts, but proposers may request what's necessary to reach a meaningful technical milestone. Multi-year. No fixed cap. Cost share not required but may strengthen proposals. Indirect cost: OT agreements use negotiated rates, not standard federal F&A.

## Deadline pattern
Open continuously through 2029-03-05. Submissions accepted on rolling basis. Solution Summary first, then (if invited) full proposal.

## Submission shape
Two-phase mandatory:
1. **Solution Summary** (Appendix A) — short (~10-15 pages) including program fit, today's-limits, novelty + quantitative metrics, who-cares, risks, team, budget synopsis. Required before any full proposal.
2. **Written feedback from ARPA-H** must be received before submitting a full proposal.
3. **Full Proposal** — Technical & Management Volume (~20 pages), Cost Volume (9 sections), Technology Development Description (TDD), policy documentation.

## Required artifacts
- Solution Summary (Appendix A) using ARPA-H template
- Full Technical & Management Proposal (~20 pages)
- Cost Proposal (9 sections including budget, base/option periods, justifications, OH/G&A)
- Biosketches / key personnel
- Letters of commitment from team members and partners
- Statement of Work
- Technology Development Description (TDD)
- Research-security / foreign-influence disclosures
- Human Subjects Research / Animal Research forms (if applicable)
- Conflict of Interest declarations
- IP / Patent rights statement

## Required topics / questions
Solution Summary structure (Appendix A):
- §1 Program fit / objective in plain language (Heilmeier Q1)
- §2 How is it done today / limits of current practice (Heilmeier Q2)
- §3 Novelty + quantitative success metrics (Heilmeier Q3 + Q8)
- §4 Who cares / stakes / beneficiaries (Heilmeier Q4)
- §5 Risks (Heilmeier Q5)
- Team / key personnel
- Budget synopsis

Full Proposal additions:
- Detailed technical approach with phased milestones
- Management approach including org chart and PD interface
- Transition-to-Practice (TTP) plan
- Equity / accessibility assurances (ARPA-H specific)
- AI-use disclosure if applicable
- Dual-use / biosecurity assessment
- IP & data governance
- Subcontractor and partner roles

## Schema gaps observed
- **Solution-Summary-vs-Full-Proposal** staging — canonical doesn't currently model two-stage federal solicitations explicitly. Likely a render-time concept (multiple sinks per funder), but needs metadata field on funder file.
- **OT (Other Transaction) agreement specifics** — IP, flow-down, audit treatment differs from FAR contracts. Could use sub-slot under U15.2 (foreground IP) noting "OT-flexible terms".
- **Research-security disclosures** — Section 223 / NSPM-33 requirements are heavier than U16 currently models. Could be A03 sub-field.
- **Equity/access assurances** specific to ARPA-H mission — already in U13, but ARPA-H requires explicit "TTP equity plan" as separate artifact (not just U13 prose).

## Notes
- ISO solicitation: ARPA-H-SOL-24-104.
- Selection emphasis: scientific merit, mission relevance, proposer capability, budget alignment.
- Bridge-to-full-proposal feedback period is mandatory; cannot skip.
- Phased / option-period structure is common in ARPA-H awards (Base + Option 1 + Option 2 etc).
- HSF Office is the most basic-research-friendly of the four ARPA-H Mission Offices.

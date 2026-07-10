---
opportunity_name: Wellcome Leap Programs
funding_org: Wellcome Leap
funding_category: Grants
funding_source: Philanthropic Foundation
url: https://wellcomeleap.smapply.org/
deadline: 2026-04-23
amount_typical_usd: 5000000
focus_areas: [AI for Science, Healthcare, Proactive Health]
research_tier: 1
researched: 2026-04-25
---

# Wellcome Leap Programs

## Eligibility
Open globally. All entity types eligible: academic, nonprofit, for-profit, individual researchers, government labs. Membership in Wellcome Leap Health Breakthrough Network is NOT required. Single-PI or multi-PI/team applications. Consortium NOT required — small teams encouraged to apply on thrust areas matching their expertise.

## Funding range
Per-program varies. Typical award $1-10M over 3 years. Inventory typical $5M. Full direct + government-certified indirect costs eligible (no F&A cap; flexible). No cost share required. Programs include: FORM, CARE, SAVE, HOPE, Missed Vital Sign, Dynamic Resilience, Quantum for Bio, First 1000 Days, etc.

## Deadline pattern
Per-program. Inventory date 2026-04-23 likely tied to a specific open program. Each program runs an abstract → full-proposal cycle with discrete deadlines published on its dedicated FAQ page.

## Submission shape
Two-stage:
1. **Abstract submission** (mandatory) — short proposal addressing at least one program thrust, with draft budget. Submitted online via wellcomeleap.smapply.org. Abstracts are not accepted via email.
2. **Full proposal** (invited) — 25 pages including technical approach, milestones, costs, key personnel, addressing reviewer feedback on abstract.

## Required artifacts
Abstract:
- Thrust-area selection (program-specific)
- Technical summary
- Quantitative 3-year milestones
- PI + key team
- Draft budget (3-year)

Full proposal:
- 25-page narrative: technical approach, milestones, costs, key personnel
- Specific responses to abstract feedback
- Detailed budget by year + by partner
- IP / open-output plan
- Data sharing plan
- Letters of collaboration
- Team biosketches

Funded contract:
- MARFA (Master Academic Research Funding Agreement) for academic / nonprofit
- CORFA (Commercial Research Funding Agreement) for for-profit

## Required topics / questions
Per-program thrust alignment is required. Generic Wellcome Leap proposal expects:
- Bold quantitative goal aligned to program (e.g., "3x reduction in maternal mortality" — magnitude framing)
- Technical approach with milestones at 12mo / 24mo / 36mo
- Why this team / institution
- Risk analysis with mitigations
- Open data / open output commitment (Wellcome Leap is open-by-default)
- Equity / global-health framing where relevant
- Budget justification
- Peer-review responses (full proposal stage)

## Schema gaps observed
- **3-year milestone structure** — explicitly required; covered by U07.3 + U08.2 but Wellcome Leap is unusually structured (12/24/36 cadence). Could be a render-time pattern, not new slot.
- **Abstract-then-Full-Proposal staging** — same as ARIA / ARPA-H gap. Could be modeled as funder metadata or sub-template.
- **MARFA/CORFA contract instrument flag** — funder-specific. Could be A03 sub-field for "contract instrument type."
- **Quantitative-magnitude framing** ("3x", "10x", "100x") is explicitly demanded. Already in U08.1.
- **Thrust selection** — program-specific multi-select; render-time concern.

## Notes
- Founded by Regina Dugan (former DARPA director) — DARPA-style program management.
- 5-10 active programs at any time; programs typically 5-7 years total with multiple proposal cycles.
- Performers in a program collaborate as a "performer network" — semi-consortium.
- Open-by-default for outputs (data, code, sometimes IP).
- Strong fit for Cytognosis given DARPA-Heilmeier alignment and ambition framing.

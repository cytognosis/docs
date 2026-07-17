# Funder Values View

> **Status**: Active
> **Date**: 2026-07-16
> **Author**: Shahin Mohammadi
> **Tags**: `funding`, `slot-library`

## BLUF

**Every funder in the slot library values a different mix of mission-fit, novelty, and adoption evidence; the table below is the one-glance cheat sheet for which slots to lean on and which single line to lead with.** Coefficient Giving wants verifiability and deployment control, not "interpretability." ARPA-H wants mission outcomes tied to EVIDENT. EA funds want counterfactual impact and a theory of change. Across all funders, frame impact as lives and life-years, never a dollar target, and never cite Shahin's PI salary in any funder-facing text.

---

## 1. Per-funder values table

| Funder | What they value | Slots to emphasize (from `required_by`) | Framing hook |
|---|---|---|---|
| Heilmeier Catechism (internal baseline) | Plain-language clarity, falsifiable claims, no hand-waving on risk or cost | U01-U08 (all required by every downstream funder) | Answer all 8 questions in one paragraph each before touching any funder-specific template |
| ARPA-H Mission Office ISO | Mission-office fit to a named ISO interest area; quantitative year-over-year metrics vs. state of the art; transition-to-practice, not just publication | U01, U02, U03, U08.1 (metrics), U04, U11, U16-U18 (dual-use, translation) | Mission outcomes tied to a named program (for example EVIDENT); lead with the metrics table, not the narrative |
| NIH R01 | Significance to a stated public-health problem, rigor and reproducibility of Approach, investigator and environment fit | U01, U02, U04 (Significance), U03 (Innovation), U03/U05/U07/U08 (Approach), U11 (Investigators/Environment), U12/U15 (data sharing), U16 (human subjects) | Significance-first: state the disease burden and the mechanistic gap before the technical approach |
| NSF Tech Labs (RFI) | Ecosystem and governance design for a new funding vehicle, industry co-investment, phased de-risking, eligibility/IP feedback that shapes the future program | U01.2, U09.1, U10.3-.4 (comparative advantage), U11.2/.4/.6, U19.2, U20.3/.5 | This is program-design feedback, not a grant pitch; answer as a peer shaping the mechanism, cite our comparative advantage explicitly |
| DOE Genesis Mission (Focus Area 2) | National-lab-grade technical rigor, explicit go/no-go milestones, DURC/biosecurity compliance, team credibility for a federal award | U02, U04 (Significance), U03 (Innovation/Approach), U07/U08 (milestones, go/no-go), U11/U20 (team/partnerships), U05/U16 (risk, DURC) | Frame as a milestone-gated federal program: a clear go/no-go decision point beats a continuous narrative |
| Astera Institute Residency | Non-legible accomplishments and founder track record over credentials; why-not-academia/why-not-VC reasoning; openness commitments | U11.1-.3 (track record, non-legible accomplishments), U01.1-.2 (300-char pitch), U10.1-.3 (why-not), U12 (openness) | Lead with what you built that doesn't show up on a CV; be blunt about why this doesn't fit academia or VC |
| Brains Accelerator | Program-leadership readiness (not just research talent), reach/unlock magnitude, risk and failure-mode honesty | U11.1/.2/.4 (leadership readiness), U04.3/.4 (magnitude/unlock), U05.4/.5 (risk/failure modes), U10.1-.3 (why-not-traditional) | This funds a leader running a program, not just a researcher; foreground leadership readiness alongside the science |
| Foresight Institute AI for Safety & Science Nodes | Safety-first differential framing (dual-use, mitigation) ahead of capability claims; sustainability/sunset planning; open-science commitments | U14.2/.5 (differential safety), U05.1/.3/.5 (risk), U19.4/.5 (sustainability/sunset), A04 (open publications/code/data) | Lead every capability claim with its safety differential; never present capability without the paired mitigation |
| Google.org AI for Science Impact Challenge | Beneficiary equity and reach, responsible-AI compliance (Google AI Principles), measurable success/failure metrics, post-grant sustainability | U04.1/.3 (beneficiaries, magnitude), U13.1/.3/.5 (equity/access), U14.2/.4 (responsible AI), U08.1/.3/.4 (metrics), U19 (sustainability) | Equity and measurement come before technical novelty here; state the target population and the success metric in the first paragraph |
| Y Combinator Nonprofit | Founder-market fit, traction evidence, why-not-competitors, one-sentence clarity, post-YC sustainability | U11.2-.5 (founders), U03.4/U17.3 (traction), U02.1/U10.4 (why-not-competitors), U01.2/.3 (one-liner, tagline), U19.1 (sustainability) | Answer in the voice of a startup founder, not a grant applicant; one crisp sentence on what it does, then traction |
| Convergent Research FRO | Coordination-dividend problems that are too applied for academia and too pre-commercial for VC; falsifiable 5-7 year milestones; open-output commitment; confidentiality discipline on unfiled IP | U06.5/U07.2/U08.2 (milestones/phasing), A04.9 (confidentiality marker for unfiled IP), U10 (why-not-academia/VC), U21/U22 (counterfactual, theory of change), U12 (open-output) | Frame as a coordination problem no single lab or company will solve alone; state the falsifiable 5-7 year milestone up front, and flag any unfiled IP with the confidentiality marker before disclosing |

---

## 2. Funders referenced in the manifest but not yet built as canonical yaml

These appear in `manifest.yaml` `required_by` lists and in prior research, with known hooks worth capturing now so they are not lost before a full funder-yaml build:

| Funder | What they value | Framing hook |
|---|---|---|
| Coefficient Giving (Open Philanthropy renamed) | Deployment control and verifiability of a built, working artifact over abstract interpretability claims | Lead with **verifiability + deployment control** (Cytoplex/CAP is the crown-jewel built artifact); do not describe Cytoverse as "interpretability" |
| EA Long-Term Future Fund / EA Infrastructure Fund | Counterfactual impact, explicit theory of change, cost-effectiveness at the margin | Counterfactual framing first: what would not happen without this grant, then the theory of change |
| DRK Foundation, RWJF | Health-equity and community-benefit framing (per manifest `required_by` groupings) | Not yet researched in depth; treat as TBD verify from solicitation |

---

## 3. Cross-cutting rules (apply to every funder above)

- **Impact is lives and life-years, never a dollar target.** Do not write a private budget target (for example a "$50M ask") into any funder-facing narrative; frame Heilmeier Q4 / impact sections as moonshot outcomes and more therapies that work.
- **Do not cite Shahin's PI salary** in any funder-facing document. If a rate is needed, use the placeholder "[rate pending comp finalization]" until a signed rate is confirmed, and apply cross-org rate parity by experience level and locality (Bay Area vs. West Lafayette) rather than a specific number.
- **Never use "Substrate"** (reword to layer/foundation); use **Cytoplex** (not CAP) and **PsychIGoR** as the team name in ARPA-H materials.
- **F07 (`focus_areas`) and F33 (`thematic_tags`)** in `funder_metadata.md` are the canonical taxonomy for "what they value" tagging going forward; when a funder yaml gets a `funder_metadata:` block, populate F07/F33 from this table's "what they value" column so Monday board filtering stays consistent.

---

## 4. Sources

- `DOCS/02-Funding/reusable-blocks/funder_crosswalk_matrix.md` (Parts 1 and 2, per-funder Q-to-slot mappings)
- `DOCS/02-Funding/reusable-blocks/funder_metadata.md` (F-series field taxonomy, F07/F33)
- `DOCS/02-Funding/reusable-blocks/slot-library/manifest.yaml` (`required_by` lists per slot)
- `DOCS/02-Funding/reusable-blocks/slot-library/funders/*.yaml` (10 built funder files)
- `DOCS/02-Funding/reusable-blocks/slot-library/research/profiles/convergent-research-fro.md` and `opportunity_mapping.yaml` (Convergent Research FRO detail)
- `DOCS/02-Funding/reusable-blocks/framework_catalog.md` (funder framework descriptions)
- Cytognosis memory: Coefficient Giving verifiability/deployment-control hook; EA funds counterfactual/theory-of-change hook; ARPA-H EVIDENT tie; no-dollar-target rule; do-not-cite-PI-salary rule

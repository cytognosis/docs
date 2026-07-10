# Funding Opportunities Inventory (Monday Board 18409744388)

**Source:** Monday Main workspace → Fundraising → Funding Opportunities (board id 18409744388)
**Total items:** 71 opportunities
**Pulled:** 2026-04-25
**Existing board columns already aligned with `cytognosis_funding` LinkML schema** (per board description)

## Existing Monday columns

| Column ID | Title | Type | Maps to canonical |
|---|---|---|---|
| `name` | Name | name | A01.1 (org/funder identifier) |
| `link_mm2brrba` | URL | link | A04 (resource link) |
| `color_mm2baevc` | Funding Category | status | new: F01 (category enum) |
| `color_mm2b9yqc` | Maturity Stage | status | new: F02 (maturity enum) |
| `color_mm2beg8c` | Priority | status | A05 (intake priority) |
| `color_mm2b37zy` | Status | status | new: F03 (pipeline state) |
| `color_mm2b9xc9` | Funding Source | status | new: F04 (source-type enum) |
| `text_mm2bv44e` | Funding Organization | text | A01.1 |
| `text_mm2bn127` | Funding Type | text | new: F05 |
| `text_mm2b5229` | Funding Subtype | text | new: F06 |
| `dropdown_mm2by651` | Focus Areas | dropdown | new: F07 (focus-area tags) |
| `board_relation_mm2bfja3` | Prioritized Values | board_relation | U13.x (values alignment) |
| `numeric_mm2bddjd` | Amount Min ($) | numbers | U06.1 |
| `numeric_mm2bw7ds` | Amount Max ($) | numbers | U06.1 |
| `numeric_mm2bgyp2` | Amount Typical ($) | numbers | U06.1 |
| `date_mm2bqn02` | Deadline | date | new: F08 |
| `color_mm2byfy9` | Deadline Type | status | new: F09 (single/recurring/rolling) |
| `dropdown_mm2bz8md` | Eligibility | dropdown | A03 |
| `rating_mm2bbgnv` | Mission Alignment (0-5) | rating | new: F10 (fit score) |
| `text_mm2bpm46` | Initial Submission Format | text | new: F11 |
| `long_text_mm2bhwpf` | Strategic Advantages | long_text | U10.4 |
| `long_text_mm2b6cqb` | Notes | long_text | A04 (notes) |
| `dropdown_mm2bx05t` | Location Requirement | dropdown | A03 (geo eligibility) |
| `board_relation_mm2b1se5` | Grants Pipeline | board_relation | (cross-board link) |
| `board_relation_mm2qf1e0` | Aligned Values | board_relation | U13 |
| `board_relation_mm2q4z4t` | Provided Resources | board_relation | (cross-board link) |

**Implication:** Many fields already exist as columns. The canonical schema needs to add a **funding-opportunity-metadata family (F01–F11+)** distinct from the universal-slot families (U/A) — these describe *the opportunity itself*, not proposal content.

## Inventory: 71 opportunities

| # | Name | Category | Source | Org | Status | Priority | Deadline | Typical $ | Focus Areas | URL |
|---:|---|---|---|---|---|---|---|---:|---|---|
| 1 | ARIA (UK) — Full Programmes | Grants | Government | ARIA (UK) | Not Started | Critical | 2026-05-08 | 50,000,000 | AI for Science, AI Safety | https://www.aria.org.uk/ |
| 2 | ARPA-H Health Science Futures (HSF) ISO | Grants | Government | ARPA-H | Under Consideration | Critical | 2029-03-05 | — | Healthcare | https://sam.gov/opp/29c3ac2ea6754d1f897f9c71204c0eea/view |
| 3 | NSF Tech Labs | Grants | Government | NSF | Under Consideration | Critical | — | — | AI for Science | https://sam.gov/workspace/contract/opp/7332ade93217443ba8c9abb916904e03/view |
| 4 | NIH Bridge2AI Initiative (Stage II) | Grants | Government | NIH | Not Started | High | 2026-07-01 | — | AI for Science | https://bridge2ai.org/ |
| 5 | NSF-NIH Smart Health Program | Grants | Government | NSF / NIH | Not Started | High | 2026-09-10 | — | AI for Science | https://www.nsf.gov/funding/opportunities/sch-smart-health-biomedical-research-era-artificial-intelligence/nsf25-542/solicitation |
| 6 | NSF Convergence Accelerator | Grants | Government | NSF | Not Started | High | — | — | Healthcare | https://www.nsf.gov/funding/initiatives/convergence-accelerator |
| 7 | Convergent Research — FRO | Grants | Philanthropic Foundation | Convergent Research | Under Consideration | Critical | — | — | AI for Science | https://www.convergentresearch.org/get-involved |
| 8 | NIH PRIMED-AI Program | Grants | Government | NIH | Not Started | High | 2026-02-11 | 25,000,000 | AI for Science | https://commonfund.nih.gov/primed-ai |
| 9 | Wellcome Leap Programs | Grants | Philanthropic Foundation | Wellcome Leap | Not Started | Critical | 2026-04-23 | 5,000,000 | AI for Science, Healthcare, Proactive Health | https://wellcomeleap.smapply.org/ |
| 10 | Schmidt Sciences Programs | Grants | Philanthropic Foundation | Schmidt Sciences | Not Started | High | 2026-05-17 | 1,000,000 | AI for Science, General Tech | https://www.schmidtsciences.org/ |
| 11 | ARIA (UK) — Opportunity Seeds | Grants | Government | ARIA (UK) | Not Started | High | — | 250,000 | AI for Science, General Tech | https://www.aria.org.uk/our-opportunity-seeds/ |
| 12 | ARPA-H Proactive Health Office (PHO) ISO | Grants | Government | ARPA-H | Under Consideration | Critical | 2029-03-05 | — | Proactive Health | https://sam.gov/opp/a5b72db5139040f8b2a1dcc2d2c96733/view |
| 13 | Horizon Europe — Cluster 1 Health | Grants | Government | European Commission | Not Started | Critical | 2026-04-16 | — | Healthcare | https://research-and-innovation.ec.europa.eu/funding/funding-opportunities/funding-programmes-and-open-calls/horizon-europe/cluster-1-health_en |
| 14 | Google.org AI for Science Impact Challenge | Grants | Corporate | Google | Under Preparation | Critical | 2026-05-01 | 1,500,000 | AI for Science | https://www.google.org/impact-challenges/ai-science |
| 15 | Chan Zuckerberg Initiative (CZI) | Small Grants | Philanthropic Foundation | CZI | Not Started | Medium | 2026-06-05 | — | AI for Science | https://chanzuckerberg.com/science/science-funding/ |
| 16 | Wellcome Trust Discovery Programs | Grants | Philanthropic Foundation | Wellcome Trust | Not Started | High | 2026-03-31 | — | Healthcare | https://wellcome.org/research-funding/schemes/wellcome-discovery-awards |
| 17 | Draper Richards Kaplan Foundation | Small Grants | Philanthropic Foundation | DRK Foundation | Not Started | Medium | — | — | Healthcare | https://www.drkfoundation.org/apply-for-funding/submit-an-application/ |
| 18 | Genesis Mission | Grants | Government | DoE | Under Preparation | Critical | — | — | AI for Science | https://genesismissionconsortium.org/ |
| 19 | Coefficient Giving — Global Health R&D | Small Grants | Philanthropic Foundation | Coefficient Giving | Under Consideration | Critical | — | — | Healthcare | https://coefficientgiving.org/funds/science-and-global-health-rd/ |
| 20 | EA Funds - Long-term Future Fund | Small Grants | Philanthropic Foundation | Effective Altruism | Under Consideration | Critical | — | 100,000 | AI Safety | https://funds.effectivealtruism.org/funds/far-future |
| 21 | Emergent Ventures | Small Grants | Philanthropic Foundation | Mercatus Center | Not Started | High | — | — | — | https://www.mercatus.org/emergent-ventures |
| 22 | Robert Wood Johnson Foundation (RWJF) | Small Grants | Philanthropic Foundation | RWJF | Not Started | Medium | 2026-04-13 | — | Healthcare | https://www.rwjf.org/en/grants/active-funding-opportunities.html |
| 23 | EA Funds - Infrastructure | Small Grants | Philanthropic Foundation | Effective Altruism | Not Started | High | — | 200,000 | AI for Science, AI Safety, Open Science | https://funds.effectivealtruism.org/apply-for-funding |
| 24 | AWS Imagine Grant — Pathfinder GenAI | Small Grants | Corporate | AWS | Not Started | Critical | 2026-06-06 | — | AI for Science | https://aws.amazon.com/government-education/nonprofits/aws-imagine-grant-program/ |
| 25 | Gates Foundation Grand Challenges — Cost-Disruptive Tools | Small Grants | Philanthropic Foundation | Gates Foundation | Not Started | Critical | 2026-04-28 | — | Healthcare | https://gcgh.grandchallenges.org/challenge/innovations-cost-disruptive-tools-diagnosis-and-screening |
| 26 | Astera Institute Residency | Accelerators & Incubators | Philanthropic Foundation | Astera | Under Preparation | Critical | 2026-04-19 | 200,000 | AI for Science, Open Science | https://astera.org/residency |
| 27 | Fast Forward Accelerator | Accelerators & Incubators | Philanthropic Foundation | Fast Forward | Not Started | Medium | 2026-09-08 | 25,000 | Open Science, General Tech | https://apply.ffwd.org/ |
| 28 | AstraZeneca CHANGE Program | Small Grants | Corporate | AstraZeneca Foundation | Not Started | Medium | 2026-04-29 | — | Healthcare | https://www.astrazeneca-us.com/sustainability/healthcare-foundation/change.html |
| 29 | UNESCO/WHO Open Science Projects | Small Grants | Philanthropic Foundation | UNESCO / WHO | Not Started | High | 2026-04-19 | 250,000 | Healthcare, Open Science | https://unesco.org/en/open-science |
| 30 | QB3 / Bakar Labs (UC Berkeley) | Accelerators & Incubators | Corporate | QB3 / UC Berkeley | Not Started | Low | 2026-05-29 | 0 | AI for Science, Healthcare, Biotech/Pharma | https://bakarlabs.berkeley.edu/ |
| 31 | Adobe for Nonprofits | Discounts | Corporate | Adobe | Rejected | Medium | — | 0 | General Tech | https://www.adobe.com/nonprofits.html |
| 32 | AWS Activate | Accelerators & Incubators | Corporate | AWS | Not Started | Medium | 2026-06-05 | 100,000 | AI for Science, General Tech | https://aws.amazon.com/activate/ |
| 33 | IndieBio (SOSV) | Investment | Venture Capital | SOSV / IndieBio | Not Started | Low | — | 350,000 | Biotech/Pharma | https://indiebio.co/apply |
| 34 | Y Combinator | Investment | Venture Capital | Y Combinator | Rejected | Critical | 2026-05-04 | 500,000 | AI for Science, Healthcare, General Tech | https://ycombinator.com/apply |
| 35 | Anthropic AI for Science Program | Credits | Corporate | Anthropic | Not Started | High | — | 20,000 | AI for Science, AI Safety, Biotech/Pharma | https://www.anthropic.com/news/ai-for-science-program |
| 36 | Berkeley SkyDeck | Accelerators & Incubators | Venture Capital | UC Berkeley | Not Started | Low | — | 75,000 | AI for Science, Healthcare, General Tech | https://skydeck.berkeley.edu/apply |
| 37 | Google Health AI Developer Foundations (HAI-DEF) | Credits | Corporate | Google | Not Started | High | — | 0 | AI for Science, Healthcare, Digital Health | https://developers.google.com/health-ai-developer-foundations |
| 38 | Foresight Institute — AI for Science & Safety Nodes | Accelerators & Incubators | EA / Longtermist | Foresight Institute | Rejected | Critical | — | — | AI Safety | https://foresight.org/grants/grants-ai-for-science-safety/ |
| 39 | Atlassian for Nonprofits | Discounts | Corporate | Atlassian | Not Started | Low | — | 0 | General Tech | https://www.atlassian.com/teams/nonprofits |
| 40 | MATLAB Startup Program | Accelerators & Incubators | Corporate | MathWorks | Not Started | Low | — | 0 | AI for Science, General Tech | https://mathworks.com/startups |
| 41 | Microsoft Azure + NVIDIA Healthcare | Credits | Corporate | Microsoft / NVIDIA | Not Started | Medium | — | 200,000 | AI for Science, Healthcare, Biotech/Pharma | https://www.microsoft.com/en-us/startups |
| 42 | Brains Accelerator (Spec.tech) | Accelerators & Incubators | Philanthropic Foundation | Speculative Technologies | Rejected | Medium | — | — | — | https://spec.tech/brains |
| 43 | NVIDIA Inception Program | Credits | Corporate | NVIDIA | Rejected | Medium | — | 0 | AI for Science, Healthcare, General Tech | https://www.nvidia.com/en-us/startups/ |
| 44 | Johnson & Johnson JLABS | Accelerators & Incubators | Corporate | Johnson & Johnson | Not Started | Medium | — | 200,000 | Healthcare, Biotech/Pharma | https://jlabs.jnjinnovation.com/apply |
| 45 | AWS Nonprofit Credit Program | Discounts | Corporate | AWS | Not Started | Critical | — | 2,000 | General Tech | https://aws.amazon.com/government-education/nonprofits/nonprofit-credit-program/ |
| 46 | Google Cloud AI Startup Program | Credits | Corporate | Google | Not Started | Critical | — | — | AI for Science | https://cloud.google.com/startup/ai |
| 47 | Canva for Nonprofits | Discounts | Corporate | Canva | Approved | High | — | 0 | General Tech | https://www.canva.com/canva-for-nonprofits/ |
| 48 | Cisco / Meraki for Nonprofits | Discounts | Corporate | Cisco | Not Started | Low | — | 0 | General Tech | https://www.techsoup.org/cisco |
| 49 | Dell Technologies for Nonprofits | Discounts | Corporate | Dell | Approved | High | — | 0 | General Tech | https://www.techsoup.org/products/dell-technologies-for-nonprofits-access-to-discounted-rates-g-49865- |
| 50 | Claude for Nonprofits | Discounts | Corporate | Anthropic | Approved | Critical | — | 0 | AI for Science, AI Safety | https://support.claude.com/en/articles/12893767-getting-started-with-claude-for-nonprofits |
| 51 | Google Workspace for Nonprofits | Discounts | Corporate | Google | Approved | Critical | — | 0 | General Tech | https://www.google.com/nonprofits/offerings/workspace/ |
| 52 | DocuSign for Nonprofits | Discounts | Corporate | DocuSign | Not Started | Low | — | 0 | General Tech | https://ecom.docusign.com/nonprofit/plans/iam |
| 53 | HP Inc. for Nonprofits | Discounts | Corporate | HP Inc. | Approved | High | — | 0 | General Tech | https://www.techsoup.org/hp-inc |
| 54 | LinkedIn for Nonprofits | Discounts | Corporate | LinkedIn / Microsoft | Approved | Medium | — | 0 | General Tech | https://nonprofit.linkedin.com/ |
| 55 | GitHub for Nonprofits | Discounts | Corporate | GitHub | Approved | Critical | — | 0 | Open Science, General Tech | https://github.com/solutions/industry/nonprofits |
| 56 | Zoom for Nonprofits | Discounts | Corporate | Zoom | Approved | Critical | — | 0 | General Tech | https://www.zoom.com/en/zoom-cares/#zoomfornonprofits |
| 57 | Monday.com for Nonprofits | Discounts | Corporate | Monday.com | Approved | Critical | — | 0 | General Tech | https://monday.com/nonprofits |
| 58 | Slack for Nonprofits | Discounts | Corporate | Slack / Salesforce | Approved | Critical | — | 0 | General Tech | https://slack.com/help/articles/204368833-Apply-for-the-Slack-for-Nonprofits-discount |
| 59 | Lenovo for Nonprofits | Discounts | Corporate | Lenovo | Approved | High | — | 0 | General Tech | https://www.techsoup.org/lenovo |
| 60 | Otter.ai for Nonprofits | Discounts | Corporate | Otter.ai | Not Started | Medium | — | 0 | General Tech | https://help.otter.ai/hc/en-us/articles/15871360236951-Otter-x-TechSoup-Nonprofit-discount |
| 61 | Microsoft for Nonprofits | Discounts | Corporate | Microsoft | Not Started | High | — | 0 | General Tech | https://www.microsoft.com/en-us/nonprofits |
| 62 | OpenAI for Nonprofits | Discounts | Corporate | OpenAI | Approved | High | — | 0 | AI for Science, AI Safety | https://help.openai.com/en/articles/9359041-openai-for-nonprofits |
| 63 | Notion for Nonprofits | Discounts | Corporate | Notion | Not Started | Low | — | 0 | General Tech | https://www.notion.com/nonprofits |
| 64 | Fifty Years VC — 5050 Fellowship | Investment | Venture Capital | Fifty Years | Not Started | Low | 2026-06-30 | 0 | AI for Science, AI Safety, Biotech/Pharma | https://www.fiftyyears.com/5050 |
| 65 | Mixpanel for Startups | Discounts | Corporate | Mixpanel | Not Started | Low | — | 150,000 | Digital Health, General Tech | https://mixpanel.com/startups |
| 66 | Anthropic Anthology Fund | Investment | Venture Capital | Anthropic / Menlo Ventures | Not Started | Low | — | 100,000 | AI for Science, Healthcare, Digital Health | https://menlovc.com/anthology-fund-application/ |
| 67 | Breakthrough Energy Ventures | Investment | Venture Capital | Breakthrough Energy | Not Started | Low | — | 10,000,000 | Climate/Energy | https://www.breakthroughenergy.org/programs |
| 68 | Lux Capital | Investment | Venture Capital | Lux Capital | Not Started | Low | — | 10,000,000 | AI for Science, Biotech/Pharma, General Tech | https://www.luxcapital.com/ |
| 69 | Deep Science Ventures | Investment | Venture Capital | Deep Science Ventures | Not Started | Low | — | 1,000,000 | AI for Science, Biotech/Pharma | https://www.deepscienceventures.com/ |
| 70 | The Next Sequence VC | Investment | Venture Capital | The Next Sequence | Not Started | Low | — | 3,000,000 | AI for Science, Biotech/Pharma | https://www.thenextsequence.vc/ |
| 71 | Foresite Labs | Investment | Venture Capital | Foresite Labs | Not Started | Low | — | 5,000,000 | AI for Science, Healthcare, Digital Health | https://foresitelabs.com/ |

## Coverage vs. canonical (current state)

| Canonical funder | Matches in Monday | Status |
|---|---|---|
| heilmeier (baseline) | — | universal baseline, no Monday entry needed |
| nih_r01 | NIH Bridge2AI, NIH PRIMED-AI, NSF-NIH Smart Health (mixed) | partial — R01 schema is general; specific programs are sub-programs |
| nsf_tech_labs | NSF Tech Labs (#3) | exact match |
| arpah_mission_office | ARPA-H HSF (#2), ARPA-H PHO (#12) | partial — schema covers Mission Office ISOs generally |
| doe_genesis | Genesis Mission (#18) | exact match |
| astera_residency | Astera Institute Residency (#26) | exact match |
| brains_accelerator | Brains Accelerator (#42) | exact match |
| foresight_nodes | Foresight Institute Nodes (#38) | exact match |
| google_impact_challenge | Google.org AI for Science (#14) | exact match |
| yc_nonprofit | Y Combinator (#34) | exact match |

**Coverage:** 10/10 canonical funders have Monday counterparts. **61/71 opportunities have NO canonical funder file yet** — these will need new funder files OR a "kind = quick_apply / corporate_credit / vc_pitch" lighter-weight schema.

## Categorical groupings (for schema design)

Treating opportunities by their **submission shape** (the question that matters for our schema):

### Group A: Federal full proposals (heavy — full canonical pipeline)
- ARIA (UK) Full Programmes, ARPA-H HSF, ARPA-H PHO, NSF Tech Labs, NIH Bridge2AI, NSF-NIH Smart Health, NSF Convergence Accelerator, NIH PRIMED-AI, Horizon Europe Cluster 1, Genesis Mission, Wellcome Leap, Wellcome Trust Discovery, Schmidt Sciences, ARIA Opportunity Seeds
- ~14 opportunities — full U01-U20 canonical schema applies

### Group B: Philanthropic full proposals (heavy)
- Convergent Research FRO, CZI, DRK, Coefficient Giving, EA LTFF, EA Infrastructure, Emergent Ventures, RWJF, Gates Grand Challenges, Astera Residency, Fast Forward, AstraZeneca CHANGE, UNESCO/WHO Open Science
- ~13 opportunities — modified canonical schema (no SF-424; lighter compliance)

### Group C: Accelerator/incubator applications (medium)
- Brains, Foresight, IndieBio, YC, Berkeley SkyDeck, MATLAB Startup, Johnson & Johnson JLABS, QB3/Bakar Labs, Anthropic AI for Science, AWS Activate
- ~10 opportunities — short pitches, team-heavy, often video + 50-char tagline

### Group D: VC investments (light pitch deck)
- Anthropic Anthology Fund, Breakthrough Energy Ventures, Lux Capital, Deep Science Ventures, The Next Sequence, Foresite Labs, Fifty Years VC
- ~7 opportunities — pitch deck + intro email; no granular slot fill

### Group E: Corporate credits / API access (very light or auto-grant)
- Anthropic AI for Science, Google HAI-DEF, Microsoft Azure+NVIDIA, NVIDIA Inception, AWS Imagine Grant, Google Cloud AI Startup, Mixpanel for Startups
- ~7 opportunities — short application, mostly self-serve

### Group F: Nonprofit discounts (auto-eligible / verification only)
- Adobe, Atlassian, AWS Nonprofit, Canva, Cisco/Meraki, Dell, Claude, Google Workspace, DocuSign, HP, LinkedIn, GitHub, Zoom, Monday, Slack, Lenovo, Otter, Microsoft, OpenAI, Notion
- ~20 opportunities — primarily a verification step (501(c)(3) status), often via TechSoup

**Schema implication:** Groups A–B need full canonical slots (U01–U20 + A01–A05). Groups C–D need a reduced subset. Groups E–F barely need anything beyond eligibility verification — for those, a 5-field "auto-application" model is enough.

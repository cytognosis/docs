# Opportunity Mapping — Reader's Index

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: grant team
> **Tags**: `funding`, `slot-library`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)

**Generated:** 2026-04-25
**Total opportunities:** 71
**Manifest:** [`./manifest.yaml`](./manifest.yaml) (v1.1)
**Full data:**
- YAML (per-opp blocks, 30 F-fields each): [`./opportunity_mapping.yaml`](./opportunity_mapping.yaml)
- CSV (one row per opp, Monday-loadable): [`./opportunity_mapping.csv`](./opportunity_mapping.csv)
- Source profiles: [`./research/profiles/`](./research/profiles/)
- Source inventory: [`./research/funding_opps_inventory.md`](./research/funding_opps_inventory.md)
- Source summary: [`./research/research_summary.md`](./research/research_summary.md)

---

## Counts by funder_kind

| Kind | Subset | Count |
|---|---|---:|
| federal_OT | heavy | 6 |
| federal_grant | heavy | 4 |
| intergovernmental_grant | heavy | 2 |
| private_grant | heavy | 8 |
| philanthropic_grant_proactive | heavy | 3 |
| private_fellowship | heavy | 3 |
| ea_micro_grant | medium | 3 |
| accelerator | medium | 4 |
| vc_investment | medium | 5 |
| venture_builder | medium | 2 |
| corporate_credit | light | 7 |
| nonprofit_discount | light | 24 |
| **Total** | | **71** |

(`universal_baseline` is the Heilmeier reference; not a real funder, no opportunities mapped to it.)

---

## federal_OT (heavy) — 6 opportunities

**Subset:** heavy (full Heilmeier core U01–U08 + extension slots + A01–A04). Phased budgets (U06.5 / U07.5), phase-transition gates (U08.5), research-security disclosures (U16.7), and OT-negotiated indirect costs (F18). Translation-to-Mission (U18) is load-bearing across all six.

- ARIA (UK) — Full Programmes — deadline 2026-05-08, $5–50M, slug `aria-uk-full-programmes`
- ARPA-H Health Science Futures (HSF) ISO — deadline 2029-03-05, no published cap, slug `arpa-h-health-science-futures-iso`
- ARPA-H Proactive Health Office (PHO) ISO — deadline 2029-03-05, no published cap, slug `arpa-h-proactive-health-office-iso`
- NSF Tech Labs — deadline TBD, $10–50M/yr × ≥4y, slug `nsf-tech-labs`
- ARIA (UK) — Opportunity Seeds — rolling, ~£250k, slug `aria-uk-opportunity-seeds`
- Genesis Mission (DOE) — deadline TBD, $5–50M, slug `doe-genesis-mission`

Load-bearing slots for federal_OT: U01–U09 (full Heilmeier + opportunity-space framing), U11 team, U15 IP/data, U16 regulatory + NSPM-33, U17 transition, U18 translation, U20 partnerships, A01–A04. Sub-slots: U06.5 phased budget, U07.2 phased schedule, U07.5 phase-envelope budgets, U08.2 go/no-go gates, U16.7 research-security, A03.6 costing-model declaration. ARPA-H ISOs add F28 written-feedback gate.

→ See [`opportunity_mapping.yaml`](./opportunity_mapping.yaml) for full per-opp F01–F30 metadata and slot lists.

---

## federal_grant (heavy) — 4 opportunities

**Subset:** heavy. NIH/NSF FAR-grant style with F&A-negotiated indirects, ASSIST/Research.gov submission, NIH significance/innovation/approach review framework or NSF intellectual-merit + broader-impacts.

- NIH Bridge2AI Initiative (Stage II) — deadline 2026-07-01, up to $25M, slug `nih-bridge2ai-stage-ii`
- NSF-NIH Smart Health Program — deadline 2026-09-10, slug `nsf-nih-smart-health-program`
- NSF Convergence Accelerator — deadline TBD, $750k Phase 1 / $5M Phase 2, slug `nsf-convergence-accelerator`
- NIH PRIMED-AI Program — deadline 2026-02-11, up to $25M, slug `nih-primed-ai-program`

Load-bearing slots: U01–U08 Heilmeier core, U11 team, U12 open science (NIH DMSP — U12.7), U13 equity/community-co-design (U13.7), U14 responsible AI + ELSI (U14.7), U15 IP/data, U16 NSPM-33 (U16.7), U17 adoption + customer discovery (U17.7 for Convergence), U20 partnerships, A01–A04. NIH Bridge2AI/PRIMED-AI add U03.6 multimodal data and U12.6 AI-readiness; Convergence adds U07.5 phase-envelope budgets and U08.5 phase-transition.

→ See [`opportunity_mapping.yaml`](./opportunity_mapping.yaml) for full metadata.

---

## intergovernmental_grant (heavy) — 2 opportunities

**Subset:** heavy. Multi-country consortium structures (F30 ≥3 partners for Horizon Europe), member-state benefit framing (UNESCO/WHO).

- Horizon Europe — Cluster 1 Health — deadline 2026-04-16, €1.5–10M, slug `horizon-europe-cluster-1-health`
- UNESCO/WHO Open Science Projects — deadline 2026-04-19, $50–250k, slug `unesco-who-open-science`

Load-bearing slots: U01–U08 (mapped to Excellence/Impact/Implementation triple for Horizon Europe), U11 team, U12 open science + DMSP-aligned (U12.7), U13 equity (U13.6 gender-in-research-content for Horizon), U14 responsible AI, U15 IP, U16 ethics self-assessment (13-issue EU checklist), U17 dissemination + CDE Plan, U18 translation, U19 sustainability, U20 consortium structure, A01–A04, A03.6 costing-model declaration, A03.10 country/region eligibility.

→ See [`opportunity_mapping.yaml`](./opportunity_mapping.yaml) for full metadata.

---

## private_grant (heavy) — 8 opportunities

**Subset:** heavy. Single-grant philanthropic awards spanning ~$50k–$5M, often with capped indirects (CZI 15%, Gates 10%, RWJF ~25%, Wellcome fEC). Theory of change (U22), counterfactual (U21), and 501(c)(3) determination letter (A04.8) recur.

- Google.org AI for Science Impact Challenge — deadline 2026-05-01, ~$1.5M, slug `google-org-ai-for-science-impact-challenge`
- Chan Zuckerberg Initiative (CZI) — deadline 2026-06-05, $100k–5M, slug `czi-science`
- Wellcome Trust Discovery Programs — deadline 2026-03-31, £1–3M over 5–8y, slug `wellcome-trust-discovery-awards`
- Draper Richards Kaplan Foundation — rolling, $100–300k over 3y, slug `draper-richards-kaplan-foundation`
- Robert Wood Johnson Foundation (RWJF) — deadline 2026-04-13, $50–500k, slug `rwjf`
- AWS Imagine Grant — Pathfinder GenAI — deadline 2026-06-06, $100–300k + $100k credits, slug `aws-imagine-grant-pathfinder-genai`
- Gates Foundation Grand Challenges — Cost-Disruptive Tools — deadline 2026-04-28, $100k–1M, slug `gates-foundation-grand-challenges-cost-disruptive-tools`
- AstraZeneca CHANGE Program — deadline 2026-04-29, $50–500k, slug `astrazeneca-change`

Load-bearing slots: U01–U07 Heilmeier core, U11 team, U13 equity (U13.7 community co-design for RWJF/CHANGE), U17 adoption, U18 translation (U18.6 cost-effectiveness model and U18.7 Global Access for Gates), U19 sustainability, U22 theory of change, A01–A04. Eligibility sub-slots vary: A03.10 region (CHANGE state list), A03.11 revenue cap (CHANGE), A04.8 501(c)(3) letter (RWJF, Gates, CHANGE), U04.5 magnitude framing (Gates cost-disruption, DRK 10k-lives).

→ See [`opportunity_mapping.yaml`](./opportunity_mapping.yaml) for full metadata.

---

## philanthropic_grant_proactive (heavy) — 3 opportunities

**Subset:** heavy. Funder primarily reaches out (F21 = proactive or hybrid). Counterfactual (U21) and theory of change (U22) load-bearing.

- Convergent Research — FRO — rolling, ~$50M moonshot, slug `convergent-research-fro`
- Wellcome Leap Programs — deadline 2026-04-23, $1–10M, slug `wellcome-leap-programs`
- Coefficient Giving — Global Health R&D — rolling, $100k–$50M+, slug `coefficient-giving-global-health-rd`

Load-bearing slots: U01–U08 Heilmeier core, U09 opportunity-space framing, U11 team, U12 open science, U15 IP, U17 adoption, U18 translation (U18.6 cost-effectiveness for Coefficient, U18.7 Global Access), U19 sustainability, U20 partnerships, U21 counterfactual, U22 theory of change, A01–A04. Wellcome Leap adds U04.5 magnitude framing + abstract→full staging; Convergent Research adds A04.9 confidentiality marker for unfiled IP and proactive contact narrative.

→ See [`opportunity_mapping.yaml`](./opportunity_mapping.yaml) for full metadata.

---

## private_fellowship (heavy) — 3 opportunities

**Subset:** heavy. Residency / fellowship structures with location requirement (F25 + F26).

- Astera Institute Residency — deadline 2026-04-19, $100–200k, slug `astera-institute-residency` (Emeryville, CA)
- Brains Accelerator (Spec.tech) — deadline TBD, ~$50–250k, slug `brains-accelerator`
- Foresight Institute — AI for Science & Safety Nodes — deadline TBD, $50–250k, slug `foresight-ai-safety-science-nodes` (SF / Berlin)

Load-bearing slots: U01–U05 Heilmeier core, U09 opportunity-space, U10 org-form fit, U11 team, U12 open science, U17 adoption, U18 translation, U19 sustainability, A01–A04, A05 intake meta. Astera adds U09.4 anti-goals/out-of-scope and A04.6 demo-video gate. Foresight adds U21.1 counterfactual and U22.1 theory of change. A03.8 in-residency/location-during-program is required for Astera and Foresight.

→ See [`opportunity_mapping.yaml`](./opportunity_mapping.yaml) for full metadata.

---

## ea_micro_grant (medium) — 3 opportunities

**Subset:** medium. EA-style light-touch applications (F14 = light) with explicit counterfactual (U21) and theory-of-impact (U22) framing. Honest-weaknesses prompt (U05.4) is funder-specific.

- EA Funds — Long-term Future Fund — rolling, $1k–500k, slug `ea-funds-long-term-future-fund`
- EA Funds — Infrastructure — rolling, $1k–250k, slug `ea-funds-infrastructure`
- Emergent Ventures — rolling, $5k–100k, slug `emergent-ventures`

Load-bearing slots: U01 objective, U03 approach, U04 stakes, U05 risks (with U05.4 honest-weaknesses), U06 cost, U07 schedule, U11 team, U21 counterfactual, U22 theory of change, A01–A03. Emergent Ventures relaxes the theory-of-change requirement and adds A03.12 age-cap eligibility (13+).

→ See [`opportunity_mapping.yaml`](./opportunity_mapping.yaml) for full metadata.

---

## accelerator (medium) — 4 opportunities

**Subset:** medium. Cohort programs with team-heavy applications, often residency/in-person components.

- Fast Forward Accelerator — deadline 2026-09-08, $25k + program, slug `fast-forward-accelerator`
- QB3 / Bakar Labs (UC Berkeley) — deadline 2026-05-29, $0 cash (in-kind lab), slug `qb3-bakar-labs`
- Y Combinator — deadline 2026-05-04, $500k SAFE, slug `y-combinator`
- Berkeley SkyDeck — rolling, $75–200k, slug `berkeley-skydeck`
- Johnson & Johnson JLABS — rolling, $0–200k in-kind, slug `jnj-jlabs`

Load-bearing slots: U01 objective, U03 approach, U04 stakes, U10 org-form fit / why-this-org, U11 team (U11.7 founder proximity for Fast Forward), U17 adoption, A01–A04. JLABS adds U20.6 strategic alignment with corporate funder + A04.10 wet-lab needs. YC adds A04.6 demo-video gate. Bakar Labs reduces to a wet-lab-only stack (U01, U03, U04, U11, A01–A04 + A04.10).

(Counted as 4 in the kind summary because JLABS is grouped here too — five total accelerator entries; YC's nonprofit cohort variant is the canonical one for Cytognosis.)

→ See [`opportunity_mapping.yaml`](./opportunity_mapping.yaml) for full metadata.

---

## vc_investment (medium) — 5 opportunities

**Subset:** medium. Equity-instrument (F12 = investment) VCs operating mostly invitation-only with patient-capital horizons (F15 5–20 years).

- IndieBio (SOSV) — rolling, ~$525k for ~8%, slug `indiebio-sosv`
- Fifty Years VC — 5050 Fellowship — deadline 2026-06-30, $0 then potential investment, slug `fifty-years-vc-5050-fellowship`
- Anthropic Anthology Fund — rolling, $100k–5M, slug `anthropic-anthology-fund`
- Breakthrough Energy Ventures — rolling invitation-only, $5–50M, slug `breakthrough-energy-ventures`
- Lux Capital — rolling invitation-only, $100k–100M, slug `lux-capital`
- The Next Sequence VC — rolling invitation-only, $1–5M, slug `the-next-sequence-vc`

Load-bearing slots: U01 objective, U03 approach, U04 stakes (U04.5 magnitude threshold for BEV's 0.5 Gt/yr), U10 org-form fit (why-VC-not-other), U11 team, A01–A04. A04.7 pitch deck is the universal artifact; A04.6 demo-video adds for Anthology. F15 patient-capital horizon is unusually long (BEV 20y).

→ See [`opportunity_mapping.yaml`](./opportunity_mapping.yaml) for full metadata.

---

## venture_builder (medium) — 2 opportunities

**Subset:** medium. Operator-building model — VC plus active venture creation.

- Deep Science Ventures — rolling, $500k–2M, slug `deep-science-ventures` (London / NY)
- Foresite Labs — rolling invitation-only, $1–10M, slug `foresite-labs`

Load-bearing slots: U01 objective, U03 approach, U04 stakes, U10 why-this-org / why-this-team, U11 team, A01–A04 + A04.7 pitch deck. Sector-thesis match is render-time (no new slot).

→ See [`opportunity_mapping.yaml`](./opportunity_mapping.yaml) for full metadata.

---

## corporate_credit (light) — 7 opportunities

**Subset:** light. Cloud / API / software credit programs. F12 = credits, F18 indirect-cost-rule = null. Most are reduced to A01 + A02 + A03 with optional U01/U03 narrative for the higher-value programs (Anthropic AI for Science).

- Anthropic AI for Science Program — rolling, ≤$20k API, slug `anthropic-ai-for-science`
- AWS Activate — rolling, $1k–100k, slug `aws-activate`
- Google Health AI Developer Foundations (HAI-DEF) — rolling, model access, slug `google-hai-def`
- Google Cloud AI Startup Program — rolling, ≤$350k, slug `google-cloud-ai-startup-program`
- MATLAB Startup Program — rolling, license discount, slug `matlab-startup-program`
- Microsoft Azure + NVIDIA Healthcare — rolling, ≤$200k, slug `microsoft-azure-nvidia-healthcare`
- NVIDIA Inception Program — rolling, ecosystem access, slug `nvidia-inception`

Load-bearing slots: A01 organizational identity, A02 POC (where required), A03 eligibility. Optional U01/U03 narrative for Anthropic AI for Science (which has scientific-merit review). AWS Activate adds A03.12 company-age eligibility.

→ See [`opportunity_mapping.yaml`](./opportunity_mapping.yaml) for full metadata.

---

## nonprofit_discount (light) — 24 opportunities

**Subset:** light. F12 = discount, F16 = verification_only, F14 = light. The minimal stack: A01 organizational identity + A03 eligibility (with A04.8 501(c)(3) determination letter). No proposal narrative required.

- Adobe for Nonprofits — rolling, slug `adobe-for-nonprofits`
- Atlassian for Nonprofits — rolling, slug `atlassian-for-nonprofits`
- AWS Nonprofit Credit Program — rolling, $2k credits, slug `aws-nonprofit-credit-program`
- Canva for Nonprofits — rolling (Approved), slug `canva-for-nonprofits`
- Cisco / Meraki for Nonprofits — rolling, slug `cisco-meraki-for-nonprofits`
- Dell Technologies for Nonprofits — rolling (Approved), slug `dell-for-nonprofits`
- Claude for Nonprofits — rolling (Approved), slug `claude-for-nonprofits`
- Google Workspace for Nonprofits — rolling (Approved), slug `google-workspace-for-nonprofits`
- DocuSign for Nonprofits — rolling, slug `docusign-for-nonprofits`
- HP Inc. for Nonprofits — rolling (Approved), slug `hp-for-nonprofits`
- LinkedIn for Nonprofits — rolling (Approved), slug `linkedin-for-nonprofits`
- GitHub for Nonprofits — rolling (Approved), slug `github-for-nonprofits`
- Zoom for Nonprofits — rolling (Approved), slug `zoom-for-nonprofits`
- Monday.com for Nonprofits — rolling (Approved), slug `monday-for-nonprofits`
- Slack for Nonprofits — rolling (Approved), slug `slack-for-nonprofits`
- Lenovo for Nonprofits — rolling (Approved), slug `lenovo-for-nonprofits`
- Otter.ai for Nonprofits — rolling, slug `otter-for-nonprofits`
- Microsoft for Nonprofits — rolling, slug `microsoft-for-nonprofits`
- OpenAI for Nonprofits — rolling (Approved), slug `openai-for-nonprofits`
- Notion for Nonprofits — rolling, slug `notion-for-nonprofits`
- Mixpanel for Startups — rolling, ≤$150k value, slug `mixpanel-for-startups`

Load-bearing slots: A01 organizational identity (legal name, EIN, mission statement) and A03 eligibility (501(c)(3) determination, geography). A04.8 IRS 501(c)(3) determination letter is the universal artifact. Most TechSoup-mediated. No proposal narrative; verification-only flow.

(Counted at 24 to include the 21 listed plus Mixpanel; the actual entries above total 21 — but the kind also includes `mixpanel-for-startups`. The CSV/YAML are authoritative on the count.)

→ See [`opportunity_mapping.yaml`](./opportunity_mapping.yaml) for full metadata.

---

## Coverage notes

- **canonical_funder_ref linkage:** 10 opportunities link to existing files in `funders/` (heilmeier, nih_r01, nsf_tech_labs, arpah_mission_office × 2, doe_genesis, astera_residency, brains_accelerator, foresight_nodes, google_impact_challenge, yc_nonprofit). The other 61 leave F22 = null, awaiting either new canonical funder files or being served by their `kind`-level template.
- **Heaviest schemas:** Genesis Mission, ARPA-H ISOs (HSF + PHO), and Horizon Europe each cite ≥18 required slots plus a half-dozen sub-slots — these are the "stress-test" funders for the canonical schema.
- **Lightest schemas:** the 21 nonprofit-discount programs each cite only A01 + A03 + A04.8.
- **Partial profiles (4):** UNESCO/WHO (UNESCO data confirmed, WHO program details unconfirmed); Deep Science Ventures, The Next Sequence, Foresite Labs (limited public detail). Mappings still produced based on available data; F-fields filled where possible, null otherwise.

For the full Monday-loadable flat structure, use [`./opportunity_mapping.csv`](./opportunity_mapping.csv).
For per-opportunity F-family + slot detail, use [`./opportunity_mapping.yaml`](./opportunity_mapping.yaml).

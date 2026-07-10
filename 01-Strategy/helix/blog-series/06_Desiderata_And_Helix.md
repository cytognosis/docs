---
title: What's Still Missing
subtitle: Structural Desiderata for Healthcare Moonshots in the Age of AI, and a First Sketch of the Helix Framework
series: The Helix Series
part: 6 of 6
reading_time: 12 min
license: CC BY 4.0
---

# What's Still Missing

## Structural Desiderata for Healthcare Moonshots in the Age of AI, and a First Sketch of the Helix Framework

We opened this series with a specific claim: no existing institutional structure is designed to carry a healthcare moonshot through its full 15-year arc. Over four posts we have looked at four categories of organization, ARPA-like, FROs, hybrids, and alternatives, each of which has produced genuine institutional innovation, and each of which covers a different slice of the arc. This final post does two things. First, it names the structural capabilities that remain unaddressed when we put all four categories together. Second, it introduces the Helix Framework as one candidate answer, with explicit acknowledgment that others are possible.

## Five things the current landscape does not do

When we read the landscape honestly, five capabilities are consistently underdeveloped.

### Cross-phase continuity

No existing model cleanly spans R-and-D, clinical validation, regulatory approval, and equitable deployment. ARPA programs and FROs are scoped to the first five years. Hybrid organizations are strong at commercial transition but weak at the initial platform build. Alternatives are narrower still. A healthcare moonshot needs a structure that owns the full fifteen years without losing operational coherence or mission commitment as it moves across phases.

### Phase-transition mechanics

When an organization successfully passes through R-and-D, what happens to its team, its IP, its mission commitments, its investors? The transitions from Phase I (R-and-D) to Phase II (clinical and commercialization) to Phase III (globalization and equity) are under-theorized. Most organizations encounter them ad hoc. The result is a lot of stalled platforms and a lot of teams scattering at exactly the moment their accumulated expertise is most needed.

### Equity of access as a structural commitment

Aspirational commitments to global equity are common. Structural mechanisms that make equity binding (tiered pricing with enforcement; technology-transfer obligations; emergency-activation protocols) are rare. Mozilla's revenue model accidentally creates equity of access because users pick Firefox *because* it is mission-aligned. Most healthcare organizations will not have that luxury; they need equity designed in structurally.

### Capital mechanisms for platform work

Healthcare platform R-and-D sits between the capital sources it needs. Philanthropic capital is typically project-scoped and short-term. VC capital requires returns on a 5-to-7-year horizon incompatible with 15-year healthcare moonshots. Federal grants are fragmented across agencies and proposal cycles. No structured capital mechanism currently spans R-and-D through clinical translation.

### Collaborative infrastructure across organizational boundaries

Most genuine healthcare breakthroughs require collaboration across academic labs, mission-driven nonprofits, ARPA-like programs, FROs, and for-profit companies. Wellcome Leap's HBNet (with MARFA and CORFA as pre-negotiated agreement templates) is the best example of what this infrastructure can look like. But HBNet is scoped to Wellcome Leap-funded consortia. The ecosystem needs equivalent pre-negotiated infrastructure at broader scope, so that (for instance) a Cytognosis-class mission-driven health nonprofit and an ARPA-H Delphi-funded biosensor program can collaborate on a shared technology stack without each pairwise relationship requiring months of bespoke contracting.

## Twelve structural desiderata

Concretely, we think any healthcare moonshot organization in 2026 and beyond should be designed to ship the following twelve capabilities from day one. We cast them as desiderata, not as a specific design, because several different structural choices can meet most of them.

| # | Capability | Why it matters |
|---|---|---|
| D1 | **Healthcare-specific, 15-year lifecycle** | Without a full-arc commitment, you are building something somebody else has to pick up, and that pickup is where things break. |
| D2 | **Collaborative-by-design infrastructure** | Pre-negotiated templates for IP, data governance, publication rights, indirect costs, and escalation. Your legal team should not be writing these from scratch for every collaborator. |
| D3 | **Nonprofit parent plus PBC subsidiary(ies)** | Mission governance lives in the nonprofit; commercial capital lives in the PBC; IP stays with the parent and licenses to the subsidiary on documented terms. |
| D4 | **Structural mission locks (not principal-dependent)** | Bylaws, IP licensing terms, and independent review should make mission drift expensive. Your successors should not be able to quietly abandon commitments your founders made. |
| D5 | **Explicit phase transitions with quantitative gates** | Every phase transition is a formal governance event with pre-defined scientific, clinical, organizational, financial, and equity criteria. Halting is a legitimate outcome. |
| D6 | **Promise of future equity for Phase I contributors** | Early team members get structural recognition of their Phase I contribution via defined fractions of future PBC capitalization, on a board-ratified schedule with vesting. |
| D7 | **People as seed funders** | Non-dilutive Phase I capital means the funding public is the seed investor. A defined fraction of future subsidiary revenue flows back to the foundation, earmarked for equity, education, and continued R-and-D. |
| D8 | **Tiered, structural equity of access** | Pricing architecture stratified by World Bank income category, with automatic technology-reserve provisions and emergency-activation triggers tied to formal health-emergency declarations. |
| D9 | **Triple-layer accountability** | Structural (charter), community (advisory boards with actual governance power), external (independent annual review). Any two layers can block actions compromising the mission. |
| D10 | **Openness as a default, not an afterthought** | Default open licenses (Apache 2.0 for code/weights; CC BY 4.0 for docs/data), pre-release checklists enforced structurally, architecture-level privacy. The Astera model for journal publication is worth adopting for healthcare equivalents. |
| D11 | **Edge-first AI and decentralized data** | Privacy architecture assumes data stays on the user's device. Federated learning for aggregate model improvement. Post-quantum cryptography from day one. No centralized honeypots. |
| D12 | **Universal biosensor adapter protocols** | Standardized sensor integration APIs with ontology-grounded data types, so new sensors (from ARPA-H Delphi, from academic labs, from commercial vendors) plug in without bespoke integration. |

If you are founding or funding a healthcare moonshot organization, we would argue these twelve belong on your day-one checklist. Several of them (D4, D6, D7, D9) require legal vetting well beyond what this blog series can provide. Others (D10, D11, D12) require technical architectural choices that compound rapidly over time and are hard to retrofit.

## The Helix Framework, briefly

The Helix Framework is one way to meet the twelve desiderata. A fuller elaboration is in our open commentary paper, which is available alongside this series. Here we summarize enough to orient readers to the shape of the answer.

**Structure.** A 501(c)(3) nonprofit parent (mission-locked, IP-owning, non-dilutively funded in Phase I) pairs with one or more Public Benefit Corporation subsidiaries (commercial, VC-compatible, license-receiving). The nonprofit owns the core platform IP and licenses it to the subsidiaries under documented terms that preserve open-source commitments for research and humanitarian applications while enabling commercial licensing for clinical products.

**Timeline.** Three phases of approximately five years each:

- **Phase I: Research and Development.** Non-dilutive capital only. Platform build. Open-source by default. Promise-of-future-equity to core Phase I contributors.
- **Phase II: Clinical and Commercialization.** Dual model. The nonprofit continues non-dilutive work and funds equity-of-access policy work. The PBC subsidiary raises VC for the product path. People-as-seed-funders revenue share is in effect.
- **Phase III: Globalization and Equitable Access.** Revenue maturity. Geographic expansion. Tiered pricing structurally enforced.

**Phase transition gates.** Each transition is a formal governance event. The G1 (Phase I → II) gate requires evidence against scientific, clinical, organizational/financial, and adoption criteria. The G2 (Phase II → III) gate is dominated by clinical success; commercial sustainability is necessary but not sufficient. Halting is a legitimate outcome and triggers re-scoping rather than collapse.

**Capital innovations.** Two novel mechanisms address the Phase I → II transition:

- **Promise of future equity.** SAFE-style documentation that allocates defined fractions of the future PBC subsidiary's capitalization to Phase I contributors, subject to board approval at the G1 gate. Provides structural recognition of Phase I contribution without false guarantees of financial outcome.
- **People as seed funders.** Non-dilutive Phase I funding is treated as an equity-equivalent investment by the funding public. A defined fraction of future subsidiary revenue flows back to the foundation, earmarked for equity of access, education, and continued R-and-D. Calibrated against comparable for-profit capitalization at equivalent stage.

**Accountability.** Triple-layer: structural (bylaws, IP-licensing terms), community (Lived Experience Advisory Council and beneficiary representation with actual governance power), external (independent annual review, third-party impact verification, whistleblower protections). Any two layers can block mission-compromising actions.

**Equity enforcement.** Tiered pricing stratified by World Bank income classification. Technology reserve requirements for emergency deployment. Pre-shared manufacturing protocols with qualified producers. Automatic licensing during WHO-declared health emergencies, binding on all investors and not overridable during crisis.

## Five open questions

We are publishing this series (and the accompanying paper) as an open commentary because the questions it raises cannot be answered by any single organization. Five questions in particular are genuinely unsolved:

**One.** What quantitative thresholds should define the Phase I → II gate? We have specified values we believe are defensible for Cytognosis, but the right thresholds may differ substantially across indication areas with different baseline maturity.

**Two.** How should "promise of future equity" be *valued*? Calibration against comparable for-profit equity at an equivalent stage is a reasonable anchor, but "equivalent stage" is not well-defined for an organization that intentionally separates research from commercialization.

**Three.** What fraction of subsidiary revenue should flow back as people-as-seed-funders reinvestment? Too low, and the mechanism is symbolic. Too high, and it strangles the subsidiary's ability to scale. A defensible band would help many organizations decide.

**Four.** Which layer of the triple-layer accountability structure is the binding constraint? Structural bylaws, IP-licensing terms, community governance, or external review? The Framework proposes all four simultaneously. In practice, which layer carries the actual weight? Which can be dropped without compromising the whole?

**Five.** How does the Framework scale to non-US jurisdictions? A UK subsidiary under different nonprofit law, a European PBC-equivalent, or a subsidiary in a low-income country with different regulatory and tax regimes: each imposes constraints the US-centric draft has not fully worked through. Cytognosis is beginning to engage with this through a planned UK office; community input from organizations that have already navigated cross-jurisdiction structure would accelerate that engagement substantially.

## Where to go from here

If you are a founder thinking about starting a mission-driven healthcare organization, we would strongly encourage you to read the five open questions above, and specifically Question Four, before finalizing your bylaws. The choice of *which* mission-lock mechanism to rely on structurally is one of the highest-leverage decisions you will make, and it is very hard to revisit after the organization is capitalized.

If you are a funder thinking about how to support healthcare moonshots, we would encourage you to look at the twelve-desiderata table above and ask which of them your existing grantees are actually designed to ship. If the answer is "fewer than half," it is worth having the conversation with your grantees early rather than late.

If you are a researcher working inside one of these structures, or about to, we would encourage you to push for structural answers (not aspirational statements) on the questions that matter most to you. The best time to ask "will this organization structurally protect its openness commitments in 2035?" is before you join it, not after.

The full Helix Framework paper, the 15-year Cytognosis strategic roadmap, and the Phase 1 operational plan that implements these ideas in one specific organizational context are all being published as open artifacts at cytognosis.org. Comments, critiques, and alternative proposals are explicitly invited at helix-commentary@cytognosis.org. The point of this series has been to open the conversation, not to close it.

*This is the final post in the Helix Series. The full open commentary paper is linked from the [series index](00_README.md).*

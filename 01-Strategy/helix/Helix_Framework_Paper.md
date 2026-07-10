# The Helix Framework

## Comparative Lessons from Mission-Driven Research Organizations, and Structural Desiderata for Healthcare Moonshots

**Working draft · Open community commentary**

**Author.** Shahin Mohammadi (Cytognosis Foundation)

**Intended audience.** Researchers, funders, and founders building mission-driven research organizations, with particular attention to structural choices that determine whether healthcare moonshots actually reach the people they are meant to serve.

**Intended venue.** Shared draft for community commentary with Astera Institute, Convergent Research, and Speculative Technologies, toward joint publication as a signed commentary on how healthcare-focused research organizations should be structured in the age of AI.

**License.** CC BY 4.0. Source is on GitHub and will carry a Zenodo DOI prior to any citation.

## Abstract

A wave of institutional experimentation has followed the post-COVID reckoning with how poorly the research enterprise responded to systemic crisis. ARPA-like agencies, Focused Research Organizations, hybrid nonprofit-plus-PBC structures, and a small set of alternatives (open-source hardware businesses, radically open research labs, researcher-centric for-profits) have each tested a distinct hypothesis about how to close the gap between curiosity-driven academia and incremental-return industry. Each has produced lessons. None has, as of 2026, produced a structure purpose-built for healthcare moonshots, specifically for work that (a) requires platform investment at moonshot ambition, (b) must eventually reach patients under regulatory and reimbursement constraints, and (c) must not compromise global equity of access. This paper synthesizes what the first generation of experiments has learned, catalogs the structural gaps that remain, and proposes a set of desiderata (and a provisional model, the Helix Framework) for organizations building healthcare technology in the age of AI. Our aim is not to declare a winner but to surface the design choices that the next generation of founders, funders, and program directors will need to make, and the honest tradeoffs each choice implies.

## Setting the stage

### When ideas do not fit mechanisms

Progress in medicine has long been driven by two institutional forces: fundamental research performed in university and government laboratories, and a commercial sector focused on specific products. For most of medicine's history, these two components were sufficient. Increasingly, they are not. The most promising ideas (those with potentially transformative impact on the health ecosystem) often do not fit either mechanism (Collins et al. 2021).

These ideas fall through the gap for specific, reproducible reasons: risk is too high for peer-reviewed grants; cost is too large for a single lab; timeframe is too long for venture capital; work is too applied for academia but too early for industry; coordination across multiple parties is required; near-term market is too small to motivate commercial investment; or scope is so broad that no single company can capture enough economic benefit to justify the effort. Many such ideas involve creating platforms, capabilities, and resources applicable across many diseases, and they are "use-driven" rather than "curiosity-driven" in Donald Stokes' sense.

This structural mismatch is not a temporary shortcoming. It is a persistent feature of the institutional landscape. Closing it requires not incremental reform but new organizational forms purpose-built for the work that falls between the cracks.

### The post-COVID reckoning

The COVID-19 pandemic served as a stress test for the global research enterprise, and the results were mixed. The rapid development of mRNA vaccines demonstrated the extraordinary power of decades-long platform investments (enabled in part by DARPA and BARDA funding) combined with wartime-scale coordination between government, academia, and industry. But the pandemic also revealed how fragile and ad hoc such coordination was. The speed of the vaccine response depended on pre-existing platform technologies developed through a handful of far-sighted investments, not on systematic institutional design.

This reckoning catalyzed a wave of writing, experimentation, and institution-building loosely grouped under the banner of "metascience": the study of how science itself is organized, funded, and conducted. Several foundational contributions emerged in rapid succession:

- Mark Lutter's *Startup Nonprofits* (2021) made the case for applying startup culture, speed, flat hierarchies, mission focus, tolerance for failure, to nonprofit organizations pursuing public-interest research.
- Matt Webb's *Towards the Orthogonal Technology Lab* (2021) proposed institutions organized around capabilities that cut across multiple domains and that no single industry has sufficient incentive to develop.
- Tom Critchlow's *Reimagining the Research Lab* (2021) explored the "research studio" model, drawing on creative industries to envision small focused teams combining rigorous investigation with rapid prototyping.
- Ben Reinhardt's *Shifting the Impossible to the Inevitable* (2021) provided the most detailed operational blueprint for adapting the DARPA model to private and philanthropic contexts. Reinhardt's subsequent *Playbook for Research Leaders* (Reinhardt and Nakahata 2025) synthesized the first generation of experiments into an operational framework centered on "coordinated research programs" (CRPs), programs combining the ambition and risk tolerance of ARPA-like models with the execution discipline and organizational focus of Focused Research Organizations. The Playbook provides much of the comparative scaffolding we use below.
- Adam Marblestone and collaborators proposed the Focused Research Organization at the Federation of American Scientists (2020), a specific institutional form for building scientific infrastructure that lies between academia and industry.
- Erika Alden DeBenedictis' *Quick-Start Guide to Research Nonprofits* (2022) addressed the practical formation challenges the more conceptual frameworks left unspecified.
- Samuel Rodriques and collaborators' *A Vision of Metascience* (2022) surveyed the emerging field and articulated principles for systematic research organizational design.

Together, these contributions established both the intellectual case and practical groundwork for a new generation of research organizations. This paper examines what that generation has built, what it has learned, and where critical gaps remain.

### A taxonomy

Drawing on this prior work, we organize the emerging landscape into four categories:

**ARPA-like models.** Government and philanthropic agencies that empower term-limited program directors to fund portfolios of high-risk, high-reward research. They operate in Pasteur's Quadrant (advancing fundamental understanding while solving practical problems) and apply the Heilmeier Catechism as a programmatic discipline. The ARPA-like models discussion below examines ARPA-H, Wellcome Leap, ARIA, the EU Horizon Europe Health Cluster, and the emerging NSF Tech Labs initiative.

**Focused Research Organizations (FROs).** Standalone, time-bounded, nonprofit research organizations structured like startups but pursuing public-interest goals. FROs build specific scientific infrastructure (tools, datasets, platforms) that removes bottlenecks holding back entire fields. The model was proposed by Marblestone and collaborators, operationalized through Convergent Research, and is now being advanced with federal funding through NSF Tech Labs. Our FRO discussion covers these in depth, with case studies of E11 Bio, Forest Neurotech, IMPRINT, and the Molecular Monitoring Platform.

**Hybrid organizations.** Entities pairing nonprofit mission governance with for-profit capital formation, testing different structural mechanisms for maintaining mission alignment at commercial scale. The hybrid organizations section examines the Chan Zuckerberg Initiative / Biohub, OpenAI, FutureHouse / Edison Scientific, Mozilla, and Arc Institute.

**Alternative structures.** Organizations demonstrating additional pathways to combine purpose and profit outside the above categories. The alternative structures section covers OpenBCI (open-source hardware with subscription revenue), Episteme (researcher-centric for-profit R-and-D), Astera Institute (open-science nonprofit philanthropy), and Arcadia Science (radical openness as an operating principle).

### What we are looking for

This analysis is not merely academic. We conduct it because the health domain imposes a particular urgency: diseases do not wait for organizational design to catch up. Every year a diagnostic platform remains in the laboratory rather than the clinic, and every month a preventive technology stays in prototype rather than production, represents lives that could have been improved or saved.

We are particularly interested in a challenge that cuts across all four categories: **the shift from capital-restricted to time-restricted organizations**. The traditional model bottlenecks research organizations on funding; teams spend years writing grants and managing donors, with actual research squeezed into whatever time and resources remain. The alternative, providing substantial capital early to enable hiring the best talent and attacking moonshot challenges from day one, requires organizational structures that can responsibly deploy significant resources while maintaining mission discipline. No existing model has fully solved this problem, particularly in healthcare where platform R-and-D must eventually hand off to clinical validation, regulatory approval, and population-scale deployment under equity constraints. The Helix Framework, introduced after the comparative analysis, proposes one answer. The more important contribution of this paper, however, is the comparative analysis itself and the desiderata it surfaces.

## ARPA-like models

### Philosophy: Pasteur's Quadrant and the Heilmeier Catechism

The most consequential scientific advances often emerge not from pure basic research (Bohr's Quadrant) or pure applied engineering (Edison's Quadrant), but from work that simultaneously pushes the frontier of fundamental understanding while solving practical problems. Donald Stokes formalized this observation as **Pasteur's Quadrant**, named after Louis Pasteur, whose investigations into microbial contamination yielded both foundational microbiology and immediate improvements in food safety and medicine.

ARPA-like organizations operate squarely in this quadrant. Their innovation model centers on program-driven research in which bold hypotheses define success rather than incremental progress. Programs begin with aspirational goals, then work backward to identify critical challenges and technical milestones. Several structural features distinguish ARPA-like program management:

- **Empowered program directors** operate with significant autonomy, recruited for fixed terms (typically three to five years) to design and manage portfolios of high-risk, high-reward projects. Their authority to start, redirect, or terminate projects based on emerging results enables rapid iteration that standing institutions rarely achieve.
- **Active management replaces "fire and forget" funding.** Program directors maintain close relationships with performers, adjusting milestones and resources in response to real-time results.
- **Portfolio logic governs risk.** Individual projects are expected to fail at high rates; the portfolio succeeds if even a fraction of its bets produce outsized impact.
- **Time-bounded urgency.** Fixed program timelines (typically three to seven years) create a forcing function that prevents the drift toward incrementalism common in open-ended institutional research.

If Pasteur's Quadrant defines where ARPA-like organizations operate, the **Heilmeier Catechism** defines how they evaluate what to pursue. Developed by former DARPA director George H. Heilmeier (1975-1977), the catechism is eight questions every proposed program must answer before it receives funding: what are you trying to do (in plain language); how is it done today and what are the limits of current practice; what is new in your approach and why will it succeed; who cares; what are the risks; how much will it cost; how long will it take; what are the mid-term and final exams to check for success.

The catechism encodes several principles that distinguish ARPA-like thinking from conventional research culture: jargon-free articulation forces clarity; current limits define the opportunity; novelty must be justified, not assumed; impact must be concrete; risk is acknowledged, not hidden; resource discipline grounds ambition; milestone-based evaluation enables course correction. Together, Pasteur's Quadrant and the Heilmeier Catechism form the philosophical backbone of ARPA-like innovation.

### ARPA-H

The Advanced Research Projects Agency for Health (ARPA-H) represents the largest and most ambitious application of the ARPA model outside national defense. Proposed by President Biden in 2021 and formally established in 2022, ARPA-H was created to address the structural gap articulated by Collins, Schwetz, Tabak, and Lander (2021).

**Structure.** Rather than concentrating operations in a single headquarters, ARPA-H operates through a distributed "ARPANET-H" network with hubs in Boston, Cambridge (MA), Durham, Dallas, and a central administrative office near NIH. Research is organized around four "mission offices" (Resilient Systems, Health Science Futures, Proactive Health, Scalable Solutions), each led by mission-office leadership analogous to DARPA's office directors.

**Funding and scale.** ARPA-H received $1 billion in initial appropriation and has steadily grown to several billion dollars in cumulative commitments. Individual programs typically range from $50 million to $500 million over three to five years, enabling the platform-scale investment that smaller ARPA-like agencies cannot.

**Adaptations beyond DARPA.** Several features distinguish ARPA-H from its defense ancestor. First, an explicit emphasis on equity: the Proactive Health and Scalable Solutions offices are structured around underserved-population access from the outset, not as a retrofit. Second, patient engagement infrastructure: ARPA-H has invested in structured mechanisms for patient and community input into program design. Third, commercialization planning: ARPA-H embeds technology-transition and deployment planning in program design, reflecting lessons from DARPA-funded technologies that reached defense applications but struggled to reach civilian markets.

**Engagement infrastructure.** ARPA-H maintains a program-manager-centric proposer-days format, a more open solicitation process than DARPA's closed procurement, and explicit outreach to academic and nonprofit performers who would not traditionally bid on DARPA contracts.

**What it has proven.** ARPA-H has demonstrated that the ARPA model can be adapted to civilian health at scale. It has already funded a meaningful number of ambitious programs and has begun to generate technology transitions. As of 2026, however, its output horizon is still too early for definitive evaluation. The more interesting question is what ARPA-H cannot do, and we return to that in the desiderata.

### Wellcome Leap

Wellcome Leap, launched in 2020 as an independent subsidiary of the Wellcome Trust, adapted the ARPA model to the philanthropic sector. Operating globally rather than nationally, with smaller total budgets but greater structural flexibility, Leap has tested whether the ARPA model translates to a funder untethered from government procurement constraints.

**Structure and programs.** Leap organizes work into "programs" (the same terminology as ARPA) led by program directors recruited on three-to-five-year tours. Each program funds a portfolio of international performers working on a shared set of technical milestones. Programs to date have spanned mental health, fetal and maternal health, gut-brain health, and human immune monitoring.

**HBNet: Health Breakthrough Network.** Perhaps Leap's most influential structural innovation is the Health Breakthrough Network (HBNet), a standing network of academic, industrial, and clinical performers who have pre-negotiated collaborative terms via two standardized agreements: the **Master Academic Research Funding Agreement (MARFA)** for academic performers, and the **Commercial Research Funding Agreement (CORFA)** for for-profit performers. By pre-negotiating IP ownership, publication rights, data sharing, and indirect-cost structures, HBNet collapses the typical 6-to-18-month contract negotiation window to days or weeks. This is a genuine institutional innovation with broad applicability beyond Leap itself.

**Distributed infrastructure, not centralized facilities.** Leap does not operate laboratories. It coordinates networks of performers, which allows it to move faster but limits its ability to build physical platform infrastructure of the kind that some healthcare moonshots require.

**Tensions.** Leap's global footprint is a strength for comparative studies and for reaching non-US populations, but creates friction around regulatory harmonization, data governance, and clinical translation pathways that differ by jurisdiction.

### ARIA

The UK Advanced Research and Invention Agency (ARIA) was established in 2023 and began operations in 2024 with a mandate to fund high-risk, high-reward research in any domain, with deliberate exemption from standard UK procurement and peer-review constraints.

**Structure.** ARIA is deliberately lean. Its initial budget (£800M over five years) is small by ARPA-H standards but substantial by historical UK research-agency norms. Programs are led by program directors with significant autonomy and explicit indemnification for failed programs.

**Distinctive features.** ARIA is among the first ARPA-like agencies to make open tolerance of failure an explicit legal and governance feature, rather than a de facto cultural norm. Program directors are protected from public-sector accountability mechanisms that would otherwise penalize failed programs, enabling genuine risk-taking. ARIA also makes explicit space for "creative discomfort": programs that sit outside established disciplinary boundaries and that established funders would reject on methodological grounds.

**Portfolio.** As of 2026, ARIA's program portfolio spans programmable plants, symbiotic robotics, neural interfaces, and climate sensing. The health footprint is modest compared to ARPA-H or Wellcome Leap, reflecting ARIA's broader mandate rather than any health-specific deprioritization.

### EU Horizon Europe: Cluster 1 (Health)

Horizon Europe's Health Cluster represents a fundamentally different model: not an ARPA-like agency but the world's largest collaborative research funding programme, with a health cluster budget of approximately €8.2 billion over 2021-2027.

**Structure.** Rather than empowered program directors, Horizon Europe operates through pre-announced work programmes developed through multi-year stakeholder consultation. Calls are published, consortia bid, and funded projects typically involve 10 to 30 partners across multiple member states. Success metrics emphasize cross-border collaboration, training, and dissemination alongside scientific deliverables.

**Partnerships in health.** The health cluster includes several structured partnerships (the Innovative Health Initiative, the Chips Joint Undertaking health components, the Global Health EDCTP3 partnership) that blend public and private funding.

**Structural contrast with ARPA-like models.** Horizon Europe's consortium-first, slow-solicitation, documentation-heavy structure sits at the opposite end of the spectrum from ARPA-like active program management. Its strength is cross-border coordination and durable infrastructure; its weakness is speed and risk tolerance. Healthcare moonshots generally require a structure closer to the ARPA end.

**Relevance for emerging innovation models.** Despite these contrasts, Horizon Europe has significant relevance: its partnership mechanisms, standardized cross-border agreements, and large-cohort infrastructure investments create capabilities that ARPA-like agencies can plug into rather than replicate.

### NSF Tech Labs

Emerging in 2026, the NSF Tech Labs initiative represents the first federal mechanism explicitly designed to fund Independent Research Organizations (IROs), including FROs. Under Tech Labs, NSF provides capital for IROs to operate for extended periods, rather than the typical project-by-project grant mechanism. The structure is deliberately permissive around the organizational form of the funded entity. This is a significant evolution: for the first time, a federal agency is explicitly funding the creation of new kinds of research institutions rather than only the projects within existing ones.

### ARPA-like models: shared principles and honest limits

All ARPA-like models share five principles: they operate in Pasteur's Quadrant; they empower program directors; they replace "fire and forget" funding with active management; they use portfolio logic to accept high per-project failure rates; and they impose time-bounded urgency. These principles explain much of their effectiveness relative to peer-reviewed grants or consortium programs.

Their honest limits are equally structural. ARPA-like programs are typically three to seven years. They start, produce outputs, and end. They do not continue operating the platforms they build, and they do not carry technologies from R-and-D through clinical validation and into deployment. For healthcare moonshots this is a critical gap: the ARPA model is excellent at the first five years of a fifteen-year program, and is not designed for the next ten. What happens to the platforms after the program ends, which organization takes responsibility for clinical translation, and how the resulting technology reaches underserved populations, are all questions the ARPA model leaves to whatever institutional structure picks up the handoff. In practice, that handoff is frequently the point of failure.

## Focused Research Organizations

### Origins: Marblestone et al. and the FRO concept

In 2020, Adam Marblestone, Sam Rodriques, and collaborators at the Federation of American Scientists proposed the Focused Research Organization (FRO) as a new institutional form: a standalone, time-bounded, nonprofit research organization structured like a startup but pursuing public-interest goals. The target problem is narrower than ARPA-like programs: FROs are designed to build **specific scientific infrastructure** (a tool, a dataset, a platform, a methodology) that removes a bottleneck holding back an entire field. The prototypical FRO question is: "What is a single capability whose absence blocks large swaths of research, and that no single lab or company has sufficient incentive to build?"

### Convergent Research: from concept to practice

Convergent Research (founded 2022) operationalized the FRO concept by providing shared operational infrastructure: legal formation, governance templates, HR, finance, and fundraising support, enabling individual FROs to focus on the scientific work. Convergent also provides access to capital: FROs are funded through a combination of philanthropic grants and, increasingly, federal mechanisms including NSF Tech Labs.

**What makes an idea "FRO-shaped?"** Convergent has articulated criteria that distinguish FRO-shaped problems from ARPA-shaped ones: the problem is concrete and well-scoped; the work is engineering-intensive rather than hypothesis-exploration; the output is a specific infrastructure artifact rather than a portfolio of discoveries; the organization has a natural end date when the infrastructure is delivered; and the output will be widely used downstream if it exists.

### FROs vs. ARPA-like programs

FROs and ARPA-like programs can look superficially similar (both are time-bounded, both use portfolio logic in some form, both operate outside traditional academic mechanisms) but they differ in critical ways:

| Dimension | ARPA-like program | FRO |
|---|---|---|
| Scope | Multi-project portfolio around a mission | Single concrete infrastructure artifact |
| Team | Distributed performers, coordinated by PM | Single integrated team |
| Organization | Program inside an agency | Standalone nonprofit |
| Duration | 3-7 years | 3-7 years (typical) |
| Termination | Program ends; performers continue independently | Organization dissolves when deliverable is complete |
| Output | Portfolio of technologies and knowledge | Single widely-usable artifact |
| Handoff | Varied (commercialization, open release, follow-on programs) | Typically open release with operational handoff to downstream community |

### Notable FRO case studies

**E11 Bio (connectomics).** E11 is building a platform for whole-brain connectomics at single-neuron resolution in small mammals, a capability currently blocked by the cost and throughput limits of existing electron microscopy approaches. E11 is a canonical FRO: engineering-intensive, single-output (a scalable connectomics pipeline), natural end date when the pipeline is delivered, and obvious downstream community (neuroscience at large).

**Forest Neurotech (BCIs).** Forest is developing minimally-invasive, whole-brain-scale recording and stimulation using ultrasound. Similar FRO shape: specific technology target, clearly defined "done" state, obvious downstream adoption if the technology works.

**IMPRINT (immune system).** IMPRINT is building high-resolution immune-system profiling infrastructure, motivated by the observation that immune heterogeneity underlies much of what is unexplained in disease variability.

**A new platform for human molecular monitoring.** The molecular monitoring FRO (motivated by the Muthusamy and Garrett 2023 white paper) is developing CMOS-integrated, programmable affinity biosensors for continuous tracking of 100+ analytes. This is particularly relevant to healthcare moonshots because continuous molecular monitoring is a platform capability that no existing FRO structure carries to clinical deployment: the FRO delivers the measurement technology; some downstream structure must carry it through clinical validation and into patient access.

### What FROs have proven, and where they run out

FROs have proven that time-bounded, startup-culture nonprofits can deliver scientific infrastructure at speed and quality competitive with industry R-and-D, with outputs that remain open and widely available. They have proven that a relatively small total investment ($20 to $100 million over five years) can produce infrastructure that unlocks much larger downstream value. They have been a genuine institutional success.

What FROs cannot do, by design, is carry the technologies they build through clinical validation and into patient deployment. The FRO is time-bounded and dissolves on schedule. The whole point is to hand the output to a downstream community: publications, open datasets, open platforms. For many kinds of scientific infrastructure this is exactly right. For healthcare technologies that require regulatory validation, reimbursement pathways, and equitable access mechanisms, it leaves the hardest ten years unaddressed.

## Hybrid organizations

Hybrid organizations pair nonprofit mission governance with for-profit capital formation, testing whether commercial-scale capital and mission-locked governance can coexist. Each has produced specific structural lessons.

### Chan Zuckerberg Initiative and Biohub

CZI is structured as an LLC rather than a traditional nonprofit foundation, giving it flexibility to make both charitable grants and for-profit investments without the usual mission-drift mechanisms of private foundations. Biohub (originally Chan Zuckerberg Biohub, now expanded into a network) operates as a research organization inside this structure.

**Lesson.** LLC structure gives flexibility, but that flexibility is a double-edged sword: it places more weight on the principals' personal mission alignment because structural mission-locks are weaker than traditional 501(c)(3) constraints.

### OpenAI: from nonprofit to public benefit corporation

OpenAI's evolution is the most cautionary hybrid case study. OpenAI began as a 501(c)(3) nonprofit committed to building AI "safely and beneficially for all of humanity" with an open-release default. Over time, the organization introduced a "capped-profit" subsidiary (OpenAI LP), negotiated a strategic investor relationship with Microsoft, progressively reduced the default-open disposition of its outputs, and (as of 2025 and 2026) is in the process of converting its commercial arm into a Public Benefit Corporation.

**Lesson.** The primary structural lesson is that when the commercial subsidiary controls critical resources (access to compute, hiring, and data) the nonprofit parent's theoretical mission control becomes nominal. Mission governance needs more than a nonprofit parent with a theoretical veto; it needs structural mechanisms that make mission drift expensive rather than convenient. The OpenAI trajectory also exposes a subtler failure: when the core IP itself (e.g., AGI-class models) becomes the commercial asset, the tension between openness and capital formation cannot be resolved by "open the tools, close the core" because the tools and the core are the same thing.

### FutureHouse and Edison Scientific

FutureHouse is a 501(c)(3) nonprofit building AI agents for scientific research (literature search, hypothesis generation, experiment design). Edison Scientific is its spinout, a commercial entity building similar capabilities for commercial customers. The two organizations share a founding team and a disposition toward open-weight model releases, but operate independently.

**Lesson.** Spinout-from-nonprofit is a cleaner model than internal capped-profit subsidiary because the structural separation is explicit, the IP licensing is auditable, and mission drift in the for-profit does not contaminate the nonprofit's governance. But it also depends on the nonprofit retaining enough capability to continue producing public-good outputs after the spinout, which requires continued philanthropic funding.

### Mozilla Foundation and Mozilla Corporation

Mozilla's structure, a nonprofit foundation that wholly owns a for-profit corporation (Mozilla Corporation, which ships Firefox), is perhaps the longest-running experiment in nonprofit-locked commercial operations at significant scale. Firefox revenue (primarily search-deal payments) flows back to the foundation, funding the foundation's open-internet advocacy and the corporation's ongoing product work.

**Lesson.** The Mozilla model works when the commercial product has durable demand from users who specifically want the mission-aligned alternative. It is less obvious how to replicate this in healthcare, where users generally want "whatever works best" rather than "the mission-aligned alternative."

### Arc Institute

Arc Institute, founded in 2021, is endowment-powered: its operating budget derives primarily from an endowment rather than from annual grants or commercial revenue. Research staff are hired on "core investigator" appointments with multi-year independence from grant writing. Arc has explicitly adopted dual internal cultures: rigorous basic science alongside engineering-focused translational work.

**Lesson.** Endowment-funded research is a powerful model where the endowment is large enough to cover significant operating cost. The constraint is capital: very few organizations have access to the sustained philanthropic capital that funds an endowment at Arc's scale. The dual-internal-cultures lesson generalizes more broadly: the ability to support both hypothesis-driven basic science and engineering-intensive platform work inside a single organization, without either culture dominating, is genuinely hard and Arc is one of the few organizations doing it well.

### Structural comparison of hybrid models

| Dimension | CZI/Biohub | OpenAI | FutureHouse/Edison | Mozilla | Arc |
|---|---|---|---|---|---|
| Primary structure | LLC + Biohub subsidiary | 501(c)(3) + capped-profit LP + PBC spinout | 501(c)(3) + independent for-profit | 501(c)(3) + wholly-owned for-profit | 501(c)(3), endowment-funded |
| Mission lock | Principal-dependent | Progressively weakened | Structural (separate entities) | Structural (ownership) | Structural (endowment + charter) |
| Commercial revenue role | Optional | Primary funding | Separate funding stream | Primary funding for both | Secondary |
| Openness default | Case-by-case | Originally open, now closed | Open weights default | Open-source product | Open but not radical |
| Transferability to healthcare | Moderate | Weak (wrong incentive structure) | Strong (clean separation) | Weak (wrong revenue model for healthcare) | Strong if endowment exists |

## Alternative structures

### OpenBCI: open-source hardware as a sustainable business

OpenBCI is a Brooklyn-based for-profit that makes open-source brain-computer interface hardware (Cyton, Ganglion, Galea) alongside associated software and subscription services. Despite operating entirely as a for-profit, its open-source hardware and radically transparent development culture have made it one of the most durable open-source-first hardware businesses.

**Diversified capital strategy.** OpenBCI combines three revenue streams: hardware sales, software subscriptions, and paid R-and-D partnerships with larger partners. This diversification has kept the company independent without requiring VC timelines that would force closure of the open-source core.

**Strategic partnerships.** OpenBCI's Galea (a mixed-reality BCI platform) has been developed in partnership with Valve Corporation, demonstrating that a fully open-source-hardware company can attract partnership capital from larger actors without compromising openness.

**Lesson.** Open-source hardware is commercially viable when the business generates sufficient margin from services, subscriptions, and partnerships to fund ongoing R-and-D. This is the model most directly applicable to healthcare hardware (wearables, sensors, consumer devices) because it aligns incentives: users pay for the product and associated subscription; the underlying hardware and software stay open; new applications of the core are enabled by the openness rather than blocked by it.

### Episteme: Bell Labs for the 21st century

Episteme positions itself as a researcher-centric for-profit R-and-D organization, explicitly modeled on the golden age of Bell Labs but updated for the modern context. Researchers are given multi-year independence, patent royalties on their own work, and shared infrastructure.

**Lesson.** The researcher-centric model is attractive to talent but has an unresolved commercial viability question: Bell Labs was sustained by AT&T's monopoly rents, a revenue source Episteme does not have. The current model depends on research outputs generating licensing and commercial revenue at sufficient scale to sustain the organization. Whether this is repeatable without a monopoly-rent parent remains an open question.

### Astera Institute

Astera operates as an open-science-first nonprofit philanthropic institute. Its residency program funds researcher-led moonshot projects with the explicit constraint that outputs are released as open, FAIR research artifacts rather than journal articles. Astera's Open Science Policy explicitly prohibits the use of Astera funds or time to contribute to journal publications, treating journals as "a relic of the past" and forcing residents to experiment with continuously published, DOI-bearing research outputs instead.

**Lesson.** Open-first institutional commitments are most credible when they are structural, not aspirational. Astera's policy is a forcing function: residents are contractually bound to publish openly, which converts "we support open science" from a value statement into an operational reality. This is a model healthcare organizations should consider adopting at the structural level.

### Arcadia Science

Arcadia Science, founded 2021, operates as a for-profit research organization with radical openness as an operating principle. All research outputs are published on Arcadia's platform as soon as they are ready for reuse. Arcadia explicitly embraces "icebox" publication of results that do not produce clean narratives, rejecting the journal-publication structure that filters for positive results.

**Lesson.** Radical openness as an operating discipline is compatible with for-profit operation. Arcadia's revenue model is early; its openness model is mature. Whether the two can co-exist at sustained scale is the core open question.

## Cross-cutting comparative analysis

### What works

Across all four categories, five patterns consistently distinguish organizations that produce outsized impact:

1. **Empowered leaders with term limits.** ARPA program directors, FRO founders, hybrid-organization CEOs with limited tenure. Authority to act decisively, combined with an end date that forces prioritization.
2. **Portfolio logic with honest failure.** Individual projects or programs are allowed, even expected, to fail; the aggregate succeeds. This requires structural commitment to failure tolerance, not just rhetorical.
3. **Active management over fire-and-forget funding.** Program directors and organizational leadership stay in close contact with performers. Course correction happens continuously.
4. **Structural mission locks.** Mechanisms that make mission drift structurally expensive (Mozilla's ownership structure; FROs' dissolution-on-delivery; Arc's endowment; Astera's open-publication contract) outperform aspirational mission statements.
5. **Pre-negotiated collaboration infrastructure.** Wellcome Leap's MARFA/CORFA, Convergent's shared operational services, ARPA-H's engagement infrastructure. Reducing transaction cost of collaboration enables more collaboration.

### What does not work

Four patterns consistently correlate with mission drift, underperformance, or outright failure:

1. **Principal-dependent mission lock.** Organizations that rely on specific individuals' mission commitment rather than structural constraints tend to drift as leadership turns over.
2. **Capped-profit as the only mission-drift brake.** OpenAI's trajectory illustrates that when the commercial subsidiary controls critical resources, caps are nominal.
3. **Handoff failure between R-and-D and deployment.** FROs and ARPA programs both hand off to downstream structures. When no such structure exists (especially true in healthcare) the handoff is the point of failure.
4. **Consortium programs without active management.** Large collaborative programs (Horizon Europe-style) without program-director-like active management tend toward diffusion of accountability and loss of urgency.

### What is missing

Four structural capabilities remain largely unaddressed across the four categories:

1. **Cross-phase continuity.** No existing model cleanly spans R-and-D, clinical validation, regulatory approval, and equitable deployment. ARPA programs and FROs are scoped to the first five years; hybrid organizations are strong at the commercial transition but weak at the initial platform build; alternative structures are narrower still. Healthcare moonshots need a structure that owns the full fifteen years.

2. **Phase transition mechanics.** When an organization successfully passes through R-and-D, what happens to its team, its IP, its mission commitments, its investors? The transitions from Phase I (R-and-D) to Phase II (clinical and commercial) to Phase III (globalization and equity) are under-theorized. Most organizations encounter them ad hoc.

3. **Equity of access as a structural commitment.** Aspirational commitments to global equity are common; structural mechanisms that make equity binding (tiered pricing with enforcement, technology-transfer obligations, emergency-activation protocols) are rare. Mozilla's revenue model accidentally creates equity of access; most healthcare organizations do not have that luxury.

4. **Capital mechanisms for platform work.** Healthcare platform R-and-D sits between the capital sources it needs. Philanthropic capital is typically project-scoped and short-term; VC capital requires returns on a 5-to-7-year horizon incompatible with 15-year healthcare moonshots; federal grants are fragmented across agencies and proposal cycles. No structured capital mechanism currently spans R-and-D through clinical translation.

## Structural desiderata

What should an organization designed to carry a healthcare moonshot through its full 15-year arc look like? The analysis above surfaces a set of structural requirements. The following desiderata are deliberately cast as design constraints, not as a proposed model; the Helix Framework in the next section is one way to meet them, but others are possible.

### In scope

- Healthcare-specific moonshots: work where platform investment is required, clinical validation is required, and equitable deployment is a first-class constraint.
- Full 15-year lifecycle across three phases: R-and-D, clinical and commercial, globalization and equity.
- Organizations designed from inception to accommodate the age of AI: hiring patterns, safety governance, edge-AI deployment, data privacy, and ontology-grounded reasoning.

### Out of scope

- Incremental commercial products that do not require platform-scale R-and-D.
- Pure basic research that does not target eventual clinical deployment.
- Defense, national-security, or dual-use applications.

### Collaborative by design

Most genuine healthcare advances require tight collaboration across academic labs, for-profit companies, and mission-aligned nonprofits. Most current mechanisms treat collaboration as an aspiration rather than an infrastructure requirement. The Wellcome Leap HBNet / MARFA / CORFA model demonstrates that pre-negotiated collaborative infrastructure is possible, but its scope is limited to Leap-funded consortia. We need equivalent infrastructure that extends across organizational boundaries, for example between a Cytognosis-class mission-driven nonprofit and an ARPA-H Delphi-funded biosensor program, where the two organizations are building complementary pieces of a shared system but have no standing mechanism for joint work.

**Desideratum.** A healthcare-moonshot organization should ship a pre-negotiated collaboration protocol covering (a) IP ownership and licensing, (b) data governance and privacy constraints, (c) publication and open-release rights, (d) indirect-cost handling, and (e) escalation and dispute resolution. These should be adoptable by external collaborators as a default rather than negotiated case by case.

### Balancing purpose and profit

Most mission-driven efforts share similar core values around openness and equity but struggle to transition after R-and-D because scaling frequently requires forms of exclusivity (exclusive IP, closed commercial channels, proprietary manufacturing) that conflict with the founding commitments. The structural question is whether these two needs can be met inside a single organization or require structurally separate entities with clean legal interfaces.

The emerging answer is the latter: a nonprofit parent (mission-locked, charitable-purpose, IP-owning) with one or more PBC subsidiaries (commercial, VC-compatible, license-receiving). Within this structure, specific questions still require answers:

- What IP stays with the parent vs. licenses to subsidiaries, and on what terms?
- How is openness preserved in the subsidiary's development (open core, closed features; time-delayed release; permissive licenses with defensive patent pools)?
- What are the mission-lock mechanisms that prevent subsidiary capture of the parent?
- What triggers emergency activation of technology reserves (automatic licensing during WHO-declared health emergencies)?

### Timeline: the three-phase, fifteen-year lifecycle

We propose a three-phase paradigm across approximately 15 years, each phase approximately 5 years:

- **Phase I: Research and Development.** Corresponds to the scope of most current mission-driven efforts. Relies on non-dilutive, mission-aligned capital: donations, grants from governments and philanthropic organizations, and other mission-aligned non-profits.
- **Phase II: Clinical and Commercialization.** Dual model: VC funding raised into a PBC subsidiary incorporated with limited scope, while the nonprofit parent continues to obtain non-dilutive funding and funds policy work for equitable access.
- **Phase III: Globalization and Equitable Access.** Primarily revenue-driven (from the subsidiary plus regional philanthropic partnerships) with a structural focus on geographic expansion, regulatory harmonization, and equity enforcement.

Each phase has distinct requirements, financial flows, and focuses, and the transitions between phases are explicit governance events rather than drift.

### Phase-transition innovations

Two novel mechanisms address the hardest structural problem, the Phase I to Phase II transition:

**Promise of future equity.** Similar logic to YC's SAFE but adapted to the Phase I core and founding team. In a nonprofit R-and-D phase, traditional equity is unavailable, but Phase I contributors still deserve structural recognition. A signed "promise of future equity" allocates a defined share of the future PBC subsidiary's capitalization to Phase I contributors, subject to Board approval at the G1 transition. This is not a guarantee of financial return; most organizations will never reach IPO-class outcomes. What it provides is structural acknowledgment that Phase I contribution warrants structural recognition, not merely salary. Operationally, this maps to a board-documented schedule defining which roles receive what fraction of subsidiary capitalization, with clear vesting and cliff provisions.

**People as seed funders.** Non-dilutive Phase I funding means that people's capital (directly via philanthropy or indirectly via public-grant taxation) is invested in the initial idea. To make this sustainable and fair, we propose that the funding public becomes the initial seed investor: a defined fraction of future revenue from the PBC subsidiary is reinvested in the foundation, specifically earmarked for equitable access programs, education, and continued R-and-D. At the G1 transition, the expected equity share that would accrue to hypothetical "0-dilution" founders in a comparable for-profit (stratified by geography and field) is computed. A fraction approximating that share is treated as the public's contribution, flowing back to the foundation rather than to new investors.

Both mechanisms require careful comparative analysis at the transition point with comparable for-profit entities to estimate fair values.

### Structural desiderata: summary

| # | Desideratum | What it constrains |
|---|---|---|
| D1 | Healthcare-specific, 15-year lifecycle | Organizational charter; budget planning; staffing model |
| D2 | Collaborative-by-design infrastructure | Pre-negotiated legal templates; standing collaboration agreements |
| D3 | Nonprofit parent + PBC subsidiary(ies) | Legal structure; IP ownership; revenue flow |
| D4 | Structural mission locks (not principal-dependent) | Bylaws; IP licensing terms; independent reviewer panels |
| D5 | Explicit phase transitions with quantitative gates | Governance cadence; transition-pack requirements |
| D6 | Promise of future equity for Phase I contributors | Board-ratified allocation schedule; vesting terms |
| D7 | People as seed funders | Revenue-share reinvestment formula; charitable use earmarks |
| D8 | Tiered, structural equity of access | Pricing architecture; technology-reserve provisions; emergency activation triggers |
| D9 | Triple-layer accountability | Structural (charter), community (advisory boards), external (independent audits) |
| D10 | Openness as a default, not an afterthought | Default open licenses; pre-release checklists; architecture-level privacy |
| D11 | Edge-first AI and decentralized data | Privacy architecture; federated learning; post-quantum cryptography |
| D12 | Universal biosensor adapter protocols | Standardized sensor integration APIs; collaboration with ARPA-H Delphi and equivalents |

## The Helix Framework

The Helix Framework is one way to meet the twelve desiderata. We present it not as a finished blueprint but as a working design that the Cytognosis Foundation is implementing and testing in real time, and that we are publishing for the field to pressure-test. The name comes from the structure's shape: two strands, a mission strand and a capital strand, wound around a shared backbone (the platform, the people, and the charitable purpose), cross-linked at defined points, and running in one direction across a fifteen-year arc. Neither strand is subordinate to the other; both are load-bearing; and the cross-links, not the strands, are where the hard engineering lives. The comparative analysis above is what gives us any confidence in the design; the sections that follow convert its lessons into structure.

### Two strands, one backbone

The structure pairs a 501(c)(3) nonprofit parent with one or more Public Benefit Corporation (PBC) subsidiaries.

The Foundation is the mission strand. It is mission-locked through its charter, it owns the core platform intellectual property, and it is funded non-dilutively in the early years through donations and grants. It holds the charitable purpose and a governance majority over each subsidiary's board.

The PBC is the capital strand. It raises dilutive capital, manufactures and scales the regulated products, and carries the work through clinical validation, reimbursement, and the market. It takes venture investment from preferred, non-controlling investors, so capital can enter at commercial scale without acquiring the votes to redirect the mission.

The comparative analysis tells us where to sit on the control spectrum. Mozilla's wholly-owned model gives unambiguous governance authority, but its revenue model (users who choose the mission-aligned product) does not transfer to healthcare, where people want whatever works best. OpenAI shows that a minority stake plus a capped-profit promise becomes a nominal lock once the subsidiary controls the compute, the hiring, and the data. The Helix design sits deliberately between them: the Foundation does not own all of the PBC, but it holds a governance majority on the PBC board and it owns the platform IP outright, with a perpetual, non-revocable license to use that IP in the open mission no matter what the PBC later decides. Control comes from the charter and the IP, not from the cap table alone.

### Intellectual property: an open core with a licensed periphery

The IP design is the first cross-link, and it is the one most organizations get wrong by deferring it.

All intellectual property arising from Foundation-funded work before the first phase gate belongs to the Foundation and stays there. The open core (the foundation models, the harmonized datasets, the schemas and ontologies, the universal biosensor adapter protocol, and the methods) is released under open licenses by default: Apache 2.0 for code and, where source data permit, for model weights; OpenRAIL-M for weights derived from controlled-access cohorts where an unrestricted release would re-encode individual-level signal; CC BY 4.0 for papers, documentation, and shareable derived data; CC0 for schemas and ontologies; and CERN-OHL-S for open hardware designs.

The PBC receives a royalty-bearing, non-exclusive, field-of-use-limited license to use Foundation IP in commercial products. Intellectual property arising from PBC-funded work after the gate (product-specific hardware, the regulated navigation engine, the continuous individual-level longitudinal record) belongs to the PBC. The Foundation retains, in writing and irrevocably, the right to use all Foundation-funded IP in its open mission regardless of any commercial choice the PBC makes later. That single clause is the structural guarantee that the map stays open even if a future board or investor wishes otherwise.

The Foundation does not pursue defensive patents on its own methods or models. For an open-mission organization, an open release plus deliberate prior-art creation is a stronger shield than a defensive patent: it stops a later actor from patenting the same method and using it to block foundational research. The PBC may patent product-specific and hardware-specific inventions where a patent protects a defensible market position; the Foundation's prior art keeps those patents from reaching back to encumber the open core.

Two IP questions remain genuinely open, and we flag them rather than paper over them. First, emergency access: the design calls for automatic, non-overridable licensing of relevant technology during formally declared health emergencies, backed by a technology reserve and pre-shared manufacturing protocols, but the legal instrument that makes such a march-in binding on downstream investors is not yet drafted, and we want the field's help with it. Second, the fair-market valuation of pre-revenue platform IP at the moment it is licensed to the PBC, which we treat below as part of the harder arm's-length problem.

### The hard part: arm's-length interaction and the 501(c)(3) constraints

This is the section the first version of this paper deferred, and it is the one that matters most, because it is the least solved across the entire field. A 501(c)(3) that helps create an affiliated for-profit, shares founders and staff with it, and licenses its IP to it, is precisely the configuration nonprofit law scrutinizes most closely. Getting it wrong does not merely look bad; it risks private inurement (impermissible benefit flowing to insiders), impermissible private benefit (more-than-incidental benefit to the for-profit and its investors), excess-benefit transactions (which trigger personal excise taxes on the insiders involved under the intermediate-sanctions rules), and, in the limit, loss of exemption, alongside unrelated-business-income-tax exposure on the wrong kind of revenue. None of this is a reason to avoid the structure. It is a reason to engineer the interface deliberately. We are not lawyers, and what follows is a design under active review by counsel, not legal advice; we publish it so others building the same interface do not start from a blank page.

The design rests on five mechanisms.

First, genuinely independent governance of the interface. The Foundation board carries an independent majority of directors with no financial stake in the PBC. Although the Foundation holds a governance majority on the PBC board, every transaction between the two entities is approved only by the disinterested directors, and any individual who sits on both sides (a founder who is CEO of the Foundation and a shareholder of the PBC, for example) recuses from the vote and from the negotiation. The point is to make the interface arm's-length in substance, not only in name.

Second, fair market value on everything that crosses the interface. Any IP license, shared service, or asset transfer between the Foundation and the PBC is priced at fair market value, supported by an independent valuation and contemporaneous comparables, and documented before the value moves. Done correctly, this is also how the organization earns the rebuttable presumption of reasonableness that the intermediate-sanctions framework offers: approval by an independent body, reliance on appropriate comparability data, and contemporaneous documentation of the basis for the decision. Valuing pre-revenue platform IP is hard precisely because clean comparables are scarce, which is one of the open questions we put to the community below.

Third, revenue structured to stay clear of unrelated-business-income tax. Royalties received by a tax-exempt organization for licensing its intellectual property are generally excluded from unrelated-business-income tax. The Foundation therefore takes its return from the PBC as a genuine, passive royalty on licensed IP rather than by running the commercial business itself, and it keeps the active commercial operation inside the PBC where it belongs. The people-as-seed-funders reinvestment described below is designed to ride that same royalty channel, so the public's return arrives as mission-restricted, tax-clean income rather than as an entanglement that would jeopardize exemption.

Fourth, reasonable compensation, documented. Compensation for any insider in either entity is benchmarked against comparable roles and approved by the independent directors. This is not a small point for early-stage founders, and we treat founder compensation as part of the same arm's-length discipline rather than as an exception to it.

Fifth, written instruments before value flows. A master IP license, the services agreements, and the PBC charter are all executed in writing and reviewed by counsel before the first dollar or the first line of code crosses the interface. The charter carries the mission-lock terms and the Foundation's governance majority, so the constraints survive changes in personnel.

We want to be honest that this is a design, not a settled answer. The hardest pieces (a defensible valuation method for pre-revenue platform IP, the tax treatment of the promise of future equity as either a current benefit or a contingent future interest, and the unrelated-business-income treatment of the reinvestment channel) are exactly the questions we hope to work through with counsel and with the field rather than to assert.

### Two capital mechanisms for the work capital markets do not fund

Between the strands sit two mechanisms that address the part of the lifecycle no existing capital source covers: the years of non-dilutive, pre-commercial platform work, and the people who do it.

The first is a promise of future equity. In a nonprofit research phase, conventional equity does not exist, yet the people who do the foundational work still deserve structural recognition, not only a salary. Borrowing the logic of a startup's SAFE, the Foundation issues each core early contributor a documented promise that allocates a defined fraction of the future PBC's capitalization to them, subject to the independent board's approval at the first phase gate and to ordinary vesting. It is not a guarantee of a financial outcome; most organizations will never reach an outcome where it pays. It is a credible, written acknowledgment that early contribution warrants a share of the upside it helped create, and it lets a mission-driven nonprofit compete for talent against ordinary startups. It must be structured so it does not constitute a current private benefit or a present taxable event, which is one reason it requires careful legal drafting.

The second is people as seed funders. When the early work is funded non-dilutively, the public (directly through philanthropy, or indirectly through the taxes behind public grants) is effectively the seed investor. To honor that, a defined fraction of future PBC revenue flows back to the Foundation, earmarked for equity-of-access programs, education, and continued research. The fraction is calibrated by asking what dilution a comparable for-profit founder would have absorbed by the equivalent stage, and treating an approximation of that share as the public's contribution, returned to the Foundation rather than captured by new investors. The right fraction is a real open question: too low and the mechanism is symbolic, too high and it starves the subsidiary of the capital it needs to scale.

### The three-phase, fifteen-year lifecycle and its gates

The framework runs across roughly fifteen years in three phases of about five years each, and the transitions between them are formal governance events rather than drift.

Phase I (Research and Development) runs on non-dilutive capital alone, builds the platform, releases the core openly, and issues the promise of future equity to its core contributors. Phase II (Clinical and Commercialization) runs a dual model: the PBC subsidiary is incorporated with limited scope and raises venture capital for the regulated product path, while the Foundation continues its non-dilutive work and funds the policy work equitable access requires; the people-as-seed-funders reinvestment begins here. Phase III (Globalization and Equitable Access) is revenue-mature, expands geographically through regional sister organizations with local policy knowledge, and enforces tiered access structurally.

Each transition is a gate, not a calendar date. The first gate (Phase I to II) requires evidence on four axes: scientific (external validation against established frameworks), clinical (clinical-scale funding plus the regulatory and ethics infrastructure to use it), organizational and financial (the PBC charter operational, the capital mechanisms legally vetted, sufficient runway), and adoption (real downstream use of the open core). The second gate (Phase II to III) is dominated by clinical success: regulatory clearance and demonstrated effect over standard of care across multiple indications, with commercial sustainability necessary but not sufficient. Halting at a gate is a legitimate outcome that triggers re-scoping rather than collapse, which is only possible because the Foundation, not the investors, controls whether the gate opens.

### Accountability and equity, locked structurally

Mission-lock in the Helix design is deliberately redundant, because the comparative analysis showed that single-point mission locks fail. Three layers operate at once. The structural layer lives in the bylaws and the IP-licensing terms. The community layer is a Patient Advocacy Council with binding (not merely advisory) rights at the bifurcation gate and over study design, release timing, and prioritization, alongside a Lived Experience Advisory Council. The external layer is independent annual review with third-party impact verification and whistleblower protection. The design intends that any two layers can block an action that compromises the mission, so no single captured board, council, or auditor can unwind the commitments. Which layer carries the binding weight in practice is one of our open questions.

Equity of access is enforced through the same discipline: pricing tiered by World Bank income classification, a technology reserve for emergency deployment, pre-shared manufacturing protocols with qualified producers, and automatic licensing during declared health emergencies that binds investors and cannot be overridden during a crisis.

### Cytognosis as the first, and honest, test case

The Cytognosis Foundation is the first implementation of the Helix Framework and the case study against which we are testing it in real time, including its uncomfortable parts. As we write, we are working through a live instance of exactly the questions above: whether and how to stand up a for-profit entity now, for a consumer product built on the open core, while the Foundation remains the mission-locked science platform; how a founder can be compensated across two entities without breaching the arm's-length discipline; and how to value an IP license when there is not yet revenue on either side. We do not present these as solved. We present the framework as the structure within which we are trying to solve them honestly, and we are publishing the operational documents (bylaws, the fifteen-year roadmap, the Phase I operational plan) as open artifacts under CC BY 4.0 so the working can be inspected and improved.

## Open questions for the community

We publish this draft as an open commentary because the questions it raises cannot be answered by any single organization. Eight questions in particular would benefit from multi-organization input:

1. **What quantitative thresholds should define the Phase I → II gate?** The existing Cytognosis draft specifies scientific (external validation against ≥ 2 frameworks), clinical (at least one $10M+ clinical-scale grant and IRB infrastructure), organizational (PBC charter operational, 24 months runway), and adoption (≥ 1,000 downloads and ≥ 50 citing publications) criteria. Are these the right axes? Are the thresholds the right strictness? How should the gates accommodate different indication areas with different baseline maturity?

2. **How should "promise of future equity" be valued?** Calibration against comparable for-profit equity at an equivalent stage is a reasonable anchor, but "equivalent stage" is not well-defined for an organization that intentionally separates research from commercialization. A shared framework would let multiple mission-driven organizations adopt the mechanism without each one reinventing the legal wheel.

3. **What fraction of subsidiary revenue should flow back as people-as-seed-funders reinvestment?** Too low, and the mechanism is symbolic. Too high, and it strangles the subsidiary's ability to reinvest in its own scale. A defensible band, informed by comparable nonprofit-to-for-profit revenue-share examples, would help many organizations decide.

4. **Should mission-lock rely primarily on bylaws, on IP-licensing terms, on community governance, or on external review?** The Framework proposes all four simultaneously. In practice, which layer is the binding constraint? Which can be dropped without compromising the whole?

5. **How does the Framework scale to non-US jurisdictions?** A UK subsidiary operating under different nonprofit law, a subsidiary with European PBC-equivalents, or a subsidiary in a low-income country with different regulatory and tax regimes, each impose constraints the US-centric draft has not yet fully worked through. We are beginning to engage with this through a planned Cytognosis UK office; community input from organizations that have already done cross-jurisdiction work would accelerate that engagement substantially.

6. **How should a 501(c)(3) and its affiliated PBC price the IP license between them when there is no revenue and few comparables?** Fair-market value is both the legal requirement and the basis for the rebuttable presumption of reasonableness, but the practical method for valuing a pre-revenue platform is unsettled. A shared, defensible approach would let many mission-driven organizations clear the same hurdle without each one improvising a valuation under audit risk.

7. **What is the cleanest tax treatment for the two capital mechanisms?** Does a promise of future equity issued during the nonprofit phase create a current private benefit or a present taxable event, and how should the people-as-seed-funders reinvestment be characterized so it reaches the Foundation as royalty income excluded from unrelated-business-income tax rather than as an entanglement that threatens exemption?

8. **When should the for-profit strand be created, and what may it build on?** The framework assumes the PBC is incorporated at the first gate, but a consumer product or an accelerator opportunity can arrive earlier and force the question. We think the cleaner answer is that an early for-profit should build on the open core that anyone may use, rather than on a transferred asset that would require a fair-value sale out of the nonprofit, but the timing, the founder's dual role, and the arm's-length mechanics deserve the field's scrutiny. We are facing this question ourselves as we write.

## Acknowledgments

This paper synthesizes ideas from a community that has been generous with its work. Special thanks to Adam Marblestone, Sam Rodriques, and collaborators at Convergent Research; Ben Reinhardt and Eileen Nakahata at Speculative Technologies (whose *Playbook for Research Leaders* provides much of the comparative scaffolding here); Prachee Avasthi and the Astera team (whose Open Science Policy is the clearest articulation we have seen of structural openness); the Wellcome Leap team behind MARFA and CORFA; and the program leadership at ARPA-H, ARIA, and Arc Institute for public writing that informed this analysis. Errors and opinions are the author's.

## References

*This is a working reference list; DOIs will be added with the Zenodo deposit of the final version.*

- Collins, F. S., Schwetz, T. A., Tabak, L. A., & Lander, E. S. (2021). ARPA-H: Accelerating biomedical breakthroughs. *Science* 373, 165-167.
- Critchlow, T. (2021). Reimagining the Research Lab. Blog post.
- DeBenedictis, E. A. (2022). Erika's Quick-Start Guide to Research Nonprofits. Substack.
- Heilmeier, G. H. (1992). Some Reflections on Innovation and Invention. *The Bridge* 22(2).
- Lutter, M. (2021). Startup Nonprofits. Blog post.
- Marblestone, A. et al. (2020). Focused Research Organizations to Accelerate Science, Technology, and Medicine. Federation of American Scientists.
- Muthusamy, A. K., & Garrett, D. (2023). Developing a Scalable Platform for Human Molecular Monitoring. Federation of American Scientists white paper.
- Reinhardt, B. (2021). Shifting the Impossible to the Inevitable: A Private ARPA User Manual.
- Reinhardt, B., & Nakahata, E. (2025). A Playbook for Research Leaders.
- Rodriques, S. et al. (2022). A Vision of Metascience.
- Stokes, D. E. (1997). Pasteur's Quadrant: Basic Science and Technological Innovation. Brookings Institution.
- Webb, M. (2021). Towards the Orthogonal Technology Lab. Blog post.

*Additional citations for specific organization structures (ARPA-H mission office documents, ARIA charter, Wellcome Leap HBNet documentation, Convergent Research FRO selection criteria, OpenAI governance documents, Mozilla MPL and organizational structure, Arc Institute founding documents, Astera Open Science Policy) to be added in the final reference list.*

*End of working draft. Comments invited at helix-commentary@cytognosis.org. Next revision cycle: Q3 2026.*

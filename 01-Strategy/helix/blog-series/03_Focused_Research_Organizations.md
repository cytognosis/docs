---
title: Focused Research Organizations
subtitle: What Convergent Research Got Right, and Where FROs Stop by Design
series: The Helix Series
part: 3 of 6
reading_time: 10 min
license: CC BY 4.0
---

# Focused Research Organizations

## What Convergent Research Got Right, and Where FROs Stop by Design

In 2020, a group of researchers led by Adam Marblestone published a short paper at the Federation of American Scientists proposing a new institutional form: the Focused Research Organization, or FRO. The paper argued that a surprisingly large class of scientific bottlenecks were of a very specific shape, and that this shape fit neither academic grants nor commercial R-and-D, and that the correct response was to build a new kind of organization. Five years later, several FROs have shipped, Convergent Research has become the operational spine supporting them, NSF Tech Labs is giving the model federal funding, and FROs are probably the single most successful new institutional form in the recent metascience wave.

This post is about what makes the FRO work, where it fits, and (critically for healthcare) the specific shape of what an FRO cannot do by design.

## The insight that makes the FRO work

Marblestone and collaborators observed that many scientific fields are bottlenecked on *specific pieces of infrastructure* that nobody is incentivized to build. A tool, a dataset, a platform, a methodology. Something whose absence blocks a huge amount of downstream work, but whose construction does not fit any existing funding mechanism.

Why not academia? Because the required work is engineering-intensive, not hypothesis-driven. It takes a team of engineers working together for years. Universities reward individual-PI publications. The engineers who would build the platform have no one's tenure case to join.

Why not industry? Because the output is infrastructure, not a product. The eventual commercial value is diffused across many downstream users, and no single company can capture enough of it to justify the upfront investment. Even if a company *would* build it, they would then own it, and its value to the field would drop to whatever license terms they offered.

Why not ARPA-like programs? This is the subtler point. ARPA programs fund *portfolios* of ambitious research, managed by a program director, distributed across many performers. They are excellent at exploring a design space. They are not structured to build one specific, concrete, integrated artifact that requires a dedicated team under unified management.

The FRO is the answer to this specific shape of problem. A standalone nonprofit organization, with a single integrated team, pursuing one concrete infrastructure artifact, on a defined timeline (typically three to seven years), and then dissolving. The output is released openly so the field can use it.

## The FRO shape test

Convergent Research, founded in 2022 to operationalize the FRO concept, has articulated criteria for what makes a problem "FRO-shaped." Simplified:

- **Concrete output.** You can name the artifact in a sentence. "A scalable platform for whole-brain connectomics at single-neuron resolution." "A programmable multi-analyte biosensor for continuous molecular monitoring."
- **Engineering-intensive.** The hard work is building something, not figuring out what to build. The science is mostly settled.
- **Single integrated team.** The work does not naturally split across independent labs. It needs one team moving in one direction.
- **Natural end date.** The organization has a clear "done" condition: when the artifact is delivered.
- **Obvious downstream community.** If the artifact exists, many people will use it. The demand is obvious; the supply is absent.
- **Widely beneficial.** The artifact opens up scientific work that would otherwise be blocked. Not a product; a capability.

This test is what makes the FRO a category, not just a nonprofit research lab. Organizations that fail the test (projects that are open-ended, exploratory, or that require ongoing operation rather than delivery of a finished artifact) are better served by other structures.

## What Convergent Research does

Convergent plays a role that would be unfamiliar to most nonprofit lawyers: it provides shared operational infrastructure to independent FROs. Legal formation, governance templates, HR, finance, fundraising, compliance. This lets the FRO founding team focus on the scientific work rather than reinventing operational wheels. The FROs remain independent legal entities with their own governance; Convergent is the shared backbone that reduces transaction cost of launching each one.

This matters for a non-obvious reason. The weakest part of most mission-driven research organizations is not the science. It is the operational scaffolding. Finding a good payroll provider for a multi-state research organization. Getting IRB coverage. Drafting IP-licensing terms that do not accidentally give up too much or hold onto too much. Negotiating the right 501(c)(3) structure. These are ten to fifteen pieces of infrastructure that every new FRO would otherwise build from scratch, and that Convergent has already built and tested.

## Four FRO case studies

### E11 Bio: connectomics at scale

E11 Bio is building infrastructure for whole-brain connectomics at single-neuron resolution in small mammals. This is canonically FRO-shaped. The scientific goal is concrete. The engineering is the hard part: existing electron microscopy pipelines cannot scale to whole-brain volumes at the required throughput, and solving the scaling problem is a multi-year team engineering project, not a set of independent PI grants. When E11 is done, neuroscience at large inherits the pipeline.

### Forest Neurotech: minimally-invasive whole-brain BCI

Forest is developing minimally-invasive, whole-brain-scale neural recording and stimulation using ultrasound. Same FRO shape: specific technology target, clearly defined "done" state, obvious downstream adoption if the technology works. The interesting wrinkle here is that the technology has commercial potential. Forest has been structured so that the FRO delivers the core technology openly, and subsequent commercial products build on that open foundation.

### IMPRINT: high-resolution immune profiling

IMPRINT is building high-resolution infrastructure for profiling immune system state. The motivating observation is that immune heterogeneity underlies a huge amount of disease variability, and that no existing infrastructure can profile it at the scale and depth required for population-level understanding. Building that infrastructure is a multi-year integrated engineering problem; once built, it unlocks a large body of work on immune-mediated conditions.

### A new platform for human molecular monitoring

The molecular monitoring FRO (motivated by the Muthusamy and Garrett 2023 white paper) is developing CMOS-integrated, programmable affinity biosensors for continuous tracking of 100+ analytes. This is particularly relevant to healthcare moonshots in our context at Cytognosis because continuous molecular monitoring is exactly the platform capability our Cytoscope program needs, and it is not something we are funded to build. The FRO builds the *measurement technology*; downstream organizations figure out what to measure for whom, how to validate clinically, and how to deploy equitably.

This relationship, FRO builds the platform, downstream organization figures out how to use it, is exactly the kind of structural complementarity the field needs more of. ARPA-H's emerging Delphi program plays a similar role on the chiplet side. But neither the FRO nor the ARPA-H program is structured to *carry* the technology through clinical validation. That has to be somebody else's job.

## What FROs have proven

FROs have demonstrated three things that are genuinely new:

1. **A startup-culture nonprofit can ship scientific infrastructure at industry speed and quality.** The team feels like a startup. The output is a public good. The model works.
2. **Modest total investment ($20 to $100M over five years) can produce infrastructure that unlocks much larger downstream value.** This is the leverage point of the whole idea.
3. **Shared operational scaffolding (Convergent) dramatically lowers the transaction cost of launching new research organizations.** This is a general lesson that applies beyond FROs.

## What FROs do not do, by design

Here is the structural limit. An FRO dissolves when its deliverable is complete. That is not a bug; it is the whole point. The artifact is handed to the downstream community, the organization wraps up, the team disperses (often to academia, industry, or to found new FROs on adjacent problems).

For scientific infrastructure, this is exactly right. The field inherits the output and uses it.

For a healthcare technology that must be carried through FDA submission, clinical validation at scale, reimbursement negotiation, manufacturing certification, and equitable deployment, the "hand it to the downstream community and dissolve" model does not work, because there is no downstream community ready to receive a technology in this regulated-product shape. The downstream community for an FRO deliverable is *the scientific field using the artifact*. The downstream community for a healthcare product is *patients under regulatory constraints*. Those are different structures, with different capital requirements, and the gap between them is where most healthcare moonshots stall.

This is not a criticism of FROs. It is a statement about what the FRO category is *for*. The right lesson is that FROs handle the first layer of a multi-layer problem exceptionally well, and that a healthcare moonshot organization needs an *additional structure* (not an FRO-replacement, but an FRO-complement) to carry the output through the next decade.

The next post is about the class of organizations that has tried to span both layers: the hybrids.

*Part 4: [The Hybrid Experiment](04_Hybrid_Organizations.md)*

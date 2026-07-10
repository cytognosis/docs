---
title: Openness as Operational Discipline
subtitle: Astera, Arcadia, OpenBCI, and What "Open Science" Looks Like When It Is a Contract Term
series: The Helix Series
part: 5 of 6
reading_time: 10 min
license: CC BY 4.0
---

# Openness as Operational Discipline

## Astera, Arcadia, OpenBCI, and What "Open Science" Looks Like When It Is a Contract Term

Almost every mission-driven research organization claims to support open science. Most of them do so in a value statement, a mission paragraph, or a blog post. A much smaller number have made openness a *structural* feature of their operations: something contractually required, operationally enforced, and unable to be quietly dropped when it becomes inconvenient.

This post is about the organizations in the second category. Four in particular are worth studying because they have taken openness from aspiration to operational discipline in different ways, and because the lessons extend well beyond any single one of them.

## Astera Institute: openness as a prohibition

Astera Institute is a nonprofit philanthropic organization that runs a residency program funding researcher-led moonshot projects across neuroscience, AI-enabled life sciences, and open science. What makes Astera structurally distinctive is not what it funds; plenty of philanthropic foundations fund moonshots. It is what it *prohibits*.

Astera's Open Science Policy (published under DOI 10.5281/zenodo.17873235) includes the following operational constraint: *Astera funds and time cannot be used to contribute, as an author or otherwise, to the creation of journal publications.* Astera will not appear as an affiliation on a journal article, will not pay publication fees, will not permit outputs to be delayed for journal review.

The framing, in Astera's own words, is that the journal-publication system "is fundamentally unfit" for openness and "is a relic of the past," and that continued support of it is incompatible with building an abundant, open future. The policy is an intentional forcing function: researchers are contractually required to publish outputs continuously as FAIR research artifacts, with DOIs, on venues like Zenodo, bioRxiv, nanopublications, and protocols.io, rather than accumulating them toward an eventual journal article.

This matters for two reasons. First, it is the clearest articulation I have seen of openness as *structural constraint* rather than *cultural aspiration*. Astera has not just said it supports open science; it has made its operational policy incompatible with the main institutional alternative. Second, it models what it looks like to forcing-function your own team into new publication habits, with full awareness that those habits are disruptive, that appropriate measures of quality and reach are not yet established in the alternative, and that researchers may find the transition uncomfortable.

The lesson generalizes: **if your organization claims an open-science commitment but your contract templates do not operationalize it, your commitment is aspirational.** Turn the aspiration into a prohibition on the alternative and the commitment becomes durable.

## Arcadia Science: radical openness as a default disposition

Arcadia Science, founded in 2021, is a for-profit research organization with a radically open default. Every result is published on Arcadia's platform as soon as it is ready for reuse. Arcadia explicitly includes an "icebox" category for results that did not produce clean narratives, rejecting the journal-publication structure that filters for only-positive results.

What makes Arcadia interesting, relative to Astera, is that it is *for-profit*. The openness is not structurally required by charitable-purpose rules. It is a choice the organization has made about how to operate. This is important because it demonstrates that openness and for-profit status are not inherently in conflict. An open-by-default for-profit is possible; Arcadia is one.

The open question is sustainability. Arcadia's revenue model, like any new research organization's, is still being developed. Whether radical openness can be sustained at scale when commercial pressures increase is the test the next five years will run.

The lesson: **openness as a default disposition is compatible with for-profit operation, but the revenue model must be designed so that closing outputs does not become the structurally easy path.** For-profit organizations that "default to open" without thinking carefully about how their revenue model interacts with that default tend to drift toward closed outputs as they scale.

## OpenBCI: open-source hardware that actually pays the bills

OpenBCI is a Brooklyn-based for-profit company making open-source brain-computer interface hardware (Cyton, Ganglion, and now the Galea mixed-reality BCI platform). The hardware is fully open: schematics, firmware, bill of materials, reference designs. The company has been operating since 2013, which makes it one of the most durable open-source-hardware businesses in existence.

The revenue model is deliberately diversified. Hardware sales. Software subscriptions. Paid R-and-D partnerships with larger actors, including a notable partnership with Valve Corporation for the Galea mixed-reality platform. This diversification has kept OpenBCI independent without requiring VC timelines that would pressure closure of the open-source core.

Two things matter about the OpenBCI model specifically for healthcare moonshot organizations thinking about hardware.

**First, the licensing choice matters.** OpenBCI's hardware is open under permissive licenses (the exact terms vary by component), which means competitors can copy it. OpenBCI competes on brand, community, service quality, and continued hardware innovation, not on legal exclusivity. This is the open-source-hardware business thesis in one line: *if your product's value comes from ongoing innovation and service rather than from being hard to copy, openness is sustainable.* For healthcare devices where service, clinical validation, regulatory approval, and ongoing support are the dominant value components, this thesis is specifically applicable.

**Second, strategic partnerships can coexist with radical openness.** The Valve partnership is not a situation where Valve gets a closed version of Galea and OpenBCI keeps the open version. Both versions are the same platform. The partnership works because Valve's business need is access to a capable, rapidly evolving platform, and OpenBCI's business need is capital and user-base growth. Neither requires closure of the core.

The lesson: **open-source hardware is commercially viable when the business generates margin from services, subscriptions, and partnerships, rather than from legal exclusivity around the core.** This is a model directly applicable to healthcare hardware (wearables, sensors, consumer devices) and one that should be specifically studied by any healthcare moonshot organization building device infrastructure.

## Episteme: researcher-centric for-profit R-and-D

Episteme positions itself as a researcher-centric for-profit R-and-D organization, explicitly modeled on the golden age of Bell Labs but updated for the modern context. Researchers are given multi-year independence. Patent royalties flow to the researchers whose work produced them. Shared infrastructure (compute, wet-lab capacity, legal and IP support) is provided centrally so researchers do not spend time on it.

Episteme is a different case from the others in this post because it is not primarily an "open by default" organization. Its openness commitments are situational: some work is open, some is patented and licensed. What makes it interesting in this context is the *researcher-centric* structural choice. Researchers retain significant economic stake in their own work. The organization operates as an alignment between researcher incentives and commercial viability, rather than asking researchers to subordinate their interests to organizational ones.

The open question is whether this model can be sustained commercially without the monopoly-rent environment that sustained Bell Labs. AT&T's monopoly funded Bell Labs' researcher independence for decades. Episteme does not have a monopoly-rent parent. Its revenue model depends on research outputs generating licensing and commercial revenue at sufficient scale to fund ongoing researcher independence. Whether this is repeatable without a monopoly is genuinely uncertain.

The lesson is indirect but important: **researcher economic stake is a lever most mission-driven organizations underuse.** FROs treat researchers as team members on a defined project. Hybrids treat researchers as employees of a nonprofit or for-profit. Episteme treats researchers as primary beneficiaries of their own work. Each of these is a defensible choice. For healthcare organizations that want to attract and retain the level of scientific talent healthcare moonshots require, the researcher-centric model is worth examining carefully, even if the exact Episteme variant is not directly replicable.

## What these four tell us together

Across the four, three durable lessons emerge.

**One: openness is most durable when it is a *structural constraint* rather than a *value statement*.** Astera's prohibition on journal publication, Arcadia's all-results-including-negative-ones default, and OpenBCI's schematics-on-GitHub default are structural. Any organization whose openness commitment can be quietly dropped by a new CEO or a new funding pressure has an aspirational commitment, not a structural one.

**Two: openness and commercial viability can coexist, but only when the revenue model does not pressure closure.** OpenBCI's diversified revenue (hardware, subscriptions, partnerships) is the best-documented example. Organizations whose revenue depends on exclusive access to IP will drift toward closing that IP, whatever their founding charter says.

**Three: the licensing and publication choices you make at founding are structural.** Astera could not have added its journal prohibition three years in without extensive organizational rework. OpenBCI could not have pivoted to closed hardware without breaking its entire community relationship. These structural choices compound. For organizations being founded now (any organization planning to operate for 15 years, any organization trying to operate at the healthcare moonshot frontier), the licensing and publication structure needs to be designed into the founding documents and not added later.

The Astera residency model in particular is worth engaging with seriously. The choice to treat journal publication as *incompatible with Astera funding* is the kind of structural forcing function that turns a stated commitment into a durable one. Any mission-driven healthcare organization should look at its own contract templates and ask: does anything here enforce the openness we claim to support, or are we relying on our own good intentions?

The next and final post in this series is about what all of these organizations, taken together, still leave unaddressed for healthcare, and about the Helix Framework as one candidate structural answer.

*Part 6: [What's Still Missing](06_Desiderata_And_Helix.md)*

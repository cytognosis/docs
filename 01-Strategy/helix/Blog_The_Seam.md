---
title: The Seam
subtitle: How do you wire a nonprofit and a for-profit together so the mission survives contact with capital?
series: The Helix Series
part: companion essay
reading_time: 11 min
license: CC BY 4.0
---

# The Seam

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: leadership
> **Tags**: `strategy`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)

## How do you wire a nonprofit and a for-profit together so the mission survives contact with capital?

Almost everyone building mission-driven science agrees on the values. Open by default. Equitable access. Patients before shareholders. You will not find an argument about whether those are good things.

The arguments that actually sink organizations are not about values. They are structural, and they show up at one specific place: the seam where the nonprofit meets the for-profit. We recently published a long comparative paper on how the new generation of research organizations is built, from ARPA-H and Wellcome Leap to Focused Research Organizations to hybrids like OpenAI and Mozilla. This essay is about the part we found hardest to write, because it is the part almost nobody writes down: the seam itself.

## Why you cannot avoid the seam in healthcare

A healthcare moonshot needs two things that no single legal entity provides well.

It needs patient, non-dilutive capital for the platform years, when you are building models, datasets, and sensors that will not generate revenue for a long time. That is nonprofit and grant territory. And it needs commercial capital, regulatory muscle, and manufacturing scale to actually reach people, under FDA and reimbursement constraints, on a timeline that venture investors will fund. That is for-profit territory.

Try to do both inside one entity and you get the failure modes the comparative analysis kept surfacing. A pure nonprofit builds beautiful open infrastructure and then hands it off at exactly the moment the hard clinical decade begins, and the handoff is where things die. A pure for-profit raises the capital but quietly optimizes away the equity-of-access commitments the moment they cost money. So you end up with two entities: a 501(c)(3) and a Public Benefit Corporation. The interesting engineering is not in either box. It is in the wire between them.

## Three ways the wire fails

The comparative work gave us a short list of how the seam breaks.

Principal-dependent mission lock. The mission holds only as long as the founder is in the room. Leadership turns over, and the commitments turn out to have been personalities, not structure.

Capped-profit as the only brake. OpenAI is the cautionary tale. When the commercial subsidiary controls the compute, the hiring, and the data, the nonprofit parent's theoretical veto becomes nominal. A cap on profit is not a lock on mission.

Handoff failure. The FRO or the ARPA program delivers its piece and dissolves, and there is no structure standing to carry the work through the next ten years. In healthcare, that gap is the whole game.

## The Helix wiring, in plain terms

Our proposed answer pairs a 501(c)(3) Foundation with one or more PBC subsidiaries, and puts the load on three things.

The Foundation owns the platform IP outright, holds a governance majority on the subsidiary's board, and keeps a perpetual, non-revocable license to use everything it built in the open mission no matter what the subsidiary decides later. Control comes from the charter and the IP, not from owning the whole cap table. That is deliberately between Mozilla (which owns its for-profit entirely, but has a revenue model that does not transfer to healthcare) and OpenAI (which holds a minority stake that the commercial reality eventually overwhelms).

The core stays open. The foundation models, datasets, schemas, and the sensor-integration protocol ship under open licenses. The subsidiary gets a royalty-bearing, field-of-use-limited license to build commercial products on top. We do not patent our own methods defensively; an open release plus prior art is a stronger shield for an open-mission organization than a patent is.

And two capital mechanisms try to fund the part the market will not. A promise of future equity gives the people who do the non-dilutive early work a documented, vesting share of the future subsidiary's upside, so a nonprofit can compete for talent against startups. People as seed funders treats the public that funded the early work (through philanthropy or through the taxes behind public grants) as the seed investor, and routes a defined slice of future revenue back to the Foundation for access, education, and more research.

## The part that actually keeps us up at night

Here is the section the first version of our paper quietly skipped, and the reason we are publishing this essay.

A charity that helps create a for-profit, shares its founder and staff with it, and licenses its IP to it, is exactly the arrangement that nonprofit law watches most closely. The words that matter are private inurement (a charity cannot let insiders skim its value), private benefit (it cannot exist to enrich a particular company), excess-benefit transactions (insiders who take more than fair value owe personal penalty taxes), and unrelated-business-income tax (the wrong kind of revenue gets taxed and, at the extreme, threatens the exemption itself). Get the wiring wrong and you do not just look bad. You can lose the thing that made the structure worth building.

We are not lawyers, and the design below is under review by our counsel rather than settled. We publish it so the next person building this seam does not start from a blank page. It rests on five moves. Independent directors with no stake in the for-profit approve every transaction across the seam, and anyone who sits on both sides recuses. Everything that crosses the seam is priced at fair market value, with an independent valuation and contemporaneous comparables, which is also how you earn the legal safe harbor (the rebuttable presumption of reasonableness). The Foundation takes its return as a genuine passive royalty, which is generally outside unrelated-business-income tax, and keeps the active business inside the PBC. Compensation for any insider is benchmarked and board-approved. And all of it is in writing, reviewed by counsel, before any value moves.

We want to be honest about what is still unsolved, because pretending otherwise is how organizations get into trouble. How do you put a fair-market value on a platform with no revenue yet and no clean comparables? Is a promise of future equity a taxable event today or a contingent interest tomorrow? How do you characterize the give-back to the Foundation so it stays clean? These are real questions, and we do not think any single organization should answer them alone.

## We are living this right now

This is not abstract for us. As we write, we are working through a textbook instance of the seam. We have a consumer product that wants to be a for-profit, and a science platform that needs to stay a mission-locked nonprofit. The clean move, we think, is to let the for-profit build on the open core that anyone may use, rather than to transfer an asset out of the charity, which would demand a fair-value sale and all the scrutiny that comes with it. We are working out how a founder can be paid across two entities without breaching the arm's-length discipline, and how to value a license when neither side has revenue. We will tell you how it goes, including if it goes badly.

## An invitation

We published the full paper, and we are publishing our operational documents (bylaws, the fifteen-year roadmap, the Phase I plan) as open artifacts under CC BY 4.0, because the questions at the seam cannot be answered by one organization staring at its own bylaws. They get answered by the people building these structures comparing notes in the open.

So this is an open invitation, and a specific one. If you are at Astera, Convergent Research, or Speculative Technologies, you each built one of the models we analyzed, and your fingerprints are already on this thinking; we would be honored to have you mark it up, argue with it, and, if it earns it, co-sign it. If you are a founder about to write your own bylaws, read the eight open questions in the paper first, especially the one about which mission-lock actually binds. If you are a funder, ask your grantees how many of the twelve desiderata they are actually built to ship.

Tell us where we are wrong. Comments are open at helix-commentary@cytognosis.org, and the source is on GitHub under CC BY 4.0. The point of writing this down was never to close the conversation. It was to start one at the seam, where the real arguments live.

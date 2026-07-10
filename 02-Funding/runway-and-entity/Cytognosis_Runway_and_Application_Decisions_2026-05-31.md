# Cytognosis — Runway and Application Decisions

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: leadership, grant team
> **Tags**: `funding`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)

**Date:** 2026-05-31 · **For:** Shahin · **Status:** decision memo (read this, then we lock the forks)
**Covers:** the Oct 1 income cliff, and go/no-go on Foresight (today), YC (overdue), EA/LTFF, and the two Coefficient Giving applications.

---

> [!IMPORTANT]
> **TL;DR (bottom line up front)**
> - **You are not as cornered as today feels.** Two facts change the picture: **Foresight is a rolling monthly deadline** (next one June 30, not a one-shot today), and **your SDI income runs until ~Oct 1**, so the cliff is about four months out.
> - **Survival should not ride on one grant.** No single grant here is a safe bet, because the best-fit runway grants (Coefficient Career Transition, EA LTFF) are framed for AI-safety / global-catastrophic-risk, not a mental-health app. So we stack several independent shots **and** lock a founder-controlled backstop.
> - **The single most important action is not a grant.** It is confirming the **SDI-while-working and Medi-Cal rules with a benefits specialist**, and pre-arranging the **401(k) rollover + personal-loan** option so it is ready if needed. That is the floor under everything else.
> - **Three decisions to make** (end of memo): how to handle **Foresight today**, whether to **wait on YC until Fall**, and what I should do **next**.

---

## 1. The real runway picture

You framed this as "income drops to $0, need income by Oct 1." Here is the precise version, from your own `FUNDING_STRATEGY_AND_PI_COMP.md` (May 29):

| Fact | Number | Note |
|---|---|---|
| SDI income now | ~$6.5K/month | Ends ~Oct 1, 2026 (52-week statutory cap; confirm exact date with EDD) |
| Personal floor | ~$7K/month net (~$135–165K/yr gross) | Fixed obligations from 20 years of senior employment |
| CEO contract pay | $0 until Foundation raises ≥$800K, then $13,750/mo | Deferred accrual (an IOU, not cash) starts Sept 8, 2026 |
| Savings | Turn negative after the cliff if nothing lands | |

So the clock is real, but it is **~4 months**, not today. That is enough time to run several grant shots to a decision **and** stand up a backstop. The job of this memo is to make sure at least one path clears the floor, with honest odds on each.

---

## 2. Decision 1 — Foresight (the "due today" one)

### What is actually true

- **It is rolling.** Foresight "AI for Science & Safety Nodes" takes applications on the **last day of every month** with ~2-month review. Today (May 31) is this month's cutoff; **June 30 is the next one.** Missing today costs one month, not the opportunity.
- **The money is small; the real prize is the node.** Grants run ~$10K–$100K. Your draft asks $45K–$75K. The bigger value is what you already identified: **a physical SF office (50 California St), local compute, and an in-person community** of AI-safety / neuro / longevity people. Ed Boyden is a past grantee; Konrad Kording, Talmo Pereira, Blake Richards are affiliates.
- **In-person is required, and that helps you.** Foresight funds "funding-only" requests only in exceptional cases; they want you physically in the hub. You are in Daly City, so the SF node is a perk, not a blocker. Your draft already commits to 4–5 days/week on-site, which fits.

### The problem (this is your deviation worry, made concrete)

Your Foresight draft pitches **"Neuroverse"** with **Solid pods, post-quantum cryptography (ML-KEM/ML-DSA), peer-to-peer federated learning, and Muse/Emotiv EEG pilots**. **Almost none of that is on the actual Yar roadmap** (Yar = Flutter + on-device Gemma + Anytype + CAP + vocal biomarkers + wearables via the sensor protocol). The draft leaned hard into Foresight's AI-safety lens and, in doing so, committed to an 18-month plan to build things you are not otherwise building.

That is exactly the trap you flagged: a grant pulling you toward work you would not do anyway. And your own May 29 strategy doc already says to fix it ("deprecate Neuroverse, frame as Cytonome, fund the platform not a pivot"), but the Foresight draft has not been updated to match.

### Recommendation

> [!TIP]
> **Realign the draft to the real roadmap, then submit. Today if you want the 2-month-earlier review; otherwise June 30. Do not submit the over-committed version as-is.**

The realignment is about 1–2 hours of editing, and makes the application both **honest** and **stronger**:

1. Rename **Neuroverse → Cytonome** (the edge/safety substrate of GPS for Health), per your strategy doc.
2. Demote **PQC + Solid pods + federated learning** from hard 18-month deliverables to **"evaluate / adopt where feasible"** roadmap items. Keep the privacy-first, on-device, zero-custody narrative (that part is genuinely true and is Foresight's lens).
3. Map milestones to the **real stack** you would build anyway: on-device Gemma, CAP safety gate, vocal-biomarker mood sensing, Brain Weather, wearables via the sensor protocol. The EEG pilot becomes optional Phase-0 exploration, not a core promise.
4. Keep the PI-sustainment line (the draft already correctly says the PI is funded via Career Transition, so Foresight money is 100% project costs).

This way, if funded, every deliverable is something that advances Yar/Cytonome regardless. No pivot.

---

## 3. Decision 2 — YC (overdue)

### Verified facts (you asked me to check)

| Question | Answer |
|---|---|
| For-profit deal | **$125K for 7%** + **$375K uncapped MFN SAFE** = "$500K standard deal." ~1% acceptance. |
| Does YC take equity from nonprofits? | **No.** Nonprofits get a **charitable donation, no equity, no dilution.** 2–4 nonprofits/batch, 30+ since 2013 (Watsi was first). |
| Catch for nonprofits | YC **favors fee-charging / cost-covering nonprofits** over donation-dependent ones. Yar (a product that can charge) fits that better than a pure-science nonprofit. |
| Next batch | **Fall 2026** (Demo Day Dec 2). Apply deadline not yet posted; by pattern **~August**. Late/rolling apps accepted. |
| YC → Google Cloud | YC acceptance **unlocks the Google Cloud $200K–$350K AI tiers** you cannot reach unbacked (today you qualify only for the ~$2K starter). |

### The strategic read

You have been rejected twice (Winter 2025, Spring 2026), and the standing weakness is the same: **no user base.** Re-applying right now repeats that weakness. But you are sitting on two things that would flip it, and you named both:

- **A warm first user base you have not activated yet** (your queer / trans / nonbinary / poly / neurodivergent community: eager, aligned, already sending WGS data, with Olivia as a design partner). This is the lowest-activation-energy move you have.
- **A potential ElevenLabs partnership** (on-device TTS for personas) that would be a real logo + capability story.

> [!TIP]
> **Recommendation: do not rush YC now. Apply Fall 2026 (deadline ~August).** Use June–August to (1) stand up the community design-partner cohort so you have real users and retention signal, (2) advance the ElevenLabs conversation, (3) ship visible Yar progress. That turns "no users" from your fatal weakness into your headline.

YC is **not a runway solution** for the Oct 1 cliff (even Fall acceptance pays out ~Sept–Oct, and for-profit means dilution + reopening the whole nonprofit-vs-PBC question). Treat YC as a **medium-term credibility + capital + Google-unlock play**, decided closer to August.

**Nonprofit vs for-profit** is a genuine fork I should not pick for you: nonprofit = zero dilution and fits the Foundation, but YC prefers fee-charging nonprofits and you have been rejected twice on the science-nonprofit framing; for-profit PBC = the $500K + Google-tier unlock, at the cost of early dilution and committing to the bifurcation now. My lean is **decide in August**, framed around whichever has users + ElevenLabs behind it.

---

## 4. The deviation worry, generalized (Foresight / EA / Coefficient)

Your rule is "no small grant that forces us into something different." Here is the honest split:

- **Where the framing is fine (no real pivot):** EA/LTFF and the two Coefficient applications fund **PI effort + the Cytonome safety substrate**, described in AI-safety / global-catastrophic-risk vocabulary. The *words* are borrowed, but the *work funded* (privacy-first edge AI, on-device safety, the founder's salary) is exactly what you are doing. That is acceptable, as long as every deliverable maps to real Cytonome/Yar work. Your strategy doc's "coordination clause" already enforces this.
- **Where it is a real over-commitment (fix it):** only **Foresight**, because it promised to *build* PQC + Solid + federated + EEG. Fixed by the §2 realignment.

So the worry is valid for exactly one application, and it is fixable. Everything else is framing, not a pivot. The guardrail (already in your strategy doc): **every application anchors to a named platform component** (Cytonome = Navigator, Cytoverse-Neuro = Map), carries the "three blindspots / intercept years before symptoms" through-line, and uses the capped-PI coordination clause.

---

## 5. Runway: ranked branches with rough odds

> [!NOTE]
> The probabilities below are **founder-judgment estimates, not precise numbers.** They are here to help you compare paths and avoid betting on one. "Fit risk" = how well a mental-health platform matches a funder built for something else.

### Short-term shots (decision/cash possible before Oct 1)

| Path | Provides | Cash timing | Rough odds | Counts to $800K? | Key risk |
|---|---|---|---|---|---|
| 🟢 **Coefficient Career Transition** (individual) | **$165K**, covers the floor alone | Rolling, ~6-wk review → cash ~Aug if submitted now | **30–45%** | No | Fit: must read as an AI-safety/safe-neuro-AI *career transition*, not "I run a startup" |
| 🟢 **EA Funds LTFF** | ~$120–130K; funds salary | Rolling, ~3.5 wk to cash if funded | **20–35%** | n/a (individual-style) | Fit: x-risk lens; reframe PI effort as safety research |
| 🟡 **AWS Imagine** | $148.5K cash + $100K credits; $62K PI line | Deadline-driven (confirm date) | **10–20%** | Yes | Competitive; confirm deadline before investing time |
| 🟡 **Coefficient Capacity Building** (org) | adds ~$40–50K PI architect line | Rolling | **15–25%** | Yes | Fit: frame as AI-safety field-building |

**Combined:** if you submit Career Transition + LTFF (+ AWS if open), the chance that **at least one** clears the floor before the cliff is meaningfully high (rough 60–70%). The residual ~30–40% is why Tier 0 below is non-negotiable.

### Medium-term (to early 2027)

| Path | Provides | Rough odds | Note |
|---|---|---|---|
| 🟡 **Foresight** (realigned) | $45–75K + SF office + compute + community + prestige | **25–40%** | Small money, big non-money value; resubmission |
| 🔴 **Google.org Impact: AI for Science** | up to $2.49M / 36 mo | **<5%** | Huge if it hits; slow; long shot |
| 🔴 **YC Fall 2026** | $500K (for-profit) or donation (nonprofit) + Google-tier unlock | **5–10%** with users + ElevenLabs | Medium-term, not runway |
| 🔵 **ARPA-H PHO** | clinical-scale | n/a near-term | Planned post-pilot, 2027+ |

---

## 6. The personal-finance backstop (founder-controlled, near-certain)

This is the part that does not depend on any funder saying yes. I am not a financial or legal advisor, so treat these as options to confirm with a CPA / benefits specialist / counsel, not instructions.

| Option | What it buys | Feasibility | Flags to clear |
|---|---|---|---|
| 🟢 **SDI to Oct 1** | ~$6.5K/mo until the cliff | Already in hand | Confirm exact exhaustion date with EDD |
| 🟢 **SDI-while-working + Medi-Cal review** | Avoids accidentally killing benefits the moment any income arrives | High | **Highest-risk unknown. Get a benefits specialist / counsel on this first.** |
| 🟢 **Solo 401(k) rollover + personal loan (up to $50K)** | ~7 months of floor (~$7K/mo) to stretch the mortgage grace period | High (subject to loan terms) | CPA on penalties/timing; this is runway-stretching debt, not income |
| 🟢 **Purdue visiting scholar (with Ananth)** | Bridge **salary** + academic affiliation **+ host-PI status for grants** + credibility | Moderate–high (Ananth is your warmest hub) | **IP terms** (work at Purdue may fall under Purdue IP policy). Resolve in writing first. |

The Purdue option is underrated: it can solve income, give you a host PI for the grants that require an academic host, and add credibility, all at once. The IP question is the thing to settle up front.

---

## 7. Sequenced action plan

Ordered so the lowest-stress, founder-controlled, no-cold-outreach items come first (your stated preference).

**This week (founder-controlled, no external ask):**
1. Book a **benefits specialist / counsel** call on SDI-while-working + Medi-Cal. Highest-risk unknown; do it first.
2. Talk to a **CPA** about the solo 401(k) rollover + personal-loan mechanics, so the option is *ready* (not drawn).
3. Decide Foresight handling (below) and let me **realign the draft**.

**This week (warm, scripted asks — I will write the exact messages):**
4. **Ananth** (visiting-scholar bridge): a short, specific ask with the why-now and the IP question named. He is "like family," so this is low activation energy.
5. Finalize and submit **Career Transition + LTFF** (the two best runway shots), with the capped-PI coordination clause and the Astera scrub your strategy doc already specifies.

**By August:**
6. Build the **community design-partner cohort** + advance **ElevenLabs**, then apply **YC Fall**.
7. With counsel: the **contract amendment** (pay PI comp from designated grant funds before the $800K threshold) + board ratification.

---

## 8. Caveats and glossary

- **Probabilities** are rough founder-judgment estimates to aid comparison, not forecasts. The point is the *shape* (stack independent shots; lock the backstop), not the exact numbers.
- I am **not a financial or legal advisor.** The 401(k), loan, SDI, Medi-Cal, and contract items need a CPA / benefits specialist / counsel.
- **Unverified externally:** exact YC nonprofit donation amount in 2026; exact YC Fall deadline (~August, estimated); AWS Imagine current deadline (confirm before investing time).

**Glossary**
- **SDI**: State Disability Insurance (your current ~$6.5K/mo income, capped at 52 weeks).
- **LTFF**: EA Funds Long-Term Future Fund (funds AI-safety work, including individual salaries).
- **Coefficient Giving**: the Nov 2025 rebrand of Open Philanthropy; its **Career Development and Transition Funding** is your runway anchor.
- **$800K threshold**: the cumulative external funding at which your CEO contract starts paying cash.
- **Capped-PI coordination clause**: the language that caps total PI pay at $165K across all grants, so concurrent awards do not look like double-dipping.

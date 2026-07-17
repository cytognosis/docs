# Fast Forward — Application Draft

> **Status:** Prep · **Date:** 2026-07-16 · **Author:** Shahin Mohammadi

## IMPORTANT correction before you read further

The brief for this draft named "Fast Forward Accelerator, due 2026-07-26." Web verification
(ffwd.org, 2026-07-16) shows that label does not match a real deadline. Two different Fast
Forward programs exist, and the one actually due around now is not the Accelerator.

| | Fast Forward **Academy** | Fast Forward **Accelerator** |
|---|---|---|
| Deadline | Jul 17 **or** Jul 26, 2026 (ffwd.org states both dates on different pages; unverified which is authoritative) | Late July to early September 2026 (2027 cohort; exact date not yet posted) |
| Grant | $10K | $25K+ |
| Length | 6 weeks, hybrid, ~4 hrs/week | 14 weeks, hybrid, ~10 hrs/week |
| Stage required | MVP built, **no real users yet** | Beta or working product, **people already using it** |
| Geography | U.S.-based only | U.S. and international |
| Fit for Cytognosis/Yar | **Strong.** Yar has an MVP (243 passing tests) and explicitly has no users in production yet. | **Not yet eligible.** Accelerator requires people already using the product; Yar does not have that yet. |

**Recommendation: apply to the Academy now, not the Accelerator.** The Academy's own eligibility
language ("MVP with some functionality, but no real users yet... figuring out who it's for") is a
close match for Yar's current state. The Accelerator's hard requirement is a working beta with
outside users, which Cytognosis does not yet have, so an Accelerator application this cycle would
likely be a poor use of the founder's time. Revisit the Accelerator for the 2027 cohort once Yar
has a TestFlight beta and a first retained cohort (targeted 4 to 6 weeks out per the YC draft).

The date conflict (Jul 17 vs Jul 26) is unresolved from Fast Forward's own site and is flagged, not
guessed. **Action needed from Shahin: submit as soon as possible, and do not wait past Jul 17
given the ambiguity.**

Source pages checked 2026-07-16: ffwd.org/academy, ffwd.org/faq, ffwd.org/accelerator,
apply.ffwd.org/2026-accelerator (password-protected placeholder, not the live Academy form),
tally.so/r/xXgb0G (live Academy application, page 1 of 5 rendered; pages 2 to 5 and the
companion Notion question list are JavaScript-gated and could not be fetched headlessly).

## Program facts (verified)

- **What it is:** A six-week, hybrid program for U.S.-based founders using AI to build for social
  impact who have an MVP but have not yet shipped to real users. Comes with a $10K grant.
- **Format:** ~4 hours/week virtual, plus one in-person week in San Francisco (week of Oct 19,
  2026). Program runs the week of Oct 5 through the week of Nov 9, 2026.
- **Notification:** rolling interviews; all applicants notified by Aug 30, 2026.
- **Hard eligibility bar:** U.S.-based founder, building an AI-powered nonprofit, needs support to
  get from MVP to beta. Registration as a nonprofit is not required to apply, but the founder must
  be committed to the tech-nonprofit path. Cytognosis Foundation is already a registered 501(c)(3),
  which exceeds this bar.
- **Cytognosis fit:** strong. Tech nonprofit (EIN 39-4383634), AI is core to the product (on-device
  model pipeline), founder has lived experience with the problem (neurodivergent, late-diagnosed),
  and the product (Yar) is exactly at the MVP-not-yet-shipped stage the Academy is built for.

## Drafted answers

### About You (page 1 of the live form, verified)

**First / last name:** Shahin Mohammadi

**LinkedIn:** [to confirm current URL from Shahin]

**Where are you based?** Daly City, CA.

**What's your current day job or primary role?** Founder and CEO, Cytognosis Foundation. Building
the science platform and its consumer product, Yar, full time since October 2025.

**How did you learn about the Academy?** [Shahin to select: Newsletter / Another organization /
Fast Forward staff / Alumni. Unknown to this draft; confirm before submitting.]

**Have you been part of other accelerators or courses for social entrepreneurs?** Yes. NUCLEATE
(2019). Grant applications are also in flight with ARPA-H, Coefficient Giving, and EA Funds for
the separate nonprofit science platform.

**Video (3 minutes max, demo + "why does the world need this right now"):** Not yet recorded.
**Action needed from Shahin.** Suggested content: a screen capture of the voice brain-dump to
structured, retrievable objects loop (the same demo referenced in the YC draft), followed by a
30-second answer on why ND adults need a private, on-device companion now: roughly one in five
adults have ADHD or are autistic, existing tools are built for a different kind of brain, and
generic health apps fail this population specifically because people stop opening them within a
month, which is why Yar earns a daily habit first and adds sensing later.

### Organization and product (later pages of the form; exact wording unverified — JavaScript-gated)

Fast Forward's stated review criteria are leadership, tech talent, impact potential, scalability,
lived experience, and alignment. The Academy page also asks founders to explain who they are
building for, whether the AI is core (not just a workflow tool), and what stands between the
current MVP and a shipped beta. Drafted answers, ready to slot into the live form once the exact
question wording is confirmed:

**What are you building, and who is it for?**
Yar is a private, on-device AI companion for people whose brains work differently: adults with
ADHD, autistic adults, and late-diagnosed adults, a population estimated at roughly one in five.
It turns voice or text brain-dumps into structured, retrievable tasks, notes, and ideas, without
forcing a linear form. It is built by and for someone who lives the problem.

**Why is AI core to this, not just a workflow tool?**
The core function, turning an unstructured spoken thought into a validated, typed, retrievable
object, is only possible because an on-device language model interprets intent and context in
real time. A safety layer (Cytoplex) sits in front of every model call and blocks diagnosis,
treatment advice, and any unconfirmed data leaving the device. The AI is the product, not an
add-on to it.

**What is the current state, and what stands between here and a shipped beta?**
The MVP works end to end: capture, on-device model, safety gate, confirmed write to a personal
knowledge graph. It has 243 passing automated tests, including 93 on the safety layer alone. What
is missing is real users. The gap to a shipped beta is packaging, onboarding, and getting the
product in front of the first 50 to 100 people in the neurodivergent and queer/trans communities
the founder is already part of, several of whom have already asked to be design partners.

**Why does the world need this right now?**
Late diagnosis of ADHD and autism in adults is a fast-growing wave, and the tools available to
this population are built for a different kind of brain. Health and wellbeing apps in general fail
because people stop opening them within weeks; the daily habit has to come first, before any
health sensing can mean anything. Impact here is measured in restored time, reduced daily friction,
and, over the long run, more people getting support that actually fits how they think, not lives
saved in a clinical sense, since Yar is a wellness and productivity product, not a medical device.

**Founder story and lived experience.**
The founder spent 37 years misdiagnosed across ten medical specialties before using his own
computational genomics work to identify the single rare mutation connecting conditions that had
been treated as unrelated. He built a 20-year career in AI (MIT, the Broad Institute, insitro,
GenBio AI) because it was the environment that fit how his brain works, and he built Yar's working
MVP solo because the tool he needed did not exist.

**What would the $10K and six weeks unlock?**
Direct funding toward the AI tooling and infrastructure costs of getting from MVP to a TestFlight
and App Store beta, plus the structure (user research, go-to-market, storytelling) to convert a
warm, already-interested community into the first measured, retained cohort.

## Submission checklist

- [ ] Resolve the Jul 17 vs Jul 26 date conflict directly with academy@ffwd.org before relying on
      either date; submit early regardless.
- [ ] Record the 3-minute demo video (screen capture of the voice-to-structured-object loop plus
      the "why now" answer above).
- [ ] Confirm current LinkedIn URL.
- [ ] Open the live form (tally.so/r/xXgb0G) and the companion Notion question list to capture the
      exact wording of pages 2 through 5, then map the drafted answers above onto them.
- [ ] Select "How did you learn about the Academy" honestly.
- [ ] Decide whether to consent to sharing the application with ecosystem partners and the
      Tech Nonprofit Directory listing (recommended: yes, low downside, adds visibility).
- [ ] Do not apply to the Accelerator this cycle; its eligibility bar (existing beta users) is not
      yet met. Revisit for the 2027 cohort once Yar has retained users.

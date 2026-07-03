> **Status**: Active
> **Date**: 2026-06-21
> **Author**: @shahin (Cytognosis Foundation)
> **Audience**: product, research, community-facing writers, future diagnostics team
> **Tags**: `yar`, `naming`, `neurodiversity-affirming`, `psych-alignment`, `convention`

# Yar Feature Naming Convention (Affirming and Psych-Aligned)

> **Reading time**: ~6 minutes.
> **If you only read one thing**: the **dual-label rule** below and the **avoid-to-use table**. Public labels describe the support, never a deficit.

---

## Why this exists

We are about to share the Yar feature set with the neurodivergent community for feedback. Labels carry meaning. A deficit-framed or clinically cold name can alienate the very people we serve before the conversation begins. **Priority 1 is affirming, considerate naming.** **Priority 2 is alignment with recognized psychological constructs**, so the labels connect cleanly to our neurobehavioral axes when we move into diagnostics. The two priorities do not conflict because we carry both, in different fields.

## The dual-label rule

Every feature carries three things:

1. **Affirming label (primary, public-facing):** warm, plain, strengths-and-support framed. It names what the feature helps a person do, not what is wrong.
2. **Construct tag (secondary, internal):** the recognized psychological or neurobehavioral construct the feature supports, for axis alignment later.
3. **Domain:** the existing functional domain (AEF, ERM, SCI, SPR, CTO, SMI).

Public-facing docs show only the affirming label and a plain description. The internal matrix keeps the construct tag in its own column and retains a stable feature ID (F01 to F62) plus the original internal name for traceability, so nothing is lost in the rename.

## Affirming principles (Priority 1)

- **Describe the support, not a deficit.** Name the help, not the problem.
- **Person-affirming.** The person is not broken; the feature meets a need or plays to a strength.
- **Use community language where it exists.** Terms like body doubling, brain dump, energy and spoons, and time awareness are owned and trusted by the community.
- **No shame, fear, or pressure framing.** Gentle and optional, never punitive.
- **Warm but not infantilizing.** Friendly metaphors are welcome; cutesy or patronizing ones are not.
- **Plain language.** Expand or avoid jargon; a newcomer should understand the label.

## Avoid to use

| Avoid in public labels | Use instead |
|---|---|
| deficit, impairment | difference, support need |
| disorder, symptom | experience, pattern |
| fix, correct, normalize | support, help with |
| detection (when user-facing and surveillant) | awareness, sensing, check-in |
| distraction blocker | focus support |
| patient, treatment | person, support |
| normal, high-functioning | (avoid; describe the situation) |
| struggle, suffer | find hard, navigate |
| collapse, failure | reset, hard day, plan change |

## Psych-alignment principles (Priority 2)

- Map each feature to a recognized construct where one fits: executive function (task initiation, working memory, prospective memory, cognitive flexibility), emotional regulation (affect, rumination, distress tolerance), social cognition and pragmatics, sensory processing, interoception, and metacognition.
- Keep the construct as the **secondary tag**; never let a clinical term override the affirming public label.
- When no construct cleanly fits, mark the tag "to confirm" rather than forcing a clinical term.

## Worked examples (the standard to match)

| ID | Original internal name | Affirming public label | Construct tag |
|---|---|---|---|
| F54 | Affect detection (voice affect route) | Voice mood awareness | Affect recognition |
| F47 | Thought deconvolution | Untangling parallel thoughts | Thought organization, cognitive flexibility |
| F42 | ND-NT communication translation | Two-way communication bridge | Social pragmatics (double empathy) |
| F48 | Emotional debrief after task collapse | Gentle reset after a hard day | Emotional regulation, self-compassion |
| (safety) | Crisis detection | Safety check-in and support | Risk awareness, safety |
| F04 | Spiciness slider (task decomposition) | Right-sized task breakdown | Executive function: task initiation |

## How this is applied

- Uniformly across the v4 formal master, the v4 ADHD master, and the CSV.
- The CSV gains a `Construct_Tag` column and keeps `ID` plus an `Internal_Name` column for traceability; the `Feature` column becomes the affirming public label.
- The public-sharing variant uses only the affirming labels and plain descriptions, with no internal construct tags or scores shown unless we choose to invite rating.

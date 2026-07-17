# Persona Profiler: Frameworks, Standards, and Schema Reference

> **Naming disambiguation:** "Persona" here means the **Trait Profiler** — a model of a real person's own personality, values, and traits, used for cofounder/collaborator matching and for tracking how social interactions with different persona types affect a Yar user's mood and cognition. This is a distinct concept from the **Voice Persona** (`spec/SPEC-personas-voice.md`), which is Yar's app companion's switchable character and TTS voice. Do not conflate the two.

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: engineers, stakeholders
> **Tags**: `yar`, `research`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)

**Prepared for:** Shahin Mohammadi, Cytognosis Foundation
**Date:** 30 May 2026
**Purpose:** A vetted reference for the scientifically defensible frameworks, instruments, ontologies, and matching methods that can underpin a persona profiler serving two use cases: (1) matching cofounders, partners, and collaborators on expertise, values, goals, and personality; and (2) the Yar / Cytonome application that tracks how social interactions with different persona types affect a user's mood and cognition.

---

## 0. How to read this document

This reference is opinionated. For every facet of "persona" it separates what is empirically robust enough to build on from what is popular but weakly supported, and it states a recommended primary instrument with free or proprietary status. It is organized in seven layers:

1. Design principles (Section 1).
2. The recommended construct stack: personality, dark-side traits, values, motivation and goals, vocational interests and work values, character strengths, and affect and wellbeing (Section 2).
3. A validity-tier table that also places the popular or commercial models (MBTI, DISC, Enneagram, CliftonStrengths) with verdicts (Section 3).
4. The two use cases, with the matching science and the Yar tracking design (Section 4).
5. The formal ontology and data-standards layer for FAIR encoding (Section 5).
6. Measurement best practices (Section 6).
7. Ethics and legal constraints, then a recommended tiered instrument battery, a schema overview, and a candid list of what the evidence does not support (Sections 7 to 10).

The companion file `persona_profiler_schema.yaml` is a LinkML schema that implements the construct stack, the provenance model, the ontology crosswalks, and the matching and Yar constructs described here.

A single thesis runs through the whole document: **measure dimensions, not types; record provenance for every score; match values and goals on similarity, skills and roles on complementarity, and personality mostly on neither; and treat clinical, dark-side, and third-party inferences as high-risk data that require consent and never act as a sole gate.**

---

## 1. Design principles

**Separate the construct layer from the encoding layer.** What you measure (a HEXACO Honesty-Humility score) is a different decision from how you represent it for interoperability (a slot annotated with a BFO disposition class, a PhenX protocol ID, and a normative reference). Keeping these layers distinct lets you swap instruments without breaking the data model, and lets you map to LOINC, OMOP, or ontology IRIs without contaminating the psychological model. The schema enforces this split.

**Prefer dimensions to types.** Every robust model in this space is dimensional (continuous scores on traits), and every weak one is typological (sorting people into discrete boxes). Types feel intuitive and communicate well, but they discard information, are unstable near the mean, and inflate classification error. You can always present a dimensional profile in friendly language; you cannot recover the lost precision of a type after the fact.

**Record provenance with every score.** A trait score is meaningless without its instrument, version, administration mode, respondent (self, informant, or inferred), normative reference, score metric (raw, T-score, or percentile), and date. Two "Conscientiousness 70" values from different instruments and norm groups are not comparable. The schema attaches a provenance record to every measurement.

**Design for consent and minimization from the start.** Both use cases process sensitive psychological data, and Yar additionally processes data about third parties (the people a user interacts with). The legally and ethically safe posture is explicit consent, purpose limitation, data minimization, and dimensional self-knowledge framing rather than third-party diagnosis. This is not a compliance afterthought; it shapes what the schema is allowed to store (Section 7).

**The two use cases share one construct core.** Personality, values, motivation, and affect are the same constructs whether you are matching two founders or tracking how a meeting moved someone's mood. The difference is granularity and cadence: matching uses stable trait estimates collected once; Yar uses repeated state measurements collected around events via ecological momentary assessment. The schema models both off a shared trait vocabulary.

---

## 2. The recommended construct stack

Each subsection gives the recommendation and rationale in prose, then a specification table. Validity tiers used throughout: **Tier A** = strong structural, cross-cultural, and predictive validity, suitable as a primary measure; **Tier B** = useful with caveats or for specific purposes; **Tier C** = not recommended as a quantitative measure. Sources are consolidated in Section 11.

### 2.1 Personality structure

Lead with **HEXACO** as the primary personality model and keep the **Big Five / Five-Factor Model** as the interoperable common language. The two converge on five shared dimensions, but HEXACO adds a sixth factor, Honesty-Humility (H), that the Big Five buries inside Agreeableness. For a cofounder profiler, H is the single most decision-relevant personality dimension because it predicts integrity, fair dealing, and resistance to exploitation, and because low H is very nearly the common core of the Dark Triad (a meta-analytic latent correlation near -.95). HEXACO Emotionality also redistributes anger out of the neuroticism space, which sharpens its interpersonal interpretation.

Big Five remains essential because it is the lingua franca: nearly all crosswalks, norms, and downstream literature are expressed in Big Five terms, and public-domain item pools (IPIP) let you score it for free. Measure at the facet level, not just the domain level, because applied prediction lives in the facets (for example HEXACO Diligence and Prudence for execution reliability, or Big Five Orderliness versus Enthusiasm for operating-role fit). The Interpersonal Circumplex adds a compact, behavior-predictive map of interaction style (Agency and Communion) that is especially useful for Yar, since it predicts the dyadic "pull" one person exerts on another.

The lexical foundation of these models is robust in Western and several East Asian languages but thins out in non-WEIRD and small-scale societies (a Bolivian Tsimane sample recovered only two factors, not five). Treat profiles as probabilistic estimates with stability that rises with age: rank-order stability is about .54 in the college years, about .64 by age 30, and plateaus near .74 between ages 50 and 70. Profiles for users under 25 deserve wider uncertainty bands.

| Construct | Instrument | Items | Facets | Status | Tier |
|---|---|---|---|---|---|
| HEXACO (6 factors) | HEXACO-PI-R | 200 | 24 + Altruism | Free for research (hexaco.org) | A |
| HEXACO (domains) | HEXACO-60 | 60 | domains only | Free for research | A |
| Big Five (FFM) | IPIP-NEO-120 / 300 | 120 / 300 | 30 | Public domain (ipip.ori.org) | A |
| Big Five | BFI-2 (+ S, XS short forms) | 60 / 30 / 15 | 15 | Free for research | A |
| Big Five aspects | BFAS | 100 | 10 aspects | Free | A |
| Big Five (FFM) | NEO-PI-3 | 240 | 30 | Proprietary (PAR) | A |
| Interaction style | IPIP-IPC (Interpersonal Circumplex) | 32 | 8 octants | Public domain | A/B |

### 2.2 Maladaptive and dark-side traits

This is the highest-value and highest-risk part of the stack. Use it only under explicit consent, in subclinical and self-report framing, and never as a sole gate for a partnership or hire (the legal and ethical reasoning is in Section 7). With those guardrails, the dark-side layer is where cofounder integrity risk actually lives.

The most useful single construct is the **Dark Factor of Personality (D)**, the general tendency to maximize one's own utility while disregarding, accepting, or provoking harm to others, with accompanying justifying beliefs. D is the common core of narcissism, Machiavellianism, psychopathy, sadism, spitefulness, greed, and entitlement, and it predicts deception, exploitation, and rule-breaking with strong reliability. The free D16 (sixteen items) is the practical screen; D35 or D70 add precision.

Underneath D, the clinical-dimensional systems have converged impressively, which is reassuring for a data model: the **DSM-5 Alternative Model for Personality Disorders (AMPD), measured by the free PID-5**, the **ICD-11 dimensional model**, and the **HiTOP** maladaptive-trait layer all describe the same low-order space. Four domains recur in all of them: Negative Affectivity, Detachment, Antagonism (called Dissociality in ICD-11), and Disinhibition. AMPD adds Psychoticism; ICD-11 adds Anankastia (rigid perfectionism) instead. For cofounder vetting, the Antagonism / Dissociality domain (callousness, deceitfulness, grandiosity, manipulativeness) is the primary signal, and it maps cleanly onto low HEXACO Honesty-Humility and high D. The Dark Triad and Dark Tetrad short scales (SD3, SD4, Dirty Dozen) are widely used but have weak subscale reliability and are easy to fake; prefer D plus the relevant PID-5 facets.

| Construct | Instrument | Items | Structure | Status | Tier |
|---|---|---|---|---|---|
| Dark Factor (D) | D16 / D35 / D70 | 16 / 35 / 70 | one general factor | Free, 35+ languages (darkfactor.org) | A (for the D construct) |
| Maladaptive traits | PID-5 / PID-5-SF / PID-5-BF | 220 / 100 / 25 | 5 domains, 25 facets | Free (APA) | A |
| Dimensional PD (global) | ICD-11 model (PDS-ICD-11, SASPD) | varies | severity + 5 qualifiers | Free / mixed | A (framework) |
| Psychopathology spectra | HiTOP-SR / B-HiTOP | varies / 45 | 6 spectra hierarchy | Free, CC BY-NC-ND | A/B |
| Dark Triad | SD3 / Dirty Dozen | 27 / 12 | 3 traits | Free | B (weak subscales) |
| Dark Tetrad | SD4 / CAST-12 | 28 / 12 | 4 traits incl. sadism | Free (items reproducible) | B |
| Leadership derailers | Hogan Development Survey | 154 | 11 derailers | Proprietary | B |

### 2.3 Values

Use the **Schwartz Theory of Basic Human Values** as the primary values model. It is the most cross-culturally validated values framework in existence, replicated across 49 cultural groups in 32 languages, and its circular (circumplex) structure is a gift for matching: you can express value compatibility as angular distance on the circle rather than as a pile of separate scores. Use the refined 19-value theory and its PVQ-RR instrument when you want resolution; use the 21-item ESS Human Values Scale (the version embedded in the European Social Survey) when you need brevity. The two higher-order axes (openness-to-change versus conservation, self-enhancement versus self-transcendence) are usually enough to characterize the conflicts that break partnerships: risk appetite, mission orientation, and whether power or universalism dominates.

Add **Moral Foundations Theory** as a supplement for the specific question of moral and political conflict. The 2023 MFQ-2 is psychometrically much improved over the original and splits fairness into Equality and Proportionality, which is exactly the fault line that divides cofounders on equity, credit, and culture decisions. Treat the older Rokeach Value Survey and the population-level World Values Survey dimensions as context only; Schwartz supersedes Rokeach, and the WVS dimensions are ecological, not individual.

| Construct | Instrument | Items | Structure | Status | Tier |
|---|---|---|---|---|---|
| Basic human values | PVQ-RR (refined) | 57 | 19 values, 4 higher-order, 2 axes | Free (Schwartz repository) | A |
| Basic human values | PVQ-21 / ESS HVS | 21 | 10 values | Free | A |
| Basic human values | SVS (Schwartz Value Survey) | 57 | 10 values | Free | A |
| Moral foundations | MFQ-2 | 36 | 6 foundations | Free (moralfoundations.org) | A |
| Values (legacy) | Rokeach Value Survey | 36 | terminal / instrumental | Public domain | C (superseded) |

### 2.4 Motivation and goals

Anchor on **Self-Determination Theory (SDT)**, the most empirically supported macro-theory of motivation. Three pieces matter for the profiler. First, the **Basic Psychological Needs** (autonomy, competence, relatedness) and specifically the satisfaction-and-frustration measure (BPNSFS): need frustration, not mere lack of satisfaction, is the proximal driver of ill-being, which makes the BPNSFS the single best instrument for Yar's event-level tracking (it can be adapted to ask, after an interaction, whether that interaction satisfied or frustrated each need). Second, the **Aspirations Index**, which separates intrinsic life goals (growth, relationships, community) from extrinsic ones (wealth, fame, image); a cofounder whose goal structure is extrinsic-dominant will clash with one whose structure is intrinsic-dominant regardless of personality fit. Third, the autonomous-versus-controlled motivation continuum, which predicts how someone responds to structure and feedback.

Supplement with **Achievement Goal Theory** (mastery versus performance, crossed with approach versus avoidance) for how people frame challenge and setbacks, and with **Regulatory Focus** (promotion versus prevention) for risk and decision tempo, noting that self-report regulatory-focus measures are noisy and should be treated as approximate. For deep work on founder drive, McClelland's distinction between implicit motives (measured by narrative coding, predicting long-run spontaneous behavior) and self-attributed motives (measured by questionnaire, predicting responses to structured situations) is worth knowing, though implicit-motive coding is too labor-intensive to scale in an app.

| Construct | Instrument | Items | Structure | Status | Tier |
|---|---|---|---|---|---|
| Basic psychological needs | BPNSFS | 24 | 3 needs x satisfaction/frustration | Free for research (SDT center) | A |
| Life goals / aspirations | Aspirations Index | 35 goals | intrinsic vs extrinsic, 7 categories | Free | A |
| Causality orientations | GCOS | 17 | autonomy / control / impersonal | Free | A/B |
| Achievement goals | AGQ / AGQ-3x2 | 12 / 18 | 2x2 or 3x2 | Free in literature | A/B |
| Regulatory focus | RFQ | 11 | promotion / prevention | Free in literature | B (noisy) |
| Implicit motives | PSE / Picture Story Exercise | varies | nAch, nAff, nPow | Coding manual; labor-intensive | B (not scalable) |
| Personal goals (idiographic) | Personal Strivings | free response | conflict / facilitation | Free method | B |

### 2.5 Vocational interests and work values

For the "complementary expertise" half of cofounder matching, two free U.S. Department of Labor instruments are the right tools. The **O*NET Interest Profiler** scores Holland's **RIASEC** types (Realistic, Investigative, Artistic, Social, Enterprising, Conventional), which is the classic way to see that an Investigative-dominant technical founder and an Enterprising-dominant business founder are complementary rather than redundant. The **O*NET Work Importance** instruments score six **work values** (Achievement, Independence, Recognition, Relationships, Support, Working Conditions) derived from the Theory of Work Adjustment and the Minnesota Importance Questionnaire; these predict where partners will disagree about autonomy, accountability, and culture. Both are public domain and map directly onto O*NET occupational data, which is a bonus for expertise matching.

| Construct | Instrument | Items | Structure | Status | Tier |
|---|---|---|---|---|---|
| Vocational interests | O*NET Interest Profiler | 60 (Mini 30) | RIASEC (6) | Public domain | A |
| Work values | O*NET Work Importance Profiler / Locator | varies | 6 work values | Public domain | A |
| Work needs (fine) | Minnesota Importance Questionnaire | 20 needs | TWA needs | Free for research | A/B |
| Work values | Super's Work Values Inventory-R | 72 | 12 values | Proprietary | B |

### 2.6 Character strengths

Use the **VIA Classification of Character Strengths** (6 virtues, 24 strengths) and its free VIA-120 survey. It is the positive-psychology counterpart to a clinical taxonomy, it is free for research, and "signature strength" use is a tractable daily predictor of engagement and positive affect, which is useful for Yar. Note honestly that the theorized six-virtue structure has never been confirmed by factor analysis (studies recover three to five factors), so treat the 24 strengths as the real unit and the virtues as organizing labels. **CliftonStrengths** (34 themes) is widely used in corporate settings and has informal pairing heuristics, but it is proprietary, ipsative, and validated mostly in-house, so prefer VIA for a research-grade profiler.

| Construct | Instrument | Items | Structure | Status | Tier |
|---|---|---|---|---|---|
| Character strengths | VIA-IS / VIA-120 | 240 / 120 | 24 strengths, 6 virtues | Free (viacharacter.org) | A (strengths), B (virtue structure) |
| Talents / themes | CliftonStrengths | ~177 pairs | 34 themes, 4 domains | Proprietary (Gallup) | B |

### 2.7 Affect and wellbeing (the Yar layer)

Yar needs a coordinate system for momentary feeling, a validated state instrument, and baseline wellbeing anchors. The coordinate system is **Russell's circumplex of core affect**: valence (pleasant to unpleasant) crossed with arousal (activated to deactivated). Two short prompts ("how pleasant do you feel right now" and "how activated do you feel") locate any moment in that space, and the four quadrants give you testable hypotheses (an antagonistic counterpart should push a user toward low-valence / high-arousal stress or low-valence / low-arousal withdrawal). The validated state instrument is the **state PANAS** (10 items, or the 5-item international short form), which scores Positive and Negative Affect as near-independent dimensions. For interoperability, the **PROMIS** emotional-distress and positive-affect item banks are the best choice because they are free, IRT-calibrated, and already LOINC-coded, so they drop straight into a FHIR or OMOP pipeline (and into your existing cytos.sensor work).

For baselines and outcomes, use the **Satisfaction With Life Scale (SWLS)** for the cognitive-evaluative component of wellbeing (monthly or quarterly, not for event sampling, since it is mood-reactive) and the **PERMA-Profiler** for multidimensional flourishing. The crucial methodological point is that Yar should use **Ecological Momentary Assessment (EMA), specifically event-contingent sampling** (a short prompt after an interaction), analyzed with multilevel models so you can separate within-person interaction effects from between-person traits. Pair the affect prompt with a one-item-per-need BPNSFS adaptation to capture the mechanism, not just the mood.

| Construct | Instrument | Items | Use | Status | Tier |
|---|---|---|---|---|---|
| Core affect | Russell circumplex (valence x arousal); SAM | 2 to 3 | EMA momentary affect | Free | A |
| State affect | State PANAS / I-PANAS-SF | 10 / 5 | EMA momentary affect | Free for research | A |
| Emotional distress + positive affect | PROMIS short forms / CAT | 4 to 8 | interoperable, LOINC-coded | Free (NIH) | A |
| Life satisfaction | SWLS | 5 | trait baseline | Free | A |
| Flourishing | PERMA-Profiler | 23 | wellbeing outcome | Free | A/B |
| Need satisfaction / frustration | BPNSFS (event-adapted) | 6 to 24 | interaction mechanism | Free for research | A |

---

## 3. Validity tiers and the popular models

The construct stack above is deliberately built from Tier A and selected Tier B instruments. The table below consolidates the verdicts and, importantly, places the popular or commercial models that your users will have heard of, with the evidence and a Big Five crosswalk so you can absorb their signal without adopting their measurement.

| Model | Verdict | Why | If you must use it |
|---|---|---|---|
| Big Five / FFM | Tier A | Strong structure, heritability near .40, broad predictive validity, free items | Use as the common language |
| HEXACO | Tier A | Adds Honesty-Humility; best for integrity and trust | Use as the primary model |
| Schwartz values | Tier A | Best cross-cultural validity; circumplex enables distance metrics | Use as the primary values model |
| SDT (needs, aspirations) | Tier A | Most supported motivation theory; frustration predicts ill-being | Use for motivation and Yar mechanism |
| RIASEC / O*NET | Tier A | Hexagon replicates across cultures; free; ties to occupations | Use for interest complementarity |
| VIA strengths | Tier A (strengths) | Free; strengths-use predicts engagement | Use the 24 strengths, not the 6 virtues |
| Dark Factor D | Tier A (construct) | Unifying core of aversive traits; predicts harm | Use D16 as a consent-gated screen |
| PID-5 / ICD-11 / HiTOP | Tier A (frameworks) | Convergent dimensional psychopathology | Subclinical framing only |
| MBTI | Tier C for measurement | 39 to 76 percent get a different type on retest; dichotomizes continua; no Neuroticism; no incremental validity | Discussion anchor only; never score-based decisions |
| DISC | Tier C for measurement | Ipsative artifacts; no single validated instrument; omits Openness, Neuroticism, Honesty-Humility | Team-role vocabulary only |
| Enneagram | Tier C for measurement | Factor analyses do not recover nine types; secondary constructs unsupported | Self-reflection scaffold only |
| True Colors | Tier C | No peer-reviewed validation; an MBTI derivative | Avoid for prediction |
| CliftonStrengths | Tier B | Proprietary, ipsative, mostly in-house validation | Prefer VIA for research use |

**Crosswalks (so you do not lose the popular-model signal).** MBTI Extraversion-Introversion maps to Big Five Extraversion (r about -.7), Sensing-Intuition to Openness (r about .72), Thinking-Feeling to Agreeableness (r about .2 to .44), Judging-Perceiving to Conscientiousness (r about -.49), and MBTI has no Neuroticism counterpart at all. DISC Dominance maps to high Extraversion plus low Agreeableness, Influence to Extraversion plus Openness, Steadiness to Agreeableness plus low Neuroticism, Conscientiousness to Big Five Conscientiousness. Enneagram types correlate descriptively with Big Five (Type 1 with high Conscientiousness and low Agreeableness, Type 4 with high Openness and Neuroticism, and so on) but these correlations are post hoc, not derived from the instrument. The practical implication: if a user arrives with an MBTI or Enneagram result, you can translate it into approximate Big Five priors, but you should collect a real dimensional measure for anything consequential.

---

## 4. The two use cases

### 4.1 Cofounder and partner matching

The hardest and most important finding to internalize is that **dyadic compatibility is only weakly predictable from pre-meeting self-report**, and an honest profiler should be built around that humility rather than against it. Two landmark machine-learning studies make the point: Joel and colleagues (2017) found that self-report data predicts a person's general tendency to desire others and to be desired, but predicts essentially none of the relationship-specific variance (which two particular people will click); and Joel and colleagues (2020), pooling 43 longitudinal datasets, found that relationship-specific perceptions (commitment, appreciation, conflict) predict relationship quality far better than either partner's personality, and that personality could not predict whose relationship would improve or decline. Build the matcher as decision support that narrows and explains, not as an oracle that scores couples.

Within that constraint, the evidence supports a clear tripartite rule, and it is the backbone of the matching logic in the schema:

**Match values and goals on similarity (congruence).** Value congruence is the most robust predictor of person-organization satisfaction, team cohesion, and relationship stability, and social attitudes show the strongest partner assortment of any trait class. This is where Schwartz angular distance and Aspirations Index intrinsic-versus-extrinsic alignment do real work. Wasserman's survey of roughly 10,000 founders found that conflict over money, roles, and strategy, rooted in misaligned values and commitment, is a leading cause of failure in high-potential startups.

**Match skills, roles, and interests on complementarity.** Functional and expertise diversity is additive for startups; complementary RIASEC profiles and complementary domain skills are the well-supported "complementary skills, similar values" heuristic. This is the half of matching where difference is an asset.

**Treat personality as mostly similarity-neutral, with three specific exceptions.** Actual personality assortment in real couples is weak (partner correlations of .08 to .21 across the Big Five), and broad-trait complementarity ("opposites attract") has essentially no empirical support. The exceptions that do matter are: (a) higher mean-level Conscientiousness and Agreeableness help teams; (b) a single member very low on Agreeableness, Emotional Stability, or Conscientiousness disproportionately drags a team down (the "bad apple" effect, asymmetric and large); and (c) integrity screening via high HEXACO Honesty-Humility and low Dark Factor D is protective. So for personality, the profiler should check for a bad-apple risk and an integrity risk rather than chase trait similarity or complementarity.

A defensible matching pipeline therefore computes, per construct family, a similarity score (values, goals), a complementarity score (interests, skills), and risk flags (low H or high D integrity flag; bad-apple flag), then combines them with transparent, user-adjustable weights and presents the result with explicit uncertainty and the reasons behind it. The schema's `DimensionMatchingPolicy` and `DyadMatch` classes encode exactly this.

### 4.2 Yar / Cytonome interaction tracking

Yar's goal is to learn how interacting with different persona types affects a user's mood and cognition. The correct paradigm is **event-contingent Ecological Momentary Assessment**: a short prompt after (or about) an interaction that captures the user's current core affect (valence and arousal), a one-item-per-need read on whether the interaction satisfied or frustrated autonomy, competence, and relatedness, and optionally a brief cognitive check (focus, rumination, energy). Over many events, multilevel or dynamic models separate the stable between-person baseline from the within-person effect of interacting with a given counterpart type, yielding statements like "interactions with high-dominance, low-warmth counterparts reliably move this user into low-valence / high-arousal states and frustrate autonomy."

Two design rules are non-negotiable. First, **the counterpart's "persona type" must be framed as the user's experience, not a diagnosis of a third party.** Yar can characterize how the user perceives and is affected by an interaction; it must not assert that a named, non-consenting third person "is a narcissist." The same data supports the safe framing (how this interaction affected me) and forbids the unsafe one (what that person is). Second, **dark-side or clinical labels applied to third parties from behavioral traces are off-limits** because error rates are high, the models are not validated for that purpose, and the harm from mislabeling is severe. The schema models the counterpart as a pseudonymous entity with a consent flag and stores effects on the user, not traits of the other person.

The instruments are the affect layer from Section 2.7: Russell valence and arousal as the coordinate system, state PANAS as the validated read, BPNSFS event items for mechanism, and PROMIS short forms (LOINC-coded) when you want clinical-grade, interoperable distress measurement and safety monitoring. SWLS and PERMA provide the slow baselines against which event effects are interpreted.

---

## 5. Formal ontologies and data standards (the FAIR layer)

The candid headline: **standardization in this domain is mature for affect and clinical measurement, and immature for personality, values, and goals.** Plan accordingly. The recommended architecture is to use established codes wherever they exist, use upper-ontology classes for construct semantics, invent local terms only where nothing exists, and declare every cross-reference as an explicit mapping (SSSOM-style) in a LinkML schema.

**Use established codes where they exist.** Affect and distress instruments are well covered by **LOINC**: PHQ-9 (panel 44249-1), GAD-7 (69737-5), and the PROMIS family (for example Emotional Distress Anxiety item bank 61922-1, Depression short form 4a 76343-3, pediatric Positive Affect 91355-8) all have panel, item, and answer-list codes, and surface as FHIR Questionnaire resources. Store survey results in the **OMOP CDM** using SURVEY_CONDUCT for the administration event and OBSERVATION for item responses and computed scores, with `observation_type` patient self-report. This is the same plumbing your cytos.sensor schema already uses, so the Yar affect stream is interoperable by construction.

**Use upper-ontology classes for construct semantics.** The cleanest available framework is the **Mental Functioning Ontology (MF)** and its **Emotion Ontology (MFOEM)**, both BFO-grounded and OBO-registered. The ontologically correct move, and one that matters for your work specifically, is to model personality traits as **BFO dispositions** (`BFO_0000016`), not qualities: an introvert has a standing disposition to behave a certain way under social circumstances even when not currently expressing it, which is exactly the disposition pattern, whereas a current mood state is better modeled as a quality or a process. MFOEM already models valence, arousal, mood, and appraisal, so the Yar affect constructs have real homes.

**Accept that personality, values, and goals lack named terms, and bridge with mappings.** There is no actively maintained, registered ontology that enumerates the Big Five or HEXACO traits as classes; MF gives you the parent framework but not "extraversion" as a term. LOINC has no codes for the BFI, NEO, IPIP, or PID-5. Values and goals have only research-prototype ontologies (ValueNet for Schwartz and Moral Foundations; iStar and GORO for goals), none registered with stable PURLs. The practical bridges that do exist are: the **PhenX Toolkit protocol 121101**, which designates the 44-item BFI as the standard personality measure for genomic and large-cohort research (use it as an `exact_mapping` for Big Five items); the **NIMH Data Archive** category structure, which has explicit Personality, Temperament, Emotions, Goals, Mood, and Self-Concept categories; **Wikidata** items such as Q378132 for the Big Five model (resolvable URIs usable as `close_mappings`); and the lone curiosity that **FOAF** even has a `foaf:myersBriggs` property (evidence of how thin Web-vocabulary coverage is). The **RDoC** matrix is not a set of stable IRIs but is the best theoretical crosswalk from your trait constructs to neurobehavioral systems (Negative Valence to Neuroticism, Positive Valence and Social Processes to Extraversion and Agreeableness, Cognitive Systems to Conscientiousness and Openness).

The crosswalk table below is the recommended set of anchors to attach to schema slots. Where a precise code is absent, attach the closest construct-level class as a broad mapping and the relevant Wikidata or PhenX identifier as a close mapping, and label the local term clearly.

| Construct family | Primary code/IRI to attach | Mapping strength | Storage |
|---|---|---|---|
| Affect / distress instruments | LOINC (PROMIS, PHQ-9, GAD-7 codes) | exact | OMOP SURVEY_CONDUCT + OBSERVATION |
| Emotion / mood constructs | MFOEM classes (valence, arousal, mood) | close | OMOP / FHIR |
| Personality trait (generic) | BFO_0000016 disposition; MF framework | broad | LinkML slot annotation |
| Big Five items | PhenX 121101 (BFI-44); Wikidata Q378132 | exact / close | local term + mapping |
| Personality / disorder findings | SNOMED CT (e.g., 225760008 personality finding) | close (clinical only) | OMOP |
| Values (Schwartz, MFT) | ValueNet OWL classes; cite Schwartz 2012 | close (prototype) | local term + mapping |
| Goals | iStar / GORO goal classes | close (prototype) | local term + mapping |
| Research data structures | NDA categories (Personality, Mood, Goals) | organizational | NDA submission |
| Identity / social graph | schema.org/Person, FOAF | alignment | LinkML slot annotation |

Net recommendation: build the persona model in **LinkML** under a Cytognosis namespace, register the prefix in Bioregistry for resolvability, carry `exact_mappings`, `close_mappings`, and `broad_mappings` on every construct slot, and keep instrument administration metadata separate from construct semantics. The companion schema does this.

---

## 6. Measurement best practices

**Prefer public-domain instruments** so you can inspect, translate, and embed items without licensing friction: IPIP for Big Five and many facet scales, HEXACO-PI-R (free for research), BFI-2, BFAS, the Schwartz instruments, O*NET tools, VIA-120, PID-5, D16, PANAS, SWLS, PERMA-Profiler, and PROMIS are all free. The main proprietary holdouts (NEO-PI-3, CliftonStrengths, Hogan Development Survey, Super's WVI-R) have free or near-equivalent substitutes already in the stack.

**Report reliability with omega, not just alpha.** Cronbach's alpha understates or misstates reliability for the multidimensional, non-tau-equivalent facet scales that dominate this field; McDonald's omega (total and hierarchical) is the modern standard. Also report test-retest stability over months, since a profiler implicitly assumes temporal stability.

**Establish measurement invariance before you compare or match people.** This is the most under-appreciated requirement and it is essential for fairness. Before scores from two people (or two groups) can be compared, the instrument must show at least metric and ideally scalar invariance across the relevant groups (gender, age, language, culture), tested by multi-group confirmatory factor analysis. Without scalar invariance, an apparent difference between two candidates may be a measurement artifact, not a real difference, and a matcher that ignores this will systematically misjudge cross-cultural pairs. Use normative T-scores or percentiles tied to a specified reference sample, and only from invariant scales.

**Plan for faking and social desirability**, which are acute in high-stakes vetting precisely because the people most worth screening (high D) are the most motivated to misrepresent themselves. Mitigations, in rough order of practicality: forced-choice or Thurstonian-IRT formats (more faking-resistant, though they complicate scoring), informant or peer reports (less self-presentational bias, often equal or better validity), verifiable biodata, and explicit faking warnings. Correcting scores with a social-desirability scale is psychometrically dubious; prefer design-level mitigations.

**Treat digital-trace inference as a weak signal.** Models that infer Big Five from social media (the Kosinski and Youyou line) achieve moderate accuracy for Openness and less for other traits, with high individual error and demographic confounds. They are not a substitute for validated self-report or informant data, and using them to infer dark-side or clinical traits about third parties is both inaccurate and ethically fraught (Section 7).

---

## 7. Ethics and legal constraints

This section is short, blunt, and load-bearing. The profiler touches three regulated areas: selection and hiring law, data-protection law, and research ethics. Getting this wrong is not a style issue; it creates liability and harm.

**Selection and hiring (if the profiler ever informs who gets hired, funded, or partnered with).** Under U.S. law (Title VII, the Uniform Guidelines, and Griggs v. Duke Power), any selection procedure with disparate impact on a protected group must be job-related and justified by business necessity; personality tests are explicitly covered, and the EEOC has extracted multi-million-dollar settlements (Target, CVS, Best Buy) over personality assessments with disparate impact. The SIOP Principles require documented criterion, content, or construct validity for the specific use. A critical line under the ADA: a test that screens for mental impairments or disorders is a "medical examination," subject to strict pre-offer prohibitions and confidentiality rules. Clinical and dark-side instruments (PID-5, anything diagnostic) can cross that line; Soroka v. Dayton Hudson established that even ordinary personality items can violate privacy when they probe protected or sensitive attributes without job-relatedness. Practical posture: for any consequential selection use, restrict to validated, job-relevant constructs (Conscientiousness, relevant facets, value congruence), keep clinical and dark-side measures out of the gating logic, and document validity and adverse-impact analyses.

**Data protection (GDPR and UK GDPR).** Inferred personality, values, and affect are personal data; where they reveal or effectively diagnose mental-health characteristics they become Article 9 special-category data requiring explicit consent or another narrow basis, and inferring a special-category characteristic from ordinary data still engages Article 9. A profiler is "profiling" under Article 4(4), and matching or excluding someone by largely automated means can trigger Article 22 protections (right to human intervention, to contest, to an explanation). A Data Protection Impact Assessment is effectively mandatory for psychological profiling at this sensitivity. Build in lawful basis, purpose limitation, minimization, and user rights from the start.

**The Yar third-party problem and the Cambridge Analytica lesson.** Yar analyzes interactions that necessarily involve other people who have not consented and whose data you are processing. Cambridge Analytica is the cautionary archetype: data harvested via a quiz, extended to non-consenting contacts across a social graph, repurposed for profiling, with no transparency. Avoid every element of that pattern. Concretely: collect and store only what the focal, consenting user provides; model counterparts pseudonymously; store effects on the user rather than inferred traits of the counterpart; never label a non-consenting third party with a dark-side or clinical construct; give users visibility, correction, and deletion over the inferences made about them; and frame all output as self-knowledge.

**Guardrails checklist (encoded as constraints in the schema where possible):** explicit, specific, informed consent per assessment and per purpose; no single score as a sole disqualifier; dimensional scores with uncertainty rather than type labels; clinical and dark-side measures consent-gated, subclinical-framed, and excluded from automated gating; measurement invariance verified before cross-group comparison; a DPIA before deployment; and an ethics or IRB review for any research use or any deployment that affects people's opportunities.

---

## 8. Recommended instrument battery

Three tiers, depending on how much respondent time you can spend and whether you need clinical or research-grade rigor. All listed instruments are free unless noted.

**Minimal viable battery (about 15 to 20 minutes), for broad matching.** HEXACO-60 (personality, including Honesty-Humility); PVQ-21 / ESS Human Values (values); a short Aspirations Index plus the autonomy items of the BPNSFS (goals and motivation); O*NET Mini Interest Profiler (RIASEC, for complementarity); and, consent-gated, the D16 (integrity screen). For Yar, the 2-item Russell valence/arousal prompt plus 3 BPNSFS need items per event.

**Standard battery (about 45 to 60 minutes), for serious cofounder profiling.** HEXACO-PI-R (full facets) plus IPIP-NEO-120 for Big Five interoperability; PVQ-RR (19 values); full Aspirations Index, BPNSFS, and an achievement-goal measure; O*NET Interest Profiler plus Work Importance Profiler; VIA-120 strengths; and, consent-gated and subclinical-framed, D35 plus PID-5-BF. Add the IPIP-IPC for interaction style.

**Research-grade additions.** PID-5 full or PID-5-SF and B-HiTOP for dimensional psychopathology (under appropriate ethics oversight); MFQ-2 for moral-conflict mapping; PROMIS CAT for clinical-grade, LOINC-coded affect; SWLS and PERMA-Profiler baselines; informant-report versions of the personality measures to counter faking; and forced-choice formats where stakes are high.

---

## 9. Schema overview

The companion file `persona_profiler_schema.yaml` is a LinkML schema implementing this reference. Its structure:

- A shared **trait vocabulary** via enums (HEXACO and Big Five facets, PID-5 domains and facets, Schwartz 19 values, MFT foundations, SDT needs, RIASEC types, O*NET work values, VIA strengths) so matching and Yar draw on the same constructs.
- A **MeasurementProvenance / Assessment** class attached to every score, carrying instrument, version, LOINC code where available, administration mode, respondent type, normative reference, omega reliability, score metric, confidence, and a consent reference.
- A **PersonaProfile** aggregating PersonalityProfile, DarkSideProfile (flagged high-sensitivity and consent-gated), ValueProfile, MotivationProfile, VocationalProfile, StrengthsProfile, AffectBaseline, and WellbeingProfile.
- **Matching constructs**: a `DimensionMatchingPolicy` that encodes the similarity-versus-complementarity rule and weights per construct family, and a `DyadMatch` that records computed similarity, complementarity, risk flags (integrity, bad-apple), an overall compatibility estimate, and an explicit uncertainty and rationale.
- **Yar constructs**: an `AffectState` (valence, arousal, PANAS, timestamp, context) for EMA; a `SocialInteractionEvent` linking a user to a pseudonymous, consent-flagged counterpart with pre- and post-interaction affect and need satisfaction or frustration; and a `PersonaTypeEffect` aggregating how a counterpart persona type affects the user, framed as the user's experience.
- **FAIR annotations**: prefixes and `exact_mappings` / `close_mappings` / `broad_mappings` on construct slots (LOINC, BFO, MF, MFOEM, PATO, Wikidata, PhenX, SNOMED, schema.org) so the model is interoperable and registerable.

---

## 10. What the evidence does not support (read this before overbuilding)

A reference that only said what works would mislead you. The following are real limits, not hedges:

Dyadic compatibility is not reliably predictable from pre-meeting self-report (Joel 2017, 2020); a matcher should narrow and explain, not score couples with false confidence. Personality complementarity ("opposites attract") has essentially no empirical support at the broad-trait level; do not build matching logic around it. The Big Five is less universal than often claimed; its structure thins in non-WEIRD and small-scale societies, so cross-cultural matching needs invariance testing and humility. The six-virtue VIA structure and several proposed sub-constructs (Enneagram wings and arrows, regulatory-focus self-reports) are weakly supported; lean on the better-validated layers. Type instruments (MBTI, DISC, Enneagram, True Colors) do not measure what their popularity implies and should never drive consequential decisions. And inferring stable traits, especially dark-side or clinical ones, from digital behavior or from third parties in a social graph is inaccurate, ethically hazardous, and in several jurisdictions legally constrained.

The strongest, safest design is therefore modest in its claims and rigorous in its plumbing: dimensional measurement, provenance on every score, similarity for values and complementarity for skills, integrity and bad-apple risk flags rather than personality matching, consent and self-knowledge framing throughout, and interoperable encoding via LOINC, OMOP, BFO, and LinkML.

---

## 11. References

Selected primary and authoritative sources, grouped by section. URLs were verified during research in May 2026.

**Personality structure.** Ashton & Lee (2007, 2009) HEXACO, hexaco.org. Soto & John (2017) BFI-2, JPSP 113. DeYoung et al. (2007) BFAS, JPSP 93. Goldberg et al. (2006) IPIP, ipip.ori.org. McCrae & Costa (1989, 2010) FFM / NEO. Roberts & DelVecchio (2000) stability, Psychological Bulletin 126. Roberts et al. (2006) mean-level change, Psychological Bulletin 132. Vukasovic & Bratko (2015) heritability. Gurven et al. (2013) Tsimane, JPSP. Markey & Markey (2009) IPIP-IPC. Howard & Van Zandt (2020) H-H and Dark Triad. McCrae & Costa (1989) MBTI-to-Big-Five. Pittenger (1993) MBTI reliability. Hook et al. (2021) Enneagram review.

**Values, motivation, strengths, vocational.** Schwartz (1992); Schwartz et al. (2012) refined theory; Schwartz & Cieciuch (2022) PVQ-RR across 49 groups. Atari, Haidt, Graham et al. (2023) MFQ-2. Ryan & Deci (2017) SDT; Chen et al. (2015) BPNSFS; Kasser & Ryan (1993, 1996) Aspirations. Elliot & McGregor (2001) 2x2 achievement goals; Elliot et al. (2011) 3x2. Higgins et al. (2001) regulatory focus. McClelland et al. (1989) implicit motives. Holland (1997); Rounds et al. (2021) O*NET Interest Profiler. Dawis & Lofquist (1984) Theory of Work Adjustment; O*NET Work Importance. Peterson & Seligman (2004) VIA; Partsch et al. (2022) VIA structure.

**Clinical, dark-side, affect.** Insel et al. (2010) and NIMH (2024) RDoC. Kotov et al. (2017) and Conway et al. (2024) HiTOP. Krueger et al. (2012) and Sharp et al. (2025) AMPD / PID-5. Mulder et al. (2022) ICD-11 model. Paulhus & Williams (2002) Dark Triad; Jones & Paulhus (2014) SD3; Paulhus (2021) SD4. Moshagen, Hilbig & Zettler (2018, 2020) Dark Factor D, darkfactor.org. Russell (1980, 2003) core affect. Watson, Clark & Tellegen (1988) PANAS. Cella et al. (2010) PROMIS. Butler & Kern (2016) PERMA-Profiler. Diener et al. (1985) SWLS. Stone & Shiffman (1994) EMA.

**Ontologies and standards.** Hastings et al. (2012, 2014) Mental Functioning Ontology and Emotion Ontology, obofoundry.org. Arp & Smith, BFO 2020, ISO/IEC 21838-2:2021. De Giorgis et al. (2022) ValueNet, EKAW. LOINC (loinc.org) PROMIS, PHQ-9, GAD-7 panels. OHDSI OMOP CDM SURVEY_CONDUCT. PhenX Toolkit protocol 121101 (BFI-44). NIMH Data Archive data dictionary. Wikidata Q378132. LinkML (linkml.io).

**Matching, measurement, ethics.** Joel, Eastwick & Finkel (2017) Psychological Science; Joel et al. (2020) PNAS. Horwitz et al. (2023) assortative mating, Nature Human Behaviour. Bell (2007) and Peeters et al. (2006) team composition. Felps et al. (2006) bad apples. Kern et al. (2023) founder personalities, Scientific Reports. Kristof-Brown et al. (2005) person-environment fit. Wasserman (2012) The Founder's Dilemmas. Goldberg et al. (2006) IPIP. Flora (2020) omega. EEOC Employment Tests guidance (2007); SIOP Principles (2018). APA, Soroka v. Dayton Hudson. GDPR Articles 4, 9, 22; ICO profiling guidance; WP29 wp251rev.01. Youyou et al. (2015) and Kosinski et al. (2013) digital traces.


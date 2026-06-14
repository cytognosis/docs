> **Status**: Active
> **Date**: 2026-06-14
> **Author**: Cytognosis Foundation
> **Audience**: researchers, grant writers, communications leads
> **Tags**: `writing`, `grants`, `cytognosis-writer`, `science-communication`

# cytognosis-writer — Science Writing and Grant Skill

> **Reading time**: ~6 minutes
> **If you only read one thing**: Load this skill for grants, proposals, pitch decks, science narratives, and any external-facing content. Always read the appropriate funder reference file before drafting — never guess what a funder wants.

---

## What It Is and Why

`cytognosis-writer` covers structured, strategic writing for the Cytognosis Foundation: NIH, ARPA-H, NSF, Wellcome Leap, and FRO proposals; YC applications; pitch decks; scientific narratives; open science language; FAIR data management plans; and meeting-to-grant content extraction.

This is not a generic academic prose skill. Every output is built from established language blocks, structured by the Revelation Arc, and tailored to the specific funder or audience.

**When to load this skill**:

- Writing a grant (NIH, ARPA-H, NSF, FRO, Wellcome, DARPA, DOE)
- Writing a proposal or pitch deck narrative
- Writing about the science platform (Three Blindspots, GPS for Health, Cytoverse)
- Writing the founder story
- Extracting grant-ready content from meeting transcripts
- Writing about open science, FAIR, licensing, or data management plans

**When NOT to load this skill**:

- Visual design for the output: load `cytognosis-design-system-master` in a separate response
- File locations for grant docs: load `cytognosis-org`
- Technical documentation (ADRs, specs): load `cytognosis-doc`

This skill owns **strategic writing patterns**. The design-system master owns the **voice rules** (single source of truth; do not duplicate them here).

---

## Decision Tree

```
Writing a grant / proposal / pitch?
├─ READ references/science-platform.md (narrative foundation)
└─ READ references/grant-strategy.md (funder-specific strategy)

Writing about open science, licensing, FAIR, or DMS plans?
└─ READ references/openness-policy.md

Extracting grant content from meeting transcripts?
└─ READ references/meeting-extraction.md

Writing about WHAT Cytognosis is or HOW it works?
└─ READ references/science-platform.md
```

---

## The Revelation Arc

Every Cytognosis narrative follows: **Mystery → Insight → Resolution**.

1. **The Mystery**: the diagnostic failure, the biological unknown, the years-of-odyssey
2. **The Insight**: cellular intelligence, the GPS for Health framework
3. **The Resolution**: health autonomy, disease interception years before symptoms

---

## Strategic Terminology

| Use | Instead of |
|-----|-----------|
| intercept | prevent |
| detect and intercept | diagnose and treat |
| years before symptoms | early detection |
| people / individuals | patients (unless clinical) |

**Proper nouns** (always capitalize): Cytoverse, Cytoscope, Cytonome, Helix model, GPS for Human Health.

**Bridge line**: "Cytognosis exists so no one else waits decades for answers."

---

## Voice (Quick Recap)

Voice rules are the single source of truth in `cytognosis-design-system-master/references/voice.md` and the full v10 spec at `branding/design-system/references/02_voice_and_tone.md`. Do not duplicate them here.

Most-used rules:

- No em dashes
- No "patients" outside clinical context
- No hype words (revolutionary, cure, game-changing, breakthrough, disrupt)
- Active present tense
- Oxford comma always
- Title Case headings, sentence case for UI labels
- "Cytognosis" always capital C; product names always capital

---

## Tone by Context

| Audience | Register | Key Trait |
|----------|---------|-----------|
| Public / social | Warm, accessible | Low formality |
| Website | Clear, confident | Medium formality |
| Grants (ARPA-H) | Bold, moonshot | High formality, commercial transition |
| Grants (NIH) | Rigorous, conservative | High formality, reproducibility |
| Grants (FRO) | Infrastructure, engineering | High formality, public utility |
| Scientific papers | Precise, rigorous | Very high formality |
| Internal / technical | Direct, efficient | Low formality |

---

## Reasoning Before Writing

Before any substantive piece:

1. **Audience**: who reads this? what do they already know?
2. **Objective**: what decision should the reader make after reading?
3. **Evidence hierarchy**: what claims need citations vs. accepted knowledge?
4. **Second-order effects**: how might this be misread? what counterarguments exist?

---

## Reference Files

| Reference | When to Read |
|-----------|-------------|
| `references/science-platform.md` | Platform narrative, Three Blindspots, GPS for Health, TBX1 founder story |
| `references/grant-strategy.md` | Funder-specific strategy, language blocks, drafting workflow |
| `references/openness-policy.md` | Licensing, FAIR pillars, open AI models, open-core rule |
| `references/meeting-extraction.md` | Extraction personas, synthesis protocol, output template |

### Deep Dives (load only for specific funders)

| Directory | Contents |
|-----------|---------|
| `references/agencies/` | ARPA-H, NIH, NSF, DARPA, DOE, Wellcome, and FRO-specific guidelines |
| `references/science/` | Founder story variants, technology detail, Three Blindspots deep dive |

### Tools

| File | Purpose |
|------|---------|
| `scripts/budget_calculator.py` | Grant budget computation |
| `scripts/compliance_checker.py` | Funder compliance checks |
| `templates/` | ARPA-H solution summary template |

---

## Open Science Rules (Key Points)

Never just say "We follow FAIR." Map each principle to infrastructure:

| FAIR Principle | Cytognosis infrastructure |
|----------------|--------------------------|
| Findable | Metadata in data catalog + DOI minted at release |
| Accessible | Open access at cytognosis.org; API available |
| Interoperable | Open standards (LinkML schemas, JSON-LD, BioLink) |
| Reusable | Apache 2.0 (code), CC BY 4.0 (data), permissive licenses |

Never suggest GPL or copyleft for Cytognosis projects.

---

## Hard Rules (NEVER)

- NEVER use em dashes in any output
- NEVER use passive voice; subject does the action
- NEVER use hype words (revolutionary, cure, game-changing, breakthrough, disrupt)
- NEVER write from scratch for grants; assemble from established language blocks
- NEVER guess what a funder wants; read their specific reference file
- NEVER just say "We follow FAIR"; map each principle to infrastructure
- NEVER ask "Which sections would you like me to draft?"; draft all requested sections
- NEVER write generic meeting minutes; extract grant-ready content through a focused lens
- NEVER suggest GPL or copyleft for Cytognosis projects

---

## Related Skills

| Task | Skill |
|------|-------|
| Visual / brand / voice for the output | `cytognosis-design-system-master` |
| Deep voice spec from v10 references | `cytognosis-branding` |
| Coordinated multi-skill task | `cytognosis-orchestrator` |
| Where to put the finished file | `cytognosis-org` |
| Technical documentation | `cytognosis-doc` |

---

## Example 1: Writing an NIH Grant Section

Task: "Write the Specific Aims for an NIH R01 on cell-state mapping."

1. Load `cytognosis-writer`.
2. Read `references/science-platform.md` (Three Blindspots narrative, GPS for Health framing).
3. Read `references/agencies/nih.md` (NIH-specific strategy, conservative register, reproducibility emphasis).
4. Read `references/grant-strategy.md` (language blocks, drafting workflow).
5. Apply the Revelation Arc: open with the diagnostic gap (Mystery), present cellular intelligence as the solution (Insight), show health autonomy as the outcome (Resolution).
6. Save as `Grant-NIH-R01-Specific-Aims-v1-2026-06.md` in Drive `01-Grants-and-Funding`.

## Example 2: Extracting Grant Content from a Meeting

Task: "Extract the key scientific claims from this meeting transcript for the ARPA-H application."

1. Load `cytognosis-writer`.
2. Read `references/meeting-extraction.md` (extraction personas, synthesis protocol).
3. Apply extraction: identify technical claims, evidence statements, milestone language, and differentiators.
4. Cross-reference against `references/grant-strategy.md` language blocks for ARPA-H register.
5. Produce structured output ready to paste into the grant doc.

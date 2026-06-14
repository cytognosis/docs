> **Status**: Active
> **Date**: 2026-06-14
> **Author**: Cytognosis Foundation
> **Audience**: researchers, grant writers, communications leads
> **Tags**: `quick-reference`, `cytognosis-writer`

# cytognosis-writer — Quick Reference

> **One line**: Load this skill for grants, proposals, pitch decks, science narratives, and any external-facing Cytognosis content; always read the funder-specific reference file before drafting.
> **Full doc**: [cytognosis-writer.md](cytognosis-writer.md)

---

## Key Concepts

| Term | Definition |
|------|-----------|
| **Revelation Arc** | Cytognosis narrative structure: Mystery (diagnostic failure) → Insight (cellular intelligence) → Resolution (disease interception). Applies to all external writing. |
| **Three Blindspots** | The three gaps in current healthcare that Cytognosis addresses. Detail in `references/science-platform.md`. |
| **GPS for Human Health** | The core Cytognosis metaphor: a health navigation system that detects disease early. |
| **Bridge line** | Rhetorical anchor: "Cytognosis exists so no one else waits decades for answers." |
| **Language blocks** | Pre-approved, reusable text for grants. Never draft from scratch; assemble from blocks in `references/grant-strategy.md`. |
| **FAIR** | Findable, Accessible, Interoperable, Reusable. Never assert FAIR compliance without mapping each principle to infrastructure. |

---

## Decision Tree

| Task | Read |
|------|------|
| Writing any grant or proposal | `references/science-platform.md` + `references/grant-strategy.md` |
| Writing about open science, FAIR, or DMP | `references/openness-policy.md` |
| Extracting grant content from meeting transcript | `references/meeting-extraction.md` |
| Writing about Cytognosis science or technology | `references/science-platform.md` |
| NIH-specific writing | `references/agencies/nih.md` |
| ARPA-H-specific writing | `references/agencies/arpa-h.md` |

---

## Strategic Terminology

| Use | Instead of |
|-----|-----------|
| intercept | prevent |
| detect and intercept | diagnose and treat |
| years before symptoms | early detection |
| people / individuals | patients (except clinical context) |

---

## Tone by Audience

| Audience | Register |
|----------|---------|
| ARPA-H | Bold, moonshot, commercial transition |
| NIH | Rigorous, conservative, reproducibility-focused |
| FRO | Infrastructure, engineering, public utility |
| NSF | Scientific merit, broader impacts |
| Public / social | Warm, accessible |
| Website | Clear, confident |
| Scientific papers | Precise, rigorous |

---

## Voice Rules (Abbreviated)

| Rule | Correct |
|------|---------|
| Em dashes | Forbidden. Use commas or semicolons. |
| Voice | Active present. "We detect disease." |
| "Patients" | Only in clinical context. |
| Hype words | No "revolutionary", "cure", "breakthrough", "disrupt" |
| Intercept vs. prevent | Always "intercept" |
| Capitalization | Cytoverse, Cytoscope, Cytonome, Helix model (always capital) |

---

## Common Patterns

```
# NIH grant section workflow
1. READ references/science-platform.md
2. READ references/agencies/nih.md
3. READ references/grant-strategy.md (language blocks)
4. Apply Revelation Arc: Mystery → Insight → Resolution
5. Save as: Grant-NIH-R01-<Section>-v1-<YYYY-MM>.md in 01-Grants-and-Funding

# Meeting-to-grant extraction
1. READ references/meeting-extraction.md
2. Apply extraction personas
3. Output: structured claims, evidence statements, milestone language
4. Cross-reference against grant-strategy.md language blocks

# FAIR compliance statement
1. READ references/openness-policy.md
2. Map each FAIR principle to Cytognosis infrastructure
3. Never write "We follow FAIR" without the mapping table
```

---

## Reference Files

| File | When to Read |
|------|-------------|
| `references/science-platform.md` | Platform narrative, Three Blindspots, founder story |
| `references/grant-strategy.md` | Funder-specific strategy, language blocks |
| `references/openness-policy.md` | Licensing, FAIR, open AI models, open-core rule |
| `references/meeting-extraction.md` | Extracting grant content from transcripts |
| `references/agencies/` | Per-funder guidelines (ARPA-H, NIH, NSF, FRO, DARPA, DOE, Wellcome) |

---

## NEVER

- NEVER draft grant sections from scratch; assemble from language blocks in `grant-strategy.md`
- NEVER guess funder requirements; read their `references/agencies/<funder>.md`
- NEVER write "We follow FAIR" without a per-principle infrastructure mapping
- NEVER use em dashes, hype words, or passive voice
- NEVER suggest GPL or copyleft licensing
- NEVER ask which sections to draft; draft all requested sections

---

## Error Quick-Fix

| Error / Symptom | Fix |
|-----------------|-----|
| Grant section uses wrong register | Check tone table above; NIH = rigorous/conservative, ARPA-H = bold/moonshot |
| "Revolutionary" or "breakthrough" in draft | Replace with specific evidence: "X% improvement", "first platform to..." |
| Missing FAIR mapping | Open `references/openness-policy.md` and map each F/A/I/R to actual infrastructure |
| Writing from scratch instead of language blocks | Open `references/grant-strategy.md`; locate the relevant block; adapt |

---

## See Also

- [Full documentation](cytognosis-writer.md) — comprehensive reference + explanation
- [cytognosis-design-system-master](../cytognosis-design-system-master/cytognosis-design-system-master.md) — voice rules and visual design for output
- [cytognosis-doc](../cytognosis-doc/cytognosis-doc.md) — DMP template, grant-section template
- [cytognosis-org](../cytognosis-org/cytognosis-org.md) — where to store finished grant files

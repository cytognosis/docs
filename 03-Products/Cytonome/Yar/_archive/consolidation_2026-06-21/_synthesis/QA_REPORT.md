> **Status**: QA Report
> **Date**: 2026-06-21
> **Author**: Claude Code QA (automated)
> **Audience**: @shahin, engineering
> **Tags**: `yar`, `qa`, `feature-matrix`, `v4`

# QA Report: Yar Feature Comparison v4 (Formal Master + ADHD Variant)

**Overall verdict: FAIL**

**Feature count: 62** (F01 through F62, no duplicates, no missing IDs)

Section breakdown: AEF 15 / ERM 18 / SCI 4 / SPR 2 / CTO 16 / SMI 7.

---

## Issues (numbered by check)

### Check 1: Em dashes

**FAIL.** One em-dash character found in the ADHD variant.

- `yar-unified-feature-comparison-v4-adhd.md` line 42, inside the Mermaid node label:
  `YAR["Yar — unified ND companion<br/>spans all 6 domains"]`
  Replace the em dash with a comma or hyphen, for example: `"Yar, unified ND companion"`.

The formal master has zero em dashes. PASS for that file.

---

### Check 2: Forbidden words

**PASS.** No occurrences of "revolutionary", "breakthrough", "cure", or "game-changing" in either file.

---

### Check 3: Naming ("Substrate" and CSP/USAP)

**PASS (conditional).** "Substrate" appears exactly three times across the two files, all inside the explicit rename-flag notes where it is acceptable:

- Formal master line 267: recommendation to retire "Substrate" in code.
- Formal master line 299: decision row G1 flagging `substrate_interop.py`.
- ADHD variant line 140: "retire Substrate in code" reminder.

No other use of "Substrate" as a product or layer name was found.

CSP is presented as the canonical name throughout. USAP appears once in the formal master at line 295 in the D1 decision row, documented explicitly as "the engineering alias". That is the correct and only acceptable use.

F12 feature row header reads "Cytonome Sensor Protocol (universal sensor adapter)", which leads with CSP. PASS.

---

### Check 4: AI-Fit arithmetic

**FAIL.** 14 of 62 features have a mismatch between the AI-Fit /20 value printed in the formal master Section 4 tables and the value calculated from the CSV (AI_Leverage + Differentiation + ND_Impact + Feasibility).

| Feature ID | Doc says | CSV calc | Breakdown (L+D+N+F) |
|---|:---:|:---:|---|
| F01 | 17 | 18 | 5+3+5+5 |
| F02 | 17 | 18 | 5+3+5+5 |
| F03 | 17 | 18 | 5+3+5+5 |
| F04 | 16 | 18 | 4+4+5+5 |
| F08 | 13 | 15 | 3+3+4+5 |
| F09 | 14 | 15 | 4+3+4+4 |
| F10 | 14 | 15 | 4+3+4+4 |
| F20 | 14 | 16 | 3+3+5+5 |
| F21 | 13 | 15 | 3+3+4+5 |
| F22 | 13 | 15 | 3+3+4+5 |
| F23 | 14 | 16 | 3+3+5+5 |
| F24 | 16 | 18 | 5+3+5+5 |
| F26 | 13 | 15 | 3+3+4+5 |
| F28 | 14 | 15 | 4+3+4+4 |

All mismatches are in the formal master tables; the CSV is the source of truth. Either the CSV axis scores or the printed AI-Fit totals must be reconciled. Root cause: the doc values appear to have been calculated without one of the four axes (possibly Feasibility was omitted in an earlier draft pass).

---

### Check 5: Feature count and ID completeness

**PASS.** Section 4 contains exactly 62 data rows. All IDs F01 through F62 are present exactly once. No duplicates. No gaps.

---

### Check 6: Priority and Prior-AI columns vs. CSV

**Priority: PASS.** All 62 priority values in the formal master tables match the CSV `Priority_draft` column exactly.

**Prior-AI: FAIL.** Six features have a mismatch between the Prior-AI /5 value printed in the formal master and the `PriorAI_Maturity` column in the CSV.

| Feature ID | Doc says | CSV says |
|---|:---:|:---:|
| F01 | 5 | 4 |
| F02 | 5 | 4 |
| F03 | 5 | 4 |
| F04 | 4 | 3 |
| F09 | 4 | 3 |
| F10 | 4 | 3 |

---

### Check 7: Formal vs. ADHD agreement

**PARTIAL FAIL.** One substantive omission found.

The ADHD variant "What to build first (P1)" section lists 18 features across capture core, companion core, brainmap core, and sensing core. The formal master P1 build list contains 23 features. Five P1 features from the formal master are not mentioned in the ADHD P1 summary:

- F06 Social Presence AI (body-doubling)
- F07 Dual-track planning (ideal vs. baseline)
- F08 Emoji mood on tasks
- F17 Private emotional notes before planning
- F57 Adaptive personas (implicit mood/mindset matching)

All five are confirmed P1 in the CSV. This is an omission in the ADHD variant, not a contradiction, but a reader relying solely on the ADHD variant would build an incomplete P1 set. Recommend adding them or noting the ADHD variant is a curated subset.

No other contradictions found. The moat features table (8 rows, all AI-Fit 19) matches the CSV exactly. The leaders table matches the formal master. The caveats (Mindstrong, Brain.fm, Chen et al., Blue Lin) are consistent with the formal master. The safety-gap warning (privacy schema, crisis detection) matches Section 11.

---

### Check 8: Mermaid diagram syntax

**FAIL.** The Mermaid diagram in the ADHD variant (lines 40 to 56) contains one syntax problem that is also the em-dash violation from Check 1.

- Line 42: `YAR["Yar — unified ND companion<br/>spans all 6 domains"]` uses an em-dash character inside a quoted node label. Mermaid parsers may accept this, but it violates the no-em-dash rule and is a latent rendering risk.

All bracket types are balanced. Node IDs are valid. `style YAR fill:#8B3FC7` is present and correct (line 49). All six domain nodes have matching `style` declarations. `graph TB` direction declaration is valid. No other syntax problems detected.

---

### Check 9: Voice and neurodiversity-affirming language

**PASS.** All headings use active voice. No deficit-framed language found in headings or key claims. Social communication differences are consistently framed through the double-empathy problem. The phrase "people with ADHD symptoms" in Section 10.2 of the formal master is clinically precise and appropriate in a caveat context (it accurately describes the Brain.fm study population, not a characterization of users). No non-person-first constructions detected.

---

### Check 10: Metadata headers

**PASS.** Both files have a complete metadata header block.

Formal master: Status, Date, Author, Audience, Tags, Supersedes. All fields populated.

ADHD variant: Status, Date, Author, Audience, Tags, Canonical source. All fields populated.

---

## Summary of required fixes

| # | File | Severity | Fix |
|---|---|---|---|
| 1 | `*-adhd.md` line 42 | Medium | Remove em dash from Mermaid YAR node label |
| 4a | `*-v4.md` Section 4 tables | High | Reconcile 14 AI-Fit /20 values with CSV source (or update CSV axis scores) |
| 6 | `*-v4.md` Section 4 tables | Medium | Reconcile 6 Prior-AI /5 values with CSV (F01, F02, F03, F04, F09, F10) |
| 7 | `*-adhd.md` lines 113-117 | Low | Add F06, F07, F08, F17, F57 to the P1 section or note that the list is a curated subset |

No changes needed to: forbidden words, Substrate naming, CSP/USAP framing, feature count, priorities, caveats, leaders table, Mermaid structure, voice/framing, or metadata headers.

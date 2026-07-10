# Contractor and Subawardee Restrictions — IGoR Transcript Extraction

**Source session:** local_f3f4021c-5d7b-436a-b6a1-96c16339a287
**Session title:** "Contractor and subawardee restrictions"
**Recency rank:** 4
**Extraction date:** 2026-06-19

---

## Summary

This transcript analyzed eligibility, teaming, and OCI rules for IGoR (ARPA-H-SOL-26-155, ISO/OT) across TA1–TA4, with a specific focus on whether Matt Tegtmeyer and Purdue could participate on both PsychIGoR and a competing IGoR team. Key finding: the solicitation imposes no per-person or per-org cap on participation in multiple proposals; the binding constraints are committed effort ≤100%, OCI disclosure, and a post-award sub de-duplication rule. The transcript also reconciled a factual conflict on the Program Manager identity (Sheehan, not Vodovotz), and updated ~30 docs after Matt and Anne's roles were clarified.

---

## Key facts (with dates)

### Multi-proposal participation rules
- "An organization may serve as a sub-performer under multiple proposals." (Appendix A §5.1; no explicit date; recency rank 4)
- The solicitation is **silent** on person-level participation limits; no cap on individuals appearing on multiple proposals. (Appendix A §5.1; no explicit date; recency rank 4)
- An org priming two competing teams is not banned in text but is discouraged by optics; the one-PI/one-prime structure per proposal does not contemplate self-competition. (no explicit date; recency rank 4)
- Same concept funded elsewhere is **barred** by the conformance rule. (Appendix C §1.1(a); no explicit date; recency rank 4)

### Post-award de-duplication
- If the same sub lands on two selected teams doing overlapping same-TA work, ARPA-H may fund it once or require the sub to elect one team. This triggers **at selection, not at proposal**. (no explicit date; recency rank 4)
- There is no TA-to-TA separation rule. OCI is disclosure-based only. (no explicit date; recency rank 4)

### Stage-gate enforcement
| Stage | Key rules active |
|---|---|
| Solution Summary (Jun 25) | No committed effort, no OCI disclosure, team is non-binding. No conflict gate. |
| Full Proposal (Aug 6) | Named roles + committed hours + Current-and-Pending + OCI disclosure required for Key Personnel. |
| Award | Effort limits become contractual (≤100%); sub de-duplication can trigger. |

### SAM/UEI
- SAM/UEI is optional at Solution Summary; **required for prime** at Full Proposal. (no explicit date; recency rank 4)
- IPAI is a Purdue unit on Purdue's UEI, not a separate registrant. They cannot be split into two primes. (no explicit date; recency rank 4)

### Prime/sub structure
- PsychIGoR structure: **IPAI/Purdue as prime, Cytognosis as sub.** (confirmed in team tracker; no explicit date; recency rank 4)
- Matt Tegtmeyer's other IGoR bid goes through **Indiana University (IU) as prime**, not Purdue. This means two different legal entities priming (Purdue vs IU), which is clean — no prime-level conflict. (confirmed 2026-06-17 per transcript context)
- If Matt is Purdue faculty and joins the IU team, Purdue likely takes a subaward on that IU team to host his effort. That is allowed (org as sub on multiple proposals), but Matt's Purdue wet-lab bench must not be double-committed. (no explicit date; recency rank 4)

### Program Manager
- The IGoR Program Manager is **Paul E. Sheehan, Ph.D.** (ex-DARPA BTO), confirmed via ARPA-H website. (verified 2026-06-17 per transcript)
- "Yoram Vodovotz" in the draft OT Agreement (Appendix E) is a **template acting-AOR placeholder**, not the real PM. Any doc using "Vodovotz" as PM was corrected during this session.

### Anne Carpenter and Matt Tegtmeyer role clarification
- Anne Carpenter: **purely computational** — interpretable morphology/imaging models. **No wet-lab bench**. (clarified by Matt, 2026-06-17 per transcript)
- Matt Tegtmeyer: **all experiments** — academic experimental arm TA4. Uses **Element Biosciences AVITI24 / Teton CytoProfiling** (fixed-cell in-situ, RNA + protein + Cell-Painting morphology from same sample, CRISPR-guide sequencing). (clarified 2026-06-17)
- Both Anne and Matt are also on a competing IGoR team led by 5 other PIs via IU as prime; Purdue likely subawardee there.

### TA4 structure (finalized in this session)
| Layer | Who | Role |
|---|---|---|
| Academic experimental arm | Matt Tegtmeyer lab (Purdue) | All wet-lab experiments; Element AVITI24/Teton |
| Industry experimental arm | Cellanome | R3200 live-cell + Perturb-LINK |
| Computational | Anne Carpenter | Interpretable morphology/imaging models; no bench |

- The ">=2 TA4 labs" IGoR requirement is met by Matt's lab + Cellanome. (no explicit date; recency rank 4)

---

## Cost/indirect implications

- The transcript flagged ~31 dollar figures in the cost model for re-derivation after the Anne/Matt role correction. These were labeled `[FLAG 2026-06-17]` and were **not auto-changed** — attribution narrative was updated but no numbers were altered. (2026-06-17)
- Anne moves from wet-lab capex to personnel + compute in the cost model (implication, not explicit figure).
- Equipment stand-up is Matt's bench, not Cellanome's, pending Cellanome pricing decision.
- Cellanome decision pending: **R3200 in-lab (capex)** vs **send-out (opex)** — Cellanome to send pricing numbers. (2026-06-17)
- The session noted that indirect costs and de minimis rate implications for Cytognosis as sub were not analyzed in this transcript; the focus was on eligibility and teaming rules, not rate calculations.
- Element Biosciences is a platform Matt's lab already uses, **not a confirmed teaming partner**; no budget line for Element should be created without a partnership confirmation.

---

## Decisions

1. **Matt is primary on PsychIGoR** — to be confirmed at Jun 29–Jul 3 Purdue visit. His committed hours on PsychIGoR and the IU team must not overlap.
2. **IU is the other team's prime** (not Purdue) — confirmed by Matt per transcript context (2026-06-17).
3. **Anne Carpenter role fixed** — purely computational across all docs; her role on the IU team does not conflict with PsychIGoR (different legal entity, no bench commitment).
4. **Cellanome framing corrected** — head-to-head Matt-lab vs Cellanome comparison reframed as a Phase I cross-arm concordance milestone (validation), not a standing funder-toward-Cellanome commitment. This was identified as a framing risk introduced in the Cellanome meeting.
5. **Paul E. Sheehan confirmed as PM** — all docs updated; Vodovotz references removed.
6. **~31 cost figures deferred** to Shahin/Ananth for re-derivation; none were auto-changed.

---

## Conflicts to flag

1. **Matt and Anne on competing IGoR team (IU-prime):** Permitted by solicitation, but at Full Proposal stage (Aug 6), Matt's committed effort must be split with non-overlapping hours and disclosed in Current-and-Pending. Risk: if both PsychIGoR and the IU team are selected, Purdue's bench could be flagged for de-duplication. Resolve at Purdue visit Jun 29–Jul 3.

2. **Anne as lead PI candidate vs IU team:** If Anne is considered for lead PI on PsychIGoR, her concurrent role on the competing IU team needs explicit reconciliation. The transcript flagged this but did not resolve it.

3. **Purdue subaward on IU team:** If Purdue takes a subaward on the IU team to host Matt's (or Anne's) effort, Purdue appears as sub on two competing proposals. This is permitted but must be disclosed at OCI and the bench/compute must not be double-committed.

4. **Cost model not yet re-derived:** ~31 figures carry `[FLAG 2026-06-17]` labels; the cost model as of this session is **not submission-ready** on numbers.

5. **Cellanome pricing outstanding:** The R3200-in-lab vs send-out decision is unresolved. This affects capex vs opex structure of the TA4 budget line and must be resolved before the Aug 6 Full Proposal.

6. **Element Biosciences not a confirmed partner:** Referenced as a platform Matt uses; must not be listed as a teaming partner in any submission without explicit confirmation.

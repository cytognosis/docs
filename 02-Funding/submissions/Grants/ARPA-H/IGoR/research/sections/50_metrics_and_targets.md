## 50. Metrics, milestones, and quantitative targets

**Program marquee metrics (from IGoR Appendix A):** The IGoR program targets at least a 4x improvement in experimental cycle time by Phase II and at least a 10x improvement by Phase III, with at least 90% cross-laboratory concordance and at least 85% of TA2-proposed experiments rated high-value by an expert panel.

Our proposed targets meet or exceed every program minimum. Items where our self-set targets exceed the program minimum are marked with an asterisk (*).

---

### Integrated go/no-go table by phase and TA

| TA | Metric | Phase I (mo 18) | Phase II (mo 36) | Phase III (mo 60) | Notes |
|---|---|---|---|---|---|
| **TA1** | Disease-model sub-models | >=3 | >=10, across >=2 scales | >=15, across >=3 scales | Program minimum not stated at this granularity; self-set |
| **TA1** | Quantitative knowledge gaps detected | >=3 algorithmically | Ongoing; gaps feed TA2 | Ongoing | Self-set; makes gaps explicit and rankable |
| **TA1** | Variance explained (22q11DS cell-type shifts) | >=30% | Not specified | Not specified | Self-set; Phase I go/no-go* |
| **TA1** | Parameter uncertainty reduction (first TA4 return) | >=20% | Not specified | Not specified | Self-set* |
| **TA1** | Novel prediction confirmed | Not applicable | >=1 in independent dataset | Novel validated hypotheses in both diseases | Self-set Phase II go/no-go |
| **TA1** | Model update latency | Baseline established | <=24 h | <=4 h | Self-set; program asks for "low latency" without a number |
| **TA2** | Expert panel rating (high-value experiments) | >=50% | >=75% | >=85% | Matches program minimum by Phase III |
| **TA2** | Usability (researchers rating system useful) | Not applicable | >=70% (>=10 scientists) | >=80% (>=20 researchers incl. external) | Self-set |
| **TA2** | Model backends (>=1 open-weight) | 1 | >=2 | >=2 | Program asks for open-weight capability; self-set Phase II target |
| **TA3** | Modalities covered | >=2 | >=3 | >=4 | Program minimum >=3 modalities; Phase I target is below program minimum (build ramp) |
| **TA3** | Labs running protocols | 2 (team only) | >=3 (incl. >=1 cross-team) | >=5 across teams | Matches program requirements |
| **TA3** | RFCs | Not applicable | >=2 | Ongoing | Self-set governance metric |
| **TA4** | Cross-lab concordance | >=80% (intra-team) | >=90% (cross-team) | >=90% across marketplace | Meets program minimum (>=90%) by Phase II* |
| **TA4** | Experiments executed to concordance standard | >=1 at 2 labs | >=3 (cross-team) | Marketplace scale | Program requires >=2 labs; self-set experiment counts |
| **TA4** | Exceptions handled autonomously | Not applicable | Reduced >=50% vs. Phase I | >=70% autonomous | Self-set Phase II/III targets |
| **Program** | Experimental cycle time | Baseline established | >=4x faster vs. baseline | >=10x faster vs. baseline | Matches IGoR marquee metrics |

---

### Metrics that exceed program minimums (starred items)

1. **TA1 variance explained (>=30%, Phase I):** The program does not specify a percentage; we set this as a Phase I go/no-go to make TA1 progress falsifiable at the first gate.
2. **TA1 parameter uncertainty reduction (>=20%, first TA4 return):** Directly tests the closed-loop hypothesis that TA4 data constrains the TA1 model; program does not require this specific check.
3. **TA4 concordance at Phase II (>=90%):** The program requires >=90% concordance but does not specify it must be achieved by Phase II. We set this as a Phase II target, one phase earlier than the program minimum.

---

### Dropped metric: Spearman r >=0.4 (TA2 Phase I)

The **2026-06-02 Solution Summary** included a TA2 Phase I go/no-go metric requiring hypothesis rank to correlate with experimental effect size at Spearman r >=0.4 on the first ten experiments. This metric does not appear in the **FULLPROPOSAL_DRAFT (2026-06-12)** milestone table.

This metric is scientifically important: it provides a direct, falsifiable test of whether the TA2 value-of-information ranking is actually predictive. It should be restored in the full proposal. The program does not require it, but including it demonstrates mechanistic rigor.

---

### Program-level cycle-time target pathway

| Phase | Cycle-time target | How we demonstrate it |
|---|---|---|
| Phase I | Baseline established (conventional research, months to years) | Document a representative conventional experiment timeline at Phase I kickoff |
| Phase II | >=4x faster than baseline | Measure time from TA2 query to validated TA4 data return; compare to baseline |
| Phase III | >=10x faster than baseline | Same measurement at marketplace scale; document in transition plan |

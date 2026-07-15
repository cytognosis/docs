# IGoR Cost Breakdown (planning model)

**Date:** 2026-06-02 · For the full Price Proposal (Aug 6) and the Solution Summary Basis of Estimate (Jun 25). **Planning model, not a quote.** IGoR states **no funding ceiling**; ARPA-H negotiates the budget and indirect rate per OT. All figures are ranges from reputable sources; confirm with a grants administrator/CPA and with Cellanome and Purdue for their actual rates.

## Total and split (5 years, 3 phases: 18 + 18 + 24 mo)

Anchored to comparable ARPA-H multi-team programs (PARADIGM ~$17M/team avg; NITRO ~$20-39M/performer). Modeled midpoint **~$30M consortium total** (defensible range $25-60M).

| Performer | Role | Share | 5-yr total | ~Annual |
|---|---|---|---|---|
| **Cytognosis** (prime) | TA1 + TA2 | ~45% | ~$13.5M | ~$2.5-2.7M |
| **Cellanome** (sub) | TA3 + TA4 (experiments) | ~35% | ~$10.5M | ~$2.0-2.1M |
| **Purdue / IPAI** (sub) | TA1/TA2 support (Grama, Carpenter) | ~20% | ~$6.0M | ~$1.2M |

Phasing ramps: Phase I ~80% of steady-state (build), Phase II full (integration), Phase III heaviest (second-disease + external experiments).

## Cytognosis prime, annual (~$2.5-2.7M)

**Personnel (fully-loaded = base + ~30% fringe, Bay Area), ~7 FTE:**

| Role | FTE | Fully-loaded | Source anchor (BLS OEWS May 2024 + market) |
|---|---|---|---|
| PI (Mohammadi), partial effort | 0.5 | ~$100K | reasonable-comp ~$200K/yr, coordinated/capped across awards |
| Software architect (TA2/integration; IGoR-required) | 1.0 | ~$240K | SOC 15-1252; San Jose median ~$180K base |
| Senior ML/AI engineer (TA2) | 1.0 | ~$260K | SOC 15-1221; Bay base $180-220K |
| ML/AI research scientist (TA1/TA2) | 1.0 | ~$240K | SOC 15-1221 |
| Computational biologists (TA1) | 2.0 | ~$420K | SOC 19-1029; Bay base $140-175K |
| Technical project manager (IGoR-required) | 1.0 | ~$200K | SOC 11-3021/15-1299 |
| Research scientist / postdoc | 1.0 | ~$110K | NIH NRSA floor + Bay premium |
| **Personnel subtotal** | ~7.5 | **~$1.57M** | |

**Other prime costs (annual):** compute ~$400K (TA1 training ~$250K + TA2 inference/orchestration ~$150K; H100 blended ~$2.50/GPU-hr); other direct (travel, open-source infra/CI, data licensing, external security/audit, dev hardware) ~$200K; **indirect at the 15% de minimis MTDC rate** ~$330K (effective ~12% after equipment + over-$50K-subaward exclusions). **Prime annual ≈ $2.5M.**

## Cellanome sub (TA3/TA4), ~$2.0M/yr

Experiment-heavy. Annual envelope: optical pooled screens (R3200) ~$50-500K each; targeted Perturb-seq $5-30K/screen (genome-scale $50-300K); scRNA-seq ~$200-700/sample multiplexed; iPSC-to-neuron differentiation ~$3-15K/run. Plus Cellanome personnel + instrument time + their G&A. Model **~$2M/yr** (3-5 screens + ~100 scRNA-seq samples + iPSC lines/yr, scaling in Phase III). Confirm Cellanome's actual per-screen pricing for the sub-award justification.

## Purdue/IPAI sub, ~$1.2M/yr

1-2 researchers + Grama and Carpenter effort + students; Purdue applies its **negotiated F&A (~55-60% MTDC, on-campus)**. Covers TA1 mechanistic-modeling reinforcement and pooled-optical-screening expertise (Carpenter).

## Indirect / F&A notes

- **Cytognosis:** 15% de minimis MTDC (2 CFR 200.414(f), 2024 update) is the simplest defensible anchor; a negotiated NICRA (18-24 mo to establish) could be higher. On an **OT**, ARPA-H is not bound by 2 CFR 200, so propose the actual rate and justify it (IGoR FAQ: "ARPA-H does not have a fixed indirect cost rate").
- MTDC base includes only the **first $50K of each subaward**; amounts above are excluded from the prime's indirect.
- Each sub applies its own rate (Purdue negotiated; Cellanome G&A).

## Compute note: build vs buy

H100 on-demand: ~$2.99 (Lambda), ~$3.00 (GCP), ~$3.90 (AWS P5); marketplace floor ~$1.50-2.00. On-prem 8xH100 server ~$200-320K hardware; amortized ~$4-8/GPU-hr at 50% use; break-even vs cloud ~18 months of continuous use. Recommend cloud/committed for Phase I, reassess on-prem if utilization is sustained.

## Solution Summary Basis of Estimate (the short version for the 5-pager)

A 5-year, 3-phase consortium. Cytognosis (prime) leads TA1/TA2 with ~7 FTE (PI, software architect, ML/AI engineering and science, computational biology, project manager) plus compute and the open-source release stack. Cellanome (TA3/TA4) provides R3200-based interoperable protocol execution and the experiment marketplace. Purdue/IPAI reinforces TA1 mechanistic modeling and pooled optical screening. Costs are driven by personnel and experimental throughput, ramping across phases as the second disease area and external validation come online. Cost-sharing via shared infrastructure, open data, and IP-access arrangements will be incorporated. Specific figures provided in the full Price Proposal.

## Sources

BLS OEWS May 2024 (USDL-25-0451; SOC 15-1221, 15-1252, 19-1029, 11-3021); NIH FY2026 NRSA (NOT-OD-26-044); 2 CFR 200.414(f) de minimis 15% MTDC (Clark Nuber); IGoR FAQs (ARPA-H, indirect negotiated per OT); H100/A100 pricing (IntuitionLabs, Spheron, May-Jun 2026); Perturb-seq/scRNA-seq costs (Stanford Perturb-seq protocol; Replogle et al. Nat Biotech 2023; Satija Lab cost-per-cell); ARPA-H comparables (PARADIGM $139M/8 teams; NITRO ~$20-39M/performer); DARPA per-performer ranges. Full URLs in the cost-research subagent log (this session).

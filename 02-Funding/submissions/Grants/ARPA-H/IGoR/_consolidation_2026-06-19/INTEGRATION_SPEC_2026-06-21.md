# IGoR Integration Spec — Dan's TA2/TA3, SIFT cost, innovations, phases, messaging (2026-06-21)

**Purpose:** Single durable capture of everything from Shahin's 2026-06-21 directive, ready to execute as a clean program in a fresh session. Nothing here is yet cascaded into the SS / C1 / C2 / C3 / cost docs or Google. Two decisions (below) gate the budget and the Google sync.

**BLUF (3 sentences):** Integrate Dan's TA2/TA3 write-up and SIFT's real $7.0M cost, add a Duane legal line, fold in five methodological innovations and the three experimental stages, and add the "only team with both clinical and cellular world-experts" messaging, across local docs and Google. Two blockers gate execution: native Google Doc editing/commenting is not available via current connectors, and SIFT at $7.0M (vs $5.0M placeholder) plus a Duane line breaks the $50M envelope. Both need a decision before the cascade.

---

## DECISIONS NEEDED (gate everything)

1. **Budget envelope.** SIFT $5.0M -> **$7.0M** (+$2.0M, Dan's real figure). Plus a new Duane legal/IP consultant line (proposed ~$150-300K). Options: (a) raise the total ask above $50M if the IGoR solicitation ceiling allows (verify the per-award ceiling in Appendix A first), or (b) hold $50M and cut ~$2.2M+ from other lines (candidates: Phylo optional $4.0M, Illumina optional $4.0M, cross-team reserve $2.8M). Recommendation: confirm the ceiling, then prefer trimming the two optional lines (Phylo/Illumina) before touching core performers. Needs Shahin + Ananth.
2. **Google sync pathway.** No native Google Docs edit/comment tool is connected. Options: (a) connect a Google Docs MCP with edit + comment scope (durable; enables programmatic inline comments and in-place updates), or (b) use Claude in Chrome to edit the docs and add comments in-browser (works now, slower, more fragile). Recommendation: (a). Until then, the local .docx/.pdf remain the build-of-record and get re-uploaded to Drive.

---

## 1. SIFT cost (Dan, 2026-06-21) — supersedes the $5.0M placeholder

| Category | Amount |
|---|---|
| Direct Labor (fully burdened) | $4,094,437 |
| Labor hours | 24,204 |
| Subcontracts/Consultants | — |
| Materials | — |
| Equipment | — |
| Travel | $69,747 |
| Other Direct Costs | (not specified) |
| Indirect Costs | $2,199,941 |
| Profit | $636,412 |
| **Total (all phases)** | **$7,000,537** |
| Resource Sharing | — |

Action: update SIFT to $7.0M (round) in C3, COST_MODEL_DETAILED, the SS BOE per-performer table, and the C4 workbook; re-run the envelope reconciliation per Decision 1. Keep the 70% Bryce / 30% Goldman split note; add labor hours (24,204) and the travel line.

## 2. Duane legal/IP budget + role (to add)

Duane Valz = outside counsel for Cytognosis (IP, OT agreement, data/IP flows; ex-insitro). Add a Consultants/Subcontracts line for legal: IP strategy, OT/Other-Transaction agreement review, data-use and IP-flow governance, field-of-use splits. Proposed placeholder ~$150-300K over 5 years (rate ~$500/hr). Role: legal/IP advisor (not key personnel). FLAG for Duane (scope/rate) and Ananth (financial verification). Exact figure pending Decision 1.

## 3. Dan's TA2/TA3 write-up (verbatim, to integrate; mark sections as SIFT-authored DRAFT/sketch for Dan to revise)

**TA2: New Science Engine.** SIFT's TA2 contribution builds on its XPlan experimental planner from DARPA SD2. From a prioritized set of knowledge gaps, SIFT develops hypotheses and identifies experimental designs to close them, expressed as experimental intent in a new ontology layer. Agentic programming methods connect human experts with TA1 mechanistic models and emerging protocols to collaboratively develop a machine-interpretable representation of experimental intent. Expressing intent in structured, ontology-grounded terms (biological entities, experimental variables, measurable outcomes, expected model updates) provides the semantic specificity to drive downstream TA3 protocol generation.

**TA2-TA3 interface: shared ontologies and knowledge graphs.** SIFT leads the design and implementation. Builds on LabOP (open spec, open-source Python library, example protocols) which already integrates ontologies for measurement units, container types, chemical entities, biological materials. IGoR needs a richer shared semantic layer encoding relationships among mechanistic disease models, knowledge gaps, experimental variables, and protocol steps, so TA2 hypothesis outputs translate into TA3 protocol specs through structured, traceable representations rather than ad hoc text generation. Formally specified during the Phase I Domain-Driven Design workshop, with explicit data models defining what flows TA2->TA3, in what format, under what validation constraints.

**TA3: interoperable experimental procedures.** LabOP's layered model maps onto IGoR's protocol-stack requirement (separating intent from instrument-level execution). Three tiers: (1) a UML Activity Model base (control flow, dataflow, parameterization, activity composition); (2) LabOP protocols above it (sample arrays, datasets, primitive operations, external ontologies for measures/units/strains/chemicals/media/containers); (3) LabOP Executions at top (execution sequences, runtime variable bindings, datasets, provenance per W3C PROV-O). Existing execution engine spans metadata simulation -> semi-automated -> fully automated, exporting machine-readable and natural-language formats for TA4 labs of varying sophistication. SIFT will enhance the engine to support protocol authoring against TA1 mechanistic models (simulating biological and protocol behavior before lab execution), expand LabOP primitive libraries for the chosen disease focus, and support IV&V bake-offs and the RFC process, contributing LabOP as the candidate program-wide protocol standard for adoption beyond the period of performance.

Integration note: this refines (and is consistent with) the current TA3 stack (LabOP + SiLA 2 + RFC governance + LinkML/Biolink). XPlan/SD2 lineage and PROV-O provenance are NEW specifics to add. Mark all TA2/TA3 prose as "SIFT draft, pending Dan's revision."

## 4. Five methodological innovations (integrate into full proposal; summarize the top ones in the SS)

1. **Residual-space alignment of cellular and clinical models.** iPSC/organoid models differ from primary cells (stem signatures, primary-cell-type memory, differentiation artifacts) yet respond similarly (positions differ, but velocity/acceleration vectors align). Align by computing each model's "disease axes" (biologically disentangled processes separating healthy vs disease states) and explicitly aligning axes across models via regularization/constraints (e.g., OT / MMD distance between posterior distributions in variational models).
2. **Universal treatment+disease language on a shared delta-pathway feature space.** Convert treatment effects (genetic/chemical) and disease onto the same feature space (delta processes/pathways), so all enter one structural causal model (SCM) with three latent sets: basal cell state; disease (causal on cell state); treatment (causal on cell state via an indirect path through disease and a direct disease-independent/side-effect path).
3. **Ontology-grounded semantic embeddings + OOD projection head.** Pre-embed EL++ ontologies (TransBox) for MONDO (disease), GO (cellular function), Cell Ontology (cell types), etc.; add a projection head for out-of-distribution prediction of unseen entities (e.g., new cell types) via similarity/distance to seen entities.
4. **Pretrained genomic foundation models + genomic factorization.** AlphaGenome, VariantFormer, plus added layers for genomic factorization into biologically disentangled genotypic archetypes of disease.
5. **Multiresolution network-diffusion GNNs.** Graph-wavelet models capturing both short- and long-range diffusion in biological networks.

TODO: read prior grants (Google Impact and others) for additional innovations/context and fold into the full proposal; summarize the highest-impact ones in the SS. (Likely locations: search the Grants repo and prior funding folders for "Google Impact" / Coefficient / EA / NSF / NIH narratives.)

## 5. Three experimental stages (map to the three proposal phases and milestones)

- **Stage 1 — create and prioritize disease models.** Use the curated SZ genomic variations (Shahin's list) + prioritized genes/experiments from PsyGene / SSPsyGene (https://sspsygene.ucsc.edu/). Pooled or arrayed (decide by gene count + cost) in healthy NGN2 lines; decide number of genetically distinct backgrounds and control ethnicities. Panels: SZ-specific (CNVs + SCHEMA genes), BD variants, broader psych variants, control genes. Collect transcriptomic, morphological, functional (calcium-imaging) readouts. Prioritize 5-10 genes with the most robust, reproducible, prominent phenotypic shifts vs controls for screening (exact numbers + quantitative metrics become milestones). Optionally spike in a broader gene set if pooled. Feeds TA1 to build cellular/in-vitro disease axes; clinical counterpart = genotypes + snRNA-seq from primary samples.
- **Stage 2 — disease-model-specific unbiased pooled assays (Perturb-seq)** in the prioritized lines, as the basis for validating treatment effects; feeds TA1 to learn treatment embeddings.
- **Stage 3 — targeted perturbation** of pathways/processes nominated by TA1/TA2; strategic combinatorial perturbations of multiple key genes (compensatory/redundant pathways mean single-point interventions are limited except at hubs, which risk broad side-effects).

These map to Phases I/II/III and define key milestones (use the quantitative gene-count and effect-size metrics from Stage 1 as Phase I milestones).

## 6. "Best team" messaging (Patty's emphasis; repeat, paraphrased, across sections; keep politically correct)

Core claim: our team uniquely brings together world experts in BOTH the clinical (Shahin, Brad) AND the cellular (Matt, Anne) sides of neuropsychiatric disease, for the first time. These are usually done in disjoint organizations with different expertise, language, and even literatures, led by different people who rarely talk to each other (illustrative, stated diplomatically: the separation between clinical-ML and cellular-ML groups in industry). Phrase as a strength of integration, never as criticism of others.

Supporting points to weave in:
- Why clinical matters: ~2-3x higher clinical success for genetically-supported targets; enables precision-medicine matching of therapeutics/interventions to individuals.
- Clinical-side challenges this team overcomes: most variants are noncoding and of unclear disease relevance; complex interactions among variants hypothesized to converge on shared biological processes across familial/rare and sporadic/common forms, but never verified nor modeled; inability to experimentally test these hypotheses; causal modeling limited to Mendelian randomization and mediation analysis (instrumental but strong-assumption, narrow-scope).
- Why cellular bridges it: disease-in-a-dish enables high-throughput screening of many genetic/chemical interventions to find disease-inducing and disease-reverting (protective-variant-matching) effects, perfect for bridging clinical hypothesis formation (TA1) -> hypothesis generation (TA2) -> cellular validation (TA3/TA4).

## 7. Per-person inline-comment tagging map (for the Google Doc, once an edit/comment pathway exists)

| Topic / section | Tag | Note style |
|---|---|---|
| TA2 and TA3 sections | **Dan** (SIFT) | Mark as sketches/drafts; invite him and his team to revise/rewrite |
| TA1 (disease modeling, causal/SCM, genomic factorization) | **Ananth** | Questions / requests for review |
| Experimental procedures, costs, what is available at Purdue vs needs buying, what is/ isn't experimentally possible | **Matt** (optionally Anne) | Confirm feasibility, equipment, line counts |
| Computational morphology / Cell Painting / imaging models | **Anne** | Confirm method/feasibility |
| Legal, IP, financial flows | **Duane** | Legal/IP review |
| Financial (any budget figure) | **Ananth** (+ Duane for legal-financial) | Verification |
| TA4 R3200; TA3-TA4 and TA4-TA1 interfaces | **Cellanome** | Confirm platform capability and interfaces |
| Concept Summary and all crisp, no-jargon, impactful messaging | **Patty + Ananth** | Feedback on clarity/impact |

## 8. New standing rule (persisted to memory)

From 2026-06-21: every IGoR update must be ALWAYS and FULLY reflected in the associated Google Docs as the central source of truth, with per-person inline comments per the map above. Constraint: no native Google Docs edit/comment connector is currently available; resolve via Decision 2.

## 9. Execution plan for the fresh session (once decisions are made)

1. Read prior grants (Google Impact, Coefficient/EA/NSF/NIH narratives) to harvest additional innovations + context.
2. Rebalance the budget per Decision 1 (SIFT $7.0M, Duane line); update C3, COST_MODEL_DETAILED, SS BOE, C4 workbook; keep arithmetic consistent.
3. Integrate Dan's TA2/TA3 (marked SIFT-draft), the 5 innovations, the 3 stages, and the best-team messaging into C1/C2 (full) and the SS (summarized within the 5-page body).
4. Regenerate all .docx; rebuild the branded SS (Inter 11pt, <=5 pages).
5. Sync to Google per Decision 2; add the per-person inline comments per the map.
6. Verify: page count, citations, envelope arithmetic, comment placement, zero stale terms.

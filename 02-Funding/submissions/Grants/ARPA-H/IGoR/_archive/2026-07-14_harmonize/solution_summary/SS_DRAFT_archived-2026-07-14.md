# ARPA-H IGoR: Solution Summary (DRAFT content)

**For:** ARPA-H-SOL-26-155 (IGoR), Solution Summary due 2026-06-25. Sections 1–4 ≤ 5 pages; BOE and References excluded from the limit.

> DRAFTING NOTES (delete before submission): Prime/PI base case is Purdue/IPAI (PI: Ananth Grama) with Cytognosis as TA1/TA2 lead sub-awardee, per the decided IPAI-prime structure. Flipping to Cytognosis-prime changes only the cover block, PI line, and BOE order. Partner confirmation status: Cytognosis, Ruzicka confirmed; Grama/IPAI, Carpenter, Cellanome, Phylo, SIFT, Illumina warm/in-discussion. DataTecnica (TA2) and Transfyr (TA3) held as alternates pending eligibility/OCI clearance and are not named here.

---

## COVER BLOCK

| Field | Entry |
|---|---|
| Innovative Solutions Opening Title | Intelligent Generator of Research (IGoR), ARPA-H-SOL-26-155 |
| Solution Summary Title | A Closed-Loop, Mechanistically Grounded Research Engine for Complex Neuropsychiatric Disease: Schizophrenia to Bipolar Disorder |
| Prime Organization Name | Purdue University, Institute for Physical AI (IPAI) |
| Prime Organization Type | ☒ Academia |
| SAM.gov UEI | Purdue UEI (on file; Cytognosis UEI HS4PRLL7AKY5 for the lead sub) |
| Contact Address: State | Indiana (Prime); California (Cytognosis) |
| Estimated Project Duration | 60 months (Phase I 18 mo, Phase II 18 mo, Phase III 24 mo) |
| Animal Subjects | ☒ No (cell/tissue culture and lower invertebrates only; no vertebrate work proposed) |
| Human Subjects | ☒ No (secondary analysis of existing de-identified human genomic and single-cell data; no new human-subjects research) |
| Total Funds Requested From ARPA-H (all phases) | $50,000,000 |
| Resource Sharing | Performer in-kind ~$4.0M (data, sequencing credits, instrument access); Gov't $50.0M |
| Place(s) of Performance | West Lafayette, IN; South San Francisco / Daly City, CA; Cambridge, MA; partner laboratory sites |

Key personnel / sub-awardees: Cytognosis Foundation (TA1 lead, TA2 co-lead); Phylo (TA2); SIFT (TA3); Carpenter Laboratory (TA4); Cellanome (TA4); Illumina (TA4); McLean Hospital / Harvard Medical School (clinical co-lead).

---

## 1. CONCEPT SUMMARY

Biomedical discovery for complex diseases is slowed by three compounding failures: models that correlate rather than explain, experiments designed by intuition rather than by what the model most needs to learn, and data that cannot be reproduced or reused across laboratories. The result is that knowledge for diseases such as schizophrenia accumulates slowly, fragments across scales, and rarely yields validated, non-obvious targets.

We propose a complete IGoR team that closes this loop for complex neuropsychiatric disease. Our system couples (TA1) a mechanistic, multiscale disease model that treats disease itself as a causal perturbation on cell state; (TA2) a New Science Engine that interrogates that model to find the knowledge gaps whose resolution matters most and designs the experiments that resolve them; (TA3) a layered, instrument-agnostic protocol stack so any qualified laboratory runs the same experiment reproducibly; and (TA4) a marketplace of validated laboratories that execute those protocols and return gold-standard data that updates the model. The disease focus is schizophrenia in Phases I and II, extending to bipolar disorder, a biologically and genetically related disorder, in Phase III.

This directly addresses every IGoR interest area. TA1 supplies the shared, computable, mechanistic memory the program requires; TA2 is an orchestration layer grounded in that model rather than a wrapper around a language model; TA3 and TA4 make experiments portable and trustworthy. Our differentiator is scientific: where the field's virtual-cell and perturbation models predict the effect of an experimenter's genetic or chemical intervention, we model the perturbation that disease and its associated genetic variation impose on cells, and we factorize that signal into sparse, biologically interpretable "disease axes." Targets that emerge from this model carry human genetic support, which roughly doubles to triples the probability of clinical success (Minikel et al., 2024).

## 2. INNOVATION AND IMPACT

**Outcome sought.** A validated, openly released research engine that generates non-obvious, experimentally confirmed disease mechanisms and candidate targets for schizophrenia and bipolar disorder at least 10x faster than conventional research, with the disease model, protocols, and marketplace reusable by any researcher.

**Why this is innovative and potentially transformative.** Three ideas distinguish our approach from the state of the art. First, disease as the causal perturbation: we invert the virtual-cell paradigm (Bunne et al., 2024) so that disease-associated genetic variation acts as a soft intervention on a latent causal model of cellular biological processes, for which identifiability guarantees exist (Zhang et al., 2023). Second, factorized disease axes: we extend polygenic risk scoring from a single aggregate number to many sparse, pathway-disentangled axes that are interpretable, transdiagnostic, and double as candidate biotypes, building on the sparsity-of-shift-mechanism principle (Bereket and Karaletsos, 2023; de la Fuente et al., 2025). Third, mechanistic experiment design: TA2 proposes experiments that most reduce uncertainty in this causal model, not experiments retrieved from literature, closing the loop with reproducible execution.

**Disruptive relative to current and emerging technology.** Foundation models (scGPT, Geneformer, STATE) and perturbation predictors learn associations and cannot tell which cellular signatures are clinically relevant versus artifacts of a culture system. Agentic-science systems (Co-Scientist, Biomni, Virtual Lab) propose experiments but do not interrogate a mechanistic disease model. No platform integrates atlas-scale data, causal perturbation modeling, instrument-agnostic protocols, and a validated-lab marketplace into a self-updating loop. The table below states our aggressive year-over-year targets against that baseline.

| Capability (challenge) | State-of-the-art baseline | Phase I (mo 18) | Phase II (mo 36) | Phase III (mo 60) |
|---|---|---|---|---|
| Disease model basis | Correlational embeddings; single-scale mechanistic tools | Mechanistic, ≥3 sub-models, ≥3 quantitative gaps detected | ≥10 sub-models, ≥2 scales; ≥1 novel prediction confirmed | ≥15 sub-models, ≥3 scales; validated in 2 diseases |
| Experimental cycle time | Conventional (months to years) | Baseline established | ≥4x faster | ≥10x faster |
| Cross-lab reproducibility | Ad hoc, batch-effect-laden | ≥2 labs, ≥80% concordance | ≥3 labs, ≥90% concordance | ≥90% across marketplace labs |
| Experiment design quality | Intuition / literature-mined | ≥50% rated high-value by experts | ≥75% high-value | ≥85% high-value |
| Model update latency | Manual, months | Baseline | ≤24 h | ≤4 h |
| Disease coverage | One disease, retrospective | Schizophrenia (cellular + clinical) | Schizophrenia (closed loop) | + Bipolar disorder (extension) |

**Who is affected.** Schizophrenia and bipolar disorder affect tens of millions worldwide, and first-line treatments fail a large fraction of people because they target symptoms, not mechanism. A research engine that yields genetically supported, mechanism-anchored targets shortens the path to better therapies and, because it is open and reusable, accelerates discovery far beyond these two disorders.

## 3. PROPOSED WORK

**Final deliverables.** (1) An open, certified-executable, multiscale causal disease model for schizophrenia and bipolar disorder, with model cards and algorithmic gap detection. (2) A New Science Engine that designs high-value experiments grounded in that model, with explainable narratives. (3) An open, layered protocol stack covering ≥4 experimental modalities. (4) A validated-lab marketplace operating across teams with ≥90% concordance. (5) A transition path sustaining the marketplace beyond the program.

**Technical approach.** TA1 builds the disease model on a curated multiscale interaction network (protein-protein, signaling, regulatory, and cell-type-specific edges from PsychENCODE and related resources), with a causal generative layer that decomposes each cell state into a basal state plus sparse additive mechanism shifts. Disease-associated genetic variation, drawn from PGC schizophrenia GWAS (Trubetskoy et al., 2022) and rare-variant data, enters as soft interventions; the model learns sparse "disease axes" that align cellular (induced) and clinical (natural) signals in a common pathway-shift space, which is what lets us separate clinically relevant axes from culture artifacts. We consolidate molecular and target evidence from the Open Targets Platform (Falaguera et al., 2025), scholarly knowledge from the PubMed Knowledge Graph, and our own single-cell multi-cohort schizophrenia atlas (Ruzicka, Mohammadi et al., 2024). TA2 treats the TA1 model as a queryable object: it identifies poorly constrained parameters and missing edges, runs competing hypothesis streams with verification and dissent, and selects the experiment with the highest value of information, expressed in sufficient detail (cell type, perturbation, timepoint, readout) for protocol generation. TA3 encodes those designs in an intent–protocol–calibration–hardware stack built on open standards (LabOP lineage), distinguishing scientifically meaningful parameters from arbitrary local preference. TA4 executes via at least two validated laboratories spanning live-cell imaging with same-cell sequencing, optical pooled and Cell Painting morphological screens, and high-throughput sequencing, returning data that updates TA1.

**Concrete, falsifiable starting point.** Phase I anchors on a high-penetrance cellular model of schizophrenia: paired isogenic iPSC lines carrying a 22q11.2-region lesion, CRISPR-corrected to a matched control and differentiated to neurons. The 22q11.2 deletion is among the strongest known genetic risk factors for schizophrenia, and its cell-type morphological and molecular signatures are experimentally tractable (Tegtmeyer et al., 2025). TA2 designs a discriminating screen; Carpenter and Cellanome execute morphological, live-cell, and transcriptomic readouts; TA1 defines the disease axes and ingests the results, establishing the cycle-time baseline.

**Interim milestones.** Phase I: disease-model architecture documented; ≥3 quantitative knowledge gaps detected; walking-skeleton closed loop (TA2→TA3→TA4→TA1) demonstrated within the team; ≥2 labs at ≥80% concordance. Phase II: automatic model updates from ≥10 data returns; ≥1 novel prediction experimentally confirmed; cross-team experiment executed; ≥4x cycle-time improvement. Phase III: extension to bipolar disorder with validated novel hypotheses in both diseases; unified marketplace at ≥90% concordance; ≥10x cycle-time improvement; all artifacts deposited open-access.

**Alternatives considered.** A purely correlational foundation-model approach was rejected because it cannot identify clinically relevant axes or support causal experiment design. An LLM-agent-only approach was rejected because it lacks mechanistic grounding, which IGoR explicitly excludes. An in-vitro-only optimization (make disease cells resemble healthy cells) was rejected because it cannot distinguish disease axes from model-system artifacts; our joint cellular-clinical shift space is designed precisely to solve this.

**Adoption challenges and technical risk.** Key risks: cellular models may not faithfully represent in-vivo disease (mitigated by the joint cellular-clinical alignment and genetic anchoring); cross-lab concordance is hard (mitigated by the calibration layer and IV&V collaboration); causal identifiability from observational genomic data is non-trivial (mitigated by interventional cellular data closing the loop). These are substantial risks, counterbalanced by the transformative payoff of a self-updating, reusable engine that produces genetically supported targets.

## 4. TEAM ORGANIZATION AND CAPABILITIES

The team is one integrated performer led by a single PI, addressing all four TAs across all three phases. Roles: IPAI/Purdue (prime) leads integration, program management, and software architecture, and supports TA1/TA2; Cytognosis leads TA1 and co-leads TA2; Phylo co-leads TA2 (agentic science); SIFT leads TA3; Carpenter, Cellanome, and Illumina constitute the TA4 laboratory network; McLean/HMS provides clinical and translational grounding.

- **Ananth Grama, PhD, Director, Institute for Physical AI, Purdue (Principal Investigator).** Large-scale computational systems, high-performance computing, and data science; leads cross-team integration and management.
- **Shahin Mohammadi, PhD, Founder and CEO, Cytognosis (TA1 lead, TA2 co-lead).** Twenty years in computational biology (MIT, Broad, insitro, GenBio AI); co-first author of the single-cell multi-cohort schizophrenia atlas; built sparse mechanism-shift perturbation models for single-cell data.
- **Kexin Huang, PhD, Founder, Phylo (TA2).** Creator of Biomni; agentic biomedical AI and multi-agent scientific reasoning.
- **Anne Carpenter, PhD, Senior Director and Institute Scientist, Broad Institute (TA4, optical/morphological).** Inventor of Cell Painting; co-author of the 22q11.2 deletion phenomics study central to our Phase I anchor.
- **Robert Goldman, PhD and Dan Bryce, PhD, SIFT (TA3).** Developers of LabOP; automated planning and laboratory protocol interoperability.
- **Dwight Baker, SVP Product Development, Cellanome (TA4, live-cell + Perturb-seq).** Single-cell live-imaging and pooled CRISPR screening platform for neuronal models.
- **W. Brad Ruzicka, MD, PhD, McLean Hospital / Harvard Medical School (clinical co-lead).** Co-led the single-cell schizophrenia atlas; psychiatric neuroscience and human postmortem genomics.
- **Illumina (TA4, sequencing and data; key contact in discussion).** High-throughput sequencing and the Billion Cell Atlas perturbation resource, contributed in part as in-kind resource sharing.
- **Software Architect, Cytognosis (to be named; recruiting underway).** Distinct from the PI and Project Manager; architectural authority over interfaces and interoperability, with experience building API-first, open-source infrastructure.
- **Project Manager, Patty Purcell (in discussion).** Day-to-day management of a large multi-organization effort.

---

## 5. BASIS OF ESTIMATE (BOE): not in the page limit

| Category | Amount | Basis |
|---|---|---|
| Direct Labor (fully burdened) | $22.0M | ~14 funded FTE/yr across 7 organizations × 2026 loaded rates |
| Labor hours | ~147,000 | $22.0M ÷ ~$150/hr blended (salary + fringe) |
| Subcontracts / Consultants | $1.0M | Clinical co-lead, biostatistics, ethics/IRB, standards consultants |
| Materials | $6.0M | iPSC + NGN2 differentiation, CRISPR libraries, Perturb-seq kits, Cell Painting reagents, sequencing consumables |
| Equipment | $2.5M | Imaging and instrument access/amortization, lab and GPU hardware |
| Travel | $1.0M | DDD workshop, TA3 bake-offs, connect-a-thon, biannual IV&V reviews, dissemination |
| Other Direct Costs | $7.0M | GPU/cloud compute (TA1 training + TA2 inference), sequencing-as-a-service, storage, licenses, tuition |
| Indirect | $9.0M | Cytognosis 15% de minimis MTDC; Purdue ~57% F&A; commercial overhead reconciled |
| Profit / Fee | $1.5M | Commercial subs ~7–10% on cost base; none for nonprofit/academia |
| **Total (all phases)** | **$50.0M** | Phase I $13.5M; Phase II $15.0M; Phase III $21.5M |
| Resource Sharing (Performer, in-kind) | ~$4.0M | Illumina data + sequencing credits; Cellanome instrument access; cloud compute credits |

Value to the taxpayer: an open, reusable disease model, protocol stack, and validated-lab marketplace; genetically supported targets with a higher probability of clinical success; and a sustainable engine that compounds in value as data accrue.

## 6. REFERENCES CITED: not in the page limit

1. Bunne C, Roohani Y, Rosen Y, et al. How to build the virtual cell with artificial intelligence: priorities and opportunities. Cell. 2024;187(25):7045–7063. doi:10.1016/j.cell.2024.11.015.
2. Zhang J, Squires C, Greenewald K, et al. Identifiability guarantees for causal disentanglement from soft interventions. NeurIPS. 2023. arXiv:2307.06250.
3. Bereket M, Karaletsos T. Modelling cellular perturbations with the sparse additive mechanism shift variational autoencoder. NeurIPS. 2023. arXiv:2311.02794.
4. de la Fuente J, Lehmann R, Ruiz-Arenas C, et al. Interpretable causal representation learning for biological data in the pathway space (SENA-discrepancy-VAE). ICLR. 2025. arXiv:2506.12439.
5. Minikel EV, Painter JL, Dong CC, Nelson MR. Refining the impact of genetic evidence on clinical success. Nature. 2024;629(8012):624–629. doi:10.1038/s41586-024-07316-0.
6. Trubetskoy V, Pardiñas AF, Qi T, et al. Mapping genomic loci implicates genes and synaptic biology in schizophrenia. Nature. 2022;604(7906):502–508. doi:10.1038/s41586-022-04434-5.
7. Ruzicka WB, Mohammadi S, Fullard JF, et al. Single-cell multi-cohort dissection of the schizophrenia transcriptome. Science. 2024;384(6698):eadg5136. doi:10.1126/science.adg5136.
8. Tegtmeyer M, Liyanage D, Han Y, et al. Combining phenomics with transcriptomics reveals cell-type-specific morphological and molecular signatures of the 22q11.2 deletion. Nat Commun. 2025;16(1):6332. doi:10.1038/s41467-025-61547-x.
9. Falaguera MJ, McDonagh EM, Ochoa D, et al. Temporal trends in evidence supporting novel drug target discovery (Open Targets Platform). Nat Commun. 2025;17(1):492. doi:10.1038/s41467-025-67180-y.
10. Emani PS, Liu JJ, Clarke D, et al. Single-cell genomics and regulatory networks for 388 human brains. Science. 2024;384(6698):eadi5199. doi:10.1126/science.adi5199.

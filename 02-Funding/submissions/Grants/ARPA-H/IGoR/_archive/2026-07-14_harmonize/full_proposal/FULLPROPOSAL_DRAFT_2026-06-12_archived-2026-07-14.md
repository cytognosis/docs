# ARPA-H IGoR: Full Proposal (DRAFT content)

**ARPA-H-SOL-26-155. Award instrument: Other Transaction. Period of performance: 60 months (Phase I 18 mo; Phase II 18 mo; Phase III 24 mo).**

> DRAFTING NOTES (delete before submission): Prime/PI base case = Purdue/IPAI (PI: Ananth Grama); Cytognosis = TA1 and TA2 co-leads. C.1 body limit is 40 pages (sections 1–7); Gantt, biosketches, references, TDD, cost, OTA are excluded. The factorized-PRS method is marked PROPRIETARY where it appears. DataTecnica (TA2) is an alternate pending OCI/eligibility clearance; Transfyr (TA3) and SPOC Biosciences declined 2026-06-18 and are not named here.

---

# APPENDIX C.1: TECHNICAL AND MANAGEMENT PROPOSAL

## Cover block
- Proposal Title: A Closed-Loop, Mechanistically Grounded Research Engine for Complex Neuropsychiatric Disease: Schizophrenia to Bipolar Disorder
- Prime: Purdue University, Institute for Physical AI (IPAI). Type: Academia. Award instrument requested: Other Transaction.
- Animal Subjects: No. Human Subjects: No (secondary analysis of existing de-identified data).
- Total Funds Requested (all phases): $50,000,000. Resource sharing (in-kind, Performer): ~$4.0M. Validity period: 120 days.
- Sub-awardees: Cytognosis Foundation; Phylo; SIFT; Cellanome; Illumina; McLean Hospital/HMS.

## 1. PROPOSAL SUMMARY

### A. Overview

**What we are doing.** We are building a complete IGoR team that closes the research loop for complex neuropsychiatric disease. The system has four coupled parts: a mechanistic, multiscale causal disease model (TA1) that treats disease and disease-associated genetic variation as a causal perturbation on cell state; a New Science Engine (TA2) that interrogates the model to find the most valuable knowledge gaps and design experiments to resolve them; a layered, instrument-agnostic protocol stack (TA3); and a validated-laboratory marketplace (TA4) that executes experiments and returns data that updates the model. We focus on schizophrenia in Phases I and II and extend to bipolar disorder, a genetically and biologically related disorder, in Phase III.

**How it improves health outcomes.** Schizophrenia and bipolar disorder are leading causes of disability, and most therapies target symptoms rather than mechanism. By producing non-obvious, experimentally validated mechanisms and candidate targets that carry human genetic support, which roughly doubles to triples the probability of clinical success (Minikel et al., 2024), the engine shortens the path to mechanism-based therapies. Because the model, protocols, and marketplace are released openly, the same infrastructure accelerates discovery across many diseases.

**How it is done today and the limitations.** Today, individual laboratories generate hypotheses constrained by local expertise, run experiments described in insufficient detail, and publish selected results that are difficult to reproduce; up to 89% of preclinical work cannot be fully reproduced. Computational disease modeling is fragmented: foundation models (scGPT, Geneformer, STATE) learn correlational embeddings, perturbation predictors model an experimenter's intervention, and systems-biology networks are single-scale and not experimentally updatable. No platform unifies atlas-scale data, causal perturbation modeling, portable protocols, and validated execution in a self-updating loop.

**What is new and why it will succeed.** Three ideas. First, we invert the virtual-cell paradigm (Bunne et al., 2024): disease genotype acts as a soft intervention on a latent causal model of biological processes, for which identifiability guarantees exist (Zhang et al., 2023). Second, we factorize the genotype-phenotype map into sparse, pathway-disentangled "disease axes" (extending the sparsity-of-shift-mechanism principle of Bereket and Karaletsos, 2023, and the pathway-space causal representation learning of de la Fuente et al., 2025). Third, TA2 designs experiments by value of information against this mechanistic model rather than by literature mining. It will succeed because we close the loop with reproducible cellular experiments that supply the interventional data the causal model needs, and because the team has built the constituent methods and datasets before.

**Emerging trends and why we are superior.** Agentic-science systems (Co-Scientist, Biomni, the Virtual Lab) are advancing rapidly but propose experiments without interrogating a mechanistic disease model; foundation models scale but remain correlational. Our system is grounded in a causal, physically interpretable model and a validated experimental marketplace, exactly the capabilities IGoR states current LLM-to-lab integrations lack.

**Key risks and mitigations.** Technical: cellular models may not represent in-vivo disease (mitigated by joint cellular-clinical alignment and genetic anchoring); cross-lab concordance is hard (calibration layer + IV&V); causal identifiability from observational genomics is non-trivial (closed-loop interventional cellular data). Programmatic: partner and personnel confirmation (named alternates for TA2/TA3; active recruiting for the Software Architect). Translational: targets must be credible to drug developers (genetic-support prioritization).

**Who is affected and the impact.** Tens of millions of people with schizophrenia and bipolar disorder, the researchers who study them, and, through the open marketplace, the broader biomedical community.

**Specific applications.** Target and biomarker discovery for neuropsychiatric disease; a reusable disease-modeling and experiment-design engine; an open protocol stack and validated-lab marketplace usable by any researcher.

**Equitable access, cost, and user experience.** All computational artifacts are open-source under permissive licenses; protocols and marketplace interfaces are designed for any qualified lab, not only well-resourced centers; explainable TA2 narratives keep the human researcher in control.

**Misperception and misuse.** The system augments researchers, it does not replace them, and it makes no consequential commitment without human authorization. We will not conduct human clinical trials. We will mark narrowly scoped proprietary methods and follow NIH genomic-data-sharing policy for any controlled data.

### B. Innovative Claims Table

| ISO reference | Technical challenge | Innovation and evidence | Proposal reference |
|---|---|---|---|
| App. A §4.1.1, pp.5–6 (TA1 mechanistic/multiscale/verifiable) | Disease models are correlational or single-scale and cannot be experimentally updated | Causal, multiscale model with disease genotype as a soft intervention; identifiability guarantees (Zhang 2023); prior single-cell atlas (Ruzicka, Mohammadi 2024) | §4 TA1 |
| App. A §4.1.1 (knowledge gap identification) | Identifying which gaps most advance understanding | Sparse "disease axes" + network coverage map make gaps explicit and rankable | §4 TA1/TA2 interface |
| App. A §4.1.2, p.7 ("not a wrapper around an LLM") | Grounding experiment design in mechanism | Value-of-information design against the TA1 causal model; multi-agent dissent/verification | §4 TA2 |
| App. A §4.1.3, p.9 (eliminate arbitrary procedural variation) | Portable, reproducible protocols | Layered intent/protocol/calibration/hardware stack on LabOP; RFC governance | §4 TA3 |
| App. A §4.1.4, pp.10–11 (validated marketplace, ≥2 labs) | Trustworthy, interoperable execution | Complementary validated labs (Carpenter, Cellanome, Illumina) at ≥90% concordance | §4 TA4 |
| App. A §3, p.4 (Phase III second disease) | Generalization beyond one disease | Schizophrenia → bipolar extension with shared axes | §2, §4 |
| App. C §2.5 (open-source/IP) | Sustainable, open transition | Apache-2.0/MIT/BSD; open marketplace; nonprofit steward | §6 |

## 2. GOALS AND IMPACT

The goal is a validated, openly released research engine that generates non-obvious, experimentally confirmed disease mechanisms and candidate targets for schizophrenia and bipolar disorder at least 10x faster than conventional research. Quantitatively, by Phase III we target: a ≥10x improvement in experimental cycle time against a Phase I baseline; ≥90% inter-laboratory concordance across the marketplace; ≥85% of TA2-proposed experiments rated high-value by an expert panel; a TA1 model spanning ≥15 mechanistic sub-models across ≥3 biological scales with ≤4 h update latency; and validated novel hypotheses in both diseases. The work relates to, and goes beyond, our prior single-cell multi-cohort schizophrenia atlas (Ruzicka, Mohammadi et al., 2024) and the broader virtual-cell and perturbation-modeling literature by adding causal structure, experiment design, and reproducible execution. The lasting impact is infrastructure: a reusable disease model, an open protocol stack, and a validated marketplace that compound in value as data accrue, lowering the barrier to mechanism-based discovery across biomedicine.

## 3. GANTT CHART TIMELINE (excluded from page limit)

A Gantt chart accompanies the proposal showing, across the 60-month period: Phase I (mo 0–18) architecture and walking-skeleton; Phase II (mo 18–36) closed-loop operation and cross-team interoperability; Phase III (mo 36–60) scaling, bipolar extension, and unified marketplace. Program milestones (Domain-Driven Design workshop at kickoff; bake-offs; connect-a-thon) and phase go/no-go gates are marked. (Rendered figure embedded in the submission.)

## 4. TECHNICAL PLAN

The plan is organized by Technical Area; each area states its approach, how it meets the Program-Level and TA-specific IGoR requirements, and measurable milestones tied to the IGoR metric thresholds (App. A Tables 1–2). The task structure mirrors the Task Description Document (Appendix C.2).

### 4.1 TA1: Comprehensive Disease Models (Cytognosis and IPAI)

TA1 builds a modular, mechanistic, multiscale, verifiable model in four pillars.

**Pillar 1: Network priors.** We curate a multiscale interaction network harmonized on the Molecular Interaction ontology, integrating protein-protein, signaling, regulatory, and metabolic edges with cell-type-specific layers from PsychENCODE single-cell regulatory networks (Emani et al., 2024) and depth-corrected co-expression. A coverage map records which processes and edge types are well supported, serving both as a confidence prior and as the driver for TA2 to target under-covered regions.

**Pillar 2: Causal generative modeling.** Each cell state is decomposed into a basal state plus sparse additive mechanism shifts, extending SAMS-VAE (Bereket and Karaletsos, 2023). Disease-associated genetic variation enters as soft interventions with identifiability guarantees (Zhang et al., 2023); pathway-space structure follows the causal representation learning of de la Fuente et al. (2025). We replace conditionally independent decoders with covariance-preserving decoders so reconstructed cells retain real gene-gene dependence. Gene identity is grounded in regulatory-network topology using a spectral, co-expression-aware positional encoding with adaptive repositioning developed by our team (manuscript under review, 2026), which captures perturbation-induced functional rewiring. For intervention design we adopt a graph neural network over the interaction network that proposes perturbations shifting a diseased state toward a healthy target and predicts responses (PDGrapher; Gonzalez et al., 2025).

> PROPRIETARY (TA1, Pillar 2b): We additionally factorize patient-level genetic variation into sparse, pathway-disentangled, transdiagnostic axes that double as candidate biotypes. The detailed factorization method is proprietary; novelty is claimed precisely against pathway-partitioned PRS as the nearest precedent. This subsection is marked proprietary on all affected pages.

**Pillar 3: Joint cellular and clinical shift space.** Every signal, cellular or clinical, is represented as a shift in pathway space relative to a matched control, which lets us aggregate induced (cellular) and natural (clinical) evidence in one model and surface disease axes consistent across scales and robust to model-system artifacts.

**Pillar 4: Ontology-conditioned experiment design.** We condition predictions on disease (MONDO), cell type (Cell Ontology), tissue (UBERON), and process (Gene Ontology) ontologies, and express hypotheses in a fixed template ("perturbing process X shifts disease Y toward healthy by modulating Z"). We select hub nodes whose perturbation modulates the most downstream biology in a disease-enriched process as the highest-value experiments, handing these to TA2.

Data sources: PGC schizophrenia GWAS (Trubetskoy et al., 2022) and rare-variant data; PsychENCODE single-cell (Emani et al., 2024); our multi-cohort atlas (Ruzicka, Mohammadi et al., 2024); Open Targets (Falaguera et al., 2025); a PubMed knowledge graph for literature grounding.

TA1 milestones. Phase I: architecture (languages, schemas, ontologies) documented; ≥3 mechanistic sub-models; ≥3 quantitative knowledge gaps algorithmically detected; ingest ≥1 TA4 data return; cycle-time baseline. Phase II: automatic updates from ≥10 data returns; ≥10 sub-models across ≥2 scales; ≥1 novel prediction confirmed via TA4; update latency ≤24 h. Phase III: ≥15 sub-models across ≥3 scales; extension to bipolar with novel validated hypotheses in both diseases; latency ≤4 h; all models deposited open-access in certified executable form.

### 4.2 TA2: New Science Engine (Cytognosis + Phylo + IPAI)

TA2 treats the TA1 model as a first-class queryable object. It identifies unconstrained parameters, hypothetical edges, and inconsistent predictions, then proposes the experiment with the highest value of information. The architecture has three components: a tournament of competing causal-link hypotheses with adversarial critics grounded in mechanistic constraints; mechanistic-model-grounded retrieval-augmented planning whose retrieval corpus is the structured output of TA1, not literature alone; and test-time validation in which lightweight simulations pre-screen hypotheses. This is explicitly not a wrapper around a frontier language model: it demonstrates mechanistic grounding via TA1, multimodal design via TA3, and distributed execution via TA4. The system is built on open, swappable scaffolding (stateful agent graphs, multi-agent debate, explainable critique traces, and tool access via open biomedical tool registries) so future models can be incorporated without re-engineering, and it explains its reasoning through narratives and visualizations so the researcher directs the work. Consequential actions require human authorization. Phylo (creator of Biomni) co-leads agentic design with Cytognosis and IPAI.

TA2 milestones. Phase I: orchestration architecture documented; interfaces to TA1 and TA3 demonstrated; ≥3 experiments proposed and executed; ≥50% rated high-value by experts. Phase II: ≥2 model backends including ≥1 open-weight; usability study with ≥10 domain scientists, ≥70% useful; ≥75% high-value; designs lead to measurable TA1 improvement. Phase III: ≥85% high-value; demonstrated on bipolar; design efficiency quantified against a conventional baseline; ≥20 researchers including external users, ≥80% useful.

### 4.3 TA3: Interoperable Experimental Procedures (SIFT lead)

TA3 defines a layered protocol stack on the LabOP lineage with four abstraction layers: intent (declarative scientific question and quality requirements), protocol (standard processes with error handling), calibration (parameters and uncertainty standardized across devices, with IV&V calibration artifacts), and hardware (machine-specific settings isolated behind common interfaces). A central goal is to eliminate procedural variation with weak scientific justification; changes to locked parameters go through a Request-for-Comments process. The stack supports at least four modalities (live-cell imaging, optical/morphological screening, sequencing-based assays, and functional assays) and encodes rich metadata (cell lines, reagents, calibration status, QC, power analyses, uncertainty). SIFT (developers of LabOP) leads, engaging equipment makers and standards bodies and participating in program bake-offs.

TA3 milestones. Phase I: protocol schema and calibration artifacts defined; same protocol run at two team labs with comparable outcomes on ≥1 experiment; ≥2 modalities. Phase II: RFC process operational with ≥2 RFCs; protocols run at ≥3 labs including ≥1 cross-team, each executing ≥3 experiments to predefined reproducibility thresholds; ≥3 modalities. Phase III: open data and metadata layer delivered; engagement with ≥1 external standards body or manufacturer; protocols run at ≥5 labs across teams; ≥4 modalities; connect-a-thon interoperability demonstrated.

### 4.4 TA4: Experiment Marketplace (Carpenter, Cellanome, Illumina; ≥2 labs)

TA4 establishes a network of validated laboratories that execute TA3 protocols and return model-ready data. The team has two experimental arms: **Matt Tegtmeyer's lab (Purdue, TA4.1 academic arm)** runs all wet-lab experiments (iPSC-neuron disease models and multi-modal readouts via Element AVITI24 / Teton CytoProfiling), and **Cellanome (TA4.1 industry arm)** contributes live-cell imaging with same-cell pooled CRISPR sequencing on the R3200. **Anne Carpenter (IPAI/Purdue)** provides the computational morphology and imaging models as the common analysis layer across both arms (no wet bench). **Illumina (TA4.2)** contributes high-throughput sequencing, DRAGEN processing, and the Billion Cell Atlas perturbation resource, partly as in-kind resource sharing. Labs define and validate cell lines and reference materials, develop QC parameters, demonstrate cross-laboratory concordance, and progressively automate exception handling. The Phase I anchor is paired isogenic iPSC lines carrying a 22q11.2-region lesion, CRISPR-corrected to a matched control and differentiated to neurons; the morphological and molecular signatures of the 22q11.2 deletion are experimentally established (Tegtmeyer et al., 2025).

TA4 milestones. Phase I: ≥1 cell line and instrument validated on IV&V artifacts at each of two labs; intra-team reproducibility with same experiment at both labs at ≥85% concordance; two-way capability communication. Phase II: ≥2 additional instruments validated per lab; marketplace request/return interface; cross-team execution at ≥85% concordance; exceptions per experiment reduced ≥50% versus Phase I. Phase III: unified marketplace across teams; experiments ordered and executed across teams; ≥90% concordance; ≥70% of exceptions handled autonomously; connect-a-thon completed.

### 4.5 Program-level integration and disease strategy

Interfaces follow a high-cohesion, low-coupling design; we participate in the kickoff Domain-Driven Design workshop, bake-offs, the RFC process, and the Phase III connect-a-thon, and we collaborate with the IV&V partner (containerization, documentation, materials transfer, biannual reviews) without budgeting for them. Disease strategy: schizophrenia is the Phase I–II disease, anchored at the cellular scale by the 22q11.2 deletion model and at the population scale by PGC genetics and the PsychENCODE/our multi-cohort atlas; bipolar disorder is the related Phase III extension, which shares genetic architecture and cellular biology, allowing the same disease axes and protocols to transfer.

## 5. RISK MITIGATION, CONTINGENCY, AND ALTERNATIVE APPROACHES

| Risk | Type | Mitigation / contingency | Alternative considered |
|---|---|---|---|
| Cellular model not representative of in-vivo disease | Technical | Joint cellular-clinical shift space; genetic anchoring; multiple cell types | In-vitro-only optimization (rejected: cannot separate artifacts) |
| Causal identifiability from observational genomics | Technical | Closed-loop interventional cellular data; identifiability theory (Zhang 2023) | Correlational FM only (rejected: not mechanistic) |
| Cross-lab concordance below threshold | Technical | Calibration layer; reference materials; IV&V artifacts; RFC governance | Single-lab execution (rejected: violates marketplace goal) |
| TA1/TA2 boundary for gap identification unclear | Programmatic | Co-design at DDD workshop; explicit coverage map; iterate interface | Monolithic design (rejected: low cohesion) |
| Partner or personnel not confirmed (TA2 optional add-on; final Architect confirmation) | Programmatic | SIFT confirmed as TA3 lead; Elham confirmed tentatively as Software/Systems Architect; Patricia Purcell confirmed as PM; DataTecnica (TA2) pending OCI/eligibility clearance | Sole-source dependence (rejected) |
| OCI / eligibility (former ARPA-H affiliation; federal-contractor status) | Compliance | Counsel-led OCI review; exclude unclear parties from the base team | Include without clearance (rejected) |
| LLM hallucination in TA2 | Technical | Mechanistic grounding; verification agents; human authorization of consequential actions | LLM-only design (rejected, and excluded by IGoR) |

## 6. COMMERCIALIZATION STRATEGY NARRATIVE (≤3 pages)

IGoR components reach sustained use through an open-core model stewarded by a nonprofit. All software and data are released under permissive open-source licenses (Apache-2.0, MIT, or BSD), which maximizes adoption and aligns with ARPA-H's open-source preference; narrowly scoped proprietary methods (the factorized-PRS axis method) are kept in an extensible proprietary namespace, which TA3 explicitly permits. Three transition paths sustain the work beyond the program: a public-private partnership or cloud-lab provider operating the experiment marketplace as a continuing service; an academic-consortium or NIH-center home for the open disease model and protocol standards; and milestone-based funding from philanthropies, agencies, and patient organizations that invest in defined disease-understanding milestones. Cytognosis, as a 501(c)(3), can steward the open assets while a public-benefit pathway commercializes services without compromising openness. Throughout, we will demonstrate proof of concept by integrating IGoR technologies into realistic research workflows with external users in Phase III.

## 7. CAPABILITIES / MANAGEMENT PLAN (≤2 pages)

The team is one integrated performer under a single PI. IPAI/Purdue (prime) leads integration, program management, and software architecture and supports TA1/TA2; Cytognosis leads TA1 and co-leads TA2; Phylo co-leads TA2 (optional); SIFT leads TA3 (Daniel Bryce lead, Robert Goldman advisory); Tegtmeyer (academic arm) and Cellanome (industry arm) constitute TA4.1; Illumina is TA4.2; Anne Carpenter (IPAI/Purdue) provides computational morphology and imaging models across TA4 arms (no wet bench); McLean/HMS provides clinical grounding. Required roles are filled distinctly: Principal Investigator (Ananth Grama, IPAI), Project Manager (Patricia Purcell, confirmed), and Software and Systems Architect (Elham Jebalbarezi Sarbijan, IPAI/Purdue, tentative), the last with architectural authority over interfaces and experience building API-first open-source systems and explicitly distinct from the PI and PM. We manage with a living interface specification from the Domain-Driven Design workshop, milestone-based delivery tracking, dependency management across organizations, and Associate Performer Agreements to enable cross-team information exchange by Phase III. Cross-team integration leads and their annual hours are identified in the management plan and cross-walked to the cost proposal.

## 8. BIOGRAPHICAL INFORMATION (excluded from page limit)

NIH-format biosketches are provided for: Ananth Grama (PI; computational systems, HPC, data science); Shahin Mohammadi (TA1 and TA2 co-leads; computational biology, single-cell genomics, perturbation modeling; co-first author, schizophrenia single-cell atlas); Matthew Tegtmeyer (TA4.1 academic arm; iPSC-neuron disease models, multi-modal readouts); Anne Carpenter (computational morphology and imaging models, IPAI/Purdue; Cell Painting, image-based profiling); Daniel Bryce and Robert Goldman (TA3; LabOP, automated planning); Dwight Baker (TA4.1 industry arm, Cellanome; single-cell platforms); Kexin Huang (TA2 optional add-on; agentic biomedical AI, Biomni); W. Brad Ruzicka (clinical co-lead; psychiatric neuroscience). (Full biosketches appended.)

## 9. REFERENCES CITED (excluded from page limit)

See consolidated reference list at the end of this document.

---

# APPENDIX C.2: TASK DESCRIPTION DOCUMENT (TDD)

**General objective.** Build and validate a closed-loop research engine (TA1–TA4) for schizophrenia, extended to bipolar disorder in Phase III. Tasks are organized by Phase and Technical Area; milestones are quantitative and cross-walked to the Cost Proposal. Human/animal subjects: none (cell/tissue culture and existing de-identified data).

## PHASE I (Months 0–18): Concept and Component Development

**1.1.0 TA1: Disease model architecture.** Objective: establish languages, schemas, ontologies, and the causal generative core. Approach: Pillars 1–2 above; ingest existing atlases and the 22q11.2 cellular data. Location: Cytognosis (CA), IPAI (IN). Responsible: Cytognosis. Deliverables: architecture document; ≥3 mechanistic sub-models; algorithmic detection of ≥3 quantitative knowledge gaps; containerized artifacts for IV&V (Unlimited Rights except the proprietary axis method). Milestones: (1) architecture documented; (2) ≥3 sub-models built; (3) ≥3 gaps detected; (4) ≥1 TA4 data return ingested.

**1.2.0 TA2: Orchestration core.** Objective: gap-to-experiment design grounded in TA1. Approach: hypothesis tournament + mechanistic RAP + value-of-information selection. Location: Cytognosis, Phylo (CA), IPAI. Responsible: Cytognosis/Phylo. Deliverables: orchestration architecture; ≥3 proposed experiments with explainable narratives. Milestone: ≥50% of proposed experiments rated high-value by an expert panel.

**1.3.0 TA3: Protocol schema v1.** Objective: layered protocol stack and calibration artifacts. Approach: LabOP-based intent/protocol/calibration/hardware layers. Location: SIFT. Responsible: SIFT. Deliverables: protocol schema; calibration artifacts; ≥2 modalities. Milestone: same protocol executed at two team labs with comparable outcomes on ≥1 experiment.

**1.4.0 TA4: Intra-team validation.** Objective: validate cell lines/instruments and demonstrate reproducibility. Approach: 22q11.2 isogenic iPSC-neuron anchor; morphological, live-cell, transcriptomic readouts. Location: Tegtmeyer lab (Purdue/IPAI), Cellanome (CA). Responsible: Tegtmeyer, Cellanome; Carpenter contributes computational morphology models. Deliverables: workflow summary table; validated cell line + instrument at each of two labs. Milestone: same experiment at both labs at ≥80% concordance.

**1.5.0 Program: Integration.** Objective: shared interfaces and walking-skeleton loop. Approach: Domain-Driven Design workshop; containerization for IV&V. Location: all. Responsible: IPAI (prime). Deliverables: shared interface specification; walking-skeleton demonstration (TA2→TA3→TA4→TA1). Milestone: closed-loop cycle demonstrated within the team; 100% of TA1 artifacts build/execute on the IV&V environment.

## PHASE II (Months 18–36): Integration and Interoperability

**2.1.0 TA1: Auto-updating model.** Deliverables: automatic updates from ≥10 data returns; ≥10 sub-models across ≥2 scales; model cards. Milestones: ≥1 novel prediction experimentally confirmed; update latency ≤24 h; statistically significant improvement over a literature-only model.

**2.2.0 TA2: Backends and usability.** Deliverables: ≥2 model backends (≥1 open-weight); usability study (≥10 scientists). Milestones: ≥75% high-value; ≥70% rate the system useful.

**2.3.0 TA3: RFC and cross-team.** Deliverables: RFC process; ≥2 RFCs; ≥3 modalities. Milestone: protocols run at ≥3 labs (incl. ≥1 cross-team), each executing ≥3 experiments to reproducibility thresholds.

**2.4.0 TA4: Cross-team execution.** Deliverables: marketplace request/return interface; multicellular systems. Milestones: cross-team experiment at ≥90% concordance across ≥3 experiments; exceptions reduced ≥50% vs Phase I.

**2.5.0 Program: Interoperability.** Milestone: ≥1 successful cross-team interoperability test; cycle time ≥4x faster than baseline.

## PHASE III (Months 36–60): Scaling, Generalization, Transition

**3.1.0 TA1: Second disease.** Deliverables: bipolar extension; ≥15 sub-models across ≥3 scales; open-access deposit in certified executable form. Milestones: novel validated hypotheses in both diseases; latency ≤4 h; ≥2x prediction improvement over Phase I.

**3.2.0 TA2: Generalization.** Milestones: ≥85% high-value; demonstrated on bipolar; ≥20 researchers (incl. external), ≥80% useful; design efficiency quantified vs conventional baseline.

**3.3.0 TA3: Open standards.** Deliverables: open data/metadata layer; engagement with ≥1 external standards body/manufacturer; ≥4 modalities; ≥5 labs across teams. Milestone: connect-a-thon interoperability.

**3.4.0 TA4: Unified marketplace.** Deliverables: onboarding documentation; public capability manifests. Milestones: ≥90% concordance across marketplace; ≥70% exceptions autonomous; experiments ordered/executed across teams.

**3.5.0 Program: Transition.** Deliverables: transition plan; ≥1 sustained partnership or adoption path; all artifacts open-access certified. Milestone: external researchers use IGoR end-to-end; ≥10x cycle-time improvement.

---

# APPENDIX C.3: PRICE PROPOSAL (narrative)

**Cover.** Total price (all phases, inclusive of resource sharing): $50,000,000 ARPA-H + ~$4,000,000 Performer in-kind. Phase I: $13.5M. Phase II: $15.0M. Phase III: $21.5M. Government: $50.0M; Performer (in-kind): ~$4.0M.

**1. Level of Effort and Labor.** ~14 funded FTE/year at steady state across seven organizations, rising with experimentation in Phase III. Key labor categories with 2026 fully burdened rates: senior ML/AI engineer ~$260K; ML research scientist ~$240K; software architect ~$250K; computational biologist ~$210K; research scientist/postdoc ~$120–130K; technical project manager ~$200K; academic postdoc ~$70K + F&A; PhD student ~$50K stipend + tuition. Total direct labor ~$22.0M over ~147,000 hours. Cytognosis carries ~7.5 FTE at steady state (PI 0.5; software architect 1.0; senior ML engineer 1.0; ML research scientist 1.0; computational biologists 2.0; technical PM 1.0; research scientist 1.0).

**2. Equipment Purchases (~$2.5M).** Imaging and instrument access/amortization (including Cellanome R3200 time), laboratory equipment, and GPU hardware. Items exceeding $10,000 will be supported by vendor quotes, catalog prices, or prior purchase orders at full-proposal finalization.

**3. Travel (~$1.0M).** Domain-Driven Design workshop (kickoff), TA3 bake-offs, Phase III connect-a-thon, biannual IV&V reviews, and dissemination. Each trip is justified against a specific task or milestone.

**4. Other Direct Costs (~$7.0M).** GPU/cloud compute for TA1 training (~$250–400K/yr) and TA2 agentic inference (~$150–250K/yr) at a blended H100 rate of ~$2.50–3.00/GPU-hour; sequencing-as-a-service and wet-lab reagents (iPSC/NGN2 differentiation $3–15K/run; targeted Perturb-seq $5–30K, genome-scale $50–300K; Cell Painting screens $50–500K; multiplexed scRNA-seq $200–700/sample); data storage; software/API licenses; graduate tuition. Materials are budgeted separately (~$6.0M).

**5. Resource Sharing (~$4.0M, in-kind).** Illumina Billion Cell Atlas data access and sequencing credits; Cellanome discounted instrument access; cloud compute research credits; leverage of open JUMP Cell Painting reference data. Government and Performer shares sum to the total project value (~$54.0M).

Indirect: Cytognosis 15% de minimis on MTDC (2 CFR 200.414(f)); Purdue ~57% on-campus F&A; commercial subs' overhead embedded in loaded rates plus fee ~7–10%. Rates finalized at OT negotiation. The Appendix C.4 cost workbook provides per-organization, per-phase detail; the Appendix E draft OT agreement will be submitted with counsel redlines.

---

# CONSOLIDATED REFERENCES

1. Bunne C, Roohani Y, Rosen Y, et al. How to build the virtual cell with artificial intelligence: priorities and opportunities. Cell. 2024;187(25):7045–7063. doi:10.1016/j.cell.2024.11.015.
2. Zhang J, Squires C, Greenewald K, Srivastava A, Shanmugam K, Uhler C. Identifiability guarantees for causal disentanglement from soft interventions. NeurIPS. 2023. arXiv:2307.06250.
3. Bereket M, Karaletsos T. Modelling cellular perturbations with the sparse additive mechanism shift variational autoencoder (SAMS-VAE). NeurIPS. 2023. arXiv:2311.02794.
4. de la Fuente J, Lehmann R, Ruiz-Arenas C, et al. Interpretable causal representation learning for biological data in the pathway space (SENA-discrepancy-VAE). ICLR. 2025. arXiv:2506.12439.
5. Lopez R, Tagasovska N, Ra S, Cho K, Pritchard JK, Regev A. Learning causal representations of single cells via sparse mechanism shift modeling (sVAE+). CLeaR. 2023. arXiv:2211.03553.
6. Gonzalez G, Lin X, Herath I, Veselkov K, Bronstein M, Zitnik M. Combinatorial prediction of therapeutic perturbations using causally inspired neural networks (PDGrapher). Nat Biomed Eng. 2025. doi:10.1038/s41551-025-01481-x.
7. Minikel EV, Painter JL, Dong CC, Nelson MR. Refining the impact of genetic evidence on clinical success. Nature. 2024;629(8012):624–629. doi:10.1038/s41586-024-07316-0.
8. Nelson MR, Tipney H, Painter JL, et al. The support of human genetic evidence for approved drug indications. Nat Genet. 2015;47(8):856–860. doi:10.1038/ng.3314.
9. Trubetskoy V, Pardiñas AF, Qi T, et al. Mapping genomic loci implicates genes and synaptic biology in schizophrenia. Nature. 2022;604(7906):502–508. doi:10.1038/s41586-022-04434-5.
10. Singh T, Poterba T, Curtis D, et al. Rare coding variants in ten genes confer substantial risk for schizophrenia (SCHEMA). Nature. 2022;604(7906):509–516. doi:10.1038/s41586-022-04556-w.
11. Ruzicka WB, Mohammadi S, Fullard JF, et al. Single-cell multi-cohort dissection of the schizophrenia transcriptome. Science. 2024;384(6698):eadg5136. doi:10.1126/science.adg5136.
12. Emani PS, Liu JJ, Clarke D, et al. Single-cell genomics and regulatory networks for 388 human brains. Science. 2024;384(6698):eadi5199. doi:10.1126/science.adi5199.
13. Tegtmeyer M, Liyanage D, Han Y, et al. Combining phenomics with transcriptomics reveals cell-type-specific morphological and molecular signatures of the 22q11.2 deletion. Nat Commun. 2025;16(1):6332. doi:10.1038/s41467-025-61547-x.
14. Falaguera MJ, McDonagh EM, Ochoa D, et al. Temporal trends in evidence supporting novel drug target discovery (Open Targets Platform). Nat Commun. 2025;17(1):492. doi:10.1038/s41467-025-67180-y.
15. Ochoa D, Hercules A, Carmona M, et al. The next-generation Open Targets Platform. Nucleic Acids Res. 2023;51(D1):D1353–D1359. doi:10.1093/nar/gkac1046.
16. Mountjoy E, Schmidt EM, Carmona M, et al. An open approach to systematically prioritize causal variants and genes at GWAS loci (Locus-to-Gene). Nat Genet. 2021;53:1527–1533. doi:10.1038/s41588-021-00945-5.
17. Xu J, Yu C, Xu J, et al. PubMed knowledge graph 2.0: connecting papers, patents, and clinical trials in biomedical science. Sci Data. 2025;12:1018. doi:10.1038/s41597-025-05343-8.
18. ARPA-H. Intelligent Generator of Research (IGoR) Innovative Solutions Opening, ARPA-H-SOL-26-155. 2026.

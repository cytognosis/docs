# AWS Imagine Grant 2026: Round One Application

Application Link: https://aws.amazon.com/government-education/nonprofits/aws-imagine-grant-program/
Application Portal: https://apply.younoodle.com/showcase/competition/2026_aws_imagine_grant

**Category:** Go Further, Faster
**Organization:** Cytognosis Foundation, Inc. (501(c)(3), Delaware)
**Project:** Psychoverse / Cytoverse-Neuro v1.0, the open Map: Phenotype-Aligned Genomic Foundation Embeddings for Transdiagnostic Neuropsychiatric Variation

This grant funds the Cytoverse / Cytoverse-Neuro layer, the open molecular and foundation-model neuropsychiatric Map of Cytognosis Foundation's GPS for Health platform. It does not fund the consumer application. Psychoverse / Cytoverse v1.0 is the first public release of that open Map.

---

## Organizational information (Q1–Q13)

| # | Field | Answer |
|---|---|---|
| 1 | Full registered organization name | Cytognosis Foundation, Inc. |
| 2 | Tax ID (EIN) | 39-4383634 |
| 3 | Website URL | https://www.cytognosis.org |
| 4 | Organization full address | 394 Innisfree Dr, Daly City, CA 94015 (founder's residence; no separate office). |
| 5 | Annual organizational revenue (FY2025) | Less than $50,000 |
| 6 | Annual IT budget (FY2025) | Less than $10,000 |
| 7 | Proposal contact | Shahin Mohammadi, PhD, Founder, President and CEO, mohammadi@cytognosis.org, (765) 409-1883 |
| 8 | Project lead | Shahin Mohammadi, PhD, Founder, President and CEO, mohammadi@cytognosis.org, (765) 409-1883 |
| 9 | Project lead role | President or CEO |
| 10 | Project lead functional area | Leadership or overall management |
| 11 | Primary mission area | Science, Technology, and Social Science |
| 12 | AWS account? | Yes. AWS account "cytognosis" (Account ID 630287362866) is active under root email mohammadi@cytognosis.org, with the standard $100 activation credit. |
| 13 | Applied for Imagine Grant before? | No |

---

## Project information (Q14–Q28)

### Q14: Project overview (75 words)

Psychoverse / Cytoverse-Neuro v1.0 builds an open, phenotype-aligned genomic embedding model for transdiagnostic neuropsychiatric variation. It is the open Map layer of Cytognosis Foundation's GPS for Health platform. We fine-tune AlphaGenome on paired single-cell brain data from 388 donors, learn a sparse interpretable phenotype representation, and align the two into a coordinate system anchored to clinical reality. The result is free, open-weight software and a public HIPAA-eligible inference API, hosted on Amazon SageMaker.

*Word count: 73*

---

### Q15: Award category

Go Further, Faster

---

### Q17 and Q18: N/A (Go Further, Faster applicant)

Q17 ("How is your organization using data to make decisions today?") and Q18 ("What type of AI services will you integrate into your project?") are designated for Pathfinder applicants only per the 2026 AWS Imagine Grant guidelines. This application is submitted under the Go Further, Faster award category (Q15). These questions do not appear on the Go Further, Faster submission form, so they are intentionally omitted. The question numbering below (Q16 followed by Q19) is correct for the Go Further, Faster form.

For completeness, if a reviewer requests equivalent context: Cytognosis Foundation today makes decisions from published single-cell and genomic cohort data (PsychENCODE, ROSMAP, PsychAD) analyzed with the PI's open-source ACTIONet framework, and the AI services this project integrates are Amazon SageMaker (training and HIPAA-eligible inference), AWS HealthOmics (genomic data workflows), and a scoped follow-on evaluation of Amazon Bedrock for a later clinical agent layer.

---

### Q16: Project description and mission relation (350 words)

Cytognosis Foundation exists to detect and intercept disease years before symptoms. Psychiatry is the most painful expression of medicine's reactive paradigm: first-line treatments fail 47 to 58 percent of patients, relapse rates run 40 to 71 percent, and the underlying biology is collapsed into binary diagnostic labels that ignore continuous molecular variation. Psychoverse, also designated Cytoverse-Neuro, is the open Map layer of Cytognosis Foundation's GPS for Health platform and serves as the neuropsychiatric coordinate-system foundation model. This grant funds that open Map, not the consumer application. This project builds its first public release, Psychoverse / Cytoverse v1.0. Our principal investigator co-led the first multi-cohort single-cell atlas of schizophrenia (Ruzicka, Mohammadi et al., *Science* 2024), establishing that continuous biological axes exist within one DSM diagnosis. v1.0 turns that result into reusable open infrastructure.

The project executes in three phases over nine months. Phase 1 (cell-type-aware genomic fine-tuning) fine-tunes AlphaGenome-PyTorch using low-rank adaptation (LoRA) on the PsychENCODE 388-donor cohort, which provides matched whole-genome sequencing with single-nucleus RNA-seq and ATAC-seq from the same brains. Training signals are pseudobulked snRNA and snATAC BigWig profiles per individual at iteratively finer cell-type resolutions, teaching the model brain cell-type-specific regulatory context.

Phase 2 (sparse interpretable phenotype embedding) trains a sparse autoencoder on NeuroBioBank harmonized neuro-behavioral phenotypic data, jointly optimizing reconstruction and disease-label prediction to learn a compressed, interpretable representation of symptom manifestations across the cohort. PsychENCODE phenotypes serve as held-out cross-cohort validation.

Phase 3 (phenotype-aligned coordinate system) pools Phase 1 embeddings per gene, applies a multi-resolution graph-wavelet graph neural network (GNN) over curated gene functional networks, and then uses Manifold-approximated Kernel Alignment (MKA) to align the genomic kernel against the phenotypic kernel. The result is an interpretable, phenotype-aligned set of axes onto which any individual can be projected.

Every artifact ships under Apache 2.0 (code, model weights, LoRA adapters) and CC BY 4.0 (documentation, model cards, benchmarks). We host a public HIPAA-eligible inference API on AWS so researchers, clinicians, and patient-advocacy partners can project new individuals without local compute. The mission link is direct: replace categorical psychiatric labels with biology-anchored coordinates everyone can access for free.

*Word count: 349*

---

### Q19: Intended outcomes and new capabilities unlocked (350 words)

By month nine, we will release Psychoverse v1.0: an open-weights, phenotype-aligned genomic embedding model trained on PsychENCODE and NeuroBioBank, paired with a free public inference API hosted on AWS HIPAA-eligible infrastructure, complete documentation, ancestry-disaggregated demographic performance cards, and a published threat model from an external security audit.

Three new capabilities flow from this release.

**Continuous, biology-anchored psychiatric coordinates.** Today a clinician working with a person carrying a schizophrenia diagnosis has access to a binary label and a symptom score. Psychoverse v1.0 lets the same clinician project that person's genome and phenotypes into an interpretable, multi-axis coordinate space where adjacent individuals reflect biologically similar regulatory architecture rather than identical checklist scores. This is the precondition for moving beyond one-size-fits-all psychiatric care.

**Cell-type regulatory inference at the individual level.** Phase 1's fine-tuning produces the first AlphaGenome derivative that has seen single-cell brain regulatory data at scale. Researchers studying any neuropsychiatric condition can use it to ask which cell types contribute to a given variant's effect, an inference that today's pretrained genomic foundation models cannot reliably make in brain tissue. This capability unlocks downstream applications in target discovery, treatment-response modeling, and clinical trial enrichment.

**A reusable open scaffold for cross-cohort, cross-modality alignment.** The MKA-based alignment protocol in Phase 3 is general. Any future Cytognosis cohort, any external collaborator with paired molecular and phenotypic data, and any patient-advocacy partner running a pilot can project their cohort into the same coordinate space without retraining from scratch. The architecture deliberately turns one cohort's effort into shared community infrastructure.

For Cytognosis Foundation, this is our first organizational AWS-native deliverable. Operationally, it establishes HIPAA-eligible cloud infrastructure, a published threat model, an ML-ops baseline using Amazon SageMaker, AWS HealthOmics, and AWS Audit Manager, and an inference-serving capability that future Cytognosis releases can build on directly. It also stands up our first publicly accessible API, which we expect adopting organizations to integrate into clinical research pipelines within six months of release.

Milestones: Phase 1 complete at month 3 (LoRA adapters released); Phase 2 at month 5 (autoencoder released); Phase 3 and full v1.0 release at month 9 (coordinate system, API, documentation, threat model).

*Word count: 329*

---

### Q20: What is driving the need? Why now? (350 words)

Three convergent forces make the next 12 months the right window.

**The scientific foundation just became available.** AlphaGenome was released by Google DeepMind in 2025 as a state-of-the-art DNA foundation model, and the PyTorch port shipped with first-class fine-tuning interfaces including LoRA in early 2026. Independently, PsychENCODE released the 388-donor paired single-cell plus whole-genome sequencing capstone in *Science* 2024. Grotzinger et al. (*Nature*, 2025; DOI: 10.1038/s41586-025-09820-3) demonstrated that 66 percent of psychiatric genetic variance compresses into a five-factor structure across 14 disorders. Each of these components is necessary; together they make Psychoverse tractable in a way that was not possible 18 months ago.

**The clinical baseline failure is now load-bearing.** Mental disorders are the leading cause of global years lived with disability (17.3 percent of all-cause health loss; 1.17 billion prevalent cases; GBD 2023 Mental Disorders Collaborators, *Lancet* 2026). U.S. first-line psychiatric treatment failure runs 47 to 58 percent, and the annual cost of suboptimal care is estimated at $528 billion. The April 2026 U.S. White House Executive Order on Accelerating Medical Treatments for Serious Mental Illness explicitly opens regulatory pathways for AI-assisted clinical tools. Demand-side urgency is at an all-time high.

**The infrastructure choice locks in for the field.** Within 18 months, either an open public-good coordinate system will serve as the de facto reference layer that downstream tools build on, or proprietary alternatives will entrench inside closed clinical pipelines, locking out the open scientific community. Cytognosis Foundation is uniquely positioned to ship the open version: our principal investigator co-led the foundational *Science* and *Nature* atlases the model trains on, our Co-Lead at McLean Hospital is the NeuroBioBank liaison, and our senior advisor at Purdue's Institute for Physical Artificial Intelligence provides the foundation-model architecture review.

AWS Imagine accelerates this timeline by 9 to 12 months compared with waiting on a larger NIH or ARPA-H award cycle. The AWS Promotional Credit ($100K) directly covers the compute-intensive AlphaGenome fine-tuning on Amazon EC2 P5 instances and SageMaker training jobs, while the cash award ($150K) covers personnel and data access. Speed here determines whether the open coordinate system or a proprietary one becomes the field's reference.

*Word count: 340*

---

### Q21: Project stage

**Under development.** Architecture and scientific design are complete; key datasets (PsychENCODE, NeuroBioBank) are accessible through established data-use agreements; and early AWS infrastructure scoping is underway. The engineering hire and formal HIPAA-eligible AWS account provisioning are the remaining unlocks.

---

### Q22: Best alignment

**(g) Inform better decision making by aggregating disparate data sources and applying analytics (visualization, AI/ML).**

Psychoverse v1.0 aggregates paired genomic and phenotypic data from two independent cohorts (PsychENCODE and NeuroBioBank), applies multi-modal deep learning to align them, and delivers an analytics layer (an interpretable coordinate system plus public inference API) that researchers and clinicians can use to place individuals in biologically meaningful psychiatric space.

---

### Q23: Long-term support, stakeholders, partners, and other funding (250 words)

**Stakeholders and partners.** Co-Lead Brad Ruzicka, MD/PhD (McLean Hospital / Harvard Medical School), is co-first author with the PI on the single-cell schizophrenia atlas (Ruzicka, Mohammadi et al., Science 2024), Assistant Professor at Harvard Medical School, and the Harvard Brain Tissue Resource Center / NeuroBioBank liaison; he anchors clinical validation, the IRB pathway, and clinical ground truth. Senior Scientific Advisor Ananth Grama (Purdue Institute for Physical Artificial Intelligence) reviews foundation-model architecture and scalable computing. Patient-advocacy distribution partners include One Mind (transdiagnostic), the American Psychiatric Association Council on Digital Health, the Center for Digital Mental Health at Harvard/MGH, and the American Society of Addiction Medicine.

**Other funding (pending, not awarded).** Parallel applications are pending for adjacent, non-duplicative scopes: ARPA-H Health Science Futures (HSF) submission (clinical-scale validation, decision pending); Coefficient Giving Capacity Building ($150K, open-source defensive AI infrastructure, pending); Coefficient Giving Career Development and Transition ($165K, individual PI payroll, pending); and EA Funds Long-Term Future Fund (approximately $120K to $130K, edge AI and safety research, pending). The PI compensation line in this AWS budget covers 50 percent effort for the AWS-hosted genomic-phenotype alignment workload, which no other pending application funds.

**Long-term sustainability.** Psychoverse v1.0 anchors two follow-on submissions planned for Q1 2027: an NSF Technology, Translation, and Innovation award for open-science infrastructure in precision psychiatry, and an ARPA-H Proactive Health Office submission for clinical-scale validation. The open-core model is central to sustainability: Apache 2.0 and CC BY 4.0 licensing keep the inference API and model weights free indefinitely. A planned for-profit arm will manufacture the Psychoscope biosensor and generate revenue through device sales and subscriptions, comparable to OpenBCI's open-core structure. Clinical data and models remain owned by Cytognosis Foundation; intellectual property is licensed to the for-profit arm (the M42 bifurcation structure). Psychoverse v1.0 is the public-good foundation that the commercial layer builds on, not the commercial layer itself.

*Word count: 291*

---

## Technical design (Q24–Q28)

### Q24: Technical design at a high level (350 words)

Psychoverse v1.0 is a three-phase pipeline that fine-tunes a genomic foundation model on cell-type-resolved brain data, learns an interpretable phenotypic representation, and aligns the two into a shared coordinate space. The full stack runs on AWS HIPAA-eligible services, with AWS HealthOmics as the genomic data warehouse and Amazon SageMaker as the training and serving engine.

**Phase 1, AlphaGenome cell-type-aware fine-tuning.** AlphaGenome-PyTorch (open source) is fine-tuned with LoRA on PsychENCODE 388-donor paired data. Training inputs are pseudobulked snRNA-seq and snATAC-seq BigWig tracks per individual at multiple cell-type resolutions. Input files are stored in AWS HealthOmics; large intermediate files (BigWig tracks, embeddings, checkpoints) land on Amazon S3 backed by Amazon FSx for Lustre for high-throughput access during training. Training runs on Amazon EC2 P5 instances (H100 GPUs) or AWS Trainium 2 (Trn2) instances via Amazon SageMaker training jobs; AWS Trainium 2 is evaluated for cost-efficiency at scale. Checkpoints are encrypted with AWS Key Management Service inside a HIPAA-scoped VPC. Output: cell-type-aware LoRA adapters that embed each genomic variant in brain-regulatory context.

**Phase 2, sparse phenotype autoencoder.** NeuroBioBank harmonized neuro-behavioral phenotypes train a sparse autoencoder with joint reconstruction-plus-disease-label-prediction loss. PsychENCODE phenotypes hold out for cross-cohort generalization. Compute is modest; one SageMaker training job on an ml.g6 instance handles this phase.

**Phase 3, phenotype-aligned coordinate system.** Phase 1 embeddings are pooled per gene. A multi-resolution graph-wavelet GNN over curated gene functional networks reduces these to a low-dimensional per-individual representation. We then compute kernel matrices in both the genomic and phenotypic spaces and apply Manifold-approximated Kernel Alignment to learn phenotype-aligned axes. AWS Batch orchestrates the full multi-step pipeline across phases.

**Inference and release.**  The final model serves through a SageMaker real-time inference endpoint behind Amazon API Gateway with AWS Lambda authorization, documented under an OpenAPI specification. AWS Audit Manager, AWS CloudTrail, and AWS Config provide the HIPAA evidence trail. Open weights and LoRA adapters mirror to Hugging Face. Documentation, ancestry-disaggregated model cards, and the published threat model ship via Amazon S3 and Amazon CloudFront. Amazon Bedrock is scoped for the clinical agent layer in a planned follow-on phase.

*Word count: 338*

---

### Q25: Resources and skills needed (350 words)

**In-house expertise.** Cytognosis Foundation has more than 20 years of combined experience in artificial intelligence for biology, single-cell brain genomics, and foundation-model architecture across the principal investigator and senior advisor. The PI contributed to the first single-cell Alzheimer's disease atlas (Mathys et al. 2019, *Nature*), co-led the first multi-cohort single-cell schizophrenia atlas (Ruzicka, Mohammadi et al., *Science* 2024, co-first author), and co-led the bipolar disorder single-cell atlas (*European Neuropsychopharmacology* 87:48, 2024, co-first author). The PI also led interactome modeling for AIDO, an early multi-scale biological foundation model, at GenBio AI, directly relevant experience in fine-tuning and integrating genomic foundation models. The PI authored ACTIONet (github.com/shmohammadi86/ACTIONet, Apache 2.0), the analytical framework adopted by PsychENCODE, ROSMAP, and PsychAD. Senior Advisor Ananth Grama directs Purdue's Institute for Physical Artificial Intelligence and provides foundation-model architecture review. Co-Lead Brad Ruzicka, MD/PhD, is the McLean Hospital NeuroBioBank liaison who anchors the data access pathway. This is the team that built the upstream scientific foundation this project depends on.

**To be acquired through this grant.** One full-time ML and bioinformatics engineer (nine months) handles day-to-day fine-tuning, BigWig pipeline construction, sparse autoencoder training, GNN implementation, and inference-API deployment on AWS. Recruiting is underway. A short-engagement cloud architect consultant (approximately 40 hours) will stand up the HIPAA-eligible AWS environment, including AWS Business Associate Agreement execution, KMS key topology, VPC isolation, AWS HealthOmics workflows, and AWS Audit Manager configuration.

**AWS-specific skills and support.** We request an AWS implementation partner with genomics or healthcare ML expertise, particularly experience with HealthOmics-based variant pipelines and HIPAA-eligible SageMaker deployments (see Q26). We also plan to engage the AWS Generative AI Innovation Center for SageMaker HyperPod tuning on AlphaGenome-class architectures and for ongoing security review during the public-API hardening phase.

**Data access.** PsychENCODE access is established through the PI's existing dbGaP credentials and consortium membership. NeuroBioBank access routes through Brad Ruzicka's McLean Hospital liaison role. A North Star IRB submission is budgeted for any data-handling amendments required by AWS HIPAA processing. No new external data agreements are blockers to starting the project.

*Word count: 318*

---

### Q26: Implementation partner

**(b) Yes, I do not have a partner identified but would like a recommendation.**

We would welcome AWS pairing us with a Partner specializing in genomics or healthcare machine learning on AWS, particularly one experienced in HealthOmics-based variant pipelines and HIPAA-eligible SageMaker deployments. We are open to engagement with the AWS Generative AI Innovation Center if eligible.

---

### Q27: Current IT infrastructure

**With another provider.** Google Workspace for collaboration; minimal current compute footprint. Our organizational IT footprint is intentionally lean.

---

### Q28: Project IT infrastructure (proposed)

**Net-new to your organization.** The Psychoverse v1.0 workload is a greenfield AWS deployment under a newly established HIPAA Business Associate Agreement, scoped to a single isolated AWS account dedicated to this project.

---

## Certification and consent

[Yes] I consent and agree to AWS processing my information as defined above.
[Yes] I certify that I have reviewed and agree to the AWS Imagine Grant Terms and Conditions.

---

# Appendix A: Budget summary (Internal / Round Two only, not submitted in Round One)

**Total cash requested:** $149,800
**Total AWS Promotional Credit requested:** $100,000

## Cash budget

| Line | Amount | Notes |
|---|---|---|
| PI Shahin Mohammadi (0.50 FTE x 9 months, fully loaded) | $62,000 | $135K W-2 gross x 0.50 x 9/12 = $50,625 + employer-side (FICA, health, payroll) x 0.50 x 9/12 = approximately $11,375. This line funds 50% of the PI's effort scoped to the AWS-hosted genomic-phenotype alignment workload. The PI is 1.0 FTE total, capped at $165,000/year across all funding sources. Coordination clause below governs how this line interacts with the PI's other applications. |

**PI compensation coordination clause (verbatim, inserted in every application):**

> The PI is compensated as 1.0 FTE at a fully-loaded, board-approved rate of $165,000/year, approximately 65% of the PI's prior market salary. Total PI compensation across all funded sources is capped at this amount in any 12-month period. Where awards overlap, PI-effort lines in project grants are reduced and reallocated to non-PI direct costs, and the Career Development and Transition award (if held) is reduced to the level needed to reach the runway floor. This prevents duplicative compensation while ensuring the PI's full-time effort is sustained if any single source funds.

The Coefficient Giving Career Development and Transition award ($165K, individual PI payroll) is the runway floor and is reduced proportionally as project-effort lines such as this AWS line are funded. No other pending application funds the AWS-scope PI effort.
| ML / Bioinformatics Engineer (0.80 FTE x 9 months) | $46,800 | $6,500/month direct, below-market nonprofit rate. Scaled from 1.0 FTE since PI provides 50% project effort. |
| Senior Scientific Advisor (Grama, 0.10 FTE x 9 months) | $6,000 | Consulting at architecture-review checkpoints. |
| Cloud architect / HIPAA setup consultant (approximately 40 hours) | $5,000 | AWS HealthOmics + BAA + VPC + KMS topology. |
| North Star IRB submission and amendments | $3,500 | |
| dbGaP / NBB / data-use agreement fees and legal | $3,000 | NeuroBioBank access via HBTRC liaison. |
| Local dev hardware (workstation + 1 dev machine) | $4,000 | Data prep and small-scale ablations. |
| External security and data-governance audit | $6,000 | Single focused audit cycle; threat model published under Apache 2.0. |
| Conferences (ASHG primary; NeurIPS or OHBM secondary) | $4,000 | |
| Open-source infrastructure (Hugging Face, CI/CD, docs) | $3,000 | |
| Contingency (approximately 4.5% of direct costs) | $6,500 | |
| Indirect | $0 | Absorbed from other funding; AWS funds direct project costs only. |
| **Total cash** | **$149,800** | |

## AWS Promotional Credit budget

| Line | Amount | Phase |
|---|---|---|
| Phase 1: AlphaGenome LoRA fine-tuning (EC2 P5 / Trn2, 3 to 4 weeks) | $35,000 | 1 |
| Phase 2: Sparse autoencoder training (SageMaker ml.g6) | $5,000 | 2 |
| Phase 3: GNN + MKA alignment training (SageMaker training jobs) | $15,000 | 3 |
| AWS HealthOmics variant storage and workflows | $6,000 | All |
| Amazon S3 + FSx for Lustre (BigWig tracks, embeddings, checkpoints) | $5,000 | All |
| SageMaker real-time inference endpoints (public API) | $15,000 | Release |
| KMS + CloudTrail + Config + VPC + Audit Manager + API Gateway | $2,000 | All |
| Reserve for ablations and iteration | $17,000 | All |
| **Total credits** | **$100,000** | |

---

# Appendix B: Open items for final submission

1. Org mailing address confirmed: 394 Innisfree Dr, Daly City, CA 94015 (Q4).
2. AWS account confirmed active: account name "cytognosis," Account ID 630287362866, root email mohammadi@cytognosis.org, with the $100 activation credit. The Account ID is now filled in Q12; sign in with the org root email at submission, and consider enrolling in the AWS Nonprofit Credit Program ($5K baseline).
3. Confirm whether we want to attach the parallel Google.org and Coefficient Giving applications as supporting context (not required in Round One; may be useful in Round Two if invited).
4. Decide whether to register the North Star IRB application in advance of the grant period to demonstrate readiness, or hold until award.
5. SDI exhaustion date confirmed by the founder as October 1, 2026; Career Transition cross-reference dates in Q23 use this.
6. **Round One form structure confirmed (2026-05-31, live AWS page).** Round One is a SHORT application: organization information (Q1–Q13) plus category selection, with a brief project summary at most. The full project and technical questions (Q14–Q28) and the budget are deferred to **Round Two, which is by invitation only**, based on Round One evaluation. Action: submit Q1–Q13 plus the selected category for Round One, and keep Q14–Q28 and the budget here as the Round Two reservoir. Category is chosen at Round One and is effectively locked. **Round One deadline: June 5, 2026, 11:59 PM EDT.**
7. **Incorporation/address (confirmed, consistent):** Cytognosis Foundation is **incorporated in Delaware** as a nonprofit, **IRS 501(c)(3) approved**, **EIN 39-4383634**, with a **mailing address of 394 Innisfree Dr, Daly City, CA 94015** (founder's residence, no office). Delaware (state of incorporation) and Daly City (mailing address) are not in conflict; ensure Q1 through Q4 reflect this and match the IRS determination letter. (Note: the v1 Google.org draft says "founded 2024"; the correct date is Sept 8, 2025.)
8. ARPA-H strategy alignment: per the current funding plan, **HSF is the single Mission-Office ISO** to pursue (PHO is the mutually-exclusive alternative), and **IGoR** is a separate PHO *program* solicitation: keep Q23 consistent with whichever is actually live at submission.

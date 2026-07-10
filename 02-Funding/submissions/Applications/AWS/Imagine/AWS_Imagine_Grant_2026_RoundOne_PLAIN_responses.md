# AWS Imagine Grant 2026 — Round One, paste-ready responses (plain-language rewrite)

**Reading time: ~6 min. If you only read one thing:** the deadline is **tonight, June 5, 2026, 11:59 PM Eastern (8:59 PM Pacific)**. Every response below is rewritten for a non-scientist reviewer and fits its word limit. Copy each block straight into the portal.

---

## Decisions I made for you (flagged, change only if you disagree)

| Decision | What I chose | Why |
|---|---|---|
| **Category (2.2)** | **Go Further, Faster** | The live form you pasted is the Go Further, Faster question set (no Pathfinder-only data/AI questions). Your budget is already sized to its $150K + $100K cap. It cleanly fits "advanced AI/ML on cloud." Pathfinder pays up to $200K cash but needs two more strong answers tonight and a frontier-AI framing; not worth the risk this close to deadline. If declined, AWS can auto-route you to Go Further, Faster in Round Two anyway. |
| **Branding/jargon** | **Confined to 2.3's opening, each term defined** via the GPS-for-Health metaphor (Cytoverse, Cytoscope, Cytonome, Psychoverse); removed everywhere else, including "Neuro Layer" and "open Map layer" | Ananth's objection was undefined branding. Defining the platform once, through an intuitive GPS metaphor, in the mission question keeps the narrative while staying legible. 2.1 and all other answers stay plain. |
| **AlphaGenome** | **De-centered**; lead with open-weights models (Evo 2, Nucleotide Transformer) | AlphaGenome is a Google DeepMind product (an AWS competitor) and its weights are not open, so you cannot fine-tune it freely. Open models are both more honest and strategically smarter here. |
| **"genomic foundation model"** | **Defined in plain words** at first use | Even Ananth asked you to define it. Now glossed as "a large AI model for DNA, like ChatGPT but for the genome." |
| **"biotype" / "phenotype"** | **Used where they add rigor, defined inline** (2.1, 2.3, 3.1) | Precise terms are welcome as long as each is defined on first use. |
| **Audience recalibration** | **AI/ML terms used freely** (multimodal, foundation model, machine-learning-guided); clinical terms defined on use | This is an AI/ML-heavy program; the panel will know ML vocabulary. The plain-language rule now targets clinical and branding jargon specifically, not standard ML terms. |
| **Personalized-intervention motivation** | **Added to 2.1, 2.3, 2.4** | Motivates the non-invasive, personalized, ML-guided treatment payoff the map enables, not just biotyping. Evidence: Stanford SAINT (individualized targeting) plus Nan et al. 2026, the N-of-1 ML lifestyle-targeting study (npj Digital Psychiatry and Neuroscience). |
| **Project stage (2.6)** | **Under development** | Design complete, data access established, engineering hire pending. Honest and strong. |
| **Executive Order framing** | Cited as **federal urgency**, not an AI mandate | The April 18, 2026 EO is about accelerating treatments for serious mental illness; it does not name AI tools. Overclaiming would be a factual risk. |

---

# SECTION 1 — Organizational information (not scored)

Copy these into the structured fields.

| Field | Value to enter |
|---|---|
| Full, Registered Organisation Name | **Cytognosis Foundation, Inc.** |
| 1.1 Tax ID (9 digits, no dash) | **394383634** |
| 1.2 Website URL | **https://www.cytognosis.org** |
| 1.3 Street | **394 Innisfree Dr** |
| 1.3 City | **Daly City** |
| 1.3 State | **California** |
| 1.3 Zip Code | **94015** |
| 1.4 Annual Organizational Revenue (most recent FY) | **Under $50,000** (FY2025). Select the lowest revenue bucket the dropdown offers. |
| 1.5 Annual IT Budget (most recent FY) | **Under $10,000** (FY2025). Select the lowest IT-budget bucket the dropdown offers. |
| 1.6 Proposal Contact — Name | **Shahin Mohammadi** |
| 1.6 Proposal Contact — Email | **mohammadi@cytognosis.org** |
| 1.6 Proposal Contact — Phone (numbers only) | **7654091883** |
| 1.7 Project Lead — Name | **Shahin Mohammadi** |
| 1.7 Project Lead — Email | **mohammadi@cytognosis.org** |
| 1.7 Project Lead — Phone (numbers only) | **7654091883** |
| 1.7 Project Lead — Role in Organization | **President or CEO** |
| 1.8 Project Lead — Functional Area | **Leadership or overall management** |
| 1.9 Primary Mission Area | **Science, Technology, and Social Science** |
| 1.10 AWS account? | **Yes** (account "cytognosis," Account ID 630287362866, root email mohammadi@cytognosis.org) |
| 1.11 Applied for Imagine Grant before? | **No** |

---

# SECTION 2 — Project information

### 2.1 — High-level overview (limit 100 words) — *paste-ready, 96 words*

Mental illness is the leading cause of disability worldwide, yet psychiatry still sorts patients into categories like "schizophrenia" or "autism" that hide large biological differences between individuals and leave roughly half without an effective first treatment. We will build an open multimodal psychiatric map ("foundation model"), learned jointly from genomic and phenotypic (mood and cognitive symptom) data from clinically relevant populations, that enables quantitative mapping, profiling, and biotyping of individual patients. This biology-anchored map is the missing layer for precision psychiatry, including personalized behavioral interventions that recently produced large improvements in depression, well beyond generic programs.

---

### 2.2 — Award category

**Go Further, Faster**

---

### 2.3 — Describe your project in depth and how it relates to your mission (limit 350 words) — *paste-ready, 312 words*

Cytognosis is building a cellular intelligence platform, a GPS for Health, with three parts: the Cytoverse, a multimodal map whose continuous biological axes (a longitude and latitude for health) replace imprecise disease labels; the Cytoscope, a sensor that locates each person on that map; and the Cytonome, a navigator that turns coordinates into mechanistic guidance. This project builds the Cytoverse map for neuropsychiatric conditions, the Psychoverse.

Today a person is labeled with "schizophrenia," "autism," or "depression" and treated by that label, yet patients who share a diagnosis often differ biologically and respond very differently, one reason being that roughly half do not improve on their first treatment.

When patients within a diagnosis are instead sorted into biologically defined subgroups (biotypes) and treated as individuals, outcomes improve sharply: individualized brain-stimulation targeting, behind Stanford's FDA-cleared SAINT therapy, drove remission in most treatment-resistant cases, and a 2026 study that personalized each patient's intervention from their own data produced large, on-target symptom reductions. The individual, not the diagnostic average, is the right unit of analysis.

Because the biology driving these subgroups also crosses diagnostic boundaries, we build one transdiagnostic map rather than a model per disorder. This grant delivers its first public release: an open model that places each person on shared genomic-and-symptom axes learned from clinically relevant patient populations. It turns a one-word diagnosis into an interpretable, biology-anchored profile, a biotype, where proximity reflects shared biology rather than matching checklists. For the field, it converts scattered cohorts into one common coordinate system any group can extend; for clinicians, it is the foundation for matching care to a person's biology rather than a label; and for patients, it is a path away from trial-and-error prescribing. We make it openly available as an AWS-hosted service that any researcher, clinician, or patient-advocacy group can use, directly advancing our mission to replace imprecise diagnostic labels with open, biology-anchored tools.

---

### 2.4 — Intended outcomes and new capabilities (limit 350 words) — *paste-ready, 346 words*

By the end of a nine-month project, we will release the first public version of the model, with three concrete outcomes.

First, an open tool that maps a person's genomic and phenotypic data onto the multimodal map, the Psychoverse. Today, a clinician has only a diagnostic label and subjective symptom scores. Our model provides an interpretable patient scoring ("biotype"), in which people who are closer together share similar underlying biology rather than identical questionnaire responses. This is the prerequisite for matching treatments to individual biologies, rather than symptoms (much like treating bacterial infection rather than cough). Second, a reusable way to combine genetic and symptom data across different patient groups. Any future clinician with both types of data can place their patients on the same map without having to rebuild the model from scratch. One group's effort becomes shared infrastructure for the whole field. Third, a public service, hosted on AWS, that lets researchers and clinicians use the model over the internet to run inference without their own computing power. We will publish complete documentation, performance results broken down by ancestry group to demonstrate that the tool is tested for fairness, and an independent security review.

For Cytognosis Foundation, this is our first cloud-native product and our first public service. It establishes a secure, health-data-compliant infrastructure on AWS, using Amazon SageMaker for model training and hosting, AWS HealthOmics for genomic data, and a reusable engineering foundation and a published security baseline that every future release can build on. We expect early-adopting research groups to integrate the public service into their pipelines within six months of release.

Milestones: an adapted genomic model at month three, the symptom model at month five, and the full aligned map, public service, documentation, and security review at month nine. Each milestone ships as an open release, so value is delivered continuously rather than only at the very end. Strategically, this genomic and phenotypic map is the first module of a multiscale platform, with an architecture designed to integrate brain-connectivity (connectomic) data and capture environmental drivers that the genome alone cannot encode.

---

### 2.5 — What is driving the need? Why now? (limit 350 words) — *paste-ready, 347 words*

Three forces make the next twelve months the right window.

The need is overwhelming and rising. Mental disorders are now the leading cause of disability worldwide, affecting about 1.17 billion people and accounting for roughly one in six of all the years people live with disability. The burden has nearly doubled since 1990 and peaks in adolescents aged 15 to 19. In the United States, more than 14 million adults live with serious mental illness, and roughly half of patients do not improve on their first treatment. Federal urgency is explicit: in April 2026, a White House Executive Order directed agencies to accelerate innovative treatments for serious mental illness.

The enabling pieces only recently arrived. Whole-genome sequencing has fallen below $1,000, putting each person's full genome within clinical reach. That reframes the opportunity: rather than reading the handful of genes in today's pharmacogenomic panels (GeneSight tests about a dozen), we can now group whole-genome variation into functionally interpretable factors for diagnosis and treatment selection. The other pieces are equally new: genomic foundation models that read DNA reached strong performance only in the past two years, brain-tissue biobanks released the paired genetic and cellular datasets the approach needs, and a 2025 study showed psychiatric risk across 14 conditions compresses into a few shared factors. None existed in usable form 18 months ago.

The open-versus-closed window is closing. Within roughly 18 months, either an open, public-good tool becomes the shared reference that the field builds on, or proprietary tools become entrenched in closed clinical systems and lock out the open scientific community. Cytognosis is well-positioned to lead this project, as our team co-led the foundational brain atlases across diverse neuropsychiatric disorders and the first wave of models trained on these atlases, and our collaborators provide clinical and biobank access and an AI architecture review.

AWS support compresses this timeline by 9 to 12 months versus waiting on a larger federal grant cycle. The promotional credits cover the compute-intensive model training, and the cash award covers the people and the data access needed to deliver an open public tool quickly.

---

### 2.6 — Project stage

**Under development.** The scientific design is complete, access to the key datasets is established through existing research credentials and our clinical co-lead's biobank role, and early AWS infrastructure scoping is underway. The remaining unlocks are the engineering hire and provisioning the secure, HIPAA-eligible AWS environment.

---

### 2.7 — What most closely aligns with what this project will enable

Select the option about **informing better decision-making by aggregating disparate data sources and applying analytics (AI/ML)**.

(Plain rationale, if helpful: the model brings together two independent data sources, genetic data and symptom data, and applies AI to produce a usable analytics layer, an open map plus a public service, that researchers and clinicians use to place individuals in biologically meaningful terms.)

---

### 2.8 — Long-term support, stakeholders, partners, other funding (limit 250 words) — *paste-ready, 247 words*

Stakeholders and partners. Our project co-lead, Brad Ruzicka, MD/PhD (McLean Hospital and Harvard Medical School), co-authored the single-cell schizophrenia atlas this work builds on and serves as our brain-biobank liaison; he anchors clinical validation and data access. Our senior scientific advisor, Ananth Grama (Purdue University), reviews the AI architecture and large-scale computing design. Distribution partners for reaching patients and clinicians include One Mind, the American Psychiatric Association's digital-health group, and the Center for Digital Mental Health at Harvard and Massachusetts General Hospital.

Other funding (pending, not yet awarded). We have parallel applications for separate, non-overlapping scopes; the personnel in this AWS request fund the cloud-hosted genome-and-phenotype alignment work specifically, which no other application duplicates.

Long-term support. This map is one module of a multiscale platform. Because psychiatric risk reflects both genome and environment, and environmental effects (identical twins can diverge, one developing schizophrenia and one not) are absent from the genome but imprinted in brain connectivity, our next stage adds an integrated connectomic foundation model. We are preparing an ARPA-H submission toward it, building on the ARPA-H-funded EVIDENT effort, which is generating the rapid-acting interventional data that stage will use. We serve inference openly and publish code and documentation openly, sharing model weights where data-use agreements permit. Ongoing AWS hosting is funded by follow-on grants (including this ARPA-H submission), the AWS nonprofit credit program, and revenue from a separate self-funding brain-sensing device line. The open model stays nonprofit-owned; the commercial layer builds on it, not the reverse.

---

# SECTION 3 — Technical design

### 3.1 — Technical design at a high level: what does it do and how? (limit 350 words) — *paste-ready, 259 words*

The system is built in three stages, all on AWS health-data-compliant services, with AWS HealthOmics as the genomic data store and Amazon SageMaker for training and hosting.

Stage one, the genomic encoder. We fine-tune a pretrained genomic foundation model (for example, Evo 2), which has learned the evolutionarily conserved "grammar" of DNA, on clinically relevant genomes from patients with neuropsychiatric and neurodegenerative disorders (the NIH NeuroBioBank cohort). Its encoder embeds each person's genome in the 1-Mbp context around every gene; a multi-resolution graph neural network (GNN) then propagates these embeddings over gene networks to capture disease-associated signaling, and we pool them into a patient-level embedding that predicts disease labels.

Stage two, the phenotype encoder, trained in parallel. A sparse autoencoder embeds neurobehavioral phenotypes (a person's observable symptoms, traits, and clinical features) across patients, compressing them into interpretable factors.

Stage three, alignment. A contrastive loss aligns the genome- and phenotype-derived embeddings to yield multimodal biotypes: groups of patients with similar genomic variation and similar symptom profiles. Our working hypothesis is that the genomic factors drive the phenotypic ones; we will test that later with causal and mediation analyses, not assume it.

Training runs on Amazon EC2 GPU instances through SageMaker, with large files on Amazon S3 and FSx for Lustre and checkpoints encrypted by AWS KMS inside an isolated, HIPAA-eligible network. We serve the model openly for inference through a SageMaker endpoint behind Amazon API Gateway, publish code and documentation openly, and release model weights where data-use agreements permit; AWS audit, logging, and configuration services provide the health-data compliance trail.

---

### 3.2 — Resources and technical skills needed (limit 350 words) — *paste-ready, 343 words*

In-house expertise. The core team built much of the science this project depends on. Our principal investigator has roughly 20 years in AI for biology and brain genomics: he co-led the first single-cell atlases of schizophrenia and bipolar disorder, contributed to the first single-cell atlas of Alzheimer's disease, and led biological-network modeling for an early large-scale biological foundation model in industry. He also authored an open-source analysis framework adopted by major brain-genomics consortia, and brings years of hands-on experience deploying large-scale machine learning on AWS in prior industry roles (including at insitro), so the team can build on AWS from day one even though the Foundation's current compute runs on another cloud. Our project co-lead, Brad Ruzicka, MD/PhD (McLean Hospital and Harvard Medical School), provides clinical expertise and brain-biobank access. Our senior advisor, Ananth Grama (Purdue University), reviews the AI architecture and large-scale computing design. This is the team that produced the upstream datasets and methods the project uses.

To be acquired through this grant. We will hire one full-time machine-learning and bioinformatics engineer for nine months to run the day-to-day model training, data pipelines, and deployment of the public service. Recruiting is underway. We will also engage a cloud architect for a short setup engagement, about 40 hours, to stand up the secure, HIPAA-eligible AWS environment, including the business associate agreement, encryption-key setup, network isolation, and audit configuration.

AWS support requested. We would value an AWS implementation partner with genomics or healthcare machine-learning experience, particularly with HealthOmics data pipelines and HIPAA-eligible SageMaker deployments. We are also interested in the AWS Generative AI Innovation Center for help tuning large foundation models and for security review while we harden the public service.

Data access. Access to the brain-genomics datasets is established through the principal investigator's existing research credentials and through our co-lead's biobank role. A small budget covers any data-governance review needed for processing data in the AWS environment. No new external data agreement is a blocker to starting the project, so the team can begin building on day one of the grant period.

---

### 3.3 — Need a technology / implementation partner?

**Yes, I do not have a partner identified but would like a recommendation.** We would welcome an AWS Partner specializing in genomics or healthcare machine learning, particularly one experienced with AWS HealthOmics pipelines and HIPAA-eligible SageMaker deployments, and we are open to the AWS Generative AI Innovation Center if eligible.

**Live-form note:** Select the recommendation option, not "I already work with a specific partner," and leave 3.3.1 blank. Purdue's IPAI (Ananth Grama) is your scientific and AI-architecture advisor (credited in 2.8 and 3.2), not an AWS implementation Partner, so it should not be entered here. Requesting a recommendation matches you to a genomics/healthcare-ML AWS Partner, which is the right move for a team new to AWS.

---

### 3.4 — Is your organization's IT infrastructure currently:

**With another provider.** Our current compute runs on another cloud provider, with Google Workspace for collaboration; the Foundation's footprint is intentionally lean, and this grant funds our first AWS deployment.

---

### 3.5 — Is the IT infrastructure for this project currently:

**Net-new to your organization.** The project's AWS environment does not exist yet; it is a greenfield deployment under a newly established HIPAA Business Associate Agreement, scoped to a single isolated AWS account. Your current development runs on another cloud, so the proposed AWS infrastructure is new to the organization, which is the accurate choice here.

---

# SECTION 4 — Certification & consent

- **4.1** Consent to AWS processing your information: **YES**
- **4.2** Reviewed and agree to the AWS Imagine Grant Terms and Conditions: **YES**

---

## Before you submit (2-minute checklist)

1. **Time zone:** deadline is 11:59 PM **Eastern** = **8:59 PM Pacific** tonight. Submit with margin.
2. **Category locked at submission:** you are choosing **Go Further, Faster**. This is effectively locked for both rounds.
3. **Revenue / IT budget dropdowns:** pick the lowest bucket that contains "under $50,000" and "under $10,000" respectively.
4. **Phone and Tax ID:** numbers only (7654091883; 394383634).
5. **Word limits:** every open response above is within its limit; safe to paste as-is.

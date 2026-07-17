> **Status**: Active
> **Date**: 2026-06-03
> **Author**: @mohammadi
> **Audience**: engineers, stakeholders
> **Tags**: `cytonome`, `funding`, `grant`, `foresight`

# Foresight — AI for Science & Safety Nodes (2026 submission)

Application link: https://foresight.org/grants/grants-ai-for-science-safety/

**Project:** Cytonome: An Open, On-Device Private-AI Framework for Cognitive Sovereignty and Safe Neuro-AI
**Applicant:** Cytognosis Foundation (501(c)(3), Delaware; PI founded the Foundation as Founder and Board Chair, October 2025)
**Track:** AI for Neuro, Brain-Computer Interfaces & Whole Brain Emulation
**Requesting:** Funding (grant), physical node access (Bay Area), local compute

---

## About You

**Full name:** Shahin Mohammadi
**Email:** mohammadi@cytognosis.org
**Affiliated organization:** Cytognosis Foundation
**Profile:** https://www.linkedin.com/in/shmohammadi/
**Applying as:** Organization
**Primary region / country:** America / USA
**Org type:** Non-profit, US (501(c)(3))

---

## Track Record

### What is your/your team's track record?

Our team brings together computational neuroscience, clinical psychiatry, AI systems architecture, and multi-scale brain mapping. Over the past decade we helped build the first molecular atlases of human neuropsychiatric and neurodegenerative disease across major international consortia (PsychENCODE, PsychAD, ROSMAP), with over 40 peer-reviewed publications, including in Science and Nature. We built the molecular foundation that any safe brain-computer interface or whole-brain emulation framework will eventually have to map onto.

- **Shahin Mohammadi, PhD** (PI, Cytognosis Foundation). 20 years building AI for biological and medical systems across MIT, Broad Institute, Purdue, insitro, and GenBio AI. Creator of ACTIONet (github.com/shmohammadi86/ACTIONet, Apache 2.0), used across the psychiatric-genomics consortia. Co-led the first single-cell multi-cohort atlas of schizophrenia (Ruzicka, Mohammadi et al., Science 2024), which identified continuous disease axes and biologically distinct subtypes within one DSM diagnosis, the direct scientific foundation for Cytonome. Co-first author on the multi-cohort bipolar atlas (Han, Mohammadi et al., European Neuropsychopharmacology 2024). Contributor to the first single-cell study of Alzheimer's disease (Mathys, Davila-Velderrain, Mohammadi et al., Nature 2019). Contributing author on the PsychENCODE capstone (Emani et al., Science 2024).
- **Brad Ruzicka, MD/PhD** (Co-Lead, Assistant Professor, McLean Hospital / Harvard Medical School). Practicing clinical psychiatrist-scientist; co-first author with the PI on the single-cell multi-cohort schizophrenia atlas (Ruzicka, Mohammadi et al., Science 2024) and a current collaborator on our multi-cohort bipolar work. Our liaison to the Harvard Brain Tissue Resource Center / NeuroBioBank, with a joint IRB protocol for the clinical pilot already in preparation. Anchors clinical validation, the IRB pathway, and PHQ-9/GAD-7 ground truth.
- **Ananth Grama, PhD** (Senior Scientific Advisor, Purdue University). Samuel Conte Distinguished Professor; Director of the Institute for Physical AI. Foundation-model architecture and scalable distributed compute.

### Project participants
- PI: Shahin Mohammadi, PhD
- Co-Lead: Brad Ruzicka, MD/PhD, McLean Hospital / Harvard Medical School
- Senior Scientific Advisor: Ananth Grama, PhD, Purdue IPAI

### Primary reference
Jose Davila-Velderrain, PhD, Group Leader (computational neuroscience), Human Technopole; co-author on the PsychENCODE single-cell capstone and the PsychAD atlas (Science 2024); a long-standing collaborator who can speak to the PI's research record. Contact provided on request.

---

## About Your Project

### What are you applying for?
Funding (grant), physical node access (Bay Area), local compute.

### Foresight focus area
AI for Neuro, Brain-Computer Interfaces & Whole Brain Emulation.

### Project title
**Cytonome: An Open, On-Device Private-AI Framework for Cognitive Sovereignty and Safe Neuro-AI**

### What are you trying to do? (max 350 characters)

We build Cytonome, an open, on-device private-AI framework that turns voice and wearable signals into private mental-state coordinates on a user's own phone, governed by a hard safety boundary (Cytoplex), as the privacy-first edge any safe BCI or brain-emulation effort will need.

### How is today's approach limited? What is new in your approach, and what does success look like?

#### Today's limits: a centralization crisis, not a clinical one

The neuro-AI landscape is racing toward a future where corporate and state actors centrally own the highest-fidelity map of human cognition ever assembled, and we have no defensive primitives in place.

1. **The capability/defense gap has inverted.** Recent clinical validation (Nan et al., 2026) shows N-of-1 ML models can decode individual psychological states with high accuracy (Cohen's d = -0.89 for depression alleviation under AI-guided lifestyle optimization). Population-scale genomic modeling now resolves psychiatric variance into a five-factor structure across 14 disorders (Grotzinger et al., Nature 2025), and our own Science 2024 schizophrenia atlas resolves continuous disease axes within a single DSM label. The capability to map and steer a human being is here. The open, defensive infrastructure to prevent its capture is not.

2. **Centralized custody is the wrong primitive.** The 23andMe bankruptcy turned millions of users' immutable genomic profiles into liquidatable assets the moment shareholder duties shifted. Standard federated learning does not solve this: the bulk aggregator remains a single point of failure. Cognitive data is even less recoverable than a genome. You can change a password; you cannot change your brain.

3. **The macro-to-micro mapping does not exist as a public good.** No open system connects real-time behavior (voice, wearables) to meso-scale signals to micro-scale molecular dimensions. Without this, safe BCI alignment and whole-brain-emulation primitives are being designed in the dark, and whoever builds the closed version first owns that layer.

#### What's new

Cytognosis builds a "GPS for Health" platform with three components: the **Cytoverse** (the Map, our validated molecular coordinates), the **Cytoscope** (the Sensor, longitudinal measurement), and the **Cytonome** (the Navigator, the privacy-first on-device private-AI framework). This proposal funds **Cytonome**, the on-device navigator that maps brain variation across three scales, governed by **Cytoplex**, its hard safety boundary.

- **Micro:** genotype and single-cell transcriptomics (PsychENCODE, ROSMAP, NeuroBioBank), our published molecular track record.
- **Meso:** brain connectomics over public neuroimaging (fMRI/EEG consortia).
- **Macro:** behavioral and wearable physiology (voice, HRV, sleep, activity), the on-device edge Foresight funds.

Cytonome is real and partly shipped (a working on-device voice loop, with Cytoplex, its safety boundary, implemented and passing 93 safety tests). Three design commitments differentiate it, in order of how load-bearing and how built they are:

1. **On-device perception (built, shipping).** Compact models (Gemma 4 family, on the order of 3B parameters or less) run entirely on the user's phone via LiteRT and Flutter. Voice and wearable signals are turned into mental-state coordinates locally. No cloud egress of raw signals by default.

2. **A hard safety protocol: Cytoplex (built).** The **Cytoplex** is an execution boundary, not advice-time guidance. Only allow-listed operations run; nothing leaves the device or reaches an external tool without explicit user confirmation; diagnosis and treatment claims are blocked; uncertain interpretations must use uncertainty language. Cytoplex-Lite is implemented and tested. This is the primitive that makes an on-device cognitive companion safe, and we open-source it for any project that needs the same boundary.

3. **User-owned data, by default (baseline today, hardened over the grant).** Raw data stays on-device in a local store with a granular, revocable, machine-readable consent ledger. Over the grant we will adopt a user-owned data-pod model (for example, Solid) so the Foundation is structurally a zero-custody entity, and we will evaluate post-quantum primitives (ML-KEM, ML-DSA) for at-rest hardening where feasible. These are hardening steps on a working private-by-default baseline, not prerequisites.

Every component (models, training code, the Cytoplex safety layer, the open sensor-adapter protocol, evaluation benchmarks) is released as a public good under Apache 2.0 (code/models) and CC BY 4.0 (documentation). Not "open weights." Truly open: data provenance, code, weights, and evaluation.

```
[ voice (mic) · wearables: Oura, Apple Watch / smartwatches ]
                          |
                          v
        [ on-device perception: Gemma 4 via LiteRT ]
                          |
                          v
        [ Cytoplex safety boundary: allow-listed ops only ]
                          |
                          v
   [ user-owned local store + consent ledger (Solid pod where feasible) ]
                          |
                          v
   [ optional, where feasible: privacy-preserving aggregation ]
```

#### Success looks like (18 months)

By month 18 we will have delivered: a validated, on-device, Cytoplex-governed mental-state engine on consumer phones, with clinical correlation r > 0.7 against PHQ-9 / GAD-7 on held-out data; multimodal fusion (voice plus Oura Ring physiology); our first proprietary Cytonome multimodal dataset from a 3-month self-experimentation pilot within the core team; and a 20 to 30 person external pilot showing that continuous multimodal monitoring detects clinically meaningful changes that periodic assessment misses. The Cytoplex safety boundary, models, training code, and the open sensor-adapter protocol are released under Apache 2.0, with CC BY 4.0 documentation. Optional EEG exploration (Muse / Emotiv) is a stretch item, not a core deliverable. This generates preliminary data for an ARPA-H Proactive Health Office follow-on.

### If there are risks, can you differentially advance the safety-enhancing aspects first?

Yes, and we have organized the 18 months around exactly that. Cytonome is a defensive-first stack: every safety-enhancing primitive is built, audited, and open-sourced before any sensor stream is ingested or any external participant is enrolled.

1. **Cytoplex safety boundary first (Months 1-6).** The Cytoplex is the core safety primitive and is already implemented (Cytoplex-Lite, 93 passing safety tests). In the first phase we harden it, document it, and open-source it so any researcher can adopt the same execution boundary. This is the single most reusable safety artifact we produce.

2. **On-device, zero-custody by default (architectural, Months 1-18).** Raw data stays on the device under a granular, revocable consent ledger. We adopt a user-owned data-pod model (Solid) where feasible so the Foundation holds zero raw data and cannot become a 23andMe-style honeypot.

3. **Edge-native duty-to-warn override (Months 1-6, before deployment).** When locally computed crisis markers cross a clinician-set threshold, the stack bypasses the conversational agent and surfaces local emergency resources (988, Crisis Text Line) or alerts a pre-designated human proxy, without ever exporting raw psychological signals. Therapy substitution is not a mode we ship.

4. **Hardening where feasible (throughout).** Post-quantum primitives (ML-KEM, ML-DSA) for at-rest data and privacy-preserving aggregation are evaluated and adopted where feasible. We treat these as hardening on a working private baseline, not as prerequisites, so the safety value lands early and reliably.

### Project milestones (start April 2026, end September 2027)

#### Phase 1: Cytoplex safety boundary (Months 1-6)
- M1-2: Harden and document the Cytoplex safety layer; crisis-detection / duty-to-warn module; bias-audit protocol; open protocol spec; IRB submission; clinical dialogue dataset curation paired with PHQ-9/GAD-7/PCL-5.
- M3-4: On-device model fine-tuning (3B-parameter-class model for mental-state quantification, LoRA + DPO on local compute); clinical correlation benchmarks.
- M5-6: Edge optimization (distillation + quantization for LiteRT); user-owned local store + consent ledger; Solid-pod and post-quantum hardening evaluated and adopted where feasible; retrospective validation.
- **Go/No-Go at M6:** r > 0.6 against PHQ-9/GAD-7 on held-out data; Cytoplex safety layer open-sourced and externally reviewable.

#### Phase 2a: Phase 0 multimodal pilot (Months 7-9)
- M7: Core team (3 to 5) instrument themselves with Oura Ring 4 plus voice capture (EEG optional).
- M8: Continuous collection (HRV, sleep, activity, conversational state) under biweekly self-administered clinical instruments.
- M9: Multimodal fusion model v0; voice-only vs. voice + physiology benchmarking.

#### Phase 2b: Validation (Months 10-12)
- M10: On-device personalization pipeline; privacy-preserving aggregation prototyped where feasible.
- M11: Clinical validation (prospective on Phase 0 data plus retrospective benchmarks).
- M12: Open-access preprint; full open-source release under Apache 2.0 (models, code, Cytoplex) and CC BY 4.0 (docs).
- **Go/No-Go at M12:** edge inference within 5% of cloud baseline; multimodal outperforms voice-only.

#### Phase 3: External pilot (Months 13-18)
- M13-14: 20 to 30 participants across MDD, GAD, PTSD, neurotypical; baseline assessments; device deployment.
- M15-16: 3 months of daily multimodal tracking; biweekly clinical ground-truth; personalized baseline learning.
- M17-18: Pilot results; final open-source release; publication; ARPA-H PHO submission.

### If this goes well, how do you scale it for safe-AI impact in 3 years?

**Year 2 (2027-2028): clinical-scale validation via ARPA-H PHO.** The Phase 0/1 multimodal dataset supports an ARPA-H Proactive Health Office submission (engagement in progress). Target scope: 500 to 1,000 participants across 6 psychiatric conditions under continuous monitoring, with the Foresight-funded Cytonome edge architecture as the backbone.

**Year 2-3: cross-scale macro-to-micro bridge.** Connect validated macro behavioral coordinates to our established micro single-cell molecular axes. The question becomes: can a behavioral-plus-wearable trajectory predict molecular subtype? If so, precision psychiatry stops requiring brain tissue and runs on a phone.

**Year 3: population deployment as a public good.** Target 5,000+ continuously monitored users; all models, infrastructure, and validation released under Apache 2.0 / CC BY 4.0; no subscription wall on the open core; no corporate data harvesting.

#### Direct contributions to safe AI
- **Open private-compute blueprint.** The on-device + Cytoplex + consent + (where feasible) post-quantum stack is a reusable template for any AI application requiring privacy preservation.
- **A reusable safety boundary.** Cytoplex is an open execution-boundary protocol any agentic system can adopt to block unsafe actions, not just ours.
- **Multi-scale Rosetta Stone for WBE/BCI alignment.** Cytonome is the open macro-to-molecular mapping that safe BCI alignment will need, released as a public good rather than captured by a closed stack.
- **Interpretable disease dimensions.** Coordinates grounded in validated clinical constructs (PHQ-9/GAD-7) and dimensional frameworks (HiTOP, Grotzinger 2025), with biological interpretability as the macro-to-micro bridge matures.

### Additional information

#### Key publications
1. Ruzicka WB, Mohammadi S, et al. (2024). Single-cell multi-cohort dissection of schizophrenia. Science 384(6698).
2. Mathys H, Davila-Velderrain J, Mohammadi S, et al. (2019). Single-cell transcriptomic analysis of Alzheimer's disease. Nature 570, 332-337.
3. Emani PS, et al. (incl. Mohammadi S, Davila-Velderrain J) (2024). PsychENCODE single-cell genomics across 388 human brains. Science 384(6698).
4. Han X, Mohammadi S, et al. (2024). Single-cell multi-cohort transcriptomic dissection of bipolar disorder. European Neuropsychopharmacology 87, 48. Co-first author.
5. Grotzinger AD, et al. (2025). Mapping the genetic landscape across 14 psychiatric disorders. Nature. DOI: 10.1038/s41586-025-09820-3.

#### Existing open-source contributions
- ACTIONet: github.com/shmohammadi86/ACTIONet (Apache 2.0). Used across PsychENCODE, ROSMAP, PsychAD.
- ACTION: archetypal analysis for multi-omic data.

#### Strategic alignment with Foresight
- **Private local compute.** Cytonome demonstrates that clinically meaningful AI health monitoring runs end-to-end on private, local infrastructure. Training on Foresight local compute means no cognitive dialogue data touches a third-party cloud, and our pipeline becomes a reproducible reference for other Node projects.
- **Decentralized / cooperative AI.** Privacy-preserving aggregation (where feasible) avoids the bulk-aggregator honeypot of standard federated learning.
- **AI for Neuro / BCI / WBE.** We build the multi-scale macro-to-meso-to-micro mapping that safe BCI alignment and any future WBE primitive will need.
- **Safety-first.** Every safety primitive (Cytoplex, crisis detection, bias audit, consent) is built and audited before any data work, and open-sourced first.
- **Impact-first nonprofit structure.** Cytognosis Foundation was deliberately structured as a 501(c)(3) rather than a venture-backed for-profit, because immutable biological data should never be a liquid asset subject to fiduciary duty toward shareholders. Operating as a nonprofit is the institutional analogue of operating as a zero-custody architecture: structural integrity, not stated good intent.

#### Context: Cytognosis Foundation
Cytognosis Foundation is a 501(c)(3) incorporated in Delaware. The PI founded it as Founder and Board Chair in October 2025, after leaving a senior industry role to focus full-time on open-source infrastructure for precision medicine and safe neuro-AI. This proposal is our transition from self-funded development to externally supported research. Concurrent applications anchor to the same platform: Google.org Impact Challenge: AI for Science (the Map, pending); AWS Imagine (the Map, pending); Coefficient Giving Capacity Building (the Cytonome navigator, pending); EA Funds LTFF (the Cytonome navigator, pending); Coefficient Giving Career Development and Transition (PI sustainment, pending); ARPA-H PHO (planned, post-pilot).

---

## About Your Request

### Physical node
**Which node?** Bay Area.
**For how long?** 18 months: April 1, 2026 to September 30, 2027.
**Who?** Full-time (4 to 5 days/week): Shahin Mohammadi (PI). Part-time: 1 ML/Edge AI Engineer (hired with grant funding), 3 to 4 days/week during Phases 2 and 3. Visiting collaborators periodically.
**Total:** 1 to 2 regularly, occasionally 3.
**How to use the space:** physical office, co-working. (The PI is based in the Bay Area; in-person residency is a fit, not a constraint.)

**Contributing to the community:**
1. Quarterly open workshops on private local compute for sensitive health data (edge model deployment, on-device safety boundaries, consent architecture, differential privacy).
2. Weekly open office hours on foundation-model fine-tuning, single-cell analysis, multimodal fusion, and edge AI.
3. Inter-Node integration. Our Cytoplex safety boundary and open sensor-adapter protocol are designed to plug into other Node projects working on private or decentralized AI and on BCI/cognitive-state estimation. We will actively pursue at least two such integrations.
4. Shared infrastructure. All ML pipeline templates, sensor-integration code, and deployment configs documented and shared as open-source toolkits.
5. Neurotechnology Seminar Group participation.

**Workshop participation:** Yes.

### How we plan to use the node and build community

**How we will use the space.** The PI is Bay-Area-based and will work from the Node 4 to 5 days a week for the full 18 months, making it the primary home of the project rather than an occasional drop-in. The ML/edge engineer hired on this grant works alongside the PI on-site through the build and pilot phases, and visiting collaborators (our clinical Co-Lead at McLean, our Senior Advisor at Purdue, and design partners from the neurodivergent and mental-health community) use the space for working sessions, pilot onboarding, and co-design. The Node becomes where the on-device stack is built, where the self-experimentation pilot is run, and where we host the people the work is for.

**What we will build with the community.** We want the Node to make private, on-device AI for sensitive data a shared, teachable practice rather than one project's private knowledge. We commit to: (1) quarterly open workshops on private local compute for sensitive health data, covering edge model deployment, on-device safety boundaries, consent architecture, and differential privacy, with runnable code; (2) weekly open office hours where any member can get hands-on help with foundation-model fine-tuning, single-cell analysis, multimodal sensor fusion, or edge AI, areas where the PI has two decades of depth; (3) open-sourcing every reusable primitive we produce (the Cytoplex safety boundary, the sensor-adapter protocol, ML pipeline templates, deployment configs) under Apache 2.0 and CC BY 4.0 so members can adopt them the day they ship.

**How we will contribute to a mission-aligned community.** Cytonome is deliberately built from interfaces other people can plug into. Cytoplex is an open execution-boundary protocol any agentic system can adopt, and the open sensor-adapter protocol lets any Node project working on private or decentralized AI, BCI, or cognitive-state estimation feed into or build on our stack. We will pursue at least two such integrations with other Node projects during the grant and document them as reference patterns. We will take part in the Neurotechnology and the Decentralized / Cooperative AI seminar groups, present our results and our failures openly, and help bring neurodivergent and mental-health voices, usually absent from neurotech rooms, into the Node's orbit. Our aim is that a researcher down the hall can take our safety boundary, our consent ledger, or our sensor protocol and stand up their own private, defensible on-device system without starting from scratch, which is the compounding, defense-first infrastructure Foresight's Nodes exist to seed.

### Funding
**Requesting funding?** Yes.
**Overhead?** No. 100% direct to project. Lean nonprofit, no indirect rate.
**PI sustainment:** the PI is sustained through the Coefficient Giving Career Development and Transition award and capped PI-effort lines in project grants; total PI compensation across all concurrent awards is capped at $165K/year to prevent duplication, so Foresight funds are 100% directed to project costs.
**Requested:** $67,500 in direct project costs. Compute is requested separately below as Node GPU-hours (in-kind), not cash.

#### Budget ($67,500 direct project costs)

| Line item | Amount | % |
|---|---|---|
| Core software build: ML/Edge engineer (6 mo), edge dev hardware, data infrastructure, IRB (North Star), travel, open-source infra, security review, contingency | $35,000 | 52% |
| Wearables: Oura Ring 4 (primary); optional Muse/Emotiv exploration | $12,000 | 18% |
| Phase 0 internal pilot (3 mo, 3 to 5 people) | $5,000 | 7% |
| Extended ML engineer (+3 mo, multimodal fusion + wearable SDKs) | $9,000 | 13% |
| External pilot participant compensation (20 to 30 x $150 to 225) | $4,500 | 7% |
| Additional contingency | $2,000 | 3% |
| **Total direct request** | **$67,500** | **100%** |

This budget delivers our first proprietary multimodal dataset, a validated fusion model, a 20 to 30 person external pilot, and publication-ready preliminary data for an ARPA-H PHO follow-on. The Phase 0 self-experimentation pilot is the single most de-risking step: it validates the multimodal pipeline on real humans before any external participant is enrolled, and produces the proprietary dataset that competitive follow-on proposals require.

### Moderate and ambitious versions of this request

Our requested amount is **$67,500** (the recommended scope). The work is staged so the open safety artifact ships first at any size, which lets us scale cleanly in either direction.

**Moderate (~$35,000, software-only).** Funds Phase 1 alone: we harden, document, and open-source the Cytoplex safety boundary and the on-device mental-state engine, validate clinical correlation retrospectively against PHQ-9/GAD-7, and release the models, training code, and open sensor-adapter protocol. This still ships the single most reusable safety artifact (Cytoplex) and a working on-device private-AI framework. It drops the wearables, the Phase 0 self-experimentation pilot, and the external pilot, so validation is retrospective only and no new proprietary multimodal data is generated.

**Recommended ($67,500).** Everything in moderate, plus multimodal fusion (voice plus Oura physiology), our first proprietary multimodal dataset from a 3-month internal self-experimentation pilot, and a 20 to 30 person external pilot. This is the version that produces the preliminary data an ARPA-H Proactive Health Office follow-on needs.

**Ambitious (~$150,000, clinical-scale acceleration).** Everything in recommended, plus: a larger, longer external pilot (60 to 100 participants across MDD, GAD, PTSD, and neurotypical controls, tracked for 6 months rather than 3); consumer EEG as a core modality rather than an optional stretch, validated alongside voice and physiology; a second ML/edge engineer so safety-hardening and the multimodal pipeline run in parallel, compressing the 18-month timeline toward 12; and a dedicated external security and red-team audit of the full private-compute stack, published openly. This version would let us enter the ARPA-H PHO cycle roughly a year earlier with prospective, multi-condition evidence in hand, and would let the open Cytoplex boundary ship with an independent security attestation that other Node projects could build on directly.

### Compute
**Requesting compute?** Yes.
**GPU-hours:** ~3,200 A100-equivalent, over 18 months.
- Phase 1 (M1-6): ~1,200 GPU-hr. Base fine-tune (LoRA + DPO), interpretability, distillation + quantization.
- Phase 2a (M7-9): ~700 GPU-hr. Multimodal fusion.
- Phase 2b (M10-12): ~800 GPU-hr. Validation + ablations.
- Phase 3 (M13-18): ~500 GPU-hr. Pilot analysis + personalization.
- GPU: A100 80GB sufficient; H100 preferred.

**Why local, private compute matters here:** the project's thesis is that clinically meaningful health AI can be developed end-to-end under data sovereignty. Training on third-party cloud creates the centralized honeypot the project exists to prevent. Training on Foresight local infrastructure keeps sensitive clinical dialogue off third-party clouds and produces reproducible, cloud-independent training instructions.

**Requirements:** 4x A100 80GB (or equivalent), 2 TB NVMe, Python/PyTorch/HuggingFace.

---

## Miscellaneous
**Consent to share with advisors:** Yes.
**Expedited processing needed:** No.
**Confidential information:** None.
**How did you discover this opportunity?** Foresight website and community network; resubmission following prior feedback.
**Seminar groups:** Neurotechnology; Decentralized AI / Cooperative AI; BCI (cross-collaboration interest).

### What changed since our prior application
This resubmission makes the project faithful to what we are actually building and shipping. (1) We renamed the project from "Neuroverse" to **Cytonome**, its true identity as the on-device Navigator of the Cytognosis platform. (2) We lead with the safety primitive we have actually built, the **Cytoplex execution boundary** (Cytoplex-Lite, 93 passing safety tests), as the reusable open artifact. (3) We reframed post-quantum cryptography, user-owned data pods (Solid), and privacy-preserving aggregation as hardening steps adopted where feasible on a working private-by-default baseline, rather than as prerequisites, so the safety value lands early and reliably. (4) We grounded every milestone in the shipped stack (on-device Gemma, Cytoplex, local store, voice and wearable signals via an open sensor protocol), with EEG as an optional exploration. (5) We made the in-person node fit explicit: the PI is Bay-Area-based.

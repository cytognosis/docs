# Coefficient Giving: Capacity Building RFP Application

Application Link: https://coefficientgiving.org/funds/navigating-transformative-ai/funding-for-work-that-builds-capacity-to-address-risks-from-transformative-ai/



**RFP applied to:** **Funding for work that builds capacity to address risks from transformative AI** (primary). Open to redirection to "Funding for programs and events on global catastrophic risk, effective altruism, and other topics" if Coefficient Giving determines it's a better fit.

**Funding request type:** **Organization.** Cytognosis Foundation, 501(c)(3), Delaware.

**Renewal or new grant:** **New grant.**

---

## Applicant

**First name:** Shahin
**Last name:** Mohammadi
**Email (long-lived):** mohammadi@cytognosis.org

---

## Funding request summary (<20 words)

Cytognosis Foundation requests $175,000 to build the open, on-device Cytonome safety layer as reusable AI-safety infrastructure.

---

## Funding period

**12 months** (July 1, 2026 to June 30, 2027). This is the minimum window to design, externally audit, ship, and seed adoption of the open Cytonome safety layer (Edge AI perception, Solid pod storage, PQC encapsulation, on-device duty-to-warn override, and peer-to-peer federated protocol) before centralized cognitive-AI deployment patterns become structurally entrenched.

We have scoped this as a 12-month ask rather than a 2-year ask because Cytognosis Foundation is a recently-founded (incorporated September 8, 2025) nonprofit without a prior Coefficient Giving or Open Philanthropy relationship. A 12-month milestone-gated grant gives both parties a clean review point for renewal.

---

## Description of activities over the funding period

### Why this matters now: three converging timelines

**1. Capability and defense inversion.** N-of-1 ML models can now decode human emotional states with up to 95% accuracy (Nan et al., *NPP Digital Psychiatry and Neuroscience* [a Nature Portfolio journal], May 2026; a pilot study; Cohen's *d* = -0.89 for depression alleviation under AI-guided lifestyle optimization). The Grotzinger et al. 2025 *Nature* result (DOI: 10.1038/s41586-025-09820-3) demonstrates that 66% of cross-disorder psychiatric variance reduces to a five-factor genomic structure across 14 disorders. The capability to map, predict, and behaviorally steer a human being at clinical-grade accuracy now exists in production. The defensive open-source infrastructure to prevent its capture does not.

**2. Population-scale exposure.** Mental disorders are now the leading cause of global years lived with disability (YLDs), at 17.3% of all-cause health loss and 1.17 billion prevalent cases worldwide (GBD 2023 Mental Disorders Collaborators, *Lancet*, May 2026). The April 2026 White House Executive Order on Accelerating Medical Treatments for Serious Mental Illness explicitly authorizes new agentic-AI clinical pathways, accelerating an already expanding deployment surface.

**3. Quantum + immutable-data timeline.** State and non-state actors are actively performing "Harvest Now, Decrypt Later" (HNDL) capture of encrypted human health time-series, with the explicit intention to decrypt via cryptanalytically relevant quantum computers within the decade. Brain connectomes and behavioral exposomes are the highest-value HNDL targets in existence because they are *immutable*: a leaked password can be rotated, a leaked cognitive baseline cannot.

The structural failure mode in current deployments is centralized custody itself. The May 2025 23andMe bankruptcy and consent crisis demonstrated that for-profit custody of immutable biological data collapses under fiduciary duty pressure: user consent parameters dissolve, private biological profiles become liquidatable assets. Standard federated learning does not solve this: the bulk aggregator remains vulnerable to gradient inversion, institutional coercion, and re-consent under restructuring. The trust collapse is not limited to small companies; it applies at every institutional scale.

### What we will build

The **Cytonome safety layer**: a reusable, open-source, post-quantum, edge-native, on-device navigator and safety layer. Cytonome is the privacy-first edge-AI Navigator within the Cytognosis GPS for Health platform, the platform that aims to intercept disease years before symptoms emerge, and the funded work builds its safety layer as public infrastructure, released under permissive Apache 2.0 (code, models) and CC BY 4.0 (documentation). Cytonome ensures that early interception never becomes surveillance. The layer is designed to be adopted by any future AI application that processes sensitive personal cognitive or psychological time-series. The four components below are reusable AI-safety primitives, and mental health is the first deployment context, not the only one.

#### Component 1: Zero-Custody Storage Core (Solid Personal Data Pods)
Full integration of the W3C Solid (Social Linked Data) specification as the storage layer. All raw multi-modal streams, including conversation transcripts, wearable physiology, and EEG/fNIRS prefrontal hemodynamics, are written into the user's cryptographically owned Solid personal data pod. Cytognosis Foundation operates as a **zero-custody entity** that is architecturally incapable of selling, pooling, or being legally compelled to surrender data we never possess. This eliminates the 23andMe-class systemic risk by construction. It ships with a published Solid pod schema for psychiatric and behavioral time-series, designed for reuse by other health AI projects.

#### Component 2: Localized Inference and Post-Quantum Security
Compact language models (Gemma 4 family, no more than 3B parameters) fine-tuned with LoRA and DPO for mental-state quantification, distilled and quantized for on-device inference via LiteRT and Flutter on consumer smartphones. All model-derived embeddings, federated learning gradients, and inter-pod traffic are encapsulated with NIST-approved post-quantum cryptographic (PQC) primitives (ML-KEM / Kyber for key encapsulation, and ML-DSA / Dilithium for signatures). Local inference is HNDL-resilient from day one rather than as a v2 retrofit.

```
[ multimodal sensors: speech · Oura · Muse S Athena ]
                  │
                  ▼
   [ on-device perception: Gemma 4 via LiteRT ]
                  │
                  ▼
[ sovereign storage: user-owned Solid personal data pod ]
                  │
                  ▼
   [ peer-to-peer federated learning · PQC-encapsulated gradients ]
```

#### Component 3: Edge-Native "Duty-to-Warn" Override
This is the core technical answer to the "unregulated AI therapist" crisis. General-purpose centralized cloud LLMs are being adopted by millions as ad-hoc therapists despite being non-HIPAA-compliant, lacking localized clinical guardrails, and documented in *JAMA* and elsewhere to reinforce harmful feedback loops and amplify suicidal ideation. Centralized models cannot safely execute a clinical "duty to warn," because doing so would require routing acute crisis data through corporate servers, creating a serious surveillance risk.

We resolve this with a cryptographic, **on-device** override module. When locally computed crisis markers (acute self-harm or suicidal-ideation indicators) cross a threshold, the layer bypasses the conversational agent and surfaces localized emergency resources (988 Suicide and Crisis Lifeline, and Crisis Text Line) and/or cryptographically alerts a pre-designated human proxy, **without ever exporting raw psychological or neural signals to a cloud environment**.

#### Component 4: Peer-to-Peer Federated Learning with Differential Privacy
A peer-to-peer (P2P) federated learning protocol replaces the bulk-aggregator topology of standard federated learning. Gradients are PQC-encapsulated, individual contributions are protected with explicit epsilon differential-privacy budgets, and no single node can reconstruct an individual's trajectory. This is the missing primitive for collective model improvement without re-introducing centralized custody.

### Activities timeline

| Quarter | Activities | Deliverables (all Apache 2.0 / CC BY 4.0) |
|---|---|---|
| **Q1 (M1–3)** | Open protocol specification across all 4 layers (Edge, Solid, PQC, P2P Federated). Crisis-detection module and bias-audit framework. IRB submission via North Star. Hire 1.0 FTE Edge AI / PQC Engineer. | Layered protocol spec; crisis-detection module v0; bias-audit framework v0; North Star IRB submitted. |
| **Q2 (M4–6)** | Gemma 4 fine-tuning (LoRA + DPO) for mental-state quantification; edge distillation + quantization via LiteRT; Solid pod schema for psychiatric time-series; PQC integration into edge embedding + federated channels; external cryptographic red-team kickoff. | Edge model v1 (open weights + adapters); Solid pod schema; PQC reference implementation. |
| **Q3 (M7–9)** | Internal multimodal pilot with core team (3–5 people) generating proprietary multimodal dataset; on-device duty-to-warn override engineering; external red-team findings ship as published threat model. | Multimodal fusion model v1; on-device duty-to-warn module; published threat model. |
| **Q4 (M10–12)** | 20–30 person external pilot (MDD, GAD, PTSD, neurotypical); peer-to-peer federated protocol deployment; full open-source release; ARPA-H PHO and NSF Tech Labs follow-on submissions. | Cytonome safety layer v1.0, full open-source release; published pilot results; demographic performance cards (NeuroGAP-anchored). |

### What "success" looks like at M12

- **Engineering gates:** Edge model r > 0.6 against PHQ-9 / GAD-7 / PSS-10 / PCL-5; edge inference latency < 300ms; at least 95% parity versus cloud inference; zero raw-signal cloud egress under threat-model audit.
- **Open-source adoption:** At least one unrelated open-source or academic project integrates at least one Cytonome layer primitive (Solid pod schema, PQC edge module, on-device duty-to-warn, or P2P federated protocol) into its own production stack within 6 months of release.
- **Ecosystem reuse:** Quarterly published workshop with the Foresight Institute Bay Area Node, the EA-aligned AI safety community, and the BlueDot Impact alumni network, demonstrating the Cytonome layer components on their own use cases.
- **Pilot results:** 20–30 person external pilot demonstrates continuous multimodal monitoring detects clinically meaningful changes that periodic assessment misses, with full demographic-performance cards.

### Why this builds capacity for AI safety beyond mental health

The four Cytonome layer components are deliberately designed as **reusable open-source AI safety primitives**, not a mental-health product. Any future AI application that processes sensitive personal cognitive or psychological time-series, including clinical decision support, education, workforce wellbeing, content moderation, and behavioral nudging, will need exactly this defensive layer. By shipping it as Apache 2.0 and CC BY 4.0 public goods, this grant builds defensive capacity across the frontier AI ecosystem, and not just at Cytognosis. This is field-building for AI safety and a deliberate organizational-capacity build at a recently-founded nonprofit.

---

## Total funding requested

**Total request: $175,000 USD over 12 months** (mainline scenario, including a PI architect effort line tied to PI effort designing the Cytonome safety layer; see Budget section for rationale).

**Minimal scenario: $90,000 USD over 12 months.** This drops the external cryptographic red-team ($22K) and the external 20–30 person pilot ($10K, with the ecosystem scaling buffer reduced). It delivers the open-source Cytonome layer and Phase 0 internal pilot under retrospective and internal validation only. It still ships every defensive primitive, but without the external security audit publication and without prospective multimodal validation.

**Ambitious scenario: $200,000 USD over 12 months.** This adds a 0.25 FTE part-time clinical safety advisor, a deeper external red-team budget ($40K total), and seed funding for two open-source maintainer micro-grants ($10K) to accelerate downstream adoption.

---

## Budget

[TO FINALIZE AT SUBMISSION]

### Mainline budget: $175,000

| Category | Amount | % | Programmatic mapping |
|---|---|---|---|
| **PI architect effort (Cytonome safety layer)** | $45,000 | 25.7% | PI Shahin Mohammadi, 0.3 FTE x 12 months at the board-approved fully-loaded rate of $165,000/year. Covers architectural design, safety-specification leadership, and integration oversight of the Cytonome safety layer. This is partial PI effort, coordinated and capped per the coordination clause below, and does not duplicate other funded sources. |
| **Core software engineering** | $72,000 | 41.1% | 1.0 FTE Edge AI / PQC Software Engineer x 12 months. LiteRT multi-agent pipeline, Solid pod APIs, NIST PQC integration (ML-KEM, ML-DSA), peer-to-peer federated protocol, on-device duty-to-warn override. Below-market nonprofit rate ($6K/month direct, fringe absorbed). |
| **PQC + Solid security audit** | $22,000 | 12.6% | External cryptographic and privacy red-team. Membership-inference defense validation, gradient-inversion attack testing on the P2P federated layer, quantum-resistance verification of PQC primitives. Published threat model ships open-source. |
| **Local verification infrastructure** | $13,000 | 7.4% | NVIDIA DGX Spark + Mac Studio dev machines + sensor units for prospective validation (Oura Ring 4 x10, Muse S Athena x5, Emotiv Insight x5). Avoids cloud-honeypot training for sensitive clinical dialogue and physiological data. |
| **External 20–30 person pilot** | $10,000 | 5.7% | Participant compensation ($150–225 x 20–30); recruitment infrastructure; clinical assessment kits; North Star IRB review and amendments. |
| **Ecosystem scaling + adoption** | $10,000 | 5.7% | Quarterly open workshops; documentation; conference presentations (OHBM, NeurIPS, Hugging Face Open Source AI); contributor onboarding for early adopters. Includes the explicit operational contingency buffer (LTFF/EA-style 10% guidance applied here in line with funder operational expectations). |
| **Indirect / overhead** | $3,000 | 1.7% | Organizational insurance, lean data hosting, compliance frameworks (FAIR / SPDX / REUSE), accounting. |
| **Total** | **$175,000** | **100%** | |

### PI compensation coordination clause

The PI line in this budget is partial (the ~$45K architect effort described above), not 100% of PI compensation. The PI is 1.0 FTE total, and PI compensation is capped across all funded sources, per the following coordination clause applied to every active application:

> The PI is compensated as 1.0 FTE at a fully-loaded, board-approved rate of $165,000/year, approximately 65% of the PI's prior market salary. Total PI compensation across all funded sources is capped at this amount in any 12-month period. Where awards overlap, PI-effort lines in project grants are reduced and reallocated to non-PI direct costs, and the Career Development and Transition award (if held) is reduced to the level needed to reach the runway floor. This prevents duplicative compensation while ensuring the PI's full-time effort is sustained if any single source funds.

### Reasoning on rates and benchmarks
- PI architect rate ($45K, 0.3 FTE, 12 months) derives from the board-approved fully-loaded rate of $165,000/year. This is approximately 65% of the PI's prior $255K market salary and is documented as reasonable compensation for a 501(c)(3) scientist-CEO. This line is partial PI effort and is coordinated and capped per the clause above.
- Engineer rate ($6K/month direct, $72K/year) is below 2026 Bay-Area market for senior Edge AI and cryptography engineers (Pave and levels.fyi reference $180K+ base for comparable roles). We make this work via the foundation's open-source mission and the ability to publish Apache 2.0 reference implementations.
- External red-team rate ($22K) is benchmarked against 2026 published Trail of Bits and NCC Group rates for comparable scope.
- Indirect rate (1.7%) is intentionally well below the 10–15% nonprofit indirect rate typical for institutional grants, because we route maximum funds to direct project costs.
- **Budget option chosen:** The $175,000 mainline sits well within the $200,000 ambitious ceiling. This is cleaner than trimming the engineer line below the $6K/month floor needed to attract a qualified PQC engineer, and it preserves the full security audit scope essential for credible open-source adoption. A $90,000 minimal variant and a $200,000 ambitious variant are described in the Total funding requested section.

---

## Runway

Cytognosis Foundation is currently in its bootstrap stage. The PI operates without salary, sustained by PI runway routed through the Career Development and Transition application ($165,000) plus capped PI-effort lines in project grants, under the coordination cap described above. The organization has approximately 3–6 months of operational runway at the current burn rate. The Career Development and Transition grant (Coefficient Giving, individual, $165,000) and the EA Funds Long-Term Future Fund (LTFF) application serve as fast personal-runway bridges across the runway cliff. This Capacity Building grant funds the org build, meaning the engineering hire and open-source infrastructure that the PI alone cannot deliver. This three-layer structure, with Career Transition as floor, LTFF as bridge, and Capacity Building as org enabler, removes the single-point-of-failure risk that a single grant decision could halt progress.

This Capacity Building grant, together with the parallel applications listed below, is the operational bootstrap for the foundation. Without it, the technical engineering hire (Core Software Engineering, $72K) cannot be made, and the open-source Cytonome layer ships at a 9–12 month slower pace.

---

## University student-focused project?

**No.**

---

## Track record

### Scientific track record (PI)
- **Ruzicka WB, Mohammadi S, et al. (2024).** Single-cell multi-cohort dissection of schizophrenia. *Science* 384(6698). **Co-first author.**
- **Mathys H, Davila-Velderrain J, Mohammadi S, et al. (2019).** Single-cell transcriptomic analysis of Alzheimer's disease. *Nature* 570, 332–337. (Mohammadi contributed to this work.)
- **Emani PS, … Mohammadi S, … Davila-Velderrain J, et al. (2024).** PsychENCODE single-cell genomics across 388 human brains. *Science* 384(6698).
- **Han X, Mohammadi S, et al. (2024).** Single-cell multi-cohort transcriptomic dissection of bipolar disorder. *European Neuropsychopharmacology* 87, 48. **Co-first author.**
- **Menon M, Mohammadi S, et al. (2019).** Single-cell transcriptomic atlas of the human retina identifies cell types associated with age-related macular degeneration. *Nature Communications* 10, 4902. **Co-first author.**
- **Mohammadi S, Davila-Velderrain J, Kellis M. (2020).** A multiresolution framework to characterize single-cell state landscapes. *Nature Communications* 11, 5399. **Co-first author.** (ACTIONet.)
- Over 40 peer-reviewed publications; approximately 4,000+ citations (Google Scholar).

### Open-source track record
- **ACTIONet** (github.com/shmohammadi86/ACTIONet, Apache 2.0). Single-cell analysis framework used across the psychiatric-genomics consortia (PsychENCODE, ROSMAP, and PsychAD). This is exactly the kind of reusable open-source primitive that becomes infrastructure for the field, and it is what we are now building at the AI-safety layer.
- **ACTION** (github.com/shmohammadi/ACTION). Archetypal analysis for multi-omic data.

### Team
- **PI Shahin Mohammadi, PhD.** 20 years building AI for biological systems across MIT, Broad Institute, Purdue, insitro, and GenBio AI.
- **Brad Ruzicka, MD/PhD, Co-Lead.** Assistant Professor, McLean Hospital / Harvard Medical School; co-first author with the PI on the single-cell schizophrenia atlas (Ruzicka, Mohammadi et al., Science 2024); Harvard Brain Tissue Resource Center / NeuroBioBank liaison; anchors clinical validation, the IRB pathway, and clinical ground truth.
- **Senior Scientific Advisor Ananth Grama, PhD.** Samuel Conte Distinguished Professor and Director of the Institute for Physical AI, Purdue University. Foundation-model architecture and scalable, distributed compute.

### Organizational track record (honest)
Cytognosis Foundation is a recently-founded 501(c)(3) (incorporated September 8, 2025) without prior external grants. This would be our first organizational grant from Coefficient Giving. The relevant track record is therefore the PI's individual research and open-source record above, plus the demonstrated ability of ACTIONet to become adopted infrastructure across major brain consortia. That is exactly the trajectory we are now executing at the AI-safety primitive layer.

### Public benefit / charitable purpose (2–3 sentences)

The Cytognosis Foundation will use this grant to design and release the open Cytonome safety layer, a reusable, post-quantum, edge-native cryptographic defense layer that any future AI application processing sensitive cognitive or psychological data can adopt, free of charge, under permissive Apache 2.0 and CC BY 4.0 licenses. This directly serves the public benefit by establishing defensive infrastructure against algorithmic cognitive manipulation, centralized biotype capture, and quantum-vulnerable harvest of immutable human health data, which are risks that disproportionately affect populations with the least capacity to defend against them. The released primitives are designed for reuse by other AI safety researchers, open-source maintainers, and institutional health AI deployments.

---

## Alternatives to funding

In the last 6 weeks we have submitted concurrent applications across the highly adjacent safety networks:

| Funder | Scope | Amount | Status |
|---|---|---|---|
| **Google.org Impact Challenge: AI for Science** | Organizational, Cytoverse Neuro v1.0 (connectomic + phenotype core) | $2,490,000 / 36 months | Pending (expected decision Q3 2026) |
| **Foresight AI for Safety and Science Nodes 2026** | Organizational, Bay Area Node defensive layer | $45,000–$75,000 / 18 months | Pending (resubmission, May 2026) |
| **EA Funds, Long-Term Future Fund (LTFF)** | Organizational, technical AI safety primitives | $120,000–$130,000 / 9 months | Pending (May 2026) |
| **AWS Imagine Grant** | Organizational, Cytoverse foundation model | $148,500 cash + $100,000 credits / 9 months | Pending (May 2026) |
| **Coefficient Giving, Career Development and Transition Funding** | Individual, PI personal runway / transition stipend | $165,000 | Pending (May 2026) |

Each application is **sized for the specific scope of work that funder uniquely supports**, and the concurrent applications are not duplicative. The Career Development and Transition grant carries the full PI runway floor ($165,000). PI-effort lines in project grants (including this one) are coordinated and capped as described in the budget section above.

**If Coefficient Giving does not fund the organizational request:** The engineering hire required to ship the open-source Cytonome layer at full velocity is delayed by 9–12 months while we wait for the larger Google.org determination. The core team would split focus between the technical build and additional fundraising and consulting to bridge the gap. The defensive primitives still ship, just on a slower timeline, during which centralized cloud LLMs continue to harvest immutable cognitive data into non-quantum-safe corporate silos with no localized clinical guardrails.

---

## Anything else

The deliberate choice to structure Cytognosis as a 501(c)(3) nonprofit rather than a venture-backed for-profit is load-bearing for the funding case. A for-profit framework would have made capitalization substantially easier, but the May 2025 23andMe collapse demonstrated that for-profit custody of immutable biological data fails the moment fiduciary duty pressure overrides user consent. Brain connectomes and behavioral exposomes are even less recoverable than genomes. Operating as an impact-first nonprofit is the institutional analogue of operating as a zero-custody data architecture: structural integrity, not stated good intent. This is also why the entire Shield Stack ships under Apache 2.0 by construction, and why the foundation's infrastructure is incapable of being commercialized into a closed surveillance product even under future leadership changes.

---

## Confidential information

None we wish to redact. The concurrent application list above is consistent across all active funders.

---

## Referral to other funders

**Yes.** Please refer if Coefficient Giving determines a better fit elsewhere (e.g., your technical AI safety team, AI governance team, or other private AI safety donors).

---

## Grant logistics

### Location of grant activities
**Primary:** USA (Cambridge, MA + Bay Area, CA).
**Secondary collaborator nodes:** Italy (Human Technopole Milan); USA (Purdue West Lafayette).

### Address of grant recipient
Cytognosis Foundation, [TO FINALIZE AT SUBMISSION]. Mailing address: [TO FINALIZE AT SUBMISSION].

### Payment defaults
**Single payment for no more than 1-year grants.** Yes, this works for us.

### Prior Coefficient Giving (Open Philanthropy) funding?
**No.** This is our first application.

### Minimum standards compliance
We commit to bringing organizational policies into compliance with the minimum standards described in the Coefficient Giving Minimum Standards document as soon as practicable, and no later than by the time of any potential renewal application.

---

## How did I hear about this opportunity?

Coefficient Giving program documentation (Capacity Building RFP page on openphilanthropy.org); cross-referenced from the Career Development and Transition Funding page submitted in parallel.

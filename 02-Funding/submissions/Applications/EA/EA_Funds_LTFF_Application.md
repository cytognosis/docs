# EA Funds Grant Application

Application Link: https://funds.effectivealtruism.org/apply-for-funding

**Primary fund:** Long-Term Future Fund (LTFF)
**Secondary fund (transfer OK):** EA Infrastructure Fund (EAIF): Yes
**Prior Open Philanthropy / Coefficient Giving funding:** None. We have coordinated, non-overlapping applications in review with Coefficient Giving (Capacity Building, and a personal Career Development and Transition request); see Alternatives to Funding.

---

## Basic information

**Name:** Shahin Mohammadi
**Organization name:** Cytognosis Foundation (501(c)(3), Delaware)
**Main collaborators:** Brad Ruzicka, MD/PhD, Co-Lead (Assistant Professor, McLean Hospital and Harvard Medical School; co-first author with the PI on the single-cell schizophrenia atlas, Ruzicka, Mohammadi et al., *Science* 2024; Harvard Brain Tissue Resource Center and NeuroBioBank liaison; anchors clinical validation, the IRB pathway, and clinical ground truth); Ananth Grama, PhD (Director, Institute for Physical AI, Purdue University); Jose Davila-Velderrain, PhD (Group Leader, Computational Neuroscience, Human Technopole Milan).
**Email:** mohammadi@cytognosis.org
**Previously employed/contracted by Effective Ventures or projects:** No.

---

## Project information

### Short description (≤120 characters)

Open-source on-device verifiability and deployment-control layer for high-stakes AI, validated first in mental health.

### Summary (≤1,000 characters)

Personal-AI capability has outrun its verifiability. N-of-1 models now match clinician coach-assignment at up to 95% accuracy (Nan et al., NPP Digital Psychiatry and Neuroscience, 2026, n=40), yet millions use cloud LLMs as ad-hoc therapists with no way to check a claim, no deployment control, and no recourse once immutable cognitive data is captured. We build two open-source primitives: Cytoverse, interpretable-by-design representations that make outputs falsifiable (verifiability); and Cytoplex, an on-device control layer that blocks unverified clinical claims, enforces calibrated uncertainty, refuses out-of-distribution inputs, and resists manipulative optimization (93 passing safety tests today). Zero-custody storage (Solid pods, NIST post-quantum crypto) keeps the layer from becoming a surveillance vector. Mental health is the first, highest-stakes deployment; the primitives generalize. This $250K, 12-month grant ships both under Apache 2.0 with a public benchmark.

### Project goals: actions, impact, and theory of change

#### What the world looks like without this project

The capability-versus-verifiability gap in personal AI has inverted. On the capability side:
- N-of-1 ML models match clinician coach-assignment at up to 95% accuracy and reduce depression with Cohen's d = -0.89 (Nan et al., *NPP Digital Psychiatry and Neuroscience*, a Nature Portfolio journal, Vol. 4, Article 10, DOI 10.1038/s44277-026-00062-3, 19 May 2026; pilot study, n=40).
- Multi-disorder genomic modeling resolves psychiatric variance into a five-factor structure across 14 disorders, explaining roughly 66% of genetic variance (Grotzinger et al., *Nature*, 10 Dec 2025, DOI 10.1038/s41586-025-09820-3).
- Mental disorders are the single largest contributor to global years lived with disability, at 17.3% (GBD 2023), 1.17 billion prevalent cases worldwide. Recent US policy explicitly authorizes new agentic-AI clinical pathways.

On the defense side: almost nothing. Centralized cloud LLMs are adopted as ad-hoc therapists at population scale, despite being non-HIPAA-compliant, lacking deployment controls, and documented to reinforce harmful feedback loops and amplify suicidal ideation. There is no standard way to verify a model's claim, to make it refuse when out of its depth, or to stop it optimizing for engagement over the user's interest. The 23andMe bankruptcy showed that for-profit custody of immutable biological data is one asset-liquidation event from collapse, and because brain connectomes and behavioral exposomes are immutable, they are prime targets for "Harvest Now, Decrypt Later" quantum capture.

Without open-source verifiability and deployment-control primitives shipped before this becomes pervasive, a small number of centralized actors hold the deepest map of human cognition ever assembled, with no architectural recourse. This is a tractable long-term AI-risk vector with a clear, time-critical defensive intervention.

#### What we will build (12-month sprint)

A reusable, open-source, on-device safety layer released under Apache 2.0, organized around two pillars, with privacy as supporting infrastructure. The work is the defensive core of Cytonome, the Navigator layer of Cytognosis's platform (Cytoverse is the Map; Cytoscope is the Sensor; Cytonome is the Navigator). Mental health is the first deployment because the capability-versus-defense gap is widest there and the harm from data capture is least reversible; the primitives are domain-general.

**Pillar 1, verifiability (interpretable-by-design).** Cytoverse represents a model's state on transparent biological axes rather than opaque embeddings, so an output can be falsified, audited, and checked against named, inspectable factors. We add faithfulness checks and activation monitoring so that what the model reports tracks what it computes.

**Pillar 2, deployment control.** Cytoplex is an on-device control layer that (a) blocks unverified clinical claims, (b) enforces calibrated uncertainty and refuses out-of-distribution inputs, (c) resists manipulative reward optimization, and (d) provides an on-device duty-to-warn override that surfaces local crisis resources (for example, the 988 Suicide and Crisis Lifeline) without exporting raw signals. It ships with a control-evaluation suite (currently 93 passing safety tests), which we expand into a public benchmark.

**Supporting infrastructure, zero-custody privacy.** All streams are written to the user's cryptographically owned Solid pod; Cytognosis is architecturally incapable of pooling or surrendering data it never holds. NIST post-quantum cryptography (ML-KEM, ML-DSA) encapsulates embeddings, gradients, and inter-pod traffic, making the data Harvest-Now-Decrypt-Later-resilient. A peer-to-peer federated protocol with explicit differential-privacy budgets removes the bulk-aggregator honeypot. These keep the safety layer from becoming a surveillance vector.

Existing privacy-preserving ML tools address encryption and gradient protection in isolation. Our additive contribution is wiring verifiability and on-device deployment control into a single deployable primitive for continuous biopsychological streams, with a published control-evaluation benchmark.

#### How we will know we have succeeded

- **M6 go/no-go:** the edge-quantized model achieves r > 0.6 against PHQ-9, GAD-7, PSS-10, and PCL-5 on held-out clinical data, and the control suite blocks a defined set of unverified-claim and manipulation probes.
- **M12 release:** full Apache 2.0 release, including the verifiability representations, the Cytoplex control layer and its public control-evaluation benchmark, on-device duty-to-warn, Solid pod schemas, the post-quantum reference implementation, the peer-to-peer federated protocol, and demographic bias-audit cards.
- **Adoption at M+6:** at least one other group (academic, open-source, or AI-safety-aligned) integrates at least one primitive (the control-evaluation suite, the verifiability representations, the Solid schema, or the on-device override) into its own stack.

#### Path to impact and fund alignment

LTFF's core remit is mitigation of global catastrophic risks, especially from transformative AI. This project addresses two specific risk vectors and contributes reusable infrastructure beyond them.

- **Algorithmic cognitive manipulation.** Systems with high-fidelity behavioral models of a person are the most direct technical foundation for automated psychological coercion at scale. On-device deployment control and verifiability are tractable, ship-now defenses.
- **Biotype capture.** Immutable cognitive and connectomic data, once captured centrally, cannot be un-captured. This is the rare AI-risk vector where the defensive infrastructure cannot be retrofitted; it must exist before the data is generated.

Beyond direct impact, the verifiability and deployment-control primitives are reusable by the AI-safety community for any application processing sensitive personal time-series, which is epistemic-security and infrastructure work consistent with EAIF's remit if LTFF managers judge it a better fit there.

### Track record

#### Research and publications (PI)
Publication strength: one *Science*, one *Nature*, three *Nature Communications*; 40+ publications, ~4,800 citations.
- **Ruzicka WB, Mohammadi S, et al. (2024).** Single-cell multi-cohort dissection of schizophrenia. *Science* 384(6698). **Co-first author.** doi.org/10.1126/science.adg5136
- **Mathys H, Davila-Velderrain J, Mohammadi S, et al. (2019).** Single-cell transcriptomic analysis of Alzheimer's disease. *Nature* 570, 332-337. Contributed to the first single-cell Alzheimer's atlas (5th author).
- **Emani PS, ... Mohammadi S, et al. (2024).** PsychENCODE single-cell genomics across 388 human brains. *Science* 384(6698).
- **Han X, Mohammadi S, et al. (2024).** Single-cell multi-cohort dissection of bipolar disorder. *European Neuropsychopharmacology* 87, 48. **Co-first author** (WCPG conference abstract).
- **Menon M, Mohammadi S, et al. (2019).** Human retina atlas identifying cell types associated with AMD. *Nature Communications* 10, 4902. **Co-first author.**
- **Mohammadi S, Davila-Velderrain J, Kellis M. (2020).** A multiresolution framework to characterize single-cell state landscapes (ACTIONet). *Nature Communications* 11, 5399. **Co-first author.** doi.org/10.1038/s41467-020-18416-6

#### Open-source infrastructure
- **ACTIONet** (github.com/shmohammadi86/ACTIONet, Apache 2.0): single-cell analysis framework used across the psychiatric-genomics consortia (PsychENCODE, ROSMAP, PsychAD) whose data underpin this work.
- **ACTION** (github.com/shmohammadi86/ACTION): archetypal analysis for multi-omic data.

#### Team strength
- **PI Shahin Mohammadi:** 20 years building AI for biological systems across MIT, the Broad Institute, Purdue, insitro, and GenBio AI.
- **Brad Ruzicka, MD/PhD, Co-Lead:** Assistant Professor, McLean Hospital and Harvard Medical School; co-first author with the PI on the schizophrenia atlas; anchors clinical validation, the IRB pathway, and clinical ground truth.
- **Senior Scientific Advisor Ananth Grama:** Samuel Conte Distinguished Professor and Director of the Institute for Physical AI at Purdue; foundation-model architecture and scalable, distributed compute.

#### Organizational track record and expenditure
- Cytognosis Foundation: 501(c)(3) incorporated in Delaware. The PI founded it and became Founder/CEO in October 2025. The organization has run on PI self-funded runway to date: $0 grant revenue and 1 FTE in 2025 (Q4 onward) and 2026 to date. This would be our first external research grant.
- PI compensation is coordinated across sources (see the coordination clause in the budget). The LTFF request includes a capped, org-side PI research line for direct safety-research effort, so the engineering sustains itself even if the personal Career Development and Transition request is slow or declined.

#### Honest weaknesses
- We are a recently founded nonprofit (Oct 2025) with no prior grants; the track record is the PI's individual research record, not the organization's.
- Technical AI safety is a career pivot for the PI from computational neuroscience. It is supported by deep adjacent expertise and foundation-model architecture work under Grama at Purdue IPAI, and the domain we intervene in is exactly where the PI is world-class, but it is a pivot, not a long history of EA-community AI-safety work.
- The duty-to-warn override needs design review with crisis-response experts to avoid false-positive harm; we have budgeted engineering and IRB time and seek pro bono advisor connections.
- **Single-founder, key-person risk.** The Foundation currently has one full-time person. Continuity depends on Co-Lead Brad Ruzicka and advisor Ananth Grama; we are expanding the board and advisory board in 2026 to distribute governance and scientific oversight.

### Public portfolio
- **Org:** cytognosis.org
- **LinkedIn:** https://www.linkedin.com/in/shmohammadi/
- **GitHub:** github.com/shmohammadi86 (ACTIONet, Apache 2.0)
- **Open-access flagship:** Ruzicka, Mohammadi et al., *Science* 2024, doi.org/10.1126/science.adg5136

---

## Funding

### Funding amount and breakdown

**Total requested: $250,000 (mainline), over 12 months.** A **$130,000 floor** (PI-only) and a **$320,000 stretch** are described below.

**Mainline budget ($250,000):**

| Line item | Amount | % | Notes |
|---|---|---|---|
| PI compensation (0.7 FTE x 12 mo at $165K/yr fully loaded) | $115,500 | 46% | Direct safety-research effort: verifiability representations, control-evaluation design, calibrated-uncertainty and duty-to-warn architecture. Board-approved $165K/yr loaded rate (~65% of prior market salary). Coordinated and capped across all awards. |
| Edge / ML engineer (1.0 FTE x 12 mo) | $100,000 | 40% | Distillation, quantization, on-device control-layer integration, faithfulness and activation-monitoring tooling, post-quantum integration. Mission-driven nonprofit rate, below Bay Area market. |
| Validation hardware | $15,000 | 6% | Wearables (physiology) and edge dev devices for prospective multimodal validation. |
| Open-source infrastructure, IRB, data, CI | $6,000 | 2.4% | North Star IRB review, encrypted local storage, dataset access, Hugging Face hosting, docs, model cards. |
| Contingency (~10% of non-PI direct) | $13,500 | 5.4% | Hardware procurement risk and control-evaluation or red-team scope expansion. |
| **Total request** | **$250,000** | | 0% indirect. |

**PI compensation coordination clause.** The PI is compensated at a fully loaded, board-approved rate of $165,000/year. Total PI compensation across all funded sources is coordinated and capped within fair market (and below the NIH cap of $228,000) in any 12-month period; where awards overlap, project PI-effort lines are reduced and reallocated to non-PI direct costs. The personal Career Development and Transition request to Coefficient Giving covers personal transition runway; this LTFF line covers org-side research effort. Nothing is double-paid.

**Why a 10% contingency is structurally appropriate:** LTFF guidance notes that applicants systematically underestimate real costs. The largest risks here are hardware procurement (medical-grade sensors can ship late or defective) and red-team scope expansion if early control-evaluation findings warrant deeper investigation.

I am applying on behalf of Cytognosis Foundation; the grant can flow to the Foundation directly. The PI compensation line accounts for applicable employment taxes; the organization operates as a 501(c)(3) W-2 employer for the PI.

#### Floor scenario ($130,000)
PI-only. Delivers the software verifiability layer and the Cytoplex control suite with its public benchmark, validated retrospectively, released under Apache 2.0. Drops the engineer, most hardware, and prospective validation. A $130K PI-only award is already in the top ~15% of LTFF grants by size and ships the core safety primitives.

#### Stretch scenario ($320,000)
Mainline plus an external security and control-evaluation red-team ($30K), a 3-month runway buffer for PI and engineer ($25K), and a small prospective validation pilot of 20–30 participants ($15K) to convert retrospective into prospective validation, which strengthens follow-on federal proposals.

Budget spreadsheet (LTFF template): linked at submission, "anyone with the link can view," with comment access to funds@effectivealtruism.org.

### Requested amount (USD)
$250,000 (mainline).

### Organizational budget (USD)
Cytognosis Foundation FY2026 operating budget to date is PI self-funded runway; this LTFF grant would be the first external research grant. Coordinated, non-overlapping requests in review include a personal Career Development and Transition stipend ($62,500, tracked separately as personal income) and a Capacity Building request (organizational infrastructure). As a lean nonprofit with 0% indirect, roughly 92% of every funded dollar flows to direct project costs (PI and engineer effort, hardware, validation).

### Alternatives to funding

These applications are coordinated; each funds a distinct scope, and PI effort and compensation are coordinated so nothing is double-paid.

| Funder | Scope | Amount | Relationship |
|---|---|---|---|
| Coefficient Giving, Career Development and Transition | PI personal transition runway | $62,500 / 6 mo | Personal income only; does not fund this build. |
| Coefficient Giving, Capacity Building | Organizational infrastructure to harden the layer into reusable tooling | organizational scale / 12 mo | Different deliverables; no overlap with this sprint. |
| **EA Funds LTFF (this request)** | The 12-month verifiability and deployment-control sprint (engineer, hardware, org-side PI research line) | $250,000 | The engineering core. |

**If LTFF does not fund:** the project proceeds 9–12 months slower, with the PI splitting time into private computational-biology consulting to preserve continuity. The verifiability and deployment-control primitives still ship, just later, leaving a wider window in which centralized conversational models continue to capture immutable cognitive data with no verifiability or control. Unrelated domain-science and compute funding for other parts of the platform is pursued on separate tracks that do not overlap this PI effort or these deliverables.

### Use for additional funding

If awarded more than requested, marginal funds would, in priority order: (1) extend the engineer to support a deeper external red-team and a published threat model; (2) fund the prospective validation pilot; (3) expand the control-evaluation benchmark with additional manipulation and faithfulness probes; (4) reserve the remainder as organizational runway during the bootstrap phase.

---

## Further information

**Confidential information:** None we wish to redact. The coordinated application list above is consistent across the related funders.

**LinkedIn / CV:**
- PI: https://www.linkedin.com/in/shmohammadi/
- PI GitHub: github.com/shmohammadi86
- Org: cytognosis.org

**Start date:** flexible, on funding (target Q4 2026).
**End date:** 12 months from start (compressible to a 9-month version at the floor).
**Requested currency:** USD.

**Location:** Operating from Daly City and the Bay Area, CA, USA; implemented in the USA, with collaborator nodes in Milan (Human Technopole) and West Lafayette (Purdue IPAI).

**Activities in China or India:** No.
**Award in recognition of past achievement:** No.
**People under 18 contributing:** No.
**Lobbying / political activity:** None.

**References:**
- **Ananth Grama, PhD:** Director, Institute for Physical AI, Purdue University; Senior Scientific Advisor to Cytognosis. Foundation-model architecture, scalable compute, and the PI's technical judgment.
- **Jose Davila-Velderrain, PhD:** Group Leader, Computational Neuroscience, Human Technopole Milan. Project design and the PI's research track record.

**Organisational leadership:** Cytognosis Foundation, Board of Directors: Shahin Mohammadi, PhD (President/CEO). Additional directors and advisory-board members are being recruited in 2026, targeting at least three additional governance members by year end, which directly mitigates single-founder risk. Senior Scientific Advisor: Ananth Grama, PhD. Clinical Co-Lead: Brad Ruzicka, MD/PhD.

**Referral to other funders:** Yes.
**How did you hear about EA Funds?** Coefficient Giving program documentation referenced EA Funds for individuals; followed cross-references to LTFF and EAIF.
**Time-sensitive grant:** Soft yes. Earlier funding accelerates the defensive timeline against ongoing capture of high-fidelity health time-series, but there is no hard deadline.
**Public reporting:** Public; happy to have a public grant report.
**Network sharing:** Yes, open to job opportunities, mentorship, and connections for the team.
**Grant reporting:** Confirmed; 6-month progress report and a final report.

### Anything else?

Structuring Cytognosis as a 501(c)(3) rather than a venture-backed for-profit is load-bearing. A for-profit framework would have made capitalization easier; we rejected it because the 23andMe collapse showed that for-profit custody of immutable biological data fails under fiduciary pressure, and because operating impact-first is the institutional analogue of a zero-custody data architecture: structural integrity, not stated good intent. The entire stack ships under Apache 2.0 by construction, so the verifiability and deployment-control primitives cannot be closed into a surveillance product even if the Foundation's leadership were replaced.

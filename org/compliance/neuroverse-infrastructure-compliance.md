# Neuroverse Infrastructure Compliance: What the Four Sources Actually Require

**Document owner:** Shahin Mohammadi, CEO, Cytognosis Foundation **Audience:** Internal; shared with Duane and infrastructure decision-makers **Status:** Working reference for SAE design decisions

------

## 1. The Four Sources

### 1.1 NIST SP 800-66 Rev. 2 (February 2024)

**Title:** Implementing the HIPAA Security Rule: A Cybersecurity Resource Guide **Author:** Jeffrey Marron, NIST **Status:** Final, supersedes Rev. 1 from 2008

- Landing page: https://csrc.nist.gov/pubs/sp/800/66/r2/final
- Direct PDF: https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-66r2.pdf
- DOI: https://doi.org/10.6028/NIST.SP.800-66r2

This is the canonical, government-issued implementation guide that maps every HIPAA Security Rule standard to operational controls. It explicitly maps to NIST SP 800-53r5 security controls and to the NIST Cybersecurity Framework, so when GCP, AWS, or Azure publish their HIPAA alignment, this is the document they're aligning to.

### 1.2 HHS OCR Guidance on De-identification (November 26, 2012)

**Title:** Guidance Regarding Methods for De-identification of Protected Health Information

- Landing page: https://www.hhs.gov/hipaa/for-professionals/special-topics/de-identification/index.html
- Direct PDF: https://www.hhs.gov/sites/default/files/ocr/privacy/hipaa/understanding/coveredentities/De-identification/hhs_deid_guidance.pdf

The operative regulation on what makes data "de-identified" under HIPAA. The 2012 date is misleading; this is still the active guidance. Defines the two acceptable methods: Expert Determination (statistical) and Safe Harbor (the 18-identifier checklist).

### 1.3 NIH Genomic Data Sharing Policy and Security Best Practices

**Three nested documents matter:**

- Policy landing page: https://grants.nih.gov/policy-and-compliance/policy-topics/sharing-policies/gds/overview
- Using Genomic Data Responsibly: https://grants.nih.gov/policy-and-compliance/policy-topics/sharing-policies/accessing-data/using-genomic-data
- **NIH Security Best Practices for Users of Controlled-Access Data (current, effective for DUCs issued after January 25, 2025):** https://grants.nih.gov/sites/default/files/flmngr/NIH-Security-BPs-for-Users-of-Controlled-Access-Data.pdf
- Previous version (applies to DUCs approved before January 25, 2025 until renewal): https://grants.nih.gov/sites/default/files/flmngr/NIH_Best_Practices_for_Controlled-Access_Data_Subject_to_the_NIH_GDS_Policy.pdf
- Implementation Update NOT-OD-24-157: https://grants.nih.gov/grants/guide/notice-files/NOT-OD-24-157.html

For Cytognosis, **all new DUCs from this point forward fall under the 2025 Best Practices document**. NIH also issues a Data Use Certification (DUC) for each dataset:

- DUC overview: https://grants.nih.gov/policy-and-compliance/policy-topics/sharing-policies/accessing-data/certification-agreement
- Genomic Data User Code of Conduct: https://grants.nih.gov/policy-and-compliance/policy-topics/sharing-policies/accessing-data/user-code-of-conduct

The crucial rule: **NIH holds the institution accountable, not the cloud provider.** Cloud Service Providers must "meet the same standards" as the Best Practices document, but if anything goes wrong, NIH comes after Cytognosis, not after GCP.

### 1.4 All of Us Researcher Workbench Documentation

- Main support hub: https://support.researchallofus.org/
- Tier policy reference: https://support.researchallofus.org/hc/en-us/articles/35016255209876-Workspace-Questions
- Policy questions: https://support.researchallofus.org/hc/en-us/articles/34814131370388-Policy-Questions
- New Researcher Workbench 2.0 (powered by Verily Pre on GCP): https://support.researchallofus.org/hc/en-us/articles/41981050556564-Getting-Started-in-new-Researcher-Workbench-2-0

Worth studying not for direct compliance (Cytognosis isn't required to look like All of Us) but as a working example of how a federally-funded program engineers a secure GCP-backed environment. The operational design choices answer the question "what does compliant look like in practice?"

------

## 2. What These Four Sources Actually Require for Cytognosis

### 2.1 Translation table: Source → Cytognosis obligation

| Source                             | What it directly requires of Cytognosis                      |
| ---------------------------------- | ------------------------------------------------------------ |
| NIST SP 800-66r2                   | Not directly binding on Cytognosis unless Cytognosis is a HIPAA Covered Entity or Business Associate. Becomes binding the moment Cytognosis touches L4 data (MGB Biobank, Mayo, Mt Sinai) under a DUA that flows HIPAA obligations down. Not directly triggered by NDA, UKB, HCP, or ABCD data. |
| HHS OCR De-identification Guidance | Defines what counts as "de-identified" PHI. Important for understanding what aggregate Neuroverse outputs (axes, embeddings on aggregate cohorts) can be shared openly versus what stays controlled. Defines the universe of identifiers Cytognosis must NOT attempt to re-attach. |
| NIH GDS Best Practices             | **Directly binding on Cytognosis for every NDA DUC, dbGaP DUC, and Synapse DUC** covering controlled-access data (NBB, PEC, PsychAD, ROSMAP, ABCD, B-SNIP). This is the single most operationally consequential document for Neuroverse. |
| All of Us documentation            | Aspirational reference architecture. Becomes directly binding only when Cytognosis credentials individuals to the Researcher Workbench; their work stays inside Researcher Workbench, not in Cytognosis SAE. |

### 2.2 The eight things NIH GDS Best Practices actually require

These are the operational baselines for any environment storing or processing controlled-access NIH genomic data. The current (2025) Best Practices document expects:

1. **Access controls.** Authentication using multi-factor; explicit authorization for each Approved User; no shared accounts; automatic session timeout.
2. **Encryption.** At rest and in transit, with documented key management.
3. **Audit logging.** Tracking who accessed what, when. Logs themselves must be protected from tampering.
4. **Data destruction.** Documented procedures for data destruction at DUC expiration or project close-out, including any local copies.
5. **No copies outside the secure environment.** Personnel cannot download to personal devices, store in non-approved locations, or move data to non-approved systems.
6. **Physical security.** For hosted environments (cloud or institutional), the underlying infrastructure must have physical access controls; for Cytognosis this is satisfied by GCP's HIPAA-aligned regions and inherits from Google's controls.
7. **Incident response.** Documented plan for what happens if a breach, unauthorized access, or loss is suspected; reportable to NIH within specified timeframes (data management incidents).
8. **Personnel obligations.** Every Approved User must be named on the DUC, complete training, sign the Genomic Data User Code of Conduct.

If a Cloud Service Provider is involved (which is your case), NIH expects the CSP to meet the same standards, and Cytognosis bears the institutional accountability.

### 2.3 The Safe Harbor 18-identifier list (HHS OCR)

For any output Cytognosis publishes or shares openly, none of these can be present (whether in the data, in model outputs, in embeddings, or in metadata):

1. Names
2. Geographic subdivisions smaller than state (with limited ZIP exceptions)
3. Dates (other than year) directly related to an individual
4. Telephone numbers
5. Fax numbers
6. Email addresses
7. Social Security numbers
8. Medical record numbers
9. Health plan beneficiary numbers
10. Account numbers
11. Certificate or license numbers
12. Vehicle identifiers and serial numbers
13. Device identifiers and serial numbers
14. URLs
15. IP addresses
16. Biometric identifiers (finger and voice prints)
17. Full face photographs and any comparable images
18. Any other unique identifying number, characteristic, or code

Plus the actual knowledge clause: even after removing all 18, Cytognosis cannot release data if it has actual knowledge the residuals could re-identify someone.

**Two implications for Neuroverse:** the face MRI question (because of item 17, defaced MRI must defeat facial recognition before being shareable), and the model output question (item 18, "unique identifying characteristic" is broad enough to capture embeddings that uniquely identify training individuals, which is precisely the member-inference question).

------

## 3. GCP Configuration: Minimum Compliant Setup

This is the actual cloud configuration to satisfy NIH GDS Best Practices and align with NIST 800-66r2 for the data classes in scope.

### 3.1 Account-level foundations

| Setting                          | Configuration                                                |
| -------------------------------- | ------------------------------------------------------------ |
| **Cloud Identity**               | Federated to Google Workspace under cytognosis.org. No personal Gmail accounts may access any data-bearing resource. |
| **Organization policy**          | Resource Manager organization at the top level; one folder per environment (production, development, sandbox). Production folder where controlled-access data lives is isolated. |
| **BAA**                          | Signed Business Associate Addendum with Google. Required even though most Neuroverse data isn't HIPAA-covered, because Google's HIPAA-eligible services list is the operational guarantee path. Sign before any L3+ data ingestion. URL: https://cloud.google.com/security/compliance/hipaa |
| **HIPAA-eligible services only** | All compute, storage, and database services used for L2+ data must appear on Google's list of HIPAA-eligible services. The list excludes some services Cytognosis might otherwise use (some BigQuery features have specific configurations, some AI APIs are not on the list). Check before adopting any new service. |
| **Region pinning**               | All data-bearing resources pinned to US regions (us-central1, us-east4, etc.). No multi-region for controlled-access genomic data without explicit DUC permission. Some DUCs (UKB) require specific regions. |
| **Billing alerts**               | Set per-project budget alerts at 50%, 80%, 100% of monthly cap. Cost discipline is also a security practice (anomalous spend can indicate compromise). |

### 3.2 Identity and access (HIPAA Security Rule technical safeguards + NIH BP #1, #7)

| Setting                    | Configuration                                                |
| -------------------------- | ------------------------------------------------------------ |
| **MFA**                    | Mandatory for all human accounts. Hardware security keys preferred for admin accounts. |
| **Service accounts**       | No long-lived service-account keys. Use Workload Identity Federation for any external workload that needs to authenticate. |
| **Privileged access**      | Just-in-time elevation via PAM. Never grant Owner role to humans; use Editor sparingly. Use predefined IAM roles, not Basic roles. |
| **Per-DUC access control** | Each DUC gets a Google Group (`duc-nbb@cytognosis.org`, `duc-pec@cytognosis.org`, etc.). Approved Users are added to the corresponding group. Bucket and dataset IAM grants are at the group level, never at the user level, so adding or removing a person is a one-place change. |
| **Session timeout**        | 15-minute idle timeout on the browser-based SAE (Jupyter, VS Code Server). Compute instances themselves time out for billing reasons. |
| **No SSH from internet**   | All shell access via Identity-Aware Proxy (IAP) tunneling, which enforces IAM. No public IPs on any data-bearing resource. |

### 3.3 Storage (HIPAA Security Rule + NIH BP #2, #5)

| Setting                         | Configuration                                                |
| ------------------------------- | ------------------------------------------------------------ |
| **Cloud Storage buckets**       | One bucket per DUC. Bucket name includes the DUC reference. Uniform bucket-level access enabled (no ACLs). Public access prevention enforced at the organization level. |
| **Encryption at rest**          | CMEK (customer-managed encryption keys) via Cloud KMS for all L2+ buckets. HSM-backed keys for L3. Key rotation every 90 days. |
| **Encryption in transit**       | TLS 1.2 minimum on all endpoints; Google Front End handles this. Mutual TLS for inter-service where applicable. |
| **Bucket versioning**           | Enabled on input buckets (resilience against accidental deletion); disabled on output buckets that contain large model artifacts (cost). |
| **Object lifecycle**            | Automatic transition to Coldline at 90 days unused; deletion at DUC expiration date (configurable per DUC). |
| **Logging**                     | Bucket access logs to a separate, locked-down audit log bucket. Audit log bucket has retention lock (cannot be deleted) for the longest applicable retention period (7 years default; 10 years if HIPAA-covered). |
| **No personal Drive / Dropbox** | Documented policy. Audited monthly.                          |

### 3.4 Compute (HIPAA Security Rule + NIH BP #1, #5)

| Setting                                  | Configuration                                                |
| ---------------------------------------- | ------------------------------------------------------------ |
| **Vertex AI Workbench**                  | For interactive analysis on L2 data. Instances are user-isolated. Data attaches via per-DUC bucket mounts. Idle shutdown after 60 minutes. |
| **Vertex AI Training / Custom Training** | For batch model training. Spot/preemptible instances by default. Logs to centralized audit log. |
| **GKE / Compute Engine**                 | If needed, only private clusters with no public IPs. Use Confidential Computing for L3 workloads where supported. |
| **VPC architecture**                     | One VPC per environment; data buckets and compute share a VPC via Private Service Connect. VPC Service Controls enforce a perimeter around L2+ resources: no egress to non-allowlisted destinations. This is the single most important control: it blocks data exfiltration to non-Cytognosis Google projects even if credentials leak. |
| **No outbound internet from compute**    | Compute instances handling L2+ data have egress routed through a controlled NAT with allow-list. PyPI mirrors and approved repositories are allow-listed; everything else is blocked by default. |

### 3.5 Audit and incident response (HIPAA Security Rule administrative safeguards + NIH BP #3, #7)

| Setting                       | Configuration                                                |
| ----------------------------- | ------------------------------------------------------------ |
| **Cloud Audit Logs**          | Admin Activity logs always enabled (no opt-out). Data Access logs enabled for all L2+ buckets and datasets. Retention: 7 years minimum. |
| **Log sink**                  | Aggregated sink at the organization level routing all logs to a dedicated audit log bucket with retention lock. |
| **Alerting**                  | Cloud Monitoring alert policies for: anomalous bucket reads (volume spike), IAM grants outside the change window, access from a new geography, key rotation failures, KMS key disable. Alerts route to Cytognosis on-call (you, for now). |
| **Incident response runbook** | Document the response steps for: (a) suspected unauthorized access, (b) data exfiltration suspicion, (c) credential compromise, (d) lost device, (e) account takeover. Tested annually with a tabletop exercise. NIH GDS data management incidents must be reported to NIH per DUC terms (typically within 24-72 hours of discovery). |
| **Security Command Center**   | Standard tier minimum. Premium tier when budget allows; surfaces misconfiguration findings automatically. |

### 3.6 Data destruction (NIH BP #4)

| Setting                     | Configuration                                                |
| --------------------------- | ------------------------------------------------------------ |
| **DUC expiration tracking** | Master tracker has DUC expiration date for every cohort. Calendar event 60 days before expiration to either renew or destroy. |
| **Destruction procedure**   | Bucket-wide lifecycle deletion combined with CMEK key destruction. KMS key destruction is the cryptographic-erasure mechanism that satisfies NIH BP without requiring physical media wipe. Document destruction certificate per DUC. |
| **Personnel offboarding**   | When a person leaves Cytognosis or moves off a DUC, remove from the relevant Google Group within 24 hours; revoke session tokens. Audit log review confirms revocation. |

------

## 4. Modality-Specific Compliance Notes

Each data class has specific quirks. What follows is what to do, by modality, on top of the baseline above.

### 4.1 Genomic (WGS, WES, array)

- **DUC obligations:** all eight NIH BP items in Section 2.2.
- **Storage:** L2 in Cytognosis SAE under per-DUC bucket; CMEK with HSM backing.
- **Compute:** VPC Service Controls perimeter enforced; no egress to non-allowlisted destinations.
- **Output sensitivity:** allele frequencies and summary statistics are not automatically safe (see beacon attack literature). Aggregate genetic statistics released openly should pass a documented re-identification risk review.
- **GCP-specific:** Cloud Life Sciences API and Batch are HIPAA-eligible and convenient for variant calling pipelines.

### 4.2 Single-cell omics

- **DUC obligations:** same as bulk genomic data because per-cell genotype content is recoverable from expression data.
- **Storage:** L2; same as genomics.
- **Output sensitivity:** cell-type-level aggregate signatures generally safe; per-donor cell distributions are not. Trajectory and pseudo-time outputs require case-by-case review.
- **Practical:** AnnData and Zarr stores work well on Cloud Storage with FUSE mounts; CellxGene Census architecture is a reference design.

### 4.3 Structural and functional MRI

- **DUC obligations:** standard.
- **Critical defacing requirement:** Cytognosis SAE must verify that all incoming MRI data is defaced before any pipeline that produces shareable outputs runs against the raw data. For data from sources that don't pre-deface (rare), Cytognosis runs `mri_deface` or `pydeface` at ingest and stores both versions (defaced for analysis, raw under tighter access).
- **Storage:** BIDS-formatted on Cloud Storage; NIfTI files at scale go to standard buckets with metadata sidecars.
- **GCP-specific:** medical imaging often benefits from large local SSDs on training instances rather than streaming from Cloud Storage.
- **Watch:** diffusion-model re-facing literature (2025) is closing the gap; treat defacing as a current best practice with a known shelf life, not a permanent solution.

### 4.4 Connectomes and derived features

- **Output sensitivity:** **individual-level resting-state connectivity profiles are themselves identifying** (Finn et al. 2015 functional connectome fingerprinting). Cytognosis-produced connectivity matrices on identified subjects inherit the source data's classification.
- **Aggregate features:** atlas-mapped group-average connectivity matrices are L0/L1. Per-subject embeddings on shared cohorts are L2 unless declassified through a documented review.

### 4.5 EEG/MEG

- **Identifiability:** lower than genomics or MRI but non-trivial; resting-state EEG has biometric-like signatures.
- **Practical:** standard L2 treatment is sufficient for Neuroverse scope.

### 4.6 Clinical and EHR data

- **HIPAA implications:** structured clinical data and EHR notes are PHI when linked to patient identifiers. Limited Data Sets (no direct identifiers, dates and ZIP allowed) are L3 in your classification.
- **For institutional biobanks (MGB, Mayo, Mt Sinai):** the DUA dictates exact requirements. Most expect the data to stay inside the originating institution's environment; what Cytognosis receives is typically already a Limited Data Set, possibly further processed.
- **Free-text notes:** never transfer raw; require de-identification at the source (Philter, MIST, or commercial de-id services).
- **Storage when transferred:** L3 in Cytognosis SAE; CMEK with HSM; tighter access controls than L2; HIPAA-aligned bucket configuration.

### 4.7 Wearable and continuous sensor data

- **Identifiability:** high (mobility traces are biometric).
- **Treatment:** L2 minimum; L3 if linked to PHI.
- **For future Cytoscope work:** Apple HealthKit and Google Fit data ingestion architectures are HIPAA-aligned but require explicit user consent flows.

------

## 5. Longer-Term Privacy Posture (Beyond Minimum Compliance)

Compliance with NIH BP and HIPAA gets the data in the door. The questions you asked (when does an embedding remain PHI, what aggregates can be shared) need a more demanding posture. The following adds privacy depth without blocking research velocity.

### 5.1 Privacy Impact Assessment (PIA) per cohort

For each new dataset added to the master tracker, write a one-page PIA covering: (a) source identifiability, (b) what Cytognosis-produced derivatives might inherit identifiability, (c) what aggregate outputs are intended for release, (d) what gates apply before release. Document in the cohort row of the master tracker. Time cost: 30-60 minutes per cohort.

### 5.2 Pre-release member-inference evaluation

Before releasing any Neuroverse model artifact (pre-trained weights, embeddings on shared cohorts), run a documented member-inference attack against the model and report the success rate. Standard methodology: Shokri et al. shadow-model approach or its more recent successors. Release only if the attack performs at or near chance.

Code reference implementations: PrivacyRaven, ML Privacy Meter, TensorFlow Privacy. Build the evaluation into the Neuroverse release pipeline so it runs automatically before any model card publication.

### 5.3 Differential privacy on aggregate releases

For aggregate axes, summary embeddings, and group-level statistics intended for open release, apply differential privacy with documented epsilon budgets. Reasonable starting point: per-statistic epsilon of 1.0 for tables intended as published methods supplements; tighter (0.1) for higher-risk statistics like rare-variant frequencies.

OpenDP and Google's differential-privacy-library are usable on GCP. The All of Us Researcher Workbench applies DP to its Data Browser counts (suppression below 20); this is a sensible policy floor.

### 5.4 Federated computation as default for ENIGMA-style collaborations

For ENIGMA working groups and similar federated structures, keep the federation. Don't try to pull data centrally into Cytognosis SAE if the consortium's norm is federated meta-analysis. The federation IS the privacy architecture for these collaborations.

### 5.5 Output review board (lightweight)

Even at one person, document a process: any open release (paper, supplementary data, embeddings on Hugging Face, model card with sample outputs) requires Cytognosis sign-off using a one-page checklist. Sign-off attests: classification reviewed, identifiability re-check performed, member-inference evaluated where applicable, DP applied where applicable, no Safe Harbor identifiers present.

For now, sign-off is Shahin. When a second technical person joins, two-person review. When formal structure justifies it, a small board.

### 5.6 Synthetic data generation as research multiplier

For sharing across institutions outside a DUC, synthetic data generated from Neuroverse representations (with documented DP guarantees) is a powerful pattern. It's not a regulatory requirement but it lets Brad's lab or Ananth's lab work on a representative-but-non-identifying dataset for early prototyping while the formal DUC paperwork is in flight.

### 5.7 Annual SAE security review

Once a year, a one-day internal review of the SAE configuration against the latest NIH BP, NIST 800-66r2, and any new GDS policy notices. Two output products: (a) an internal memo updating Doc B Infrastructure with what changed, (b) a remediation plan with deadlines for any gaps.

------

## 6. What to Do This Week

Concrete next actions, ordered by leverage:

1. **Sign the Google BAA.** Even though Neuroverse Batch 1 doesn't touch HIPAA-covered data, the BAA is required before any L3 work, and it doesn't cost anything in tokens or time to have it in place early. https://cloud.google.com/security/compliance/hipaa
2. **Read the 2025 NIH Security Best Practices PDF** (linked in Section 1.3). It's ~15 pages and tells you exactly what NIH expects when they audit a DUC holder.
3. **Spin up the Cytognosis production GCP organization** with the foundations from Section 3.1 (org policy, folder structure, region pinning, billing alerts). This is achievable in one focused afternoon.
4. **Create the first DUC bucket pattern** (for NBB, since it's first in Batch 1) including: CMEK with HSM, VPC Service Controls perimeter, audit log sink, per-DUC IAM group, lifecycle rules. Document as a Terraform template so subsequent buckets are one configuration change away.
5. **Bookmark the four sources** in Cytognosis Drive for easy reference; you'll consult NIH BP and OCR Safe Harbor often as DUCs are drafted.
6. **Identify the cohort PIA template** (Section 5.1) so it's ready when Batch 1 DUCs are filed.

------

## 7. Reference Quick-Card

| Question                                                  | Source                                                       |
| --------------------------------------------------------- | ------------------------------------------------------------ |
| Are we in HIPAA scope?                                    | OCR de-identification guidance + dataset-by-dataset analysis |
| Does this aggregate output need review?                   | NIST 800-66r2 administrative safeguards + OCR Safe Harbor + member-inference check |
| What does NIH expect of our cloud setup for genomic data? | NIH GDS Best Practices 2025                                  |
| How does a working environment do this in practice?       | All of Us Researcher Workbench (reference architecture)      |
| What identifiers must NEVER appear in published outputs?  | OCR Safe Harbor 18-item list                                 |
| How long must we retain audit logs?                       | NIH GDS: per DUC; HIPAA: 6 years from creation or last effective date; default to 7 years |
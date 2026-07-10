# NIH Genomic Data Sharing — Operational Requirements

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: operators
> **Tags**: `operations`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)
**Effective for Cytognosis**: All new/renewed DUCs from 2025-01-25 onward
**Primary regulation**: [NOT-OD-24-157](https://grants.nih.gov/grants/guide/notice-files/NOT-OD-24-157.html) + [NOT-OD-25-083](https://grants.nih.gov/grants/guide/notice-files/NOT-OD-25-083.html)
**Companion doc**: [HIPAA-STATUS.md](HIPAA-STATUS.md) — full 45 CFR control matrix
**Last updated**: 2026-05-22

---

## 1. Which Regulation Applies to Cytognosis?

NIH operates a layered framework. The tiers below determine what applies:

| Regulation | When it applies to Cytognosis | Binding? |
|---|---|---|
| **NIH GDS Policy 2014** | Any NIH-funded research involving human genomic data | Yes (from first NIH award) |
| **NIH Security Best Practices 2025** (NIST 800-171 based) | All DUCs submitted/renewed after 2025-01-25 | **Yes — all new Neuroverse DUCs** |
| **HIPAA** | When handling PHI from clinical sources under a covered entity relationship | Yes (MGB Biobank, Mayo, Mt Sinai data) |
| **HHS OCR De-identification Guidance** | All data releases and model outputs | Yes |
| **All of Us workbench** | Only when credentialing users into the Researcher Workbench | Only if/when we integrate |
| **NIST SP 800-66r2** | HIPAA-covered data handling; references NIST 800-53 controls | Yes for PHI |

**Bottom line for Neuroverse**: NIH GDS Best Practices 2025 is the dominant framework.
HIPAA applies when we touch clinical-source data (MGB, Mayo, Mt Sinai). Both apply
simultaneously for ROSMAP and PsychAD (which are controlled-access AND may contain
HIPAA-covered clinical data).

---

## 2. The 8 NIH GDS Operational Requirements

These are extracted from the 2025 NIH Security Best Practices document. They apply to
any environment (cloud, institutional HPC, local server) where controlled-access
NIH genomic data is stored or processed.

### Requirement 1: Access Controls
- **MFA required** for all Approved Users accessing controlled data.
- **No shared accounts** — each researcher must have a unique identity.
- **Explicit authorization** per dataset — being on one DUC does not grant access to another.
- **Automatic session timeout** after a period of inactivity.
- **Cytognosis implementation**: Google Workspace + GCP enforces MFA; per-DUC IAM groups
  restrict access to named Approved Users only. See [duc-iam-pattern.md](duc-iam-pattern.md).

### Requirement 2: Encryption
- **At rest**: all controlled data must be encrypted at rest with documented key management.
- **In transit**: TLS 1.2+ required for all data transfers.
- **Key management**: rotation schedule documented; no hardcoded credentials.
- **Cytognosis implementation**: GCP-managed encryption at rest by default; CMEK activated
  on PHI buckets at first DUC data ingest (see [deferred-controls.md](deferred-controls.md)).
  TLS enforced on all endpoints via Caddy + GCP.

### Requirement 3: Audit Logging
- **Track who accessed what, when**, including reads, writes, admin actions, and auth events.
- **Logs must be protected from tampering** — not deletable by the same principal who created them.
- **Retention**: typically 7 years recommended; NIH does not specify a period but audits can
  look back to DUC issuance date.
- **Cytognosis implementation**: Cloud Audit Logs → `gs://cytognosis-audit-7yr` (locked
  2026-05-22, irrevocable). See [audit-log-retention.md](audit-log-retention.md).

### Requirement 4: Data Destruction
- **Documented destruction procedure** at DUC expiration or project close-out.
- All copies (primary, backup, cache, derivative) must be destroyed or returned.
- Destruction must be certified in writing.
- **Cytognosis implementation**: DUC close-out procedure in [duc-iam-pattern.md](duc-iam-pattern.md)
  §Close-out.

### Requirement 5: No Copies Outside the Secure Environment
- Personnel cannot download to personal devices.
- Data cannot be stored in non-approved locations (personal Dropbox, GitHub, etc.).
- Movement to non-approved systems is prohibited.
- **Cytognosis implementation**: DUC-IAM pattern restricts access to GCP SAE buckets.
  Enforced via VPC Service Controls (deferred until first external PHI receipt).

### Requirement 6: Physical Security
- Underlying infrastructure must have physical access controls.
- For cloud deployments, the CSP must certify physical security.
- **Cytognosis implementation**: Inherited from GCP (ISO 27001, SOC 2 Type II, HIPAA
  Business Associate). `cytognosis-phi-prod` uses `us-central1` (Council Bluffs, Iowa).

### Requirement 7: Incident Response
- **Documented plan** for breach, unauthorized access, suspected misuse.
- Must report to NIH data access committee within the timeframes specified in the DUC.
- **Cytognosis implementation**: [incident-response-runbook.md](incident-response-runbook.md).
  Reporting contacts per DUC are tracked in the master dataset tracker
  ([../../programs/neuroverse/datasets-cohorts.md](../../../05-Research/neuroverse/datasets-cohorts.md)).

### Requirement 8: Personnel Obligations
- Every Approved User must be **named on the DUC** before accessing data.
- All Approved Users must complete **required training** (varies by data access committee).
- All Approved Users must sign the **Genomic Data User Code of Conduct**.
- **Cytognosis implementation**: Training tracked in HIPAA-STATUS.md §Training.
  DUC Approved User lists are maintained in the master dataset tracker.

---

## 3. 2025 Policy Updates — What's New

### NIST SP 800-171 Compliance (Effective 2025-01-25)

All environments processing NIH controlled-access data must comply with
[NIST SP 800-171](https://csrc.nist.gov/publications/detail/sp/800-171/rev-3/final)
(Protecting Controlled Unclassified Information). This replaced the previous simpler
"best practices" checklist.

**NIST 800-171 has 110 controls across 14 families:**

| Family | Key requirements | Cytognosis status |
|---|---|---|
| AC — Access Control | MFA, least-privilege, session control | ✅ Partial |
| AU — Audit & Accountability | Logging, protection, review | ✅ Done |
| CM — Configuration Management | Baseline, change control, patch | ⏳ Partial |
| IA — Identification & Auth | MFA, password policy, OIDC | ✅ Done |
| IR — Incident Response | Plan, testing, reporting | ✅ Done |
| MA — Maintenance | Controlled maintenance, remote sessions | ⏳ TBD |
| MP — Media Protection | Sanitization, transport, CUI marking | ✅ N/A (cloud only) |
| PE — Physical Protection | Facility, visitor control | ✅ Inherited/GCP |
| PS — Personnel Security | Background checks, termination | ⏳ Policy needed |
| RA — Risk Assessment | Risk assessment, scanning | ✅ Template done |
| CA — Security Assessment | System assessment, plan of action | ⏳ Pre-DUC |
| SC — System & Comms | Separation, data-in-transit, VPN | ✅ Partial |
| SI — System & Info Integrity | Malware, patching, alerts | ⏳ Partial |
| SR — Supply Chain Risk | N/A for software-only | ✅ N/A |

> [!IMPORTANT]
> A formal NIST 800-171 self-assessment (POA&M document) is required before the first
> DUC submission. Estimated effort: 1–2 weeks. Use [risk-assessment-template.md](risk-assessment-template.md)
> as the starting point, adding NIST 800-171 control IDs to each item.

### Countries of Concern Restriction (NOT-OD-25-083, effective 2025-04-02)

NIH prohibits access to controlled-access data by **individuals or institutions located in
countries of concern** (defined by Executive Order 14117). This applies to:
- Collaborators at institutions in restricted countries
- Cloud regions operated by restricted-country subsidiaries
- Any sub-processor located in a restricted country

**Cytognosis action**: All GCP resources are in `us-central1`. No collaborator outside the
US, McLean, or Purdue is currently named on any DUC. When onboarding future collaborators,
verify against the [current country-of-concern list](https://grants.nih.gov/grants/guide/notice-files/NOT-OD-25-083.html)
before filing DUC amendments.

### Generative AI Restriction (2025 GDS Update)

NIH's 2025 GDS update explicitly states:
> "Users of NIH controlled-access data are **prohibited from using that data to train
> generative AI models without explicit NIH approval**."
>
> "Generative AI models and their parameters are considered **Data Derivatives** and must
> be protected and shared only with other authorized Approved Users."

**Implications for Neuroverse**:
- The Neuroverse foundation model is trained on controlled-access data — its weights are
  **Data Derivatives** under this definition.
- Open model release requires: member-inference evaluation passing the AUC < 0.55 threshold
  (see [member-inference-eval.md](member-inference-eval.md)), AND differential-privacy
  certification of aggregate outputs, AND NIH approval (DAC review process TBD).
- Pre-trained weights **cannot be released publicly** until this approval is obtained.
- Embeddings on controlled-access cohorts (NBB, PEC, ROSMAP) are Data Derivatives
  and cannot be shared outside the DUC-authorized team.

---

## 4. DUC Submission Checklist

Before submitting any new NDA/dbGaP/Synapse DUC:

- [ ] Verify environment meets NIST SP 800-171 (formal self-assessment complete)
- [ ] Confirm all Approved Users are named on the DUC
- [ ] Confirm all Approved Users have completed required training
- [ ] Confirm no collaborators at institutions in countries of concern
- [ ] Confirm GCP project is `cytognosis-phi-prod` or `cytognosis-phi-staging`
- [ ] Confirm DUC-specific IAM group exists (see [duc-iam-pattern.md](duc-iam-pattern.md))
- [ ] Confirm DUC-specific bucket exists with CMEK pending or active
- [ ] Complete Privacy Impact Assessment ([pia-template.md](pia-template.md))
- [ ] Register DUC in the master dataset tracker ([../../programs/neuroverse/datasets-cohorts.md](../../../05-Research/neuroverse/datasets-cohorts.md))

---

## 5. Key Reference URLs

| Resource | URL |
|---|---|
| NIH Genomic Data Sharing Policy overview | https://sharing.nih.gov/genomic-data-sharing-policy |
| NIH Security Best Practices 2025 (PDF) | https://grants.nih.gov/sites/default/files/flmngr/NIH-Security-BPs-for-Users-of-Controlled-Access-Data.pdf |
| NOT-OD-24-157 (2025 implementation update) | https://grants.nih.gov/grants/guide/notice-files/NOT-OD-24-157.html |
| NOT-OD-25-083 (countries of concern) | https://grants.nih.gov/grants/guide/notice-files/NOT-OD-25-083.html |
| NIST SP 800-171 Rev 3 | https://csrc.nist.gov/publications/detail/sp/800-171/rev-3/final |
| HHS De-identification guidance | https://www.hhs.gov/hipaa/for-professionals/privacy/special-topics/de-identification/ |
| Genomic Data User Code of Conduct | https://grants.nih.gov/policy-and-compliance/policy-topics/sharing-policies/accessing-data/user-code-of-conduct |

---

*Review this document when submitting a new DUC, when NIH issues a policy update,
or when onboarding a new collaborator institution.*

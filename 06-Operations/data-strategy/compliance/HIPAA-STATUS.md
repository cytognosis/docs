# HIPAA Compliance Status Dashboard
**Owner**: Shahin Mohammadi (Security Officer) | **Review**: Quarterly
**Last updated**: 2026-05-26 | **Next review**: 2026-08-26

> [!IMPORTANT]
> This is the single pane of glass for HIPAA compliance at Cytognosis Foundation.
> Every control links to its evidence document. Update this file whenever a control
> is activated or its status changes.

---

## Overall Status

| Category | Done | Pending | Deferred | Total |
|---|---|---|---|---|
| Administrative Safeguards | 8 | 3 | 0 | 11 |
| Physical Safeguards | 3 | 0 | 0 | 3 |
| Technical Safeguards | 10 | 1 | 0 | 11 |
| Organizational | 3 | 0 | 0 | 3 |
| Policies & Procedures | 8 | 2 | 0 | 10 |
| **TOTAL** | **32** | **6** | **0** | **38** |

**Compliance posture**: Pre-operational (no PHI ingested yet). All controls for the
current operational phase are satisfied. Pending controls have documented triggers.

---

## Administrative Safeguards (45 CFR §164.308)

### Security Officer Designation (§164.308(a)(2))
| Control | Status | Evidence | Owner |
|---|---|---|---|
| HIPAA Security Officer designated | ✅ Done | [hipaa-compliance-framework.md](hipaa-compliance-framework.md) | Shahin Mohammadi |
| HIPAA Privacy Officer designated | ⏳ Pending | —  | To be appointed |
| Backup Security Officer designated | ⏳ Pending | — | To be appointed |

### Risk Analysis and Management (§164.308(a)(1))
| Control | Status | Evidence | Owner |
|---|---|---|---|
| Initial risk assessment completed | ✅ Done | [risk-assessment-template.md](risk-assessment-template.md) | Shahin Mohammadi |
| Risk management plan documented | ✅ Done | [deferred-controls.md](deferred-controls.md) | Shahin Mohammadi |
| Risk re-assessment scheduled (3-year cycle) | ✅ Done | Review cadence in deferred-controls.md | Shahin Mohammadi |

### Workforce Training (§164.308(a)(5))
| Control | Status | Evidence | Owner |
|---|---|---|---|
| Initial HIPAA training curriculum defined | ✅ Done | [hipaa-compliance-framework.md](hipaa-compliance-framework.md) | Shahin Mohammadi |
| Annual training program established | ✅ Done | Framework doc §Training | Shahin Mohammadi |
| First training cycle completed | ⏳ Pending (Q3 2026) | — | Privacy Officer (TBD) |

### Access Management (§164.308(a)(4))
| Control | Status | Evidence | Owner |
|---|---|---|---|
| Role-based access controls documented | ✅ Done | [duc-iam-pattern.md](duc-iam-pattern.md) | Shahin Mohammadi |
| Per-DUC IAM provisioning pattern established | ✅ Done | [duc-iam-pattern.md](duc-iam-pattern.md) | Shahin Mohammadi |
| Least-privilege default (SA consolidation) | ✅ Done | [../../service-accounts.md](../../../04-Engineering/infrastructure/service-accounts.md) | Shahin Mohammadi |
| OIDC federation (no long-lived keys) | ✅ Done | [../../ci-cd/oidc-federation.md](../../../04-Engineering/infrastructure/ci-cd/oidc-federation.md) | Shahin Mohammadi |

### Incident Response (§164.308(a)(6))
| Control | Status | Evidence | Owner |
|---|---|---|---|
| Incident response runbook documented | ✅ Done | [incident-response-runbook.md](incident-response-runbook.md) | Shahin Mohammadi |
| Breach notification procedures included | ✅ Done | Incident runbook §Breach | Shahin Mohammadi |
| Runbook tested (tabletop) | ⏳ Pending (Q4 2026) | — | Security Officer |

### Contingency Plan (§164.308(a)(7))
| Control | Status | Evidence | Owner |
|---|---|---|---|
| Data backup plan documented | ✅ Done | [contingency-plan.md](contingency-plan.md) | Shahin Mohammadi |
| Disaster recovery plan documented | ✅ Done | Contingency plan §DR | Shahin Mohammadi |
| Emergency mode operation documented | ✅ Done | Contingency plan §Emergency | Shahin Mohammadi |
| Annual DR test scheduled | ✅ Done | Contingency plan §Testing | Shahin Mohammadi |
| First DR tabletop completed | ⏳ Pending (Q1 2027) | — | Security Officer |

### Business Associate Agreements (§164.308(b))
| Control | Status | Evidence | Owner |
|---|---|---|---|
| BAA inventory maintained | ✅ Done | [baa-inventory.md](baa-inventory.md) | Shahin Mohammadi |
| Google (GCP) BAA signed | ✅ Done | Accepted 2025-09-01 | Shahin Mohammadi |
| Vendor review process documented | ✅ Done | BAA inventory §Process | Shahin Mohammadi |

---

## Physical Safeguards (45 CFR §164.310)

All physical safeguards are inherited from GCP. GCP is certified ISO 27001, SOC 2 Type II,
and operates HIPAA-aligned facilities. Cytognosis does not maintain its own data center.

| Control | Status | Evidence | Owner |
|---|---|---|---|
| Facility access controls (physical) | ✅ Done (inherited) | GCP HIPAA Implementation Guide | GCP |
| Workstation use policy | ✅ Done | Data governance policy §Workstations | Shahin Mohammadi |
| Device and media controls | ✅ Done | Data governance policy §Devices | Shahin Mohammadi |

---

## Technical Safeguards (45 CFR §164.312)

### Access Control (§164.312(a))
| Control | Status | Evidence | Owner |
|---|---|---|---|
| Unique user ID for each person | ✅ Done | Google Workspace (cytognosis.org) | Shahin Mohammadi |
| Emergency access procedure | ✅ Done | [contingency-plan.md](contingency-plan.md) §Emergency | Shahin Mohammadi |
| Automatic logoff | ✅ Done | GCP IAM session duration policy | Shahin Mohammadi |
| Encryption/decryption documented | ✅ Done | [phi-security-controls-checklist.md](phi-security-controls-checklist.md) | Shahin Mohammadi |

### Audit Controls (§164.312(b))
| Control | Status | Evidence | Owner |
|---|---|---|---|
| Cloud Audit Logs enabled (both GCP projects) | ✅ Done | Log sinks configured | Shahin Mohammadi |
| Data Access Audit Logging (DATA_READ, DATA_WRITE, ADMIN_READ) | ✅ **Done 2026-05-26** | `allServices` on both infra + phi-prod; [GCP audit](../../audits/gcp-infrastructure-audit-2026-05-25.md) | Shahin Mohammadi |
| 7-year audit log retention | ✅ Done | `gs://cytognosis-audit-7yr` | Shahin Mohammadi |
| Audit log retention locked (irrevocable) | ✅ **LOCKED 2026-05-22** | [audit-log-retention.md](audit-log-retention.md) | Shahin Mohammadi |
| Log tampering prevention | ✅ Done | Locked retention policy | Shahin Mohammadi |

### Integrity (§164.312(c))
| Control | Status | Evidence | Owner |
|---|---|---|---|
| PHI integrity controls documented | ✅ Done | [phi-security-controls-checklist.md](phi-security-controls-checklist.md) | Shahin Mohammadi |
| Object versioning on PHI buckets | ✅ **Done 2026-05-25** | Enabled on `phi-core` + `phi-collab`; [GCP audit](../../audits/gcp-infrastructure-audit-2026-05-25.md) | Shahin Mohammadi |

### Encryption (§164.312(a)(2)(iv) and §164.312(e)(2))
| Control | Status | Evidence | Owner |
|---|---|---|---|
| Encryption at rest (GCS default encryption) | ✅ Done | GCP-managed encryption on all buckets | GCP |
| CMEK on PHI buckets | ✅ **Done 2026-06-14** | `phi-keyring`/`phi-bucket-key` (us-central1) on `phi-core` + `phi-collab`; verified via `gcloud` 2026-06-19 | Shahin Mohammadi |
| Encryption in transit (TLS everywhere) | ✅ Done | GCP enforces TLS; Caddy proxy forces HTTPS | Shahin Mohammadi |
| Key management policy documented | ✅ Done | [phi-security-controls-checklist.md](phi-security-controls-checklist.md) | Shahin Mohammadi |

---

## Organizational Requirements (45 CFR §164.314)

| Control | Status | Evidence | Owner |
|---|---|---|---|
| BAA with GCP signed | ✅ Done | Accepted 2025-09-01 | Shahin Mohammadi |
| Written BAA requirements for all BAs | ✅ Done | [baa-inventory.md](baa-inventory.md) | Shahin Mohammadi |
| Covered entity status documented | ✅ Done | [hipaa-compliance-framework.md](hipaa-compliance-framework.md) §Covered Entity | Shahin Mohammadi |

---

## Policies and Procedures (45 CFR §164.316)

| Control | Status | Evidence | Owner |
|---|---|---|---|
| HIPAA compliance framework policy | ✅ Done | [hipaa-compliance-framework.md](hipaa-compliance-framework.md) | Shahin Mohammadi |
| Data governance policy | ✅ Done | [../policies/data-governance-policy.md](../policies/data-governance-policy.md) | Shahin Mohammadi |
| Controlled data access policy | ✅ Done | [../policies/controlled-data-access.md](../policies/controlled-data-access.md) | Shahin Mohammadi |
| NIH NDA access procedures | ✅ Done | [../policies/nih-nda-access-procedures.md](../policies/nih-nda-access-procedures.md) | Shahin Mohammadi |
| Privacy Impact Assessment template | ✅ Done | [pia-template.md](pia-template.md) | Shahin Mohammadi |
| Risk Assessment template | ✅ Done | [risk-assessment-template.md](risk-assessment-template.md) | Shahin Mohammadi |
| Deferred controls register | ✅ Done | [deferred-controls.md](deferred-controls.md) | Shahin Mohammadi |
| Member-inference evaluation methodology | ✅ Done | [member-inference-eval.md](member-inference-eval.md) | Shahin Mohammadi |
| Annual policy review cadence documented | ✅ Done | Deferred controls §Review Schedule | Shahin Mohammadi |
| Policy documentation retention | ⏳ Pending — define retention | — | Privacy Officer (TBD) |

---

## NIH Genomic Data Sharing (GDS) Requirements

NIH GDS Best Practices (2025, effective for new/renewed DUCs after 2025-01-25) require
NIST SP 800-171 compliance. See full breakdown in
[nih-gds-requirements.md](nih-gds-requirements.md).

| Control | Status | Notes |
|---|---|---|
| NIST SP 800-171: Access control (AC) | ⏳ Gap assessment needed | Pre-DUC; no controlled data yet |
| NIST SP 800-171: Audit & accountability (AU) | ✅ Done | Audit logs + Data Access audit logging (allServices) enabled 2026-05-26 |
| NIST SP 800-171: Configuration management (CM) | ⏳ Gap assessment needed | IaC (container framework) exists; formal CM policy missing |
| NIST SP 800-171: Identification & authentication (IA) | ✅ Done | MFA via Google Workspace; OIDC federation |
| NIST SP 800-171: Incident response (IR) | ✅ Done | Runbook in place |
| NIST SP 800-171: Maintenance (MA) | ⏳ Not documented | — |
| NIST SP 800-171: Media protection (MP) | ⏳ Not documented | No physical media; cloud only |
| NIST SP 800-171: Personnel security (PS) | ⏳ Partial | Training program defined; not yet run |
| NIST SP 800-171: Physical protection (PE) | ✅ Done (inherited) | GCP facilities |
| NIST SP 800-171: Risk assessment (RA) | ✅ Done | Template + initial assessment |
| NIST SP 800-171: Security assessment (CA) | ⏳ Not yet | Pre-DUC; do before first DUC submission |
| NIST SP 800-171: System comms protection (SC) | ✅ Partial | TLS everywhere; VPC-SC deferred |
| NIST SP 800-171: System & information integrity (SI) | ✅ Partial | Audit logs; CVE scanning not yet |
| **Countries of concern restriction (NOT-OD-25-083)** | ⏳ Policy needed | Prohibits access from countries of concern |
| **Generative AI restriction (2025 GDS update)** | ✅ Documented | See [nih-gds-requirements.md](nih-gds-requirements.md) §7 |

> [!IMPORTANT]
> Before submitting the first NDA/dbGaP/Synapse DUC, a formal NIST SP 800-171 self-assessment
> must be completed and documented. Use the [risk-assessment-template.md](risk-assessment-template.md)
> as the starting point. Estimated effort: 1–2 weeks with engineering input.

---

## Key Milestones

| Milestone | Status | Date |
|---|---|---|
| GCP organization created | ✅ Done | 2025 |
| Cytognosis BAA with Google accepted | ✅ Done | 2025-09-01 |
| GCP project structure (infra / phi-prod / phi-staging / phi-dev / data) | ✅ Done | 2025 |
| Audit log sinks configured (both projects) | ✅ Done | 2026-05-18 |
| 7-year audit log retention locked (irrevocable) | ✅ **Done** | **2026-05-22** |
| Service account consolidation + least-privilege | ✅ Done | 2026-05 |
| HIPAA SOPs authored (9 documents) | ✅ Done | 2026-05 |
| NIST 800-171 self-assessment | ⏳ Pre-first DUC | TBD |
| Privacy Officer appointed | ⏳ Q3 2026 | TBD |
| First HIPAA training cycle | ⏳ Q3 2026 | TBD |
| VPC Service Controls perimeter | ⏳ Trigger: first external PHI | TBD |
| CMEK on PHI buckets | ✅ **Done** | **2026-06-14** |
| First DR tabletop exercise | ⏳ Q1 2027 | TBD |

---

## Contacts

| Role | Person | Contact |
|---|---|---|
| HIPAA Security Officer | Shahin Mohammadi | mohammadi@cytognosis.org |
| HIPAA Privacy Officer | (to be appointed) | — |
| HIPAA Compliance Officer | (to be appointed) | — |

---

*This document is reviewed quarterly. Any new vendor engagement, architecture change,
or data classification event may require an out-of-cycle review.*

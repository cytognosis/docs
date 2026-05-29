# SOP: Risk Assessment Template
**Control**: HIPAA 164.308(a)(1)(ii)(A) — Risk Analysis
**Effective**: 2026-05-19 | **Owner**: Privacy Officer | **Review**: Annual + after major system change

## Instructions
Complete one instance of this template per year (annual) or after any significant system change
(new data type, new vendor, new compute tier, major architecture change). Store completed
assessments in `compliance/risk-assessments/YYYY-MM-risk-assessment.md`.

---

# HIPAA Risk Assessment — [Date] — [Scope]

**Prepared by**: [Name]
**Review date**: [Date]
**Scope**: [e.g., "Full Cytognosis GCP infrastructure", "PsychENCODE DUC data ingestion"]
**Applicable data tiers**: [Tier 3 / Tier 4 / Both]

## 1. Inventory of ePHI (Electronic Protected Health Information)

| System | Data type | PHI identifiers present | Location | Classification |
|---|---|---|---|---|
| [e.g. cytognosis-phi-core] | [WGS genotype] | [genomic sequence = HIPAA identifier] | [gs://cytognosis-phi-core/duc-nbb/] | Tier 4 |

## 2. Threat Identification

For each system holding ePHI, identify realistic threats:

| Threat | Likelihood (H/M/L) | Current controls | Residual risk |
|---|---|---|---|
| Unauthorized access (external) | L | VPC-SC (planned), IAM, OIDC-only CI | L |
| Insider threat | L | Group-based access, audit logs, least-privilege | L |
| Ransomware / malware | L | No public IPs on phi instances, IAP-only access | L |
| Accidental disclosure | M | No public buckets, uniform bucket-level access | L |
| Supply chain (compromised dependency) | M | Artifact Registry private registry, dependency scanning | M |
| Service provider breach (GCP) | L | Google BAA signed; CMEK (deferred) | L |
| Data in transit interception | L | TLS 1.3 enforced on all Cloud Run services | L |

## 3. Vulnerability Assessment

| Vulnerability | Systems affected | Severity | Remediation | Target date |
|---|---|---|---|---|
| No CMEK on phi-core bucket | cytognosis-phi-core | Medium | Activate KMS on first data ingestion | Before first Tier 4 data |
| VPC-SC not yet configured | All phi-prod | High | Implement before any external PHI receipt | Before DUC data arrives |
| Retention lock not applied | cytognosis-audit-7yr | Low | Lock after 7-day verification | [date] |

## 4. Risk Rating Summary

| Risk area | Inherent risk | Controls | Residual risk | Acceptable? |
|---|---|---|---|---|
| Access control | High | IAM groups, OIDC, audit logs | Low | ✅ |
| Encryption at rest | Medium | Deferred CMEK | Medium | ⚠️ (mitigate before PHI) |
| Network security | High | Cloud Run only; no public IPs on phi | Low | ✅ |
| Audit trail | Medium | 7yr retention bucket + log sinks | Low | ✅ |
| Incident response | High | Runbook exists (see incident-response-runbook.md) | Medium | ⚠️ (test annually) |

## 5. Remediation Plan

| Action | Owner | Due date | Status |
|---|---|---|---|
| Activate CMEK on phi-core | Engineering | Before first DUC data | Pending |
| Implement VPC-SC perimeter | Engineering | Before first DUC data | Pending |
| Lock audit log retention | Privacy Officer | 2026-05-26 | Pending |
| Conduct first tabletop incident exercise | Privacy + Eng | 2026-08-01 | Not started |

## 6. Sign-Off

| Role | Name | Date | Signature |
|---|---|---|---|
| Privacy Officer | [Name] | [Date] | [Initials] |
| Executive Lead | Shahin Mohammadi | [Date] | |

# SOP: Privacy Impact Assessment (PIA) Template
**Control**: HIPAA 164.308(a)(1) — Risk Analysis; Best practice for new data onboarding
**Effective**: 2026-05-19 | **Owner**: Privacy Officer | **Review**: Per cohort + annually

## Instructions
Complete one PIA before onboarding any new cohort or dataset that may contain Tier 3 or
Tier 4 data. Store completed PIAs in `compliance/pias/YYYY-MM-<cohort>.md`.

---

# Privacy Impact Assessment — [Cohort Name] — [Date]

**Prepared by**: [Name]
**Dataset**: [e.g., PsychENCODE WGS cohort v3]
**Data source**: [e.g., NIH NDA, dbGaP, internal collection]
**Approving authority**: Shahin Mohammadi, Founder & CEO
**DUC/IRB reference**: [DUC number / IRB protocol]

## 1. Data Description

| Field | Value |
|---|---|
| Modalities | [e.g., WGS genotypes, RNA-seq, clinical phenotypes] |
| N individuals | [number] |
| Age range | [e.g., adult 18-85] |
| Geographic origin | [e.g., US, multi-site] |
| PHI identifiers present | [list any of the 18 HIPAA identifiers present] |
| De-identification method | [Safe Harbor / Expert Determination / N/A] |
| Re-identification risk | [Low / Medium / High — with justification] |

## 2. Data Use

| Field | Value |
|---|---|
| Intended use | [e.g., GWAS + gene expression QTL analysis] |
| Permitted uses per DUC | [list exactly what the DUC allows] |
| Prohibited uses | [list explicitly prohibited uses per DUC] |
| Data sharing | [Internal only / Purdue collaboration / etc.] |
| Publication plans | [summary statistics only / no individual-level data] |

## 3. Infrastructure Placement

| Component | Configuration | Justification |
|---|---|---|
| Storage bucket | `gs://cytognosis-phi-core/duc-<name>/` | Tier 4 PHI bucket |
| Encryption | CMEK (activate before ingest) | DUC requirement |
| Access group | `duc-<name>@cytognosis.org` | Approved-user-only access |
| Network controls | No public IP; IAP access only | DUC / NIH GDS requirement |
| Audit logging | All access logged to `cytognosis-audit-7yr` | HIPAA 164.312(b) |

## 4. Privacy Risks & Mitigations

| Risk | Likelihood | Mitigation | Residual risk |
|---|---|---|---|
| Re-identification from genomic data | Medium | No public release of individual-level data; k-anonymity enforced | Low |
| Scope creep (use beyond DUC) | Low | DUC terms documented; access scoped to approved users only | Low |
| Accidental disclosure via model | Medium | Member-inference evaluation before model release (see member-inference-eval.md) | Low |
| Insider access | Low | Audit logs; group-based access; least-privilege | Low |

## 5. Data Retention & Deletion

| Phase | Action | Timeline |
|---|---|---|
| Active analysis | Data retained in phi-core | Duration of DUC |
| DUC expiration | Remove user access; notify data custodian | Within 30 days of expiry |
| Data deletion | Delete objects + KMS key destruction (cryptographic erasure) | Per DUC terms (typically within 60-90 days of expiry) |

## 6. Approvals

| Role | Name | Date |
|---|---|---|
| Privacy Officer | [Name] | [Date] |
| Executive Lead | Shahin Mohammadi | [Date] |
| IRB confirmation | [N/A / Protocol #] | [Date] |

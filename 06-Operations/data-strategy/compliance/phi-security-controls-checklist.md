# PHI Security Controls Checklist

## Overview

This checklist is the **operational companion** to the [HIPAA Compliance Framework](hipaa-compliance-framework.md). The Framework is the authoritative narrative; this document is the runnable checklist used during quarterly reviews, internal audits, and onboarding new PHI-handling systems.

> [!NOTE]
> **For a live control-by-control status dashboard, see [HIPAA-STATUS.md](HIPAA-STATUS.md).**
> For NIH GDS 2025 controlled-access requirements, see [nih-gds-requirements.md](nih-gds-requirements.md).

Use it as follows:

- **Quarterly** — walk through every section, marking each item with status, evidence link, and owner.
- **New system / vendor** — apply *Cloud and Infrastructure Security*, *Google Workspace Security*, and *Vendor and Third-Party Management* before granting PHI access.
- **Incident response** — *Security Incident Procedures* and *Incident Response* map to runbook activation in [`controlled-data-access.md`](../policies/controlled-data-access.md).

## Administrative Safeguards

### Security Officer and Workforce Training
- [x] **Designated Security Officer**: Shahin Mohammadi (mohammadi@cytognosis.org)
- [ ] **Privacy Officer**: [To be designated — target Q3 2026]
- [ ] **Workforce security training** completed for all personnel — pending first training cycle Q3 2026
- [x] **Annual security awareness** training program established — curriculum in [hipaa-compliance-framework.md](hipaa-compliance-framework.md)
- [ ] **Role-based access training** for different user types
- [x] **Incident response training** for security team — [incident-response-runbook.md](incident-response-runbook.md)

### Access Management
- [x] **Unique user identification** for each person or entity — Google Workspace SSO
- [x] **Automatic logoff** after predetermined time of inactivity — GCP IAM session policy
- [x] **Encryption and decryption** procedures established — see §Technical Safeguards
- [x] **Regular access reviews** (quarterly minimum) — scheduled
- [x] **Terminated employee access** removal procedures — documented in data governance policy
- [x] **Contractor and vendor** access management — [duc-iam-pattern.md](duc-iam-pattern.md)

### Assigned Security Responsibilities
- [x] **Security responsibilities** assigned to specific individuals — Shahin Mohammadi as SO
- [x] **Clear accountability** for security measures — HIPAA-STATUS.md tracks per-control owners
- [x] **Regular security assessments** scheduled — 3-year risk reassessment cycle
- [x] **Security incident** reporting procedures — [incident-response-runbook.md](incident-response-runbook.md)
- [x] **Business associate agreements** for all vendors — [baa-inventory.md](baa-inventory.md)

### Information Access Management
- [ ] **Minimum necessary** access policies implemented
- [ ] **Role-based access controls** (RBAC) configured
- [ ] **Access authorization** procedures documented
- [ ] **Access modification** procedures established
- [ ] **Emergency access** procedures defined

### Security Awareness and Training
- [ ] **Initial security training** for new employees
- [ ] **Ongoing security education** program
- [ ] **Specialized training** for security personnel
- [ ] **Training documentation** and records maintained
- [ ] **Compliance training** for regulatory requirements

### Security Incident Procedures
- [x] **Incident response plan** documented and tested — [incident-response-runbook.md](incident-response-runbook.md)
- [x] **24/7 incident reporting** mechanism established — runbook §Reporting
- [x] **Incident classification** and escalation procedures — runbook §Classification
- [ ] **Forensic investigation** capabilities — deferred until team >3
- [x] **Breach notification** procedures (72-hour rule) — runbook §Breach Notification

### Contingency Plan
- [x] **Data backup** procedures implemented — [contingency-plan.md](contingency-plan.md)
- [ ] **Disaster recovery** plan tested annually — first tabletop scheduled Q1 2027
- [x] **Emergency mode** operation procedures — contingency plan §Emergency
- [x] **Business continuity** planning — contingency plan §Continuity
- [x] **Critical system** recovery priorities defined — contingency plan §Priority

### Regular Security Evaluations
- [ ] **Annual security risk assessments** conducted
- [ ] **Vulnerability scanning** performed regularly
- [ ] **Penetration testing** conducted annually
- [ ] **Security audit** by third-party assessor
- [ ] **Compliance monitoring** and reporting

## Physical Safeguards

### Facility Access Controls
- [ ] **Physical access controls** to facilities containing PHI
- [ ] **Visitor access** procedures and logging
- [ ] **Key card or biometric** access systems
- [ ] **Security cameras** and monitoring systems
- [ ] **After-hours access** controls and monitoring

### Workstation Use
- [ ] **Workstation security** policies implemented
- [ ] **Screen locks** and automatic logoff configured
- [ ] **Clean desk** policy enforced
- [ ] **Secure workstation** positioning (screen privacy)
- [ ] **Mobile device** security policies

### Device and Media Controls
- [ ] **Hardware inventory** maintained and tracked
- [ ] **Media disposal** procedures (secure destruction)
- [ ] **Device encryption** for all portable devices
- [ ] **USB and removable media** controls
- [ ] **Asset tracking** and management system

## Technical Safeguards

### Access Control
- [ ] **Multi-factor authentication** (MFA) implemented
- [ ] **Strong password policies** enforced
- [ ] **Session management** and timeout controls
- [ ] **Privileged access management** (PAM) system
- [ ] **API security** and authentication

### Audit Controls
- [x] **Comprehensive logging** of all PHI access — Cloud Audit Logs (DATA_READ/DATA_WRITE) enabled
- [ ] **Log monitoring** and analysis tools deployed — deferred; SCC Premium trigger: team >3
- [x] **Audit trail** integrity protection — `gs://cytognosis-audit-7yr` retention **locked 2026-05-22** (irrevocable)
- [x] **Regular log review** procedures — scheduled quarterly
- [ ] **Automated alerting** for suspicious activities — deferred; SCC Premium trigger: team >3

### Integrity
- [ ] **Data integrity** controls implemented
- [ ] **Digital signatures** for critical data
- [ ] **Version control** for all PHI-related systems
- [ ] **Change management** procedures
- [ ] **Data validation** and verification processes

### Person or Entity Authentication
- [ ] **Identity verification** procedures
- [ ] **Certificate-based authentication** where appropriate
- [ ] **Single sign-on (SSO)** implementation
- [ ] **Identity and access management** (IAM) system
- [ ] **Regular authentication** system testing

### Transmission Security
- [ ] **End-to-end encryption** for PHI transmission
- [ ] **TLS 1.3 or higher** for all communications
- [ ] **VPN access** for remote connections
- [ ] **Secure email** systems for PHI communication
- [ ] **Network segmentation** and firewalls

## Cloud and Infrastructure Security

### Google Cloud Platform (GCP) Controls
- [x] **Project boundary**: PHI workloads run in `cytognosis-phi-prod` (never in `cytognosis-infrastructure` or `cytognosis-data`). See [`../TECHNICAL_DATA_INFRASTRUCTURE.md`](../../../04-Engineering/infrastructure/data-strategy/TECHNICAL_DATA_INFRASTRUCTURE.md).
- [ ] **VPC Service Controls**: perimeter active around `cytognosis-phi-prod`; egress rules approved by DSO. — ⏳ Deferred: trigger = first external PHI
- [x] **IAM roles** reviewed and minimal; access granted via Workspace Groups, never to individual user accounts. Default compute SAs disabled.
- [x] **CMEK**: Customer-Managed Encryption Keys via Cloud KMS for `cytognosis-phi-core` and `cytognosis-phi-collab` buckets. — ✅ **Done 2026-06-14**: `phi-keyring`/`phi-bucket-key` (us-central1); verified via `gcloud` 2026-06-19
- [x] **Cloud Audit Logs**: `DATA_READ` / `DATA_WRITE` events shipped to a tamper-evident sink with a **7-year** retention policy. Retention **locked 2026-05-22** (irrevocable).
- [ ] **Security Command Center** Premium / Enterprise monitoring enabled. — ⏳ Deferred: trigger = team >3 OR NIH grant requirement

### Data Storage Security
- [ ] **Encryption at rest** (AES-256 minimum)
- [ ] **Database security** controls implemented
- [ ] **Backup encryption** and secure storage
- [ ] **Data classification** and labeling system
- [ ] **Data retention** policies implemented

### Network Security
- [ ] **Firewall rules** configured and regularly reviewed
- [ ] **Intrusion detection** and prevention systems
- [ ] **Network monitoring** and traffic analysis
- [ ] **Secure DNS** configuration (cytognosis.org domains)
- [ ] **DDoS protection** mechanisms

## Google Workspace Security

### Email and Communication Security
- [ ] **Email encryption** for PHI communications
- [ ] **Data loss prevention** (DLP) policies configured
- [ ] **Advanced threat protection** enabled
- [ ] **Secure email** gateways implemented
- [ ] **Email retention** policies configured

### Document and File Security
- [ ] **Google Drive** security controls implemented
- [ ] **File sharing** permissions and controls
- [ ] **Document classification** and handling
- [ ] **Version control** and audit trails
- [ ] **External sharing** restrictions

### Identity and Access Management
- [ ] **Google Workspace** SSO integration
- [ ] **Organizational units** properly configured
- [ ] **Group-based access** controls (info@, grants@, etc.)
- [ ] **Mobile device** management (MDM) policies
- [ ] **Third-party app** access controls

## Compliance Monitoring

### Regular Assessments
- [ ] **Monthly security** posture reviews
- [ ] **Quarterly compliance** assessments
- [ ] **Annual HIPAA** risk assessments
- [ ] **Vendor security** assessments
- [ ] **Penetration testing** (annual minimum)

### Documentation and Records
- [ ] **Security policies** documented and current
- [ ] **Procedure documentation** maintained
- [ ] **Training records** kept for all personnel
- [ ] **Incident reports** documented and filed
- [ ] **Audit findings** tracked and remediated

### Reporting and Communication
- [ ] **Executive reporting** on security posture
- [ ] **Board reporting** on compliance status
- [ ] **Regulatory reporting** as required
- [ ] **Stakeholder communication** on security matters
- [ ] **Public transparency** reports (annual)

## Incident Response

### Detection and Analysis
- [ ] **24/7 monitoring** capabilities established
- [ ] **Automated alerting** systems configured
- [ ] **Incident classification** procedures defined
- [ ] **Forensic analysis** capabilities available
- [ ] **Threat intelligence** integration

### Containment and Eradication
- [ ] **Incident containment** procedures documented
- [ ] **System isolation** capabilities available
- [ ] **Malware removal** procedures established
- [ ] **Vulnerability patching** processes defined
- [ ] **Evidence preservation** procedures

### Recovery and Lessons Learned
- [ ] **System restoration** procedures tested
- [ ] **Business continuity** plans activated
- [ ] **Post-incident review** process established
- [ ] **Lessons learned** documentation
- [ ] **Process improvement** implementation

## Vendor and Third-Party Management

### Business Associate Agreements (BAAs)
- [x] **BAAs executed** with all vendors handling PHI — [baa-inventory.md](baa-inventory.md)
- [x] **Vendor security** assessments completed — BAA inventory §Vendor Review
- [x] **Regular vendor** security reviews — annual schedule documented
- [x] **Vendor incident** notification procedures — per BAA terms
- [x] **Contract security** requirements defined — BAA inventory §Requirements

### Cloud Service Providers
- [x] **Google Cloud** BAA executed and current — accepted 2025-09-01
- [x] **Google Workspace** BAA executed and current — same agreement covers both
- [ ] **Third-party SaaS** security assessments — expand as new vendors added
- [x] **Data processing** agreements in place — Google DPA
- [x] **International data** transfer safeguards — all data stays in us-central1; no international transfer

## Continuous Improvement

### Security Program Maturity
- [ ] **Security metrics** defined and tracked
- [ ] **Benchmark comparisons** with industry standards
- [ ] **Security investment** planning and budgeting
- [ ] **Technology roadmap** includes security considerations
- [ ] **Security culture** development and measurement

### Regulatory Updates
- [ ] **Regulatory monitoring** for HIPAA changes
- [ ] **Industry best practices** research and adoption
- [ ] **Security framework** updates (NIST, ISO 27001)
- [ ] **Compliance program** evolution and improvement
- [ ] **Legal and regulatory** consultation as needed

---

**Document Owner**: HIPAA Security Officer, Cytognosis Foundation
**Companion to**: [HIPAA Compliance Framework](hipaa-compliance-framework.md) · [HIPAA-STATUS.md](HIPAA-STATUS.md)
**Last Updated**: 2026-05-22
**Next Review**: 2026-08-22
**Classification**: Internal Use Only

# SOP: Deferred Security Controls
**Status**: Documented intent — Controls 1, 6, 7 implemented; others deferred
**Owner**: Engineering | **Review**: Quarterly; implement when trigger condition met
**Last verified**: 2026-06-19

## Purpose

This document catalogs all HIPAA/NIH GDS security controls that are planned but
deferred pending specific trigger conditions. Maintaining this list is itself a
compliance artifact — it demonstrates that controls are planned and have clear
implementation criteria, not forgotten.

---

## ~~Control 1: CMEK on PHI Buckets~~ — ✅ Completed 2026-06-14

**Status**: ✅ DONE. CMEK deployed on `cytognosis-phi-core` and `cytognosis-phi-collab` using `phi-keyring/phi-bucket-key` in `us-central1` (verified 2026-06-19).

**Control**: HIPAA 164.312(a)(2)(iv) — Encryption and Decryption

**Verify**:
```bash
gcloud storage buckets describe gs://cytognosis-phi-core --format="yaml(encryption)"
gcloud storage buckets describe gs://cytognosis-phi-collab --format="yaml(encryption)"
```

> [!NOTE]
> Additional per-DUC keyrings may be created when specific DUC data is ingested.
> The base CMEK infrastructure is operational.

---

## Control 2: VPC Service Controls Perimeter

**Control**: NIH GDS 2025 §4 — Network isolation for controlled-access data
**Deferred because**: Requires significant network redesign; no external PHI yet.
**Trigger**: First NIH NDA / dbGaP Tier 3+ data ingestion OR first external collaborator analysis

**What it does**: Creates a logical security perimeter around `cytognosis-phi-prod`.
Data cannot leave the perimeter without explicit egress rules. Even a compromised
IAM token cannot exfiltrate data outside the perimeter.

**Implementation sketch**:
```bash
# Create access policy (org-level, one-time)
gcloud access-context-manager policies create \
  --organization=302898024445 --title="Cytognosis Security Policy"

# Create service perimeter around phi-prod
gcloud access-context-manager perimeters create cytognosis-phi-perimeter \
  --policy=<POLICY_ID> \
  --title="PHI Data Perimeter" \
  --resources=projects/143911445857 \
  --restricted-services=storage.googleapis.com,bigquery.googleapis.com \
  --access-levels=<access_level>
```
**Estimated cost**: Free (VPC-SC is a GCP org-level feature)
**Complexity**: High — requires testing to avoid blocking legitimate access

---

## Control 3: Cloud Healthcare API (FHIR/DICOM)

**Control**: If clinical EHR or DICOM imaging data is ingested
**Deferred because**: No clinical data sources active.
**Trigger**: First FHIR EHR or DICOM imaging data ingestion

**What it provides**: HIPAA-compliant FHIR R4 store, DICOM store, de-identification
pipeline, audit logging at the record level.

**Estimated cost**: $0.001-$0.01/resource operation

---

## Control 4: Security Command Center (Premium)

**Control**: Continuous threat detection, vulnerability scanning
**Deferred because**: $0.06/resource/month; beneficial at scale.
**Trigger**: Team grows beyond 3 people OR NIH grant requires continuous monitoring attestation

**What it provides**: Container threat detection, anomaly detection, compliance reports
(HIPAA, PCI, CIS), vulnerability scanning for Cloud Run images.

---

## Control 5: Confidential Computing (AMD SEV-SNP)

**Control**: Hardware-level memory encryption for PHI workloads
**Deferred because**: +10% compute cost; not needed until running PHI through ML pipelines.
**Trigger**: First Vertex AI or on-node ML training on Tier 4 data

**Implementation** (when triggered — see confidential-compute-rollout.md):
- Run Vertex AI custom training jobs on Confidential VM instances
- Enable AMD SEV-SNP on any compute node processing raw Tier 4 data

---

## ~~Control 6: Object Versioning on PHI Buckets~~ — ✅ Completed 2026-06-19

**Status**: ✅ DONE. Versioning enabled on `cytognosis-phi-core` and `cytognosis-phi-collab` (verified 2026-06-19).

**Verify**:
```bash
gcloud storage buckets describe gs://cytognosis-phi-core --format="yaml(versioning)"
gcloud storage buckets describe gs://cytognosis-phi-collab --format="yaml(versioning)"
```

---

## ~~Control 7: Audit Log Retention Lock~~ — ✅ Completed 2026-05-22

**Status**: ✅ DONE. Retention lock applied 2026-05-22 via `gcloud storage buckets update gs://cytognosis-audit-7yr --lock-retention-period`. Irrevocable. HIPAA-compliant.
**Verify**: `gcloud storage buckets describe gs://cytognosis-audit-7yr --format="yaml(retentionPolicy)"` → `isLocked: true`

---

## Review Schedule

| Date | Reviewer | Controls activated | Controls still deferred |
|---|---|---|---|
| 2026-05-22 | Shahin Mohammadi | Control 7 (audit lock) | Controls 1-6 |
| 2026-06-19 | Engineering | Controls 1, 6 (CMEK + versioning) | Controls 2-5 |
| 2026-08-22 | Privacy Officer | [to be filled] | [to be filled] |
| 2026-11-22 | Privacy Officer | | |
| 2027-05-22 | Privacy Officer | | |

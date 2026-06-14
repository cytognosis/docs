# SOP: DUC IAM Provisioning Pattern
**Control**: HIPAA 164.308(a)(3)(ii)(A) — Access Authorization
**Effective**: 2026-05-19 | **Owner**: Privacy Officer | **Review**: Annual

## Purpose

Establish a repeatable, auditable process for provisioning GCP access for each
Data Use Certification (DUC) or Data Use Agreement (DUA) approved by an external
data repository (NIH NDA, dbGaP, etc.).

## Pattern

Each DUC gets:
1. A dedicated **Google Group** (`duc-<name>@cytognosis.org`) — membership = approved users per the DUC's approved-user list
2. **Conditional IAM** on `cytognosis-phi-core` scoped to a sub-path (`duc-<name>/`)
3. A **KMS key ring** for CMEK of that sub-path (activate when first data arrives)
4. An entry in the **DUC log** (`compliance/duc-log.md`)

## Provisioning Script

```bash
#!/usr/bin/env bash
# Run as Privacy Officer. Requires: gcloud, appropriate org admin permissions.
set -euo pipefail

DUC_NAME="${1:?Usage: $0 <duc-name> (e.g. psychencoder, nbb, bsnip)}"
DUC_GROUP="duc-${DUC_NAME}@cytognosis.org"
BUCKET="cytognosis-phi-core"
SUBPATH="duc-${DUC_NAME}"
PROJECT="cytognosis-infrastructure"
LOCATION="us-central1"

echo "[1/5] Creating Google Group ${DUC_GROUP} (manual step)"
echo "      Go to: admin.google.com → Directory → Groups → Create group"
echo "      Name: DUC ${DUC_NAME^^} Approved Users"
echo "      Email: ${DUC_GROUP}"
read -p "Press Enter once group is created..."

echo "[2/5] Granting conditional IAM on phi-core bucket..."
gcloud storage buckets add-iam-policy-binding gs://${BUCKET} \
  --member="group:${DUC_GROUP}" \
  --role="roles/storage.objectViewer" \
  --condition="expression=resource.name.startsWith(\"projects/_/buckets/${BUCKET}/objects/${SUBPATH}/\"),title=duc-${DUC_NAME}-subpath,description=Restrict to DUC ${DUC_NAME} sub-path only" \
  --project=${PROJECT}

echo "[3/5] Creating KMS key ring (activate when first data ingested)..."
echo "      DEFER: gcloud kms keyrings create duc-${DUC_NAME} --location=${LOCATION} --project=${PROJECT}"
echo "      DEFER: gcloud kms keys create data-key-v1 --keyring=duc-${DUC_NAME} --location=${LOCATION} --purpose=encryption --rotation-period=90d --project=${PROJECT}"

echo "[4/5] Logging DUC in duc-log.md..."
cat >> "$(dirname "$0")/../docs/data-strategy/compliance/duc-log.md" << EOF

## DUC: ${DUC_NAME^^}
- **Group**: ${DUC_GROUP}
- **Bucket sub-path**: gs://${BUCKET}/${SUBPATH}/
- **Provisioned**: $(date -Iseconds)
- **Provisioned by**: $(gcloud config get-value account)
- **KMS key ring**: duc-${DUC_NAME} (deferred until data ingestion)
- **Approved user list**: [link to signed DUC document]
- **Expiration**: [date from DUC]
EOF

echo "[5/5] Done. Next steps:"
echo "  - Add approved users to ${DUC_GROUP} per signed DUC approved-user list"
echo "  - Activate KMS key when staging data ingestion"
echo "  - Notify users of access (gcloud storage ls gs://${BUCKET}/${SUBPATH}/)"
```

## De-provisioning (Expired DUC)

```bash
# 1. Remove all members from the group (admin.google.com)
# 2. Remove IAM binding
gcloud storage buckets remove-iam-policy-binding gs://cytognosis-phi-core \
  --member="group:duc-${DUC_NAME}@cytognosis.org" \
  --role="roles/storage.objectViewer"
# 3. If KMS was activated: schedule key destruction (cryptographic erasure)
gcloud kms keys versions destroy 1 --key=data-key-v1 \
  --keyring=duc-${DUC_NAME} --location=us-central1 --project=cytognosis-infrastructure
# 4. Set lifecycle on sub-path to delete objects
# 5. Record in duc-log.md
```

## Existing DUCs

| DUC | Group | Sub-path | Status | Expiration |
|---|---|---|---|---|
| NIH (placeholder) | duc-nih@cytognosis.org | duc-nih/ | Bucket created | TBD |

See `duc-log.md` for running log.

## References
- NIH GDS Policy 2025 §5 (Approved User management)
- HHS OCR de-identification guidance
- All of Us Researcher Workbench 2.0 (reference architecture)

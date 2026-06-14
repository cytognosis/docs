# Cytognosis Service Account Architecture

> **Status**: Active
> **Date**: 2026-06-14
> **Author**: @mohammadi
> **Audience**: engineers, operators
> **Tags**: `iam`, `service-accounts`, `oidc`

**Last verified: 2026-06-14**

## Canonical Service Accounts

This document is the authoritative reference for all GCP service accounts in the
Cytognosis ecosystem. All SAs are audited quarterly; stale ones are disabled then deleted.

> [!WARNING]
> The default compute SA on `cytohost` (`517562623935-compute@developer.gserviceaccount.com`) is **disabled**. cytohost currently has no functional service account, which will cause Cloud Logging, Monitoring, and Pub/Sub writes to fail. Remediation pending.

---

## Active Service Accounts

### `website-deployer` — Primary CI/CD SA

| Field | Value |
|---|---|
| **Email** | `website-deployer@cytognosis-infrastructure.iam.gserviceaccount.com` |
| **Project** | `cytognosis-infrastructure` |
| **Purpose** | All GitHub Actions CI/CD across the entire `cytognosis` GitHub org |
| **Created** | 2024 (original) |
| **Status** | ✅ Active |

**OIDC binding** (no long-lived keys — all auth via Workload Identity Federation):
```
Pool:      github-pool  (projects/517562623935/locations/global/workloadIdentityPools/github-pool)
Provider:  github-provider
Condition: attribute.repository_owner == "cytognosis"
```
This single binding covers **all repositories** under the `cytognosis` GitHub org automatically.
No per-repo configuration needed.

**Roles on `cytognosis-infrastructure`**:
- `roles/compute.loadBalancerAdmin` — DNS / load balancer management
- `roles/storage.objectAdmin` — read/write to all infra-project buckets

**Roles on `cytognosis-phi-prod`** (cross-project grants):
- `roles/artifactregistry.writer` — push Docker images to phi-prod registries
- `roles/run.admin` — deploy Cloud Run services
- `roles/iam.serviceAccountUser` — run Cloud Run services as the runtime SA
- `roles/secretmanager.secretAccessor` — read secrets at deploy time

**Usage in workflows**:
```yaml
- uses: google-github-actions/auth@v2
  with:
    workload_identity_provider: "projects/517562623935/locations/global/workloadIdentityPools/github-pool/providers/github-provider"
    service_account: "website-deployer@cytognosis-infrastructure.iam.gserviceaccount.com"
```

---

### `stories-api-sa` — Runtime SA for Stories API

| Field | Value |
|---|---|
| **Email** | `stories-api-sa@cytognosis-phi-prod.iam.gserviceaccount.com` |
| **Project** | `cytognosis-phi-prod` |
| **Purpose** | Runtime identity for the `stories-api` Cloud Run service |
| **Status** | ✅ Active |

**Roles**:
- `roles/datastore.user` — read/write Firestore/Datastore for the Stories API

**Note**: This SA has no OIDC binding — it is a runtime SA, not a CI SA.
Cloud Run attaches it to the service container identity automatically.

---

## Disabled Service Accounts

These SAs are disabled (not deleted) as a safety measure. They can be re-enabled
if a legitimate use case is identified, but should not be used in new infrastructure.

| Email | Reason disabled | Date |
|---|---|---|
| `517562623935-compute@developer.gserviceaccount.com` | Default compute SA — overly permissive, not used by any service | 2026-05-19 |
| `143911445857-compute@developer.gserviceaccount.com` | Default compute SA — overly permissive, not used by any service | 2026-05-19 |

---

## Deleted Service Accounts

| Email | Reason | Date |
|---|---|---|
| `github-action-deployer@cytognosis-phi-prod.iam.gserviceaccount.com` | Redundant — no OIDC binding, never referenced in any workflow. Roles migrated to `website-deployer`. | 2026-05-19 |

---

## Adding a New Service Account

Only create a new SA if:
1. The use case cannot be handled by `website-deployer` (CI/CD) or `stories-api-sa` (runtime)
2. The new SA follows least-privilege — only the minimum roles needed

**Template**:
```bash
gcloud iam service-accounts create <sa-name> \
  --display-name="<Human readable purpose>" \
  --project=<project-id>

# Add minimum required roles only
gcloud projects add-iam-policy-binding <project-id> \
  --member="serviceAccount:<sa-name>@<project-id>.iam.gserviceaccount.com" \
  --role="<specific-role>"

# For CI/CD: add OIDC binding (no long-lived keys)
gcloud iam service-accounts add-iam-policy-binding \
  <sa-name>@<project-id>.iam.gserviceaccount.com \
  --role="roles/iam.workloadIdentityUser" \
  --member="principalSet://iam.googleapis.com/projects/517562623935/locations/global/workloadIdentityPools/github-pool/attribute.repository_owner/cytognosis"

# Document in this file before merging
```

---

## Audit Checklist (Quarterly)

Run this to review all active SAs:
```bash
for project in cytognosis-infrastructure cytognosis-phi-prod; do
  echo "=== $project ==="
  gcloud iam service-accounts list --project=$project \
    --format="table(email,displayName,disabled)"
done
```

Review questions:
- [ ] Are all active SAs referenced in a current workflow or service?
- [ ] Do any SAs have broader roles than needed?
- [ ] Have any SAs generated keys (long-lived credentials)? If so, rotate or remove.
- [ ] Are disabled SAs still justified, or can they be deleted?

---

## Workload Identity Federation (OIDC)

**Pool**: `github-pool`
**Provider**: `github-provider`
**Attribute mapping**:
```json
{
  "google.subject": "assertion.sub",
  "attribute.repository": "assertion.repository",
  "attribute.repository_owner": "assertion.repository_owner",
  "attribute.actor": "assertion.actor",
  "attribute.aud": "assertion.aud"
}
```
**Condition**: `attribute.repository_owner == "cytognosis"`

This means **any repo under `github.com/cytognosis/`** can authenticate as
`website-deployer` via OIDC — no per-repo registration needed. The SA binding
uses `attribute.repository_owner` (org-wide), not `attribute.repository` (per-repo).

---

**Document version**: 1.1
**Last updated**: 2026-06-14
**Owner**: Infrastructure, Cytognosis Foundation
**Next audit**: 2026-08-19

> [!NOTE]
> Verified against live GCP state 2026-06-14. Two SAs confirmed in cytognosis-infrastructure (website-deployer active, default compute disabled). Two SAs confirmed in cytognosis-phi-prod (stories-api-sa active, default compute active). OIDC pool github-pool confirmed ACTIVE in cytognosis-infrastructure only (zero pools in cytognosis-phi-prod).

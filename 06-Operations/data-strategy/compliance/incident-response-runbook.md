# SOP: Incident Response Runbook

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: operators
> **Tags**: `operations`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)
**Control**: HIPAA 164.308(a)(6) — Security Incident Procedures
**Effective**: 2026-05-19 | **Owner**: Privacy Officer + Engineering | **Review**: Annual + post-incident

## Severity Levels

| Level | Definition | Response time | Example |
|---|---|---|---|
| P0 — Critical | Confirmed PHI breach or exfiltration | 1 hour | Unauthorized bucket access to phi-core |
| P1 — High | Suspected breach; system compromised | 4 hours | Unusual IAM grant; SA key leaked |
| P2 — Medium | Security anomaly; no confirmed breach | 24 hours | Failed auth spikes; new geo access |
| P3 — Low | Policy violation; no data impact | 72 hours | Workflow using wrong SA |

## Contacts

| Role | Name | Contact |
|---|---|---|
| Incident Commander | Shahin Mohammadi | mohammadi@cytognosis.org |
| Privacy Officer | [TBD] | [TBD] |
| Technical Lead | [TBD] | engineering@cytognosis.org |
| Legal | [TBD — engage for P0 only] | [TBD] |

---

## Scenario 1: Unauthorized Access to PHI Bucket (P0)

**Trigger**: Cloud Audit Log shows unexpected read/list on `gs://cytognosis-phi-core/`

```bash
# Step 1: Identify the accessor
gcloud logging read \
  'resource.type="gcs_bucket" AND resource.labels.bucket_name="cytognosis-phi-core" AND protoPayload.methodName=~"storage.objects"' \
  --project=cytognosis-infrastructure \
  --format="json" \
  --limit=50 | jq '.[] | {time: .timestamp, who: .protoPayload.authenticationInfo.principalEmail, what: .protoPayload.methodName, object: .protoPayload.resourceName}'

# Step 2: Revoke access immediately
gcloud projects remove-iam-policy-binding cytognosis-phi-prod \
  --member="<IDENTITY>" --role="<ROLE>"

# Step 3: Preserve evidence (do NOT delete logs)
# Export the relevant log entries to a tamper-evident location

# Step 4: Notify HHS OCR within 60 days (or 30 days if >500 individuals affected)
# HHS Breach Portal: https://ocrportal.hhs.gov/ocr/breach/wizard.jsf
```

**HHS notification requirement**: HIPAA Breach Notification Rule requires notice to
HHS and affected individuals within 60 days of discovering a breach affecting ePHI.

---

## Scenario 2: Service Account Key or OIDC Token Compromise (P1)

**Trigger**: Unexpected API calls using `website-deployer` SA; unknown GitHub Actions run

```bash
# Step 1: Immediately disable the SA
gcloud iam service-accounts disable \
  website-deployer@cytognosis-infrastructure.iam.gserviceaccount.com

# Step 2: Check recent activity
gcloud logging read \
  'protoPayload.authenticationInfo.serviceAccountKeyName=~"website-deployer"' \
  --project=cytognosis-infrastructure --limit=100

# Step 3: Re-enable after investigation, rotate OIDC pool if needed
gcloud iam service-accounts enable \
  website-deployer@cytognosis-infrastructure.iam.gserviceaccount.com

# Step 4: If OIDC pool compromised, delete and recreate provider:
gcloud iam workload-identity-pools providers delete github-provider \
  --workload-identity-pool=github-pool --location=global
```

---

## Scenario 3: Compute Node Compromise (P1)

**Trigger**: `cytohost` shows unexpected outbound connections; unusual process activity

```bash
# Step 1: Isolate the node (remove external IP / deny all egress)
gcloud compute instances delete-access-config cytohost \
  --access-config-name="External NAT" --zone=us-central1-b

# Step 2: Create a forensic disk snapshot
gcloud compute disks snapshot cytohost \
  --zone=us-central1-b --snapshot-names="forensic-$(date +%Y%m%d%H%M)"

# Step 3: Stop the instance
gcloud compute instances stop cytohost --zone=us-central1-b

# Step 4: Provision a clean replacement from the container framework
# (follow runner-setup.md)
```

---

## Scenario 4: Accidental Public Bucket Exposure (P2)

**Trigger**: Public access alert; data appears in public bucket scans

```bash
# Step 1: Re-enable uniform bucket-level access (removes all ACLs)
gcloud storage buckets update gs://<BUCKET> --uniform-bucket-level-access

# Step 2: Revoke any allUsers / allAuthenticatedUsers bindings
gcloud storage buckets remove-iam-policy-binding gs://<BUCKET> \
  --member=allUsers --role=roles/storage.objectViewer

# Step 3: Audit what was exposed (which objects, for how long)
# Check audit logs for public reads in the exposure window

# Step 4: If PHI was exposed → escalate to P0 procedures
```

---

## Scenario 5: CI/CD Supply Chain Attack (P2)

**Trigger**: Unexpected dependency in published package; unauthorized push to registries

```bash
# Step 1: Identify what was pushed
gcloud artifacts docker images list \
  us-central1-docker.pkg.dev/cytognosis-phi-prod/cytognosis-website-v2 \
  --include-tags --sort-by="~UPDATE_TIME" | head -10

# Step 2: Delete malicious artifact
gcloud artifacts docker images delete \
  us-central1-docker.pkg.dev/.../website:<SHA> --quiet

# Step 3: Rotate all CI secrets
# GitHub: org settings → Secrets → rotate any compromised values
# Secret Manager: create new secret versions, update Cloud Run env vars

# Step 4: Review and tighten OIDC condition
gcloud iam workload-identity-pools providers update-oidc github-provider \
  --workload-identity-pool=github-pool --location=global \
  --attribute-condition='attribute.repository_owner=="cytognosis"'
```

---

## Post-Incident Requirements

1. **Document**: Create `compliance/incident-log/YYYY-MM-DD-<description>.md`
2. **Root cause analysis**: Complete within 5 business days of P0/P1 closure
3. **Update SOPs**: If runbook was missing a step or a control failed, update this document
4. **HHS report**: For PHI breaches, file with HHS within 60 days regardless of scope
5. **Annual drill**: Conduct tabletop exercise for at least one scenario per year

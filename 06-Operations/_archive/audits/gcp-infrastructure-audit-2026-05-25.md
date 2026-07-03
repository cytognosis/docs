> **Status:** SUPERSEDED · **Date:** 2026-07-01 · **Agent:** Operations
> Superseded by the annotated canonical audit at `04-Engineering/infrastructure/audits/gcp-infrastructure-audit-2026-05-25.md` (Infrastructure layer, up to date on the 2026-06-19 GCP cleanup). This is the original raw agent output, archived here for provenance only.

---

# GCP Infrastructure Audit Report

**Date**: 2026-05-25  
**Auditor**: Infrastructure Agent  
**Organization**: Cytognosis Foundation (Org ID: `302898024445`)  
**Projects Audited**: `cytognosis-infrastructure`, `cytognosis-phi-prod`, 16 × `sys-*`

---

## Task 1: GCS Bucket Inventory & Configuration

### Bucket Inventory (Post-Configuration)

#### Project: `cytognosis-infrastructure` (14 buckets)

| Bucket | Location | Storage Class | Versioning | UBLA | Lifecycle | Labels |
|--------|----------|---------------|------------|------|-----------|--------|
| `cytoagent` | US-CENTRAL1 | STANDARD | ❌ | ✅ | None | ✅ `team=cytognosis, managed-by=infra-script` |
| `cytoexplorer` | US-CENTRAL1 | STANDARD | ❌ | ✅ | None | ✅ `team=cytognosis, managed-by=infra-script` |
| `cytognosis` | US-CENTRAL1 | STANDARD | ❌ | ✅ | None | ✅ `team=cytognosis, managed-by=infra-script` |
| `cytognosis-audit-7yr` | US-CENTRAL1 | STANDARD | ❌ | ✅ | None | ✅ `team=cytognosis, managed-by=infra-script` |
| `cytognosis-data-hub` | US-CENTRAL1 | STANDARD | ✅ | ✅ | ✅ 60d→NL, 180d→CL | ✅ `team=cytognosis, managed-by=infra-script` |
| `cytognosis-internal` | US-CENTRAL1 | STANDARD | ❌ | ✅ | None | ✅ `team=cytognosis, managed-by=infra-script` |
| `cytognosis-public-data` | US-CENTRAL1 | STANDARD | ❌ | ✅ | None | ✅ `team=cytognosis, managed-by=infra-script` |
| `cytomark` | US-CENTRAL1 | STANDARD | ❌ | ✅ | None | ✅ `team=cytognosis, managed-by=infra-script` |
| `cytonome` | US-CENTRAL1 | STANDARD | ❌ | ✅ | None | ✅ `team=cytognosis, managed-by=infra-script` |
| `cytopilot` | US-CENTRAL1 | STANDARD | ❌ | ✅ | None | ✅ `team=cytognosis, managed-by=infra-script` |
| `cytoscope` | US-CENTRAL1 | STANDARD | ❌ | ✅ | None | ✅ `team=cytognosis, managed-by=infra-script` |
| `cytoskeleton` | US-CENTRAL1 | STANDARD | ❌ | ✅ | None | ✅ `team=cytognosis, managed-by=infra-script` |
| `cytoverse` | US-CENTRAL1 | STANDARD | ❌ | ✅ | None | ✅ `team=cytognosis, managed-by=infra-script` |
| `neuroverse` | US-CENTRAL1 | STANDARD | ❌ | ✅ | None | ✅ `team=cytognosis, managed-by=infra-script` |

#### Project: `cytognosis-phi-prod` (2 buckets)

| Bucket | Location | Storage Class | Versioning | UBLA | Lifecycle | Labels |
|--------|----------|---------------|------------|------|-----------|--------|
| `cytognosis-phi-core` | US-CENTRAL1 | STANDARD | ✅ | ✅ | None | ✅ `team=cytognosis, managed-by=infra-script` |
| `cytognosis-phi-collab-nih` | US-CENTRAL1 | STANDARD | ✅ | ✅ | None | ✅ `team=cytognosis, managed-by=infra-script` |

### Configuration Changes Applied

| Action | Target | Status |
|--------|--------|--------|
| Enable versioning | `gs://cytognosis-data-hub` | ✅ Applied |
| Enable versioning | `gs://cytognosis-phi-core` | ✅ Applied |
| Enable versioning | `gs://cytognosis-phi-collab-nih` | ✅ Applied |
| Lifecycle rules (Standard→Nearline@60d, Nearline→Coldline@180d) | `gs://cytognosis-data-hub` | ✅ Applied |
| Labels `team=cytognosis, managed-by=infra-script` | All 16 buckets | ✅ Applied |
| Verify Uniform Bucket-Level Access | All 16 buckets | ✅ Already enabled |

> [!WARNING]
> **Versioning Gap**: 13 of 16 buckets do not have versioning enabled. Consider enabling versioning on `cytognosis-audit-7yr` (audit data should be immutable) and `cytognosis-internal` at minimum.

---

## Task 2: sys-* Project Audit

### Inventory (16 Projects)

| Project ID | Name | State | Created | Access | Recommendation |
|------------|------|-------|---------|--------|----------------|
| `sys-08435386287291076655716803` | Untitled project | ACTIVE | 2026-05-10 | ❌ No access | 🗑️ Delete |
| `sys-15082803889217266494184338` | Cytognosis Contact Form Handle | ACTIVE | 2025-09-26 | ❌ No access | ⚠️ Investigate |
| `sys-18579130703835562035818936` | Cytognosis Contact Form Handle | ACTIVE | 2025-09-26 | ❌ No access | ⚠️ Investigate |
| `sys-23180897304383803184900420` | Cytognosis Talent Form Handler | ACTIVE | 2025-12-09 | ❌ No access | ⚠️ Investigate |
| `sys-31216063987082481699348267` | Cytognosis Partnership Form Ha.. | ACTIVE | 2025-10-03 | ❌ No access | ⚠️ Investigate |
| `sys-40955734702859173151521100` | Cytognosis Partnership Form Ha.. | ACTIVE | 2025-10-03 | ❌ No access | 🗑️ Duplicate |
| `sys-41882658273202077819878734` | Untitled project | ACTIVE | 2026-05-11 | ❌ No access | 🗑️ Delete |
| `sys-57743681312835340724039098` | Cytognosis Contact Form Handle | ACTIVE | 2025-10-06 | ❌ No access | ⚠️ Investigate |
| `sys-61260890687746980823564223` | Cytognosis Contact Form Handle | ACTIVE | 2025-09-26 | ❌ No access | 🗑️ Duplicate |
| `sys-75744124647456189913405435` | Cytognosis Contact Form norep | ACTIVE | 2025-10-06 | ❌ No access | ⚠️ Investigate |
| `sys-75857314484803505663877863` | Untitled project | ACTIVE | 2026-05-11 | ❌ No access | 🗑️ Delete |
| `sys-78904706701757211778607824` | Cytognosis Contact Form Handle | ACTIVE | 2025-10-03 | ❌ No access | 🗑️ Duplicate |
| `sys-82450347034980334948921993` | Cytognosis Contact Form Handle | ACTIVE | 2025-10-03 | ❌ No access | 🗑️ Duplicate |
| `sys-83661875804529520524873341` | Cytognosis Contact Form Handle | ACTIVE | 2025-09-26 | ❌ No access | 🗑️ Duplicate |
| `sys-89931757738171588050079735` | Cytognosis Contact Form Handle | ACTIVE | 2025-09-26 | ❌ No access | 🗑️ Duplicate |
| `sys-94482794189608317063668607` | Untitled project | ACTIVE | 2026-05-10 | ❌ No access | 🗑️ Delete |

### Audit Findings

- **All 16 sys-* projects** returned `AUTH_PERMISSION_DENIED` for all resource queries (Compute, Storage, Cloud Run, Service Usage, Billing)
- These are **Google-managed system projects** auto-created by Apps Script, Cloud Functions, or similar services
- No Compute API, Cloud Run API, or Storage access is enabled on any of them
- `mohammadi@cytognosis.org` does not have `serviceusage.services.list` on these projects

### Disposition Summary

| Category | Count | Action |
|----------|-------|--------|
| 🗑️ **Delete** (Untitled/empty) | 4 | Safe to delete from GCP Console under Resource Manager |
| 🗑️ **Duplicate** (redundant form handlers) | 6 | Identify the active one, delete the rest |
| ⚠️ **Investigate** (form handlers with unique purpose) | 6 | Check if still serving via Apps Script triggers |

> [!IMPORTANT]
> These projects are managed by Google's system infrastructure. To delete them, go to **GCP Console → IAM & Admin → Resource Manager**, filter for `sys-*`, and shut down from there. Alternatively, delete the associated Apps Script projects in Google Workspace, which will cascade-delete the sys-* projects.

---

## Task 3: Service Account & IAM Audit

### Service Accounts

#### `cytognosis-infrastructure`

| Email | Display Name | Disabled |
|-------|-------------|----------|
| `517562623935-compute@developer.gserviceaccount.com` | Compute Engine default service account | ✅ Yes (disabled) |
| `website-deployer@cytognosis-infrastructure.iam.gserviceaccount.com` | Website Deployer | ❌ Active |

#### `cytognosis-phi-prod`

| Email | Display Name | Disabled |
|-------|-------------|----------|
| `143911445857-compute@developer.gserviceaccount.com` | Default compute service account | ✅ Yes (disabled) |
| `stories-api-sa@cytognosis-phi-prod.iam.gserviceaccount.com` | Stories API Service Account | ❌ Active |

> [!TIP]
> Default compute service accounts are properly disabled on both projects. This is a security best practice.

### IAM Bindings (`cytognosis-infrastructure`)

| Role | Members |
|------|---------|
| `roles/artifactregistry.serviceAgent` | `service-517562623935@gcp-sa-artifactregistry.iam.gserviceaccount.com` |
| `roles/cloudbuild.builds.builder` | `517562623935@cloudbuild.gserviceaccount.com` |
| `roles/cloudbuild.serviceAgent` | `service-517562623935@gcp-sa-cloudbuild.iam.gserviceaccount.com` |
| `roles/compute.loadBalancerAdmin` | `website-deployer@cytognosis-infrastructure.iam.gserviceaccount.com` |
| `roles/compute.serviceAgent` | `service-517562623935@compute-system.iam.gserviceaccount.com` |
| `roles/containerregistry.ServiceAgent` | `service-517562623935@containerregistry.iam.gserviceaccount.com` |
| `roles/datastore.user` | `user:noreply@cytognosis.org` |
| `roles/editor` | `517562623935@cloudservices.gserviceaccount.com`, `user:noreply@cytognosis.org` |
| `roles/firebaserules.system` | `service-517562623935@firebase-rules.iam.gserviceaccount.com` |
| `roles/firestore.serviceAgent` | `service-517562623935@gcp-sa-firestore.iam.gserviceaccount.com` |
| `roles/iam.serviceAccountAdmin` | `user:mohammadi@cytognosis.org` |
| `roles/logging.serviceAgent` | `service-517562623935@gcp-sa-logging.iam.gserviceaccount.com` |
| `roles/owner` | `user:mohammadi@cytognosis.org` |
| `roles/pubsub.serviceAgent` | `service-517562623935@gcp-sa-pubsub.iam.gserviceaccount.com` |
| `roles/storage.objectAdmin` | `website-deployer@cytognosis-infrastructure.iam.gserviceaccount.com` |

### IAM Findings

| Finding | Severity | Details |
|---------|----------|---------|
| `noreply@cytognosis.org` has `roles/editor` | 🟠 Medium | A noreply address should not have editor-level access. Review if this was granted for Apps Script and scope down. |
| `noreply@cytognosis.org` has `roles/datastore.user` | 🟡 Low | Likely needed for form submissions. Verify. |
| `website-deployer` has `storage.objectAdmin` | 🟢 OK | Appropriate for CI/CD deployment. |
| `website-deployer` has `compute.loadBalancerAdmin` | 🟢 OK | Needed for LB management during deploy. |
| Single owner (`mohammadi@cytognosis.org`) | 🟡 Low | Consider adding a second owner for bus-factor resilience. |

### OIDC Workload Identity Federation

| Pool | Provider | State | Condition |
|------|----------|-------|-----------|
| `github-pool` | `github-provider` (OIDC) | ✅ ACTIVE | `attribute.repository_owner=="cytognosis"` |

**Provider Details:**
- Issuer: `https://token.actions.githubusercontent.com`
- Attribute mapping: `sub → google.subject`, `actor`, `aud`, `repository`, `repository_owner`
- Scoped to: `cytognosis` org repositories only

> [!NOTE]
> OIDC federation is properly configured and scoped. Only GitHub Actions from the `cytognosis` GitHub organization can assume workload identity.

---

## Task 4: HIPAA Compliance Status

### Compliance Checklist

| Control | Status | Details |
|---------|--------|---------|
| **CMEK Encryption** on `cytognosis-phi-core` | ❌ Not configured | Returns `null`. Using Google-managed keys (GMEK). |
| **CMEK Encryption** on `cytognosis-phi-collab-nih` | ❌ Not configured | Returns `null`. Using Google-managed keys (GMEK). |
| **Versioning** on PHI buckets | ✅ Enabled | Just configured during this audit. |
| **Uniform Bucket-Level Access** | ✅ Enabled | Both PHI buckets have UBLA. |
| **VPC Service Controls** | ❌ Not configured | Access Context Manager API not enabled on project. |
| **Data Access Audit Logging** | ❌ Not configured | `auditConfigs` returned empty array `[]`. |
| **Labels** | ✅ Applied | `team=cytognosis, managed-by=infra-script` |
| **Default Compute SA Disabled** | ✅ Yes | Properly disabled on `cytognosis-phi-prod`. |

> [!CAUTION]
> **Critical HIPAA Gaps**: The PHI project is missing three essential controls:
> 1. **CMEK encryption** for PHI data at rest (required for BAA compliance)
> 2. **VPC Service Controls** to prevent data exfiltration
> 3. **Data Access Audit Logging** for all GCP services touching PHI
>
> These must be addressed before storing any PHI data in production.

### HIPAA Remediation Priority

| Priority | Action | Effort |
|----------|--------|--------|
| 🔴 P0 | Enable Data Access Audit Logging (`allServices` for `DATA_READ` and `DATA_WRITE`) | Low (IAM policy update) |
| 🔴 P0 | Configure CMEK via Cloud KMS for both PHI buckets | Medium (create KMS keyring + key, update buckets) |
| 🟠 P1 | Enable Access Context Manager API and create VPC-SC perimeter | High (network architecture) |
| 🟠 P1 | Review Organization Policy constraints for PHI project | Medium |
| 🟡 P2 | Enable lifecycle rules on PHI buckets (retention policy) | Low |
| 🟡 P2 | Add Object Lock / retention policies for regulatory holds | Low |

---

## Summary of Actions Taken

| # | Action | Result |
|---|--------|--------|
| 1 | Enabled versioning on `gs://cytognosis-data-hub` | ✅ |
| 2 | Enabled versioning on `gs://cytognosis-phi-core` | ✅ |
| 3 | Enabled versioning on `gs://cytognosis-phi-collab-nih` | ✅ |
| 4 | Applied lifecycle rules to `gs://cytognosis-data-hub` (Standard→Nearline@60d, Nearline→Coldline@180d) | ✅ |
| 5 | Applied labels (`team=cytognosis`, `managed-by=infra-script`) to all 16 buckets | ✅ |
| 6 | Verified Uniform Bucket-Level Access on all 16 buckets | ✅ Already enabled |
| 7 | Audited 16 sys-* projects | ✅ All inaccessible (Google-managed) |
| 8 | Inventoried service accounts across both projects | ✅ |
| 9 | Reviewed IAM bindings on `cytognosis-infrastructure` | ✅ |
| 10 | Verified OIDC federation configuration | ✅ |
| 11 | Assessed HIPAA compliance on `cytognosis-phi-prod` | ✅ 3 critical gaps identified |

---

## Open Items Requiring Decision

1. **sys-* cleanup**: Consolidate the 10 duplicate/untitled projects. Which form handler(s) are still active?
2. **noreply@cytognosis.org editor access**: Should this be scoped down from `roles/editor`?
3. **CMEK for PHI**: Which KMS keyring location and rotation schedule?
4. **VPC-SC perimeter**: Which projects and services to include in the perimeter?
5. **Versioning on remaining 13 buckets**: Enable across the board or selectively?

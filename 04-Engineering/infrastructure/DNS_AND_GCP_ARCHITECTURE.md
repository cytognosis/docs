> **Status**: Approved
> **Date**: 2026-06-14
> **Author**: Cytognosis Engineering
> **Audience**: Engineering, DevOps
> **Tags**: `dns`, `gcp`, `architecture`, `networking`
> **Last verified**: 2026-06-14 against gcloud

# DNS & GCP Architecture

## BLUF

Six Cloud DNS zones in `cytognosis-infrastructure` — three duplicate pairs. Authoritative zones are `cg-org`, `com-zone`, and `cg-ai`. The three duplicates are pending deletion. All `*.cytognosis.org` service subdomains currently point to cytohost's **ephemeral** IP 34.171.23.255; attaching the reserved static IP is a pending remediation.

---

## 1. GCP Projects Topology

Cytognosis segregates workloads across two live projects to enforce HIPAA compliance boundaries.

| Project ID | Purpose | Classification |
|---|---|---|
| `cytognosis-infrastructure` | DNS zones, IAM root, Artifact Registry, legacy buckets, Compute Engine | Management |
| `cytognosis-phi-prod` | Cloud Run (website + Stories API), PHI storage, HIPAA workloads | **Sensitive (PHI)** |
| `cytognosis-data` | Data platform, analytics | **Planned — does not exist** |

---

## 2. Domain Taxonomy

Three primary apex domains registered at Squarespace:

| Domain | Purpose |
|---|---|
| `cytognosis.org` | Primary canonical |
| `cytognosis.com` | Secondary canonical |
| `cytognosis.ai` | Technology canonical |

---

## 3. Cloud DNS Zones and Dedup Plan

Six managed zones exist in `cytognosis-infrastructure`, one for each domain × 2. Only one zone per domain is authoritative (delegated at the registrar). The duplicates are slated for deletion.

| Domain | Zone to KEEP | Zone to DELETE (dedup pending) | Evidence |
|---|---|---|---|
| cytognosis.org | `cg-org` (ns-cloud-d, SOA serial 13) | `org-zone` (ns-cloud-b, serial 4) | `cg-org` has complete DKIM, DMARC, full subdomain set, current IP (34.171.23.255). `org-zone` has stale IPs and partial DKIM. |
| cytognosis.com | `com-zone` (ns-cloud-c, SOA serial 6) | `cg-com` (ns-cloud-a, serial 9) | `com-zone` has 4-address A record and complete 2048-bit DKIM. `cg-com` has single-address A and partial DKIM (first segment missing). |
| cytognosis.ai | `cg-ai` (ns-cloud-d, SOA serial 11) | `ai-zone` (ns-cloud-e, serial 5) | `cg-ai` has real infra IP (34.98.121.181), SPF/DMARC/Anthropic TXT, modern www A record. `ai-zone` uses legacy Google Sites IPs (216.239.x.x). |

> [!WARNING]
> **Pre-deletion checklist** (do not delete duplicates until these are migrated to the keeper zone):
> - `zotero.cytognosis.org A 34.61.134.177` exists only in `org-zone`; migrate to `cg-org` before deleting.
> - Anthropic domain verification TXT exists in `cg-com` but not in `com-zone`; copy to `com-zone` before deleting.
> - Registrar delegation must be verified per domain; the "keep" verdict is based on record completeness, not confirmed registrar state.

---

## 4. Canonical DNS Records (Keeper Zones)

### cytognosis.org — zone `cg-org`

```text
# Apex
@      A      300    216.239.32.21, 216.239.34.21, 216.239.36.21, 216.239.38.21
@      AAAA   300    2001:4860:4802:32::15, .34::15, .36::15, .38::15

# www
www    CNAME  300    ghs.googlehosted.com.

# Email
@      MX     300    1 aspmx.l.google.com., 5 alt1/alt2, 10 alt3/alt4
@      TXT    300    v=spf1 include:_spf.google.com ~all
_dmarc TXT    300    v=DMARC1; p=none; rua=mailto:dmarc@cytognosis.org
google._domainkey  TXT  300  [full 2-segment DKIM key]

# cytohost service subdomains (current ephemeral IP — remediation pending)
cal        A  300   34.171.23.255
code       A  300   34.171.23.255
draw       A  300   34.171.23.255
hub        A  300   34.171.23.255
kg         A  300   34.171.23.255
mermaid    A  300   34.171.23.255
mlflow     A  300   34.171.23.255
notes      A  300   34.171.23.255
prefect    A  300   34.171.23.255
search     A  300   34.171.23.255
whiteboard A  300   34.171.23.255
wiki       A  300   34.171.23.255

# Third-party verifications
@     TXT  300  google-site-verification=...
@     TXT  300  anthropic-domain-verification-1fpkv3=RwAA...  [note: possible typo in value]
@     TXT  300  canva-site-verification=...
```

> [!WARNING]
> All service subdomain A records point to `34.171.23.255` (ephemeral). If cytohost restarts, all subdomain DNS breaks. Remediation: attach `cytohost-ip` (136.111.39.188) to the VM and update these records.

### cytognosis.com — zone `com-zone`

```text
# Apex (full redundant set)
@      A     300    216.239.32.21, .34.21, .36.21, .38.21
@      AAAA  300    2001:4860:4802:32/34/36/38::15
www    A     300    [same set]
www    AAAA  300    [same set]

# Email
@  MX   21600  5 smtp.google.com.
@  TXT  21600  v=spf1 ...  [3-part SPF]
_dmarc  TXT  21600  v=DMARC1; p=quarantine; ...
google._domainkey  TXT  300  [full 2048-bit DKIM key]
@  TXT  21600  google-site-verification=...
```

> [!NOTE]
> Anthropic domain verification TXT exists in `cg-com` only. Must be migrated to `com-zone` before `cg-com` is deleted.

### cytognosis.ai — zone `cg-ai`

```text
# Apex — CDN/LB frontend
@    A     300   34.98.121.181  (cytognosis-ip static address — global LB/CDN)
@    AAAA  300   2600:1901:0:a16f::
www  A     300   34.36.143.5
www  AAAA  300   2600:1901:0:a16f::

# Email
@  MX   300  1 aspmx.l.google.com., 5 alt1/alt2, 10 alt3/alt4
@  TXT  300  v=spf1 include:_spf.google.com ~all
_dmarc  TXT  300  v=DMARC1; p=none; ...
google._domainkey  TXT  300  [empty string — DKIM BROKEN]
@  TXT  300  anthropic-domain-verification=...
@  TXT  300  google-site-verification=...
```

> [!WARNING]
> `google._domainkey.cytognosis.ai` in `cg-ai` is an **empty TXT record** — DKIM signing for `cytognosis.ai` email will fail. A valid DKIM key must be populated.

---

## 5. Static IP Addresses

| Name | Address | Region | Status | Usage |
|---|---|---|---|---|
| `cytognosis-ip` | 34.98.121.181 | global | RESERVED | `cytognosis.ai` A record (CDN/LB frontend) |
| `core-services-ip` | 34.70.62.117 | us-central1 | RESERVED | Legacy subdomain records in `org-zone` (stale zone) |
| `cytohost-ip` | 136.111.39.188 | us-central1 | **RESERVED BUT NOT ATTACHED** | Should be attached to cytohost; currently unused |

---

## 6. Email Routing (Google Workspace)

Standard Google Workspace MX for all three domains:

```text
1  aspmx.l.google.com.
5  alt1.aspmx.l.google.com.
5  alt2.aspmx.l.google.com.
10 alt3.aspmx.l.google.com.
10 alt4.aspmx.l.google.com.
```

---

## 7. DNS Remediation Checklist (Verified 2026-06-14)

Six Cloud DNS zones, three duplicate pairs. Authoritative delegation: `.org` → `cg-org` (ns-cloud-d), `.com` → `com-zone` (ns-cloud-c), `.ai` → `ai-zone` (ns-cloud-e).

> [!IMPORTANT]
> Items marked **email-sensitive / irreversible** require care. A misconfigured SPF, DMARC, or DKIM record can silently break outbound email delivery for all cytognosis.ai senders. Make changes one record at a time and allow 24-48 hours for propagation before proceeding to the next item.

### Done

- [x] `zotero.cytognosis.org A 34.61.134.177` added to `cg-org` (was only in `org-zone`)
- [x] `cytohost-static` static IP reservation created; `34.171.23.255` promoted from ephemeral to static (2026-06-14)

### Pending — Infrastructure (safe, non-email)

- [ ] **Release orphaned reserved IP `cytohost-ip` (136.111.39.188)** — RESERVED but not attached to any VM; safely releasable once `cytohost-static` is confirmed stable. Run: `gcloud compute addresses delete cytohost-ip --region us-central1`
- [ ] **Verify registrar delegation per domain** — Confirm at Squarespace that each domain's NS records match the authoritative zone's nameservers: `.org` → ns-cloud-d, `.com` → ns-cloud-c, `.ai` → ns-cloud-e. Verdicts above are based on record completeness, not confirmed registrar state.
- [ ] **Decide `.ai` apex hosting** — `ai-zone` A records (216.239.x.x) point to Google Sites. Confirm whether `cytognosis.ai` should remain a Google Sites landing page or migrate to the infrastructure LB (34.98.121.181 = `cytognosis-ip`). This decision gates the zone consolidation below.

### Pending — Email-Sensitive (require care, do in order)

> [!CAUTION]
> Each item below touches live DNS records that affect email delivery. Apply one record at a time. Verify with `dig TXT cytognosis.ai` or [Google Admin Toolbox](https://toolbox.googleapps.com/apps/checkmx/) before proceeding to the next item.

**For `cytognosis.ai` (live zone: `ai-zone`, ns-cloud-e):**

- [ ] **Add SPF to `ai-zone`** — `ai-zone` currently lacks an SPF record. `cg-ai` has `v=spf1 include:_spf.google.com ~all`. Add to `ai-zone` apex:
  ```
  TXT  "v=spf1 include:_spf.google.com ~all"
  ```
- [ ] **Add DMARC to `ai-zone`** — `ai-zone` has no `_dmarc` record. Copy from `cg-ai` (p=none):
  ```
  _dmarc.cytognosis.ai.  TXT  "v=DMARC1; p=none; rua=mailto:dmarc@cytognosis.ai"
  ```
- [ ] **Fix DKIM in `ai-zone`** — `google._domainkey.cytognosis.ai` in `cg-ai` is an **empty TXT record** (DKIM signing will fail for cytognosis.ai email). Get the real DKIM key from Google Workspace Admin > Apps > Google Workspace > Gmail > Authenticate email, then add to `ai-zone`:
  ```
  google._domainkey.cytognosis.ai.  TXT  "v=DKIM1; k=rsa; p=<real-key-from-admin>"
  ```

**For `cytognosis.com` (live zone: `com-zone`, ns-cloud-c):**

- [ ] **Copy Anthropic domain verification TXT to `com-zone`** — Present in `cg-com` only. Must be migrated before `cg-com` is deleted. Value (from `cg-com`):
  ```
  cytognosis.com.  TXT  "anthropic-domain-verification-1fpkv3=..."
  ```
  Retrieve exact value from `cg-com` with: `gcloud dns record-sets list --zone=cg-com --name=cytognosis.com. --type=TXT`

### Pending — Zone Cleanup (do last, after all records verified)

> [!WARNING]
> Delete zones only after: (1) all email-sensitive records above are live in the authoritative zones, (2) registrar delegation is confirmed, and (3) you have verified email delivery still works for all three domains.

- [ ] Delete `org-zone` (cytognosis.org non-authoritative duplicate, ns-cloud-b)
- [ ] Delete `cg-com` (cytognosis.com non-authoritative duplicate, ns-cloud-a)
- [ ] Delete `cg-ai` (cytognosis.ai non-authoritative duplicate, ns-cloud-d) — only after records copied to `ai-zone`

**Delete command pattern:** `gcloud dns managed-zones delete <zone-name> --project=cytognosis-infrastructure`
Zones must be empty (all non-SOA/NS records deleted) before the zone itself can be deleted.

---

## 8. Static IP Summary

| Name | Address | Region | Status | Usage |
|---|---|---|---|---|
| `cytohost-static` | 34.171.23.255 | us-central1 | ATTACHED to cytohost | All `*.cytognosis.org` subdomain A records |
| `cytognosis-ip` | 34.98.121.181 | global | RESERVED | `cytognosis.ai` A record (CDN/LB frontend) |
| `core-services-ip` | 34.70.62.117 | us-central1 | RESERVED | Legacy records in `org-zone` (stale zone, pending delete) |
| `cytohost-ip` | 136.111.39.188 | us-central1 | **ORPHANED — releasable** | Was planned for cytohost; replaced by `cytohost-static` |

---

## Cross-References

| Document | Relationship |
|---|---|
| [Architecture Overview](architecture.md) | Parent topology |
| [QUICK_REFERENCE.md](QUICK_REFERENCE.md) | Master infra quick reference including DNS zone table |
| [GCP Setup](gcp-setup.md) | Bucket and IAM detail |
| [Hosting & Deployment](HOSTING_AND_DEPLOYMENT.md) | Cloud Run + CDN frontend |
| [Compute: Node Types](compute/node-types.md) | cytohost VM detail |

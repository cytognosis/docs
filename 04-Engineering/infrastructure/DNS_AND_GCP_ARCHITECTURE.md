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

## 7. Pending Remediation Items

| Item | Priority | Detail |
|---|---|---|
| Attach `cytohost-ip` to VM | High | Prevents DNS breakage on VM restart; update all `*.cytognosis.org` A records to 136.111.39.188 after attach |
| Fix `cg-ai` DKIM record | High | `google._domainkey.cytognosis.ai` is empty; populate with real DKIM key |
| DNS zone deduplication | Medium | Delete `org-zone`, `cg-com`, `ai-zone` after pre-deletion checklist above |
| Migrate `zotero.cytognosis.org` record | Medium | A → 34.61.134.177 exists only in `org-zone`; add to `cg-org` |
| Migrate Anthropic TXT to `com-zone` | Medium | Required before deleting `cg-com` |
| Verify registrar delegation | Medium | Confirm correct NS delegation at Squarespace for each domain |
| Fix Anthropic TXT typo check | Low | `anthropic-domain-verification-1fpkv3=RwAA...` (vs RWaA) — verify against Anthropic console |

---

## Cross-References

| Document | Relationship |
|---|---|
| [Architecture Overview](architecture.md) | Parent topology |
| [GCP Setup](gcp-setup.md) | Bucket and IAM detail |
| [Hosting & Deployment](HOSTING_AND_DEPLOYMENT.md) | Cloud Run + CDN frontend |
| [Compute: Node Types](compute/node-types.md) | cytohost VM detail |

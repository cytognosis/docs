> **Status**: Approved
> **Date**: 2026-06-14
> **Author**: Cytognosis Engineering
> **Audience**: Engineering, DevOps
> **Tags**: `dns`, `gcp`, `architecture`, `networking`
> **Variants**: Technical (this doc) - Readable (same filename in Obsidian vault: 04-Engineering/infrastructure/) - Agent (n/a)
> **Last verified**: 2026-06-19 against gcloud

# DNS & GCP Architecture

## BLUF

Three Cloud DNS zones in `cytognosis-infrastructure`: `cg-org`, `com-zone`, `cg-ai`. Duplicate zones (`org-zone`, `cg-com`, `ai-zone`) were deleted 2026-06-19. All `*.cytognosis.org` service subdomains point to the `cytohost-static` IP (34.171.23.255). One static IP remains: `cytohost-static`.

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

## 3. Cloud DNS Zones

Three managed zones in `cytognosis-infrastructure`, one per domain. Duplicate zones were deleted 2026-06-19 after migrating all unique records to the keeper zones.

| Domain | Zone | Nameservers | Status |
|---|---|---|---|
| cytognosis.org | `cg-org` | ns-cloud-d | ✅ Authoritative |
| cytognosis.com | `com-zone` | ns-cloud-c | ✅ Authoritative |
| cytognosis.ai | `cg-ai` | ns-cloud-d | ✅ Authoritative |

> [!NOTE]
> **Deleted zones (2026-06-19)**: `org-zone` (was ns-cloud-b), `cg-com` (was ns-cloud-a), `ai-zone` (was ns-cloud-e). All unique records (zotero A record, Anthropic verification TXT) were migrated to keeper zones before deletion.

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

# cytohost service subdomains (cytohost-static IP)
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

> [!NOTE]
> All service subdomain A records point to `34.171.23.255` (`cytohost-static`), a static IP promoted from ephemeral on 2026-06-14. DNS is stable across VM restarts.

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
> Anthropic domain verification TXT was migrated from `cg-com` to `com-zone` before `cg-com` was deleted (2026-06-19).

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
| `cytohost-static` | 34.171.23.255 | us-central1 | **ATTACHED** to cytohost | All `*.cytognosis.org` subdomain A records |

> [!NOTE]
> **Deleted IPs (2026-06-19)**: `cytognosis-ip` (34.98.121.181, global), `core-services-ip` (34.70.62.117, us-central1), `cytohost-ip` (136.111.39.188, us-central1). All were orphaned or unused. Only `cytohost-static` remains.

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

## 7. DNS Remediation Log

All remediation items from the 2026-06-14 audit have been completed as of 2026-06-19.

### Completed (2026-06-14 through 2026-06-19)

- [x] `zotero.cytognosis.org A 34.61.134.177` added to `cg-org` (was only in `org-zone`)
- [x] `cytohost-static` static IP reservation created; `34.171.23.255` promoted from ephemeral to static (2026-06-14)
- [x] Orphaned reserved IPs released: `cytohost-ip` (136.111.39.188), `core-services-ip` (34.70.62.117), `cytognosis-ip` (34.98.121.181) (2026-06-19)
- [x] Anthropic domain verification TXT migrated from `cg-com` to `com-zone` (2026-06-19)
- [x] Duplicate zones deleted: `org-zone`, `cg-com`, `ai-zone` (2026-06-19)
- [x] `cytohost-sa` service account created and attached to cytohost with OS Login enabled (2026-06-19)

### Remaining (email-sensitive, still pending)

> [!CAUTION]
> These items touch live DNS records that affect email delivery. Apply one record at a time. Verify with `dig TXT cytognosis.ai` or [Google Admin Toolbox](https://toolbox.googleapps.com/apps/checkmx/) before proceeding.

- [ ] **Fix DKIM for `cytognosis.ai`** — `google._domainkey.cytognosis.ai` in `cg-ai` has an **empty TXT record** (DKIM signing fails). Get the real key from Google Workspace Admin > Apps > Gmail > Authenticate email.

---

## 8. Static IP Summary

| Name | Address | Region | Status | Usage |
|---|---|---|---|---|
| `cytohost-static` | 34.171.23.255 | us-central1 | **ATTACHED** to cytohost | All `*.cytognosis.org` subdomain A records |

---

## Cross-References

| Document | Relationship |
|---|---|
| [Architecture Overview](architecture.md) | Parent topology |
| [QUICK_REFERENCE.md](QUICK_REFERENCE.md) | Master infra quick reference including DNS zone table |
| [GCP Setup](gcp-setup.md) | Bucket and IAM detail |
| [Hosting & Deployment](HOSTING_AND_DEPLOYMENT.md) | Cloud Run + CDN frontend |
| [Compute: Node Types](compute/node-types.md) | cytohost VM detail |

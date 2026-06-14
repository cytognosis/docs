# DNS & GCP Architecture

**Last Updated**: May 2026

## 1. GCP Projects Topology

Cytognosis segregates workloads aggressively to enforce HIPAA-ready compliance boundaries.

| Project ID | Purpose | Classification |
|------------|---------|----------------|
| `cytognosis-infrastructure` | Primary structural footprint (DNS Zones, legacy bucket graveyard, IAM root) | Management |
| `cytognosis-phi-prod` | Secure backend for Website & Services, User data | **Sensitive (PHI)** |
| `cytognosis-data` | Data platform, Analytics | Regulated |

## 2. Domain Taxonomy

The Cytognosis Foundation controls three primary apex domains:

- `.org` (Primary Canonical)
- `.com` (Secondary Canonical)
- `.ai` (Technology Canonical)

All legacy domains hosted on Google Domains have fully migrated to Squarespace as part of the 2024 acquisition.

## 3. DNS Routing (Cloud DNS)

We enforce a hybrid DNS architecture split between our stateless consumer fronts and our stateful internal operations.

- **Main Website**: Apex and `www` traffic explicitly resolves to Google Cloud Run via Serverless NEGs.
- **Core Services**: Specific subdomains (e.g., `cal.`, `notes.`, `whiteboard.`, `code.`, `hub.`) resolve to dedicated stateful compute instances (e.g., `cytohost`) orchestrated by our internal Container Framework.

### Dual-Zone Topology

To maintain 100% backwards compatibility during the registrar migrations, we maintain a dual-zone mapping structure within Cloud DNS (`cytognosis-infrastructure`):

- `cg-org` (Active Canonical Zone) vs `org-zone` (Legacy Fallback Zone)
- `cg-com` (Active Canonical Zone) vs `com-zone` (Legacy Fallback Zone)
- `cg-ai` (Active Canonical Zone) vs `ai-zone` (Legacy Fallback Zone)

### Canonical A & CNAME Records

```text
# Cloud Run Apex Mapping (Serverless)
@    A      300    216.239.32.21, 216.239.34.21, 216.239.36.21, 216.239.38.21

# Cloud Run Subdomain Mapping (Managed SSL)
www  CNAME  300    ghs.googlehosted.com.

# Internal Core Services Mapping (Stateful VM)
cal     A      300    136.111.39.188
code    A      300    136.111.39.188
hub     A      300    136.111.39.188
```

### Authentication & Third-Party Validations

Universal TXT matrices injected across all three TLDs:

```text
TXT  v=spf1 include:_spf.google.com ~all
TXT  v=DMARC1; p=none; rua=mailto:dmarc@cytognosis.org; pct=100; fo=1
TXT  google._domainkey (DKIM core key)
TXT  anthropic-domain-verification-1fpkv3=MMafCt8EWGm7KbVHRWaA2Wb20 (Claude AI Verification)
```

### MX Routing (Google Workspace)

```text
1  aspmx.l.google.com
5  alt1.aspmx.l.google.com
5  alt2.aspmx.l.google.com
10 alt3.aspmx.l.google.com
10 alt4.aspmx.l.google.com
```

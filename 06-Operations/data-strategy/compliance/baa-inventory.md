# SOP: BAA Inventory & Vendor HIPAA Compliance

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: operators
> **Tags**: `operations`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)
**Control**: HIPAA 164.308(b)(1) — Business Associate Contracts
**Effective**: 2026-05-19 | **Owner**: Privacy Officer | **Review**: Annual + before new vendor

## Signed BAAs

| Vendor | Scope | BAA type | Signed | Signed by | Notes |
|---|---|---|---|---|---|
| **Google Cloud / Workspace** | All HIPAA-eligible GCP services + Workspace | Google Workspace HIPAA BAA | 2025-09-01 | mohammadi@cytognosis.org | Covers Cloud Run, GCS, Cloud SQL, BigQuery, Artifact Registry, Secret Manager. Does NOT cover all AI APIs — check before using. |
| **Google Cloud CDPA** | EU data processing | Cloud Data Processing Addendum | 2025-09-01 | mohammadi@cytognosis.org | EU GDPR compliance |
| **EU Data Protection** | EU subjects | EU DPL certification | 2025-09-01 | mohammadi@cytognosis.org | Certified via Admin console |

**Where to verify**: `admin.google.com → Account → Account settings → Legal & Compliance → Security and Privacy Additional Terms`

## Vendors WITHOUT BAAs (PHI must NOT flow to these)

| Vendor | Used for | PHI risk | Mitigation |
|---|---|---|---|
| **GitHub** | Source code, CI/CD | None — no PHI in repos | Secret scanning enabled; verify no PHI in code/configs |
| **Zotero** | Reference management | None | Metadata only; PDFs on Drive |
| **Anthropic** | Internal Claude usage | None currently | Do not send PHI to Claude; use only de-identified examples |
| **Monday.com** | Project management | None | No PHI data entered; task tracking only |
| **Cal.com** (self-hosted) | Scheduling | Low | Self-hosted instance; no PHI in scheduling fields |

## Process for Adding a New Vendor

1. **Check**: Does this vendor ever process, store, or transmit PHI?
2. **If yes**: Obtain signed BAA BEFORE any PHI data flows. Do not rely on vendor's "HIPAA-ready" marketing — require a signed legal document.
3. **If no**: Document why not (what data does flow, what mitigations exist).
4. **Update this file** before vendor goes live.

## GCP Covered Services (Key Subset)
The Google Cloud BAA covers ≈120 services. Key ones for Cytognosis:
- ✅ Cloud Run, Cloud Build, Cloud Storage, Cloud SQL
- ✅ BigQuery, Artifact Registry, Secret Manager
- ✅ Cloud Logging, Cloud Monitoring, Cloud KMS
- ✅ Identity-Aware Proxy, VPC Service Controls
- ⚠️ Vertex AI (covered for some features; verify per use case)
- ❌ Some generative AI APIs — check https://cloud.google.com/security/compliance/hipaa before using

## Annual Review Checklist
- [ ] All vendors with PHI access have current signed BAAs
- [ ] No new vendors added without BAA assessment
- [ ] GCP covered services list reviewed against new services adopted
- [ ] BAA signing authority (mohammadi@cytognosis.org) still current

# HIPAA Compliance Overview

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: operators
> **Tags**: `operations`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)

> ADHD-friendly quick reference. For full details, see the [compliance docs](../../data-strategy/compliance/).

## Current Status: Pre-Operational

Cytognosis has **not yet ingested any PHI**. All current datasets are either public (T1) or licensed academic (T3). The HIPAA infrastructure exists but is not yet active.

## GCP Security Architecture

```mermaid
graph TD
    subgraph "cytognosis-infrastructure"
        Hub["Data Hub<br/><i>gs://cytognosis-data-hub</i>"]
        Internal["Internal Ops<br/><i>gs://cytognosis-internal</i>"]
        Public["Public Data<br/><i>gs://cytognosis-public-data</i>"]
    end
    
    subgraph "cytognosis-phi-prod"
        PHI["PHI Core<br/><i>gs://cytognosis-phi-core</i><br/>CMEK encrypted"]
        Collab["PHI Collab<br/><i>gs://cytognosis-phi-collab</i><br/>CMEK encrypted"]
    end
    
    style PHI fill:#ff4444,color:#fff
    style Collab fill:#ff8800,color:#fff
    style Hub fill:#44aa44,color:#fff
```

## What's Implemented vs Planned

| Control | Status | Notes |
|---------|--------|-------|
| Project isolation (PHI vs non-PHI) | ✅ Done | `cytognosis-phi-prod` separate project |
| CMEK encryption at rest | ✅ Done | `phi-keyring/phi-bucket-key` deployed on PHI buckets (verified 2026-06-19) |
| Uniform bucket access | ✅ Done | Enabled on all buckets |
| Bucket versioning | ✅ Done | Enabled on data-hub, phi-core, phi-collab |
| VPC Service Controls | ⏳ Planned | Not yet configured |
| Audit logging | ✅ Done | Data access logs enabled |
| De-identification pipeline | 📋 Planned | DLP API + Healthcare API |
| BAA with Google | 📋 Needed | Required before PHI ingestion |
| NIST 800-171 self-assessment | 📋 Needed | Required for DUC submissions |

## When Do We Need Full HIPAA?

Before ingesting **any** T4 (Restricted/PHI) data:
1. Complete NIST 800-171 self-assessment
2. Sign BAA with Google Cloud
3. Enable VPC Service Controls on phi-prod
4. Verify CMEK on all PHI buckets
5. Enable audit logging for all data access
6. Deploy de-identification pipeline
7. Train all personnel with PHI access

## Related Docs

- [Data Governance Policy](../../data-strategy/policies/data-governance-policy.md)
- [HIPAA Status](../../data-strategy/compliance/HIPAA-STATUS.md)
- [Technical Infrastructure](../../../04-Engineering/infrastructure/data-strategy/TECHNICAL_DATA_INFRASTRUCTURE.md) (Infrastructure layer)

# SOP: Audit Log Retention (7 Years)
**Control**: HIPAA 164.312(b) — Audit Controls; 164.316(b)(2)(i) — Retention
**Effective**: 2026-05-19 | **Owner**: Privacy Officer | **Review**: Annual

## Current Configuration

| Component | Value |
|---|---|
| Audit bucket | `gs://cytognosis-audit-7yr` (us-central1) |
| Retention policy | 7 years (2,557 days) |
| Retention lock | **✅ LOCKED 2026-05-22** — irrevocable, HIPAA-compliant |
| Log sink (infra) | `cytognosis-audit-7yr-sink` in `cytognosis-infrastructure` |
| Log sink (phi-prod) | `cytognosis-audit-7yr-sink` in `cytognosis-phi-prod` |
| Logging SAs granted | `service-517562623935@gcp-sa-logging.iam.gserviceaccount.com` + phi-prod equivalent |

> **Compliance note**: The retention lock was applied 2026-05-22 (4 days after the policy
> was created, after confirming log flow). The lock is irrevocable — GCP will not allow
> objects to be deleted or the retention period to be shortened under any circumstances.
> This satisfies HIPAA 164.316(b)(2)(i) and HHS audit log guidance.

## Verifying Lock Status

```bash
gcloud storage buckets describe gs://cytognosis-audit-7yr \
  --project=cytognosis-infrastructure \
  --format="yaml(retentionPolicy)"
# Should show: isLocked: true
```



## What Gets Logged

**From `cytognosis-infrastructure`**: Admin activity, IAM changes, compute events, storage access, DNS changes, GitHub Actions runner activity.

**From `cytognosis-phi-prod`**: Cloud Run deployments, Secret Manager access, Artifact Registry pushes, all data access to phi-prod resources.

**Log filter applied**:
```
severity>=NOTICE OR logName=~"cloudaudit" OR logName=~"data_access"
```

## Adding cytognosis-data Project (when provisioned)

```bash
gcloud logging sinks create cytognosis-audit-7yr-sink \
  storage.googleapis.com/cytognosis-audit-7yr \
  --project=cytognosis-data \
  --log-filter='severity>=NOTICE OR logName=~"cloudaudit"'

# Grant logging SA write access
gcloud storage buckets add-iam-policy-binding gs://cytognosis-audit-7yr \
  --member="serviceAccount:service-<DATA_PROJECT_NUM>@gcp-sa-logging.iam.gserviceaccount.com" \
  --role="roles/storage.objectCreator"
```

## Monitoring & Alerting

Set up Cloud Monitoring alerts for anomalous activity (do when SCC is enabled):
- IAM policy changes on any phi-prod resource
- Access from unexpected geographies
- Audit bucket writes from unexpected SAs
- Volume spikes (>2× daily baseline reads on phi-core)

## Review Cadence
- **Weekly**: automated digest (once Monitoring alerts are wired)
- **Quarterly**: manual sampling — Privacy Officer reviews 10 random audit entries
- **Annually**: comprehensive review for compliance attestation; update this SOP

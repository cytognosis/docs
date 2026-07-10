# SOP: Contingency Plan (Disaster Recovery)

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: operators
> **Tags**: `operations`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)
**Control**: HIPAA 164.308(a)(7) — Contingency Plan
**Effective**: 2026-05-19 | **Owner**: Engineering + Privacy Officer | **Review**: Annual + after DR test

## Recovery Objectives

| System | RTO (Recovery Time) | RPO (Recovery Point) | Priority |
|---|---|---|---|
| cytognosis.org website (Cloud Run) | 15 min | 0 (stateless) | P1 |
| Self-hosted services (cal, whiteboard, mlflow, etc.) | 2 hours | 24 hours | P2 |
| GCS data buckets | N/A (GCS is 11-nine durable) | Instant (object versioning) | — |
| Artifact Registry | 30 min | Last CI build | P2 |
| DNS (Cloud DNS) | 5 min | Near-instant (managed) | P1 |

## Backup Strategy

### Website + Stories API (Cloud Run)
- **State**: Stateless — redeploy from registry in <15 min
- **Database backup**: `website-db-url` secret points to Cloud SQL; enable automated backups

```bash
# Manual redeploy from last known-good image
gcloud run deploy cytognosis-website-v2 \
  --image=us-central1-docker.pkg.dev/cytognosis-phi-prod/cytognosis-website-v2/website:<LAST_GOOD_SHA> \
  --region=us-central1 --project=cytognosis-phi-prod
```

### cytohost (Self-Hosted Stack)
- **Backup**: Daily disk snapshot via `gcloud compute disks snapshot`
- **Container config**: Fully described in `container_framework/` — rebuild from scratch in ~30 min if snapshot unavailable
- **Data**: Cal.com PostgreSQL data on the disk; MLflow experiments in GCS

```bash
# Restore from latest snapshot
SNAPSHOT=$(gcloud compute snapshots list \
  --filter="sourceDisk=cytohost" \
  --sort-by="~creationTimestamp" \
  --format="value(name)" --limit=1)

gcloud compute disks create cytohost-restored \
  --source-snapshot=$SNAPSHOT \
  --zone=us-central1-b --project=cytognosis-infrastructure

gcloud compute instances create cytohost \
  --zone=us-central1-b --machine-type=t2a-standard-2 \
  --disk=name=cytohost-restored,boot=yes \
  --project=cytognosis-infrastructure
```

### GCS Buckets (Data)
GCS standard replication provides 11-nine durability. For additional protection:
- `cytognosis-phi-core`: Enable object versioning when CMEK is activated
- `cytognosis-data-hub`: Enable object versioning for pipeline outputs
- `cytognosis-audit-7yr`: Retention lock + immutability (do not version — logs are append-only)

```bash
# Enable versioning on key buckets
for bucket in cytognosis-phi-core cytognosis-data-hub; do
  gcloud storage buckets update gs://$bucket --versioning
done
```

### DNS
Cloud DNS is managed and globally replicated. TTLs are set to 300s (5 min) —
in a regional failure, updating A records to a new IP propagates within ~10 min.

## Disaster Scenarios

### Scenario A: cytohost node lost (hardware failure)
1. Create new `t2a-standard-2` in `us-central1-b` from latest disk snapshot (~15 min)
2. Update DNS A records to new IP (~5 min propagation)
3. Re-register GitHub Actions runner (~10 min)
**Total RTO**: ~30 min

### Scenario B: GCP project-level incident (project deletion/corruption)
1. Contact GCP Support immediately — deleted projects recoverable within 30 days
2. If unrecoverable: restore from GCS bucket exports (data tier) + container_framework config (services tier)
**Total RTO**: Hours to days depending on scope

### Scenario C: Artifact Registry unavailable
- Cloud Run services continue running (images are cached in Cloud Run)
- New deployments blocked until registry recovers
- Mitigation: Pin known-good image SHAs in deployment manifests

### Scenario D: Cloud DNS failure
- Switch to backup DNS provider (Cloudflare) using existing records export
```bash
# Export current DNS records
gcloud dns record-sets export dns-backup.yaml \
  --zone=cg-org --project=cytognosis-infrastructure
```

## Annual DR Test

Conduct annually in a non-production window:
1. Restore `cytohost` from snapshot to a test instance
2. Verify all 6 services start correctly
3. Simulate DNS failover to new IP
4. Test Cloud Run rollback to previous image
5. Document results in `compliance/dr-test-log.md`

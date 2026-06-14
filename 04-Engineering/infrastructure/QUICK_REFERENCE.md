> **Status**: Active
> **Date**: 2026-06-14
> **Author**: Cytognosis Engineering
> **Audience**: engineers, operators
> **Tags**: `quick-reference`, `infrastructure`, `gcp`, `cytohost`
> **Last verified**: 2026-06-14 against gcloud

# Cytognosis Infrastructure — Quick Reference

> **One line**: Current-state snapshot of every live GCP resource, cytohost service, and key CLI command as of 2026-06-14.
> **Full doc**: [MASTER_INFRASTRUCTURE.md](MASTER_INFRASTRUCTURE.md) | [DNS & GCP Architecture](DNS_AND_GCP_ARCHITECTURE.md) | [cytoinfra docs](cytoinfra/cytoinfra.md)

---

## GCP Projects

| Project ID | Number | Purpose |
|---|---|---|
| `cytognosis-infrastructure` | 517562623935 | DNS, IAM root, Artifact Registry, Compute Engine, GCS (general) |
| `cytognosis-phi-prod` | 143911445857 | Cloud Run (website + Stories API), PHI storage, HIPAA workloads |
| `cytognosis-data` | — | **Planned — does not exist** |

---

## Compute: cytohost

| Field | Value |
|---|---|
| **Instance name** | `cytohost` |
| **Machine type** | `e2-highmem-2` |
| **Architecture** | x86_64 |
| **Zone** | `us-central1-b` |
| **Current external IP** | `34.171.23.255` (static reservation `cytohost-static`, promoted 2026-06-14) |
| **Orphaned static IP** | `cytohost-ip` → `136.111.39.188` (RESERVED, not attached — releasable) |
| **Internal IP** | `10.128.0.6` |
| **Project** | `cytognosis-infrastructure` |
| **Uptime model** | 24/7 (no auto start/stop scheduler — Cloud Scheduler API disabled) |
| **Network tags** | `http-server`, `https-server`, `research-stack` |
| **Default compute SA** | **Disabled** (`517562623935-compute@developer.gserviceaccount.com`) |

> [!WARNING]
> The default compute SA on cytohost is disabled. Monitoring writes and storage reads will fail unless a functional SA is attached. Use OIDC / `website-deployer` SA for CI tasks.

---

## Self-Hosted Stack (cytohost — docker compose, 11 containers)

| Container | Public Subdomain | URL | Notes |
|---|---|---|---|
| `cyto-caddy` | (reverse proxy) | — | TLS termination for all services |
| `cyto-calcom` | `cal` | https://cal.cytognosis.org | Scheduling |
| `cyto-excalidraw` | `draw` | https://draw.cytognosis.org | Whiteboard; `cyto-excalidraw-room` sidecar |
| `cyto-gitea` | `code` | https://code.cytognosis.org | Internal Git forge |
| `cyto-mlflow` | `mlflow` | https://mlflow.cytognosis.org | ML experiment tracking |
| `cyto-neo4j` | `hub`, `kg` | https://hub.cytognosis.org | Knowledge graph |
| `cyto-postgres` | — | internal | Shared PostgreSQL (Wiki.js, other services) |
| `cyto-prefect` | `prefect` | https://prefect.cytognosis.org | Workflow orchestration |
| `cyto-wiki` | `notes` | https://notes.cytognosis.org | Wiki.js collaborative docs |
| `cyto-zoekt` | `search` | https://search.cytognosis.org | Code search |

All subdomains above are A records in zone `cg-org` pointing to `34.171.23.255` (cytohost static IP).

---

## Cloud Run Services (cytognosis-phi-prod, us-central1)

| Service | Last Deployed | Status |
|---|---|---|
| `cytognosis-website-v2` | 2026-06-09 | Active |
| `stories-api` | 2025-12-09 | **Potentially stale — verify if still needed** |

Deployed by GitHub Actions OIDC via `website-deployer` SA. Cloud Run API is **disabled** in `cytognosis-infrastructure`.

---

## GCS Buckets

### cytognosis-infrastructure (16 buckets, all us-central1)

| Bucket | Versioning | Retention Lock | Notes |
|---|---|---|---|
| `cytoagent` | No | No | |
| `cytoexplorer` | No | No | |
| `cytognosis` | No | No | Oldest (2026-02-22) |
| `cytognosis-audit-7yr` | No | **7yr locked** | Immutable audit log |
| `cytognosis-data-hub` | Yes | No | Lifecycle: Standard→Nearline@60d→Coldline@180d |
| `cytognosis-internal` | No | No | |
| `cytognosis-mlflow-artifacts` | — | — | **Created 2026-06-14** |
| `cytognosis-phi-prod` | Yes | **7yr locked** | labels: compliance=hipaa, data-class=phi |
| `cytognosis-public-data` | No | No | |
| `cytognosis-restricted-prod` | No | **1yr locked** | public_access_prevention: enforced |
| `cytomark` | No | No | |

Additional general-purpose buckets (no retention/versioning): `cytonome`, `cytopilot`, `cytoscope`, `cytoskeleton`, `cytoverse`, `neuroverse`.

### cytognosis-phi-prod (3 buckets, us-central1, CMEK)

| Bucket | Versioning | CMEK Key | Notes |
|---|---|---|---|
| `cytognosis-phi-collab-nih` | Yes | `phi-bucket-key` | PHI — NIH collaboration |
| `cytognosis-phi-core` | Yes | `phi-bucket-key` | PHI — core data |
| `cytognosis-phi-prod_cloudbuild` | No | None | Cloud Build staging (US multi-region) |

KMS keyring: `phi-keyring` in `cytognosis-phi-prod`.

---

## Artifact Registry (cytognosis-infrastructure, us-central1)

| Repository | Format | Notes |
|---|---|---|
| `cytognosis-compute` | Docker | Modular heavy compute images (empty) |
| `cytognosis-npm` | npm | Internal npm packages |
| `cytognosis-python` | Python | Internal PyPI |

---

## OIDC / Workload Identity

| Field | Value |
|---|---|
| Pool | `github-pool` (GitHub OIDC Pool) |
| Provider | `github-provider` |
| Project | `cytognosis-infrastructure` (517562623935) |
| Issuer | `https://token.actions.githubusercontent.com` |
| Attribute condition | `attribute.repository_owner=="cytognosis"` |
| State | ACTIVE |

Default compute SA is intentionally disabled; all CI/CD uses OIDC federation.

---

## CI Runner

| Field | Value |
|---|---|
| Runner name | `cytohost` |
| Labels | `self-hosted`, `linux`, `x64`, `cytohost` |
| Host | cytohost VM |
| Service | systemd |
| Status | Online |

---

## DNS Managed Zones

| Domain | Live Zone | Nameservers | Duplicate to Delete |
|---|---|---|---|
| `cytognosis.org` | `cg-org` | ns-cloud-d1-4 | `org-zone` |
| `cytognosis.com` | `com-zone` | ns-cloud-c1-4 | `cg-com` |
| `cytognosis.ai` | `ai-zone` | ns-cloud-e1-4 | `cg-ai` |

> [!NOTE]
> The task prompt specifies `.ai` live zone is `ai-zone` (ns-cloud-e). See [DNS_AND_GCP_ARCHITECTURE.md](DNS_AND_GCP_ARCHITECTURE.md) for the full dedup/remediation plan including pre-deletion checklist and pending email-protection tasks.

---

## Key Commands

```bash
# cytoinfra CLI — container management
cytoinfra container list                        # List registered container entries
cytoinfra container add <name> --image <img>    # Register a new container
cytoinfra container remove <name>               # Remove a registry entry
cytoinfra container build <name>                # Build container image
cytoinfra container push <name>                 # Push image to registry
cytoinfra container pull <name>                 # Pull image from registry

# cytoinfra CLI — service management
cytoinfra service deploy <name>                 # Deploy via local docker-compose
cytoinfra service deploy <name> --host user@host  # Deploy over SSH
cytoinfra service status                        # Show all running containers
cytoinfra service status <name>                 # Show single service status
cytoinfra service stop <name>                   # Stop a service

# cytoinfra CLI — wiki-js
cytoinfra wiki-js setup                         # Deploy Wiki.js to wiki.cytognosis.org
cytoinfra wiki-js sync-config                   # Generate git sync config for Wiki.js Admin

# cytoinfra CLI — compute (Cloud Batch + Prefect)
cytoinfra compute pools                         # List compute pools
cytoinfra compute init                          # Generate default pools config
cytoinfra run <cmd> [--pool <pool>]             # Submit job to Prefect + Cloud Batch
cytoinfra run python train.py --pool gpu-t4     # Example: GPU job

# cytoinfra CLI — Cloud Run (manual/emergency path)
cytoinfra cloud-run deploy <image>              # Deploy image to Cloud Run
cytoinfra cloud-run deploy <image> --dry-run    # Preview gcloud command only

# gcloud — VM management
gcloud compute instances describe cytohost --zone us-central1-b
gcloud compute instances start  cytohost --zone us-central1-b
gcloud compute instances stop   cytohost --zone us-central1-b

# GitHub Actions runner
sudo systemctl status actions.runner.*         # Runner service status
sudo systemctl restart actions.runner.*        # Restart runner
```

---

## Environment Variables (cytoinfra)

| Variable | Used By | Default | Purpose |
|---|---|---|---|
| `CYTOINFRA_COMPOSE_FILE` | `wiki-js setup`, `service deploy` | auto-resolved | Override path to docker-compose file |
| `WIKI_DB_PASSWORD` | `wiki-js setup` | (required) | PostgreSQL password for Wiki.js |
| `CYTOINFRA_CLOUD_RUN_PROJECT` | `cloud-run deploy` | `cytognosis-phi-prod` | GCP project for Cloud Run |
| `CYTOINFRA_CLOUD_RUN_REGION` | `cloud-run deploy` | `us-central1` | GCP region |
| `CYTOINFRA_CLOUD_RUN_SERVICE` | `cloud-run deploy` | `cytognosis-website-v2` | Cloud Run service name |

---

## See Also

- [MASTER_INFRASTRUCTURE.md](MASTER_INFRASTRUCTURE.md) — full infrastructure narrative
- [DNS_AND_GCP_ARCHITECTURE.md](DNS_AND_GCP_ARCHITECTURE.md) — DNS zones, dedup plan, remediation checklist
- [cytoinfra/cytoinfra.md](cytoinfra/cytoinfra.md) — cytoinfra package comprehensive doc
- [cytoinfra/cytoinfra-quickref.md](cytoinfra/cytoinfra-quickref.md) — cytoinfra CLI quick reference
- [compute/node-types.md](compute/node-types.md) — cytohost VM detail
- [HOSTING_AND_DEPLOYMENT.md](HOSTING_AND_DEPLOYMENT.md) — Cloud Run + CDN frontend

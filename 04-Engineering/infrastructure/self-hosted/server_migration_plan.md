# Server Migration & Optimization Plan

> **Status**: Historical planning document — superseded by the consolidated cytohost architecture.
> **Date**: 2026-06-14
> **Author**: @mohammadi
> **Audience**: engineers
> **Tags**: `compute`, `self-hosted`, `migration`

> [!IMPORTANT]
> **Outcome (2026-06-14)**: The `calcom-server` and `research-stack-server` instances described below have been consolidated into a single **`cytohost`** VM: `e2-highmem-2` (2 vCPU, 16 GB RAM), zone `us-central1-b`, running 24/7. All 11 self-hosted containers (core + research stacks) run on cytohost. None of the migration options below were selected — the e2-highmem-2 consolidation was the actual outcome. See [deployment_walkthrough.md](deployment_walkthrough.md) for the live state.

## Current State Analysis (Historical — pre-consolidation)

Previously, `cytognosis-infrastructure` had the following footprint:
- **`calcom-server`** (`e2-medium`): Running self-hosted services (Cal.com, Caddy, etc.).
- **`research-stack-server`** (`e2-standard-4`): Was running but shut down to save ~$100/mo.

## The Problem (Historical)
Running self-hosted core apps on an `e2-medium` cost around $300/year; the E2 family was inefficient for memory-intensive workloads. The `research-stack-server` was costing $100/mo but was idle most of the time.

## Recommended Target Architecture

### Option A: The "T2A ARM" Sweet Spot (Highly Recommended)
Google's `t2a` (Ampere Altra ARM) instances offer the best price-to-performance ratio for web services.
- **Instance**: `t2a-standard-1` (1 vCPU, 4GB RAM) OR `t2a-standard-2` (2 vCPU, 8GB RAM).
- **Cost**: A `t2a-standard-1` is ~$18/month (cheaper than `e2-medium`) but offers much more consistent single-core performance. A `t2a-standard-2` is ~$36/month and provides double the RAM for heavy Docker networking.
- **Why**: Cal.com, Postgres, and Caddy all have native ARM64 Docker images. You will get more stable performance for less money.

### Option B: The "E2 Small" Downgrade (Max Savings)
If traffic is extremely low and mostly internal.
- **Instance**: `e2-small` (2 shared vCPU, 2GB RAM).
- **Cost**: ~$12/month.
- **Why**: Maximum cost savings, but the 2GB of RAM is dangerously low for running Cal.com + Postgres + Excalidraw + MLFlow simultaneously. Container OOM (Out of Memory) crashes are highly likely.

### Option C: The Spot Instance Approach (For Occasional Runs)
For the GitHub Actions runner (heavy compiles), we should provision a **Spot Instance** (e.g., `e2-standard-8` Spot). Spot instances are 60-90% cheaper.
- We can spin it up dynamically via GitHub Actions API when a build starts, and tear it down right after. This means we only pay pennies per compile.

---

## Migration Steps (Future Task)

When we are ready to migrate `calcom-server` to a new instance (e.g., `t2a-standard-2`):

1. **Snapshot Existing Disk**:
   Create a snapshot of `calcom-server`'s boot disk to preserve the SQLite/Postgres databases and Docker volumes.
2. **Provision Target Instance**:
   Create the new `t2a` instance in `us-central1-a`. Give it a static external IP.
3. **Data Transfer**:
   Use `rsync` or direct disk mounting to move the `/var/lib/docker/volumes` and the `container_framework/` directory to the new host.
4. **Update DNS Records**:
   Update Google Cloud DNS A-records for the following domains to point to the *new* static IP:
   - `cal.cytognosis.org`
   - `whiteboard.cytognosis.org`
   - `mermaid.cytognosis.org`
   - `notes.cytognosis.org`
   - `mlflow.cytognosis.org`
5. **Start Services**:
   Run `docker-compose up -d` on the new host. Caddy will automatically re-provision the SSL certificates from Let's Encrypt upon seeing the new IP routing.
6. **Decommission Old Host**:
   Once DNS propagation is confirmed and services are verified, permanently delete `calcom-server`.

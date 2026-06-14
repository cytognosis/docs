# Hosting & Deployment Architecture

**Last Updated**: May 2026

## 1. The Cloud Run Evolution

**Status: ACTIVE**

Historically, the Cytognosis frontend was statically compiled and hosted on Google Cloud Storage buckets (e.g. `gs://cytognosis`).

**Why We Migrated**:

- Requirement for dynamic form handling, OAuth/OIDC login integrations, SQLite parsing, and HIPAA-ready data processing.
- Static buckets lack backend computational capabilities or advanced request interception.

**Current Deployment**:

- **Application**: The `cytognosis/website` repository executes entirely via a fully Serverless **Google Cloud Run** container footprint.
- **Region**: `us-central1`
- **Tech Stack**: Python 3.13, FastAPI, Uvicorn, SQLModel, Jinja2 Templates.

## 2. CI/CD Operations

Deployments are fully automated under the Cytognosis GitHub organization.

### Workload Identity Federation

Instead of provisioning long-lived, high-risk JSON service account keys, GitHub Actions authenticates to Google Cloud via short-lived OIDC tokens.

- **Provider**: GitHub Actions (`cytognosis/website`)
- **Service Account**: `website-deployer@cytognosis-infrastructure.iam.gserviceaccount.com`
- **Capabilities**: Artifact Registry Push, Cloud Run Deployments.

## 3. Artifact Registries & Container Matrix

| Registry Area | Purpose | Status |
|---------------|---------|--------|
| `cytognosis-website-v2` | Holds immutable builds of the main platform web server | Active |
| `cytognosis-compute` | Standardized Jupyter data science environments | Active |
| `neo4j` | Containerized graph mappings for Molecular Medical NLP | Active |
| `cal.com` | Internal HIPAA-managed appointment scheduling proxy | Active |

## 4. Developer Spin-Up Protocol

When validating architecture locally, developers bypass Docker compose for rapid frontend traversal:

```bash
# 1. Update packages
uv sync

# 2. Spin up the ASGI server on a custom port
uv run uvicorn main:app --port 8000 --reload
```

*Note: All local deployments simulate cloud data architectures natively via SQLite (`database.db`), guaranteeing schema 1:1 mirroring prior to Cloud SQL production synchronizations.*

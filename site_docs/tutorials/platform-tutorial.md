# Cytognosis Platform — Integrated Hands-On Tutorial

> A complete, worked guide to the Cytognosis toolchain: managing assets,
> environments, datasets, containers, services, and skills across all packages.

---

## Architecture Overview

```mermaid
graph TD
    subgraph "Global Store (~/.cytognosis/)"
        GI[index.yaml]
        GA[assets/]
        GA --> SK[skills/]
        GA --> CO[components/]
    end

    subgraph "Package Ecosystem"
        CS[cytoskeleton<br/>Core asset framework]
        CI[cytoinfra<br/>Containers & services]
        CY[cytos<br/>Schemas, datasets, ontologies]
        CC[cytocast<br/>Package scaffolding]
        BR[branding<br/>Design assets]
        CSK[cytoskills<br/>Agent skills]
    end

    CS --> GI
    CI -->|depends on| CS
    CY -->|depends on| CS
    CC -->|depends on| CS
    BR -->|depends on| CS
    CSK -->|depends on| CS

    subgraph "Agent Symlinks"
        AG[~/.agents/skills/]
        GM[~/.gemini/antigravity/skills/]
        CL[~/.claude/skills/]
        KI[~/.kiro/skills/]
    end

    SK --> AG
    AG --> GM
    AG --> CL
    AG --> KI

    subgraph "Cytohost (GCP VM)"
        CH[34.171.23.255<br/>cytohost-static via IAP]
        N4[neo4j:5-community]
        FK[falkordb:latest]
        WK[wiki.js + postgres]
        CD[caddy reverse proxy + TLS]
    end

    CI -->|SSH deploy| CH
```

---

## 1. Asset Management Fundamentals (cytoskeleton)

### How It Works

Cytoskeleton manages assets in two scopes:

| Scope | Location | Visible To |
|-------|----------|------------|
| **Global** | `~/.cytognosis/assets/` | All workspaces on this machine |
| **Local** | `./assets/` (per-workspace) | Current workspace only |
| **Remote** | Repo manifests / GCS | Available for pull |

### Full ID Format

Every asset has a canonical identifier:

```
<managing_package>/<asset_type>/<name>@<version>
```

Examples:
- `cytoskills/skills/cytognosis-doc@3.0.0`
- `cytoinfra/containers/neo4j@5.18.1`
- `cytos/datasets/allen-adult-brain-atlas@2024.1`
- `branding/branding/cytognosis-design-system-v10@10.0.0`

After the first pull, use the short name: `cytognosis-doc`, `neo4j`, etc.

### List Assets

```bash
# List globally installed assets
cytoskeleton store list
```

```text
  [G] cytognosis-branding (3.0.0) — cytoskills/skills/cytognosis-branding@3.0.0
  [G] cytognosis-dev (3.0.0)      — cytoskills/skills/cytognosis-dev@3.0.0
  [G] cytognosis-doc (3.0.0)      — cytoskills/skills/cytognosis-doc@3.0.0
  [G] cytognosis-orchestrator (3.0.0) — cytoskills/skills/cytognosis-orchestrator@3.0.0
  [G] cytognosis-org (3.0.0)      — cytoskills/skills/cytognosis-org@3.0.0
  [G] cytognosis-writer (3.0.0)   — cytoskills/skills/cytognosis-writer@3.0.0
  [G] cytognosis-design-system-master (3.0.0) — cytoskills/skills/cytognosis-design-system-master@3.0.0
  [G] cytognosis-template-master (3.0.0) — cytoskills/skills/cytognosis-template-master@3.0.0
```

```bash
# List remotely available assets (from repo manifests)
cytoskeleton store list --remote
```

```text
  [R] neo4j (5-community)           — cytoinfra/containers/neo4j@5-community
  [R] falkordb (latest)              — cytoinfra/containers/falkordb@latest
  [R] mlflow (2.21.0)              — cytoinfra/containers/mlflow@2.21.0
  [R] caddy (2-alpine)             — cytoinfra/containers/caddy@2-alpine
  [R] hedgedoc (latest)            — cytoinfra/containers/hedgedoc@latest
  [R] grobid (0.8.1)               — cytoinfra/containers/grobid@0.8.1
  [R] cytognosis-compute (0.6.0)   — cytoinfra/containers/cytognosis-compute@0.6.0
  [R] cytognosis-gpu (0.6.0)       — cytoinfra/containers/cytognosis-gpu@0.6.0
  [R] cytos-core (2026.5.0)        — cytos/schemas/cytos-core@2026.5.0
  [R] allen-adult-brain-atlas (2024.1) — cytos/datasets/allen-adult-brain-atlas@2024.1
  [R] transdiagnostic-connectome (1.1.3) — cytos/datasets/transdiagnostic-connectome@1.1.3
  [R] cell-ontology (2024-05-15)   — cytos/ontologies/cell-ontology@2024-05-15
  ... (26 total remote assets)
```

```bash
# List only local assets (in current workspace)
cytoskeleton store list --local

# Filter by type
cytoskeleton store list --type skills

# Search by name
cytoskeleton store search neo4j
```

### Pull an Asset

```bash
# Pull a schema to global store
cytoskeleton store pull cytos/schemas/cytos-core@2026.5.0

# Pull to local workspace only
cytoskeleton store pull cytos/schemas/cytos-core@2026.5.0 --local
```

### Merge Local to Global

```bash
# After local modifications, promote to global
cytoskeleton store merge cytos-core
```

> [!TIP]
> Merging compares SWHIDs to detect conflicts. If the global version
> has changed, you'll be warned before overwriting.

### Switch Scope

```bash
# Switch an asset from global to local (creates a local copy)
cytoskeleton store switch cytos-core --local

# Switch back to global reference
cytoskeleton store switch cytos-core --global
```

---

## 2. Environment Management (cytoskeleton env)

### Creating a Virtual Environment

```python
from cytoskeleton.env_sync.venv_sync import VenvSyncer

syncer = VenvSyncer(
    env_path=Path(".venv"),
    python_version="3.13",
)
syncer.create()             # Uses uv if available, falls back to stdlib
syncer.sync_from_lockfile(  # Installs from lockfile
    Path("uv.lock"),
)
```

### CLI Usage

```bash
# Sync environment from lockfile (auto-detects venv vs conda)
cytoskeleton env sync pytorch-env --backend venv

# Create a global conda environment
cytoskeleton env sync pytorch-env --backend mamba --global
```

### Example: Set Up a PyTorch Research Environment

```bash
# Create project venv with uv
cd ~/repos/cytognosis/my-experiment
cytoskeleton env sync experiment-env --backend venv

# This auto-detects uv, creates .venv, and installs from uv.lock:
```

```text
✓ Created venv with uv: .venv
✓ Synced from uv.lock: 47 packages installed
✓ Environment ready: source .venv/bin/activate
```

### Creating Conda Environments

```python
from cytoskeleton.env_sync.conda_sync import CondaSyncer

syncer = CondaSyncer(
    env_name="single-cell-analysis",
    backend="auto",  # tries micromamba → mamba → conda
    python_version="3.12",
)
syncer.create()
syncer.install_packages([
    "scanpy>=1.10",
    "anndata>=0.10",
    "pytorch>=2.0",
])
```

> [!NOTE]
> The `backend="auto"` setting prefers micromamba (fastest), then mamba,
> then conda. This matches our default toolchain.

---

## 3. Working with Datasets (cytos)

### The ScientificDataset Schema

Datasets in cytos follow the `ScientificDataset` class from our scholarly KG schema:

```yaml
# From cytos/schemas/domains/scholarly.yaml
ScientificDataset:
  class_uri: schema:Dataset
  is_a: ScholarlyResource     # inherits DOI, authors, keywords, license, etc.
  attributes:
    measurement_technique: []  # e.g., "scRNA-seq", "ATAC-seq"
    variable_measured: []
    species: []                # e.g., "Homo sapiens"
    health_condition: []       # e.g., "Alzheimer disease"
    data_standard: ""          # e.g., "CellxGene", "BIDS"
    distribution: []           # download links (DataDownload objects)
    sample_size: 0
    zenodo_doi: ""
    huggingface_id: ""
    internal_data_lake_path: ""
    conforms_to: []
    is_accessible_for_free: true
```

> [!IMPORTANT]
> Datasets are stored **as-is** from the source (paper, database, repository).
> They are NOT type-assigned or normalized by default. Each dataset is an
> opaque object associated with source metadata (publication DOI, measurement
> technique, species, etc.) using the `ScientificDataset` schema.

### Dataset Manifest Entry

```yaml
# In cytos/assets/datasets/manifest.yaml
entries:
  - name: geo-GSE123456-scrna
    version: "2024.1"
    source_url: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE123456
    format: h5ad
    modality: transcriptomics
    organism: Homo sapiens
    tissue: brain
    cell_count: 50000
    license: CC0-1.0
    citation: "Smith et al., Nature 2024"
    description: >-
      Single-cell RNA-seq of human prefrontal cortex, 50k cells,
      12 donors, annotated cell types.
    tags:
      - single-cell
      - brain
      - prefrontal-cortex
    provenance:
      doi: "10.1038/s41586-024-12345-6"
      geo_accession: GSE123456
      download_date: "2024-06-15"
      downloaded_by: "cytos-ingest-pipeline"
```

### Python API: Register a New Dataset

```python
from pathlib import Path
from cytos.assets.dataset_registry import DatasetAsset, DatasetRegistry

# Load the registry
reg = DatasetRegistry(
    Path("~/repos/cytognosis/cytos/assets/datasets/manifest.yaml").expanduser()
)
reg.load()

# Register a new dataset downloaded from GEO
dataset = DatasetAsset(
    name="geo-GSE234567-multiome",
    version="2025.1",
    source_url="https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE234567",
    format="h5ad",
    modality="multi-omics",
    organism="Homo sapiens",
    tissue="blood",
    cell_count=120000,
    license="CC-BY-4.0",
    citation="Johnson et al., Cell 2025",
    description="Multiome (RNA+ATAC) of human PBMCs, 120k cells, healthy donors.",
    tags=["multiome", "PBMC", "ATAC-seq", "scRNA-seq"],
    provenance={
        "doi": "10.1016/j.cell.2025.01.042",
        "geo_accession": "GSE234567",
        "download_date": "2025-05-28",
    },
)
reg.add(dataset)
reg.save()

print(f"Registered: {dataset.name} ({dataset.cell_count} cells)")
```

```text
Registered: geo-GSE234567-multiome (120000 cells)
```

### Query Datasets

```python
# Search by keyword
results = reg.search("brain")
for ds in results:
    print(f"  {ds.name}: {ds.modality} ({ds.organism})")

# Filter by modality
transcriptomics = reg.list_by_modality("transcriptomics")
print(f"Transcriptomics datasets: {len(transcriptomics)}")

# Get a specific dataset
atlas = reg.get("allen-adult-brain-atlas")
if atlas:
    print(f"Atlas: {atlas.source_url}")
```

---

## 4. Container Management (cytoinfra)

### Container Manifest Structure

```yaml
# infrastructure/assets/containers/manifest.yaml
manifest_version: "1.0.0"
managing_package: cytoinfra
asset_type: containers
remote_bucket: gs://cytognosis-data-hub/assets/containers/

containers:
  - name: neo4j
    version: "5.18.1"
    image: neo4j:5.18.1-community
    source: docker-hub
    registry_url: https://hub.docker.com/_/neo4j
    ports:
      http: 7474
      bolt: 7687
    volumes:
      data: /data
    environment:
      NEO4J_AUTH: "neo4j/cytognosis2026"
    min_ram: "2 GB"
    description: "Neo4j graph database for knowledge graph storage"
    tags: [kg, graph-database, production]

  - name: cytognosis-compute
    version: "0.6.0"
    image: us-central1-docker.pkg.dev/cytognosis-infrastructure/cytognosis-compute/compute:0.6.0
    source: internal
    min_ram: "4 GB"
    description: "Cytognosis base compute image (Python 3.13 + scientific stack)"
    tags: [compute, internal, base-image]
```

### CLI: Container Operations

```bash
# List all registered containers
cytoinfra container list
```

```text
  neo4j              5.18.1     docker-hub  Neo4j graph database
  surrealdb          v2         docker-hub  SurrealDB multi-model database
  mlflow             2.21.0     docker-hub  MLflow experiment tracker
  caddy              2-alpine   docker-hub  Caddy reverse proxy
  hedgedoc           latest     quay        HedgeDoc collaborative editor
  grobid             0.8.1      docker-hub  GROBID PDF extraction
  cytognosis-compute 0.6.0      internal    Base compute image
  cytognosis-gpu     0.6.0      internal    GPU compute image
```

```bash
# Get details for a specific container
cytoinfra container info neo4j
```

```text
  Name:        neo4j
  Version:     5.18.1
  Image:       neo4j:5.18.1-community
  Source:      docker-hub
  Ports:       http=7474, bolt=7687
  RAM:         2 GB
  Tags:        kg, graph-database, production
```

### Start a Container Locally

```bash
# Pull and start neo4j
cytoinfra container pull neo4j
cytoinfra container start neo4j
```

```text
  Pulling neo4j:5.18.1-community...
  ✓ Image pulled successfully
  Starting neo4j with ports 7474:7474, 7687:7687...
  ✓ Container 'cytos-neo4j' started
  → Browser: http://localhost:7474
  → Bolt:    bolt://localhost:7687
```

### Python API: Container Registry

```python
from pathlib import Path
from cytoinfra.containers.registry import ContainerEntry, ContainerRegistry

# Load registry
reg = ContainerRegistry(
    Path("~/repos/cytognosis/infrastructure/assets/containers/manifest.yaml").expanduser()
)
reg.load()

# Add a custom container
entry = ContainerEntry(
    name="jupyter-lab",
    version="4.2.0",
    image="quay.io/jupyter/scipy-notebook:2024-06-01",
    source="quay",
    ports={"http": 8888},
    environment={"JUPYTER_TOKEN": "cytognosis"},
    min_ram="2 GB",
    description="JupyterLab with scipy stack for analysis",
    tags=["notebook", "analysis"],
)
reg.add(entry)
reg.save()
```

### Build and Push to Internal Registry

```bash
# Build from Dockerfile
cytoinfra container build cytognosis-compute \
    --dockerfile infrastructure/container_framework/Dockerfile.compute

# Push to GCP Artifact Registry
cytoinfra container push cytognosis-compute
```

```text
  Building cytognosis-compute:0.6.0...
  ✓ Built in 4m 23s
  Pushing to us-central1-docker.pkg.dev/cytognosis-infrastructure/cytognosis-compute/compute:0.6.0...
  ✓ Pushed successfully
```

---

## 5. Service Deployment — Local & Remote (cytoinfra)

### Cytohost Connection

Cytohost is our GCP VM, accessed via IAP tunnel:

```bash
# SSH to cytohost
gcloud compute start-iap-tunnel cytohost 22 \
    --listen-on-stdin \
    --project=cytognosis-infrastructure \
    --zone=us-central1-b
```

Or via SSH config (already configured):

```bash
ssh cytohost  # Uses IAP tunnel (34.171.23.255)
```

### Deploy a Service Locally

```python
from pathlib import Path
from cytoinfra.services.deploy import deploy_local, get_status

# Deploy neo4j locally
result = deploy_local(
    service_name="neo4j",
    compose_file=Path("infrastructure/container_framework/docker-compose.yaml"),
)

# Check status
status = get_status("cytos-neo4j")
print(f"Running: {status.running}, Uptime: {status.uptime}")
```

### Deploy to Cytohost (Remote)

```python
from cytoinfra.services.deploy import deploy_remote

# Deploy to cytohost via SSH
deploy_remote(
    service_name="neo4j",
    host="mohammadi@34.171.23.255",
    compose_file=Path("infrastructure/container_framework/docker-compose.yaml"),
    remote_dir="/opt/cytognosis",
)
```

### CLI: Service Management

```bash
# Deploy a service locally
cytoinfra service deploy neo4j

# Deploy to cytohost
cytoinfra service deploy neo4j --remote mohammadi@34.171.23.255

# Check service status
cytoinfra service status neo4j
```

```text
  Service: cytos-neo4j
  Status:  Running (Up 3 hours)
  Image:   neo4j:5.18.1-community
  Ports:   7474→7474, 7687→7687
```

```bash
# Stop a service
cytoinfra service stop neo4j

# View logs
cytoinfra service logs neo4j --tail 50
```

### Start/Stop Services on Cytohost

```bash
# SSH into cytohost and manage services
ssh cytohost 'docker ps --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"'
```

```text
NAMES              STATUS         PORTS
cytos-neo4j        Up 3 hours     0.0.0.0:7474->7474/tcp, 0.0.0.0:7687->7687/tcp
cytos-falkordb     Up 3 hours     0.0.0.0:6379->6379/tcp
caddy              Up 5 days      0.0.0.0:80->80/tcp, 0.0.0.0:443->443/tcp
```

```bash
# Stop a specific service
ssh cytohost 'cd /opt/cytognosis && docker compose stop neo4j'

# Start it again
ssh cytohost 'cd /opt/cytognosis && docker compose start neo4j'

# Restart with fresh config
ssh cytohost 'cd /opt/cytognosis && docker compose up -d neo4j'
```

---

## 6. HedgeDoc Collaborative Editor

### What It Is

HedgeDoc is our self-hosted collaborative markdown editor, similar to HackMD.
We use it for real-time meeting notes, design documents, and shared drafts.

### Service Configuration

```yaml
# infrastructure/container_framework/configs/services/hedgedoc.yaml
name: hedgedoc
image: quay.io/hedgedoc/hedgedoc:latest
ports:
  - "3005:3000"
min_ram: 512 MB
auxiliary_services:
  hedgedoc-db:
    image: postgres:17-alpine
    environment:
      POSTGRES_USER: hedgedoc
      POSTGRES_PASSWORD: "${HEDGEDOC_DB_PASSWORD:-cytognosis2026}"
      POSTGRES_DB: hedgedoc
    volumes:
      - hedgedoc-db-data:/var/lib/postgresql/data
environment:
  CMD_DB_URL: "postgres://hedgedoc:${HEDGEDOC_DB_PASSWORD}@hedgedoc-db:5432/hedgedoc"
  CMD_DOMAIN: "docs.cytognosis.org"
  CMD_PROTOCOL_USESSL: "true"
  CMD_ALLOW_ANONYMOUS: "false"
```

### Caddy Reverse Proxy

HedgeDoc is accessible via Caddy's automatic HTTPS:

```text
# From the Caddyfile (excerpt)
docs.cytognosis.org {
    reverse_proxy hedgedoc:3000
}
```

### Access HedgeDoc

| Item | Value |
|------|-------|
| **URL** | `https://docs.cytognosis.org` |
| **Internal port** | 3005 (mapped from container's 3000) |
| **Database** | PostgreSQL 17 (hedgedoc-db container) |
| **Auth** | Anonymous access disabled; login required |

### Deploy HedgeDoc

```bash
# Deploy using the cytoinfra CLI
cytoinfra hedgedoc deploy

# Or deploy to cytohost
cytoinfra hedgedoc deploy --remote mohammadi@34.171.23.255
```

```text
  Deploying HedgeDoc stack...
  ✓ hedgedoc-db (postgres:17-alpine) started
  ✓ hedgedoc (quay.io/hedgedoc/hedgedoc:latest) started
  → Access at: https://docs.cytognosis.org
```

### Verify It's Running

```bash
# Check status
cytoinfra service status hedgedoc

# Or directly on cytohost
ssh cytohost 'docker ps | grep hedgedoc'
```

```text
hedgedoc       quay.io/hedgedoc/hedgedoc:latest  Up 2 hours  0.0.0.0:3005->3000/tcp
hedgedoc-db    postgres:17-alpine                Up 2 hours  5432/tcp
```

---

## 7. Package Scaffolding (cytocast)

### Creating a New Project

Cytocast uses Copier templates to scaffold new projects:

```bash
# Create a new ML project
copier copy gh:cytognosis/cytocast ./my-ml-project \
    --data project_name=my-ml-project \
    --data profile=ml \
    --data compute_backend=cuda

# Or use the cytocast CLI shortcut
cytocast create my-ml-project --profile ml
```

### Available Profiles

| Profile | Description | Includes |
|---------|-------------|----------|
| `ml` | Machine learning project | PyTorch, wandb, hydra |
| `data-science` | Data analysis | Polars, seaborn, jupyter |
| `single-cell` | Single-cell analysis | Scanpy, anndata, scvi |
| `api` | FastAPI service | FastAPI, pydantic, uvicorn |
| `library` | Python library | Ruff, mypy, pytest, docs |

### Auto-Manifest Push

When a project is created, a hook automatically registers it as an asset:

```python
# cytocast/scripts/hooks/push_manifest.py (runs automatically)
from cytocast.package_manifest import PackageManifest

manifest = PackageManifest(
    name="my-ml-project",
    version="0.1.0",
    profile="ml",
    template_version="0.6.0",
    github_url="https://github.com/cytognosis/my-ml-project",
    registry_url="https://pypi.org/project/my-ml-project/",
    docs_url="https://my-ml-project.readthedocs.io",
    compute_backend="cuda",
    python_version="3.13",
)
```

### Package Manifest Fields

```yaml
# Generated package manifest
name: my-ml-project
version: "0.1.0"
profile: ml
template_version: "0.6.0"
github_url: https://github.com/cytognosis/my-ml-project
registry_url: https://pypi.org/project/my-ml-project/
docs_url: https://my-ml-project.readthedocs.io
compute_backend: cuda
python_version: "3.13"
created_at: "2025-05-28T19:00:00+00:00"
dependencies:
  - torch>=2.4
  - wandb>=0.17
  - hydra-core>=1.3
```

---

## 8. Skills as Global Assets

### The Symlink Chain

Skills are deployed as global assets and symlinked to all agent directories:

```mermaid
graph LR
    STORE["~/.cytognosis/assets/skills/<br/>cytognosis-doc/"] --> AGENTS["~/.agents/skills/<br/>cytognosis-doc"]
    AGENTS --> GEMINI["~/.gemini/antigravity/<br/>skills/cytognosis-doc"]
    AGENTS --> CLAUDE["~/.claude/skills/<br/>cytognosis-doc"]
    AGENTS --> KIRO["~/.kiro/skills/<br/>cytognosis-doc"]
```

### Currently Deployed Skills (8 total)

| Skill | Description |
|-------|-------------|
| `cytognosis-doc` | Document creation (ADR, proposal, SOP, etc.) |
| `cytognosis-dev` | Development workflow and code standards |
| `cytognosis-branding` | Brand identity, colors, voice, design tokens |
| `cytognosis-orchestrator` | Multi-step task orchestration |
| `cytognosis-org` | Organizational structure and processes |
| `cytognosis-writer` | Long-form writing with Cytognosis voice |
| `cytognosis-design-system-master` | Complete design system reference |
| `cytognosis-template-master` | Document and presentation templates |

### Pull and Verify a Skill

```bash
# Pull a skill to global store
cytoskeleton store pull cytoskills/skills/cytognosis-doc@3.0.0

# Verify it's accessible from all agents
for dir in ~/.agents/skills ~/.claude/skills ~/.kiro/skills ~/.gemini/antigravity/skills; do
    if [ -L "$dir/cytognosis-doc" ]; then
        echo "✓ $(basename $(dirname $dir))/$(basename $dir)/cytognosis-doc → $(readlink -f $dir/cytognosis-doc)"
    else
        echo "✗ $dir/cytognosis-doc missing"
    fi
done
```

```text
✓ agents/skills/cytognosis-doc → ~/.cytognosis/assets/skills/cytognosis-doc
✓ claude/skills/cytognosis-doc → ~/.cytognosis/assets/skills/cytognosis-doc
✓ kiro/skills/cytognosis-doc → ~/.cytognosis/assets/skills/cytognosis-doc
✓ antigravity/skills/cytognosis-doc → ~/.cytognosis/assets/skills/cytognosis-doc
```

### Skill File Structure

Each skill has a `SKILL.md` at its root:

```
~/.cytognosis/assets/skills/cytognosis-doc/
├── SKILL.md              # Main instructions (YAML frontmatter + markdown)
├── references/           # Supporting documentation
│   ├── document_types.md
│   └── templates/
└── examples/             # Example outputs
```

---

## 9. Cross-Package Integration Scenarios

### Scenario A: New Research Project

**Goal**: Create a new single-cell analysis project, pull datasets, set up environment, start neo4j.

```bash
# 1. Scaffold the project with cytocast
cytocast create sc-alzheimers --profile single-cell
cd sc-alzheimers

# 2. Set up the environment
cytoskeleton env sync sc-env --backend mamba
```

```text
✓ Created conda env: sc-env (micromamba)
✓ Installed: scanpy, anndata, pytorch, scvi-tools
```

```bash
# 3. Pull the brain atlas dataset
cytoskeleton store pull cytos/datasets/allen-adult-brain-atlas@2024.1 --local
```

```text
✓ Pulled allen-adult-brain-atlas to ./assets/datasets/
```

```python
# 4. Load the dataset with cytos API
from cytos.assets.dataset_registry import DatasetRegistry
from pathlib import Path

reg = DatasetRegistry(Path("assets/datasets/manifest.yaml"))
reg.load()
atlas = reg.get("allen-adult-brain-atlas")
print(f"Dataset: {atlas.name}, {atlas.cell_count} cells, {atlas.format}")
```

```text
Dataset: allen-adult-brain-atlas, 0 cells, h5ad
```

```bash
# 5. Start neo4j for KG queries
cytoinfra container start neo4j
```

```text
✓ Container 'cytos-neo4j' started
→ Browser: http://localhost:7474
→ Bolt:    bolt://localhost:7687
```

---

### Scenario B: Deploy a New Service to Cytohost

**Goal**: Add a custom Streamlit dashboard, build it, and deploy to cytohost.

```python
# 1. Add the container to the manifest
from cytoinfra.containers.registry import ContainerEntry, ContainerRegistry
from pathlib import Path

reg = ContainerRegistry(
    Path("~/repos/cytognosis/infrastructure/assets/containers/manifest.yaml").expanduser()
)
reg.load()

streamlit = ContainerEntry(
    name="cytognosis-dashboard",
    version="0.1.0",
    image="us-central1-docker.pkg.dev/cytognosis-infrastructure/cytognosis-compute/dashboard:0.1.0",
    source="internal",
    ports={"http": 8501},
    min_ram="1 GB",
    description="Cytognosis interactive data dashboard",
    tags=["dashboard", "internal"],
)
reg.add(streamlit)
reg.save()
```

```bash
# 2. Build the image
cytoinfra container build cytognosis-dashboard \
    --dockerfile infrastructure/container_framework/Dockerfile.dashboard

# 3. Push to internal registry
cytoinfra container push cytognosis-dashboard

# 4. Deploy to cytohost
cytoinfra service deploy cytognosis-dashboard \
    --remote mohammadi@34.171.23.255
```

```text
✓ Built cytognosis-dashboard:0.1.0
✓ Pushed to GCP Artifact Registry
✓ Deployed to cytohost
→ Add Caddy entry for dashboard.cytognosis.org
```

```bash
# 5. Add Caddy reverse proxy entry (on cytohost)
ssh cytohost 'cat >> /opt/cytognosis/Caddyfile << EOF
dashboard.cytognosis.org {
    reverse_proxy cytognosis-dashboard:8501
}
EOF
docker restart caddy'
```

---

### Scenario C: Share a Dataset Across Projects

**Goal**: Register a dataset in one workspace, work on it locally, then share globally.

```bash
# 1. In workspace A — register the dataset locally
cd ~/repos/cytognosis/my-project
```

```python
from cytos.assets.dataset_registry import DatasetAsset, DatasetRegistry
from pathlib import Path

# Create a local registry
reg = DatasetRegistry(Path("assets/datasets/manifest.yaml"))
reg.load()

reg.add(DatasetAsset(
    name="pbmc-10x-multiome",
    version="2025.1",
    source_url="https://www.10xgenomics.com/datasets/pbmc-granulocyte-sorted-10k",
    format="h5ad",
    modality="multi-omics",
    organism="Homo sapiens",
    tissue="blood",
    cell_count=10000,
    license="CC-BY-4.0",
    citation="10x Genomics, 2024",
    description="10k PBMCs with multiome (RNA+ATAC)",
    tags=["10x", "multiome", "PBMC"],
))
reg.save()
```

```bash
# 2. Register as a local asset in cytoskeleton
cytoskeleton store push assets/datasets/ --type datasets --local

# 3. Work with it, iterate...

# 4. When ready, merge to global for all projects
cytoskeleton store merge pbmc-10x-multiome
```

```text
✓ Merged pbmc-10x-multiome from local → global
  Path: ~/.cytognosis/assets/datasets/pbmc-10x-multiome/
```

```bash
# 5. In workspace B — access the shared dataset
cd ~/repos/cytognosis/another-project
cytoskeleton store pull pbmc-10x-multiome
```

---

## Quick Reference

### CLI Commands

| Command | Description |
|---------|-------------|
| `cytoskeleton store list [--local\|--global\|--remote]` | List assets |
| `cytoskeleton store pull <id> [--local\|--global]` | Pull an asset |
| `cytoskeleton store push <path> --type <type>` | Push an asset |
| `cytoskeleton store merge <name>` | Merge local → global |
| `cytoskeleton store search <query>` | Search assets |
| `cytoskeleton env sync <name> --backend <be>` | Sync environment |
| `cytoinfra container list` | List containers |
| `cytoinfra container start <name>` | Start a container |
| `cytoinfra container stop <name>` | Stop a container |
| `cytoinfra service deploy <name> [--remote host]` | Deploy a service |
| `cytoinfra service status <name>` | Check service status |
| `cytoinfra hedgedoc deploy [--remote host]` | Deploy HedgeDoc |
| `cytocast create <name> --profile <profile>` | Scaffold a project |

### Key Paths

| Path | Purpose |
|------|---------|
| `~/.cytognosis/` | Global asset store root |
| `~/.cytognosis/assets/` | Asset content directory |
| `~/.cytognosis/index.yaml` | Global asset index |
| `.cytognosis-index.yaml` | Local (per-workspace) index |
| `~/.agents/skills/` | Central skill symlinks |
| `/opt/cytognosis/` | Cytohost service directory |

### Cytohost Services

| Service | Port | URL |
|---------|------|-----|
| neo4j | 7474, 7687 | `http://cytohost:7474` |
| surrealdb | 8000 | `http://cytohost:8000` |
| hedgedoc | 3005 | `https://docs.cytognosis.org` |
| mlflow | 5000 | `https://mlflow.cytognosis.org` |
| caddy | 80, 443 | Reverse proxy for all services |

### Caddy Subdomains

| Subdomain | Service |
|-----------|---------|
| `docs.cytognosis.org` | HedgeDoc |
| `mlflow.cytognosis.org` | MLflow |
| `code.cytognosis.org` | Zoekt code search |
| `hub.cytognosis.org` | SEEK data hub |
| `cal.cytognosis.org` | Cal.com scheduling |
| `whiteboard.cytognosis.org` | Excalidraw |
| `mermaid.cytognosis.org` | Mermaid diagram editor |
| `notes.cytognosis.org` | Logseq |

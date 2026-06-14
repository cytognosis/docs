# Deep-Dive: Data Storage & Infrastructure Tool Evaluation

> Answering: What does each tool *actually implement* versus wrap? How do they fit (or conflict with) what Cytognosis already builds?

---

## 1. LaminDB: Implementation vs. Wrapper Breakdown

### What LaminDB actually implements (its own code)

LaminDB is a **metadata management layer** written in Python. Its core dependencies reveal what it builds versus what it wraps:

```
lamindb-core
├── lamin_utils (pure Python utilities)
├── lamin_cli (CLI, pure Python)
├── lamindb_setup (Django ORM + fsspec)
│   └── Django → PostgreSQL or SQLite
│   └── fsspec → storage abstraction (local, S3, GCS, HF)
└── psycopg2-binary (Postgres driver)
```

**LaminDB's own implementation consists of:**

| Component | What it does | Lines of code |
| --- | --- | --- |
| **Artifact registry** | SQL models for `Artifact`, `Collection`, `Run`, `Transform`, `ULabel`, `Feature`, `FeatureSet` | Django ORM models |
| **Lineage tracker** | Auto-captures: git commit hash, notebook state, container SHA, environment hash, input/output artifact links | Python decorators around `ln.track()` / `ln.finish()` |
| **Content hashing** | SHA-1 hash of file/folder contents for deduplication | Pure Python (via `lamin_utils`) |
| **Curator API** | Schema validation against `FeatureSet` definitions before save | Python + pandera |
| **Query engine** | `ln.Artifact.filter(cell_type="T cell")` → Django ORM SQL | Django QuerySet wrappers |
| **CLI** | `lamin init`, `lamin connect`, `lamin close` | Python Click CLI |

### What LaminDB wraps (from other projects)

| Wrapped tool | What LaminDB uses it for | Required? |
| --- | --- | --- |
| **Django ORM** | All SQL metadata (Artifact, Run, Transform, Feature models) | Yes (core) |
| **fsspec** | Storage abstraction (local FS, S3, GCS, Azure, HF Hub) | Yes (core) |
| **PostgreSQL** (or SQLite) | Metadata database backend | Yes (core) |
| **pyarrow** | Parquet read/write | Optional (`[full]` extra) |
| **anndata** | `.h5ad` / AnnData read/write | Optional (`[full]` extra) |
| **pandas** | DataFrame operations | Optional (`[full]` extra) |
| **pandera** | Schema validation for DataFrames | Optional (`[full]` extra) |
| **bionty** | Biological ontology lookups (Gene, CellType, Disease, Tissue, Organism) | Optional (`[full]` extra) |
| **pertdb** | Perturbation database access | Optional (`[full]` extra) |

### How critical is TileDB to LaminDB?

**Not critical at all.** TileDB is **not a dependency** of LaminDB. Looking at the `pyproject.toml`, there is no `tiledb` or `tiledbsoma` in any dependency group. LaminDB is storage-format-agnostic — it tracks **any file** as an `Artifact` with a hash and a URI pointing to wherever the data lives.

The connection between LaminDB and TileDB exists through:
- **CELLxGENE Census**: uses TileDB-SOMA under the hood. LaminDB can register Census query outputs as Artifacts
- **Cytognosis choice**: we chose TileDB as the storage engine and LaminDB as the metadata/lineage layer. They're independent.

```
LaminDB ≠ TileDB wrapper
LaminDB = metadata layer that can track files stored in ANY backend:
  - Local filesystem
  - AWS S3
  - Google Cloud Storage (via lamindb_setup[gcp])
  - Azure Blob Storage
  - HuggingFace Hub
  - Any fsspec-compatible backend
```

### How do workflow managers (redun, Nextflow) integrate?

LaminDB does **not execute workflows**. It provides hooks for workflow managers to report lineage:

#### redun integration (manual instrumentation)
```python
import lamindb as ln
from redun import task

@task()
def my_pipeline(input_path: str):
    ln.track()  # Start a Run, capture git hash + environment
    
    # ... your redun pipeline logic ...
    artifact = ln.Artifact(output_path, description="Pipeline output")
    artifact.save()  # Register in LaminDB with lineage
    
    ln.finish()  # Finalize the Run
```

redun does its own AST + data hashing for caching/reproducibility. LaminDB just records the execution context. They're complementary, not overlapping.

#### Nextflow integration (via nf-lamin plugin)
```groovy
// nextflow.config
plugins { id 'nf-lamin' }
lamin { instance = 'myorg/myinstance' }
```

The plugin auto-registers Nextflow outputs as LaminDB Artifacts after pipeline completion.

### What you might already be doing independently

| Function | LaminDB provides | You might already have |
| --- | --- | --- |
| File hashing for dedup | `ln.Artifact` auto-hashes on save | Git + DVC content hashing |
| Lineage tracking | `Run → Transform → Artifact` chain | Manual provenance in notebooks |
| Ontology validation | bionty plugin for Gene/CellType/Disease | OAK/PyOBO scripts |
| Schema validation | Curator API + pandera | Custom Pydantic validators |
| Storage abstraction | fsspec backends | Direct GCS/boto3 calls |

**Bottom line**: LaminDB's unique value is the *unified query interface across all of these*. You can ask "show me all artifacts produced by pipeline X that contain T cells from human donors" in one query. Without LaminDB, you'd need to write custom join logic across git logs, file metadata, and ontology annotations.

---

## 2. MLflow MCP: How it connects to your existing deployment

### Current state

You already have MLflow self-hosted at `https://mlflow.cytognosis.org/` — this is the **MLflow Tracking Server** running in the container framework's `core` stack.

### What MLflow MCP adds

The MLflow MCP Server is a **local process** that acts as a bridge between your AI agents (Antigravity, Claude, Cursor) and your existing MLflow instance. It does **not** replace your deployment. It connects to it.

```
┌─────────────────────────────┐
│ Your AI Agent (Antigravity)  │
│ "Show me the best model     │
│  from the neuro experiment" │
└─────────┬───────────────────┘
          │ MCP protocol (stdio)
          ▼
┌─────────────────────────────┐
│ MLflow MCP Server (local)    │
│ pip install 'mlflow[mcp]'    │
│ MLFLOW_TRACKING_URI=         │
│   https://mlflow.cytognosis  │
│   .org/                      │
└─────────┬───────────────────┘
          │ HTTP (MLflow API)
          ▼
┌─────────────────────────────┐
│ mlflow.cytognosis.org        │
│ (your existing deployment)   │
└─────────────────────────────┘
```

### Concrete configuration

```json
// ~/.gemini/antigravity/mcp_config.json (or ~/.cursor/mcp.json)
{
  "mcpServers": {
    "mlflow": {
      "command": "python",
      "args": ["-m", "mlflow.mcp.server"],
      "env": {
        "MLFLOW_TRACKING_URI": "https://mlflow.cytognosis.org/"
      }
    }
  }
}
```

### What the MCP server exposes (16 tools)

| Tool | What it does | Example prompt to your agent |
| --- | --- | --- |
| `search_experiments` | List/filter experiments | "What experiments do we have?" |
| `search_runs` | Query runs with metrics/params | "Show the top 5 runs by F1 score in the scRNA experiment" |
| `get_run` | Get full details of a run | "What hyperparameters did run abc123 use?" |
| `get_metric_history` | Time-series of a metric | "Plot the loss curve for the latest training run" |
| `search_model_versions` | Query model registry | "What models are registered for the cell-type classifier?" |
| `create_model_version` | Register a new model | "Register the latest checkpoint as v3 of the classifier" |
| `set_model_version_alias` | Set aliases (champion/challenger) | "Promote v3 to champion" |
| `create_registered_model` | Create new model entry | "Create a new model called brain-segmentation" |
| `log_feedback` | Log human/AI assessments | "Mark run xyz as validated by reviewer" |
| `list_artifacts` | Browse run artifacts | "What artifacts did run abc123 produce?" |

### How you'd use the Model Registry

The Model Registry is the part of MLflow that tracks **model versions** with lifecycle stages:

```
Model: cytognosis-cell-classifier
├── v1 (alias: archived) — trained on CELLxGENE Census 2024
├── v2 (alias: challenger) — retrained with bionty v2 ontologies
└── v3 (alias: champion) — current production model
```

With MCP, your agents can query and promote models during development without leaving the IDE. A concrete workflow:

1. Train a model in a notebook → MLflow auto-logs metrics/params
2. Ask your agent: "Compare the last 3 runs and register the best one"
3. Agent calls `search_runs` → finds best → calls `create_model_version`
4. Later: "Promote v3 to champion" → agent calls `set_model_version_alias`

### Is it worth deploying?

**Yes**, for very low effort. It's `pip install 'mlflow[mcp]>=3.5.1'` + one JSON config entry. The value is that your existing MLflow deployment becomes queryable by every AI agent in the Cytognosis stack. No infrastructure changes needed.

---

## 3. DagsHub: Architecture Deep-Dive

### What DagsHub actually is

DagsHub is a **proprietary SaaS platform** (closed source) that provides a unified UI and hosting layer over open-source ML tools. Here is the exact decomposition:

```
┌───────────────────────────────────────────────────────────┐
│                DagsHub Platform (proprietary)               │
│                                                             │
│  ┌──────────────────────────────────────────────────────┐  │
│  │ DagsHub's Own Implementation (closed source)         │  │
│  │                                                      │  │
│  │  • Unified Web UI (React-based dashboard)            │  │
│  │  • "Data Science Pull Requests" (code+data+model)    │  │
│  │  • Data Engine (multimodal annotation/versioning)    │  │
│  │  • Metadata indexing (cross-links Git↔DVC↔MLflow)    │  │
│  │  • User/team management + RBAC + SSO                 │  │
│  │  • Managed hosting infrastructure                    │  │
│  │  • Auto-configuration (tokens, remotes, endpoints)   │  │
│  └──────────────────────────────────────────────────────┘  │
│                                                             │
│  ┌──────────────────────────────────────────────────────┐  │
│  │ Open-Source Components (hosted/managed by DagsHub)    │  │
│  │                                                      │  │
│  │  • Git server (code versioning)                      │  │
│  │  • DVC remote storage (data versioning)              │  │
│  │  • MLflow tracking server (experiment tracking)      │  │
│  │  • Label Studio (data annotation)                    │  │
│  └──────────────────────────────────────────────────────┘  │
└───────────────────────────────────────────────────────────┘
```

### The critical question: What does DagsHub give you that you don't already have?

| DagsHub provides | You already have |
| --- | --- |
| Hosted Git repos | **GitHub** (cytognosis org) |
| Managed MLflow server | **mlflow.cytognosis.org** (self-hosted) |
| DVC remote storage | **GCS** (multi-project) |
| Unified UI | MLflow UI + GitHub UI + CLI tools |
| "Data Science PR" review | GitHub PRs for code + manual review for data |
| Multimodal annotation | Not yet needed (no annotation pipeline) |
| Team RBAC | GitHub org roles + GCP IAM |

**The only novel feature** DagsHub provides is the "Data Science Pull Request" — the ability to review code changes, data version changes, and experiment metric changes in a single view. Everything else is a managed wrapper over tools you already self-host.

### Why it doesn't fit Cytognosis

1. **PHI surface**: Adding DagsHub means another system to audit under HIPAA. Your self-hosted stack keeps everything within the GCP VPC perimeter
2. **Cost at team scale**: Free tier is 20GB / 100 experiments. Team plan is paid. You already have unlimited on self-hosted MLflow + GCS
3. **Vendor lock-in**: DagsHub's proprietary UI layer creates dependency. If they shut down or change pricing (like Sourcegraph did), you lose the integration layer
4. **Solo-founder overhead**: The collaboration features (RBAC, team reviews) are premature until team > 3

---

## 4. Zoekt: Complete Technical Profile

Cloned and inspected at `infrastructure/third_party/zoekt`.

### What Zoekt is

Zoekt is a **trigram-indexed full-text code search engine** written in Go, originally created at Google by Han-Wen Nienhuys and now maintained by Sourcegraph. It's the search backend that powers Sourcegraph (and by extension, GitLab's "Exact Code Search").

### Architecture

```
                                Zoekt System
                                     
    ┌─────────────┐         ┌──────────────┐        ┌──────────────┐
    │  Repository  │         │   Indexer     │        │  Web Server  │
    │  Sources     │         │              │        │   + API      │
    │              │         │  zoekt-git-  │        │              │
    │  • GitHub    │◀───────▶│  index       │───────▶│  zoekt-      │
    │  • Gitiles   │  clone  │              │ shard  │  webserver   │
    │  • GitLab    │         │  zoekt-index │ files  │              │
    │  • Bitbucket │         │              │  on    │  Port 6070   │
    │  • Gitea     │         │  zoekt-      │  SSD   │  Web UI      │
    │  • Local     │         │  indexserver │        │  JSON API    │
    └─────────────┘         └──────────────┘        │  gRPC API    │
                                                     └──────────────┘
```

### Key binaries (from `cmd/`)

| Binary | Purpose |
| --- | --- |
| `zoekt-git-index` | Index a single local git repo |
| `zoekt-index` | Index any local directory (non-git) |
| `zoekt` | CLI search tool against local index |
| `zoekt-indexserver` | Daemon that periodically fetches + indexes repos from code hosts |
| `zoekt-webserver` | HTTP server with web UI + JSON API + gRPC API |
| `zoekt-mirror-github` | Mirror GitHub org repos for indexing |
| `zoekt-mirror-gitlab` | Mirror GitLab repos |
| `zoekt-mirror-gitea` | Mirror Gitea repos |
| `zoekt-merge-index` | Merge multiple index shards |

### How the trigram index works

For a string "banana", Zoekt builds:
```
"ban" → offset 0
"ana" → offsets 1, 3
"nan" → offset 2
```

To search for "needle in haystack", Zoekt:
1. Picks two trigrams (e.g., "nee" and "ack")
2. Looks up their posting lists (position offsets)
3. Checks if they appear at the correct distance apart
4. Verifies the full match on candidate documents

**Performance**: sub-50ms on 2GB+ codebases (Android, Chrome scale). Index is ~3.5× corpus size, stored on SSD.

### Query language

```
# Search for a function name
sym:"processData"

# Search in specific language
lang:python content:"import torch"

# Search in specific repo
repo:"cytognosis/cytos" content:"AnnData"

# Complex boolean
(repo:cytos or repo:infrastructure) lang:python content:"ln.track"

# Regex
content:/def\s+process_\w+/
```

### Container image

```bash
# Start web server (search UI at http://localhost:6070)
docker run --rm -p 6070:6070 -v "$PWD/index:/data/index" ghcr.io/sourcegraph/zoekt

# Index a GitHub org
docker run --rm \
  -v "$PWD/config.json:/config.json:ro" \
  -v "$PWD/token.txt:/home/zoekt/token.txt:ro" \
  -v "$PWD/zoekt-data:/data" \
  ghcr.io/sourcegraph/zoekt \
  zoekt-indexserver -mirror_config /config.json -data_dir /data
```

### What Zoekt does NOT do
- No semantic search (pure trigram/BM25 text matching)
- No code graph / dependency analysis
- No AST parsing for symbol relationships
- No MCP integration
- No AI/agent integration

### Deployment for Cytognosis

Would be added as a service in `container_framework/configs/services/zoekt.yaml`:

```yaml
name: zoekt
description: "Trigram code search across all Cytognosis repos"
image: ghcr.io/sourcegraph/zoekt:latest
ports:
  - "6070:6070"
volumes:
  - zoekt-data:/data
environment:
  - GITHUB_TOKEN=${GITHUB_TOKEN}
resources:
  min_memory: "512m"
  recommended_memory: "2g"
```

---

## 5. GitNexus: Complete Technical Profile

Cloned and inspected at `infrastructure/third_party/gitnexus`.

### What GitNexus is

GitNexus is a **code knowledge graph builder** that parses codebases using Tree-sitter ASTs, stores the graph in LadybugDB (formerly KuzuDB), and exposes 16 MCP tools for AI agents. Written in TypeScript/Node.js.

### Architecture (from source inspection)

```
┌────────────────────────────────────────────────────────────┐
│                     GitNexus Pipeline                       │
│                                                             │
│  1. FILE WALKER                                             │
│     Walks directory tree, respects .gitignore                │
│                    ▼                                        │
│  2. TREE-SITTER PARSER (14 languages)                       │
│     Extracts: functions, classes, methods, interfaces        │
│     Resolves: imports, calls, inheritance, constructors      │
│                    ▼                                        │
│  3. GRAPH BUILDER                                           │
│     Nodes: File, Function, Class, Method, Interface          │
│     Edges: CALLS, IMPORTS, EXTENDS, IMPLEMENTS, MEMBER_OF    │
│                    ▼                                        │
│  4. LEIDEN CLUSTERING (via Graphology)                       │
│     Groups related symbols into functional communities       │
│                    ▼                                        │
│  5. PROCESS TRACING                                         │
│     Traces execution flows from entry points                 │
│                    ▼                                        │
│  6. SEARCH INDEX (BM25 + optional embeddings)               │
│     Hybrid search with Reciprocal Rank Fusion               │
│                    ▼                                        │
│  7. STORAGE: LadybugDB (embedded graph database)            │
│     Stored in .gitnexus/ (gitignored, local-first)           │
│                    ▼                                        │
│  8. MCP SERVER (16 tools via @modelcontextprotocol/sdk)     │
│     AI agents query the graph via standard MCP protocol      │
└────────────────────────────────────────────────────────────┘
```

### Dependencies (from `gitnexus/package.json`)

| Dependency | Role |
| --- | --- |
| `@ladybugdb/core` (formerly KuzuDB) | Embedded graph database. Stores the code KG locally. Supports Cypher queries |
| `tree-sitter` + 14 language grammars | AST parsing (Python, TypeScript, Go, Rust, Java, C#, C, C++, Ruby, PHP, Swift, Kotlin, Dart, JavaScript) |
| `@modelcontextprotocol/sdk` | MCP server implementation |
| `graphology` + `graphology-indices` | In-memory graph data structure for Leiden clustering |
| `@huggingface/transformers` | Optional: semantic embeddings for hybrid search |
| `onnxruntime-node` | ONNX runtime for embedding model inference |
| `express` | HTTP server for `gitnexus serve` (bridge to web UI) |

### The 16 MCP tools

| # | Tool | Purpose |
| --- | --- | --- |
| 1 | `list_repos` | Discover all indexed repositories |
| 2 | `query` | Process-grouped hybrid search (BM25 + semantic + RRF) |
| 3 | `context` | 360-degree symbol view — who calls it, what it calls, which processes |
| 4 | `impact` | Blast radius analysis with depth grouping and confidence |
| 5 | `detect_changes` | Git-diff impact — maps changed lines to affected processes |
| 6 | `rename` | Multi-file coordinated rename using graph + text search |
| 7 | `cypher` | Raw Cypher queries against the knowledge graph |
| 8 | `group_list` | List configured repository groups |
| 9 | `group_sync` | Extract contracts and match across repos/services |
| 10 | `group_contracts` | Inspect extracted contracts and cross-links |
| 11 | `group_query` | Search execution flows across all repos in a group |
| 12 | `group_status` | Check staleness of repos in a group |
| 13-16 | Resources | `repos`, `context`, `clusters`, `processes`, `schema` |

### Concrete example: impact analysis

```
> impact({target: "process_anndata", direction: "upstream", minConfidence: 0.8})

TARGET: Function process_anndata (src/pipelines/scRNA.py)

UPSTREAM (what depends on this):
  Depth 1 (WILL BREAK):
    train_model [CALLS 90%] → src/models/cell_classifier.py:45
    validate_data [CALLS 85%] → src/validation/schema.py:78
  Depth 2 (LIKELY AFFECTED):
    run_pipeline [IMPORTS] → src/main.py
    test_scRNA [CALLS] → tests/test_pipeline.py
```

### License concern

> [!WARNING]
> GitNexus uses **PolyForm Noncommercial License 1.0.0**. This is **not** an open-source license by OSI standards. However, the license explicitly permits use by "charitable organization, educational institution, public research organization." As a 501(c)(3) nonprofit, Cytognosis qualifies under the "Noncommercial Organizations" clause. Enterprise/commercial use requires a separate license from akonlabs.com.

### Zoekt vs GitNexus: complementary, not competing

| Dimension | Zoekt | GitNexus |
| --- | --- | --- |
| **Search type** | Trigram text search (exact pattern matching) | Graph-based structural search (symbol relationships) |
| **Knows code structure?** | No (treats code as text) | Yes (full AST-aware dependency graph) |
| **Query language** | Text-based (`repo:x lang:go content:"foo"`) | Graph-based (`impact()`, `context()`, Cypher) |
| **MCP integration** | None | 16 tools + 7 resources + 2 prompts |
| **Best for** | "Find all files containing `import torch`" | "What breaks if I change `process_anndata`?" |
| **Language** | Go | TypeScript/Node.js |
| **License** | Apache 2.0 | PolyForm Noncommercial |
| **Storage** | Trigram index shards on SSD | LadybugDB (embedded graph DB) |

They compose naturally: Zoekt finds text, GitNexus understands structure.

---

## Summary: What to deploy and in what order

| Priority | Tool | Action | Effort |
| --- | --- | --- | --- |
| 🔴 Now | **MLflow MCP** | Add to `mcp_config.json`, point at `mlflow.cytognosis.org` | 5 min |
| 🔴 Now | **GitNexus** | `npx gitnexus analyze` on each Cytognosis repo, add MCP config | 15 min |
| 🟡 Next | **Zoekt** | Add Docker service to container framework, index cytognosis org | 1 hour |
| 🟡 Next | **LaminDB** | `lamin init --storage gs://cytognosis-internal --schema bionty` on GCS, PostgreSQL backend | 2 hours |
| ⏸️ Defer | **DagsHub** | Keep in catalog as alternative, revisit when team > 5 | — |
| ❌ Skip | **Kedro** | Redundant with redun + LaminDB + copier | — |

### Decisions needed

1. **LaminDB**: Deploy now on `cytognosis-data` (PostgreSQL + GCS)? Or wait until redun workflows are operational?
2. **GitNexus license**: Comfortable with PolyForm Noncommercial (you qualify as 501(c)(3))? Or prefer to wait for an Apache/MIT alternative?
3. **MLflow MCP**: Should I add the config to `mcp_config.json` right now?

# cytomem GraphRAG Integration and Optimization Assessment

**Version:** 1.0  
**Date:** 2026-06-22  
**Author:** Cytognosis Agents (Sonnet 4.6)  
**Status:** Draft for Shahin review  
**Scope:** cytomem v0 Neo4j architecture, Yar-benchmarked engines, GraphRAG framework landscape, optimization and migration recommendations

---

## TL;DR

cytomem already uses Neo4j with Graphiti (a GraphRAG-native temporal graph layer) and a 384-dim local vector index. **Keep Neo4j.** The primary optimizations are: add a full-text index to hybridize the default keyword search, add `PROFILE` query monitoring, and integrate `neo4j-graphrag-python`'s `HybridRetriever` as the MCP recall path. None of the Yar-benchmarked engines (SurrealDB, FalkorDB, Kuzu, SQLite) should replace Neo4j for cytomem. FalkorDB deserves an additional benchmark as a latency-optimized Neo4j alternative. LightRAG is the highest-value additional GraphRAG benchmark for the Yar harness because it adds document-level entity extraction at a fraction of Microsoft GraphRAG's cost.

---

## 1. cytomem Current Architecture

### 1.1 Neo4j Connection and Driver

cytomem connects to Neo4j Community Edition at `bolt://localhost:7687` via the official `neo4j>=5.18` Python driver (`GraphDatabase.driver`). The `GraphClient` singleton (`src/cytomem/graph/client.py`) holds the bolt connection and also lazily initializes a `Graphiti` instance (from `graphiti-core>=0.10`) using the same bolt URI. Graphiti uses `LocalEmbedder` (fastembed BAAI/bge-small-en-v1.5, 384 dims, CPU ONNX) as its embedding client and `GeminiLLMClient` (Gemini 2.5 Flash via ADC or API key, with a stub fallback) as its LLM client for entity extraction. The database holds approximately 7,322 `Artifact` nodes across 14 repositories as of mid-June 2026.

### 1.2 Graph Schema and Ontology

The graph is a property-graph (not an RDF triple store). Node labels and their key properties:

| Label | Key properties | Index |
|---|---|---|
| `Artifact` | `id` (cytognosis:// URI), `repo`, `path`, `title`, `content_hash`, `artifact_type`, `asset_kind`, `lifecycle`, `branch`, `commit_sha`, `created_by`, `modified_at`, `embedding` (float[384]) | B-tree on `id`, `repo`, `content_hash`, `artifact_type`; vector index on `embedding` (cosine, 384 dims) |
| `Episode` | `id` (UUID), `reference_time`, `content`, `source_id` | B-tree on `source_id`, `reference_time` |
| `Task` | `id`, `title`, `status`, `priority`, `repo`, `track`, `description`, `deliverable`, `verification` | B-tree on `id`, `status` |
| `Backlog` | `id`, `idea`, `priority`, `track`, `status` | B-tree on `id` |

Relationship types: `REFERENCES` (Episode to Artifact), `RELATES_TO` (Artifact to Artifact, carries `type` property from the set `DEPENDS_ON | SUPERSEDES | IMPORTS | TESTS | DOCUMENTS`), `PROMOTED_FROM` (Task to Backlog).

The schema is relatively shallow. Artifacts are the primary node type; Episodes form a temporal audit log. Cross-repo relationships are created manually (`link add`) or via a name-matching heuristic (`link auto`). There is no LLM-extracted entity graph beyond what Graphiti builds internally when `get_graphiti()` is called.

### 1.3 Ingestion Pipeline

Three scanner paths, all producing `TrackedArtifact` Pydantic models that flow into `add_episode()`:

- **`scan_repo`** (git-backed): iterates `repo.head.commit.tree.traverse()` for all blob objects tracked by git; skips binary extensions (`.png`, `.pdf`, `.db`, etc.); classifies by filename pattern into `ArtifactType` and `AssetKind`.
- **`scan_doc_source`** (folder-based): `rglob` with configurable include/exclude globs; defaults to `*.md, *.txt, *.ipynb, *.json, *.yaml, *.toml`; skips files over 1 MB.
- **`scan_agent_artifacts`** (agent session scanner, currently hardcoded to `antigravity` type, scans up to 20 conversations).

The `add_episode()` coroutine runs a MERGE-based Cypher upsert. It: (1) generates an embedding for a short descriptive string about the artifact using `LocalEmbedder`; (2) uses `MERGE (a:Artifact {id: $artifact_id})` with `ON CREATE / ON MATCH` to detect whether the artifact is new or changed (comparing `content_hash`); (3) creates an `Episode` node and `REFERENCES` relationship only when the content changed. This is a write-heavy operation per artifact, and it is called sequentially in a for-loop (though inside `asyncio.to_thread` to avoid blocking).

### 1.4 Recall and Query Patterns

cytomem exposes two retrieval modes, both available via MCP tool `cytomem_recall` and the CLI `search` command:

- **Keyword search** (`ARTIFACT_SEARCH`): `WHERE a.title CONTAINS $q OR a.path CONTAINS $q OR a.repo CONTAINS $q`. This is a full-graph linear scan with no index support because Neo4j B-tree indexes do not accelerate `CONTAINS` predicates. For 7,322 nodes this is fast enough today but will degrade linearly as the graph grows.
- **Semantic search** (`SEMANTIC_SEARCH`): `CALL db.index.vector.queryNodes('artifact_embedding', $k, $embedding)`. This is a proper ANN search against the 384-dim cosine vector index. It is the performance-correct path but requires the caller to pass `semantic=True`.

Additional query patterns: `DUPLICATE_GROUPS` (collect/group by `content_hash`), `ARTIFACT_TIMELINE` (temporal Episode chain for one artifact), `ARTIFACTS_PER_REPO` (aggregate count), and task/backlog CRUD queries. These are all infrequent or fast.

### 1.5 MCP Server Interface

`cytomem-mcp` runs as a FastMCP server (`src/cytomem/mcp/server.py`). It exposes 14 tools: `cytomem_recall`, `cytomem_stats`, `cytomem_duplicates`, `cytomem_timeline`, task CRUD (add/list/update/delete), backlog CRUD (add/list/promote/delete), and `cytomem_link_add` / `cytomem_link_list`. All tools open a Neo4j driver session per call (no connection pooling beyond the driver's internal pool). The MCP server is the primary interface used by Claude agents in the Cowork sandbox.

### 1.6 Embeddings

Local ONNX model via `fastembed`: `BAAI/bge-small-en-v1.5`, 384 dimensions, CPU-only, no API key required. Embeddings are generated at ingest time and stored in `a.embedding`. The vector index is Neo4j's native HNSW implementation (`CREATE VECTOR INDEX artifact_embedding`). The embedding content is a short string of the form `"Artifact {id} ({title}) at {repo}/{path}."`, not the full file content. This means semantic recall is primarily over artifact metadata, not document body text.

### 1.7 Performance-Sensitive Paths

In order of sensitivity:

1. **Ingest loop** (`add_episode` called for 7,322+ artifacts serially): embedding generation is the bottleneck (CPU ONNX model, synchronous under `asyncio.to_thread`). A full re-ingest is not a routine operation, but partial re-ingests on large repos are.
2. **Keyword search** (`ARTIFACT_SEARCH` CONTAINS scan): O(n) over all Artifact nodes; no index acceleration. At 7K nodes, latency is sub-100ms, but at 50K nodes this becomes the bottleneck.
3. **MCP recall latency**: each `cytomem_recall` call opens a Neo4j session, runs a query, and returns JSON. Session overhead is negligible on localhost but accumulates if agents call recall many times per task.
4. **Graphiti entity extraction** (when `get_graphiti()` is active with a live LLM): Gemini API round-trips add 200-800ms per entity extraction call during ingest. This is not on the hot path for most queries but matters for incremental ingest.

---

## 2. Fit of the Yar-Benchmarked Engines to cytomem

The Yar benchmark harness evaluated SurrealDB, FalkorDB, Kuzu, and SQLite-stack (likely SQLite + sqlite-vec or similar) for the Yar on-device use case. cytomem's requirements differ materially: it is a desktop-local server process (not on-device), it already has a live 7K-node graph that would need migration, and its core value is the temporal audit trail (Episodes) plus cross-repo relationship graph, not pure vector recall.

### 2.1 Engine-by-Engine Assessment

| Engine | Graph model | Vector search | Desktop local | cytomem fit | Verdict |
|---|---|---|---|---|---|
| **SurrealDB** | Multi-model (document + graph via SurrealQL) | Yes (vector type, HNSW) | Yes (single binary) | Graph model is less mature than Neo4j's property graph; Cypher-to-SurrealQL migration non-trivial; prior Yar benchmark showed SurrealDB last-place likely due to config issues (FTS index misconfiguration + per-call connection overhead), retest pending | Not recommended for migration; re-evaluate after Yar retest |
| **FalkorDB** | Redis-based sparse-matrix property graph, Cypher-compatible | Yes (built-in vector index) | Yes (Docker image, ~300 MB) | Cypher-compatible means cytomem queries port with minimal changes; GraphRAG-SDK v1.0 exists; benchmarks show sub-millisecond query latency vs Neo4j; source-available license (RSALv2) | **Benchmark candidate**: strongest Neo4j swap candidate if latency becomes critical |
| **Kuzu** | Embedded in-process columnar graph (OLAP-optimized) | Yes (via DuckDB-style extensions) | Yes (embedded, no server) | Acquired by Apple Oct 2025, archived; community forks exist but carry abandonment risk; designed for analytical graph queries, not agent memory writes | Not recommended; abandonment risk is disqualifying |
| **SQLite-stack** | Relational; graph via self-joins | Yes (sqlite-vec extension) | Yes (embedded) | No native property graph; RELATES_TO multi-hop queries require recursive CTEs; Episode temporal chain becomes complex; not a graph database | Not suitable for cytomem's graph semantics |

### 2.2 Migration Feasibility Summary

A migration from Neo4j to any of these engines is not warranted at the current scale (7K nodes). The cost of rewriting Cypher queries, testing the MCP server, and validating the vector index behavior outweighs any latency benefit at desktop-local operation. The only scenario that would justify migration is if cytomem were deployed as a shared multi-user service with thousands of concurrent agent sessions, at which point FalkorDB's throughput advantage becomes meaningful.

**Recommendation: keep Neo4j. Optimize in place.**

---

## 3. Standard GraphRAG Frameworks

### 3.1 Framework Comparison Table

| Framework | Backend support | Desktop / local fit | Retrieval approach | How to benchmark |
|---|---|---|---|---|
| **Microsoft GraphRAG** | Cosmos DB, Azure AI Search, DuckDB (local), Neo4j (experimental) | Yes, but indexing costs $50-200 / 500 pages with GPT-4 and 45+ min; can use local LLM (Ollama) to reduce cost | Global: community summary hierarchy (Leiden algorithm); Local: entity neighborhood + text chunks; DRIFT search combines both | GraphRAG-Bench (Novel / Medical datasets); compare global query recall vs LightRAG and vector baseline; measure per-query latency and cost |
| **LightRAG** | In-memory, JSON/KV store, Neo4j, any LLM backend | Yes; indexes 500 pages in ~3 min for ~$0.50 with GPT-4o-mini; fully local with Ollama | Dual-mode: naive vector similarity + keyword; local graph traversal; global community summarization (lighter than MSFT); hybrid combining both | Same GraphRAG-Bench datasets; compare Hits@10 and answer quality vs MSFT GraphRAG at 1/100th cost; measure latency P50/P95 |
| **nano-graphrag** | In-memory by default; pluggable (Neo4j, DuckDB) | Yes; ~1,000 lines of Python, zero external dependencies beyond LLM API | Simplified extraction, flat graph, no community detection | Use as a baseline / ablation; plug in cytomem's embedding model and measure recall vs cytomem keyword search |
| **LlamaIndex PropertyGraphIndex** | Neo4j, Nebula, in-memory; integrates with any LlamaIndex retriever | Yes; runs against local Neo4j instance; no extra infra needed | Combines graph traversal (entity subgraph) with vector similarity; supports both keyword and semantic entity lookup | LlamaIndex RAGAS eval harness; measure faithfulness and relevance on a cytomem query set; compare against cytomem's current SEMANTIC_SEARCH path |
| **neo4j-graphrag-python** | Neo4j only | Yes; direct bolt connection, no server change needed | VectorRetriever, FulltextRetriever, HybridRetriever (vector + BM25), GraphRAGRetriever (graph traversal + vector); Neo4j 2026.01+ routes SEARCH clause to in-index filtering | Use HybridRetriever on the existing cytomem graph; measure recall vs current CONTAINS-scan keyword path; latency comparison is immediate |
| **Graphiti (Zep)** | Neo4j, FalkorDB | Yes; ships as Python package, runs against local Neo4j | Temporal bi-graph: entities + relationships + Episode facts; hybrid search combining BM25, semantic embeddings, and graph traversal; P95 latency 300ms | Already integrated in cytomem (`graphiti-core` in pyproject.toml); benchmark: compare `cytomem_recall semantic=True` vs `graphiti.search()` on the same query set; measure recall and latency |

### 3.2 Desktop Fit Assessment

For cytomem's context (single-user, localhost Neo4j, CPU-only embeddings), the ranking by immediate integration value is:

1. **neo4j-graphrag-python `HybridRetriever`**: zero infra change, direct drop-in over the current SEMANTIC_SEARCH path, adds BM25 full-text to complement the vector index.
2. **Graphiti**: already a dependency; the `get_graphiti()` path in `GraphClient` is unused in the MCP recall path today; enabling it adds temporal reasoning with no new infrastructure.
3. **LightRAG**: adds document-level entity extraction; requires running a local LLM (Ollama) or Gemini API; most relevant for the planned v1 migration where full file content is indexed, not just metadata strings.
4. **LlamaIndex PropertyGraphIndex**: highest integration complexity; most useful if cytomem moves toward a multi-retriever pipeline.
5. **Microsoft GraphRAG** and **nano-graphrag**: reference benchmarks only; not recommended for production integration at cytomem's scale.

---

## 4. Recommendation for cytomem

### 4.1 Keep Neo4j

**Recommendation: keep Neo4j. Do not migrate.**

Reasoning:

- cytomem already stores 7,322 nodes with a working vector index, temporal Episode chain, and Graphiti integration. Migration disruption exceeds any achievable latency benefit at this scale.
- The primary performance problem is the `CONTAINS` keyword scan, which is fixable with a Neo4j full-text index, not a database swap.
- FalkorDB is Cypher-compatible but introduces a license constraint (RSALv2, not Apache 2.0) and requires Docker. Neo4j Community Edition is free and already running.
- The planned v1 migration to LinkML-generated schemas and cytognosis:// URIs is already scoped for Neo4j; re-targeting it to a new engine doubles migration work.

### 4.2 Concrete Neo4j Optimizations

**Priority 1: Add a full-text index for keyword search.** Replace the `CONTAINS` linear scan with a Lucene-backed full-text index. This is a one-line schema change and eliminates the O(n) recall problem.

```cypher
CREATE FULLTEXT INDEX artifact_fulltext IF NOT EXISTS
FOR (a:Artifact)
ON EACH [a.title, a.path, a.repo, a.artifact_type]
OPTIONS { indexConfig: { `fulltext.analyzer`: 'standard-no-stop-words' } }
```

Then update `ARTIFACT_SEARCH` and `recall_episodes` to use `CALL db.index.fulltext.queryNodes('artifact_fulltext', $q)`.

**Priority 2: Add `neo4j-graphrag-python` `HybridRetriever` to the MCP recall path.** The `HybridRetriever` combines the vector index and the new full-text index in a single ranked retrieval call, with Neo4j 2026.01's in-index filtering for simple property filters. This replaces the current choice between `ARTIFACT_SEARCH` (keyword only) and `SEMANTIC_SEARCH` (vector only) with a unified hybrid call.

**Priority 3: Embed document body text, not just metadata strings.** The current embedding content is `"Artifact {id} ({title}) at {repo}/{path}."`. This limits semantic recall to artifact identity. For the v1 migration, embed the first 512 tokens of each file's content alongside the metadata string to make semantic recall content-aware.

**Priority 4: Batch ingest embeddings.** `LocalEmbedder.create_batch()` is already implemented. The ingest loop calls `embedder.create(content)` per artifact. Switch to `create_batch()` in chunks of 64-128 artifacts to reduce ONNX model overhead during full re-ingests.

**Priority 5: Enable `PROFILE` monitoring for slow queries.** Add a dev-mode flag that prefixes Cypher queries with `PROFILE` and logs the execution plan. This makes it easy to detect query plan regressions as the graph grows.

**On APOC and GDS:**

- APOC is not needed for cytomem's current query patterns. It would become relevant if cytomem added path-based queries (e.g., shortest path between two artifacts) or graph projection for community detection.
- GDS (Graph Data Science library) would be valuable for a future "find related artifacts" feature using node similarity or community detection, but it is not free for production use and is out of scope for v0.

### 4.3 Whether to Add a GraphRAG Retrieval Layer

**Recommendation: yes, add `neo4j-graphrag-python` `HybridRetriever` as the default recall path, and activate the existing Graphiti integration for temporal queries.**

The Graphiti integration (`graphiti-core` is already in `pyproject.toml`; `get_graphiti()` is in `GraphClient`) is currently only used at ingest time for entity extraction when Gemini credentials are available. The MCP `cytomem_recall` tool bypasses it entirely. Routing `cytomem_recall semantic=True` through `graphiti.search()` adds: (1) BM25 keyword matching; (2) semantic vector similarity; (3) graph traversal over entity relationships extracted by Graphiti; and (4) temporal recency weighting. Graphiti reports P95 latency of 300ms on localhost Neo4j for hybrid search, well within the agent response budget.

For LightRAG: defer to the v1 migration, when full document content will be embedded. LightRAG's value (document entity extraction, dual-mode retrieval) is maximized when the full artifact body is indexed rather than a short metadata string.

---

## 5. Additional Desktop Benchmark Plan

### 5.1 Benchmark Objectives

The Yar harness (as described in `STORAGE_BENCHMARK_TRACKER.md`) evaluated storage engines on: vector recall (Hits@K), exact-match keyword recall, write throughput (ingest), read latency (P50/P95), and index build time. The cytomem GraphRAG benchmark extends this with: **retrieval quality over a realistic cytomem query set** (not just ANN recall), **multi-hop graph traversal accuracy**, and **latency under MCP call patterns** (short queries, frequent, from an agent loop).

### 5.2 Query Workload

Construct a fixed query set of 50 questions representative of cytomem agent use:

- **Class A (15 queries): artifact lookup** -- "Find the IGoR solution summary", "What is the latest version of the Yar feature spec". Baseline: `ARTIFACT_SEARCH` keyword scan.
- **Class B (15 queries): semantic recall** -- "Show me research docs about BDNF", "Find planning documents for the NSF grant". Baseline: `SEMANTIC_SEARCH` vector index.
- **Class C (10 queries): cross-repo relationship** -- "What artifacts in the docs repo relate to cytomem?", "Which tasks are linked to the IGoR track?". Requires graph traversal over `RELATES_TO` edges.
- **Class D (10 queries): temporal / recency** -- "What changed in the Grants repo in the last 7 days?", "Show the history of the IGoR solution summary". Requires Episode chain traversal.

Ground truth: manually label top-5 correct results per query from the live 7K-node graph (one-time effort, ~2-3 hours).

### 5.3 Tools to Benchmark

| Tool | What to benchmark | New infra needed |
|---|---|---|
| **cytomem current** (`ARTIFACT_SEARCH`) | Class A baseline | None |
| **cytomem current** (`SEMANTIC_SEARCH`) | Class B baseline | None |
| **neo4j-graphrag-python `HybridRetriever`** | Class A+B unified | `pip install neo4j-graphrag`; no server change |
| **Graphiti `search()`** (already in codebase) | Class A+B+D with temporal weighting | Enable in MCP recall path (code change only) |
| **LightRAG** (local Ollama + cytomem Neo4j backend) | Class A+B+C using extracted entity graph | `ollama pull llama3.1`; pip install `lightrag-hku`; 3-min index build |
| **FalkorDB** (drop-in Neo4j swap) | Latency/throughput parity test for all classes | `docker run falkordb/falkordb:latest`; cytomem query migration (~1 day effort) |

### 5.4 Metrics

For each tool, measure:

- **Hits@5** (fraction of queries where at least one correct result is in top 5)
- **MRR** (mean reciprocal rank of first correct result)
- **P50 / P95 latency** (wall-clock from query string to result list, measured from the MCP tool call layer)
- **Index build time** (time to re-ingest a 1,000-artifact test subset)
- **Memory footprint** (RSS of the backend process during query)

### 5.5 Integration with Yar Harness

The Yar storage benchmark harness (in `Yar/benchmark/`) currently targets on-device engines. cytomem's benchmark targets desktop-local server processes but can share:

- The query set format and Hits@K / MRR scoring functions (extract into a shared `benchmark_utils.py`).
- The result reporting schema (JSON or TSV with engine, query class, metric, value).
- The `STORAGE_BENCHMARK_TRACKER.md` format for tracking results over time.

A thin adapter layer maps the cytomem query set (Cypher/MCP calls) to the same harness runner that the Yar benchmark uses for storage calls. This keeps the two benchmark tracks parallel without requiring a unified harness refactor.

### 5.6 Execution Sequence

1. **Week 1**: add full-text index, update `ARTIFACT_SEARCH` query, label ground-truth query set (50 queries).
2. **Week 1-2**: run Class A+B baseline benchmarks (cytomem current, `HybridRetriever`). Record results in `STORAGE_BENCHMARK_TRACKER.md`.
3. **Week 2**: enable Graphiti `search()` in MCP recall; run Class A+B+D with Graphiti.
4. **Week 3**: run LightRAG index build on 1,000-artifact subset with Ollama; run all query classes.
5. **Week 4**: FalkorDB latency parity test (optional; only if a latency regression is observed in the above steps).

---

## 6. Sources

- [Graph RAG in 2026: What Works in Production (Paperclipped, March 2026)](https://www.paperclipped.de/en/blog/graph-rag-production/) -- framework cost comparison, type taxonomy, Graphiti and LightRAG analysis.
- [GitHub: getzep/graphiti](https://github.com/getzep/graphiti) -- Graphiti architecture, FalkorDB + Neo4j backend support, P95 300ms latency claim.
- [Graphiti: Knowledge graph memory for an agentic world (Neo4j blog)](https://neo4j.com/blog/developer/graphiti-knowledge-graph-memory/) -- temporal bi-graph architecture.
- [GitHub: FalkorDB/GraphRAG-SDK](https://github.com/FalkorDB/GraphRAG-SDK) -- GraphRAG-SDK v1.0, GraphRAG-Bench Novel + Medical #1 ranking.
- [FalkorDB benchmark tool](https://github.com/FalkorDB/benchmark) -- throughput comparisons vs Neo4j.
- [neo4j-graphrag-python documentation](https://neo4j.com/docs/neo4j-graphrag-python/current/) -- HybridRetriever, VectorRetriever, FulltextRetriever, in-index filtering in Neo4j 2026.01+.
- [Hybrid Retrieval for GraphRAG (Neo4j Developer Blog)](https://medium.com/neo4j/hybrid-retrieval-for-graphrag-applications-using-the-neo4j-genai-python-package-fddfafe06ff3) -- HybridRetriever implementation patterns.
- [Neo4j Vector Indexes -- Cypher Manual](https://neo4j.com/docs/cypher-manual/current/indexes/semantic-indexes/vector-indexes/) -- SEARCH clause, HNSW index configuration.
- [LlamaIndex GraphRAG V2](https://docs.llamaindex.ai/en/stable/examples/cookbooks/GraphRAG_v2/) -- PropertyGraphIndex, Neo4j backend integration.
- [GraphRAG-Bench: When to Use Graphs in RAG (ICLR 2026)](https://github.com/GraphRAG-Bench/GraphRAG-Benchmark) -- standardized benchmark suite for GraphRAG evaluation.
- [Microsoft GraphRAG benchmarking datasets](https://github.com/microsoft/graphrag-benchmarking-datasets) -- Kevin Scott Podcasts dataset, 125 open-ended questions.
- [Neo4j alternatives in 2026 (ArcadeDB blog)](https://arcadedb.com/blog/neo4j-alternatives-in-2026-a-fair-look-at-the-open-source-options/) -- Kuzu acquisition by Apple, KuzuDB abandonment risk.
- [KuzuDB benchmark study (prrao87)](https://github.com/prrao87/kuzudb-study) -- embedded graph database performance on social network datasets.
- [GraphRAG in 2026: Practical Buyer's Guide (Medium)](https://medium.com/@tongbing00/graphrag-in-2026-a-practical-buyers-guide-to-knowledge-graph-augmented-rag-43e5e72d522d) -- LightRAG vs Microsoft GraphRAG cost analysis.
- [Building GraphRAG Locally (Neo4j Developer Blog)](https://medium.com/neo4j/building-graphrag-locally-0c8e11752644) -- local Neo4j Desktop setup, Ollama integration.

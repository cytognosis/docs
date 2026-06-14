# Neo4j vs SurrealDB Benchmark Report

This document captures the evaluation results comparing the existing Neo4j graph deployment to the new SurrealDB implementation.

## Methodology
- Both databases run locally.
- Sample dataset ingested via the `KGXToSurrealConverter` pipeline.
- Queries run 10x for warmup, then measured over 100 iterations.

## Expected Query Dimensions
1. **Simple Lookup**: Fetching a node strictly by ID.
2. **1-hop Traversal**: Fetching direct relationships.
3. **Multi-hop Traversal**: Complex recursive graph relationships.
4. **Aggregation**: Analytics querying on edge metadata.

*(Run `python src/cytos/benchmarks/benchmark_neo4j_vs_surrealdb.py` to append live results here)*
\n\n## Automated Benchmark Results\n- **lookup**\n  - Neo4j: 0.49269934999756515s\n  - SurrealDB: FAILs\n- **1_hop**\n  - Neo4j: 0.006738647003658116s\n  - SurrealDB: FAILs\n- **aggregation**\n  - Neo4j: 0.0068114429886918515s\n  - SurrealDB: FAILs\n\n\n## Automated Benchmark Results\n- **lookup**\n  - Neo4j: 0.3958501099841669s\n  - SurrealDB: FAILs\n- **1_hop**\n  - Neo4j: 0.007071535015711561s\n  - SurrealDB: FAILs\n- **aggregation**\n  - Neo4j: 0.00800005701603368s\n  - SurrealDB: FAILs\n\n\n## Automated Benchmark Results\n- **lookup**\n  - Neo4j: 0.35119104900513776s\n  - SurrealDB: 0.00198320799972862s\n- **1_hop**\n  - Neo4j: 0.0074474060093052685s\n  - SurrealDB: 0.0016637480002827942s\n- **aggregation**\n  - Neo4j: 0.00770993999321945s\n  - SurrealDB: 0.0013849349925294518s\n\n\n## Automated Benchmark Results\n- **lookup**\n  - Neo4j: 0.3490445979987271s\n  - SurrealDB: 0.0011601849982980639s\n- **1_hop**\n  - Neo4j: 0.005892597982892767s\n  - SurrealDB: 0.0012493610265664756s\n- **aggregation**\n  - Neo4j: 0.0054522400023415685s\n  - SurrealDB: 0.0007982430106494576s\n
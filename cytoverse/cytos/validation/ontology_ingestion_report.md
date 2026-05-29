# Ontology Ingestion Report

> Completed: 2026-05-12 09:40 UTC

## Summary

Downloaded and ingested 47 ontologies into the Cytos Knowledge Graph, adding **567,216 new nodes** and **2,540,565 new edges** (including 1,273,903 OLS4 SSSOM cross-ontology mapping edges).

**Updated KG: 6,372,056 nodes × 55,294,641 edges**

## OWL Downloads

| Status | Count | Details |
|--------|-------|---------|
| ✅ Downloaded | 37 | 5.4 GB total from OBO Foundry PURLs |
| ✅ Parsed (batch) | 30 | Ontologies <200MB via pronto |
| ✅ Parsed (individual) | 2 | EFO (332MB), MONDO (232MB) |
| ⏭ Deferred (large) | 5 | CHEBI (775M), DRON (670M), NCIT (775M), UPHENO (397M), PR (1.3G) |
| 📡 SSSOM-only | 8 | MBA, DMBA, HBA, DHBA, MESH, HGNC, LIPIDMAPS, ICTV |
| ℹ Already in KG | 18 | Via UMLS/bero/HRA imports |

## Parsed Ontologies (32 OWL files)

| Ontology | Prefix | Nodes | Edges | Size |
|----------|--------|-------|-------|------|
| EFO | EFO | 93,299 | 156,651 | 332M |
| OBA | OBA | 82,874 | — | 159M |
| MONDO | MONDO | 58,940 | 98,023 | 232M |
| GO | GO | 51,937 | — | 124M |
| CLO | CLO | 43,327 | — | 42M |
| PCL | PCL | 37,210 | 62,182 | 160M |
| MP | MP | 35,151 | — | 98M |
| HP | HP | 32,085 | — | 73M |
| DOID | DOID | 19,493 | — | 27M |
| CL | CL | 19,150 | — | 63M |
| ORDO | ORDO | 15,788 | — | 7.3M |
| UBERON | UBERON | 11,831 | — | 94M |
| PATO | PATO | 8,625 | 18,964 | 21M |
| MAXO | MAXO | 7,120 | — | 16M |
| OBI | OBI | 5,178 | — | 9.4M |
| ONS | ONS | 4,834 | — | 2.8M |
| NBO | NBO | 4,546 | 10,776 | 5.4M |
| CMO | CMO | 4,144 | — | 9.0M |
| ZFA | ZFA | 3,285 | 12,293 | 7.1M |
| OPMI | OPMI | 3,153 | — | 4.0M |
| PW | PW | 2,760 | 3,389 | 5.2M |
| XCO | XCO | 1,826 | 2,431 | 4.2M |
| ICO | ICO | 1,558 | — | 1.8M |
| BAO | BAO | 1,534 | — | 1.6M |
| DPO | DPO | 1,552 | — | 3.9M |
| MPATH | MPATH | 891 | 949 | 1.4M |
| MMO | MMO | 869 | 982 | 1.9M |
| WBls | WBls | 796 | 3,408 | 1.8M |
| MF | MF | 400 | 452 | 421K |
| HsapDv | HsapDv | 260 | 366 | 517K |
| FBdv | FBdv | 250 | 712 | 512K |
| MmusDv | MmusDv | 178 | 388 | 359K |

## OLS4 SSSOM Cross-Ontology Mappings (45 files)

| SSSOM Source | Mapping Edges |
|-------------|--------------|
| PR | 238,940 |
| CHEBI | 229,395 |
| NCIT | 155,054 |
| MONDO | 146,765 |
| LIPIDMAPS | 119,807 |
| ORDO | 56,774 |
| UBERON | 49,369 |
| DOID | 37,839 |
| DRON | 36,593 |
| EFO | 36,071 |
| HP | 33,565 |
| GO | 26,807 |
| MESH | 21,554 |
| CLO | 20,624 |
| PCL | 13,502 |
| OBA | 11,890 |
| MP | 10,244 |
| CMO | 6,114 |
| CL | 3,126 |
| ZFA | 3,108 |
| XCO | 2,870 |
| OBI | 2,097 |
| PW | 2,048 |
| BAO | 1,986 |
| PATO | 1,551 |
| MAXO | 1,447 |
| MMO | 884 |
| MPATH | 744 |
| NBO | 727 |
| OPMI | 512 |
| ICO | 377 |
| ONS | 258 |
| HsapDv | 174 |
| WBls | 64 |
| HBA | 55 |
| MmusDv | 50 |
| DHBA | 47 |
| MBA | 36 |
| DPO | 30 |
| FBdv | 16 |
| HGNC | 7 |
| DMBA | 1 |

**Total SSSOM mapping edges: 1,273,903**

## Files Created/Modified

| File | Description |
|------|-------------|
| [ontology_owl.py](file:///home/mohammadi/repos/cytognosis/cytos/src/cytos/ingest/ontology_owl.py) | OWL→KGX ingestion pipeline |
| [cellxgene.py](file:///home/mohammadi/repos/cytognosis/cytos/src/cytos/services/cellxgene.py) | CellxGeneService + EnsemblOntologyResolver |
| [test_cellxgene_service.py](file:///home/mohammadi/repos/cytognosis/cytos/tests/test_cellxgene_service.py) | 11 tests for CXG service |
| [TASKS.md](file:///home/mohammadi/repos/cytognosis/cytos/design/TASKS.md) | Updated task registry |
| `~/datasets/latest/ontologies/` | 37 OWL files (5.4 GB) |
| `data/kg/nodes.tsv` | 6,372,056 nodes |
| `data/kg/edges.tsv` | 55,294,641 edges |

## Ontologies Not Available as OWL

These ontologies don't have standard OWL distributions, but their cross-references are captured via OLS4 SSSOM mappings:

| Ontology | Reason | Alternative |
|----------|--------|------------|
| MBA/HBA/DMBA/DHBA | Allen Institute proprietary format | SSSOM mappings ingested |
| MESH | NLM proprietary (already 16,825 nodes via UMLS) | SSSOM mappings ingested |
| HGNC | Gene nomenclature (7,283 nodes via KG + Ensembl xrefs) | SSSOM mappings ingested |
| LIPID MAPS | No OWL download available | 119,807 SSSOM mappings ingested |
| ICTV | No OWL format available | 0 mappings (no cross-references) |
| Ensembl Glossary | Available via Ensembl ontology DB (601K terms) | Resolved via EnsemblOntologyResolver |
| Lifestyle Factors Ontology | No OLS4 SSSOM or OWL available | Future: manually curate |

## Deferred Large Ontologies

These ontologies are >200MB and can be parsed individually when needed:

| Ontology | Size | Status |
|----------|------|--------|
| CHEBI | 775M | 205K nodes already in KG + 229K SSSOM mappings |
| PR | 1.3G | 18K nodes already in KG + 239K SSSOM mappings |
| NCIT | 775M | 111K nodes already in KG + 155K SSSOM mappings |
| DRON | 670M | 6 nodes in KG + 36.6K SSSOM mappings |
| UPHENO | 397M | 37K nodes already in KG + 701 SSSOM mappings |

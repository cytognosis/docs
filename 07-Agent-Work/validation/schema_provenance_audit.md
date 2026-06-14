# Schema Alignment & Provenance Audit

> **Date**: 2026-05-12

## 1. Schema Alignment: KG Categories vs LinkML Classes

### Node Categories: 36 in KG vs 20 in schema

| KG Category | Has Schema Class? | Schema File | Notes |
|-------------|:-:|---|---|
| `biolink:AnatomicalEntity` | ✅ | anatomy.yaml | `AnatomicalEntity` |
| `biolink:Cell` | ⚠️ | anatomy.yaml | Mapped to `CellularComponent` class_uri, not `Cell` |
| `biolink:CellLine` | ❌ | — | **Needs schema** (167K nodes from Cellosaurus) |
| `biolink:CellularComponent` | ✅ | anatomy.yaml / pathway.yaml | `CellType`, `CellularComponent` |
| `biolink:ChemicalEntity` | ✅ | drug.yaml | `ChemicalCompound` |
| `biolink:ClinicalAttribute` | ❌ | — | **Needs schema** (422K nodes from LOINC/UMLS) |
| `biolink:ClinicalFinding` | ❌ | — | **Needs schema** (831K nodes from SNOMED/UMLS) |
| `biolink:Device` | ❌ | — | **Needs schema** (70K nodes from UMLS) |
| `biolink:Disease` | ✅ | disease.yaml | `Disease` |
| `biolink:Drug` | ✅ | drug.yaml | `Drug` |
| `biolink:EnvironmentalFeature` | ❌ | — | **Needs schema** (366K nodes from BERO/ENVO) |
| `biolink:ExperimentalFactor` | ❌ | — | **Needs schema** (77K nodes from EFO) |
| `biolink:Gene` | ✅ | gene.yaml | `Gene` |
| `biolink:GenomicEntity` | ❌ | gene.yaml | Partial: `Transcript` but not generic `GenomicEntity` |
| `biolink:GeographicLocation` | ❌ | — | Low priority (4.7K nodes) |
| `biolink:IndividualOrganism` | ❌ | — | Low priority (7.8K nodes) |
| `biolink:InformationContentEntity` | ❌ | — | **Needs schema** (547K nodes from MeSH/UMLS) |
| `biolink:LifeStage` | ❌ | — | Low priority (372 nodes) |
| `biolink:MolecularActivity` | ✅ | pathway.yaml | `MolecularFunction` |
| `biolink:MolecularEntity` | ❌ | — | Tiny (12 nodes) |
| `biolink:NamedThing` | ✅ | — | BioLink root, no schema needed |
| `biolink:NucleicAcidEntity` | ❌ | — | **Needs schema** (16.8K nodes) |
| `biolink:OntologyClass` | ❌ | — | **NEW: Semantic Network types** (127 nodes) |
| `biolink:OrganismTaxon` | ❌ | — | **Needs schema** (812K nodes) |
| `biolink:Phenomenon` | ❌ | — | Low priority (1.9K nodes) |
| `biolink:PhenotypicFeature` | ✅ | disease.yaml / phenotype.yaml | `PhenotypicFeature` |
| `biolink:PhenotypicQuality` | ✅ | phenotype.yaml | `PhenotypicQuality` |
| `biolink:PopulationOfIndividualOrganisms` | ❌ | — | Low priority (2.4K nodes) |
| `biolink:Procedure` | ❌ | — | **Needs schema** (MAXO + UMLS) |
| `biolink:Protein` | ✅ | gene.yaml | `Protein` |
| `biolink:RelationshipType` | ❌ | — | **NEW: Semantic Network relations** (54 nodes) |
| `biolink:SoftwareOrTool` | ❌ | — | Low priority (SWO, ~100 nodes) |
| `biolink:Activity` | ❌ | — | 12.6K nodes |
| `biolink:Agent` | ❌ | — | 3.1K nodes |
| `biolink:Behavior` | ❌ | — | 2.6K nodes |
| `biolink:BiologicalProcess` | ✅ | pathway.yaml | `Pathway` |

### Gap Summary

| Priority | Missing Schema Classes | Node Count |
|----------|----------------------|------:|
| **High** | ClinicalFinding, ClinicalAttribute, InformationContentEntity | 1.8M |
| **Medium** | OrganismTaxon, EnvironmentalFeature, CellLine, Device | 1.4M |
| **Low** | OntologyClass, RelationshipType, ExperimentalFactor, Procedure, NucleicAcidEntity | 0.1M |
| **Negligible** | GeographicLocation, LifeStage, Phenomenon, etc. | <20K |

### Edge Predicates: 53 in KG vs 0 explicitly defined in schema

> [!WARNING]
> The `CytosAssociation` class has `predicate: range: uriorcurie` but **no enum or validation** of allowed predicates. All 53 predicates from the Semantic Network (biolink:affects, biolink:treats, biolink:causes, etc.) are valid BioLink predicates, but our schema doesn't constrain them.

**Action needed**: Add a `PredicateEnum` or import the BioLink predicate hierarchy.

---

## 2. Provenance Tracking: Current State

### What exists

| Layer | Mechanism | Coverage | Issues |
|-------|-----------|----------|--------|
| **Per-file provenance** | `.provenance.yaml` sidecar | Ontology terms only | Missing for UMLS, SNOMED, KG outputs |
| **Run-level tracking** | `data/provenance/last_run.yaml` | All phases | Overwritten each run, no history |
| **Source checksums** | SHA-256 in `.provenance.yaml` | Ontologies only | Not computed for UMLS/SNOMED Parquets |
| **Version tracking** | `source_version` field | Per ontology | No central manifest |
| **Git commit** | `transform_commit` in provenance | Per ontology | Only records cytos commit, not source data commit |

### What's missing

1. **No UMLS provenance sidecars**: The 10 UMLS Parquet files in `neuro-pheno/data/UMLS/` have no `.provenance.yaml`
2. **No SNOMED provenance sidecars**: SNOMED files similarly lack provenance
3. **No version manifest**: No central `data/versions.yaml` tracking all source versions in one place
4. **No run history**: `last_run.yaml` is overwritten; previous runs are lost
5. **No path stability**: If `neuro-pheno/data/UMLS` moves, the hardcoded fallback in `_find_umls_file()` breaks
6. **No DVC tracking**: Despite planning to use DVC, it's not wired in
7. **No RO-Crate packaging**: The RO-Crate publisher exists in code but isn't invoked

### Path Resolution: Current Logic

```python
def _find_umls_file(self, name: str) -> Path | None:
    # 1. Try staged symlink: staged_dir/umls/{name}.parquet
    # 2. Fallback: /home/mohammadi/repos/cytognosis/neuro-pheno/data/UMLS/{name}.parquet
```

> [!CAUTION]
> The hardcoded fallback path means:
> - Moving `neuro-pheno/data/UMLS/` breaks the pipeline silently
> - No checksums verify the files are the expected versions
> - No provenance tracks *which* UMLS release generated these Parquets

---

## 3. Recommended Actions

### Schema Updates (Priority order)

1. **Create `schemas/domains/clinical.yaml`**: ClinicalFinding, ClinicalAttribute classes
2. **Create `schemas/domains/taxonomy.yaml`**: OrganismTaxon class  
3. **Create `schemas/domains/environment.yaml`**: EnvironmentalFeature, ExperimentalFactor
4. **Create `schemas/domains/semantic_network.yaml`**: OntologyClass, RelationshipType for UMLS SN
5. **Add `PredicateEnum`** to `core.yaml` with all 53 biolink predicates
6. **Add `CellLine`** class to anatomy.yaml or new cell_line.yaml
7. **Add `Device`, `Procedure`** to relevant domain schemas

### Provenance Fixes

1. **Generate provenance sidecars for UMLS/SNOMED** during Parquet conversion
2. **Create `data/versions.yaml`** central manifest:
   ```yaml
   umls: { version: "2026AA", release_date: "2026-05-01", sha256: "..." }
   snomed_int: { version: "20260501", sha256: "..." }
   ```
3. **Append run history** instead of overwriting `last_run.yaml`
4. **Replace hardcoded paths** with `data_sources.yaml` config
5. **Wire DVC**: Track `data/kg/*.tsv` and `data/normalized/` with DVC
6. **Invoke RO-Crate** at export time to package provenance with data

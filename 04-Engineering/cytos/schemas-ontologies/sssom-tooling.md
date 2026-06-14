# SSSOM Tooling for the Cytognosis Scholarly KG

A LinkML-native reference for cross-ontology mapping in the Cytognosis stack,
with single-cell (CELLxGENE) integration patterns and a worked example using
SNOMED CT mappings from OLS4.

- Owner: Cytognosis Foundation Infrastructure & Tooling
- Companion schema: `cytognosis_scholarly_kg_v0.4.0.yaml`
- Last updated: 2026-05-06

---

## 1. Why SSSOM, why LinkML

SSSOM (Simple Standard for Sharing Ontological Mappings) is a tabular,
metadata-rich format for cross-ontology mappings. Each row is a `Mapping`
between a `subject_id` and an `object_id` with an explicit `predicate_id`
(`skos:exactMatch`, `skos:closeMatch`, `owl:equivalentClass`, etc.) plus
provenance: `mapping_justification`, `mapping_tool`, `confidence`,
`creator_id`, `mapping_date`, `license`, and so on.

The schema is itself written in LinkML, so it slots cleanly into the
Cytognosis scholarly KG and codegens to JSON Schema, Pydantic, OWL, SHACL,
and SQL DDL. Adopting SSSOM gives us:

- A single canonical edge type for mappings across UMLS, MONDO, HP, CL, CHEBI,
  NCBITaxon, SNOMED CT, ICD, GO, etc.
- Provenance and confidence on every edge — required for Translator and for
  auditable reasoning.
- Free interop with OAK, Koza, KGX, Boomer, Biomappings, and the wider Mapping
  Commons / Monarch / Translator ecosystems.

---

## 2. The schema itself

`sssom-schema` is the canonical LinkML source for SSSOM.

- Repo: https://github.com/mapping-commons/sssom
- PyPI: `pip install sssom-schema`
- LinkML root: `MappingSet` → `Mapping[]` plus a `MappingRegistry`

Recommended pattern: **import** `sssom-schema` into
`cytognosis_scholarly_kg_v0.4.0.yaml` rather than redefining its classes.
Pin the version in `pyproject.toml` so codegen is deterministic.

```yaml
# cytognosis_scholarly_kg_v0.4.0.yaml (excerpt)
imports:
  - linkml:types
  - sssom_schema:sssom_schema       # via sssom-schema PyPI install
prefixes:
  sssom: https://w3id.org/sssom/
  semapv: https://w3id.org/semapv/vocabulary/
  skos:  http://www.w3.org/2004/02/skos/core#
  pav:   http://purl.org/pav/
  bioregistry: https://bioregistry.io/registry/
classes:
  EntityMapping:
    is_a: Mapping            # inherited from sssom_schema
    description: |
      Cytognosis-side mapping edge. Reuses SSSOM Mapping semantics; adds
      attribution to the ResearchObject / RO-Crate context that produced
      the mapping.
    slot_usage:
      mapping_provider:
        range: ResearchObject
```

This keeps SSSOM rows round-trippable as TSV while letting us attach them to
our `ResearchObject` / RO-Crate provenance.

---

## 3. The Python toolkit: `sssom-py`

Workhorse library and CLI. All major operations are LinkML-aware.

- Repo: https://github.com/mapping-commons/sssom-py
- Install: `pip install sssom`
- CLI entrypoint: `sssom`

What you actually use:

- `MappingSetDataFrame` — pandas wrapper that carries the SSSOM metadata
  header (CURIE map, license, version) alongside the rows.
- Parsers: `parse_sssom_table`, `parse_sssom_json`, `parse_sssom_rdf`.
- Writers: `write_table`, `write_json`, `write_owl`, `write_rdf`.
- Set algebra: `merge_msdf`, `compare_dataframes`, `filter_redundant_rows`.
- Validation: `sssom validate <file>` — runs the LinkML validator against
  `sssom-schema` and reports row-level errors.
- Conversion: `sssom convert -O {tsv,json,owl,rdf,fhir-r4}`.

---

## 4. Ontology Access Kit (OAK / `oaklib`)

The most useful day-to-day tool for *generating* and *operating on* SSSOM.

- Repo: https://github.com/INCATools/ontology-access-kit
- Install: `pip install oaklib`
- CLI: `runoak`

Subcommands you will actually use:

| Command | Purpose |
| --- | --- |
| `runoak lexmatch` | Bootstrap mappings between two ontologies as SSSOM. |
| `runoak diff` | Compare two ontology versions; emit changes as SSSOM. |
| `runoak mappings` | Extract embedded `oboInOwl:hasDbXref` etc. into SSSOM. |
| `runoak validate-mappings` | Cross-check mappings against label evidence. |
| `runoak similarity` | Information-content-based similarity over an ontology. |

Adapters (the `--input` / `-i` argument) cover SQLite, OBO, OWL, SPARQL, OLS,
BioPortal, Ubergraph, Pronto. This is how we'll bridge UMLS / MONDO / HP /
CHEBI / SNOMED into the Cytognosis KG without bespoke loaders.

---

## 5. CURIE and prefix handling

Identifier hygiene matters for SSSOM because subject/object IDs are CURIEs
that must round-trip to IRIs.

- `curies` — https://github.com/biopragmatics/curies — high-performance
  CURIE↔IRI conversion, prefix priority, and converter chaining.
- `prefixmaps` — https://github.com/linkml/prefixmaps — curated context-keyed
  prefix maps (`obo`, `linked_data`, `bioregistry.upper`, ...).
- `bioregistry` — https://bioregistry.io — the canonical registry; drive
  SSSOM CURIE maps from it.

Pattern:

```python
from prefixmaps import load_converter
converter = load_converter("merged")   # bioregistry + obo + sssom defaults
converter.compress("http://purl.obolibrary.org/obo/CL_0000084")  # -> "CL:0000084"
converter.expand("MONDO:0005148")
```

Use the resulting prefix map to populate the `prefixes:` block of
`cytognosis_scholarly_kg_v0.4.0.yaml` and the SSSOM file headers.

---

## 6. Mapping generation

Beyond `runoak lexmatch`:

- **AgreementMakerLight (AML)** — Java ontology matcher; SSSOM export via
  wrappers.
- **LogMap** — OWL ontology matcher; SSSOM export via wrappers.
- **Boomer** — https://github.com/INCATools/boomer — Bayesian probabilistic
  refinement of SSSOM mapping sets. Use when you have noisy, multi-source
  mappings with weighted provenance.
- **SapBERT / BioBERT embeddings** — neural matchers; output formatted via
  `sssom-py` writers.
- **Biomappings** — https://github.com/biopragmatics/biomappings —
  community-curated, semi-automated, SSSOM-native mappings.

---

## 7. KG ingest and Translator alignment

Cytognosis v0.4.0 already targets Translator. The right SSSOM-aware ingest
glue is:

- **Koza** — https://github.com/monarch-initiative/koza — LinkML-native ETL
  framework Monarch uses; consumes SSSOM for entity normalization, emits
  Biolink-compliant KGX.
- **KGX** — https://github.com/biolink/kgx — reads SSSOM for mapping-driven
  node merging.
- **NodeNormalization / Name Resolver** — Translator services that produce
  SSSOM-shaped outputs.

---

## 8. Validation and codegen

- `linkml validate --schema sssom_schema.yaml --target-class MappingSet
  my.sssom.tsv` — schema-level validation independent of `sssom-py`.
- `gen-pydantic`, `gen-json-schema`, `gen-owl`, `gen-shacl`,
  `gen-sqlddl` — codegen targets for downstream services.
- `linkml-map` — https://github.com/linkml/linkml-map — declarative
  class-to-class transforms between schemas. Useful when mapping
  OpenAlex / UMLS / Translator records to SSSOM `Mapping` rows.

---

## 9. Curated SSSOM sources

- Mapping Commons org: https://github.com/mapping-commons
  - `mondo-mappings`, `disease-mappings`, `umls-cui-mappings`,
    `snomed-mondo-mappings`, `cl-uberon-mappings`, `chebi-uniprot-mappings`.
- Biomappings: https://github.com/biopragmatics/biomappings
- OBO ontology repos — most modern OBO ontologies ship a `mappings/` folder
  with SSSOM TSVs.
- OLS4 — every ontology page exposes a Mappings tab with downloadable SSSOM
  TSV (this is the source we use in the worked example below).

---

## 10. Single-cell integration: CELLxGENE + LinkML + SSSOM

### 10.1 How CZI applies its schema

The CZI `single-cell-curation` repo enforces structure via the
`cellxgene-schema` Python CLI. It dictates the structural composition of the
AnnData (`.h5ad`) object — `X` must be a sparse matrix, `var` must contain
specific gene metadata — and enforces semantic standards in the `obs` (cell
metadata) layer. Columns like `cell_type_ontology_term_id`,
`disease_ontology_term_id`, and `organism_ontology_term_id` are validated
against pinned versions of CL, MONDO, and NCBITaxon respectively.

Other portals (ScPCA, BICAN, HCA) align their export pipelines to be
"CELLxGENE compliant" because that guarantees integration with downstream
tools like `scVI` and `celltypist`. Many consortia treat the CZI schema as
the baseline and layer extensions on top for spatial omics or richer disease
metadata.

### 10.2 Reuse vs. LinkML reimplementation

| | Reuse `cellxgene-schema` | Reimplement in LinkML |
| --- | --- | --- |
| Cost | Zero for base schema; one-line CLI validation. | Schema authoring, AnnData wrapper. |
| Structural checks (`X`, `var`, `obsm`) | Native, perfect. | Not native — LinkML doesn't read `.h5ad`. |
| Semantic checks on `obs` | Hard-coded against pinned ontology versions. | Declarative, extensible, codegens to Pydantic/JSON Schema/SHACL/OWL. |
| Internal extensions (clinical, treatment) | Requires a custom fork. | Add slots in `schema.yaml`. |
| Ontology mapping | Manual. | Native via OAK + SSSOM. |
| Integration target | CELLxGENE portal compatibility. | Internal data governance, multi-modal DB, Translator. |

**Recommendation: hybrid.** Use `cellxgene-schema` to validate structural
integrity of the AnnData object. Use **LinkML + OAK + SSSOM** for curation,
harmonization, and metadata validation. This keeps CZI compliance while
giving us declarative extensibility and automated ontology mapping.

### 10.3 Workflows

**A — CZI tools only (today's default):**

1. `pip install cellxgene-schema`.
2. Researchers manually map text labels to ontology IDs in pandas:
   `"T-cell"` → `"CL:0000084"`, `"human"` → `"NCBITaxon:9606"`.
3. `cellxgene-schema validate my_data.h5ad`.
4. On failure, edit pandas, repeat.

**B — LinkML + OAK + SSSOM (recommended hybrid):**

1. Define `CellMetadata` in our LinkML schema with slots like
   `cell_type_ontology_term_id` (range constrained by pattern
   `^CL:[0-9]+$`), `disease_ontology_term_id`, `treatment_group`, etc.
2. Codegen Pydantic.
3. Harmonize free-text metadata with OAK against OLS / BioPortal:

   ```python
   from oaklib import get_adapter
   cl = get_adapter("sqlite:obo:cl")
   cl_id = next(iter(cl.basic_search("T cell")))    # -> "CL:0000084"
   adata.obs["cell_type_ontology_term_id"] = cl_id
   ```

4. Where source data is in another vocabulary (SNOMED CT clinical codes,
   ICD-10, UMLS CUIs), apply an SSSOM mapping table to translate to CZI's
   target ontologies (CL/MONDO/NCBITaxon) — the section below shows this for
   SNOMED → MONDO.
5. Validate `adata.obs.to_dict(orient="records")` through the codegen'd
   Pydantic models. Then run `cellxgene-schema validate` for structural
   checks.

The SSSOM layer is what makes step 4 declarative: instead of bespoke
translation code per source, we attach mapping sets as data, version them,
audit them, and reuse them.

---

## 11. Worked example: loading SNOMED CT SSSOM from OLS4

Every ontology in OLS4 (https://www.ebi.ac.uk/ols4/) has a Mappings tab with
a downloadable SSSOM TSV. SNOMED CT is the densest clinical-terminology
source; mapping it to MONDO/HP/CL is what turns clinical EHR-style metadata
into something CELLxGENE-compliant.

> Note on availability: OLS4 hosts the redistributable SNOMED CT subsets
> (e.g. the GPS / international subset). The exact ontology slug and SSSOM
> URL surface on the ontology's OLS4 page — the URL pattern below is the
> stable shape; check the page if a slug has been versioned.

### 11.1 Download

```bash
# OLS4 SSSOM export endpoint — the same shape works for any OLS4 ontology
mkdir -p data/sssom && cd data/sssom

curl -L -o snomed.sssom.tsv \
  "https://www.ebi.ac.uk/ols4/api/v2/ontologies/snomed/exports/sssom"

# Or, equivalently, the canonical Mapping Commons mirror (often fresher):
# curl -L -o snomed-mondo.sssom.tsv \
#   "https://raw.githubusercontent.com/mapping-commons/snomed-mondo-mappings/main/mappings/snomed-mondo.sssom.tsv"

head -40 snomed.sssom.tsv
```

The TSV begins with a YAML metadata header (lines prefixed with `#`):
`mapping_set_id`, `license`, `mapping_set_version`,
`mapping_provider`, plus the `curie_map`. Columns then follow:
`subject_id`, `subject_label`, `predicate_id`, `object_id`,
`object_label`, `mapping_justification`, `confidence`, …

### 11.2 Load and inspect with `sssom-py`

```python
from sssom.parsers import parse_sssom_table
from sssom.util import MappingSetDataFrame

msdf: MappingSetDataFrame = parse_sssom_table("data/sssom/snomed.sssom.tsv")

# The metadata header (CURIE map, license, version, provenance)
print(msdf.metadata)
print(msdf.prefix_map["SNOMED"])   # e.g. "http://snomed.info/id/"
print(msdf.prefix_map["MONDO"])    # "http://purl.obolibrary.org/obo/MONDO_"

# The dataframe
df = msdf.df
print(df.shape)
print(df.columns.tolist())
# ['subject_id', 'subject_label', 'predicate_id', 'object_id',
#  'object_label', 'mapping_justification', 'confidence', ...]

# Pull exact-match SNOMED -> MONDO rows
exact_to_mondo = df[
    (df["predicate_id"] == "skos:exactMatch")
    & df["object_id"].str.startswith("MONDO:")
]
print(exact_to_mondo.head())
```

### 11.3 Validate against the LinkML schema

```bash
# sssom-py CLI — round-trips through the LinkML validator
sssom validate data/sssom/snomed.sssom.tsv

# Or directly with the LinkML CLI
linkml validate \
  --schema $(python -c "import sssom_schema, os; print(os.path.dirname(sssom_schema.__file__) + '/schema/sssom_schema.yaml')") \
  --target-class MappingSet \
  data/sssom/snomed.sssom.tsv
```

### 11.4 Convert formats / merge with another set

```bash
# To RDF/Turtle for triplestore ingest
sssom convert -O rdf data/sssom/snomed.sssom.tsv \
  -o data/sssom/snomed.sssom.ttl

# Merge with a Mondo-side mapping set
sssom merge data/sssom/snomed.sssom.tsv data/sssom/mondo.sssom.tsv \
  -o data/sssom/clinical-merged.sssom.tsv
```

### 11.5 Apply to a CELLxGENE-bound AnnData

This is where the hybrid pattern from §10 lands:

```python
import anndata as ad
from sssom.parsers import parse_sssom_table

adata = ad.read_h5ad("dataset.h5ad")

# Build a SNOMED -> MONDO exact-match lookup
msdf = parse_sssom_table("data/sssom/snomed.sssom.tsv")
df = msdf.df
exact = df[df["predicate_id"] == "skos:exactMatch"]
snomed_to_mondo = dict(zip(exact["subject_id"], exact["object_id"]))

# Translate clinical SNOMED codes into MONDO IDs for the
# `disease_ontology_term_id` column expected by cellxgene-schema
adata.obs["disease_ontology_term_id"] = (
    adata.obs["snomed_disease_code"]
        .map(lambda s: snomed_to_mondo.get(s))
)

unmapped = adata.obs.loc[
    adata.obs["disease_ontology_term_id"].isna(),
    "snomed_disease_code"
].dropna().unique()
print(f"{len(unmapped)} SNOMED codes without exact MONDO match — escalate "
      f"to OAK lexmatch or curate in biomappings.")

adata.write_h5ad("dataset.harmonized.h5ad")
```

Then run `cellxgene-schema validate dataset.harmonized.h5ad` for the
structural checks CZI does best.

### 11.6 Generalizing to any OLS4 ontology

```bash
for ONT in mondo hp cl ncbitaxon chebi efo go uberon; do
  curl -L -o "data/sssom/${ONT}.sssom.tsv" \
    "https://www.ebi.ac.uk/ols4/api/v2/ontologies/${ONT}/exports/sssom"
done
```

Then iterate `parse_sssom_table` over the directory and merge into a
single `clinical-bridge.sssom.tsv` for the harmonization layer.

---

## 12. Recommended Cytognosis stack

Minimal, LinkML-native, Translator-compatible:

- `sssom-schema` — imported into `cytognosis_scholarly_kg_v0.4.0.yaml`.
- `sssom` (sssom-py) — I/O, validation, set algebra, format conversion.
- `oaklib` — ontology access, lexmatch, mapping extraction.
- `curies` + `prefixmaps` (driven from `bioregistry`) — identifier hygiene.
- `koza` — LinkML-native ETL; consumes SSSOM for normalization; emits KGX.
- `cellxgene-schema` — structural validation of AnnData (hybrid pattern).
- `linkml` — schema validation, codegen (Pydantic/JSON Schema/OWL/SHACL/SQL).
- Optional: `boomer` for probabilistic mapping refinement; `biomappings`
  for community-curated supplementary mappings.

---

## 13. Integration sketch with `cytognosis_scholarly_kg_v0.4.0.yaml`

```yaml
# cytognosis_scholarly_kg_v0.5.0.yaml (proposed delta)
imports:
  - linkml:types
  - sssom_schema:sssom_schema
prefixes:
  sssom: https://w3id.org/sssom/
  semapv: https://w3id.org/semapv/vocabulary/
  skos:  http://www.w3.org/2004/02/skos/core#
  cellxgene: https://cellxgene.cziscience.com/

classes:
  EntityMapping:
    is_a: Mapping
    description: |
      A cross-ontology mapping edge in the Cytognosis KG.
      Reuses SSSOM Mapping; attaches Cytognosis provenance.
    slot_usage:
      mapping_provider:
        range: ResearchObject
      mapping_tool:
        examples:
          - value: "oaklib.runoak.lexmatch"
          - value: "biomappings"
          - value: "manual:cytognosis-curator"

  CellMetadata:
    description: |
      Per-cell semantic metadata, CELLxGENE-compliant baseline plus
      Cytognosis extensions.
    slots:
      - cell_type_ontology_term_id
      - disease_ontology_term_id
      - organism_ontology_term_id
      - tissue_ontology_term_id
      - treatment_group       # Cytognosis extension
      - cohort_id             # Cytognosis extension

slots:
  cell_type_ontology_term_id:
    range: uriorcurie
    pattern: "^CL:[0-9]+$"
    required: true
  disease_ontology_term_id:
    range: uriorcurie
    pattern: "^MONDO:[0-9]+$"
  organism_ontology_term_id:
    range: uriorcurie
    pattern: "^NCBITaxon:[0-9]+$"
  tissue_ontology_term_id:
    range: uriorcurie
    pattern: "^UBERON:[0-9]+$"
```

This gives us one schema that:

- Validates SSSOM mapping sets natively.
- Validates CELLxGENE-bound `obs` records natively.
- Lets a `ResearchObject` (RO-Crate root from v0.4.0) cite the
  `MappingSet`s it depended on via `prov:used` /
  `pav:derivedFrom`, closing the provenance loop.

---

## 14. Open questions / next steps

- Confirm the SNOMED CT subset slug currently published on OLS4 and pin a
  version in our prefix map.
- Decide where SSSOM TSVs live in the Cytognosis Drive — proposed
  `Infrastructure and Tooling/sssom/` mirroring the schema folder.
- Wire `sssom validate` into CI alongside the existing LinkML schema checks.
- Prototype the `EntityMapping` class against a real SNOMED→MONDO load and
  walk the resulting Neo4j graph from a `Paper` node via `mentions →
  Disease → EntityMapping → SNOMED concept`.

# 11 — Open Targets Platform Schemas → LinkML

> **Goal** – take the Open Targets Platform's published schemas and
> produce a LinkML schema that round-trips with their Parquet data.
> **Time** – 60 minutes.
> **Prereqs** – chapters 01, 02, 04 (Biolink). Chapter 15 (BioCypher)
> is what you'll plug this into afterward.

---

## What Open Targets gives you

Open Targets ships data as **Parquet** with embedded schemas (every
Parquet file is self-describing — column names, types, nested structs).
Their docs publish a per-entity reference at
https://platform-docs.opentargets.org.

The major entity tables:

| Table | Entity | Notes |
| --- | --- | --- |
| `targets/` | Gene/protein target | one row per Ensembl ID |
| `diseases/` | Disease | EFO/MONDO ID hub |
| `drug/molecule/` | Drug/compound | ChEMBL-rooted |
| `mechanismOfAction/` | MoA edge | source–target–action |
| `evidence/` | Target–disease evidence | huge; per-source typed |
| `associations/` | Target–disease aggregate | precomputed scores |
| `goldStandardCurated/` | Curated gold standards | benchmarks |

---

## 1. Pull the schemas

```bash
mkdir -p downloads/opentargets
cd downloads/opentargets
# Latest release path (FTP):
curl -L -O "https://ftp.ebi.ac.uk/pub/databases/opentargets/platform/latest/output/etl/parquet/targets/_metadata"
# Each Parquet has its schema; we'll extract programmatically
```

Or grab a sample file:

```bash
# A small partition of `diseases`:
wget -r -np -nH --cut-dirs=8 -A "*.parquet" \
  "https://ftp.ebi.ac.uk/pub/databases/opentargets/platform/latest/output/etl/parquet/diseases/" \
  -P downloads/opentargets/diseases/
```

---

## 2. Extract the Parquet schema

```python
# scripts/ot_schema_to_linkml.py
import sys, json, yaml
import pyarrow.parquet as pq

src = sys.argv[1]                 # path to one parquet file or a dir
out = sys.argv[2]                 # path to LinkML yaml
cls_name = sys.argv[3]            # e.g. "Disease"

schema = pq.read_metadata(src).schema.to_arrow_schema()

def arrow_to_linkml(field):
    t = field.type
    if pa_is_string(t):  return "string"
    if pa_is_int(t):     return "integer"
    if pa_is_float(t):   return "float"
    if pa_is_bool(t):    return "boolean"
    if pa_is_list(t):    return arrow_to_linkml(field.with_type(t.value_type)) + "[]"
    if pa_is_struct(t):  return f"{cls_name}_{field.name.title()}"
    return "string"

import pyarrow as pa
def pa_is_string(t): return pa.types.is_string(t) or pa.types.is_large_string(t)
def pa_is_int(t):    return pa.types.is_integer(t)
def pa_is_float(t):  return pa.types.is_floating(t)
def pa_is_bool(t):   return pa.types.is_boolean(t)
def pa_is_list(t):   return pa.types.is_list(t) or pa.types.is_large_list(t)
def pa_is_struct(t): return pa.types.is_struct(t)

slots = {}
for field in schema:
    rng = arrow_to_linkml(field)
    multivalued = rng.endswith("[]")
    rng = rng.rstrip("[]")
    slots[field.name] = {
        "range": rng,
        "multivalued": multivalued,
        "required": not field.nullable,
    }

doc = {
    "id": f"https://cytognosis.org/schemas/opentargets_{cls_name.lower()}",
    "name": f"opentargets_{cls_name.lower()}",
    "prefixes": {
        "ot":     "https://platform.opentargets.org/",
        "linkml": "https://w3id.org/linkml/",
        "biolink":"https://w3id.org/biolink/",
    },
    "default_prefix": "ot",
    "imports": ["linkml:types", "https://w3id.org/biolink/biolink-model"],
    "classes": {
        cls_name: {
            "is_a": f"biolink:{cls_name}",
            "slots": list(slots),
        }
    },
    "slots": slots,
}
open(out, "w").write(yaml.safe_dump(doc, sort_keys=False))
print(f"Wrote {out}")
```

Run it for each table:

```bash
python scripts/ot_schema_to_linkml.py \
  downloads/opentargets/diseases/part-00000-*.parquet \
  schemas/opentargets/disease.yaml \
  Disease
```

---

## 3. Tidy the result

The auto-generated YAML will have:
- Anonymous nested structs as separate classes (`Disease_Therapeutic`, etc.)
- Snake-case field names from the Parquet
- No descriptions

Pass over it once with these heuristics:

```yaml
# schemas/opentargets/disease.yaml (excerpt, after cleanup)
classes:
  Disease:
    is_a: biolink:Disease
    description: Open Targets aggregated disease record (EFO/MONDO-rooted).
    slot_usage:
      id:
        identifier: true
        pattern: "^(MONDO|EFO|HP|DOID):[0-9]+$"
      name:
        required: true
    slots:
      - id
      - name
      - therapeuticAreas
      - synonyms
      - dbXRefs
      - descendants
      - parents

slots:
  id:
    range: uriorcurie
  name:
    range: string
  therapeuticAreas:
    multivalued: true
    range: string
  synonyms:
    multivalued: true
    range: SynonymRecord       # nested struct -> own class
  dbXRefs:
    multivalued: true
    range: DbXref
```

Lift each repeated nested struct (`SynonymRecord`, `DbXref`) into its own
LinkML class.

---

## 4. Validate

Spot-check a few rows from the actual Parquet against the schema:

```python
import duckdb, json, yaml
from linkml.validator import Validator

schema_path = "schemas/opentargets/disease.yaml"
v = Validator(schema_path, target_class="Disease")

con = duckdb.connect()
for row in con.execute("""
    SELECT * FROM read_parquet('downloads/opentargets/diseases/*.parquet') LIMIT 50
""").fetchall():
    rec = dict(zip(con.description, row))
    rec = {k[0]: v for k, v in zip(con.description, row)}
    report = v.validate(rec)
    if not report.results:
        continue
    print(rec.get("id"), [r.message for r in report.results])
```

> **Checkpoint** – 0 validation errors on a 50-row sample, or all errors
> are diagnosable (almost always: missing pattern on a CURIE column).

---

## 5. Wire into BioCypher

Once you have `schemas/opentargets/{disease,target,drug,evidence}.yaml`:

```yaml
# config/biocypher_config.yaml
biocypher:
  schema_config:
    head_ontology:
      url: schemas/cytognosis/master.yaml     # imports OT subschemas
      root_node: NamedThing
```

```yaml
# config/schema_config.yaml
disease:
  represented_as: node
  preferred_id: mondo
  input_label: ot_disease
  is_a: biolink:Disease

target:
  represented_as: node
  preferred_id: ensembl
  input_label: ot_target
  is_a: biolink:Gene

target to disease association:
  represented_as: edge
  source: target
  target: disease
  is_a: biolink:GeneToDiseaseAssociation
  properties:
    overall_score: float
    datatype_scores: object
```

Then write adapters per chapter 15 against the Parquet files.

---

## 6. Hands-on

1. Download just `diseases/` from OT FTP.
2. Run `ot_schema_to_linkml.py` on one parquet partition.
3. Clean up the output (rename nested structs, tighten patterns).
4. Validate 50 rows and fix any reported issues.
5. Add the YAML to `schemas/cytognosis/master.yaml` imports.

---

## 7. Pitfalls

- **`evidence/` is huge** (>50 GB). Only pull it if you really need
  per-source target–disease evidence. Aggregate `associations/` is
  usually enough for a starter KG.
- **Some columns are arrays of structs** (e.g., `dbXRefs`). The conversion
  script flattens once — re-run with explicit struct handling for
  deeper nesting.
- **Schema can change between releases.** Pin the OT release version
  (e.g., `25.06`) in your downloader; regenerate LinkML on bumps.

---

## Further reading

- OT Platform docs: https://platform-docs.opentargets.org
- OT data schema: https://platform-docs.opentargets.org/data-access/data-schema
- Open Targets BioCypher adapter: https://github.com/biocypher/open-targets

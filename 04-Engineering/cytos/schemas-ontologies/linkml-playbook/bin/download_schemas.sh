#!/usr/bin/env bash
# Downloads every upstream schema this playbook touches into ./downloads/
# Idempotent: re-running just refreshes mtimes.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
DL="$ROOT/downloads"
mkdir -p "$DL"/{schema_org,bioschemas,biolink,sssom,sosa_ssn,cellxgene,opentargets,openalex}

echo "==> schema.org JSON-LD"
curl -L --fail -o "$DL/schema_org/schemaorg-current-https.jsonld" \
  https://schema.org/version/latest/schemaorg-current-https.jsonld

echo "==> Bioschemas profiles (clone repo for full set)"
if [[ ! -d "$DL/bioschemas/specifications" ]]; then
  git clone --depth 1 https://github.com/BioSchemas/specifications "$DL/bioschemas/specifications"
fi

echo "==> Biolink Model"
curl -L --fail -o "$DL/biolink/biolink-model.yaml" \
  https://raw.githubusercontent.com/biolink/biolink-model/master/src/biolink_model/schema/biolink_model.yaml

echo "==> SSSOM schema"
curl -L --fail -o "$DL/sssom/sssom_schema.yaml" \
  https://raw.githubusercontent.com/mapping-commons/sssom/master/src/sssom_schema/schema/sssom_schema.yaml

echo "==> SOSA + SSN (W3C TTL)"
curl -L --fail -o "$DL/sosa_ssn/sosa.ttl" https://www.w3.org/ns/sosa/
curl -L --fail -o "$DL/sosa_ssn/ssn.ttl"  https://www.w3.org/ns/ssn/

echo "==> CZI CELLxGENE schema (markdown source)"
if [[ ! -d "$DL/cellxgene/single-cell-curation" ]]; then
  git clone --depth 1 https://github.com/chanzuckerberg/single-cell-curation \
    "$DL/cellxgene/single-cell-curation"
fi

echo "==> OLS4 SSSOM mappings (full tarball)"
curl -L --fail -o "$DL/sssom/mappings_sssom.tgz" \
  https://ftp.ebi.ac.uk/pub/databases/spot/ols/latest/mappings_sssom.tgz
mkdir -p "$DL/sssom/extracted"
tar -xzf "$DL/sssom/mappings_sssom.tgz" -C "$DL/sssom/extracted"

echo "==> Open Targets Platform metadata (small JSON dictionary; full data via FTP)"
curl -L --fail -o "$DL/opentargets/data-schema.html" \
  https://platform-docs.opentargets.org/data-access/data-schema || true

echo "==> GA4GH: VRS, VA, Phenopackets, Pedigree, Beacon v2"
mkdir -p "$DL/ga4gh"
[[ -d "$DL/ga4gh/vrs" ]] || \
  git clone --depth 1 https://github.com/ga4gh/vrs "$DL/ga4gh/vrs"
[[ -d "$DL/ga4gh/va-spec" ]] || \
  git clone --depth 1 https://github.com/ga4gh/va-spec "$DL/ga4gh/va-spec"
[[ -d "$DL/ga4gh/phenopacket-schema" ]] || \
  git clone --depth 1 https://github.com/phenopackets/phenopacket-schema \
    "$DL/ga4gh/phenopacket-schema"
[[ -d "$DL/ga4gh/pedigree-standard" ]] || \
  git clone --depth 1 https://github.com/ga4gh/pedigree-standard \
    "$DL/ga4gh/pedigree-standard"
[[ -d "$DL/ga4gh/beacon-v2" ]] || \
  git clone --depth 1 https://github.com/ga4gh-beacon/beacon-v2 \
    "$DL/ga4gh/beacon-v2"
[[ -d "$DL/ga4gh/linkml-phenopackets" ]] || \
  git clone --depth 1 https://github.com/cmungall/linkml-phenopackets \
    "$DL/ga4gh/linkml-phenopackets"

echo "==> HDMF / NWB schemas"
mkdir -p "$DL/hdmf"
[[ -d "$DL/hdmf/common" ]] || \
  git clone --depth 1 https://github.com/hdmf-dev/hdmf-common-schema \
    "$DL/hdmf/common"
[[ -d "$DL/hdmf/nwb-schema" ]] || \
  git clone --depth 1 https://github.com/NeurodataWithoutBorders/nwb-schema \
    "$DL/hdmf/nwb-schema"

echo "==> Done. Inspect $DL"

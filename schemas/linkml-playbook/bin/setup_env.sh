#!/usr/bin/env bash
# Bootstraps the environment used in the LinkML + KG Playbook.
# Assumes Python 3.11+ is active (uv venv or conda env).
set -euo pipefail

echo "==> Core LinkML + schema importers"
pip install \
  "linkml>=1.7" \
  "linkml-runtime>=1.7" \
  "linkml-map" \
  "schemasheets" \
  "schema-automator"

echo "==> SSSOM + ontology access"
pip install \
  "sssom>=0.4" \
  "sssom-schema" \
  "oaklib>=0.6" \
  "curies" \
  "prefixmaps" \
  "bioregistry"

echo "==> KG frameworks"
pip install \
  "biocypher>=0.7" \
  "koza>=0.6" \
  "kgx" \
  "bmt"

echo "==> Single-cell"
pip install \
  "anndata>=0.10" \
  "cellxgene-schema>=5.2" \
  "scanpy"

echo "==> Source parsers"
pip install \
  "pyalex" \
  "bibtexparser" \
  "rdflib" \
  "pyyaml" \
  "pandas" \
  "duckdb" \
  "linkml-renderer"

echo "==> BioThings (APIs + JSON-LD schema engine)"
pip install \
  "biothings-client" \
  "biothings-schema"

echo "==> GA4GH (VRS Pydantic + Phenopackets Protobuf bindings + LinkML port)"
pip install \
  "ga4gh-vrs" \
  "phenopackets" \
  "linkml-phenopackets"

echo "==> HDMF / NWB stack"
pip install \
  "hdmf" \
  "pynwb" \
  "hdmf-zarr" \
  "nwbinspector" \
  "linkml-arrays"

echo "==> Verifying CLIs"
for cmd in linkml-validate runoak sssom koza cellxgene-schema; do
  if ! command -v "$cmd" >/dev/null 2>&1; then
    echo "!! $cmd not on PATH" >&2
    exit 1
  fi
done

echo "==> Done. You're ready."

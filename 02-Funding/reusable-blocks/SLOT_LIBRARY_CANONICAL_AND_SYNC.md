# Slot Library: Canonical Source, Render Engine, and Sync Rule

> **Status:** Active · **Date:** 2026-07-16 · **Author:** Shahin Mohammadi · **Tags:** `funding`, `slot-library`, `cytos`

**If you only read one thing:** the **docs** slot-library is the authoring source of truth; the copy inside **cytos** is the code-consumed mirror. Keep them in sync (docs to cytos), and verify with the cytos parser.

## Canonical map

| Role | Location |
|---|---|
| Authoring source of truth (slots, funders, manifest, opportunity map) | `docs/02-Funding/reusable-blocks/slot-library/` |
| Code-consumed mirror (loaded by the engine) | `cytos/src/cytos/scholarly/funding/schemas/` |
| Render / parse engine | `cytos/src/cytos/scholarly/funding/` (`parser.py`, `extractor.py`, `harmonizer.py`, `generator.py`, `render.py`, `registry.py`) |
| CLI | `cytos funding parse` (and `--criticmarkup`); nox session `parse_grants` |
| Raw parsed solicitations (source corpus) | `cytos/data/staged/grants/` (ARPA-H mission_office_isos + programs, NSF Tech Labs, NSF X-Labs, DOE Genesis) |
| Funder-metadata / values companions | `docs/02-Funding/reusable-blocks/{funder_metadata.md,funder_crosswalk_matrix.md}` |

## Counts of record (docs source, 2026-07-16)

- **27 slots** (22 universal U01-U22 + 5 administrative A01-A05).
- **10 funder configs** on disk = `funders/*.yaml` (heilmeier baseline + 9 real funders).
- **38 funder-metadata fields** (F01-F38); **12 funder kinds**; **71 opportunities** mapped.

## Drift record (2026-07-16)

Compared `cytos/.../schemas/` against the docs source:

- `opportunity_mapping.yaml`, `opportunity_mapping.csv`, `groups.yaml`: **IDENTICAL**.
- `manifest.yaml`: **DIFFERS**. cytos (last updated 2026-05-24) registers **6 extra funders** that the docs source does not: `nsf_xlabs`, `nsf_sbir_phase1`, `nsf_sbir_phase2`, `nsf_sbir_phase2b`, `nih_r21`, `arpah_program_iso`. Neither side has the matching `funders/*.yaml` files yet, so these are aspirational registry entries.

## Decisions and follow-ups

1. **Adopt the 6 extra registry entries into the docs source** (they are real future funders), then re-sync docs to cytos so both `manifest.yaml` match. Do this rather than dropping them from cytos.
2. **Build the 6 missing funder configs.** Priority: `arpah_program_iso` (feeds the precision-psychiatry Mission Office ISO build) and `nsf_xlabs`.
3. **Relabel `yc_nonprofit`**: YC Summer 2026 is a for-profit PBC, so the id/name is misleading; plan a careful rename across `manifest.yaml`, `funders/`, and `opportunity_mapping` (touches multiple references, do as one atomic change).
4. **Validation caveat:** `manifest.yaml` sets `require_all_funder_files: true`; once the 6 entries are adopted, either build the files or mark those entries `planned: true` so validation passes.

## Sync rule (going forward)

- The docs source is authoritative. After any change to the docs `slot-library/{manifest.yaml,opportunity_mapping.*,groups.yaml}`, copy those files into `cytos/src/cytos/scholarly/funding/schemas/`, then run `nox -s parse_grants` in the cytos repo to confirm the engine loads them. Commit the cytos change separately in the cytos repo as Shahin Mohammadi.
- Never edit the cytos mirror directly for content; edit the docs source and sync.

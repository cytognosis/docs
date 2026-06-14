> **Status**: Active
> **Date**: 2026-06-14
> **Author**: @mohammadi
> **Audience**: engineers
> **Tags**: `cytoplex`, `cap`, `refactor`

# Refactoring Notes

## What Changed

- Moved implementation modules into `src/cap_protocol`.
- Preserved legacy top-level commands as thin wrappers.
- Kept `schemas/` and `policies/` as top-level canonical artifacts.
- Added packaging metadata, console scripts, dev dependencies, tests, and developer documentation.
- Removed runtime package installation from model helpers; real-model dependencies are now explicit setup work.
- Moved protobuf regeneration into `scripts/generate_proto.py`.

## Compatibility

These commands remain supported:

```bash
python run_final_cap.py --target both
python run_production_hardening.py
python VERIFY_FINAL_PACKAGE.py
python reference_grpc/run_demo.py
python second_http/run_demo.py
```

New preferred installed commands:

```bash
cap-run-final --target both
cap-run-hardening
cap-verify-package
cap-check-v1-schema-drift
```

## Known Risks

- External code importing old top-level implementation modules should move to `cap_protocol.*` imports.
- gRPC generated protobuf files must retain package-relative imports after regeneration.
- Colab and Modal workflows rely on top-level wrappers; keep them when changing CLI internals.
- Real-model mode now fails fast when optional model packages are missing instead of installing them at runtime.

## Removed Generated Artifacts

Only generated/noise files were removed: `.DS_Store`, `__pycache__/`, and local `runtime_data/` output.

> **Status**: Pending human approval
> **Date**: 2026-06-21
> **Author**: @shahin
> **Audience**: Shahin (decision-maker)
> **Tags**: `yar`, `hygiene`, `cleanup`

# Yar Research Hygiene: Low-Priority Cleanup

These items require explicit approval before execution. No files have been moved or deleted.

## Awaiting Shahin Approval

- [ ] **Move v3 files to `_archive/`** -- Awaiting Shahin approval.
  - `03-Products/Cytonome/Yar/research/yar-unified-feature-comparison-v3.md`
  - `04-Engineering/yar/research/yar-unified-feature-comparison-v3.md`
  Both are now banner-marked as superseded. Physically archiving them removes clutter from the active research listing.

- [ ] **Collapse duplicate master to a symlink** -- Awaiting Shahin approval.
  `03-Products/Cytonome/Yar/yar-master-features-requirements.md` is byte-identical to `yar-product-feature-master.md`. Replace it with a symlink pointing to the canonical file so there is only one editable copy.

- [ ] **Rename `substrate_interop.py` in the codebase** -- Awaiting Shahin approval.
  The filename uses the retired term "substrate". Rename to remove that term (proposed name: `layer_interop.py` or `foundation_interop.py`; confirm preferred replacement before executing).

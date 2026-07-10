> [!NOTE]
> This is the **source of record** for the science and technology behind the IGoR proposal: the external methods landscape and our key contributions as expressed across proposal variants. It is compiled from modular section files in `sections/` by `build.py`. Edit the section files, not this compiled output.

> [!CAUTION]
> **Restricted sections** (the proprietary factorization method, a perturbation model under review, and the Phase I personal-genomic anchor) appear only in the `internal` build. The `shareable` build drops proprietary, personal, and internal-decision sections; treat it as an internal working draft and review it before any external or partner use, and mark proprietary pages "Proprietary" in any ARPA-H submission.

**How to build:** `python build.py --all` produces both profiles in markdown and PDF. Use `--profile shareable` for the partner-safe version. PDF rendering uses pandoc with weasyprint; diagrams are embedded as figure images from `../figures/` so they render in both markdown and PDF.

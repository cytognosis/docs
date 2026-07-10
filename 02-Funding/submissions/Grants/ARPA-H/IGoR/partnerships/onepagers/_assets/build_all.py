#!/usr/bin/env python3
"""Compile every top-level *.md one-pager in this folder to PDF and DOCX.

Each one-pager is a standalone markdown file (tailored per recipient), so there
is no manifest. Files whose names start with "_" are skipped. Output PDFs and
DOCX land next to the sources. Uses pandoc + weasyprint with the shared CSS.

Usage:
  python3 _assets/build_all.py            # build all
  python3 _assets/build_all.py SIFT       # build only files matching a substring
  python3 _assets/build_all.py --no-docx
"""
import subprocess
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
CSS = Path(__file__).resolve().parent / "pdf.css"


def main():
    args = [a for a in sys.argv[1:]]
    no_docx = "--no-docx" in args
    filters = [a for a in args if not a.startswith("--")]
    mds = sorted(p for p in BASE.glob("*.md") if not p.name.startswith("_"))
    if filters:
        mds = [p for p in mds if any(f.lower() in p.name.lower() for f in filters)]
    if not mds:
        print("no matching markdown files")
        return
    for md in mds:
        pdf = md.with_suffix(".pdf")
        cmd = ["pandoc", str(md), "-o", str(pdf), "--pdf-engine=weasyprint"]
        if CSS.exists():
            cmd += ["-c", str(CSS)]
        r = subprocess.run(cmd, capture_output=True, text=True)
        print(f"[pdf] {pdf.name}" if pdf.exists() else f"[pdf] FAILED {md.name}\n" + r.stderr[-1200:])
        if not no_docx:
            docx = md.with_suffix(".docx")
            r = subprocess.run(["pandoc", str(md), "-o", str(docx)], capture_output=True, text=True)
            print(f"[docx] {docx.name}" if docx.exists() else f"[docx] FAILED {md.name}")


if __name__ == "__main__":
    main()

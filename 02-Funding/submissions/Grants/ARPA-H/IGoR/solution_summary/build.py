#!/usr/bin/env python3
"""Compile a deliverable (one-pager, Solution Summary, full proposal) from modular sections.

Clean output: concatenates section files in manifest order, with no auto-generated
index or profile banner (unlike the research master build). Emits markdown, PDF
(pandoc + weasyprint), and optionally DOCX. Reusable across the deliverable folders.

Usage:
  python3 build.py                 # default profile -> md + pdf + docx
  python3 build.py --profile shareable
  python3 build.py --no-docx
"""
import argparse
import json
import subprocess
from pathlib import Path

BASE = Path(__file__).resolve().parent
TPL = BASE / "_template"
SECT = BASE / "sections"


def load():
    return json.loads((TPL / "manifest.json").read_text())


def assemble(m, profile):
    secs = m["sections"]
    if profile == "shareable":
        secs = [s for s in secs if not s.get("restricted")]
    parts, missing = [], []
    for s in secs:
        f = SECT / s["file"]
        if f.exists():
            parts.append(f.read_text().strip())
        else:
            missing.append(s["file"])
    return "\n\n".join(parts) + "\n", missing


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--profile", default="default")
    ap.add_argument("--no-pdf", action="store_true")
    ap.add_argument("--no-docx", action="store_true")
    a = ap.parse_args()
    m = load()
    md, missing = assemble(m, a.profile)
    base = m.get("output_basename", "deliverable")
    suffix = "" if a.profile in ("default", "internal") else f"_{a.profile}"
    out_md = BASE / f"{base}{suffix}.md"
    out_md.write_text(md)
    print(f"[md] {out_md.name} ({md.count(chr(10))} lines)")
    if missing:
        print("[warn] missing sections:", ", ".join(missing))
    css = TPL / "pdf.css"
    if not a.no_pdf:
        pdf = BASE / f"{base}{suffix}.pdf"
        cmd = ["pandoc", str(out_md), "-o", str(pdf), "--pdf-engine=weasyprint"]
        if css.exists():
            cmd += ["-c", str(css)]
        r = subprocess.run(cmd, capture_output=True, text=True)
        print(f"[pdf] {pdf.name}" if pdf.exists() else "[pdf] FAILED\n" + r.stderr[-1500:])
    if not a.no_docx:
        docx = BASE / f"{base}{suffix}.docx"
        r = subprocess.run(["pandoc", str(out_md), "-o", str(docx)], capture_output=True, text=True)
        print(f"[docx] {docx.name}" if docx.exists() else "[docx] FAILED\n" + r.stderr[-1500:])


if __name__ == "__main__":
    main()

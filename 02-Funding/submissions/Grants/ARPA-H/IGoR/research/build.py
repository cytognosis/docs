#!/usr/bin/env python3
"""Compile the IGoR research master from modular section files.

Content lives in sections/ (one file per section). Structure and metadata live
in _template/manifest.json and _template/master_head.md. This separation lets us
edit content without touching the template, then compile to markdown and PDF.

Profiles:
  internal   - all sections, including restricted (proprietary / personal). Do not distribute.
  shareable  - excludes restricted sections; safe basis for partner-facing and public text.

Usage:
  python build.py                          # internal, markdown only
  python build.py --profile shareable      # exclude restricted sections
  python build.py --pdf                     # also emit PDF (pandoc + weasyprint)
  python build.py --profile shareable --pdf
  python build.py --all                     # build both profiles, md + pdf
"""
import argparse
import json
import subprocess
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent
TPL = BASE / "_template"
SECT = BASE / "sections"


def load_manifest():
    return json.loads((TPL / "manifest.json").read_text())


def build_markdown(m, profile):
    secs = m["sections"]
    if profile == "shareable":
        secs = [s for s in secs if not s.get("restricted")]
    p = []
    p.append(f"# {m['title']}\n")
    if m.get("subtitle"):
        p.append(f"**{m['subtitle']}**\n")
    note = ("excludes restricted sections" if profile == "shareable"
            else "includes restricted sections, do not distribute")
    p.append(f"Compiled {m.get('date','')} | Profile: **{profile}** ({note})\n")
    head = TPL / "master_head.md"
    if head.exists():
        p.append(head.read_text().strip() + "\n")
    p.append("## Section index\n")
    for s in secs:
        tag = " `restricted`" if s.get("restricted") else ""
        p.append(f"- [{s['title']}](sections/{s['file']}){tag}")
    p.append("")
    missing = []
    for s in secs:
        f = SECT / s["file"]
        p.append("\n---\n")
        if f.exists():
            p.append(f.read_text().strip() + "\n")
        else:
            missing.append(s["file"])
            p.append(f"## {s['title']}\n\n> [!NOTE]\n> Section `sections/{s['file']}` not yet authored.\n")
    return "\n".join(p), missing


def to_pdf(md_path, pdf_path, title):
    css = TPL / "pdf.css"
    cmd = ["pandoc", str(md_path), "-o", str(pdf_path),
           "--pdf-engine=weasyprint", "--toc", "--toc-depth=2",
           "--metadata", f"title={title}"]
    if css.exists():
        cmd += ["-c", str(css)]
    r = subprocess.run(cmd, capture_output=True, text=True)
    ok = r.returncode == 0 and pdf_path.exists()
    if not ok:
        print("[pdf] FAILED:\n" + (r.stderr or r.stdout)[-2000:])
    return ok


def build_profile(m, profile, pdf):
    md, missing = build_markdown(m, profile)
    suffix = "" if profile == "internal" else "_shareable"
    out_md = BASE / f"IGoR_Research_Master{suffix}.md"
    out_md.write_text(md)
    print(f"[md] {out_md.name} ({md.count(chr(10))} lines)")
    if missing:
        print(f"[warn] {len(missing)} section(s) not yet authored: {', '.join(missing)}")
    if pdf:
        if to_pdf(out_md, BASE / f"IGoR_Research_Master{suffix}.pdf", m["title"]):
            print(f"[pdf] IGoR_Research_Master{suffix}.pdf")
        else:
            return False
    return True


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--profile", choices=["internal", "shareable"], default="internal")
    ap.add_argument("--pdf", action="store_true")
    ap.add_argument("--all", action="store_true", help="build both profiles, md + pdf")
    a = ap.parse_args()
    m = load_manifest()
    if a.all:
        ok = build_profile(m, "internal", True) and build_profile(m, "shareable", True)
    else:
        ok = build_profile(m, a.profile, a.pdf)
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()

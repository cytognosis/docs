#!/usr/bin/env python3
"""Cytognosis Master Catalog builder. Re-runnable. Walks docs repo + projects,
records every file with inferred group/type/variant + parsed header metadata.
Does NOT follow symlinks (project _context/ mirrors the docs repo)."""
import os, re, csv, json, datetime

HOME = os.path.expanduser("~")
DOCS = os.path.join(HOME, "repos/cytognosis/docs")
PROJECTS = os.path.join(HOME, "Claude/Projects")
OUT_TSV = os.path.join(DOCS, "06-Operations/inventory/catalog.tsv")
OUT_JSON = os.path.join(DOCS, "06-Operations/inventory/catalog-summary.json")

PRUNE = {".git","node_modules",".venv","venv","__pycache__",".obsidian","site",
         "site_docs","dist","build",".mypy_cache",".ruff_cache",".pytest_cache",
         "_safety-archives",".cache",".idea",".vscode"}

PREFIX_TYPE = [("ADR-","adr"),("MODULE-","module-spec"),("RFC-","rfc"),("EVAL-","evaluation"),
    ("SYSTEM-","system-doc"),("STANDARDS-","standards-inventory"),("ARCHITECTURE-","architecture"),
    ("API-","api-reference"),("DEPLOY-","deployment-runbook"),("SOP-","operational-sop"),
    ("GRANT-","grant-section"),("FUND-","funding-profile"),("MEETING-","meeting-notes"),
    ("DECISIONS-","decision-log"),("QUICKREF-","quick-reference"),("MODEL-CARD-","model-card"),
    ("TROUBLESHOOT-","troubleshooting")]
EXACT_TYPE = {"README.md":"readme","CITATION.cff":"citation","CHANGELOG.md":"changelog",
    "metadata.json":"croissant-data-card"}

def infer_type(fn, section):
    if fn in EXACT_TYPE: return EXACT_TYPE[fn]
    up = fn.upper()
    for pre,t in PREFIX_TYPE:
        if up.startswith(pre): return t
    low = fn.lower()
    if low.endswith(".csv"): return "data-table"
    if low.endswith((".mmd",".png",".svg")): return "diagram/asset"
    if low.endswith((".yaml",".yml",".json")): return "config/schema"
    if low.endswith((".py",".sh",".js",".css")): return "code"
    sec = (section or "").lower()
    if "research" in sec: return "research"
    if "funding" in sec: return "funding"
    if "strategy" in sec: return "strategy"
    if "product" in sec: return "product-spec"
    if "engineering" in sec: return "engineering"
    if "design" in sec: return "design"
    if "operations" in sec: return "operations"
    return "other"

def infer_variant(path, fn):
    low = fn.lower(); p = path.lower()
    for suf,v in [(".technical.md","technical"),(".readable.md","readable"),
                  (".agent.md","agent"),(".simple.md","simple")]:
        if low.endswith(suf): return v
    if low.endswith("_prompt.md"): return "agent"
    if "/_archive/" in p or "/archive/" in p: return "archive"
    if "/adhd/" in p: return "readable"
    if "/simple/" in p: return "simple"
    return "primary"

hdr_status = re.compile(r'^>\s*\*\*Status\*\*:\s*(.+)$', re.I)
hdr_date   = re.compile(r'^>\s*\*\*Date\*\*:\s*(.+)$', re.I)
hdr_tags   = re.compile(r'^>\s*\*\*Tags\*\*:\s*(.+)$', re.I)
h1         = re.compile(r'^#\s+(.+)$')

def parse_head(fp):
    status=date=tags=title=""
    try:
        with open(fp,"r",encoding="utf-8",errors="replace") as f:
            head=f.read(4096)
    except Exception:
        return status,date,tags,title
    for ln in head.splitlines()[:25]:
        if not title:
            m=h1.match(ln)
            if m: title=m.group(1).strip()[:120]
        if not status:
            m=hdr_status.match(ln);  status=m.group(1).strip() if m else status
        if not date:
            m=hdr_date.match(ln);    date=m.group(1).strip() if m else date
        if not tags:
            m=hdr_tags.match(ln);    tags=m.group(1).strip().replace("`","")[:160] if m else tags
    return status,date,tags,title

def walk(root_dir, root_label):
    rows=[]
    for dirpath,dirnames,filenames in os.walk(root_dir, followlinks=False):
        dirnames[:] = [d for d in dirnames if d not in PRUNE]
        rel = os.path.relpath(dirpath, root_dir)
        section = "(root)" if rel=="." else rel.split(os.sep)[0]
        for fn in filenames:
            fp=os.path.join(dirpath,fn)
            is_link=os.path.islink(fp)
            tgt=""
            if is_link:
                try: tgt=os.readlink(fp)
                except Exception: tgt="?"
            ext=fn.rsplit(".",1)[-1].lower() if "." in fn else ""
            try: size_kb = 0 if is_link else round(os.path.getsize(fp)/1024,1)
            except Exception: size_kb=0
            status=date=tags=title=""
            if not is_link and ext=="md":
                status,date,tags,title=parse_head(fp)
            rows.append(dict(root=root_label, section=section,
                doc_type=infer_type(fn,section), variant=infer_variant(fp,fn),
                symlink=("yes" if is_link else "no"), symlink_target=tgt,
                size_kb=size_kb, status=status, date=date, tags=tags,
                title=title, path=os.path.relpath(fp,HOME)))
    return rows

rows=[]
rows+=walk(DOCS,"docs")
if os.path.isdir(PROJECTS):
    for name in sorted(os.listdir(PROJECTS)):
        if name.startswith(".") or name in PRUNE: continue
        pd=os.path.join(PROJECTS,name)
        if os.path.isdir(pd): rows+=walk(pd,f"project:{name}")

cols=["root","section","doc_type","variant","symlink","symlink_target","size_kb","status","date","tags","title","path"]
with open(OUT_TSV,"w",newline="",encoding="utf-8") as f:
    w=csv.DictWriter(f,fieldnames=cols,delimiter="\t"); w.writeheader()
    for r in rows: w.writerow(r)

def tally(key, flt=lambda r:True):
    d={}
    for r in rows:
        if flt(r): d[r[key]]=d.get(r[key],0)+1
    return dict(sorted(d.items(), key=lambda x:-x[1]))

summary=dict(generated=datetime.date.today().isoformat(), total_files=len(rows),
    non_symlink=sum(1 for r in rows if r["symlink"]=="no"),
    symlinks=sum(1 for r in rows if r["symlink"]=="yes"),
    by_root=tally("root"),
    docs_by_section=tally("section", lambda r:r["root"]=="docs"),
    by_doc_type=tally("doc_type"),
    by_variant=tally("variant"),
    md_with_std_header=sum(1 for r in rows if r["path"].endswith(".md") and r["status"]),
    md_total=sum(1 for r in rows if r["path"].endswith(".md") and r["symlink"]=="no"))
with open(OUT_JSON,"w",encoding="utf-8") as f: json.dump(summary,f,indent=2)

OUT_TABLES = os.path.join(DOCS, "06-Operations/inventory/catalog-tables.md")
def md_table(title, d, cols=("Key","Count"), limit=None):
    items=list(d.items())[:limit] if limit else list(d.items())
    out=[f"### {title}","",f"| {cols[0]} | {cols[1]} |","|---|---:|"]
    out+= [f"| {k} | {v} |" for k,v in items]
    return "\n".join(out)+"\n"
with open(OUT_TABLES,"w",encoding="utf-8") as f:
    f.write(f"<!-- AUTO-GENERATED by build_catalog.py on {summary['generated']}. Do not edit by hand; re-run the script. -->\n\n")
    f.write(f"Total files tracked: **{summary['total_files']}** (non-symlink {summary['non_symlink']}, symlinks {summary['symlinks']}). Standardized headers: **{summary['md_with_std_header']}/{summary['md_total']}** markdown files.\n\n")
    f.write(md_table("By root (home of record vs project workspaces)", summary["by_root"])+"\n")
    f.write(md_table("Docs repo by section", summary["docs_by_section"])+"\n")
    f.write(md_table("By document type", summary["by_doc_type"])+"\n")
    f.write(md_table("By variant", summary["by_variant"])+"\n")

print("TOTAL rows:",len(rows),"| non-symlink:",summary["non_symlink"],"| symlinks:",summary["symlinks"])
print("BY ROOT:",json.dumps(summary["by_root"]))
print("DOCS BY SECTION:",json.dumps(summary["docs_by_section"]))
print("BY VARIANT:",json.dumps(summary["by_variant"]))
print("TOP DOC TYPES:",json.dumps(dict(list(summary["by_doc_type"].items())[:12])))
print("MD standardized header:",summary["md_with_std_header"],"/",summary["md_total"])
print("Wrote:",OUT_TSV)

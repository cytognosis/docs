#!/usr/bin/env python3
"""Convert ARPA-H ISO PDFs to properly structured markdown.

v3: Fixes TOC leakage, section-title echo, criterion splitting,
    lettered item handling, and CONFORMING/NON-CONFORMING blocks.
"""

import re
import fitz
from pathlib import Path

INPUT_DIR = Path(
    "/home/mohammadi/repos/cytognosis/strategy/input/grants"
    "/ARPA-H - Mission Office ISOs"
)
OUTPUT_DIR = Path(
    "/home/mohammadi/repos/cytognosis/strategy/output/templates/raw"
)


# ── Configuration ───────────────────────────────────────────────────────────

HSF = {
    "pdf": "HSF_MO_ISO_AMEND_3.pdf",
    "out": "arpah_hsf_iso_v2.md",
    "sol": "ARPA-H-SOL-24-104",
    "title": (
        "ARPA-H Health Science Futures (HSF) Mission Office "
        "Innovative Solutions Opening (ISO)"
    ),
    "short": "Health Science Futures (HSF)",
    "mission_acronyms": [("HSF", "Health Science Futures")],
}

PHO = {
    "pdf": "PHO_MO_ISO_AMEND_3.pdf",
    "out": "arpah_pho_iso_v2.md",
    "sol": "ARPA-H-SOL-24-106",
    "title": (
        "ARPA-H Proactive Health Office (PHO) Mission Office "
        "Innovative Solutions Opening (ISO)"
    ),
    "short": "Proactive Health Office (PHO)",
    "mission_acronyms": [
        ("PHO", "Proactive Health Office"),
        ("RSO", "Resilient Systems Office"),
    ],
}

# ── Shared data ─────────────────────────────────────────────────────────────

ACRONYMS = [
    ("AO", "Agreements Officer"),
    ("API", "Application Programming Interface"),
    ("ARPA-H", "Advanced Research Projects Agency for Health"),
    ("ASR", "Animal Subjects Research"),
    ("CFR", "Code of Federal Regulations"),
    ("CHIPS", "Creating Helpful Incentives to Produce Semiconductors"),
    ("COC", "Conflict of Commitment"),
    ("COI", "Conflict of Interest"),
    ("CUI", "Controlled Unclassified Information"),
    ("FAR", "Federal Acquisition Regulation"),
    ("FCOC", "Foreign Country of Concern"),
    ("FHIR", "Fast Healthcare Interoperability Resources"),
    ("FFRDC", "Federally Funded Research and Development Center"),
    ("FOIA", "Freedom of Information Act"),
    ("GDS", "Genomic Data Sharing"),
    ("HHS", "Health and Human Services"),
    ("HSR", "Human Subjects Research"),
    ("IP", "Intellectual Property"),
    ("ISO", "Innovative Solutions Opening"),
    ("IT", "Information Technology"),
    ("MFTRP", "Malign Foreign Talent Recruitment Program"),
    ("NDA", "Non-Disclosure Agreement"),
    ("OCI", "Organizational Conflict of Interest"),
    ("ONC", "Office of the National Coordinator for Health Information Technology"),
    ("OSI", "Open Systems Interconnection"),
    ("OT", "Other Transaction"),
    ("PII", "Personally Identifiable Information"),
    ("Q&As", "Questions and Answers"),
    ("R&D", "Research and Development"),
    ("SAM", "System for Award Management"),
    ("TEFCA", "Trusted Exchange Framework and Common Agreement"),
    ("UEI", "Unique Entity Identifier"),
    ("U.S.", "United States"),
    ("U.S.C", "United States Code"),
]

HYPERLINKS = [
    ("2.2", "42 U.S.C. § 290c(g)(1)(D)",
     "https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title42-section290c&num=0&edition=prelim"),
    ("2.3", "ARPA-H's public website",
     "https://arpa-h.gov/explore-funding/open-funding-opportunities"),
    ("2.3", "SAM.gov",
     "https://sam.gov/content/home"),
    ("2.4", "National Archives (CUI Registry)",
     "https://www.archives.gov/cui/registry/category-list"),
    ("3.2", "ARPA-H's Solution Submission Portal",
     "https://solutions.arpa-h.gov/Ask-A-Question/"),
    ("3.4", "CHIPS and Science Act of 2022",
     "https://www.govinfo.gov/content/pkg/PLAW-117publ167/pdf/PLAW-117publ167.pdf"),
    ("3.4", "50 U.S.C. § 3059",
     "https://uscode.house.gov/view.xhtml?req=(title:50%20section:3059%20edition:prelim)"),
    ("4.2", "ARPA-H's Solution Submission Portal",
     "https://solutions.arpa-h.gov/Ask-A-Question/"),
    ("4.3", "SAM.gov",
     "https://sam.gov/content/home"),
    ("4.4", "ARPA-H's Solution Submission Portal",
     "https://solutions.arpa-h.gov/Ask-A-Question/"),
    ("6.1", "32 CFR § 2002 (CUI)",
     "https://www.ecfr.gov/current/title-32/subtitle-B/chapter-XX/part-2002"),
    ("6.1", "45 CFR § 46 (HSR)",
     "https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-A/part-46"),
    ("6.1", "Office of Human Research Protection",
     "https://www.hhs.gov/ohrp/index.html"),
    ("6.1", "21 CFR § 56",
     "https://www.ecfr.gov/current/title-21/chapter-I/subchapter-A/part-56"),
    ("6.1", "Animal Welfare Act",
     "https://www.nal.usda.gov/animal-health-and-welfare/animal-welfare-act"),
    ("6.1", "PHS Policy on Laboratory Animals",
     "https://olaw.nih.gov/policies-laws/phs-policy.htm"),
    ("6.1", "NSPM-33",
     "https://www.nsf.gov/bfa/dias/policy/nspm-33-implementation-guidance"),
    ("6.1", "Payment Management Services",
     "https://pms.psc.gov/"),
    ("6.1", "ARPA-H Q&A / Resources",
     "https://arpa-h.gov/explore-funding/submission-resources-and-FAQs"),
]

SECTION_TITLES = {
    "1.0": "Innovative Solutions Opening Solicitation Overview Information",
    "2.0": "Description of the Solicitation",
    "2.1": "Introduction",
    "2.2": "Acquisition Strategy",
    "2.3": "Solicitation Procedures",
    "2.4": "Award Information",
    "3.0": "Eligibility Information",
    "3.1": "Eligible Proposers",
    "3.2": ("Prohibition of Performer Participation from Federally Funded "
            "Research and Development Centers (FFRDCs) and Government Entities"),
    "3.3": "Current Professional Support",
    "3.4": "Non-U.S. Organizations",
    "4.0": "Solution Summary and Proposal Preparation and Submission Information",
    "4.1": "Solution Summary Preparation",
    "4.2": "Solution Summary Submissions",
    "4.3": "SAM.gov Information",
    "4.4": "Proposal Submission Information",
    "4.5": "Solution Summary and Proposal Submission Deadlines",
    "4.6": "Proprietary Information",
    "5.0": "Solution Summary Review and Evaluation of Proposals",
    "5.1": "Solution Summary Review Process",
    "5.2": "Evaluation Criteria for Award",
    "5.3": "Review and Selection Process",
    "5.4": "Notices",
    "5.5": "Handling of Selection Sensitive Information",
    "6.0": "Award Administration Information",
    "6.1": "Administrative & National Policy Requirements",
}

SUBTOPICS = [
    "CUI ON NON-FEDERAL INFORMATION SYSTEMS",
    "INTELLECTUAL PROPERTY",
    "SOFTWARE COMPONENT STANDARDS",
    "GENOMIC DATA SHARING (GDS) POLICY",
    "HUMAN SUBJECTS RESEARCH (HSR)",
    "ANIMAL SUBJECTS RESEARCH (ASR)",
    "ORGANIZATIONAL CONFLICTS OF INTEREST (OCI)",
    "AGENCY SUPPLEMENTAL OCI POLICY",
    "RESEARCH SECURITY DISCLOSURES",
    "ELECTRONIC INVOICING AND PAYMENTS",
    "GOVERNMENT-FURNISHED PROPERTY/EQUIPMENT/INFORMATION",
    "QUESTIONS & ANSWERS (Q&AS)",
]


# ── Extraction ──────────────────────────────────────────────────────────────

def extract_pages(pdf_path: str) -> list[list[str]]:
    """Extract text from each page as a list of stripped lines."""
    doc = fitz.open(pdf_path)
    pages = []
    for page in doc:
        text = page.get_text()
        lines = [ln.strip() for ln in text.split("\n")]
        pages.append(lines)
    doc.close()
    return pages


def is_toc_page(lines: list[str]) -> bool:
    """Detect Table of Contents pages (contain dotted leaders)."""
    dot_count = sum(1 for ln in lines if "....." in ln)
    return dot_count >= 3


def is_cover_page(lines: list[str]) -> bool:
    """Detect the title cover page."""
    text = " ".join(lines)
    return (
        "MISSION OFFICE INNOVATIVE SOLUTIONS OPENING" in text
        and "TABLE OF CONTENTS" not in text
        and "2.0" not in text
    )


def is_overview_page(lines: list[str]) -> bool:
    """Detect Section 1.0 overview page (key-value metadata table)."""
    text = " ".join(lines)
    return "FEDERAL AGENCY NAME:" in text and "SOLICITATION TITLE:" in text


def filter_hf(lines: list[str], sol: str) -> list[str]:
    """Remove header, footer, and page-number lines."""
    out = []
    for ln in lines:
        # Header lines
        if ln == sol or ln.startswith("AMENDMENT"):
            continue
        if ln.startswith("APPENDIX") and len(ln) < 15:
            continue
        # Page numbers
        if re.match(r"^\d{1,2}$", ln):
            continue
        # Roman numeral page numbers
        if re.match(r"^[ivxl]+$", ln):
            continue
        out.append(ln)
    return out


# ── Paragraph reconstruction ───────────────────────────────────────────────

def is_para_break(line: str) -> bool:
    """Detect lines that start new paragraphs."""
    if not line:
        return True
    # Bullet
    if line.startswith("•"):
        return True
    # Lettered sub-items
    if re.match(r"^\([a-z]\)$", line) or re.match(r"^\([a-z]\)\s", line):
        return True
    # Section number on its own line
    if re.match(r"^\d+\.\d+$", line) or re.match(r"^\d+\.0$", line):
        return True
    # Numbered category heading "1." or "2." alone
    if re.match(r"^\d+\.$", line):
        return True
    # Numbered list "1. Text" or "2. Text"
    if re.match(r"^\d+\.\s+[A-Z]", line):
        return True
    # ALL-CAPS heading
    if (
        line == line.upper()
        and len(line) > 8
        and re.match(r"^[A-Z][A-Z &/(),.\-\':;§]+$", line)
        and "....." not in line
    ):
        return True
    # NOTE: blocks
    if line.startswith("NOTE:"):
        return True
    # CONFORMING/NON-CONFORMING
    if line.startswith("CONFORMING PROPOSALS:"):
        return True
    if line.startswith("NON-CONFORMING PROPOSALS:"):
        return True
    # Roman numeral sub-items (PHO)
    if re.match(r"^[ivx]+\.\s", line):
        return True
    return False


def rejoin_paragraphs(lines: list[str]) -> list[str]:
    """Reconstruct paragraphs from PDF-split lines."""
    paragraphs: list[str] = []
    buf: list[str] = []

    for raw in lines:
        line = raw.strip()

        if not line:
            if buf:
                paragraphs.append(" ".join(buf))
                buf = []
            continue

        if is_para_break(line) and buf:
            paragraphs.append(" ".join(buf))
            buf = []

        buf.append(line)

    if buf:
        paragraphs.append(" ".join(buf))

    return paragraphs


# ── Markdown generation ────────────────────────────────────────────────────

def build_md(cfg: dict) -> str:
    """Build the complete markdown document for one ISO."""
    pdf_path = str(INPUT_DIR / cfg["pdf"])
    pages = extract_pages(pdf_path)

    # Collect body lines: skip cover, TOC, overview pages
    body_raw: list[str] = []
    footnotes: list[str] = []

    for page_lines in pages:
        if is_cover_page(page_lines):
            continue
        if is_toc_page(page_lines):
            continue
        if is_overview_page(page_lines):
            continue

        cleaned = filter_hf(page_lines, cfg["sol"])

        for ln in cleaned:
            # Capture footnotes (small superscript numbers)
            fn_m = re.match(
                r"^(\d)\s+(Support services|ISO/IEC|https://www\.healthit|Examples of)",
                ln,
            )
            if fn_m:
                footnotes.append(ln)
                continue
            # Skip appendix raw dump headers
            if ln.strip() == "APPENDIX A: MISSION OFFICE SOLUTION SUMMARY TEMPLATE":
                break
            if ln.strip() == "SEE THE ISO ATTACHMENT.":
                continue

            body_raw.append(ln)

        # Stop at appendices
        joined = " ".join(page_lines)
        if "APPENDIX A: MISSION OFFICE SOLUTION SUMMARY TEMPLATE" in joined:
            break

    # Rejoin into paragraphs
    paragraphs = rejoin_paragraphs(body_raw)

    # ── Build output ──
    md: list[str] = []

    # Front matter
    md.append(f"# {cfg['title']}")
    md.append("")
    md.append(f"**Solicitation Number:** {cfg['sol']}  ")
    md.append("**Amendment:** 03 (October 14, 2025)  ")
    md.append("**Agency:** Advanced Research Projects Agency for Health (ARPA-H)  ")
    md.append(f"**Mission Office:** {cfg['short']}  ")
    md.append("**Award Type:** Other Transactions (OTs)  ")
    md.append("**Closing Date:** March 5, 2029  ")
    md.append(
        "**Eligible Entities:** Academia, Non-Profit Organizations, "
        "For-Profit Entities"
    )
    md.append("")
    md.append("---")
    md.append("")

    # Section 1.0: Overview Table
    md.append(
        "## 1.0 Innovative Solutions Opening Solicitation Overview Information"
    )
    md.append("")
    md.append("| Field | Details |")
    md.append("|-------|---------|")
    md.append(
        "| **Federal Agency Name** | "
        "Advanced Research Projects Agency for Health (ARPA-H) |"
    )
    md.append(f"| **Solicitation Title** | {cfg['title']} |")
    md.append(f"| **Solicitation Number** | {cfg['sol']} |")
    md.append(
        "| **Solution Summary Submissions** | "
        "<https://solutions.arpa-h.gov/Submit-Solution/> |"
    )
    md.append(
        "| **Proposal Submissions** | "
        "<https://solutions.arpa-h.gov/Submit-Proposal/> |"
    )
    md.append(
        "| **ISO Questions** | "
        "<https://solutions.arpa-h.gov/Ask-A-Question/> |"
    )
    md.append("| **Dates/Times** | All times listed herein are Eastern Time |")
    md.append(
        "| **Release and Amendment Dates** | "
        "Release: March 14, 2024; Amendment 01: September 25, 2024; "
        "Amendment 02: June 06, 2025; Amendment 03: October 14, 2025 |"
    )
    md.append(
        "| **Q&A Due Date** | "
        "Questions may be asked while this solicitation is open |"
    )
    md.append("| **Closing Date** | March 5, 2029 |")
    md.append("| **Anticipated Award** | Multiple awards are anticipated |")
    md.append("| **Types of Instruments** | Other Transactions (OTs) |")
    md.append(
        "| **Proposers/Eligible Entities** | "
        "Academia, Non-Profit Organizations, and For-Profit Entities |"
    )
    md.append(
        "| **Resource Sharing** | "
        "Resource sharing may be encouraged or requested |"
    )
    md.append("")

    # ── Process body paragraphs ──
    i = 0
    while i < len(paragraphs):
        p = paragraphs[i].strip()
        if not p:
            i += 1
            continue

        # ── Section numbers (X.0) ──
        m = re.match(r"^(\d+)\.0$", p)
        if m:
            num = f"{m.group(1)}.0"
            title = SECTION_TITLES.get(num, "")
            md.append(f"## {num} {title}")
            md.append("")
            i += 1
            # Skip the next paragraph if it's just the title echo
            if i < len(paragraphs):
                nxt = paragraphs[i].strip()
                nxt_upper = nxt.upper().rstrip(":")
                if nxt_upper == title.upper().rstrip(":"):
                    i += 1
                elif nxt_upper.startswith(title.upper()[:20]):
                    i += 1
            continue

        # ── Sub-section numbers (X.Y) ──
        m = re.match(r"^(\d+\.\d+)$", p)
        if m:
            num = m.group(1)
            title = SECTION_TITLES.get(num, "")
            level = "###"
            md.append(f"{level} {num} {title}")
            md.append("")
            i += 1
            # Skip echo
            if i < len(paragraphs):
                nxt = paragraphs[i].strip()
                nxt_clean = nxt.upper().rstrip(":").strip()
                title_clean = title.upper().rstrip(":").strip()
                if nxt_clean == title_clean:
                    i += 1
                # Sometimes the title + first paragraph are merged
                elif nxt_clean.startswith(title_clean):
                    remainder = nxt[len(title):].strip().lstrip(":").strip()
                    if remainder:
                        md.append(remainder)
                        md.append("")
                    i += 1
            continue

        # ── Criterion headings: "1. CRITERION 1: ..." ──
        m = re.match(r"^(\d+)\.\s+(CRITERION\s+\d+:\s+.+)", p)
        if m:
            crit_num = m.group(1)
            crit_rest = m.group(2).strip()
            md.append(f"**{crit_num}. {crit_rest}**")
            md.append("")
            i += 1
            continue

        # ── Numbered category heading alone: "1." ──
        m = re.match(r"^(\d+)\.$", p)
        if m:
            # Next paragraph should be the category title
            if i + 1 < len(paragraphs):
                title_line = paragraphs[i + 1].strip()
                md.append(f"{m.group(1)}. {title_line}")
                md.append("")
                i += 2
                continue

        # ── SUBTOPICS (ALL-CAPS under 6.1) ──
        p_upper = p.upper().strip()
        matched_st = False
        for st in SUBTOPICS:
            if p_upper == st or p_upper.startswith(st):
                display = st.title()
                # Fix special cases
                display = display.replace("Cui ", "CUI ")
                display = display.replace("Oci", "OCI")
                display = display.replace("(Oci)", "(OCI)")
                display = display.replace("Gds", "GDS")
                display = display.replace("(Gds)", "(GDS)")
                display = display.replace("Hsr", "HSR")
                display = display.replace("(Hsr)", "(HSR)")
                display = display.replace("Asr", "ASR")
                display = display.replace("(Asr)", "(ASR)")
                display = display.replace("Q&Ans", "Q&As")
                display = display.replace("(Q&Ans)", "(Q&As)")
                display = display.replace("(Q&as)", "(Q&As)")

                md.append(f"#### {display}")
                md.append("")
                leftover = p[len(st):].strip()
                if leftover:
                    md.append(leftover)
                    md.append("")
                matched_st = True
                break
        if matched_st:
            i += 1
            continue

        # ── NOTE: blocks ──
        if p.startswith("NOTE:"):
            md.append(f"> **NOTE:** {p[5:].strip()}")
            md.append("")
            i += 1
            continue

        # ── CONFORMING/NON-CONFORMING ──
        if p.startswith("CONFORMING PROPOSALS:"):
            md.append(f"**Conforming Proposals:** {p[21:].strip()}")
            md.append("")
            i += 1
            continue
        if p.startswith("NON-CONFORMING PROPOSALS:"):
            md.append(f"**Non-Conforming Proposals:** {p[25:].strip()}")
            md.append("")
            i += 1
            continue

        # ── Bullet points ──
        if p.startswith("•"):
            md.append(f"- {p[1:].strip()}")
            i += 1
            continue

        # ── Lettered items: (a), (b) ──
        lm = re.match(r"^\(([a-z])\)\s*(.*)", p)
        if lm:
            md.append(f"({lm.group(1)}) {lm.group(2)}")
            md.append("")
            i += 1
            continue

        # ── Roman numeral sub-items (PHO) ──
        rm = re.match(r"^([ivx]+)\.\s+(.*)", p)
        if rm:
            md.append(f"  {rm.group(1)}. {rm.group(2)}")
            i += 1
            continue

        # ── Numbered list items ──
        nm = re.match(r"^(\d+)\.\s+(.+)$", p)
        if nm and len(p) > 5:
            md.append(f"{nm.group(1)}. {nm.group(2)}")
            md.append("")
            i += 1
            continue

        # ── Regular paragraph ──
        md.append(p)
        md.append("")
        i += 1

    # ── Appendices ──
    md.append("---")
    md.append("")

    md.append("## Appendix A: Mission Office Solution Summary Template")
    md.append("")
    md.append("*See the ISO Attachment.*")
    md.append("")

    # Acronyms table
    all_acr = sorted(ACRONYMS + cfg["mission_acronyms"], key=lambda x: x[0].upper())
    md.append("## Appendix B: Acronyms")
    md.append("")
    md.append("| Acronym | Definition |")
    md.append("|---------|------------|")
    for acr, defn in all_acr:
        md.append(f"| {acr} | {defn} |")
    md.append("")

    # Hyperlinks table
    md.append("## Appendix C: Hyperlinks")
    md.append("")
    md.append("| ISO Section | Reference | URL |")
    md.append("|-------------|-----------|-----|")
    for sec, ref, url in HYPERLINKS:
        md.append(f"| {sec} | {ref} | <{url}> |")
    md.append("")

    # Footnotes
    if footnotes:
        md.append("---")
        md.append("")
        md.append("## Footnotes")
        md.append("")
        for fn in footnotes:
            fn_m = re.match(r"^(\d)\s+(.+)$", fn)
            if fn_m:
                md.append(f"[^{fn_m.group(1)}]: {fn_m.group(2)}")
            else:
                md.append(f"- {fn}")
        md.append("")

    result = "\n".join(md)
    result = re.sub(r"\n{3,}", "\n\n", result)
    return result.strip() + "\n"


# ── Main ────────────────────────────────────────────────────────────────────

def main():
    for cfg in [HSF, PHO]:
        pdf_path = INPUT_DIR / cfg["pdf"]
        if not pdf_path.exists():
            print(f"  SKIP {cfg['pdf']} (not found)")
            continue

        out_path = OUTPUT_DIR / cfg["out"]
        print(f"  CONVERT {cfg['pdf']} -> {cfg['out']}")
        result = build_md(cfg)
        out_path.write_text(result, encoding="utf-8")
        lc = result.count("\n")
        print(f"    -> {len(result):,} bytes, {lc} lines")


if __name__ == "__main__":
    main()

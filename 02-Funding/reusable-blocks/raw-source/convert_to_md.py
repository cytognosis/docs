#!/usr/bin/env python3
"""Convert raw .txt grant template files to structured markdown."""

import re
import textwrap
from pathlib import Path

RAW_DIR = Path(__file__).parent


def clean_form_feeds(text: str) -> str:
    """Remove form feed characters and associated page headers/footers."""
    # Remove form feeds
    text = text.replace("\f", "\n")
    # Remove standalone page numbers (e.g., lines that are just "1" or "18")
    text = re.sub(r"\n\s*\d{1,3}\s*\n", "\n\n", text)
    # Remove repeated header lines like "ARPA-H-SOL-24-104" / "Amendment 03"
    text = re.sub(
        r"\n\s*(ARPA-H-SOL-24-\d+)\s*\n\s*(AMENDMENT \d+|Amendment \d+)\s*\n",
        "\n",
        text,
        flags=re.IGNORECASE,
    )
    # Remove DOE header lines
    text = re.sub(
        r"\n\s*U\.S\. Department of Energy \| Genesis Mission National Science and Technology Challenges\s*\n",
        "\n",
        text,
    )
    # Remove repeated "Other Arrangements/Transactions Guide" headers
    text = re.sub(
        r"\n\s*Other Arrangements/Transactions Guide\s*\n\s*\(Effective [^)]+\)\s*\n\s*Page \d+ of \d+\s*\n",
        "\n",
        text,
    )
    # Collapse 3+ blank lines to 2
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text


def convert_pdf_document(text: str, title: str, metadata: dict) -> str:
    """Convert a PDF-extracted government document to structured markdown."""
    text = clean_form_feeds(text)

    lines = text.split("\n")
    output_lines = []

    # Add YAML-style front matter as markdown
    output_lines.append(f"# {title}")
    output_lines.append("")
    if metadata:
        for key, val in metadata.items():
            output_lines.append(f"- **{key}**: {val}")
        output_lines.append("")
        output_lines.append("---")
        output_lines.append("")

    # Process lines: detect section headings and structure
    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        # Skip empty lines (will be handled by paragraph logic)
        if not stripped:
            output_lines.append("")
            i += 1
            continue

        # Detect numbered section headings like "1.0  TITLE" or "A. TITLE"
        section_match = re.match(
            r"^(\d+\.\d+)\s+(.+)$", stripped
        )
        subsection_match = re.match(
            r"^(\d+\.\d+)\s+(.+)$", stripped
        )

        # Top-level sections: "1.0 TITLE"
        top_section = re.match(r"^(\d+)\.0\s+(.+)$", stripped)
        if top_section:
            output_lines.append(f"## {top_section.group(1)}.0 {top_section.group(2)}")
            i += 1
            continue

        # Sub-sections: "2.1 TITLE" or "A. TITLE"
        sub_section = re.match(r"^(\d+\.\d+)\s+(.+)$", stripped)
        if sub_section and stripped.upper() == stripped and len(stripped) < 120:
            output_lines.append(
                f"### {sub_section.group(1)} {sub_section.group(2)}"
            )
            i += 1
            continue

        # Letter sections: "A. TITLE"
        letter_section = re.match(r"^([A-Z])\.\s+(.+)$", stripped)
        if letter_section and stripped.upper() == stripped and len(stripped) < 100:
            output_lines.append(
                f"### {letter_section.group(1)}. {letter_section.group(2)}"
            )
            i += 1
            continue

        # ALL CAPS lines that look like sub-headings
        if (
            stripped.upper() == stripped
            and len(stripped) > 5
            and len(stripped) < 80
            and not stripped.startswith("•")
            and not stripped.startswith("-")
            and re.match(r"^[A-Z][A-Z\s&/(),\-]+$", stripped)
        ):
            output_lines.append(f"#### {stripped.title()}")
            i += 1
            continue

        # Bullet points
        if stripped.startswith("•") or stripped.startswith("·"):
            output_lines.append(f"- {stripped[1:].strip()}")
            i += 1
            continue

        # Numbered list items
        numbered = re.match(r"^(\d+)\.\s+(.+)$", stripped)
        if numbered and len(stripped) < 200:
            num = numbered.group(1)
            content = numbered.group(2)
            # Check if it's a criterion or list item vs a section
            if not content.upper() == content:
                output_lines.append(f"{num}. {content}")
                i += 1
                continue

        # Regular text
        output_lines.append(stripped)
        i += 1

    result = "\n".join(output_lines)
    # Clean up excessive blank lines
    result = re.sub(r"\n{3,}", "\n\n", result)
    return result.strip() + "\n"


def convert_excel_document(text: str, title: str) -> str:
    """Convert an Excel-extracted spreadsheet to structured markdown."""
    lines = text.split("\n")
    output_lines = [f"# {title}", ""]

    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        if not stripped:
            output_lines.append("")
            i += 1
            continue

        # Sheet headers
        sheet_match = re.match(r"^## Sheet:\s*(.+?)(?:\s*\(dims:.+\))?$", stripped)
        if sheet_match:
            output_lines.append(f"## {sheet_match.group(1).strip()}")
            output_lines.append("")
            i += 1
            continue

        # Cell references like [A1] Value
        cell_match = re.match(r"^\[([A-Z]+\d+)\]\s*(.*)$", stripped)
        if cell_match:
            cell_ref = cell_match.group(1)
            cell_val = cell_match.group(2).strip()

            # Check if it's a formula
            if cell_val.startswith("="):
                output_lines.append(f"- **{cell_ref}**: `{cell_val}`")
            elif cell_val:
                output_lines.append(f"- **{cell_ref}**: {cell_val}")
            i += 1
            continue

        # Regular content
        output_lines.append(stripped)
        i += 1

    result = "\n".join(output_lines)
    result = re.sub(r"\n{3,}", "\n\n", result)
    return result.strip() + "\n"


def convert_slides_document(text: str, title: str) -> str:
    """Convert webinar slide text to structured markdown."""
    text = clean_form_feeds(text)
    lines = text.split("\n")
    output_lines = [f"# {title}", ""]

    slide_num = 0
    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        if not stripped:
            output_lines.append("")
            i += 1
            continue

        # Skip standalone page/slide numbers and email footers
        if re.match(r"^\d{1,2}$", stripped):
            i += 1
            continue
        if stripped == "TechLabs@nsf.gov":
            i += 1
            continue
        if re.match(r"^Read the RFI on SAM\.gov$", stripped):
            i += 1
            continue

        # Detect slide titles (short lines, often title case or specific patterns)
        if (
            len(stripped) < 60
            and not stripped.startswith("•")
            and not stripped.startswith("-")
            and not stripped.startswith("Click")
            and i > 0
            and (not lines[i - 1].strip())
            and re.match(r"^[A-Z]", stripped)
            and not re.match(r"^\d", stripped)
        ):
            # Check if next line is also empty or a bullet, suggesting this is a heading
            next_line = lines[i + 1].strip() if i + 1 < len(lines) else ""
            if not next_line or next_line.startswith("•") or next_line.startswith("-"):
                slide_num += 1
                output_lines.append(f"## Slide {slide_num}: {stripped}")
                i += 1
                continue

        # Bullets
        if stripped.startswith("•"):
            output_lines.append(f"- {stripped[1:].strip()}")
            i += 1
            continue

        output_lines.append(stripped)
        i += 1

    result = "\n".join(output_lines)
    result = re.sub(r"\n{3,}", "\n\n", result)
    return result.strip() + "\n"


def convert_st_challenges(text: str) -> str:
    """Convert the DOE S&T Challenges document."""
    text = clean_form_feeds(text)
    lines = text.split("\n")
    output_lines = [
        "# DOE Genesis Mission: National Science and Technology Challenges",
        "",
        "U.S. Department of Energy",
        "",
        "---",
        "",
    ]

    i = 0
    current_challenge = None
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        if not stripped:
            output_lines.append("")
            i += 1
            continue

        # Skip standalone page numbers
        if re.match(r"^\d{1,2}$", stripped):
            i += 1
            continue

        # Skip repeated doc headers
        if "Genesis Mission" in stripped and "Contents" not in stripped:
            if "U.S. Department of Energy" in stripped or "U.S. DEPARTMENT" in stripped:
                i += 1
                continue

        # TOC entries
        if re.match(r"^.+\.{3,}\s*\d+$", stripped):
            entry = re.sub(r"\.{3,}\s*\d+$", "", stripped).strip()
            output_lines.append(f"- {entry}")
            i += 1
            continue

        # Challenge section titles (centered, multi-word, title-like)
        if (
            len(stripped) < 80
            and not stripped.startswith("Challenge:")
            and not stripped.startswith("AI Solution:")
            and not stripped.startswith("Justification:")
            and not stripped.startswith("National Impact:")
            and re.match(r"^[A-Z]", stripped)
            and stripped[0].isupper()
            and not any(
                stripped.startswith(p) for p in ["The ", "This ", "A ", "An ", "By "]
            )
        ):
            # Look ahead: if next non-blank line starts with "Challenge:", this is a heading
            j = i + 1
            while j < len(lines) and not lines[j].strip():
                j += 1
            if j < len(lines) and lines[j].strip().startswith("Challenge:"):
                # Might be a multi-line title
                title_parts = [stripped]
                k = i + 1
                while k < len(lines) and lines[k].strip() and not lines[k].strip().startswith("Challenge:"):
                    title_parts.append(lines[k].strip())
                    k += 1
                full_title = " ".join(title_parts)
                output_lines.append(f"## {full_title}")
                output_lines.append("")
                i = k
                continue

        # Section labels within challenges
        for label in ["Challenge:", "AI Solution:", "Justification:", "National Impact:"]:
            if stripped.startswith(label):
                content = stripped[len(label):].strip()
                output_lines.append(f"**{label}** {content}")
                i += 1
                break
        else:
            # Footnotes
            if re.match(r"^\d+\s+", stripped) and len(stripped) > 20:
                fn_match = re.match(r"^(\d+)\s+(.+)$", stripped)
                if fn_match:
                    output_lines.append(
                        f"[^{fn_match.group(1)}]: {fn_match.group(2)}"
                    )
                    i += 1
                    continue

            output_lines.append(stripped)
            i += 1
            continue
        continue

    result = "\n".join(output_lines)
    result = re.sub(r"\n{3,}", "\n\n", result)
    return result.strip() + "\n"


def convert_rfa_announcement(text: str) -> str:
    """Convert DOE RFA announcement (Lewis-Burke analysis)."""
    text = clean_form_feeds(text)
    lines = text.split("\n")
    output_lines = [
        "# DOE Genesis Mission: Request for Application Analysis",
        "",
        "**Source**: Lewis-Burke Associates LLC, March 19, 2026",
        "",
        "**RFA Number**: DE-FOA-0003612",
        "",
        "**Total Funding**: $294 million",
        "",
        "---",
        "",
    ]

    i = 0
    in_table = False
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        if not stripped:
            if in_table:
                in_table = False
            output_lines.append("")
            i += 1
            continue

        # Detect section headings
        if stripped in [
            "Eligibility and Key Requirements",
            "Review Process and Other Considerations",
            "Topics and Focus Areas",
        ]:
            output_lines.append(f"## {stripped}")
            i += 1
            continue

        # Bullets
        if stripped.startswith("•"):
            output_lines.append(f"- {stripped[1:].strip()}")
            i += 1
            continue

        # Quoted text
        if stripped.startswith('"') or stripped.startswith('"'):
            output_lines.append(f"> {stripped}")
            i += 1
            continue

        # Challenge area table entries
        challenge_match = re.match(r"^(\d{1,2})\s+(.+)$", stripped)
        if challenge_match and len(stripped) < 60:
            num = challenge_match.group(1)
            name = challenge_match.group(2)
            output_lines.append(f"### {num}. {name}")
            i += 1
            continue

        output_lines.append(stripped)
        i += 1

    result = "\n".join(output_lines)
    result = re.sub(r"\n{3,}", "\n\n", result)
    return result.strip() + "\n"


# ── File-specific converters ──

CONVERTERS = {
    "arpah_hsf_iso.txt": lambda text: convert_pdf_document(
        text,
        "ARPA-H Health Science Futures (HSF) Innovative Solutions Opening",
        {
            "Solicitation Number": "ARPA-H-SOL-24-104",
            "Amendment": "03 (October 14, 2025)",
            "Agency": "Advanced Research Projects Agency for Health (ARPA-H)",
            "Mission Office": "Health Science Futures (HSF)",
            "Award Type": "Other Transactions (OTs)",
            "Closing Date": "March 5, 2029",
            "Eligible Entities": "Academia, Non-Profit Organizations, For-Profit Entities",
        },
    ),
    "arpah_pho_iso.txt": lambda text: convert_pdf_document(
        text,
        "ARPA-H Proactive Health Office (PHO) Innovative Solutions Opening",
        {
            "Solicitation Number": "ARPA-H-SOL-24-106",
            "Amendment": "03 (October 14, 2025)",
            "Agency": "Advanced Research Projects Agency for Health (ARPA-H)",
            "Mission Office": "Proactive Health Office (PHO)",
            "Award Type": "Other Transactions (OTs)",
            "Closing Date": "March 5, 2029",
            "Eligible Entities": "Academia, Non-Profit Organizations, For-Profit Entities",
        },
    ),
    "arpah_cost_workbook.txt": lambda text: convert_excel_document(
        text,
        "ARPA-H Cost Proposal Workbook (Other Transactions)",
    ),
    "arpah_cost_workbook_resource_sharing.txt": lambda text: convert_excel_document(
        text,
        "ARPA-H Cost Proposal Workbook (Other Transactions, Resource Sharing)",
    ),
    "doe_foa.txt": lambda text: convert_pdf_document(
        text,
        "DOE Genesis Mission: Transforming Science and Energy with AI",
        {
            "RFA Number": "DE-FOA-0003612",
            "RFA Type": "Initial",
            "Assistance Listings": "81.049",
            "Issue Date": "March 17, 2026",
            "Phase I Deadline": "April 28, 2026 (11:59 PM ET)",
            "Phase II LOI Deadline": "April 28, 2026 (5:00 PM ET)",
            "Phase II Application Deadline": "May 19, 2026 (11:59 PM ET)",
            "Participating Offices": "SC, CMEI, EM, OE, NE, HGEO",
            "Total Funding": "$293.76 million",
        },
    ),
    "doe_phase_i_template.txt": lambda text: convert_excel_document(
        text,
        "DOE Genesis Mission: Phase I Application Template",
    ),
    "doe_phase_ii_loi_template.txt": lambda text: convert_excel_document(
        text,
        "DOE Genesis Mission: Phase II Letter of Intent Template",
    ),
    "doe_rfa_announcement.txt": lambda text: convert_rfa_announcement(text),
    "doe_st_challenges.txt": lambda text: convert_st_challenges(text),
    "nsf_ot_guide.txt": lambda text: convert_pdf_document(
        text,
        "NSF Other Arrangements/Transactions Guide (OA/T Guide)",
        {
            "Version": "1.0",
            "Effective Date": "April 22, 2024",
            "Agency": "U.S. National Science Foundation",
            "Division": "Division of Acquisition and Cooperative Support",
        },
    ),
    "nsf_tech_labs_rfi.txt": lambda text: convert_pdf_document(
        text,
        "NSF Tech Labs Initiative: Request for Information",
        {
            "Agency": "U.S. National Science Foundation, Directorate for Technology, Innovation and Partnerships (TIP)",
            "Response Deadline": "January 20, 2026 at 3:00 PM EST",
            "Contact": "TechLabs@nsf.gov",
            "Funding Mechanism": "Other Transaction (OT) contracts",
            "Expected Funding": "$10M-$50M per team per year (beyond Phase 0)",
        },
    ),
    "nsf_webinar_slides.txt": lambda text: convert_slides_document(
        text,
        "NSF Tech Labs Initiative: Webinar Slides (December 17, 2025)",
    ),
}


def main():
    converted = 0
    skipped = 0

    for txt_file in sorted(RAW_DIR.glob("*.txt")):
        name = txt_file.name
        md_name = txt_file.stem + ".md"
        md_path = RAW_DIR / md_name

        if name not in CONVERTERS:
            print(f"  SKIP  {name} (no converter defined)")
            skipped += 1
            continue

        if md_path.exists():
            print(f"  EXISTS {md_name} (already converted)")
            skipped += 1
            continue

        print(f"  CONVERT {name} -> {md_name}")
        text = txt_file.read_text(encoding="utf-8")
        converter = CONVERTERS[name]
        result = converter(text)
        md_path.write_text(result, encoding="utf-8")
        converted += 1

    print(f"\nDone: {converted} converted, {skipped} skipped")


if __name__ == "__main__":
    main()

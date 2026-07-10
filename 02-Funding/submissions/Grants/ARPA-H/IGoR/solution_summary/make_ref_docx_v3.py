"""
Build brand_reference.docx v3 -- maximum compliant density.
Body: Inter Variable 11pt (minimum per spec), line spacing 13pt.
Headings: slightly tighter before/after.
Tables: 9pt (post-processed separately).
"""
from docx import Document
from docx.shared import Pt, Inches, RGBColor

SRC = "/tmp/ref.docx"
DST = "/home/mohammadi/Claude/Projects/Grants/02-submissions/Grants/ARPA-H/IGoR/solution_summary/brand_reference.docx"

INDIGO = RGBColor(0x51, 0x45, 0xA8)
VIOLET = RGBColor(0x8B, 0x3F, 0xC7)

doc = Document(SRC)

for section in doc.sections:
    section.page_width    = Inches(8.5)
    section.page_height   = Inches(11)
    section.left_margin   = Inches(1.0)
    section.right_margin  = Inches(1.0)
    section.top_margin    = Inches(1.0)
    section.bottom_margin = Inches(1.0)

style_map = {
    "Normal":    ("Inter Variable", 11, False, None,   0,  3, 13),
    "Body Text": ("Inter Variable", 11, False, None,   0,  3, 13),
    "Heading 1": ("Inter Variable", 13, True,  INDIGO, 6,  2, None),
    "Heading 2": ("Inter Variable", 11.5, True, VIOLET, 4, 2, None),
    "Heading 3": ("Inter Variable", 11, True,  VIOLET, 4,  2, None),
    "Title":     ("Inter Variable", 16, True,  INDIGO, 0,  4, None),
    "Compact":   ("Inter Variable", 11, False, None,   0,  2, 12),
}

for sname, (fname, fsize, fbold, fcolor, sb, sa, ls) in style_map.items():
    try:
        st = doc.styles[sname]
    except KeyError:
        continue
    st.font.name = fname
    st.font.size = Pt(fsize)
    st.font.bold = fbold
    if fcolor:
        st.font.color.rgb = fcolor
    if not hasattr(st, 'paragraph_format'):
        continue
    pf = st.paragraph_format
    pf.space_before = Pt(sb)
    pf.space_after  = Pt(sa)
    if ls:
        pf.line_spacing = Pt(ls)

doc.save(DST)
print(f"Saved v3 reference: {DST}")

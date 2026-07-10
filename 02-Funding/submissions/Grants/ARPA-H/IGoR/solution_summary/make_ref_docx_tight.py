"""
Build brand_reference.docx (tight version) from pandoc's default reference.docx.
Tighter paragraph spacing to compress Sections 1-4.
"""
from docx import Document
from docx.shared import Pt, Inches, RGBColor

SRC = "/tmp/ref.docx"
DST = "/home/mohammadi/Claude/Projects/Grants/02-submissions/Grants/ARPA-H/IGoR/solution_summary/brand_reference.docx"

INDIGO = RGBColor(0x51, 0x45, 0xA8)
VIOLET = RGBColor(0x8B, 0x3F, 0xC7)

doc = Document(SRC)

# --- Page setup: Letter, 1-inch margins ---
for section in doc.sections:
    section.page_width    = Inches(8.5)
    section.page_height   = Inches(11)
    section.left_margin   = Inches(1.0)
    section.right_margin  = Inches(1.0)
    section.top_margin    = Inches(1.0)
    section.bottom_margin = Inches(1.0)

style_map = {
    "Normal":    ("Inter Variable", 11, False, None),
    "Body Text": ("Inter Variable", 11, False, None),
    "Heading 1": ("Inter Variable", 13, True,  INDIGO),
    "Heading 2": ("Inter Variable", 11.5, True,  VIOLET),
    "Heading 3": ("Inter Variable", 11, True,  VIOLET),
    "Title":     ("Inter Variable", 16, True,  INDIGO),
    "Default Paragraph Font": ("Inter Variable", 11, False, None),
    "Table Contents": ("Inter Variable", 9.5, False, None),
    "Table Paragraph": ("Inter Variable", 9.5, False, None),
    "Compact":   ("Inter Variable", 11, False, None),
}

for sname, (fname, fsize, fbold, fcolor) in style_map.items():
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
    if sname in ("Normal", "Body Text"):
        pf.space_before = Pt(0)
        pf.space_after  = Pt(3)
        pf.line_spacing = Pt(14)
    elif sname.startswith("Heading"):
        pf.space_before = Pt(6)
        pf.space_after  = Pt(3)
    elif sname in ("Table Contents", "Table Paragraph", "Compact"):
        pf.space_before = Pt(1)
        pf.space_after  = Pt(1)
        pf.line_spacing = Pt(12)

doc.save(DST)
print(f"Saved tight reference: {DST}")

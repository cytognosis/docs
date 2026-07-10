"""
Build brand_reference.docx from pandoc's default reference.docx.
Sets Inter font, brand heading colors, Letter page, 1-inch margins.
"""
import shutil
from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
import copy

SRC = "/tmp/ref.docx"
DST = "/home/mohammadi/Claude/Projects/Grants/02-submissions/Grants/ARPA-H/IGoR/solution_summary/brand_reference.docx"

INDIGO  = RGBColor(0x51, 0x45, 0xA8)   # #5145A8
VIOLET  = RGBColor(0x8B, 0x3F, 0xC7)   # #8B3FC7

def set_font(run_or_font, name, size_pt, bold=False, color=None):
    f = run_or_font if hasattr(run_or_font, 'name') else run_or_font.font
    f.name = name
    f.size = Pt(size_pt)
    f.bold = bold
    if color:
        f.color.rgb = color

doc = Document(SRC)

# --- Page setup: Letter, 1-inch margins ---
for section in doc.sections:
    section.page_width  = Inches(8.5)
    section.page_height = Inches(11)
    section.left_margin   = Inches(1.0)
    section.right_margin  = Inches(1.0)
    section.top_margin    = Inches(1.0)
    section.bottom_margin = Inches(1.0)

# --- Style tweaks ---
style_map = {
    "Normal":    ("Inter Variable", 11, False, None),
    "Body Text": ("Inter Variable", 11, False, None),
    "Heading 1": ("Inter Variable", 14, True,  INDIGO),
    "Heading 2": ("Inter Variable", 12, True,  VIOLET),
    "Heading 3": ("Inter Variable", 11, True,  VIOLET),
    "Title":     ("Inter Variable", 18, True,  INDIGO),
    "Default Paragraph Font": ("Inter Variable", 11, False, None),
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
    # paragraph spacing
    if sname in ("Normal", "Body Text"):
        st.paragraph_format.space_before = Pt(0)
        st.paragraph_format.space_after  = Pt(4)
    if sname.startswith("Heading"):
        st.paragraph_format.space_before = Pt(8)
        st.paragraph_format.space_after  = Pt(4)

doc.save(DST)
print(f"Saved: {DST}")

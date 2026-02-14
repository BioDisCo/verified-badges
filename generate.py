#!/usr/bin/env python3
"""Generate verified/formalized badge SVGs, changing the prover name and badge kind."""

BADGE_KINDS = {
    "verified": {
        "label": "VERIFIED",
        "color": "#2a6e3f",
        "suffix": "",
        "extra_width": 0,
    },
    "formalized": {
        "label": "FORMALIZED",
        "color": "#2a5a8f",
        "suffix": "-formalized",
        "extra_width": 22,  # "FORMALIZED" is wider than "VERIFIED"
    },
}

TEMPLATE = '''<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<svg
   viewBox="0 0 {width} 34"
   width="{width}"
   height="34"
   version="1.1"
   xmlns="http://www.w3.org/2000/svg">
  <g transform="translate(5.0002495)">
    <g transform="translate(-4,-2)">
      <path
         d="M 17,2 30,8 V 20 C 30,29 17,36 17,36 17,36 4,29 4,20 V 8 Z"
         fill="{color}" />
      <polyline
         points="10,18 15,23 24,13"
         fill="none"
         stroke="#ffffff"
         stroke-width="2.6"
         stroke-linecap="round"
         stroke-linejoin="round" />
    </g>
    <g transform="translate(-2,-1.2295261)">
      <text
         x="35.832798"
         y="12.691075"
         font-family="'Helvetica Neue', Arial, sans-serif"
         font-size="10.2464px"
         font-weight="600"
         fill="{color}"
         letter-spacing="2"
         style="stroke-width:1.46378">{label}</text>
      <text
         x="34.9412"
         y="30.866396"
         font-family="Georgia, serif"
         font-size="17.1337px"
         font-weight="400"
         fill="{color}"
         letter-spacing="0.5"
         style="stroke-width:1.22383">{name}</text>
    </g>
  </g>
</svg>'''

# Approximate widths tuned to name length (Lean original = 104.27)
provers = {
    "lean":     {"name": "Lean",     "width": "108"},
    "coq":      {"name": "Coq",      "width": "108"},
    "rocq":     {"name": "Rocq",     "width": "108"},
    "isabelle": {"name": "Isabelle", "width": "118"},
    "agda":     {"name": "Agda",     "width": "108"},
    "hol4":     {"name": "HOL4",     "width": "108"},
    "dafny":    {"name": "Dafny",    "width": "108"},
    "fstar":    {"name": "F*",       "width": "108"},
    "tla":      {"name": "TLA+",     "width": "108"},
    "idris":    {"name": "Idris",    "width": "108"},
    "pvs":      {"name": "PVS",      "width": "108"},
}

try:
    import cairosvg
    can_pdf = True
except ImportError:
    can_pdf = False

count = 0
for kind, kind_info in BADGE_KINDS.items():
    for key, info in provers.items():
        filename = f"{key}{kind_info['suffix']}"
        badge_width = str(int(info["width"]) + kind_info["extra_width"])
        svg = TEMPLATE.format(
            name=info["name"],
            width=badge_width,
            color=kind_info["color"],
            label=kind_info["label"],
        )
        with open(f"badges/{filename}.svg", "w") as f:
            f.write(svg)
        if can_pdf:
            cairosvg.svg2pdf(bytestring=svg.encode(), write_to=f"badges/{filename}.pdf")
        print(f"  ✓ badges/{filename}.svg" + (" + .pdf" if can_pdf else "") + f"  ({kind}: {info['name']})")
        count += 1

print(f"\nGenerated {count} badges.")
if not can_pdf:
    print("Note: install cairosvg (pip install cairosvg) to also generate PDFs.")

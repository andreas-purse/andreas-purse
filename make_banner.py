"""Generate the blueprint-style header banner (light + dark) for the profile README."""
from pathlib import Path

THEMES = {
    "dark": dict(bg="#0b2545", minor="#123563", major="#1b4580", frame="#8fb3e6",
                 ink="#eaf2ff", muted="#8fb3e6", accent="#ffb703"),
    "light": dict(bg="#f5f8fc", minor="#e3eaf4", major="#cbd8ea", frame="#0b2545",
                  ink="#0b2545", muted="#4a6a96", accent="#d97706"),
}

W, H = 1200, 360
SANS = "'Segoe UI', -apple-system, Helvetica, Arial, sans-serif"
MONO = "ui-monospace, 'SFMono-Regular', Consolas, 'Liberation Mono', monospace"


def svg(t):
    zones_x = "".join(
        f'<text x="{40 + 280 * i + 140}" y="27" class="z">{i + 1}</text>'
        f'<text x="{40 + 280 * i + 140}" y="{H - 17}" class="z">{i + 1}</text>'
        for i in range(4))
    zones_y = "".join(
        f'<text x="23" y="{40 + 93 * i + 50}" class="z">{c}</text>'
        f'<text x="{W - 23}" y="{40 + 93 * i + 50}" class="z">{c}</text>'
        for i, c in enumerate("ABC"))
    ticks = "".join(
        f'<line x1="{40 + 280 * i}" y1="30" x2="{40 + 280 * i}" y2="40"/>'
        f'<line x1="{40 + 280 * i}" y1="{H - 40}" x2="{40 + 280 * i}" y2="{H - 30}"/>'
        for i in range(1, 4))

    # part drawing on the right: a disc with centre lines, a rotating dashed ring
    cx, cy, r = 800, 160, 78
    part = f'''
  <g class="part">
    <circle cx="{cx}" cy="{cy}" r="{r}" class="edge"/>
    <circle cx="{cx}" cy="{cy}" r="{r - 26}" class="edge thin"/>
    <circle cx="{cx}" cy="{cy}" r="9" class="edge"/>
    <g class="spin"><circle cx="{cx}" cy="{cy}" r="{r + 16}" class="ring"/></g>
    <line x1="{cx - r - 34}" y1="{cy}" x2="{cx + r + 34}" y2="{cy}" class="cl"/>
    <line x1="{cx}" y1="{cy - r - 34}" x2="{cx}" y2="{cy + r + 34}" class="cl"/>
    <line x1="{cx - r}" y1="{cy + r + 46}" x2="{cx + r}" y2="{cy + r + 46}" class="dim" marker-start="url(#a)" marker-end="url(#a)"/>
    <line x1="{cx - r}" y1="{cy + 4}" x2="{cx - r}" y2="{cy + r + 54}" class="ext"/>
    <line x1="{cx + r}" y1="{cy + 4}" x2="{cx + r}" y2="{cy + r + 54}" class="ext"/>
    <rect x="{cx - 52}" y="{cy + r + 36}" width="104" height="20" class="lbl-bg"/>
    <text x="{cx}" y="{cy + r + 50}" class="dimt">Ø IDEA → BUILD</text>
  </g>'''

    # title block, bottom right
    bx, by, bw = 960, 262, 200
    tb = f'''
  <g class="tb">
    <rect x="{bx}" y="{by}" width="{bw}" height="58"/>
    <line x1="{bx}" y1="{by + 20}" x2="{bx + bw}" y2="{by + 20}"/>
    <line x1="{bx}" y1="{by + 39}" x2="{bx + bw}" y2="{by + 39}"/>
    <line x1="{bx + 92}" y1="{by + 20}" x2="{bx + 92}" y2="{by + 58}"/>
    <text x="{bx + 8}" y="{by + 14}" class="tbt">DWG AP-001 · ANDREAS PURSE</text>
    <text x="{bx + 8}" y="{by + 33}" class="tbt">REV 2026.10</text>
    <text x="{bx + 100}" y="{by + 33}" class="tbt">SCALE 1:1</text>
    <text x="{bx + 8}" y="{by + 52}" class="tbt">LBORO · PDE</text>
    <text x="{bx + 100}" y="{by + 52}" class="tbt">MATL: CLAUDE</text>
  </g>'''

    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Andreas Purse. Product design engineer who builds with AI.">
  <defs>
    <pattern id="m" width="20" height="20" patternUnits="userSpaceOnUse"><path d="M20 0H0V20" fill="none" stroke="{t['minor']}" stroke-width="1"/></pattern>
    <pattern id="M" width="100" height="100" patternUnits="userSpaceOnUse"><rect width="100" height="100" fill="url(#m)"/><path d="M100 0H0V100" fill="none" stroke="{t['major']}" stroke-width="1"/></pattern>
    <marker id="a" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 1L10 5L0 9z" fill="{t['accent']}"/></marker>
  </defs>
  <style>
    .z{{font:600 11px {MONO};fill:{t['muted']};text-anchor:middle}}
    .ticks line{{stroke:{t['frame']};stroke-width:1}}
    .name{{font:700 76px {SANS};fill:{t['ink']};letter-spacing:-1.5px}}
    .tag{{font:500 22px {MONO};fill:{t['ink']}}}
    .acc{{fill:{t['accent']}}}
    .sub{{font:500 14px {MONO};fill:{t['muted']};letter-spacing:2px}}
    .cur{{fill:{t['accent']};animation:blink 1.1s steps(1) infinite}}
    .edge{{fill:none;stroke:{t['ink']};stroke-width:2}}
    .thin{{stroke-width:1.2;opacity:.7}}
    .ring{{fill:none;stroke:{t['accent']};stroke-width:1.5;stroke-dasharray:6 8}}
    .spin{{transform-origin:{cx}px {cy}px;animation:spin 24s linear infinite}}
    .cl{{stroke:{t['muted']};stroke-width:1;stroke-dasharray:18 4 3 4}}
    .dim{{stroke:{t['accent']};stroke-width:1.2}}
    .ext{{stroke:{t['muted']};stroke-width:.8}}
    .lbl-bg{{fill:{t['bg']}}}
    .dimt{{font:600 11px {MONO};fill:{t['accent']};text-anchor:middle;letter-spacing:1px}}
    .tb rect,.tb line{{fill:none;stroke:{t['frame']};stroke-width:1}}
    .tbt{{font:600 9.5px {MONO};fill:{t['ink']};letter-spacing:.5px}}
    .lead{{stroke:{t['accent']};stroke-width:1.2;fill:none}}
    .fade{{opacity:0;animation:in .9s ease-out forwards}}
    .d1{{animation-delay:.15s}} .d2{{animation-delay:.45s}} .d3{{animation-delay:.75s}}
    @keyframes in{{from{{opacity:0;transform:translateY(6px)}}to{{opacity:1;transform:none}}}}
    @keyframes blink{{50%{{opacity:0}}}}
    @keyframes spin{{to{{transform:rotate(360deg)}}}}
  </style>
  <rect width="{W}" height="{H}" fill="{t['bg']}"/>
  <rect x="40" y="40" width="{W - 80}" height="{H - 80}" fill="url(#M)"/>
  <rect x="10" y="10" width="{W - 20}" height="{H - 20}" fill="none" stroke="{t['frame']}" stroke-width="1"/>
  <rect x="40" y="40" width="{W - 80}" height="{H - 80}" fill="none" stroke="{t['frame']}" stroke-width="2"/>
  <g class="ticks">{ticks}</g>
  {zones_x}{zones_y}

  <text x="90" y="112" class="sub">PRODUCT DESIGN ENGINEER</text>
  <text x="84" y="190" class="name">Andreas Purse</text>
  <text x="90" y="238" class="tag"><tspan class="acc">&gt;</tspan> I build things with AI.<tspan class="cur">▍</tspan></text>
  <text x="90" y="290" class="sub">HARDWARE · SOFTWARE · BRAND</text>
  <path d="M610 284 H680 L742 218" class="lead"/>
  <circle cx="640" cy="284" r="3" class="acc"/>
  {part}
  {tb}
</svg>
'''


out = Path(__file__).parent / "assets"
out.mkdir(exist_ok=True)
for name, t in THEMES.items():
    (out / f"banner-{name}.svg").write_text(svg(t), encoding="utf-8")
print("ok")

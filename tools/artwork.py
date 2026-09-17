#!/usr/bin/env python3
"""
NOIR ECHELON — project artwork generator.

Emits the vector compositions used across the portfolio and case studies:
interface mockups, typography specimens, device pairs and palette boards.
Vector keeps them razor sharp at any breakpoint and costs a few kilobytes.

    python3 tools/artwork.py
"""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "assets", "img", "work")

PROJECTS = {
    "meridian": {
        "name": "Meridian House",
        "paper": "#0C0B0A", "ink": "#EFE9E0", "dim": "#8A8279",
        "accent": "#C9A87C", "band": "#171512", "muted": "#241F1A",
        "headline": ["Twelve residences.", "One address."],
        "eyebrow": "MERIDIAN HOUSE — MANCHESTER",
        "nav": ["Residences", "Location", "Specification", "Register"],
        "cta": "REGISTER INTEREST",
    },
    "varona": {
        "name": "Atelier Varona",
        "paper": "#F2EEE7", "ink": "#16110F", "dim": "#6E6560",
        "accent": "#7A2E2A", "band": "#E4DCD1", "muted": "#D6CBBD",
        "headline": ["Made to be", "worn for decades."],
        "eyebrow": "ATELIER VARONA — READY TO WEAR",
        "nav": ["Collection", "Atelier", "Fittings", "Cart (0)"],
        "cta": "SHOP THE COLLECTION",
    },
    "calder": {
        "name": "Calder & Roe",
        "paper": "#0A0F0D", "ink": "#ECEFEC", "dim": "#7E8A85",
        "accent": "#9BB5A4", "band": "#0F1613", "muted": "#18211D",
        "headline": ["Patient capital,", "carefully advised."],
        "eyebrow": "CALDER & ROE — PRIVATE WEALTH",
        "nav": ["Approach", "Team", "Insight", "Enquire"],
        "cta": "ARRANGE A CONVERSATION",
    },
}

SERIF = "Cormorant Garamond, Georgia, 'Times New Roman', serif"
SANS = "Inter, Helvetica, Arial, sans-serif"


def esc(text):
    """SVG is XML: a bare ampersand in a client name is a parse error."""
    return (str(text).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


def head(w, h, bg):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" '
        f'width="{w}" height="{h}" role="img">'
        f'<rect width="{w}" height="{h}" fill="{bg}"/>'
    )


def micro(x, y, text, fill, size=11, spacing=3.2, anchor="start", weight="500"):
    return (
        f'<text x="{x}" y="{y}" fill="{fill}" font-family="{SANS}" font-size="{size}" '
        f'letter-spacing="{spacing}" font-weight="{weight}" text-anchor="{anchor}">{esc(text)}</text>'
    )


def serif(x, y, text, fill, size, anchor="start", style="normal", weight="300"):
    return (
        f'<text x="{x}" y="{y}" fill="{fill}" font-family="{SERIF}" font-size="{size}" '
        f'font-weight="{weight}" font-style="{style}" text-anchor="{anchor}">{esc(text)}</text>'
    )


def cover(key, p):
    """Full homepage interface, 16:10."""
    W, H = 1600, 1000
    s = [head(W, H, p["paper"])]
    s.append(
        f'<defs><linearGradient id="g{key}" x1="0" y1="0" x2="1" y2="1">'
        f'<stop offset="0" stop-color="{p["accent"]}" stop-opacity="0.16"/>'
        f'<stop offset="0.6" stop-color="{p["accent"]}" stop-opacity="0.02"/>'
        f'<stop offset="1" stop-color="{p["accent"]}" stop-opacity="0"/></linearGradient>'
        f'<linearGradient id="b{key}" x1="0" y1="0" x2="0" y2="1">'
        f'<stop offset="0" stop-color="{p["band"]}"/>'
        f'<stop offset="1" stop-color="{p["muted"]}"/></linearGradient></defs>'
    )
    s.append(f'<rect width="{W}" height="{H}" fill="url(#g{key})"/>')

    # Browser chrome — a whisper, not a frame
    s.append(f'<rect x="0" y="0" width="{W}" height="54" fill="{p["band"]}" opacity="0.7"/>')
    for cx in (34, 56, 78):
        s.append(f'<circle cx="{cx}" cy="27" r="4.5" fill="{p["dim"]}" opacity="0.45"/>')
    s.append(f'<rect x="120" y="16" width="360" height="22" rx="2" fill="{p["muted"]}" opacity="0.7"/>')
    s.append(micro(136, 31, f'{key}.com', p["dim"], 10, 2.4))

    # Site navigation
    s.append(micro(90, 122, p["name"].upper(), p["ink"], 13, 5.4))
    x = 900
    for label in p["nav"]:
        s.append(micro(x, 122, label.upper(), p["dim"], 10, 2.8))
        x += 150
    s.append(f'<line x1="90" y1="160" x2="{W-90}" y2="160" stroke="{p["ink"]}" stroke-opacity="0.12"/>')

    # Hero type
    s.append(micro(90, 238, p["eyebrow"], p["accent"], 11, 4.2))
    s.append(serif(84, 372, p["headline"][0], p["ink"], 104))
    s.append(serif(84, 482, p["headline"][1], p["ink"], 104, style="italic"))

    # Hero rule + CTA
    s.append(f'<line x1="90" y1="556" x2="430" y2="556" stroke="{p["accent"]}" stroke-opacity="0.75"/>')
    s.append(micro(90, 604, p["cta"], p["ink"], 11, 4.0))
    arrow_x = 90 + len(p["cta"]) * 10.8 + 18
    s.append(f'<path d="M {arrow_x} 600 l 13 0 m -5.5 -5.5 l 5.5 5.5 l -5.5 5.5" '
             f'stroke="{p["accent"]}" fill="none" stroke-width="1.2"/>')

    # Editorial image band
    s.append(f'<rect x="90" y="676" width="620" height="252" fill="url(#b{key})"/>')
    s.append(f'<rect x="90" y="676" width="620" height="252" fill="none" stroke="{p["ink"]}" stroke-opacity="0.08"/>')
    s.append(serif(400, 826, "01", p["accent"], 64, anchor="middle"))

    s.append(f'<rect x="740" y="676" width="360" height="252" fill="{p["muted"]}"/>')
    s.append(micro(772, 716, "SELECTED", p["dim"], 10, 3.0))
    for i in range(4):
        y = 756 + i * 34
        s.append(f'<line x1="772" y1="{y}" x2="1068" y2="{y}" stroke="{p["ink"]}" stroke-opacity="0.10"/>')
        s.append(micro(772, y - 10, ["ONE", "TWO", "THREE", "FOUR"][i], p["ink"], 11, 2.6))

    s.append(f'<rect x="1130" y="676" width="380" height="252" fill="{p["band"]}"/>')
    s.append(serif(1160, 760, "Considered", p["ink"], 40))
    s.append(serif(1160, 806, "in every", p["ink"], 40, style="italic"))
    s.append(serif(1160, 852, "detail.", p["ink"], 40))
    s.append("</svg>")
    return "".join(s)


def typography(key, p):
    """Typography specimen, 4:3."""
    W, H = 1200, 900
    s = [head(W, H, p["paper"])]
    s.append(serif(80, 470, "Aa", p["ink"], 380))
    s.append(f'<line x1="80" y1="524" x2="{W-80}" y2="524" stroke="{p["ink"]}" stroke-opacity="0.14"/>')
    s.append(micro(80, 570, "DISPLAY — 300", p["accent"], 11, 4.0))
    s.append(serif(80, 648, "ABCDEFGHIJKLM", p["ink"], 58))
    s.append(serif(80, 716, "NOPQRSTUVWXYZ", p["dim"], 58))
    s.append(micro(80, 782, "INTERFACE — 400 / 500", p["accent"], 11, 4.0))
    s.append(micro(80, 826, "ABCDEFGHIJKLMNOPQRSTUVWXYZ 0123456789", p["ink"], 20, 2.2, weight="400"))
    s.append(micro(W - 80, 160, p["name"].upper(), p["dim"], 11, 4.0, anchor="end"))
    s.append("</svg>")
    return "".join(s)


def devices(key, p):
    """Two handsets, 4:3."""
    W, H = 1200, 900
    s = [head(W, H, p["band"])]
    for i, ox in enumerate((250, 660)):
        oy = 120 if i == 0 else 180
        s.append(f'<rect x="{ox}" y="{oy}" width="290" height="600" rx="26" fill="{p["paper"]}" '
                 f'stroke="{p["ink"]}" stroke-opacity="0.12"/>')
        s.append(f'<rect x="{ox+112}" y="{oy+16}" width="66" height="7" rx="3.5" fill="{p["ink"]}" opacity="0.14"/>')
        s.append(micro(ox + 28, oy + 74, p["name"].upper(), p["ink"], 9, 3.0))
        s.append(f'<line x1="{ox+28}" y1="{oy+94}" x2="{ox+262}" y2="{oy+94}" stroke="{p["ink"]}" stroke-opacity="0.10"/>')
        if i == 0:
            s.append(serif(ox + 28, oy + 176, p["headline"][0].split(" ")[0], p["ink"], 46))
            s.append(serif(ox + 28, oy + 222, p["headline"][0].split(" ")[-1].strip(".,"), p["ink"], 46, style="italic"))
            s.append(f'<rect x="{ox+28}" y="{oy+266}" width="234" height="180" fill="{p["muted"]}"/>')
            s.append(f'<rect x="{ox+28}" y="{oy+474}" width="234" height="44" fill="{p["accent"]}" opacity="0.92"/>')
            s.append(micro(ox + 145, oy + 501, "ENQUIRE", p["paper"], 9, 3.0, anchor="middle"))
        else:
            for r in range(3):
                y = oy + 120 + r * 150
                s.append(f'<rect x="{ox+28}" y="{y}" width="108" height="128" fill="{p["muted"]}"/>')
                s.append(f'<rect x="{ox+154}" y="{y}" width="108" height="128" fill="{p["band"]}" '
                         f'stroke="{p["ink"]}" stroke-opacity="0.08"/>')
        s.append(f'<rect x="{ox+110}" y="{oy+578}" width="70" height="3" rx="1.5" fill="{p["ink"]}" opacity="0.22"/>')
    s.append("</svg>")
    return "".join(s)


def palette(key, p):
    """Colour and grid board, 4:3."""
    W, H = 1200, 900
    s = [head(W, H, p["paper"])]
    swatches = [("PAPER", p["paper"]), ("INK", p["ink"]), ("ACCENT", p["accent"]),
                ("BAND", p["band"]), ("MUTED", p["muted"])]
    x = 80
    for label, col in swatches:
        s.append(f'<rect x="{x}" y="120" width="190" height="240" fill="{col}" '
                 f'stroke="{p["ink"]}" stroke-opacity="0.14"/>')
        s.append(micro(x, 394, label, p["dim"], 10, 3.0))
        s.append(micro(x, 420, col.upper(), p["ink"], 11, 1.8, weight="400"))
        x += 214
    s.append(f'<line x1="80" y1="486" x2="{W-80}" y2="486" stroke="{p["ink"]}" stroke-opacity="0.14"/>')
    s.append(micro(80, 532, "LAYOUT GRID — 12 COLUMN", p["accent"], 11, 4.0))
    for c in range(12):
        cx = 80 + c * 87
        s.append(f'<rect x="{cx}" y="566" width="62" height="250" fill="{p["accent"]}" opacity="0.10"/>')
    for r in range(5):
        y = 566 + r * 62
        s.append(f'<line x1="80" y1="{y}" x2="{W-80}" y2="{y}" stroke="{p["ink"]}" stroke-opacity="0.07"/>')
    s.append("</svg>")
    return "".join(s)


def main():
    os.makedirs(OUT, exist_ok=True)
    total = 0
    for key, p in PROJECTS.items():
        for suffix, fn in (("cover", cover), ("type", typography),
                           ("devices", devices), ("palette", palette)):
            svg = fn(key, p)
            path = os.path.join(OUT, f"{key}-{suffix}.svg")
            with open(path, "w", encoding="utf-8") as fh:
                fh.write(svg)
            total += len(svg)
            print(f"  work/{key}-{suffix}.svg  {len(svg):>7,} bytes")
    print(f"Total {total:,} bytes")


if __name__ == "__main__":
    main()

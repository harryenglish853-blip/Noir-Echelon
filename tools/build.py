#!/usr/bin/env python3
"""
NOIR ECHELON — static site builder.

Renders the site's shared chrome (head, header, menu, footer, SVG defs) once and
emits fully self-contained HTML files. No dependencies, no runtime framework.

    python3 tools/build.py

Content lives in tools/content.py. Edit the generated HTML directly for small
copy changes; re-run this builder when the global chrome changes.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

SITE = "https://www.noirechelon.com"
BRAND = "Noir Echelon"
TAGLINE = "Web Development &amp; Digital Marketing"
EMAIL = "noirechelon.tech@icloud.com"

NAV = [
    ("Work", "work.html"),
    ("Services", "services.html"),
    ("Studio", "studio.html"),
    ("Contact", "contact.html"),
]

# The NE monogram, redrawn as a hairline-precise vector for interface use.
MONOGRAM = """<svg class="ne-mark" viewBox="0 0 112 80" fill="currentColor" aria-hidden="true" focusable="false"><g><rect x="10" y="8" width="4" height="64"/><rect x="4" y="8" width="16" height="2.6"/><rect x="4" y="69.4" width="16" height="2.6"/><polygon points="14,8 24.5,8 62,66 62,72 52.5,72"/><rect x="58" y="8" width="4" height="64"/><rect x="52" y="8" width="16" height="2.6"/><rect x="52" y="69.4" width="16" height="2.6"/><rect x="62" y="8" width="42" height="3.4"/><rect x="100.6" y="8" width="3.4" height="11"/><rect x="62" y="38.3" width="31" height="2.8"/><rect x="90.2" y="38.3" width="2.8" height="8.4"/><rect x="62" y="68.6" width="46" height="3.4"/><rect x="104.6" y="61" width="3.4" height="11"/></g></svg>"""

# Four-point star from the brand divider — used as a section ornament.
STAR = """<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true" focusable="false" class="ne-star">
  <path d="M12 0c.6 6.3 5.1 10.8 12 12-6.9 1.2-11.4 5.7-12 12-.6-6.3-5.1-10.8-12-12C6.9 10.8 11.4 6.3 12 0z"/>
</svg>"""

ARROW = '<span class="arrow" aria-hidden="true">&#8599;</span>'
ARROW_R = '<span class="arrow" aria-hidden="true">&#8594;</span>'



# Offsets and zone abbreviations are both read from the browser's own tz
# database at runtime, so the strip stays correct through every daylight-saving
# change without a redeploy.
CLOCKS = [
    ("London", "Europe/London"),
    ("Arizona", "America/Phoenix"),
    ("New York", "America/New_York"),
    ("Dubai", "Asia/Dubai"),
    ("Manila", "Asia/Manila"),
]


def clock_strip():
    cells = ""
    for city, tz in CLOCKS:
        cells += f"""
        <div class="clock">
          <p class="clock__city">{city}</p>
          <p class="clock__read">
            <span class="clock__zone" data-zone></span>
            <span class="clock__time" data-tz="{tz}"><span class="sr-only">Local time in {city}</span>--:-- --</span>
          </p>
        </div>"""
    return f'<div class="clocks">{cells}\n      </div>'


def head(meta, root):
    """Document head. `root` is the relative prefix to the site root."""
    title = meta["title"]
    desc = meta["description"]
    canonical = SITE + "/" + meta["path"] if meta["path"] != "index.html" else SITE + "/"
    body_class = meta.get("body_class", "")
    schema = meta.get("schema", "")
    return f"""<!doctype html>
<html lang="en" class="{meta.get('html_class', '')}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canonical}">
<meta name="theme-color" content="#040404">
<meta name="robots" content="{meta.get('robots', 'index, follow, max-image-preview:large')}">

<meta property="og:type" content="{meta.get('og_type', 'website')}">
<meta property="og:site_name" content="{BRAND}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{SITE}/assets/img/og-cover.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Noir Echelon — web development and digital marketing">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{SITE}/assets/img/og-cover.png">

<link rel="icon" href="{root}assets/img/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="{root}assets/img/apple-touch-icon.png">
<link rel="manifest" href="{root}site.webmanifest">

<link rel="preload" href="{root}assets/fonts/playfair-display.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="{root}assets/fonts/inter.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{root}assets/css/noir.css">
<script src="{root}assets/js/noir.js" defer></script>
{schema}
</head>
<body class="{body_class}">
<a class="skip-link" href="#main">Skip to content</a>
<span id="top"></span>
<div class="grain" aria-hidden="true"></div>"""


def loader():
    return f"""
<div class="loader" role="presentation">
  <div class="loader__glow" aria-hidden="true"></div>
  <div class="loader__inner">
    <div class="loader__mark">{MONOGRAM}</div>
    <p class="loader__word">Noir Echelon</p>
    <div class="loader__bar" aria-hidden="true"><i></i></div>
  </div>
</div>"""


def header(active, root):
    links = ""
    for label, href in NAV:
        current = ' aria-current="page"' if href == active else ""
        links += f'\n        <a class="nav-link" href="{root}{href}"{current}>{label}</a>'

    menu_items = ""
    for i, (label, href) in enumerate(NAV, 1):
        menu_items += (
            f'\n        <li class="menu__item"><a class="menu__link" href="{root}{href}">'
            f'<i>0{i}</i>{label}</a></li>'
        )

    return f"""
<header class="site-head">
  <div class="shell site-head__inner">
    <a class="brand" href="{root}index.html" aria-label="Noir Echelon — home">
      <span class="brand__mark">{MONOGRAM}</span>
      <span class="brand__type">Noir Echelon</span>
    </a>

    <nav class="nav nav--desk" aria-label="Primary">{links}
    </nav>

    <a class="btn btn--sm nav__cta" href="{root}contact.html" data-magnetic="0.18">
      <span>Start a project</span>{ARROW}
    </a>

    <button class="menu-btn" type="button" aria-expanded="false" aria-controls="site-menu">
      <span class="menu-btn__label">Menu</span>
      <span class="menu-btn__bars" aria-hidden="true"><i></i><i></i></span>
    </button>
  </div>
</header>

<div class="menu" id="site-menu" aria-hidden="true">
  <nav aria-label="Menu">
    <ul class="menu__list">{menu_items}
    </ul>
  </nav>
  <div class="menu__cta">
    <a class="btn btn--solid" href="{root}contact.html"><span>Start a project</span>{ARROW}</a>
  </div>
  <div class="menu__foot">
    <a class="micro dim" href="mailto:{EMAIL}">{EMAIL}</a>
    <span class="micro dim">{TAGLINE}</span>
  </div>
</div>"""


def cta_band(root, title=None, note=None):
    title = title or "Let's make the first<br>impression count."
    note = note or "Tell us about the project. We reply within one business day."
    return f"""
<section class="section cta-band">
  <div class="cta-band__mark" aria-hidden="true">{MONOGRAM}</div>
  <div class="shell cta-band__inner">
    <div class="grid">
      <div class="col-7">
        <p class="eyebrow"><span class="idx">—</span> Start here</p>
        <h2 class="cta-band__title mt-m" data-reveal>{title}</h2>
      </div>
      <div class="col-4 start-9 flex items-end">
        <p class="dim" style="font-size:var(--fs-small);max-width:34ch" data-reveal>{note}</p>
      </div>
    </div>
    <div class="cta-band__actions">
      <a class="btn btn--solid" href="{root}contact.html" data-magnetic="0.2"><span>Start a project</span>{ARROW}</a>
      <a class="link" href="mailto:{EMAIL}">{EMAIL} {ARROW_R}</a>
    </div>
  </div>
</section>"""


def footer(root):
    return f"""
<footer class="site-foot">
  <div class="site-foot__scene" aria-hidden="true">
    <img src="{root}assets/img/foot-scene.jpg"
         srcset="{root}assets/img/foot-scene-900.jpg 900w, {root}assets/img/foot-scene.jpg 1600w"
         sizes="100vw" alt="" width="1600" height="900" loading="lazy" decoding="async">
  </div>
  <div class="shell">
    <div class="foot-eyebrow">
      <p class="foot-eyebrow__label">Get in touch</p>
      <span class="foot-eyebrow__rule" aria-hidden="true"></span>
    </div>

    {clock_strip()}

    <div class="foot-sign" data-sign>
      <p class="foot-sign__name">Harry English</p>
      <span class="foot-sign__rule" aria-hidden="true"></span>
      <p class="foot-sign__line">Let&rsquo;s build something worth being seen in.</p>
    </div>

    <div class="foot-rule" aria-hidden="true"></div>

    <div class="foot-head">
      <div class="foot-id">
        <span class="foot-id__mark">{MONOGRAM}</span>
        <div>
          <p class="foot-id__name">{BRAND}</p>
          <p class="foot-id__tag">Web development &middot; Digital marketing</p>
        </div>
      </div>
      <div class="foot-reach">
        <a class="foot-mail" href="mailto:{EMAIL}">{EMAIL}</a>
        <a class="to-top" href="#top">Back to top <span class="arrow" aria-hidden="true">&#8593;</span></a>
      </div>
    </div>

    <div class="foot-rule" aria-hidden="true"></div>

    <div class="foot-base">
      <span>&copy; <span data-year>2026</span> {BRAND}</span>
      <nav aria-label="Footer">
        <a href="{root}services.html">Services</a>
        <a href="{root}work.html">Work</a>
        <a href="{root}studio.html">Studio</a>
        <a href="{root}contact.html">Contact</a>
        <a href="{root}privacy.html">Privacy</a>
        <a href="{root}terms.html">Terms</a>
      </nav>
      <span class="foot-base__end" data-localtime></span>
    </div>
  </div>
</footer>
</body>
</html>"""


def page(meta, body, active=None, root=""):
    """Assemble a complete document."""
    parts = [head(meta, root)]
    if meta.get("loader", True):
        parts.append(loader())
    parts.append(header(active or meta["path"], root))
    parts.append('\n<main id="main">')
    parts.append(body)
    parts.append("\n</main>")
    if meta.get("cta", True):
        parts.append(cta_band(root, meta.get("cta_title"), meta.get("cta_note")))
    parts.append(footer(root))
    return "".join(parts)


def write(path, html):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full) or ".", exist_ok=True)
    with open(full, "w", encoding="utf-8") as fh:
        fh.write(html)
    print("  {:<42} {:>7,} bytes".format(path, len(html.encode("utf-8"))))


def main():
    import content
    print("Building Noir Echelon —")
    for spec in content.pages():
        meta, body = spec
        write(meta["path"], page(meta, body, meta.get("active"), meta.get("root", "")))
    print("Done.")


if __name__ == "__main__":
    main()

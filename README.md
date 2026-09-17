# Noir Echelon

The digital flagship for Noir Echelon — web development and digital marketing.

A hand-built static site. No framework, no build pipeline required to deploy, no
runtime dependencies. The whole site loads in **~164 KB across 8 requests**.

---

## Running it

Any static server will do:

```bash
python3 -m http.server 8080      # then open http://localhost:8080
```

There is nothing to install and nothing to compile.

## Deploying it

Upload the repository root as-is. `netlify.toml` carries the security headers and
caching policy; the same values work on Vercel, Cloudflare Pages, S3 + CloudFront
or Nginx:

| Path              | Cache-Control                            |
|-------------------|------------------------------------------|
| `/assets/fonts/*` | `public, max-age=31536000, immutable`    |
| `/assets/img/*`   | `public, max-age=2592000`                |
| `/assets/css,js/*`| `public, max-age=604800`                 |
| `*.html`          | `public, max-age=0, must-revalidate`     |

Point `404.html` at the host's not-found handler, and serve over HTTPS with the
`Strict-Transport-Security` header in `netlify.toml`.

---

## Structure

```
index.html              Home
work.html               Selected work
services.html           Services + investment + FAQ
studio.html             Studio, principles, process
contact.html            Five-step inquiry
privacy.html            Privacy notice (noindex)
404.html
work/*.html             Case studies

assets/css/noir.css     The entire design system, one file
assets/js/noir.js       All behaviour, ~18 KB, no dependencies
assets/fonts/*.woff2    Self-hosted, latin subset, preloaded
assets/img/work/*.svg   Project artwork (vector)

tools/build.py          Renders the pages from shared chrome + content
tools/content.py        Every page's copy and structure
tools/artwork.py        Generates the project artwork
```

### Editing content

For a copy tweak, **edit the HTML directly** — the files are self-contained and
readable.

For anything global (navigation, footer, meta tags, a new page), edit
`tools/content.py` or `tools/build.py` and regenerate:

```bash
python3 tools/build.py      # rewrites every HTML file
python3 tools/artwork.py    # regenerates project artwork
```

Regenerating overwrites hand edits made to the HTML, so pick one approach per
change and keep `tools/content.py` in step.

---

## The design system

Everything is driven by custom properties at the top of `assets/css/noir.css`.

**Colour.** Black is treated as an environment with tonal depth (`--void`
through `--noir-4`), not a flat background. Champagne (`--gold`) is used like
jewellery — hairlines, small capitals, arrows, one solid button — never as a
large fill.

**Type.** Cormorant Garamond for display, Inter for interface. Sizes are fluid
`clamp()` values; small capitals carry `0.26em`–`0.3em` tracking.

**Motion.** Transform and opacity only. Reveals are driven by
`IntersectionObserver` with an explicit sweep for anything already on screen, so
a visitor who never scrolls still sees a finished page. Everything is disabled
under `prefers-reduced-motion`, and the magnetic buttons, parallax and custom
cursor also switch off on coarse pointers and low-core devices.

**The loader** runs once per session (1.4 s maximum), is skippable by click or
`Esc`, and never runs for reduced-motion visitors.

---

## Standards this build holds to

- **Accessibility** — one `h1` per page, no heading-level jumps, labelled
  controls, a visible champagne focus ring, a skip link, a focus-trapped menu,
  live-region form feedback. All body text measures at least 6.3:1 against the
  background (WCAG AA is 4.5:1).
- **Performance** — self-hosted preloaded woff2, vector artwork, lazy-loaded
  below-fold images, no third-party scripts, no layout-shifting webfont swap.
- **SEO** — canonical URLs, unique titles and descriptions, Open Graph and
  Twitter cards, `ProfessionalService` structured data, `sitemap.xml`,
  `robots.txt`.
- **Privacy** — no trackers, no cookie banner, no third-party requests at all.

Verified in Chromium at 1440, 1280 and 390 px: no console errors, no horizontal
overflow, no unrevealed content above the fold, and every interaction
(menu, accordion, five-step form with validation) exercised end to end.

---

## Before you go live

See **[CONTENT.md](CONTENT.md)**. The portfolio, the operating facts and the
contact details in this build are **placeholders** and must be replaced with
real ones.

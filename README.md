# Noir Echelon

The digital flagship for Noir Echelon — web development and digital marketing.

A hand-built static site. No framework, no build pipeline required to deploy, no
runtime dependencies. The home page loads in **~512 KB across 8 requests**;
interior pages, which skip the brand hero, are around 200 KB. The brand reveal
video is lazy-loaded and never counts against that first paint.

---

## Running it

Any static server will do:

```bash
python3 -m http.server 8080      # then open http://localhost:8080
```

There is nothing to install and nothing to compile.

## Deploying it

There is no build step. Any static host serves the repository root as-is.

### Vercel (configured)

`vercel.json` is already in the repo — security headers, caching policy, no
framework, no build command. Two ways to ship it:

**From the dashboard (recommended).** At vercel.com, *Add New → Project*, import
`harryenglish853-blip/Noir-Echelon` and pick this branch. Framework Preset:
**Other**. Build Command: leave empty. Output Directory: leave empty (the repo
root is the site). Vercel reads `vercel.json` and every push redeploys.

**From the CLI.**

```bash
npm i -g vercel     # or: npx vercel@latest
vercel login
vercel              # preview deployment
vercel --prod       # production
```

Notes for this site specifically:

- `404.html` at the root is picked up automatically as the not-found page.
- The brand reveal scrubs by seeking, which needs HTTP range requests. Vercel
  serves those natively — nothing to configure.
- `cleanUrls` is deliberately **off**, so `/work.html` is served directly with no
  redirect hop. Internal links, canonical tags and `sitemap.xml` all use the
  `.html` form consistently. If you would rather have `/work`, set
  `"cleanUrls": true` and say so — the links, canonicals and sitemap need
  updating in the same pass to stay consistent.
- `.vercelignore` keeps `tools/` and the docs out of the deployment.

### Other hosts

`netlify.toml` carries the same headers and caching policy, and the values below
work on Cloudflare Pages, S3 + CloudFront or Nginx:

| Path              | Cache-Control                            |
|-------------------|------------------------------------------|
| `/assets/fonts/*` | `public, max-age=31536000, immutable`    |
| `/assets/video/*` | `public, max-age=31536000, immutable`    |
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
contact.html            Inquiry form
privacy.html            Privacy notice (noindex)
terms.html              Terms of use (noindex)
404.html
work/*.html             Case studies

assets/css/noir.css     The entire design system, one file
assets/js/noir.js       All behaviour, ~18 KB, no dependencies
assets/fonts/*.woff2    Self-hosted, latin subset, preloaded
assets/img/work/*.svg   Project artwork (vector)
assets/video/reveal-*   Scroll-scrubbed brand reveal (VP9 + H.264)

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

**Colour.** The system has two halves. Noir is the default: black as an
environment with tonal depth, champagne (`--gold`) used like jewellery — hairlines,
small capitals, arrows — never as a large fill. Paper is the light half: warm ivory
with a bronze accent.

Components never name a palette colour directly. They read semantic tokens
(`--bg`, `--fg`, `--fg-2`, `--fg-3`, `--accent`, `--hair`), and adding the `paper`
class to a section redefines those tokens so everything inside re-themes itself —
buttons, rules, eyebrows and rows included. Alternating the two is what gives the
page its editorial rhythm.

**Type.** Playfair Display for display, Inter for interface. Sizes are fluid
`clamp()` values; small capitals carry `0.26em`–`0.3em` tracking.

**Motion.** Transform and opacity only. Reveals use `IntersectionObserver` as a
fast path with a throttled scroll sweep as the guarantee — the observer alone
proved unreliable both before webfonts settle the layout and for elements
scrolled into view in one jump. The sweep skips anything already shown and
removes its own listeners once every target has fired. Everything is disabled
under `prefers-reduced-motion`, and the magnetic buttons, parallax and custom
cursor also switch off on coarse pointers and low-core devices.

**The loader** runs once per session (1.4 s maximum), is skippable by click or
`Esc`, and never runs for reduced-motion visitors.

**The brand reveal** (`#reveal`) is a scroll-scrubbed video: a tall track gives
the scroll distance, the stage pins inside it, and the visitor's scroll position
drives `currentTime` — the video never plays itself. It is encoded with a
keyframe every 8 frames so seeking is cheap, served as VP9 to browsers that take
it and H.264 to the rest, and fetched only when the section is within one and a
half screens.

The footage is never cropped. `.reel__media` carries the video's own 16:9 ratio
and grows until whichever dimension runs out first, so the complete lockup is
visible from an ultrawide desktop to a phone in portrait — the black around it on
tall screens is letterbox, not a mistake, and it reads as one field because the
footage is black too. Three source tiers are chosen from how many device pixels
the frame will actually occupy (1920 / 1280 / 854), with phones pinned to the
small cut whatever their pixel ratio claims, to save close to a megabyte on
cellular. Reduced motion, a saver connection or no video support collapses
the track and shows the poster still instead, costing nothing.

Note for hosting: seeking requires HTTP range requests. Every real static host
supports them (Vercel, Netlify, Cloudflare, S3, nginx); Python's
`http.server` does not, so use `npx serve` or similar if you preview locally.

---

## Standards this build holds to

- **Accessibility** — one `h1` per page, no heading-level jumps, labelled
  controls, a visible champagne focus ring, a skip link, a focus-trapped menu,
  live-region form feedback. Every text colour clears WCAG AA on both the noir
  and paper backgrounds (4.96:1 at the lowest, against a 4.5:1 requirement).
  Where type sits over the photograph — the footer and the reveal's opening
  plate — contrast is measured against the brightest pixel actually behind each
  element rather than assumed, and the scrims are banded to hold it: 5.37:1 at
  the lowest there. Every control clears the 24px minimum target size (WCAG 2.2
  SC 2.5.8); links inline in a sentence take the exception and are left at their
  natural size.
- **Performance** — self-hosted preloaded woff2, vector artwork, lazy-loaded
  below-fold images, no third-party scripts, no layout-shifting webfont swap.
- **SEO** — canonical URLs, unique titles and descriptions, Open Graph and
  Twitter cards, `ProfessionalService` structured data, `sitemap.xml`,
  `robots.txt`.
- **Privacy** — no trackers, no cookie banner, no third-party requests at all.
- **Licensing** — no third-party code of any kind. Fonts are SIL OFL with their
  licences bundled at `assets/fonts/*-OFL.txt`. See **[NOTICE.md](NOTICE.md)**
  for full asset provenance and the questions still open before launch.

Verified in Chromium at 1440, 1280 and 390 px: no console errors, no horizontal
overflow, no unrevealed content above the fold, and every interaction
(menu, accordion, inquiry form with validation) exercised end to end, and every
reveal target confirmed to fire on a normal scroll through all ten pages.

---

## Before you go live

See **[CONTENT.md](CONTENT.md)**. The portfolio, the operating facts and the
contact details in this build are **placeholders** and must be replaced with
real ones.

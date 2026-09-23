# Before launch — what must be replaced

This build ships with **placeholder content** so the structure, tone and layout
can be reviewed as a finished thing. Publishing it unchanged would claim clients
and commitments that do not exist yet. Work through this list first.

---

## 1. The portfolio — real, and sourced

The portfolio is genuine client work, written from the project repositories
rather than invented:

| Project | Source |
|---|---|
| Quik Burrito — Anthem, AZ | `harryenglish853-blip/Quik-Burrito-KaLeb-Owner`, branch `claude/quik-burrito-website-y8jtv1` |
| The Ol' Clip Joint — Phoenix, AZ | `harryenglish853-blip/pho`, branch `claude/ol-clip-joint-appointments-qkr1n1` |

Every claim in the case studies traces to those repositories' own READMEs and
code. The "The result" chapters describe **what shipped**, not what it earned —
each one carries an HTML comment marking where evidenced figures go. Do not add
numbers you cannot show a client.

Cards and case-study figures are **screenshots of the running sites**, captured
by building and serving each project locally — not mockups, and not stock.

Two things worth doing when you have them:

- **Live links.** If the sites are public, the cards can link out to them
  alongside the case study.
- **Quik Burrito photography.** That repo ships one real food photo (the birria
  tacos). Every other image slot renders a blur placeholder, which is visible in
  the screenshot. Real photography improves that site and this portfolio card at
  the same time.

Artwork lives in `assets/img/work/` and is referenced by the `img` key in
`PROJECTS` (`tools/content.py`).

## 2. The operating facts — check each one

`tools/content.py` → `FACTS`, shown on the home, services and studio pages:

- `4–10 weeks, typical build`
- `01 senior team, no handoffs`
- `90+ Core Web Vitals target`
- `24h inquiry response`

These are promises to prospective clients. Keep only the ones you will honour.

## 3. Pricing language — check it

`services.html` (`SERVICE_DETAIL` / the Investment section) and the FAQ state
that most website engagements start at a mid five-figure sum. Adjust to your
actual floor, or remove the figure.

## 4. Contact details

**Email — done.** `EMAIL` in `tools/build.py` is `noirechelon.tech@icloud.com`.
It drives every mailto on the site, the structured data, and the address the
inquiry form composes to.

**Domain — done.** `SITE` in `tools/build.py` is `https://noirechelon.tech`.
It is the single source for every canonical tag, the Open Graph URLs, the
structured data and `sitemap.xml`, all of which the build now generates — so
changing that one line and re-running `python3 tools/build.py` moves the whole
site. `sitemap.xml` and `robots.txt` used to be hand-maintained, which is how
they came to disagree with the pages; they are generated now and cannot drift.

The sitemap lists only indexable pages. `privacy.html`, `terms.html` and
`404.html` are excluded deliberately — the first two carry `noindex` while they
are unreviewed drafts. When a lawyer has signed them off, drop them from
`SITEMAP_SKIP` in `tools/build.py` and remove the noindex.

**Phone — removed.** The build carried a placeholder `+44` number that nothing
rendered any more. If you want a phone number on the site, add it back
deliberately rather than shipping a fake one.

**Social links.** The footer no longer carries Instagram or LinkedIn links.
Add them to `footer()` in `tools/build.py` when the accounts exist.

## 5. Wire up the inquiry form — required

The form appears twice (the home page's closing section and `contact.html`) and
both are rendered from `enquiry_form()` in `tools/content.py`.

Until an endpoint is set, Send composes the inquiry as an email, opens the
visitor's mail app and copies the text to their clipboard. That is a working
fallback, not a finished state — it depends on the visitor actually sending the
email. Set a real endpoint before launch:

```html
<form class="enquiry enquiry-form" data-endpoint="https://formspree.io/f/xxxxxxx" ...>
```

With an endpoint set, the form POSTs `FormData` and expects a 2xx response;
anything else re-enables the button and points at the fallback email. Formspree,
Basin, Netlify Forms or your own handler all work. Test a real submission before
launch, and add spam protection (honeypot or captcha) if the inbox gets noisy.

## 5b. Client testimonials — required or remove

The two cards in the Client Experience section are written as visible
placeholders. Replace them with verified reviews (`TESTIMONIALS` in
`tools/content.py`) or delete the section. Never publish an invented quote.

## 6. Legal, licensing and provenance

**Read [NOTICE.md](NOTICE.md) before launch.** It inventories every asset the
site ships, states what is settled (code written from scratch, zero third-party
libraries, zero external requests, fonts under the SIL OFL with their licences
now bundled) and lists what is not — permission to publish client work, rights
in the photograph of Matt, the brand reveal video's licence, and the status of
the Noir Echelon lockup.

## 6b. Privacy and terms — have them reviewed

`privacy.html` is written as a readable starting point, not legal advice. Have it
checked against your jurisdiction, and make its claims true — it currently states
there are no advertising trackers on the site, which is only true while that
remains the case.

## 7. Social sharing image — optional

`assets/img/og-cover.png` (1200×630) is cut from the supplied brand lockup.
Replace it if you want the shared preview to show work instead of the logo.

---

## Launch checklist

- [x] Real projects in, placeholder projects out
- [ ] Every claim in `FACTS` and the FAQ verified
- [ ] Real domain in `SITE`, then `python3 tools/build.py`
- [x] Real email wired through the site
- [ ] Real domain in `SITE`, sitemap and robots
- [ ] Form endpoint wired and tested end to end
- [ ] NOTICE.md worked through; client permissions obtained in writing
- [ ] Privacy notice and terms reviewed by a lawyer
- [ ] `sitemap.xml` and `robots.txt` pointing at the live domain
- [ ] Analytics chosen (and the privacy notice updated to match)
- [ ] HTTPS with HSTS, 404 handler mapped to `404.html`
- [ ] Lighthouse run on the deployed URL, not localhost

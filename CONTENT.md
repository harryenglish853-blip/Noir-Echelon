# Before launch — what must be replaced

This build ships with **placeholder content** so the structure, tone and layout
can be reviewed as a finished thing. Publishing it unchanged would claim clients
and commitments that do not exist yet. Work through this list first.

---

## 1. The portfolio — required

`Meridian House`, `Atelier Varona` and `Calder & Roe` are **invented** projects.
They demonstrate the case-study format; they are not work that was delivered.

Replace, per project:

| What | Where |
|---|---|
| Name, sector, scope, year, summary | `tools/content.py` → `PROJECTS` |
| Case-study chapters | `tools/content.py` → `CASES` |
| Artwork (4 images each) | `assets/img/work/<key>-{cover,type,devices,palette}.svg` |

The artwork is generated vector placeholder. Swap in real screenshots — export
at 1600×1000 for covers and 1200×900 for detail figures, as AVIF or WebP with a
JPEG fallback, and update the `<img>` `src`, `width` and `height`.

**Do not publish outcome figures you cannot evidence.** Each case study's
"The result" chapter carries an HTML comment marking where verified numbers go.
Until you have them, describe what was delivered rather than what it earned.

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

**Domain — still a placeholder.** `SITE` in `tools/build.py` is
`https://www.noirechelon.com`, and it sets every canonical tag, the Open Graph
URLs and `sitemap.xml`. If the live domain is different, change it there and
re-run `python3 tools/build.py`, then update `robots.txt` and `sitemap.xml` to
match. Canonicals pointing at a domain you do not own will hurt you in search.

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

## 6. Privacy notice — have it reviewed

`privacy.html` is written as a readable starting point, not legal advice. Have it
checked against your jurisdiction, and make its claims true — it currently states
there are no advertising trackers on the site, which is only true while that
remains the case.

## 7. Social sharing image — optional

`assets/img/og-cover.png` (1200×630) is cut from the supplied brand lockup.
Replace it if you want the shared preview to show work instead of the logo.

---

## Launch checklist

- [ ] Real projects in, placeholder projects out
- [ ] Every claim in `FACTS` and the FAQ verified
- [ ] Real domain in `SITE`, then `python3 tools/build.py`
- [x] Real email wired through the site
- [ ] Real domain in `SITE`, sitemap and robots
- [ ] Form endpoint wired and tested end to end
- [ ] Privacy notice reviewed
- [ ] `sitemap.xml` and `robots.txt` pointing at the live domain
- [ ] Analytics chosen (and the privacy notice updated to match)
- [ ] HTTPS with HSTS, 404 handler mapped to `404.html`
- [ ] Lighthouse run on the deployed URL, not localhost

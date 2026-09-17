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

## 4. Contact details — required

`tools/build.py`:

```python
SITE  = "https://www.noirechelon.com"     # real domain
EMAIL = "studio@noirechelon.com"          # real inbox
PHONE_DISPLAY = "+44 (0) 000 000 0000"    # real number, or delete the footer row
PHONE_HREF    = "+440000000000"
```

Also update the Instagram and LinkedIn URLs in `footer()`, or remove those links.

## 5. Wire up the inquiry form — required

`contact.html` currently validates and shows its success state without sending
anywhere. Set the endpoint on the form:

```html
<form id="inquiry-form" data-endpoint="https://formspree.io/f/xxxxxxx" ...>
```

The form POSTs `FormData` and expects a 2xx response; anything else re-enables
the button and surfaces the fallback email. Formspree, Basin, Netlify Forms or
your own handler all work. Test a real submission before launch, and add
server-side spam protection (honeypot or captcha) if the inbox gets noisy.

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
- [ ] Real email, phone and social links
- [ ] Form endpoint wired and tested end to end
- [ ] Privacy notice reviewed
- [ ] `sitemap.xml` and `robots.txt` pointing at the live domain
- [ ] Analytics chosen (and the privacy notice updated to match)
- [ ] HTTPS with HSTS, 404 handler mapped to `404.html`
- [ ] Lighthouse run on the deployed URL, not localhost

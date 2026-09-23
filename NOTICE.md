# Provenance, licensing and open questions

An inventory of everything this site ships, where it came from, and what is
settled versus unresolved. Written so the unresolved items are visible rather
than buried.

**This is not legal advice.** It is an engineering audit. The items under
"Unresolved" need a decision from you, and in places a lawyer.

---

## Settled

### Code

`assets/css/noir.css`, `assets/js/noir.js`, every `.html` file, and the build
tooling in `tools/` were written from scratch for this project. No code was
copied from another site, template or tutorial.

**There are no third-party libraries.** No React, no jQuery, no GSAP, no
analytics SDK, no cookie banner vendor — the dependency count is zero. Nothing
here carries a copyleft obligation, an attribution requirement or a supply-chain
risk, because nothing here is anyone else's code.

### No external requests

The site makes **no requests to any third-party domain at runtime**. Fonts,
images and video are all self-hosted. There is no Google Fonts call, no CDN, no
tracking pixel, no embedded map or social widget.

Two consequences worth knowing:

- Nothing on this site sets a third-party cookie or transmits a visitor's IP to
  anyone but your own host. That is why the privacy notice can say what it says,
  and it is a materially better position than most marketing sites.
- Adding any embed later — a YouTube video, a Google Map, a chat widget, a
  Meta pixel — changes that, and the privacy notice would need updating to match.

### Fonts

| Font | Licence | Copyright |
|---|---|---|
| Inter | SIL Open Font License 1.1 | 2020 The Inter Project Authors |
| Playfair Display | SIL Open Font License 1.1 | 2017 The Playfair Display Project Authors |
| Mrs Saint Delafield | SIL Open Font License 1.1 | 2011 Brian J. Bonislawsky, Astigmatic |

All three licences permit self-hosting and commercial use. The OFL requires the
licence travel with the font files, which was **not** the case until now —
the full texts are bundled at `assets/fonts/Inter-OFL.txt`,
`assets/fonts/PlayfairDisplay-OFL.txt` and
`assets/fonts/MrsSaintDelafield-OFL.txt`. Keep them there when you deploy.

Mrs Saint Delafield is the script face used for the "Harry English" signature in
the footer. It is a **typeface**, not a scan or trace of a handwritten
signature, so it carries no third-party handwriting rights — but note that it is
also not a legally distinctive mark. It is a decorative sign-off, not a
signature that should ever be presented as executing a document.

Playfair Display carries a Reserved Font Name. You may use and redistribute it;
you may not release a *modified* version of the font under that name. The files
here are Google's own latin subsets, unmodified.

---

## Unresolved — these need your decision

### 1. Permission to show client work

The portfolio publishes screenshots of Quik Burrito's and The Ol' Clip Joint's
websites, their business names, addresses and phone numbers, and describes the
engagements.

You built these sites, but **building a site does not by itself grant the right
to publish the client's name and marks in your own marketing.** Whether it does
depends on what your agreement with each client says. If there was no written
agreement, ask for permission in writing. It is a short email and it removes the
whole question.

Their names and logos are their trademarks, not yours. Showing them to identify
work you did is normally fine; presenting them so as to imply endorsement or
partnership is not.

### 2. The photograph of Matt

`assets/img/work/ol-clip-joint-detail.jpg` shows an identifiable person
mid-shave, and `ol-clip-joint-film.jpg` is a frame from the shop film.

This is **not only a copyright question**. Using a recognisable person's image
in commercial marketing generally requires their permission, separately from
whoever owns the photograph. Two things to confirm: who took the photographs and
on what terms, and whether Matt has agreed to appear in *your* promotional
material as well as his own.

If either answer is unclear, the case study works without those two images.

### 3. The brand reveal video

`assets/video/reveal-*` is re-encoded from the file you supplied. Its original
filename indicated it came from an AI video generator.

Confirm what that tool's terms say about commercial use, and whether they apply
to the plan you were on when you generated it. Some tools restrict commercial
use on free tiers, some require attribution, and some grant full rights. This is
a five-minute check of the terms you already agreed to, and worth doing before
the site fronts a business.

### 3b. The footer background image

`assets/img/foot-scene.jpg` (and its 900px variant) is resized and compressed
from the image you supplied for the footer. It appears to be AI-generated, which
puts it in the same category as the reveal video above: **check the generator's
terms for commercial use** on the plan you produced it under.

Two further points, because this image is different in kind from the video:

- It **depicts people**. Faces produced by an image generator are usually not
  real individuals, but they can resemble one closely enough to draw a
  complaint, and some generators' terms specifically bar using outputs to
  suggest a person's endorsement. Nothing on the page names or endorses anyone,
  which is the right side of that line.
- As noted in §4 below, purely machine-generated images may not be protectable
  by copyright in several jurisdictions. You can use it; you may not be able to
  stop someone else using the same output.

If either check comes back unfavourable, the footer degrades cleanly — removing
the `.site-foot__scene` block leaves a plain black footer with the clocks and
signature intact.

### 4. The Noir Echelon lockup

`assets/img/brand-hero*.png`, `og-cover.png`, `icon-512.png` and
`apple-touch-icon.png` are all derived from the logo image you supplied. The
`NE` monogram in the navigation and loader is a vector I drew to match it.

If the logo was commissioned, check the designer assigned the copyright to you
rather than licensing it. If it was AI-generated, note that in several
jurisdictions — the US among them — purely machine-generated images may not be
protectable by copyright at all. That does not stop you using it; it may stop
you stopping someone else from using it. If the mark matters to the business,
a trademark filing protects the name and logo in a way copyright will not.

### 5. Claims the site makes

These appear as statements of fact and could be held against you:

| Claim | Where |
|---|---|
| "4–10 weeks, typical build" | home, services, studio |
| "01 — senior team, no handoffs" | home, services, studio |
| "90+ Core Web Vitals target" | home, services, studio |
| "24h inquiry response" / "within one business day" | home, contact, services, work |
| "Most website engagements start at a mid five-figure sum" | services, FAQ |
| "Domains, hosting, code, design files, analytics and ad accounts are in your name from day one" | studio, FAQ |

None are unreasonable. All are promises. Keep the ones you will honour and
delete the rest — an unmet published promise is the easiest kind of dispute to
avoid and the hardest to argue away once someone has relied on it.

### 6. Legal pages

`privacy.html` and `terms.html` are **drafts written to be readable, not
reviewed by a lawyer**. They need checking against the law where you and your
clients operate — in Arizona that includes the state consumer-protection
position, and if you ever take an EU or UK client, GDPR/UK-GDPR obligations
attach to the enquiry data regardless of where you are.

The inquiry form collects a name, email, phone and free-text business detail.
That is personal data. Decide how long you keep it, where it lives, and who can
read it, and make the privacy notice say that truthfully.

#!/usr/bin/env python3
"""
NOIR ECHELON — site content.

Every page body lives here so structure and copy stay in one reviewable place.
Run tools/build.py to render these into static HTML.

NOTE ON PLACEHOLDER CONTENT
---------------------------
The three portfolio projects, the operating facts and the contact details are
PLACEHOLDERS. They are written to demonstrate structure and tone, not to claim
work that has been delivered. Replace them with real projects, real numbers and
real contact details before the site goes live. See CONTENT.md.
"""

from build import ARROW, ARROW_R, EMAIL, MONOGRAM, SITE, STAR

# ---------------------------------------------------------------------------
# Shared fragments
# ---------------------------------------------------------------------------

def eyebrow(idx, label):
    return f'<p class="eyebrow"><span class="idx">{idx}</span> {label}</p>'


def lines(*rows):
    """Headline rows that rise into place, one after another."""
    out = []
    for i, row in enumerate(rows):
        out.append(f'<span class="reveal-line" style="--d:{i * 110}ms"><span>{row}</span></span>')
    return "".join(out)


PROJECTS = [
    {
        "slug": "quik-burrito",
        "key": "quik-burrito",
        "name": "Quik Burrito",
        "sector": "Restaurant &middot; Anthem, Arizona",
        "scope": "Website, menu, locations &amp; reviews",
        "year": "2026",
        "summary": "A conversion-first restaurant site whose homepage is one continuous "
                   "scroll-scrubbed journey through the food, the kitchen and the people, "
                   "ending on the order button.",
        "img": "quik-burrito-cover.jpg",
        "alt": "Birria tacos pulled apart over consommé, from the Quik Burrito site",
    },
    {
        "slug": "pho-thanh",
        "key": "pho-thanh",
        "name": "Ph&#7903; Th&agrave;nh",
        "sector": "Vietnamese restaurant &middot; Phoenix",
        "scope": "Single-page scroll story &amp; full menu system",
        "year": "2026",
        "summary": "One photograph, layered on itself and masked ingredient by ingredient, "
                   "so that scrolling takes the bowl apart and puts the whole menu within "
                   "reach underneath it.",
        "img": "pho-thanh-cover.jpg",
        "alt": "A bowl of ph\u1edf suspended mid-air, beef and garnishes lifting away from the broth",
    },
    {
        "slug": "ol-clip-joint",
        "key": "ol-clip-joint",
        "name": "The Ol&rsquo; Clip Joint",
        "sector": "Barbershop &middot; Phoenix",
        "scope": "Website &amp; confirm-first appointment line",
        "year": "2026",
        "summary": "A booking system built on one rule: a request is not an appointment "
                   "until the barber says so. Nothing on the site can put a client in the "
                   "chair on its own.",
        "img": "ol-clip-joint-cover.jpg",
        "alt": "A hot-towel shave in progress at The Ol' Clip Joint in Phoenix",
    },
]


def project_by(slug):
    for p in PROJECTS:
        if p["slug"] == slug:
            return p
    raise KeyError(slug)


def work_item(p, root="", tall=False, index="01"):
    cls = "work-item work-item--tall" if tall else "work-item"
    return f"""
<article class="{cls}" data-reveal>
  <a class="work-item__link" href="{root}work/{p['slug']}.html" data-cursor="view"
     aria-label="{p['name']} — view case study">
    <div class="work-item__frame">
      <img class="work-item__media" src="{root}assets/img/work/{p['img']}"
           alt="{p['alt']}" loading="lazy" decoding="async" width="1600" height="1000">
    </div>
    <div class="work-item__head">
      <div>
        <h3 class="work-item__title">{p['name']}</h3>
        <p class="work-item__sub">{p['sector']} &middot; {p['scope']}</p>
      </div>
      <span class="micro work-item__cta">View case study {ARROW_R}</span>
    </div>
  </a>
</article>"""


FAQ = [
    ("What does a project with you cost?",
     "Most website engagements start at a mid five-figure sum, and e-commerce or "
     "multi-market builds sit above that. Marketing retainers are monthly and sized "
     "to the channel, not to a package. We give you a fixed price after the first "
     "conversation, before any work begins — never a range that quietly widens."),
    ("How long does it take?",
     "A focused site is typically four to ten weeks from kick-off to launch. Larger "
     "builds run longer, and we will tell you that at the outset rather than "
     "discovering it in month three. You receive a dated plan with every milestone "
     "on it, and we hold ourselves to it."),
    ("Who actually does the work?",
     "The people you meet. We are a small senior team by design — no account layer, "
     "no junior handoff, no outsourcing to an offshore production line. The person "
     "who designs your site is the person who answers your email about it."),
    ("What happens after launch?",
     "Launch is the beginning of the useful data. We monitor performance, watch how "
     "people actually move through the site, and improve it. Care plans cover "
     "hosting, security, backups, performance budgets and a named contact. You are "
     "never left with a site nobody knows how to change."),
    ("Do we own everything?",
     "Yes. Domains, hosting, code, design files, analytics and ad accounts are in "
     "your name from day one. If you ever leave, you leave with everything — that is "
     "written into the contract, not promised in a meeting."),
    ("Will you work with our existing team?",
     "Often. We work alongside in-house marketers, developers and agencies, and we "
     "are straightforward about where our responsibility starts and stops. Good work "
     "does not require us to own every part of it."),
]


def faq_block(start=1):
    items = ""
    for i, (q, a) in enumerate(FAQ, start):
        items += f"""
  <div class="acc__item">
    <h3>
      <button class="acc__btn" type="button" aria-expanded="false" aria-controls="faq-{i}" id="faq-btn-{i}">
        <span>{q}</span>
        <span class="acc__sign" aria-hidden="true"></span>
      </button>
    </h3>
    <div class="acc__panel" id="faq-{i}" role="region" aria-labelledby="faq-btn-{i}">
      <div><p>{a}</p></div>
    </div>
  </div>"""
    return f'<div class="acc mt-l">{items}\n</div>'


FACTS = [
    ("4&ndash;10", "Weeks, typical build"),
    ("01", "Senior team, no handoffs"),
    ("90+", "Core Web Vitals target"),
    ("24h", "Inquiry response"),
]


def facts_block():
    cells = "".join(
        f'<div class="fact" data-reveal><p class="fact__val">{v}</p><p class="fact__lbl">{l}</p></div>'
        for v, l in FACTS
    )
    return f'<div class="facts mt-l" data-stagger="110">{cells}</div>'


PROCESS = [
    ("01", "Discovery", "We learn your business, customers, goals, competitors "
     "and positioning."),
    ("02", "Strategy", "We shape the user journey, messaging, conversion plan "
     "and creative direction."),
    ("03", "Design", "We art-direct a premium interface built around clarity, "
     "emotion and trust."),
    ("04", "Development", "We turn the approved direction into a responsive, "
     "optimised experience."),
    ("05", "Launch + Growth", "We launch, refine, measure and improve the system "
     "as your business grows."),
]


def process_block():
    steps = "".join(
        f"""
    <div class="row-link" data-reveal style="cursor:default">
      <span class="row-link__idx">{n}</span>
      <span class="row-link__name">{name}</span>
      <span class="row-link__desc">{body}</span>
      <span class="row-link__arrow"></span>
    </div>"""
        for n, name, body in PROCESS
    )
    return f'<div class="rows" data-stagger="80">{steps}\n  </div>'


# ---------------------------------------------------------------------------
# Client experience
# ---------------------------------------------------------------------------
# PLACEHOLDER CONTENT — these two cards are written as placeholders on purpose.
# Replace them with verified reviews from real clients, or delete the section.
# Never publish an invented testimonial.

TESTIMONIALS = [
    ("Client testimonial placeholder. Replace this with a verified review from a "
     "real Noir Echelon client.", "Client name", "Business name"),
    ("Client testimonial placeholder. Use this area for a specific result, "
     "experience, or transformation.", "Client name", "Business name"),
]


def testimonials_block():
    cards = ""
    for text, name, biz in TESTIMONIALS:
        cards += f"""
      <figure class="quote" data-reveal>
        <span class="quote__mark" aria-hidden="true">&ldquo;</span>
        <blockquote class="quote__text">{text}</blockquote>
        <figcaption class="quote__who">
          <p class="quote__name">{name}</p>
          <p class="quote__biz">{biz}</p>
        </figcaption>
      </figure>"""
    return f'<div class="quotes" data-stagger="120">{cards}\n    </div>'


# ---------------------------------------------------------------------------
# Inquiry form
# ---------------------------------------------------------------------------

SERVICE_OPTIONS = ["Web Design", "Web Development", "Digital Marketing",
                   "Local SEO", "Website Management", "Something else"]
INVESTMENT_OPTIONS = ["Under $10k", "$10k – $25k", "$25k – $60k", "$60k +",
                      "Monthly retainer", "Not sure yet"]


def select_field(name, label, placeholder, options):
    opts = "".join(f'<option value="{o}">{o}</option>' for o in options)
    return f"""
        <div class="field--line">
          <label for="{name}">{label}</label>
          <select id="{name}" name="{name}">
            <option value="" selected>{placeholder}</option>
            {opts}
          </select>
        </div>"""


def enquiry_form(root=""):
    """The single-screen inquiry. Set data-endpoint to post it somewhere."""
    return f"""
    <form class="enquiry enquiry-form" novalidate data-endpoint="" data-mailto="{EMAIL}">
      <div class="enquiry__grid">
        <div class="field--line">
          <label for="name">Name</label>
          <input type="text" id="name" name="name" autocomplete="name"
                 placeholder="Your name" data-required>
        </div>
        <div class="field--line">
          <label for="company">Company</label>
          <input type="text" id="company" name="company" autocomplete="organization"
                 placeholder="Business name">
        </div>
        <div class="field--line">
          <label for="email">Email</label>
          <input type="email" id="email" name="email" autocomplete="email"
                 placeholder="you@company.com" data-required>
        </div>
        <div class="field--line">
          <label for="phone">Phone</label>
          <input type="tel" id="phone" name="phone" autocomplete="tel"
                 placeholder="(000) 000-0000">
        </div>
        {select_field('service', 'Service', 'Select a service', SERVICE_OPTIONS)}
        {select_field('investment', 'Investment', 'Select range', INVESTMENT_OPTIONS)}
        <div class="field--line enquiry__full">
          <label for="project">Tell us about your project</label>
          <textarea id="project" name="project" rows="4" data-required
                    placeholder="What are you trying to build, improve, or grow?"></textarea>
        </div>
      </div>

      <div class="enquiry__foot">
        <button class="btn enquiry-send" type="submit" data-magnetic="0.18"
                aria-describedby="enquiry-note">
          <span class="enquiry-send__label">Send inquiry</span>{ARROW}
        </button>
        <p class="enquiry__note" id="enquiry-note">
          Press Send, or hit Enter from any field. Your inquiry is prepared so it
          can be copied or opened in your email app &mdash; add your business
          receiving email before launch for automatic delivery.
        </p>
      </div>
      <p class="enquiry__status" role="status" aria-live="polite"></p>
    </form>"""


# ---------------------------------------------------------------------------
# Capabilities
# ---------------------------------------------------------------------------

CAPABILITIES = [
    ("01", "Web Design", "design",
     "Refined, custom digital experiences built around your brand, your customer, "
     "and your goals."),
    ("02", "Web Development", "development",
     "Responsive, fast, modern builds that feel polished across desktop, tablet "
     "and mobile."),
    ("03", "Digital Marketing", "marketing",
     "Campaign strategy designed to turn attention into qualified opportunities "
     "and measurable growth."),
    ("04", "Local SEO", "seo",
     "Search visibility systems that help your business appear where high-intent "
     "customers are looking."),
    ("05", "Website Management", "care",
     "Ongoing optimisation, maintenance, content support and performance "
     "refinement after launch."),
]


def capability_rows(root=""):
    rows = ""
    for idx, name, anchor, desc in CAPABILITIES:
        rows += f"""
      <a class="row-link" href="{root}services.html#{anchor}" data-reveal>
        <span class="row-link__idx">{idx}</span>
        <span class="row-link__name">{name}</span>
        <span class="row-link__desc">{desc}</span>
        <span class="row-link__arrow" aria-hidden="true">&#8599;</span>
      </a>"""
    return f'<div class="rows" data-stagger="70">{rows}\n    </div>'


# ---------------------------------------------------------------------------
# Home
# ---------------------------------------------------------------------------

ORG_SCHEMA = """<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "ProfessionalService",
  "name": "Noir Echelon",
  "description": "Premium web design, development and digital marketing.",
  "url": "https://www.noirechelon.com/",
  "logo": "https://www.noirechelon.com/assets/img/icon-512.png",
  "image": "https://www.noirechelon.com/assets/img/og-cover.png",
  "email": "__EMAIL__",
  "knowsAbout": [
    "Web design", "Web development", "E-commerce", "Search engine optimisation",
    "Conversion rate optimisation", "Brand identity"
  ]
}
</script>""".replace("__EMAIL__", EMAIL)


def home():
    meta = {
        "path": "index.html",
        "active": "index.html",
        "title": "Noir Echelon — Premium Web Design, Development &amp; Digital Marketing",
        "description": "Noir Echelon creates premium websites and digital growth systems "
                       "for businesses that refuse to look ordinary. Web design, development, "
                       "marketing and local SEO.",
        "schema": ORG_SCHEMA,
        "cta": False,
    }

    body = f"""
<section class="hero hero--brand">
  <div class="ambient" aria-hidden="true"></div>

  <div class="hero__plate" aria-hidden="true">
    <img src="assets/img/brand-hero.png"
         srcset="assets/img/brand-hero-760.png 760w, assets/img/brand-hero.png 1400w"
         sizes="(max-width: 900px) 100vw, 66vw"
         alt="" width="1400" height="933" fetchpriority="high" decoding="async">
  </div>

  <div class="shell hero__inner">
    <p class="hero__eyebrow is-in">Web development <i></i> Digital marketing</p>

    <h1 class="hero__title--brand mt-m is-in">
      {lines('Digital experiences', 'built to <em>elevate</em>.')}
    </h1>

    <p class="lead mt-m" data-reveal style="--d:420ms;max-width:44ch">
      Noir Echelon creates premium websites and digital growth systems for
      businesses that refuse to look ordinary.
    </p>

    <div class="flex wrap gap-m items-center mt-l" data-reveal style="--d:520ms">
      <a class="btn" href="contact.html" data-magnetic="0.22"><span>Start a project</span>{ARROW}</a>
      <a class="link" href="#work">View selected work <span class="arrow" aria-hidden="true">&#8595;</span></a>
    </div>

    <div class="hero__rail" data-reveal style="--d:640ms">
      <span>Strategy</span><span>Design</span><span>Development</span><span>Growth</span>
    </div>
  </div>
</section>

<section class="section paper">
  <div class="shell">
    {eyebrow('&mdash;', 'The Noir Echelon standard')}
    <div class="grid mt-l">
      <div class="col-10">
        <h2 class="centred__title" style="text-align:left;max-width:26ch;margin-inline:0" data-reveal>
          Your digital presence is often your first impression.
          <span class="roman">Make it impossible to forget.</span>
        </h2>
      </div>
    </div>
    <div class="grid mt-l">
      <div class="col-7">
        <p class="lead" data-reveal style="--d:120ms;max-width:62ch">
          We combine strategy, premium design, technology and conversion thinking to
          create websites that look established, feel intentional, and move people to act.
        </p>
      </div>
    </div>
  </div>
</section>

<section class="section" id="capabilities">
  <div class="ambient ambient--low" aria-hidden="true"></div>
  <div class="shell" style="position:relative;z-index:2">
    {eyebrow('&mdash;', 'Capabilities')}
    <div class="grid mt-m">
      <div class="col-9">
        <h2 class="centred__title" style="text-align:left;margin-inline:0;max-width:22ch" data-reveal>
          Built to look exceptional.<br><em>Engineered to perform.</em>
        </h2>
      </div>
    </div>
    {capability_rows()}
    <div class="mt-l flex between items-center wrap gap-m">
      <div class="rule" style="flex:1"></div>
      <a class="btn btn--sm" href="services.html" data-magnetic="0.18"><span>All services</span>{ARROW}</a>
    </div>
  </div>
</section>

<section class="section" id="perception">
  <div class="ambient ambient--low" aria-hidden="true"></div>
  <div class="shell centred" style="position:relative;z-index:2">
    {eyebrow('&mdash;', 'The perception principle')}
    <h2 class="centred__title mt-m" data-reveal>
      People judge your business before they ever <em>speak to you.</em>
    </h2>
    <p class="centred__lede" data-reveal style="--d:120ms">
      Your website is your first impression, your reputation, your salesperson
      and your storefront &mdash; working every hour of every day.
    </p>
    <div class="pillars" data-stagger="110">
      <div class="pillar" data-reveal><p class="pillar__num">01</p><p class="pillar__lbl">Look established</p></div>
      <div class="pillar" data-reveal><p class="pillar__num">02</p><p class="pillar__lbl">Communicate value</p></div>
      <div class="pillar" data-reveal><p class="pillar__num">03</p><p class="pillar__lbl">Convert attention</p></div>
    </div>
  </div>
</section>

<section class="section paper" id="process">
  <div class="shell">
    {eyebrow('&mdash;', 'Process')}
    <div class="grid mt-m">
      <div class="col-8">
        <h2 class="centred__title" style="text-align:left;margin-inline:0;max-width:16ch" data-reveal>
          From idea to <em>digital echelon.</em>
        </h2>
      </div>
    </div>
    {process_block()}
  </div>
</section>

<section class="section" id="work">
  <div class="shell">
    {eyebrow('&mdash;', 'Selected work')}
    <div class="grid mt-m">
      <div class="col-8">
        <h2 class="centred__title" style="text-align:left;margin-inline:0;max-width:20ch" data-reveal>
          Work that had to <em>carry weight.</em>
        </h2>
      </div>
    </div>

    <div class="work-list mt-xl">
      {work_item(PROJECTS[0])}
      <div class="work-pair">
        {work_item(PROJECTS[1])}
        {work_item(PROJECTS[2])}
      </div>
    </div>

    <div class="mt-xl flex between items-center wrap gap-m">
      <div class="rule" style="flex:1"></div>
      <a class="btn" href="work.html" data-magnetic="0.18"><span>All selected work</span>{ARROW}</a>
    </div>
  </div>
</section>

<section class="reel" id="reveal" data-reel data-phase="start">
  <div class="reel__track">
    <div class="reel__stage">
      <div class="reel__media">
        <img class="reel__still" src="assets/img/reveal-poster.jpg"
             alt="The Noir Echelon monogram and wordmark, lit against black"
             width="1920" height="1080" loading="lazy" decoding="async">
        <video class="reel__video" muted playsinline preload="none" disablepictureinpicture
               aria-hidden="true" tabindex="-1"
               poster="assets/img/reveal-start.jpg"
               data-src-small="assets/video/reveal-854.mp4"
               data-src="assets/video/reveal-1280.mp4"
               data-src-large="assets/video/reveal-1920.mp4"
               data-webm-small="assets/video/reveal-854.webm"
               data-webm="assets/video/reveal-1280.webm"
               data-webm-large="assets/video/reveal-1920.webm"
               width="1920" height="1080"></video>
        <div class="reel__veil" aria-hidden="true"></div>
        <div class="reel__frame" aria-hidden="true"></div>
      </div>

      <div class="reel__caption">
        <p class="eyebrow is-in"><span class="idx">&mdash;</span> The mark</p>
        <h2>Built in the dark,<br><em>finished in the light.</em></h2>
      </div>

      <p class="reel__cue" aria-hidden="true">Scroll to reveal <span class="arrow">&#8595;</span></p>
      <div class="reel__meter" aria-hidden="true"><i></i></div>
    </div>
  </div>
</section>

<section class="section" id="about">
  <div class="shell">
    <div class="grid">
      <div class="col-6">
        {eyebrow('&mdash;', 'About Noir Echelon')}
        <h2 class="centred__title mt-m" style="text-align:left;margin-inline:0;max-width:14ch" data-reveal>
          We don't build <em>just another website.</em>
        </h2>
      </div>
      <div class="col-5 start-8" data-reveal style="--d:120ms">
        <p class="body-copy">
          Noir Echelon was built around one idea: businesses should not have to
          settle for digital experiences that look like everyone else's.
        </p>
        <p class="body-copy">
          We combine strategy, premium design, technology and marketing to elevate
          how your business is perceived &mdash; and how effectively it converts.
        </p>
        <a class="link mt-m" href="#start">Work with Noir Echelon {ARROW}</a>
      </div>
    </div>
    {facts_block()}
  </div>
</section>

<section class="section paper" id="clients">
  <div class="shell">
    {eyebrow('&mdash;', 'Client experience')}
    <h2 class="centred__title mt-m" style="text-align:left;margin-inline:0;max-width:18ch" data-reveal>
      Proof should feel <em>as strong as the promise.</em>
    </h2>
    {testimonials_block()}
  </div>
</section>

<section class="section" id="questions">
  <div class="shell">
    <div class="grid">
      <div class="col-4">
        {eyebrow('&mdash;', 'Before you ask')}
        <h2 class="h3 mt-m" data-reveal>The questions<br>worth asking early.</h2>
        <p class="dim mt-m" style="font-size:var(--fs-small);max-width:30ch">
          If something here is not answered, ask us directly. We would rather have
          the awkward conversation now than the expensive one later.
        </p>
      </div>
      <div class="col-7 start-6">
        {faq_block()}
      </div>
    </div>
  </div>
</section>

<section class="section" id="start">
  <div class="ambient" aria-hidden="true"></div>
  <div class="shell" style="position:relative;z-index:2">
    {eyebrow('&mdash;', 'Start a project')}
    <h2 class="centred__title mt-m" style="text-align:left;margin-inline:0;max-width:14ch" data-reveal>
      Your next level <em>starts here.</em>
    </h2>
    <p class="lead mt-m" data-reveal style="--d:120ms;max-width:52ch">
      Tell us what you're building. We'll help shape a digital presence that
      reflects the quality of your business.
    </p>
    {enquiry_form()}
  </div>
</section>"""
    return meta, body


# ---------------------------------------------------------------------------
# Selected work
# ---------------------------------------------------------------------------

def work_index():
    meta = {
        "path": "work.html",
        "active": "work.html",
        "title": "Selected Work — Noir Echelon",
        "description": "Case studies from Noir Echelon: property, ready-to-wear and "
                       "private advisory. Positioning, design, engineering and the "
                       "marketing that followed.",
    }
    items = "\n".join([
        work_item(PROJECTS[0]),
        f'<div class="work-pair">{work_item(PROJECTS[1])}{work_item(PROJECTS[2])}</div>',
    ])

    body = f"""
<section class="page-hero">
  <div class="ambient" aria-hidden="true"></div>
  <div class="shell" style="position:relative;z-index:2">
    <p class="eyebrow is-in"><span class="idx">&mdash;</span> Selected work</p>
    <div class="grid page-hero__title">
      <div class="col-9">
        <h1 class="h1 is-in">{lines('Fewer projects.', 'Further considered.')}</h1>
      </div>
    </div>
    <div class="grid mt-l">
      <div class="col-5 start-8">
        <p class="body-copy" data-reveal style="--d:300ms">
          We take on a small number of engagements at a time. Each one below is
          shown the way we work: the position first, then the design, then the
          build, then what happened next.
        </p>
      </div>
    </div>
  </div>
</section>

<section class="section section--tight">
  <div class="shell">
    <div class="rule"></div>
    <h2 class="sr-only">Selected projects</h2>
    <div class="work-list mt-xl">
      {items}
    </div>
  </div>
</section>

<section class="section">
  <div class="shell">
    <div class="grid">
      <div class="col-5">
        {eyebrow('&mdash;', 'Engagement')}
        <h2 class="h3 mt-m" data-reveal>Where a project usually begins.</h2>
      </div>
      <div class="col-6 start-7" data-reveal style="--d:120ms">
        <p class="body-copy">
          Most clients arrive at one of three moments: the business has outgrown the
          website, the website is quietly losing sales, or something new needs to
          launch without looking new.
        </p>
        <p class="body-copy">
          If you recognise one of those, the first conversation is short and useful.
          We will tell you plainly whether we are the right studio for it.
        </p>
        <a class="link mt-m" href="contact.html">Start a project {ARROW_R}</a>
      </div>
    </div>
  </div>
</section>"""
    return meta, body


# ---------------------------------------------------------------------------
# Services
# ---------------------------------------------------------------------------

SERVICE_DETAIL = [
    ("Web Design", "design",
     "Before the website, the position.",
     "A business that cannot say what it is in one sentence cannot be designed for. "
     "We settle the position, the audience and the promise first, then art-direct "
     "every key screen at desktop, tablet and mobile &mdash; typography, colour, "
     "imagery, motion and the words that carry the argument. You review real "
     "screens, not a mood board.",
     ["Positioning &amp; messaging", "Visual identity &amp; art direction",
      "UX &amp; information architecture", "Interface design",
      "Responsive art direction", "Design system &amp; guidelines"]),
    ("Web Development", "development",
     "Hand-built, not assembled.",
     "The front end is written by hand, so there is no page builder bloat to slow "
     "it down, and the CMS is configured around how your team actually writes. "
     "Accessibility and performance budgets are set before design starts, not "
     "retrofitted after launch.",
     ["Front-end engineering", "CMS integration", "E-commerce builds",
      "Accessibility (WCAG 2.2 AA)", "Performance budgets", "Analytics &amp; tracking"]),
    ("Digital Marketing", "marketing",
     "Attention, bought carefully.",
     "Campaigns held to a cost per qualified enquiry rather than impressions. "
     "Content with a reason to exist, paid media that stops paying for the wrong "
     "people, and reporting in plain language, monthly. We will tell you when a "
     "channel is not working for you.",
     ["Campaign strategy", "Paid search &amp; social", "Content strategy",
      "Lifecycle email", "Attribution &amp; reporting"]),
    ("Local SEO", "seo",
     "Found where it counts.",
     "Search visibility built to compound: the technical foundation first, then "
     "the pages that answer what your customers actually type, then the local "
     "signals that decide who appears when someone is ready to buy nearby.",
     ["Technical SEO", "Local &amp; map visibility", "Keyword &amp; intent mapping",
      "On-page optimisation", "Review &amp; listing management"]),
    ("Website Management", "care",
     "A team that answers.",
     "Hosting, monitoring, backups, security patching, dependency updates and a "
     "performance budget that is enforced, not aspirational. A named contact, a "
     "response time you can hold us to, and a monthly window for the small changes "
     "that otherwise pile up for a year.",
     ["Managed hosting", "Security &amp; monitoring", "Performance care",
      "Content updates", "Conversion refinement", "Quarterly review"]),
]


def services():
    meta = {
        "path": "services.html",
        "active": "services.html",
        "title": "Services — Web Design, Development &amp; Digital Marketing | Noir Echelon",
        "description": "Brand identity, websites, e-commerce, SEO, paid media and "
                       "conversion growth. What Noir Echelon does, how it is run, and "
                       "what it costs.",
    }

    blocks = ""
    for i, (name, anchor, headline, body_text, items) in enumerate(SERVICE_DETAIL, 1):
        li = "".join(f"<li>{item}</li>" for item in items)
        blocks += f"""
<section class="chapter" id="{anchor}">
  <div class="chapter__label">
    <p class="eyebrow"><span class="idx">0{i}</span> {name}</p>
  </div>
  <div class="chapter__body">
    <h3 data-reveal>{headline}</h3>
    <p class="body-copy" data-reveal style="--d:100ms">{body_text}</p>
    <ul class="chapter__list" data-reveal style="--d:160ms">{li}</ul>
  </div>
</section>"""

    body = f"""
<section class="page-hero">
  <div class="ambient" aria-hidden="true"></div>
  <div class="shell" style="position:relative;z-index:2">
    <p class="eyebrow is-in"><span class="idx">&mdash;</span> Services</p>
    <div class="grid page-hero__title">
      <div class="col-10">
        <h1 class="h1 is-in">{lines('Everything that decides', 'whether you are chosen.')}</h1>
      </div>
    </div>
    <div class="grid mt-l">
      <div class="col-5 start-8">
        <p class="body-copy" data-reveal style="--d:300ms">
          Five disciplines, one senior team, no handoff between the people who plan
          the work and the people who make it. Engage us for one, or for the whole
          arc from position to performance.
        </p>
      </div>
    </div>
  </div>
</section>

<section class="section section--tight">
  <div class="shell">
    <h2 class="sr-only">Capabilities in detail</h2>
    {blocks}
  </div>
</section>

<section class="section" id="investment">
  <div class="shell">
    {eyebrow('&mdash;', 'Investment')}
    <div class="grid mt-l">
      <div class="col-5">
        <h2 class="h3" data-reveal>Priced before we start.<br>Not discovered later.</h2>
      </div>
      <div class="col-6 start-7" data-reveal style="--d:120ms">
        <p class="body-copy">
          After the first conversation you receive a fixed price and a dated plan.
          Not a range, not an hourly estimate that drifts, and no change-order
          theatre for things that were obviously part of the job.
        </p>
        <p class="body-copy">
          Most website engagements start at a mid five-figure sum. E-commerce and
          multi-market builds sit above that. Marketing is a monthly retainer sized
          to the channels that make sense for you.
        </p>
        <p class="body-copy">
          If the budget and the ambition do not match, we will say so in the first
          call rather than quietly reducing the work to fit.
        </p>
        <a class="link mt-m" href="contact.html">Get a fixed price {ARROW_R}</a>
      </div>
    </div>
    {facts_block()}
  </div>
</section>

<section class="section">
  <div class="shell">
    <div class="grid">
      <div class="col-4">
        {eyebrow('&mdash;', 'Before you ask')}
        <h2 class="h3 mt-m" data-reveal>Answered plainly.</h2>
      </div>
      <div class="col-7 start-6">
        {faq_block()}
      </div>
    </div>
  </div>
</section>"""
    return meta, body


# ---------------------------------------------------------------------------
# Studio
# ---------------------------------------------------------------------------

PRINCIPLES = [
    ("Restraint is the strategy",
     "Anyone can add. The discipline is deciding what to leave out so the one thing "
     "that matters is impossible to miss."),
    ("Design is an argument",
     "Every layout makes a case for why you are worth the money. If it cannot be "
     "explained, it is decoration."),
    ("Speed is part of the design",
     "A slow page is an expensive page. Performance budgets are agreed before design "
     "begins and enforced before launch."),
    ("Say the hard thing early",
     "If the budget, the timeline or the idea has a problem, you hear it in week one, "
     "not in month three."),
]


def studio():
    meta = {
        "path": "studio.html",
        "active": "studio.html",
        "title": "The Studio — Noir Echelon",
        "description": "How Noir Echelon works: a small senior team, a visible process, "
                       "and a standard of digital presentation built for businesses that "
                       "compete on quality.",
    }

    principles = "".join(
        f"""
      <div class="step" data-reveal>
        <p class="step__num">0{i}</p>
        <h3 class="step__name">{title}</h3>
        <p class="step__body">{text}</p>
      </div>"""
        for i, (title, text) in enumerate(PRINCIPLES, 1)
    )

    body = f"""
<section class="page-hero">
  <div class="ambient" aria-hidden="true"></div>
  <div class="hero__watermark" data-depth="0.04" data-depth-center="true" aria-hidden="true">{MONOGRAM}</div>
  <div class="shell" style="position:relative;z-index:2">
    <p class="eyebrow is-in"><span class="idx">&mdash;</span> The studio</p>
    <div class="grid page-hero__title">
      <div class="col-10">
        <h1 class="h1 is-in">{lines('A small studio', 'with a long memory', 'for detail.')}</h1>
      </div>
    </div>
  </div>
</section>

<section class="section section--tight">
  <div class="shell">
    <div class="rule"></div>
    <div class="grid mt-xl">
      <div class="col-5">
        <p class="statement__text" data-reveal style="font-size:clamp(1.6rem,3vw,2.6rem)">
          Noir Echelon exists for one reason: <em>perception</em> decides who gets
          considered.
        </p>
      </div>
      <div class="col-6 start-7" data-reveal style="--d:120ms">
        <p class="body-copy">
          Two businesses can offer the same service at the same price and be judged
          completely differently, and the difference is almost never the product. It
          is the impression &mdash; the typography, the speed, the photography, the
          confidence of the words, the sense that someone cared.
        </p>
        <p class="body-copy">
          That impression is buildable. It is the whole of what we do: design that
          signals quality, engineering that makes it instant, and marketing that puts
          it in front of people who can afford it.
        </p>
        <p class="body-copy">
          We keep the studio deliberately small. Fewer clients, more attention, and
          the same senior people from the first conversation to the work after launch.
        </p>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="shell">
    {eyebrow('01', 'Principles')}
    <div class="grid mt-m">
      <div class="col-7"><h2 class="h2" data-reveal>What we hold to.</h2></div>
    </div>
    <div class="process" data-stagger="90">{principles}
    </div>
  </div>
</section>

<section class="section">
  <div class="shell">
    {eyebrow('02', 'The process')}
    <div class="grid mt-m">
      <div class="col-7">
        <h2 class="h2" data-reveal>Five stages.<br>Nothing hidden.</h2>
      </div>
      <div class="col-4 start-9 flex items-end" data-reveal style="--d:120ms">
        <p class="dim" style="font-size:var(--fs-small);max-width:32ch">
          You always know what is happening, what is next, and what we need from you
          to keep it moving.
        </p>
      </div>
    </div>
    {process_block()}
  </div>
</section>

<section class="section">
  <div class="shell">
    <div class="grid">
      <div class="col-6">
        {eyebrow('03', 'Working with us')}
        <h2 class="h3 mt-m" data-reveal>What you own,<br>and what you can expect.</h2>
      </div>
      <div class="col-5 start-8" data-reveal style="--d:120ms">
        <p class="body-copy">
          Domains, hosting, source code, design files, analytics and advertising
          accounts are in your name from day one. Every project ends with a handover
          session and written documentation, whether or not you stay with us
          afterwards.
        </p>
        <p class="body-copy">
          We reply to inquiries within one business day, we do not bill for the
          conversation that decides whether we are a fit, and we will recommend
          someone else if the work is not ours to do.
        </p>
      </div>
    </div>
    {facts_block()}
  </div>
</section>"""
    return meta, body


# ---------------------------------------------------------------------------
# Contact — multi-step inquiry
# ---------------------------------------------------------------------------

STEP_ONE = [
    ("A new website", "website"),
    ("A website redesign", "redesign"),
    ("E-commerce", "ecommerce"),
    ("Digital marketing", "marketing"),
    ("SEO &amp; content", "seo"),
    ("Brand &amp; identity", "brand"),
    ("A full brand experience", "full"),
    ("Something else", "other"),
]

STEP_BUDGET = [
    ("Under &pound;10k", "u10"),
    ("&pound;10k &ndash; &pound;25k", "10-25"),
    ("&pound;25k &ndash; &pound;60k", "25-60"),
    ("&pound;60k +", "60plus"),
    ("Monthly retainer", "retainer"),
    ("Not sure yet", "unsure"),
]

STEP_TIMING = [
    ("As soon as possible", "asap"),
    ("Within 3 months", "3m"),
    ("Within 6 months", "6m"),
    ("Planning ahead", "planning"),
]


def options(name, items, cols=2):
    out = ""
    for label, value in items:
        oid = f"{name}-{value}"
        out += f"""
        <label class="option" for="{oid}">
          <input type="radio" name="{name}" id="{oid}" value="{label}">
          <span class="option__box"><i aria-hidden="true"></i>{label}</span>
        </label>"""
    return f'<div class="options">{out}\n      </div>'


def contact():
    meta = {
        "path": "contact.html",
        "active": "contact.html",
        "title": "Start a Project — Noir Echelon",
        "description": "Tell us what you're building. We'll help shape a digital "
                       "presence that reflects the quality of your business, and reply "
                       "within one business day.",
        "cta": False,
    }

    body = f"""
<section class="page-hero">
  <div class="ambient" aria-hidden="true"></div>
  <div class="shell" style="position:relative;z-index:2">
    <p class="eyebrow is-in"><span class="idx">&mdash;</span> Start a project</p>
    <div class="grid page-hero__title">
      <div class="col-9">
        <h1 class="hero__title--brand is-in">
          {lines("Your next level", "<em>starts here.</em>")}
        </h1>
      </div>
    </div>
    <div class="grid mt-m">
      <div class="col-6">
        <p class="lead" data-reveal style="--d:300ms">
          Tell us what you're building. We'll help shape a digital presence that
          reflects the quality of your business.
        </p>
      </div>
    </div>
  </div>
</section>

<section class="section section--tight">
  <div class="shell">
    {enquiry_form()}

    <div class="grid mt-xl">
      <div class="col-4">
        <div class="direct">
          <div class="direct__row">
            <h2>Prefer email</h2>
            <a href="mailto:{EMAIL}">{EMAIL}</a>
          </div>
          <div class="direct__row">
            <h2>Response time</h2>
            <p>Within one business day</p>
          </div>
        </div>
      </div>
      <div class="col-7 start-6">
        <div class="rows" data-stagger="80">
          <div class="row-link" data-reveal style="cursor:default">
            <span class="row-link__idx">01</span>
            <span class="row-link__name">We read it properly</span>
            <span class="row-link__desc">Within one business day you hear from a senior person, not an
            automated sequence. If we are not right for the work, we say so and point you elsewhere.</span>
            <span class="row-link__arrow"></span>
          </div>
          <div class="row-link" data-reveal style="cursor:default">
            <span class="row-link__idx">02</span>
            <span class="row-link__name">A short call</span>
            <span class="row-link__desc">Thirty to forty-five minutes on your business, the constraints and
            what success would actually look like. Prepared for, and free.</span>
            <span class="row-link__arrow"></span>
          </div>
          <div class="row-link" data-reveal style="cursor:default">
            <span class="row-link__idx">03</span>
            <span class="row-link__name">A fixed proposal</span>
            <span class="row-link__desc">Scope, dated milestones and a fixed price. If it is a yes, we book
            the studio time and begin. If it is not, there is no follow-up campaign.</span>
            <span class="row-link__arrow"></span>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>"""
    return meta, body


# ---------------------------------------------------------------------------
# Case studies
# ---------------------------------------------------------------------------
# PLACEHOLDER CONTENT — these three engagements illustrate the case-study
# format. Replace the copy and artwork with real projects, and only publish
# outcome figures you can evidence.

CASES = {
    "quik-burrito": {
        "eyebrow": "Restaurant &middot; Anthem, Arizona",
        "headline": "Make somebody hungry,<br>then get out of the way.",
        "meta": [
            ("Client", "Quik Burrito"),
            ("Sector", "Restaurant"),
            ("Scope", "Website, menu, locations, reviews"),
            ("Year", "2026"),
        ],
        "figures": {1: ("quik-burrito-brand.jpg", "The mark, carried through every page", 1200, 750)},
        "chapters": [
            ("The client",
             "A burrito shop in Anthem, Arizona.",
             ["Quik Burrito sells food that photographs extraordinarily well and, like most "
              "independent restaurants, was competing for attention against delivery apps "
              "whose entire business is being one tap away."]),
            ("The brief",
             "One job, stated plainly.",
             ["The site has a single job: make somebody hungry, then get them to order "
              "online in one tap. Everything was measured against that sentence. If a "
              "section did not make you hungrier or make ordering easier, it did not ship."]),
            ("The strategy",
             "Sell the food, not the restaurant.",
             ["The homepage became one continuous scroll-scrubbed journey &mdash; the "
              "burrito, the ingredients, the grill, the build, the signature dishes, the "
              "birria dip &mdash; ending on the order button. The camera is tied to the "
              "wheel, so the pace belongs to the visitor; scroll back up anywhere and the "
              "move runs in reverse.",
              "Brand, tagline and ORDER ONLINE are all in the first frame. There is nothing "
              "to wait through before you can act."]),
            ("The experience",
             "Cinematic on top, plain underneath.",
             ["Everything beneath the homepage &mdash; menu, locations, reviews &mdash; is "
              "deliberately fast and plain, and usable on a phone with one hand. The "
              "cinema earns attention; the utility pages spend it.",
              "Locations are individually addressable, so a search for the nearest branch "
              "lands on a real page rather than a map pin buried in a single contact page."]),
            ("The build",
             "Server-rendered, indexable, fast.",
             ["Built on the Next.js app router with server-rendered routes, generated "
              "<code>robots.txt</code> and <code>sitemap.xml</code>, and per-location pages "
              "on dynamic routes. Social proof is pulled in rather than screenshotted, so "
              "it stays current without anyone maintaining it."]),
            ("The result",
             "A site that behaves like the food.",
             ["Shipped with the cinematic homepage, the full menu, per-location pages and "
              "reviews, with the order path reachable from the first frame of every one.",
              "<!-- Add verified commercial outcomes here once they can be evidenced. -->"]),
        ],
        "pull": "If a section did not make you hungrier or make ordering easier, it did not ship.",
        "next": "pho-thanh",
    },
    "pho-thanh": {
        "eyebrow": "Vietnamese restaurant &middot; Phoenix",
        "headline": "One photograph,<br>taken apart by scrolling.",
        "meta": [
            ("Client", "Ph&#7903; Th&agrave;nh"),
            ("Sector", "Vietnamese restaurant"),
            ("Scope", "Single-page site, full menu system"),
            ("Year", "2026"),
        ],
        "figures": {},
        "chapters": [
            ("The client",
             "A family restaurant on West Camelback.",
             ["Ph&#7903; Th&agrave;nh has been serving Phoenix from 1702 W Camelback Road: "
              "one family, one very large menu, no fuss. The menu is the business, and it "
              "runs to well over a hundred numbered items across ph&#7903;, b&uacute;n, "
              "com and a Kwan &amp; Wok insert."]),
            ("The challenge",
             "A menu that long is usually a PDF.",
             ["The default for a restaurant with this much menu is a scanned PDF that "
              "nobody can read on a phone. The challenge was to make the size of the menu "
              "feel like abundance rather than homework &mdash; and to do it without a "
              "photo library, because there was exactly one usable photograph."]),
            ("The strategy",
             "Spend everything on the one image you have.",
             ["That single photograph became the whole opening. It is layered on top of "
              "itself inside a sticky, full-viewport stage, and each layer is masked to one "
              "ingredient &mdash; the beef slice and chopsticks, lime, jalape&ntilde;os, "
              "chilies, basil, the broth splashes, the bowl.",
              "Scrolling scrubs roughly 3,700 pixels of story: the garnishes fly out, the "
              "beef lifts, the bowl comes apart, and the copy about the broth and the "
              "kitchen reads in the gaps between."]),
            ("The experience",
             "Then the menu, in full, in plain text.",
             ["Once the theatre is over the site becomes a reference. Every numbered item "
              "is real text with jump links by section, so a customer can find item 122 on "
              "a phone in a parking lot.",
              "Steam is a canvas particle layer that thickens while the bowl is coming "
              "apart and settles at the end. Pointer movement adds a small parallax to "
              "every layer. Reduced-motion visitors get none of it &mdash; no smoothing, "
              "no parallax, no steam."]),
            ("The build",
             "No framework, no build step.",
             ["Vanilla HTML, CSS and JavaScript. The folder opens in a browser or sits on "
              "any static host, which matters for a restaurant that should never be "
              "dependent on a build pipeline it does not own.",
              "The menu lives as data: a new section is an object appended to one file, "
              "and both the menu block and its jump links render it automatically.",
              "The printed menus disagreed with each other in several places &mdash; "
              "handwritten prices, an insert that exists in two prints, differing hours. "
              "Every discrepancy is documented in the repository for the restaurant to "
              "settle rather than quietly guessed at."]),
            ("The result",
             "A menu you can actually use, wrapped in something worth watching.",
             ["Shipped as a single page carrying the full menu, the scroll sequence and "
              "the visit details, with no build step and one image.",
              "<!-- Add verified commercial outcomes here once they can be evidenced. -->"]),
        ],
        "pull": "Make the size of the menu feel like abundance rather than homework.",
        "next": "ol-clip-joint",
    },
    "ol-clip-joint": {
        "eyebrow": "Barbershop &middot; Phoenix",
        "headline": "A request is not<br>an appointment.",
        "meta": [
            ("Client", "The Ol&rsquo; Clip Joint"),
            ("Sector", "Barbershop"),
            ("Scope", "Website &amp; appointment line"),
            ("Year", "2026"),
        ],
        "figures": {
            1: ("ol-clip-joint-detail.jpg", "Classic cuts, late hours", 1200, 671),
            3: ("ol-clip-joint-film.jpg", "The shop, shot on location", 1200, 675),
        },
        "chapters": [
            ("The client",
             "Classic cuts, late hours.",
             ["The Ol&rsquo; Clip Joint sits at 5620 N 7th Street in Phoenix, and Matt runs "
              "the chair. Late hours are part of the offer, which means the booking "
              "questions arrive at all hours too."]),
            ("The challenge",
             "Booking software books people. Barbers decide.",
             ["Off-the-shelf booking tools will happily put a stranger in the chair at 9 PM "
              "without asking anyone. For a single-chair shop that is not convenience, it "
              "is a scheduling problem arriving by surprise &mdash; and a client who turns "
              "up to a slot that was never really available."]),
            ("The strategy",
             "Make the barber the last word, in the software.",
             ["The whole system is built on one rule: a request is not an appointment until "
              "Matt says so. Nothing on the site can put a client in the chair.",
              "A client picks a service, a day, a time and leaves a name and mobile. That "
              "texts Matt with who, what and when, a confirm link, and a reply code. The "
              "client is immediately texted that it is a request and nothing is booked "
              "yet. Only when Matt confirms &mdash; one tap, or a text back &mdash; does "
              "the client get the message that says they are booked."]),
            ("The experience",
             "Three ways onto the book, one source of truth.",
             ["Online, by text, or by phone for anything sooner than an hour out. The text "
              "route writes the message and opens Messages; it is still a request, and the "
              "site says so in those words.",
              "A pending request holds its slot, so two people cannot be sent to the same "
              "9 PM chair. If Matt does not answer within two hours the hold expires, the "
              "time goes back on the board, and the client is told it lapsed rather than "
              "being left wondering."]),
            ("The build",
             "State that survives a busy Saturday.",
             ["The server tracks only the online flow, and the booking states &mdash; "
              "requested, held, confirmed, declined, expired &mdash; are explicit, because "
              "the failure everyone remembers is a double booking. Confirmation happens "
              "over SMS, where Matt already is, rather than in an admin panel he would "
              "have to remember to open."]),
            ("The result",
             "Nobody is booked by a machine.",
             ["Shipped with the online request flow, the SMS confirmation loop, slot holds "
              "with expiry, and the text and phone routes alongside.",
              "<!-- Add verified commercial outcomes here once they can be evidenced. -->"]),
        ],
        "pull": "Nothing on the site can put a client in the chair.",
        "next": "quik-burrito",
    },
}


def case_study(slug):
    p = project_by(slug)
    c = CASES[slug]
    nxt = project_by(c["next"])
    root = "../"

    meta = {
        "path": f"work/{slug}.html",
        "active": "work.html",
        "root": root,
        "title": f"{p['name']} — Case Study | Noir Echelon",
        "description": p["summary"],
        "og_type": "article",
    }

    dl = "".join(f"<div><dt>{k}</dt><dd>{v}</dd></div>" for k, v in c["meta"])

    figures = {}
    for idx, (img, caption, w, h) in c.get("figures", {}).items():
        figures[idx] = f"""
<figure class="figure" data-reveal>
  <img src="{root}assets/img/work/{img}" alt="{caption}"
       loading="lazy" decoding="async" width="{w}" height="{h}">
  <figcaption>{caption}</figcaption>
</figure>"""

    chapters = ""
    for i, (label, headline, paras) in enumerate(c["chapters"]):
        body_paras = "".join(f'<p class="body-copy">{t}</p>' for t in paras)
        chapters += f"""
<section class="chapter">
  <div class="chapter__label">
    <p class="eyebrow"><span class="idx">0{i + 1}</span> {label}</p>
  </div>
  <div class="chapter__body">
    <h3 data-reveal>{headline}</h3>
    <div data-reveal style="--d:100ms">{body_paras}</div>
  </div>
</section>{figures.get(i, '')}"""
        if i == 2:
            chapters += f"""
<div class="section--tight" style="padding-block:clamp(48px,6vw,88px)">
  <p class="pull" data-reveal>{c['pull']}</p>
</div>"""

    body = f"""
<article>
<section class="case-hero">
  <div class="ambient" aria-hidden="true"></div>
  <div class="shell" style="position:relative;z-index:2">
    <p class="eyebrow is-in"><span class="idx">&mdash;</span> {c['eyebrow']}</p>
    <div class="grid case-hero__title">
      <div class="col-9">
        <h1 class="h1 is-in">{lines(*c['headline'].split('<br>'))}</h1>
      </div>
    </div>
    <div class="case-hero__frame" data-reveal="mask">
      <img src="{root}assets/img/work/{p['img']}" alt="{p['alt']}"
           width="1600" height="1000" decoding="async" fetchpriority="high">
    </div>
    <dl class="case-meta" data-stagger="80">{dl}</dl>
  </div>
</section>

<div class="shell">
  <h2 class="sr-only">The engagement, chapter by chapter</h2>
  {chapters}
</div>
</article>

<a class="next-case" href="{root}work/{nxt['slug']}.html" data-cursor="view">
  <div class="shell">
    <p class="eyebrow is-in"><span class="idx">&mdash;</span> Next project</p>
    <div class="flex between items-end wrap gap-m mt-m">
      <h2 class="next-case__title">{nxt['name']}</h2>
      <span class="micro gold nowrap">View case study {ARROW_R}</span>
    </div>
    <p class="dim mt-s" style="font-size:var(--fs-small)">{nxt['sector']} &middot; {nxt['scope']}</p>
  </div>
</a>"""
    return meta, body


# ---------------------------------------------------------------------------
# Privacy + 404
# ---------------------------------------------------------------------------

def privacy():
    meta = {
        "path": "privacy.html",
        "active": "",
        "title": "Privacy Notice — Noir Echelon",
        "description": "How Noir Echelon handles the information you send through this website.",
        "robots": "noindex, follow",
        "cta": False,
    }
    body = f"""
<section class="page-hero">
  <div class="shell">
    <p class="eyebrow is-in"><span class="idx">&mdash;</span> Legal</p>
    <div class="grid page-hero__title">
      <div class="col-8"><h1 class="h1 is-in">{lines('Privacy notice')}</h1></div>
    </div>
  </div>
</section>

<section class="section section--tight">
  <div class="shell">
    <div class="rule"></div>
    <div class="grid mt-xl">
      <div class="col-7 start-4">
        <!-- PLACEHOLDER: have this reviewed against your jurisdiction before launch. -->
        <p class="body-copy">
          This notice explains what happens to the information you send us through
          this website. It is written to be read, not to be survived.
        </p>
        <h2 class="h3 mt-l">What we collect</h2>
        <p class="body-copy">
          Only what you type into the inquiry form: your name, email address, optional
          phone number, company name and what you tell us about the project. We do not
          buy contact data and we do not sell yours.
        </p>
        <h2 class="h3 mt-l">Why we hold it</h2>
        <p class="body-copy">
          To reply to your inquiry and, if we work together, to run the engagement. We
          keep inquiries that do not become projects for twelve months, then delete them.
        </p>
        <h2 class="h3 mt-l">Analytics</h2>
        <p class="body-copy">
          We measure how pages perform in aggregate. We do not run advertising trackers
          on this site and we do not build profiles of individual visitors.
        </p>
        <h2 class="h3 mt-l">Your rights</h2>
        <p class="body-copy">
          You can ask what we hold, ask for a copy, ask us to correct it, or ask us to
          delete it. Write to <a class="gold" href="mailto:{EMAIL}">{EMAIL}</a> and we
          will act within thirty days.
        </p>
        <p class="dim mt-l" style="font-size:var(--fs-small)">
          Last updated on publication. Contact: {EMAIL}
        </p>
      </div>
    </div>
  </div>
</section>"""
    return meta, body


def not_found():
    meta = {
        "path": "404.html",
        "active": "",
        "title": "Page Not Found — Noir Echelon",
        "description": "The page you asked for is not here. Find Noir Echelon\u2019s selected work, services and studio from this page instead.",
        "robots": "noindex, nofollow",
        "cta": False,
        "loader": False,
    }
    body = f"""
<section class="lost">
  <div class="ambient" aria-hidden="true"></div>
  <div class="shell" style="position:relative;z-index:2">
    <p class="lost__code is-in">404</p>
    <h1 class="h3 mt-m is-in">This page has been<br>filed elsewhere.</h1>
    <p class="lead mt-m" style="margin-inline:auto;max-width:44ch">
      The link is broken or the page has moved. The work is still worth seeing.
    </p>
    <div class="flex gap-s wrap mt-l" style="justify-content:center">
      <a class="btn btn--solid" href="/" data-magnetic="0.2"><span>Return home</span>{ARROW}</a>
      <a class="btn" href="/work.html" data-magnetic="0.18"><span>Selected work</span></a>
    </div>
  </div>
</section>"""
    return meta, body


# ---------------------------------------------------------------------------
# Registry
# ---------------------------------------------------------------------------

def pages():
    return [
        home(),
        work_index(),
        services(),
        studio(),
        contact(),
        case_study("quik-burrito"),
        case_study("pho-thanh"),
        case_study("ol-clip-joint"),
        privacy(),
        not_found(),
    ]

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

from build import ARROW, ARROW_R, EMAIL, MONOGRAM, PHONE_DISPLAY, PHONE_HREF, SITE, STAR

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
        "slug": "meridian-house",
        "key": "meridian",
        "name": "Meridian House",
        "sector": "Property development",
        "scope": "Brand system, website, release portal",
        "year": "2025",
        "summary": "A twelve-residence development sold from a single, unhurried page \u2014 positioning, identity, website and agent reservation portal, launched in nine weeks.",
        "alt": "Meridian House homepage — serif headline over a dark editorial layout",
    },
    {
        "slug": "atelier-varona",
        "key": "varona",
        "name": "Atelier Varona",
        "sector": "Ready-to-wear",
        "scope": "E-commerce design, build, lifecycle marketing",
        "year": "2025",
        "summary": "A ready-to-wear storefront built to sell at full price rather than on discount \u2014 e-commerce design, headless build and lifecycle marketing for Atelier Varona.",
        "alt": "Atelier Varona storefront — ivory layout with oxblood accents",
    },
    {
        "slug": "calder-roe",
        "key": "calder",
        "name": "Calder &amp; Roe",
        "sector": "Private wealth advisory",
        "scope": "Positioning, website, search &amp; content",
        "year": "2024",
        "summary": "Quiet authority for a private wealth firm whose clients arrive by referral \u2014 positioning, website, accessibility and a search foundation built to compound.",
        "alt": "Calder & Roe website — deep green layout with restrained typography",
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
      <img class="work-item__media" src="{root}assets/img/work/{p['key']}-cover.svg"
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
    ("01", "Orientation", "We start with your business, not your website. What you sell, "
     "who buys it, what the sale actually costs you, and where the current experience "
     "loses people. One session, prepared for, with the people who make decisions."),
    ("02", "Direction", "A written position and a visual direction, presented together. "
     "You see the thinking and the design at the same time, because one without the "
     "other is decoration. We agree the direction before a single page is built."),
    ("03", "Design", "Every key screen, art-directed at desktop, tablet and mobile. "
     "Typography, spacing, imagery, motion and the words that carry the argument. "
     "You review real screens, not a mood board."),
    ("04", "Build", "Hand-built front-end, accessible markup, a CMS your team can "
     "actually use, and a performance budget enforced before launch. Staged, "
     "reviewed, tested on real devices, then released."),
    ("05", "Momentum", "Search, content, campaigns and measurement. We watch what "
     "people do, improve what underperforms, and report in plain language — monthly, "
     "with the numbers that matter and nothing padded."),
]


def process_block():
    steps = "".join(
        f"""
  <div class="step" data-reveal>
    <p class="step__num">{n}</p>
    <h3 class="step__name">{name}</h3>
    <p class="step__body">{body}</p>
  </div>"""
        for n, name, body in PROCESS
    )
    return f'<div class="process" data-stagger="90">{steps}\n</div>'


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
  "email": "studio@noirechelon.com",
  "knowsAbout": [
    "Web design", "Web development", "E-commerce", "Search engine optimisation",
    "Conversion rate optimisation", "Brand identity"
  ]
}
</script>"""


def home():
    meta = {
        "path": "index.html",
        "active": "index.html",
        "title": "Noir Echelon — Premium Web Design, Development &amp; Digital Marketing",
        "description": "Noir Echelon designs, builds and markets digital experiences for "
                       "businesses that intend to be taken seriously. Websites, e-commerce, "
                       "brand and growth — one senior team.",
        "schema": ORG_SCHEMA,
    }

    body = f"""
<section class="hero">
  <div class="ambient" aria-hidden="true"></div>
  <div class="hero__watermark" data-depth="0.045" data-depth-center="true" aria-hidden="true">{MONOGRAM}</div>

  <div class="shell hero__inner">
    <p class="eyebrow is-in" style="max-width:520px"><span class="idx">&mdash;</span> Web development &amp; digital marketing</p>

    <h1 class="hero__title mt-m is-in">
      {lines('People judge you', '<em>before</em> they meet you.')}
    </h1>

    <div class="hero__meta">
      <div class="hero__lede">
        <p class="lead" data-reveal style="--d:420ms">
          We design, build and market digital experiences for companies whose
          reputation should arrive first.
        </p>
      </div>
      <div class="hero__actions" data-reveal style="--d:520ms">
        <a class="btn btn--solid" href="contact.html" data-magnetic="0.22"><span>Start a project</span>{ARROW}</a>
        <a class="btn" href="work.html" data-magnetic="0.18"><span>View selected work</span></a>
      </div>
      <div class="hero__index micro" data-reveal style="--d:600ms">
        Design<br>Development<br>Marketing
      </div>
    </div>

    <div class="hero__scroll micro" data-reveal style="--d:700ms">
      <span class="flex items-center gap-s"><i class="dot" aria-hidden="true"></i> Scroll</span>
      <span class="dim">Selected work below</span>
    </div>
  </div>
</section>

<section class="section" id="premise">
  <div class="shell">
    {eyebrow('01', 'The premise')}
    <div class="grid mt-l">
      <div class="col-7">
        <p class="statement__text" data-reveal>
          Most businesses don't have a traffic problem.<br>
          They have a <em>perception</em> problem.
        </p>
      </div>
      <div class="col-4 start-9 statement__aside" data-reveal style="--d:140ms">
        <p class="body-copy">
          Your website is compared &mdash; in seconds, unconsciously &mdash; against
          every other website your customer has ever used. That comparison decides
          whether you read as established or improvised, considered or cheap, safe
          or risky.
        </p>
        <p class="body-copy">
          It happens before a word of your copy is read. We design for that moment,
          then build the machinery that turns it into revenue.
        </p>
        <a class="link mt-m" href="studio.html">How we think {ARROW_R}</a>
      </div>
    </div>
  </div>
</section>

<section class="section" id="work">
  <div class="shell">
    <div class="flex between items-end wrap gap-m">
      {eyebrow('02', 'Selected work')}
    </div>
    <div class="grid mt-m">
      <div class="col-8">
        <h2 class="h2" data-reveal>Work that had to carry weight.</h2>
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

<section class="section" id="capabilities">
  <div class="ambient ambient--low" aria-hidden="true"></div>
  <div class="shell" style="position:relative;z-index:2">
    {eyebrow('03', 'Capabilities')}
    <div class="grid mt-m">
      <div class="col-7">
        <h2 class="h2" data-reveal>Six disciplines.<br>One senior team.<br>No handoffs.</h2>
      </div>
      <div class="col-4 start-9 flex items-end" data-reveal style="--d:120ms">
        <p class="dim" style="font-size:var(--fs-small);max-width:34ch">
          Design, engineering and marketing under one roof, because the handoff
          between them is where most projects quietly lose their edge.
        </p>
      </div>
    </div>

    <div class="cap-list" data-stagger="70">
      {capabilities_rows()}
    </div>
  </div>
</section>

<section class="section" id="why">
  <div class="shell">
    {eyebrow('04', 'Why Noir Echelon')}
    <div class="grid mt-l">
      <div class="col-6">
        <h2 class="h3" data-reveal>
          We don't design for other designers.<br>We design for your customers.
        </h2>
      </div>
      <div class="col-5 start-8" data-reveal style="--d:120ms">
        <p class="body-copy">
          Awards are pleasant. Revenue is the point. Everything we make is judged
          against a simple question: does it make the right person more likely to
          choose you, and less likely to negotiate on price?
        </p>
        <p class="body-copy">
          That is why strategy, design, engineering and marketing sit in the same
          room here. A beautiful site that nobody finds is a portfolio piece. A
          site that ranks but looks improvised is a discount waiting to happen.
        </p>
      </div>
    </div>
    {facts_block()}
  </div>
</section>

<section class="section" id="process">
  <div class="shell">
    {eyebrow('05', 'How we work')}
    <div class="grid mt-m">
      <div class="col-7">
        <h2 class="h2" data-reveal>A process you can<br>see the whole way through.</h2>
      </div>
    </div>
    {process_block()}
  </div>
</section>

<section class="section" id="questions">
  <div class="shell">
    <div class="grid">
      <div class="col-4">
        {eyebrow('06', 'Before you ask')}
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
</section>"""
    return meta, body


CAPABILITIES = [
    ("01", "Brand &amp; identity", "identity",
     "Positioning, naming, art direction and the typographic system your business is "
     "judged by before anyone reads a word.",
     ["Positioning", "Art direction", "Guidelines"]),
    ("02", "Websites", "web",
     "Design and front-end engineering for sites that load instantly, read as considered "
     "on every device, and survive contact with your team's content.",
     ["UX / UI", "Front-end", "CMS"]),
    ("03", "E-commerce", "commerce",
     "Storefronts built to sell at full price: merchandising, product storytelling, "
     "frictionless checkout and the lifecycle email behind it.",
     ["Shopify", "Headless", "Lifecycle"]),
    ("04", "Digital marketing", "marketing",
     "Search, content and paid media that put the right people in front of the work &mdash; "
     "and stop paying for the wrong ones.",
     ["SEO", "Paid media", "Content"]),
    ("05", "Conversion &amp; growth", "growth",
     "Analytics, testing and iteration after launch, because a website is a product, "
     "not a project that ends.",
     ["Analytics", "CRO", "Testing"]),
    ("06", "Care &amp; evolution", "care",
     "Hosting, security, performance budgets, accessibility and a named person who "
     "answers when something needs to change.",
     ["Support", "Hosting", "Performance"]),
]


def capabilities_rows(link_root=""):
    rows = ""
    for idx, name, anchor, desc, tags in CAPABILITIES:
        tag_html = "".join(f'<span class="cap__tag">{t}</span>' for t in tags)
        rows += f"""
      <div class="cap" id="{anchor}" data-reveal>
        <p class="cap__idx">{idx}</p>
        <h3 class="cap__name">{name}</h3>
        <p class="cap__desc">{desc}</p>
        <div class="cap__tags">{tag_html}</div>
      </div>"""
    return rows


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
    ("Brand &amp; identity", "identity",
     "Before the website, the position.",
     "A business that cannot say what it is in one sentence cannot be designed for. "
     "We settle the position, the audience and the promise first, then build the "
     "visual system that carries it: typography, colour, art direction, photography "
     "direction and the rules that keep it consistent when we are no longer in the room.",
     ["Positioning &amp; messaging", "Visual identity", "Typography system",
      "Art direction", "Brand guidelines"]),
    ("Websites", "web",
     "Hand-built, not assembled.",
     "Every page is designed at desktop, tablet and mobile &mdash; not shrunk to fit. "
     "The front end is written by hand, so there is no page builder bloat to slow it "
     "down, and the CMS is configured around how your team actually writes. "
     "Accessibility and performance budgets are set before design starts, not "
     "retrofitted after launch.",
     ["UX &amp; information architecture", "Interface design", "Front-end engineering",
      "CMS integration", "Accessibility (WCAG 2.2 AA)", "Performance budgets"]),
    ("E-commerce", "commerce",
     "Built to sell at full price.",
     "Discounting is usually a design failure. We build storefronts that justify the "
     "price: product storytelling that answers real objections, photography direction "
     "that does the selling, a checkout with nothing in the way, and the lifecycle "
     "email that turns one order into three.",
     ["Shopify &amp; headless builds", "Merchandising &amp; product pages",
      "Checkout optimisation", "Lifecycle email &amp; flows", "Subscription &amp; loyalty"]),
    ("Digital marketing", "marketing",
     "Attention, bought carefully.",
     "Search that compounds, content with a reason to exist, and paid media held to a "
     "cost per qualified enquiry rather than impressions. We report in plain language, "
     "monthly, and we will tell you when a channel is not working for you.",
     ["Technical &amp; local SEO", "Content strategy", "Paid search &amp; social",
      "Analytics &amp; attribution", "Monthly reporting"]),
    ("Conversion &amp; growth", "growth",
     "The work after the launch.",
     "Launch produces the first honest data you have ever had about your customers. "
     "We read it: where attention goes, where people hesitate, which page loses the "
     "enquiry. Then we change one thing at a time and measure whether it helped.",
     ["Funnel &amp; session analysis", "A/B and structured testing",
      "Landing page systems", "Conversion copywriting"]),
    ("Care &amp; evolution", "care",
     "A team that answers.",
     "Hosting, monitoring, backups, security patching, dependency updates and a "
     "performance budget that is enforced, not aspirational. A named contact, a "
     "response time you can hold us to, and a monthly window for the small changes "
     "that otherwise pile up for a year.",
     ["Managed hosting", "Security &amp; monitoring", "Performance care",
      "Content updates", "Quarterly review"]),
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
          Six disciplines, one senior team, no handoff between the people who plan
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
        "description": "Tell us about the project. Five short questions, about sixty "
                       "seconds, and a reply within one business day.",
        "cta": False,
    }

    dots = ""
    for i in range(1, 6):
        cls = "progress__dot is-active" if i == 1 else "progress__dot"
        dots += f'<span class="{cls}">0{i}</span>'
        if i < 5:
            dots += '<span class="progress__line" aria-hidden="true"></span>'

    body = f"""
<section class="page-hero">
  <div class="ambient" aria-hidden="true"></div>
  <div class="shell" style="position:relative;z-index:2">
    <p class="eyebrow is-in"><span class="idx">&mdash;</span> Start a project</p>
    <div class="grid page-hero__title">
      <div class="col-9">
        <h1 class="h1 is-in">{lines('Tell us what', 'needs to change.')}</h1>
      </div>
    </div>
  </div>
</section>

<section class="section section--tight">
  <div class="shell">
    <div class="rule"></div>

    <div class="inquiry mt-xl">
      <div class="inquiry__rail">
        <p class="micro dim">Inquiry</p>
        <div class="progress" aria-hidden="true">{dots}</div>
        <div class="progress__bar" aria-hidden="true"><i></i></div>
        <p class="dim mt-m" style="font-size:var(--fs-small);max-width:26ch">
          Five questions, about sixty seconds. A senior person reads every one.
        </p>

        <div class="direct mt-l">
          <div class="direct__row">
            <h2>Prefer email</h2>
            <a href="mailto:{EMAIL}">{EMAIL}</a>
          </div>
        </div>
      </div>

      <div class="inquiry__main">
        <p class="sr-only" id="wizard-live" role="status" aria-live="polite"></p>

        <form id="inquiry-form" class="wizard-shell" novalidate
              data-endpoint=""
              action="mailto:{EMAIL}" method="post" enctype="text/plain">

          <div class="step-panel is-active" data-requires-choice="project" data-autoadvance>
            <p class="micro gold">Step 01</p>
            <h2 class="step-panel__q mt-s">What can we build for you?</h2>
            <p class="step-panel__hint">Choose the closest fit. We will refine it together.</p>
            {options('project', STEP_ONE)}
            <p class="field__err" data-for="project">Please choose one to continue</p>
          </div>

          <div class="step-panel">
            <p class="micro gold">Step 02</p>
            <h2 class="step-panel__q mt-s">Tell us about the business.</h2>
            <p class="step-panel__hint">What you do, who buys it, and what is not working right now.</p>
            <div class="field">
              <label for="company">Company</label>
              <input type="text" id="company" name="company" autocomplete="organization"
                     placeholder="Company name" data-required>
              <p class="field__err">Please add your company name</p>
            </div>
            <div class="field">
              <label for="brief">The situation</label>
              <textarea id="brief" name="brief" rows="5" data-required
                        placeholder="We sell ... our customers are ... the current site ..."></textarea>
              <p class="field__err">A sentence or two is plenty</p>
            </div>
          </div>

          <div class="step-panel" data-requires-choice="budget" data-autoadvance>
            <p class="micro gold">Step 03</p>
            <h2 class="step-panel__q mt-s">What are you looking to invest?</h2>
            <p class="step-panel__hint">An honest range helps us propose work that is actually buildable.</p>
            {options('budget', STEP_BUDGET)}
            <p class="field__err" data-for="budget">Please choose a range to continue</p>
          </div>

          <div class="step-panel" data-requires-choice="timing" data-autoadvance>
            <p class="micro gold">Step 04</p>
            <h2 class="step-panel__q mt-s">When would you like to launch?</h2>
            <p class="step-panel__hint">We take on a limited number of projects at a time.</p>
            {options('timing', STEP_TIMING)}
            <p class="field__err" data-for="timing">Please choose a timeframe to continue</p>
          </div>

          <div class="step-panel">
            <p class="micro gold">Step 05</p>
            <h2 class="step-panel__q mt-s">Your details.</h2>
            <p class="step-panel__hint">A senior person replies within one business day.</p>
            <div class="field-row">
              <div class="field">
                <label for="name">Name</label>
                <input type="text" id="name" name="name" autocomplete="name" placeholder="Full name" data-required>
                <p class="field__err">Please add your name</p>
              </div>
              <div class="field">
                <label for="email">Email</label>
                <input type="email" id="email" name="email" autocomplete="email"
                       placeholder="you@company.com" data-required>
                <p class="field__err">Please add a valid email address</p>
              </div>
            </div>
            <div class="field">
              <label for="phone">Phone <span class="dim">(optional)</span></label>
              <input type="tel" id="phone" name="phone" autocomplete="tel" placeholder="Direct line">
            </div>
            <div class="consent">
              <input type="checkbox" id="consent" name="consent" required>
              <label for="consent">
                I agree that Noir Echelon may contact me about this inquiry, and have read the
                <a href="privacy.html">privacy notice</a>.
              </label>
            </div>
            <p class="field__err" data-for="consent">Please confirm to send your inquiry</p>
          </div>

          <div class="wizard-nav">
            <button class="btn btn--solid wizard-next" type="button" data-magnetic="0.18">
              <span class="wizard-next__label">Continue</span>{ARROW}
            </button>
            <button class="wizard-back" type="button">Back</button>
            <span class="wizard-note">No obligation &middot; No sales sequence</span>
          </div>

          <p class="field__err wizard-error" hidden>
            Sending failed &mdash; please email {EMAIL} directly.
          </p>
        </form>

        <div class="inquiry-done">
          <div class="inquiry-done__mark">{STAR}</div>
          <h2 class="h3">Received.<br>Thank you.</h2>
          <p class="body-copy mt-m">
            A senior person will read your inquiry and reply within one business day
            &mdash; usually with a question or two, not a brochure.
          </p>
          <p class="body-copy">
            If it is urgent, email <a class="gold" href="mailto:{EMAIL}">{EMAIL}</a>.
          </p>
          <a class="btn mt-l" href="work.html" data-magnetic="0.18"><span>View selected work</span>{ARROW}</a>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="shell">
    <div class="grid">
      <div class="col-5">
        {eyebrow('&mdash;', 'What happens next')}
        <h2 class="h3 mt-m" data-reveal>No sales sequence.<br>Just a conversation.</h2>
      </div>
      <div class="col-6 start-7">
        <div class="process" data-stagger="80">
          <div class="step" data-reveal>
            <p class="step__num">01</p><h3 class="step__name">We read it properly</h3>
            <p class="step__body">Within one business day you hear from a senior person, not an
            automated sequence. If we are not right for the work, we say so and point you elsewhere.</p>
          </div>
          <div class="step" data-reveal>
            <p class="step__num">02</p><h3 class="step__name">A short call</h3>
            <p class="step__body">Thirty to forty-five minutes on your business, the constraints and
            what success would actually look like. Prepared for, and free.</p>
          </div>
          <div class="step" data-reveal>
            <p class="step__num">03</p><h3 class="step__name">A fixed proposal</h3>
            <p class="step__body">Scope, dated milestones and a fixed price. If it is a yes, we book
            the studio time and begin. If it is not, there is no follow-up campaign.</p>
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
    "meridian-house": {
        "eyebrow": "Property development &middot; Manchester",
        "headline": "Twelve residences,<br>sold from one page.",
        "meta": [
            ("Client", "Meridian House"),
            ("Sector", "Residential development"),
            ("Scope", "Positioning, identity, website, release portal"),
            ("Year", "2025"),
        ],
        "chapters": [
            ("The client",
             "A developer, not a marketer.",
             ["Meridian House is a twelve-residence conversion in a listed building. "
              "The developer had built carefully for two years and had eight weeks to "
              "present it &mdash; with a brochure site put together by the estate agency "
              "and photographs taken on a grey afternoon.",
              "The building was better than anything being said about it."]),
            ("The challenge",
             "The buyer decides in ninety seconds.",
             ["At this price a buyer is not comparing floor plans. They are deciding, "
              "almost immediately, whether the developer has taste and whether the "
              "building will be finished to the standard implied. Every signal on the "
              "old site &mdash; stock imagery, a cluttered enquiry form, a slow gallery "
              "&mdash; argued the opposite.",
              "There was a second problem. Agents wanted a portal for reservations; "
              "buyers wanted calm. Those two needs had to live in one product without "
              "the second ruining the first."]),
            ("The strategy",
             "Sell the address, not the amenities.",
             ["We rewrote the position around place and permanence rather than "
              "specification. Amenity lists moved behind a single, quiet link. The "
              "homepage was reduced to one line, one photograph and one action.",
              "The reservation portal was separated entirely: same identity, different "
              "room. Buyers browse; agents transact."]),
            ("The experience",
             "One page, unhurried.",
             ["A single scroll: the address, the light, the plans, the specification, "
              "the register. Typography carries the weight &mdash; a high-contrast serif "
              "at display sizes, wide-tracked capitals for navigation, and generous "
              "space that reads as confidence rather than emptiness.",
              "Photography is shown full-bleed and uncropped on mobile, art-directed "
              "per breakpoint rather than letterboxed. Motion is limited to reveals "
              "that follow the reader down the page."]),
            ("The build",
             "Static, instant, indexable.",
             ["Hand-written front end, statically rendered, served from the edge with "
              "responsive AVIF imagery and a hard performance budget. The reservation "
              "portal runs as a separate authenticated application against the same "
              "design tokens, so the two never drift apart visually.",
              "The developer's team updates availability from a CMS that offers exactly "
              "four fields, because a sales team should not be asked to operate a "
              "publishing platform."]),
            ("The result",
             "A release that looked finished before it was.",
             ["The site launched in nine weeks with the identity, the marketing site "
              "and the agent portal in place, and it now reads the way the building "
              "does &mdash; considered, quiet and expensive.",
              "<!-- Add verified commercial outcomes here once they can be evidenced. -->"]),
        ],
        "pull": "The building was better than anything being said about it.",
        "next": "atelier-varona",
    },
    "atelier-varona": {
        "eyebrow": "Ready-to-wear &middot; E-commerce",
        "headline": "A storefront built<br>to hold its price.",
        "meta": [
            ("Client", "Atelier Varona"),
            ("Sector", "Ready-to-wear"),
            ("Scope", "E-commerce design &amp; build, lifecycle marketing"),
            ("Year", "2025"),
        ],
        "chapters": [
            ("The client",
             "Twenty years of craft, sold like a catalogue.",
             ["Varona makes a small ready-to-wear collection in-house, in numbered runs. "
              "The clothes are made to last decades. The storefront was a stock theme "
              "with a discount banner at the top of every page."]),
            ("The challenge",
             "Discounting was doing the selling.",
             ["Nothing on the site explained why a coat cost what it cost &mdash; not "
              "the cloth, not the cutting, not the hours. In the absence of that "
              "argument, price becomes the only variable a customer can reason about, "
              "and the only lever the business has left is discount.",
              "The brief was not more traffic. It was margin."]),
            ("The strategy",
             "Make the craft visible before the price is.",
             ["We moved the making to the front: cloth origin, construction, the hands "
              "involved, the expected life of the garment. Product pages answer "
              "objections in the order customers actually raise them &mdash; fit, then "
              "fabric, then care, then return.",
              "The discount banner was removed. In its place, a numbered-run counter "
              "that tells the truth about scarcity instead of inventing it."]),
            ("The experience",
             "Editorial pace, retail precision.",
             ["Ivory paper, oxblood accents, and a serif that behaves like a fashion "
              "masthead. Collection pages read as a lookbook; product pages tighten "
              "into something closer to a spec sheet, because that is the moment "
              "reassurance matters more than atmosphere.",
              "Checkout is three fields shorter than it was, with wallet payments "
              "first and no account required &mdash; the only step where we removed "
              "storytelling entirely."]),
            ("The build",
             "Fast where it earns money.",
             ["Headless storefront with server-rendered collection and product pages, "
              "image transforms at the edge, and a cart that never blocks the page. "
              "Lifecycle email runs on the same design system, so a receipt looks like "
              "the shop it came from.",
              "Merchandising, copy blocks and the run counter are all editable by the "
              "studio without a developer."]),
            ("The result",
             "A shop that argues for its own prices.",
             ["The storefront launched with the full collection, lifecycle flows and a "
              "content system the atelier maintains itself &mdash; and without a single "
              "discount banner.",
              "<!-- Add verified commercial outcomes here once they can be evidenced. -->"]),
        ],
        "pull": "In the absence of an argument, price is the only variable a customer can reason about.",
        "next": "calder-roe",
    },
    "calder-roe": {
        "eyebrow": "Private wealth &middot; Advisory",
        "headline": "Quiet authority,<br>made findable.",
        "meta": [
            ("Client", "Calder &amp; Roe"),
            ("Sector", "Private wealth advisory"),
            ("Scope", "Positioning, website, SEO &amp; content"),
            ("Year", "2024"),
        ],
        "chapters": [
            ("The client",
             "Referrals only, and slowing.",
             ["A twelve-person advisory firm whose clients had always arrived by "
              "introduction. The introductions were still coming, but from a generation "
              "that was retiring &mdash; and their children were searching first and "
              "asking second."]),
            ("The challenge",
             "Credibility that does not survive a search.",
             ["The firm read as serious in a room and as invisible online. The site was "
              "a decade old, the partners' expertise existed only as PDFs, and the "
              "phrases prospective clients actually type had no page to land on.",
              "The risk in this sector runs both ways: look too commercial and you "
              "forfeit trust; stay silent and you are never considered at all."]),
            ("The strategy",
             "Publish the thinking, quietly.",
             ["We positioned the firm around patience &mdash; long horizons, few "
              "clients, no product sales &mdash; and built a small library of genuinely "
              "useful writing around the decisions clients face, mapped to real search "
              "demand rather than keyword volume.",
              "No gated downloads, no newsletter modal, no chat widget. Authority is "
              "demonstrated, not captured."]),
            ("The experience",
             "Restraint as a trust signal.",
             ["Deep green, ivory type, a generous measure and almost no ornament. "
              "Partner profiles lead with judgement rather than credentials, and every "
              "page ends with the same single, unhurried invitation to talk.",
              "The insight library is designed for reading: one column, real line "
              "height, and a typographic scale that holds at every width."]),
            ("The build",
             "Structured for search and for people.",
             ["Server-rendered pages with clean semantic structure, schema for the firm "
              "and its people, internal linking planned rather than incidental, and a "
              "CMS that lets advisers publish without breaking the layout.",
              "Accessibility was audited to WCAG 2.2 AA before launch &mdash; "
              "non-negotiable for an audience that skews older."]),
            ("The result",
             "A firm that can be found and still feel private.",
             ["The site launched with the new position, thirty pages of substantive "
              "writing and a search foundation the firm continues to build on, without "
              "a single tactic the partners would be uncomfortable explaining to a client.",
              "<!-- Add verified commercial outcomes here once they can be evidenced. -->"]),
        ],
        "pull": "Look too commercial and you forfeit trust. Stay silent and you are never considered.",
        "next": "meridian-house",
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

    figures = {
        1: f"""
<figure class="figure" data-reveal>
  <img src="{root}assets/img/work/{p['key']}-devices.svg" alt="{p['name']} — mobile screens"
       loading="lazy" decoding="async" width="1200" height="900">
  <figcaption>Mobile, art-directed rather than reflowed</figcaption>
</figure>""",
        3: f"""
<div class="figure-pair">
  <figure class="figure" data-reveal>
    <img src="{root}assets/img/work/{p['key']}-type.svg" alt="{p['name']} — typography specimen"
         loading="lazy" decoding="async" width="1200" height="900">
    <figcaption>Typographic system</figcaption>
  </figure>
  <figure class="figure" data-reveal style="--d:120ms">
    <img src="{root}assets/img/work/{p['key']}-palette.svg" alt="{p['name']} — colour and grid"
         loading="lazy" decoding="async" width="1200" height="900">
    <figcaption>Palette and twelve-column grid</figcaption>
  </figure>
</div>""",
    }

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
      <img src="{root}assets/img/work/{p['key']}-cover.svg" alt="{p['alt']}"
           width="1600" height="1000" decoding="async">
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
        case_study("meridian-house"),
        case_study("atelier-varona"),
        case_study("calder-roe"),
        privacy(),
        not_found(),
    ]

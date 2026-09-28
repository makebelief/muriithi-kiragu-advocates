from pathlib import Path
from html import escape

ROOT=Path('/mnt/data/muriithi-kiragu-advocates')
SITE='https://muriithi-kiragu-advocates.vercel.app'
WHATSAPP='https://wa.me/254738134932?text=Hello%20Advocate%20Kiragu%2C%20I%20would%20like%20to%20book%20a%20legal%20consultation.'
TIKTOK='https://www.tiktok.com/@adv_muriithikiragu_esq?lang=en'
PHONE='tel:+254738134932'
EMAIL='mailto:murithikiraguadvocate@gmail.com'

def meta(title, desc, path='/'):
    url=SITE+path
    return f'''<!doctype html>
<html lang="en-KE">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
  <title>{escape(title)}</title>
  <meta name="description" content="{escape(desc)}">
  <meta name="theme-color" content="#0a1f34">
  <link rel="icon" type="image/png" sizes="192x192" href="/assets/images/favicon-192.png">
  <link rel="apple-touch-icon" href="/assets/images/favicon-192.png">
  <link rel="canonical" href="{url}">
  <meta property="og:type" content="website">
  <meta property="og:title" content="{escape(title)}">
  <meta property="og:description" content="{escape(desc)}">
  <meta property="og:url" content="{url}">
  <meta property="og:image" content="{SITE}/assets/images/og-image.jpg">
  <meta name="twitter:card" content="summary_large_image">
  <link rel="stylesheet" href="/assets/css/site.css">
  <script type="application/ld+json">{{
    "@context":"https://schema.org",
    "@type":"LegalService",
    "name":"Muriithi S. Kiragu & Co. Advocates",
    "url":"{SITE}",
    "image":"{SITE}/assets/images/og-image.jpg",
    "telephone":["+254738134932","+254719134932"],
    "email":"murithikiraguadvocate@gmail.com",
    "address":{{"@type":"PostalAddress","streetAddress":"Longonot House, 2nd Floor, Suite S-06, Opposite Polo Centre","addressLocality":"Nakuru","addressCountry":"KE"}},
    "sameAs":["{TIKTOK}"],
    "areaServed":"Kenya"
  }}</script>
</head>'''

def header(current=''):
    items=[('Home','/','home'),('About','/about','about'),('Practice Areas','/practice-areas','practice'),('Muriithi Kiragu','/advocate','advocate'),('Insights','/insights','insights'),('Contact','/contact','contact')]
    links='\n'.join([f'<a href="{href}"'+(' aria-current="page"' if current==key else '')+f'>{label}</a>' for label,href,key in items])
    return f'''<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site-header">
  <div class="container navbar">
    <a class="brand" href="/" aria-label="Muriithi S. Kiragu & Co. Advocates home">
      <span class="brand-mark"><img src="/assets/images/logo-primary.webp" alt=""></span>
      <span class="brand-copy"><strong>Muriithi S. Kiragu & Co.</strong><span>Advocates · Nakuru</span></span>
    </a>
    <button class="menu-btn" data-menu aria-label="Open navigation" aria-expanded="false">☰</button>
    <nav class="nav-links" data-nav aria-label="Primary navigation">
      {links}
      <a class="nav-cta" href="{WHATSAPP}" target="_blank" rel="noopener">Book a consultation ↗</a>
    </nav>
  </div>
</header>'''

def dock():
    return f'''<aside class="contact-dock" aria-label="Quick contact">
  <a class="dock-link" href="{PHONE}" aria-label="Call the firm">CALL</a>
  <a class="dock-link" href="{WHATSAPP}" target="_blank" rel="noopener" aria-label="WhatsApp the firm">WA</a>
  <a class="dock-link" href="{TIKTOK}" target="_blank" rel="noopener" aria-label="TikTok profile">TT</a>
</aside>'''

def cta():
    return f'''<section class="section-tight">
  <div class="container">
    <div class="cta-panel reveal">
      <div>
        <span class="kicker">Speak to counsel</span>
        <h2>Bring the legal question into focus.</h2>
        <p>Call, WhatsApp or send an enquiry to discuss the next practical step for your matter.</p>
      </div>
      <a class="btn btn-primary" href="{WHATSAPP}" target="_blank" rel="noopener">Book a consultation ↗</a>
    </div>
  </div>
</section>'''

def footer():
    return f'''<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div class="footer-brand">
        <img src="/assets/images/logo-primary.webp" alt="Muriithi S. Kiragu & Co. Advocates logo">
        <div><h3>Muriithi S. Kiragu & Co. Advocates</h3><p>Boutique legal counsel in Nakuru for disputes, commercial matters, property, succession, employment, family, criminal defence and data protection.</p></div>
      </div>
      <div><div class="footer-title">Contact</div><div class="footer-links"><a href="{PHONE}">+254 738 134 932</a><a href="tel:+254719134932">+254 719 134 932</a><a href="{EMAIL}">murithikiraguadvocate@gmail.com</a><span>Longonot House, 2nd Floor, Suite S-06<br>Opposite Polo Centre, Nakuru</span></div></div>
      <div><div class="footer-title">Quick links</div><div class="footer-links"><a href="/practice-areas">Practice Areas</a><a href="/advocate">Muriithi Kiragu</a><a href="/insights">Insights</a><a href="{TIKTOK}" target="_blank" rel="noopener">TikTok ↗</a></div></div>
    </div>
    <div class="footer-bottom"><div>© <span data-year>2026</span> Muriithi S. Kiragu & Co. Advocates.</div><div><a href="/privacy">Privacy</a> · <a href="/terms">Terms</a></div></div>
  </div>
</footer>
<script src="/assets/js/site.js" defer></script>
</body></html>'''

practices=[
('01','Civil Litigation & Dispute Resolution','Strategic advice, negotiation and representation for civil disputes and formal court processes.'),
('02','Commercial & Contract Law','Commercial agreements, contract review, business disputes and practical legal support for enterprises.'),
('03','Conveyancing & Property Law','Due diligence, sale and transfer documentation, property transactions and related legal processes.'),
('04','Succession & Probate','Guidance on estate administration, probate, succession documentation and family estate matters.'),
('05','Employment & Labour Relations','Advice for employers and employees on workplace obligations, disputes and labour processes.'),
('06','Family Law','Clear, careful legal guidance for sensitive family matters and related proceedings.'),
('07','Criminal Law & Defence','Legal representation and procedural guidance in criminal matters and defence work.'),
('08','Data Protection & Privacy Law','Privacy compliance, data protection advisory and practical risk support for organisations and individuals.'),
]

def practice_cards():
    return '\n'.join([f'''<a class="practice-card reveal" href="/practice-areas#{i}"><span class="practice-no">{n}</span><div><h3>{title}</h3><p>{desc}</p></div><span class="arrow">View practice →</span></a>''' for (n,title,desc),i in zip(practices,['litigation','commercial','property','succession','employment','family','criminal','privacy'])])

home = meta('Muriithi S. Kiragu & Co. Advocates | Nakuru','Boutique law firm in Nakuru providing litigation, commercial, property, succession, employment, family, criminal defence and data protection legal services.') + header('home') + f'''
<main id="main">
<section class="hero">
  <div class="container hero-grid">
    <div class="hero-copy">
      <span class="kicker">Nakuru · Kenya · Advocate of the High Court</span>
      <h1>Clear counsel.<span class="display-line gold">Decisive action.</span></h1>
      <p class="lead">A boutique legal practice serving individuals, families and businesses across civil disputes, commercial law, property, succession, employment, criminal defence and data protection.</p>
      <div class="hero-actions"><a class="btn btn-primary" href="{WHATSAPP}" target="_blank" rel="noopener">Book a consultation ↗</a><a class="btn btn-ghost" href="/practice-areas">Explore practice areas</a></div>
      <div class="hero-facts"><span><strong>Office</strong><br>Longonot House, Nakuru</span><span><strong>Call / WhatsApp</strong><br>0738 134 932</span><span><strong>Professional standing</strong><br>Commissioner for Oaths · Notary Public</span></div>
    </div>
    <div class="hero-visual">
      <img class="hero-portrait" src="/assets/images/portrait-hero.webp" alt="Advocate Muriithi S. Kiragu in court attire" fetchpriority="high">
      <div class="hero-badge"><strong>Muriithi S. Kiragu</strong><span>Advocate · Founder · Nakuru</span></div>
    </div>
  </div>
</section>
<section class="stats-strip"><div class="container stats"><div class="stat"><span>Practice</span><strong>Boutique Law Firm</strong></div><div class="stat"><span>Location</span><strong>Nakuru, Kenya</strong></div><div class="stat"><span>Professional role</span><strong>Advocate of the High Court</strong></div><div class="stat"><span>Appointments</span><strong>Commissioner for Oaths · Notary Public</strong></div></div></section>
<section class="section">
  <div class="container">
    <div class="section-head"><div><span class="kicker">Practice areas</span><h2>Legal support across business, property and personal matters.</h2></div><p>The firm’s service profile covers both advisory work and disputes, with a direct point of contact from the first consultation through the next legal step.</p></div>
    <div class="practice-grid">{practice_cards()}</div>
  </div>
</section>
<section class="section" style="background:#f2f4f5">
  <div class="container split">
    <div class="photo-tile reveal"><img src="/assets/images/office.webp" alt="Muriithi S. Kiragu at his Nakuru office" loading="lazy"><div class="photo-caption"><strong>Direct counsel from Nakuru.</strong><span>Longonot House · 2nd Floor · Suite S-06</span></div></div>
    <div class="copy-block reveal"><span class="kicker">The practice</span><h2>Practical legal strategy with a personal point of contact.</h2><p>The firm focuses on making the legal position understandable, identifying the practical options available and moving matters forward with clear communication.</p><div class="check-list"><div class="check-item"><i>01</i><span><strong>Clarity.</strong> Understand the legal position before deciding the next move.</span></div><div class="check-item"><i>02</i><span><strong>Strategy.</strong> Advice shaped around the facts, documents and practical outcome.</span></div><div class="check-item"><i>03</i><span><strong>Access.</strong> Speak directly with the practice by phone, WhatsApp or email.</span></div></div><a class="btn btn-primary" href="/advocate">Meet Muriithi Kiragu</a></div>
  </div>
</section>
<section class="section dark-feature">
  <div class="container dark-grid">
    <div class="video-shell reveal"><video autoplay muted loop playsinline preload="metadata" poster="/assets/images/logo-primary.webp" aria-label="Muriithi S. Kiragu & Co. Advocates animated logo"><source src="/assets/video/logo-animation-4k60.mp4" type="video/mp4"></video></div>
    <div class="dark-copy reveal"><span class="kicker">Counsel for real decisions</span><h2>Legal issues rarely exist in isolation.</h2><p>Contracts, property, employment, family obligations, privacy and disputes often overlap. The practice brings the legal issues together so the client can see both the immediate requirement and the wider consequence.</p><div class="hero-actions"><a class="btn btn-gold" href="/about">About the firm</a><a class="btn btn-ghost" style="color:white;border-color:rgba(255,255,255,.25);background:transparent" href="/contact">Talk to the firm</a></div></div>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="section-head"><div><span class="kicker">Legal insights</span><h2>Useful starting points before you make the next move.</h2></div><p>General information only. Advice on a particular matter depends on its facts, documents and applicable law.</p></div>
    <div class="insight-grid">
      <a class="insight-card reveal" href="/insights#contracts"><div class="insight-image"><img src="/assets/images/service-commercial.webp" alt="Commercial and contract law visual" loading="lazy"></div><div class="insight-copy"><span class="tag">Commercial</span><h3>What should a strong contract address early?</h3><p>Payment, performance, risk, termination and dispute provisions matter most when the relationship becomes difficult.</p><span class="read">Read overview →</span></div></a>
      <a class="insight-card reveal" href="/insights#property"><div class="insight-image"><img src="/assets/images/service-corporate.webp" alt="Corporate and business law visual" loading="lazy"></div><div class="insight-copy"><span class="tag">Business</span><h3>Legal structure should follow the real business.</h3><p>Ownership, decision-making and liability should be considered before documents are signed.</p><span class="read">Read overview →</span></div></a>
      <a class="insight-card reveal" href="/insights#privacy"><div class="insight-image"><img src="/assets/images/service-privacy.webp" alt="Data protection and privacy law visual" loading="lazy"></div><div class="insight-copy"><span class="tag">Privacy</span><h3>Data protection is an operational issue.</h3><p>Organisations should know what personal data they hold, why they hold it and how it is protected.</p><span class="read">Read overview →</span></div></a>
    </div>
  </div>
</section>
{cta()}
</main>''' + dock() + footer()

about = meta('About | Muriithi S. Kiragu & Co. Advocates','About Muriithi S. Kiragu & Co. Advocates, a boutique Nakuru law firm serving individuals, families and businesses.','/about') + header('about') + f'''
<main id="main">
<section class="page-hero"><div class="container"><div class="breadcrumbs"><a href="/">Home</a> / About</div><span class="kicker">About the firm</span><h1>Practical legal support from Nakuru.</h1><p class="lead">A boutique practice built around clear advice, direct access to counsel and focused legal action across business, property and personal matters.</p></div></section>
<section class="section"><div class="container content-grid"><div class="side-label">The practice</div><div class="prose reveal"><h2>Counsel shaped around the decision in front of you.</h2><p>Muriithi S. Kiragu & Co. Advocates operates from Longonot House in Nakuru. The firm’s published service profile covers civil litigation, commercial and contract law, conveyancing and property, succession and probate, employment and labour relations, family law, criminal defence, and data protection and privacy law.</p><p>The firm is presented as a boutique practice: clients have a direct point of contact and legal work is approached with attention to the practical consequences surrounding the matter.</p><div class="pill-row"><span class="pill">Advocate of the High Court of Kenya</span><span class="pill">Commissioner for Oaths</span><span class="pill">Notary Public</span><span class="pill">Member, Law Society of Kenya</span></div></div></div></section>
<section class="section" style="background:#f2f4f5"><div class="container dark-grid"><div class="video-shell reveal"><video autoplay muted loop playsinline preload="metadata" poster="/assets/images/logo-primary.webp"><source src="/assets/video/logo-animation-4k60.mp4" type="video/mp4"></video></div><div class="copy-block reveal"><span class="kicker">How the firm works</span><h2>Clarity before complexity.</h2><p>The website deliberately avoids invented years of experience, case counts, awards or guaranteed outcomes. The emphasis is on what the practice publicly offers and how a client can start the conversation.</p><div class="check-list"><div class="check-item"><i>01</i><span>Understand the issue and relevant documents.</span></div><div class="check-item"><i>02</i><span>Identify the available legal and practical options.</span></div><div class="check-item"><i>03</i><span>Agree the next step and the communication route.</span></div></div><a class="btn btn-primary" href="/contact">Contact the firm</a></div></div></section>
{cta()}</main>''' + dock() + footer()

practice_detail='\n'.join([f'''<article class="practice-detail reveal" id="{pid}"><span class="num">{n}</span><h3>{title}</h3><p>{desc}</p><a class="read" href="{WHATSAPP}" target="_blank" rel="noopener">Discuss this matter →</a></article>''' for (n,title,desc),pid in zip(practices,['litigation','commercial','property','succession','employment','family','criminal','privacy'])])
practice = meta('Practice Areas | Muriithi S. Kiragu & Co. Advocates','Explore the practice areas of Muriithi S. Kiragu & Co. Advocates in Nakuru.','/practice-areas') + header('practice') + f'''
<main id="main"><section class="page-hero"><div class="container"><div class="breadcrumbs"><a href="/">Home</a> / Practice Areas</div><span class="kicker">Practice areas</span><h1>Business, property, disputes and personal legal work.</h1><p class="lead">Specific advice depends on the facts and documents of each matter. The areas below reflect the firm’s published service profile.</p></div></section><section class="section"><div class="container"><div class="practice-detail-grid">{practice_detail}</div></div></section>{cta()}</main>''' + dock() + footer()

advocate = meta('Muriithi S. Kiragu | Advocate | Nakuru','Profile of Muriithi S. Kiragu, advocate and founder of Muriithi S. Kiragu & Co. Advocates in Nakuru.','/advocate') + header('advocate') + f'''
<main id="main"><section class="page-hero"><div class="container"><div class="breadcrumbs"><a href="/">Home</a> / Muriithi Kiragu</div><span class="kicker">Advocate & founder</span><h1>Muriithi S. Kiragu.</h1><p class="lead">A direct point of contact for civil disputes, business matters, property, succession, employment, family, criminal defence and data protection work.</p></div></section>
<section class="section"><div class="container profile-grid"><div class="profile-image reveal"><img src="/assets/images/office.webp" alt="Muriithi S. Kiragu working at his Nakuru office" loading="eager"></div><div class="profile-copy reveal"><span class="kicker">Profile</span><h2>Professional advice with a practical lens.</h2><p>Muriithi S. Kiragu is presented publicly as an advocate and founder of Muriithi S. Kiragu & Co. Advocates. His firm operates from Nakuru and provides legal support across both contentious and advisory matters.</p><p>The firm’s own materials identify him as an Advocate of the High Court of Kenya, Commissioner for Oaths and Notary Public, and state that the firm is a member of the Law Society of Kenya.</p><div class="credential-list"><div class="credential"><strong>Advocate</strong><span>High Court of Kenya</span></div><div class="credential"><strong>Commissioner for Oaths</strong><span>Professional appointment</span></div><div class="credential"><strong>Notary Public</strong><span>Professional appointment</span></div><div class="credential"><strong>Nakuru</strong><span>Longonot House, 2nd Floor</span></div></div><div class="hero-actions"><a class="btn btn-primary" href="{WHATSAPP}" target="_blank" rel="noopener">Book a consultation ↗</a><a class="btn btn-ghost" href="{TIKTOK}" target="_blank" rel="noopener">View TikTok profile ↗</a></div></div></div></section>{cta()}</main>''' + dock() + footer()

insights = meta('Insights | Muriithi S. Kiragu & Co. Advocates','General legal information from Muriithi S. Kiragu & Co. Advocates on litigation, contracts, property, family, succession and data protection.','/insights') + header('insights') + f'''
<main id="main"><section class="page-hero"><div class="container"><div class="breadcrumbs"><a href="/">Home</a> / Insights</div><span class="kicker">Insights</span><h1>Questions worth asking early.</h1><p class="lead">General information only. Legal advice should be based on the particular facts, documents and applicable law of your matter.</p></div></section>
<section class="section"><div class="container insight-grid">
<article class="insight-card reveal" id="contracts"><div class="insight-image"><img src="/assets/images/service-commercial.webp" alt="Commercial contracts visual" loading="lazy"></div><div class="insight-copy"><span class="tag">Commercial</span><h3>Contracts should answer the difficult questions early.</h3><p>Payment, performance, risk allocation, termination, confidentiality and dispute mechanisms deserve attention before a commercial relationship becomes strained.</p></div></article>
<article class="insight-card reveal" id="property"><div class="insight-image"><img src="/assets/images/service-corporate.webp" alt="Business and corporate law visual" loading="lazy"></div><div class="insight-copy"><span class="tag">Business</span><h3>Structure should reflect how the business actually works.</h3><p>Ownership, control, responsibilities and risk should be considered alongside registration and paperwork.</p></div></article>
<article class="insight-card reveal"><div class="insight-image"><img src="/assets/images/service-litigation.webp" alt="Civil litigation visual" loading="lazy"></div><div class="insight-copy"><span class="tag">Litigation</span><h3>Preserve the record before a dispute escalates.</h3><p>Contracts, messages, receipts, notices and timelines may become important if negotiation develops into formal proceedings.</p></div></article>
<article class="insight-card reveal"><div class="insight-image"><img src="/assets/images/service-family.webp" alt="Family law visual" loading="lazy"></div><div class="insight-copy"><span class="tag">Family</span><h3>Sensitive matters still need clear documentation.</h3><p>Family disputes often involve urgent personal decisions alongside legal procedure. Early advice can help identify what documents and orders may be relevant.</p></div></article>
<article class="insight-card reveal" id="privacy"><div class="insight-image"><img src="/assets/images/service-privacy.webp" alt="Data protection visual" loading="lazy"></div><div class="insight-copy"><span class="tag">Privacy</span><h3>Know the personal data your organisation holds.</h3><p>Privacy compliance starts with understanding what data is collected, the reason for collection, how it is secured and who receives it.</p></div></article>
<article class="insight-card reveal"><div class="insight-image"><img src="/assets/images/service-overview.webp" alt="Overview of legal services" loading="lazy"></div><div class="insight-copy"><span class="tag">General</span><h3>Good legal advice begins with the actual decision.</h3><p>Bring the relevant documents, dates and desired outcome into focus before choosing a legal route.</p></div></article>
</div></section>{cta()}</main>''' + dock() + footer()

contact = meta('Contact | Muriithi S. Kiragu & Co. Advocates','Contact Muriithi S. Kiragu & Co. Advocates at Longonot House, Nakuru. Call or WhatsApp 0738 134 932.','/contact') + header('contact') + f'''
<main id="main"><section class="page-hero"><div class="container"><div class="breadcrumbs"><a href="/">Home</a> / Contact</div><span class="kicker">Contact</span><h1>Start with the matter at hand.</h1><p class="lead">Call, WhatsApp or prepare an email enquiry. The firm is located at Longonot House, 2nd Floor, Suite S-06, opposite Polo Centre in Nakuru.</p></div></section>
<section class="section"><div class="container contact-grid"><div><span class="kicker">Contact details</span><h2 style="color:var(--navy);margin:16px 0 10px">Speak directly with the firm.</h2><div class="contact-list"><div class="contact-item"><span>Phone / WhatsApp</span><a href="{PHONE}">+254 738 134 932</a><a href="tel:+254719134932">+254 719 134 932</a></div><div class="contact-item"><span>Email</span><a href="{EMAIL}">murithikiraguadvocate@gmail.com</a></div><div class="contact-item"><span>Office</span><strong>Longonot House, 2nd Floor, Suite S-06<br>Opposite Polo Centre, Nakuru</strong></div><div class="contact-item"><span>Social</span><a href="{TIKTOK}" target="_blank" rel="noopener">@adv_muriithikiragu_esq ↗</a></div></div></div>
<form class="form-card" data-enquiry-form><div class="field"><label for="name">Your name</label><input id="name" name="name" autocomplete="name" required></div><div class="field"><label for="phone">Phone number</label><input id="phone" name="phone" inputmode="tel" autocomplete="tel"></div><div class="field"><label for="email">Email address</label><input id="email" name="email" type="email" autocomplete="email"></div><div class="field"><label for="matter">Matter type</label><select id="matter" name="matter"><option>Civil Litigation & Dispute Resolution</option><option>Commercial & Contract Law</option><option>Conveyancing & Property Law</option><option>Succession & Probate</option><option>Employment & Labour Relations</option><option>Family Law</option><option>Criminal Law & Defence</option><option>Data Protection & Privacy Law</option><option>General legal enquiry</option></select></div><div class="field"><label for="message">Briefly describe the issue</label><textarea id="message" name="message" required></textarea></div><button class="btn btn-primary" type="submit">Prepare email enquiry</button><p class="form-note">Submitting this form opens an email draft on your device. It does not by itself create an advocate-client relationship.</p></form></div>
<div class="container map-shell"><iframe title="Map to Longonot House, Nakuru" loading="lazy" referrerpolicy="no-referrer-when-downgrade" src="https://www.google.com/maps?q=Longonot%20House%2C%20Nakuru%2C%20Kenya&output=embed"></iframe></div></section>{cta()}</main>''' + dock() + footer()

privacy = meta('Privacy | Muriithi S. Kiragu & Co. Advocates','Website privacy notice for Muriithi S. Kiragu & Co. Advocates.','/privacy') + header('') + f'''
<main id="main"><section class="page-hero"><div class="container"><span class="kicker">Legal notice</span><h1>Privacy.</h1><p class="lead">How information sent through this website is handled.</p></div></section><section class="section"><div class="container legal-wrap"><h2>Website enquiries</h2><p>The contact form prepares an email using your device. Information you choose to send may include your name, contact details and a short description of your matter.</p><h2>No automatic advocate-client relationship</h2><p>Sending an enquiry does not by itself create an advocate-client relationship. Avoid sending highly confidential or time-sensitive material until the firm confirms how it should be received.</p><h2>Third-party services</h2><p>This website may link to WhatsApp, TikTok, Google Maps and email services. Those services operate under their own privacy terms.</p><h2>Contact</h2><p>For privacy questions, email <a href="{EMAIL}">murithikiraguadvocate@gmail.com</a>.</p></div></section></main>''' + dock() + footer()

terms = meta('Terms | Muriithi S. Kiragu & Co. Advocates','Website terms for Muriithi S. Kiragu & Co. Advocates.','/terms') + header('') + f'''
<main id="main"><section class="page-hero"><div class="container"><span class="kicker">Legal notice</span><h1>Terms.</h1><p class="lead">General terms for use of this website.</p></div></section><section class="section"><div class="container legal-wrap"><h2>General information</h2><p>Content on this website is general information and is not a substitute for legal advice based on the facts and documents of a particular matter.</p><h2>No guarantee of outcome</h2><p>Past experience, legal information or discussion of a legal process should not be read as a guarantee of any outcome.</p><h2>External links</h2><p>Links to third-party services are provided for convenience. The firm does not control their content or availability.</p><h2>Contact</h2><p>To discuss a legal matter, call <a href="{PHONE}">+254 738 134 932</a> or email <a href="{EMAIL}">murithikiraguadvocate@gmail.com</a>.</p></div></section></main>''' + dock() + footer()

notfound = meta('Page not found | Muriithi S. Kiragu & Co. Advocates','The requested page could not be found.','/404') + header('') + f'''<main id="main"><section class="page-hero" style="min-height:60vh;display:grid;align-items:center"><div class="container"><span class="kicker">404</span><h1>That page is not here.</h1><p class="lead">Return to the main website or contact the firm directly.</p><div class="hero-actions"><a class="btn btn-primary" href="/">Back home</a><a class="btn btn-ghost" href="/contact">Contact the firm</a></div></div></section></main>''' + dock() + footer()

pages={'index.html':home,'about.html':about,'practice-areas.html':practice,'advocate.html':advocate,'insights.html':insights,'contact.html':contact,'privacy.html':privacy,'terms.html':terms,'404.html':notfound}
for name,html in pages.items():
    (ROOT/name).write_text(html,encoding='utf-8')

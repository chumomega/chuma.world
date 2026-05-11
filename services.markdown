---
layout: page
title: Services
permalink: /services/
---

<!-- Hero -->
<section class="services-hero">
  <h1>Launch the thing you've been meaning to launch.</h1>
  <p class="services-hero-tagline">
    I built and launched products at <strong>Bloomberg</strong>, <strong>Amazon</strong>, and <strong>Etsy</strong>. Now I help builders launch the things they couldn't on their own — fast, live on the web, and built to keep building on.
  </p>
  <a href="https://calendly.com/chumaokoro/scoping-call/" class="cta-button">Book a 20-min scoping call</a>
</section>

<!-- Credibility strip — companies first (signals seniority), then
     products (signals "this person ships their own work"). Sits
     between hero and the problem framing so prospects warm up to
     the credentialing before reading the rest of the page. -->
<section class="services-trust">
  <div class="services-trust-block">
    <h3>I've shipped at</h3>
    <div class="logo-marquee">
      <div class="logo-marquee-track">
        <img src="{{ site.baseurl }}/assets/Bloomberg_logo.svg" alt="Bloomberg">
        <img src="{{ site.baseurl }}/assets/amazon_ads.png" alt="Amazon Ads">
        <img src="{{ site.baseurl }}/assets/Etsy_logo.png" alt="Etsy">
        <img src="{{ site.baseurl }}/assets/cuny_tech_prep_logo.png" alt="CUNY Tech Prep">
        <img src="{{ site.baseurl }}/assets/justworks_logo.png" alt="Justworks">
        <img src="{{ site.baseurl }}/assets/Mastercard-logo.svg" alt="Mastercard">
        <img src="{{ site.baseurl }}/assets/ConEd_logo.svg" alt="Con Edison">
        <!-- duplicated for seamless loop -->
        <img src="{{ site.baseurl }}/assets/Bloomberg_logo.svg" alt="Bloomberg">
        <img src="{{ site.baseurl }}/assets/amazon_ads.png" alt="Amazon Ads">
        <img src="{{ site.baseurl }}/assets/Etsy_logo.png" alt="Etsy">
        <img src="{{ site.baseurl }}/assets/cuny_tech_prep_logo.png" alt="CUNY Tech Prep">
        <img src="{{ site.baseurl }}/assets/justworks_logo.png" alt="Justworks">
        <img src="{{ site.baseurl }}/assets/Mastercard-logo.svg" alt="Mastercard">
        <img src="{{ site.baseurl }}/assets/ConEd_logo.svg" alt="Con Edison">
      </div>
    </div>
  </div>

  <div class="services-trust-block">
    <h3>And built on my own</h3>
    <div class="projects-strip-grid">
      <a class="project-tile" href="https://apps.apple.com/us/app/tempo64/id6764440731">
        <img src="{{ site.baseurl }}/assets/tempo64_icon.png" alt="Tempo64 app icon" />
        <span class="project-tile-name">Tempo64</span>
        <span class="project-tile-tag">Chess games as shorts.</span>
      </a>
      <a class="project-tile" href="https://apps.apple.com/us/app/echochamber-break-the-bubble/id6753664425">
        <img src="{{ site.baseurl }}/assets/echo_chamber_icon.jpg" alt="Echo Chamber app icon" />
        <span class="project-tile-name">Echo Chamber</span>
        <span class="project-tile-tag">Break the bubble.</span>
      </a>
      <a class="project-tile" href="https://apps.apple.com/us/app/podrank-podcast-insights/id6746962404">
        <img src="{{ site.baseurl }}/assets/podrank_icon.jpg" alt="PodRank app icon" />
        <span class="project-tile-name">PodRank</span>
        <span class="project-tile-tag">Know before you listen.</span>
      </a>
      <a class="project-tile" href="https://apps.apple.com/us/app/scalepal-weight-tracker/id6752838575">
        <img src="{{ site.baseurl }}/assets/scalepal_icon.jpg" alt="ScalePal app icon" />
        <span class="project-tile-name">ScalePal</span>
        <span class="project-tile-tag">Weigh-ins without anxiety.</span>
      </a>
    </div>
  </div>
</section>

<!-- The Method -->
<section class="services-method">
  <h2>How I work</h2>
  <ol class="services-method-list">
    <li>
      <h3>Plan</h3>
      <p>Architecture before code. We scope on a call; you see "done" before I write a line.</p>
    </li>
    <li>
      <h3>Build</h3>
      <p>AI agents draft, I direct. Fast, without cutting corners.</p>
    </li>
    <li>
      <h3>Review</h3>
      <p>Every diff goes through me. Same bar as Bloomberg, Amazon, Etsy.</p>
    </li>
    <li>
      <h3>Launch</h3>
      <p>Deployed to your hosting — Vercel, Railway, the App Store — wired to your domain.</p>
    </li>
    <li>
      <h3>Handoff</h3>
      <p>You leave with the repo, a <code>CLAUDE.md</code>, and a 30-min Claude Code setup session.</p>
    </li>
  </ol>
</section>

<!-- Proof / Case Studies -->
<section class="services-proof">
  <h2>What this looks like in practice</h2>
  <p class="services-proof-intro">Featured case studies from my own work — and a link to the rest.</p>
  <div class="case-study case-study--with-media">
    <video class="case-study-media case-study-media--landscape"
           autoplay muted loop playsinline
           poster="{{ site.baseurl }}/assets/demos/sneakysneaks-poster.jpg">
      <source src="{{ site.baseurl }}/assets/demos/sneakysneaks.mp4" type="video/mp4">
      <source src="{{ site.baseurl }}/assets/demos/sneakysneaks.webm" type="video/webm">
    </video>
    <div class="case-study-body">
      <h3>SneakySneaks — modernized & launched</h3>
      <p>
        A sneaker app frozen on Spring Boot 2 and React 15. I rebuilt it on Spring Boot 3.3 + Java 17, React 18 + Webpack 5, swapped in PostgreSQL with form-based auth, added realtime updates over WebSocket, and deployed it to Railway as a single artifact. Documented in a <code>CLAUDE.md</code> at the repo root so it stays maintainable.
      </p>
      <p class="case-study-meta">
        Stack: Spring Boot 3.3 · Java 17 · React 18 · PostgreSQL · WebSocket/STOMP · Railway
      </p>
    </div>
  </div>
  <div class="case-study case-study--with-media">
    <video class="case-study-media case-study-media--portrait"
           autoplay muted loop playsinline
           poster="{{ site.baseurl }}/assets/demos/tempo64-poster.jpg">
      <source src="{{ site.baseurl }}/assets/demos/tempo64.mp4" type="video/mp4">
    </video>
    <div class="case-study-body">
      <h3>Tempo64 — chess games as vertical shorts</h3>
      <p>
        A native iOS app that turns a PGN or chess.com link into a 1080×1920 H.264 short with timed SFX — gunshots on hanging pieces, "fahh / bruh / rizz" on check, a TikTok-core flourish on mate. Rendered on-device with AVFoundation; no server, no upload. Shipped with a chess.com URL importer (callback API + Published-Data archive) so users can paste a link instead of hunting for the PGN. Project layout managed via XcodeGen, audio mix composed in float32 PCM, video and audio rendered in parallel and muxed via AVAssetExportSession.
      </p>
      <p class="case-study-meta">
        Stack: Swift · SwiftUI · AVFoundation · ChessKit · XcodeGen · GitHub Pages (marketing)
      </p>
    </div>
  </div>
  <div class="services-proof-more">
    <a href="{{ site.baseurl }}/projects/" class="cta-button cta-button--outline">See all my projects →</a>
  </div>
</section>

<!-- Services -->
<section class="services-tiers">
  <h2>Services</h2>

  <div class="service-card">
    <h3>Portfolio Site</h3>
    <p class="service-price">Starts at $500</p>
    <p class="service-tagline">A presence that doesn't look like a template.</p>
    <ul>
      <li>Custom-designed personal site or landing page</li>
      <li>Mobile-responsive, fast, accessible</li>
      <li>Deployed to your hosting with HTTPS</li>
      <li>30-min Claude Code setup session so you can iterate yourself</li>
      <li>Documented codebase you own outright</li>
    </ul>
    <p class="service-not-included"><strong>Not included:</strong> ongoing content writing, photoshoots, branding from scratch.</p>
    <p class="service-timeline">Typical timeline: 1–2 weeks.</p>
    <a href="https://calendly.com/chumaokoro/scoping-call/" class="cta-button cta-button--outline">Book a scoping call</a>
  </div>

  <div class="service-card">
    <h3>iOS App + App Store Submission</h3>
    <p class="service-price">Starts at $1,500</p>
    <p class="service-tagline">Your first app, in the App Store, with your name on it.</p>
    <ul>
      <li>A working iOS app built around your idea</li>
      <li>Submitted to the App Store under your developer account</li>
      <li>Walkthrough of how to update it yourself</li>
      <li>Source code + documentation</li>
    </ul>
    <p class="service-not-included"><strong>Not included:</strong> Apple Developer Program fee ($99/yr — yours to keep), guaranteed App Store approval (Apple decides), backend services beyond what the app needs.</p>
    <p class="service-timeline">Typical timeline: 2–4 weeks (plus Apple's review window).</p>
    <a href="https://calendly.com/chumaokoro/scoping-call/" class="cta-button cta-button--outline">Book a scoping call</a>
  </div>

  <div class="service-card">
    <h3>Full-Stack Web App</h3>
    <p class="service-price">Starts at $3,500</p>
    <p class="service-tagline">A real product, with a real backend, deployed and yours.</p>
    <ul>
      <li>Frontend + backend + database, architected to scale</li>
      <li>User auth, deployment, and your custom domain wired up</li>
      <li>Code review and architecture decisions documented</li>
      <li>Handoff session covering how to extend it</li>
    </ul>
    <p class="service-not-included"><strong>Not included:</strong> hosting/database costs (passed through at-cost), payments integration unless scoped in, ongoing maintenance.</p>
    <p class="service-timeline">Typical timeline: 3–6 weeks. 30/30/40 payment milestones.</p>
    <a href="https://calendly.com/chumaokoro/scoping-call/" class="cta-button cta-button--outline">Book a scoping call</a>
  </div>
</section>

<!-- Why Me -->
<section class="services-why-me">
  <h2>Why me</h2>
  <p>
    You're not hiring a freelancer who learned this last quarter. You're hiring a senior engineer who happens to launch faster than most.
  </p>
</section>

<!-- FAQ -->
<section class="services-faq">
  <h2>FAQ</h2>

  <div class="faq-item">
    <h3>Did you use AI to build this?</h3>
    <p>Yes — AI writes the first draft. I review every line, refactor what doesn't meet my bar, and own the result. You're hiring a senior engineer with a decade of production experience at Bloomberg, Amazon, and Etsy — not a prompt-and-pray service.</p>
  </div>

  <div class="faq-item">
    <h3>Why not use Cursor or Lovable myself?</h3>
    <p>You can. Most people get 60% of the way and stall on auth, deployment, or the next feature. I get you to a launched, working app — and on the handoff call, I teach you how to keep going.</p>
  </div>

  <div class="faq-item">
    <h3>Will I be locked into your work?</h3>
    <p>No. You own the repo. You get a <code>CLAUDE.md</code> documenting the codebase so any engineer — or you, with Claude Code — can pick up where I left off.</p>
  </div>

  <div class="faq-item">
    <h3>What if I don't like the output?</h3>
    <p>Each tier includes two rounds of revisions on the deliverable. We catch most direction issues during the planning phase before any code is written, which is why scoping calls matter.</p>
  </div>

  <div class="faq-item">
    <h3>How does payment work?</h3>
    <p>Stripe Invoice. 50% deposit upfront, 50% on delivery for the portfolio and iOS tiers. Full-stack tier is 30/30/40 against milestones we agree on in the Statement of Work (a one-page scope doc I send before any deposit).</p>
  </div>

  <div class="faq-item">
    <h3>Can you sign an NDA?</h3>
    <p>Yes. Send yours, or I'll provide a simple one. Default for every project is that your code, designs, and ideas are confidential.</p>
  </div>
</section>

<!-- Final CTA -->
<section class="services-cta">
  <h2>Ready to launch?</h2>
  <p>20 minutes. We scope your project, see if it's a fit, and you walk away with a clearer plan either way.</p>
  <a href="https://calendly.com/chumaokoro/scoping-call/" class="cta-button">Book a 20-min scoping call</a>
  <p class="services-cta-fallback">
    Or <a href="mailto:chuma.okoro76@gmail.com">email me</a> with a sentence about your project.
  </p>
</section>

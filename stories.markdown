---
layout: page
title: Stories
permalink: /stories/
---

<p class="page-intro">
  Articles I've written, talks I've given, interviews I've done, and the coaching sessions I've recorded — collected here.
</p>

<!-- Articles (rendered async from Medium + POCIT RSS feeds) -->
<div id="medium-feed">
  <div id="articles-pocit"><p class="article-loading">Loading POCIT articles…</p></div>
  <div id="articles-medium"><p class="article-loading">Loading Medium articles…</p></div>
</div>

<!-- Videos (rendered async from YouTube playlist RSS feeds) -->
<div id="video-feed">
  <div id="videos-presentations"><p class="article-loading">Loading presentations…</p></div>
  <div id="videos-interviews"><p class="article-loading">Loading interviews…</p></div>
  <div id="videos-podcasts"><p class="article-loading">Loading podcast features…</p></div>
  <div id="videos-coaching"><p class="article-loading">Loading coaching sessions…</p></div>
</div>

<script>
  document.addEventListener("DOMContentLoaded", function() {
    const MAX_ITEMS = 4;

    function stripHtml(html) {
      const tmp = document.createElement('div');
      tmp.innerHTML = html;
      return (tmp.textContent || tmp.innerText || '').replace(/\s+/g, ' ').trim();
    }

    function firstImageFromHtml(html) {
      const tmp = document.createElement('div');
      tmp.innerHTML = html;
      const img = tmp.querySelector('img');
      return img ? img.src : '';
    }

    function fetchFeed(url) {
      return fetch(`https://api.rss2json.com/v1/api.json?rss_url=${encodeURIComponent(url)}`)
        .then(r => r.json())
        .then(d => d.items || [])
        .catch(() => []);
    }

    /* ── Articles ───────────────────────────────────────── */
    function renderArticleCard(item, sourceLabel) {
      const date = new Date(item.pubDate).toLocaleDateString('en-US', { year: 'numeric', month: 'long' });
      const excerpt = stripHtml(item.description).slice(0, 160).trim() + '…';
      const imgSrc = item.thumbnail || firstImageFromHtml(item.description);
      const img = imgSrc
        ? `<img class="article-card-img" src="${imgSrc}" alt="${item.title}" loading="lazy" />`
        : '';
      return `
        <div class="article-card">
          ${img}
          <div class="article-card-body">
            <a class="article-title" href="${item.link}" target="_blank" rel="noopener">${item.title}</a>
            <p class="article-meta">${date}</p>
            <p class="article-excerpt">${excerpt}</p>
            <a class="article-read-more" href="${item.link}" target="_blank" rel="noopener">Read on ${sourceLabel} →</a>
          </div>
        </div>`;
    }

    function renderArticleSection(heading, shortLabel, items, moreUrl, moreLabel) {
      if (!items || !items.length) {
        return `<p>Could not load ${heading} articles.</p>`;
      }
      const visible = items.slice(0, MAX_ITEMS);
      return `
        <section class="article-section">
          <h2 class="article-section-heading">${heading}</h2>
          <div class="article-grid">${visible.map(item => renderArticleCard(item, shortLabel)).join('')}</div>
          <div class="article-cta">
            <a href="${moreUrl}" target="_blank" rel="noopener" class="cta-button cta-button--outline">${moreLabel} →</a>
          </div>
        </section>`;
    }

    fetchFeed('https://peopleofcolorintech.com/author/chuma-okoro/feed/').then(items => {
      document.getElementById('articles-pocit').innerHTML = renderArticleSection(
        'People of Color in Tech (POCIT)', 'POCIT', items,
        'https://peopleofcolorintech.com/author/chuma-okoro/',
        'More on POCIT'
      );
    });

    fetchFeed('https://medium.com/feed/@chumomega').then(items => {
      document.getElementById('articles-medium').innerHTML = renderArticleSection(
        'Medium', 'Medium', items,
        'https://medium.com/@chumomega',
        'More on Medium'
      );
    });

    /* ── Videos ─────────────────────────────────────────── */
    function videoIdFromLink(link) {
      const m = link && link.match(/[?&]v=([^&]+)/);
      return m ? m[1] : '';
    }

    function renderVideoCard(item) {
      const id = videoIdFromLink(item.link);
      const date = new Date(item.pubDate).toLocaleDateString('en-US', { year: 'numeric', month: 'long' });
      const thumb = id ? `https://i.ytimg.com/vi/${id}/mqdefault.jpg` : '';
      const img = thumb
        ? `<div class="video-card-thumb"><img src="${thumb}" alt="${item.title}" loading="lazy" /></div>`
        : '';
      return `
        <a class="video-card" href="${item.link}" target="_blank" rel="noopener" aria-label="Watch ${item.title} on YouTube">
          ${img}
          <div class="video-card-body">
            <span class="video-card-title">${item.title}</span>
            <span class="video-card-meta">${date}</span>
          </div>
        </a>`;
    }

    function renderVideoSection(heading, blurb, items, playlistUrl) {
      if (!items || !items.length) {
        return `
          <section class="article-section">
            <h2 class="article-section-heading">${heading}</h2>
            <p>${blurb}</p>
            <p>Could not load videos. <a href="${playlistUrl}" target="_blank" rel="noopener">Watch on YouTube →</a></p>
          </section>`;
      }
      const visible = items.slice(0, MAX_ITEMS);
      return `
        <section class="article-section">
          <h2 class="article-section-heading">${heading}</h2>
          <p>${blurb}</p>
          <div class="article-grid">${visible.map(renderVideoCard).join('')}</div>
          <div class="article-cta">
            <a href="${playlistUrl}" target="_blank" rel="noopener" class="cta-button cta-button--outline">Watch all on YouTube →</a>
          </div>
        </section>`;
    }

    function loadPlaylist(elementId, heading, blurb, playlistId) {
      const playlistUrl = `https://www.youtube.com/playlist?list=${playlistId}`;
      const rssUrl = `https://www.youtube.com/feeds/videos.xml?playlist_id=${playlistId}`;
      fetchFeed(rssUrl).then(items => {
        document.getElementById(elementId).innerHTML = renderVideoSection(heading, blurb, items, playlistUrl);
      });
    }

    loadPlaylist(
      'videos-presentations',
      'My Presentations',
      'Talks I delivered or was part of.',
      'PL7Zul4bhud0sclwVb8HrNY_q8UJVlZIkj'
    );

    loadPlaylist(
      'videos-interviews',
      'Interviews',
      '1-on-1 conversations with industry professionals in business and technology.',
      'PL7Zul4bhud0vgi8wqzhTm4Sup1a2Lv-NU'
    );

    loadPlaylist(
      'videos-podcasts',
      'Podcast Features',
      "Podcasts I've appeared on.",
      'PL7Zul4bhud0ss5L2wDx2RJmrVbIbq2N4Z'
    );

    loadPlaylist(
      'videos-coaching',
      'Coaching Sessions',
      '1-on-1 coaching calls I offered to people on LinkedIn looking for help breaking into or growing in tech.',
      'PL7Zul4bhud0tYjz08RZXYczu0C2koBB_7'
    );
  });
</script>

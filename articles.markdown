---
layout: page
title: Articles
permalink: /articles/
---

<div id="medium-feed">
  <div id="articles-pocit"><p class="article-loading">Loading POCIT articles…</p></div>
  <div id="articles-medium"><p class="article-loading">Loading Medium articles…</p></div>
</div>

<script>
  document.addEventListener("DOMContentLoaded", function() {
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

    function renderCard(item, sourceLabel) {
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

    function renderSection(heading, shortLabel, items, moreUrl, moreLabel) {
      if (!items || !items.length) {
        return `<p>Could not load ${heading} articles.</p>`;
      }
      return `
        <section class="article-section">
          <h2 class="article-section-heading">${heading}</h2>
          <div class="article-grid">${items.map(item => renderCard(item, shortLabel)).join('')}</div>
          <div class="article-cta">
            <a href="${moreUrl}" target="_blank" rel="noopener" class="cta-button cta-button--outline">${moreLabel} →</a>
          </div>
        </section>`;
    }

    function fetchFeed(url) {
      return fetch(`https://api.rss2json.com/v1/api.json?rss_url=${encodeURIComponent(url)}`)
        .then(r => r.json())
        .then(d => d.items || [])
        .catch(() => []);
    }

    fetchFeed('https://peopleofcolorintech.com/author/chuma-okoro/feed/').then(items => {
      document.getElementById('articles-pocit').innerHTML = renderSection(
        'People of Color in Tech (POCIT)', 'POCIT', items,
        'https://peopleofcolorintech.com/author/chuma-okoro/',
        'More on POCIT'
      );
    });

    fetchFeed('https://medium.com/feed/@chumomega').then(items => {
      document.getElementById('articles-medium').innerHTML = renderSection(
        'Medium', 'Medium', items,
        'https://medium.com/@chumomega',
        'More on Medium'
      );
    });
  });
</script>

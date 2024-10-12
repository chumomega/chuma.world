---
layout: page
title: Articles
permalink: /articles/
---
<div id="medium-feed"></div>

<script>
  document.addEventListener("DOMContentLoaded", function() {
    const mediumFeedContainer = document.getElementById('medium-feed');
    const mediumUsername = 'chumomega'; // Replace with your Medium username
    const mediumFeedUrl = `https://api.rss2json.com/v1/api.json?rss_url=https://medium.com/feed/@${mediumUsername}`;

    fetch(mediumFeedUrl)
      .then(response => response.json())
      .then(data => {
        const items = data.items;
        let articles = '';

        items.forEach(item => {
          const title = item.title;
          const link = item.link;

          // Parse description for the subtitle and image
          const parser = new DOMParser();
          const doc = parser.parseFromString(item.description, 'text/html');
          
          // Extract subtitle (first <h4> tag) and image (first <img> tag)
          const subtitle = doc.querySelector('h4') ? doc.querySelector('h4').textContent : '';
          const imageUrl = doc.querySelector('img') ? doc.querySelector('img').src : '';

          articles += `
            <div>
              <h2><a href="${link}" target="_blank">${title}</a></h2>
              <p>${subtitle}</p>
              ${imageUrl ? `<img src="${imageUrl}" alt="${title}" />` : ''}
              <br><br>
            </div>
          `;
        });

        // Add articles to the container
        mediumFeedContainer.innerHTML = `${articles}`;

        // Add "See more on Medium" link
        mediumFeedContainer.innerHTML += `
          <br/>
          <div>
            <h2><a href="https://medium.com/@${mediumUsername}" target="_blank">See more articles on Medium</a></h2>
          </div>
        `;

        // Add anchor links after Medium feed is injected
        addAnchorsToHeaders();
      })
      .catch(error => {
        console.error('Error fetching Medium feed:', error);
      });
  });
</script>

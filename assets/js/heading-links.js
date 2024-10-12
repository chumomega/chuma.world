// Function to add anchors to headers
function addAnchorsToHeaders() {
  const headers = document.querySelectorAll('h1, h2, h3, h4, h5, h6');

  headers.forEach(function(header) {
    if (!header.querySelector('.header-anchor')) {  // Avoid adding duplicate anchors
      const anchor = document.createElement('a');
      const id = header.textContent.trim().toLowerCase().replace(/\s+/g, '-'); // Generate ID from title text
      header.id = id;  // Set header ID if not already present
      anchor.href = `#${id}`;
      anchor.className = 'header-anchor';
      anchor.innerHTML = '#';  // Anchor icon
      header.insertBefore(document.createTextNode(' '), header.firstChild)
      header.insertBefore(anchor, header.firstChild);  // Insert at the beginning of header
    }
  });
}

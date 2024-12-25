---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: page
title: About Me
permalink: /
---
<link rel="icon" type="image/png" href="{{ site.baseurl }}/assets/favicon/favicon-48x48.png" sizes="48x48" />
<link rel="icon" type="image/svg+xml" href="{{ site.baseurl }}/assets/favicon/favicon.svg" />
<link rel="shortcut icon" href="{{ site.baseurl }}/assets/favicon/favicon.ico" />
<link rel="apple-touch-icon" sizes="180x180" href="{{ site.baseurl }}/assets/favicon/apple-touch-icon.png" />
<link rel="manifest" href="{{ site.baseurl }}/assets/favicon/site.webmanifest" />

<!-- About Section -->
<section id="about">
  <img src="{{ site.baseurl }}/assets/IMG_7400.JPG" alt="chuma image" width="400" style="max-width: 100%;"/>
  <p>
    I’m a thoughtful and creative engineering leader with over 6 years of experience building efficient and scalable software to solve problems for customers. My passion lies in creating impactful solutions, fostering teamwork, and educating others.
  </p>
  <a href="https://calendly.com/chumomega/free-consult" target="_blank" class="cta-button">Schedule Free Coaching</a>
</section>
<br/>
<section id="logos">
  <h2>I've Worked With</h2>
  <div class="logo-carousel">
    <div class="logo-item"><img src="{{ site.baseurl }}/assets/Bloomberg_logo.svg" alt="Bloomberg Logo"></div>
    <div class="logo-item"><img src="{{ site.baseurl }}/assets/Etsy_logo.svg" alt="Etsy Logo"></div>
    <div class="logo-item"><img src="{{ site.baseurl }}/assets/amazon_ads.jpg" alt="Amazon Ads Logo"></div>
    <div class="logo-item"><img src="{{ site.baseurl }}/assets/justworks_logo.png" alt="Justworks Logo"></div>
    <div class="logo-item"><img src="{{ site.baseurl }}/assets/Mastercard-logo.svg" alt="Mastercard Logo"></div>
    <div class="logo-item"><img src="{{ site.baseurl }}/assets/JobDiva-Logo.png" alt="JobDiva Logo"></div>
    <div class="logo-item"><img src="{{ site.baseurl }}/assets/nyc_cchr_logo.jpg" alt="NYC Commission on Human Rights Logo"></div>
    <div class="logo-item"><img src="{{ site.baseurl }}/assets/cuny_tech_prep_logo.png" alt="CUNY Tech Prep Logo"></div>
    <div class="logo-item"><img src="{{ site.baseurl }}/assets/ConEd_logo.svg" alt="Con Edison Logo"></div>
  </div>
</section>

<!-- Styles -->
<style>
  .cta-button {
    background-color: #014397; /* Secondary color */
    color: #fff;
    padding: 10px 20px;
    border-radius: 5px;
    text-decoration: none;
    font-weight: bold;
  }

  .cta-button:hover {
    transform: scale(1.1); /* Slightly enlarge the button */
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2); /* Add a subtle shadow */
    text-decoration: none; /* Remove underline on hover */
  }

  .cta-button:active {
    background-color: #014397; /* Maintain color after click */
    color: #fff; /* White text remains */
    text-decoration: none; /* Ensure no underline */
  }

  .cta-button:visited {
    background-color: #014397; /* Match default color to avoid dark blue */
    color: #fff; /* Keep white text */
    text-decoration: none; /* Remove underline for visited */
  }
  
  .logo-carousel {
    display: flex;
    gap: 20px;
    overflow: hidden;
    height: 100px; /* Fixed height for the carousel */
    align-items: center;
    position: relative;
    white-space: nowrap;
  }

  .logo-item {
    flex: 0 0 auto;
    display: inline-block;
    height: 100%; /* Match the fixed height of the carousel */
    display: flex;
    justify-content: center;
    align-items: center;
  }

  .logo-item img {
    height: 100%;
    width: auto; /* Allow width to scale proportionally */
  }

  @keyframes scroll-carousel {
    0% {
      transform: translateX(0);
    }
    100% {
      transform: translateX(calc(-50%)); /* Scroll halfway through the carousel */
    }
  }

  .logo-carousel {
    animation: scroll-carousel 20s linear infinite;
  }
</style>

<!-- Script -->
<script>
  document.addEventListener("DOMContentLoaded", function () {
    const logoCarousel = document.querySelector('.logo-carousel');
    const logos = Array.from(logoCarousel.children);

    // Duplicate the logos for seamless scrolling
    logos.forEach(logo => {
      logoCarousel.appendChild(logo.cloneNode(true));
    });

    // Ensure all logos are visible
    logoCarousel.style.width = `${logoCarousel.scrollWidth}px`;
  });
</script>

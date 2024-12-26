---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: home
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
  <p>
    Hello! My name is Chuma Okoro and welcome to my space on the internet.
  </p>
  <img src="{{ site.baseurl }}/assets/IMG_7400.JPG" alt="chuma image" width="400" style="max-width: 100%;"/>
  <br/>
  <br/>
  <p>
    <a href="https://calendly.com/chumomega/free-consult" target="_blank" class="cta-button">Schedule 1v1 Coaching</a>
  </p>

  <h2>Background</h2>
  <p>
    Since my youth as a child of Nigerian immigrants, I was fascinated with computers and business. When I got my first computer, I was hooked. I played games, watched cartoons, and downloaded music. Because internet in my home was shoddy and resources were low, I had to learn new ways to gain value from the system. This meant downloading flash games for offline play, learning about routers, and so much more. 
  </p>
  <p>
    On top of my technology pursuits, I also sought to establish myself in the business space. I spent a lot of time with my father growing up, watching him embark on his entrepreneurial endeavors. He would go to Manhattan with me to buy perfumes that he would sell in Nigeria. In addition, I used to be with him when he was negotiating the price of run down used cars to ship to Nigeria so he could repair and sell there.
  </p>
  <p>
    Unknowingly, I started to follow suit in my own way. When it snowed outside, I was first on the block to start hitting up the homeowners in East Flatbush. This turned into selling candy in high school and hypewear during undergrad. 
  </p>
  <h2>Education</h2>
  <p>
    When I was old enough for middle school, I got accepted to Mark Twain for the Gifted and Talented in NYC for the Math & Computer talent. This led to my acceptance into Brooklyn Technical High School where my major was Electro-Mechanical Engineering. Last but not least, I attended Brooklyn College for a Bachelor's of Science in Computer Science.
  </p>
  <p>
    After establishing myself in the technology space, my first love, as a Software Engineer, I decided to seriously pursue my second interest: business. I enrolled in a MBA program at the Zicklin School of Business. While there, I was blessed to learn about all the aspects of running a business including: Managing People & Organizations, Corporate Finance, Strategic Business Communication, Investment Analysis, Marketing, Strategy & Competitive Advantage, and so much more...
  </p>
  <h2>What Now?</h2>
  <p>
    I'm currently leveraging my education and over 6 years of experience working in the technology industry to build efficient and scaleable software that solves big problems. The key competencies that help me achieve this include: creative problem solving, clear written & verbal communication skills, and my bias towards action.
  </p>
  <p>
    One of the volunteer activities I like to engage in is career coaching. Growing up, I didn't know anything about the role of "Software Engineer". I got to the place I'm at through advice and mentorship from several people I've met in route. I started giving advice by writing <a href="https://chumomega.medium.com/list/recruiting-season-set-yourself-up-for-success-8d48c618701e"  target="_blank">blog posts on the tech career questions I received most.</a> For readers who have more questions, I've also opened up my schedule for 1 on 1 coaching.
  </p>
  <a href="https://calendly.com/chumomega/free-consult" target="_blank" class="cta-button">Schedule 1v1 Coaching</a>
</section>
<br/>
<section id="logos">
  <h2>I've Worked With</h2>
  <div class="logo-grid">
    <div class="logo-item"><img src="{{ site.baseurl }}/assets/Bloomberg_logo.svg" alt="Bloomberg Logo"></div>
    <div class="logo-item"><img src="{{ site.baseurl }}/assets/amazon_ads.jpg" alt="Amazon Ads Logo"></div>
    <div class="logo-item"><img src="{{ site.baseurl }}/assets/Etsy_logo.png" alt="Etsy Logo"></div>
    <div class="logo-item"><img src="{{ site.baseurl }}/assets/cuny_tech_prep_logo.png" alt="CUNY Tech Prep Logo"></div>
    <div class="logo-item"><img src="{{ site.baseurl }}/assets/justworks_logo.png" alt="Justworks Logo"></div>
    <div class="logo-item"><img src="{{ site.baseurl }}/assets/Mastercard-logo.svg" alt="Mastercard Logo"></div>
    <div class="logo-item"><img src="{{ site.baseurl }}/assets/nyc_cchr_logo.jpg" alt="NYC Commission on Human Rights Logo"></div>
    <div class="logo-item"><img src="{{ site.baseurl }}/assets/JobDiva-Logo.png" alt="JobDiva Logo"></div>
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

  .logo-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
    gap: 20px;
    justify-items: center;
    align-items: center;
    padding: 20px;
  }

  .logo-item img {
    max-height: 100px; /* Limit logo height */
    width: auto; /* Ensure proportional scaling */
  }
</style>

<script>
  document.addEventListener("DOMContentLoaded", function() {
        addAnchorsToHeaders();
  });
</script>
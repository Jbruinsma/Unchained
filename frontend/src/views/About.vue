<template>
  <div class="about-page">
    <nav class="navbar">
      <div class="container nav-content">
        <router-link to="/" class="nav-link">Home</router-link>
        <router-link to="/about" class="nav-link">About</router-link>
        <router-link to="/login" class="nav-link">Login</router-link>
      </div>
    </nav>

    <div class="container content">
      <h1 class="logo">About</h1>

      <section class="about-section">
        <h2>Who I Am</h2>
        <p>
          Hi, I'm Justin Bruinsma. Here's some default text about my background, my journey into software,
          my passion for both music and technology, and what motivates me to build projects like Unchained.
        </p>
      </section>

      <section class="about-section">
        <h2>About This Project</h2>
        <p>
          Unchained is designed to give listeners back complete ownership over their music.
          No algorithms, no data mining, just you and your MP3 collection — organized and played
          exactly how you want. This section could go into your technical philosophy, your love
          for clean architectures, or how it evolved from your original TuneTrack.
        </p>
      </section>

      <section class="about-section contact">
        <h2>Contact Me</h2>
        <p>
          Interested in talking more? Have ideas, or just want to connect? Here’s some placeholder
          contact info. This could eventually be a form or a full section with social links.
        </p>
        <a href="mailto:youremail@example.com" class="btn primary">Email Me</a>
      </section>
    </div>

    <footer>
      <div class="container">
        <p>Created by Justin Bruinsma — Crafted with purpose, structure, and a love for music.</p>
      </div>
    </footer>
  </div>
</template>

<script setup>
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&family=Libertinus+Math&display=swap');
*{box-sizing:border-box;}
body,html{font-family:'Roboto',sans-serif;}
.about-page{background:#1e1e1e;color:#f0f0f0;min-height:100vh;}
.navbar{background:#000;padding:1rem 0;}
.nav-content{align-items:center;display:flex;gap:2rem;justify-content:center;}
.nav-link{color:#fff;font-weight:500;text-decoration:none;transition:color 0.3s;}
.nav-link:hover{color:#ccc;}
.container.content{margin:auto;max-width:800px;padding:4rem 1rem;text-align:left;}
.logo{font-family:'Libertinus Math',serif;font-size:3rem;margin-bottom:1rem;text-align:center;}
.intro{color:#ccc;font-size:1.2rem;margin:0 auto 3rem;max-width:600px;text-align:center;}
.about-section{margin-bottom:3rem;}
.about-section h2{border-bottom:2px solid rgba(255,255,255,0.2);font-size:2rem;margin-bottom:1rem;padding-bottom:0.5rem;}
.about-section p{color:#ddd;font-size:1.05rem;line-height:1.6;}
.about-section.contact{text-align:center;}
.btn{background:#fff;border-radius:5px;color:#000;display:inline-block;font-weight:500;margin-top:1.5rem;padding:0.8rem 1.8rem;text-decoration:none;transition:all 0.3s;}
.btn:hover{background:#ccc;}
footer{background:#000;color:#888;padding:2rem 1rem;text-align:center;}
</style>

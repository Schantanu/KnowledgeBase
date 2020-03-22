<template>
  <section class="section is-small">
    <section class="hero is-small is-light">
      <div class="hero-body">
        <div class="container">
          <nav class="level">
            <div class="level-item has-text-centered">
              <img src="~/static/images/banner.png" width="600" />
            </div>
          </nav>
        </div>
      </div>
    </section>

    <br />

    <div class="container">
      <div class="columns is-multiline">
        <section class="hero is-small is-white">
          <div class="hero-body">
            <!-- <div class="container"> -->

            <h1 class="title is-5">What is the Knowledge Base?</h1>
            <p>
              The Knowledge Base is an information hub for your company and a repository to host Documentation and Projects using R, Python or SQL, and Automation Tools.
              Documents are in the markup format, which you can convert easily into interactive HTML pages, PDFs or just plain Word document.
            </p>

            <br />

            <h2 class="title is-5">Why the Knowledge Base?</h2>
            <div class="columns">
              <div class="column">
                <p class="title is-6">Open Source</p>
                <p>Make code Open Source, to enable access for everyone to your research, enable collaboration and easy code portability</p>
              </div>
              <div class="column">
                <p class="title is-6">Literate Programming</p>
                <p>Enable interleaving code with text, images or whatever best explains the free flowing thought process behind your project or code</p>
              </div>
              <div class="column">
                <p class="title is-6">Reproducible Research</p>
                <p>Enable peers to verify results of your research independently and strengthen your thesis</p>
              </div>
            </div>

            <div class="columns">
              <div class="column">
                <p class="title is-6">Python and R projects</p>
                <p>Run your Python and R projects using the dedicated Web Server and using RMarkdown</p>
              </div>
              <div class="column">
                <p class="title is-6">Everyone Can Code</p>
                <p>Learn programming and solve data problems in a creative manner regardless of your job level</p>
              </div>
              <div class="column">
                <p class="title is-6">ELI5</p>
                <p>Explain Like I'm 5, an approach to quickly educate on concepts one is unfamiliar with</p>
              </div>
            </div>

            <div class="columns">
              <div class="column">
                <p class="title is-6">Web Apps</p>
                <p>Host Web Apps to serve your Users with Reports or give them an ability to interact with the Data</p>
              </div>
              <div class="column">
                <p class="title is-6">Technologies</p>
                <p>Vue, Nuxt, Django, RMarkdown, Gitlab, Docker, Azure</p>
              </div>
              <div class="column">
                <!-- <p class="title is-6">Technologies</p>
                <p>Vue, Nuxt, Django, RMarkdown, Gitlab, Docker, Azure</p>-->
              </div>
            </div>
            <!-- </div> -->
          </div>
        </section>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: "About",
  head() {
    return {
      title: "About"
    };
  }
};
</script>


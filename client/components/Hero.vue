<template>
  <div id= "hero">

    <section class="hero is-info is-medium">
      <div class="hero-body">
        <div class="container">

          <nav class="level">
            <div class="level-item has-text-centered">
              <div class="greet">
                <div class="title is-5">Knowledge Base</div>
                <p>The Information Hub</p>
              </div>
            </div>
          </nav>

          <form class="has-text-centered" v-on:submit.prevent="alertMsg()">
            <input id="search" class="input has-text-centered" type="text" autocomplete="off" placeholder="What are you looking for?">
          </form>

        </div>
      </div>
    </section>

  </div>
</template>

<script>
  export default {
    name: 'Hero',
    methods: {
      alertMsg () {
        alert('Search feature coming soon!')
      }
    }
  }
</script>

<style lang="scss" scoped>
.input {
  width: 400px;
  box-sizing: border-box;
  height: 35px;
  font-size: 14px;
}

.placeholder{
  font-size: 20px;
}

.hero {
  background-color: $primary;
  margin-top: 52px;
}
</style>

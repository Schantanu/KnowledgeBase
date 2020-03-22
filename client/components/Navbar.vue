<template>
  <nav class="navbar is-fixed-top is-dark">
    <div class="container">
      <div class="navbar-brand">

        <nuxt-link class="navbar-item" to="/">
          Knowledge Base
        </nuxt-link>

        <div class="navbar-burger burger" @click="toggleMenu" :class="{'is-active': showNav}" data-target="mainNav">
          <span></span>
          <span></span>
          <span></span>
        </div>

      </div>

      <div id="mainNav" class="navbar-menu" :class="{'is-active': showNav}">
        <div class="navbar-end">
          <nuxt-link class="navbar-item" to="/">Home</nuxt-link>

          <div class="navbar-item has-dropdown is-hoverable">
            <a class="navbar-link">
              Navigation
            </a>

            <div class="navbar-dropdown">
              <nuxt-link class="navbar-item" to="/School">
                School
              </nuxt-link>
              <nuxt-link class="navbar-item" to="/Documentation">
                Documentation
              </nuxt-link>
              <nuxt-link class="navbar-item" to="/Apps">
                Apps
              </nuxt-link>
            </div>
          </div>

          <nuxt-link class="navbar-item" to="/About">About</nuxt-link>

        </div>
      </div>

    </div>
  </nav>
</template>

<script>
  export default {
    name: 'navbar',
    data () {
      return {
        showNav: false
      }
    },
    methods: {
      toggleMenu: function () {
        this.showNav = !this.showNav
      }
    }
  }
</script>

<style>

.navbar {
    max-height: 30px;
    display: inline-block;
    vertical-align: middle;
  /* padding-top: 0px; */
  /* padding-bottom: 40px; 
  /* margin-bottom: 50px;
      background-color: $gray1; */
}

.navbar-brand {
  font-size: 17px;
}

/* .is-transparent {
  background-color: transparent;
  background-image: none;
} */

</style>

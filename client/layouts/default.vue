<template>
  <div class="app">
    <Navbar/>

    <div class="appbody">
      <Nuxt/>
    </div>
  </div>
</template>

<script>
import Navbar from '@/components/Navbar'

export default {
  components:{
    Navbar
  },
}
</script>

<style lang="scss">
.appbody {
  margin-top: 52px;
  background-color: $gray2;
}

html {
  background-color: $gray2;
}
</style>


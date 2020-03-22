<template>
  <div id="navigation" class="container">
    <br />

    <nav class="breadcrumb" aria-label="breadcrumbs">
      <ul>
        <li>
          <router-link tag="a" to="/">Home</router-link>
        </li>
        <li class="is-active">
          <a href="#" aria-current="page">{{ $route.params.project }}</a>
        </li>
      </ul>
    </nav>

    <div class="columns is-multiline">
      <!-- <card v-for="card in appCards" :card="card" :key="card.id" v-show="card.project == $route.params.project && card.source != ''"/> -->
      <card
        v-for="card in appCards"
        :card="card"
        :key="card.id"
        v-show="card.project == 'Apps' && card.source != ''"
      />
    </div>
  </div>
</template>

<script>
import Card from "@/components/Card";
import Frame from "@/components/Frame";

export default {
  name: "Navigation",
  head() {
    return {
      title: "Knowledge Base"
    };
  },
  components: {
    Card,
    Frame
  },
  // computed: {
  //   cards () {
  //     return this.$store.state.cards
  //   }
  // },
  data() {
    return {
      appCards: []
    };
  },
  async asyncData({ $axios, params }) {
    try {
      let appCards = await $axios.$get(`/navcards/`);
      return { appCards };
    } catch (e) {
      return { appCards: [] };
    }
  }
};
</script>

<style>
#navigation {
  padding-bottom: 10px;
}
</style>

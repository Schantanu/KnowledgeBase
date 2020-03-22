<template>
  <section id="navigation" class="section is-small">
    <div class="container">
      <nav class="breadcrumb" aria-label="breadcrumbs">
        <ul>
          <li>
            <nuxt-link tag="a" to="/">Home</nuxt-link>
          </li>
          <li class="is-active">
            <a href="#" aria-current="page">{{ $route.params.project }}</a>
          </li>
        </ul>
      </nav>

      <div class="columns is-multiline">
        <card
          v-for="card in cards"
          :card="card"
          :key="card.id"
          v-show="card.project == $route.params.project && card.source != ''"
        />
      </div>
    </div>
  </section>
</template>

<script>
import { mapState } from "vuex";
import Card from "~/components/Card.vue";

export default {
  name: "Navigation",
  head() {
    return {
      title: this.$route.params.project
    };
  },
  components: {
    Card
  },
  computed: {
    ...mapState({
      cards: state => state.cards
    }),
    uniqueCards: function() {
      return uniqBy(this.cards, function(r) {
        return r.project;
      });
    }
  },
  mounted() {
    this.$store.dispatch("loadCards");
  }
};
</script>

<style lang="scss">
// .breadcrumb {
//   background-color: #fff;
//   padding: 10px;
//   border-style: solid;
//   border-color: $gray4;
//   border-width: 1px;
// }
</style>

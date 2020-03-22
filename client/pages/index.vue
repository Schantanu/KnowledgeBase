<template>
  <div id="Home">
    <Hero />
    <section class="section is-small">
      <div class="container">
        <div class="columns is-multiline">
          <card v-for="card in uniqueCards" :card="card" :key="card.id" />
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import { mapState } from "vuex";
import uniqBy from "lodash/uniqBy";
import Hero from "~/components/Hero.vue";
import Card from "~/components/Card.vue";

export default {
  name: "Navigation",
  head() {
    return {
      title: "Knowledge Base"
    };
  },
  components: {
    Card,
    Hero
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

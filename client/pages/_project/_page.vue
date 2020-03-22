<template>
  <div id="rmarkdown">

    <div class="container" v-if="errored">
      <br>
      <h5 class="title is-6">Document not available.</h5>
    </div>

    <div v-else>
      <div class="container" v-if="loading">
        <br>
        <h5 class="title is-6">Loading Document...</h5>
      </div>
      <div v-else>
        <iframe
        id="myIframe"
        :src= "iframeString + filteredCard.source"
        frameborder="0"
        v-on:load="load()"
        v-show="iframe.loaded"
        style="overflow:hidden; overflow-x:hidden; overflow-y:hidden;
                height:92%; width:100%; position:absolute; top:50px;
                left:0px; right:0px; bottom:0px"
        height="100%"
        width="100%"/>
      </div>
    </div>

  </div>
</template>

<script>
import axios from 'axios'
import Card from "~/components/Card.vue";
import WQMT from "~/pages/apps/WQMT/index.vue";

export default {
  name: 'Frame',
    head() {
    return {
      title: this.$route.params.page
    };
  },
  components: {
    Card, WQMT
  },
  data () {
    return {
      appCards: [],
      iframeString: '/ROutput/',
      iframe: { loaded: false },
      info: null,
      loading: true,
      errored: false
    }
  },
  async asyncData({ $axios, params }) {
    try {
      let appCards = await $axios.$get('/appcards/');
      return { appCards }
    } catch (e) {
      return { appCards: [] };
    }
  },
  mounted () {
    // Listen to message from iframe element
    window.addEventListener('message', function (msg) {
      var message = msg.data
      if (typeof message !== 'string') return
      if (message.startsWith('locHash:')) {
        var locationHash = message.substring(message.indexOf('#'))
        var newurl = window.location.protocol + '//' + window.location.host + window.location.pathname + locationHash
        window.history.pushState({ path: newurl }, '', newurl)
      }
    })
    axios
      .get(this.iframeString + this.filteredCard.source)
      .then(response => {
        this.info = response.data
      })
      .catch(error => {
        console.log(error)
        this.errored = true
      })
      .finally(loading => { this.loading = false })
  },
  computed: {
    filteredCard: function () {
      return this.appCards.find(card => {
          return card.page === this.$route.params.page
    })
    }
  },
  methods: {
    load: function () {
      this.iframe.loaded = true
      var hash = window.location.hash
      if (hash) {
        document.getElementById('myIframe').contentWindow.postMessage('parentHash:${hash}', '*')
        console.log(hash)
      }
    }
  }
}
</script>

<style>
html {
  overflow: hidden;
}

body {
  overflow: hidden;
  margin: 0px;
  padding: 0px;
}
</style>


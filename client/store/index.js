
export const state = () => ({
  cards: []
})

export const actions = {
  async loadCards ({ commit }) {
    const cards = await this.$axios.$get('/appcards/')
    commit('SET_CARDS', cards)
  }
}

export const mutations = {
  SET_CARDS (state, cards) {
    state.cards = cards
  }
}
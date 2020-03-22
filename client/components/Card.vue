
<template>

  <div class="column is-desktop is-3">
    <div class="card card-equal-height">
      <nuxt-link class="linkSpanner" :to="card.page" append/>
      <div class="card-content">
        <div class="card-title">{{ card.title }}</div>
        <div class="content">
          <p>{{ card.description }}</p>
        </div>
      </div>
    </div>
  </div>

</template>

<script>
export default {
    props: [ "card" ]
};
</script>

<style lang="scss">
.card {
  padding: 10px;
  background-color: #fff;
  border-radius: 5px;
  border-style: solid;
  border-color: lightgrey;
  border-width: 0.5px;
  word-wrap: break-word;
}

.card-title {
  font-weight: 700;
  margin-bottom: 10px !important;
}

.card-equal-height {
  display: flex;
  flex-direction: column;
  height: 100%;
}

.card-equal-height .card-footer {
  margin-top: auto;
}

.card:hover {
  border-style: solid;
  border-color: #363636;
  border-width: 0.5px;
}

.card-content {
  padding: 10px;
}

.linkSpanner {
  position: absolute;
  width: 100%;
  height: 100%;
  top: 0;
  left: 0;
  z-index: 1;
}
</style>

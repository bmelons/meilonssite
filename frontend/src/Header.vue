<template>
  <div class="box content header">
    <h1 class="site-name">Wecome my website</h1>
    <div class="hlist">
      <button v-for="txt in buttons" v-bind:id="txt" @click="clickHandle">{{ txt }}</button>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      buttons: ['Home', 'Commissions', 'Characters', 'Socials'],
    }
  },
  methods: {
    clickHandle(a) {
      console.log(a.target.id)
    },
  },
}
</script>

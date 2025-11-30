<template>
  <div class="box content header">
    <h1 class="site-name">gaykitty.online</h1>
    <div class="hlist">
      <button v-for="txt in buttons" v-bind:id="txt" @click="clickHandle">{{ txt }}</button>
    </div>
  </div>
</template>

<script lang="ts">
export default {
  data() {
    return {
      buttons: ['Home', 'Commissions', 'Characters', 'Socials'],
    }
  },
  methods: {
    clickHandle(a:any) {
      this.$emit("clickedEvent",a.target.id);
    },
  },
}
</script>

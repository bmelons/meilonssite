<template>
  <div class="box content header">
    <h1 class="site-name">gaykitty.<span style="color:plum">online</span></h1>
    <h2 class="subtitle">home of the homo</h2>
    <div id="buttonbox" class="hlist">
      <button v-for="txt in buttons" v-bind:id="txt" @click="clickHandle">{{ txt }}</button>
    </div>
  </div>
</template>

<script lang="ts">
import { computed } from "vue";
const isMobile = computed(() => {
  return screen.width <= 760;
});

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

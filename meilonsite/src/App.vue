<template>
  <h1>what the FUCK is up kyle</h1>
  <particles class="particles"></particles>
  
</template>

<script>
import Particles from "./Particles.vue";
export default {
  components: {
    Particles
  }
}
</script>

<style>
* {
  z-index: 1;
}
.particles {
  z-index: -1;
}
</style>
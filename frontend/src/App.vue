<template>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link
    href="https://fonts.googleapis.com/css2?family=Comic+Relief:wght@400;700&family=Yusei+Magic&display=swap"
    rel="stylesheet"
  />
  <link href="./style.css" rel="stylesheet" />
  <div class="content">
    <Header></Header>
    <Landing></Landing>
  </div>
  <particles class="particles"></particles>
</template>

<script>
import Header from './Header.vue'
import Particles from './Particles.vue'
import Landing from './pages/Landing.vue'
import './style.css'

export default {
  components: {
    Particles,
    Landing,
    Header,
  },
}
</script>

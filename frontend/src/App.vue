<template>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin="anonymous" />
  <link
    href="https://fonts.googleapis.com/css2?family=Comic+Relief:wght@400;700&family=Yusei+Magic&display=swap"
    rel="stylesheet"
  />
  <link href="./style.css" rel="stylesheet" />
  <div class="content">
    <Header :activePage="currentPage" @clickedEvent="changePage"></Header>
    <transition-group>
      <Landing v-if="currentPage === 'Home'"></Landing>
      <Commissions v-if="currentPage === 'Commissions'"></Commissions>
      <Characters v-if="currentPage === 'Characters'"></Characters>
    </transition-group>
  </div>
  <particles class="particles"></particles>
</template>

<script lang="ts">
import Header from './Header.vue'
import Particles from './Particles.vue'
import Characters from './pages/Characters.vue'
import Commissions from './pages/Commissions.vue'
import Landing from './pages/Landing.vue'
import './style.css'

export default {
  data() {
    return {
      currentPage: 'Home',
    }
  },
  methods: {
    changePage(id:string) {
      this.currentPage = id
      console.log(id)
    },
  },
  components: {
    Particles,
    Landing,
    Header,
    Characters,
    Commissions
  },
}
</script>

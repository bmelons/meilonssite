<template>
  <div class="box content">
    <h2>Find me here!</h2>
    <a href="https://x.com/boiledmelons"><img class="icon" src = "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Logo_of_Twitter.svg/512px-Logo_of_Twitter.svg.png?20220821125553"> @boiledmelons </a>
    <a href="https://bsky.app/profile/boiledmelons.bsky.social"><img class="icon" src = "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7a/Bluesky_Logo.svg/600px-Bluesky_Logo.svg.png"> @boiledmelons.bsky.social </a>

    
  </div>

  <div @click="isModalVisible=true" class="redBox content clickable"> 
    <h2 >Display Mature Content</h2>
  </div>

  <div class="box content " v-if="isMatureVisible">
    <h2>Find my mature content</h2>
    <a href="https://x.com/grindingmelons"><img class="icon" src = "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Logo_of_Twitter.svg/512px-Logo_of_Twitter.svg.png?20220821125553"> @grindingmelons </a>
    <a href="https://bsky.app/profile/grindingmelons.bsky.social"><img class="icon" src = "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7a/Bluesky_Logo.svg/600px-Bluesky_Logo.svg.png"> @grindingmelons.bsky.social </a>
    <a href="https://www.furaffinity.net/user/psuedocerife"><img class="icon" src = "https://www.furaffinity.net/themes/beta/img/banners/fa_logo.webp?v2"> ~psuedocerife </a>
  </div>
<maturity-modal :isVisible="isModalVisible" @ageConfirmed="onAgeConfirmed"></maturity-modal>
</template>

<style>
.clickable {
    cursor: pointer;
}
a {
    text-decoration: none;
    cursor: pointer;
    font-size: 16pt;
    background: var(--primary-bg-gradient);
    border: none;
    border-radius: 10px;
    padding: 0.5em 1em 0.5em 1em;
    line-height: 1em;
    margin: 0.5em;
    transition: 0.1s ease-out;
    box-shadow:
      0 0 3px #e9e0ea6d,
      0px 5px 10px #191518;
  }
a:visited a:active {
    text-decoration: none;
    cursor: pointer;
    font-size: 16pt;
    background: var(--primary-bg-gradient);
    border: none;
    border-radius: 10px;
    padding: 0.5em 1em 0.5em 1em;
    line-height: 1em;
    margin: 0.5em;
    transition: 0.1s ease-out;
    box-shadow:
      0 0 3px #e9e0ea6d,
      0px 5px 10px #191518;
  }

  a:hover{
    font-size: 18pt;
    transition: 0.1s ease-out;
    box-shadow:
      0 0 2px #e9e0ea6d,
      0px 5px 15px #191518,
      0 -5px 10px #e89dd44f;
  }

.icon {
    height: 16pt;
    width: 16pt;
}


</style>

<script lang="ts">
import MaturityModal from './MaturityModal.vue';

export default {
    components: {
    MaturityModal
  },
  data() {
    return {
    isMatureVisible: false,
      isModalVisible: false,
    }
  },
  methods: {
    onAgeConfirmed(isMature:boolean) {
        this.isModalVisible = false;
        if (isMature) {
            this.showMature()
        }
    },
    showMature(){
        this.isMatureVisible = true;
    },
  },
}

</script>
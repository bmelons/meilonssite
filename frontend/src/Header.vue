<template>
  <div class="box content header">
    <h1 class="site-name">gaykitty<b>.online</b></h1>
    <h2 class="subtitle">home of the homo</h2>
    <div id="buttonbox" class="hlist">
      <button v-bind:class="getClass(txt)" v-for="txt in buttons" v-bind:id="txt" @click="clickHandle">{{ txt }}</button>
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
  props: {
    activePage:{
      type:String,
      required:true
    }
  },
  methods: {
    clickHandle(a:any) {
      console.log(screen.width);
      this.$emit("clickedEvent",a.target.id);
    },
    getClass(a:string) {
      if (a == this.activePage) {
        return "active"
      }
      return ""
    }
  },
}
</script>

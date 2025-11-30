<template>
  <div class="box content">
    <h2>Commission Price Calculator</h2>
    <div class="hori">
      <div class="option" v-for="(price, v) in tiers">
        <input v-model="currentTier" type="radio" :value="v">
        <h2><b>{{ v }}</b>: {{ price }}</h2>
        </input>
      </div>
    </div>
    <div class = "box vflex">
      <h2> Additional Characters</h2>
      <p class="bignumber">{{ additionalCharacters }}</p>
      <input class="charSelector" type="range" min=0 max="5" v-model="additionalCharacters"></input>
    </div>
  </div>
  <div class="spacer"></div>
  <div class="box totalprice">
    <b>Total</b>: {{ calculate() }}
  </div>

  
  
</template>

<script>

export default {
  data() {
    return {
      currentTotal: 0,
      additionalCharacters: 0,
      currentTier: "Colored",
      tiers: {
        Shaded: 20,
        Colored: 16,
        Sketch: 10
      },
      tierAdditions: {
        Shaded: 5,
        Colored: 4,
        Sketch: 3
      }
    }
  },
  methods: {
    calculate() {
      return this.tiers[this.currentTier] + this.additionalCharacters * this.tierAdditions[this.currentTier]  ;
    }
  }
}

</script>

<style>
.option {
  display: flex;
  flex-direction: column;
  justify-content: center;
  padding: 1em;
}

.hori {
  display: flex;
  flex-direction: row;
}

.totalprice {
  position: fixed;
  bottom: 1em;
  right: 1em;
  padding: 1em;
  font-size: 30pt;
}

.bignumber {
  font-size: 80pt;
  padding: 0;
  margin: 0;
}
.charSelector {

}
.spacer {
  margin: 80pt;
}




</style>

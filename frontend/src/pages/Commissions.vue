<template>
  <div class="box content">
    <h2>Commission Price Calculator</h2>
    <div class="hori">
      <div class="option" v-for="(price, tierName) in tiers" :key="tierName">
        <label>
          <input v-model="currentTier" type="radio" :value="tierName">
          <h2><b>{{ tierName }}</b>: ${{ price }}</h2>
        </label>
      </div>
    </div>
    <div class = "box vflex">
      <h2> Additional Characters</h2>
      <p class="bignumber">{{ additionalCharacters }}</p>
      <input class="charSelector" type="range" min=0 max="5" v-model.number="additionalCharacters">
    </div>
    <div class = "box vflex">
      <h2> Additional Panels</h2>
      <p class="bignumber">{{ additionalPages }}</p>
      <input class="charSelector" type="range" min=0 max="10" v-model.number="additionalPages">
    </div>
  </div>
  <div class="spacer"></div>
  <div class="box totalprice">
      <p style="font-size: 15pt;"> 
          <b>Tier ({{ currentTier }})</b>: ${{ tiers[currentTier] }}<br/>
          <b>Additional Characters</b>: ${{ additionalCharacters * (tierAdditions[currentTier] ?? 0)  }}<br/>
          <b>Additional Pages</b>: ${{ additionalPagesCost }} 
        </p>
    <hr/>
    <b>Total</b>: ${{ totalPrice }}
  </div>
</template>

<script lang="ts">
interface sn {
    [key:string]: number;
}

type Tier = "Shaded" | "Colored" | "Sketch";

export default {
  data() {
    return {
      additionalCharacters: 0,
      additionalPages: 0,
      currentTier: "Colored" as Tier,
      tiers: {
        "Shaded": 20,
        "Colored": 16,
        "Sketch": 10
      } as sn,
      tierAdditions: {
        "Shaded": 5,
        "Colored": 4,
        "Sketch": 3
      } as sn
    }
  },
  computed: {
    baseAndCharCost(): number {
      const basePrice = this.tiers[this.currentTier];
      const adadad = this.tierAdditions[this.currentTier];
      if (adadad === undefined || basePrice === undefined) {
        return 1;
      }
      const charPrice = this.additionalCharacters * adadad;
      
      return basePrice + charPrice;
    },
    additionalPagesCost(): number {
        // The logic here seems to be (base + chars - 5) * pages.
        // Keeping the original calculation logic.
        const costPerPage = this.baseAndCharCost - 5;
        // A page shouldn't have a negative cost.
        const effectiveCostPerPage = Math.max(0, costPerPage);
        return effectiveCostPerPage * this.additionalPages;
    },
    totalPrice(): number {
      return this.baseAndCharCost + this.additionalPagesCost;
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

.option label {
  cursor: pointer;
  justify-content: center;
  padding: 1em;
}

.hori {
  display: flex;
  flex-direction: row;
}

.totalprice {
  position: fixed;
  bottom: .5em;
  right: .5em;
  padding: .5em;
  font-size: 20pt;
}

.bignumber {
  font-size: 80pt;
  padding: 0;
  margin: 0;
}
.charSelector {

}
.spacer {
  margin: 100pt;
}

</style>

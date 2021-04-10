<template>
  <div id="dashboard">
    <h1>That's the dashboard!</h1>
    <p>You should only get here if you're authenticated!</p>
    <p v-if="email">Your email address: {{ email }}</p>
    <p>your body battery is: {{bodybatt}}</p>
    <div>
      <PlanetChart />
    </div>
  </div>
</template>

<script>
import axios from "axios";
import PlanetChart from '../charts/PlanetChart.vue'
export default {
  components: {
    PlanetChart
  },
  data() {
    return {
      bodybatt: 0
    }  
  },
  computed: {
    email() {
      return !this.$store.getters.user ? false : this.$store.getters.user.email;
    },
  },
  created() {
    this.$store.dispatch("fetchUser"); 
  },

  mounted() {
    this.setChartHealthTrend()
  },

  methods: {
    setChartHealthTrend(){
    const ahr = this.$store.getters["getAllHealthEntries"];
    console.log("[setChartHealthTrend, body battery value]: " + ahr[0].bodybatt)
    this.bodybatt= ahr[0].bodybatt
    //this.renderChart(this.chartdata, this.options)
    }
  }
};
</script>

<style scoped>
h1,
p {
  text-align: center;
}

p {
  color: red;
}
</style>

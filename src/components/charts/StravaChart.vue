<template>
  <div>
    <canvas id="strava-chart"></canvas>
  </div>
</template>

<script>
import Chart from 'chart.js'
import StravaChartData from './strava-data'

export default {
  name: 'StravaChart',
  data() {
    return {
      stravaChartData: StravaChartData
    }
  },
  mounted() {
    const graphData= this.$store.getters["getGraphData"]
    console.log("[BodyBattChart] :" + graphData)
    //console.log("[BodyBattChart] :" + this.bodyBattChartData.data.datasets[0])

    this.stravaChartData.data.labels=graphData[0]
    this.stravaChartData.data.datasets[0].data=graphData[1]
    this.stravaChartData.data.datasets[1].data=graphData[2]
    this.stravaChartData.data.datasets[2].data=graphData[3]

    const ctx = document.getElementById('strava-chart');
    new Chart(ctx, this.stravaChartData);
  }
}
</script>
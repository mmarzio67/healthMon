const ahr = this.$store.getters["getAllHealthEntries"];

export const bodyBattData = {
  type: "line",
  data: {
    labels: ahr.date,
    datasets: [
      {
        label: "Body Battery Up",
        data: [0, 0, 1, 2, 79, 82, 27, 14],
        backgroundColor: "rgba(54,73,93,.5)",
        borderColor: "#36495d",
        borderWidth: 3
      },
      {
        label: "Body Battery Down",
        data: [0.166, 2.081, 3.003, 0.323, 954.792, 285.886, 43.662, 51.514],
        backgroundColor: "rgba(71, 183,132,.5)",
        borderColor: "#47b784",
        borderWidth: 3
      }
    ]
  },
  options: {
    responsive: true,
    lineTension: 1,
    scales: {
      yAxes: [
        {
          ticks: {
            beginAtZero: true,
            padding: 25
          }
        }
      ]
    }
  }
};

export default bobyBattData;
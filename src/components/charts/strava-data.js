export const stravaData = {
  type: "line",
  data: {
    // injected in realtime
    labels: [],
    datasets: [
      {
        label: "runned distance",
        data: [],
        backgroundColor: "rgba(54,73,93,.5)",
        borderColor: "#36495d",
        borderWidth: 5
      },
      {
        label: "walked distance",
        data: [],
        backgroundColor: "rgba(71, 183,132,.5)",
        borderColor: "#47b784",
        borderWidth: 5
      },
      {
        label: "Cycled distance",
        data: [],
        backgroundColor: "rgba(255, 230, 255,.5)",
        borderColor: "#ff0066",
        borderWidth: 5
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

export default stravaData;
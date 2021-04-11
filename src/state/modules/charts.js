
export default {
    state: {
        healthGraphData: [],
    },
    mutations:{
        SET_HEALTHGRAPHDATA(state, payload) {
            state.healthGraphData = payload;
        },
    },
    actions:{
        prepHealthGraph({commit, rootGetters}) {
            const ahr = rootGetters.getAllHealthEntries;    
            // prepare the data for the chart to display
            const formatResult = [];
            const xLabels = [];
            const y1Values = [];
            const y2Values = [];
            let y1 = null;
            let y2 = null;

            ahr.forEach((row) => {
                xLabels.push(row.registerDate);
                y1 = row.bodybattU;
                y2 = row.bodybattD;
                y1Values.push(y1);
                y2Values.push(y2);
            });

            formatResult.push(xLabels);
            formatResult.push(y1Values);
            formatResult.push(y2Values);

            //console.log("[prepareHealthGraph] xAxis:" + formatResult[0])
            //console.log("[prepareHealthGraph] yAxis:" + formatResult[1])
            commit("SET_HEALTHGRAPHDATA", formatResult);         
        }
    },
    getters:{
        getGraphData: (state) => {
            return state.healthGraphData;
          },
    }
}

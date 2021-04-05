import globalAxios from "axios";
import store from "../../store";
import router from "../../router";

export default {
  state: {},
  mutations: {},
  actions: {
    dailyhealthmon({ commit, state }, dailymonData) {
      const regDate = new Date();

      if (!store.state.auth.idToken) {
        return;
      }
      console.log("[state activity.js]:", store.state.auth.idToken);
      globalAxios
        .post("/dailyhealthmon.json" + "?auth=" + store.state.auth.idToken, {
          weight: dailymonData.weight,
          bfi: dailymonData.bfi,
          imc: dailymonData.imc,
          waist: dailymonData.waist,
          spo2: dailymonData.spo2,
          breathrest: dailymonData.breathrest,
          breathactive: dailymonData.breathactive,
          hourssleep: dailymonData.timeslept,
          pulserest: dailymonData.pulserest,
          pulseactive: dailymonData.pulseactive,
          stress: dailymonData.stress,
          bodybattU: dailymonData.bodybattU,
          bodybattD: dailymonData.bodybattD,
          steps: dailymonData.steps,
          registerDate: regDate,
          userId: store.state.auth.userId,
        })
        .then((res) => {
          console.log(res);
          router.replace("/dashboard");
        })
        .catch((error) => console.log(error));
    },
  },
  getters: {},
};

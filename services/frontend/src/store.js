import Vue from "vue";
import Vuex from "vuex";
import auth from "./state/modules/auth";
import activity from "./state/modules/activity";

Vue.use(Vuex);

const Store = new Vuex.Store({
  modules: {
    auth,
    activity,
  },

  actions: {
    setLogoutTimer({ commit }, expirationTime) {
      setTimeout(() => {
        commit("clearAuthData");
      }, expirationTime * 1000);
    },
  },
});

export default Store;

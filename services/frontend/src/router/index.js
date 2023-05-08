import Vue from "vue";
import VueRouter from "vue-router";

import WelcomePage from "../components/welcome/welcomePage.vue";
import DashboardPage from "../components/dashboard/dashboardPage";
import DailyHealthPage from "../components/activity/dailyHealthMon.vue";
import SignupPage from "../components/auth/signUp.vue";
import SigninPage from "../components/auth/signIn.vue";
import store from "../store";

Vue.use(VueRouter);

const routes = [
  { path: "/", component: WelcomePage },
  { path: "/signup", component: SignupPage },
  { path: "/signin", component: SigninPage },
  {
    path: "/dashboard",
    component: DashboardPage,
    beforeEnter(to, from, next) {
      if (store.state.auth.idToken) {
        next();
      } else {
        next("/signin");
      }
    },
  },
  {
    path: "/dailyhealthmon",
    component: DailyHealthPage,
    beforeEnter(to, from, next) {
      if (store.state.auth.idToken) {
        next();
      } else {
        next("/signin");
      }
    },
  },
];

export default new VueRouter({ mode: "history", routes });

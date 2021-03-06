import Vue from "vue";
import App from "./App.vue";
import axios from "axios";

import router from "./router";
import store from "./store";

axios.defaults.baseURL =
  "https://vuejs-udemy-max-default-rtdb.europe-west1.firebasedatabase.app";
// set the headers authorization manually, demo purpose
// axios.defaults.headers.common["Authorization"] = "yourock";
axios.defaults.headers.get["accepts"] = "application/json";

// create interceptor as a middleway to be able to modify request and response on the fly (inline)
const reqInterceptor = axios.interceptors.request.use((config) => {
  console.log("Request Interceptor:", config);
  return config;
});

const resInterceptor = axios.interceptors.response.use((res) => {
  console.log("Response Interceptor:", res);
  return res;
});

// a way to turn off the interceptors above
axios.interceptors.request.eject(reqInterceptor);
axios.interceptors.response.eject(resInterceptor);

new Vue({
  el: "#app",
  router,
  store,
  render: (h) => h(App),
});

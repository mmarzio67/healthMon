import { createStore } from "vuex";

import sportactivities from './modules/sportactivities';
import users from './modules/users';


export default createStore({
  modules: {
    sportactivities,
    users,
  }
});

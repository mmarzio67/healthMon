import axios from 'axios';

const state = {
  sportactivities: null,
  sportactivity: null
};

const getters = {
  stateSportactivities: state => state.sportactivities,
  stateSportactivity: state => state.sportactivity,
};

const actions = {
  async createSportactivity({dispatch}, sportactivity) {
    await axios.post('sportactivity', sportactivity);
    await dispatch('getSportactivities');
  },
  async getSportactivities({commit}) {
    let {data} = await axios.get('sportactivities');
    commit('setSportactivities', data);
  },
  async viewSportactivity({commit}, id) {
    let {data} = await axios.get(`sportactivity/${id}`);
    commit('setSportactivity', data);
  },
  // eslint-disable-next-line no-empty-pattern
  async updateSportactivity({}, sportactivity) {
    await axios.patch(`sportactivity/${sportactivity.id}`, sportactivity.form);
  },
  // eslint-disable-next-line no-empty-pattern
  async deleteSportactivity({}, id) {
    await axios.delete(`sportactivity/${id}`);
  }
};

const mutations = {
  setSportactivities(state, sportactivities){
    state.sportactivities = sportactivities;
  },
  setSportactivity(state, sportactivity){
    state.sportactivity = sportactivity;
  },
};

export default {
  state,
  getters,
  actions,
  mutations
};

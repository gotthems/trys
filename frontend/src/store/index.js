import Vue from 'vue';
import Vuex from 'vuex';
import {ProfileData} from './module'
Vue.use(Vuex)

const state= {
  username: 'Sabcan',
  message:'Hello',

};

const getters= {

  welcomeMessage(state) {
    return `${state.message} ${state.username}`;
  },

};

const mutations = {

  setUserName(state,name){
    state.username = name;

  }
};

const actions ={
  updateUsername({commit},name){

    commit('setUserName', name);
    console.log(name)
  }

}







const store = new Vuex.Store({


          state,
          getters,
          mutations,
          actions,

  modules:
    {
      ProfileData: ProfileData

    }



})


export default store;
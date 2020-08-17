import JsonFiles from '../jsonFiles/jsonfile'
import Jsondict from '../jsonFiles/data.json'
import jsonfile from "../jsonFiles/jsonfile";

export  const JsonChoiceData = {

  state: {
    user: [],


  },
  getters: {
    user(state) {
      return state.user;
    },


  },


  mutations: {


  // : function
    getsonData (state, userinput) {

      var getJsoncleandata = jsonfile.JsonData(userinput, Jsondict.Gender)


        state.user = getJsoncleandata

        return getJsoncleandata




    }


  },

  actions: {

    inijson(context){

      context.commit('getsonData')

    },


    getJsonData(context,userinput){

      context.commit('getsonData',userinput)

    }


  }

}

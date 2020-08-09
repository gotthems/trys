
import api from '../api/index'

export const ProfileData = {

    state: {

      note:[]

    },
    getters: {
      getNote(state){
        return state.note
      }

  },
    mutations: {
  initnote(state,note){
    state.note = note
  },
      addnote(state,note){

      },
      updatenote(state,note){},
      deletenote(state,note){}


  },
    actions: {

      initApp(context){
        api.fetchNotes('get',null,null).then(res => {
          context.commit('initnote', res.data)
          console.log(res.data)

        })

      },
        addnote(context,note){},
        updatenote(context,note){},
        deletenote(context,note){}
    }
}

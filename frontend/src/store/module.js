import api from '../api/index'

export const ProfileData = {

    state: {

      note:[],
      detailNote:[]


    },
    getters: {
      getNote(state){
        return state.note
      },
      getNoteDetail(state){
        return state.detailNote
      }

  },
    mutations: {
  initnote(state,note){
    state.note = note
  },


      addnote(state,note){
        api.fetchNotes('post', null, note).then(res => {
          console.log('çalıştı')
        }).catch((e)=> {
      console.log(e)
    })
      },
      updatenote(state,notes){

     api.updateNotes('PUT', null, notes,notes.id).then(res => {

    }).catch((e)=> {
      console.log(e)
    })
      },
      deletenote(state,noteId){


     api.deleteNotes('DELETE',null,noteId).then(
        res => {

          api.fetchNotes('get',null,null).then(res => {
              state.note = res.data.reverse()
              console.log("NOTE SİLİNDİ LİSTE GÜNCELLENDİ")

        })
          console.log('deleted')

        },

      ).catch((e)=> {
      console.log(e)
    })

      },
        detailnotes(state,detailnote){
          state.detailNote = detailnote
  },
       detailnote(state,noteId){
        api.detailNotes('post', null, noteId).then(res => {

            console.log('çalıştı')
        }).catch((e)=> {
      console.log(e)

    })
       }


  },
    actions: {

      initApp(context){
        api.fetchNotes('get',null,null).then(res => {
          context.commit('initnote', res.data.reverse())
          console.log(res.data)

        })

      },
      detailnote(context, noteId) {

        context.commit('detailnotes',noteId)
      },
      addnote(context,note){
        context.commit('addnote',note)
        },
        updatenote(context,note){

        context.commit('updatenote', note)

        },
        deletenote(context,noteId){
          context.commit('deletenote', noteId)




        }
    }
}

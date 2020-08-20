import api from '../../api/advertise'

export const AdvertiseStore = {

    state: {

      AdvertiseData:[],
      userOwnerAdvertiseDataList:[]


    },
    getters: {
      getAdvertiseData(state){
        return state.AdvertiseData
      },


    },
    mutations: {

    initAdvertise(state,Data){
    state.AdvertiseData = Data
    },

    initUserOwnerAdvertise(state,Data){
    state.AdvertiseData = Data
    },


    createAdvertiseData(state,Data){
        api.CreateAdvertiseData('post', null, Data).then(res => {
          console.log('Created Advertise Data ')
        }).catch((e)=> {
      console.log(e)
    })
      },

   /* updateAdvertiseData(state,Data){

     api.UpdateAdvertiseData('PUT', null, Data,Data.id).then(res => {

    }).catch((e)=> {
      console.log(e)
    })
    },*/

   /* deleteAdvertiseData(state,DataID){
     api.DeleteAdvertiseData('DELETE',null,DataID).then(
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

    },*/

    userOwnerAdvertiseDataList(state,Data){
          state.userOwnerAdvertiseDataList = Data
    },

   /* userOwnerAdvertiseData(state,noteId){
        api.detailNotes('post', null, noteId).then(res => {

            console.log('çalıştı')
        }).catch((e)=> {
        console.log(e)

        })
    }*/


    },
    actions: {

    initAdvertiseActions(context){
        api.AllAdvertiseData('get',null,null).then(res => {
          context.commit('initAdvertise', res.data.reverse())
          console.log(res.data)

        })

      },



   /* UserOwnerAdvertiseActions(context){
        api.UserOwnedAdvertiseData('get',null,null).then(res => {
          context.commit('initUserOwnerAdvertise', res.data.reverse())
          console.log(res.data)

        })

      },*/

   /* userOwnerAdvertiseDataActions(context, Id) {
        context.commit('detailnotes',Id)
      },*/

    createAdvertiseDataActions(context,data){
        context.commit('createAdvertiseData',data)
      },

   /* updateAdvertiseDataActions(context,data){
        context.commit('updatenote', data)
    },*/

  /*  deleteAdvertiseDataAcitons(context,Id){
          context.commit('deletenote', Id)

        }*/
    }
}

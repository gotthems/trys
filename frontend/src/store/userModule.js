import api from '../api/user'

export const UserData = {

    state: {
      user:[],
      detailUser:[]


    },
    getters: {
      getUser(state){
        return state.user
      },
      getUserDetail(state){
        return state.detailUser
      }

  },
    mutations: {



  inituser(state,user){
    state.user = user
  },

      register(state,userinputdata){
        api.Register('post', null,userinputdata).then(res=>{
            console.log("Register işlemi Çalıştı")
        }).catch((e)=> {
            console.log(e + "Error")
        })

      },

      Login(state,userinputdata){
        api.loginUser('post', null, userinputdata).then(res=>{
            console.log("Login işlemi Çalıştı")
          state.detailNote = res.data
          console.log(res.data)

        })
      },


      Logout(state){


        api.logoutUser('post', null, {}).then(res=>{
            console.log("Logout işlemi Çalıştı" )

          for( var i in res.data){

            console.log(res.data[i])
          }





        })
      },


  },
    actions: {

      initUserData(context){

      api.UserProfileData('get',null,null).then(res => {

        context.commit('inituser',res)
        console.log(res)

        })
      },

      register(context,userinput){
        context.commit('register',userinput)
      },

      Login(context, userinput) {

        context.commit('Login',userinput)

      },

      Logout(context) {
        console.log("Logout Submit Methodu Çalıştı")
        context.commit('Logout')


      },





    }
}

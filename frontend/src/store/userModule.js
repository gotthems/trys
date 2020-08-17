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

      userprofilupdate(state,userinputdata){

    api.UserProfileUpdate('PATCH',null,userinputdata).then(res=>{
      console.log("User Profil Update Çalıştı")

    }).catch((e)=> {
            console.log(e + "Error")
        })
      },

      changepassword(state,userinputdata){
    api.UserChangePassword('post',null,userinputdata).then(
      res=> {
        for(var i in res){
          console.log(res[i]['detail'])
        }

        console.log('Şifre Değiştirme işlmi' )
      }
    )

      },

      Login(state,userinputdata){
        api.loginUser('post', null, userinputdata).then(res=>{
            console.log("Login işlemi Çalıştı")
           console.log(res.data)
          state.detailUser = res.data
          for(var i in state.detailUser){
            console.log(state.detailUser[i])
          }



        })
      },


      Logout(state){
        api.logoutUser('post', null, {}).then(res=>{
            console.log("Logout işlemi Çalıştı" )

          for( var i in res.data){

            console.log(res.data[i])
          }})
      },




    },
    actions: {

      initUserData(context){

      api.UserProfileData('get',null,null).then(res => {

        context.commit('inituser',res)
        console.log(res)

        })
      },

      userprofilupdate(context,userinput){
         context.commit('userprofilupdate',userinput)
      },

      register(context,userinput){
        context.commit('register',userinput)
      },

      changepassword(context,userinput){

        context.commit('changepassword', userinput)
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

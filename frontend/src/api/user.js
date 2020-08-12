import axios from 'axios'


export default {

  Register(method, params, data){
    if(method === 'post') {
      return axmethod('rest-auth/registration/', method, {data})
     console.log("Axios Register user.js")
    }
    else {
      return axmethod('rest-auth/registration/', 'get', {data}).then(
        console.log(data + "xxxxxx")
      )}},

  //Login
  loginUser(method, params, data){
    if(method === 'post') {
      return axmethod('rest-auth/login/', method, {data})
     console.log("Axios Login user.js")
    }},



      UserProfileData(method, params, data){
    if(method === 'get') {
      return axmethod('rest-auth/user/', method, {data})
    }
    else{
        return axmethod('rest-auth/user/', 'post', {})
    }},

   logoutUser(method, params,data){
    if(method === 'post') {
      return axmethod('rest-auth/logout/', method, {data})


    }

    },





}






function axmethod(url, method, options) {
  if (options !== undefined) {
    var {params = {}, data = {}} = options
  } else {
    params = data = {}
  }

  return new Promise((resolve, reject) => {
    axios({
      url,
      method,
      params,
      data
    }).then(res => {
      resolve(res)
    }, res => {
      reject(res)
    })
  })
}



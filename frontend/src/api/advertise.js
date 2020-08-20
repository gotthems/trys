import axios from 'axios'


export default {

  /* Tüm ilan modellerini görüntüleme */
  AllAdvertiseData(method, params, data){
    if(method === 'get') {
      return axmethod('advertise/AllAdvertiseListView/', method, {data})
    }

  },

  // Yanlızca Kullanıcaya ait ilan modellerinin görüntülenmesi
  UserOwnedAdvertiseData(method, params, data){
    if(method === 'post') {
      return axmethod('advertise/', method, {data})
    }
    else{
        return axmethod('advertise/', 'get', {})
    }
  },

  //İlan modeli oluşturma
  CreateAdvertiseData(method, params, data){
    if(method === 'post') {
      console.log("Axios CreateAdvertiseData")
      return axmethod('advertise/CreateAdvertiseView/', method, {data})

    }
    else {
      return axmethod('advertise/CreateAdvertiseView/', 'get', {data}).then(
        console.log(data + "xxxxxx")
      )}},


  //Kullanıcıya ait İlan modelini silme
  DeleteAdvertiseData(method, params, id){
    return axmethod('advertise/'+ id + "/" , method, {})
  },


  //Kullanıcıya ait İlan modelini güncelleme
  UpdateAdvertiseData(method, params, data, id){

      return axmethod('update/'+ id +"/", method, {data})


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



import axios from 'axios'


export default {

  fetchNotes(method, params, data){
    if(method === 'post') {
      return axmethod('apinotes/', method, {data})
    }
    else{
        return axmethod('apinotes/', 'get', {})
    }
  },

  deleteNotes(method, params, id){
    return axmethod('delete/'+ id + "/" , method, {})
  },

  updateNotes(method, params, data, id){

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



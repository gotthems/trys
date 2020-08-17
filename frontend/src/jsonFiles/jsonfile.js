import  jsondict from './data.json'
export default {




   JsonData(RestData,ChoiceJsonDict){
      var jsonlist= []

     ChoiceJsonDict.map(function(val, index) {

            if(val['text'] == RestData){

              console.log(val['value'] + "22222222222222")
              jsonlist.push(val['value'])
              console.log(jsonlist)
                return val['value']
            }

    })
        return jsonlist
  },

}

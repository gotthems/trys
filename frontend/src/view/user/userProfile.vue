<template>
<div>

<div  >
  <v-card><v-card-text>KULLANICI BİLGİLERİ</v-card-text></v-card>
<v-list >

    <v-list-item-title> Kullanıcı Adı </v-list-item-title>
 <v-list-item> <v-list-item-subtitle >  {{userdata['username']}}</v-list-item-subtitle></v-list-item>
 <v-list-item-title> Adı Soyadı</v-list-item-title>
  <v-list-item> <v-list-item-subtitle>  {{userdata['first_name']}} {{userdata['last_name']}}</v-list-item-subtitle></v-list-item>
  <v-list-item-title> E-mail</v-list-item-title>
 <v-list-item> <v-list-item-subtitle > {{userdata['email']}}</v-list-item-subtitle></v-list-item>
  <v-list-item-title> Telefon Numarası</v-list-item-title>
 <v-list-item> <v-list-item-subtitle > {{userdata['phone_number']}}</v-list-item-subtitle></v-list-item>

<v-list-item-title> Cinsiyeti</v-list-item-title>
 <v-list-item> <v-list-item-subtitle > {{this.profileData.gender}}</v-list-item-subtitle></v-list-item>
  <v-list-item-title> Öğrenim Durumu</v-list-item-title>
  <v-list-item><v-list-item-subtitle > {{this.profileData.educational_status}}</v-list-item-subtitle></v-list-item>
<v-list-item-title> Doğum günü</v-list-item-title>
  <v-list-item><v-list-item-subtitle > {{userdata['birthday']}}</v-list-item-subtitle></v-list-item>


</v-list>


</div>




</div>
</template>

<script>





      import Vuetify from "vuetify"
      import {UserData} from "../../store/userModule";
      import {JsonChoiceData} from "../../store/choiceStore";
      import jsonDict from "../../jsonFiles/data.json"
//      import JsonFile from "../../jsonFiles/jsonfile"
      import jsonfile from "../../jsonFiles/jsonfile";


      export default {
        name: "userProfile",

      data(){
          page:''
        return {
          profileData:{
            username:'',
            first_name:'',
            last_name: '',
            email:'',
            phone_number:'',
            birthday:'',
            gender:'',
            educational_status:'',
            martial_status:'',


          },


        }
      },

        methods:{
           onFocus() {
        disabled
    }

        },

      created(){
        this.$store.dispatch('initUserData')
        this.$store.dispatch('inijson')






      },

        computed:{

          gender(){

          for(var i in this.$store.getters.user){

            return this.$store.getters.user[i]
          }
          return this.$store.getters.user

        },



    userdata (){

      for(var i in this.$store.getters.getUser){
        var data = this.$store.getters.getUser[i]

        var getGenderData = jsonfile.JsonData(data['gender'],jsonDict.Gender)
          this.profileData.gender = getGenderData[0]
        var getDataEducational = jsonfile.JsonData(data['educational_status'],jsonDict.educational_status)
        this.profileData.educational_status = getDataEducational[0]


//this.$store.dispatch('getJsonData',data['gender'])
        return data

      }
        return this.$store.getters.getUser

    },





        },





      }
</script>

<style scoped>

</style>

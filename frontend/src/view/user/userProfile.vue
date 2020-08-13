<template>
<div>


<v-list>
  <v-list-item>
  {{userdata['username']}}</v-list-item>
 <v-list-item>  {{userdata['id']}}</v-list-item>
  <v-list-item>  {{userdata['email']}}</v-list-item>
  <v-list-item>  {{userdata['phone_number']}}</v-list-item>
  <v-list-item>  {{userdata['first_name']}} {{userdata['last_name']}}</v-list-item>

      {{userdata['gender']}}
  {{userdata['martial_status']}}
  {{userdata['profession']}}


</v-list>



</div>
</template>

<script>

      import Vuetify from "vuetify"
  import {UserData} from "../../store/userModule";
    export default {
        name: "userProfile",

      data(){

        return {
          datalist:[],
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

          }
        }
      },

      created(){
        this.$store.dispatch('initUserData')

      },

        computed:{

    userdata (){
      for ( var i in this.$store.getters.getUser){
        this.datalist.push(this.$store.getters.getUser[i])
        return this.$store.getters.getUser[i]
      }
      return this.$store.getters.getUser
    },

        },





    }
</script>

<style scoped>

</style>

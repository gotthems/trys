<template>

<div id="app">
  <v-app id="inspire">
    <form @submit.prevent="change">

           <v-text-field
             v-model="formsData.new_password1"
             label="Parola"
          required
          :type="value ? 'password' : 'text'"
             @click:append="() => (value = !value)"
           :append-icon="value ? 'visibility' : 'visibility_off'"

      ></v-text-field>
 <v-text-field
          v-model="formsData.new_password2"
             label="Parolanızı doğrulayınız"
        required
             :append-icon="value ? 'visibility' : 'visibility_off'"
    @click:append="() => (value = !value)"
    :type="value ? 'password' : 'text'"
      ></v-text-field>



      <v-btn class="mr-4" type="submit">Değiştir</v-btn>
  <span v-if="formsData.new_password1 === formsData.new_password2 && formsData.new_password2.length > 0"  style="color: #42b983">Parola eşleşti</span>
  <span v-else style="color: red">Parola eşleşmedi</span>


    </form>
  </v-app>


{{formsData.new_password2}}
{{formsData.new_password1}}

</div>



</template>

<script>
      import api from '../../api/user'
import Vuetify from "vuetify"
import {ProfileData} from "../../store/module";

    export default {
        name: "passwordChange",


      data(){
    return{
      value: String,

      formsData : {
        new_password1:"Sss.12641264",
        new_password2:"Sss.12641264"

      }

    }
  },

      methods:{
           change(){
             this.$store.dispatch('changepassword',this.formsData)

             console.log(this.formsData)
           }
      }




    }
</script>

<style scoped>

</style>

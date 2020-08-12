<template>


<div id="app">
  <v-app id="inspire">
    <form @submit.prevent="LoginSubmit" >
      <v-text-field
        label="Kullanıcı Adı"
        required
        v-model="formData.username"
      ></v-text-field>


           <v-text-field
             v-model="formData.password"
             label="Parola"
          required
          :type="value ? 'password' : 'text'"
             @click:append="() => (value = !value)"
           :append-icon="value ? 'visibility' : 'visibility_off'"

      ></v-text-field>




      <v-btn class="mr-4" type="submit">Giriş yap</v-btn>


    </form>
  </v-app>
</div>

</template>

<script>
    import Vuetify from "vuetify"
  import {UserData} from "../../store/userModule";

  export default {

        name: "login",
          data(){
    return{
        value: String,
      formData : {
        username: '',
        email: '',
      password:'',
      }}},

         methods: {

    LoginSubmit(){

         this.$store.dispatch('Login',this.formData)

          console.log("Login Submit Methodu Çalıştı")
      },

         },

    }
</script>

<style scoped>
  #app{
    width:40%;


    margin:auto;
  }

</style>

<template>

<div id="app">
  <v-app id="inspire">
    <form @submit.prevent="RegisterSubmit">
      <v-text-field
        label="Kullanıcı Adı"
        required
        v-model="formData.username"
      ></v-text-field>
      <v-text-field

        label="E-mail"
        required
        v-model="formData.email"

      ></v-text-field>
           <v-text-field
             v-model="formData.password1"
             label="Parola"
          required
          :type="value ? 'password' : 'text'"
             @click:append="() => (value = !value)"
           :append-icon="value ? 'visibility' : 'visibility_off'"

      ></v-text-field>
 <v-text-field
          v-model="formData.password2"
             label="Parolanızı doğrulayınız"
        required
             :append-icon="value ? 'visibility' : 'visibility_off'"
    @click:append="() => (value = !value)"
    :type="value ? 'password' : 'text'"
      ></v-text-field>



      <v-btn class="mr-4" type="submit">Kayıt ol</v-btn>
  <span v-if="formData.password1 === formData.password2 && formData.password2.length > 0"  style="color: #42b983">Parola eşleşti</span>
  <span v-else style="color: red">Parola eşleşmedi</span>


    </form>
  </v-app>





</div>

</template>


<script>
    import Vuetify from "vuetify"
  import {UserData} from "../../store/userModule";

    export default {

        data(){
    return{
      value: String,
      msg:"",
      formData : {
        username: '',
        email: '',
        password1:'',
        password2:''
      }

    }
  },
        name: "registration",

    created() {

    },



      methods: {

    RegisterSubmit(){

      if(this.formData.password1 == this.formData.password2){
        this.msg = "Parola eşleşti"
         this.$store.dispatch('register',this.formData)

      console.log("Register Submit Methodu Çalıştı")
      }
    },

      },

  mounted(){

        }

    }
</script>

<style scoped>

  #app{
    width:40%;


    margin:auto;
  }


</style>

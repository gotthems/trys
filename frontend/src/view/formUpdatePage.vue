<template>

  <div id="app">


      <form @submit.prevent="onUpdate">
      <label>İçerik Başlığı</label>
      <v-text-field type="text" v-model="formData.title"/>
      <label>Hata Çözümü</label>
       <v-textarea id="txtInput" v-model="formData.solved"></v-textarea>
       <label>Kullanılan Dil veya Diller</label>
       <v-text-field id="txtInput" v-model="formData.software_lang"></v-text-field>

      <br/>

                  <div style="float: right;">
                  <v-app>

      <v-btn color="deep-purple accent-4" depressed small width="100px" height="40px" style="color: #eeeeee;"  type="submit">Update</v-btn>

     <v-btn color="deep-purple accent-4" depressed small width="100px" height="40px" style="color: #eeeeee;"  type="submit">Cancel</v-btn>

                  </v-app>
                    </div>


    </form>
  </div>

</template>

<script>
    import api from '../api/index'
import Vuetify from "vuetify"
import navBar from "../components/navbar"
import {ProfileData} from "../store/module";

    export default {
        name: "formUpdatePage",

       name: "formPage",
  components: {navBar},

  data(){
    return{
      formData : {
          title: '',
        content: '-',
        solved:"",
        software_lang:"",
        id : this.$route.params.root
      },


    }
  },

  created(){
    this.$store.dispatch( "initApp")


  },

  computed:{
    notes (){
      return this.$store.getters.getNote
    }
  },
  methods: {
    onSubmit(){
       this.$store.dispatch('addnote',this.formData)
    },
    onUpdate(){
      console.log("asdad" +" " +this.$route.params.root)
      console.log(this.id)
      this.$store.dispatch('updatenote',this.formData)

    }
  }





    }

</script>

<style scoped>

</style>

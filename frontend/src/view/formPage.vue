<template>


  <div id="app">


      <form @submit.prevent="onSubmit">
      <label>İçerik Başlığı</label>
      <v-text-field type="text" v-model="formData.title"/>
      <label>Hata Çözümü</label>
       <v-textarea id="txtInput" v-model="formData.solved"></v-textarea>
       <label>Kullanılan Dil veya Diller</label>
       <v-text-field id="txtInput" v-model="formData.software_lang"></v-text-field>

      <br/>

                  <div style="float: right;">
                  <v-app>
      <v-btn color="deep-purple accent-4" depressed small width="100px" height="40px" style="color: #eeeeee;"  type="submit">Submit</v-btn>

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
    name: "formPage",
  components: {navBar},

  data(){
    return{
      formData : {
          title: '',
        content: '-',
        solved:"",
        software_lang:""
      }

    }
  },

  created(){

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
      this.$store.dispatch('updatenote',this.formData)
    }
  }






    }
</script>

<style scoped>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;

  color: #2c3e50;

  text-align: left;
   font-size: 16px;
  font-family: 'Cookie', cursive;
}

h1, h2 {
  font-weight: normal;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}

  input, textarea{
    width:100%;
    display: block;
    padding:6px 10px;
    border-radius: 4px;
    margin-top: 10px;
    margin-bottom: 10px;
  }

  label{
    margin-top: 10px;
    display: block;
  }

  button{
    background: #42b983;
  height: 40px;
  min-width: 80px;
  border: none;
  border-radius: 10px;
  color: #eee;
  font-size: 16px;
  font-family: 'Cookie', cursive;
  position: relative;
  -webkit-tap-highlight-color: transparent;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;



    margin: 5px;



  }
  textarea{
    height: 150px;
  }

div.sol {
        width: 35%;
        float: left;
  padding-left: 5px;

}
div.sag {
        width: 55%;
        float: right;





}
div.container {
        border: 1px solid #000000;
        overflow: hidden;
        width: 100%;
}
</style>

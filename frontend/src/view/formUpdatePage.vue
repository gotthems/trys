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
        id : ""
      },



    }
  },

  created(){
    this.$store.dispatch( "initApp")
    this.formData.id = this.$route.params.id
    console.log(this.formData.id + "create")


  },

  computed:{

    notes (){
      return this.$store.getters.getNote
    },

  },
  methods: {
    onSubmit(){
       this.$store.dispatch('addnote',this.formData)
    },
    onUpdate(){
      this.$store.dispatch('updatenote',this.formData)
      console.log(this.$route.params.id + "OnUpdate")
       this.notematch()
    },
    notematch(){
    console.log(this.formData.id + "create2")

      for( var i in  this.notes){
         console.log(i + "sayıyor")
          var listest=[];

        if(this.notes[i]['id']  == this.$route.params.id ){

          listest.push(this.notes[i]['id'])
          console.log(this.$route.params.id +"s" + this.notes[i]['id'] + "ifififif")

          break;
        }

    }
    if(listest.length==0){
      this.$router.push('/Home')
      console.log("böyle bir syfa bulunmamaktaıdr")
    }


    }
  },
      mounted() {
        this.formData.id =  this.$route.params.id

      }


    }

</script>

<style scoped>

</style>

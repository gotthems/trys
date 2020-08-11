<template>

 <div >

  <div v-for="note in notes" style=" margin: auto;width: 100%;">

 <v-card height="250px" style="padding:10px;margin: auto;width: 60%; " v-if="$route.params.id.toString().indexOf(note.id) == 0">

     <h2>{{note.title}}</h2>

   {{note.solved}}<br>
   {{note.software_lang}}<br>

   <div style="margin-left: 66%;margin-top: 110px;">
   <router-link :to="{ name : 'updateFormPage', params: { id: note.id, root: note.id}} ">
  <button style="background: #2c3e50; color: #eeeeee;float:left;" > Update </button>
 </router-link>

<v-btn style="background: red; " v-on:click="deleteNote(id = note.id)">Delete </v-btn>
</div>

 </v-card>
<div v-if="$route.params.id.toString().indexOf(note.id) == -1 && notematch().length == 0 ">
  <h2>Böyle bir sayfa bulunmamaktadır</h2>
</div >


  </div>


</div>

</template>

<script>

      import api from '../api/index'
import Vuetify from "vuetify"
import {ProfileData} from "../store/module";


    export default {
        name: "noteDetailPage",


        data(){
    return{
      formData : {

        id : ""
      }
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

             deleteNote(id){
            this.$store.dispatch('deletenote',id)
          },
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

    return listest
    }
  },
      mounted() {
        this.formData.id =  this.$route.params.id

      }










    }
</script>

<style scoped>

</style>

<template>

<div id="app">
  <p>Home</p>

  <div v-for="note in notes">
<router-link :to="{ name : 'noteDetailPage', params: { id: note.id, root: note.id}} ">
   <br> <h3  >  {{note.title}} {{note.id}} </h3>
 </router-link>
    <br> <span>{{note.solved}}</span>
    <hr style="color: white;">
<router-link :to="{ name : 'updateFormPage', params: { id: note.id, root: note.id}} ">
  <button style="background: #2c3e50; color: #eeeeee;float:left;" > Update </button>
 </router-link>

<v-btn style="background: red; " v-on:click="deleteNote(id = note.id)">Delete </v-btn>


</div>

</div>



</template>

<script>
  import {mapState, mapGetters,mapActions,mapMutations} from 'vuex'
  import Vuetify from "vuetify"
  import {ProfileData} from "../store/module";
    export default {
        name: "Home",
      created(){
    this.$store.dispatch( "initApp")
      },
  computed:{
    notes (){
      return this.$store.getters.getNote
    },
  },
      methods:{
          deleteNote(id){
            this.$store.dispatch('deletenote',id)
          }
      },
    params : ['root']
    }
</script>

<style scoped>
  .v-text-field{
      width: 400px;
}
  #app{
    width: 600px;
    height: 300px;
    padding: 20px;
    position: relative;
    margin: auto;
  }
</style>

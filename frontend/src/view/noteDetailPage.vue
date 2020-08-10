<template>


<div>
  {{$route.params.id}}

  <div v-for="note in notes">

    <h2 v-if="note.id == $route.params.id">

      {{note.title}}
      {{note.solved}}

    </h2>


  </div>

</div>




</template>

<script>
    import {ProfileData} from "../store/module";
    export default {
        name: "noteDetailPage",
      created(){
       this.$store.dispatch( "initApp")

        },

       computed:{
        notes (){
      return this.$store.getters.getNote
    },

       }


    }
</script>

<style scoped>

</style>

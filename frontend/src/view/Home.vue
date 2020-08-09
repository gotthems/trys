<template>

<div id="app">
  <p>Home</p>

  <span>{{welcomeMessage}}</span>

  <input v-model="name"/>


 <v-btn small @click="updateUser">Update Name</v-btn>

</div>



</template>

<script>
  import {mapState, mapGetters,mapActions,mapMutations} from 'vuex'
  import navbar from "../components/navbar";

    export default {



      data(){
return {
  name: "Hi"
}
      },


        name: "Home",
      components: {navbar},
      computed:{
           ...mapState([
             'message',
             'username'
           ]),
        ...mapGetters([
          "welcomeMessage"
        ])
      },
      methods:{
        updateUser(){

          this.updateUsername(this.name)
        },
       ...mapActions(['updateUsername'])

      }

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

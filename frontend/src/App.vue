<template>


  <div id="app">


    <navBar></navBar>



        <br> <h3 v-for="note in notes" :key="notes.id">  {{note.title}}</h3>



  <router-view></router-view>

  </div>
</template>

<script>

import api from './api/index'
import Vuetify from "vuetify"
import navBar from "./components/navbar"
import {ProfileData} from "./store/module";

export default {
  name: 'app',
  components: {navBar},

  created(){
    this.$store.dispatch( "initApp")
  },

  computed:{
    notes (){
      return this.$store.getters.getNote
    }
  }


}



</script>

<style lang="scss">
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

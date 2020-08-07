<template>


  <div id="app">

<v-app id="inspire" style="height: 50px">
    <div>
      <v-app-bar
        color="indigo "
        dense
        dark
      >


        <v-app-bar-nav-icon></v-app-bar-nav-icon>

        <v-toolbar-title>Page title</v-toolbar-title>

        <v-spacer></v-spacer>

        <v-btn icon>
          <v-icon>mdi-heart</v-icon>
        </v-btn>

        <v-btn icon>
          <v-icon>mdi-magnify</v-icon>
        </v-btn>

        <v-menu
          left
          bottom
        >
          <template v-slot:activator="{ on, attrs }">
            <v-btn
              icon
              v-bind="attrs"
              v-on="on"
            >
              <v-icon>mdi-dots-vertical</v-icon>
            </v-btn>
          </template>

          <v-list>
            <v-list-item
              v-for="n in 5"
              :key="n"
              @click="() => {}"
            >
              <v-list-item-title>Option {{ n }}</v-list-item-title>
            </v-list-item>
          </v-list>
        </v-menu>
      </v-app-bar>
    </div>
  </v-app>
    <h2 style="font-weight: bold; color: black; font-family: Helvetica;">CREATE AND UPDATE NOTE APP</h2>


<div class="sol">


                <form @submit.prevent="submitNote">
      <label>Title</label>
      <v-text-field type="text" v-model="formData.title"/>
      <label>Content</label>
      <v-textarea id="txtInput" v-model="formData.content"></v-textarea>

      <br/>

                  <div style="float: right;">
                  <v-app>
      <v-btn color="deep-purple accent-4" depressed small width="100px" height="40px" style="color: #eeeeee;"  type="submit">Submit</v-btn>
                    </v-app>
                    </div>



    </form>

  <br/>

  <span style="margin-left: 10px" v-if="msg == '' ">Note:  </span> <span style="color: #42b983 " v-if="msg">{{msg}}</span>
  <p style="margin-left: 10px;" v-if="msg == '' ">If you want to update a note you wrote earlier.
    Fill in the title and content field first.
    Then click the update button for the note you want to update</p>

        </div>

        <div class="sag">



    <h6 style="font-size: 18px; margin-bottom: 0px; color: #42b983">My Note List</h6>
     <hr>
    <ul>
      <li v-for="(note, index) in notes"   :key="index">
                    <h3>{{note.title}}</h3>


                <p>{{note.content}}</p>


        <span style="font-size: 12px; margin-left: 500px;  ">Created On
          {{note.created_time.slice(8,10).split("T").reverse().join("")}}
          {{note.created_time.slice(5,7).split("T").reverse().join("")}}
          {{note.created_time.slice(0,4).split("T").reverse().join("")}}
          {{note.created_time.slice(10,19).split("T").join(" ")}}</span>
        <button style="background: red; float:left;margin-left: 500px;" v-on:click="deletteNotes(id = note.id)">Delete </button>
        <button style="background: #2c3e50; color: #eeeeee;" v-on:click="UpdateNote(id = note.id)">Update </button>

        <hr>
      </li>

    </ul>
        </div>
    <br/>
<compvue></compvue>
  </div>
</template>

<script>

import api from './api/index'
import Vuetify from "vuetify"


export default {
  name: 'app',


  data() {
    return {
      msg: '',
      formData: {
        title: '',
        content: ''
      },
      notes: [],

    }
  },
  methods: {

    deletteNotes(id){
      api.deleteNotes('DELETE',null,id).then(
        res => {
          this.msg =" Deleted"
          this.fetchAllNotes()
        }
      )
    },


    submitNote() {
      api.fetchNotes('post', null, this.formData).then(res => {
        this.msg = 'Saved',
        this.fetchAllNotes()

      }).catch((e) => {
               var  sayi = 0

              var titles = this.formData.title

              console.log(this.formData.title + "girilen veri")


              this.notes.forEach(function (item, index, array) {

                if (titles == item.title) {
                  console.log(item.title + " " + "başlığıyla aynı başlığı taşıyan bir notunuz var")
                  sayi = 1
                }
              });

          if(sayi == 1) {
          this.msg = this.formData.title + " " +  " you have a note with the same name"
        }
      })

    },


    fetchAllNotes() {
      api.fetchNotes('get', null, null).then(res => {
        this.notes = res.data.reverse()
        //check log data
        console.log(this.notes)
      }).catch((e) => {
        console.log(e)

      })
    },

    UpdateNote(id) {
    api.updateNotes('PUT', null, this.formData, id).then(res => {
      this.msg = 'Note Updated',
        this.fetchAllNotes()

    }).catch((e)=> {
      console.log(e)
    })

  }




  },
  mounted() {
    this.fetchAllNotes()

  },



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
 overflow-y: scroll; height:617px;



}
div.container {
        border: 1px solid #000000;
        overflow: hidden;
        width: 100%;
}
</style>

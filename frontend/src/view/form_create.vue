<template>


  <div id="app">


    <router-view></router-view>


    <h2 style="font-weight: bold; color: black; font-family: Helvetica;">ÇÖZÜM KAYDI OLUŞTURMA FORMU</h2>


<div class="sol">

     <form @submit.prevent="submitNote">
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
    <br/>

  <span style="margin-left: 10px" v-if="msg == '' ">Note:  </span> <span style="color: #42b983 " v-if="msg"> {{msg}} </span>
  <p style="margin-left: 10px;" v-if="msg == '' ">If you want to update a note you wrote earlier.
    Fill in the title and content field first.
    Then click the update button for the note you want to update</p>


        </div>

        <div class="sag">


 <h6 style="font-size: 18px; margin-bottom: 0px; color: #42b983">Çözüm Listesi</h6>
     <hr>
    <ul>
      <li v-for="(note, index) in notes"   :key="index">
                    <h3>{{note.title}}</h3>

                <p>Hata Çözümü: {{note.solved}}</p>
                  <p>Kullanılan dil: {{note.software_lang}}</p>


        <span style="font-size: 12px; margin-left: 500px;  ">Created On
          {{note.created_time.slice(8,10).split("T").reverse().join("")}}
          {{note.created_time.slice(5,7).split("T").reverse().join("")}}
          {{note.created_time.slice(0,4).split("T").reverse().join("")}}
          {{note.created_time.slice(10,19).split("T").join(" ")}}</span>

               <button style="float: left" v-on:click="matchForm(id =note.id)">Seç</button>

        <button style="background: #2c3e50; color: #eeeeee;float:left;" v-on:click="UpdateNote(id = note.id)">Update </button>
<button style="background: red; " v-on:click="deletteNotes(id = note.id)">Delete </button>
        <hr>
      </li>

    </ul>




        </div>
    <br/>

  </div>
</template>

<script>

import api from '../api/index'
import Vuetify from "vuetify"
import navBar from "../components/navbar"
import stores from "../store";


export default {
  name: 'form_create',
  components: {navBar},


  created() {


    this.$store.dispatch('initApp')

    },

  data() {
    return {
      msg: '',
      formData: {
        title: '',
        content: '-',
        solved:"",
        software_lang:""

      },
      notes: [],

    }
  },

methods:{

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
      this.msg = "saved"
      this.notes = this.fetchAllNotes()




    }).catch((e) => {
      var sayi = 0

      var titles = this.formData.title

      console.log(this.formData.title + "girilen veri")

        this.notes.forEach(function (item, index, array) {

        if (titles == item.title) {
          console.log(item.title + " " + "başlığıyla aynı başlığı taşıyan bir notunuz var")
          sayi = 1
        }
      });

      if (sayi == 1) {
        this.msg = this.formData.title + " " + " you have a note with the same name"
      }
    })

  },


    fetchAllNotes() {
      api.fetchNotes('get', null, null).then(res => {

        this.notes = res.data.reverse()

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

  },

  matchForm(id){

        var sayi = 0

      var lister = []
        this.notes.forEach(function (item, index, array) {

       if(item.id == id){
         sayi = 1
         console.log(item.title)
        lister.push(item.title,item.solved,item.software_lang)
       }

      });

    this.formData.title = lister[0]
    this.formData.solved = lister[1]
    this.formData.software_lang = lister[2]

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





}
div.container {
        border: 1px solid #000000;
        overflow: hidden;
        width: 100%;
}
</style>

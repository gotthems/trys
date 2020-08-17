<template>


  <div id="app" style="margin: auto;width: 55%;" >

  <v-app id="inspire">
    <v-form @submit.prevent="userprofileupdate" >

  <v-row style="margin-right:auto;width: 95%;">
    <v-col cols="8" >
     <label >Kullanıcı Adı</label>
      <v-text-field solo-inverted  dense    filled v-model=username  v-bind:label="userdata['username']" hide-details="auto" ></v-text-field >

      </v-col>
    </v-row>


          <v-row style="margin-right:auto;width: 95%;">
    <v-col cols="8" >
      <label >Email</label>
      <v-text-field  solo-inverted  dense v-model=email :rules="this.rules" v-bind:label="userdata['email']" > </v-text-field>

      </v-col>
    </v-row>
        <v-row style="margin-right:auto;">

           <v-col cols="4" style="width: 85%;">
             <label>Ad</label>
        <v-text-field solo-inverted dense v-model="first_name" v-bind:label="userdata['first_name']"></v-text-field>
      </v-col>
    <v-col cols="4"  >
             <label>Soyad</label>
        <v-text-field solo-inverted dense v-model="last_name" style="width: 90%;" v-bind:label="userdata['last_name']" > </v-text-field>
      </v-col>
    </v-row>
         <v-row style="margin-right:auto;width: 95%;">
    <v-col cols="8" >
      <label >Cep Telefonu</label>
      <v-text-field  solo-inverted dense v-model=phone_number v-bind:label="userdata['phone_number']" > </v-text-field>
      </v-col>
    </v-row>
       <v-row style="margin-right:auto;width: 95%;">
    <v-col cols="8" >
      <label >Doğum Tarihi</label>
 <v-text-field  solo-inverted dense v-model=birthday > </v-text-field>


      </v-col>
    </v-row>


 <v-row style="margin-right:auto;width: 95%;">
       <v-col class="d-flex" cols="12" sm="6" >
        <v-select
          v-model="gender"
          label="Cinsiyet"
          dense solo-inverted
          item-text="value"
          item-value="text"
          :items="options"
        >

        </v-select>
      </v-col>
          </v-row>
       <v-row style="margin-right:auto;width: 95%;">
       <v-col class="d-flex" cols="12" sm="6" >
        <v-select
          v-model="educational_status"
          label="Öğrenim Durumu"
          dense solo-inverted
          item-text="value"
          item-value="text"
          :items="options2"
        >

        </v-select>
      </v-col>
          </v-row>

 <v-row style="margin-right:auto;width: 95%;">
       <v-col class="d-flex" cols="12" sm="6" >
 <v-btn class="mr-4" type="submit">Güncelle</v-btn>
           </v-col>
          </v-row>
    </v-form>

  </v-app>



</div>

</template>

<script>




      import Vuetify from "vuetify"
  import {UserData} from "../../store/userModule";
     import jsonDict from "../../jsonFiles/data.json"
import jsonfile from "../../jsonFiles/jsonfile";
    export default {

        name: "userProfileUpdate",

         data(){

        return {
          selected: "Choose Province",
            rules:[
      value => !!value || 'Bu alan boş bırakılamaz',
      value => (value || '').length <= 20 || 'Max 20 characters',
      value => {
        const pattern = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
        return pattern.test(value) || 'Geçersiz e posta'
      },
    ],
          options: jsonDict.Gender,
          options2: jsonDict.educational_status,
          educational_status:'',
          gender:'',
          birthday:'',
          email:'',
          phone_number:'',
           username:'',
           first_name:'',
          last_name:'',
          profileData:{


          }
        }

      },

      created(){

            this.$store.dispatch('initUserData')
            this.$store.dispatch('inijson')



      },

      computed:{

          genderq(){

          for(var i in this.$store.getters.user){

            return this.$store.getters.user[i]

          }
          return this.$store.getters.user


        },
            userdata(){


        for(const i in this.$store.getters.getUser){
        var data = this.$store.getters.getUser[i]

        this.username  = data['username']
          this.email  = data['email']
          this.first_name  = data['first_name']
          this.last_name  = data['last_name']
          this.phone_number  = data['phone_number']
          this.birthday  = data['birthday']
          this.gender  = data['gender']
          this.educational_status  = data['educational_status']

//this.$store.dispatch('getJsonData',data['gender'])
        return data
      }
        return this.$store.getters.getUser
    },

      },





      methods:{

          userprofileupdate(){
                  //gender
                  if(this.gender !== '' ){
                      this.profileData['gender'] = this.gender

                  } //educational status
                   if( this.educational_status !== ''){

                     this.profileData['educational_status'] = this.educational_status
                  }
                     if( this.birthday !== ''){

                     this.profileData['birthday'] = this.birthday
                  }
                      if( this.email !== ''){

                     this.profileData['email'] = this.email
                  }
                      if( this.phone_number !== ''){

                     this.profileData['phone_number'] = this.phone_number
                  }
                      if( this.username !== ''){

                     this.profileData['username'] = this.username
                  }
                       if( this.last_name !== ''){

                     this.profileData['last_name'] = this.last_name
                  }
                        if( this.first_name !== ''){

                     this.profileData['first_name'] = this.first_name
                  }



                 return this.$store.dispatch('userprofilupdate',this.profileData)



          },



      },

  mounted() {




  },



    }

</script>

<style scoped>

.v-text-field{
  height: 35px;
}

</style>

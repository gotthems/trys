<template>


<div>

    <v-card>
    <v-container fluid>
      <v-row
        align="center"
      >

        <v-col cols="12" sm="6">
          <v-select

            item-text="value"
          item-value="text"
            :items="items"
            chips
            label="Chips"
            multiple
            solo
          ></v-select>
        </v-col>
      </v-row>
    </v-container>
  </v-card>


</div>


</template>

<script>

      import Vuetify from "vuetify"
      import {AdvertiseStore} from "../../store/advertiseStore/advertiseStore";
      import jsonDict from "../../jsonFiles/advertisejson/advertiseChoice.json"
      import jsonfile from "../../jsonFiles/jsonfile";

    export default {
        name: "createAdvertise",



      created() {
      this.advertiseCreate()
          },

      data(){

        return {

          items: jsonDict.interior_feature,
          options: jsonDict.exterior_feature,
          options2: jsonDict.educational_status,
           profileData:{
             title: "aaaaaa",
            description: "aaaaa",
            price: 200,
            square_meter: 200,
            number_of_rooms: 1,
            building_age: 0,
            floor: 0,
            number_of_floors: 2,
            number_of_bathrooms: 1,
            heating: 2,
            balcony_exists: true,
            using_status: 0,
            housing_shape: 2,
            status: 0,
            visibility: 0,
            image: null,
            frontal: [8],
            interior_feature: [46],
            exterior_feature: [29],
            locality: [48],
            transportation: [26],
            landscape: [16,17,18],
            suitable_for_disabled: [16]
           }
          }

        },

      methods:{

           advertiseCreate(){
            console.log("AÇlıştı")
            return  this.$store.dispatch('createAdvertiseDataActions',this.profileData)


      }

      }



    }
</script>

<style scoped>

</style>

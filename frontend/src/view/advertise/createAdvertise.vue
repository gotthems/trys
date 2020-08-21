<template>


<div class="app">

 <v-form @submit.prevent="advertiseCreate">



    <v-row align="center">
        <v-col cols="12" sm="6">
          <v-list-item>
          <v-list-item-title>Oda Sayısı</v-list-item-title>
            </v-list-item>
          <v-select
            v-model="profileData.number_of_rooms"
            item-text="value"
          item-value="text"
            :items="items_NumberOfRoomsChoices"
            label="Seçiniz"
            solo
            style="width: 400px"
          ></v-select>
        </v-col>
      </v-row>

    <v-row align="center">
        <v-col cols="12" sm="6">
          <v-list-item>
          <v-list-item-title>Bina Yaşı</v-list-item-title>
            </v-list-item>
          <v-select
            v-model="profileData.building_age"
            item-text="value"
          item-value="text"
            :items="items_NumberOfBuildingAgeChoices"
            label="Seçiniz"
            solo

            style="width: 400px"
          ></v-select>
        </v-col>
      </v-row>

    <v-row align="center">
        <v-col cols="12" sm="6">
          <v-list-item>
          <v-list-item-title>Bina Kat Sayısı</v-list-item-title>
            </v-list-item>
          <v-select
            v-model="profileData.number_of_floors"
            item-text="value"
          item-value="text"
            :items="items_FLOOR_TOTAL_CHOICES"
            label="Seçiniz"
            solo

            style="width: 400px"
          ></v-select>
        </v-col>
      </v-row>

    <v-row align="center">
        <v-col cols="12" sm="6">
          <v-list-item>
          <v-list-item-title>Bulunduğu Kat</v-list-item-title>
            </v-list-item>
          <v-select
            v-model="profileData.floor"
            item-text="value"
          item-value="text"
            :items="items_FLOOR_LOCATION_CHOICES"
            label="Seçiniz"
            solo

            style="width: 400px"
          ></v-select>
        </v-col>
      </v-row>

    <v-row align="center">
        <v-col cols="12" sm="6">
          <v-list-item>
          <v-list-item-title>Isınma Şekli</v-list-item-title>
            </v-list-item>
          <v-select
            v-model="profileData.heating"
            item-text="value"
          item-value="text"
            :items="items_HeatingChoices"
            label="Seçiniz"
            solo

            style="width: 400px"
          ></v-select>
        </v-col>
      </v-row>

    <v-row align="center">
        <v-col cols="12" sm="6">
          <v-list-item>
          <v-list-item-title>Banyo Sayısı</v-list-item-title>
            </v-list-item>
          <v-select
            v-model="profileData.number_of_bathrooms"
            item-text="value"
          item-value="text"
            :items="items_NumberOfBathroomsChoices"
            label="Seçiniz"
            solo

            style="width: 400px"
          ></v-select>
        </v-col>
      </v-row>

    <v-row align="center">
        <v-col cols="12" sm="6">
          <v-list-item>
          <v-list-item-title>Kullanım Durumu</v-list-item-title>
            </v-list-item>
          <v-select
            v-model="profileData.using_status"
            item-text="value"
          item-value="text"
            :items="items_UsingStatusChoices"
            label="Seçiniz"
            solo

            style="width: 400px"
          ></v-select>
        </v-col>
      </v-row>

    <v-row align="center">
        <v-col cols="12" sm="6">
          <v-list-item>
          <v-list-item-title>İlan Görünürlük Durumu</v-list-item-title>
            </v-list-item>
          <v-select
            v-model="profileData.visibility"
            item-text="value"
          item-value="text"
            :items="items_AdvertiseVisibilityChoices"
            label="Seçiniz"
            solo

            style="width: 400px"
          ></v-select>
        </v-col>
      </v-row>

    <v-row align="center">
        <v-col cols="12" sm="6">
          <v-list-item>
          <v-list-item-title>İlan Durumu</v-list-item-title>
            </v-list-item>
          <v-select
            v-model="profileData.status"
            item-text="value"
          item-value="text"
            :items="items_AdvertiseStatusChoices"
            label="Seçiniz"
            solo
            single-line
            style="width: 400px"
          ></v-select>
        </v-col>
      </v-row>

    <v-row align="center">
        <v-col cols="12" sm="6">
          <v-list-item>
          <v-list-item-title>İç Özellikler</v-list-item-title>
            </v-list-item>
          <v-select
            v-model="profileData.interior_feature"
            item-text="value"
          item-value="text"
            :items="items_interior_feature"
            chips
            label="Seçiniz"
            multiple
            solo
            style="width: 400px"
          ></v-select>
        </v-col>
      </v-row>

     <v-row align="center">
        <v-col cols="12" sm="6">
          <v-list-item>
          <v-list-item-title>Dış Özellikler</v-list-item-title>
            </v-list-item>
          <v-select
            v-model="profileData.exterior_feature"
            item-text="value"
          item-value="text"
            :items="items_exterior_feature"
            chips
            label="Seçiniz"
            multiple
            solo
            style="width: 400px"
          ></v-select>
        </v-col>
      </v-row>

      <v-row align="center" >

        <v-col cols="12" sm="6">
          <v-list-item>
          <v-list-item-title>Yakınında Bulunan Yer/Alan/Mekan</v-list-item-title>
            </v-list-item>

          <v-select
            v-model="profileData.locality"
            item-text="value"
          item-value="text"
            :items="items_locality"
            chips
            label="Seçiniz"
            multiple
            solo

          ></v-select>
        </v-col>
      </v-row>

   <v-row align="center" >

        <v-col cols="12" sm="6">
          <v-list-item>
          <v-list-item-title>Ulaşım Olanakları</v-list-item-title>
            </v-list-item>

          <v-select
            v-model="profileData.transportation"
            item-text="value"
          item-value="text"
            :items="items_transportation"
            chips
            label="Seçiniz"
            multiple
            solo

          ></v-select>
        </v-col>
      </v-row>

     <v-row align="center" >

        <v-col cols="12" sm="6">
          <v-list-item>
          <v-list-item-title>Manzara</v-list-item-title>
            </v-list-item>

          <v-select
            v-model="profileData.landscape"
            item-text="value"
            item-value="text"
            :items="items_landscape"
            chips
            label="Seçiniz"
            multiple
            solo
            style="width: 400px"
          ></v-select>
        </v-col>
      </v-row>

    <v-row align="center" >

        <v-col cols="12" sm="6">
          <v-list-item>
          <v-list-item-title>Engelliler için</v-list-item-title>
            </v-list-item>

          <v-select
            v-model="profileData.suitable_for_disabled"
            item-text="value"
          item-value="text"
            :items="items_suitable_for_disabled"
            chips
            label="Seçiniz"
            multiple
            solo

          ></v-select>
        </v-col>
      </v-row>


   <v-row align="center" >

        <v-col cols="12" sm="6">
          <v-list-item>
          <v-list-item-title>Balkon</v-list-item-title>
            </v-list-item>

          <v-select
            v-model="profileData.balcony_exists"
            item-text="value"
          item-value="text"
            :items="items_balcony_exist"

            label="Seçiniz"

            solo

          ></v-select>
        </v-col>
      </v-row>

  <v-btn type="submit">İlan Oluştur</v-btn>
 </v-form>

</div>


</template>

<script>

      import Vuetify from "vuetify"
      import {AdvertiseStore} from "../../store/advertiseStore/advertiseStore";
      import jsonDict from "../../jsonFiles/advertisejson/advertiseChoice.json"
      import jsonfile from "../../jsonFiles/jsonfile";

    export default {
        name: "createAdvertise",





      data(){

        return {

          items_interior_feature: jsonDict.interior_feature,
          /*items_HousingShapeChoices: jsonDict.HousingShapeChoices, tanım bulamadığım için atlıyorum*/
          items_AdvertiseStatusChoices: jsonDict.AdvertiseStatusChoices,
          items_AdvertiseVisibilityChoices: jsonDict.AdvertiseVisibilityChoices,
          items_UsingStatusChoices: jsonDict.UsingStatusChoices,
          items_NumberOfBathroomsChoices: jsonDict.NumberOfBathroomsChoices,
          items_HeatingChoices: jsonDict.HeatingChoices,
          items_FLOOR_LOCATION_CHOICES: jsonDict.FLOOR_LOCATION_CHOICES,
          items_FLOOR_TOTAL_CHOICES: jsonDict.FLOOR_TOTAL_CHOICES,
          items_NumberOfBuildingAgeChoices: jsonDict.NumberOfBuildingAgeChoices,
          items_NumberOfRoomsChoices: jsonDict.NumberOfRoomsChoices,
          items_exterior_feature: jsonDict.exterior_feature,
          items_locality: jsonDict.locality,
          items_transportation: jsonDict.transportation,
          items_landscape: jsonDict.landscape,
          items_suitable_for_disabled: jsonDict.suitable_for_disabled,
          items_visibility: jsonDict.visibility,
          items_status: jsonDict.status,
          items_balcony_exist: jsonDict.balcony_exist,

           profileData:{
             title: "asdas2qsqqq",
            description: "qqqqqq",
            price: 200,
            square_meter: 200,
            number_of_rooms: "",
            building_age: "",
            floor: "",
            number_of_floors: "",
            number_of_bathrooms: "",
            heating: "",
            balcony_exists: true,
            using_status: "",
            housing_shape: "",
            status: "",
            visibility: "",
            image: null,
            frontal: [8],
            interior_feature: "",
            exterior_feature: [29],
            locality: [],
            transportation: [26],
            landscape: [16,17,18],
            suitable_for_disabled: [16]
           }
          }

        },

      methods:{

           advertiseCreate(){
            console.log("AÇlıştı")

             for(var i in this.profileData.interior_feature ){
                           console.log(this.profileData.interior_feature[i])

             }

            return  this.$store.dispatch('createAdvertiseDataActions',this.profileData)


      }

      }



    }
</script>

<style scoped>

</style>

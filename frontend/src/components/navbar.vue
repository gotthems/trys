<template>

  <v-app id="inspire" style="height: 50px">

    <div>
      <v-app-bar
        color="indigo "
        dense
        dark
      >


<router-link style="text-decoration:none;color: white" to="/">

        <v-toolbar-title>Helpcom</v-toolbar-title>
</router-link>
<v-spacer></v-spacer>
 <v-toolbar flat   max-width="700px" dark height="48%"  >
          <v-text-field ></v-text-field>


          <v-btn icon>
            <v-icon>mdi-magnify</v-icon>
          </v-btn>


          <v-btn icon>
            <v-icon>mdi-dots-vertical</v-icon>
          </v-btn>

        </v-toolbar>
        <v-spacer></v-spacer>
        <router-link style="text-decoration: none;" to="/Home">
        <v-btn icon >

             <v-icon color="white">mdi-home</v-icon>

        </v-btn>

</router-link>
<router-link style="text-decoration: none;" to="/formPage">
        <v-btn icon>

          <v-icon color="white">mdi-plus</v-icon>

        </v-btn>
</router-link>

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

</template>

<script>
    export default {
        name: "navbar"

    }



</script>

<style scoped>

v-toolbar{


    position: relative;
    margin: auto;
  }
</style>

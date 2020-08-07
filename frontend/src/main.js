import Vue from 'vue'
import App from './App.vue'
import axios from 'axios'
import vuetify from '../src/plugins/vuetify'
import 'material-design-icons-iconfont/dist/material-design-icons.css'
import '@mdi/font/css/materialdesignicons.css'




new Vue({
  el: '#app',
    vuetify,
  beforeCreate(){
    Vue.prototype.$http = axios
    axios.defaults.xsrfHeaderName = 'X-CSRFToken'
    axios.defaults.xsrfCookieName = 'csrftoken'

  },
  render: h => h(App)
})

import Vue from 'vue'
import App from './App.vue'
import axios from 'axios'


new Vue({
  el: '#app',
  beforeCreate(){
    Vue.prototype.$http = axios
    axios.defaults.xsrfHeaderName = 'X-CSRFToken'
    axios.defaults.xsrfCookieName = 'csrftoken'

  },
  render: h => h(App)
})

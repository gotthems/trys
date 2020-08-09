import Vue from 'vue'
import Router from 'vue-router'
import App from '../App.vue'
import Home from '../view/Home'
import form_create from '../view/form_create'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/App',
      name: 'App',
      component: App
    },
      {
      path: '/Home',
      name: 'Home',
      component: Home
    },
    {
      path: '/form_create',
      name: 'form_create',
      component: form_create
    },

  ]
})

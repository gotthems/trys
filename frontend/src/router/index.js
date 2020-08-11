import Vue from 'vue'
import Router from 'vue-router'
import App from '../App.vue'
import Home from '../view/Home'
import form_create from '../view/form_create'
import formPage from '../view/formPage'
import updateFormPage from '../view/formUpdatePage'
import noteDetailPage from '../view/noteDetailPage'

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
      {
      path: '/formPage',
      name: 'formPage',
      component: formPage
    },
    {
      path: '/updateFormPage/:id',
      name: 'updateFormPage',
      component: updateFormPage
    },
     {
      path: '/noteDetailPage/:id',
      name: 'noteDetailPage',
      component: noteDetailPage
    },


  ]
})

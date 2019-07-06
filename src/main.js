import Vue from 'vue'
import App from './App.vue'
import router from './router'
//import { yandexMap, ymapMarker } from 'vue-yandex-maps'

Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')

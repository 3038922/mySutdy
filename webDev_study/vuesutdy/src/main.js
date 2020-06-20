import Vue from 'vue' // ES6 模块导入方式
import App from './App.vue'
import a from './router'
import store from './store'

Vue.config.productionTip = false

new Vue({
  router: a,
  store,
  render: h => h(App)
}).$mount('#app')

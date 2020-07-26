import Vue from 'vue'
import ElementUI from 'element-ui' // 导入ELEMENTUI
import App from './App.vue'
import store from './store'
import router from './router'
import './plugins/element.js'
import 'element-ui/lib/theme-chalk/index.css' //导入样式

Vue.use(ElementUI)
Vue.config.productionTip = false

new Vue({
  store,
  router,
  render: (h) => h(App)
}).$mount('#app')

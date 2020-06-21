import Vue from 'vue' // ES6 模块导入方式
import App from './App.vue'
import a from './router'
import store from './store'
// 下面这行没用啊
// eslint-disable-line no-unused-vars
// import Alla from './module/moduleA' // 导入所有接口
import { a1, a2 as mya2 } from './module/moduleB' // 可以只导入某几个接口
// 引入 ElementUI
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'

Vue.use(ElementUI)

Vue.config.productionTip = false

console.log(a1, mya2)

new Vue({
  router: a,
  store,
  render: (h) => h(App)
}).$mount('#app')

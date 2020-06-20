import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    isTabbarShow: true // 自定义的共享状态
  },
  mutations: {
    // 为了更好的监控 DEBUG
    test(state, data) {
      state.isTabbarShow = data
      console.log('I am test', data)
    }
  },
  actions: {},
  modules: {}
})

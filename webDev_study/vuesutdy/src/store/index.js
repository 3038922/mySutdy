import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    isTabbarShow: true, // 自定义的共享状态
    cominglist: [] // 缓存用的吧
  },
  mutations: {
    // 为了更好的监控 DEBUG
    test(state, data) {
      state.isTabbarShow = data
      console.log('I am test', data)
    },
    comingListMutation(state, data) {
      state.cominglist = data
    }
  },
  actions: {
    // 专门写异步处理的
    getComingListAction(store) {
      axios({
        url: 'https://m.maizuo.com/gateway?type=2&cityId=620100&k=1616921',
        headers: {
          'X-Client-Info': '{"a":"3000","ch":"1002","v":"5.0.4","e":"1592581289360498079989762"}',
          'X-Host': 'mall.film-ticket.film.list'
        }
      }).then(res => {
        console.log(res.data)
        store.commit('getComingListAction', res.data.data.films)
      })
    }
  },
  modules: {}
})

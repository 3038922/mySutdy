import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    isTabbarShow: true, // 自定义的共享状态
    cominglist: [] // 缓存用的吧
  },
  getters: {
    /**
     * 使用这个函数看 comingsoon.vue
     * @param {*} state 必须用这个传cominglist
     */
    cominglistGetter(state) {
      return state.cominglist.filter((item, index) => index < 3) // 仅取出返回数组的前三个
    }
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
        url: 'https://m.maizuo.com/gateway?cityId=620100&pageNum=1&pageSize=10&type=2&k=4884084',
        headers: {
          'X-Client-Info': '{"a":"3000","ch":"1002","v":"5.0.4","e":"1592581289360498079989762"}',
          'X-Host': 'mall.film-ticket.film.list'
        }
      }).then((res) => {
        console.log(res.data)
        // 传数据这样 comlist 就可以获得数据了
        store.commit('comingListMutation', res.data.data.films)
      })
    }
  },
  modules: {}
})

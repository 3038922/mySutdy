import Vue from 'vue'
import Router from 'vue-router'

import Film from '@/views/film'
import Cinema from '@/views/cinema'
import Center from '@/views/center'
import Nowplaying from '@/views/film/nowplaying'
import Comingsoon from '@/views//film/comingsoon'
Vue.use(Router)

const router = new Router({
  // mode: 'history',
  // base: process.env.BASE_URL,
  routes: [
    {
      path: '/film',
      component: Film,
      // 二级路由
      children: [
        {
          path: 'nowplaying',
          component: Nowplaying
        },
        {
          path: 'comingsoon',
          component: Comingsoon
        },
        {
          path: '',
          redirect: 'nowplaying'
        }
      ]
    },
    {
      path: '/cinema',
      component: Cinema
    },
    {
      path: '/center',
      component: Center
    },
    // 如果都不匹配 重定向
    {
      path: '*',
      redirect: '/film'
    }
  ]
})

export default router

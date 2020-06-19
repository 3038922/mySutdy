import Vue from 'vue'
import Router from 'vue-router'

import Film from '@/views/film'
import Nowplaying from '@/views/film/nowplaying'
import Comingsoon from '@/views/film/comingsoon'

import Cinema from '@/views/cinema'
import Center from '@/views/center'
import Detail from '@/views/detail'
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
      path: '/detail/:id', // 动态路由写法
      // 命名路由 可以命名跳转
      name: 'ares',
      component: Detail
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

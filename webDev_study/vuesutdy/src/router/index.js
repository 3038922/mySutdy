import Vue from 'vue'
import Router from 'vue-router'

import Film from '@/views/film'
import Nowplaying from '@/views/film/nowplaying'
import Comingsoon from '@/views/film/comingsoon'

import Cinema from '@/views/cinema'
import Center from '@/views/center'
import Detail from '@/views/detail'
import Login from '@/views/login'
import City from '@/views/city'
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
      path: '/login',
      component: Login
    },
    {
      path: '/detail/:id', // 动态路由写法
      // 命名路由 可以命名跳转
      name: 'ares',
      component: Detail
    },
    {
      path: '/center',
      alias: '/my',
      component: Center
    },
    {
      path: '/city',
      component: City
    },
    // 如果都不匹配 重定向
    {
      path: '*',
      redirect: '/film'
    }
  ]
})
// const auth = {
//   isLogin() {
//     return false;
//   },
// };
// 全局守卫 路由守卫
// router.beforeEach((to, from, next) => {
//   if (to.path === "/center") {
//     if (auth.isLogin()) {
//       console.log("允许访问");
//       next();
//     } else {
//       console.log("拒绝访问");
//       next("/login");
//     }
//   } else {
//     // 必须用next()放行
//     next();
//   }
// });
export default router

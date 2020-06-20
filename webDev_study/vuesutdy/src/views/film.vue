<template>
  <div>
    <!-- 为了保证周期 所以弄个数组长度做key -->
    <swiper :key="looplist.length">
      <div class="swiper-slide" v-for="data in looplist" :key="data.id">
        <img :src="data.img | filterPath" />
      </div>
    </swiper>
    <!-- 路由容器 -->
    <router-view></router-view>
  </div>
</template>

<script>
import Swiper from '@/views/film/swiper'
import axios from 'axios'
import Vue from 'vue'
/**
 * 过滤地址 替换 w.h
 */
Vue.filter('filterPath', (res) => {
  return res.replace('w.h', '128.180')
})
export default {
  components: {
    // EC6 简化定义
    swiper: Swiper
  },
  data() {
    return {
      looplist: []
    }
  },
  mounted() {
    axios.get('/json/maoyan.json').then((res) => {
      this.looplist = res.data.movieList
      console.log(this.looplist)
    })
  }
}
</script>

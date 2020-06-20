<template>
  <div>
    <!-- 为了保证周期 所以弄个数组长度做key -->
    <swiper :key="looplist.length" ref="myswiper">
      <div class="swiper-slide" v-for="data in looplist" :key="data.id">
        <img :src="data.img | filterPath" />
      </div>
    </swiper>
    <!-- 记得加: -->
    <filmheader :class="isFixed ? 'fixed' : ''"></filmheader>
    <!-- 路由容器 -->
    <router-view></router-view>
  </div>
</template>

<script>
import Swiper from '@/views/film/swiper'
import axios from 'axios'
import Vue from 'vue'
import Filmheader from '@/views/film/filmheader'
/**
 * 过滤地址 替换 w.h
 */
Vue.filter('filterPath', res => {
  return res.replace('w.h', '128.180')
})
export default {
  components: {
    // EC6 简化定义
    swiper: Swiper,
    filmheader: Filmheader
  },
  data() {
    return {
      looplist: [],
      isFixed: false
    }
  },
  mounted() {
    axios.get('/json/maoyan.json').then(res => {
      this.looplist = res.data.movieList
    })
    // 监听 注意这里是全局 必须设置离开解绑
    window.onscroll = this.handleScroll
  },

  beforeDestroy() {
    // 离开页面解绑
    window.onscroll = null
  },
  methods: {
    handleScroll() {
      /**
       * 判断是否超过HEAD的位置
       */
      if (document.documentElement.scrollTop >= this.$refs.myswiper.$el.offsetHeight) {
        this.isFixed = true
      } else {
        this.isFixed = false
      }
    }
  }
}
</script>
<style lang="scss" scoped></style>

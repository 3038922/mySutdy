<template>
  <!-- 判断是否为空 空的话就等待 -->
  <div v-if="filminfo">
    <img :src="filminfo.img | filterPath" alt="" />
    <h2>{{ filminfo.nm }}</h2>
    <h3>演职人员</h3>
    <swiper>
      <div class="swiper-slide" v-for="data in stars" :key="data">
        <p>{{ data }}</p>
      </div>
    </swiper>
  </div>
</template>

<script>
/**
 * 过滤地址 替换 w.h
 */
import Vue from 'vue'
import Swiper from '@/views/detail/detailswiper'
Vue.filter('filterPath', (res) => {
  return res.replace('w.h', '256.360')
})
export default {
  // 注册成局部组件
  components: {
    swiper: Swiper
  },
  data() {
    return {
      filminfo: null,
      stars: [111, 222, 333, 444, 666, 788, 999, 1112, 333, 444, 555, 666, 777, 88]
    }
  },
  mounted() {
    // 这里拿到了电影的IP 其实应该去后端根据ID 发送请求 拿到详细信息.
    // 获取动态路由信息
    this.filminfo = this.$route.params.id
    // axios({
    //   url: `https://maoyan.com/films/${this.$route.params.id.id}`
    // }).then((res) => {
    //   console.log('要id获取详情信息', res.data)
    // })
  }
}
</script>
<style lang="scss" scope>
* {
  text-align: center;
}
</style>

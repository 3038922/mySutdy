<template>
  <div class="swiper-container detailswiper">
    <div class="swiper-wrapper">
      <slot></slot>
    </div>
    <!-- 如果需要分页器 -->
    <div class="swiper-pagination"></div>
  </div>
</template>

<script>
// 上课学的不标准写法
import Swiper from 'swiper'
// 还要引入swiper的CSS文件
import 'Swiper/css/swiper.min.css'
export default {
  mounted() {
    /* eslint-disable no-new */
    new Swiper('.detailswiper', {
      sliidesPerView: 3,
      spaceBetween: 30,
      freeMode: true
    })
  }
}
</script>
<style lang="scss" scoped>
.swiper-wrapper {
  img {
    text-align: center;
    width: 200px;
  }
}
</style>

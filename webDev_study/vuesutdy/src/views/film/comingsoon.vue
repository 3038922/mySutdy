<template>
  <div>
    <ul>
      <li v-for="data in $store.state.cominglist" :key="data.filmId">
        <img :src="data.poster" alt="" />
        <h3>{{ data.name }}</h3>
        <p>导演:{{ data.director }}</p>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  mounted() {
    if (this.$store.state.cominglist.length === 0) {
      this.$store.dispatch('getComingListAction')
      // // ajax请求
    } else {
      // 否则自动读取缓存 不需要另外设置
      console.log('使用缓存')
    }
  }
}
</script>

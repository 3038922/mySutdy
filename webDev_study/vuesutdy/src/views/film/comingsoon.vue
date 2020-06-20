<template>
  <div>
    <h2>即将上映</h2>
  </div>
</template>

<script>
export default {
  mounted() {
    if (this.$store.state.cominglist.length === 0) {
      console.log('发送请求')
      this.$stote.dispatch('getComingListAction')
      // // ajax请求
    } else {
      console.log('使用缓存')
    }
  }
}
</script>

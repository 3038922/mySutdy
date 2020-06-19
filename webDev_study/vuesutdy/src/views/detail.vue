<template>
  <div>
    detail
  </div>
</template>

<script>
export default {
  mounted () {
    // 获取动态路由信息
    console.log('要id获取详情信息', this.$route.params.id)
  }
}
</script>

<template>
  <div>
    nowplaying
    <ul>
      <li v-for="data in datalist" :key="data" @click="handleChangePage(data)">
        {{data}}
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  data () {
    return {
      datalist: ['1111', '2222', '3333']
    }
  },
  methods: {
    handleChangePage (id) {
      console.log(id)
      // 编程式导航 ES6 规则``
      // 传统方式 this.$router.push(`/detail/${id}`)
      // 用路由名字导航 更麻烦
      this.$router.push(
        { name: 'ares', params: { id: id } }
      )
    }
  }
}
</script>

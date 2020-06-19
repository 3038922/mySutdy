<template>
  <div>
    nowplaying
    <ul>
      <li v-for="data in datalist" :key="data.filmId" @click="handleChangePage(data)">
        {{ data.name }}
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  data() {
    return {
      datalist: []
    }
  },
  mounted() {
    // ajax请求放这里
    // axios.get('/json/maoyan.json').then((res) => {
    //   console.log(res.data)
    // })
    axios({
      url: 'https://m.maizuo.com/gateway?cityId=620100&pageNum=1&pageSize=10&type=1&k=1917647',
      headers: {
        'X-Client-Info': '{"a":"3000","ch":"1002","v":"5.0.4","e":"1592581289360498079989762"}',
        'X-Host': 'mall.film-ticket.film.list'
      }
    }).then((res) => {
      console.log(res.data)
      this.datalist = res.data.data.films
    })
  },
  methods: {
    handleChangePage(id) {
      console.log(id)
      // 编程式导航 ES6 规则``
      // 传统方式 this.$router.push(`/detail/${id}`)
      // 用路由名字导航 更麻烦
      this.$router.push({ name: 'ares', params: { id: id } })
    }
  }
}
</script>

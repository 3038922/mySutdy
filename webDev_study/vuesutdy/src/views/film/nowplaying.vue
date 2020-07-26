<template>
  <div>
    <ul v-infinite-scroll="loadMore" infinite-scroll-disabled="loading" infinite-scroll-distance="10" infinite-scroll-immediate-check="false">
      <li v-for="data in datalist" :key="data.id" @click="handleChangePage(data)">
        <!-- 记得加个: 不知道啥意思 -->
        <img :src="data.img | filterPath" alt="" />
        <h3>{{ data.nm }}</h3>
        <p>日期:{{ data.rt }}</p>
        <!-- 返回的是数组,用过滤器 -->
        <p>主演:{{ data.star }}</p>
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios'
import Vue from 'vue'
/**
 * 过滤地址 替换 w.h
 */
Vue.filter('filterPath', (res) => {
  return res.replace('w.h', '128.180')
})
/**
 * 过滤原来的那种字符串名字
 */
Vue.filter('actorfilter', (data) => {
  var newlist = data.map((item) => item.name)
  return newlist.join(' ') // 不加join 返回的是字符串
})
export default {
  data() {
    return {
      datalist: [],
      loading: false
    }
  },
  mounted() {
    // ajax请求放这里
    axios.get('/json/maoyan.json').then((res) => {
      this.datalist = res.data.movieList
    })
    // axios({
    //   url: 'https://m.maizuo.com/gateway?cityId=620100&pageNum=1&pageSize=10&type=1&k=1917647',
    //   headers: {
    //     'X-Client-Info': '{"a":"3000","ch":"1002","v":"5.0.4","e":"1592581289360498079989762"}',
    //     'X-Host': 'mall.film-ticket.film.list'
    //   }
    // }).then((res) => {
    //   console.log(res.data)
    //   this.datalist = res.data.data.films
    // })
  },
  methods: {
    handleChangePage(id) {
      console.log(id)
      // 编程式导航 ES6 规则``
      // 传统方式 this.$router.push(`/detail/${id}`)
      // 用路由名字导航 更麻烦
      this.$router.push({ name: 'ares', params: { id: id } })
    },
    loadMore() {
      console.log('到底了')
      this.loading = true
      setTimeout(() => {
        // let last = this.list[this.list.length - 1]
        // for (let i = 1; i <= 10; i++) {
        //   this.list.push(last + i)
        // }
        this.loading = false
      }, 2500)
    }
  }
}
</script>

<style lang="scss" scoped>
ul {
  li {
    overflow: hidden;
    padding: 10px;
    img {
      float: left;
      width: 100px;
    }
  }
}
</style>

<template>
  <div>
    <mt-index-list ref="mylist">
      <mt-index-section v-for="data in datalist" :key="data.index" :index="data.index">
        <!-- 原生mt-cell 不支持click 所以弄个div就好了 -->
        <div @click="handleClick(city.cityId)" v-for="city in data.list" :key="city.cityId">
          <mt-cell :title="city.name"></mt-cell>
        </div>
      </mt-index-section>
    </mt-index-list>
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
    // 下面这行不写就看不到 tabber了 不知道为啥
    this.$refs.mylist.$el.style.height = document.documentElement.clientHeight - 100 + 'px'
    // 发送请求
    axios({
      url: 'https://m.maizuo.com/gateway?k=4390692',
      headers: {
        'X-Client-Info': '{"a":"3000","ch":"1002","v":"5.0.4","e":"1592581289360498079989762","bc":"110100"}',
        'X-Host': ' mall.film-ticket.city.list'
      }
    }).then(res => {
      this.handleCity(res.data.data.cities)
    })
  },
  methods: {
    handleCity(datalist) {
      var letterArr = []
      for (var i = 65; i < 91; i++) {
        letterArr.push(String.fromCharCode(i)) // 收集26个英文字母
      }
      var newList = []
      for (var j = 0; j < letterArr.length; j++) {
        var arr = datalist.filter(item => item.pinyin.substring(0, 1) === letterArr[j].toLowerCase()) // 取出datalist每个城市的首字母
        if (arr.length > 0) {
          newList.push({
            index: letterArr[j],
            list: arr
          })
        }
      }
      this.datalist = newList
    },
    handleClick(id) {
      // 本地缓存 不是Cookies太麻烦
      localStorage.setItem('cityId', id)
      this.$router.push('/cinema') // 跳转
    }
  }
}
</script>

<style lang="scss" scoped>
* {
  background: rgb(36, 41, 46);
  color: black;
}
</style>

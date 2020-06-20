<template>
  <div v-if="datalist" class="cinema">
    <ul>
      <li v-for="data in datalist" :key="data.cinemaId">{{ data.name }}---{{ data.address }}</li>
    </ul>
  </div>
</template>
<script>
import axios from 'axios'
import Bscroll from 'better-scroll'
export default {
  components: {
    // EC6 简化定义
  },
  data() {
    return {
      datalist: null
    }
  },
  mounted() {
    axios({
      url: 'https://m.maizuo.com/gateway?cityId=110100&ticketFlag=1&k=6622498',
      headers: {
        'X-Client-Info': '{"a":"3000","ch":"1002","v":"5.0.4","e":"1592638718370406569541637","bc":"110100"}',
        'X-Host': 'mall.film-ticket.cinema.list'
      }
    }).then((res) => {
      console.log(res.data)
      this.datalist = res.data.data.cinemas
      // 等数据全加载好了 才调用
      this.$nextTick(() => {
        /* eslint-disable no-new */
        new Bscroll('.cinema', {
          scrollbar: { fade: true, interactive: false }
        })
      })
    })
  }
}
</script>
<style lang="scss" scoped>
li {
  height: 50px;
}
.cinema {
  height: 800px;
  overflow: hidden;
  position: relative;
}
</style>

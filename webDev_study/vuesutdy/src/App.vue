<template>
  <div>
    <h2>HDfans新版</h2>
    <tabbar v-if="$store.state.isTabbarShow"></tabbar>
    <!-- 路由容器 -->
    <router-view></router-view>
  </div>
</template>

<script>
// 导入组件
// import axios from 'axios'
// import Navbar from '@/components/Navbar'
// import Sidebar from '@/components/Sidebar'
import Tabbar from '@/components/Tabbar'
// import bus from '@/bus/index.js'
// 注册成全局组件
// 定义vue
// import Vue from 'vue'
// Vue.component('axios', axios)
// Vue.component("sidebar", sidebar);

// ES6 导出
export default {
  data() {
    return {
      datalist: []
    }
  },
  methods: {
    handleAdd() {
      this.datalist.push(this.$refs.mytext.value)
    }
  },
  components: {
    // 局部定义
    // navbar: Navbar,
    // sidebar: Sidebar,
    tabbar: Tabbar
  },
  mounted() {
    // 监听 一定记得加$$$$$$$
    // bus.$on('maizuo', (data) => {
    //   this.isShow = data
    // })
  }
}
</script>

<style lang="scss">
//全局样式
* {
  margin: 0;
  padding: 0;
}
html {
  height: 100%;
}
li {
  list-style: none;
}
</style>

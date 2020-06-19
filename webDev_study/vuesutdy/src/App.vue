<template>
  <div>
    hello vue
    <input type="text"
           ref="mytext" />
    <button @click="handleAdd()">add</button>
    <ul>
      <li v-for="data in datalist"
          :key="data">{{ data }}</li>
    </ul>
    <navbar>
      <button @click="isShow = !isShow">click</button>
    </navbar>
    <sidebar v-show="isShow"></sidebar>
  </div>
</template>

<script>
import Navbar from './components/Navbar'
import Sidebar from './components/Sidebar'
import axios from 'axios'
// 注册成全局组件
// 定义vue
// import Vue from "vue";
// Vue.component("navbar", navbar);
// Vue.component("sidebar", sidebar);

// ES6 导出
export default {
  data () {
    return {
      datalist: [],
      isShow: false
    }
  },
  methods: {
    handleAdd () {
      this.datalist.push(this.$refs.mytext.value)
    }
  },
  components: {
    // 局部定义
    navbar: Navbar,
    sidebar: Sidebar
  },
  mounted () {
    // ajax请求放这里
    axios.get('/json/maoyan.json').then((res) => {
      console.log(res.data)
    })
  }
}
</script>

<style lang="scss">
ul {
  list-style: none;
  li {
    background: orange;
  }
}
</style>

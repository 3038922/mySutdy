<template>
  <div>
    hello vue
    <input
      type='text'
      ref='mytext'
    />
    <button @click='handleAdd()'>add</button>
    <ul>
      <li
        v-for='data in datalist'
        :key='data'
      >{{ data }}</li>
    </ul>
  </div>
</template>

<script>
import navbar from './components/Navbar'
import sidebar from './components/Sidebar'
// 定义vue
import Vue from 'vue'
Vue.component('navbar', navbar)
Vue.component('sidebar', sidebar)
// 注册成全局组件

// ES6 导出
export default {
  data () {
    return {
      datalist: []
    }
  },
  methods: {
    handleAdd () {
      this.datalist.push(this.$refs.mytext.value)
    }
  }
}
</script>

<style lang='scss'>
ul {
  list-style: none;
  li {
    background: orange;
  }
}
</style>

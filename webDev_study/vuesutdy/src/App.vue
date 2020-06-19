<template>
  <div>
    <tabbar></tabbar>hello vue
    <input type="text" ref="mytext" />
    <button @click="handleAdd()">add</button>
    <ul>
      <li v-for="data in datalist" :key="data">{{ data }}</li>
    </ul>
    <!-- <navbar>
      <button @click="isShow = !isShow">click</button>
    </navbar> -->
    <sidebar v-show="isShow"></sidebar>
    <!-- 路由容器 -->
    <router-view></router-view>
  </div>
</template>

<script>
// 导入组件
// import Navbar from '@/components/Navbar'
import Sidebar from '@/components/Sidebar'
import Tabbar from '@/components/Tabbar'

// 注册成全局组件
// 定义vue
// import Vue from "vue";
// Vue.component("navbar", navbar);
// Vue.component("sidebar", sidebar);

// ES6 导出
export default {
  data() {
    return {
      datalist: [],
      isShow: false
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
    sidebar: Sidebar,
    tabbar: Tabbar
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

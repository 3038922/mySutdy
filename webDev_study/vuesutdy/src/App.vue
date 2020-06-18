<template>
  <div>
    hello vue
    <input type="text" ref="mytext" />
    <button @click="handleAdd()">add</button>
    <ul>
      <li v-for="data in datalist" :key="data">{{data}}</li>
    </ul>
  </div>
</template>

<script>
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

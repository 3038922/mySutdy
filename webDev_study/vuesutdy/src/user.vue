<template>
  <div>hello vue</div>
  <input type="text" ref="mytext" />
  <button>add</button>
  <ul>
    <li v-for="data in datalist" :key="data">{{data}}</li>
  </ul>
</template>

<script>
// ES6 导出
export default {
  data(){
    return {  
      datalist:[]
    }
  },
  methods: {
    handleAdd() {
      this.datalist.push(this.)
      console.log("add11111",this.$refs.mytext.value);
    }
  },
};
</script>
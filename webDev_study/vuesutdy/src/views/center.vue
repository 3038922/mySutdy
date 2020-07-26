<template>
  <div>
    <el-row>
      <el-button>center</el-button>
      <el-button type="primary">主要按钮</el-button>
      <el-button type="success">成功按钮</el-button>
      <el-button type="info">信息按钮</el-button>
      <el-button type="warning">警告按钮</el-button>
      <el-button type="danger">危险按钮</el-button>
    </el-row>
    <mt-swipe :auto="4000">
      <mt-swipe-item>1</mt-swipe-item>
      <mt-swipe-item>2</mt-swipe-item>
      <mt-swipe-item>3</mt-swipe-item>
    </mt-swipe>
  </div>
</template>
<script>
const auth = {
  isLogin() {
    return true
  }
}
export default {
  data() {
    return {
      radio: 2,
      value: true,
      dialogVisible: false
    }
  },
  methods: {
    handleClose(done) {
      this.$confirm('确认关闭？')
        .then(_ => {
          done()
        })
        .catch(_ => {})
    }
  },
  // 触发时间要早
  beforeRouteEnter(to, from, next) {
    console.log('局部盘查')
    if (auth.isLogin()) {
      next()
    } else {
      next('/login')
    }
  }
}
</script>
<style>
.mint-swipe {
  height: 200px;
  background: coral;
}
</style>

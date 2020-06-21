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
    <el-radio-group v-model="radio">
      <el-radio :label="1">vue</el-radio>
      <el-radio :label="2">c</el-radio>
      <el-radio :label="3">python</el-radio>
    </el-radio-group>
    <p><el-switch v-model="value" active-color="#13ce66" inactive-color="#ff4949"></el-switch>开关</p>
    <el-alert title="成功提示的文案" type="success" effect="dark"> </el-alert>
    <el-alert title="消息提示的文案" type="info" effect="dark"> </el-alert>
    <el-alert title="警告提示的文案" type="warning" effect="dark"> </el-alert>
    <el-alert title="错误提示的文案" type="error" effect="dark"> </el-alert>

    <!-- 弹框 -->
    <el-button type="text" @click="dialogVisible = true">点击打开 Dialog</el-button>

    <el-dialog title="提示" :visible.sync="dialogVisible" width="30%" :before-close="handleClose">
      <span>这是一段信息</span>
      <span slot="footer" class="dialog-footer">
        <el-button @click="dialogVisible = false">取 消</el-button>
        <el-button type="primary" @click="dialogVisible = false">确 定</el-button>
      </span>
    </el-dialog>
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
        .then((_) => {
          done()
        })
        .catch((_) => {})
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

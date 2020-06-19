<template>
  <div>
    cennter
  </div>
</template>
<script>
const auth = {
  isLogin() {
    return false;
  },
};
export default {
  // 触发时间要早
  beforeRouteEnter(to, from, next) {
    console.log("局部盘查");
    if (auth.isLogin()) {
      next();
    } else {
      next("/login");
    }
  },
};
</script>

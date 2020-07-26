<template>
  <div>
    <ul>
      <!-- 路由 -->
      <router-link to="/film/nowplaying" tag="li" activeClass="active">正在上映</router-link>
      <router-link to="/film/comingsoon" tag="li" activeClass="active">即将上映</router-link>
    </ul>
  </div>
</template>

<style lang="scss" scoped>
ul {
  display: flex; //横向排列
  li {
    flex: 1; //调整横向排列位置
    height: 40px;
    line-height: 40px;
    text-align: center;
    background: rgb(24, 26, 31);
    color: #e1e4e8;
  }
}
.active {
  color: rgb(157, 165, 180);
  border-bottom: 2px solid rgb(157, 165, 180);
}
.fixed {
  position: fixed;
  left: 0px;
  top: 0px;
  width: 100%;
  height: 40px;
  background: rgb(24, 26, 31);
}
</style>

<template>
  <nav>
    <!-- 声明式导航 -->
    <ul>
      <!-- tag='li' 可以替代外面的li -->
      <router-link to='/film'
                   tag="li"
                   activeClass="myactive">film </router-link>
      <router-link to='/center'
                   tag="li"
                   activeClass="myactive">center</router-link>
      <router-link to='/cinema'
                   tag="li"
                   activeClass="myactive">cinema</router-link>
      <!-- #一定要的 淘汰了 -->
      <!-- <li><a href='/#/film'>film</a></li>
      <li><a href='#/cinema'>cinema</a></li>
      <li><a href='#/center'>center</a></li> -->
    </ul>
  </nav>
</template>

<style lang="scss" scope>
.myactive {
  color: red;
}
</style>

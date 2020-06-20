<template>
  <nav>
    <!-- 声明式导航 -->
    <ul>
      <!-- tag='li' 可以替代外面的li -->
      <router-link to="/film" tag="li" activeClass="myactive">
        <!-- 实际没找到合适的iconfont -->
        <i class="iconfont icon-form"></i>
        电影
      </router-link>
      <router-link to="/center" tag="li" activeClass="myactive">电视剧</router-link>
      <router-link to="/cinema" tag="li" activeClass="myactive">音乐</router-link>
      <router-link to="/cinema" tag="li" activeClass="myactive">游戏</router-link>
      <router-link to="/cinema" tag="li" activeClass="myactive">软件</router-link>
      <router-link to="/cinema" tag="li" activeClass="myactive">其他</router-link>
      <router-link to="/cinema" tag="li" activeClass="myactive">小姐姐</router-link>
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
nav {
  position: fixed;
  bottom: 0px;
  left: 0px;
  width: 100%;
  height: 50px;
  background: white;
  ul {
    display: flex;
    li {
      flex: 1;
      line-height: 50px;
      text-align: center;
    }
  }
}
</style>

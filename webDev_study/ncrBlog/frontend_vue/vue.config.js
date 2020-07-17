// // 反向代理
// module.exports = {
//   devServer: {
//     proxy: {
//       '/json': {
//         target: 'http://10.195.106.43:11111',
//         // ws: true,
//         changeOrigin: true
//       }
//     }
//   }
// }

//端口修改
module.exports = {
  devServer: {
    port: 11111
  }
};

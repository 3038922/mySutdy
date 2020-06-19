// // 反向代理
module.exports = {
  devServer: {
    proxy: {
      "/json": {
        target: "http://10.195.106.43:11112",
        // ws: true,
        changeOrigin: true,
      },
    },
  },
};

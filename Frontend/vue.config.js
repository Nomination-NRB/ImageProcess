const { defineConfig } = require("@vue/cli-service");

const path = require("path");
function resolve(dir) {
  return path.join(__dirname, dir);
}

module.exports = defineConfig({
  devServer: {
    // open: true,
    // proxy: {
    //   "/api": {
    //     target: "http://127.0.0.1:8000/api", // 要代理的本地api地址，也可以换成线上测试地址
    //     changeOrigin: true, // 允许跨域
    //     pathRewrite: { "^/api": "" },
    //   },
    // },
  },
  transpileDependencies: true,
  lintOnSave: false,
  configureWebpack: {
    resolve: {
      alias: {
        "@": resolve("src"),
      },
    },
  },
});

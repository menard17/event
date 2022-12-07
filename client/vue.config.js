const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  devServer: {
    proxy: {
      '^/': {
        target: 'http://127.0.0.1:8000/',
        ws: false,
        changeOrigin: true,
      }
    },
    // proxy: {
    //   '^/event': {
    //     target: 'http://127.0.0.1:8000/',
    //     ws: false,
    //     changeOrigin: true,
    //     pathRewrite: {'^/event' : '/event'}
    //   }
    // }
  }
})
import { createApp } from "vue";
import App from "./App.vue";
const app = createApp(App);

// 引入Element Plus
import ElementPlus from "element-plus";
import "element-plus/dist/index.css";
app.use(ElementPlus);
// for in 全局注册图标
// 统一导入el-icon图标
import * as icons from "@element-plus/icons-vue";
for (let iconName in icons) {
  app.component(iconName, icons[iconName]);
}

//Vue Router
import { router } from "./router";
app.use(router);

import store from "./store";
app.use(store);

//全局css
import "@/styles/index.css";

//echarts 封装 https://juejin.cn/post/6995518429952212999#heading-5
import eChartFn from "@/components/chart/index.js";
import ChartPanel from "@/components/chart/index.vue";
app.component(ChartPanel.name, ChartPanel);
app.config.globalProperties.$eChartFn = eChartFn; //vue3原型链设置

app.mount("#app");

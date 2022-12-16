import { createRouter, createWebHashHistory } from "vue-router";

//注册
const home = () => import("@/views/home/index");

//规则
const routes = [
  {
    path: "/",
    name: "home",
    component: home,
  },
];


//导出
export const router = createRouter({
  history: createWebHashHistory(),
  routes: routes
});

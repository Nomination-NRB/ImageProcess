import axios from "axios";
import { ElMessage } from "element-plus";

// 创建axios实例
const service = axios.create({
  baseURL: process.env.VUE_APP_BASE_API, // url = base url + request url
  timeout: 55000, // 默认超时时间
});

let loading = null;

// 添加请求拦截器
service.interceptors.request.use(
  (config) => {
    // 在发送请求之前做些什么
    // 添加X-Token
    // if (config.url.split("/").pop() !== "login") {
    //   let token = await getToken();
    //   console.log(token);
    //   config.headers["X-Token"] = token;
    // }
    return config;
  },
  (error) => {
    // 对请求错误做些什么
    console.log(error); // for debug
    return Promise.reject(error);
  }
);

// 响应拦截器
service.interceptors.response.use(
  (response) => {
    // 2xx 范围内的状态码都会触发该函数。
    if (response.headers["content-type"] === "application/octet-stream")
      return response;

    const res = response.data;
    return res;
  },
  (error) => {
    // 超出 2xx 范围的状态码都会触发该函数。
    console.log("err" + error); // for debug
    ElMessage({
      message: error.message,
      type: "error",
      duration: 5 * 1000,
    });
    return error;
  }
);

export default service;

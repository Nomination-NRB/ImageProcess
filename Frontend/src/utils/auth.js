import Cookies from "js-cookie";
import request from "@/utils/request";

function login(data) {
  return request({
    url: "/login",
    method: "post",
    data,
  });
}

const TokenKey = "vue_admin_template_token";

export async function getToken() {
  if (!Cookies.get(TokenKey)) await setToken();
  return Cookies.get(TokenKey);
}

export async function setToken() {
  const { data: token } = await login({ username: "20183220079", password: "111111" });
  return Cookies.set(TokenKey, token);
}

export function removeToken() {
  return Cookies.remove(TokenKey);
}

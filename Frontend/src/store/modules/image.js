//状态
const state = {
  id: null,
  url: null,
  // token: null,
};

//值修改
const mutations = {
  SET_ID: (state, _id) => {
    state.id = _id;
  },
  SET_URL: (state, url) => {
    state.url = url;
  },
};

//异步操作
const actions = {
  /**
   * @description 第三方登录
   * @param {*} {}
   * @param {*} tokenData
   */
  // async socialLogin({ commit }, tokenData) {
  //   const { data } = await socialLogin(tokenData.backend, tokenData.data);
  //   const token = data["token"];
  //   if (token) {
  //     commit("SET_TOKEN", token);
  //     //access_token置换被访人token
  //     let taRespon = await refreshTokenAndRoles("JZG");
  //     if (!taRespon) throw new Error("refreshTokenAndRoles error");
  //     return new Promise((resolve) => {
  //       resolve(state.roles);
  //     });
  //   } else {
  //     const err = `login核心接口异常,请检查返回JSON格式是否正确,是否正确返回token等..`;
  //     throw new Error(err);
  //   }
  // },
};

export default {
  namespaced: true,
  state,
  mutations,
  actions,
};

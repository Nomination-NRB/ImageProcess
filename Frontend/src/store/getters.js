const getters = {
  id: (state) => state.image.id,
  url: (state) => state.image.url,
  // token: (state) => {
  //   if (state.user.token == null) return null;
  //   else return "JWT " + state.user.token;
  // },
};
export default getters;

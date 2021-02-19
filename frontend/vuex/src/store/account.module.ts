import ApiService from "@/common/api.service";
import {
    GET_PROFILE,
} from "./actions.type";
import {
  SET_ERROR,
  SET_PROFILE
} from "./mutations.type";


const state = {
  errors: null,
  profile: {},
};


const getters = {
  // Get profile
  profile(state: any) {
    return state.profile;
  },
};


const actions = {
  // Get proofile
  [GET_PROFILE](context: any, id: number) {
    return new Promise(resolve => {
      ApiService.get("categories/" + id)
        .then(({ data }) => {
          console.log(data)
          context.commit(SET_PROFILE, data);
          resolve(data);
        })
        .catch(({ response }) => {
          context.commit(SET_ERROR, response);
        });
    });
  },
};


const mutations = {
  // Set errors
  [SET_ERROR](state: any, error: any) {
    state.errors = error;
  },

  // Set profile
  [SET_PROFILE](state: any, categories: any) {
    state.categories = categories;
    state.errors = {};
  },
};


export default {
  state,
  actions,
  mutations,
  getters
};
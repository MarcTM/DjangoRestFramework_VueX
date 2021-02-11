import ApiService from "@/common/api.service";
import {
    GET_CATEGORIES
} from "./actions.type";
import { SET_CATEGORIES, SET_ERROR } from "./mutations.type";


const state = {
  errors: null,
  categories: []
};


const getters = {

  // Get categories
  categories(state: any) {
    return state.categories;
  }

};


const actions = {
  // Get categories
  [GET_CATEGORIES](context: any) {
    return new Promise(resolve => {
      ApiService.get("categories")
        .then(({ data }) => {
          context.commit(SET_CATEGORIES, data);
          resolve(data);
        })
        .catch(({ response }) => {
          context.commit(SET_ERROR, response);
        });
    });
  }
};


const mutations = {
  // Set errors
  [SET_ERROR](state: any, error: any) {
    state.errors = error;
  },

  // Set categories
  [SET_CATEGORIES](state: any, categories: any) {
    state.categories = categories;
    state.errors = {};
  }
};


export default {
  state,
  actions,
  mutations,
  getters
};
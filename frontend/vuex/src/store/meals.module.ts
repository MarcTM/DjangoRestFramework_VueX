import ApiService from "@/common/api.service";
import {
    GET_MEALS
} from "./actions.type";
import { SET_MEALS, SET_ERROR } from "./mutations.type";


const state = {
  errors: null,
  meals: {},
};


const getters = {

  // Get meals
  getMeals(state: any) {
    return state.meals;
  }
  
};


const actions = {
  // Login
  [GET_MEALS](context: any) {
    return new Promise(resolve => {
      ApiService.get("recipes")
        .then(({ data }) => {
          context.commit(SET_MEALS, data);
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

  // Set auth
  [SET_MEALS](state: any, meals: any) {
    state.meals = meals;
    state.errors = {};
  }
};


export default {
  state,
  actions,
  mutations,
  getters
};
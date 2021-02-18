import ApiService from "@/common/api.service";
import {
    GET_MEALS,
    GET_MEAL
} from "./actions.type";
import { SET_MEALS, SET_MEAL, SET_ERROR } from "./mutations.type";


const state = {
  errors: null,
  meals: [],
  meal: {}
};


const getters = {

  // Get meals
  meals(state: any) {
    return state.meals.results;
  },

  // Get total meals
  meals_count(state: any) {
    return state.meals.count;
  },

  // Get meal
  meal(state: any) {
    return state.meal;
  }
  
};


const actions = {
  // Login
  [GET_MEALS](context: any) {
    return new Promise(resolve => {
      ApiService.get("meals")
        .then(({ data }) => {
          console.log(data)
          context.commit(SET_MEALS, data);
          resolve(data);
        })
        .catch(({ response }) => {
          context.commit(SET_ERROR, response);
        });
    });
  },

  [GET_MEAL](context: any, id: number) {
    return new Promise(resolve => {
      ApiService.get("meals/" + id)
        .then(({ data }) => {
          context.commit(SET_MEAL, data);
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

  // Set meals
  [SET_MEALS](state: any, meals: any) {
    state.meals = meals;
    state.errors = {};
  },

  // Set meal
  [SET_MEAL](state: any, meals: any) {
    state.meal = meals;
    state.errors = {};
  }
};


export default {
  state,
  actions,
  mutations,
  getters
};
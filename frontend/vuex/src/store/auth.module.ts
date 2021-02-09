import ApiService from "@/common/api.service";
import JwtService from "@/common/jwt.service";
import {
  LOGIN,
  LOGOUT,
  REGISTER,
  CHECK_AUTH
} from "./actions.type";
import { SET_AUTH, PURGE_AUTH, SET_ERROR } from "./mutations.type";


const state = {
  errors: null,
  user: {},
  isAuthenticated: !!JwtService.getToken()
};


const getters = {
  // Current user
  currentUser(state: any) {
    return state.user;
  },

  // Is authenticated
  isAuthenticated(state: any) {
    return state.isAuthenticated;
  },

  // Get errors
  getErrors(state: any) {
    return state.errors;
  }
};


const actions = {
  // Login
  [LOGIN](context: any, credentials: any) {
    return new Promise(resolve => {
      ApiService.post("users/login", credentials)
        .then(({ data }) => {
          context.commit(SET_AUTH, data.token);
          resolve(data);
        })
        .catch(({ response }) => {
          console.log(response.data.non_field_errors);
          context.commit(SET_ERROR, response.data.non_field_errors);
        });
    });
  },


  // Logout
  [LOGOUT](context: any) {
    context.commit(PURGE_AUTH);
  },


  // Register
  [REGISTER](context: any, credentials: any) {
    return new Promise((resolve, reject) => {
      ApiService.post("users/register", credentials)
        .then(({ data }) => {
          resolve(data);
        })
        .catch(({ response }) => {
          context.commit(SET_ERROR, response.data);
          reject(response);
        });
    });
  },


  // Check auth
  [CHECK_AUTH](context: any) {
    if (JwtService.getToken()) {
      ApiService.get("user")
        .then(({ data }: any) => {
          context.commit(SET_AUTH, data.user);
        })
        .catch(({ response }) => {
          context.commit(SET_ERROR, response.data.errors);
        });
    } else {
      context.commit(PURGE_AUTH);
    }
  }
};


const mutations = {
  // Set errors
  [SET_ERROR](state: any, error: any) {
    state.errors = error;
  },

  // Set auth
  [SET_AUTH](state: any, token: string) {
    state.isAuthenticated = true;
    state.user.token = token;
    state.errors = {};
    JwtService.saveToken(state.user.token);
  },

  // Purge auth
  [PURGE_AUTH](state: any) {
    state.isAuthenticated = false;
    state.user = {};
    state.errors = {};
    JwtService.destroyToken();
  }
};


export default {
  state,
  actions,
  mutations,
  getters
};
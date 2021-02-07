import { createStore } from 'vuex'
import auth from "./auth.module";
import meals from "./meals.module";

const store = createStore({
  modules: {
    auth,
    meals
  }
})

export default store
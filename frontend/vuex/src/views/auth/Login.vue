<template>
  <section class="login">
    <h1>SIGN IN</h1>

      <form class="login-form" @submit.prevent="onSubmit(username, password)">
        <label>Email</label>
        <input type="email" v-model="username" rerquired />

        <label>Password</label>
        <input type="password" v-model="password" required />

        <button class="login-button">SIGN IN</button>
      </form>
  </section>
</template>



<script>
  import {useStore} from 'vuex'
  import { LOGIN } from "@/store/actions.type";

  export default {

    name: "Login",

    data() {
      return {
        username: null,
        password: null
      };
    },

    methods: {
        onSubmit(username, password) {
            this.$store.dispatch(LOGIN, { username, password })
            .then((response) => {
              this.$router.push({ name: "Home"})
            })
            .catch((error) => {console.log(error)})
        }
    },
  }
</script>



<style scoped>
  .login {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 20px;
  }

  .login h1 {
    margin-top: 40px;
    width: 80%;
    padding-bottom: 20px;
    border-bottom: 1px solid grey;
  }

  .login-form {
    margin-top: 40px;
    display: flex;
    flex-direction: column;
    width: 80%;
  }

  form label {
    text-align: left;
    display: block;
    margin-bottom: 10px;
    font-weight: bold;
    text-transform: uppercase;
    font-size: 0.8em;
  }

  form input {
    padding-left: 10px;
    width: 40%;
    height: 50px;
    margin-bottom: 40px;
    border: 1.5px solid grey;
    border-radius: 0;
  }

  .login-button {
    cursor: pointer;
    width: 20%;
    height: 50px;
    color: white;
    background-color: grey;
    border: 1px solid grey;
  }

  .login-button:hover {
    transition: 0.4s;
    background-color: #f7432e;
    border: 1px solid  #f7432e;
  }
</style>
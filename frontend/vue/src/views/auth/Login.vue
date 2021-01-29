<template>
  <section class="login">
    <h1>SIGN IN</h1>

      <form class="login-form">
        <label>Email</label>
        <input type="email" rerquired />

        <label>Password</label>
        <input type="password" required />

        <button class="login-button">SIGN IN</button>
      </form>
  </section>
</template>



<script lang="ts">
  import { Vue } from 'vue-class-component';
  export default class Login extends Vue {}
</script>



<style>
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
    width: 40%;
    height: 50px;
    margin-bottom: 40px;
    border: 1.5px solid grey;
    border-radius: 0;
  }

  .login-button {
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
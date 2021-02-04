<template>
  <section class="register">
    <h1>SIGN UP</h1>

      <form class="register-form" @submit.prevent="onSubmit(username, email, password, rpassword)">
        <label>Username</label>
        <input type="text" v-model="username" rerquired />
        
        <label>Email</label>
        <input type="email" v-model="email" rerquired />

        <label>Password</label>
        <input type="password" v-model="password" rerquired />

        <label>Repeat Password</label>
        <input type="password" v-model="rpassword" required />

        <button class="register-button">SIGN UP</button>
      </form>
  </section>
</template>



<script lang="ts">
  import { Vue } from 'vue-class-component';
  import { REGISTER } from "@/store/actions.type";


  export default class Register extends Vue {

    data() {
      return {
        username: null,
        email: null,
        password: null
      };
    }

    onSubmit(username: string, email: string, password: string, rpassword: string) {
        this.$store
          .dispatch(REGISTER, { username, email, password, rpassword })
          // .then(() => this.$router.push({ name: "home" }));
          // .then(() => {console.log(email + password)})
    }

  }
</script>



<style>
  .register {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 20px;
  }

  .register h1 {
    margin-top: 40px;
    width: 80%;
    padding-bottom: 20px;
    border-bottom: 1px solid grey;
  }

  .register-form {
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

  .register-button {
    width: 20%;
    height: 50px;
    color: white;
    background-color: grey;
    border: 1px solid grey;
  }

  .register-button:hover {
    transition: 0.4s;
    background-color: #f7432e;
    border: 1px solid #f7432e;
  }
</style>
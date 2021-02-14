<template>
  <section class="header">

    <nav class="top-header">
      <div class="top-header-logo">
        <h1>MARC</h1>
      </div>

      <div class="top-header-nav" v-if="!isAuthenticated">
        <router-link to="/login">Login</router-link>
        <router-link to="/register">Register</router-link>
      </div>

      <div v-else class="top-header-nav">
        <a class="logout" @click="logout">Logout</a>
        <router-link to="/cart"><img class="cart-header" src="../../assets/cart.png" /></router-link>
      </div>
    </nav>

    <nav class="main-nav">
      <router-link to="/home">Home</router-link>
      <router-link to="/shop">Shop</router-link>
      <router-link to="/contact">Contact</router-link>
    </nav>

  </section>
</template>



<script>
import { LOGOUT } from "@/store/actions.type";
import { mapGetters } from "vuex";

export default {
    name: "Header",

    computed: {
        ...mapGetters(["isAuthenticated"]),
    },

    methods: {
      logout() {
        this.$store.dispatch(LOGOUT)
      }
    }
}
</script>



<style scoped>
  .header {
    background-color: aquamarine;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    width: 100%;
    box-sizing: border-box;
    padding: 20px 40px 40px 40px;
  }

  .header a {
    display: inline-block;
    margin-left: 20px;
    font-weight: bold;
  }

  .top-header {
    width: 100%;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    margin-bottom: 30px;
  }

  .top-header-logo {
    cursor: pointer;
  }

  a, a:visited, a:active {
    color: black;
    text-decoration: none;
  }

  .top-header-nav {
    display: flex;
    align-items: center;
    text-transform: uppercase;
    text-align: right;
  }

  .main-nav {
    width: 90%;
    font-weight: bold;
    text-transform: uppercase;
  }

  .logout {
    cursor: pointer;
  }

  .cart-header {
    width: 100%;
    height: 30px;
  }
</style>
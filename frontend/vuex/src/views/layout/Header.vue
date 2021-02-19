<template>
  <section class="header">

    <nav class="top-header">
      <div class="top-header-logo">
        <h1>MARC</h1>
      </div>

      <div v-if="!isAuthenticated" class="top-header-nav">
        <router-link to="/login">Login</router-link>
        <router-link to="/register">Register</router-link>
      </div>

      <div v-else class="top-header-nav">
        <router-link to="/account">Your account</router-link>
        <a class="logout" @click="logout">Logout</a>
        <router-link to="/cart"><img class="cart-header" src="../../assets/cart.png" /></router-link>
      </div>
    </nav>

    <nav class="main-nav">
      <router-link to="/home">Home</router-link>
      <router-link to="/shop">Shop</router-link>
    </nav>

  </section>
</template>


<script>
import {
  LOGOUT,
  VALIDATE
} from "@/store/actions.type";
import { mapGetters } from "vuex";

export default {
    name: "Header",

    mounted() {
        this.validate_token()
    },

    computed: {
        ...mapGetters(["isAuthenticated"]),
    },

    methods: {
      validate_token() {
        this.$store.dispatch(VALIDATE)
      },

      logout() {
        this.$store.dispatch(LOGOUT)
        this.$router.push({ name: "Home"})
      }
    }
}
</script>


<style scoped>
  .header {
    color: black;
    background-color: #eee;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    width: 100%;
    box-sizing: border-box;
    padding: 20px 40px 40px 40px;
    border-bottom: 1px solid #bbb;
  }

  .header a {
    display: inline-block;
    margin-left: 20px;
    font-weight: bold;
  }

  .header a:hover {
    transition: 0.2s;
    color: #222;
    border-bottom: 0.8px solid #785fab;
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
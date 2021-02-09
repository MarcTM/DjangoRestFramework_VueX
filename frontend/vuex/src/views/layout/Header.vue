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
        <a class="logout" @click="logout">Logout</a>
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

    mounted() {
      (localStorage.getItem("token"))? this.authed = true : this.authed = false
    },

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
</style>
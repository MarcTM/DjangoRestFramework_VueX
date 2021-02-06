<template>
  <section class="header">

    <nav class="top-header">
      <div class="top-header-logo">
        <h1>MARC</h1>
      </div>

      <div class="top-header-nav">
        <router-link to="/login">Login</router-link>
        <router-link to="/register">Register</router-link>
      </div>
    </nav>

    <nav class="main-nav">
      <router-link to="/home">Home</router-link>
      <router-link to="/shop">Shop</router-link>
      <router-link to="/contact">Contact</router-link>
    </nav>

  </section>
</template>



<script lang="ts">
  export default {
      name: "Header",
  }
</script>



<style>
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
  }

  .top-header {
    width: 100%;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    margin-bottom: 30px;
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
</style>
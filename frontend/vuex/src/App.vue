<template>
  <Header />
  <router-view />
</template>



<script>
  import Header from '@/views/layout/Header.vue';

  export default {
    name: "App",
    components: {
      Header
    }
  }
</script>



<style>
  #app {
    position: absolute;
    top: 0;
    left: 0;
    bottom: 0;
    right: 0;
    
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
  }

  #nav {
    padding: 30px;
  }

  #nav a {
    font-weight: bold;
    color: #2c3e50;
  }

  #nav a.router-link-exact-active {
    color: #42b983;
  }
</style>
<template>
  <div class="home">

    <div class="categories">
      <div v-for="category in categories" class="category">
        <h2 class="category-title">{{ category.title }}</h2>
        <img class="category-image" v-bind:src="category.image" />
      </div>
    </div>
    
  </div>
</template>



<script>
import { defineComponent } from 'vue';
import { GET_CATEGORIES } from "@/store/actions.type";
import { mapGetters } from "vuex";

export default defineComponent({
  name: 'Home',

  mounted() {
      this.getCategories()
  },

  computed: {
      ...mapGetters(["categories"]),
  },

  methods: {
      getCategories() {
          this.$store.dispatch(GET_CATEGORIES).then((response) => console.log(response))
      }
  },
});
</script>



<style scoped>
.categories {
  width: 100%;
  box-sizing: border-box;
  padding: 50px;

  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
}

.category {
  cursor: pointer;
  color: black;
  padding: 10px;
  margin: 10px;

  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.category:hover {
  transition: 0.4s;
  background-color: #eeefff;
}

.category-title {
  transition: 0.4s;
  color: #3a3a3a;
  text-transform: capitalize;
  font-size: 1.2em;
  margin-bottom: 5px;
}

img {
  width: 75%;
  height: 220px;
}
</style>
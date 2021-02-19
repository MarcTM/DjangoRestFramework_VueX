<template>
  <div class="home">
    <div class="home-categories">
      <div class="categories">
        <div v-for="category in categories" class="category" @click="getCategory(category.id)">
          <h2 class="category-title">{{ category.title }}</h2>
          <img class="category-image" v-bind:src="category.image" />
        </div>
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

  data () {
    return {
      value: 0
    }
  },

  mounted() {
      this.getCategories()
  },

  computed: {
      ...mapGetters(["categories"]),
  },

  methods: {
      getCategories() {
          this.$store.dispatch(GET_CATEGORIES).then((response) => console.log(response))
      },

      getCategory(id) {
        this.$router.push({ name: "Category", params: {id: id}});
      }
  },
});
</script>



<style scoped>
.categories {
  background-color: #eee;
  width: 100%;
  box-sizing: border-box;
  padding: 50px;
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
}

.category {
  cursor: pointer;
  padding: 10px;
  margin: 10px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.category-title {
  color: black;
  text-transform: capitalize;
  font-size: 1.2em;
  margin-bottom: 5px;
}

img {
  width: 75%;
  height: 220px;
}
</style>
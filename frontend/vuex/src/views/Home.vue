<template>
  <div class="home">
    HOME
    <div class="categories">
      <div v-for="category in categories" class="category">
        {{ category.title }}
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
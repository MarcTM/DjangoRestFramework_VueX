<template>
  <div class="meals-list">
        <div v-for="meal in meals">
            <MealPreview v-bind:meal="meal" />
        </div>
  </div>
</template>



<script>
import MealPreview from '@/components/MealPreview.vue';
import store from '@/store';
import { GET_MEALS } from "@/store/actions.type";
import { mapGetters } from "vuex";

export default {
    name: 'MealsList',

    components: {
        MealPreview
    },

    mounted() {
        this.getMeals()
    },

    computed: {
        ...mapGetters(["meals"]),
    },

    methods: {
        getMeals() {
            this.$store.dispatch(GET_MEALS)
        }
    },
};
</script>



<style scoped>
.meals-list {
    width: 100%;
    box-sizing: border-box;
    padding: 10px;

    display: grid;
    grid-template-columns: 1fr 1fr 1fr 1fr;
}
</style>
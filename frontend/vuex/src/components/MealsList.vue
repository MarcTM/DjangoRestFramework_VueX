<template>
  <div class="meals-list">
    MEALS LIST
    <button @click="getMeals()">PROVA</button>
    
    <div v-for="meal in meals">
        <MealPreview />
    </div>
  </div>
</template>



<script lang="ts">
import MealPreview from '@/components/MealPreview.vue';
import store from '@/store';
import { GET_MEALS } from "@/store/actions.type";

export default {
    name: 'MealsList',

    components: {
        MealPreview
    },

    data () {
        return {
            meals: [
                {title: "primera"},
                {title: "segona"}
            ]
        }
    },

    beforeCreate() {
        store
            .dispatch(GET_MEALS)
            .then((response: any) => {console.log(response)})
            .catch((response: any) => {console.log(response)})
    },

    methods: {
        getMeals() {
            console.log(store.getters.getMeals)
            // store
            //     .dispatch(GET_MEALS)
            //     .then((response: any) => {console.log(response)})
            //     .catch((response: any) => {console.log(response)})
        }
    },
};
</script>



<style scoped>
</style>

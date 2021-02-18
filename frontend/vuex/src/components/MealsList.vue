<template>
  <div class="meals-list">
        <form class="search-meals" @submit.prevent="onSubmit(search)">
            <input type="text" v-model="search" placeholder="Search..." />
            <button class="search-button">Search</button>
        </form>

        <div class="meals">
            <div v-for="meal in meals">
                <MealPreview v-bind:meal="meal" />
            </div>
        </div>

        <div class="meals-pagination">
            <button @click="previous" class="pagination-previous">PREVIOUS</button>
            <button @click="next" class="pagination-next">NEXT</button>
        </div>
  </div>
</template>



<script>
import MealPreview from '@/components/MealPreview.vue';
import store from '@/store';
import { GET_MEALS, GET_MEALS_BY_SEARCH } from "@/store/actions.type";
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
        ...mapGetters(["meals_count"])
    },

    methods: {
        getMeals() {
            this.$store.dispatch(GET_MEALS)
        },

        onSubmit(search) {
            console.log(search);
            (!search)
            ? this.$store.dispatch(GET_MEALS)
            : this.$store.dispatch(GET_MEALS_BY_SEARCH, `?search=${search}`)
        },

        previous() {
            alert("previous")
        },

        next() {
            alert("next")
        }
    },
};
</script>



<style scoped>
.meals-list {
    width: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
}

.meals-list .meals {
    width: 100%;
    box-sizing: border-box;
    padding: 10px;

    display: grid;
    grid-template-columns: 1fr 1fr 1fr 1fr;
}

.search-meals {
    box-sizing: border-box;
    width: 100%;
    padding: 20px;
    display: flex;
    justify-content: space-between;
    margin-bottom: 20px;
}

.search-meals input {
    box-sizing: border-box;
    width: 80%;
    height: 50px;
    margin-right: 20px;

    border: 1px solid black;
    padding: 5px 10px;
}

.search-meals button {
    width: 20%;
    border: 1px solid grey;
    background-color: black;
    color: white;
}

input:focus,
select:focus,
textarea:focus,
button:focus {
    outline: none;
}

.meals-pagination {
    margin: 50px 0px;
    width: 90%;
    display: flex;
    justify-content: center;
}

.pagination-previous {
    width: 15%;
    margin-right: 20px;
    height: 50px;
    border: 1px solid black;
    border-radius: 8px;
    background-color: #eeeeff;
    color: black;
}

.pagination-previous:hover {
    transition: 0.4s;
    background-color: #ddddee;
}

.pagination-next {
    width: 15%;
    margin-right: 20px;
    height: 50px;
    border: 1px solid black;
    border-radius: 8px;
    background-color: #eeeeff;
    color: black;
}

.pagination-next:hover {
    transition: 0.4s;
    background-color: #ddddee;
}
</style>
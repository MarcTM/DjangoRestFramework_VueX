<template>
  <div @click="details(meal.id)" class="meal-preview">
    <img class="meal-image" v-bind:src="meal.image" />
    <p class="meal-title">{{ meal.title }}</p>
    <label class="meal-price">6.5 €</label>
  </div>
</template>



<script>
export default {
    name: 'MealPreview',

    props: [
      'meal'
    ],

    methods: {
      details(id) {
        this.$router.push({ name: "Meal", params: {id: id}});
      }
    }
}
</script>



<style scoped>
.meal-preview {
  cursor: pointer;
  color: black;
  padding: 10px;
  margin: 10px;

  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.meal-preview:hover {
  transition: 0.4s;
    background-color: #eeefff;
}

.meal-image:hover + .meal-title {
  color: #ef5555;
}

.meal-title {
  transition: 0.4s;
  color: #3a3a3a;
  text-transform: capitalize;
  font-size: 1.2em;
  margin-bottom: 5px;
}

.meal-price {
  font-weight: bold;
}

img {
  width: 90%;
  height: 200px;
}
</style>
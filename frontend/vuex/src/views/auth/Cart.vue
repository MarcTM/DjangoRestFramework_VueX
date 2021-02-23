<template>
  <section class="cart">
    <h1 class="cart-title">YOUR CART</h1>

    <div v-if="cart.meals" class="your-cart">
      <div v-for="meal in cart.meals" @click="details(meal.id)" class="cart-product">
        <img class="meal-image" v-bind:src="meal.image" />
        <p class="meal-title">{{ meal.title }}</p>
        <label class="meal-price">{{ meal.price }} €</label>
      </div>
    </div>

    <div v-else>
      <h1>NOTHING IN YOUR CART</h1>
    </div>

  </section>
</template>


<script>
import {
    GET_CART
} from "@/store/actions.type";
import { mapGetters } from 'vuex';

export default {
  name: "Cart",

  mounted() {
      this.get_cart()
  },

  computed: {
      ...mapGetters(["cart"]),
  },

  methods: {
      get_cart() {
          this.$store.dispatch(GET_CART)
      },

      details(id) {
        this.$router.push({ name: "Meal", params: {id: id}});
      }
  },
}
</script>


<style scoped>
.cart {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    padding: 50px;
}

.cart-title {
    text-align: left;
    width: 100%;
    color: black;
    padding-bottom: 5px;
    border-bottom: 1px solid black;
    margin-bottom: 50px;
}

.your-cart {
    width: 100%;
    box-sizing: border-box;
    padding: 10px;

    display: grid;
    grid-template-columns: 1fr 1fr 1fr 1fr;
}

.cart-product {
  cursor: pointer;
  color: black;
  padding: 10px;
  margin: 10px;

  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.cart-product:hover {
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
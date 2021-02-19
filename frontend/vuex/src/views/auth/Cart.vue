<template>
  <section class="cart">
    <h1 class="cart-title">YOUR CART</h1>

    <div class="your-cart">
    your cart
    </div>
  </section>
</template>


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
}
</style>
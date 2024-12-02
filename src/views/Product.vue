<template>
  <div class="page-product">
    <div class="columns is-multiline">
      <!-- Product Image and Description -->
      <div class="column is-9">
        <figure class="image mb-6">
          <img :src="product.get_image" alt="Product Image">
        </figure>
        <h1 class="title">{{ product.name }}</h1>
        <p>{{ product.description }}</p>
      </div>

      <!-- Product Information and Add to Cart -->
      <div class="column is-3">
        <h2 class="subtitle">Information</h2>
        <p><strong>Price: </strong>${{ product.price }}</p>

        <div class="field has-addons mt-6">
          <div class="control">
            <input
              type="number"
              class="input"
              min="1"
              v-model="quantity"
              @input="validateQuantity"
            >
          </div>
          <div class="control">
            <button class="button is-dark" @click="addToCart">Add to cart</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { toast } from "bulma-toast";

export default {
  name: "Product",
  data() {
    return {
      product: {},
      quantity: 1,
    };
  },
  mounted() {
    this.fetchProduct();
  },
  methods: {
    // Fetch product details based on route params
    async fetchProduct() {
      this.$store.commit("setIsLoading", true);

      const { category_slug, product_slug } = this.$route.params;

      try {
        const response = await axios.get(
          /api/v1/products/${category_slug}/${product_slug}
        );
        this.product = response.data;
        document.title = ${this.product.name} | Djackets;
      } catch (error) {
        console.error("Error fetching product:", error);
      } finally {
        this.$store.commit("setIsLoading", false);
      }
    },

    // Validate quantity input
    validateQuantity() {
      if (isNaN(this.quantity) || this.quantity < 1) {
        this.quantity = 1;
      }
    },

    // Add product to the cart
    addToCart() {
      this.validateQuantity();

      const item = {
        product: this.product,
        quantity: this.quantity,
      };

      this.$store.commit("addToCart", item);

      toast({
        message: "The product was added to the cart",
        type: "is-success",
        dismissible: true,
        pauseOnHover: true,
        duration: 2000,
        position: "bottom-right",
      });
    },
  },
};
</script>
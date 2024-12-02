<template>
  <div class="home">
     <div class="home">
    <section class="hero is-medium is-dark mb-6">
        <div class="hero-body has-text-centered">
            <p class="title mb-6">
                Welcome to Djacket
            </p>
            <p class="subtitle">
                The best jacket store online
            </p>
        </div>
    </section>
  </div>

  <div class="columns is-multiline">
      <div class="column is-12">
          <h2 class="is-size-2 has-text-centered">Latest products</h2>
   </div>

   <ProductBox 
  v-for="product in latestProducts"
  :key="product.id"
  :product="product" />

      <div v-for="product in latestProducts" :key="product.id" class="box">
      <figure class="image mb-4">
        <img :src="product.get_thumbnail" alt="Product Thumbnail" />
      </figure>
      <h3 class="is-size-4">{{ product.name }}</h3>
      <p class="is-size-6 has-text-grey">${{ product.price }}</p>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: 'Home',
  data() {
    return {
      latestProducts: []
    }
  },
  components: {
    
  },
  mounted() {
    this.getLatestProducts()
  },
  methods: {
    async getLatestProducts() {
      this.$store.commit('setIsLoading', true)

      await axios
        .get('/api/v1/latest-products/')
        .then(response => {
          this.latestProducts = response.data
        })
        .catch(error => {
          console.log(error)
        })

      this.$store.commit('setIsLoading', false)
    }
  }
}
</script>


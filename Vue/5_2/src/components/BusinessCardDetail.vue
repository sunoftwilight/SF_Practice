<template>
  <div class="businessCard" v-for="businessCard in businessCards">
    <h4>이름 : {{ businessCard.name }}</h4>
    <p>직함 : {{ businessCard.title }}</p>
  </div>
</template>

<script setup>
defineProps({
  businessCards: Array,
})
</script>

<style scoped>
.businessCard {
  border: 1px solid rgb(194, 194, 194);
  background-color: rgb(226, 226, 226);
  text-align: center;
  width: 45%;
  padding: 10px;
  margin: 10px;
}
</style>
<template>
  <div>
    <h1>가수 목록</h1>
    <div class="singer-list" v-for="singer in singers">
      <!-- <span v-for="singer in singers"> -->
      <SingerDetail />
      <!-- </span> -->
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import SingerDetail from '@/components/singers/SingerDetail.vue';

const singers = ref([
  {name: 'Adele'},
  {name: 'Maroon5'},
  {name: 'Dua Lipa'},
])
</script>

<style scoped>
h1 {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-top: 70px;
  margin-bottom: 10px;
  color: orangered;
}

.singer-list {
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
}
</style>
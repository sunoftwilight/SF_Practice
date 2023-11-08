<template>
  <div>
    <h1>가수 목록</h1>
    <div class="singer-list">
      <SingerDetail />
      <SingerDetail />
    </div>
  </div>
</template>

<script setup>
import SingerDetail from '@/components/singers/SingerDetail.vue';
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
}
</style>
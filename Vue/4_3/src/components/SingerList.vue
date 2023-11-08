<template>
  <div>
    <h2>가수 목록</h2>
    <SingerDetail />
  </div>
</template>

<script setup>
import SingerDetail from '@/components/singers/SingerDetail.vue';
</script>

<style scoped>
h2 {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-top: 70px;
}
</style>
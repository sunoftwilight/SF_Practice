<template>
  <h3>보유 명함 목록</h3>
  <article class="card">
    <BusinessCardDetail :businessCards="businessCards" />
  </article>
</template>

<script setup>
import { ref } from 'vue'
import BusinessCardDetail from '@/components/BusinessCardDetail.vue'

const businessCards = ref([
  {name: '일론 머스크', title: '테슬라 테크노킹'},
  {name: '래리 엘리슨', title: '오라클 창업주'},
  {name: '빌 게이츠', title: '마이크로소프트 공동창업주'},
  {name: '래리 페이지', title: '구글 공동창업주'},
  {name: '세르게이 브린', title: '구글 공동창업주'},
])
</script>

<style scoped>
.card {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
}
</style>
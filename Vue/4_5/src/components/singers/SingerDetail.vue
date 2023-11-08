<template>
  <div class="card">
    <!-- <span> -->
    <h1>가수 이름</h1>
    <img src="@/assets/singer.jpg" alt="가수 사진">
    <p>가수 소개글</p>
    <SingerAlbum />
    <!-- </span> -->
  </div>
</template>

<script setup>
import SingerAlbum from '@/components/singers/SingerAlbum.vue';
</script>

<style scoped>
.card {
  /* display: inline-block; */
  justify-content: center;
  margin: 20px;

  display: flex;
  flex-direction: column;
  align-items: center;
  border: 1px solid;
  width: 40%;
  flex-wrap: wrap;
}

/* span {
  display: flex;
  flex-direction: column;
  align-items: center;
  border: 1px solid;
} */

img {
  width: 200px;
  border-radius: 50%;
}
</style>
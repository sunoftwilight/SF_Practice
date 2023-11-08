<template>
  <div class="card">
    <span>
      <h1>가수 이름</h1>
      <img src="@/assets/singer.jpg" alt="가수 사진">
      <p>가수 소개글</p>
    </span>
  </div>
</template>

<script setup>

</script>

<style scoped>
.card {
  display: inline-block;
  width: 40%;
  justify-content: center;
  margin: 20px;
}

span {
  display: flex;
  flex-direction: column;
  align-items: center;
  border: 1px solid;
}

img {
  width: 200px;
  border-radius: 50%;
}
</style>
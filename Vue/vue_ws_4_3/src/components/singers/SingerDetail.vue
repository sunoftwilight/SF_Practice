<template>
  <div class="detailbox">
    <span>
      <h2>가수 이름</h2>
      <img src="@/assets/singer.jpg" alt="가수 사진">
      <p>가수 소개글</p>
    </span>
  </div>
</template>

<script setup>

</script>

<style scoped>
.detailbox {
  display: flex;
  justify-content: center;
}

span {
  display: flex;
  flex-direction: column;
  align-items: center;
  border: 2px solid;
  width: 90%;
}

img {
  width: 200px;
  border-radius: 50%;
}
</style>
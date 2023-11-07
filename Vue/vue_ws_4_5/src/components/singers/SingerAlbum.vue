<template>
  <div class="singer-album">
    <p class="album-name">앨범제목</p>
    <p class="song-name">노래 목록 1</p>
    <p class="song-name">노래 목록 2</p>
    <p class="song-name">노래 목록 3</p>
  </div>
</template>

<script setup>

</script>

<style scoped>
.singer-album {
  display: flex;
  flex-direction: column;
  align-items: center;
  border: 1px solid rgb(185, 185, 185);
  width: 60%;
  border-radius: 10%;
  background-color: rgb(236, 236, 236);
  margin-bottom: 20px;
  box-shadow: 0px 0px 10px 1px #8d8c8c;
}

.album-name {
  font-weight: bold;
}

.song-name {
  color: orange;
  margin-top: 2px;
}
</style>
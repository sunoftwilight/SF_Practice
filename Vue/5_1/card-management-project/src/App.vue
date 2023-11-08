<template>
  <div class="app">

    <header>
      <h1>명함 관리 페이지</h1>
    </header>
    
    <main>
      <p>명함을 관리하는 페이지입니다. 여기에 명함 목록이 표시됩니다.</p>
      <article></article>
    </main>

    <footer>
      <p>ⓒ 2023 My Business Cards</p>
    </footer>
    
  </div>
</template>

<script setup>

</script>

<style scoped>
.app {
  display: flex;
  flex-direction: column;
  align-items: center;
}

h1 {
  border: 1px solid rgb(40, 118, 182);
  padding-left: 20px;
  padding-right: 20px;
  padding-top: 50px;
  padding-bottom: 50px;
  margin: 0;
  background-color: rgb(40, 118, 182);
  color: white;
}

main {
  text-align: center;
  /* min-height: 100vh; */
}

footer {
  /* display: inline; */
  text-align: center;
  position: fixed;
  /* display: inline; */
  background-color: rgb(230, 230, 230);
  bottom: 0;
  width: 100%;
}
</style>
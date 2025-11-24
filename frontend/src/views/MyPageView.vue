<template>
  <TheNavbar />

  <div class="page">
    <h1 class="title">마이페이지</h1>
    <p class="desc">
      로그인 / 내가 남긴 리뷰, 나중에 붙일 예정 👀<br />
      지금은 간단히 레이아웃만 잡아두었어요.
    </p>

    <section class="box">
      <h2>내 최근 리뷰</h2>
      <p>로그인 기능 구현 후, 내가 남긴 리뷰를 여기서 모아서 볼 수 있게 만들면 좋아요.</p>
    </section>

    <section class="box">
      <h2>찜한 영화 / 봤어요</h2>
      <p>지금 만든 “보고싶어요 / 봤어요” 버튼이랑 연동해서 보여주면 딱.</p>
    </section>
  </div>
</template>

<script setup>
import TheNavbar from '@/components/layout/TheNavbar.vue'
</script>

<style scoped>
.page {
  padding: 80px 60px 40px;
  color: white;
}

.title {
  font-size: 28px;
  margin-bottom: 10px;
}

.desc {
  margin-bottom: 20px;
  opacity: 0.9;
}

.box {
  margin-top: 20px;
  padding: 16px 18px;
  border-radius: 8px;
  background: #181818;
}
</style>

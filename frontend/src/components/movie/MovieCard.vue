<template>
  <RouterLink :to="`/movies/${movie.id}`" class="movie-card">
    <img :src="posterSrc" alt="포스터" />


    <div class="overlay">
      <h4>{{ movie.title }}</h4>
      <p>⭐ {{ movie.avg_score ?? '평점 없음' }}</p>
    </div>
  </RouterLink>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  movie: {
    type: Object,
    required: true,
  },
})

const posterSrc = computed(() => {
  const url = props.movie.poster_url
  if (!url) return ''  // 필요하면 기본 이미지 경로 넣어도 됨

  // TMDB처럼 http/https로 시작하면 그대로 사용
  if (url.startsWith('http')) {
    return url
  }
  // 예전처럼 /media/posters/... 같이 상대경로면 백엔드 주소 붙이기
  return `http://127.0.0.1:8000${url}`
})
</script>


<style scoped>
.movie-card {
  position: relative;
  min-width: 220px;
  height: 330px;
  background: #141414;
  border-radius: 10px;
  overflow: hidden;
  transition: transform 0.3s ease, z-index 0.3s ease;
  cursor: pointer;
  display: block; /* 클릭 영역 전체 확보 */
}

.movie-card:hover {
  transform: scale(1.1);
  z-index: 10;
  background: #141414;
}

.movie-card img {
  width: 100%;
  height: 100%;
  background: #141414;
  object-fit: cover;
}

.overlay {
  position: absolute;
  bottom: 0;
  width: 100%;
  padding: 10px;
  background: linear-gradient(transparent, black);
}
</style>

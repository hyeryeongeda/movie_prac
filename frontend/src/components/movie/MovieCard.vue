<template>
  <RouterLink :to="`/movies/${movie.id}`" class="movie-card">
    <img :src="`http://127.0.0.1:8000${movie.poster_url}`" alt="" />

    <div class="overlay">
      <h4>{{ movie.title }}</h4>
      <p>⭐ {{ movie.avg_score ?? '평점 없음' }}</p>
    </div>
  </RouterLink>
</template>

<script setup>
defineProps({
  movie: Object,
})
</script>

<style scoped>
.movie-card {
  position: relative;
  min-width: 220px;
  height: 330px;
  border-radius: 10px;
  overflow: hidden;
  transition: transform 0.3s ease, z-index 0.3s ease;
  cursor: pointer;
  display: block; /* 클릭 영역 전체 확보 */
}

.movie-card:hover {
  transform: scale(1.1);
  z-index: 10;
}

.movie-card img {
  width: 100%;
  height: 100%;
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

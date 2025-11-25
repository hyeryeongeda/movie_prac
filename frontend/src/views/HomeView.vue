<template>
  <TheNavbar />

  <!-- 히어로 영역 -->
 <div class="hero" v-if="heroMovie":style="heroBgStyle">
    <div class="hero-content">
      <h1>{{ heroMovie.title }}</h1>
      <p>{{ heroMovie.overview }}</p>
      <button class="detail-btn" @click="goDetail(heroMovie.id)">
        자세히 보기
      </button>
    </div>
  </div>

  <div v-else class="hero hero-empty">
    <div class="hero-content">
      <h1>영화가 아직 없습니다</h1>
      <p>Django admin에서 Movie를 추가해보세요.</p>
    </div>
  </div>

  <!-- 영화 Row 섹션 -->
  <MovieRow
    v-if="movies.length > 0"
    title="지금 인기 영화"
    :movies="movies"
  />

  <MovieRow
    v-if="movies.length > 0"
    title="내 취향 추천"
    :movies="movies"
  />
</template>

<script setup>
import { useRouter } from 'vue-router'
import TheNavbar from '@/components/layout/TheNavbar.vue'
import MovieRow from '@/components/movie/MovieRow.vue'
import api from '@/api/axios'
import { ref, onMounted, computed } from 'vue'

const heroBgStyle = computed(() => {
  if (!heroMovie.value || !heroMovie.value.poster_url) {
    return {}
  }
  const url = heroMovie.value.poster_url
  const finalUrl = url.startsWith('http') ? url : `http://127.0.0.1:8000${url}`
  return {
    backgroundImage: `url(${finalUrl})`,
  }
})


const movies = ref([])
const heroMovie = ref(null)
const router = useRouter()

const goDetail = (id) => {
  router.push(`/movies/${id}`)
}

onMounted(async () => {
  try {
    const res = await api.get('movies/')
    const data = res.data
    const list = Array.isArray(data) ? data : data.results ?? []

    movies.value = list
    heroMovie.value = movies.value[0] || null

    console.log('API 응답:', data)
    console.log('movies:', movies.value)
  } catch (error) {
    console.error('영화 불러오기 실패:', error)
  }
})
</script>

<style scoped>
.hero {
  height: 70vh;
  background-size: cover;
  background-position: center;
  display: flex;
  align-items: center;
}

.hero-empty {
  background-color: #141414;
}

.hero-content {
  margin-left: 60px;
  max-width: 500px;
}

.hero h1 {
  font-size: 48px;
}

.hero p {
  margin: 20px 0;
  opacity: 0.9;
}

.detail-btn {
  background: #e50914;
  padding: 12px 20px;
  font-size: 16px;
  border-radius: 5px;
}
</style>

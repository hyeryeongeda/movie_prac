<template>
  <TheNavbar />

  <!-- 1) 로딩 중 -->
  <div v-if="loading" class="detail-page">
    로딩중...
  </div>

  <!-- 2) 영화 데이터가 있을 때 -->
  <div v-else-if="movie" class="detail-page">
    <!-- ✅ 1. 상세 영역 -->
    <div class="detail-hero">
      <div class="poster">
        <img :src="`http://127.0.0.1:8000${movie.poster_url}`" alt="" />
      </div>

      <div class="info">
        <h1>{{ movie.title }}</h1>
        <p class="meta">
          {{ movie.release_year }} · {{ movie.country }}
        </p>

        <RatingStar v-model="myRating" />
        <WatchButtons />

        <!-- 기존 overview -->
        <p class="overview">
          {{ movie.overview }}
        </p>

        <!-- ✅ 리뷰 작성 + 목록 -->
        <ReviewForm
          :movie-id="movie.id"
          @created="onReviewCreated"
        />

        <ReviewList
          :movie-id="movie.id"
          :reload-key="reviewsReloadKey"
        />

      </div>
    </div>

    <!-- ✅ 2. 아래에 비슷한 영화 -->
    <section class="similar-section" v-if="similarMovies.length > 0">
      <MovieRow
        title="비슷한 영화 추천"
        :movies="similarMovies"
      />
    </section>
  </div>

  <!-- 3) 영화 못 불러왔을 때 -->
  <div v-else class="detail-page">
    영화를 불러오지 못했습니다.
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import ReviewForm from '@/components/review/ReviewForm.vue'
import ReviewList from '@/components/review/ReviewList.vue'

import MovieRow from '@/components/movie/MovieRow.vue'
import TheNavbar from '@/components/layout/TheNavbar.vue'
import RatingStar from '@/components/movie/RatingStar.vue'
import WatchButtons from '@/components/movie/WatchButtons.vue'
import api from '@/api/axios'
const reviewsReloadKey = ref(0)
const onReviewCreated = () => {
  reviewsReloadKey.value++
}

const similarMovies = ref([])
const route = useRoute()
const movie = ref(null)
const loading = ref(true)
const myRating = ref(0)

onMounted(async () => {
  try {
    const id = route.params.id

    const res = await api.get(`movies/${id}/`)
    movie.value = res.data

    const similarRes = await api.get(`movies/${id}/similar/`)
    const similarData = similarRes.data
    const similarList = Array.isArray(similarData)
      ? similarData
      : similarData.results ?? []

    similarMovies.value = similarList
  } catch (error) {
    console.error('영화 불러오기 실패:', error)
  } finally {
    loading.value = false
  }
})
</script>

<style scoped>
.detail-page {
  padding: 40px 60px;
  color: white;
}

.detail-hero {
  display: flex;
  align-items: center;
  gap: 60px;
  padding: 40px 20px;
}

.poster img {
  width: 260px;
  border-radius: 8px;
  object-fit: cover;
}

.info {
  max-width: 600px;
}

.meta {
  margin-top: 10px;
  opacity: 0.8;
}

.overview {
  margin-top: 20px;
  line-height: 1.6;
}

.similar-section {
  padding: 40px 0;
}
</style>

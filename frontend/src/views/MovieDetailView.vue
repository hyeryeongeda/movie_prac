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
        <img :src="posterSrc" />
      </div>

      <div class="info">
        <h1>{{ movie.title }}</h1>
        <p class="meta">{{ movie.release_year }} · {{ movie.country }}</p>

        <!-- ✅ 장르 태그 -->
        <div class="genre-chips" v-if="movie.genres?.length">
          <span
            v-for="genre in movie.genres"
            :key="genre.id"
            class="chip"
          >
            {{ genre.name }}
          </span>
        </div>

        <!-- ✅ 감독/배우 정보 -->
        <div class="people" v-if="directors.length || actors.length">
          <p v-if="directors.length">
            <strong>감독</strong>
            <span
              v-for="d in directors"
              :key="d.id"
              class="person-name"
            >
              {{ d.person.name }}
            </span>
          </p>

          <p v-if="actors.length">
            <strong>출연</strong>
            <span
              v-for="a in actors"
              :key="a.id"
              class="person-name"
            >
              {{ a.person.name }}
              <span v-if="a.character_name"> ({{ a.character_name }})</span>
            </span>
          </p>
        </div>

        <RatingStar v-model="myRating" />
        <WatchButtons :movie-id="movie.id" />

        <p class="overview">{{ movie.overview }}</p>

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
import { ref, onMounted, watch, computed } from 'vue'
import { useRoute } from 'vue-router'
import MovieRow from '@/components/movie/MovieRow.vue'
import TheNavbar from '@/components/layout/TheNavbar.vue'
import RatingStar from '@/components/movie/RatingStar.vue'
import WatchButtons from '@/components/movie/WatchButtons.vue'
import ReviewForm from '@/components/review/ReviewForm.vue'
import ReviewList from '@/components/review/ReviewList.vue'
import api from '@/api/axios'

const route = useRoute()

const movie = ref(null)
const similarMovies = ref([])
const loading = ref(true)
const myRating = ref(0)

const directors = ref([])
const actors = ref([])

// 포스터 URL 계산
const posterSrc = computed(() => {
  if (!movie.value?.poster_url) return ''
  const url = movie.value.poster_url
  return url.startsWith('http')
    ? url
    : `http://127.0.0.1:8000${url}`
})

// 영화 가져오기
const fetchMovie = async (id) => {
  console.log("📌 Fetch Movie:", id)
  loading.value = true

  try {
    const res = await api.get(`movies/${id}/`)
    console.log("📌 API Response movie:", res.data)

    movie.value = res.data

    // casts 존재 여부 체크
    if (!movie.value.casts) {
      console.warn("⚠ movie.casts 없음!")
      directors.value = []
      actors.value = []
    } else {
      directors.value = movie.value.casts.filter(c => c.role === 'director')
      actors.value = movie.value.casts.filter(c => c.role === 'actor')
    }

    // similar
    const s = await api.get(`movies/${id}/similar/`)
    console.log("📌 API Response similar:", s.data)

    similarMovies.value = Array.isArray(s.data) ? s.data : (s.data.results ?? [])

  } catch (err) {
    console.error("❌ fetchMovie ERROR:", err)
  } finally {
    loading.value = false
  }
}

onMounted(() => {
  fetchMovie(route.params.id)
})

watch(() => route.params.id, (newId, oldId) => {
  console.log("📌 route changed:", oldId, "→", newId)
  if (newId) fetchMovie(newId)
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
.genre-chips {
  margin-top: 8px;
  margin-bottom: 8px;
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
}

.chip {
  padding: 4px 8px;
  border-radius: 999px;
  background: #262626;
  font-size: 12px;
}

.people {
  margin-top: 8px;
  margin-bottom: 12px;
  font-size: 13px;
}

.people p {
  margin: 2px 0;
}

.person-name + .person-name::before {
  content: ' · ';
}

</style>

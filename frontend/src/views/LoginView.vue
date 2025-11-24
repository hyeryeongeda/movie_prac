<template>
  <TheNavbar />

  <div class="page">
    <div class="card">
      <h1>로그인</h1>

      <form @submit.prevent="onSubmit">
        <input
          v-model="username"
          type="text"
          placeholder="아이디"
          required
        />
        <input
          v-model="password"
          type="password"
          placeholder="비밀번호"
          required
        />
        <button type="submit">로그인</button>
      </form>

      <p class="error" v-if="error">{{ error }}</p>

      <p class="hint">
        아직 계정이 없다면, 나중에 회원가입 페이지도 추가할 수 있어요 🙂
      </p>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import TheNavbar from '@/components/layout/TheNavbar.vue'
import { useAuth } from '@/stores/auth'

const username = ref('')
const password = ref('')
const error = ref('')
const router = useRouter()
const auth = useAuth()

const onSubmit = async () => {
  error.value = ''
  try {
    await auth.login(username.value, password.value)
    await auth.fetchMe()
    router.push('/')   // 로그인 후 홈으로
  } catch (e) {
    console.error(e)
    error.value = '로그인에 실패했습니다. 아이디/비밀번호를 확인해 주세요.'
  }
}
</script>

<style scoped>
.page {
  padding-top: 80px;
  display: flex;
  justify-content: center;
}

.card {
  width: 320px;
  background: #181818;
  padding: 24px 26px;
  border-radius: 10px;
  color: white;
}

h1 {
  margin-bottom: 16px;
  font-size: 22px;
}

form {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

input {
  padding: 8px 10px;
  border-radius: 4px;
  border: 1px solid #444;
  background: #111;
  color: white;
}

button {
  margin-top: 10px;
  padding: 8px 10px;
  border-radius: 4px;
  border: none;
  background: #e50914;
  color: white;
  cursor: pointer;
}

.error {
  margin-top: 10px;
  color: #ff8080;
  font-size: 14px;
}

.hint {
  margin-top: 14px;
  font-size: 12px;
  opacity: 0.8;
}
</style>

// src/stores/auth.js
import { reactive, computed } from 'vue'
import api from '@/api/axios'

const state = reactive({
  access: localStorage.getItem('access'),
  refresh: localStorage.getItem('refresh'),
  user: null,
})

const isAuthenticated = computed(() => !!state.access)

async function login(username, password) {
  const res = await api.post('auth/login/', { username, password })
  state.access = res.data.access
  state.refresh = res.data.refresh

  localStorage.setItem('access', state.access)
  localStorage.setItem('refresh', state.refresh)

  await fetchMe()
}

async function fetchMe() {
  if (!state.access) return
  try {
    const res = await api.get('auth/me/')
    state.user = res.data
  } catch (error) {
    console.error('내 정보 가져오기 실패:', error)
  }
}

function logout() {
  state.access = null
  state.refresh = null
  state.user = null
  localStorage.removeItem('access')
  localStorage.removeItem('refresh')
}

async function register(username, password) {
  await api.post('auth/register/', { username, password })
  // 회원가입 후 바로 로그인 시켜도 되고, 로그인 페이지로 보내도 되고
}

export function useAuth() {
  return {
    state,
    isAuthenticated,
    login,
    logout,
    register,
    fetchMe,
  }
}

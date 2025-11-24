// src/api/axios.js
import axios from 'axios'

const api = axios.create({
  baseURL: 'http://127.0.0.1:8000/api/v1/',
})

// 매 요청마다 access 토큰 있으면 Authorization 헤더로 추가
api.interceptors.request.use((config) => {
  const token = localStorage.getItem('access')
  if (token) {
    config.headers.Authorization = `Bearer ${token}`
  }
  return config
})

export default api

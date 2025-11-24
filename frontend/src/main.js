// main.js 예시
import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import { useAuth } from '@/stores/auth'

const app = createApp(App)
app.use(router)

const auth = useAuth()
auth.fetchMe()   // 저장된 토큰이 있으면 유저 정보 미리 가져오기

app.mount('#app')

<template>
  <div class="watch-buttons">
    <button
      :class="{ active: wished }"
      @click="toggleWish"
    >
      🤍 보고싶어요
    </button>

    <button
      :class="{ active: watched }"
      @click="toggleWatched"
    >
      ✅ 봤어요
    </button>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const wished = ref(false)
const watched = ref(false)

const toggleWish = () => {
  wished.value = !wished.value
}

const toggleWatched = () => {
  watched.value = !watched.value
}
</script>

<style scoped>
.watch-buttons {
  display: flex;
  gap: 10px;
  margin-top: 15px;
}

button {
  background: transparent;
  border: 1px solid #666;
  padding: 8px 14px;
  border-radius: 20px;
  color: white;
  cursor: pointer;
}

button.active {
  background: #e50914;
  border-color: #e50914;
}
</style>

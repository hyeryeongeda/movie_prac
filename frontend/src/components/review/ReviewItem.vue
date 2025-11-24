<template>
  <div class="review-item">
    <div class="top">
      <strong class="author">{{ review.author || '익명' }}</strong>
      <span class="date">{{ formattedDate }}</span>
    </div>
    <p class="content">{{ review.content }}</p>
  </div>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  review: {
    type: Object,
    required: true,
  },
})

const formattedDate = computed(() => {
  if (!props.review.created_at) return ''
  return props.review.created_at.slice(0, 10)
})
</script>

<style scoped>
.review-item {
  padding: 10px 0;
  border-bottom: 1px solid #333;
}

.top {
  display: flex;
  justify-content: space-between;
  margin-bottom: 4px;
}

.author {
  font-size: 14px;
}

.date {
  font-size: 12px;
  opacity: 0.7;
}

.content {
  font-size: 14px;
  line-height: 1.4;
}
</style>

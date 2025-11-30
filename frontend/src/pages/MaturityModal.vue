<template>
  <div class="modal-overlay" v-if="isVisible">
    <div class="modal-content">
      <h2>Are you over 18?</h2>
      <p>This section contains mature content. Please confirm your age to proceed.</p>
      <div class="modal-actions">
        <button @click="confirmAge(true)">Yes, I am 18+</button>
        <button @click="confirmAge(false)">No, I am not 18+</button>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
export default {
  props: {
    isVisible: {
      type: Boolean,
      required: true
    }
  },
  methods: {
    confirmAge(isOver18: boolean) {
      this.$emit('ageConfirmed', isOver18);
    }
  }
};
</script>

<style scoped>
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.7);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
}

.modal-content {
  background: var(--primary-bg-gradient);
  padding: 2em;
  border-radius: 10px;
  text-align: center;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
  max-width: 500px;
  color: var(--text-color);
}

.modal-content h2 {
  margin-top: 0;
  color: var(--header-color);
}

.modal-content p {
  margin-bottom: 1.5em;
  font-size: 1.1em;
}

.modal-actions button {
  background-color: var(--button-bg-color);
  color: var(--button-text-color);
}
</style>
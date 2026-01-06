<template>
  <!-- Overlay -->
  <div
    class="fixed inset-0 bg-black bg-opacity-40 z-50 flex items-center justify-center"
  >
    <!-- Modal box -->
    <div
      class="bg-white rounded-xl shadow-2xl w-full max-w-2xl p-6 relative overflow-y-auto max-h-[90vh]"
    >
      <h2 class="text-xl font-bold mb-4">Provider Modal</h2>

      <!-- Form container -->
      <el-form
        :model="form"
        label-width="120px"
        label-position="left"
        class="w-full"
      >
        <slot />
      </el-form>

      <!-- Action buttons -->
      <div class="flex justify-end gap-2 mt-6">
        <el-button type="primary" @click="$emit('save')">Save</el-button>
        <el-button @click="$emit('close')">Close</el-button>
      </div>
    </div>
  </div>
</template>

<script setup>
defineProps({
  form: { type: Object, required: true },
});
</script>

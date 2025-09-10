<template>
  <!-- Overlay làm mờ nền -->
  <div
    class="fixed inset-0 bg-black bg-opacity-40 z-50 flex items-center justify-center"
  >
    <!-- Modal box -->
    <div
      class="bg-white rounded-xl shadow-2xl w-full max-w-2xl p-6 relative overflow-y-auto max-h-[90vh]"
    >
      <h2 class="text-xl font-bold mb-4">Provider Modal</h2>

      <!-- Form bên trong -->
      <el-form
        :model="form"
        label-width="120px"
        label-position="left"
        class="w-full"
      >
        <el-form-item label="Name">
          <el-input v-model="form.name" placeholder="Enter provider name" />
        </el-form-item>

        <el-form-item label="Description">
          <el-input
            v-model="form.description"
            type="textarea"
            placeholder="Enter description"
            rows="3"
          />
        </el-form-item>

        <el-form-item label="Enable">
          <el-switch v-model="form.is_enabled" />
        </el-form-item>
      </el-form>

      <!-- Action buttons -->
      <div class="flex justify-end gap-2 mt-6">
        <el-button type="primary" @click="$emit('save', form)">Save</el-button>
        <el-button @click="$emit('close')">Close</el-button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";

const form = ref({
  name: "",
  description: "",
  is_enabled: false,
});
</script>

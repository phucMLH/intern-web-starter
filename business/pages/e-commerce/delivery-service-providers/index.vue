<template>
  <div class="p-6">
    <h1 class="text-2xl font-bold mb-4">Delivery Service Providers</h1>

    <!-- Nút thêm mới -->
    <button
      class="bg-blue-500 text-white px-4 py-2 rounded mb-4"
      @click="$router.push('/e-commerce/delivery-service-providers/new')"
    >
      + Add Provider
    </button>

    <div class="border rounded bg-white shadow">
      <!-- Trạng thái loading -->
      <div v-if="loading" class="text-center py-6 text-gray-500">
        Loading...
      </div>

      <!-- Khi load xong -->
      <table v-else class="table-auto w-full border-collapse">
        <thead>
          <tr class="bg-gray-200">
            <th class="px-4 py-2 border">ID</th>
            <th class="px-4 py-2 border">Name</th>
            <th class="px-4 py-2 border">Default</th>
            <th class="px-4 py-2 border">Actions</th>
          </tr>
        </thead>

        <!-- Có dữ liệu -->
        <tbody v-if="providers.length > 0">
          <tr
            v-for="p in providers"
            :key="p.id"
            class="hover:bg-gray-50 transition"
          >
            <td class="border px-4 py-2">{{ p.id }}</td>
            <td class="border px-4 py-2">{{ p.name }}</td>
            <td class="border px-4 py-2 text-center">
              <span v-if="p.is_default">✅</span>
            </td>
            <td class="border px-4 py-2">
              <router-link
                class="text-blue-600 hover:underline"
                :to="`/e-commerce/delivery-service-providers/${p.id}`"
              >
                Edit
              </router-link>
            </td>
          </tr>
        </tbody>

        <!-- Không có dữ liệu -->
        <tbody v-else>
          <tr>
            <td colspan="4" class="text-center py-6 text-gray-500">
              No providers yet
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import axios from "axios";

// ✅ Để có sidebar
definePageMeta({
  layout: "ecommerce",
});

const providers = ref([]);
const loading = ref(true);

onMounted(async () => {
  try {
    const res = await axios.get(
      "http://127.0.0.1:8008/api/v1/ecommerce/delivery-service-providers"
    );
    console.log("API response:", res.data);
    providers.value = res.data;
  } catch (err) {
    console.error("API error:", err);
  } finally {
    loading.value = false; // ✅ luôn tắt loading sau khi gọi xong
  }
});
</script>

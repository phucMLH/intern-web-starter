<template>
  <div class="p-6">
    <h1 class="text-2xl font-bold mb-4">Delivery Service Providers</h1>

    <!-- Nút thêm mới -->
    <button
      class="bg-red-500 text-white px-4 py-2 rounded mb-4 hover:bg-blue-600 transition"
      @click="$router.push('/e-commerce/delivery-service-providers/new')"
    >
      + Add Provider
    </button>

    <div class="border rounded bg-white shadow overflow-x-auto">
      <!-- Trạng thái loading -->
      <div v-if="loading" class="text-center py-6 text-gray-500">
        Loading...
      </div>

      <!-- Khi load xong -->
      <table v-else class="table-auto w-full border-collapse">
        <thead class="bg-gray-200 sticky top-0">
          <tr>
            <th class="px-4 py-2 border">ID</th>
            <th class="px-4 py-2 border">Name</th>
            <th class="px-4 py-2 border">Default</th>
            <th class="px-4 py-2 border">Actions</th>
          </tr>
        </thead>

        <tbody>
          <!-- Nếu không có dữ liệu -->
          <tr v-if="providers.length === 0">
            <td colspan="4" class="text-center py-6 text-gray-500">
              No providers yet
            </td>
          </tr>

          <!-- Có dữ liệu -->
          <tr
            v-for="p in providers"
            :key="p.id"
            class="hover:bg-gray-50 transition"
            v-else
          >
            <!-- Hiển thị ID rút gọn + nút copy -->
            <td class="border px-4 py-2 flex items-center gap-2">
              <span>{{ p.id.slice(0, 8) }}...</span>
              <button
                class="text-gray-600 hover:text-blue-600"
                @click="copyId(p.id)"
              >
                <DocumentCopy class="w-4 h-4" />
              </button>
            </td>

            <td class="border px-4 py-2">{{ p.name }}</td>
            <td class="border px-4 py-2 text-center">
              <Check
                v-if="p.is_default"
                class="w-5 h-5 text-green-600 inline-block"
              />
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
      </table>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import axios from "axios";
import { useRouter } from "vue-router";
import { useOauthStore } from "@/stores/oauth";

// Import icons từ Element Plus
import { Check, DocumentCopy } from "@element-plus/icons-vue";

definePageMeta({
  layout: "ecommerce",
});

const providers = ref([]);
const loading = ref(true);

const oauthStore = useOauthStore();
const router = useRouter();

onMounted(async () => {
  try {
    const accessToken = oauthStore.tokenInfo?.access_token;
    if (!accessToken) {
      router.push("/login");
      return;
    }

    const res = await axios.get(
      "http://127.0.0.1:8008/api/v1/ecommerce/delivery-service-providers",
      {
        headers: {
          Authorization: `Bearer ${accessToken}`,
        },
      }
    );

    providers.value = Array.isArray(res.data)
      ? res.data
      : res.data.results || [];
  } catch (err) {
    console.error("API error:", err);
  } finally {
    loading.value = false;
  }
});

// Hàm copy UUID full vào clipboard
function copyId(id) {
  navigator.clipboard
    .writeText(id)
    .then(() => {
      alert("Copied: " + id);
    })
    .catch((err) => {
      console.error("Failed to copy: ", err);
    });
}
</script>

<template>
  <div class="flex flex-row w-full justify-center pt-20">
    <ProviderModal @save="handleSave" @close="handleClose">
      <el-form-item :label="t('Name')" prop="name">
        <el-input v-model="form.name" />
      </el-form-item>

      <el-form-item :label="t('Config (JSON)')" prop="config">
        <el-input
          type="textarea"
          v-model="form.config"
          placeholder='{"api_url": "...", "api_key": "..."}'
          rows="6"
        />
      </el-form-item>

      <el-form-item :label="t('Default')">
        <el-switch v-model="form.is_default" />
      </el-form-item>
    </ProviderModal>
  </div>
</template>

<script setup>
import { reactive } from "vue";
import { useRouter } from "vue-router";
import ProviderModal from "@/components/ecommerce/provider/ProviderModal.vue";
import DeliveryServiceProviderService from "@/services/e-commerce/deliveryServiceProvider";

definePageMeta({
  layout: "ecommerce",
});

const { t } = useI18n();

const form = reactive({
  name: "",
  config: "{}",
  is_default: false,
});

const router = useRouter();

const handleSave = async () => {
  try {
    await DeliveryServiceProviderService.create({
      name: form.name,
      config: form.config,
      is_default: form.is_default,
    });
    // Hiển thị thông báo thành công nếu muốn
    router.push("/e-commerce/delivery-service-providers");
  } catch (err) {
    // Xử lý lỗi, có thể hiển thị thông báo lỗi
    console.error("Create provider failed", err);
  }
};

const handleClose = () => {
  router.push("/e-commerce/delivery-service-providers");
};
</script>

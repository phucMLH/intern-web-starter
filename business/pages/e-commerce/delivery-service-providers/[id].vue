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
import { reactive, onMounted } from "vue";
import { useRoute, useRouter } from "vue-router";
import ProviderModal from "@/components/ecommerce/provider/ProviderModal.vue";
import DeliveryServiceProviderService from "@/services/e-commerce/deliveryServiceProvider";

definePageMeta({
  layout: "ecommerce",
});

const { t } = useI18n();
const route = useRoute();
const router = useRouter();

const form = reactive({
  name: "",
  config: "{}",
  is_default: false,
});

// Load dữ liệu khi edit
onMounted(async () => {
  if (route.params.id) {
    try {
      const res = await DeliveryServiceProviderService.retrieve(
        route.params.id
      );
      console.log(data);
      form.name = data.name;
      form.config = JSON.stringify(data.config, null, 2); // format JSON
      form.is_default = data.is_default;
    } catch (err) {
      console.error("Load provider failed", err);
    }
  }
});

const handleSave = async () => {
  try {
    await DeliveryServiceProviderService.update(route.params.id, {
      name: form.name,
      config: form.config,
      is_default: form.is_default,
    });
    router.push("/e-commerce/delivery-service-providers");
  } catch (err) {
    console.error("Update provider failed", err);
  }
};

const handleClose = () => {
  router.push("/e-commerce/delivery-service-providers");
};
</script>

<template>
  <div class="flex flex-row w-full justify-center pt-20">
    <FormModal
      :service="DeliveryServiceProviderService"
      :title="t('Add Delivery Service Provider')"
      redirect="/e-commerce/delivery-service-providers"
    >
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
    </FormModal>
  </div>
</template>

<script setup>
import { reactive } from "vue";
import FormModal from "@/components/FormModal.vue";
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
</script>

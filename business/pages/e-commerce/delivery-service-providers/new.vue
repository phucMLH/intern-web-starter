<template>
  <div class="flex flex-row w-full justify-center pt-20">
    <ProviderModal :form="form" @save="handleSave" @close="handleClose">
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
import axios from "axios";
import ProviderModal from "@/components/ecommerce/provider/ProviderModal.vue";
import { useOauthStore } from "@/stores/oauth";

definePageMeta({
  layout: "ecommerce",
});

const { t } = useI18n();
const router = useRouter();
const oauthStore = useOauthStore();

const form = reactive({
  name: "",
  config: "",
  is_default: false,
});

const handleSave = async () => {
  try {
    const accessToken = oauthStore.tokenInfo?.access_token;
    if (!accessToken) {
      router.push("/login");
      return;
    }

    const payload = {
      name: form.name,
      is_default: form.is_default,
    };

    if (form.config && form.config.trim() !== "") {
      try {
        payload.config = JSON.parse(form.config);
      } catch (e) {
        alert("Config phải là JSON hợp lệ");
        return;
      }
    }

    await axios.post(
      "http://127.0.0.1:8008/api/v1/ecommerce/delivery-service-providers",
      payload,
      {
        headers: {
          Authorization: `Bearer ${accessToken}`,
          "Content-Type": "application/json",
        },
      }
    );

    router.push("/e-commerce/delivery-service-providers");
  } catch (err) {
    console.error("Create provider failed", err);
  }
};

const handleClose = () => {
  router.push("/e-commerce/delivery-service-providers");
};
</script>

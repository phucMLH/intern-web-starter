<template>
  <div class="flex flex-row w-full justify-center pt-20">
    <PaginationTable
      :page-size="5"
      :service="DeliveryServiceProviderService"
      :canDeleteItems="canEdit"
      :canEditItems="canEdit"
      :canAddItems="canEdit"
      :multipleSelect="canEdit"
      :allowExportToExcel="true"
      :allowExportToJson="true"
      :searchable="true"
    >
      <el-table-column prop="name" :label="t('Name')" min-width="200" />
      <el-table-column prop="is_default" :label="t('Default')" min-width="120">
        <template #default="scope">
          <span v-if="scope.row.is_default">✅</span>
          <span v-else>❌</span>
        </template>
      </el-table-column>
      <el-table-column
        prop="updated_at"
        :label="t('Updated_at')"
        min-width="180"
      >
        <template #default="scope">
          {{ formatDateTime(scope.row.updated_at) }}
        </template>
      </el-table-column>
    </PaginationTable>
  </div>
</template>

<script setup>
import DeliveryServiceProviderService from "@/services/e-commerce/deliveryServiceProvider";
import PaginationTable from "@/components/PaginationTable.vue";
import { formatDateTime } from "~/utils/time";
import { useOauthStore } from "@/stores/oauth";

definePageMeta({
  layout: "ecommerce",
});

const { t } = useI18n();
const oauthStore = useOauthStore();

const canEdit = computed(() =>
  oauthStore.hasOneOfScopes(["ecommerce:delivery_service_providers:edit"])
);
</script>

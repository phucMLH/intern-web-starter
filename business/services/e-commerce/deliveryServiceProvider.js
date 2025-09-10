import ApiService from "@/services/api";

export default {
  list(params) {
    return ApiService.get("/api/delivery-service-providers/", { params });
  },
  retrieve(id) {
    return ApiService.get(`/api/delivery-service-providers/${id}/`);
  },
  create(data) {
    return ApiService.post("/api/delivery-service-providers/", data);
  },
  update(id, data) {
    return ApiService.put(`/api/delivery-service-providers/${id}/`, data);
  },
  delete(id) {
    return ApiService.delete(`/api/delivery-service-providers/${id}/`);
  },
};

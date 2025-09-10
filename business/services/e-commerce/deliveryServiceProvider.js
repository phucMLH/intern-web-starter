import ApiService from "@/services/api";

const baseUrl = "http://127.0.0.1:8008/api/v1/ecommerce/delivery-service-providers";

export default {
  create(data) {
    return ApiService.post(baseUrl, data, {
      headers: { "Content-Type": "application/json" },
    });
  },
  getAll() {
    return ApiService.get(baseUrl);
  },
  getById(id) {
    return ApiService.get(`${baseUrl}/${id}`);
  },
  update(id, data) {
    return ApiService.put(`${baseUrl}/${id}`, data, {
      headers: { "Content-Type": "application/json" },
    });
  },
  delete(id) {
    return ApiService.delete(`${baseUrl}/${id}`);
  },
};

import axios from "axios";
import JwtService from "@/common/jwt.service";
import { API_URL } from "@/common/config";

const ApiService = {
  // Query
  query(resource: any, params: any) {
    return axios.get(resource, params).catch((error) => {
      throw new Error(`[RWV] ApiService ${error}`);
    });
  },

  // Get
  get(resource: any, slug = "") {
    return axios.get(`${API_URL}/${resource}/${slug}`).catch((error) => {
      throw new Error(`[RWV] ApiService ${error}`)
    });
  },

  // Post
  post(resource: any, params: any) {
    axios.post('URL')
      .then(function (response) {
        alert (response.data);
      })
      .catch(function (error) {
        alert(error);
    });
    return axios.post(`${resource}`, params);
  },

  // Update
  update(resource: any, slug: any, params: any) {
    return axios.put(`${resource}/${slug}`, params);
  },

  // Put
  put(resource: any, params: any) {
    return axios.put(`${resource}`, params);
  },

  // Delete
  delete(resource: any) {
    return axios.delete(resource).catch((error) => {
      throw new Error(`[RWV] ApiService ${error}`);
    });
  }
};

export default ApiService;
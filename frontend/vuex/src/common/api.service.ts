import axios, { AxiosRequestConfig } from "axios";
import JwtService from "@/common/jwt.service";
import { API_URL } from "@/common/config";


const headers = {
  "Authorization": `Token ${JwtService.getToken()}`,
}

const ApiService = {
  // Query
  query(resource: string, params: any) {
    return axios.get(`${API_URL}/${resource}?${params}`).catch((error) => {
      throw new Error(`[RWV] ApiService ${error}`);
    });
  },

  // Get
  get(resource: string, context=false) {
    if (context) {
      return axios.get(`${API_URL}/${resource}`, {headers}).catch((error) => {
        throw new Error(`[RWV] ApiService ${error}`)
      });
    } else {
      return axios.get(`${API_URL}/${resource}`).catch((error) => {
        throw new Error(`[RWV] ApiService ${error}`)
      });
    }
  },

  // Post
  post(resource: string, params: any) {
    return axios.post(`${API_URL}/${resource}`, params);
  },

  // Update
  update(resource: string, slug: string, params: any) {
    return axios.put(`${resource}/${slug}`, params);
  },

  // Put
  put(resource: string, params: any) {
    return axios.put(`${resource}`, params);
  },

  // Delete
  delete(resource: string) {
    return axios.delete(resource).catch((error) => {
      throw new Error(`[RWV] ApiService ${error}`);
    });
  }
};

export default ApiService;
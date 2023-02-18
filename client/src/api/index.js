import axios from "axios";

const API = axios.create({ baseURL: "http://127.0.0.1:5000" });
export const fetchPost = (page) => API.get(`/posts?page=${page}`);
export const createUser = (data) => API.post("/auth/signup", data);
export const loginUser = (data) => API.post("/auth/login", data);
export const fetchSinglePostDetails = (postId) =>
  API.get(`posts/post-details/${postId}`);

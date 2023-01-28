import axios from "axios";

const URL = "http://127.0.0.1:5000";

export const fetchPost = () => axios.get(`${URL}/posts/`);

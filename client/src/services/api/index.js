import axios from "axios";

const url = "http://127.0.0.1:5000";

export const fetchMessage = () => axios.get("/api/hello");

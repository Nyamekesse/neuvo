import { configureStore } from "@reduxjs/toolkit";
import userReducer from "../features/user/userSlice";
import postReducer from "../features/post/postSlice";
import alertReducer from "../features/alerts/alertSlice";
const store = configureStore({
  reducer: {
    user: userReducer,
    post: postReducer,
    alert: alertReducer,
  },
});

export default store;

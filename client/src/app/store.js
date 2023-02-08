import { configureStore } from "@reduxjs/toolkit";
import userReducer from "../features/auth/authenticationSlice";
import postReducer from "../features/post/postSlice";
import alertReducer from "../features/alerts/alertSlice";
const store = configureStore({
  reducer: {
    authentication: userReducer,
    post: postReducer,
    alert: alertReducer,
  },
});

export default store;

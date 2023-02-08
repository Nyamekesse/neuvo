import { configureStore } from "@reduxjs/toolkit";
import authenticationReducer from "../features/auth/authenticationSlice";
import postReducer from "../features/post/postSlice";
import alertReducer from "../features/alerts/alertSlice";
const store = configureStore({
  reducer: {
    authentication: authenticationReducer,
    post: postReducer,
    alert: alertReducer,
  },
});

export default store;

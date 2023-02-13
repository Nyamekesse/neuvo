import { combineReducers, configureStore } from "@reduxjs/toolkit";
import authenticationReducer from "../features/auth/authenticationSlice";
import postReducer from "../features/post/postSlice";
import alertReducer from "../features/alerts/alertSlice";
import storage from "redux-persist/lib/storage";
import { persistReducer } from "redux-persist";

const persistConfig = {
  key: "root",
  storage,
};

const reducer = combineReducers({
  authentication: authenticationReducer,
  post: postReducer,
  alert: alertReducer,
});

const persistedReducer = persistReducer(persistConfig, reducer);
const store = configureStore({
  reducer: persistedReducer,
});

export default store;

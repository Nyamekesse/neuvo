import { combineReducers, configureStore } from "@reduxjs/toolkit";
import authenticationReducer from "../features/auth/authenticationSlice";
import postReducer from "../features/post/postSlice";
import alertReducer from "../features/alerts/alertSlice";
import storage from "redux-persist/lib/storage";
import { persistReducer } from "redux-persist";

const persistConfig = {
  key: "root",
  storage,
  version: 1,
  blacklist: ["authentication", "alert"],
};

const reducer = combineReducers({
  authentication: authenticationReducer,
  post: postReducer,
  alert: alertReducer,
});

const persistedReducer = persistReducer(persistConfig, reducer);
const store = configureStore({
  reducer: persistedReducer,
  middleware: (getDefaultMiddleware) =>
    getDefaultMiddleware({
      serializableCheck: {
        ignoredActions: ["persist/PERSIST"],
      },
    }),
});

export default store;

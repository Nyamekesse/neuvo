import { createAsyncThunk, createSlice } from "@reduxjs/toolkit";
import { createUser, loginUser } from "../../api";
import { displayAlert } from "../alerts/alertSlice";
import { ACCESS_TOKEN, ERROR, REFRESH_TOKEN, SUCCESS } from "../../constants";
import { localStorageSet } from "../../utils";
export const signup = createAsyncThunk(
  "authentication/signup",
  async (data, thunkAPI) => {
    try {
      const res = await createUser(data);
      if (res.status === 200 && res.statusText === "OK") {
        const { data } = res;
        if (data.success) {
          thunkAPI.dispatch(
            displayAlert({ text: data.message, severity: SUCCESS })
          );

          return data;
        } else {
          thunkAPI.dispatch(
            displayAlert({ text: data.message, severity: ERROR })
          );
        }
      }
    } catch (error) {
      thunkAPI.dispatch(displayAlert({ text: error.message, severity: ERROR }));
      return error.message;
    }
  }
);

export const login = createAsyncThunk(
  "authentication/login",
  async (data, thunkAPI) => {
    try {
      const res = await loginUser(data);
      if (res.status === 200 && res.statusText === "OK") {
        const { data } = res;
        if (data.success) {
          thunkAPI.dispatch(
            displayAlert({ text: data.message, severity: SUCCESS })
          );
          console.log(data);
          // localStorage.setItem("profile", JSON.stringify({ ...data?.profile }));
          return data;
        } else {
          thunkAPI.dispatch(
            displayAlert({ text: data.message, severity: ERROR })
          );
        }
      }
    } catch (error) {
      thunkAPI.dispatch(displayAlert({ text: error.message, severity: ERROR }));
      return error.message;
    }
  }
);

const initialAuthState = {
  isLoading: false,
  profile: {},
  isLoggedIn: false,
  success: false,
};
const authenticationSlice = createSlice({
  name: "authentication",
  initialState: initialAuthState,
  reducers: {
    logout: () => {
      return initialAuthState;
    },
  },
  extraReducers: (builder) => {
    builder.addCase(signup.pending, (state) => {
      state.isLoading = true;
    });
    builder.addCase(signup.fulfilled, (state, { payload }) => {
      state.isLoading = false;
      state.success = payload?.success;
    });
    builder.addCase(signup.rejected, (state) => {
      state.isLoading = false;
    });
    builder.addCase(login.pending, (state) => {
      state.isLoading = true;
    });
    builder.addCase(login.fulfilled, (state, { payload }) => {
      state.isLoading = false;
      state.profile = payload?.profile;
      state.success = payload?.success;
      state.isLoggedIn = true;
      localStorageSet(ACCESS_TOKEN, payload?.access_token);
      localStorageSet(REFRESH_TOKEN, payload?.refresh_token);
    });
    builder.addCase(login.rejected, (state) => {
      state.isLoading = false;
    });
  },
});

export const { logout } = authenticationSlice.actions;
export default authenticationSlice.reducer;

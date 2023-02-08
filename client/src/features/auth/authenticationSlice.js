import { createAsyncThunk, createSlice } from "@reduxjs/toolkit";
import { createUser, loginUser } from "../../api";
import { displayAlert } from "../alerts/alertSlice";
import { ERROR, SUCCESS } from "../../constants";
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
          localStorage.setItem("profile", JSON.stringify({ ...data?.profile }));
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
  isLoading: true,
  newUser: "",
  message: "",
  profile: {},
  accessToken: "",
  refreshToken: "",
  isLoggedIn: false,
  success: false,
};
const authenticationSlice = createSlice({
  name: "authentication",
  initialState: initialAuthState,
  extraReducers: (builder) => {
    builder.addCase(signup.pending, (state) => {
      state.isLoading = true;
    });
    builder.addCase(signup.fulfilled, (state, { payload }) => {
      state.isLoading = false;
      state.newUser = payload?.new_user;
      state.message = payload?.message;
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
      state.accessToken = payload?.access_token;
      state.refreshToken = payload?.refresh_token;
      state.message = payload?.message;
      state.success = payload?.success;
      state.isLoggedIn = true;
    });
    builder.addCase(login.rejected, (state) => {
      state.isLoading = false;
    });
  },
});

export default authenticationSlice.reducer;

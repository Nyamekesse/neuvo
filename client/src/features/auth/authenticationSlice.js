import { createAsyncThunk, createSlice } from "@reduxjs/toolkit";
import { createUser } from "../../api";
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
const initialPostState = {
  isLoading: true,
  newUser: "",
  message: "",
  profile: {},
  isLoggedIn: false,
  success: false,
};
const authenticationSlice = createSlice({
  name: "authentication",
  initialState: initialPostState,
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
  },
});

export default authenticationSlice.reducer;

import { createAsyncThunk, createSlice } from "@reduxjs/toolkit";
import { createUser } from "../../api";
import { displayAlert } from "../alerts/alertSlice";
import { ERROR, INFO, SUCCESS } from "../../constants";

export const signUpUser = createAsyncThunk(
  "user/createNewUser",
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
};
const userSlice = createSlice({
  name: "user",
  initialState: initialPostState,
  extraReducers: (builder) => {
    builder.addCase(signUpUser.pending, (state) => {
      state.isLoading = true;
    });
    builder.addCase(signUpUser.fulfilled, (state, { payload }) => {
      state.isLoading = false;
      state.newUser = payload?.new_user;
      state.message = payload?.message;
    });
    builder.addCase(signUpUser.rejected, (state) => {
      state.isLoading = false;
    });
  },
});

export default userSlice.reducer;

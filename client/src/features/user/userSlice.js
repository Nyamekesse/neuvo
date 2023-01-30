import { createAsyncThunk, createSlice } from "@reduxjs/toolkit";
import { createUser } from "../../api";

export const signUpUser = createAsyncThunk(
  "user/createNewUser",
  async (data) => {
    try {
      const res = await createUser(data);
      console.log(res);
      return res.data;
    } catch (error) {
      console.log(error.message);
    }
  }
);
const initialPostState = {
  isLoading: true,
  userId: "",
  message: "",
  error: "",
};
const userSlice = createSlice({
  name: "user",
  initialState: initialPostState,
  extraReducers: (builder) => {
    builder.addCase(signUpUser.pending, (state, action) => {
      state.isLoading = true;
    });
    builder.addCase(signUpUser.fulfilled, (state, action) => {
      state.isLoading = false;
      state.userId = action.payload.user_id;
      state.message = action.payload.message;
    });
    builder.addCase(signUpUser.rejected, (state, action) => {
      state.isLoading = false;
      state.error = error.message;
    });
  },
});

export default userSlice.reducer;

import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";
import { fetchPost } from "../../api";

const initialPostState = {
  loading: false,
  posts: [],
  error: "",
};

export const getAllPosts = createAsyncThunk("post/getAllPosts", async () => {
  try {
    const { data } = await fetchPost();
    return data;
  } catch (error) {
    console.log(error.message);
  }
});

const postSlice = createSlice({
  name: "post",
  initialState: initialPostState,
  reducers: {
    createPost: (state, action) => {
      console.log("");
    },
    deletePost: (state, action) => {
      console.log("");
    },
    updatePost: (state, action) => {
      console.log("");
    },
  },
  extraReducers: (builder) => {
    builder.addCase(getAllPosts.pending, (state, action) => {
      state.loading = true;
    });
    builder.addCase(getAllPosts.fulfilled, (state, action) => {
      state.loading = false;
      state.posts = action.payload;
    });
    builder.addCase(getAllPosts.rejected, (state, action) => {
      state.loading = false;
      state.error = error.message;
    });
  },
});

export default postSlice.reducer;

import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";
import { fetchPost } from "../../api";

const initialPostState = {
  isLoading: true,
  posts: [],
  numberOfPages: 1,
  currentPage: 1,
  error: "",
};

export const getAllPosts = createAsyncThunk(
  "post/getAllPosts",
  async (page) => {
    try {
      const { data } = await fetchPost(page);
      return data;
    } catch (error) {
      console.log(error.message);
    }
  }
);

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
      state.isLoading = true;
    });
    builder.addCase(getAllPosts.fulfilled, (state, action) => {
      state.isLoading = false;
      state.posts = action.payload.results;
      state.currentPage = action.payload.current_page;
      state.numberOfPages = action.payload.number_of_pages;
    });
    builder.addCase(getAllPosts.rejected, (state, action) => {
      state.isLoading = false;
      state.error = error.message;
    });
  },
});

export default postSlice.reducer;

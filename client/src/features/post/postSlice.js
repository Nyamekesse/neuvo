import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";
import { fetchPost, fetchSinglePostDetails } from "../../api";
import { ERROR } from "../../constants";
import { displayAlert } from "../alerts/alertSlice";

const initialPostState = {
  isLoading: false,
  posts: [],
  singlePost: {},
  numberOfPages: 1,
  currentPage: 1,
};

export const getAllPosts = createAsyncThunk(
  "post/getAllPosts",
  async (page, thunkAPI) => {
    try {
      const res = await fetchPost(page);
      if (res.status === 200 && res.statusText === "OK") {
        const { data } = res;

        if (data.success) {
          return data;
        } else {
          thunkAPI.dispatch(
            displayAlert({
              text: "Something went wrong while fetching posts, please try again later",
              severity: ERROR,
            })
          );
        }
      }
    } catch (error) {
      thunkAPI.dispatch(
        displayAlert({
          text: error.response.data
            ? error.response.data.message
            : error.message,
          severity: ERROR,
        })
      );
      return rejectWithValue(
        error.response.data ? error.response.data.message : error.message
      );
    }
  }
);

export const getSinglePostDetails = createAsyncThunk(
  "post/getSinglePost",
  async (postId) => {
    try {
      const res = await fetchSinglePostDetails(postId);
      if (res.status === 200 && res.statusText === "OK") {
        const { data } = res;
        if (data.success) return data.post;

        thunkAPI.dispatch(
          displayAlert({
            text: "Something went wrong while fetching posts, please try again later",
            severity: ERROR,
          })
        );
      }
    } catch (error) {
      thunkAPI.dispatch(
        displayAlert({
          text: error.response.data
            ? error.response.data.message
            : error.message,
          severity: ERROR,
        })
      );
      return rejectWithValue(
        error.response.data ? error.response.data.message : error.message
      );
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
    builder.addCase(getAllPosts.pending, (state) => {
      state.isLoading = true;
    });
    builder.addCase(getAllPosts.fulfilled, (state, { payload }) => {
      state.isLoading = false;
      state.posts = payload.results;
      state.currentPage = payload.current_page;
      state.numberOfPages = payload.number_of_pages;
    });
    builder.addCase(getAllPosts.rejected, (state) => {
      state.isLoading = false;
    });
    builder.addCase(getSinglePostDetails.pending, (state, action) => {
      state.isLoading = true;
    });
    builder.addCase(getSinglePostDetails.fulfilled, (state, { payload }) => {
      state.isLoading = false;
      state.singlePost = payload;
    });
    builder.addCase(getSinglePostDetails.rejected, (state) => {
      state.isLoading = false;
    });
  },
});

export default postSlice.reducer;

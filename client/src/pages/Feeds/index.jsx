import React, { useEffect } from "react";
import { Pagination, Postcard } from "../../components";
import { useDispatch, useSelector } from "react-redux";
import { getAllPosts } from "../../features/post/postSlice";
import { useLocation } from "react-router-dom";

const useQuery = () => {
  return new URLSearchParams(useLocation().search);
};

const Feeds = () => {
  const query = useQuery();
  const page = query.get("page") || 1;
  const { posts, isLoading, numberOfPages } = useSelector(
    (state) => state.post
  );
  const dispatch = useDispatch(page);
  useEffect(() => {
    dispatch(getAllPosts());
  }, []);

  return (
    <>
      {isLoading ? (
        <h1>loading</h1>
      ) : !posts?.length ? (
        <h1>No post</h1>
      ) : (
        posts.map((post) => {
          return (
            <div key={post.id}>
              <Postcard {...post} />
            </div>
          );
        })
      )}
      <Pagination page={page} numberOfPages={numberOfPages} />
    </>
  );
};

export default Feeds;

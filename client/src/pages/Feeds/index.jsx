import React, { useEffect } from "react";
import { Pagination, Postcard } from "../../components";
import { useDispatch, useSelector } from "react-redux";
import { getAllPosts } from "../../features/post/postSlice";

const Feeds = () => {
  const dispatch = useDispatch();
  useEffect(() => {
    dispatch(getAllPosts());
  }, []);
  const res = useSelector((state) => state.post.posts);

  return (
    <>
      {res.map((post) => {
        return (
          <div key={post.id}>
            <Postcard />
          </div>
        );
      })}

      <Pagination />
    </>
  );
};

export default Feeds;

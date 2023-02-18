import React, { useEffect } from "react";
import { PostDetail } from "../../components";
import { useLocation } from "react-router-dom";
import { useDispatch, useSelector } from "react-redux";
import { getSinglePostDetails } from "../../features/post/postSlice";

const PostDetails = () => {
  const location = useLocation();
  const searchParams = new URLSearchParams(location.search);
  const postId = searchParams.get("postId");
  const dispatch = useDispatch();
  const { singlePost } = useSelector((store) => store.post);
  useEffect(() => {
    postId ? dispatch(getSinglePostDetails(postId)) : null;
  }, [dispatch]);
  return <PostDetail post={singlePost} />;
};

export default PostDetails;

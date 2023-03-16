import React from "react";
import Feeds from "../pages/Feeds";
import Home from "../pages/Home";
import LogIn from "../pages/Log-in";
import SignUp from "../pages/Sign-up";
import PostDetails from "../pages/PostDetails";
import { Routes, Route, Navigate } from "react-router-dom";
import PageNotFound from "../pages/404-Page";
import { CustomEditor } from "../components";
const Views = () => {
  return (
    <Routes>
      <Route index element={<Navigate to={"/posts"} replace />} />
      <Route exact path="/posts" element={<Feeds />} />
      <Route exact path="/welcome-to-blog-x" element={<Home />} />
      <Route exact path="/log-in" element={<LogIn />} />
      <Route exact path="/sign-up" element={<SignUp />} />
      <Route exact path="/post-details" element={<PostDetails />} />
      <Route exact path="/posts/search" element={<PostDetails />} />
      <Route exact path="/editor" element={<CustomEditor />} />
      <Route path="/page-not-found" element={<PageNotFound />} />
      <Route path="*" element={<Navigate to="/page-not-found" />} />
    </Routes>
  );
};

export default Views;

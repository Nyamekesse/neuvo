import React from "react";
import Feeds from "../pages/Feeds";
import Home from "../pages/Home";
import LogIn from "../pages/Log-in";
import SignUp from "../pages/Sign-up";
import Post from "../pages/Post";
import { Routes, Route, Navigate } from "react-router-dom";
import PageNotFound from "../pages/404-Page";
const Views = () => {
  return (
    <Routes>
      <Route index element={<Feeds />} />
      <Route exact path="/welcome-to-blog-x" element={<Home />} />
      <Route exact path="/log-in" element={<LogIn />} />
      <Route exact path="/sign-up" element={<SignUp />} />
      <Route exact path="/post-details" element={<Post />} />
      <Route path="/page-not-found" element={<PageNotFound />} />
      <Route path="*" element={<Navigate to="/page-not-found" />} />
    </Routes>
  );
};

export default Views;

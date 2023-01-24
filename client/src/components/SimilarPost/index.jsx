import React from "react";
import "slick-carousel/slick/slick.css";
import "slick-carousel/slick/slick-theme.css";
import Slider from "react-slick";
import { Box, Typography } from "@mui/material";
import SuggestedPostCard from "../SuggestedPostCard";
import settings from "./settings";
const SimilarPost = () => {
  return (
    <Box mt={1} mb={1}>
      <Typography
        variant="caption"
        component={"p"}
        fontSize={18}
        fontWeight={700}
        align="center"
        mt={1}
        mb={1}
      >
        Similar posts
      </Typography>
      <Slider {...settings}>
        <SuggestedPostCard />
        <SuggestedPostCard />
        <SuggestedPostCard />
      </Slider>
    </Box>
  );
};

export default SimilarPost;

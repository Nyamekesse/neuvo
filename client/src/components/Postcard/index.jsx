import React from "react";
import { PostDetails, PostImage, Wrap } from "./style";
import { Typography } from "@mui/material";
import Image1 from "../../assets/pexels-sl-wong-947384.jpg";
const Postcard = () => {
  return (
    <Wrap>
      <PostImage>
        <img src={Image1} alt={Image1} />
      </PostImage>
      <PostDetails>
        <Typography
          variant="h6"
          component={"h3"}
          fontWeight={700}
          fontSize={28}
          mb={1}
        >
          How to be more productive?
        </Typography>
        <Typography
          variant="caption"
          color={"#888888"}
          component={"p"}
          fontSize={14}
          fontWeight={400}
          mb={1}
        >
          19 May 2021, {"8"} comments
        </Typography>
        <Typography
          variant="body2"
          component={"p"}
          fontSize={18}
          fontWeight={400}
        >
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Praesentium
          et illum hic exercitationem nobis dolore saepe consequuntur, vel
          laborum dolorem sit. Velit quidem aut numquam sit fugit quia quo
          doloribus! dolorem sit. Velit quidem aut numquam sit fugit quia quo
          doloribus! doloribus!dolorem sit. Velit quidem aut numquam sit
          fugit...
        </Typography>
      </PostDetails>
    </Wrap>
  );
};

export default Postcard;

import React from "react";
import { PostDetails, PostImage, Wrap } from "./style";
import { Typography } from "@mui/material";
import Image1 from "../../assets/pexels-sl-wong-947384.jpg";
import { Link } from "react-router-dom";
import moment from "moment";
const Postcard = ({
  id,
  title,
  post_image,
  author_id,
  post_content,
  date_posted,
  author_name,
}) => {
  return (
    <Link to={`/post-details${`?postId=${id}`}`}>
      <Wrap data-author-id={author_id}>
        <PostImage>
          <img src={post_image} alt={Image1} />
        </PostImage>
        <PostDetails>
          <Typography
            variant="h6"
            component={"h3"}
            fontWeight={700}
            fontSize={28}
            mb={1}
          >
            {title.length > 55 ? title.slice(0, 55) + " …" : title}
          </Typography>
          <Typography
            variant="caption"
            color={"#888888"}
            component={"p"}
            fontSize={14}
            fontWeight={400}
            mb={1}
          >
            by: <b>{author_name}</b>
          </Typography>
          <Typography
            variant="caption"
            color={"#888888"}
            component={"p"}
            fontSize={14}
            fontWeight={400}
            mb={1}
          >
            {moment(date_posted).fromNow()}
          </Typography>
          <Typography
            variant="body2"
            component={"p"}
            fontSize={18}
            fontWeight={400}
          >
            {post_content.length > 155
              ? post_content.slice(0, 155 - 1) + " …"
              : post_content}
          </Typography>
        </PostDetails>
      </Wrap>
    </Link>
  );
};

export default Postcard;

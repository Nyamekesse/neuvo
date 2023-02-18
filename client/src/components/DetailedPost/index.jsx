import React from "react";
import {
  CommentCard,
  CommentSection,
  CommentText,
  Comments,
  Image,
  Post,
  Wrap,
} from "./style";
import { Box, Button, Typography } from "@mui/material";
import TextField from "@mui/material/TextField";
import image from "../../assets/pexels-sl-wong-947384.jpg";
import Avatar from "@mui/material/Avatar";
import profile1 from "../../assets/profile-1.jpg";
import profile2 from "../../assets/profile-2.jpg";
import profile3 from "../../assets/profile-3.jpg";
import { SimilarPost } from "../../components";
const PostDetail = ({ post }) => {
  return (
    <Wrap>
      <Post component={"section"}>
        <Typography
          variant={"h3"}
          component={"h1"}
          fontWeight={700}
          fontSize={28}
          align="center"
          mb={1}
        >
          {post.title}
        </Typography>
        <Typography
          variant="caption"
          color={"#111"}
          component={"p"}
          fontSize={13}
          fontWeight={400}
          mb={1}
        >
          by: <b>{post.author_name}</b>
        </Typography>
        <Typography
          variant="caption"
          color={"#888888"}
          component={"p"}
          fontSize={12}
          fontWeight={400}
          mb={1}
        >
          {post.date_posted}
        </Typography>
        <Image>
          <img src={post.post_image} alt={image} />
        </Image>
        <Typography
          variant="subtitle1"
          component={"p"}
          fontSize={16}
          fontWeight={400}
          mt={4}
          mb={2}
        >
          {post.post_content}
        </Typography>
      </Post>
      <CommentSection component={"section"}>
        <Typography
          component={"p"}
          variant="subtitle2"
          fontSize={14}
          fontWeight={700}
          align="center"
          mb={2}
        >
          What do you think?
        </Typography>
        <TextField
          multiline
          minRows={5}
          placeholder="write your comments here..."
          variant="outlined"
          fullWidth
        />
        <Box
          sx={{
            display: "flex",
            justifyContent: "flex-end",
          }}
        >
          <Button
            disableElevation
            variant={"contained"}
            sx={{ marginTop: "20px" }}
            component={"button"}
          >
            Comment
          </Button>
        </Box>

        <Comments>
          <CommentCard>
            <Avatar
              alt="Remy Sharp"
              src={profile1}
              sx={{ marginRight: "20px" }}
            />
            <Box>
              <CommentText>
                <Typography
                  variant="caption"
                  component={"p"}
                  fontSize={14}
                  fontWeight={400}
                >
                  Really nice post! I have applied those methods for daily.
                </Typography>
              </CommentText>
              <Typography
                variant="caption"
                component={"p"}
                color={"#888888"}
                fontSize={12}
                fontWeight={400}
                mt={1}
              >
                2 hours ago
              </Typography>
            </Box>
          </CommentCard>
          <CommentCard>
            <Avatar
              alt="Remy Sharp"
              src={profile2}
              sx={{ marginRight: "20px" }}
            />
            <Box>
              <CommentText>
                <Typography
                  variant="caption"
                  component={"p"}
                  fontSize={14}
                  fontWeight={400}
                >
                  I love your writing style! It’s easy to understand and so
                  engaging to read it until the end of the line! I have read so
                  many productivity tips and this is so far the best I found! On
                  this fast-changing world we need to be more productive. I
                  wrote some life tips also, you can check on my page. Thank you
                  for sharing mate!
                </Typography>
              </CommentText>
              <Typography
                variant="caption"
                component={"p"}
                color={"#888888"}
                fontSize={12}
                fontWeight={400}
                mt={1}
              >
                yesterday
              </Typography>
            </Box>
          </CommentCard>
          <CommentCard>
            <Avatar
              alt="Remy Sharp"
              src={profile3}
              sx={{ marginRight: "20px" }}
            />
            <Box>
              <CommentText>
                <Typography
                  variant="caption"
                  component={"p"}
                  fontSize={14}
                  fontWeight={400}
                >
                  Thank you so much for these tips! I never thought these simple
                  steps and trick on the first place!
                </Typography>
              </CommentText>
              <Typography
                variant="caption"
                component={"p"}
                color={"#888888"}
                fontSize={12}
                fontWeight={400}
                mt={1}
              >
                a week ago
              </Typography>
            </Box>
          </CommentCard>
        </Comments>
      </CommentSection>
      <Box
        sx={{
          width: "100%",
          // backgroundColor: "red",
        }}
      >
        <SimilarPost />
      </Box>
    </Wrap>
  );
};
export default PostDetail;

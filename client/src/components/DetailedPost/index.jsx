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
const PostDetail = () => {
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
          How to be more productive
        </Typography>
        <Typography
          variant="caption"
          color={"#888888"}
          component={"p"}
          fontSize={12}
          fontWeight={400}
          mb={1}
        >
          19 May 2021
        </Typography>
        <Image>
          <img src={image} alt={image} />
        </Image>
        <Typography
          variant="subtitle1"
          component={"p"}
          fontSize={16}
          fontWeight={400}
          mt={4}
          mb={2}
        >
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Praesentium
          et illum hic exercitationem nobis dolore saepe consequuntur, vel
          laborum dolorem sit. Velit quidem aut numquam sit fugit quia quo
          doloribus! dolorem sit. Velit quidem aut numquam sit fugit quia quo
          doloribus! doloribus!dolorem sit. Velit quidem aut numquam sit fugit.
          Lorem ipsum dolor sit amet consectetur, adipisicing elit. Velit harum
          fuga quibusdam est, consectetur distinctio nesciunt. Earum quisquam
          incidunt illum ullam nesciunt deserunt a obcaecati molestias, quod
          esse? Magnam, atque. Lorem ipsum dolor sit amet consectetur
          adipisicing elit. Enim voluptas harum nemo adipisci culpa nam fugiat
          eos, ad eum accusamus eligendi illum exercitationem natus similique
          magni libero. Sapiente, commodi sed? Lorem ipsum dolor sit, amet
          consectetur adipisicing elit. Earum dolorem cum consectetur minus sed.
          Voluptates nobis impedit perferendis amet, vero omnis numquam nesciunt
          similique asperiores quia. Vitae aliquam recusandae exercitationem.
          Lorem ipsum dolor, sit amet consectetur adipisicing elit. Dolore,
          maiores!
          <br />
          <br />
          Lorem, ipsum dolor sit amet consectetur adipisicing elit. Vitae sunt
          odit unde adipisci, maiores aperiam a dolor facilis officia
          blanditiis! Lorem ipsum dolor, sit amet consectetur adipisicing elit.
          Voluptatum deserunt sit officiis eius architecto unde est veniam, quae
          possimus culpa dolor nobis fugiat alias odit repellendus laboriosam
          accusamus consequatur deleniti enim quod ex. Rem fuga praesentium
          error at veniam. Tenetur iusto, suscipit nostrum sint minus labore
          optio deleniti vel ipsa. Lorem ipsum dolor sit amet consectetur
          adipisicing elit. Enim numquam quaerat itaque rerum unde pariatur
          distinctio, perspiciatis aperiam doloremque velit vel quas, fuga
          nostrum quia sed aliquam porro commodi consequuntur laborum! Ipsam
          pariatur, libero delectus aut ratione quibusdam suscipit. Iusto eos
          hic temporibus veritatis aperiam adipisci impedit doloremque minus
          quaerat dicta. Ut quasi facilis odit debitis ab quia officia deserunt
          blanditiis veniam, magni ipsam provident nostrum? Eum error in, ipsa
          ea laudantium voluptates quaerat eligendi cupiditate earum,
          repudiandae expedita facilis eius ullam, animi odio tenetur labore
          nobis magni. Ab voluptates commodi hic at iste sequi officiis maiores.
          Quod, harum consequatur!
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

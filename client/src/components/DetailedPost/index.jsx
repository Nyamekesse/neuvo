import React from "react";
import { CommentSection, Comments, Image, Post, Wrap } from "./style";
import { Box, Button, Typography } from "@mui/material";
import TextField from "@mui/material/TextField";
import image from "../../assets/pexels-sl-wong-947384.jpg";
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

        <Button
          disableElevation
          variant={"contained"}
          sx={{ marginTop: "20px" }}
          component={"button"}
        >
          Comment
        </Button>

        <Comments></Comments>
      </CommentSection>
    </Wrap>
  );
};
export default PostDetail;

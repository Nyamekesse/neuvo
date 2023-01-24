import React from "react";
import { Image, Wrap } from "./style";
import { Typography } from "@mui/material";
import place from "../../assets/place.jpg";
const SuggestedPostCard = () => {
  return (
    <Wrap>
      <Image>
        <img src={place} alt={place} />
      </Image>
      <Typography
        variant="body1"
        component={"h4"}
        fontSize={16}
        fontWeight={400}
        mt={1}
      >
        Do these every single day and you will become a more creative person
      </Typography>
    </Wrap>
  );
};

export default SuggestedPostCard;

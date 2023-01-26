import React from "react";
import ShowcaseImage from "../../../assets/writter.svg";
import { Image, Showcase } from "./style";
import Typography from "@mui/material/Typography";
const ShowcaseSection = () => {
  return (
    <Showcase>
      <Typography variant="h5" component={"h2"} fontWeight={500} fontSize={25}>
        Lorem ipsum dolor sit amet, incididunt consectetur adipiscing elit.
      </Typography>
      <Typography variant="caption" component={"span"} color={"#898D93"} mt={1}>
        Incididunt ut labore et dolore magna aliqua.
      </Typography>
      <Image>
        <img src={ShowcaseImage} alt={ShowcaseImage} />
      </Image>
    </Showcase>
  );
};

export default ShowcaseSection;

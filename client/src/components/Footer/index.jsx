import React from "react";
import { Socials, Wrap } from "./style";
import { IconButton, Typography } from "@mui/material";
import FacebookIcon from "@mui/icons-material/Facebook";
import InstagramIcon from "@mui/icons-material/Instagram";
import LinkedInIcon from "@mui/icons-material/LinkedIn";
const Footer = () => {
  return (
    <Wrap>
      <Typography
        variant="caption"
        component={"p"}
        align="center"
        fontSize={14}
      >
        Samuel Nyamekesse &copy; {new Date().getFullYear()} All rights reserved
      </Typography>
      <Socials>
        <IconButton>
          <FacebookIcon />
        </IconButton>
        <IconButton>
          <InstagramIcon />
        </IconButton>
        <IconButton>
          <LinkedInIcon />
        </IconButton>
      </Socials>
    </Wrap>
  );
};

export default Footer;

import React from "react";
import { Container, Title } from "./style";
import MenuIcon from "@mui/icons-material/Menu";
import { IconButton, Typography } from "@mui/material";

const Header = () => {
  return (
    <>
      <Container>
        <IconButton size="large">
          <MenuIcon fontSize="large" />
        </IconButton>

        <Title>
          <Typography
            variant="h6"
            component={"h1"}
            align={"center"}
            fontWeight={700}
            fontSize={36}
          >
            BlogX
          </Typography>
        </Title>
      </Container>
    </>
  );
};

export default Header;

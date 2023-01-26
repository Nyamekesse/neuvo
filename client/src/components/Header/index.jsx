import React from "react";
import { ButtonGroup, Container, Title } from "./style";
import MenuIcon from "@mui/icons-material/Menu";
import { Button, IconButton, Typography } from "@mui/material";
import { Link } from "react-router-dom";

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
            <Link to={"/"}>BlogX</Link>
          </Typography>
        </Title>
        <ButtonGroup>
          <Button
            variant="outlined"
            size="medium"
            disableElevation
            sx={{
              textTransform: "initial",
              margin: "0 5px",
              border: "1px solid #111",

              ":hover, :active": {
                border: "1px solid #111",
                backgroundColor: "initial",
              },
            }}
          >
            <Link to={"/log-in"}>Log in</Link>
          </Button>
          <Button
            variant="contained"
            size="medium"
            disableElevation
            sx={{ backgroundColor: "#111", margin: "0 5px" }}
          >
            <Link to={"/sign-up"} style={{ color: "#fff" }}>
              Sign up
            </Link>
          </Button>
        </ButtonGroup>
      </Container>
    </>
  );
};

export default Header;

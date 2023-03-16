import React, { useState, useEffect, useLayoutEffect } from "react";
import { ButtonGroup, Container, Title } from "./style";
import MenuIcon from "@mui/icons-material/Menu";
import { Avatar, Box, Button, IconButton, Typography } from "@mui/material";
import { Link, useLocation } from "react-router-dom";
import profile1 from "../../assets/profile-1.jpg";
import { PROFILE } from "../../constants";
import { decodeJWT, secureStorageGetToken } from "../../utils";
import { useSelector } from "react-redux";
const Header = () => {
  const { isLoggedIn } = useSelector((store) => store.authentication);

  const [user, setUser] = useState({});
  useEffect(() => {
    const { sub } = decodeJWT(secureStorageGetToken(PROFILE)) ?? {};
    setUser(sub);
  }, [isLoggedIn]);
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
            <Link to={"/posts?page=1"}>BlogX</Link>
          </Typography>
        </Title>
        {user ? (
          <Box
            display={"flex"}
            alignItems={"center"}
            justifyContent={"space-between"}
          >
            <Avatar alt={user.display_picture} src={user.display_picture} />
            <Typography ml={4} variant="h5" fontWeight={600}>
              {user.username}
            </Typography>
          </Box>
        ) : (
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
        )}
      </Container>
    </>
  );
};

export default Header;

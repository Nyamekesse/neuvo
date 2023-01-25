import React from "react";
import {
  Container,
  Form,
  FormArea,
  Image,
  InputSection,
  Logo,
  Root,
  Showcase,
  Wrap,
} from "./style";
import { Box, Button, TextField, Typography } from "@mui/material";
import ShowcaseImage from "../../assets/writter.svg";
import logo from "../../assets/blogX.png";
import GoogleIcon from "../../assets/google-g-2015.svg";
import Divider from "@mui/material/Divider";
import TrendingFlatIcon from "@mui/icons-material/TrendingFlat";
import { Link } from "react-router-dom";
const LogIn = () => {
  return (
    <Wrap>
      <Container>
        <Showcase>
          <Typography
            variant="h5"
            component={"h2"}
            fontWeight={500}
            fontSize={25}
          >
            Lorem ipsum dolor sit amet, incididunt consectetur adipiscing elit.
          </Typography>
          <Typography
            variant="caption"
            component={"span"}
            color={"#898D93"}
            mt={1}
          >
            Incididunt ut labore et dolore magna aliqua.
          </Typography>
          <Image>
            <img src={ShowcaseImage} alt={ShowcaseImage} />
          </Image>
        </Showcase>
        <FormArea>
          <Form component={"form"}>
            <Typography
              variant="h6"
              component={"h1"}
              align={"center"}
              fontWeight={700}
              fontSize={36}
            >
              BlogX
            </Typography>
            <Typography
              component={"p"}
              variant={"caption"}
              color={"#898D93"}
              fontWeight={400}
              fontSize={14}
              mt={2}
            >
              Welcome, Please log in into your account
            </Typography>
            <Button
              variant="outlined"
              sx={{ textTransform: "initial", marginTop: "10%" }}
              fullWidth
            >
              <Box width={"20px"} height={"20px"} marginRight={1}>
                <img src={GoogleIcon} alt={GoogleIcon} />
              </Box>
              Log in with Google
            </Button>
            <Root>
              <Divider>
                <Typography
                  component={"p"}
                  variant="caption"
                  textTransform={"uppercase"}
                  color={"#E74425"}
                  fontWeight={500}
                  fontSize={12}
                >
                  log in for external user
                </Typography>
              </Divider>
            </Root>
            <Box
              sx={{
                display: "flex",
                flexDirection: "column",
                width: "100%",
              }}
            >
              <InputSection>
                <Typography
                  color={"#50565F"}
                  fontWeight={500}
                  fontSize={16}
                  component={"p"}
                  variant="body1"
                  mb={1}
                >
                  Username or Email
                </Typography>
                <TextField
                  placeholder="Enter user email or username"
                  fullWidth
                  size="small"
                  required
                  sx={{ backgroundColor: "#fff" }}
                />
              </InputSection>
              <InputSection>
                <Typography
                  color={"#50565F"}
                  fontWeight={500}
                  fontSize={16}
                  component={"p"}
                  variant="body1"
                  mt={3}
                  mb={1}
                >
                  Password
                </Typography>
                <TextField
                  placeholder="Enter your password"
                  fullWidth
                  size="small"
                  required
                  sx={{ backgroundColor: "#fff" }}
                />
              </InputSection>
            </Box>
            <Button
              variant="contained"
              endIcon={<TrendingFlatIcon />}
              fullWidth
              disableElevation
              sx={{
                marginTop: "30px",
                textTransform: "capitalize",
                background:
                  "linear-gradient(89.95deg, #E73125 0.04%, #E74825 99.96%)",
              }}
            >
              log in
            </Button>
          </Form>
          <Typography component={"span"} variant="caption" mt={2}>
            Don't have an account?{" "}
            <Link to={"/sign-up"}>
              {" "}
              <span style={{ textDecoration: "underline" }}>Sign up</span>
            </Link>
          </Typography>
        </FormArea>
      </Container>
    </Wrap>
  );
};

export default LogIn;

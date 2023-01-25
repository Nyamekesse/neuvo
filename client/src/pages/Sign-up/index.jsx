import React from "react";
import {
  Container,
  Form,
  FormArea,
  InputSection,
  Showcase,
  Wrap,
} from "./style";
import { Box, IconButton, TextField, Typography } from "@mui/material";
import { Link } from "react-router-dom";
import VisibilityIcon from "@mui/icons-material/Visibility";
import VisibilityOffIcon from "@mui/icons-material/VisibilityOff";
const SignUp = () => {
  return (
    <Wrap>
      <Container>
        <FormArea>
          <Form component={"form"}>
            <Typography color={"#333333"} fontWeight={500} fontSize={32}>
              Welcome to BlogX Community
            </Typography>
            <Typography
              component={"span"}
              variant="caption"
              fontSize={16}
              fontWeight={400}
              mt={2}
              color={"#333333"}
            >
              Already have an account?{" "}
              <Link to={"/log-in"}>
                {" "}
                <span style={{ textDecoration: "underline" }}>Log in</span>
              </Link>
            </Typography>
            <InputSection>
              <Typography
                color={"#50565F"}
                fontWeight={400}
                fontSize={16}
                component={"p"}
                variant="body1"
                mb={1}
              >
                Email
              </Typography>
              <TextField
                placeholder="Enter user email "
                fullWidth
                size="small"
                required
                type={"email"}
                sx={{ backgroundColor: "#fff" }}
              />
            </InputSection>
            <InputSection>
              <Typography
                color={"#50565F"}
                fontWeight={400}
                fontSize={16}
                component={"p"}
                variant="body1"
                mb={1}
              >
                Username
              </Typography>
              <TextField
                placeholder="Enter  username"
                fullWidth
                size="small"
                required
                type={"text"}
                sx={{ backgroundColor: "#fff" }}
              />
            </InputSection>
            <InputSection>
              <Box
                sx={{
                  display: "flex",
                  flexDirection: "row",
                  width: "100%",
                  alignItems: "center",
                  justifyContent: "space-between",
                }}
              >
                <Typography
                  color={"#50565F"}
                  fontWeight={400}
                  fontSize={16}
                  component={"p"}
                  variant="body1"
                  mt={3}
                  mb={1}
                >
                  Password
                </Typography>
                <Box
                  sx={{
                    display: "flex",
                    flexDirection: "row",
                    alignItems: "center",
                  }}
                >
                  <VisibilityOffIcon
                    sx={{
                      width: "15px",
                      marginRight: "10px",
                      color: "rgba(102, 102, 102, 0.8)",
                    }}
                  />
                  <Typography
                    fontWeight={400}
                    fontSize={18}
                    sx={{ color: "rgba(102, 102, 102, 0.8)" }}
                  >
                    Hide
                  </Typography>
                </Box>
              </Box>
              <TextField
                placeholder="Enter your password"
                fullWidth
                size="small"
                required
                type={"password"}
                sx={{ backgroundColor: "#fff" }}
              />
            </InputSection>
          </Form>
        </FormArea>
        <Showcase></Showcase>
      </Container>
    </Wrap>
  );
};

export default SignUp;

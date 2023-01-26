import Box from "@mui/material/Box";
import Button from "@mui/material/Button";
import Typography from "@mui/material/Typography";
import React from "react";
import Divider from "@mui/material/Divider";
import TrendingFlatIcon from "@mui/icons-material/TrendingFlat";
import { Form, FormArea, InputGroup, InputSection, Root } from "./style";
import { Link } from "react-router-dom";
import GoogleIcon from "../../../assets/google-g-2015.svg";
import TextField from "@mui/material/TextField";
const FormSection = () => {
  return (
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
        <InputGroup>
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
        </InputGroup>
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
  );
};

export default FormSection;

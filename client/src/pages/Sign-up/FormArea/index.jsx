import React, { useState } from "react";
import VisibilityIcon from "@mui/icons-material/Visibility";
import VisibilityOffIcon from "@mui/icons-material/VisibilityOff";
import Box from "@mui/material/Box";
import Button from "@mui/material/Button";
import TextField from "@mui/material/TextField";
import Typography from "@mui/material/Typography";
import { Link } from "react-router-dom";
import {
  Form,
  FormArea,
  Indicator,
  InputSection,
  Validators,
  Wrapper,
} from "./style";
const FormAreaSection = () => {
  const [state, setState] = useState({
    email: "",
    username: "",
    password: "",
  });
  const handleFormChange = (event) => {
    setState({ ...state, [event.target.name]: event.target.value });
  };
  const handleFormSubmit = (event) => {
    event.preventDefault();
    console.log(state);
    setState({ email: "", username: "", password: "" });
  };
  return (
    <FormArea>
      <Form component={"form"} onSubmit={handleFormSubmit}>
        <Typography color={"#333333"} fontWeight={500} fontSize={32}>
          Welcome to BlogX Community
        </Typography>
        <Typography
          component={"span"}
          variant="caption"
          fontSize={12}
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
            fontSize={15}
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
            name="email"
            type={"email"}
            value={state.email}
            onChange={handleFormChange}
            sx={{ backgroundColor: "#fff" }}
          />
        </InputSection>
        <InputSection>
          <Typography
            color={"#50565F"}
            fontWeight={400}
            fontSize={14}
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
            name="username"
            type={"text"}
            value={state.username}
            onChange={handleFormChange}
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
              fontSize={14}
              component={"p"}
              variant="body1"
              mt={3}
              mb={1}
            >
              Password
            </Typography>
            <Button
              variant="text"
              startIcon={<VisibilityOffIcon />}
              size="medium"
              disableElevation
              disableRipple
              disableFocusRipple
              fontSize={14}
              sx={{
                color: "rgba(102, 102, 102, 0.8)",
                textTransform: "initial",
                padding: 0,
                margin: 0,
                fontSize: "14px",
              }}
            >
              Hide
            </Button>
          </Box>
          <TextField
            placeholder="Enter your password"
            fullWidth
            size="small"
            required
            name="password"
            type={"password"}
            value={state.password}
            onChange={handleFormChange}
            sx={{ backgroundColor: "#fff" }}
          />
        </InputSection>
        <Validators>
          <Wrapper>
            <Indicator>
              <Typography
                fontSize={12}
                fontWeight={400}
                color={" rgba(102, 102, 102, 0.6);"}
              >
                Use 8 or more characters
              </Typography>
            </Indicator>
            <Indicator>
              <Typography
                fontSize={12}
                fontWeight={400}
                color={" rgba(102, 102, 102, 0.6);"}
              >
                One Uppercase character
              </Typography>
            </Indicator>
            <Indicator>
              <Typography
                fontSize={12}
                fontWeight={400}
                color={" rgba(102, 102, 102, 0.6);"}
              >
                One Lowercase character
              </Typography>
            </Indicator>
            <Indicator>
              {" "}
              <Typography
                fontSize={12}
                fontWeight={400}
                color={" rgba(102, 102, 102, 0.6);"}
              >
                One special character
              </Typography>
            </Indicator>
            <Indicator>
              {" "}
              <Typography
                fontSize={12}
                fontWeight={400}
                color={" rgba(102, 102, 102, 0.6);"}
              >
                One number
              </Typography>
            </Indicator>
          </Wrapper>
        </Validators>
        <Typography fontWeight={400} fontSize={12} color={"#333333"} mt={2}>
          By creating an account, you agree to the{" "}
          <Link to={"/"}>
            <span style={{ textDecoration: "underline" }}>Terms of use</span>
          </Link>{" "}
          and{" "}
          <Link to={"/"}>
            <span style={{ textDecoration: "underline" }}>Privacy Policy </span>
          </Link>
          .
        </Typography>
        <Box>
          <Button
            variant={"contained"}
            sx={{
              marginTop: "10px",
              textTransform: "initial",
              background:
                "linear-gradient(89.95deg, #E73125 0.04%, #E74825 99.96%)",
            }}
            type="submit"
            fullWidth={false}
          >
            Create an account
          </Button>
        </Box>
        <Typography
          component={"span"}
          variant="caption"
          fontSize={12}
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
      </Form>
    </FormArea>
  );
};

export default FormAreaSection;

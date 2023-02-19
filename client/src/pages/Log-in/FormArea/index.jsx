import Box from "@mui/material/Box";
import Button from "@mui/material/Button";
import Typography from "@mui/material/Typography";
import React, { useEffect } from "react";
import Divider from "@mui/material/Divider";
import TrendingFlatIcon from "@mui/icons-material/TrendingFlat";
import { Form, FormArea, InputGroup, Root } from "./style";
import { Link, useNavigate } from "react-router-dom";
import GoogleIcon from "../../../assets/google-g-2015.svg";
import { TextFields } from "../../../components";
import * as yup from "yup";
import { yupResolver } from "@hookform/resolvers/yup";
import { useForm } from "react-hook-form";
import { initialLogInValues } from "../../../utils";
import { loginInUserSchema } from "../../../validation";
import { useDispatch } from "react-redux";
import { login } from "../../../features/auth/authenticationSlice";
import { trim, normalizeEmail, escape, isEmail } from "validator";

const FormSection = () => {
  const dispatch = useDispatch();
  const navigate = useNavigate();
  const {
    handleSubmit,
    control,
    reset,
    formState: { errors, isValid, isSubmitSuccessful },
  } = useForm({
    defaultValues: initialLogInValues,
    resolver: yupResolver(loginInUserSchema),
  });
  const onSubmit = (data) => {
    isValid
      ? dispatch(
          login({
            usernameOrEmail: isEmail(data.usernameOrEmail)
              ? normalizeEmail(escape(data.usernameOrEmail))
              : trim(escape(data.usernameOrEmail)),
            password: trim(escape(data.password)),
          })
        ) & reset()
      : null;
  };
  useEffect(() => {
    isSubmitSuccessful ? navigate("/", { replace: true }) : null;
  }, [isSubmitSuccessful]);
  return (
    <FormArea>
      <Form
        component={"form"}
        onSubmit={handleSubmit(onSubmit)}
        noValidate
        autoComplete="off"
      >
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
          <TextFields
            label="Username or Email"
            placeholder="enter a username or email"
            type={"text"}
            control={control}
            name="usernameOrEmail"
            errors={errors}
          />
          <TextFields
            label="Password"
            placeholder="enter your password"
            type={"password"}
            control={control}
            name="password"
            errors={errors}
          />
        </InputGroup>
        <Button
          variant="contained"
          endIcon={<TrendingFlatIcon />}
          fullWidth
          disableElevation
          type="submit"
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

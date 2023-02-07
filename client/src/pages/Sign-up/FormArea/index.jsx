import React, { useEffect, useState } from "react";
import Box from "@mui/material/Box";
import Button from "@mui/material/Button";
import { yupResolver } from "@hookform/resolvers/yup";
import Typography from "@mui/material/Typography";
import { Link } from "react-router-dom";
import { useForm } from "react-hook-form";
import { Form, FormArea } from "./style";
import { useDispatch } from "react-redux";
import { signUpUser } from "../../../features/user/userSlice";
import { CheckBoxes, TextFields } from "../../../components";
import { signUpUserSchema } from "../../../validation";
import { initialSignUpValues } from "../../../utils";
const FormAreaSection = () => {
  const {
    handleSubmit,
    control,
    reset,
    formState: { errors, isValid },
  } = useForm({
    defaultValues: initialSignUpValues,
    resolver: yupResolver(signUpUserSchema),
  });

  const dispatch = useDispatch();
  const onSubmit = (data) => {
    isValid
      ? dispatch(
          signUpUser({
            username: data.username,
            email: data.email,
            password: data.password,
          })
        ) & reset()
      : null;
  };

  return (
    <FormArea>
      <Form
        component={"form"}
        onSubmit={handleSubmit(onSubmit)}
        noValidate
        autoComplete="off"
      >
        <Typography color={"#333333"} fontWeight={500} fontSize={32}>
          Welcome to BlogX Community
        </Typography>

        <TextFields
          label="Username"
          placeholder="enter your username"
          type={"text"}
          control={control}
          name="username"
          errors={errors}
        />
        <TextFields
          label="Email"
          placeholder="enter your email address"
          type={"email"}
          control={control}
          name="email"
          errors={errors}
        />
        <TextFields
          label="Password"
          placeholder="enter a password"
          type={"password"}
          control={control}
          name="password"
          errors={errors}
        />
        <TextFields
          label="Confirm Password"
          placeholder="re-enter password"
          type={"password"}
          control={control}
          name="confirmPassword"
          errors={errors}
        />
        <Typography fontWeight={400} fontSize={12} color={"#333333"} mt={2}>
          By creating an account, you agree to the
          <Link to={"/"}>
            <span style={{ textDecoration: "underline" }}>Terms of use</span>
          </Link>
          &nbsp; and &nbsp;
          <Link to={"/"}>
            <span style={{ textDecoration: "underline" }}>Privacy Policy</span>
          </Link>
        </Typography>
        <CheckBoxes
          label="I Agree to Terms and Privacy Policy"
          control={control}
          name="agreeTerms"
          errors={errors}
        />
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
          Already have an account?
          <Link to={"/log-in"}>
            <span style={{ textDecoration: "underline" }}>Log in</span>
          </Link>
        </Typography>
      </Form>
    </FormArea>
  );
};

export default FormAreaSection;

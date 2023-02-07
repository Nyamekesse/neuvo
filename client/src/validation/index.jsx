import * as yup from "yup";
import { passwdRegExp } from "../utils";
// creating new user schema for validation
export const signUpUserSchema = yup.object({
  username: yup.string().required("type in your username"),
  email: yup.string().required().email("kindly enter a valid email"),
  password: yup
    .string()
    .required("kindly enter a password")
    .matches(
      passwdRegExp,
      "must be 8 characters and above, One Uppercase, One lowerCase, One number and one Special case character"
    ),
  confirmPassword: yup
    .string()
    .oneOf([yup.ref("password"), null], "password must match"),
  agreeTerms: yup.bool().oneOf([true], "field must be checked"),
});

import * as yup from "yup";
import { passwdRegExp } from "../utils";
import validator from "validator";
// creating new user schema for validation
export const signUpUserSchema = yup.object({
  username: yup
    .string()
    .min(3, "username must be more than 3 characters")
    .required("type in your username"),
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

export const loginInUserSchema = yup.object({
  usernameOrEmail: yup
    .string()
    .test("is-email-or-username", "Invalid username or email", (value) => {
      return (
        yup.string().email().isValidSync(value) ||
        yup.string().min(3).isValidSync(value)
      );
    })
    .required("enter a username or an email address"),
  password: yup.string().required("kindly enter a password"),
});

const validatorSchema = {
  name: {
    in: ["body"],
    isString: true,
    trim: true,
    escape: true,
  },
  email: {
    in: ["body"],
    isEmail: true,
    normalizeEmail: true,
    trim: true,
    escape: true,
  },
  password: {
    in: ["body"],
    isString: true,
    trim: true,
    escape: true,
  },
};

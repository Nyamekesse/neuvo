export const passwdRegExp =
  /^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$/;

export const initialSignUpValues = {
  username: "",
  email: "",
  password: "",
  confirmPassword: "",
  agreeTerms: false,
};

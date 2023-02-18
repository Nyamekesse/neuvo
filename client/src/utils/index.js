import SecureLS from "secure-ls";
import jwt_decode from "jwt-decode";
export const passwdRegExp =
  /^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$/;

export const initialSignUpValues = {
  username: "",
  email: "",
  password: "",
  confirmPassword: "",
  agreeTerms: false,
};

export const initialLogInValues = {
  usernameOrEmail: "",
  password: "",
};

export const secureStore = new SecureLS({
  encodingType: "aes",
  isCompression: true,
});
export const secureStorageSetToken = (key, data) => {
  return data ? secureStore.set(key, data) : false;
};

export const secureStorageGetToken = (key) => {
  const data = secureStore.get(key);
  return data ? data : false;
};

export const secureStorageRemoveToken = (key) => {
  secureStore.remove(key);
};

export const decodeJWT = (token) => {
  return token ? jwt_decode(token) : null;
};

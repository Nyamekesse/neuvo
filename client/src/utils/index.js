import SecureLS from "secure-ls";

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

const secureStore = new SecureLS({ encodingType: "aes", isCompression: true });
export const localStorageSet = (key, data) => {
  return secureStore.set(key, data);
};

export const localStorageGet = (key) => {
  const data = secureStore.get(key);
  return data ? data : false;
};

export const localStorageRemove = (key) => {
  secureStore.remove(key);
};

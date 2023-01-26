import Box from "@mui/material/Box";
import { styled } from "@mui/material/styles";

export const FormArea = styled(Box)(({ theme }) => ({
  width: "60%",
  height: "100%",
  display: "flex",
  flexDirection: "column",
  padding: "3% 5%",
  backgroundColor: "#fff",
}));

export const Form = styled(Box)(({ theme }) => ({
  display: "flex",
  flexDirection: "column",
}));

export const InputSection = styled(Box)(({ theme }) => ({
  display: "flex",
  flexDirection: "column",
  marginTop: "2%",
}));

export const Validators = styled(Box)(({ theme }) => ({
  width: "100%",
  margin: "5px 0",
}));

export const Wrapper = styled("ul")(({ theme }) => ({
  display: "flex",
  flexWrap: "wrap",
  width: "100%",
  alignItems: "start",
  justifyContent: "start",
}));

export const Indicator = styled("li")(({ theme }) => ({
  margin: "2px 10px",
  width: "150px",
}));

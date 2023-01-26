import Box from "@mui/material/Box";
import { styled } from "@mui/material/styles";

export const FormArea = styled(Box)(({ theme }) => ({
  width: "50%",
  height: "100%",
  display: "flex",
  flexDirection: "column",
  padding: "2% 10% 5%",
  backgroundColor: "#fff",
}));
export const Form = styled(Box)(({ theme }) => ({
  display: "flex",
  flexDirection: "column",
  alignItems: "center",
}));

export const Root = styled("div")(({ theme }) => ({
  width: "100%",
  margin: "10% auto",
}));

export const InputGroup = styled(Box)(({ theme }) => ({
  display: "flex",
  flexDirection: "column",
  width: "100%",
}));
export const InputSection = styled(Box)(({ theme }) => ({
  display: "flex",
  flexDirection: "column",
}));

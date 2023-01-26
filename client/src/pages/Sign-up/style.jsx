import { styled } from "@mui/material";
import { Box } from "@mui/system";

export const Wrap = styled(Box)(({ theme }) => ({
  width: "100vw",
  height: "100vh",
  backgroundColor: "#c5c5c5",
}));

export const Container = styled(Box)(({ theme }) => ({
  display: "flex",
  flexDirection: "row",
  alignItems: "flex-start",
  position: "absolute",
  top: "50%",
  left: "50%",
  transform: "translate(-50%, -50%)",
  width: "90%",
  height: "90%",
}));

export const Showcase = styled(Box)(({ theme }) => ({
  width: "40%",
  display: "flex",
  flexDirection: "column",
  padding: "8% 5% 3%",
  height: "100%",
  backgroundColor: "#E5E5E5",
  alignItems: "center",
  justifyContent: "center",
}));

export const FormArea = styled(Box)(({ theme }) => ({
  width: "60%",
  height: "100%",
  display: "flex",
  flexDirection: "column",
  padding: "3% 5%",
  backgroundColor: "#fff",
}));

export const Image = styled(Box)(({ theme }) => ({
  width: "100%",
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

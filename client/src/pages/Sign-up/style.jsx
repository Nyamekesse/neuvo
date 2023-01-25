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
  backgroundColor: "pink",
  //   backgroundColor: "#E5E5E5",
}));

export const FormArea = styled(Box)(({ theme }) => ({
  width: "60%",
  height: "100%",
  display: "flex",
  flexDirection: "column",
  padding: "5% 5%",
  backgroundColor: "#fff",
}));

export const Image = styled(Box)(({ theme }) => ({
  width: "350px",
  justifySelf: "baseline",
  margin: "20% auto 0",
}));

export const Form = styled(Box)(({ theme }) => ({
  display: "flex",
  flexDirection: "column",
}));

export const Logo = styled(Box)(({ theme }) => ({
  width: "150px",
  margin: "0 auto",
}));

export const InputSection = styled(Box)(({ theme }) => ({
  display: "flex",
  flexDirection: "column",
  marginTop: "2%",
}));

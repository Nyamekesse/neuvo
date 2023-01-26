import { styled } from "@mui/material/styles";
import Box from "@mui/material/Box";

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

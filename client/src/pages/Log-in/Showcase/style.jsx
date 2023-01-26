import Box from "@mui/material/Box";
import { styled } from "@mui/material/styles";

export const Showcase = styled(Box)(({ theme }) => ({
  width: "50%",
  display: "flex",
  flexDirection: "column",
  padding: "8% 5% 3%",
  height: "100%",
  backgroundColor: "#E5E5E5",
}));

export const Image = styled(Box)(({ theme }) => ({
  width: "350px",
  justifySelf: "baseline",
  margin: "20% auto 0",
}));

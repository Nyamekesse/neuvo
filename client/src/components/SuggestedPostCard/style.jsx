import { Box, styled } from "@mui/material";

export const Wrap = styled(Box)(({ theme }) => ({
  height: "auto",
  width: "280px",
  display: "flex",
  flexDirection: "column",
}));

export const Image = styled(Box)(({ theme }) => ({
  width: "100%",
  height: "150px",
}));

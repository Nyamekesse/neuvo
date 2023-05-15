import { Box, styled } from "@mui/material";

export const Wrap = styled(Box)(() => ({
  display: "flex",
  flexDirection: "column",
  alignItems: "center",
  justifyContent: "center",
  padding: "1% 0",
  width: "100%",
  backgroundColor: "#fafafa",
  marginTop: "1%",
}));

export const Socials = styled(Box)(() => ({
  display: "flex",
  flexDirection: "row",
}));

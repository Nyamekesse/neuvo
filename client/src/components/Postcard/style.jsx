import { Box, styled } from "@mui/material";

export const Wrap = styled(Box)(({ theme }) => ({
  display: "flex",
  flexDirection: "row",
  width: "100%",
  height: "250px",
  alignItems: "flex-start",
  justifyContent: "space-between",
  marginBottom: "3%",
}));

export const PostImage = styled(Box)(({ theme }) => ({
  width: "45%",
  height: "100%",
  backgroundPosition: "center",
  backgroundRepeat: "no-repeat",
}));

export const PostDetails = styled(Box)(({ theme }) => ({
  width: "52%",
  height: "100%",
  padding: "0.5% 0",
}));

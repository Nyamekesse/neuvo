import { Box, styled } from "@mui/material";

export const Wrap = styled(Box)(({ theme }) => ({
  width: "100%",
  display: "flex",
  flexDirection: "column",
  alignItems: "center",
}));

export const Post = styled(Box)(({ theme }) => ({
  width: "100%",
  display: "flex",
  flexDirection: "column",
  alignItems: "center",
}));

export const Image = styled(Box)(({ theme }) => ({
  width: "100%",
  height: "280px",
}));

export const CommentSection = styled(Box)(({ theme }) => ({
  width: "100%",
  margin: "2% 0",
}));

export const Comments = styled(Box)(({ theme }) => ({
  display: "flex",
  flexDirection: "column",
  width: "100%",
  height: "414px",
  backgroundColor: "yellow",
  margin: "5% 0 2%",
  overflowY: "auto",
}));

import { Box, styled } from "@mui/material";
import { height, width } from "@mui/system";

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
  margin: "5% 0 2%",
  overflowY: "auto",
  padding: "3% 1.5%",
  boxShadow: "0px 2px 2px rgba(142, 142, 142, 0.25)",
}));

export const CommentCard = styled(Box)(({ theme }) => ({
  display: "flex",
  flexDirection: "row",
  alignItems: "flex-start",
  marginBottom: "20px",
}));

export const CommentText = styled(Box)(({ theme }) => ({
  width: "auto",
  maxHeight: "150px",
  padding: "1% 2%",
  backgroundColor: "#EEEEEE;",
  borderRadius: "4px",
}));

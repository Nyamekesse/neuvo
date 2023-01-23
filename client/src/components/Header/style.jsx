import { styled } from "@mui/material/styles";
import Box from "@mui/material/Box";

export const Container = styled(Box)(({ theme }) => ({
  width: "100%",
  padding: "2%",
  display: "flex",
  flexDirection: "row",
  alignItems: "center",
  backgroundColor: "gray",
}));

export const Title = styled(Box)(({ theme }) => ({
  width: "100%",
}));

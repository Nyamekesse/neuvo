import React from "react";
import { MainEditor } from "../../components";
import { Box, Grid } from "@mui/material";

const ComposePostPage = () => {
  return (
    <Grid container columnSpacing={2} direction={{ xs: "column", md: "row" }}>
      <Grid item sx={{ flexGrow: 1 }}>
        <MainEditor />
      </Grid>
      <Grid item>
        <Box>hello</Box>
      </Grid>
    </Grid>
  );
};
export default ComposePostPage;

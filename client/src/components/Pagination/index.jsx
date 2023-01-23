import React from "react";
import Pagination from "@mui/material/Pagination";
import Stack from "@mui/material/Stack";

const CustomPagination = () => {
  return (
    <Stack spacing={2} mt={1} mb={1}>
      <Pagination count={10} variant="outlined" />
    </Stack>
  );
};

export default CustomPagination;

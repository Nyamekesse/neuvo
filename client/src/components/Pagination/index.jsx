import React, { useEffect } from "react";
import Pagination from "@mui/material/Pagination";
import Stack from "@mui/material/Stack";
import { PaginationItem } from "@mui/material";
import { Link } from "react-router-dom";
import { useDispatch, useSelector } from "react-redux";
import { getAllPosts } from "../../features/post/postSlice";

const CustomPagination = ({ page, numberOfPages }) => {
  const dispatch = useDispatch();

  useEffect(() => {
    dispatch(getAllPosts(page));
  }, [page]);
  return (
    <Stack spacing={2} mt={1} mb={1}>
      <Pagination
        count={numberOfPages}
        variant="outlined"
        page={Number(page) || 1}
        renderItem={(item) => (
          <PaginationItem
            {...item}
            component={Link}
            to={`/posts?page=${item.page}`}
          />
        )}
      />
    </Stack>
  );
};

export default CustomPagination;

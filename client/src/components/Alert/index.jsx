import React from "react";
import Alert from "@mui/material/Alert";
import Stack from "@mui/material/Stack";
import { useDispatch, useSelector } from "react-redux";
import { removeAlert } from "../../features/alerts/alertSlice";

const CustomAlert = () => {
  const displayAlert = useSelector((store) => store.alert);
  const dispatch = useDispatch();
  setTimeout(() => {
    dispatch(removeAlert());
  }, 10000);
  return (
    <Stack
      sx={{
        width: "30%",
        display: displayAlert.show ? "inline-block" : "none",
        position: "fixed",
        bottom: "10%",
        right: "5%",
      }}
      spacing={2}
    >
      <Alert
        severity={displayAlert.severity}
        onClose={() => {
          dispatch(removeAlert());
        }}
      >
        {displayAlert.text}
      </Alert>
    </Stack>
  );
};

export default CustomAlert;

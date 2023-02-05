import { createSlice } from "@reduxjs/toolkit";
import { SUCCESS } from "../../constants";

const initialState = {
  show: false,
  text: "",
  severity: SUCCESS,
};

const alertSlice = createSlice({
  name: "alert",
  initialState: initialState,
  reducers: {
    displayAlert: (state, { payload }) => {
      state.show = true;
      state.text = payload.text;
      state.severity = payload.severity;
    },
    removeAlert: (state) => {
      state.show = false;
      state.text = "";
      state.severity = SUCCESS;
    },
  },
});

export const { displayAlert, removeAlert } = alertSlice.actions;
export default alertSlice.reducer;

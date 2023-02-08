import React from "react";
import Checkbox from "@mui/material/Checkbox";
import { FormControlLabel, Typography } from "@mui/material";
import { Controller } from "react-hook-form";
const CheckBoxes = ({ label, name, control, errors }) => {
  return (
    <>
      <Controller
        name={name}
        control={control}
        render={({ field }) => (
          <FormControlLabel
            {...field}
            control={<Checkbox required />}
            label={label}
          />
        )}
      />
      {errors[name] ? (
        <Typography
          component={"span"}
          fontSize={"11px"}
          fontWeight={800}
          color={"error"}
        >
          {errors[name].message}
        </Typography>
      ) : null}
    </>
  );
};

export default CheckBoxes;

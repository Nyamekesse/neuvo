import { TextField, Typography } from "@mui/material";
import React from "react";
import { InputSection } from "./style";
import { Controller } from "react-hook-form";

const TextFields = ({ label, placeholder, type, name, control, errors }) => {
  return (
    <InputSection>
      <Typography
        color={"#50565F"}
        fontWeight={400}
        fontSize={14}
        component={"p"}
        variant="body1"
        mb={1}
      >
        {label}
      </Typography>
      <Controller
        name={name}
        control={control}
        render={({ field }) => (
          <TextField
            {...field}
            placeholder={placeholder}
            fullWidth
            required
            type={type}
            size="small"
            sx={{
              backgroundColor: "#fff",
              borderColor: errors[name] ? "red" : "",
            }}
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
    </InputSection>
  );
};

export default TextFields;

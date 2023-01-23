import { createTheme } from "@mui/material/styles";

const theme = createTheme({
  breakpoints: {
    values: {
      mobile_0: 0, //
      mobile_240: 240,
      mobile_320: 320,
      mobile_360: 360,
      mobile_375: 375,
      mobile_384: 384,
      mobile_393: 393,
      mobile_400: 400,
      mobile_450: 450,
      mobile_550: 550,
      tablet_600: 600, //
      tablet_650: 650,
      tablet_688: 688,
      tablet_769: 768,
      tablet_800: 800,
      tablet_834: 834,
      tablet_840: 840,
      laptop_1024: 1024, //
      laptop_1152: 1152,
      laptop_1280: 1280,
      desktop_1440: 1440, //
    },
  },

  components: {
    MuiIconButton: {
      styleOverrides: {
        root: {
          backgroundColor: "transparent",
          borderRadius: "50%",
          color: "#000",
        },
      },
    },
    MuiTextField: {
      styleOverrides: {
        root: {
          backgroundColor: "#F5F5F5",
          border: "1px solid #CED4DA",
          borderRadius: "4px",
          "& .MuiOutlinedInput-root .MuiOutlinedInput-notchedOutline": {
            border: "none",
          },
        },
      },
    },
    MuiButton: {
      styleOverrides: {
        contained: {
          backgroundColor: "#555555",
          textTransform: "capitalize",
          ":hover, :focus": {
            backgroundColor: "#555555",
          },
        },
      },
    },
  },
});

export default theme;

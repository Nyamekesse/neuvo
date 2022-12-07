import "./App.css";
import Typography from "@mui/material/Typography";
import Box from "@mui/material/Box";
import Button from "@mui/material/Button";
import { useEffect, useState } from "react";
import { fetchMessage } from "./services/api";
import axios from "axios";
function App() {
  const [message, setMessage] = useState("");
  const sender = async () => {
    try {
      const res = await fetchMessage();
      const data = await res.data;
      if (res.status === 200 && res.statusText === "OK") {
        setMessage(data.msg);
      }
    } catch (error) {
      console.log(error.message);
    }
  };
  useEffect(() => {
    sender();
  }, []);
  return (
    <Box>
      <Typography variant="h6">{message}</Typography>
      <Button variant="outlined">Click to make a request</Button>
    </Box>
  );
}

export default App;

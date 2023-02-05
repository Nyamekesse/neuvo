import { useLocation } from "react-router-dom";
import "./App.css";
import { Footer, Header } from "./components";
import Views from "./views/Views";
import Box from "@mui/material/Box";
import { styled } from "@mui/material/styles";
import CustomAlert from "./components/Alert";
const AppContainer = styled(Box)({
  display: "flex",
  flexDirection: "column",
  alignItems: "center",
  margin: "0 auto",
  padding: "0 15%",
  position: "relative",
});

function App() {
  let currentUrl = useLocation();
  const exceptPath = ["/log-in", "/sign-up", "/page-not-found"];
  return (
    <>
      {!exceptPath.includes(currentUrl.pathname) && <Header />}
      <AppContainer>
        <Views />
        <CustomAlert />
      </AppContainer>

      {!exceptPath.includes(currentUrl.pathname) && <Footer />}
    </>
  );
}

export default App;

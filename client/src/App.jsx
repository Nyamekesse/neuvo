import { useLocation } from "react-router-dom";
import "./App.css";
import { Footer, Header } from "./components";
import Views from "./views/Views";

function App() {
  let currentUrl = useLocation();
  const exceptPath = ["/log-in", "/sign-up", "/page-not-found"];
  return (
    <>
      {!exceptPath.includes(currentUrl.pathname) && <Header />}
      <Views />
      {!exceptPath.includes(currentUrl.pathname) && <Footer />}
    </>
  );
}

export default App;

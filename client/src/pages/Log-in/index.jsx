import React from "react";
import { Container, Wrap } from "./style";
import ShowcaseSection from "./Showcase";
import FormSection from "./FormArea";
const LogIn = () => {
  return (
    <Wrap>
      <Container>
        <ShowcaseSection />
        <FormSection />
      </Container>
    </Wrap>
  );
};

export default LogIn;

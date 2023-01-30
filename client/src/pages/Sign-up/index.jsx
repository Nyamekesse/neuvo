import React from "react";
import { Container, Image, Showcase, Wrap } from "./style";
import Display from "../../assets/content_creator_re_pt5b.svg";
import FormAreaSection from "./FormArea";

const SignUp = () => {
  return (
    <Wrap>
      <Container>
        <FormAreaSection />
        <Showcase>
          <Image>
            <img src={Display} alt={Display} />
          </Image>
        </Showcase>
      </Container>
    </Wrap>
  );
};

export default SignUp;

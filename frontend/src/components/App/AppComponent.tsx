import React from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import styled from 'styled-components';

import Closed from '../Closed';

function App() {
  return (
    <BrowserRouter>
      <Switch>
        <Route path="/the-coco-cabana">
          <Closed />
        </Route>
        <Route path="*">
          <FullScreenContainer>
            <Logo>The<br />Clubhouse</Logo>
          </FullScreenContainer>
        </Route>
      </Switch>
    </BrowserRouter>
  );
}

const FullScreenContainer = styled.div`
  background-color: rgb(3, 3, 3);
  background-image: url("https://the-clubhouse.s3.amazonaws.com/the-clubhouse.jpg");
  height: 100vh;
  width: 100vw;

  @media (max-width: 826px) {
    align-items: center;
    display: flex;
    justify-content: center;
  }
`;

const Logo = styled.div`
  color: #f9f9f9;
  font-family: Monoton;
  font-size: 95px;
  line-height: 100px;
  padding-left: 90px;
  padding-top: 90px;

  @media (max-width: 826px) {
    font-size: 43px;
    line-height: 45px;
    padding-left: 0;
    padding-top: 0;
  }
`;

export default App;
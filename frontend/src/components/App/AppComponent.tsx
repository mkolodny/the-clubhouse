import React from 'react';
import styled from 'styled-components';


function App() {
  return (
    <FullScreenContainer>
      <Logo>The<br />Clubhouse</Logo>
    </FullScreenContainer>
  );
}

const FullScreenContainer = styled.div`
  background-image: url("https://the-clubhouse.s3.amazonaws.com/the-clubhouse.jpg");
  height: 100vh;
  width: 100vw;
`;

const Logo = styled.div`
  color: #f9f9f9;
  font-family: Monoton, cursive;
  font-size: 95px;
  line-height: 100px;
  padding-left: 90px;
  padding-top: 90px;
`;

export default App;
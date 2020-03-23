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
  align-items: center;
  display: flex;
  height: 100vh;
  justify-content: center;
  width: 100vw;
`;

const Logo = styled.span`
  font-family: 'Patrick Hand SC', cursive;
  font-size: 115px;
  line-height: 85px;
  text-align: center;
`;

export default App;
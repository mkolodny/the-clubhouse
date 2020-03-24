import React from 'react';
import styled from 'styled-components';


function Closed() {
  return (
    <FullScreenContainer>
      <Padding>
        <Logo>The<br />Clubhouse</Logo>
        <ClubhouseContainer>
          <ClubhouseName>The Coco Cabana</ClubhouseName>
          <HoursHeader>Open Hours:</HoursHeader>
          <ClubhouseHours>6:30pm - 7:30pm Pacific Time, every day</ClubhouseHours>
          <ClubhouseDescription>The Coco Cabana is an online clubhouse for you and your friends to hangout in while sheltering from the Coronavirus<br />♪┏(・o・)┛♪┗ ( ・o・) ┓♪</ClubhouseDescription>
        </ClubhouseContainer>
      </Padding>
    </FullScreenContainer>
  );
}

const ClubhouseContainer = styled.div`
  background-color: rgba(0, 0, 0, 0.8);
  border-radius: 6px;
  margin-top: 70px;
  padding-bottom: 70px;
  padding-left: 70px;
  padding-right: 70px;
  padding-top: 40px;
  text-align: center;
`;

const ClubhouseDescription = styled.div`
  font-size: 30px;
  margin-bottom: 0;
  margin-top: 70px;
  margin-left: auto;
  margin-right: auto;
  max-width: 800px;
  line-height: 42px;
  text-align: center;
`;

const ClubhouseHours = styled.p`
  font-size: 40px;
  margin-bottom: 0;
  margin-top: 20px;
`;

const ClubhouseName = styled.h1`
  font-size: 90px;
  line-height: 90px;
  margin-bottom: 0;
  margin-top: 0;
`;

const HoursHeader = styled.h2`
  font-size: 40px;
  margin-bottom: 0;
  margin-top: 70px;
`;

const FullScreenContainer = styled.div`
  background-image: url("https://the-clubhouse.s3.amazonaws.com/the-clubhouse.jpg");
  color: #f9f9f9;
  min-height: 100vh;
  width: 100vw;
`;

const Logo = styled.div`
  font-family: Monoton, cursive;
  font-size: 70px;
  line-height: 70px;
`;

const Padding = styled.div`
  padding: 90px;
`;

export default Closed;
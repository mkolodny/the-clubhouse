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
          <ClubhouseDescription>The Coco Cabana is a video chat clubhouse for you and your friends to hangout in while you shelter from the Coronavirus<br />♪┏(・o・)┛♪<DancersBreak />┗ ( ・o・) ┓♪</ClubhouseDescription>
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
  padding-top: 55px;
  text-align: center;

  @media (max-width: 826px) {
    margin-top: 40px;
    padding-bottom: 40px;
    padding-left: 20px;
    padding-right: 20px;
    padding-top: 40px;
  }
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

  @media (max-width: 826px) {
    font-size: 25px;
    line-height: 30px;
    margin-top: 60px;
  }
`;

const ClubhouseHours = styled.p`
  font-size: 40px;
  margin-bottom: 0;
  margin-top: 20px;

  @media (max-width: 826px) {
    font-size: 32px;
    line-height: 35px;
  }
`;

const ClubhouseName = styled.h1`
  font-size: 90px;
  line-height: 90px;
  margin-bottom: 0;
  margin-top: 0;

  @media (max-width: 826px) {
    font-size: 50px;
    line-height: 50px;
  }
`;

const DancersBreak = styled.br`
  display: none;

  @media (max-width: 826px) {
    display: block;
  }
`;

const FullScreenContainer = styled.div`
  background-color: rgb(3, 3, 3);
  background-image: url("https://the-clubhouse.s3.amazonaws.com/the-clubhouse.jpg");
  color: #f9f9f9;
  min-height: 100vh;
  width: 100vw;
`;

const HoursHeader = styled.h2`
  font-size: 40px;
  margin-bottom: 0;
  margin-top: 70px;

  @media (max-width: 826px) {
    font-size: 32px;
    line-height: 35px;
  }
`;

const Logo = styled.div`
  font-family: Monoton, cursive;
  font-size: 70px;
  line-height: 70px;

  @media (max-width: 826px) {
    line-height: 42px;
    font-size: 42px;
    padding-top: 20px;
  }
`;

const Padding = styled.div`
  padding: 90px;

  @media (max-width: 826px) {
    padding: 15px;
  }
`;

export default Closed;
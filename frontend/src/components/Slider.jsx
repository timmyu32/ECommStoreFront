import styled from 'styled-components';
import { BiLeftArrowAlt, BiRightArrowAlt } from "react-icons/bi";
import React, { useState, setState, useEffect } from 'react';
import { sliderItem } from '../data'
import axios from "axios";


const Container = styled.div`
    width: 100%;
    height: 100vh;
    display: flex;
    position: relative;
    overflow: hidden;
`;

const Arrow = styled.div`
    width: 50px;
    height: 50px;
    background-color: #fff7f7;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    position: absolute;
    top: 0;
    bottom: 0;
    left: ${props => props.direction === "left" && "10px"};
    right: ${props => props.direction === "right" && "10px"};
    margin: auto;
    cursor: pointer;
    opacity: 0.5;
    z-index: 2;
`;

const Wrapper = styled.div`
    height: 100%;
    display: flex;
    transition: all 1.5s ease;
    transform: translateX(${props => props.slideIndex * -99}vw);
`;
 

const Slide = styled.div`
    width: 99vw;
    height: 100vh;
    display: flex;
    align-items: center;
    background-color: #${props => props.bg};
`;

const ImageContainer = styled.div`
    flex: 1;
    height: 100%;

`;

const Image = styled.img`
    height: 80%;

`;

const InfoContainer = styled.div`
    flex:1
    padding: 50px;
`;

const Title = styled.h1`
    font-size: 70px;
`;
const Description = styled.p`
    margin: 30px 0px;
    font-size: 20px;
    font-weight: 500;
    letter-spacing: 3px;
`;
const Button = styled.button`
    padding: 10px;
    font-size: 20px;
    background-color: transparent;
    cursor: pointer;
    transition: all 0.7s ease;

    &:hover{
        background-color: black;
        color: white;
    }

`;



const Slider = () => {
    const [slideIndex, setSlideIndex] = useState(0); 
    const handleClick = (direction) => {

        if (direction == "left"){
            setSlideIndex(slideIndex > 0 ? slideIndex-1 : 2);
        } else {
            setSlideIndex(slideIndex < 2 ? slideIndex+1 : 0);
        }

    };

    const [data, setData] = useState([]);

    useEffect(() =>{
        getSliderData();
    }, []);

    const getSliderData = async () => {
        await axios.get("http://127.0.0.1:8000/api/slider/3").then(res => {
        setData(res.data.sliderData);
        }).catch(err => console.log(err));
        
}


  return (
    <Container>
        <Arrow direction="left" onClick={()=>handleClick("left")}>
            <BiLeftArrowAlt/>
        </Arrow>
        <Wrapper slideIndex={slideIndex}>
            {data.map(item => (
                <Slide bg={item.bg}>
                <ImageContainer>
                    <Image src={item.img}/>
                </ImageContainer>
                <InfoContainer>
                    <Title>{item.title}</Title>
                    <Description>{item.desc}</Description>
                    <Button>SHOP NOW</Button>
                </InfoContainer>
            </Slide>

            ))}
        </Wrapper>

        <Arrow direction="right" onClick={()=>handleClick("right")}>
            <BiRightArrowAlt/>
        </Arrow>
    </Container>
  )
}

export default Slider

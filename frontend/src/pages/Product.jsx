import React from 'react'
import styled from 'styled-components';
import Navbar from '../components/Navbar';
import Announcement from '../components/Announcement';
import Newsletter from '../components/Newsletter';
import Footer from '../components/Footer';
import { IoAddCircleSharp, IoRemoveCircleSharp } from 'react-icons/io5';


const Container = styled.div`

`;

const Wrapper = styled.div`
    padding: 50px;
    display: flex;
`;
const ImgContainer = styled.div`
    flex: 1;
`;
const Image = styled.img`
    width: 90%;
    height: 90vh;
    object-fit: cover;
`;
const InfoContainer = styled.div`
    flex: 1;
    padding: 0px 50px;

`;
const Title = styled.h1`
    font-weight: 200;
`;
const Desc = styled.p`
    margin: 20px 0px;
`;
const Price = styled.span`
    font-weight: 100;
    font-size: 40px;
`;

const FilterContainer = styled.div`
    display: flex;
    justify-content: space-between;
    width: 50%;
    margin: 30px 0px;
`;

const Filter = styled.div`
    display: flex;
    align-items: center;   
`;

const FilterTitle = styled.span`
    font-size: 20px;
    font-weight: 200;
`;

const FilterSize = styled.select`
    padding: 5px`;

const FilterSizeOption = styled.option``;

const AddContainer = styled.div`
    display: flex;
    width: 50%;
    align-items: center;
    justify-content: space-between;

`;
const AmountContainer = styled.div`
    display: flex;
    align-items: center;
    font-weight: 700;

`;
const Amount = styled.span`
    width: 30px;
    height: 30px;
    display: flex;
    border-radius: 10px;
    border: 1px solid gray;
    align-items: center;
    justify-content: center;
    margin: 0px 5px;
`;
const Button = styled.button`
    padding: 15px;
    border: 2px solid gray;
    background-color: white;
    transition: all 0.5s ease;
    cursor: pointer;
    font-weight: 600;
    
    &:hover{
        background-color: teal;
        color: white;
    }
`;



const Product = () => {
  return (
    <Container>
        <Navbar/>
        <Announcement/>
        <Wrapper>
            <ImgContainer>
                <Image src="https://n.nordstrommedia.com/id/sr3/80eb5b5a-efaa-4c5c-bfb3-912915f9e232.jpeg"/>
            </ImgContainer>
            <InfoContainer>
                <Title>Classic Dress Shirt</Title>
                <Desc>Lorem ipsum dolor sit amet consectetur adipisicing elit. Ut, fugit cum possimus consequatur dignissimos laboriosam. Autem fugit totam ipsam deserunt possimus dolorem nemo, voluptatibus aspernatur sunt excepturi quaerat! Ipsam, nulla!</Desc>
                <Price>$50</Price>
            
                <FilterContainer>
                    <Filter>
                        <FilterTitle>Size</FilterTitle>
                        <FilterSize>
                            <FilterSizeOption>XS</FilterSizeOption>
                            <FilterSizeOption>S</FilterSizeOption>
                            <FilterSizeOption>M</FilterSizeOption>
                            <FilterSizeOption>L</FilterSizeOption>
                            <FilterSizeOption>XL</FilterSizeOption>
                        </FilterSize>
                    </Filter>
                </FilterContainer>
                <AddContainer>
                    <AmountContainer>
                        <IoRemoveCircleSharp color='teal'/>
                        <Amount>1</Amount>
                        <IoAddCircleSharp color='teal'/>
                    </AmountContainer>
                    <Button>ADD TO CART</Button>
                </AddContainer>
            </InfoContainer>

        </Wrapper>
        <Newsletter/>
        <Footer/>
      
    </Container>
  )
}

export default Product

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
    padding: 20px;
`;

const Title = styled.h1`
    font-weight: 300;
    text-align: center;
`;
const Top = styled.div`
    display: flex;
    justify-content: space-between;
    align-items: center;
`;

const TopButton = styled.button`
    padding: 10px;
    font-weight: 600;
    cursor: pointer;
    background-color: black;
    transition: all 0.5s ease;
    font-weight: 600;
    color: white;


    &:hover{
        background-color: white;
        color: black;
    }
`;

const Bottom = styled.div`
    display: flex;
    justify-content: space-between;

`;
const Info = styled.div`
    flex: 3;
`;
const Summary = styled.div`
    flex: 1;
    border: 0.5px solid lightgray;
    border-radius: 10px;
    padding: 20px;
    background-color: #eee;
    height: 50vh;
`;

const Product = styled.div`
    display: flex;
    justify-content: space-between;
`;
const ProductDetails = styled.div`
    flex: 2;
    display: flex;
`;

const PriceDetails = styled.div`
    flex: 1;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
`;

const ProductAmountContainer =styled.div`
    display: flex;
    align-items: center;
    margin-bottom: 20px;
`;

const Amount =styled.div`
    font-size: 24px;
    margin: 5px;

`;

const ProductPrice =styled.div`
    font-size: 30px;
    font-weight: 200;

`;



const Image = styled.img`    
    width: 200px;
   
`;

const Details = styled.div`
    padding: 20px;
    display: flex;
    flex-direction: column;    
    justify-content: space-around;
`;

const Hr = styled.hr`
    background-color: #eee;
    border: none;
    height: 2px;
`;

const SummaryTitle = styled.h1`
    font-weight: 200;
`;
const SummaryItem = styled.div`
    margin: 20px 0px;
    display: flex;
    justify-content: space-between;
    font-weight: ${props => props.type === 'total' && '500'};
    font-size: ${props => props.type === 'total' && '24px'};

`;
const SummaryItemText = styled.span``;
const SummaryItemPrice = styled.span``;
const Button = styled.button`
    width: 100%;
    padding: 10px;
    background-color: white;
    transition: all 0.5s ease;
    cursor: pointer;
    font-weight: 600;

    &:hover{
        background-color: black;
        color: white;
    }
`;


const ProductName = styled.span``;

const ProductID = styled.span``;

const ProductSize = styled.span``;


const Cart = () => {
  return (
    <Container>
        <Navbar/>
        <Announcement/>
        <Wrapper>
            <Title>YOUR CART</Title>
            <Top>
                <TopButton>CONTINUE SHOPPING</TopButton>
                <TopButton>PROCEED TO CHECK-OUT</TopButton>
            </Top>
            <Bottom>
                <Info>
                    <Product>
                        <ProductDetails>
                            <Image src="https://n.nordstrommedia.com/id/sr3/80eb5b5a-efaa-4c5c-bfb3-912915f9e232.jpeg"/>
                            <Details>
                                <ProductName><b>Item: </b>Classic Dress Shirt</ProductName>
                                <ProductID><b>ID: </b>5719248306</ProductID>
                                <ProductSize><b>Size: </b>L</ProductSize>
                            </Details>
                        </ProductDetails>
                        <PriceDetails>
                            <ProductAmountContainer>
                                <IoRemoveCircleSharp color='teal'/>
                                <Amount>2</Amount>
                                <IoAddCircleSharp color='teal'/>
                            </ProductAmountContainer>
                            <ProductPrice>$30</ProductPrice>

                        </PriceDetails>
                    </Product>
                    <Hr />
                    <Product>
                        <ProductDetails>
                            <Image src="https://n.nordstrommedia.com/id/sr3/ee8a895a-a597-48a9-af42-437071b92236.jpeg"/>
                            <Details>
                                <ProductName><b>Item: </b>Classic Dress Shirt</ProductName>
                                <ProductID><b>ID: </b>7811296806</ProductID>
                                <ProductSize><b>Size: </b>L</ProductSize>
                            </Details>
                        </ProductDetails>
                        <PriceDetails>
                            <ProductAmountContainer>
                                <IoRemoveCircleSharp color='teal'/>
                                <Amount>1</Amount>
                                <IoAddCircleSharp color='teal'/>
                            </ProductAmountContainer>
                            <ProductPrice>$30</ProductPrice>

                        </PriceDetails>
                    </Product>
                </Info>
                <Summary>
                    <SummaryTitle>ORDER SUMMARY</SummaryTitle>
                    <SummaryItem>
                        <SummaryItemText>Subtotal</SummaryItemText>
                        <SummaryItemPrice>$60</SummaryItemPrice>
                    </SummaryItem>
                    <SummaryItem>
                        <SummaryItemText>Shipping</SummaryItemText>
                        <SummaryItemPrice>$4.65</SummaryItemPrice>
                    </SummaryItem>
                    <SummaryItem>
                        <SummaryItemText>Shipping Discount</SummaryItemText>
                        <SummaryItemPrice>-$4.65</SummaryItemPrice>
                    </SummaryItem>
                    <SummaryItem type="total">
                        <SummaryItemText>Total</SummaryItemText>
                        <SummaryItemPrice>$60</SummaryItemPrice>
                    </SummaryItem>
                    <Button>PROCEED TO CHECK-OUT</Button>
                </Summary>
            </Bottom>
        
        
        </Wrapper>


        <Footer/>
    </Container>
  )
}

export default Cart

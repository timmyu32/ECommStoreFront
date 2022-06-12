import React from 'react'
import styled from 'styled-components';
import Navbar from '../components/Navbar';
import Announcement from '../components/Announcement';
import Products from '../components/Products';
import Newsletter from '../components/Newsletter';
import Footer from '../components/Footer';


const Container = styled.div`

`;

const Container2 = styled.div`
    display: flex;
`;

const FilterContainer = styled.div`
    display: flex;
    justify-content: space-between;
`;

const Title = styled.h1`
    margin: 20px;
`;

const Filter = styled.div`
    margin-right: 20px;
`;

const FilterText = styled.span`
    font-size: 20px;
    font-weight: 600;
`;

const Select = styled.select`
    padding: 10px;
    margin-right: 10px;
`;

const Option = styled.option`

`;


const ProductList = () => {
  return (
    <Container>
        <Navbar/>
        <Announcement/>
        <Title>Dress Shirts</Title>
        <FilterContainer>
            <Container2>
            <Filter><FilterText>Filter Products</FilterText></Filter>
            <Select>
                <Option disabled selected>
                    Color
                </Option>
                <Option>White</Option>
                <Option>Black</Option>
                <Option>Blue</Option>
                <Option>Yellow</Option>
                <Option>Green</Option>
            </Select>
            <Select>
                <Option disabled selected>
                    Size
                </Option>
                <Option>XS</Option>
                <Option>S</Option>
                <Option>M</Option>
                <Option>L</Option>
                <Option>XL</Option>
            </Select>
            </Container2>
            <Container2>
                <Filter><FilterText>Sort Products</FilterText></Filter>
                <Select>
                    <Option selected>
                        Newest
                    </Option>
                    <Option>Price (asc)</Option>
                    <Option>Price (decc)</Option>
                </Select>
            </Container2>
        </FilterContainer>  
        <Products limit={0}/>
        <Newsletter/>
        <Footer/>

      
    </Container>
  )
}

export default ProductList
